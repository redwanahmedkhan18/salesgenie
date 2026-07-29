"""
Auth Service Data Models & Schemas
Database models for User Sessions, Devices, MFA Secrets, OAuth Accounts, and Invitations.
"""

import uuid
from datetime import datetime, timezone
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from enterprise_ai_platform.common.models_base import (
    Base,
    UUIDPrimaryKeyMixin,
    TimestampMixin,
    TenantIsolationMixin,
)
from enterprise_ai_platform.common.security_rbac import PlatformRole


# -------------------------------------------------------------------
# SQLAlchemy Database Models
# -------------------------------------------------------------------

class UserSession(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Tracks active user sessions across web and mobile devices."""
    __tablename__ = "auth_user_sessions"

    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False, index=True)
    refresh_token_hash: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    device_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    ip_address: Mapped[Optional[str]] = mapped_column(String(45), nullable=True)
    user_agent: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)


class UserDevice(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Tracks trusted devices registered for Multi-Factor Authentication."""
    __tablename__ = "auth_user_devices"

    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False, index=True)
    device_identifier: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    device_type: Mapped[str] = mapped_column(String(50), nullable=False)  # 'web', 'ios', 'android'
    is_trusted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    last_used_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)


class MFASecret(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Stores TOTP secret keys and backup recovery codes for users."""
    __tablename__ = "auth_mfa_secrets"

    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False, unique=True, index=True)
    secret_key: Mapped[str] = mapped_column(String(255), nullable=False)
    is_enabled: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    backup_codes: Mapped[dict] = mapped_column(JSONB, default=list, nullable=False)


class WorkspaceInvitation(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Manages organization workspace email invitations."""
    __tablename__ = "auth_workspace_invitations"

    email: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    role: Mapped[str] = mapped_column(String(50), default=PlatformRole.SUPPORT_AGENT.value, nullable=False)
    invited_by_user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    token: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
    status: Mapped[str] = mapped_column(String(30), default="pending", nullable=False)  # pending, accepted, expired
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)


class OAuthAccount(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Links user accounts with social OAuth2 providers (Google, Microsoft, GitHub)."""
    __tablename__ = "auth_oauth_accounts"

    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False, index=True)
    provider: Mapped[str] = mapped_column(String(50), nullable=False)  # 'google', 'microsoft', 'github'
    provider_user_id: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    access_token: Mapped[str] = mapped_column(Text, nullable=False)
    refresh_token: Mapped[Optional[str]] = mapped_column(Text, nullable=True)


# -------------------------------------------------------------------
# Pydantic Schemas / DTOs
# -------------------------------------------------------------------

class LoginRequest(BaseModel):
    email: EmailStr
    password: str
    tenant_id: Optional[str] = "default_tenant"
    mfa_code: Optional[str] = None


class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "Bearer"
    expires_in: int
    user_id: str
    roles: List[str]
    tenant_id: str
    mfa_required: bool = False


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class MFASetupResponse(BaseModel):
    secret_key: str
    qr_code_uri: str
    backup_codes: List[str]


class MFAVerifyRequest(BaseModel):
    code: str


class SessionDTO(BaseModel):
    id: uuid.UUID
    device_name: Optional[str]
    ip_address: Optional[str]
    user_agent: Optional[str]
    created_at: datetime
    is_active: bool


class CreateInvitationRequest(BaseModel):
    email: EmailStr
    role: PlatformRole
    tenant_id: str


class InvitationDTO(BaseModel):
    id: uuid.UUID
    email: EmailStr
    role: str
    tenant_id: str
    status: str
    created_at: datetime
    expires_at: datetime
