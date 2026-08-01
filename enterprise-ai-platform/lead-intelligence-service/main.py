"""
Lead Intelligence Service Main Application
AI-powered lead discovery, enrichment, and qualification.
"""


import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from enterprise_ai_platform.common.config import settings
from enterprise_ai_platform.lead_intelligence_service.src.router_lead_intelligence import router


app = FastAPI(
    title="SalesGenie Lead Intelligence Engine",
    description="AI-powered lead discovery, enrichment, and qualification",
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
    return {"status": "UP", "service": "lead-intelligence-service"}


@app.get("/health/ready", tags=["Health Checks"])
async def health_ready():
    return {"status": "READY", "service": "lead-intelligence-service"}


@app.on_event("startup")
async def startup_event():
    """Initialize service on startup."""
    pass


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown."""
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8022)