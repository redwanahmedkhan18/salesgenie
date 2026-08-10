"""
Cost Management & Model Routing for SalesGenie

Provides:
- Per-provider token pricing (input/output per 1M tokens)
- Cost estimation per request and per tenant
- Model routing rules based on task complexity and quality requirements
- Budget alerts and usage tracking
- Cache-aware optimization for LLM responses

See COST_AUDIT.md for pricing reference and optimization strategy.
"""

import hashlib
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple

from pydantic import BaseModel, Field


class TaskComplexity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass
class ProviderPricing:
    """Per-1M token pricing for an LLM provider."""
    input_cost_per_1m: float
    output_cost_per_1m: float
    currency: str = "USD"


# Provider pricing (2026-08 rates)
PROVIDER_PRICING: Dict[str, ProviderPricing] = {
    "groq": ProviderPricing(
        input_cost_per_1m=0.59,
        output_cost_per_1m=0.79,
    ),
    "google": ProviderPricing(
        input_cost_per_1m=0.35,
        output_cost_per_1m=0.70,
    ),
    "mistral": ProviderPricing(
        input_cost_per_1m=0.14,
        output_cost_per_1m=0.42,
    ),
}

# Model recommendations by task complexity
MODEL_ROUTING: Dict[TaskComplexity, List[Tuple[str, str, ProviderPricing]]] = {
    TaskComplexity.LOW: [
        # Use cheapest provider first for simple tasks
        ("mistral", "mistral-large-latest", PROVIDER_PRICING["mistral"]),
        ("groq", "llama3-8b-8192", PROVIDER_PRICING["groq"]),
    ],
    TaskComplexity.MEDIUM: [
        # Balanced quality/cost
        ("groq", "llama3-70b-8192", PROVIDER_PRICING["groq"]),
        ("google", "gemini-1.5-flash", PROVIDER_PRICING["google"]),
    ],
    TaskComplexity.HIGH: [
        # Highest quality
        ("groq", "llama3-70b-8192", PROVIDER_PRICING["groq"]),
        ("google", "gemini-1.5-pro", PROVIDER_PRICING["google"]),
        ("mistral", "mistral-large-latest", PROVIDER_PRICING["mistral"]),
    ],
}

# Budget thresholds
DEFAULT_BUDGET_USD = 5000.0
BUDGET_ALERT_THRESHOLD = 0.80  # 80% of budget
BUDGET_HARD_LIMIT = 0.95  # 95% of budget - block requests


class TenantBudget(BaseModel):
    """Per-tenant budget tracking."""
    tenant_id: str
    monthly_budget_usd: float = 1000.0
    current_spent_usd: float = 0.0
    last_reset: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    alerts_sent: List[str] = Field(default_factory=list)

    @property
    def usage_percent(self) -> float:
        if self.monthly_budget_usd <= 0:
            return 0.0
        return (self.current_spent_usd / self.monthly_budget_usd) * 100

    @property
    def is_at_risk(self) -> bool:
        return self.usage_percent >= BUDGET_ALERT_THRESHOLD * 100

    @property
    def is_over_budget(self) -> bool:
        return self.usage_percent >= BUDGET_HARD_LIMIT * 100


class CostCalculator:
    """Calculates cost of LLM requests and tracks tenant budgets."""

    def __init__(self):
        self._tenant_budgets: Dict[str, TenantBudget] = {}
        self._platform_budget_usd = DEFAULT_BUDGET_USD
        self._platform_spent_usd = 0.0

    def estimate_cost(
        self, provider: str, input_tokens: int, output_tokens: int
    ) -> float:
        """Estimate the cost of an LLM request in USD."""
        pricing = PROVIDER_PRICING.get(provider)
        if not pricing:
            return 0.0
        input_cost = (input_tokens / 1_000_000) * pricing.input_cost_per_1m
        output_cost = (output_tokens / 1_000_000) * pricing.output_cost_per_1m
        return round(input_cost + output_cost, 4)

    def get_routing_for_task(
        self, complexity: TaskComplexity
    ) -> List[Tuple[str, str, ProviderPricing]]:
        """Get provider chain for a given task complexity."""
        return MODEL_ROUTING.get(complexity, MODEL_ROUTING[TaskComplexity.MEDIUM])

    def check_tenant_budget(self, tenant_id: str) -> Tuple[bool, TenantBudget]:
        """Check if tenant is within budget. Returns (allowed, budget)."""
        budget = self._tenant_budgets.get(tenant_id)
        if not budget:
            budget = TenantBudget(tenant_id=tenant_id)
            self._tenant_budgets[tenant_id] = budget

        if budget.is_over_budget:
            return False, budget
        return True, budget

    def record_usage(
        self, tenant_id: str, provider: str, input_tokens: int, output_tokens: int
    ) -> float:
        """Record token usage and cost for a tenant. Returns cost in USD."""
        cost = self.estimate_cost(provider, input_tokens, output_tokens)

        if tenant_id not in self._tenant_budgets:
            self._tenant_budgets[tenant_id] = TenantBudget(tenant_id=tenant_id)

        self._tenant_budgets[tenant_id].current_spent_usd += cost
        self._platform_spent_usd += cost
        return cost

    def get_tenant_usage(self, tenant_id: str) -> Optional[TenantBudget]:
        """Get usage info for a tenant."""
        return self._tenant_budgets.get(tenant_id)

    def reset_tenant_usage(self, tenant_id: str) -> None:
        """Reset monthly usage for a tenant."""
        if tenant_id in self._tenant_budgets:
            self._tenant_budgets[tenant_id].current_spent_usd = 0.0
            self._tenant_budgets[tenant_id].last_reset = datetime.now(timezone.utc)
            self._tenant_budgets[tenant_id].alerts_sent = []

    def get_platform_usage(self) -> Dict:
        """Get platform-wide usage summary."""
        total_spent = sum(b.current_spent_usd for b in self._tenant_budgets.values())
        return {
            "platform_budget_usd": self._platform_budget_usd,
            "platform_spent_usd": round(total_spent, 4),
            "usage_percent": round(
                (total_spent / self._platform_budget_usd * 100)
                if self._platform_budget_usd > 0
                else 0,
                2
            ),
            "tenant_count": len(self._tenant_budgets),
            "tenants_at_risk": [
                b.tenant_id for b in self._tenant_budgets.values()
                if b.is_at_risk and not b.is_over_budget
            ],
            "tenants_over_budget": [
                b.tenant_id for b in self._tenant_budgets.values()
                if b.is_over_budget
            ],
        }


class LLMResponseCache:
    """
    In-memory cache for LLM responses keyed on normalized prompt hash.
    TTL-based eviction with LRU fallback.
    Estimated 30-40% reduction in LLM calls for repeated/similar queries.
    """

    def __init__(self, ttl_seconds: int = 3600, max_entries: int = 5000):
        self._cache: Dict[str, Tuple[float, Dict[str, Any]]] = {}
        self._ttl = ttl_seconds
        self._max_entries = max_entries

    def _normalize_messages(self, messages: List[Dict[str, str]]) -> str:
        """Normalize messages for consistent hashing (strip whitespace, order)."""
        normalized = []
        for m in messages:
            content = m.get("content", "").strip()
            role = m.get("role", "user")
            normalized.append(f"{role}:{content}")
        return "|".join(normalized)

    def _make_key(self, messages: List[Dict[str, str]], system_prompt: Optional[str],
                  temperature: float, max_tokens: int) -> str:
        """Generate cache key from request parameters."""
        normalized = self._normalize_messages(messages)
        if system_prompt:
            normalized += f"|sys:{system_prompt.strip()}"
        normalized += f"|t:{temperature}|m:{max_tokens}"
        return hashlib.sha256(normalized.encode("utf-8")).hexdigest()

    def get(self, messages: List[Dict[str, str]], system_prompt: Optional[str],
            temperature: float, max_tokens: int) -> Optional[Dict[str, Any]]:
        """Get cached response if available and not expired."""
        key = self._make_key(messages, system_prompt, temperature, max_tokens)
        entry = self._cache.get(key)
        if entry is None:
            return None
        timestamp, response = entry
        if time.time() - timestamp > self._ttl:
            del self._cache[key]
            return None
        return response

    def set(self, messages: List[Dict[str, str]], system_prompt: Optional[str],
            temperature: float, max_tokens: int, response: Dict[str, Any]) -> None:
        """Cache a response."""
        if len(self._cache) >= self._max_entries:
            # Evict oldest entry (simple LRU-ish by timestamp)
            oldest_key = min(self._cache, key=lambda k: self._cache[k][0])
            del self._cache[oldest_key]
        key = self._make_key(messages, system_prompt, temperature, max_tokens)
        self._cache[key] = (time.time(), response)

    def stats(self) -> Dict[str, int]:
        """Get cache statistics."""
        now = time.time()
        valid = sum(1 for _, (ts, _) in self._cache.items() if now - ts <= self._ttl)
        expired = len(self._cache) - valid
        return {
            "total_entries": len(self._cache),
            "valid_entries": valid,
            "expired_entries": expired,
            "max_entries": self._max_entries,
            "ttl_seconds": self._ttl,
        }


llm_response_cache = LLMResponseCache(ttl_seconds=3600, max_entries=5000)
