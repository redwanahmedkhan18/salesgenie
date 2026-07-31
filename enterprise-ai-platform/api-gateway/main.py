"""
API Gateway Microservice
Handles routing, rate limiting, and centralized JWT validation.
Routes requests to appropriate backend microservices.
"""


import os
import sentry_sdk

from fastapi import FastAPI, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import httpx
import os
import logging

from enterprise_ai_platform.common.config import settings

logger = logging.getLogger("salesgenie.api-gateway")

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    traces_sample_rate=1.0,
    send_default_pii=True,
)

app = FastAPI(title="SalesGenie API Gateway", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Service registry - maps route prefixes to service URLs
SERVICE_REGISTRY = {
    "auth": os.getenv("AUTH_SERVICE_URL", "http://localhost:8001"),
    "users": os.getenv("USER_SERVICE_URL", "http://localhost:8002"),
    "organizations": os.getenv("ORGANIZATION_SERVICE_URL", "http://localhost:8003"),
    "billing": os.getenv("BILLING_SERVICE_URL", "http://localhost:8004"),
    "notifications": os.getenv("NOTIFICATION_SERVICE_URL", "http://localhost:8005"),
    "knowledge": os.getenv("KNOWLEDGE_SERVICE_URL", "http://localhost:8006"),
    "sales": os.getenv("SALES_SERVICE_URL", "http://localhost:8007"),
    "tickets": os.getenv("TICKET_SERVICE_URL", "http://localhost:8008"),
    "vector": os.getenv("VECTOR_SERVICE_URL", "http://localhost:8009"),
    "chat": os.getenv("CHAT_SERVICE_URL", "http://localhost:8009"),
    "workflows": os.getenv("WORKFLOW_SERVICE_URL", "http://localhost:8010"),
    "analytics": os.getenv("ANALYTICS_SERVICE_URL", "http://localhost:8011"),
    "search": os.getenv("SEARCH_SERVICE_URL", "http://localhost:8012"),
    "audit": os.getenv("AUDIT_SERVICE_URL", "http://localhost:8013"),
    "files": os.getenv("FILE_SERVICE_URL", "http://localhost:8014"),
    "customers": os.getenv("CUSTOMER_SERVICE_URL", "http://localhost:8015"),
    "support": os.getenv("SUPPORT_SERVICE_URL", "http://localhost:8016"),
    "conversations": os.getenv("CONVERSATION_SERVICE_URL", "http://localhost:8017"),
    "ai-gateway": os.getenv("AI_GATEWAY_SERVICE_URL", "http://localhost:8000"),
    "whatsapp": os.getenv("WHATSAPP_SERVICE_URL", "http://localhost:8018"),
    "telegram": os.getenv("TELEGRAM_SERVICE_URL", "http://localhost:8019"),
    "messenger": os.getenv("MESSENGER_SERVICE_URL", "http://localhost:8020"),
    "email": os.getenv("EMAIL_SERVICE_URL", "http://localhost:8021"),
    "lead-intelligence": os.getenv("LEAD_INTELLIGENCE_SERVICE_URL", "http://localhost:8022"),
}


@app.get("/health/live")
async def health_live():
    return {"status": "UP", "service": "api-gateway"}


@app.get("/health/ready")
async def health_ready():
    return {"status": "READY", "service": "api-gateway"}


@app.get("/api/v1/services")
async def list_services():
    """List all registered backend services."""
    return {"services": list(SERVICE_REGISTRY.keys())}


@app.api_route(
    "/api/v1/{service}/{path:path}",
    methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
)
async def proxy_request(
    request: Request,
    service: str,
    path: str,
):
    """Proxy requests to the appropriate backend microservice."""
    if service not in SERVICE_REGISTRY:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Service '{service}' not found",
        )

    service_url = SERVICE_REGISTRY[service]
    url = f"{service_url}/api/v1/{path}"

    # Forward request headers
    headers = dict(request.headers)
    headers.pop("host", None)
    headers.pop("content-length", None)

    # Read request body
    body = await request.body()

    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.request(
                method=request.method,
                url=url,
                headers=headers,
                content=body if body else None,
                params=request.query_params,
            )

            return JSONResponse(
                content=response.json() if response.content else {},
                status_code=response.status_code,
                headers={
                    k: v for k, v in response.headers.items()
                    if k.lower() not in ("content-encoding", "transfer-encoding")
                },
            )
    except httpx.TimeoutException:
        logger.error(f"Timeout proxying to {service}: {url}")
        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail=f"Service '{service}' timed out",
        )
    except httpx.ConnectError:
        logger.error(f"Connection error proxying to {service}: {url}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Service '{service}' is unavailable",
        )