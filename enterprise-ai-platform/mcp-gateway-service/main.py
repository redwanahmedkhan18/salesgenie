"""
MCP Gateway Service Main Application
Controlled MCP tool gateway for SalesGenie AI agents.
"""

import logging

import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from sqlalchemy import select

from enterprise_ai_platform.common.config import settings
from enterprise_ai_platform.common.database import async_engine, get_async_db
from enterprise_ai_platform.common.request_logging import add_request_logging
from enterprise_ai_platform.common.security_middleware import add_security_middleware
from enterprise_ai_platform.common.rate_limiter import add_rate_limiter
from enterprise_ai_platform.mcp_gateway_service.src.router_mcp import router, MCPTool
from sqlalchemy.ext.asyncio import AsyncSession

logger = logging.getLogger(__name__)


app = FastAPI(
    title="SalesGenie MCP Gateway",
    description="Controlled MCP tool gateway for AI agents",
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
    return {"status": "UP", "service": "mcp-gateway-service"}


@app.get("/health/ready", tags=["Health Checks"])
async def health_ready():
    try:
        from sqlalchemy import select, text
        async with async_engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        return {"status": "READY", "service": "mcp-gateway-service", "database": "connected"}
    except Exception as e:
        logger.error(f"Database connection failed during readiness check: {e}")
        return {"status": "NOT_READY", "service": "mcp-gateway-service", "database": "disconnected", "error": str(e)}


@app.get("/health/tools", tags=["Health Checks"])
async def health_tools(db: AsyncSession = Depends(get_async_db)):
    """List all available MCP tools."""
    result = await db.execute(select(MCPTool).where(MCPTool.enabled == True))
    tools = result.scalars().all()
    await db.close()
    return {
        "total_tools": len(tools),
        "tools": [{"name": t.name, "category": t.category, "servers": [t.server_name]} for t in tools],
    }


add_request_logging(app, service_name="mcp-gateway-service")
add_security_middleware(app)
add_rate_limiter(app)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.MCP_GATEWAY_SERVICE_PORT)
