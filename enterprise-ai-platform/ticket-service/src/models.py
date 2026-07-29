"""
Ticket Service Data Models & Schemas
Database models for Customer Tickets, Ticket Messages, State Audit Logs, Refunds, and Shipment Tracking.
"""

import uuid
from enum import Enum
from datetime import datetime, timezone
from typing import Optional, List
from pydantic import BaseModel, Field
from sqlalchemy import Column, String, Float, Integer, Boolean, DateTime, Text, Enum as SQLEnum
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column

from enterprise_ai_platform.common.models_base import (
    Base,
    UUIDPrimaryKeyMixin,
    TimestampMixin,
    TenantIsolationMixin,
)


class TicketStatus(str, Enum):
    NEW = "new"
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    PENDING_CUSTOMER = "pending_customer"
    ESCALATED = "escalated"
    RESOLVED = "resolved"
    CLOSED = "closed"


class TicketPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class TicketCategory(str, Enum):
    BILLING = "billing"
    TECHNICAL_SUPPORT = "technical_support"
    ORDER_REFUND = "order_refund"
    SHIPMENT_TRACKING = "shipment_tracking"
    GENERAL_INQUIRY = "general_inquiry"


class Ticket(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Customer support ticket entity with SLA tracking and AI handoff metrics."""
    __tablename__ = "tickets"

    ticket_number: Mapped[str] = mapped_column(String(50), nullable=False, unique=True, index=True)
    customer_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False, index=True)
    assigned_agent_id: Mapped[Optional[uuid.UUID]] = mapped_column(UUID(as_uuid=True), nullable=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Text] = mapped_column(Text, nullable=False)
    status: Mapped[TicketStatus] = mapped_column(SQLEnum(TicketStatus), default=TicketStatus.NEW, nullable=False, index=True)
    priority: Mapped[TicketPriority] = mapped_column(SQLEnum(TicketPriority), default=TicketPriority.MEDIUM, nullable=False)
    category: Mapped[TicketCategory] = mapped_column(SQLEnum(TicketCategory), default=TicketCategory.GENERAL_INQUIRY, nullable=False)
    ai_confidence_score: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    is_escalated: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    tags: Mapped[dict] = mapped_column(JSONB, default=list, nullable=False)


class TicketMessage(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Messages and internal notes associated with a ticket."""
    __tablename__ = "ticket_messages"

    ticket_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False, index=True)
    sender_type: Mapped[str] = mapped_column(String(20), nullable=False)  # 'customer', 'ai_agent', 'human_agent'
    sender_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    is_internal_note: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    attachments: Mapped[dict] = mapped_column(JSONB, default=list, nullable=False)


class RefundRequest(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Tracks customer refund requests and AI auto-approval workflows."""
    __tablename__ = "ticket_refund_requests"

    ticket_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False, index=True)
    order_id: Mapped[str] = mapped_column(String(100), nullable=False)
    amount_usd: Mapped[float] = mapped_column(Float, nullable=False)
    reason: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[str] = mapped_column(String(30), default="pending_review", nullable=False)  # pending_review, approved, rejected


class ShipmentTracking(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """External shipment tracking cache for customer orders."""
    __tablename__ = "ticket_shipment_tracking"

    order_id: Mapped[str] = mapped_column(String(100), nullable=False, unique=True, index=True)
    carrier: Mapped[str] = mapped_column(String(50), nullable=False)  # 'FedEx', 'UPS', 'DHL'
    tracking_number: Mapped[str] = mapped_column(String(100), nullable=False)
    current_status: Mapped[str] = mapped_column(String(100), nullable=False)
    estimated_delivery: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)


# -------------------------------------------------------------------
# Pydantic Schemas / DTOs
# -------------------------------------------------------------------

class CreateTicketRequest(BaseModel):
    title: str = Field(..., min_length=3, max_length=255)
    description: str
    category: TicketCategory
    priority: Optional[TicketPriority] = TicketPriority.MEDIUM
    customer_id: str


class TicketDTO(BaseModel):
    id: uuid.UUID
    ticket_number: str
    customer_id: uuid.UUID
    assigned_agent_id: Optional[uuid.UUID]
    title: str
    description: str
    status: TicketStatus
    priority: TicketPriority
    category: TicketCategory
    ai_confidence_score: float
    is_escalated: bool
    tags: List[str]
    created_at: datetime


class TransferTicketRequest(BaseModel):
    target_agent_id: str
    transfer_reason: Optional[str] = None


class RefundRequestDTO(BaseModel):
    id: uuid.UUID
    ticket_id: uuid.UUID
    order_id: str
    amount_usd: float
    reason: str
    status: str
    created_at: datetime
