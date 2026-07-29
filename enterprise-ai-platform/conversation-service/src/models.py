"""
Conversation Service Data Models & Schemas
Conversation and message models with AI agent integration.
"""

import uuid
from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
import enum

from enterprise_ai_platform.common.models_base import (
    Base,
    UUIDPrimaryKeyMixin,
    TimestampMixin,
    TenantIsolationMixin,
)
from sqlalchemy import Column, String, Boolean, Text, Integer, ForeignKey, JSON, Float
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column


class ConversationStatus(str, enum.Enum):
    """Status of a conversation."""
    ACTIVE = "active"
    PAUSED = "paused"
    RESOLVED = "resolved"
    CLOSED = "closed"


class MessageRole(str, enum.Enum):
    """Role of a message sender."""
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"
    AGENT = "agent"


class MessageStatus(str, enum.Enum):
    """Status of a message."""
    SENDING = "sending"
    SENT = "sent"
    DELIVERED = "delivered"
    READ = "read"
    FAILED = "failed"


class ConversationChannel(str, enum.Enum):
    """Channel type for conversation."""
    WEB = "web"
    MOBILE = "mobile"
    API = "api"
    EMAIL = "email"
    SLACK = "slack"
    DISCORD = "discord"


class Conversation(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Conversation session with a customer or user."""
    __tablename__ = "conversations"

    title: Mapped[Optional[str]] = mapped_column(
        String(255), nullable=True,
        comment="Title/summary of the conversation"
    )
    status: Mapped[str] = mapped_column(
        String(20), nullable=False, default="active",
        comment="Status of the conversation"
    )
    channel: Mapped[str] = mapped_column(
        String(20), nullable=False, default="web",
        comment="Channel type"
    )
    customer_id: Mapped[Optional[str]] = mapped_column(
        String(100), nullable=True, index=True,
        comment="ID of the customer in this conversation"
    )
    agent_id: Mapped[Optional[str]] = mapped_column(
        String(100), nullable=True, index=True,
        comment="ID of the AI agent handling this conversation"
    )
    assigned_to: Mapped[Optional[str]] = mapped_column(
        String(100), nullable=True, index=True,
        comment="ID of the human agent assigned to this conversation"
    )
    initiated_by: Mapped[str] = mapped_column(
        String(20), nullable=False, default="user",
        comment="Who initiated the conversation: user, agent, system"
    )
    source_url: Mapped[Optional[str]] = mapped_column(
        Text, nullable=True,
        comment="Source URL if web-based"
    )
    metadata_json: Mapped[Optional[dict]] = mapped_column(
        JSONB, nullable=True,
        comment="Additional conversation metadata"
    )
    tags: Mapped[Optional[List[str]]] = mapped_column(
        JSONB, nullable=True,
        comment="Tags for the conversation"
    )
    message_count: Mapped[int] = mapped_column(
        Integer, default=0, nullable=False,
        comment="Total number of messages in the conversation"
    )
    last_message_at: Mapped[Optional[datetime]] = mapped_column(
        nullable=True,
        comment="Timestamp of the last message"
    )
    last_message_preview: Mapped[Optional[str]] = mapped_column(
        Text, nullable=True,
        comment="Preview text of the last message"
    )
    resolved_at: Mapped[Optional[datetime]] = mapped_column(
        nullable=True,
        comment="When the conversation was resolved"
    )
    satisfaction_score: Mapped[Optional[float]] = mapped_column(
        Float, nullable=True,
        comment="Customer satisfaction score (1-5)"
    )
    satisfaction_feedback: Mapped[Optional[str]] = mapped_column(
        Text, nullable=True,
        comment="Customer satisfaction feedback text"
    )
    is_handoff: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False,
        comment="Whether this conversation was handed off to a human"
    )
    handoff_reason: Mapped[Optional[str]] = mapped_column(
        Text, nullable=True,
        comment="Reason for handoff if applicable"
    )
    handoff_at: Mapped[Optional[datetime]] = mapped_column(
        nullable=True,
        comment="When the conversation was handed off"
    )
    handoff_to: Mapped[Optional[str]] = mapped_column(
        String(100), nullable=True,
        comment="ID of the human agent handed off to"
    )
    duration_seconds: Mapped[Optional[int]] = mapped_column(
        Integer, nullable=True,
        comment="Duration of the conversation in seconds"
    )


class Message(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Individual message within a conversation."""
    __tablename__ = "messages"

    conversation_id: Mapped[str] = mapped_column(
        String(100), nullable=False, index=True,
        comment="ID of the conversation this message belongs to"
    )
    role: Mapped[str] = mapped_column(
        String(20), nullable=False,
        comment="Role of the message sender"
    )
    content: Mapped[str] = mapped_column(
        Text, nullable=False,
        comment="Message content"
    )
    status: Mapped[str] = mapped_column(
        String(20), nullable=False, default="sent",
        comment="Status of the message"
    )
    sender_id: Mapped[Optional[str]] = mapped_column(
        String(100), nullable=True,
        comment="ID of the sender (user or agent)"
    )
    token_count: Mapped[Optional[int]] = mapped_column(
        Integer, nullable=True,
        comment="Number of tokens in the message"
    )
    metadata_json: Mapped[Optional[dict]] = mapped_column(
        JSONB, nullable=True,
        comment="Additional message metadata (tool calls, etc.)"
    )
    is_edited: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False,
        comment="Whether the message was edited"
    )
    edited_at: Mapped[Optional[datetime]] = mapped_column(
        nullable=True,
        comment="When the message was last edited"
    )
    read_by: Mapped[Optional[List[str]]] = mapped_column(
        JSONB, nullable=True,
        comment="List of user IDs who have read this message"
    )


# -------------------------------------------------------------------
# Pydantic Schemas / DTOs
# -------------------------------------------------------------------

class ConversationDTO(BaseModel):
    id: str
    title: Optional[str] = None
    status: str
    channel: str
    customer_id: Optional[str] = None
    agent_id: Optional[str] = None
    assigned_to: Optional[str] = None
    initiated_by: str
    source_url: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    tags: Optional[List[str]] = None
    message_count: int
    last_message_at: Optional[datetime] = None
    last_message_preview: Optional[str] = None
    resolved_at: Optional[datetime] = None
    satisfaction_score: Optional[float] = None
    satisfaction_feedback: Optional[str] = None
    is_handoff: bool
    handoff_reason: Optional[str] = None
    handoff_at: Optional[datetime] = None
    handoff_to: Optional[str] = None
    duration_seconds: Optional[int] = None
    tenant_id: str
    created_at: datetime
    updated_at: datetime


class MessageDTO(BaseModel):
    id: str
    conversation_id: str
    role: str
    content: str
    status: str
    sender_id: Optional[str] = None
    token_count: Optional[int] = None
    metadata: Optional[Dict[str, Any]] = None
    is_edited: bool
    edited_at: Optional[datetime] = None
    read_by: Optional[List[str]] = None
    tenant_id: str
    created_at: datetime
    updated_at: datetime


class ConversationCreateRequest(BaseModel):
    title: Optional[str] = None
    channel: str = "web"
    customer_id: Optional[str] = None
    agent_id: Optional[str] = None
    initiated_by: str = "user"
    source_url: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    tags: Optional[List[str]] = None


class ConversationCreateResponse(BaseModel):
    conversation_id: str
    status: str
    created_at: datetime
    title: Optional[str] = None


class MessageCreateRequest(BaseModel):
    conversation_id: str
    role: str = "user"
    content: str
    sender_id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class MessageCreateResponse(BaseModel):
    message_id: str
    status: str
    created_at: datetime


class ConversationSearchRequest(BaseModel):
    query: Optional[str] = None
    statuses: Optional[List[str]] = None
    channels: Optional[List[str]] = None
    customer_ids: Optional[List[str]] = None
    agent_ids: Optional[List[str]] = None
    assigned_to: Optional[str] = None
    is_handoff: Optional[bool] = None
    tags: Optional[List[str]] = None
    date_from: Optional[datetime] = None
    date_to: Optional[datetime] = None
    size: int = 50
    from_: int = 0
    sort_by: str = "last_message_at"
    sort_order: str = "desc"


class ConversationSearchResponse(BaseModel):
    total_hits: int
    hits: List[ConversationDTO]
    took_ms: int


class MessageSearchResponse(BaseModel):
    total_hits: int
    hits: List[MessageDTO]
    took_ms: int


class ConversationStatsDTO(BaseModel):
    status: str
    count: int
    percentage: float


class ConversationOverviewDTO(BaseModel):
    total_conversations: int
    active_conversations: int
    resolved_conversations: int
    closed_conversations: int
    avg_duration_seconds: int
    avg_satisfaction_score: float
    handoff_rate: float
    conversations_by_channel: Dict[str, int]
    conversations_by_status: Dict[str, int]
    top_agents: List[Dict[str, Any]]
    recent_conversations: List[ConversationDTO]


class ConversationUpdateRequest(BaseModel):
    title: Optional[str] = None
    status: Optional[str] = None
    assigned_to: Optional[str] = None
    tags: Optional[List[str]] = None
    satisfaction_score: Optional[float] = None
    satisfaction_feedback: Optional[str] = None
    is_handoff: Optional[bool] = None
    handoff_reason: Optional[str] = None
    handoff_to: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class ConversationHandoffRequest(BaseModel):
    conversation_id: str
    handoff_to: str
    reason: Optional[str] = None
    priority: str = "normal"