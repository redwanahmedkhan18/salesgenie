"""
Rate Limiting Middleware for SalesGenie
Prevents API abuse, DDoS attacks, and excessive AI token usage.
"""

import time
import asyncio
from typing import Dict, Optional, Callable, Any
from dataclasses import dataclass, field
from collections import defaultdict
from fastapi import Request, HTTPException, status
from fastapi.responses import JSONResponse
import jwt


@dataclass
class RateLimitConfig:
    requests_per_minute: int = 100
    requests_per_hour: int = 1000
    burst_size: int = 20
    ai_token_quota_per_hour: int = 100000
    ai_token_quota_per_minute: int = 5000


@dataclass
class ClientLimitState:
    requests_minute: int = 0
    requests_hour: int = 0
    minute_reset: float = field(default_factory=time.time)
    hour_reset: float = field(default_factory=time.time)
    tokens_minute: int = 0
    tokens_hour: int = 0
    ai_calls_minute: int = 0


class RateLimiter:
    def __init__(self):
        self._client_states: Dict[str, ClientLimitState] = defaultdict(ClientLimitState)
        self._global_lock = asyncio.Lock()
        self._configs: Dict[str, RateLimitConfig] = {}

    def get_config_for_tier(self, tier: str) -> RateLimitConfig:
        configs = {
            'free': RateLimitConfig(
                requests_per_minute=60,
                requests_per_hour=500,
                ai_token_quota_per_hour=100000,
                ai_token_quota_per_minute=5000,
            ),
            'starter': RateLimitConfig(
                requests_per_minute=120,
                requests_per_hour=2000,
                ai_token_quota_per_hour=500000,
                ai_token_quota_per_minute=25000,
            ),
            'growth': RateLimitConfig(
                requests_per_minute=300,
                requests_per_hour=10000,
                ai_token_quota_per_hour=2000000,
                ai_token_quota_per_minute=100000,
            ),
            'enterprise': RateLimitConfig(
                requests_per_minute=1000,
                requests_per_hour=50000,
                ai_token_quota_per_hour=10000000,
                ai_token_quota_per_minute=500000,
            ),
        }
        return configs.get(tier, configs['free'])

    def _get_client_key(self, request: Request) -> str:
        auth_header = request.headers.get('authorization', '')
        if auth_header.startswith('Bearer '):
            token = auth_header[7:]
            try:
                payload = jwt.decode(token, options={'verify_signature': False})
                return f"user:{payload.get('user_id', 'anonymous')}"
            except Exception:
                pass
        
        client_ip = request.client.host if request.client else 'unknown'
        return f"ip:{client_ip}"

    def _reset_if_needed(self, state: ClientLimitState) -> None:
        current_time = time.time()
        
        if current_time - state.minute_reset >= 60:
            state.requests_minute = 0
            state.minute_reset = current_time
        
        if current_time - state.hour_reset >= 3600:
            state.requests_hour = 0
            state.tokens_hour = 0
            state.ai_calls_minute = 0
            state.hour_reset = current_time

    async def check_rate_limit(
        self,
        request: Request,
        tier: str = 'free',
        tokens: int = 0,
        is_ai_request: bool = False
    ) -> Optional[JSONResponse]:
        client_key = self._get_client_key(request)
        config = self.get_config_for_tier(tier)
        
        async with self._global_lock:
            state = self._client_states[client_key]
            self._reset_if_needed(state)
            
            state.requests_minute += 1
            state.requests_hour += 1
            
            if tokens > 0:
                state.tokens_minute += tokens
                state.tokens_hour += tokens
            
            if is_ai_request:
                state.ai_calls_minute += 1
            
            if state.requests_minute > config.requests_per_minute:
                return JSONResponse(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    content={
                        'detail': f'Rate limit exceeded. Try again in {60 - (time.time() - state.minute_reset):.0f} seconds.',
                        'retry_after': int(60 - (time.time() - state.minute_reset)),
                    },
                    headers={'Retry-After': str(int(60 - (time.time() - state.minute_reset)))}
                )
            
            if state.requests_hour > config.requests_per_hour:
                return JSONResponse(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    content={
                        'detail': f'Hourly rate limit exceeded. Try again in {3600 - (time.time() - state.hour_reset):.0f} seconds.',
                        'retry_after': int(3600 - (time.time() - state.hour_reset)),
                    },
                    headers={'Retry-After': str(int(3600 - (time.time() - state.hour_reset)))}
                )
            
            if tokens > 0 and state.tokens_hour > config.ai_token_quota_per_hour:
                return JSONResponse(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    content={
                        'detail': f'Token quota exceeded for the hour.',
                        'retry_after': 3600,
                    },
                    headers={'Retry-After': '3600'}
                )
            
            if is_ai_request and state.ai_calls_minute > config.requests_per_minute // 10:
                return JSONResponse(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    content={
                        'detail': f'AI rate limit exceeded. Reduce request frequency.',
                        'retry_after': 60,
                    },
                    headers={'Retry-After': '60'}
                )
        
        return None


rate_limiter = RateLimiter()


async def rate_limit_middleware(request: Request, call_next: Callable) -> Any:
    tier = request.headers.get('x-rate-limit-tier', 'free')
    tokens = int(request.headers.get('x-rate-limit-tokens', '0'))
    is_ai_request = 'lead-intelligence' in str(request.url) or 'agents' in str(request.url)
    
    rate_limit_response = await rate_limiter.check_rate_limit(request, tier, tokens, is_ai_request)
    if rate_limit_response:
        return rate_limit_response
    
    response = await call_next(request)
    response.headers['X-RateLimit-Limit'] = str(rate_limiter.get_config_for_tier(tier).requests_per_minute)
    response.headers['X-RateLimit-Remaining'] = str(max(0, rate_limiter.get_config_for_tier(tier).requests_per_minute - rate_limiter._client_states[rate_limiter._get_client_key(request)].requests_minute))
    return response