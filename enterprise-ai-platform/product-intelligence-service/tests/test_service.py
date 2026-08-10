"""
Test suite for Product Intelligence Service business logic.
Tests models, DTOs, router endpoints, and analysis flows.
"""

import pytest
import uuid
from datetime import datetime, timezone
from unittest.mock import MagicMock, AsyncMock

from enterprise_ai_platform.common.models_base import UUIDPrimaryKeyMixin


@pytest.fixture
def mock_current_user():
    """Mock authenticated user token payload."""
    return MagicMock(
        sub=str(uuid.uuid4()),
        tenant_id="salesgenie-tenant",
        email="pi-manager@salesgenie.ai",
        roles=["knowledge_manager"],
        permissions=["knowledge:read", "knowledge:write"],
        exp=int(datetime.now(timezone.utc).timestamp()) + 3600,
    )


@pytest.fixture
def mock_db_session():
    """Mock async database session."""
    session = AsyncMock()
    session.commit = AsyncMock()
    session.rollback = AsyncMock()
    session.close = AsyncMock()
    session.execute = AsyncMock()
    session.add = MagicMock()
    session.flush = AsyncMock()
    session.refresh = AsyncMock()
    session.delete = AsyncMock()
    return session


class TestProductIntelligenceModels:
    """Test product intelligence models."""

    def test_research_project_has_uuid_primary_key(self):
        from enterprise_ai_platform.product_intelligence_service.src.models import ResearchProject
        assert hasattr(ResearchProject, "id")
        assert hasattr(ResearchProject, "tenant_id")
        assert hasattr(ResearchProject, "name")
        assert hasattr(ResearchProject, "product_name")
        assert hasattr(ResearchProject, "product_category")
        assert hasattr(ResearchProject, "target_market")
        assert hasattr(ResearchProject, "geographic_market")
        assert hasattr(ResearchProject, "status")
        assert hasattr(ResearchProject, "created_by")

    def test_evidence_item_model(self):
        from enterprise_ai_platform.product_intelligence_service.src.models import EvidenceItem
        assert hasattr(EvidenceItem, "project_id")
        assert hasattr(EvidenceItem, "evidence_type")
        assert hasattr(EvidenceItem, "source_name")
        assert hasattr(EvidenceItem, "confidence")
        assert hasattr(EvidenceItem, "confidence_score")

    def test_competitor_model(self):
        from enterprise_ai_platform.product_intelligence_service.src.models import Competitor
        assert hasattr(Competitor, "project_id")
        assert hasattr(Competitor, "name")
        assert hasattr(Competitor, "domain")
        assert hasattr(Competitor, "strengths")
        assert hasattr(Competitor, "weaknesses")
        assert hasattr(Competitor, "confidence_score")
        assert hasattr(Competitor, "pricing_model")
        assert hasattr(Competitor, "market_position")

    def test_market_opportunity_model(self):
        from enterprise_ai_platform.product_intelligence_service.src.models import MarketOpportunity
        assert hasattr(MarketOpportunity, "project_id")
        assert hasattr(MarketOpportunity, "title")
        assert hasattr(MarketOpportunity, "description")
        assert hasattr(MarketOpportunity, "category")
        assert hasattr(MarketOpportunity, "severity")
        assert hasattr(MarketOpportunity, "supporting_evidence")
        assert hasattr(MarketOpportunity, "estimated_market_size_usd")

    def test_product_strategy_model(self):
        from enterprise_ai_platform.product_intelligence_service.src.models import ProductStrategy
        assert hasattr(ProductStrategy, "project_id")
        assert hasattr(ProductStrategy, "positioning_statement")
        assert hasattr(ProductStrategy, "target_market_segments")
        assert hasattr(ProductStrategy, "pricing_recommendation")
        assert hasattr(ProductStrategy, "key_differentiators")
        assert hasattr(ProductStrategy, "strategic_risks")
        assert hasattr(ProductStrategy, "ai_model_version")

    def test_scenario_model(self):
        from enterprise_ai_platform.product_intelligence_service.src.models import ScenarioModel
        assert hasattr(ScenarioModel, "project_id")
        assert hasattr(ScenarioModel, "name")
        assert hasattr(ScenarioModel, "assumptions")
        assert hasattr(ScenarioModel, "revenue_projection")
        assert hasattr(ScenarioModel, "cac_estimate")
        assert hasattr(ScenarioModel, "ltv_estimate")
        assert hasattr(ScenarioModel, "break_even_months")
        assert hasattr(ScenarioModel, "probability")

    def test_launch_plan_model(self):
        from enterprise_ai_platform.product_intelligence_service.src.models import LaunchPlan
        assert hasattr(LaunchPlan, "project_id")
        assert hasattr(LaunchPlan, "phase_name")
        assert hasattr(LaunchPlan, "phase_order")
        assert hasattr(LaunchPlan, "objectives")
        assert hasattr(LaunchPlan, "kpis")
        assert hasattr(LaunchPlan, "experiments")
        assert hasattr(LaunchPlan, "budget_estimate_usd")
        assert hasattr(LaunchPlan, "exit_criteria")

    def test_product_report_model(self):
        from enterprise_ai_platform.product_intelligence_service.src.models import ProductReport
        assert hasattr(ProductReport, "project_id")
        assert hasattr(ProductReport, "title")
        assert hasattr(ProductReport, "executive_summary")
        assert hasattr(ProductReport, "market_opportunity")
        assert hasattr(ProductReport, "competitive_analysis")
        assert hasattr(ProductReport, "positioning")
        assert hasattr(ProductReport, "go_to_market")
        assert hasattr(ProductReport, "financial_scenarios")
        assert hasattr(ProductReport, "risk_analysis")
        assert hasattr(ProductReport, "recommendations")
        assert hasattr(ProductReport, "evidence_summary")
        assert hasattr(ProductReport, "confidence_level")


class TestProductIntelligenceDTOs:
    """Test product intelligence Pydantic DTOs."""

    def test_create_project_request(self):
        from enterprise_ai_platform.product_intelligence_service.src.models import CreateProjectRequest
        req = CreateProjectRequest(
            name="Q3 Product Launch",
            product_name="AI Support",
            product_description="AI customer support platform",
            product_category="SaaS",
            target_market="e-commerce",
            geographic_market="Southeast Asia",
        )
        assert req.name == "Q3 Product Launch"
        assert req.product_name == "AI Support"
        assert req.product_category == "SaaS"

    def test_update_project_request_partial(self):
        from enterprise_ai_platform.product_intelligence_service.src.models import UpdateProjectRequest
        req = UpdateProjectRequest(status="completed")
        assert req.status == "completed"
        assert req.name is None

    def test_add_evidence_request(self):
        from enterprise_ai_platform.product_intelligence_service.src.models import AddEvidenceRequest
        req = AddEvidenceRequest(
            project_id=uuid.uuid4(),
            evidence_type="market_trend",
            source_name="TechCrunch",
            title="SaaS Growth Report",
            content="The SaaS market grew 22% YoY...",
            confidence="high",
            confidence_score=0.9,
        )
        assert req.evidence_type == "market_trend"
        assert req.confidence_score == 0.9

    def test_add_competitor_request(self):
        from enterprise_ai_platform.product_intelligence_service.src.models import AddCompetitorRequest
        req = AddCompetitorRequest(
            project_id=uuid.uuid4(),
            name="Competitor A",
            domain="comp-a.com",
            industry="SaaS",
            strengths=["strong brand"],
            weaknesses=["slow support"],
            confidence_score=0.8,
        )
        assert req.name == "Competitor A"
        assert req.strengths == ["strong brand"]

    def test_create_scenario_request(self):
        from enterprise_ai_platform.product_intelligence_service.src.models import CreateScenarioRequest
        req = CreateScenarioRequest(
            project_id=uuid.uuid4(),
            name="Conservative",
            assumptions={"growth_rate": 0.05},
            revenue_projection={"year_1": 100000},
            cac_estimate=150.0,
            ltv_estimate=1500.0,
            break_even_months=12,
            probability=0.5,
        )
        assert req.name == "Conservative"
        assert req.break_even_months == 12

    def test_analysis_request(self):
        from enterprise_ai_platform.product_intelligence_service.src.models import AnalysisRequest
        req = AnalysisRequest(
            project_id=uuid.uuid4(),
            analysis_type="full",
            language="en",
        )
        assert req.analysis_type == "full"
        assert req.language == "en"


class TestProductIntelligenceRouter:
    """Test product intelligence API router endpoints."""

    @pytest.fixture
    def router(self):
        from enterprise_ai_platform.product_intelligence_service.src.router_product_intelligence import router
        return router

    def test_router_prefix(self, router):
        assert router.prefix == "/api/v1/product-intelligence"

    def test_router_has_project_endpoints(self, router):
        route_paths = [r.path for r in router.routes if hasattr(r, "path")]
        assert "/api/v1/product-intelligence/projects" in route_paths
        assert "/api/v1/product-intelligence/projects/{project_id}" in route_paths

    def test_router_has_evidence_endpoints(self, router):
        route_paths = [r.path for r in router.routes if hasattr(r, "path")]
        assert "/api/v1/product-intelligence/evidence" in route_paths
        assert "/api/v1/product-intelligence/projects/{project_id}/evidence" in route_paths

    def test_router_has_competitor_endpoints(self, router):
        route_paths = [r.path for r in router.routes if hasattr(r, "path")]
        assert "/api/v1/product-intelligence/competitors" in route_paths
        assert "/api/v1/product-intelligence/projects/{project_id}/competitors" in route_paths

    def test_router_has_analysis_endpoints(self, router):
        route_paths = [r.path for r in router.routes if hasattr(r, "path")]
        assert "/api/v1/product-intelligence/projects/{project_id}/analyze" in route_paths
        assert "/api/v1/product-intelligence/analyze" in route_paths

    def test_router_has_strategy_endpoints(self, router):
        route_paths = [r.path for r in router.routes if hasattr(r, "path")]
        assert "/api/v1/product-intelligence/projects/{project_id}/strategy" in route_paths
        assert "/api/v1/product-intelligence/projects/{project_id}/opportunities" in route_paths
        assert "/api/v1/product-intelligence/projects/{project_id}/scenarios" in route_paths
        assert "/api/v1/product-intelligence/projects/{project_id}/launch-plan" in route_paths
        assert "/api/v1/product-intelligence/projects/{project_id}/report" in route_paths

    def test_create_project_callable(self, router):
        from enterprise_ai_platform.product_intelligence_service.src.router_product_intelligence import create_project
        assert callable(create_project)

    def test_list_projects_callable(self, router):
        from enterprise_ai_platform.product_intelligence_service.src.router_product_intelligence import list_projects
        assert callable(list_projects)

    def test_trigger_analysis_callable(self, router):
        from enterprise_ai_platform.product_intelligence_service.src.router_product_intelligence import trigger_analysis
        assert callable(trigger_analysis)

    def test_quick_analysis_callable(self, router):
        from enterprise_ai_platform.product_intelligence_service.src.router_product_intelligence import quick_analysis
        assert callable(quick_analysis)

    def test_add_evidence_callable(self, router):
        from enterprise_ai_platform.product_intelligence_service.src.router_product_intelligence import add_evidence
        assert callable(add_evidence)

    def test_add_competitor_callable(self, router):
        from enterprise_ai_platform.product_intelligence_service.src.router_product_intelligence import add_competitor
        assert callable(add_competitor)


class TestProductIntelligenceTenantIsolation:
    """Test tenant isolation logic."""

    def test_get_tenant_uuid(self, mock_current_user):
        from enterprise_ai_platform.product_intelligence_service.src.router_product_intelligence import _get_tenant_uuid
        result = _get_tenant_uuid(mock_current_user)
        assert isinstance(result, uuid.UUID)
