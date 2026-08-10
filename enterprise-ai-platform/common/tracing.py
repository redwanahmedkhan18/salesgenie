"""
Trace Context Propagation for SalesGenie Enterprise Platform

Provides W3C Trace Context propagation (traceparent header) for distributed tracing
across microservices. Works without OpenTelemetry — extracts/propagates trace IDs
via HTTP headers.

Follows observability.md Section 8 (Distributed Tracing Architecture).

Usage:
    from enterprise_ai_platform.common.tracing import extract_trace_context, inject_trace_context

    # Extract from incoming request
    trace_context = extract_trace_context(request.headers)

    # When making outbound HTTP calls, inject into headers
    headers = inject_trace_context(base_headers, trace_context)
"""

import uuid
import re
from typing import Dict, Optional, Tuple
from contextvars import ContextVar

from .logging import get_structured_logger, set_request_context

logger = get_structured_logger("salesgenie.tracing", "tracing")

_trace_context: ContextVar[Dict[str, str]] = ContextVar("trace_context", default={})

_TRACEPARENT_RE = re.compile(
    r'^([0-9a-f]{2})-([0-9a-f]{32})-([0-9a-f]{16})-([0-9a-f]{2})$'
)


def _generate_trace_id() -> str:
    return uuid.uuid4().hex


def _generate_span_id() -> str:
    return uuid.uuid4().hex[:16]


def extract_trace_context(headers: Dict[str, str]) -> Dict[str, str]:
    """Extract trace context from HTTP headers.

    Supports W3C Trace Context (traceparent), B3 (X-B3-TraceId/X-B3-ParentSpanId),
    and X-Trace-Id headers.
    """
    trace_context = {}

    traceparent = None
    for k in headers:
        if k.lower() == "traceparent":
            traceparent = headers[k]
            break

    if traceparent:
        match = _TRACEPARENT_RE.match(traceparent)
        if match:
            trace_context = {
                "trace_id": match.group(2),
                "span_id": match.group(3),
                "trace_flags": match.group(4),
                "version": match.group(1),
            }
        else:
            logger.warning(
                "Invalid traceparent header format",
                extra={"traceparent": "[REDACTED]"}
            )
    else:
        trace_id = headers.get("x-trace-id") or headers.get("x-b3-traceid")
        span_id = headers.get("x-b3-spanid") or _generate_span_id()
        if trace_id:
            trace_context = {"trace_id": trace_id, "span_id": span_id}

    if not trace_context:
        trace_context = {
            "trace_id": _generate_trace_id(),
            "span_id": _generate_span_id(),
        }

    _trace_context.set(trace_context)
    return trace_context


def inject_trace_context(headers: Dict[str, str], trace_context: Dict[str, str]) -> Dict[str, str]:
    """Inject trace context into HTTP headers for outbound calls."""
    result = dict(headers)
    trace_id = trace_context.get("trace_id", _generate_trace_id())
    span_id = trace_context.get("span_id", _generate_span_id())

    result["traceparent"] = f"00-{trace_id}-{span_id}-01"
    result["x-b3-traceid"] = trace_id
    result["x-b3-spanid"] = span_id
    result["x-request-id"] = trace_context.get("request_id", str(uuid.uuid4()))

    return result


def get_trace_context() -> Dict[str, str]:
    """Get the current trace context."""
    return _trace_context.get()


def start_span(trace_ctx: Dict[str, str], span_name: str) -> str:
    """Start a new span and return the span ID."""
    parent_span_id = trace_ctx.get("span_id", _generate_span_id())
    new_span_id = _generate_span_id()
    logger.debug(
        f"Span started: {span_name}",
        extra={
            "span_name": span_name,
            "trace_id": trace_ctx.get("trace_id", ""),
            "parent_span_id": parent_span_id,
            "span_id": new_span_id,
        }
    )
    return new_span_id


def propagate_context(request_id: str, trace_id: str, span_id: str,
                      user_id: Optional[str] = None, tenant_id: Optional[str] = None):
    """Set up full request context for an incoming request."""
    set_request_context(
        request_id=request_id,
        user_id=user_id,
        tenant_id=tenant_id,
        trace_id=trace_id,
        span_id=span_id,
    )
    _trace_context.set({
        "trace_id": trace_id,
        "span_id": span_id,
        "request_id": request_id,
    })
