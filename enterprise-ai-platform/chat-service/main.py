"""
Chat Microservice Entrypoint
Initializes FastAPI microservice for WebSocket real-time chat and omnichannel webhooks.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from enterprise_ai_platform.common.config import settings
from src.router_chat import router as chat_router

app = FastAPI(
    title=f"{settings.PROJECT_NAME} - Chat Service",
    description="Real-time WebSocket Pub-Sub, Omnichannel Messaging (WhatsApp, Slack, Telegram, Email), & Webhooks",
    version="1.0.0",
    docs_url="/docs",
    openapi_url="/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health/live", tags=["Health Checks"])
async def liveness_probe():
    return {"status": "UP", "service": "chat-service"}


@app.get("/health/ready", tags=["Health Checks"])
async def readiness_probe():
    return {"status": "READY", "service": "chat-service"}


app.include_router(chat_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8009, reload=settings.DEBUG)
