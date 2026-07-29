"""
Organization Service Data Models & Schemas
Database models for Organization Workspaces, Branding, Tenant Metrics, and Member Subscriptions.
"""

import uuid
from datetime import datetime, timezone
from typing import Optional, List
from pydantic import BaseModel, Field, HttpUrl
from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column

from enterprise_ai_platform.common.models_base import (
    Base,
    UUIDPrimaryKeyMixin,
    TimestampMixin,
    SoftDeleteMixin,
    TenantIsolationMixin,
)


class OrganizationWorkspace(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin):
    """Multi-tenant organization workspace entity."""
    __tablename__ = "org_workspaces"

    name: Mapped[str] = mapped_column(String(150), nullable=False, index=True)
    slug: Mapped[str] = mapped_column(String(100), nullable=False, unique=True, index=True)
    domain: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    subscription_tier: Mapped[str] = mapped_column(String(50), default="growth", nullable=False)  # starter, growth, enterprise
    max_seats: Mapped[int] = mapped_column(Integer, default=10, nullable=False)
    max_monthly_tokens: Mapped[int] = mapped_column(Integer, default=5000000, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)


class TenantMetrics(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Real-time performance and usage metrics tracked per tenant organization."""
    __tablename__ = "org_tenant_metrics"

    total_conversations: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    active_conversations: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    total_tokens_used: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    ai_cost_usd: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    ai_accuracy_rate: Mapped[float] = mapped_column(Float, default=98.5, nullable=False)
    hallucination_rate: Mapped[float] = mapped_column(Float, default=0.4, nullable=False)
    sales_conversion_rate: Mapped[float] = mapped_column(Float, default=14.2, nullable=False)


class OrganizationBranding(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """White-label custom styling and branding preferences."""
    __tablename__ = "org_branding"

    primary_color: Mapped[str] = mapped_column(String(20), default="#f7a501", nullable=False)
    secondary_color: Mapped[str] = mapped_column(String(20), default="#23251d", nullable=False)
    logo_url: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    favicon_url: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    custom_domain: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    is_white_label_enabled: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)


class WorkspaceMember(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Mapping of users to workspace membership and roles."""
    __tablename__ = "org_workspace_members"

    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False, index=True)
    role: Mapped[str] = mapped_column(String(50), default="support_agent", nullable=False)
    status: Mapped[str] = mapped_column(String(30), default="active", nullable=False)  # active, suspended, pending


# -------------------------------------------------------------------
# Pydantic DTO Schemas
# -------------------------------------------------------------------

class CreateOrganizationRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=150)
    slug: str = Field(..., min_length=2, max_length=100)
    domain: Optional[str] = None
    subscription_tier: Optional[str] = "growth"


class OrganizationDTO(BaseModel):
    id: uuid.UUID
    name: str
    slug: str
    domain: Optional[str]
    subscription_tier: str
    max_seats: int
    max_monthly_tokens: int
    is_active: bool
    created_at: datetime


class UpdateBrandingRequest(BaseModel):
    primary_color: Optional[str] = None
    secondary_color: Optional[str] = None
    logo_url: Optional[str] = None
    favicon_url: Optional[str] = None
    custom_domain: Optional[str] = None
    is_white_label_enabled: Optional[bool] = None


class BrandingDTO(BaseModel):
    tenant_id: uuid.UUID
    primary_color: str
    secondary_color: str
    logo_url: Optional[str]
    custom_domain: Optional[str]
    is_white_label_enabled: bool


class TenantMetricsDTO(BaseModel):
    tenant_id: uuid.UUID
    total_conversations: int
    active_conversations: int
    total_tokens_used: int
    ai_cost_usd: float
    ai_accuracy_rate: float
    hallucination_rate: float
    sales_conversion_rate: float


class WorkspaceMemberDTO(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    role: str
    status: str
    created_at: datetime


class AddMemberRequest(BaseModel):
    user_id: str
    role: str = "support_agent"


class UpdateMemberRoleRequest(BaseModel):
    role: str
