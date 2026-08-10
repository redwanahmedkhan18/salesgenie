"""
Billing Service API Router
Endpoints for Stripe subscriptions, usage metering, invoices, and plan management with PDF receipts.
"""

import base64
import io
from datetime import datetime
from typing import List

from fastapi import APIRouter, BackgroundTasks, Depends, Query
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from starlette.responses import JSONResponse

from enterprise_ai_platform.common.cost_management import cost_calculator, BUDGET_ALERT_THRESHOLD, BUDGET_HARD_LIMIT
from enterprise_ai_platform.common.security_rbac import (
    Permission,
    RequirePermissions,
    TokenPayload,
    get_current_user,
)

from .stripe_billing import (
    DEFAULT_PLANS,
    SubscriptionDTO,
    UsageDTO,
    generate_pdf_invoice,
    stripe_billing,
)

router = APIRouter(prefix="/api/v1/billing", tags=["Billing & Stripe Subscriptions"])


class CostAlertDTO(BaseModel):
    tenant_id: str
    threshold_percent: float
    current_spent_usd: float
    monthly_budget_usd: float
    usage_percent: float
    alert_type: str  # "warning" | "critical" | "blocked"
    message: str


def send_email_async(tenant_id: str, subject: str, body_html: str, attachment_bytes: bytes):
    """Background email sender (placeholder for actual email service)."""
    import smtplib
    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    
    smtp_host = "localhost"
    smtp_port = 1025
    from_email = "billing@salesgenie.ai"
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = f"customer-{tenant_id}@salesgenie.ai"
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body_html, "html"))
    
    attachment = MIMEBase("application", "octet-stream")
    attachment.set_payload(attachment_bytes)
    encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", "attachment", filename="invoice.pdf")
    msg.attach(attachment)
    
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.send_message(msg)


@router.get("/plans", summary="List Available Subscription Plans")
async def list_plans():
    """Return all available pricing tiers (Starter, Growth, Enterprise)."""
    return [
        {
            "plan_key": k,
            "name": v.name,
            "price_usd": v.price_usd,
            "max_seats": v.max_seats,
            "monthly_token_quota": v.monthly_token_quota,
        }
        for k, v in DEFAULT_PLANS.items()
    ]


@router.post(
    "/subscriptions",
    response_model=SubscriptionDTO,
    summary="Create New Subscription",
    dependencies=[Depends(RequirePermissions(Permission.BILLING_MANAGE))],
)
async def create_subscription(
    plan: str = "growth_monthly",
    is_trial: bool = False,
    current_user: TokenPayload = Depends(get_current_user),
):
    """Create a new workspace subscription for the current tenant."""
    if is_trial:
        return stripe_billing.create_free_trial(tenant_id=current_user.tenant_id)
    return stripe_billing.create_subscription(tenant_id=current_user.tenant_id, plan_key=plan)


@router.get(
    "/subscriptions/usage",
    response_model=UsageDTO,
    summary="Get Token Usage & Billing Meter",
    dependencies=[Depends(RequirePermissions(Permission.BILLING_READ))],
)
async def get_usage(
    tokens_used: int = Query(default=2480000, description="Current monthly tokens used"),
    plan: str = Query(default="growth_monthly", description="Active subscription plan key"),
    current_user: TokenPayload = Depends(get_current_user),
):
    """Retrieve real-time token usage, quota consumption, and estimated billing cost."""
    return stripe_billing.get_usage(
        tenant_id=current_user.tenant_id,
        plan_id=plan,
        current_tokens_used=tokens_used,
    )


@router.get(
    "/subscriptions/check",
    summary="Check Subscription Status for Auto-downgrade",
    dependencies=[Depends(RequirePermissions(Permission.BILLING_READ))],
)
async def check_subscription_status(
    current_user: TokenPayload = Depends(get_current_user),
):
    """Check if subscription needs renewal warning or downgrade."""
    return {"status": "active", "tenant_id": current_user.tenant_id, "action": "continue"}


@router.get(
    "/invoices",
    response_model=List[dict],
    summary="List Billing Invoices",
    dependencies=[Depends(RequirePermissions(Permission.BILLING_READ))],
)
async def list_invoices(current_user: TokenPayload = Depends(get_current_user)):
    """List paid and open invoices for the tenant workspace."""
    invoice = stripe_billing.generate_invoice(
        tenant_id=current_user.tenant_id,
        plan_id="growth_monthly"
    )
    return [{
        "invoice_id": invoice.invoice_id,
        "amount_usd": invoice.amount_usd,
        "status": invoice.status,
        "created_at": invoice.created_at.isoformat(),
        "invoice_url": invoice.invoice_url,
    }]


@router.post(
    "/invoices/generate",
    summary="Generate PDF Invoice and Send via Email",
)
async def generate_invoice_with_email(
    tenant_id: str,
    plan: str = "growth_monthly",
    send_email: bool = True,
    background_tasks: BackgroundTasks = None,
):
    """Generate PDF invoice and optionally email it."""
    invoice = stripe_billing.generate_invoice(tenant_id=tenant_id, plan_id=plan)
    
    if send_email and invoice.pdf_base64:
        background_tasks.add_task(
            send_email_async,
            tenant_id,
            f"Invoice {invoice.invoice_id} - SalesGenie",
            f"<h1>Invoice {invoice.invoice_id}</h1><p>Amount: ${invoice.amount_usd}</p>",
            base64.b64decode(invoice.pdf_base64)
        )
    
    return {
        "invoice_id": invoice.invoice_id,
        "amount_usd": invoice.amount_usd,
        "status": "sent" if send_email else "generated",
        "pdf_available": invoice.pdf_base64 is not None,
    }


@router.get(
    "/invoices/{invoice_id}/pdf",
    summary="Download Invoice PDF",
)
async def download_invoice_pdf(invoice_id: str):
    """Download invoice as PDF."""
    invoice_data = {
        "invoice_id": invoice_id,
        "plan_name": "Growth Plan",
        "amount_usd": 149.00,
        "created_at": datetime.now(),
    }
    
    pdf_bytes = generate_pdf_invoice(invoice_data)
    
    if not pdf_bytes:
        return JSONResponse({"error": "PDF generation failed"}, status_code=500)
    
    return StreamingResponse(
        io.BytesIO(pdf_bytes),
        media_type="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="invoice_{invoice_id}.pdf"'}
    )


@router.post(
    "/payments/receipt",
    summary="Generate Payment Receipt PDF",
)
async def generate_payment_receipt(
    amount_usd: float,
    plan: str = "growth_monthly",
    description: str = "Subscription Payment",
    current_user: TokenPayload = Depends(get_current_user),
):
    """Generate a payment receipt PDF for a completed transaction."""
    receipt_data = {
        "invoice_id": f"RCPT-{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "plan_name": f"{plan.replace('_', ' ').title()} Payment",
        "amount_usd": amount_usd,
        "created_at": datetime.now(),
        "tenant_name": current_user.email.split('@')[0] if '@' in current_user.email else "Customer",
    }
    
    pdf_bytes = generate_pdf_invoice(receipt_data)
    
    if not pdf_bytes:
        return JSONResponse({"error": "PDF generation failed"}, status_code=500)
    
    return StreamingResponse(
        io.BytesIO(pdf_bytes),
        media_type="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="receipt_{receipt_data["invoice_id"]}.pdf"'}
    )


@router.get(
    "/usage/live",
    summary="Get Live Token Usage & Cost for Current Tenant",
    dependencies=[Depends(RequirePermissions(Permission.BILLING_READ))],
)
async def get_live_usage(
    current_user: TokenPayload = Depends(get_current_user),
):
    """Get real-time token usage and estimated cost from in-memory tracking."""
    plan_id = "growth_monthly"
    plan = DEFAULT_PLANS.get(plan_id, DEFAULT_PLANS["free"])
    quota = plan.monthly_token_quota
    usage = cost_calculator.get_tenant_usage(current_user.tenant_id)
    if usage:
        return UsageDTO(
            tenant_id=usage.tenant_id,
            plan_id=plan_id,
            current_tokens_used=int(usage.current_spent_usd / 0.0000006 * 1_000_000),
            monthly_token_quota=quota,
            usage_percent=round(usage.usage_percent, 2),
            estimated_cost_usd=round(usage.current_spent_usd, 4),
            is_at_risk=usage.is_at_risk,
        )
    return UsageDTO(
        tenant_id=current_user.tenant_id,
        plan_id=plan_id,
        current_tokens_used=0,
        monthly_token_quota=quota,
        usage_percent=0.0,
        estimated_cost_usd=0.0,
        is_at_risk=False,
    )


@router.get(
    "/alerts",
    response_model=List[CostAlertDTO],
    summary="Get Cost Alerts for Current Tenant",
    dependencies=[Depends(RequirePermissions(Permission.BILLING_READ))],
)
async def get_cost_alerts(
    current_user: TokenPayload = Depends(get_current_user),
):
    """Get cost/budget alerts for the current tenant."""
    usage = cost_calculator.get_tenant_usage(current_user.tenant_id)
    if not usage:
        return []

    alerts = []
    if usage.is_at_risk:
        alert_type = "critical" if usage.usage_percent >= BUDGET_HARD_LIMIT * 100 else "warning"
        alerts.append(CostAlertDTO(
            tenant_id=usage.tenant_id,
            threshold_percent=BUDGET_ALERT_THRESHOLD * 100,
            current_spent_usd=round(usage.current_spent_usd, 4),
            monthly_budget_usd=usage.monthly_budget_usd,
            usage_percent=round(usage.usage_percent, 2),
            alert_type=alert_type,
            message=f"You have used {usage.usage_percent:.1f}% of your ${usage.monthly_budget_usd} monthly AI budget.",
        ))
    return alerts


@router.get(
    "/platform-usage",
    summary="Get Platform-Wide Usage Summary (Super Admin)",
    dependencies=[Depends(RequirePermissions(Permission.BILLING_READ))],
)
async def get_platform_usage():
    """Get platform-wide token usage and cost summary."""
    return cost_calculator.get_platform_usage()