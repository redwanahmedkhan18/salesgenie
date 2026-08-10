"""
Sentry Integration for Backend Error Reporting

Initializes Sentry for all backend microservices. Captures:
- Unhandled exceptions with full stack traces
- Request context (path, method, user_id, tenant_id)
- Release and environment tracking
- Performance monitoring (transactions)
- Breadcrumb trails for debugging

Usage in each service's main.py:
    from enterprise_ai_platform.common.observability import init_sentry
    init_sentry("salesgenie-service-name")
"""

import logging
import os
from typing import Optional

from enterprise_ai_platform.common.config import settings

logger = logging.getLogger("salesgenie.observability.sentry")


def init_sentry(service_name: str) -> bool:
    """
    Initialize Sentry SDK for a backend microservice.

    Returns True if Sentry was initialized, False if disabled or failed.
    """
    sentry_dsn = os.getenv("SENTRY_DSN") or getattr(settings, "SENTRY_DSN", None)

    if not sentry_dsn:
        logger.info("Sentry DSN not configured — error reporting disabled (service=%s)", service_name)
        return False

    try:
        import sentry_sdk
        from sentry_sdk.integrations.logging import LoggingIntegration
        from sentry_sdk.integrations.fastapi import FastApiIntegration
        from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration

        sentry_logging = LoggingIntegration(
            level=logging.INFO,
            event_level=logging.ERROR,
        )

        sentry_sdk.init(
            dsn=sentry_dsn,
            integrations=[
                FastApiIntegration(),
                sentry_logging,
                SqlalchemyIntegration(),
            ],
            traces_sample_rate=0.1,
            profiles_sample_rate=0.1,
            send_default_pii=False,
            request_bodies="never",
            before_send=_before_send,
            before_breadcrumb=_before_breadcrumb,
        )

        sentry_sdk.set_tag("service", service_name)
        sentry_sdk.set_tag("environment", settings.ENVIRONMENT)
        sentry_sdk.set_tag("release", os.getenv("RELEASE_VERSION", "unknown"))

        logger.info("Sentry initialized for service: %s", service_name)
        return True

    except ImportError:
        logger.warning("sentry-sdk not installed — error reporting disabled")
        return False
    except Exception as e:
        logger.error("Failed to initialize Sentry: %s", e)
        return False


def _before_send(event, hint):
    """Filter sensitive data from Sentry events before sending."""
    if "request" in event:
        # Remove sensitive headers
        sensitive_headers = {"authorization", "cookie", "set-cookie", "x-api-key", "x-auth-token"}
        if "headers" in event["request"]:
            event["request"]["headers"] = {
                k: v for k, v in event["request"]["headers"].items()
                if k.lower() not in sensitive_headers
            }

    # Remove sensitive user data from events
    if "user" in event:
        event["user"].pop("email", None)
        event["user"].pop("ip_address", None)

    return event


def _before_breadcrumb(breadcrumb, hint):
    """Filter sensitive data from Sentry breadcrumbs."""
    if breadcrumb.get("data"):
        sensitive_keys = {"password", "token", "api_key", "secret", "credit_card"}
        for key in list(breadcrumb["data"].keys()):
            if any(s in key.lower() for s in sensitive_keys):
                breadcrumb["data"][key] = "[REDACTED]"

    return breadcrumb


def capture_exception(exc: Optional[Exception] = None, **tags) -> None:
    """Manually capture an exception with additional context."""
    try:
        import sentry_sdk

        with sentry_sdk.configure_scope() as scope:
            for key, value in tags.items():
                scope.set_tag(key, str(value))

            if exc:
                sentry_sdk.capture_exception(exc)
    except ImportError:
        pass


def capture_message(message: str, **tags) -> None:
    """Manually capture a message/event."""
    try:
        import sentry_sdk

        with sentry_sdk.configure_scope() as scope:
            for key, value in tags.items():
                scope.set_tag(key, str(value))

            sentry_sdk.capture_message(message, level="warning")
    except ImportError:
        pass
