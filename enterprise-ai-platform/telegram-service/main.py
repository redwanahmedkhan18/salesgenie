"""
Telegram Service Main Application
FastAPI application entry point for Telegram Bot integration.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse

from enterprise_ai_platform.common.config import settings
from enterprise_ai_platform.common.request_logging import add_request_logging
from enterprise_ai_platform.telegram_service.src.router_telegram import router

app = FastAPI(
    title="Telegram Bot Service",
    description="Integration with Telegram Bot API for messaging and notifications",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

add_request_logging(app, service_name="telegram-service")

app.include_router(router, prefix="/api/v1/telegram")


@app.get("/metrics", tags=["Monitoring"])
async def metrics_endpoint():
    """Prometheus-compatible metrics endpoint."""
    from enterprise_ai_platform.common.metrics import get_all_metrics
    all_metrics = get_all_metrics()
    lines = []
    for svc_name, mc in all_metrics.items():
        lines.append(f"# Service: {svc_name}")
        lines.append(mc.to_prometheus())
        lines.append("")
    return PlainTextResponse(content="\n".join(lines), media_type="text/plain")


@app.get("/health/live", tags=["Health Checks"])
async def liveness_probe():
    return {"status": "UP", "service": "telegram-service"}


@app.get("/health/ready", tags=["Health Checks"])
async def readiness_probe():
    """Check if the service is ready to accept requests."""
    try:
        from enterprise_ai_platform.common.config import settings
        if settings.TELEGRAM_BOT_TOKEN:
            return {"status": "READY", "service": "telegram-service"}
        return {"status": "NOT_READY", "reason": "No bot token configured"}, 503
    except Exception as e:
        return {"status": "NOT_READY", "reason": str(e)}, 503


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=settings.TELEGRAM_SERVICE_PORT)