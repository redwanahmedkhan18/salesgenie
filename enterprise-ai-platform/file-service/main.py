"""
File Service
Manages file storage, uploads, downloads, and metadata using MinIO.
"""


import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from enterprise_ai_platform.common.config import settings
from enterprise_ai_platform.file_service.src.router_files import router as files_router


app = FastAPI(
    title=f"{settings.PROJECT_NAME} - File Service",
    description="Manages file storage, uploads, downloads, and metadata using MinIO",
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
    return {"status": "UP", "service": "file-service"}


@app.get("/health/ready", tags=["Health Checks"])
async def readiness_probe():
    return {"status": "READY", "service": "file-service"}


app.include_router(files_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8014, reload=settings.DEBUG)