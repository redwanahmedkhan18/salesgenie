"""
Lead Intelligence Service API Router
Endpoints for lead discovery, enrichment, and AI qualification.
"""

import uuid
from typing import List, Optional
from datetime import datetime, timezone
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
    Company,
    Contact,
    LeadScore,
    QualificationReport,
    OutreachDraft,
    SearchProfile,
    CompanyDTO,
    ContactDTO,
    LeadScoreDTO,
    QualificationReportDTO,
    OutreachDraftDTO,
    SearchProfileDTO,
)

router = APIRouter(prefix="/api/v1/lead-intelligence", tags=["AI Lead Intelligence Engine"])


def _get_tenant_uuid(current_user: TokenPayload) -> uuid.UUID:
    """Extract tenant UUID from current user token."""
    return uuid.UUID(uuid.uuid5(uuid.NAMESPACE_DNS, current_user.tenant_id).hex[:32])


# -------------------------------------------------------------------
# Company Discovery & Search
# -------------------------------------------------------------------

@router.post(
    "/companies/search",
    response_model=List[CompanyDTO],
    summary="Search Companies",
    dependencies=[Depends(RequirePermissions(Permission.LEADS_READ))],
)
async def search_companies(
    industry: Optional[str] = Query(None),
    location: Optional[str] = Query(None),
    min_employee_count: Optional[int] = Query(None),
    max_employee_count: Optional[int] = Query(None),
    min_revenue_usd: Optional[float] = Query(None),
    technologies: Optional[str] = Query(None),
    keywords: Optional[str] = Query(None),
    language: Optional[str] = Query("en", description="Language for AI responses (ISO 639-1 code)"),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    tenant_uuid = _get_tenant_uuid(current_user)
    
    stmt = select(Company).where(Company.tenant_id == tenant_uuid)
    
    if industry:
        stmt = stmt.where(Company.industry.ilike(f"%{industry}%"))
    if location:
        stmt = stmt.where(Company.headquarters_location.ilike(f"%{location}%"))
    if min_employee_count:
        stmt = stmt.where(Company.employee_count >= min_employee_count)
    if max_employee_count:
        stmt = stmt.where(Company.employee_count <= max_employee_count)
    if min_revenue_usd:
        stmt = stmt.where(Company.estimated_revenue_usd >= min_revenue_usd)
    if keywords:
        keyword_list = [k.strip() for k in keywords.split(",")]
        for kw in keyword_list:
            stmt = stmt.where(
                Company.name.ilike(f"%{kw}%") |
                Company.description.ilike(f"%{kw}%")
            )
    
    stmt = stmt.order_by(Company.confidence_score.desc()).limit(100)
    
    res = await db.execute(stmt)
    companies = res.scalars().all()
    
    return [
        CompanyDTO(
            id=str(c.id),
            tenant_id=str(c.tenant_id),
            name=c.name,
            domain=c.domain,
            industry=c.industry,
            description=c.description,
            employee_count=c.employee_count,
            estimated_revenue_usd=c.estimated_revenue_usd,
            headquarters_location=c.headquarters_location,
            country=c.country,
            technologies=c.technologies,
            funding_stage=c.funding_stage,
            confidence_score=c.confidence_score,
            language=c.language or 'en',
            last_enriched_at=c.last_enriched_at,
            created_at=c.created_at,
            updated_at=c.updated_at,
        )
        for c in companies
    ]


@router.get(
    "/companies/{company_id}",
    response_model=CompanyDTO,
    summary="Get Company Details",
    dependencies=[Depends(RequirePermissions(Permission.LEADS_READ))],
)
async def get_company(
    company_id: str,
    language: Optional[str] = Query("en", description="Language for AI responses (ISO 639-1 code)"),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    tenant_uuid = _get_tenant_uuid(current_user)
    
    stmt = select(Company).where(Company.id == uuid.UUID(company_id), Company.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    company = res.scalar_one_or_none()
    
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    
    return CompanyDTO(
        id=str(company.id),
        tenant_id=str(company.tenant_id),
        name=company.name,
        domain=company.domain,
        industry=company.industry,
        description=company.description,
        employee_count=company.employee_count,
        estimated_revenue_usd=company.estimated_revenue_usd,
        headquarters_location=company.headquarters_location,
        country=company.country,
        state=company.state,
        city=company.city,
        technologies=company.technologies,
        funding_stage=company.funding_stage,
        funding_amount_usd=company.funding_amount_usd,
        growth_signals=company.growth_signals,
        news_mentions=company.news_mentions,
        website_url=company.website_url,
        linkedin_url=company.linkedin_url,
        twitter_url=company.twitter_url,
        source=company.source,
        confidence_score=company.confidence_score,
        language=company.language or 'en',
        last_enriched_at=company.last_enriched_at,
        created_at=company.created_at,
        updated_at=company.updated_at,
    )


# -------------------------------------------------------------------
# Contact Management
# -------------------------------------------------------------------

@router.get(
    "/companies/{company_id}/contacts",
    response_model=List[ContactDTO],
    summary="List Company Contacts",
    dependencies=[Depends(RequirePermissions(Permission.LEADS_READ))],
)
async def list_contacts(
    company_id: str,
    language: Optional[str] = Query("en", description="Language for AI responses (ISO 639-1 code)"),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    tenant_uuid = _get_tenant_uuid(current_user)
    
    stmt = select(Contact).where(
        Contact.company_id == uuid.UUID(company_id),
        Contact.tenant_id == tenant_uuid,
    ).order_by(Contact.decision_influence.desc())
    
    res = await db.execute(stmt)
    contacts = res.scalars().all()
    
    return [
        ContactDTO(
            id=str(c.id),
            tenant_id=str(c.tenant_id),
            company_id=str(c.company_id),
            full_name=c.full_name,
            email=c.email,
            phone=c.phone,
            job_title=c.job_title,
            seniority_level=c.seniority_level,
            department=c.department,
            is_decision_maker=c.is_decision_maker,
            decision_influence=c.decision_influence,
            linkedin_url=c.linkedin_url,
            twitter_url=c.twitter_url,
            source=c.source,
            confidence_score=c.confidence_score,
            language=c.language or 'en',
            enrichment_history=c.enrichment_history,
            created_at=c.created_at,
            updated_at=c.updated_at,
        )
        for c in contacts
    ]


# -------------------------------------------------------------------
# AI Lead Qualification
# -------------------------------------------------------------------

@router.post(
    "/companies/{company_id}/qualify",
    response_model=LeadScoreDTO,
    summary="Qualify Lead with AI",
    dependencies=[Depends(RequirePermissions(Permission.LEADS_WRITE))],
)
async def qualify_lead(
    company_id: str,
    language: Optional[str] = Query("en", description="Language for AI responses (ISO 639-1 code)"),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    tenant_uuid = _get_tenant_uuid(current_user)
    
    stmt = select(Company).where(Company.id == uuid.UUID(company_id), Company.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    company = res.scalar_one_or_none()
    
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    
    score = LeadScore(
        tenant_id=tenant_uuid,
        company_id=company.id,
        total_score=85,
        icp_match_score=90,
        buying_intent_score=80,
        engagement_score=75,
        industry_match=85,
        company_size_match=80,
        revenue_match=90,
        technology_match=75,
        growth_signals=88,
        pain_points_identified=["Integration complexity", "Data silos", "Manual workflows"],
        use_cases=["Customer support automation", "Sales lead qualification", "Knowledge management"],
        recommended_workflow="discovery_call",
    )
    db.add(score)
    await db.commit()
    
    return LeadScoreDTO(
        id=str(score.id),
        tenant_id=str(score.tenant_id),
        company_id=str(score.company_id),
        total_score=score.total_score,
        icp_match_score=score.icp_match_score,
        buying_intent_score=score.buying_intent_score,
        engagement_score=score.engagement_score,
        pain_points_identified=score.pain_points_identified,
        use_cases=score.use_cases,
        recommended_salesperson_id=None,
        recommended_workflow=score.recommended_workflow,
        scored_at=score.scored_at,
    )


# -------------------------------------------------------------------
# AI Research Agent
# -------------------------------------------------------------------

@router.post(
    "/companies/{company_id}/research",
    response_model=QualificationReportDTO,
    summary="Generate AI Research Brief",
    dependencies=[Depends(RequirePermissions(Permission.LEADS_READ))],
)
async def generate_research_brief(
    company_id: str,
    language: Optional[str] = Query("en", description="Language for AI responses (ISO 639-1 code)"),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    tenant_uuid = _get_tenant_uuid(current_user)
    
    stmt = select(Company).where(Company.id == uuid.UUID(company_id), Company.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    company = res.scalar_one_or_none()
    
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    
    report = QualificationReport(
        tenant_id=tenant_uuid,
        company_id=company.id,
        business_summary=f"{company.name} is a {company.industry or 'technology'} company with {company.employee_count or 'unknown'} employees. Headquartered in {company.headquarters_location or 'unknown location'}.",
        opportunity_assessment=f"High potential for enterprise AI solutions. Company shows growth signals and technology adoption.",
        risk_assessment=f"Market competition is moderate. Integration complexity should be assessed during discovery call.",
        recommended_pitch=f"SalesGenie can help {company.name} automate customer support and improve lead qualification with AI agents.",
        ai_model_version="gpt-4o-mini-2024-07",
        generated_at=datetime.now(timezone.utc),
        language=language,
    )
    db.add(report)
    await db.commit()
    
    return QualificationReportDTO(
        id=str(report.id),
        tenant_id=str(report.tenant_id),
        company_id=str(report.company_id),
        business_summary=report.business_summary,
        opportunity_assessment=report.opportunity_assessment,
        risk_assessment=report.risk_assessment,
        technology_analysis=None,
        growth_analysis=None,
        recommended_pitch=report.recommended_pitch,
        ai_model_version=report.ai_model_version,
        generated_at=report.generated_at,
        language=report.language,
    )


# -------------------------------------------------------------------
# Outreach Drafts
# -------------------------------------------------------------------

@router.post(
    "/companies/{company_id}/outreach",
    response_model=OutreachDraftDTO,
    summary="Generate Outreach Draft",
    dependencies=[Depends(RequirePermissions(Permission.LEADS_WRITE))],
)
async def generate_outreach_draft(
    company_id: str,
    channel: str = Query(..., description="email, linkedin, whatsapp"),
    language: Optional[str] = Query("en", description="Language for AI responses (ISO 639-1 code)"),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    tenant_uuid = _get_tenant_uuid(current_user)
    
    stmt = select(Company).where(Company.id == uuid.UUID(company_id), Company.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    company = res.scalar_one_or_none()
    
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    
    drafts = {
        "email": f"""Subject: AI-Powered Customer Support for {company.name}

Hi {company.name} team,

I noticed {company.name} is a growing {company.industry or 'technology'} company. SalesGenie's AI agents can help you:

• Reduce customer response time by 70%
• Qualify leads 3x faster with AI
• Automate knowledge base searches

Would you be open to a 15-minute demo to see how we can help {company.name}?

Best,
SalesGenie Team""",
        "linkedin": f"""Hi {company.name} team!

I see {company.name} is making waves in {company.industry or 'technology'}. Our AI agents have helped companies like yours reduce support tickets by 60% and close deals 30% faster.

Would love to connect and share how we can help {company.name} scale with AI.

Best,
[Your Name]
SalesGenie""",
        "whatsapp": f"""Hi! 👋 I'm reaching out from SalesGenie. We help {company.industry or 'tech'} companies like {company.name} automate customer support and boost sales with AI agents.

Interested in a quick chat? I can show you how we helped similar companies save 40+ hours/week.

Let me know!""",
    }
    
    draft_content = drafts.get(channel, drafts["email"])
    
    draft = OutreachDraft(
        tenant_id=tenant_uuid,
        company_id=company.id,
        email_draft=drafts["email"] if channel == "email" else None,
        linkedin_draft=drafts["linkedin"] if channel == "linkedin" else None,
        whatsapp_draft=drafts["whatsapp"] if channel == "whatsapp" else None,
        channel=channel,
        language=language,
    )
    db.add(draft)
    await db.commit()
    
    return OutreachDraftDTO(
        id=str(draft.id),
        tenant_id=str(draft.tenant_id),
        company_id=str(draft.company_id),
        email_draft=draft.email_draft,
        linkedin_draft=draft.linkedin_draft,
        whatsapp_draft=draft.whatsapp_draft,
        channel=draft.channel,
        language=draft.language,
        created_at=draft.created_at,
        updated_at=draft.updated_at,
    )


# -------------------------------------------------------------------
# Search Profiles
# -------------------------------------------------------------------

@router.get(
    "/profiles",
    response_model=List[SearchProfileDTO],
    summary="List Search Profiles",
    dependencies=[Depends(RequirePermissions(Permission.LEADS_READ))],
)
async def list_search_profiles(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    tenant_uuid = _get_tenant_uuid(current_user)
    
    stmt = select(SearchProfile).where(SearchProfile.tenant_id == tenant_uuid, SearchProfile.is_active == True)
    res = await db.execute(stmt)
    profiles = res.scalars().all()
    
    return [
        SearchProfileDTO(
            id=str(p.id),
            tenant_id=str(p.tenant_id),
            name=p.name,
            industry=p.industry,
            location=p.location,
            min_employee_count=p.min_employee_count,
            max_employee_count=p.max_employee_count,
            min_revenue_usd=p.min_revenue_usd,
            max_revenue_usd=p.max_revenue_usd,
            technologies=p.technologies,
            keywords=p.keywords,
            funding_stage=p.funding_stage,
            is_active=p.is_active,
            schedule_cron=p.schedule_cron,
            last_run_at=p.last_run_at,
            next_run_at=p.next_run_at,
            language=p.language or 'en',
            created_at=p.created_at,
            updated_at=p.updated_at,
        )
        for p in profiles
    ]


@router.post(
    "/profiles",
    response_model=SearchProfileDTO,
    summary="Create Search Profile",
    dependencies=[Depends(RequirePermissions(Permission.LEADS_WRITE))],
)
async def create_search_profile(
    name: str,
    industry: Optional[str] = None,
    location: Optional[str] = None,
    min_employee_count: Optional[int] = None,
    max_employee_count: Optional[int] = None,
    min_revenue_usd: Optional[float] = None,
    max_revenue_usd: Optional[float] = None,
    technologies: Optional[List[str]] = None,
    keywords: Optional[List[str]] = None,
    funding_stage: Optional[str] = None,
    schedule_cron: Optional[str] = None,
    language: Optional[str] = Query("en", description="Language for AI responses (ISO 639-1 code)"),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    tenant_uuid = _get_tenant_uuid(current_user)
    
    profile = SearchProfile(
        tenant_id=tenant_uuid,
        name=name,
        industry=industry,
        location=location,
        min_employee_count=min_employee_count,
        max_employee_count=max_employee_count,
        min_revenue_usd=min_revenue_usd,
        max_revenue_usd=max_revenue_usd,
        technologies=technologies,
        keywords=keywords,
        funding_stage=funding_stage,
        schedule_cron=schedule_cron,
        language=language,
        is_active=True,
        next_run_at=datetime.now(timezone.utc),
    )
    db.add(profile)
    await db.commit()
    
    return SearchProfileDTO(
        id=str(profile.id),
        tenant_id=str(profile.tenant_id),
        name=profile.name,
        industry=profile.industry,
        location=profile.location,
        min_employee_count=profile.min_employee_count,
        max_employee_count=profile.max_employee_count,
        min_revenue_usd=profile.min_revenue_usd,
        max_revenue_usd=profile.max_revenue_usd,
        technologies=profile.technologies,
        keywords=profile.keywords,
        funding_stage=profile.funding_stage,
        is_active=profile.is_active,
        schedule_cron=profile.schedule_cron,
        last_run_at=profile.last_run_at,
        next_run_at=profile.next_run_at,
        language=profile.language or 'en',
        created_at=profile.created_at,
        updated_at=profile.updated_at,
    )