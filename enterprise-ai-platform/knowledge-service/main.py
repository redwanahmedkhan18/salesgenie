"""
Knowledge Base Microservice Entrypoint
Initializes FastAPI microservice for document ingestion, chunking, OCR, and audio pipelines.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from enterprise_ai_platform.common.config import settings
from src.router_knowledge import router as knowledge_router

app = FastAPI(
    title=f"{settings.PROJECT_NAME} - Knowledge Service",
    description="Document Ingestion, Recursive Chunking, OCR (Tesseract), Whisper STT, & Coqui TTS",
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
    return {"status": "UP", "service": "knowledge-service"}


@app.get("/health/ready", tags=["Health Checks"])
async def readiness_probe():
    return {"status": "READY", "service": "knowledge-service"}


app.include_router(knowledge_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8007, reload=settings.DEBUG)
