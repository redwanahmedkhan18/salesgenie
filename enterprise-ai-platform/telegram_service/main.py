"""Telegram Service Main Application"""
import os, sentry_sdk
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from enterprise_ai_platform.common.config import settings
from enterprise_ai_platform.telegram_service.src.router_telegram import router

sentry_sdk.init(dsn=os.getenv("SENTRY_DSN"), traces_sample_rate=1.0, send_default_pii=True)

app = FastAPI(title="Telegram Bot Service", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(router, prefix="/api/v1/telegram")

@app.get("/health/live")
async def liveness_probe():
    return {"status": "UP", "service": "telegram-service"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8019)
