"""
Rate Limiting Middleware
Simple in-memory sliding window rate limiter for protecting auth endpoints.
Uses Redis if available for distributed rate limiting across multiple instances.
"""

import asyncio
import time
import logging
from collections import defaultdict
from typing import Dict, List, Tuple
from fastapi import Request, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from fastapi.responses import JSONResponse as FastAPIJSONResponse

logger = logging.getLogger("salesgenie.ratelimit")


AUTH_RATE_LIMITS: Dict[str, Tuple[int, int]] = {
    "/api/v1/auth/login": (5, 60),
    "/api/v1/auth/signup": (3, 60),
    "/api/v1/auth/forgot-password": (3, 3600),
    "/api/v1/auth/refresh": (10, 60),
    "/api/v1/auth/mfa/verify": (5, 60),
}


class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self._requests: Dict[str, List[float]] = defaultdict(list)
        self._lock = asyncio.Lock()
        self._redis_client = None
        try:
            import os
            redis_url = os.getenv("REDIS_URL", "")
            if redis_url:
                import redis.asyncio as redis
                self._redis_client = redis.from_url(redis_url, decode_responses=True)
        except Exception:
            logger.warning("Redis not available for distributed rate limiting, using in-memory")

    def _get_client_id(self, request: Request) -> str:
        forwarded_for = request.headers.get("X-Forwarded-For")
        if forwarded_for:
            return forwarded_for.split(",")[0].strip()
        return request.client.host if request.client else "unknown"

    async def dispatch(self, request: Request, call_next):
        path = request.url.path
        if path in AUTH_RATE_LIMITS:
            max_requests, window_seconds = AUTH_RATE_LIMITS[path]
            client_id = self._get_client_id(request)

            allowed = await self._check_rate_limit(
                f"rate_limit:{client_id}:{path}",
                max_requests,
                window_seconds,
            )

            if not allowed:
                logger.warning(f"Rate limit exceeded for {client_id} on {path}")
                return JSONResponse(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    content={
                        "detail": "Too many requests. Please try again later.",
                        "retry_after": window_seconds,
                    },
                    headers={"Retry-After": str(window_seconds)},
                )

        return await call_next(request)

    async def _check_rate_limit(self, key: str, max_requests: int, window: int) -> bool:
        if self._redis_client:
            try:
                now = time.time()
                pipeline = self._redis_client.pipeline()
                pipeline.zremrangebyscore(key, 0, now - window)
                pipeline.zadd(key, {str(now): now})
                pipeline.expire(key, window)
                pipeline.zcard(key)
                results = await pipeline.execute()
                count = results[-1]
                return count <= max_requests
            except Exception as e:
                logger.warning(f"Redis rate limit check failed, falling back to in-memory: {type(e).__name__}")

        now = time.time()
        async with self._lock:
            requests = self._requests[key]
            cutoff = now - window
            self._requests[key] = [t for t in requests if t > cutoff]
            if len(self._requests[key]) >= max_requests:
                return False
            self._requests[key].append(now)
        return True


def add_rate_limiter(app):
    """Add rate limiting middleware to a FastAPI app."""
    from enterprise_ai_platform.common.config import settings
    if settings.DEBUG or settings.ENVIRONMENT == "test":
        return app
    app.add_middleware(RateLimitMiddleware)
    return app
