"""
Customer Service Data Models & Schemas
Database models for Customer Profiles, Segments, Tags, Notes, Orders, and Interaction Summaries.
"""

import uuid
from datetime import datetime, timezone
from typing import Optional, List
from pydantic import BaseModel, Field
from sqlalchemy import Column, String, Boolean, DateTime, Text, Integer, ForeignKey, Numeric
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from enterprise_ai_platform.common.models_base import (
    Base,
    UUIDPrimaryKeyMixin,
    TimestampMixin,
    TenantIsolationMixin,
)


class CustomerSegment(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Customer segmentation for targeted campaigns."""
    __tablename__ = "customer_segments"

    name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    color: Mapped[str] = mapped_column(String(7), default="#6b7280", nullable=False)  # hex color
    is_system: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    customers: Mapped[List["Customer"]] = relationship(
        "Customer",
        secondary="customer_segment_members",
        back_populates="segments",
    )


class CustomerSegmentMember(Base):
    """Association table for customer-segment many-to-many relationship."""
    __tablename__ = "customer_segment_members"

    customer_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("customers.id", ondelete="CASCADE"), primary_key=True
    )
    segment_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("customer_segments.id", ondelete="CASCADE"), primary_key=True
    )


class CustomerTag(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Customer tags for quick categorization."""
    __tablename__ = "customer_tags"

    name: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    color: Mapped[str] = mapped_column(String(7), default="#6b7280", nullable=False)

    customers: Mapped[List["Customer"]] = relationship(
        "Customer",
        secondary="customer_tag_members",
        back_populates="tags",
    )


class CustomerTagMember(Base):
    """Association table for customer-tag many-to-many relationship."""
    __tablename__ = "customer_tag_members"

    customer_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("customers.id", ondelete="CASCADE"), primary_key=True
    )
    tag_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("customer_tags.id", ondelete="CASCADE"), primary_key=True
    )


class Customer(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Customer profile - NOT a platform user. Customers interact with AI agents."""
    __tablename__ = "customers"

    email: Mapped[Optional[str]] = mapped_column(String(255), nullable=True, index=True)
    phone_number: Mapped[Optional[str]] = mapped_column(String(30), nullable=True, index=True)
    full_name: Mapped[str] = mapped_column(String(150), nullable=False)
    company_name: Mapped[Optional[str]] = mapped_column(String(150), nullable=True)
    avatar_url: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    job_title: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    lead_status: Mapped[str] = mapped_column(
        String(30), default="cold", nullable=False,
        comment="cold, warm, hot, qualified, converted, churned"
    )
    lead_score: Mapped[int] = mapped_column(Integer, default=0, nullable=False, comment="0-100")
    lifetime_value: Mapped[Numeric] = mapped_column(Numeric(12, 2), default=0, nullable=False)
    total_orders: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    last_interaction_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    metadata_json: Mapped[Optional[dict]] = mapped_column(JSONB, nullable=True)

    segments: Mapped[List[CustomerSegment]] = relationship(
        "CustomerSegment",
        secondary="customer_segment_members",
        back_populates="customers",
    )
    tags: Mapped[List[CustomerTag]] = relationship(
        "CustomerTag",
        secondary="customer_tag_members",
        back_populates="customers",
    )
    orders: Mapped[List["CustomerOrder"]] = relationship("CustomerOrder", back_populates="customer")
    notes: Mapped[List["CustomerNote"]] = relationship("CustomerNote", back_populates="customer")
    interaction_summary: Mapped[Optional["CustomerInteractionSummary"]] = relationship(
        "CustomerInteractionSummary", back_populates="customer", uselist=False
    )


class CustomerNote(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Internal notes about a customer."""
    __tablename__ = "customer_notes"

    customer_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("customers.id", ondelete="CASCADE"), nullable=False, index=True
    )
    author_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), nullable=False, comment="User ID of note author"
    )
    content: Mapped[str] = mapped_column(Text, nullable=False)
    is_internal: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    customer: Mapped[Customer] = relationship("Customer", back_populates="notes")


class CustomerOrder(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Customer purchase history."""
    __tablename__ = "customer_orders"

    customer_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("customers.id", ondelete="CASCADE"), nullable=False, index=True
    )
    order_number: Mapped[str] = mapped_column(String(50), nullable=False, unique=True, index=True)
    amount: Mapped[Numeric] = mapped_column(Numeric(12, 2), nullable=False)
    currency: Mapped[str] = mapped_column(String(3), default="USD", nullable=False)
    status: Mapped[str] = mapped_column(
        String(20), default="pending", nullable=False,
        comment="pending, paid, refunded, cancelled"
    )
    product_name: Mapped[Optional[str]] = mapped_column(String(150), nullable=True)
    metadata_json: Mapped[Optional[dict]] = mapped_column(JSONB, nullable=True)

    customer: Mapped[Customer] = relationship("Customer", back_populates="orders")


class CustomerInteractionSummary(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """AI-generated summary of customer interactions."""
    __tablename__ = "customer_interaction_summaries"

    customer_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("customers.id", ondelete="CASCADE"), nullable=False, unique=True, index=True
    )
    summary_text: Mapped[str] = mapped_column(Text, nullable=False)
    sentiment: Mapped[str] = mapped_column(String(20), default="neutral", nullable=False)
    key_topics: Mapped[Optional[List[str]]] = mapped_column(JSONB, nullable=True)
    last_conversation_id: Mapped[Optional[uuid.UUID]] = mapped_column(UUID(as_uuid=True), nullable=True)

    customer: Mapped[Customer] = relationship("Customer", back_populates="interaction_summary")


# -------------------------------------------------------------------
# Pydantic Schemas / DTOs
# -------------------------------------------------------------------

class CustomerDTO(BaseModel):
    id: uuid.UUID
    email: Optional[str]
    phone_number: Optional[str]
    full_name: str
    company_name: Optional[str]
    avatar_url: Optional[str]
    job_title: Optional[str]
    lead_status: str
    lead_score: int
    lifetime_value: float
    total_orders: int
    last_interaction_at: Optional[datetime]
    is_active: bool
    tenant_id: uuid.UUID
    created_at: datetime
    segments: List[str] = Field(default_factory=list)
    tags: List[str] = Field(default_factory=list)


class CreateCustomerRequest(BaseModel):
    email: Optional[str] = None
    phone_number: Optional[str] = None
    full_name: str
    company_name: Optional[str] = None
    avatar_url: Optional[str] = None
    job_title: Optional[str] = None
    lead_status: str = "cold"
    lead_score: int = 0
    segment_ids: List[uuid.UUID] = Field(default_factory=list)
    tag_ids: List[uuid.UUID] = Field(default_factory=list)


class UpdateCustomerRequest(BaseModel):
    email: Optional[str] = None
    phone_number: Optional[str] = None
    full_name: Optional[str] = None
    company_name: Optional[str] = None
    avatar_url: Optional[str] = None
    job_title: Optional[str] = None
    lead_status: Optional[str] = None
    lead_score: Optional[int] = None
    is_active: Optional[bool] = None
    segment_ids: Optional[List[uuid.UUID]] = None
    tag_ids: Optional[List[uuid.UUID]] = None


class CustomerSegmentDTO(BaseModel):
    id: uuid.UUID
    name: str
    description: Optional[str]
    color: str
    is_system: bool
    customer_count: int = 0
    tenant_id: uuid.UUID
    created_at: datetime


class CreateSegmentRequest(BaseModel):
    name: str
    description: Optional[str] = None
    color: str = "#6b7280"


class CustomerTagDTO(BaseModel):
    id: uuid.UUID
    name: str
    color: str
    customer_count: int = 0
    tenant_id: uuid.UUID
    created_at: datetime


class CreateTagRequest(BaseModel):
    name: str
    color: str = "#6b7280"


class CustomerNoteDTO(BaseModel):
    id: uuid.UUID
    customer_id: uuid.UUID
    author_id: uuid.UUID
    content: str
    is_internal: bool
    created_at: datetime
    updated_at: datetime


class CreateNoteRequest(BaseModel):
    customer_id: uuid.UUID
    content: str
    is_internal: bool = True


class CustomerOrderDTO(BaseModel):
    id: uuid.UUID
    customer_id: uuid.UUID
    order_number: str
    amount: float
    currency: str
    status: str
    product_name: Optional[str]
    created_at: datetime


class CustomerHistoryDTO(BaseModel):
    customer: CustomerDTO
    notes: List[CustomerNoteDTO] = Field(default_factory=list)
    orders: List[CustomerOrderDTO] = Field(default_factory=list)
    interaction_summary: Optional[str] = None