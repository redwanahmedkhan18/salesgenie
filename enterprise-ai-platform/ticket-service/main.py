"""
Ticket Microservice Entrypoint
Initializes FastAPI microservice for ticket state management and human handoff routing.
"""


import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from enterprise_ai_platform.common.config import settings
from enterprise_ai_platform.ticket_service.src.router_ticket import router as ticket_router


app = FastAPI(
    title=f"{settings.PROJECT_NAME} - Ticket Service",
    description="Customer Ticketing State Machine, Priority Queues, Refunds, & Human Agent Handoff",
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
    return {"status": "UP", "service": "ticket-service"}


@app.get("/health/ready", tags=["Health Checks"])
async def readiness_probe():
    return {"status": "READY", "service": "ticket-service"}


app.include_router(ticket_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004, reload=settings.DEBUG)
