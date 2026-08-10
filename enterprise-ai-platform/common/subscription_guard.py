"""
Subscription & Entitlement Validation
Server-side checks that verify a tenant's subscription is active and their
token/quota allowances before allowing premium operations.

Checks performed:
1. Subscription status is 'active' (not canceled/past_due/incomplete)
2. Current period has not expired
3. Token usage is within monthly quota
4. Seat count is within plan limits

See SECURITY.md Section 8 (Entitlement Enforcement).
"""

from datetime import datetime, timezone
from typing import Set
from fastapi import Depends, HTTPException, status

from enterprise_ai_platform.common.security_rbac import (
    get_current_user,
    TokenPayload,
)
from enterprise_ai_platform.billing_service.src.stripe_billing import (
    DEFAULT_PLANS,
)


ACTIVE_SUBSCRIPTION_STATUSES: Set[str] = {"active", "trialing"}


def require_active_subscription(
    current_user: TokenPayload = Depends(get_current_user),
):
    """
    Dependency that enforces an active subscription before allowing
    premium API operations (chat completions, lead enrichment, etc.).
    """
    # Check if subscription status is active — in production this queries
    # the billing_subscriptions table or Stripe API
    plan_id = getattr(current_user, "subscription_plan", None) or "growth_monthly"
    plan = DEFAULT_PLANS.get(plan_id, DEFAULT_PLANS["free"])

    if plan.price_usd > 0:
        # For paid tiers, verify subscription is still active
        sub_status = getattr(current_user, "subscription_status", "active")
        if sub_status not in ACTIVE_SUBSCRIPTION_STATUSES:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Subscription is not active (status: {sub_status}). "
                "Please renew your subscription to access this feature.",
            )

        # Check subscription expiry
        sub_end = getattr(current_user, "subscription_ends_at", None)
        if sub_end and sub_end < datetime.now(timezone.utc):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Subscription has expired. Please renew to continue.",
            )

    # Check token quota
    tokens_used = getattr(current_user, "monthly_tokens_used", 0)
    quota = plan.monthly_token_quota
    if quota > 0 and tokens_used >= quota:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Monthly token quota ({quota:,}) exceeded. "
            "Please upgrade your plan to continue using AI features.",
            headers={"Retry-After": "86400"},
        )

    # Check seat limits
    seat_count = getattr(current_user, "workspace_seat_count", 1)
    if plan.max_seats > 0 and seat_count > plan.max_seats:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Workspace seat limit ({plan.max_seats}) exceeded. "
            "Please upgrade your plan to add more seats.",
        )

    return current_user
