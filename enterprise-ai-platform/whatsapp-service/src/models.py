"""
WhatsApp Service Models
Database models for WhatsApp integration.
"""

import uuid
from datetime import datetime, timezone
from typing import Optional, List, Any
from sqlalchemy import Column, String, Text, Boolean, Integer, DateTime, JSON, ForeignKey, Float, Enum
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from pydantic import BaseModel
from enum import Enum as PyEnum

class Base(DeclarativeBase):
    pass


class MessageType(str, PyEnum):
    TEXT = "text"
    IMAGE = "image"
    AUDIO = "audio"
    VIDEO = "video"
    DOCUMENT = "document"
    CONTACT = "contact"
    LOCATION = "location"
    TEMPLATE = "template"


class MessageStatus(str, PyEnum):
    SENT = "sent"
    DELIVERED = "delivered"
    READ = "read"
    FAILED = "failed"
    PENDING = "pending"


class Direction(str, PyEnum):
    INCOMING = "incoming"
    OUTGOING = "outgoing"


class WhatsAppAccount(Base):
    __tablename__ = "whatsapp_accounts"

    id: uuid.UUID = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: str = Column(String(100), nullable=False)
    access_token: str = Column(Text, nullable=False)
    phone_number_id: str = Column(String(100), nullable=False, unique=True)
    app_id: Optional[str] = Column(String(100), nullable=True)
    app_secret: Optional[str] = Column(Text, nullable=True)
    webhook_url: Optional[str] = Column(Text, nullable=True)
    is_active: bool = Column(Boolean, default=True)
    verified: bool = Column(Boolean, default=False)
    created_at: datetime = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))


class WhatsAppPhoneNumber(Base):
    __tablename__ = "whatsapp_phone_numbers"

    id: uuid.UUID = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    account_id: uuid.UUID = Column(PGUUID(as_uuid=True), ForeignKey("whatsapp_accounts.id"), nullable=False)
    phone_number: str = Column(String(20), nullable=False)
    phone_number_id: str = Column(String(100), nullable=False, unique=True)
    display_name: Optional[str] = Column(String(100), nullable=True)
    is_verified: bool = Column(Boolean, default=False)
    status: str = Column(String(50), default="pending_verification")
    created_at: datetime = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))


class WhatsAppMessage(Base):
    __tablename__ = "whatsapp_messages"

    id: uuid.UUID = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False)
    phone_number_id: str = Column(String(100), nullable=False)
    direction: str = Column(String(20), nullable=False)
    message_type: str = Column(String(20), nullable=False)
    message_id: Optional[str] = Column(String(100), nullable=True, unique=True)
    from_number: Optional[str] = Column(String(30), nullable=True)
    to_number: Optional[str] = Column(String(30), nullable=True)
    content: Optional[str] = Column(Text, nullable=True)
    media_url: Optional[str] = Column(Text, nullable=True)
    media_type: Optional[str] = Column(String(50), nullable=True)
    caption: Optional[str] = Column(Text, nullable=True)
    status: str = Column(String(20), default="pending")
    reply_to_message_id: Optional[str] = Column(String(100), nullable=True)
    metadata_data: Optional[dict] = Column(JSON, nullable=True)
    created_at: datetime = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))


class MessageTemplate(Base):
    __tablename__ = "message_templates"

    id: uuid.UUID = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False)
    name: str = Column(String(100), nullable=False)
    category: str = Column(String(50), nullable=False)
    language: str = Column(String(10), default="en")
    components: List[dict] = Column(JSON, nullable=False)
    status: str = Column(String(20), default="draft")
    last_used_at: Optional[datetime] = Column(DateTime(timezone=True), nullable=True)
    created_at: datetime = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))


class ConversationSession(Base):
    __tablename__ = "conversation_sessions"

    id: uuid.UUID = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False)
    phone_number_id: str = Column(String(100), nullable=False)
    customer_phone: str = Column(String(30), nullable=False)
    last_message_at: datetime = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    conversation_id: Optional[str] = Column(String(100), nullable=True)
    assigned_to: Optional[str] = Column(String(100), nullable=True)
    is_active: bool = Column(Boolean, default=True)
    created_at: datetime = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    __table_args__ = {}


class MediaFile(Base):
    __tablename__ = "media_files"

    id: uuid.UUID = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False)
    message_id: str = Column(String(100), nullable=False)
    media_url: str = Column(Text, nullable=False)
    media_type: str = Column(String(50), nullable=False)
    filename: Optional[str] = Column(String(255), nullable=True)
    size_bytes: Optional[int] = Column(Integer, nullable=True)
    downloaded: bool = Column(Boolean, default=False)
    downloaded_at: Optional[datetime] = Column(DateTime(timezone=True), nullable=True)
    created_at: datetime = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))


# Pydantic DTOs for API responses

class WhatsAppAccountDTO(BaseModel):
    id: str
    name: str
    phone_number_id: str
    webhook_url: Optional[str] = None
    is_active: bool
    verified: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class MessageTemplateDTO(BaseModel):
    id: str
    name: str
    category: str
    language: str
    status: str
    last_used_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ConversationSessionDTO(BaseModel):
    id: str
    tenant_id: str
    phone_number_id: str
    customer_phone: str
    last_message_at: datetime
    conversation_id: Optional[str] = None
    assigned_to: Optional[str] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True