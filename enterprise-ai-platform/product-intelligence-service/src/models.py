"""
Product Intelligence Service Data Models & Schemas
Database models for market research projects, competitor analysis,
opportunity detection, and launch strategy recommendations.
"""

import uuid
from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from sqlalchemy import Column, String, Text, Integer, Boolean, DateTime, Float, JSON
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ProjectStatus(str, ):
    """Product intelligence project status."""
    DRAFT = "draft"
    RESEARCH = "research"
    ANALYSIS = "analysis"
    REVIEW = "review"
    COMPLETED = "completed"
    ARCHIVED = "archived"


class EvidenceConfidence(str, ):
    """Confidence level for evidence items."""
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    UNKNOWN = "unknown"


class EvidenceType(str, ):
    """Types of evidence sources."""
    WEB_SEARCH = "web_search"
    NEWS = "news"
    REPORT = "report"
    COMPETITOR_WEBSITE = "competitor_website"
    CUSTOMER_FEEDBACK = "customer_feedback"
    INDUSTRY_ANALYSIS = "industry_analysis"
    FINANCIAL_DATA = "financial_data"
    SOCIAL_MEDIA = "social_media"
    REVIEW_SITE = "review_site"
    MCP_TOOL = "mcp_tool"


# ============================================================================
# Database Models
# ============================================================================

class ResearchProject(Base):
    """A product intelligence research project initiated by a user."""
    __tablename__ = "pi_research_projects"

    id: uuid.UUID = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False, index=True)

    name: str = Column(String(255), nullable=False)
    description: Optional[str] = Column(Text, nullable=True)
    product_name: str = Column(String(255), nullable=False)
    product_description: Text = Column(Text, nullable=False)
    product_category: str = Column(String(100), nullable=False)
    target_market: str = Column(String(200), nullable=False)
    geographic_market: str = Column(String(200), nullable=False)
    business_model: Optional[str] = Column(Text, nullable=True)
    expected_price: Optional[str] = Column(String(100), nullable=True)
    product_stage: Optional[str] = Column(String(50), nullable=True)
    competitive_advantages: Optional[str] = Column(Text, nullable=True)

    status: str = Column(String(20), nullable=False, default=ProjectStatus.DRAFT)
    created_by: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False)
    created_at: datetime = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at: datetime = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)


class EvidenceItem(Base):
    """Raw evidence collected during research."""
    __tablename__ = "pi_evidence_items"

    id: uuid.UUID = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False, index=True)
    project_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False, index=True)

    evidence_type: str = Column(String(50), nullable=False)
    source_name: str = Column(String(255), nullable=False)
    source_url: Optional[str] = Column(String(500), nullable=True)
    title: str = Column(String(500), nullable=False)
    content: Text = Column(Text, nullable=False)
    confidence: str = Column(String(20), nullable=False, default=EvidenceConfidence.UNKNOWN)
    confidence_score: float = Column(Float, default=0.5, nullable=False)
    collected_at: datetime = Column(DateTime(timezone=True), default=datetime.utcnow)
    metadata_json: Optional[dict] = Column(JSON, nullable=True)


class Competitor(Base):
    """Competitor company profile."""
    __tablename__ = "pi_competitors"

    id: uuid.UUID = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False, index=True)
    project_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False, index=True)

    name: str = Column(String(255), nullable=False)
    domain: Optional[str] = Column(String(255), nullable=True)
    description: Optional[str] = Column(Text, nullable=True)
    industry: Optional[str] = Column(String(100), nullable=True)
    headquarters: Optional[str] = Column(String(200), nullable=True)
    employee_count: Optional[int] = Column(Integer, nullable=True)
    estimated_revenue_usd: Optional[float] = Column(Float, nullable=True)
    funding_stage: Optional[str] = Column(String(50), nullable=True)
    funding_amount_usd: Optional[float] = Column(Float, nullable=True)

    product_name: Optional[str] = Column(String(255), nullable=True)
    product_description: Optional[str] = Column(Text, nullable=True)
    pricing_model: Optional[str] = Column(Text, nullable=True)
    target_market: Optional[str] = Column(String(200), nullable=True)

    strengths: Optional[List[str]] = Column(JSON, nullable=True)
    weaknesses: Optional[List[str]] = Column(JSON, nullable=True)
    market_position: Optional[str] = Column(String(100), nullable=True)

    website_url: Optional[str] = Column(String(500), nullable=True)
    linkedin_url: Optional[str] = Column(String(500), nullable=True)

    confidence_score: float = Column(Float, default=0.5, nullable=False)
    last_updated: datetime = Column(DateTime(timezone=True), default=datetime.utcnow)
    created_at: datetime = Column(DateTime(timezone=True), default=datetime.utcnow)


class MarketOpportunity(Base):
    """Identified market opportunity from gap analysis."""
    __tablename__ = "pi_market_opportunities"

    id: uuid.UUID = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False, index=True)
    project_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False, index=True)

    title: str = Column(String(255), nullable=False)
    description: Text = Column(Text, nullable=False)
    category: str = Column(String(100), nullable=False)
    severity: str = Column(String(20), nullable=False, default="high")

    supporting_evidence: Optional[List[Dict[str, Any]]] = Column(JSON, nullable=True)
    affected_competitors: Optional[List[str]] = Column(JSON, nullable=True)
    estimated_market_size_usd: Optional[float] = Column(Float, nullable=True)
    confidence_score: float = Column(Float, default=0.5, nullable=False)

    created_at: datetime = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at: datetime = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)


class ProductStrategy(Base):
    """AI-generated product strategy recommendation."""
    __tablename__ = "pi_product_strategies"

    id: uuid.UUID = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False, index=True)
    project_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False, index=True)

    positioning_statement: Text = Column(Text, nullable=False)
    target_market_segments: Optional[List[str]] = Column(JSON, nullable=True)
    pricing_recommendation: Optional[Dict[str, Any]] = Column(JSON, nullable=True)
    key_differentiators: Optional[List[str]] = Column(JSON, nullable=True)
    strategic_risks: Optional[List[str]] = Column(JSON, nullable=True)
    supporting_evidence_ids: Optional[List[str]] = Column(JSON, nullable=True)
    ai_model_version: str = Column(String(50), nullable=False)
    confidence_score: float = Column(Float, default=0.5, nullable=False)
    created_at: datetime = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at: datetime = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)


class ScenarioModel(Base):
    """Financial scenario model for product launch."""
    __tablename__ = "pi_scenario_models"

    id: uuid.UUID = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False, index=True)
    project_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False, index=True)

    name: str = Column(String(100), nullable=False)
    description: Optional[str] = Column(Text, nullable=True)
    assumptions: Optional[Dict[str, Any]] = Column(JSON, nullable=True)
    revenue_projection: Optional[Dict[str, Any]] = Column(JSON, nullable=True)
    cac_estimate: Optional[float] = Column(Float, nullable=True)
    ltv_estimate: Optional[float] = Column(Float, nullable=True)
    break_even_months: Optional[int] = Column(Integer, nullable=True)
    probability: float = Column(Float, default=0.33, nullable=False)
    created_at: datetime = Column(DateTime(timezone=True), default=datetime.utcnow)


class LaunchPlan(Base):
    """90-day product launch plan."""
    __tablename__ = "pi_launch_plans"

    id: uuid.UUID = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False, index=True)
    project_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False, index=True)

    phase_name: str = Column(String(100), nullable=False)
    phase_order: int = Column(Integer, nullable=False)
    objectives: Optional[List[str]] = Column(JSON, nullable=True)
    kpis: Optional[List[str]] = Column(JSON, nullable=True)
    experiments: Optional[List[Dict[str, Any]]] = Column(JSON, nullable=True)
    budget_estimate_usd: Optional[float] = Column(Float, nullable=True)
    risks: Optional[List[str]] = Column(JSON, nullable=True)
    exit_criteria: Optional[List[str]] = Column(JSON, nullable=True)
    duration_weeks: Optional[int] = Column(Integer, nullable=True)
    created_at: datetime = Column(DateTime(timezone=True), default=datetime.utcnow)


class ProductReport(Base):
    """Final consolidated AI-generated report."""
    __tablename__ = "pi_reports"

    id: uuid.UUID = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False, index=True)
    project_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False, unique=True, index=True)

    title: str = Column(String(255), nullable=False)
    executive_summary: Text = Column(Text, nullable=False)
    market_opportunity: Text = Column(Text, nullable=False)
    competitive_analysis: Text = Column(Text, nullable=False)
    positioning: Text = Column(Text, nullable=False)
    go_to_market: Text = Column(Text, nullable=False)
    financial_scenarios: Optional[Dict[str, Any]] = Column(JSON, nullable=True)
    risk_analysis: Text = Column(Text, nullable=False)
    recommendations: Text = Column(Text, nullable=False)
    evidence_summary: Optional[Dict[str, Any]] = Column(JSON, nullable=True)
    confidence_level: str = Column(String(20), nullable=False, default=EvidenceConfidence.MEDIUM)
    ai_model_version: str = Column(String(50), nullable=False)
    created_at: datetime = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at: datetime = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)


# ============================================================================
# Pydantic DTOs
# ============================================================================

class ResearchProjectDTO(BaseModel):
    id: str
    name: str
    description: Optional[str]
    product_name: str
    product_description: str
    product_category: str
    target_market: str
    geographic_market: str
    business_model: Optional[str]
    expected_price: Optional[str]
    product_stage: Optional[str]
    competitive_advantages: Optional[str]
    status: str
    created_by: str
    tenant_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class CreateProjectRequest(BaseModel):
    name: str
    description: Optional[str] = None
    product_name: str
    product_description: str
    product_category: str
    target_market: str
    geographic_market: str
    business_model: Optional[str] = None
    expected_price: Optional[str] = None
    product_stage: Optional[str] = None
    competitive_advantages: Optional[str] = None


class UpdateProjectRequest(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    product_name: Optional[str] = None
    product_description: Optional[str] = None
    product_category: Optional[str] = None
    target_market: Optional[str] = None
    geographic_market: Optional[str] = None
    business_model: Optional[str] = None
    expected_price: Optional[str] = None
    product_stage: Optional[str] = None
    competitive_advantages: Optional[str] = None
    status: Optional[str] = None


class EvidenceItemDTO(BaseModel):
    id: str
    project_id: str
    evidence_type: str
    source_name: str
    source_url: Optional[str]
    title: str
    content: str
    confidence: str
    confidence_score: float
    collected_at: datetime
    metadata_json: Optional[Dict[str, Any]]
    tenant_id: str

    class Config:
        from_attributes = True


class AddEvidenceRequest(BaseModel):
    evidence_type: str
    source_name: str
    source_url: Optional[str] = None
    title: str
    content: str
    confidence: str = "unknown"
    confidence_score: float = 0.5
    metadata_json: Optional[Dict[str, Any]] = None


class CompetitorDTO(BaseModel):
    id: str
    name: str
    domain: Optional[str]
    description: Optional[str]
    industry: Optional[str]
    headquarters: Optional[str]
    employee_count: Optional[int]
    estimated_revenue_usd: Optional[float]
    funding_stage: Optional[str]
    funding_amount_usd: Optional[float]
    product_name: Optional[str]
    product_description: Optional[str]
    pricing_model: Optional[str]
    target_market: Optional[str]
    strengths: Optional[List[str]]
    weaknesses: Optional[List[str]]
    market_position: Optional[str]
    website_url: Optional[str]
    linkedin_url: Optional[str]
    confidence_score: float
    last_updated: datetime
    created_at: datetime
    tenant_id: str

    class Config:
        from_attributes = True


class AddCompetitorRequest(BaseModel):
    project_id: uuid.UUID
    name: str
    domain: Optional[str] = None
    description: Optional[str] = None
    industry: Optional[str] = None
    headquarters: Optional[str] = None
    employee_count: Optional[int] = None
    estimated_revenue_usd: Optional[float] = None
    funding_stage: Optional[str] = None
    funding_amount_usd: Optional[float] = None
    product_name: Optional[str] = None
    product_description: Optional[str] = None
    pricing_model: Optional[str] = None
    target_market: Optional[str] = None
    strengths: Optional[List[str]] = None
    weaknesses: Optional[List[str]] = None
    market_position: Optional[str] = None
    website_url: Optional[str] = None
    linkedin_url: Optional[str] = None
    confidence_score: float = 0.5


class MarketOpportunityDTO(BaseModel):
    id: str
    project_id: str
    title: str
    description: str
    category: str
    severity: str
    supporting_evidence: Optional[List[Dict[str, Any]]]
    affected_competitors: Optional[List[str]]
    estimated_market_size_usd: Optional[float]
    confidence_score: float
    created_at: datetime
    updated_at: datetime
    tenant_id: str

    class Config:
        from_attributes = True


class ProductStrategyDTO(BaseModel):
    id: str
    project_id: str
    positioning_statement: str
    target_market_segments: Optional[List[str]]
    pricing_recommendation: Optional[Dict[str, Any]]
    key_differentiators: Optional[List[str]]
    strategic_risks: Optional[List[str]]
    supporting_evidence_ids: Optional[List[str]]
    ai_model_version: str
    confidence_score: float
    created_at: datetime
    updated_at: datetime
    tenant_id: str

    class Config:
        from_attributes = True


class ScenarioModelDTO(BaseModel):
    id: str
    project_id: str
    name: str
    description: Optional[str]
    assumptions: Optional[Dict[str, Any]]
    revenue_projection: Optional[Dict[str, Any]]
    cac_estimate: Optional[float]
    ltv_estimate: Optional[float]
    break_even_months: Optional[int]
    probability: float
    created_at: datetime
    tenant_id: str

    class Config:
        from_attributes = True


class CreateScenarioRequest(BaseModel):
    project_id: uuid.UUID
    name: str
    description: Optional[str] = None
    assumptions: Optional[Dict[str, Any]] = None
    revenue_projection: Optional[Dict[str, Any]] = None
    cac_estimate: Optional[float] = None
    ltv_estimate: Optional[float] = None
    break_even_months: Optional[int] = None
    probability: float = 0.33


class LaunchPlanDTO(BaseModel):
    id: str
    project_id: str
    phase_name: str
    phase_order: int
    objectives: Optional[List[str]]
    kpis: Optional[List[str]]
    experiments: Optional[List[Dict[str, Any]]]
    budget_estimate_usd: Optional[float]
    risks: Optional[List[str]]
    exit_criteria: Optional[List[str]]
    duration_weeks: Optional[int]
    created_at: datetime
    tenant_id: str

    class Config:
        from_attributes = True


class ProductReportDTO(BaseModel):
    id: str
    project_id: str
    title: str
    executive_summary: str
    market_opportunity: str
    competitive_analysis: str
    positioning: str
    go_to_market: str
    financial_scenarios: Optional[Dict[str, Any]]
    risk_analysis: str
    recommendations: str
    evidence_summary: Optional[Dict[str, Any]]
    confidence_level: str
    ai_model_version: str
    created_at: datetime
    updated_at: datetime
    tenant_id: str

    class Config:
        from_attributes = True


class AnalysisRequest(BaseModel):
    """Request to trigger AI analysis on a research project."""
    project_id: uuid.UUID
    analysis_type: str = Field(..., description="market_research, competitor_analysis, opportunity_gaps, strategy, full")
    language: str = "en"
    model: Optional[str] = None
