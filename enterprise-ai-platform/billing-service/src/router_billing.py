"""
Billing Service API Router
Endpoints for Stripe subscriptions, usage metering, invoices, and plan management.
"""

from typing import List, Optional
from fastapi import APIRouter, Depends, Query

from enterprise_ai_platform.common.security_rbac import (
    get_current_user,
    TokenPayload,
    RequirePermissions,
    Permission,
)
from .stripe_billing import (
    stripe_billing,
    SubscriptionDTO,
    InvoiceDTO,
    UsageDTO,
    SUBSCRIPTION_PLANS,
)

router = APIRouter(prefix="/api/v1/billing", tags=["Billing & Stripe Subscriptions"])


@router.get("/plans", summary="List Available Subscription Plans")
async def list_plans():
    """Return all available pricing tiers (Starter, Growth, Enterprise)."""
    return [
        {
            "plan_key": k,
            "name": v["name"],
            "price_usd": v["price_usd"],
            "max_seats": v["max_seats"],
            "monthly_token_quota": v["monthly_token_quota"],
        }
        for k, v in SUBSCRIPTION_PLANS.items()
    ]


@router.post(
    "/subscriptions",
    response_model=SubscriptionDTO,
    summary="Create New Stripe Subscription",
    dependencies=[Depends(RequirePermissions(Permission.BILLING_MANAGE))],
)
async def create_subscription(
    plan: str = "growth",
    current_user: TokenPayload = Depends(get_current_user),
):
    """Create a new workspace subscription for the current tenant."""
    return stripe_billing.create_subscription(tenant_id=current_user.tenant_id, plan_key=plan)


@router.get(
    "/usage",
    response_model=UsageDTO,
    summary="Get Token Usage & Billing Meter",
    dependencies=[Depends(RequirePermissions(Permission.BILLING_READ))],
)
async def get_usage(
    tokens_used: int = Query(default=2480000, description="Current monthly tokens used"),
    plan: str = Query(default="growth", description="Active subscription plan key"),
    current_user: TokenPayload = Depends(get_current_user),
):
    """Retrieve real-time token usage, quota consumption, and estimated billing cost."""
    return stripe_billing.get_usage(
        tenant_id=current_user.tenant_id,
        current_tokens_used=tokens_used,
        plan_key=plan,
    )


@router.get(
    "/invoices",
    response_model=List[InvoiceDTO],
    summary="List Billing Invoices",
    dependencies=[Depends(RequirePermissions(Permission.BILLING_READ))],
)
async def list_invoices(
    current_user: TokenPayload = Depends(get_current_user),
):
    """List paid and open invoices for the tenant workspace."""
    return [
        stripe_billing.generate_invoice(tenant_id=current_user.tenant_id, plan_key="growth"),
        stripe_billing.generate_invoice(tenant_id=current_user.tenant_id, plan_key="enterprise"),
    ]
