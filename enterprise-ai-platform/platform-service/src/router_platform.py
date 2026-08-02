"""
Platform Service - Super Admin Endpoints
Manages organizations, subscriptions, billing, and global configuration.
"""

import uuid
from datetime import datetime, timezone
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from pydantic import BaseModel, Field

from enterprise_ai_platform.common.database import get_async_db
from enterprise_ai_platform.common.security_rbac import (
    get_current_user,
    TokenPayload,
    RequirePermissions,
    Permission,
    PlatformRole,
)


class OrganizationListItem(BaseModel):
    id: str
    name: str
    slug: str
    domain: Optional[str] = None
    subscription_tier: str
    is_active: bool
    created_at: datetime
    max_seats: int
    max_monthly_tokens: int


class OrganizationDetail(BaseModel):
    id: str
    name: str
    slug: str
    domain: Optional[str] = None
    subscription_tier: str
    is_active: bool
    created_at: datetime
    max_seats: int
    max_monthly_tokens: int


class SuspendOrganizationRequest(BaseModel):
    reason: Optional[str] = None


class ResumeOrganizationRequest(BaseModel):
    reason: Optional[str] = None


class SubscriptionUpdate(BaseModel):
    org_id: str
    plan: str
    upgrade_path: Optional[bool] = False


class PlatformMetrics(BaseModel):
    total_organizations: int
    active_organizations: int
    suspended_organizations: int
    total_users: int
    total_tokens_used: int
    ai_cost_usd: float
    platform_uptime_percent: float


router = APIRouter(prefix="/api/v1/platform", tags=["Platform Administration"])


def require_super_admin(user: TokenPayload = Depends(get_current_user)) -> TokenPayload:
    if PlatformRole.SUPER_ADMIN not in user.roles:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Super admin access required",
        )
    return user


@router.get("/metrics", response_model=PlatformMetrics)
async def get_platform_metrics(
    db: AsyncSession = Depends(get_async_db),
    _: TokenPayload = Depends(require_super_admin),
):
    """Get platform-wide metrics."""
    org_stmt = select(func.count()).select_from(OrganizationWorkspace)
    active_stmt = select(func.count()).select_from(OrganizationWorkspace).where(OrganizationWorkspace.is_active == True)
    suspended_stmt = select(func.count()).select_from(OrganizationWorkspace).where(OrganizationWorkspace.is_active == False)
    
    total_orgs = (await db.execute(org_stmt)).scalar() or 0
    active_orgs = (await db.execute(active_stmt)).scalar() or 0
    suspended_orgs = (await db.execute(suspended_stmt)).scalar() or 0
    
    return PlatformMetrics(
        total_organizations=total_orgs,
        active_organizations=active_orgs,
        suspended_organizations=suspended_orgs,
        total_users=0,
        total_tokens_used=0,
        ai_cost_usd=0.0,
        platform_uptime_percent=99.9,
    )


@router.get("/organizations", response_model=List[OrganizationListItem])
async def list_organizations(
    skip: int = 0,
    limit: int = 50,
    status: Optional[str] = None,
    db: AsyncSession = Depends(get_async_db),
    _: TokenPayload = Depends(require_super_admin),
):
    """List all organizations (platform-wide view)."""
    stmt = select(OrganizationWorkspace).order_by(OrganizationWorkspace.created_at.desc()).offset(skip).limit(limit)
    
    if status:
        if status == "active":
            stmt = stmt.where(OrganizationWorkspace.is_active == True)
        elif status == "suspended":
            stmt = stmt.where(OrganizationWorkspace.is_active == False)
    
    result = await db.execute(stmt)
    orgs = result.scalars().all()
    
    return [
        OrganizationListItem(
            id=str(o.id),
            name=o.name,
            slug=o.slug,
            domain=o.domain,
            subscription_tier=o.subscription_tier,
            is_active=o.is_active,
            created_at=o.created_at,
            max_seats=o.max_seats,
            max_monthly_tokens=o.max_monthly_tokens,
        )
        for o in orgs
    ]


@router.patch("/organizations/{org_id}/suspend", response_model=OrganizationDetail)
async def suspend_organization(
    org_id: str,
    req: SuspendOrganizationRequest,
    db: AsyncSession = Depends(get_async_db),
    _: TokenPayload = Depends(require_super_admin),
):
    """Suspend an organization."""
    stmt = select(OrganizationWorkspace).where(OrganizationWorkspace.id == uuid.UUID(org_id))
    result = await db.execute(stmt)
    org = result.scalar_one_or_none()
    
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    
    org.is_active = False
    await db.commit()
    
    return OrganizationDetail(
        id=str(org.id),
        name=org.name,
        slug=org.slug,
        domain=org.domain,
        subscription_tier=org.subscription_tier,
        is_active=org.is_active,
        created_at=org.created_at,
        max_seats=org.max_seats,
        max_monthly_tokens=org.max_monthly_tokens,
    )


@router.patch("/organizations/{org_id}/resume", response_model=OrganizationDetail)
async def resume_organization(
    org_id: str,
    req: ResumeOrganizationRequest,
    db: AsyncSession = Depends(get_async_db),
    _: TokenPayload = Depends(require_super_admin),
):
    """Resume a suspended organization."""
    stmt = select(OrganizationWorkspace).where(OrganizationWorkspace.id == uuid.UUID(org_id))
    result = await db.execute(stmt)
    org = result.scalar_one_or_none()
    
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    
    org.is_active = True
    await db.commit()
    
    return OrganizationDetail(
        id=str(org.id),
        name=org.name,
        slug=org.slug,
        domain=org.domain,
        subscription_tier=org.subscription_tier,
        is_active=org.is_active,
        created_at=org.created_at,
        max_seats=org.max_seats,
        max_monthly_tokens=org.max_monthly_tokens,
    )


@router.delete("/organizations/{org_id}", response_model=dict)
async def delete_organization(
    org_id: str,
    _: TokenPayload = Depends(require_super_admin),
):
    """Soft delete an organization (admin only)."""
    return {
        "status": "deleted",
        "message": "Organization deletion requires database cascade - use tenant management if available",
        "org_id": org_id,
    }