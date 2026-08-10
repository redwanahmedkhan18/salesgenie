"""
Product Intelligence Service Main Application
AI-powered market research, competitor analysis, and product launch strategy.
"""

import logging

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse

from enterprise_ai_platform.common.config import settings
from enterprise_ai_platform.common.database import async_engine
from enterprise_ai_platform.common.request_logging import add_request_logging
from enterprise_ai_platform.common.security_middleware import add_security_middleware
from enterprise_ai_platform.common.rate_limiter import add_rate_limiter
from enterprise_ai_platform.product_intelligence_service.src.router_product_intelligence import router

logger = logging.getLogger(__name__)


app = FastAPI(
    title="SalesGenie Product Intelligence Engine",
    description="AI-powered market research, competitor analysis, and product launch strategy",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS_LIST,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["Authorization", "Content-Type", "X-Request-ID"],
)

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
    return {"status": "UP", "service": "product-intelligence-service"}


@app.get("/health/ready", tags=["Health Checks"])
async def health_ready():
    try:
        from sqlalchemy import select, text
        async with async_engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        return {"status": "READY", "service": "product-intelligence-service", "database": "connected"}
    except Exception as e:
        logger.error(f"Database connection failed during readiness check: {e}")
        return {"status": "NOT_READY", "service": "product-intelligence-service", "database": "disconnected", "error": str(e)}


@app.on_event("startup")
async def startup_event():
    pass


@app.on_event("shutdown")
async def shutdown_event():
    pass


add_request_logging(app, service_name="product-intelligence-service")
add_security_middleware(app)
add_rate_limiter(app)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.PRODUCT_INTELLIGENCE_SERVICE_PORT)
