"""
Chat Service Data Models & Schemas
Database models for Omnichannel Conversations, Channels, and Message Streams.
"""

import uuid
from enum import Enum
from datetime import datetime, timezone
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from sqlalchemy import Column, String, Boolean, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column

from enterprise_ai_platform.common.models_base import (
    Base,
    UUIDPrimaryKeyMixin,
    TimestampMixin,
    TenantIsolationMixin,
)


class ChannelType(str, Enum):
    WEBSITE = "website"
    WHATSAPP = "whatsapp"
    MESSENGER = "messenger"
    TELEGRAM = "telegram"
    INSTAGRAM = "instagram"
    SLACK = "slack"
    DISCORD = "discord"
    EMAIL = "email"
    VOICE = "voice"


class ConversationSession(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Omnichannel real-time conversation session."""
    __tablename__ = "chat_conversation_sessions"

    channel: Mapped[ChannelType] = mapped_column(String(30), default=ChannelType.WEBSITE, nullable=False, index=True)
    customer_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False, index=True)
    assigned_agent_id: Mapped[Optional[uuid.UUID]] = mapped_column(UUID(as_uuid=True), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    unread_count: Mapped[int] = mapped_column(default=0, nullable=False)
    last_message_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)


class NormalizedMessagePayload(BaseModel):
    session_id: str
    channel: ChannelType
    sender_id: str
    sender_type: str  # 'customer', 'ai_agent', 'human_agent'
    content: str
    media_url: Optional[str] = None
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    metadata: Dict[str, Any] = Field(default_factory=dict)
