"""
Sales Service Data Models & Schemas
Database models for Leads, Sales Pipeline Deals, Product Catalog, Coupons, and Calendar Bookings.
"""

import uuid
from datetime import datetime, timezone
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import Column, String, Float, Integer, Boolean, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column

from enterprise_ai_platform.common.models_base import (
    Base,
    UUIDPrimaryKeyMixin,
    TimestampMixin,
    TenantIsolationMixin,
)


class Lead(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Qualified sales lead entity with AI lead score and BANT metrics."""
    __tablename__ = "sales_leads"

    email: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    full_name: Mapped[str] = mapped_column(String(150), nullable=False)
    company: Mapped[Optional[str]] = mapped_column(String(150), nullable=True)
    phone: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    lead_score: Mapped[int] = mapped_column(Integer, default=0, nullable=False, index=True)  # 0 to 100
    status: Mapped[str] = mapped_column(String(30), default="new", nullable=False)  # 'new', 'qualified', 'contacted', 'disqualified'
    budget_usd: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    timeline: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)


class Deal(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Sales pipeline opportunity deal stage entity."""
    __tablename__ = "sales_deals"

    title: Mapped[str] = mapped_column(String(200), nullable=False)
    lead_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False, index=True)
    value_usd: Mapped[float] = mapped_column(Float, nullable=False)
    pipeline_stage: Mapped[str] = mapped_column(String(50), default="discovery", nullable=False)  # discovery, demo, proposal, negotiation, won, lost
    probability: Mapped[float] = mapped_column(Float, default=0.2, nullable=False)


class ProductCatalog(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Product catalog item entity for AI sales recommendation engines."""
    __tablename__ = "sales_products"

    sku: Mapped[str] = mapped_column(String(100), nullable=False, unique=True, index=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    category: Mapped[str] = mapped_column(String(100), nullable=False)
    price_usd: Mapped[float] = mapped_column(Float, nullable=False)
    description: Mapped[Text] = mapped_column(Text, nullable=False)
    inventory_count: Mapped[int] = mapped_column(Integer, default=100, nullable=False)


class Coupon(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Promotional discount coupons distributed during sales conversations."""
    __tablename__ = "sales_coupons"

    code: Mapped[str] = mapped_column(String(50), nullable=False, unique=True, index=True)
    discount_percent: Mapped[float] = mapped_column(Float, nullable=False)
    max_uses: Mapped[int] = mapped_column(Integer, default=500, nullable=False)
    current_uses: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)


class CalendarBooking(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Automated sales demo meeting booking schedules."""
    __tablename__ = "sales_calendar_bookings"

    lead_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False, index=True)
    sales_rep_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    meeting_title: Mapped[str] = mapped_column(String(200), nullable=False)
    start_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    end_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    meeting_link: Mapped[str] = mapped_column(Text, nullable=False)


# -------------------------------------------------------------------
# Pydantic Schemas / DTOs
# -------------------------------------------------------------------

class CreateLeadRequest(BaseModel):
    email: EmailStr
    full_name: str
    company: Optional[str] = None
    phone: Optional[str] = None
    budget_usd: Optional[float] = None
    timeline: Optional[str] = None


class LeadDTO(BaseModel):
    id: uuid.UUID
    email: EmailStr
    full_name: str
    company: Optional[str]
    lead_score: int
    status: str
    budget_usd: Optional[float]
    created_at: datetime


class ProductRecommendationDTO(BaseModel):
    product_id: uuid.UUID
    sku: str
    name: str
    category: str
    price_usd: float
    recommendation_reason: str
    upsell_discount_offer: Optional[str] = None


class BookMeetingRequest(BaseModel):
    lead_id: str
    sales_rep_id: str
    start_time: datetime
    duration_minutes: Optional[int] = 30
