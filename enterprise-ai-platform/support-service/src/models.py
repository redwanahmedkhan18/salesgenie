"""
Support Service Data Models & Schemas
Database models for Support Tickets, Ticket Notes, Ticket Assignments, and Live Chat Handoff.
"""

import uuid
from datetime import datetime, timezone
from typing import Optional, List
from pydantic import BaseModel, Field
from sqlalchemy import Column, String, Boolean, DateTime, Text, Integer, ForeignKey, Numeric, Enum
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum

from enterprise_ai_platform.common.models_base import (
    Base,
    UUIDPrimaryKeyMixin,
    TimestampMixin,
    TenantIsolationMixin,
)


class TicketStatus(str, enum.Enum):
    """Support ticket status values."""
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    PENDING = "pending"
    RESOLVED = "resolved"
    CLOSED = "closed"
    REOPENED = "reopened"


class TicketPriority(str, enum.Enum):
    """Support ticket priority levels."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"
    CRITICAL = "critical"


class TicketCategory(str, enum.Enum):
    """Support ticket categories."""
    BILLING = "billing"
    TECHNICAL = "technical"
    SALES = "sales"
    ACCOUNT = "account"
    FEATURE = "feature"
    BUG = "bug"
    GENERAL = "general"


class TicketSource(str, enum.Enum):
    """How the ticket was created."""
    WEB = "web"
    CHAT = "chat"
    EMAIL = "email"
    API = "api"
    PHONE = "phone"


class Ticket(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Support ticket representing a customer support request."""
    __tablename__ = "support_tickets"

    customer_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), nullable=False, index=True,
        comment="Reference to customer profile"
    )
    conversation_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), nullable=True, index=True,
        comment="Reference to conversation if from chat"
    )
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[str] = mapped_column(
        String(20), default=TicketStatus.OPEN.value, nullable=False, index=True
    )
    priority: Mapped[str] = mapped_column(
        String(20), default=TicketPriority.MEDIUM.value, nullable=False, index=True
    )
    category: Mapped[str] = mapped_column(
        String(20), default=TicketCategory.GENERAL.value, nullable=False, index=True
    )
    source: Mapped[str] = mapped_column(
        String(20), default=TicketSource.WEB.value, nullable=False
    )
    assigned_to: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), nullable=True, index=True,
        comment="Agent ID assigned to this ticket"
    )
    assigned_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    resolved_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    closed_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    resolution_notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    satisfaction_score: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, comment="1-5 rating")
    satisfaction_feedback: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    is_escalated: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    escalation_reason: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    metadata_json: Mapped[Optional[dict]] = mapped_column(JSONB, nullable=True)

    notes: Mapped[List["TicketNote"]] = relationship("TicketNote", back_populates="ticket")
    assignments: Mapped[List["TicketAssignment"]] = relationship("TicketAssignment", back_populates="ticket")
    handoff: Mapped[Optional["LiveHandoff"]] = relationship("LiveHandoff", back_populates="ticket", uselist=False)


class TicketNote(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Notes added to a support ticket by agents or customers."""
    __tablename__ = "ticket_notes"

    ticket_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("support_tickets.id", ondelete="CASCADE"),
        nullable=False, index=True
    )
    author_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), nullable=False,
        comment="User ID of note author"
    )
    author_type: Mapped[str] = mapped_column(
        String(20), default="agent", nullable=False,
        comment="agent, customer, system"
    )
    content: Mapped[str] = mapped_column(Text, nullable=False)
    is_internal: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    ticket: Mapped[Ticket] = relationship("Ticket", back_populates="notes")


class TicketAssignment(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """History of ticket assignments to support agents."""
    __tablename__ = "ticket_assignments"

    ticket_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("support_tickets.id", ondelete="CASCADE"),
        nullable=False, index=True
    )
    agent_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), nullable=False, index=True
    )
    assigned_by: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), nullable=False,
        comment="User ID of who assigned the ticket"
    )
    assigned_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False
    )
    unassigned_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    ticket: Mapped[Ticket] = relationship("Ticket", back_populates="assignments")


class LiveHandoff(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Live chat handoff from AI agent to human agent."""
    __tablename__ = "live_handoffs"

    ticket_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("support_tickets.id", ondelete="SET NULL"),
        nullable=True, index=True
    )
    conversation_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), nullable=False, index=True
    )
    customer_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), nullable=False, index=True
    )
    requested_by: Mapped[str] = mapped_column(
        String(20), nullable=False,
        comment="ai_agent, customer, system"
    )
    reason: Mapped[str] = mapped_column(Text, nullable=False)
    assigned_agent_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), nullable=True, index=True
    )
    accepted_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    declined_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    status: Mapped[str] = mapped_column(
        String(20), default="pending", nullable=False,
        comment="pending, accepted, declined, completed, timed_out"
    )
    timeout_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False,
        comment="When the handoff expires if not accepted"
    )

    ticket: Mapped[Optional[Ticket]] = relationship("Ticket", back_populates="handoff")


# -------------------------------------------------------------------
# Pydantic Schemas / DTOs
# -------------------------------------------------------------------

class TicketDTO(BaseModel):
    id: uuid.UUID
    customer_id: uuid.UUID
    conversation_id: Optional[uuid.UUID]
    title: str
    description: str
    status: str
    priority: str
    category: str
    source: str
    assigned_to: Optional[uuid.UUID]
    assigned_at: Optional[datetime]
    resolved_at: Optional[datetime]
    closed_at: Optional[datetime]
    resolution_notes: Optional[str]
    satisfaction_score: Optional[int]
    satisfaction_feedback: Optional[str]
    is_escalated: bool
    escalation_reason: Optional[str]
    tenant_id: uuid.UUID
    created_at: datetime
    updated_at: datetime


class CreateTicketRequest(BaseModel):
    customer_id: uuid.UUID
    conversation_id: Optional[uuid.UUID] = None
    title: str
    description: str
    priority: str = "medium"
    category: str = "general"
    source: str = "web"
    metadata_json: Optional[dict] = None


class UpdateTicketRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    category: Optional[str] = None
    assigned_to: Optional[uuid.UUID] = None
    resolution_notes: Optional[str] = None
    satisfaction_score: Optional[int] = None
    satisfaction_feedback: Optional[str] = None
    is_escalated: Optional[bool] = None
    escalation_reason: Optional[str] = None


class AssignTicketRequest(BaseModel):
    agent_id: uuid.UUID
    assigned_by: uuid.UUID


class TicketNoteDTO(BaseModel):
    id: uuid.UUID
    ticket_id: uuid.UUID
    author_id: uuid.UUID
    author_type: str
    content: str
    is_internal: bool
    created_at: datetime
    updated_at: datetime


class CreateNoteRequest(BaseModel):
    ticket_id: uuid.UUID
    content: str
    is_internal: bool = True


class LiveHandoffDTO(BaseModel):
    id: uuid.UUID
    ticket_id: Optional[uuid.UUID]
    conversation_id: uuid.UUID
    customer_id: uuid.UUID
    requested_by: str
    reason: str
    assigned_agent_id: Optional[uuid.UUID]
    accepted_at: Optional[datetime]
    declined_at: Optional[datetime]
    status: str
    timeout_at: datetime
    tenant_id: uuid.UUID
    created_at: datetime


class CreateHandoffRequest(BaseModel):
    conversation_id: uuid.UUID
    customer_id: uuid.UUID
    requested_by: str = "ai_agent"
    reason: str = "Customer requested human agent"


class TicketAnalyticsDTO(BaseModel):
    total_tickets: int
    open_tickets: int
    in_progress_tickets: int
    resolved_tickets: int
    closed_tickets: int
    avg_resolution_time_hours: float
    avg_satisfaction_score: float
    tickets_by_priority: dict
    tickets_by_category: dict
    escalation_rate: float