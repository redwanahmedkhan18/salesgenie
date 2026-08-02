"""
Auth Service - Main entry point
"""
from enterprise_ai_platform.auth_service.src.main import app

if __name__ == "__main__":
    import uvicorn
    from enterprise_ai_platform.common.config import settings
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=settings.AUTH_SERVICE_PORT,
        reload=settings.DEBUG,
    )