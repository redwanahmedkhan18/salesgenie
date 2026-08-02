"""
Telegram Service Main Application
FastAPI application entry point for Telegram Bot integration.
"""

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from enterprise_ai_platform.common.config import settings
from enterprise_ai_platform.telegram_service.src.router_telegram import router

app = FastAPI(
    title="Telegram Bot Service",
    description="Integration with Telegram Bot API for messaging and notifications",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1/telegram")


@app.get("/health/live", tags=["Health Checks"])
async def liveness_probe():
    return {"status": "UP", "service": "telegram-service"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=settings.TELEGRAM_SERVICE_PORT)