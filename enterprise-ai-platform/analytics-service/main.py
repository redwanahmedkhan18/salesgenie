"""
Analytics Microservice Entrypoint
Initializes FastAPI microservice for Grafana/Prometheus metrics, performance tracking, and reports.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from enterprise_ai_platform.common.config import settings
from src.router_analytics import router as analytics_router

app = FastAPI(
    title=f"{settings.PROJECT_NAME} - Analytics Service",
    description="Prometheus/Grafana KPI Metrics, AI Accuracy Tracking, Revenue Analytics, & Export Reports",
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
    return {"status": "UP", "service": "analytics-service"}


@app.get("/health/ready", tags=["Health Checks"])
async def readiness_probe():
    return {"status": "READY", "service": "analytics-service"}


app.include_router(analytics_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8010, reload=settings.DEBUG)
