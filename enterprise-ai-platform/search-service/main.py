"""
Search Service
Manages full-text search using OpenSearch across knowledge base, customers, tickets, and conversations.
"""


import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse

from enterprise_ai_platform.common.config import settings
from enterprise_ai_platform.common.request_logging import add_request_logging
from enterprise_ai_platform.search_service.src.router_search import router as search_router


app = FastAPI(
    title=f"{settings.PROJECT_NAME} - Search Service",
    description="Full-text search across knowledge base, customers, tickets, and conversations",
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


add_request_logging(app, service_name="search-service")


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
    return {"status": "UP", "service": "search-service"}


@app.get("/health/ready", tags=["Health Checks"])
async def readiness_probe():
    return {"status": "READY", "service": "search-service"}


app.include_router(search_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=settings.SEARCH_SERVICE_PORT, reload=settings.DEBUG)