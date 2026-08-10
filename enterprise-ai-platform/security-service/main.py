"""
Security & Governance Service

AI Security Gateway, MCP Security Gateway, threat detection, and governance.

Security Standards:
- OWASP Top 10 for Web Applications
- OWASP Top 10 for LLM Applications (2025)
- OWASP Top 10 for Agentic Applications
- OWASP MCP Security Cheat Sheet
- Zero Trust Architecture
"""

import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse

from enterprise_ai_platform.common.config import settings
from enterprise_ai_platform.common.database import async_engine
from enterprise_ai_platform.common.request_logging import add_request_logging
from enterprise_ai_platform.common.security_middleware import add_security_middleware
from enterprise_ai_platform.common.rate_limiter import add_rate_limiter
from enterprise_ai_platform.security_service.src.router_security import router as security_router

logger = logging.getLogger(__name__)

app = FastAPI(
    title=f"{settings.PROJECT_NAME} - Security Service",
    description="AI Security Gateway, MCP Security Gateway, threat detection, and governance",
    version="1.0.0",
    docs_url="/docs" if settings.ENVIRONMENT != "production" else None,
    redoc_url="/redoc" if settings.ENVIRONMENT != "production" else None,
    openapi_url="/openapi.json" if settings.ENVIRONMENT != "production" else None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://salesgenie.ai", "https://app.salesgenie.ai"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["Authorization", "Content-Type", "X-Request-ID"],
)

_security_router = security_router


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
    return {"status": "UP", "service": "security-service"}


@app.get("/health/ready", tags=["Health Checks"])
async def readiness_probe():
    try:
        from sqlalchemy import select, text
        async with async_engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        return {"status": "READY", "service": "security-service", "database": "connected"}
    except Exception as e:
        logger.error(f"Database connection failed during readiness check: {e}")
        return {"status": "NOT_READY", "service": "security-service", "database": "disconnected", "error": str(e)}


app.include_router(_security_router)

add_request_logging(app, service_name="security-service")
add_security_middleware(app)
add_rate_limiter(app)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=settings.SECURITY_SERVICE_PORT, reload=settings.DEBUG)
