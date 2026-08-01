"""
Billing Microservice Entrypoint
Initializes FastAPI microservice for Stripe usage-based billing, subscriptions, and invoices.
"""

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from enterprise_ai_platform.common.config import settings
from enterprise_ai_platform.billing_service.src.router_billing import router as billing_router


app = FastAPI(
    title=f"{settings.PROJECT_NAME} - Billing Service",
    description="Stripe Usage-Based Subscriptions (Starter/Growth/Enterprise), Token Metering, & Invoice Management",
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
    return {"status": "UP", "service": "billing-service"}


@app.get("/health/ready", tags=["Health Checks"])
async def readiness_probe():
    return {"status": "READY", "service": "billing-service"}


app.include_router(billing_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004, reload=settings.DEBUG)