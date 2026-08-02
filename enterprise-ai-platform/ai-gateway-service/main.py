"""
AI Gateway Service Main Application
FastAPI application entry point for AI gateway and agent orchestration.
"""

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from enterprise_ai_platform.common.config import settings
from enterprise_ai_platform.ai_gateway_service.src.router_ai import router as ai_router


app = FastAPI(
    title=f"{settings.PROJECT_NAME} - AI Gateway Service",
    description="AI Agent Orchestration, LLM Provider Routing, Multi-Agent Chat",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ai_router)


@app.get("/health/live", tags=["Health Checks"])
async def liveness_probe():
    return {"status": "UP", "service": "ai-gateway-service"}


if __name__ == "__main__":
    import uvicorn
    from enterprise_ai_platform.common.config import settings
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=settings.AI_GATEWAY_SERVICE_PORT,
        reload=settings.DEBUG,
    )

@app.get("/health/ready", tags=["Health Checks"])
async def readiness_probe():
    return {"status": "READY", "service": "ai-gateway-service"}