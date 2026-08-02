"""
Stripe Billing Engine with PDF Receipt Generation
Manages subscription plans, usage metering, invoices, and automatic downgrades.
PDF generation uses reportlab for lightweight, server-side generation.
"""

import uuid
from datetime import datetime, timezone, timedelta
from typing import Dict, Any, List, Optional
from pydantic import BaseModel
import logging
import io
import base64

logger = logging.getLogger("salesgenie.billing.stripe")

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    from reportlab.lib import colors
    from reportlab.lib.units import inch
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False
    canvas = None


class BillingPlan:
    """Subscription plan definition."""
    def __init__(
        self,
        id: str,
        name: str,
        interval: str,
        price_usd: float,
        max_seats: int,
        monthly_token_quota: int,
        is_free_trial_eligible: bool = True,
        is_default: bool = False,
        features: Dict[str, Any] = None
    ):
        self.id = id
        self.name = name
        self.interval = interval  # 'monthly' or 'yearly'
        self.price_usd = price_usd
        self.max_seats = max_seats
        self.monthly_token_quota = monthly_token_quota
        self.is_free_trial_eligible = is_free_trial_eligible
        self.is_default = is_default
        self.features = features or {}

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "interval": self.interval,
            "price_usd": self.price_usd,
            "max_seats": self.max_seats,
            "monthly_token_quota": self.monthly_token_quota,
            "is_free_trial_eligible": self.is_free_trial_eligible,
            "is_default": self.is_default,
            "features": self.features,
        }


class FreeTierPlan(BillingPlan):
    """Free tier plan with token limits."""
    def __init__(self):
        super().__init__(
            id="free",
            name="Free Tier",
            interval="monthly",
            price_usd=0.0,
            max_seats=1,
            monthly_token_quota=100000,
            is_free_trial_eligible=False,
            is_default=True,
            features={
                "knowledge_base": True,
                "agents": 1,
                "support": False,
                "analytics": False,
                "teams": False,
                "token_reset_interval_seconds": 3600
            }
        )


class SubscriptionDTO(BaseModel):
    subscription_id: str
    tenant_id: str
    plan_id: str
    plan_name: str
    stripe_customer_id: str
    stripe_subscription_id: Optional[str] = None
    status: str
    current_period_start: datetime
    current_period_end: datetime
    cancel_at_period_end: bool = False
    trial_ends_at: Optional[datetime] = None
    price_usd: float
    max_seats: int
    monthly_token_quota: int


class InvoiceDTO(BaseModel):
    invoice_id: str
    tenant_id: str
    subscription_id: str
    plan_id: str
    amount_usd: float
    status: str
    created_at: datetime
    due_date: Optional[datetime] = None
    paid_at: Optional[datetime] = None
    invoice_url: str
    pdf_base64: Optional[str] = None


class UsageDTO(BaseModel):
    tenant_id: str
    plan_id: str
    current_tokens_used: int
    monthly_token_quota: int
    usage_percent: float
    estimated_cost_usd: float
    is_at_risk: bool = False


class WebhookDTO(BaseModel):
    id: str
    tenant_id: Optional[str]
    event_type: str
    data: Dict[str, Any]
    processed: bool = False
    created_at: datetime


DEFAULT_PLANS = {
    "free": FreeTierPlan(),
    "starter_monthly": BillingPlan(
        id="starter_monthly", name="Starter (Monthly)", interval="monthly",
        price_usd=49.0, max_seats=5, monthly_token_quota=1000000,
        features={"knowledge_base": True, "agents": 3, "support": True, "analytics": True}
    ),
    "starter_yearly": BillingPlan(
        id="starter_yearly", name="Starter (Yearly)", interval="yearly",
        price_usd=499.0, max_seats=5, monthly_token_quota=11000000,
        features={"knowledge_base": True, "agents": 3, "support": True, "analytics": True}
    ),
    "growth_monthly": BillingPlan(
        id="growth_monthly", name="Growth (Monthly)", interval="monthly",
        price_usd=149.0, max_seats=25, monthly_token_quota=10000000,
        features={"knowledge_base": True, "agents": 10, "support": True, "analytics": True, "teams": True}
    ),
    "growth_yearly": BillingPlan(
        id="growth_yearly", name="Growth (Yearly)", interval="yearly",
        price_usd=1499.0, max_seats=25, monthly_token_quota=11000000,
        features={"knowledge_base": True, "agents": 10, "support": True, "analytics": True, "teams": True}
    ),
    "enterprise": BillingPlan(
        id="enterprise", name="Enterprise", interval="yearly",
        price_usd=4999.0, max_seats=-1, monthly_token_quota=100000000,
        is_free_trial_eligible=False,
        features={"knowledge_base": True, "agents": -1, "support": True, "analytics": True, "teams": True, "custom_ai": True}
    ),
}


def generate_pdf_invoice(invoice_data: dict) -> Optional[bytes]:
    """Generate PDF invoice using reportlab."""
    if not PDF_AVAILABLE:
        logger.warning("reportlab not available, skipping PDF generation")
        return None

    try:
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        story = []

        styles = getSampleStyleSheet()
        title = Paragraph("INVOICE", styles['Title'])
        story.append(title)
        story.append(Spacer(1, 12))

        data = [
            ["Field", "Value"],
            ["Invoice ID", invoice_data['invoice_id']],
            ["Plan Name", invoice_data['plan_name']],
            ["Amount", f"${invoice_data['amount_usd']:.2f}"],
            ["Date", invoice_data['created_at'].strftime('%Y-%m-%d')],
        ]

        tbl = Table(data, colWidths=[2*inch, 3*inch])
        tbl.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.grey),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('ALIGN', (0,0), (-1,-1), 'LEFT'),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('FONTSIZE', (0,0), (-1,0), 14),
            ('BOTTOMPADDING', (0,0), (-1,0), 12),
            ('BACKGROUND', (0,1), (-1,-1), colors.beige),
            ('GRID', (0,0), (-1,-1), 1, colors.black)
        ]))
        story.append(tbl)
        story.append(Spacer(1, 24))
        story.append(Paragraph(f"Thank you for your business!", styles['Normal']))

        doc.build(story)
        buffer.seek(0)
        return buffer.getvalue()
    except Exception as e:
        logger.error(f"PDF generation error: {e}")
        return None


class StripeBillingEngine:
    """Stripe payment and subscription lifecycle management engine."""

    @staticmethod
    def list_plans(include_free: bool = True) -> List[dict]:
        """Return all available subscription plans."""
        plans = []
        for plan_key, plan in DEFAULT_PLANS.items():
            if not include_free and plan.id == "free":
                continue
            plans.append(plan.to_dict())
        return plans

    @staticmethod
    def create_subscription(tenant_id: str, plan_id: str, is_trial: bool = False) -> SubscriptionDTO:
        """Create a new subscription for an organization workspace."""
        plan = DEFAULT_PLANS.get(plan_id, DEFAULT_PLANS["starter_monthly"])
        
        now = datetime.now(timezone.utc)
        period_end = now + (
            timedelta(days=365) if plan.interval == "yearly" else timedelta(days=30)
        )

        logger.info(f"Creating {plan_id} subscription for tenant {tenant_id}")

        return SubscriptionDTO(
            subscription_id=f"sub_{uuid.uuid4().hex[:16]}",
            tenant_id=tenant_id,
            plan_id=plan_id,
            plan_name=plan.name,
            stripe_customer_id=f"cus_{uuid.uuid4().hex[:16]}",
            stripe_subscription_id=f"si_{uuid.uuid4().hex[:16]}",
            status="active",
            current_period_start=now,
            current_period_end=period_end,
            cancel_at_period_end=False,
            price_usd=plan.price_usd,
            max_seats=plan.max_seats,
            monthly_token_quota=plan.monthly_token_quota,
        )

    @staticmethod
    def create_free_trial(tenant_id: str) -> SubscriptionDTO:
        """Create a free trial subscription (1 month)."""
        now = datetime.now(timezone.utc)
        period_end = now + timedelta(days=30)
        
        logger.info(f"Creating free trial for tenant {tenant_id}")

        return SubscriptionDTO(
            subscription_id=f"trial_{uuid.uuid4().hex[:16]}",
            tenant_id=tenant_id,
            plan_id="free",
            plan_name="Free Tier Trial",
            stripe_customer_id=f"cus_{uuid.uuid4().hex[:16]}",
            status="trial",
            current_period_start=now,
            current_period_end=period_end,
            cancel_at_period_end=False,
            trial_ends_at=period_end,
            price_usd=0.0,
            max_seats=1,
            monthly_token_quota=100000,
        )

    @staticmethod
    def downgrade_to_free(tenant_id: str, reason: str = "subscription_expired") -> dict:
        """Downgrade tenant to free tier."""
        logger.warning(f"Downgrading tenant {tenant_id} to free tier: {reason}")
        return {
            "tenant_id": tenant_id,
            "new_plan_id": "free",
            "status": "downgraded",
            "reason": reason
        }

    @staticmethod
    def get_usage(tenant_id: str, plan_id: str, current_tokens_used: int) -> UsageDTO:
        """Returns usage metrics for the current billing cycle."""
        plan = DEFAULT_PLANS.get(plan_id, DEFAULT_PLANS["free"])
        quota = plan.monthly_token_quota
        cost_per_1m_tokens = 0.60
        estimated_cost = (current_tokens_used / 1_000_000) * cost_per_1m_tokens
        usage_percent = (current_tokens_used / quota * 100) if quota > 0 else 0
        
        return UsageDTO(
            tenant_id=tenant_id,
            plan_id=plan_id,
            current_tokens_used=current_tokens_used,
            monthly_token_quota=quota,
            usage_percent=round(usage_percent, 2),
            estimated_cost_usd=round(estimated_cost, 4),
            is_at_risk=usage_percent > 90
        )

    @staticmethod
    def check_subscription_status(tenant_id: str, current_period_end: datetime, has_renewed: bool = False) -> dict:
        """Check if subscription needs renewal or downgrade."""
        now = datetime.now(timezone.utc)
        days_remaining = (current_period_end - now).days
        
        if days_remaining <= 0:
            return {"action": "downgrade", "reason": "period_expired"}
        if days_remaining <= 7 and not has_renewed:
            return {"action": "warn", "reason": "subscription_expiring_soon", "days_remaining": days_remaining}
        return {"action": "continue", "days_remaining": days_remaining}

    @staticmethod
    def generate_invoice(tenant_id: str, plan_id: str) -> InvoiceDTO:
        """Generates an invoice for the current period."""
        plan = DEFAULT_PLANS.get(plan_id, DEFAULT_PLANS["growth_monthly"])
        invoice_id = f"inv_{datetime.now().strftime('%Y%m%d')}{uuid.uuid4().hex[:8]}"
        now = datetime.now(timezone.utc)

        pdf_bytes = generate_pdf_invoice({
            "invoice_id": invoice_id,
            "plan_name": plan.name,
            "amount_usd": plan.price_usd,
            "created_at": now,
        })

        pdf_base64 = base64.b64encode(pdf_bytes).decode() if pdf_bytes else None

        return InvoiceDTO(
            invoice_id=invoice_id,
            tenant_id=tenant_id,
            subscription_id=f"sub_{uuid.uuid4().hex[:16]}",
            plan_id=plan_id,
            amount_usd=plan.price_usd,
            status="paid",
            created_at=now,
            due_date=None,
            paid_at=now,
            invoice_url=f"https://billing.salesgenie.ai/invoices/{invoice_id}.pdf",
            pdf_base64=pdf_base64,
        )


stripe_billing = StripeBillingEngine()
PLAN_LIST = [plan.to_dict() for plan in DEFAULT_PLANS.values()]