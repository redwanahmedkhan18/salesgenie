"""
Facebook Messenger Service Main Application
FastAPI application entry point.
"""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from enterprise_ai_platform.messenger_service.src.router_messenger import router
from enterprise_ai_platform.common.config import settings

app = FastAPI(
    title="Facebook Messenger Service",
    description="Integration with Meta Facebook Messenger Platform",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1/messenger")


@app.on_event("startup")
async def startup_event():
    """Initialize service on startup."""
    pass


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown."""
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8020)