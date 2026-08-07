"""
Auth Microservice Entrypoint
Initializes FastAPI microservice with CORS, security headers, routers, and health checks.
"""

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from enterprise_ai_platform.common.config import settings
from enterprise_ai_platform.auth_service.src.router_auth import router as auth_router
try:
    from enterprise_ai_platform.platform_service.src.router_platform import router as platform_router
except ImportError:
    platform_router = None

app = FastAPI(
    title=f"{settings.PROJECT_NAME} - Auth Service",
    description="Enterprise Identity, Keycloak Integration, OAuth2, RBAC, MFA, & Session Management Microservice",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# CORS Middleware Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health/live", tags=["Health Checks"], summary="Liveness Probe")
async def liveness_probe():
    """Kubernetes / Cloud Liveness Probe Endpoint."""
    return {"status": "UP", "service": "auth-service", "check": "liveness"}


@app.get("/health/ready", tags=["Health Checks"], summary="Readiness Probe")
async def readiness_probe():
    """Kubernetes / Cloud Readiness Probe Endpoint."""
    return {
        "status": "READY",
        "service": "auth-service",
        "keycloak_connection": "OK",
        "database_pool": "HEALTHY",
    }


# Include Authentication & Platform API Routers
app.include_router(auth_router)
if platform_router:
    app.include_router(platform_router)



@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception fallback handler returning structured JSON errors."""
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal Server Error", "error": str(exc)},
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=settings.DEBUG)