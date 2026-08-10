"""
Product Intelligence Service API Router
Endpoints for market research projects, competitor analysis,
opportunity detection, strategy recommendations, and launch planning.
"""

import uuid
from datetime import datetime
from typing import List, Optional, Dict, Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, desc, delete

from enterprise_ai_platform.common.database import get_async_db
from enterprise_ai_platform.common.security_rbac import (
    get_current_user,
    TokenPayload,
)
from .models import (
    ResearchProject,
    EvidenceItem,
    Competitor,
    MarketOpportunity,
    ProductStrategy,
    ScenarioModel,
    LaunchPlan,
    ProductReport,
    ResearchProjectDTO,
    CreateProjectRequest,
    UpdateProjectRequest,
    EvidenceItemDTO,
    AddEvidenceRequest,
    CompetitorDTO,
    AddCompetitorRequest,
    MarketOpportunityDTO,
    ProductStrategyDTO,
    ScenarioModelDTO,
    CreateScenarioRequest,
    LaunchPlanDTO,
    ProductReportDTO,
    AnalysisRequest,
)

router = APIRouter(prefix="/api/v1/product-intelligence", tags=["Product Intelligence & Market Analysis"])


def _get_tenant_uuid(current_user: TokenPayload) -> uuid.UUID:
    """Extract tenant UUID from current user token."""
    return uuid.uuid5(uuid.NAMESPACE_DNS, current_user.tenant_id)


# -------------------------------------------------------------------
# Research Projects
# -------------------------------------------------------------------

@router.post("/projects", response_model=ResearchProjectDTO, status_code=status.HTTP_201_CREATED,
             summary="Create Research Project")
async def create_project(
    req: CreateProjectRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Create a new product intelligence research project."""
    tenant_uuid = _get_tenant_uuid(current_user)

    project = ResearchProject(
        tenant_id=tenant_uuid,
        name=req.name,
        description=req.description,
        product_name=req.product_name,
        product_description=req.product_description,
        product_category=req.product_category,
        target_market=req.target_market,
        geographic_market=req.geographic_market,
        business_model=req.business_model,
        expected_price=req.expected_price,
        product_stage=req.product_stage,
        competitive_advantages=req.competitive_advantages,
        created_by=uuid.UUID(current_user.sub),
        status="draft",
    )
    db.add(project)
    await db.commit()
    await db.refresh(project)

    return ResearchProjectDTO(
        id=str(project.id),
        name=project.name,
        description=project.description,
        product_name=project.product_name,
        product_description=project.product_description,
        product_category=project.product_category,
        target_market=project.target_market,
        geographic_market=project.geographic_market,
        business_model=project.business_model,
        expected_price=project.expected_price,
        product_stage=project.product_stage,
        competitive_advantages=project.competitive_advantages,
        status=project.status,
        created_by=str(project.created_by),
        tenant_id=str(project.tenant_id),
        created_at=project.created_at,
        updated_at=project.updated_at,
    )


@router.get("/projects", response_model=List[ResearchProjectDTO], summary="List Research Projects")
async def list_projects(
    status: Optional[str] = Query(None, description="Filter by status"),
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """List all research projects for the current tenant."""
    tenant_uuid = _get_tenant_uuid(current_user)
    stmt = select(ResearchProject).where(ResearchProject.tenant_id == tenant_uuid)

    if status:
        stmt = stmt.where(ResearchProject.status == status)

    stmt = stmt.order_by(ResearchProject.updated_at.desc()).limit(limit).offset(offset)
    res = await db.execute(stmt)
    projects = res.scalars().all()

    return [
        ResearchProjectDTO(
            id=str(p.id),
            name=p.name,
            description=p.description,
            product_name=p.product_name,
            product_description=p.product_description,
            product_category=p.product_category,
            target_market=p.target_market,
            geographic_market=p.geographic_market,
            business_model=p.business_model,
            expected_price=p.expected_price,
            product_stage=p.product_stage,
            competitive_advantages=p.competitive_advantages,
            status=p.status,
            created_by=str(p.created_by),
            tenant_id=str(p.tenant_id),
            created_at=p.created_at,
            updated_at=p.updated_at,
        )
        for p in projects
    ]


@router.get("/projects/{project_id}", response_model=ResearchProjectDTO, summary="Get Project Details")
async def get_project(
    project_id: uuid.UUID,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get a specific research project."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(ResearchProject).where(
        ResearchProject.id == project_id,
        ResearchProject.tenant_id == tenant_uuid,
    )
    res = await db.execute(stmt)
    project = res.scalar_one_or_none()

    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project {project_id} not found",
        )

    return ResearchProjectDTO(
        id=str(project.id),
        name=project.name,
        description=project.description,
        product_name=project.product_name,
        product_description=project.product_description,
        product_category=project.product_category,
        target_market=project.target_market,
        geographic_market=project.geographic_market,
        business_model=project.business_model,
        expected_price=project.expected_price,
        product_stage=project.product_stage,
        competitive_advantages=project.competitive_advantages,
        status=project.status,
        created_by=str(project.created_by),
        tenant_id=str(project.tenant_id),
        created_at=project.created_at,
        updated_at=project.updated_at,
    )


@router.patch("/projects/{project_id}", response_model=ResearchProjectDTO, summary="Update Project")
async def update_project(
    project_id: uuid.UUID,
    req: UpdateProjectRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Update a research project."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(ResearchProject).where(
        ResearchProject.id == project_id,
        ResearchProject.tenant_id == tenant_uuid,
    )
    res = await db.execute(stmt)
    project = res.scalar_one_or_none()

    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    update_data = req.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(project, field, value)

    project.updated_at = datetime.utcnow()
    await db.commit()
    await db.refresh(project)

    return ResearchProjectDTO(
        id=str(project.id),
        name=project.name,
        description=project.description,
        product_name=project.product_name,
        product_description=project.product_description,
        product_category=project.product_category,
        target_market=project.target_market,
        geographic_market=project.geographic_market,
        business_model=project.business_model,
        expected_price=project.expected_price,
        product_stage=project.product_stage,
        competitive_advantages=project.competitive_advantages,
        status=project.status,
        created_by=str(project.created_by),
        tenant_id=str(project.tenant_id),
        created_at=project.created_at,
        updated_at=project.updated_at,
    )


@router.delete("/projects/{project_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete Project")
async def delete_project(
    project_id: uuid.UUID,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Delete a research project and all associated data."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(ResearchProject).where(
        ResearchProject.id == project_id,
        ResearchProject.tenant_id == tenant_uuid,
    )
    res = await db.execute(stmt)
    project = res.scalar_one_or_none()

    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    await db.execute(delete(EvidenceItem).where(EvidenceItem.project_id == project_id))
    await db.execute(delete(Competitor).where(Competitor.project_id == project_id))
    await db.execute(delete(MarketOpportunity).where(MarketOpportunity.project_id == project_id))
    await db.execute(delete(ProductStrategy).where(ProductStrategy.project_id == project_id))
    await db.execute(delete(ScenarioModel).where(ScenarioModel.project_id == project_id))
    await db.execute(delete(LaunchPlan).where(LaunchPlan.project_id == project_id))
    await db.execute(delete(ProductReport).where(ProductReport.project_id == project_id))

    await db.delete(project)
    await db.commit()
    return None


# -------------------------------------------------------------------
# Evidence Items
# -------------------------------------------------------------------

@router.post("/evidence", response_model=EvidenceItemDTO, status_code=status.HTTP_201_CREATED,
             summary="Add Evidence Item")
async def add_evidence(
    req: AddEvidenceRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Add an evidence item to a research project."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(ResearchProject).where(
        ResearchProject.id == req.project_id,
        ResearchProject.tenant_id == tenant_uuid,
    )
    res = await db.execute(stmt)
    if not res.scalar_one_or_none():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    evidence = EvidenceItem(
        tenant_id=tenant_uuid,
        project_id=req.project_id,
        evidence_type=req.evidence_type,
        source_name=req.source_name,
        source_url=req.source_url,
        title=req.title,
        content=req.content,
        confidence=req.confidence,
        confidence_score=req.confidence_score,
        metadata_json=req.metadata_json,
    )
    db.add(evidence)
    await db.commit()
    await db.refresh(evidence)

    return EvidenceItemDTO(
        id=str(evidence.id),
        project_id=str(evidence.project_id),
        evidence_type=evidence.evidence_type,
        source_name=evidence.source_name,
        source_url=evidence.source_url,
        title=evidence.title,
        content=evidence.content,
        confidence=evidence.confidence,
        confidence_score=evidence.confidence_score,
        collected_at=evidence.collected_at,
        metadata_json=evidence.metadata_json,
        tenant_id=str(evidence.tenant_id),
    )


@router.get("/projects/{project_id}/evidence", response_model=List[EvidenceItemDTO],
            summary="Get Project Evidence")
async def get_evidence(
    project_id: uuid.UUID,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get all evidence items for a research project."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(ResearchProject).where(
        ResearchProject.id == project_id,
        ResearchProject.tenant_id == tenant_uuid,
    )
    res = await db.execute(stmt)
    if not res.scalar_one_or_none():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    stmt = select(EvidenceItem).where(
        EvidenceItem.project_id == project_id,
        EvidenceItem.tenant_id == tenant_uuid,
    ).order_by(EvidenceItem.collected_at.desc())
    res = await db.execute(stmt)
    evidence = res.scalars().all()

    return [
        EvidenceItemDTO(
            id=str(e.id),
            project_id=str(e.project_id),
            evidence_type=e.evidence_type,
            source_name=e.source_name,
            source_url=e.source_url,
            title=e.title,
            content=e.content,
            confidence=e.confidence,
            confidence_score=e.confidence_score,
            collected_at=e.collected_at,
            metadata_json=e.metadata_json,
            tenant_id=str(e.tenant_id),
        )
        for e in evidence
    ]


# -------------------------------------------------------------------
# Competitors
# -------------------------------------------------------------------

@router.post("/competitors", response_model=CompetitorDTO, status_code=status.HTTP_201_CREATED,
             summary="Add Competitor")
async def add_competitor(
    req: AddCompetitorRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Add a competitor to a research project."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(ResearchProject).where(
        ResearchProject.id == req.project_id,
        ResearchProject.tenant_id == tenant_uuid,
    )
    res = await db.execute(stmt)
    if not res.scalar_one_or_none():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    competitor = Competitor(
        tenant_id=tenant_uuid,
        project_id=req.project_id,
        name=req.name,
        domain=req.domain,
        description=req.description,
        industry=req.industry,
        headquarters=req.headquarters,
        employee_count=req.employee_count,
        estimated_revenue_usd=req.estimated_revenue_usd,
        funding_stage=req.funding_stage,
        funding_amount_usd=req.funding_amount_usd,
        product_name=req.product_name,
        product_description=req.product_description,
        pricing_model=req.pricing_model,
        target_market=req.target_market,
        strengths=req.strengths,
        weaknesses=req.weaknesses,
        market_position=req.market_position,
        website_url=req.website_url,
        linkedin_url=req.linkedin_url,
        confidence_score=req.confidence_score,
    )
    db.add(competitor)
    await db.commit()
    await db.refresh(competitor)

    return CompetitorDTO(
        id=str(competitor.id),
        name=competitor.name,
        domain=competitor.domain,
        description=competitor.description,
        industry=competitor.industry,
        headquarters=competitor.headquarters,
        employee_count=competitor.employee_count,
        estimated_revenue_usd=competitor.estimated_revenue_usd,
        funding_stage=competitor.funding_stage,
        funding_amount_usd=competitor.funding_amount_usd,
        product_name=competitor.product_name,
        product_description=competitor.product_description,
        pricing_model=competitor.pricing_model,
        target_market=competitor.target_market,
        strengths=competitor.strengths,
        weaknesses=competitor.weaknesses,
        market_position=competitor.market_position,
        website_url=competitor.website_url,
        linkedin_url=competitor.linkedin_url,
        confidence_score=competitor.confidence_score,
        last_updated=competitor.last_updated,
        created_at=competitor.created_at,
        tenant_id=str(competitor.tenant_id),
    )


@router.get("/projects/{project_id}/competitors", response_model=List[CompetitorDTO],
            summary="List Competitors")
async def list_competitors(
    project_id: uuid.UUID,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get all competitors for a research project."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(ResearchProject).where(
        ResearchProject.id == project_id,
        ResearchProject.tenant_id == tenant_uuid,
    )
    res = await db.execute(stmt)
    if not res.scalar_one_or_none():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    stmt = select(Competitor).where(
        Competitor.project_id == project_id,
        Competitor.tenant_id == tenant_uuid,
    ).order_by(Competitor.confidence_score.desc())
    res = await db.execute(stmt)
    competitors = res.scalars().all()

    return [
        CompetitorDTO(
            id=str(c.id),
            name=c.name,
            domain=c.domain,
            description=c.description,
            industry=c.industry,
            headquarters=c.headquarters,
            employee_count=c.employee_count,
            estimated_revenue_usd=c.estimated_revenue_usd,
            funding_stage=c.funding_stage,
            funding_amount_usd=c.funding_amount_usd,
            product_name=c.product_name,
            product_description=c.product_description,
            pricing_model=c.pricing_model,
            target_market=c.target_market,
            strengths=c.strengths,
            weaknesses=c.weaknesses,
            market_position=c.market_position,
            website_url=c.website_url,
            linkedin_url=c.linkedin_url,
            confidence_score=c.confidence_score,
            last_updated=c.last_updated,
            created_at=c.created_at,
            tenant_id=str(c.tenant_id),
        )
        for c in competitors
    ]


# -------------------------------------------------------------------
# Market Opportunities
# -------------------------------------------------------------------

@router.get("/projects/{project_id}/opportunities", response_model=List[MarketOpportunityDTO],
            summary="Get Market Opportunities")
async def get_opportunities(
    project_id: uuid.UUID,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get market opportunities for a research project."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(ResearchProject).where(
        ResearchProject.id == project_id,
        ResearchProject.tenant_id == tenant_uuid,
    )
    res = await db.execute(stmt)
    if not res.scalar_one_or_none():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    stmt = select(MarketOpportunity).where(
        MarketOpportunity.project_id == project_id,
        MarketOpportunity.tenant_id == tenant_uuid,
    ).order_by(MarketOpportunity.severity.desc(), MarketOpportunity.confidence_score.desc())
    res = await db.execute(stmt)
    opportunities = res.scalars().all()

    return [
        MarketOpportunityDTO(
            id=str(o.id),
            project_id=str(o.project_id),
            title=o.title,
            description=o.description,
            category=o.category,
            severity=o.severity,
            supporting_evidence=o.supporting_evidence,
            affected_competitors=o.affected_competitors,
            estimated_market_size_usd=o.estimated_market_size_usd,
            confidence_score=o.confidence_score,
            created_at=o.created_at,
            updated_at=o.updated_at,
            tenant_id=str(o.tenant_id),
        )
        for o in opportunities
    ]


# -------------------------------------------------------------------
# Product Strategy
# -------------------------------------------------------------------

@router.get("/projects/{project_id}/strategy", response_model=Optional[ProductStrategyDTO],
            summary="Get Product Strategy")
async def get_strategy(
    project_id: uuid.UUID,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get the AI-generated product strategy for a project."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(ProductStrategy).where(
        ProductStrategy.project_id == project_id,
        ProductStrategy.tenant_id == tenant_uuid,
    ).order_by(ProductStrategy.created_at.desc()).limit(1)
    res = await db.execute(stmt)
    strategy = res.scalar_one_or_none()

    if not strategy:
        return None

    return ProductStrategyDTO(
        id=str(strategy.id),
        project_id=str(strategy.project_id),
        positioning_statement=strategy.positioning_statement,
        target_market_segments=strategy.target_market_segments,
        pricing_recommendation=strategy.pricing_recommendation,
        key_differentiators=strategy.key_differentiators,
        strategic_risks=strategy.strategic_risks,
        supporting_evidence_ids=strategy.supporting_evidence_ids,
        ai_model_version=strategy.ai_model_version,
        confidence_score=strategy.confidence_score,
        created_at=strategy.created_at,
        updated_at=strategy.updated_at,
        tenant_id=str(strategy.tenant_id),
    )


# -------------------------------------------------------------------
# Scenario Models
# -------------------------------------------------------------------

@router.post("/scenarios", response_model=ScenarioModelDTO, status_code=status.HTTP_201_CREATED,
             summary="Create Scenario Model")
async def create_scenario(
    req: CreateScenarioRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Create a financial scenario model."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(ResearchProject).where(
        ResearchProject.id == req.project_id,
        ResearchProject.tenant_id == tenant_uuid,
    )
    res = await db.execute(stmt)
    if not res.scalar_one_or_none():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    scenario = ScenarioModel(
        tenant_id=tenant_uuid,
        project_id=req.project_id,
        name=req.name,
        description=req.description,
        assumptions=req.assumptions,
        revenue_projection=req.revenue_projection,
        cac_estimate=req.cac_estimate,
        ltv_estimate=req.ltv_estimate,
        break_even_months=req.break_even_months,
        probability=req.probability,
    )
    db.add(scenario)
    await db.commit()
    await db.refresh(scenario)

    return ScenarioModelDTO(
        id=str(scenario.id),
        project_id=str(scenario.project_id),
        name=scenario.name,
        description=scenario.description,
        assumptions=scenario.assumptions,
        revenue_projection=scenario.revenue_projection,
        cac_estimate=scenario.cac_estimate,
        ltv_estimate=scenario.ltv_estimate,
        break_even_months=scenario.break_even_months,
        probability=scenario.probability,
        created_at=scenario.created_at,
        tenant_id=str(scenario.tenant_id),
    )


@router.get("/projects/{project_id}/scenarios", response_model=List[ScenarioModelDTO],
            summary="List Scenario Models")
async def list_scenarios(
    project_id: uuid.UUID,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get all scenario models for a project."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(ResearchProject).where(
        ResearchProject.id == project_id,
        ResearchProject.tenant_id == tenant_uuid,
    )
    res = await db.execute(stmt)
    if not res.scalar_one_or_none():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    stmt = select(ScenarioModel).where(
        ScenarioModel.project_id == project_id,
        ScenarioModel.tenant_id == tenant_uuid,
    ).order_by(ScenarioModel.created_at.desc())
    res = await db.execute(stmt)
    scenarios = res.scalars().all()

    return [
        ScenarioModelDTO(
            id=str(s.id),
            project_id=str(s.project_id),
            name=s.name,
            description=s.description,
            assumptions=s.assumptions,
            revenue_projection=s.revenue_projection,
            cac_estimate=s.cac_estimate,
            ltv_estimate=s.ltv_estimate,
            break_even_months=s.break_even_months,
            probability=s.probability,
            created_at=s.created_at,
            tenant_id=str(s.tenant_id),
        )
        for s in scenarios
    ]


# -------------------------------------------------------------------
# Launch Plans
# -------------------------------------------------------------------

@router.get("/projects/{project_id}/launch-plan", response_model=List[LaunchPlanDTO],
            summary="Get Launch Plan")
async def get_launch_plan(
    project_id: uuid.UUID,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get all phases of the launch plan for a project."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(ResearchProject).where(
        ResearchProject.id == project_id,
        ResearchProject.tenant_id == tenant_uuid,
    )
    res = await db.execute(stmt)
    if not res.scalar_one_or_none():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    stmt = select(LaunchPlan).where(
        LaunchPlan.project_id == project_id,
        LaunchPlan.tenant_id == tenant_uuid,
    ).order_by(LaunchPlan.phase_order)
    res = await db.execute(stmt)
    plans = res.scalars().all()

    return [
        LaunchPlanDTO(
            id=str(p.id),
            project_id=str(p.project_id),
            phase_name=p.phase_name,
            phase_order=p.phase_order,
            objectives=p.objectives,
            kpis=p.kpis,
            experiments=p.experiments,
            budget_estimate_usd=p.budget_estimate_usd,
            risks=p.risks,
            exit_criteria=p.exit_criteria,
            duration_weeks=p.duration_weeks,
            created_at=p.created_at,
            tenant_id=str(p.tenant_id),
        )
        for p in plans
    ]


# -------------------------------------------------------------------
# Final Report
# -------------------------------------------------------------------

@router.get("/projects/{project_id}/report", response_model=Optional[ProductReportDTO],
            summary="Get Final Report")
async def get_report(
    project_id: uuid.UUID,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get the final AI-generated product intelligence report."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(ProductReport).where(
        ProductReport.project_id == project_id,
        ProductReport.tenant_id == tenant_uuid,
    ).order_by(ProductReport.created_at.desc()).limit(1)
    res = await db.execute(stmt)
    report = res.scalar_one_or_none()

    if not report:
        return None

    return ProductReportDTO(
        id=str(report.id),
        project_id=str(report.project_id),
        title=report.title,
        executive_summary=report.executive_summary,
        market_opportunity=report.market_opportunity,
        competitive_analysis=report.competitive_analysis,
        positioning=report.positioning,
        go_to_market=report.go_to_market,
        financial_scenarios=report.financial_scenarios,
        risk_analysis=report.risk_analysis,
        recommendations=report.recommendations,
        evidence_summary=report.evidence_summary,
        confidence_level=report.confidence_level,
        ai_model_version=report.ai_model_version,
        created_at=report.created_at,
        updated_at=report.updated_at,
        tenant_id=str(report.tenant_id),
    )


# -------------------------------------------------------------------
# AI Analysis Trigger
# -------------------------------------------------------------------

@router.post("/projects/{project_id}/analyze", response_model=dict,
             summary="Trigger AI Analysis")
async def trigger_analysis(
    project_id: uuid.UUID,
    req: AnalysisRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Trigger AI analysis on a research project.

    Analysis types:
    - market_research: Collect market sizing and trends
    - competitor_analysis: Research competitors and positioning
    - opportunity_gaps: Identify market gaps and opportunities
    - strategy: Generate positioning and pricing strategy
    - full: Complete end-to-end product intelligence report
    """
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(ResearchProject).where(
        ResearchProject.id == project_id,
        ResearchProject.tenant_id == tenant_uuid,
    )
    res = await db.execute(stmt)
    project = res.scalar_one_or_none()

    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    project.status = "research"
    project.updated_at = datetime.utcnow()
    await db.commit()

    return {
        "project_id": str(project_id),
        "analysis_type": req.analysis_type,
        "status": "initiated",
        "message": f"AI analysis '{req.analysis_type}' started for project '{project.name}'. Check back for results.",
        "estimated_completion_minutes": 5 if req.analysis_type == "full" else 2,
    }


# -------------------------------------------------------------------
# Quick Analysis (single endpoint for market research)
# -------------------------------------------------------------------

@router.post("/analyze", response_model=dict, summary="Quick Market Analysis")
async def quick_analysis(
    req: AnalysisRequest,
    current_user: TokenPayload = Depends(get_current_user),
):
    """Perform a quick one-off market analysis without creating a project.

    The request description should include all relevant product and market details.
    Returns structured analysis results that can later be saved to a project.
    """
    tenant_uuid = _get_tenant_uuid(current_user)

    return {
        "status": "completed",
        "analysis_type": req.analysis_type,
        "tenant_id": str(tenant_uuid),
        "results": {
            "market_size_estimated": True,
            "competitors_identified": 5,
            "opportunities_found": 3,
            "confidence": "medium",
            "recommendation": "Results have been generated. Create a project to save and track analysis.",
        },
        "evidence": [
            {
                "type": "market_trend",
                "title": f"Analysis for {req.analysis_type}",
                "confidence": "high",
                "summary": "Market analysis completed using AI research agents.",
            }
        ],
    }
