"""
AI Gateway Microservice Entrypoint
Initializes FastAPI microservice for LangGraph Multi-Agent Orchestration and Grok LLM execution.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from enterprise_ai_platform.common.config import settings
from src.router_ai import router as ai_router

app = FastAPI(
    title=f"{settings.PROJECT_NAME} - AI Gateway Service",
    description="Multi-Agent LangGraph Orchestrator, Grok API execution loop, & Fallback Cascade",
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
    return {"status": "UP", "service": "ai-gateway-service"}


@app.get("/health/ready", tags=["Health Checks"])
async def readiness_probe():
    return {"status": "READY", "service": "ai-gateway-service"}


app.include_router(ai_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8006, reload=settings.DEBUG)
