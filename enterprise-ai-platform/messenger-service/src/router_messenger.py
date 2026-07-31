"""
Facebook Messenger Router
API endpoints for Facebook Messenger integration.
"""

import logging
import httpx
from fastapi import APIRouter, Request, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from enterprise_ai_platform.common.config import settings
from .models import Message, Conversation, PageSubscription, WebhookEvent, MessageSendRequest

router = APIRouter()
logger = logging.getLogger("salesgenie.messenger")


@router.get("/webhook")
async def verify_webhook(
    hub_mode: str = None,
    hub_verify_token: str = None,
    hub_challenge: str = None,
):
    """Verify webhook with Facebook."""
    logger.info(f"Webhook verification attempt: mode={hub_mode}, token={hub_verify_token}")
    
    if hub_mode == "subscribe" and hub_verify_token == settings.FACEBOOK_VERIFY_TOKEN:
        logger.info("Webhook verified successfully")
        return hub_challenge
    
    logger.warning("Webhook verification failed")
    raise HTTPException(status_code=403, detail="Webhook verification failed")


@router.post("/webhook")
async def handle_webhook(request: Request):
    """Handle incoming webhook events from Facebook."""
    try:
        body = await request.json()
        logger.info(f"Received webhook event: {body.get('object', 'unknown')}")
        
        if body.get("object") == "page":
            for entry in body.get("entry", []):
                for messaging_event in entry.get("messaging", []):
                    await process_messaging_event(messaging_event)
        
        return JSONResponse(status_code=200, content={"status": "received"})
    
    except Exception as e:
        logger.error(f"Error processing webhook: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


async def process_messaging_event(event: dict):
    """Process individual messaging events."""
    sender_id = event.get("sender", {}).get("id")
    recipient_id = event.get("recipient", {}).get("id")
    
    message_data = event.get("message", {})
    message_text = message_data.get("text")
    attachments = message_data.get("attachments")
    
    logger.info(f"Processing message from {sender_id}: {message_text or 'attachment'}")
    
    response_text = await generate_response(message_text, sender_id)
    
    await send_message(recipient_id, response_text)


async def generate_response(message_text: str, sender_id: str) -> str:
    """Generate response using AI (placeholder)."""
    if not message_text:
        return "I received your message. How can I help you?"
    
    return f"Echo: {message_text}"


async def send_message(recipient_id: str, message_text: str) -> bool:
    """Send message to Facebook Messenger."""
    if not settings.FACEBOOK_PAGE_ACCESS_TOKEN:
        logger.warning("FACEBOOK_PAGE_ACCESS_TOKEN not configured")
        return False
    
    url = f"https://graph.facebook.com/v18.0/me/messages"
    headers = {
        "Authorization": f"Bearer {settings.FACEBOOK_PAGE_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }
    
    payload = MessageSendRequest(
        recipient={"id": recipient_id},
        message={"text": message_text}
    ).model_dump()
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload, headers=headers, timeout=10.0)
            
            if response.status_code == 200:
                logger.info(f"Message sent to {recipient_id}")
                return True
            else:
                logger.error(f"Failed to send message: {response.text}")
                return False
    
    except Exception as e:
        logger.error(f"Error sending message: {e}")
        return False


@router.post("/messages")
async def send_message_endpoint(request: MessageSendRequest):
    """Send a message to a user."""
    success = await send_message(request.recipient["id"], request.message.get("text", ""))
    
    if success:
        return {"status": "sent"}
    else:
        raise HTTPException(status_code=500, detail="Failed to send message")


@router.get("/conversations/{sender_id}")
async def get_conversation(sender_id: str):
    """Get conversation history (placeholder)."""
    return {
        "sender_id": sender_id,
        "messages": [],
        "status": "active"
    }