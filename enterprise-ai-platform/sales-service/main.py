"""
Sales Microservice Entrypoint
Initializes FastAPI microservice for AI lead qualification, product recommendations, and calendar bookings.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from enterprise_ai_platform.common.config import settings
from src.router_sales import router as sales_router

app = FastAPI(
    title=f"{settings.PROJECT_NAME} - Sales Service",
    description="Lead Qualification Engines, Product Recommendations, Upsell Decision Nodes, & Calendar Booking",
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
    return {"status": "UP", "service": "sales-service"}


@app.get("/health/ready", tags=["Health Checks"])
async def readiness_probe():
    return {"status": "READY", "service": "sales-service"}


app.include_router(sales_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8005, reload=settings.DEBUG)
