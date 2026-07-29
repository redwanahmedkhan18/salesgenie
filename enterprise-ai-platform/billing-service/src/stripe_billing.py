"""
Stripe Billing Engine
Manages subscription plans, usage-based metering, invoice creation, and coupon redemption.
"""

import uuid
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional
from pydantic import BaseModel
import logging

logger = logging.getLogger("salesgenie.billing.stripe")


SUBSCRIPTION_PLANS = {
    "starter": {
        "name": "Starter",
        "price_usd": 49.0,
        "max_seats": 5,
        "monthly_token_quota": 1_000_000,
        "stripe_price_id": "price_starter_monthly",
    },
    "growth": {
        "name": "Growth",
        "price_usd": 149.0,
        "max_seats": 25,
        "monthly_token_quota": 10_000_000,
        "stripe_price_id": "price_growth_monthly",
    },
    "enterprise": {
        "name": "Enterprise",
        "price_usd": 499.0,
        "max_seats": -1,  # Unlimited
        "monthly_token_quota": 100_000_000,
        "stripe_price_id": "price_enterprise_monthly",
    },
}


class SubscriptionDTO(BaseModel):
    subscription_id: str
    tenant_id: str
    plan: str
    price_usd: float
    max_seats: int
    monthly_token_quota: int
    status: str
    current_period_end: datetime


class InvoiceDTO(BaseModel):
    invoice_id: str
    tenant_id: str
    amount_due_usd: float
    status: str  # 'paid', 'open', 'void'
    created_at: datetime
    invoice_url: str


class UsageDTO(BaseModel):
    tenant_id: str
    current_tokens_used: int
    monthly_token_quota: int
    usage_percent: float
    estimated_cost_usd: float


class StripeBillingEngine:
    """Stripe payment and subscription lifecycle management engine."""

    @staticmethod
    def create_subscription(tenant_id: str, plan_key: str) -> SubscriptionDTO:
        """Create a new Stripe subscription for an organization workspace."""
        plan = SUBSCRIPTION_PLANS.get(plan_key, SUBSCRIPTION_PLANS["growth"])
        logger.info(f"Creating {plan_key} subscription for tenant {tenant_id}")

        return SubscriptionDTO(
            subscription_id=f"sub_{uuid.uuid4().hex[:16]}",
            tenant_id=tenant_id,
            plan=plan["name"],
            price_usd=plan["price_usd"],
            max_seats=plan["max_seats"],
            monthly_token_quota=plan["monthly_token_quota"],
            status="active",
            current_period_end=datetime(2026, 8, 29, tzinfo=timezone.utc),
        )

    @staticmethod
    def get_usage(tenant_id: str, current_tokens_used: int, plan_key: str) -> UsageDTO:
        """Returns token usage billing metrics for the current billing cycle."""
        plan = SUBSCRIPTION_PLANS.get(plan_key, SUBSCRIPTION_PLANS["growth"])
        quota = plan["monthly_token_quota"]
        cost_per_1m_tokens = 0.60
        estimated_cost = (current_tokens_used / 1_000_000) * cost_per_1m_tokens

        return UsageDTO(
            tenant_id=tenant_id,
            current_tokens_used=current_tokens_used,
            monthly_token_quota=quota,
            usage_percent=round((current_tokens_used / quota) * 100, 2),
            estimated_cost_usd=round(estimated_cost, 4),
        )

    @staticmethod
    def generate_invoice(tenant_id: str, plan_key: str) -> InvoiceDTO:
        """Generates an invoice for the current subscription period."""
        plan = SUBSCRIPTION_PLANS.get(plan_key, SUBSCRIPTION_PLANS["growth"])
        invoice_id = f"inv_{uuid.uuid4().hex[:12]}"

        return InvoiceDTO(
            invoice_id=invoice_id,
            tenant_id=tenant_id,
            amount_due_usd=plan["price_usd"],
            status="paid",
            created_at=datetime.now(timezone.utc),
            invoice_url=f"https://billing.salesgenie.ai/invoices/{invoice_id}.pdf",
        )


stripe_billing = StripeBillingEngine()
