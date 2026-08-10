"""
Request Logging & Correlation ID Middleware for SalesGenie Enterprise Platform

Provides:
- Request ID generation and propagation (X-Request-ID header)
- Trace ID propagation (traceparent / X-B3-TraceId headers)
- User/tenant context extraction from JWT token
- Structured request logging with timing
- Response header injection for client-side tracing
- Sensitive header redaction in logs

Follows observability.md Section 7.1 (Logging Standards) and Section 8 (Distributed Tracing).
"""

import uuid
import time
import logging
from typing import Optional, Callable, Any
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp

from .logging import (
    set_request_context,
    clear_request_context,
    get_structured_logger,
    redact_sensitive_headers,
    SensitiveDataFilter,
)
from .config import settings
from .tracing import extract_trace_context, propagate_context

logger = get_structured_logger("salesgenie.middleware.request", "api-gateway")

SENSITIVE_HEADER_NAMES = {
    'authorization',
    'cookie',
    'set-cookie',
    'x-api-key',
    'x-auth-token',
    'x-access-token',
    'authentication',
    'proxy-authorization',
}


def _extract_user_context(request: Request) -> tuple:
    """Extract user_id and tenant_id from JWT token in request."""
    user_id = None
    tenant_id = None

    auth_header = request.headers.get("authorization", "")
    if auth_header.startswith("Bearer "):
        token = auth_header[7:]
        try:
            from .security_rbac import verify_jwt_token
            payload = verify_jwt_token(token)
            user_id = str(payload.sub)
            tenant_id = str(payload.tenant_id)
        except Exception:
            pass

    return user_id, tenant_id


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """Middleware that generates request IDs, sets log context, and logs request lifecycle."""

    def __init__(self, app: ASGIApp, service_name: str = "salesgenie"):
        super().__init__(app)
        self._service_name = service_name
        self._logger = get_structured_logger("salesgenie.middleware.request", service_name)

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        start_time = time.time()

        request_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())
        trace_context = extract_trace_context(dict(request.headers))
        user_id, tenant_id = _extract_user_context(request)

        propagate_context(
            request_id=request_id,
            trace_id=trace_context["trace_id"],
            span_id=trace_context["span_id"],
            user_id=user_id,
            tenant_id=tenant_id,
        )

        self._logger.info(
            "Incoming request",
            extra={
                "method": request.method,
                "path": str(request.url.path),
                "request_id": request_id,
                "user_id": user_id or "",
                "tenant_id": tenant_id or "",
                "trace_id": trace_context["trace_id"],
                "span_id": trace_context["span_id"],
                "headers": redact_sensitive_headers(dict(request.headers))
            }
        )

        try:
            response = await call_next(request)
            duration_ms = round((time.time() - start_time) * 1000, 2)

            response.headers["X-Request-ID"] = request_id
            response.headers["X-Trace-ID"] = trace_context["trace_id"]
            response.headers["X-Span-ID"] = trace_context["span_id"]
            response.headers["traceparent"] = f"00-{trace_context['trace_id']}-{trace_context['span_id']}-01"

            self._logger.info(
                "Request completed",
                extra={
                    "method": request.method,
                    "path": str(request.url.path),
                    "status_code": response.status_code,
                    "duration_ms": duration_ms,
                    "request_id": request_id,
                    "user_id": user_id or "",
                    "tenant_id": tenant_id or "",
                    "trace_id": trace_context["trace_id"],
                }
            )

            return response

        except Exception as e:
            duration_ms = round((time.time() - start_time) * 1000, 2)
            self._logger.error(
                "Request failed",
                extra={
                    "method": request.method,
                    "path": str(request.url.path),
                    "error": str(e),
                    "duration_ms": duration_ms,
                    "request_id": request_id,
                    "user_id": user_id or "",
                    "tenant_id": tenant_id or "",
                    "trace_id": trace_context["trace_id"],
                }
            )
            raise
        finally:
            clear_request_context()


def add_request_logging(app: ASGIApp, service_name: str = "salesgenie") -> ASGIApp:
    """Add request logging and correlation ID middleware to a FastAPI app."""
    from enterprise_ai_platform.common.logging import setup_logging
    setup_logging(service_name=service_name, level=settings.LOG_LEVEL)

    existing_middleware = [type(m.cls) for m in app.user_middleware if hasattr(m, 'cls')]
    if RequestLoggingMiddleware not in existing_middleware:
        app.add_middleware(RequestLoggingMiddleware, service_name=service_name)

    logging.getLogger().addFilter(SensitiveDataFilter())
    return app
