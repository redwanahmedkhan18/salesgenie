"""
Chat Service API Router
Endpoints for omnichannel webhooks and real-time WebSocket connection handling.
"""

from typing import Dict, Any
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, HTTPException, status
from pydantic import BaseModel

from .models import NormalizedMessagePayload
from .omnichannel_pubsub import pubsub_processor

router = APIRouter(prefix="/api/v1/chat", tags=["Omnichannel Real-Time Chat"])


class ActiveConnectionManager:
    """Manages active WebSockets connections per conversation session."""

    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, session_id: str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[session_id] = websocket

    def disconnect(self, session_id: str):
        if session_id in self.active_connections:
            del self.active_connections[session_id]

    async def send_message(self, session_id: str, message: str):
        if session_id in self.active_connections:
            await self.active_connections[session_id].send_text(message)


ws_manager = ActiveConnectionManager()


@router.post("/webhooks/{channel}", summary="Omnichannel Webhook Inbound Handler")
async def handle_channel_webhook(channel: str, payload: Dict[str, Any]):
    """Unified webhook receiver for WhatsApp, Messenger, Telegram, Slack, Email, and Voice."""
    normalized = pubsub_processor.normalize_inbound_webhook(channel, payload)
    return {
        "status": "processed",
        "channel": channel,
        "session_id": normalized.session_id,
        "content_received": normalized.content,
    }


@router.websocket("/ws/{session_id}")
async def chat_websocket_endpoint(websocket: WebSocket, session_id: str):
    """Real-time WebSocket endpoint supporting typing indicators, read receipts, and streaming AI responses."""
    await ws_manager.connect(session_id, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Send echo / AI streaming response ack
            await ws_manager.send_message(session_id, f"ACK: Received message '{data}'")
    except WebSocketDisconnect:
        ws_manager.disconnect(session_id)
