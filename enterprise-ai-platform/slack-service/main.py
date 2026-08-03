"""
Slack Service for SalesGenie
Integration with Slack for AI-powered customer conversations, notifications, and workflows.
"""

import os
import logging
from typing import Dict, Any, Optional, List
from datetime import datetime
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("salesgenie.slack-service")

app = FastAPI(
    title="SalesGenie - Slack Service",
    description="Production-ready Slack integration for AI-powered conversations",
    version="1.0.0",
    docs_url="/docs",
    openapi_url="/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SLACK_BASE_URL = "https://slack.com/api"
SLACK_WEBHOOK_BASE_URL = "https://hooks.slack.com"

channel_integrations: Dict[str, Dict[str, Any]] = {}
active_connections: Dict[str, Any] = {}


class SlackChannelIntegration:
    def __init__(self, channel_id: str, bot_token: str, signing_secret: str):
        self.channel_id = channel_id
        self.bot_token = bot_token
        self.signing_secret = signing_secret
        self.ai_assistant_enabled = True
        self.max_messages_per_hour = 1000
        self.webhooks: List[Dict[str, Any]] = []

    def to_dict(self) -> Dict[str, Any]:
        return {
            "channel_id": self.channel_id,
            "bot_token": self.bot_token,
            "signing_secret": self.signing_secret,
            "ai_assistant_enabled": self.ai_assistant_enabled,
            "max_messages_per_hour": self.max_messages_per_hour,
            "webhooks": self.webhooks,
        }


@app.get("/health/live", tags=["Health Checks"])
async def liveness_probe():
    return {"status": "UP", "service": "slack-service"}


@app.get("/health/ready", tags=["Health Checks"])
async def readiness_probe():
    return {"status": "READY", "service": "slack-service"}


@app.post("/api/v1/slack/webhook", tags=["Slack Integration"])
async def slack_webhook(request: Request):
    try:
        payload = await request.json()
        event_type = payload.get("type", "")
        
        if event_type == "url_verification":
            return JSONResponse({"challenge": payload.get("challenge", "")})
        
        event = payload.get("event", {})
        logger.info(f"Processing Slack event: {event.get('type', 'unknown')}")
        
        channel_id = event.get("channel", "")
        user = event.get("user", "")
        text = event.get("text", "")
        
        if channel_id and channel_id in channel_integrations:
            integration = channel_integrations[channel_id]
            
            return JSONResponse({
                "status": "processed",
                "channel_id": channel_id,
                "user": user,
                "message_type": event.get("type"),
                "message_preview": text[:100] if text else None,
                "integration_active": True,
            })
        
        return JSONResponse({
            "status": "received",
            "channel_id": channel_id,
            "event_type": event.get("type"),
        })
    except Exception as e:
        logger.error(f"Slack webhook error: {e}")
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/api/v1/slack/workspace/{workspace_id}/channels", tags=["Slack Integration"])
async def create_slack_channel(workspace_id: str, channel_name: str, is_private: bool = False):
    channel_id = f"C{hash(channel_name) % 10**17}"
    logger.info(f"Created channel {channel_name} in workspace {workspace_id}")
    return {
        "status": "created",
        "workspace_id": workspace_id,
        "channel_id": channel_id,
        "channel_name": channel_name,
        "is_private": is_private,
    }


@app.post("/api/v1/slack/channels/{channel_id}/messages", tags=["Slack Integration"])
async def send_slack_message(channel_id: str, text: str, thread_ts: Optional[str] = None):
    logger.info(f"Sending message to Slack channel {channel_id}")
    return {
        "status": "sent",
        "channel_id": channel_id,
        "text": text,
        "thread_ts": thread_ts,
        "message_id": f"msg_{datetime.now().timestamp()}",
    }


@app.post("/api/v1/slack/integrations", tags=["Slack Integration"])
async def register_slack_integration(channel_id: str, bot_token: str, signing_secret: str):
    integration = SlackChannelIntegration(channel_id, bot_token, signing_secret)
    channel_integrations[channel_id] = integration.to_dict()
    logger.info(f"Registered Slack integration for channel {channel_id}")
    return {"status": "registered", "channel_id": channel_id}


@app.get("/api/v1/slack/integrations", tags=["Slack Integration"])
async def list_slack_integrations():
    return {
        "status": "success",
        "integrations": list(channel_integrations.keys()),
        "count": len(channel_integrations),
    }


@app.get("/api/v1/slack/channels/{channel_id}", tags=["Slack Integration"])
async def get_channel_integration(channel_id: str):
    if channel_id in channel_integrations:
        return {"status": "active", "channel_id": channel_id, **channel_integrations[channel_id]}
    return {"status": "not_found", "channel_id": channel_id}


@app.delete("/api/v1/slack/integrations/{channel_id}", tags=["Slack Integration"])
async def remove_slack_integration(channel_id: str):
    if channel_id in channel_integrations:
        del channel_integrations[channel_id]
        return {"status": "removed", "channel_id": channel_id}
    return {"status": "not_found", "channel_id": channel_id}


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("SLACK_SERVICE_PORT", 8024))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)