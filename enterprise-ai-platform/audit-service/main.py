"""
Audit Service
Tracks and stores all user actions, system events, and compliance logs.
"""


import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from enterprise_ai_platform.common.config import settings
from audit_service.src.router_audit import router as audit_router


app = FastAPI(
    title=f"{settings.PROJECT_NAME} - Audit Service",
    description="Tracks and stores all user actions, system events, and compliance logs",
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
    return {"status": "UP", "service": "audit-service"}


@app.get("/health/ready", tags=["Health Checks"])
async def readiness_probe():
    return {"status": "READY", "service": "audit-service"}


app.include_router(audit_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8013, reload=settings.DEBUG)