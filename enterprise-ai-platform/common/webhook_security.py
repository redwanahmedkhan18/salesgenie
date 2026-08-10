"""
Webhook Signature Verification for Integration Services

Provides HMAC-SHA256 signature verification for inbound webhooks from:
- WhatsApp (verify token)
- Slack (signing secret)
- Telegram (secret token)
- Discord (interactions public key)
- Facebook Messenger (app secret)

Prevents spoofed webhook messages from untrusted sources.
"""

import hashlib
import hmac
import logging
import time
from typing import Optional

from enterprise_ai_platform.common.config import settings

logger = logging.getLogger("salesgenie.webhooks.verify")

WEBHOOK_TOLERANCE_SECONDS = 300


def verify_slack_signature(signature: str, timestamp: str, body: str) -> bool:
    """Verify Slack webhook signature using signing secret."""
    if not getattr(settings, "SLACK_SIGNING_SECRET", None):
        logger.warning("SLACK_SIGNING_SECRET not configured — webhook verification disabled")
        return True

    if not signature or not timestamp:
        logger.warning("Missing Slack signature or timestamp")
        return False

    try:
        ts = int(timestamp)
        now = int(time.time())
        if abs(now - ts) > WEBHOOK_TOLERANCE_SECONDS:
            logger.warning("Slack webhook timestamp out of tolerance (possible replay attack)")
            return False
    except ValueError:
        logger.warning("Invalid Slack webhook timestamp")
        return False

    sig_basestring = f"v0:{timestamp}:{body}"
    computed = hmac.new(
        settings.SLACK_SIGNING_SECRET.encode("utf-8"),
        sig_basestring.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()
    expected = f"v0={computed}"

    if not hmac.compare_digest(expected, signature):
        logger.warning("Slack webhook signature mismatch")
        return False

    return True


def verify_telegram_signature(token: str, signature: Optional[str]) -> bool:
    """Verify Telegram webhook secret token."""
    expected_token = getattr(settings, "TELEGRAM_BOT_TOKEN", None)
    if not expected_token:
        logger.warning("TELEGRAM_BOT_TOKEN not configured — webhook verification disabled")
        return True

    if not signature:
        logger.warning("Missing Telegram secret token header")
        return False

    if not hmac.compare_digest(token, expected_token):
        logger.warning("Telegram webhook secret token mismatch")
        return False

    return True


def verify_discord_signature(signature: str, timestamp: str, body: str) -> bool:
    """Verify Discord interaction signature using public key (ed25519)."""
    try:
        from cryptography.hazmat.primitives import serialization
        from cryptography.hazmat.primitives.asymmetric import ed25519
        from cryptography.exceptions import InvalidSignature
    except ImportError:
        logger.warning("cryptography not available — Discord webhook verification disabled")
        return True

    public_key_pem = getattr(settings, "DISCORD_PUBLIC_KEY", None)
    if not public_key_pem:
        logger.warning("DISCORD_PUBLIC_KEY not configured — webhook verification disabled")
        return True

    try:
        public_key = serialization.load_pem_public_key(public_key_pem.encode("utf-8"))
        if not isinstance(public_key, ed25519.Ed25519PublicKey):
            logger.warning("Invalid Discord public key type")
            return False

        message = f"{timestamp}{body}"
        try:
            public_key.verify(
                bytes.fromhex(signature),
                message.encode("utf-8"),
            )
        except InvalidSignature:
            logger.warning("Discord webhook signature verification failed")
            return False
    except Exception as e:
        logger.warning("Discord webhook signature verification error: %s", e)
        return False

    return True


def verify_messenger_signature(signature: str, body: str) -> bool:
    """Verify Facebook Messenger webhook signature."""
    app_secret = getattr(settings, "MESSENGER_APP_SECRET", None)
    if not app_secret:
        logger.warning("MESSENGER_APP_SECRET not configured — webhook verification disabled")
        return True

    if not signature:
        logger.warning("Missing Messenger X-Hub-Signature header")
        return False

    expected_sig = hmac.new(
        app_secret.encode("utf-8"),
        body.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()

    try:
        algorithm, provided_sig = signature.split("=", 1)
        if algorithm != "sha256":
            logger.warning("Unsupported signature algorithm: %s", algorithm)
            return False

        if not hmac.compare_digest(expected_sig, provided_sig):
            logger.warning("Messenger webhook signature mismatch")
            return False
    except ValueError:
        logger.warning("Malformed Messenger signature")
        return False

    return True


def verify_whatsapp_signature(signature: str, body: str) -> bool:
    """Verify WhatsApp webhook signature from Meta."""
    app_secret = getattr(settings, "WHATSAPP_APP_SECRET", None)
    if not app_secret:
        logger.warning("WHATSAPP_APP_SECRET not configured — webhook verification disabled")
        return True

    if not signature:
        logger.warning("Missing WhatsApp X-Hub-Signature header")
        return False

    expected_sig = hmac.new(
        app_secret.encode("utf-8"),
        body.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()

    try:
        provided_sig = signature.split("=", 1)[1]
        if not hmac.compare_digest(expected_sig, provided_sig):
            logger.warning("WhatsApp webhook signature mismatch")
            return False
    except (IndexError, ValueError):
        logger.warning("Malformed WhatsApp signature")
        return False

    return True


def verify_generic_hmac_signature(
    signature: str,
    body: str,
    secret: Optional[str],
    header_format: str = "sha256=",
) -> bool:
    """Generic HMAC signature verification for custom webhook providers."""
    if not secret:
        logger.warning("Webhook secret not configured — verification disabled")
        return True

    if not signature:
        logger.warning("Missing webhook signature header")
        return False

    expected_sig = hmac.new(
        secret.encode("utf-8"),
        body.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()
    expected_sig = f"{header_format}{expected_sig}"

    if not hmac.compare_digest(expected_sig, signature):
        logger.warning("Webhook signature mismatch (generic HMAC)")
        return False

    return True
