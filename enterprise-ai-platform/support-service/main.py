"""
Support Service
Manages support tickets, live chat handoff, and customer support operations.
"""


import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse

from enterprise_ai_platform.common.config import settings
from enterprise_ai_platform.common.request_logging import add_request_logging
from enterprise_ai_platform.support_service.src.router_support import router as support_router


app = FastAPI(
    title=f"{settings.PROJECT_NAME} - Support Service",
    description="Support ticket management, live chat handoff, and customer support operations",
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


add_request_logging(app, service_name="support-service")


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
    return {"status": "UP", "service": "support-service"}


@app.get("/health/ready", tags=["Health Checks"])
async def readiness_probe():
    return {"status": "READY", "service": "support-service"}


app.include_router(support_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=settings.SUPPORT_SERVICE_PORT, reload=settings.DEBUG)