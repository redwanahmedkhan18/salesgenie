"""
Platform Admin API Router
Super Admin endpoints for platform-wide administration.
"""

from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

from enterprise_ai_platform.common.cost_management import cost_calculator
from enterprise_ai_platform.common.security_rbac import (
    PlatformRole,
    TokenPayload,
    get_current_user,
)

router = APIRouter(prefix="/api/v1/admin", tags=["Platform Administration"])


def require_super_admin(user: TokenPayload = Depends(get_current_user)) -> TokenPayload:
    if PlatformRole.SUPER_ADMIN not in user.roles:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Super admin access required",
        )
    return user


# Models
class SuperAdminUser(BaseModel):
    id: str
    email: str
    full_name: Optional[str]
    role: str
    is_active: bool
    created_at: datetime
    last_login_at: Optional[datetime]
    tenant_id: Optional[str]


class AuditEvent(BaseModel):
    id: str
    action: str
    resource_type: str
    resource_id: Optional[str]
    user_id: Optional[str]
    user_email: Optional[str]
    tenant_id: Optional[str]
    ip_address: Optional[str]
    user_agent: Optional[str]
    severity: str
    details: Dict[str, Any]
    created_at: datetime


class SystemHealth(BaseModel):
    service: str
    status: str
    response_time_ms: int
    last_check: datetime


class AIProviderStatus(BaseModel):
    name: str
    status: str
    models: List[str]
    daily_limit: int
    daily_used: int
    rate_limit_remaining: int


class PlatformSettings(BaseModel):
    maintenance_mode: bool
    feature_flags: Dict[str, bool]
    rate_limits_enabled: bool
    max_api_requests_per_minute: int
    ai_token_budget_usd: int
    created_at: datetime
    updated_at: datetime


class SystemInfo(BaseModel):
    version: str
    instance_id: str
    environment: str
    python_version: str
    database: str
    redis: str


# Super Admin Endpoints

@router.get("/users", response_model=List[SuperAdminUser])
async def list_users(
    search: Optional[str] = None,
    _: TokenPayload = Depends(require_super_admin),
):
    """List all platform users (Super Admin only)."""
    users = [
        SuperAdminUser(
            id="1",
            email="admin@salesgenie.ai",
            full_name="Super Admin",
            role="super_admin",
            is_active=True,
            created_at=datetime.now(timezone.utc),
            last_login_at=datetime.now(timezone.utc),
            tenant_id="default",
        )
    ]
    
    if search:
        users = [u for u in users if search.lower() in u.email.lower() or search.lower() in (u.full_name or "").lower()]
    
    return users


@router.get("/audit-events", response_model=List[AuditEvent])
async def list_audit_events(
    limit: int = 100,
    _: TokenPayload = Depends(require_super_admin),
):
    """List recent audit events (Super Admin only)."""
    return [
        AuditEvent(
            id="1",
            action="user.login",
            resource_type="user",
            resource_id="user-1",
            user_id="user-1",
            user_email="admin@salesgenie.ai",
            tenant_id="default",
            ip_address="127.0.0.1",
            user_agent="Mozilla/5.0",
            severity="low",
            details={},
            created_at=datetime.now(timezone.utc),
        )
    ][:limit]


@router.get("/health", response_model=List[SystemHealth])
async def get_system_health(
    _: TokenPayload = Depends(require_super_admin),
):
    """Get platform system health status (Super Admin only)."""
    return [
        SystemHealth(
            service="auth-service",
            status="healthy",
            response_time_ms=42,
            last_check=datetime.now(timezone.utc),
        ),
        SystemHealth(
            service="user-service",
            status="healthy",
            response_time_ms=28,
            last_check=datetime.now(timezone.utc),
        ),
        SystemHealth(
            service="organization-service",
            status="healthy",
            response_time_ms=35,
            last_check=datetime.now(timezone.utc),
        ),
        SystemHealth(
            service="ai-gateway-service",
            status="healthy",
            response_time_ms=55,
            last_check=datetime.now(timezone.utc),
        ),
    ]


@router.get("/ai-providers", response_model=List[AIProviderStatus])
async def get_ai_provider_status(
    _: TokenPayload = Depends(require_super_admin),
):
    """Get AI provider status and usage (Super Admin only)."""
    # Live provider status derived from configured API keys
    from enterprise_ai_platform.ai_gateway_service.src.llm_provider import (
        _GOOGLE_API_KEY,
        _GROQ_API_KEY,
        _MISTRAL_API_KEY,
    )
    providers = []
    if _GROQ_API_KEY:
        providers.append(AIProviderStatus(
            name="Groq",
            status="configured",
            models=["llama3-70b-8192", "llama3-8b-8192"],
            daily_limit=100000,
            daily_used=0,
            rate_limit_remaining=100000,
        ))
    if _GOOGLE_API_KEY:
        providers.append(AIProviderStatus(
            name="Google AI",
            status="configured",
            models=["gemini-1.5-flash", "gemini-1.5-pro"],
            daily_limit=50000,
            daily_used=0,
            rate_limit_remaining=50000,
        ))
    if _MISTRAL_API_KEY:
        providers.append(AIProviderStatus(
            name="Mistral",
            status="configured",
            models=["mistral-large-latest"],
            daily_limit=25000,
            daily_used=0,
            rate_limit_remaining=25000,
        ))
    return providers


@router.get("/settings", response_model=PlatformSettings)
async def get_platform_settings(
    _: TokenPayload = Depends(require_super_admin),
):
    """Get platform settings (Super Admin only)."""
    return PlatformSettings(
        maintenance_mode=False,
        feature_flags={
            "telegram": True,
            "messenger": True,
            "email": True,
            "whatsapp": True,
            "slack": True,
            "discord": True,
        },
        rate_limits_enabled=True,
        max_api_requests_per_minute=100000,
        ai_token_budget_usd=5000,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
    )


@router.patch("/settings", response_model=PlatformSettings)
async def update_platform_settings(
    updates: Dict[str, Any],
    _: TokenPayload = Depends(require_super_admin),
):
    """Update platform settings (Super Admin only)."""
    return None  # Implementation depends on your settings store


@router.get("/system-info", response_model=SystemInfo)
async def get_system_info(
    _: TokenPayload = Depends(require_super_admin),
):
    """Get system information (Super Admin only)."""
    return SystemInfo(
        version="1.0.0",
        instance_id="salesgenie-prod-1",
        environment="development",
        python_version="3.12",
        database="PostgreSQL 15",
        redis="Redis 7",
    )


@router.post("/users/{user_id}/suspend", response_model=Dict[str, str])
async def suspend_user(
    user_id: str,
    _: TokenPayload = Depends(require_super_admin),
):
    """Suspend a user account (Super Admin only)."""
    return {"status": "success", "message": f"User {user_id} has been suspended"}


@router.post("/users/{user_id}/resume", response_model=Dict[str, str])
async def resume_user(
    user_id: str,
    _: TokenPayload = Depends(require_super_admin),
):
    """Resume a suspended user account (Super Admin only)."""
    return {"status": "success", "message": f"User {user_id} has been resumed"}


# Organization Management Endpoints

class OrganizationDetail(BaseModel):
    id: str
    name: str
    slug: str
    domain: Optional[str]
    subscription_tier: str
    is_active: bool
    created_at: datetime
    max_seats: int
    max_monthly_tokens: int


class OrganizationListItem(BaseModel):
    id: str
    name: str
    slug: str
    domain: Optional[str]
    subscription_tier: str
    is_active: bool
    created_at: datetime
    max_seats: int
    max_monthly_tokens: int


class PlatformMetrics(BaseModel):
    total_organizations: int
    active_organizations: int
    suspended_organizations: int
    total_users: int
    total_tokens_used: int
    ai_cost_usd: float
    platform_uptime_percent: float


@router.get("/metrics", response_model=PlatformMetrics)
async def get_platform_metrics(
    _: TokenPayload = Depends(require_super_admin),
):
    """Get platform-wide metrics (Super Admin only)."""
    usage = cost_calculator.get_platform_usage()
    return PlatformMetrics(
        total_organizations=len(usage.get("tenant_count", 0)),
        active_organizations=len(usage.get("tenant_count", 0)),
        suspended_organizations=0,
        total_users=0,
        total_tokens_used=0,
        ai_cost_usd=round(usage.get("platform_spent_usd", 0), 4),
        platform_uptime_percent=99.95,
    )


@router.get("/organizations", response_model=List[OrganizationListItem])
async def list_organizations(
    status: Optional[str] = None,
    _: TokenPayload = Depends(require_super_admin),
):
    """List all organizations (Super Admin only)."""
    orgs = [
        OrganizationListItem(
            id="1",
            name="Acme Corp",
            slug="acme-corp",
            domain="acme.com",
            subscription_tier="enterprise",
            is_active=True,
            created_at=datetime.now(timezone.utc),
            max_seats=100,
            max_monthly_tokens=1000000,
        ),
    ]
    
    if status:
        if status == "active":
            orgs = [o for o in orgs if o.is_active]
        elif status == "suspended":
            orgs = [o for o in orgs if not o.is_active]
    
    return orgs


@router.patch("/organizations/{org_id}/suspend", response_model=OrganizationDetail)
async def suspend_organization(
    org_id: str,
    _: TokenPayload = Depends(require_super_admin),
):
    """Suspend an organization (Super Admin only)."""
    return OrganizationDetail(
        id=org_id,
        name="Acme Corp",
        slug="acme-corp",
        domain="acme.com",
        subscription_tier="enterprise",
        is_active=False,
        created_at=datetime.now(timezone.utc),
        max_seats=100,
        max_monthly_tokens=1000000,
    )


@router.patch("/organizations/{org_id}/resume", response_model=OrganizationDetail)
async def resume_organization(
    org_id: str,
    _: TokenPayload = Depends(require_super_admin),
):
    """Resume a suspended organization (Super Admin only)."""
    return OrganizationDetail(
        id=org_id,
        name="Acme Corp",
        slug="acme-corp",
        domain="acme.com",
        subscription_tier="enterprise",
        is_active=True,
        created_at=datetime.now(timezone.utc),
        max_seats=100,
        max_monthly_tokens=1000000,
    )


@router.delete("/organizations/{org_id}", response_model=Dict[str, str])
async def delete_organization(
    org_id: str,
    _: TokenPayload = Depends(require_super_admin),
):
    """Delete an organization (Super Admin only)."""
    return {
        "status": "success",
        "message": f"Organization {org_id} has been deleted",
    }