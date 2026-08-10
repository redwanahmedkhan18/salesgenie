"""
Unified LLM Execution Engine & Provider Fallback Cascade
Executes LLM inference using Groq, Google, and Mistral AI with automatic failover.

Observability:
- Structured JSON logging with request_id, user_id, tenant_id, trace_id
- Latency metrics logged per provider attempt
- All sensitive data (API keys) redacted from logs
- Per-provider timeout and retry with exponential backoff

See observability.md Section 14 (LLM Monitoring) and Section 5.3 (Logs).
"""

import asyncio
import os
import time
import uuid
from collections import deque
from enum import Enum
from typing import Any, Dict, List, Optional

import httpx

from enterprise_ai_platform.common.cost_management import (
    TaskComplexity,
    cost_calculator,
    llm_response_cache,
)
from enterprise_ai_platform.common.logging import get_structured_logger
from enterprise_ai_platform.common.metrics import get_metrics

logger = get_structured_logger("salesgenie.ai.llm", "ai-gateway-service")
metrics = get_metrics("ai-gateway-service")

PROVIDER_TIMEOUT_SECONDS = 30.0
MAX_RETRIES_PER_PROVIDER = 1
BASE_BACKOFF_SECONDS = 1.0

_CIRCUIT_FAILURE_THRESHOLD = 5
_CIRCUIT_RECOVERY_TIMEOUT = 60


class CircuitState(str, Enum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"


class CircuitBreaker:
    """Per-provider circuit breaker preventing cascade failures."""

    def __init__(self, provider: str):
        self._provider = provider
        self._state = CircuitState.CLOSED
        self._failure_count = 0
        self._last_failure_time: Optional[float] = None
        self._recent_failures: deque = deque(maxlen=_CIRCUIT_FAILURE_THRESHOLD)

    def can_execute(self) -> bool:
        """Check if the circuit allows execution."""
        if self._state == CircuitState.CLOSED:
            return True
        if self._state == CircuitState.HALF_OPEN:
            return True
        # OPEN state — check if recovery timeout has elapsed
        if self._last_failure_time and (time.time() - self._last_failure_time) >= _CIRCUIT_RECOVERY_TIMEOUT:
            self._state = CircuitState.HALF_OPEN
            logger.info(
                "Circuit breaker half-open: provider=%s",
                self._provider,
                extra={"provider": self._provider, "circuit_state": self._state.value},
            )
            return True
        return False

    def record_success(self):
        """Record a successful call — reset circuit."""
        if self._state == CircuitState.HALF_OPEN:
            logger.info(
                "Circuit breaker closed: provider=%s",
                self._provider,
                extra={"provider": self._provider, "circuit_state": CircuitState.CLOSED.value},
            )
        self._state = CircuitState.CLOSED
        self._failure_count = 0
        self._last_failure_time = None
        self._recent_failures.clear()

    def record_failure(self):
        """Record a failed call — open circuit if threshold reached."""
        self._failure_count += 1
        self._last_failure_time = time.time()
        self._recent_failures.append(time.time())

        if self._failure_count >= _CIRCUIT_FAILURE_THRESHOLD:
            self._state = CircuitState.OPEN
            logger.error(
                "Circuit breaker opened: provider=%s",
                self._provider,
                extra={
                    "provider": self._provider,
                    "circuit_state": self._state.value,
                    "failure_count": self._failure_count,
                },
            )

    @property
    def state(self) -> CircuitState:
        return self._state


_circuit_breakers: Dict[str, CircuitBreaker] = {
    "groq": CircuitBreaker("groq"),
    "google": CircuitBreaker("google"),
    "mistral": CircuitBreaker("mistral"),
}

_GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
_GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
_MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY", "")

_groq_url = "https://api.groq.com/v1/chat/completions"
_google_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
_mistral_url = "https://api.mistral.ai/v1/chat/completions"


class LLMProvider:
    """Unified LLM Client supporting Groq, Google, and Mistral AI with multi-provider fallbacks."""

    def __init__(self):
        self._providers_configured = {
            "groq": bool(_GROQ_API_KEY),
            "google": bool(_GOOGLE_API_KEY),
            "mistral": bool(_MISTRAL_API_KEY),
        }
        logger.info(
            "LLM Provider initialized",
            extra={
                "providers_configured": self._providers_configured,
                "has_fallback": True,
            }
        )

    async def _call_provider(
        self,
        provider: str,
        url: str,
        headers: Dict[str, str],
        payload: Dict[str, Any],
    ) -> Optional[Dict[str, Any]]:
        """Call a single LLM provider with circuit breaker, timeout, and retry."""
        cb = _circuit_breakers.get(provider)
        if cb and not cb.can_execute():
            logger.error(
                "Provider circuit breaker is OPEN: skipping provider",
                extra={
                    "provider": provider,
                    "circuit_state": cb.state.value,
                    "failure_count": cb._failure_count,
                },
            )
            metrics.increment("llm_circuit_breaker_open_total", labels={"provider": provider})
            return None

        for attempt in range(MAX_RETRIES_PER_PROVIDER + 1):
            attempt_start = time.time()
            try:
                async with httpx.AsyncClient(timeout=PROVIDER_TIMEOUT_SECONDS) as client:
                    resp = await client.post(url, json=payload, headers=headers)
                    latency_ms = round((time.time() - attempt_start) * 1000, 2)

                    if resp.status_code == 200:
                        metrics.increment("llm_provider_success_total", labels={"provider": provider})
                        if cb:
                            cb.record_success()
                        logger.info(
                            "Provider succeeded",
                            extra={
                                "provider": provider,
                                "attempt": attempt + 1,
                                "latency_ms": latency_ms,
                                "status_code": 200,
                            },
                        )
                        return resp.json()
                    else:
                        metrics.increment("llm_provider_failure_total", labels={"provider": provider, "status": str(resp.status_code)})
                        if cb:
                            cb.record_failure()
                        logger.warning(
                            "Provider returned non-200 status",
                            extra={
                                "provider": provider,
                                "attempt": attempt + 1,
                                "latency_ms": latency_ms,
                                "status_code": resp.status_code,
                            },
                        )

            except httpx.TimeoutException:
                metrics.increment("llm_provider_failure_total", labels={"provider": provider, "status": "timeout"})
                if cb:
                    cb.record_failure()
                latency_ms = round((time.time() - attempt_start) * 1000, 2)
                logger.warning(
                    "Provider timed out",
                    extra={
                        "provider": provider,
                        "attempt": attempt + 1,
                        "latency_ms": latency_ms,
                        "error_type": "TimeoutException",
                    },
                )
            except httpx.ConnectError:
                metrics.increment("llm_provider_failure_total", labels={"provider": provider, "status": "connect_error"})
                if cb:
                    cb.record_failure()
                latency_ms = round((time.time() - attempt_start) * 1000, 2)
                logger.warning(
                    "Provider connection failed",
                    extra={
                        "provider": provider,
                        "attempt": attempt + 1,
                        "latency_ms": latency_ms,
                        "error_type": "ConnectError",
                    },
                )
            except Exception as e:
                metrics.increment("llm_provider_failure_total", labels={"provider": provider, "status": type(e).__name__})
                if cb:
                    cb.record_failure()
                latency_ms = round((time.time() - attempt_start) * 1000, 2)
                logger.warning(
                    "Provider request failed",
                    extra={
                        "provider": provider,
                        "attempt": attempt + 1,
                        "latency_ms": latency_ms,
                        "error_type": type(e).__name__,
                    },
                )

            if attempt < MAX_RETRIES_PER_PROVIDER:
                backoff = BASE_BACKOFF_SECONDS * (2 ** attempt)
                logger.info(
                    "Backing off before retry",
                    extra={"provider": provider, "backoff_seconds": backoff, "attempt": attempt + 1}
                )
                await asyncio.sleep(backoff)

        return None

    async def generate_response(
        self,
        messages: List[Dict[str, str]],
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1000,
        task_complexity: str = "medium",
        tenant_id: str = "default",
    ) -> Dict[str, Any]:
        """
        Generates text completion using cost-aware provider routing.
        Routes based on task complexity: low uses cheapest provider, high uses best quality.
        Raises RuntimeError if all providers fail or tenant is over budget.
        """
        # Check tenant budget before proceeding
        allowed, budget = cost_calculator.check_tenant_budget(tenant_id)
        if not allowed:
            logger.error(
                "Tenant budget exceeded, blocking LLM request",
                extra={
                    "tenant_id": tenant_id,
                    "usage_percent": budget.usage_percent,
                    "budget_usd": budget.monthly_budget_usd,
                }
            )
            metrics.increment("llm_budget_blocked_total", labels={"tenant_id": tenant_id})
            raise RuntimeError(
                f"Tenant {tenant_id} has exceeded budget limit "
                f"({budget.usage_percent:.1f}% of ${budget.monthly_budget_usd})"
            )
        formatted_messages = []
        if system_prompt:
            formatted_messages.append({"role": "system", "content": system_prompt})
        formatted_messages.extend(messages)

        request_id = str(uuid.uuid4())
        _gen_start = time.time()
        try:
            complexity = TaskComplexity(task_complexity)
        except ValueError:
            complexity = TaskComplexity.MEDIUM
        routing_chain = cost_calculator.get_routing_for_task(complexity)
        logger.info(
            "LLM generate_response started",
            extra={
                "request_id": request_id,
                "message_count": len(formatted_messages),
                "temperature": temperature,
                "max_tokens": max_tokens,
                "task_complexity": task_complexity,
                "routing_chain": [f"{p}:{m}" for p, m, _ in routing_chain],
            }
        )

        # Check LLM response cache before calling providers
        cached_response = llm_response_cache.get(formatted_messages, system_prompt, temperature, max_tokens)
        if cached_response:
            metrics.increment("llm_cache_hits_total", labels={"complexity": task_complexity})
            logger.info("LLM response cache hit", extra={
                "request_id": request_id, "task_complexity": task_complexity,
            })
            return {**cached_response, "cached": True}

        # Provider-specific configs
        provider_configs = {
            "groq": {
                "url": _groq_url,
                "headers": {
                    "Authorization": f"Bearer {os.getenv('GROQ_API_KEY_REDACTED', '[REDACTED]')}",
                    "Content-Type": "application/json",
                },
                "_key_present": _GROQ_API_KEY,
            },
            "google": {
                "url": f"{_google_url}?key=[REDACTED]",
                "headers": {"Content-Type": "application/json"},
                "_key_present": _GOOGLE_API_KEY,
            },
            "mistral": {
                "url": _mistral_url,
                "headers": {
                    "Authorization": f"Bearer {os.getenv('MISTRAL_API_KEY_REDACTED', '[REDACTED]')}",
                    "Content-Type": "application/json",
                },
                "_key_present": _MISTRAL_API_KEY,
            },
        }

        _input_tokens = _estimate_input_tokens(formatted_messages)

        for provider, model_name, _pricing in routing_chain:
            if not provider_configs[provider]["_key_present"]:
                continue
            _provider_start = time.time()
            headers = provider_configs[provider]["headers"]
            url = provider_configs[provider]["url"]

            if provider == "google":
                formatted_provider_messages = [
                    {"role": m["role"], "parts": [{"text": m["content"]}]}
                    for m in formatted_messages
                ]
                payload = {
                    "contents": formatted_provider_messages,
                    "generationConfig": {
                        "temperature": temperature,
                        "maxOutputTokens": max_tokens,
                    },
                }
            else:
                payload = {
                    "model": model_name,
                    "messages": formatted_messages,
                    "temperature": temperature,
                    "max_tokens": max_tokens,
                }

            data = await self._call_provider(provider, url, headers, payload)
            if data and ("choices" in data or "candidates" in data):
                if provider == "google":
                    content = data["candidates"][0]["content"]["parts"][0]["text"]
                    output_tokens = _estimate_output_tokens(content)
                else:
                    content = data["choices"][0]["message"]["content"]
                    output_tokens = data.get("usage", {}).get("total_tokens", 150) - _input_tokens
                    output_tokens = max(output_tokens, 50)
                tokens = _input_tokens + output_tokens
                _provider_duration = round((time.time() - _provider_start) * 1000, 2)
                _cost = cost_calculator.record_usage(tenant_id, provider, _input_tokens, output_tokens)
                logger.info(
                    "LLM response generated",
                    extra={
                        "request_id": request_id,
                        "provider": provider,
                        "model": model_name,
                        "tokens_used": tokens,
                        "input_tokens": _input_tokens,
                        "output_tokens": output_tokens,
                        "estimated_cost_usd": _cost,
                        "latency_ms": _provider_duration,
                        "task_complexity": task_complexity,
                    }
                )
                metrics.observe("llm_response_time_ms", _provider_duration,
                    labels={"provider": provider, "success": "true", "complexity": task_complexity})
                metrics.increment("llm_requests_total",
                    labels={"provider": provider, "success": "true", "complexity": task_complexity})
                metrics.increment("llm_tokens_total", value=tokens, labels={"provider": provider})
                metrics.observe("llm_cost_usd", _cost, labels={"provider": provider})
                metrics.increment("llm_budget_consumed_usd", value=_cost, labels={"tenant_id": tenant_id})
                llm_response_cache.set(
                    formatted_messages, system_prompt, temperature, max_tokens,
                    {
                        "content": content,
                        "provider": provider,
                        "model": model_name,
                        "tokens_used": tokens,
                        "input_tokens": _input_tokens,
                        "output_tokens": output_tokens,
                        "estimated_cost_usd": _cost,
                    }
                )
                return {
                    "content": content,
                    "provider": provider,
                    "model": model_name,
                    "tokens_used": tokens,
                    "input_tokens": _input_tokens,
                    "output_tokens": output_tokens,
                    "estimated_cost_usd": _cost,
                }
            _provider_duration = round((time.time() - _provider_start) * 1000, 2)
            metrics.increment("llm_requests_total",
                labels={"provider": provider, "success": "false", "complexity": task_complexity})
            metrics.observe("llm_response_time_ms", _provider_duration,
                labels={"provider": provider, "success": "false"})
            logger.warning(
                "Provider failed, trying next in routing chain",
                extra={"provider": provider, "request_id": request_id, "next_provider": None}
            )

        # 4. All providers failed — raise error, do NOT return fake content
        total_duration_ms = round((time.time() - _gen_start) * 1000, 2)
        metrics.increment("llm_requests_total", labels={"provider": "all", "success": "false"})
        metrics.observe("llm_response_time_ms", total_duration_ms, labels={"provider": "all", "success": "false"})
        logger.error(
            "All LLM providers failed or are unavailable",
            extra={
                "request_id": request_id,
                "providers_configured": self._providers_configured,
                "providers_attempted": [p for p, c in self._providers_configured.items() if c],
            }
        )
        raise RuntimeError(
            "All LLM providers failed or are unavailable. "
            "At least one of GROQ_API_KEY, GOOGLE_API_KEY, or MISTRAL_API_KEY must be configured and reachable."
        )


def _estimate_input_tokens(messages: List[Dict[str, str]]) -> int:
    """Rough token estimation: ~4 chars per token."""
    total_chars = sum(len(m.get("content", "")) for m in messages)
    return max(total_chars // 4, 50)


def _estimate_output_tokens(text: str) -> int:
    """Rough token estimation for output text."""
    return max(len(text) // 4, 50)


llm_provider = LLMProvider()
