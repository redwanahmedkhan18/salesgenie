"""
WhatsApp Service Main Application
FastAPI application entry point.
"""


import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from enterprise_ai_platform.whatsapp_service.src.router_whatsapp import router
from enterprise_ai_platform.common.config import settings


app = FastAPI(
    title="WhatsApp Business API Service",
    description="Integration with Meta WhatsApp Business Cloud API",
    version="1.0.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(router)


@app.get("/health/live", tags=["Health Checks"])
async def health_live():
    return {"status": "UP", "service": "whatsapp-service"}


@app.get("/health/ready", tags=["Health Checks"])
async def health_ready():
    return {"status": "READY", "service": "whatsapp-service"}


@app.on_event("startup")
async def startup_event():
    """Initialize service on startup."""
    pass


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown."""
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8005)