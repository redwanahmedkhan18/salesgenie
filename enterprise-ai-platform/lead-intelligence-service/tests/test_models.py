"""
Unit tests for Lead Intelligence Service
"""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4
from datetime import datetime, timezone

from enterprise_ai_platform.lead_intelligence_service.src.models import (
    Company, Contact, LeadScore, QualificationReport, OutreachDraft, SearchProfile,
    CompanyDTO, ContactDTO, LeadScoreDTO, QualificationReportDTO, OutreachDraftDTO, SearchProfileDTO
)


class TestCompanyModel:
    def test_company_creation(self):
        company = Company(
            id=uuid4(),
            tenant_id=uuid4(),
            name="Test Company",
            domain="test.com",
            industry="Technology",
            employee_count=100,
            estimated_revenue_usd=1000000.0,
            confidence_score=0.95,
            language="en",
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        
        assert company.name == "Test Company"
        assert company.industry == "Technology"
        assert company.confidence_score == 0.95
        assert company.language == "en"

    def test_company_dto_conversion(self):
        company = Company(
            id=uuid4(),
            tenant_id=uuid4(),
            name="Test Company",
            domain="test.com",
            industry="Technology",
            employee_count=100,
            confidence_score=0.95,
            language="en",
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        
        dto = CompanyDTO.from_orm(company)
        assert dto.name == "Test Company"
        assert dto.industry == "Technology"
        assert dto.language == "en"


class TestContactModel:
    def test_contact_creation(self):
        contact = Contact(
            id=uuid4(),
            tenant_id=uuid4(),
            company_id=uuid4(),
            full_name="John Doe",
            email="john@test.com",
            job_title="CEO",
            is_decision_maker=True,
            decision_influence=90,
            confidence_score=0.98,
            language="en",
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        
        assert contact.full_name == "John Doe"
        assert contact.is_decision_maker is True
        assert contact.decision_influence == 90


class TestLeadScoreModel:
    def test_lead_score_calculation(self):
        score = LeadScore(
            id=uuid4(),
            tenant_id=uuid4(),
            company_id=uuid4(),
            total_score=85,
            icp_match_score=90,
            buying_intent_score=80,
            engagement_score=75,
            industry_match=85,
            company_size_match=80,
            revenue_match=90,
            technology_match=75,
            growth_signals=88,
            pain_points_identated=["Integration complexity", "Data silos"],
            use_cases=["Customer support automation"],
            recommended_workflow="discovery_call",
            scored_at=datetime.now(timezone.utc),
        )
        
        assert score.total_score == 85
        assert "Integration complexity" in score.pain_points_identated


class TestQualificationReportModel:
    def test_qualification_report_creation(self):
        report = QualificationReport(
            id=uuid4(),
            tenant_id=uuid4(),
            company_id=uuid4(),
            business_summary="Test company is a technology startup",
            opportunity_assessment="High potential for AI solutions",
            risk_assessment="Low competition in the space",
            recommended_pitch="AI can help automate customer support",
            ai_model_version="gpt-4o-mini-2024-07",
            generated_at=datetime.now(timezone.utc),
            language="en",
        )
        
        assert report.business_summary == "Test company is a technology startup"
        assert report.language == "en"


class TestOutreachDraftModel:
    def test_outreach_draft_creation(self):
        draft = OutreachDraft(
            id=uuid4(),
            tenant_id=uuid4(),
            company_id=uuid4(),
            email_draft="Subject: Hello from SalesGenie",
            linkedin_draft="Hi there! I noticed your company...",
            channel="email",
            language="en",
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        
        assert draft.channel == "email"
        assert draft.language == "en"
        assert "Hello from SalesGenie" in draft.email_draft


class TestSearchProfileModel:
    def test_search_profile_creation(self):
        profile = SearchProfile(
            id=uuid4(),
            tenant_id=uuid4(),
            name="Tech Companies",
            industry="Technology",
            min_employee_count=50,
            max_employee_count=1000,
            keywords=["AI", "automation"],
            is_active=True,
            language="en",
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        
        assert profile.name == "Tech Companies"
        assert profile.industry == "Technology"
        assert profile.is_active is True


class TestLanguageSupport:
    def test_company_language_support(self):
        languages = ["en", "es", "fr", "de", "zh", "ja", "ar", "hi"]
        
        for lang in languages:
            company = Company(
                id=uuid4(),
                tenant_id=uuid4(),
                name=f"Company {lang}",
                language=lang,
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc),
            )
            assert company.language == lang

    def test_contact_language_support(self):
        languages = ["en", "es", "fr", "de", "zh", "ja", "ar", "hi"]
        
        for lang in languages:
            contact = Contact(
                id=uuid4(),
                tenant_id=uuid4(),
                company_id=uuid4(),
                full_name=f"Contact {lang}",
                language=lang,
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc),
            )
            assert contact.language == lang