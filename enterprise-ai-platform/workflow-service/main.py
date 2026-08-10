"""
Workflow Microservice Entrypoint
Initializes FastAPI microservice for n8n-style workflow automation execution engine.
"""


import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse

from enterprise_ai_platform.common.config import settings
from enterprise_ai_platform.common.request_logging import add_request_logging
from enterprise_ai_platform.workflow_service.src.router_workflow import router as workflow_router


app = FastAPI(
    title=f"{settings.PROJECT_NAME} - Workflow Service",
    description="n8n DAG Workflow Automation: Start, LLM, Condition, Email, CRM, API, Human, Database, Delay, End",
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


add_request_logging(app, service_name="workflow-service")


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
    return {"status": "UP", "service": "workflow-service"}


@app.get("/health/ready", tags=["Health Checks"])
async def readiness_probe():
    return {"status": "READY", "service": "workflow-service"}


app.include_router(workflow_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8012, reload=settings.DEBUG)
