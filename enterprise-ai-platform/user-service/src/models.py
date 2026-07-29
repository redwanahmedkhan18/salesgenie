"""
User Service Data Models & Schemas
Database models for User Profiles, Preferences, and Role Assignments.
"""

import uuid
from datetime import datetime, timezone
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import Column, String, Boolean, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column

from enterprise_ai_platform.common.models_base import (
    Base,
    UUIDPrimaryKeyMixin,
    TimestampMixin,
    TenantIsolationMixin,
)


class UserProfile(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """User account details, email, and display avatar."""
    __tablename__ = "user_profiles"

    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
    full_name: Mapped[str] = mapped_column(String(150), nullable=False)
    phone_number: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    avatar_url: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    job_title: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    department: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)


class UserPreferences(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """User interface, notification, and language settings."""
    __tablename__ = "user_preferences"

    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False, unique=True, index=True)
    theme: Mapped[str] = mapped_column(String(20), default="dark", nullable=False)  # 'light', 'dark', 'system'
    language: Mapped[str] = mapped_column(String(10), default="en", nullable=False)
    email_notifications: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    slack_notifications: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    keyboard_shortcuts: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)


# -------------------------------------------------------------------
# Pydantic Schemas / DTOs
# -------------------------------------------------------------------

class UserProfileDTO(BaseModel):
    id: uuid.UUID
    email: EmailStr
    full_name: str
    phone_number: Optional[str]
    avatar_url: Optional[str]
    job_title: Optional[str]
    department: Optional[str]
    tenant_id: uuid.UUID
    is_active: bool
    created_at: datetime


class UpdateProfileRequest(BaseModel):
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    avatar_url: Optional[str] = None
    job_title: Optional[str] = None
    department: Optional[str] = None


class UserPreferencesDTO(BaseModel):
    user_id: uuid.UUID
    theme: str
    language: str
    email_notifications: bool
    slack_notifications: bool
    keyboard_shortcuts: bool


class UpdatePreferencesRequest(BaseModel):
    theme: Optional[str] = None
    language: Optional[str] = None
    email_notifications: Optional[bool] = None
    slack_notifications: Optional[bool] = None
    keyboard_shortcuts: Optional[bool] = None
