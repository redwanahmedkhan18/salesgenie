"""
Platform Service Models
"""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field


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