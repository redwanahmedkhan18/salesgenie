"""
JWT Security Token Handler
Handles access & refresh token encoding, validation, and session claim enrichment.
"""

import hashlib
import uuid
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Any, Optional
import jwt

from enterprise_ai_platform.common.config import settings
from enterprise_ai_platform.common.security_rbac import PlatformRole


def create_access_token(
    user_id: str,
    tenant_id: str,
    email: str,
    roles: List[str],
    session_id: Optional[str] = None,
    expires_delta: Optional[timedelta] = None,
) -> str:
    """Creates signed JWT Access Token with tenant isolation claims and platform roles."""
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    payload: Dict[str, Any] = {
        "sub": str(user_id),
        "tenant_id": str(tenant_id),
        "email": email,
        "roles": roles,
        "session_id": session_id or str(uuid.uuid4()),
        "iss": settings.PROJECT_NAME,
        "exp": int(expire.timestamp()),
        "iat": int(datetime.now(timezone.utc).timestamp()),
    }

    encoded_jwt = jwt.encode(
        payload,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )
    return encoded_jwt


def create_refresh_token(
    user_id: str,
    tenant_id: str,
    session_id: str,
) -> str:
    """Creates signed JWT Refresh Token for session continuation."""
    expire = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    payload = {
        "sub": str(user_id),
        "tenant_id": str(tenant_id),
        "session_id": session_id,
        "type": "refresh",
        "exp": int(expire.timestamp()),
    }
    return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


def hash_token(token: str) -> str:
    """SHA-256 token hashing for safe session verification in database."""
    return hashlib.sha256(token.encode('utf-8')).hexdigest()
