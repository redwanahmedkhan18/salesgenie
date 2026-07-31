"""
Workflow Microservice Entrypoint
Initializes FastAPI microservice for n8n-style workflow automation execution engine.
"""


import os
import sentry_sdk

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from enterprise_ai_platform.common.config import settings
from enterprise_ai_platform.workflow_service.src.router_workflow import router as workflow_router

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    traces_sample_rate=1.0,
    send_default_pii=True,
)

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
