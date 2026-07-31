"""
Messenger Models
Pydantic models for Facebook Messenger integration.
"""

from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class Message(BaseModel):
    id: Optional[str] = None
    page_id: str
    sender_id: str
    recipient_id: str
    message_text: Optional[str] = None
    attachments: Optional[List[Dict[str, Any]]] = None
    timestamp: Optional[datetime] = None
    delivered: bool = False
    read: bool = False


class Conversation(BaseModel):
    id: Optional[str] = None
    page_id: str
    participants: List[str]
    status: str = "active"
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class PageSubscription(BaseModel):
    page_id: str
    verify_token: str
    webhook_url: str
    subscribed_fields: List[str] = ["messages", "messaging_postbacks", "message_deliveries"]


class WebhookEvent(BaseModel):
    object: str
    entry: List[Dict[str, Any]]


class DeliveryEvent(BaseModel):
    messaging_product: str = "messenger"
    recipient: Dict[str, str]
    message: Dict[str, str]


class MessageSendRequest(BaseModel):
    recipient: Dict[str, str]
    message: Dict[str, Any] = Field(..., alias="message")
    
    class Config:
        populate_by_name = True