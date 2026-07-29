"""
Conversation Service
Manages real-time conversations, messages, and chat sessions with AI agents.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from enterprise_ai_platform.common.config import settings
from conversation_service.src.router_conversations import router as conversations_router

app = FastAPI(
    title=f"{settings.PROJECT_NAME} - Conversation Service",
    description="Manages real-time conversations, messages, and chat sessions with AI agents",
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
    return {"status": "UP", "service": "conversation-service"}


@app.get("/health/ready", tags=["Health Checks"])
async def readiness_probe():
    return {"status": "READY", "service": "conversation-service"}


app.include_router(conversations_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8017, reload=settings.DEBUG)