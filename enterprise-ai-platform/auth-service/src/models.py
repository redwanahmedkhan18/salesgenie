"""
Auth Service Data Models & Schemas
Database models for User Sessions, Devices, MFA Secrets, OAuth Accounts, and Invitations.
"""

import uuid
from datetime import datetime, timezone
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Text, func, text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from passlib.hash import bcrypt

from enterprise_ai_platform.common.models_base import (
    Base,
    UUIDPrimaryKeyMixin,
    TimestampMixin,
    TenantIsolationMixin,
)
from enterprise_ai_platform.common.security_rbac import PlatformRole


class User(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Registered user account with bcrypt-hashed password and unique email."""
    __tablename__ = "auth_users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    organization_id: Mapped[Optional[uuid.UUID]] = mapped_column(UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    company: Mapped[str] = mapped_column(String(255), nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    def set_password(self, plaintext: str) -> None:
        self.password_hash = bcrypt.hash(plaintext)

    def verify_password(self, plaintext: str) -> bool:
        return bcrypt.verify(plaintext, self.password_hash)


class Organization(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Organization entity for multi-tenant support."""
    __tablename__ = "organizations"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    domain: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    plan_tier: Mapped[str] = mapped_column(String(50), default="starter", nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)


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


class UserVerificationToken(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Store email verification tokens for new user accounts."""
    __tablename__ = "auth_user_verification_tokens"

    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False, unique=True, index=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    token: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)


class PasswordResetToken(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Stores password reset tokens for users who forgot their passwords."""
    __tablename__ = "auth_password_reset_tokens"

    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False, unique=True, index=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    token: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    is_used: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)


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


class SignupRequest(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    company: str


class SignupResponse(BaseModel):
    status: str
    message: str
    requires_verification: bool = False


class ForgotPasswordRequest(BaseModel):
    email: EmailStr


class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str
    confirm_password: str
