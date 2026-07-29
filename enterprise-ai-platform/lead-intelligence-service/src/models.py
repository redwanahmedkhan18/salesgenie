"""
Lead Intelligence Service Models
Database models for company discovery, contact enrichment, and AI qualification.
"""

import uuid
from datetime import datetime, timezone
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from sqlalchemy import Column, String, Float, Integer, Boolean, DateTime, Text, JSON
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# ============================================================================
# Database Models
# ============================================================================

class Company(Base):
    __tablename__ = "lead_intelligence_companies"

    id: uuid.UUID = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False, index=True)
    
    # Company Profile
    name: str = Column(String(255), nullable=False, index=True)
    domain: Optional[str] = Column(String(255), nullable=True, index=True)
    industry: Optional[str] = Column(String(100), nullable=True, index=True)
    description: Optional[str] = Column(Text, nullable=True)
    employee_count: Optional[int] = Column(Integer, nullable=True)
    estimated_revenue_usd: Optional[float] = Column(Float, nullable=True)
    headquarters_location: Optional[str] = Column(String(200), nullable=True)
    country: Optional[str] = Column(String(100), nullable=True)
    state: Optional[str] = Column(String(100), nullable=True)
    city: Optional[str] = Column(String(100), nullable=True)
    
    # Technology & Growth
    technologies: Optional[Dict[str, Any]] = Column(JSON, nullable=True)
    funding_stage: Optional[str] = Column(String(50), nullable=True)
    funding_amount_usd: Optional[float] = Column(Float, nullable=True)
    growth_signals: Optional[Dict[str, Any]] = Column(JSON, nullable=True)
    news_mentions: Optional[int] = Column(Integer, default=0)
    
    # Social & Media
    website_url: Optional[str] = Column(String(500), nullable=True)
    linkedin_url: Optional[str] = Column(String(500), nullable=True)
    twitter_url: Optional[str] = Column(String(500), nullable=True)
    
    # Metadata
    source: Optional[str] = Column(String(100), nullable=True)
    confidence_score: float = Column(Float, default=0.5, nullable=False)
    language: Optional[str] = Column(String(10), nullable=True, default='en')
    last_enriched_at: Optional[datetime] = Column(DateTime(timezone=True), nullable=True)
    created_at: datetime = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))


class Contact(Base):
    __tablename__ = "lead_intelligence_contacts"

    id: uuid.UUID = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False, index=True)
    company_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False, index=True)
    
    # Contact Info
    full_name: str = Column(String(255), nullable=False)
    email: Optional[str] = Column(String(255), nullable=True, index=True)
    phone: Optional[str] = Column(String(30), nullable=True)
    
    # Role & Seniority
    job_title: Optional[str] = Column(String(150), nullable=True)
    seniority_level: Optional[str] = Column(String(50), nullable=True)  # executive, manager, director, etc.
    department: Optional[str] = Column(String(100), nullable=True)
    
    # Decision Making
    is_decision_maker: bool = Column(Boolean, default=False)
    decision_influence: int = Column(Integer, default=50)  # 0-100 scale
    
    # Social
    linkedin_url: Optional[str] = Column(String(500), nullable=True)
    twitter_url: Optional[str] = Column(String(500), nullable=True)
    
    # Metadata
    source: Optional[str] = Column(String(100), nullable=True)
    confidence_score: float = Column(Float, default=0.5, nullable=False)
    language: Optional[str] = Column(String(10), nullable=True, default='en')
    enrichment_history: Optional[List[Dict[str, Any]]] = Column(JSON, nullable=True)
    created_at: datetime = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))


class LeadScore(Base):
    __tablename__ = "lead_intelligence_scores"

    id: uuid.UUID = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False, index=True)
    company_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False)
    contact_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=True)
    
    # Scoring
    total_score: int = Column(Integer, nullable=False, default=0)  # 0-100
    icp_match_score: int = Column(Integer, nullable=False, default=0)  # Ideal Customer Profile
    buying_intent_score: int = Column(Integer, nullable=False, default=0)
    engagement_score: int = Column(Integer, nullable=False, default=0)
    
    # Factors
    industry_match: int = Column(Integer, nullable=False, default=0)
    company_size_match: int = Column(Integer, nullable=False, default=0)
    revenue_match: int = Column(Integer, nullable=False, default=0)
    technology_match: int = Column(Integer, nullable=False, default=0)
    growth_signals: int = Column(Integer, nullable=False, default=0)
    
    # AI Insights
    pain_points_identified: Optional[List[str]] = Column(JSON, nullable=True)
    use_cases: Optional[List[str]] = Column(JSON, nullable=True)
    challenges: Optional[List[str]] = Column(JSON, nullable=True)
    
    # Recommendation
    recommended_salesperson_id: Optional[uuid.UUID] = Column(PGUUID(as_uuid=True), nullable=True)
    recommended_workflow: Optional[str] = Column(String(100), nullable=True)
    
    # Metadata
    scored_at: datetime = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    expires_at: Optional[datetime] = Column(DateTime(timezone=True), nullable=True)


class QualificationReport(Base):
    __tablename__ = "lead_intelligence_qualifications"

    id: uuid.UUID = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False, index=True)
    company_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False)
    contact_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=True)
    
    # Executive Summary
    business_summary: str = Column(Text, nullable=False)
    opportunity_assessment: str = Column(Text, nullable=False)
    risk_assessment: str = Column(Text, nullable=False)
    
    # Analysis
    technology_analysis: str = Column(Text, nullable=True)
    growth_analysis: str = Column(Text, nullable=True)
    competitive_landscape: str = Column(Text, nullable=True)
    
    # Recommendations
    recommended_pitch: str = Column(Text, nullable=True)
    outreach_recommendations: Optional[Dict[str, Any]] = Column(JSON, nullable=True)
    
    # Generated By
    ai_model_version: str = Column(String(50), nullable=False)
    generated_at: datetime = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))


class OutreachDraft(Base):
    __tablename__ = "lead_intelligence_outreach_drafts"

    id: uuid.UUID = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False, index=True)
    company_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False)
    contact_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=True)
    
    # Channels
    email_draft: Optional[str] = Column(Text, nullable=True)
    linkedin_draft: Optional[str] = Column(Text, nullable=True)
    whatsapp_draft: Optional[str] = Column(Text, nullable=True)
    
    # Sequence
    sequence_steps: Optional[List[Dict[str, Any]]] = Column(JSON, nullable=True)
    follow_up_days: Optional[List[int]] = Column(JSON, nullable=True)
    
    # Language Support
    channel: str = Column(String(50), nullable=False)  # email, linkedin, whatsapp
    language: Optional[str] = Column(String(10), nullable=True, default='en')
    created_at: datetime = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))


class SearchProfile(Base):
    __tablename__ = "lead_intelligence_search_profiles"

    id: uuid.UUID = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False, index=True)
    
    name: str = Column(String(100), nullable=False)
    industry: Optional[str] = Column(String(100), nullable=True)
    location: Optional[str] = Column(String(200), nullable=True)
    min_employee_count: Optional[int] = Column(Integer, nullable=True)
    max_employee_count: Optional[int] = Column(Integer, nullable=True)
    min_revenue_usd: Optional[float] = Column(Float, nullable=True)
    max_revenue_usd: Optional[float] = Column(Float, nullable=True)
    technologies: Optional[List[str]] = Column(JSON, nullable=True)
    keywords: Optional[List[str]] = Column(JSON, nullable=True)
    funding_stage: Optional[str] = Column(String(50), nullable=True)
    
    # Schedule
    is_active: bool = Column(Boolean, default=True)
    schedule_cron: Optional[str] = Column(String(100), nullable=True)  # cron expression
    last_run_at: Optional[datetime] = Column(DateTime(timezone=True), nullable=True)
    next_run_at: Optional[datetime] = Column(DateTime(timezone=True), nullable=True)
    
    created_at: datetime = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))


# ============================================================================
# Pydantic Schemas / DTOs
# ============================================================================

class CompanyDTO(BaseModel):
    id: str
    tenant_id: str
    name: str
    domain: Optional[str] = None
    industry: Optional[str] = None
    description: Optional[str] = None
    employee_count: Optional[int] = None
    estimated_revenue_usd: Optional[float] = None
    headquarters_location: Optional[str] = None
    country: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    technologies: Optional[Dict[str, Any]] = None
    funding_stage: Optional[str] = None
    funding_amount_usd: Optional[float] = None
    growth_signals: Optional[Dict[str, Any]] = None
    news_mentions: int = 0
    website_url: Optional[str] = None
    linkedin_url: Optional[str] = None
    twitter_url: Optional[str] = None
    source: Optional[str] = None
    confidence_score: float = 0.5
    language: Optional[str] = 'en'
    last_enriched_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ContactDTO(BaseModel):
    id: str
    tenant_id: str
    company_id: str
    full_name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    job_title: Optional[str] = None
    seniority_level: Optional[str] = None
    department: Optional[str] = None
    is_decision_maker: bool = False
    decision_influence: int = 50
    linkedin_url: Optional[str] = None
    twitter_url: Optional[str] = None
    source: Optional[str] = None
    confidence_score: float = 0.5
    language: Optional[str] = 'en'
    enrichment_history: Optional[List[Dict[str, Any]]] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class LeadScoreDTO(BaseModel):
    id: str
    tenant_id: str
    company_id: str
    contact_id: Optional[str] = None
    total_score: int
    icp_match_score: int
    buying_intent_score: int
    engagement_score: int
    pain_points_identified: Optional[List[str]] = None
    use_cases: Optional[List[str]] = None
    recommended_salesperson_id: Optional[str] = None
    recommended_workflow: Optional[str] = None
    scored_at: datetime

    class Config:
        from_attributes = True


class QualificationReportDTO(BaseModel):
    id: str
    tenant_id: str
    company_id: str
    contact_id: Optional[str] = None
    business_summary: str
    opportunity_assessment: str
    risk_assessment: str
    technology_analysis: Optional[str] = None
    growth_analysis: Optional[str] = None
    recommended_pitch: Optional[str] = None
    ai_model_version: str
    language: Optional[str] = 'en'
    generated_at: datetime

    class Config:
        from_attributes = True


class OutreachDraftDTO(BaseModel):
    id: str
    tenant_id: str
    company_id: str
    contact_id: Optional[str] = None
    email_draft: Optional[str] = None
    linkedin_draft: Optional[str] = None
    whatsapp_draft: Optional[str] = None
    channel: str
    language: Optional[str] = 'en'
    sequence_steps: Optional[List[Dict[str, Any]]] = None
    follow_up_days: Optional[List[int]] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class SearchProfileDTO(BaseModel):
    id: str
    tenant_id: str
    name: str
    industry: Optional[str] = None
    location: Optional[str] = None
    min_employee_count: Optional[int] = None
    max_employee_count: Optional[int] = None
    min_revenue_usd: Optional[float] = None
    max_revenue_usd: Optional[float] = None
    technologies: Optional[List[str]] = None
    keywords: Optional[List[str]] = None
    funding_stage: Optional[str] = None
    is_active: bool = True
    schedule_cron: Optional[str] = None
    last_run_at: Optional[datetime] = None
    next_run_at: Optional[datetime] = None
    language: Optional[str] = 'en'
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True