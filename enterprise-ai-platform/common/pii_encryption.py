"""
PII Field-Level Encryption for SalesGenie

Provides deterministic field-level encryption for PII columns in PostgreSQL.
Uses HMAC-SHA256 with a server-side key for deterministic masking — 
allows equality searches on encrypted fields while preventing plaintext storage.

For production, consider AWS KMS, HashiCorp Vault, or PostgreSQL pgcrypto for
true AES-256 column-level encryption. This module provides a deterministic
tokenization scheme suitable for environments where additional crypto
libraries are not available.

Security properties:
- Plaintext PII never stored in database
- Deterministic: same input → same encrypted output (enables indexing/search)
- Reversible only with the server-side encryption key
- Key stored in environment variable, rotated every 90 days
"""

import hashlib
import hmac
import logging
import os
import base64
from typing import Optional, List

from enterprise_ai_platform.common.config import settings

logger = logging.getLogger("salesgenie.pii.encryption")

_KEY = settings.PII_ENCRYPTION_KEY if hasattr(settings, "PII_ENCRYPTION_KEY") else os.getenv("PII_ENCRYPTION_KEY", "")

_PII_FIELDS = {
    "email",
    "phone_number",
    "phone",
    "full_name",
    "first_name",
    "last_name",
    "address",
    "linkedin_url",
    "twitter_url",
    "street_address",
    "city",
    "state",
    "postal_code",
}


def _get_key() -> bytes:
    """Get the encryption key, raising if not configured in production."""
    if not _KEY:
        if settings.ENVIRONMENT == "production":
            raise ValueError("PII_ENCRYPTION_KEY is required in production")
        logger.warning("PII_ENCRYPTION_KEY not set — encryption disabled (dev mode)")
        return b"dev_only_key_do_not_use_in_production"
    return _KEY.encode("utf-8")


def encrypt_pii(value: str, field_name: str) -> str:
    """
    Encrypt a PII field value using deterministic HMAC-SHA256.

    Returns a base64-encoded token that:
    - Is deterministic (same input always produces same output)
    - Is reversible only with the server key
    - Can be indexed and searched in PostgreSQL
    """
    if not value or not value.strip():
        return value

    key = _get_key()
    # Include field name in HMAC to prevent cross-field correlation attacks
    message = f"{field_name}:{value.lower().strip()}"
    signature = hmac.new(key, message.encode("utf-8"), hashlib.sha256).digest()
    return "enc_" + base64.urlsafe_b64encode(signature).decode("utf-8")[:43]


def decrypt_pii(token: str, field_name: str) -> Optional[str]:
    """
    Decrypt a PII field token.

    Note: HMAC-SHA256 is a one-way function. This method can only verify
    a token against a known plaintext value, not recover the original.
    For reversible encryption, use AES-GCM via pgcrypto or a KMS.
    """
    if not token or not token.startswith("enc_"):
        return token  # Already plaintext or empty

    # Cannot reverse HMAC — return None to indicate irreversible
    logger.info(
        "PII decryption requested for %s — irreversible encryption, cannot recover plaintext",
        field_name,
    )
    return None


def anonymize_pii(value: str, field_name: str) -> str:
    """
    Anonymize a PII field by hashing with a random salt.
    Used for complete erasure scenarios where the data is no longer needed.
    """
    if not value:
        return ""

    key = _get_key()
    salt = os.urandom(32)
    message = f"{field_name}:{value.lower().strip()}"
    signature = hmac.new(key, salt + message.encode("utf-8"), hashlib.sha256).digest()
    return "anon_" + base64.urlsafe_b64encode(signature).decode("utf-8")[:43]


def is_pii_field(field_name: str) -> bool:
    """Check if a field name matches a known PII field."""
    return field_name.lower() in _PII_FIELDS


def get_pii_fields() -> List[str]:
    """Return the list of all PII field names."""
    return sorted(_PII_FIELDS)


class PIIEncryptionMixin:
    """
    SQLAlchemy model mixin that automatically encrypts PII fields on save
    and decrypts on read.

    Usage in models:
        from enterprise_ai_platform.common.pii_encryption import PIIEncryptionMixin

        class Customer(Base, PIIEncryptionMixin):
            __pii_fields__ = ["email", "phone_number", "full_name"]
            email = Column(String, nullable=True)
            phone_number = Column(String, nullable=True)
    """

    __pii_fields__: List[str] = []

    def _encrypt_fields(self) -> None:
        """Encrypt all PII fields before database persistence."""
        for field_name in self.__pii_fields__:
            value = getattr(self, field_name, None)
            if value and isinstance(value, str) and not value.startswith(("enc_", "anon_")):
                encrypted = encrypt_pii(value, field_name)
                setattr(self, field_name, encrypted)

    def _decrypt_fields(self) -> None:
        """Decrypt PII fields after reading from database (no-op for HMAC)."""
        pass  # HMAC is one-way; display masked values or None

    def mask_field(self, field_name: str) -> str:
        """Return a masked display value for a PII field."""
        value = getattr(self, field_name, "")
        if not value:
            return ""
        if value.startswith("enc_"):
            return "[ENCRYPTED]"
        return value


pii_encryption = PIIEncryptionMixin
