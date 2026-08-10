"""
Sales Service API Router
Endpoints for lead qualification, deal pipeline management, product recommendations, coupons, and meeting booking.
"""

import uuid
from typing import List, Optional
from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from enterprise_ai_platform.common.database import get_async_db
from enterprise_ai_platform.common.security_rbac import (
    get_current_user,
    TokenPayload,
    RequirePermissions,
    Permission,
)
from .models import (
    CreateLeadRequest,
    LeadDTO,
    ProductRecommendationDTO,
    BookMeetingRequest,
    Lead,
    Deal,
    ProductCatalog,
    CalendarBooking,
)
from .sales_engine import calculate_lead_qualification_score, generate_product_recommendations
from .lead_state_machine import validate_lead_state_transition

router = APIRouter(prefix="/api/v1/sales", tags=["AI Sales & Lead Management"])

VALID_DEAL_STAGES = {"discovery", "demo", "proposal", "negotiation", "won", "lost"}
DEAL_STAGE_TRANSITIONS = {
    "discovery": {"demo", "lost"},
    "demo": {"proposal", "negotiation", "lost"},
    "proposal": {"negotiation", "won", "lost"},
    "negotiation": {"won", "lost"},
    "won": set(),
    "lost": set(),
}


@router.post(
    "/leads",
    response_model=LeadDTO,
    summary="Create & Qualify Lead",
    dependencies=[Depends(RequirePermissions(Permission.LEADS_WRITE))],
)
async def create_lead(
    req: CreateLeadRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Create a new sales lead and run automated BANT lead qualification scoring."""
    tenant_uuid = uuid.UUID(uuid.uuid5(uuid.NAMESPACE_DNS, current_user.tenant_id).hex[:32])
    score = calculate_lead_qualification_score(
        budget_usd=req.budget_usd,
        has_authority=True if req.company else False,
        need_urgency="this_quarter" if req.timeline else "exploring",
        timeline_months=1 if req.timeline == "immediate" else 3,
    )
    status_str = "qualified" if score >= 70 else "new"

    lead = Lead(
        tenant_id=tenant_uuid,
        email=req.email,
        full_name=req.full_name,
        company=req.company,
        phone=req.phone,
        lead_score=score,
        status=status_str,
        budget_usd=req.budget_usd,
        timeline=req.timeline,
    )
    db.add(lead)
    await db.commit()

    return LeadDTO(
        id=lead.id,
        email=lead.email,
        full_name=lead.full_name,
        company=lead.company,
        lead_score=lead.lead_score,
        status=lead.status,
        budget_usd=lead.budget_usd,
        created_at=lead.created_at,
    )


@router.get(
    "/leads",
    response_model=List[LeadDTO],
    summary="List Qualified Leads",
    dependencies=[Depends(RequirePermissions(Permission.LEADS_READ))],
)
async def list_leads(db: AsyncSession = Depends(get_async_db)):
    """List sales leads ordered by AI lead score."""
    stmt = select(Lead).order_by(Lead.lead_score.desc())
    res = await db.execute(stmt)
    leads = res.scalars().all()

    return [
        LeadDTO(
            id=l.id,
            email=l.email,
            full_name=l.full_name,
            company=l.company,
            lead_score=l.lead_score,
            status=l.status,
            budget_usd=l.budget_usd,
            created_at=l.created_at,
        )
        for l in leads
    ]


@router.patch(
    "/leads/{lead_id}",
    response_model=LeadDTO,
    summary="Update Lead Status (state machine enforced)",
    dependencies=[Depends(RequirePermissions(Permission.LEADS_WRITE))],
)
async def update_lead(
    lead_id: str,
    status: Optional[str] = Query(None),
    lead_score: Optional[int] = Query(None, ge=0, le=100),
    db: AsyncSession = Depends(get_async_db),
    current_user: TokenPayload = Depends(get_current_user),
):
    """Transition a lead to a new status with state machine validation."""
    tenant_uuid = uuid.UUID(uuid.uuid5(uuid.NAMESPACE_DNS, current_user.tenant_id).hex[:32])
    stmt = select(Lead).where(Lead.id == uuid.UUID(lead_id), Lead.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    lead = res.scalar_one_or_none()

    if not lead:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lead {lead_id} not found",
        )

    if status is not None:
        validate_lead_state_transition(lead.status, status)
        lead.status = status

    if lead_score is not None:
        lead.lead_score = lead_score

    await db.commit()
    await db.refresh(lead)

    return LeadDTO(
        id=lead.id,
        email=lead.email,
        full_name=lead.full_name,
        company=lead.company,
        lead_score=lead.lead_score,
        status=lead.status,
        budget_usd=lead.budget_usd,
        created_at=lead.created_at,
    )


@router.patch(
    "/deals/{deal_id}/stage",
    summary="Update Deal Pipeline Stage",
    dependencies=[Depends(RequirePermissions(Permission.LEADS_WRITE))],
)
async def update_deal_stage(
    deal_id: str,
    new_stage: str,
    db: AsyncSession = Depends(get_async_db),
    current_user: TokenPayload = Depends(get_current_user),
):
    """Transition a deal to a new pipeline stage with validation."""
    tenant_uuid = uuid.UUID(uuid.uuid5(uuid.NAMESPACE_DNS, current_user.tenant_id).hex[:32])
    stmt = select(Deal).where(Deal.id == uuid.UUID(deal_id), Deal.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    deal = res.scalar_one_or_none()

    if not deal:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Deal {deal_id} not found",
        )

    if new_stage not in VALID_DEAL_STAGES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid deal stage '{new_stage}'. Must be one of: {', '.join(sorted(VALID_DEAL_STAGES))}",
        )

    allowed = DEAL_STAGE_TRANSITIONS.get(deal.pipeline_stage, set())
    if new_stage not in allowed:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid deal stage transition from '{deal.pipeline_stage}' to '{new_stage}'.",
        )

    old_stage = deal.pipeline_stage
    deal.pipeline_stage = new_stage

    # Auto-calculate probability based on stage
    stage_probabilities = {
        "discovery": 0.2, "demo": 0.25, "proposal": 0.5,
        "negotiation": 0.75, "won": 1.0, "lost": 0.0,
    }
    deal.probability = stage_probabilities.get(new_stage, deal.probability)

    await db.commit()

    return {
        "deal_id": deal_id,
        "old_stage": old_stage,
        "new_stage": new_stage,
        "probability": deal.probability,
    }


@router.get(
    "/recommendations",
    response_model=List[ProductRecommendationDTO],
    summary="Get AI Product Recommendations & Upsells",
    dependencies=[Depends(RequirePermissions(Permission.AGENT_EXECUTE))],
)
async def get_recommendations(category: str = "Enterprise AI"):
    """Fetch AI personalized product recommendations with upsell/cross-sell coupons."""
    mock_products = [
        ProductCatalog(
            id=uuid.uuid4(),
            sku="AI-AGENT-ENTERPRISE",
            name="SalesGenie Multi-Agent Suite",
            category="Enterprise AI",
            price_usd=499.0,
            description="Full-scale multi-agent platform for customer support & sales.",
        ),
        ProductCatalog(
            id=uuid.uuid4(),
            sku="AI-KNOWLEDGE-PRO",
            name="RAG Document Vector Indexer",
            category="Enterprise AI",
            price_usd=199.0,
            description="High-speed document chunking & vector search engine.",
        ),
    ]
    return generate_product_recommendations(category, mock_products)


@router.post(
    "/bookings",
    summary="Schedule Calendar Meeting Booking",
    dependencies=[Depends(RequirePermissions(Permission.LEADS_WRITE))],
)
async def book_meeting(
    req: BookMeetingRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Automatically book sales demo call between qualified lead and sales representative."""
    tenant_uuid = uuid.UUID(uuid.uuid5(uuid.NAMESPACE_DNS, current_user.tenant_id).hex[:32])
    end_time = req.start_time + timedelta(minutes=req.duration_minutes or 30)
    meeting_link = f"https://meet.salesgenie.ai/demo-{uuid.uuid4().hex[:6]}"

    booking = CalendarBooking(
        tenant_id=tenant_uuid,
        lead_id=uuid.UUID(req.lead_id),
        sales_rep_id=uuid.UUID(req.sales_rep_id),
        meeting_title="SalesGenie AI Platform Demo & Strategy Session",
        start_time=req.start_time,
        end_time=end_time,
        meeting_link=meeting_link,
    )
    db.add(booking)
    await db.commit()

    return {
        "status": "confirmed",
        "booking_id": str(booking.id),
        "meeting_link": meeting_link,
        "start_time": req.start_time.isoformat(),
        "end_time": end_time.isoformat(),
    }
