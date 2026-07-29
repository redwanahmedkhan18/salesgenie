"""
Vector Microservice Entrypoint
Initializes FastAPI microservice for BAAI bge-m3 embeddings, pgvector HNSW search, and BAAI Reranker.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from enterprise_ai_platform.common.config import settings
from src.router_vector import router as vector_router

app = FastAPI(
    title=f"{settings.PROJECT_NAME} - Vector Service",
    description="BAAI bge-m3 1024-dim Embeddings, pgvector HNSW Index, & BAAI Re-ranking Engine",
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
    return {"status": "UP", "service": "vector-service"}


@app.get("/health/ready", tags=["Health Checks"])
async def readiness_probe():
    return {"status": "READY", "service": "vector-service"}


app.include_router(vector_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8008, reload=settings.DEBUG)
