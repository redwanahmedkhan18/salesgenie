"""
Structured Logging System for SalesGenie Enterprise Platform

Provides:
- JSON structured logging with correlation IDs, request IDs, tenant IDs, user IDs, trace IDs
- Sensitive data redaction (API keys, tokens, passwords, PII)
- Log context propagation via context variables
- Log level configuration from environment

Follows observability.md standards (Section 7.1 - Logging Standards).
Self-contained — uses only Python standard library (no external dependencies).
"""

import json
import logging
import re
import uuid
import time
from datetime import datetime
from typing import Any, Dict, Optional
from contextvars import ContextVar

logging.getLogger("salesgenie.logging")


_request_id_ctx: ContextVar[Optional[str]] = ContextVar("request_id", default=None)
_user_id_ctx: ContextVar[Optional[str]] = ContextVar("user_id", default=None)
_tenant_id_ctx: ContextVar[Optional[str]] = ContextVar("tenant_id", default=None)
_trace_id_ctx: ContextVar[Optional[str]] = ContextVar("trace_id", default=None)
_span_id_ctx: ContextVar[Optional[str]] = ContextVar("span_id", default=None)

SENSITIVE_KEY_PATTERNS = [
    re.compile(r'(?i)(password)', re.IGNORECASE),
    re.compile(r'(?i)(secret_key)', re.IGNORECASE),
    re.compile(r'(?i)(api_key)', re.IGNORECASE),
    re.compile(r'(?i)(apikey)', re.IGNORECASE),
    re.compile(r'(?i)(access_token)', re.IGNORECASE),
    re.compile(r'(?i)(auth_token)', re.IGNORECASE),
    re.compile(r'(?i)(refresh_token)', re.IGNORECASE),
    re.compile(r'(?i)(credit_card)', re.IGNORECASE),
    re.compile(r'(?i)(card_number)', re.IGNORECASE),
    re.compile(r'(?i)(cvv)', re.IGNORECASE),
    re.compile(r'(?i)(ssn)', re.IGNORECASE),
    re.compile(r'(?i)(private_key)', re.IGNORECASE),
]

SENSITIVE_KEY_NAMES = {
    'password', 'secret_key', 'api_key', 'apikey', 'access_token', 'auth_token',
    'refresh_token', 'credit_card', 'card_number', 'cvv', 'ssn', 'private_key',
    'token', 'credential', 'password_hash', 'secret',
}

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

REDACTED_PLACEHOLDER = "[REDACTED]"


def set_request_context(
    request_id: Optional[str] = None,
    user_id: Optional[str] = None,
    tenant_id: Optional[str] = None,
    trace_id: Optional[str] = None,
    span_id: Optional[str] = None,
):
    """Set logging context for the current async context. Call at request start."""
    _request_id_ctx.set(request_id or str(uuid.uuid4()))
    if user_id is not None:
        _user_id_ctx.set(user_id)
    if tenant_id is not None:
        _tenant_id_ctx.set(tenant_id)
    if trace_id is not None:
        _trace_id_ctx.set(trace_id)
    if span_id is not None:
        _span_id_ctx.set(span_id)


def clear_request_context():
    """Clear logging context. Call at request end."""
    _request_id_ctx.set(None)
    _user_id_ctx.set(None)
    _tenant_id_ctx.set(None)
    _trace_id_ctx.set(None)
    _span_id_ctx.set(None)


def get_request_id() -> str:
    rid = _request_id_ctx.get()
    if not rid:
        rid = str(uuid.uuid4())
        _request_id_ctx.set(rid)
    return rid


def get_log_context() -> Dict[str, str]:
    """Get current logging context for inclusion in log records."""
    return {
        "request_id": _request_id_ctx.get() or "",
        "user_id": _user_id_ctx.get() or "",
        "tenant_id": _tenant_id_ctx.get() or "",
        "trace_id": _trace_id_ctx.get() or "",
        "span_id": _span_id_ctx.get() or "",
    }


def redact_sensitive_data(value: str) -> str:
    """Redact sensitive data patterns from a string value."""
    if not isinstance(value, str):
        return value
    redacted = value
    for pattern in SENSITIVE_KEY_PATTERNS:
        redacted = pattern.sub(lambda m: m.group(1) + "=" + REDACTED_PLACEHOLDER, redacted)
    return redacted


def redact_sensitive_dict(data: Any) -> Any:
    """Recursively redact sensitive keys from dicts/lists."""
    if isinstance(data, dict):
        result = {}
        for k, v in data.items():
            key_lower = k.lower() if isinstance(k, str) else str(k).lower()
            if key_lower in SENSITIVE_KEY_NAMES or any(s in key_lower for s in SENSITIVE_KEY_NAMES):
                result[k] = REDACTED_PLACEHOLDER
            else:
                result[k] = redact_sensitive_dict(v)
        return result
    elif isinstance(data, list):
        return [redact_sensitive_dict(item) for item in data]
    elif isinstance(data, str):
        return redact_sensitive_data(data)
    return data


def redact_sensitive_headers(headers: Dict[str, str]) -> Dict[str, str]:
    """Redact sensitive HTTP headers."""
    result = {}
    for k, v in headers.items():
        if k.lower() in SENSITIVE_HEADER_NAMES:
            result[k] = REDACTED_PLACEHOLDER
        else:
            result[k] = redact_sensitive_data(str(v))
    return result


class SensitiveDataFilter(logging.Filter):
    """Logging filter that redacts sensitive data from log records."""

    def filter(self, record: logging.LogRecord) -> bool:
        try:
            if hasattr(record, "msg") and isinstance(record.msg, str):
                record.msg = redact_sensitive_data(record.msg)
            if hasattr(record, "args") and record.args:
                if isinstance(record.args, dict):
                    record.args = redact_sensitive_dict(record.args)
                elif isinstance(record.args, (tuple, list)):
                    record.args = tuple(redact_sensitive_data(str(a)) if isinstance(a, str) else a for a in record.args)
        except Exception:
            pass
        return True


class JSONFormatter(logging.Formatter):
    """JSON formatter that includes structured fields per observability.md Section 7.1."""

    def __init__(self, service_name: str = "salesgenie"):
        super().__init__()
        self._service_name = service_name

    def format(self, record: logging.LogRecord) -> str:
        ctx = get_log_context()

        if isinstance(record.msg, dict):
            log_entry = dict(record.msg)
        else:
            log_entry = {"message": record.getMessage()}

        log_entry.update({
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "service": self._service_name,
            "logger": record.name,
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        })

        for key, default in ctx.items():
            if default:
                log_entry.setdefault(key, default)

        if hasattr(record, "extra_data"):
            log_entry["context"] = redact_sensitive_dict(getattr(record, "extra_data"))

        if record.exc_info:
            log_entry["exception"] = self.formatException(record.exc_info)

        return json.dumps(log_entry, default=str, ensure_ascii=False)


class StructuredLogger:
    """Wrapper around standard logging that emits structured JSON with context."""

    def __init__(self, name: str, service_name: str = "salesgenie"):
        self._logger = logging.getLogger(name)
        self._service_name = service_name

    def _log(self, level: int, message: str, extra: Optional[Dict[str, Any]] = None):
        ctx = get_log_context()
        log_data = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "service": self._service_name,
            "level": logging.getLevelName(level),
            "message": redact_sensitive_data(message),
            "logger": self._logger.name,
            "request_id": ctx.get("request_id", ""),
            "user_id": ctx.get("user_id", ""),
            "tenant_id": ctx.get("tenant_id", ""),
            "trace_id": ctx.get("trace_id", ""),
            "span_id": ctx.get("span_id", ""),
        }
        if extra:
            log_data["context"] = redact_sensitive_dict(extra)
        self._logger.log(level, json.dumps(log_data, default=str, ensure_ascii=False))

    def debug(self, message: str, extra: Optional[Dict[str, Any]] = None):
        self._log(logging.DEBUG, message, extra)

    def info(self, message: str, extra: Optional[Dict[str, Any]] = None):
        self._log(logging.INFO, message, extra)

    def warning(self, message: str, extra: Optional[Dict[str, Any]] = None):
        self._log(logging.WARNING, message, extra)

    def error(self, message: str, extra: Optional[Dict[str, Any]] = None):
        self._log(logging.ERROR, message, extra)

    def critical(self, message: str, extra: Optional[Dict[str, Any]] = None):
        self._log(logging.CRITICAL, message, extra)

    def exception(self, message: str, extra: Optional[Dict[str, Any]] = None):
        import traceback
        exc_info = traceback.format_exc()
        merged_extra = dict(extra or {})
        merged_extra["exception"] = redact_sensitive_data(exc_info)
        self._log(logging.ERROR, message, merged_extra)


def get_structured_logger(name: str, service_name: str = "salesgenie") -> StructuredLogger:
    """Get a structured logger instance."""
    return StructuredLogger(name, service_name)


def setup_logging(service_name: str = "salesgenie", level: str = "INFO"):
    """Configure structured JSON logging for a service."""
    import os

    log_level = level if os.getenv("LOG_LEVEL") is None else os.getenv("LOG_LEVEL")
    numeric_level = getattr(logging, log_level.upper(), logging.INFO)

    root_logger = logging.getLogger()
    root_logger.setLevel(numeric_level)

    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(numeric_level)
    console_handler.setFormatter(JSONFormatter(service_name=service_name))
    console_handler.addFilter(SensitiveDataFilter())
    root_logger.addHandler(console_handler)

    salesgenie_logger = logging.getLogger("enterprise_ai_platform")
    salesgenie_logger.setLevel(numeric_level)
    salesgenie_logger.handlers = [console_handler]
    salesgenie_logger.propagate = False

    _logger = get_structured_logger("salesgenie.logging", service_name)
    _logger.info(f"Structured logging initialized for service '{service_name}' at level {log_level}")


class RequestLogger:
    """Helper to log request lifecycle events with timing."""

    def __init__(self, logger_instance: StructuredLogger):
        self._logger = logger_instance
        self._start_time: Optional[float] = None

    def start(self):
        self._start_time = time.time()

    def log_request(self, method: str, path: str, status_code: int,
                    user_id: Optional[str] = None, tenant_id: Optional[str] = None):
        duration_ms = 0.0
        if self._start_time:
            duration_ms = round((time.time() - self._start_time) * 1000, 2)
        self._logger.info(
            f"HTTP {method} {path} {status_code}",
            extra={
                "method": method,
                "path": path,
                "status_code": status_code,
                "duration_ms": duration_ms,
                "user_id": user_id or "",
                "tenant_id": tenant_id or "",
            }
        )

    def log_error(self, method: str, path: str, error: str,
                  status_code: int = 500):
        duration_ms = 0.0
        if self._start_time:
            duration_ms = round((time.time() - self._start_time) * 1000, 2)
        self._logger.error(
            f"HTTP {method} {path} {status_code} - {error}",
            extra={
                "method": method,
                "path": path,
                "status_code": status_code,
                "duration_ms": duration_ms,
                "error": redact_sensitive_data(error),
            }
        )
