"""
WhatsApp Service API Router
Endpoints for WhatsApp Business API integration.
"""

import uuid
import time
import hmac
import hashlib
from typing import List, Optional, Dict, Any
from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, status, Request, Query, Body
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from pydantic import BaseModel
import httpx

from enterprise_ai_platform.common.database import get_async_db
from enterprise_ai_platform.common.security_rbac import (
    get_current_user,
    TokenPayload,
    RequirePermissions,
    Permission,
)
from .models import (
    WhatsAppAccount,
    WhatsAppPhoneNumber,
    WhatsAppMessage,
    MessageTemplate,
    ConversationSession,
    MediaFile,
    WhatsAppAccountDTO,
    MessageTemplateDTO,
    ConversationSessionDTO,
    MessageType,
    MessageStatus,
    Direction,
)

router = APIRouter(prefix="/api/v1/whatsapp", tags=["WhatsApp Business API"])

WHATSAPP_API_URL = "https://graph.facebook.com/v19.0"


def _get_tenant_uuid(current_user: TokenPayload) -> uuid.UUID:
    """Extract tenant UUID from current user token."""
    return uuid.UUID(uuid.uuid5(uuid.NAMESPACE_DNS, current_user.tenant_id).hex[:32])


# -------------------------------------------------------------------
# Webhook Verification & Handling
# -------------------------------------------------------------------

@router.post("/webhook", summary="WhatsApp Webhook Endpoint")
async def whatsapp_webhook(
    request: Request,
    hub_mode: str = Query(None, alias="hub.mode"),
    hub_challenge: str = Query(None, alias="hub.challenge"),
    hub_verify_token: str = Query(None, alias="hub.verify_token"),
    db: AsyncSession = Depends(get_async_db),
):
    """
    Handle WhatsApp webhook events.
    Supports verification (GET) and message handling (POST).
    """
    if hub_mode == "subscribe":
        # Verification challenge
        if hub_verify_token == "salesgenie_webhook_verify_token":
            return {"hub_challenge": hub_challenge}
        raise HTTPException(status_code=403, detail="Webhook verification failed")

    # Handle POST - message events
    body = await request.json()
    
    # Process incoming messages
    if "entry" in body:
        for entry in body["entry"]:
            for change in entry.get("changes", []):
                value = change.get("value", {})
                messages = value.get("messages", [])
                
                for message in messages:
                    await _process_incoming_message(message, value, db)

    return {"status": "ok"}


async def _process_incoming_message(message: Dict, value: Dict, db: AsyncSession):
    """Process an incoming WhatsApp message."""
    phone_number_id = value.get("metadata", {}).get("phone_number_id")
    from_number = message.get("from")
    message_id = message.get("id")
    message_type = message.get("type")
    timestamp = int(message.get("timestamp", 0))
    
    # Extract content based on message type
    content = None
    media_url = None
    
    if message_type == "text":
        content = message.get("text", {}).get("body")
    elif message_type == "image":
        image_data = message.get("image", {})
        content = image_data.get("caption")
        media_url = image_data.get("link")
    
    # Save message to database
    whatsapp_msg = WhatsAppMessage(
        tenant_id=uuid.uuid4(),  # Will be resolved from user context in real implementation
        phone_number_id=phone_number_id or "",
        direction=Direction.INCOMING,
        message_type=MessageType.TEXT if message_type == "text" else MessageType.IMAGE,
        message_id=message_id,
        from_number=from_number,
        to_number=phone_number_id,
        content=content,
        media_url=media_url,
        status=MessageStatus.SENT,
        created_at=datetime.fromtimestamp(timestamp, tz=timezone.utc),
    )
    db.add(whatsapp_msg)
    await db.commit()


# -------------------------------------------------------------------
# Message Sending
# -------------------------------------------------------------------

class SendMessageRequest(BaseModel):
    to: str
    message: str
    message_type: str = "text"
    media_url: Optional[str] = None
    caption: Optional[str] = None
    template_name: Optional[str] = None
    template_language: Optional[str] = "en"
    template_components: Optional[List[Dict[str, Any]]] = None


@router.post("/messages", response_model=Dict[str, Any], summary="Send WhatsApp Message")
async def send_message(
    req: SendMessageRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Send a message via WhatsApp Business API."""
    tenant_uuid = _get_tenant_uuid(current_user)
    
    # Get WhatsApp account for tenant
    stmt = select(WhatsAppAccount).where(
        WhatsAppAccount.tenant_id == tenant_uuid,
        WhatsAppAccount.is_active == True,
    )
    res = await db.execute(stmt)
    account = res.scalar_one_or_none()
    
    if not account:
        raise HTTPException(status_code=404, detail="WhatsApp account not configured for tenant")
    
    # Prepare message payload
    payload = {
        "messaging_product": "whatsapp",
        "to": req.to,
    }
    
    if req.message_type == "text":
        payload["text"] = {"body": req.message}
    elif req.message_type == "image":
        payload["image"] = {
            "link": req.media_url,
            "caption": req.caption or req.message,
        }
    elif req.message_type == "template":
        payload["template"] = {
            "name": req.template_name,
            "language": req.template_language,
            "components": req.template_components or [],
        }
    
    # Send via WhatsApp API
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{WHATSAPP_API_URL}/{account.phone_number_id}/messages",
            headers={
                "Authorization": f"Bearer {account.access_token}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=30.0,
        )
    
    if response.status_code != 200:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to send message: {response.text}",
        )
    
    result = response.json()
    message_id = result.get("messages", [{}])[0].get("id")
    
    # Save sent message
    whatsapp_msg = WhatsAppMessage(
        tenant_id=tenant_uuid,
        phone_number_id=account.phone_number_id,
        direction=Direction.OUTGOING,
        message_type=MessageType.TEXT if req.message_type == "text" else MessageType.TEMPLATE,
        message_id=message_id,
        to_number=req.to,
        content=req.message,
        status=MessageStatus.SENT,
        metadata={"payload": payload},
    )
    db.add(whatsapp_msg)
    await db.commit()
    
    return {
        "status": "sent",
        "message_id": message_id,
        "recipient": req.to,
    }


# -------------------------------------------------------------------
# Account Management
# -------------------------------------------------------------------

class WhatsAppAccountCreate(BaseModel):
    name: str
    access_token: str
    phone_number_id: str
    app_id: Optional[str] = None
    app_secret: Optional[str] = None
    webhook_url: Optional[str] = None


@router.post(
    "/accounts",
    response_model=WhatsAppAccountDTO,
    summary="Configure WhatsApp Account",
    dependencies=[Depends(RequirePermissions(Permission.ORG_WRITE))],
)
async def create_whatsapp_account(
    req: WhatsAppAccountCreate,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Configure a WhatsApp Business account."""
    tenant_uuid = _get_tenant_uuid(current_user)
    
    # Check if account already exists
    stmt = select(WhatsAppAccount).where(WhatsAppAccount.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    if res.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="WhatsApp account already configured for tenant")
    
    account = WhatsAppAccount(
        tenant_id=tenant_uuid,
        name=req.name,
        access_token=req.access_token,
        phone_number_id=req.phone_number_id,
        app_id=req.app_id,
        app_secret=req.app_secret,
        webhook_url=req.webhook_url,
        is_active=True,
        verified=False,
    )
    db.add(account)
    await db.commit()
    
    return WhatsAppAccountDTO(
        id=str(account.id),
        name=account.name,
        phone_number_id=account.phone_number_id,
        webhook_url=account.webhook_url,
        is_active=account.is_active,
        verified=account.verified,
        created_at=account.created_at,
        updated_at=account.updated_at,
    )


@router.get(
    "/accounts",
    response_model=WhatsAppAccountDTO,
    summary="Get WhatsApp Account",
    dependencies=[Depends(RequirePermissions(Permission.ORG_READ))],
)
async def get_whatsapp_account(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get configured WhatsApp account for tenant."""
    tenant_uuid = _get_tenant_uuid(current_user)
    
    stmt = select(WhatsAppAccount).where(WhatsAppAccount.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    account = res.scalar_one_or_none()
    
    if not account:
        raise HTTPException(status_code=404, detail="WhatsApp account not configured")
    
    return WhatsAppAccountDTO(
        id=str(account.id),
        name=account.name,
        phone_number_id=account.phone_number_id,
        webhook_url=account.webhook_url,
        is_active=account.is_active,
        verified=account.verified,
        created_at=account.created_at,
        updated_at=account.updated_at,
    )


# -------------------------------------------------------------------
# Template Management
# -------------------------------------------------------------------

@router.get(
    "/templates",
    response_model=List[MessageTemplateDTO],
    summary="List Message Templates",
    dependencies=[Depends(RequirePermissions(Permission.KNOWLEDGE_READ))],
)
async def list_templates(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """List saved message templates."""
    tenant_uuid = _get_tenant_uuid(current_user)
    
    stmt = select(MessageTemplate).where(MessageTemplate.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    templates = res.scalars().all()
    
    return [
        MessageTemplateDTO(
            id=str(t.id),
            name=t.name,
            category=t.category,
            language=t.language,
            status=t.status,
            last_used_at=t.last_used_at,
            created_at=t.created_at,
            updated_at=t.updated_at,
        )
        for t in templates
    ]


@router.post(
    "/templates",
    response_model=MessageTemplateDTO,
    summary="Create Message Template",
    dependencies=[Depends(RequirePermissions(Permission.KNOWLEDGE_WRITE))],
)
async def create_template(
    name: str = Body(...),
    category: str = Body(...),
    language: str = Body("en"),
    components: List[Dict[str, Any]] = Body(...),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Create a new message template."""
    tenant_uuid = _get_tenant_uuid(current_user)
    
    # Check if template already exists
    stmt = select(MessageTemplate).where(
        MessageTemplate.tenant_id == tenant_uuid,
        MessageTemplate.name == name,
    )
    res = await db.execute(stmt)
    if res.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Template with this name already exists")
    
    template = MessageTemplate(
        tenant_id=tenant_uuid,
        name=name,
        category=category,
        language=language,
        components=components,
        status="approved",  # In production, would check with Meta
    )
    db.add(template)
    await db.commit()
    
    return MessageTemplateDTO(
        id=str(template.id),
        name=template.name,
        category=template.category,
        language=template.language,
        status=template.status,
        last_used_at=template.last_used_at,
        created_at=template.created_at,
        updated_at=template.updated_at,
    )


# -------------------------------------------------------------------
# Conversation Sessions
# -------------------------------------------------------------------

@router.get(
    "/conversations",
    response_model=List[ConversationSessionDTO],
    summary="List Active Conversations",
    dependencies=[Depends(RequirePermissions(Permission.TICKET_READ))],
)
async def list_conversations(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """List active WhatsApp conversations."""
    tenant_uuid = _get_tenant_uuid(current_user)
    
    stmt = select(ConversationSession).where(
        ConversationSession.tenant_id == tenant_uuid,
        ConversationSession.is_active == True,
    )
    res = await db.execute(stmt)
    sessions = res.scalars().all()
    
    return [
        ConversationSessionDTO(
            id=str(s.id),
            tenant_id=str(s.tenant_id),
            phone_number_id=s.phone_number_id,
            customer_phone=s.customer_phone,
            last_message_at=s.last_message_at,
            conversation_id=s.conversation_id,
            assigned_to=s.assigned_to,
            is_active=s.is_active,
            created_at=s.created_at,
            updated_at=s.updated_at,
        )
        for s in sessions
    ]


# -------------------------------------------------------------------
# Media Upload
# -------------------------------------------------------------------

class MediaUploadRequest(BaseModel):
    url: str
    filename: Optional[str] = None
    media_type: str


@router.post("/media/upload", summary="Register Media File")
async def register_media(
    req: MediaUploadRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Register an uploaded media file for a message."""
    tenant_uuid = _get_tenant_uuid(current_user)
    
    media = MediaFile(
        tenant_id=tenant_uuid,
        message_id=req.url.split("/")[-2] if "/" in req.url else str(uuid.uuid4()),
        media_url=req.url,
        media_type=req.media_type,
        filename=req.filename,
        size_bytes=0,  # Would be calculated from actual download
        downloaded=True,
    )
    db.add(media)
    await db.commit()
    
    return {
        "status": "registered",
        "media_id": str(media.id),
        "url": req.url,
    }