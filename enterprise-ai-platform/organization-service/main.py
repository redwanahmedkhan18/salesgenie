"""
Organization Microservice Entrypoint
Initializes FastAPI microservice for workspace and multi-tenant organization management.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from enterprise_ai_platform.common.config import settings
from src.router_org import router as org_router

app = FastAPI(
    title=f"{settings.PROJECT_NAME} - Organization Service",
    description="Multi-Tenant Isolation, Workspaces, Tenant Metrics, & White-label Branding",
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
    return {"status": "UP", "service": "organization-service"}


@app.get("/health/ready", tags=["Health Checks"])
async def readiness_probe():
    return {"status": "READY", "service": "organization-service"}


app.include_router(org_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8002, reload=settings.DEBUG)
