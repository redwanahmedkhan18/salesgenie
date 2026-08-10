"""
AI Gateway Service Main Application
FastAPI application entry point for AI gateway and agent orchestration.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from enterprise_ai_platform.common.config import settings
from enterprise_ai_platform.common.request_logging import add_request_logging
from enterprise_ai_platform.common.observability import init_sentry
from enterprise_ai_platform.ai_gateway_service.src.router_ai import router as ai_router
from enterprise_ai_platform.ai_gateway_service.src.router_admin import router as admin_router

init_sentry("ai-gateway-service")


app = FastAPI(
    title=f"{settings.PROJECT_NAME} - AI Gateway Service",
    description="AI Agent Orchestration, LLM Provider Routing, Multi-Agent Chat",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

add_request_logging(app, service_name="ai-gateway-service")

app.include_router(ai_router)
app.include_router(admin_router)


@app.get("/metrics", tags=["Monitoring"])
async def metrics_endpoint():
    """Prometheus-compatible metrics endpoint."""
    from enterprise_ai_platform.common.metrics import get_all_metrics
    from fastapi.responses import PlainTextResponse
    all_metrics = get_all_metrics()
    lines = []
    for svc_name, mc in all_metrics.items():
        lines.append(f"# Service: {svc_name}")
        lines.append(mc.to_prometheus())
        lines.append("")
    return PlainTextResponse(content="\n".join(lines), media_type="text/plain")


@app.get("/health/live", tags=["Health Checks"])
async def liveness_probe():
    return {"status": "UP", "service": "ai-gateway-service"}


@app.get("/health/ready", tags=["Health Checks"])
async def readiness_probe():
    try:
        from enterprise_ai_platform.common.database import async_engine
        from sqlalchemy import text
        async with async_engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        return {"status": "READY", "service": "ai-gateway-service", "database": "connected"}
    except Exception as e:
        import logging
        logging.error("Database connection failed during readiness check: %s", e)
        return {"status": "NOT_READY", "service": "ai-gateway-service", "database": "disconnected"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=settings.AI_GATEWAY_SERVICE_PORT,
        reload=settings.DEBUG,
    )