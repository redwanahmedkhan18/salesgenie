"""Telegram Router"""

import logging
import httpx
from fastapi import APIRouter, Request, HTTPException, Query
from fastapi.responses import JSONResponse, PlainTextResponse
from enterprise_ai_platform.common.config import settings
from .models import Update, SendMessageRequest

router = APIRouter()
logger = logging.getLogger("salesgenie.telegram")

@router.get("/bot-info")
async def get_bot_info():
    if not settings.TELEGRAM_BOT_TOKEN:
        raise HTTPException(status_code=500, detail="TELEGRAM_BOT_TOKEN not configured")
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/getMe"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, timeout=10.0)
        if response.status_code == 200:
            data = response.json()
            if data.get("ok"):
                return data.get("result", {})
    raise HTTPException(status_code=500, detail="Failed to get bot info")

@router.get("/webhook")
async def verify_webhook(mode: str = Query(None, alias="hub.mode"), 
                         token: str = Query(None, alias="hub.verify_token"),
                         challenge: str = Query(None, alias="hub.challenge")):
    if mode == "subscribe":
        return PlainTextResponse(content=challenge, status_code=200)
    raise HTTPException(status_code=403, detail="Webhook verification failed")

@router.post("/webhook")
async def handle_webhook(request: Request):
    body = await request.json()
    update = Update(**body)
    return JSONResponse(status_code=200, content={"status": "received"})
