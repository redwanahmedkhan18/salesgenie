"""
WhatsApp Service Main Application
FastAPI application entry point.
"""


import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse

from enterprise_ai_platform.common.config import settings
from enterprise_ai_platform.common.request_logging import add_request_logging
from enterprise_ai_platform.whatsapp_service.src.router_whatsapp import router


app = FastAPI(
    title="WhatsApp Business API Service",
    description="Integration with Meta WhatsApp Business Cloud API",
    version="1.0.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

add_request_logging(app, service_name="whatsapp-service")

# Include routers
app.include_router(router)


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
async def health_live():
    return {"status": "UP", "service": "whatsapp-service"}


@app.get("/health/ready", tags=["Health Checks"])
async def health_ready():
    return {"status": "READY", "service": "whatsapp-service"}


@app.on_event("startup")
async def startup_event():
    """Initialize service on startup."""
    pass


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown."""
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=settings.WHATSAPP_SERVICE_PORT)