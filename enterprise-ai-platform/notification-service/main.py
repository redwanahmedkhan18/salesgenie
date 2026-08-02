"""
Notification Service Main Application
FastAPI application entry point for multi-channel notifications.
"""

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from enterprise_ai_platform.common.config import settings
from enterprise_ai_platform.notification_service.src.router_notification import router as notification_router


app = FastAPI(
    title=f"{settings.PROJECT_NAME} - Notification Service",
    description="Multi-Channel Notifications (Email, Slack, SMS, Push, Webhooks)",
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
    return {"status": "UP", "service": "notification-service"}


@app.get("/health/ready", tags=["Health Checks"])
async def readiness_probe():
    return {"status": "READY", "service": "notification-service"}


app.include_router(notification_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=settings.NOTIFICATION_SERVICE_PORT, reload=settings.DEBUG)
