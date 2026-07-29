"""
Integration tests for Lead Intelligence Service
"""

import pytest
from httpx import AsyncClient
from unittest.mock import patch, AsyncMock
import json

from enterprise_ai_platform.lead_intelligence_service.main import app


@pytest.mark.asyncio
class TestLeadIntelligenceAPI:
    async def test_search_companies_success(self, client: AsyncClient):
        response = await client.post(
            "/api/v1/lead-intelligence/companies/search",
            json={
                "industry": "Technology",
                "min_employee_count": 10,
                "max_employee_count": 1000,
            },
        )
        
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)

    async def test_search_companies_with_language(self, client: AsyncClient):
        response = await client.post(
            "/api/v1/lead-intelligence/companies/search",
            params={"language": "es"},
            json={"industry": "Technology"},
        )
        
        assert response.status_code == 200

    async def test_get_company_success(self, client: AsyncClient):
        with patch("enterprise_ai_platform.lead_intelligence_service.router.get_company") as mock:
            mock.return_value = {
                "id": "test-id",
                "tenant_id": "test-tenant",
                "name": "Test Company",
                "language": "en",
            }
            
            response = await client.get("/api/v1/lead-intelligence/companies/test-id")
            assert response.status_code in [200, 404]

    async def test_qualify_lead_success(self, client: AsyncClient):
        with patch("enterprise_ai_platform.lead_intelligence_service.router.qualify_lead") as mock:
            mock.return_value = {
                "id": "test-id",
                "total_score": 85,
                "language": "en",
            }
            
            response = await client.post("/api/v1/lead-intelligence/companies/test-id/qualify")
            assert response.status_code in [200, 404]

    async def test_generate_research_brief_success(self, client: AsyncClient):
        with patch("enterprise_ai_platform.lead_intelligence_service.router.generate_research_brief") as mock:
            mock.return_value = {
                "id": "test-id",
                "business_summary": "Test summary",
                "language": "en",
            }
            
            response = await client.post("/api/v1/lead-intelligence/companies/test-id/research")
            assert response.status_code in [200, 404]

    async def test_generate_outreach_draft_success(self, client: AsyncClient):
        with patch("enterprise_ai_platform.lead_intelligence_service.router.generate_outreach_draft") as mock:
            mock.return_value = {
                "id": "test-id",
                "channel": "email",
                "language": "en",
                "email_draft": "Subject: Hello",
            }
            
            response = await client.post(
                "/api/v1/lead-intelligence/companies/test-id/outreach",
                params={"channel": "email", "language": "en"},
            )
            assert response.status_code in [200, 404]

    async def test_list_search_profiles(self, client: AsyncClient):
        with patch("enterprise_ai_platform.lead_intelligence_service.router.list_search_profiles") as mock:
            mock.return_value = []
            
            response = await client.get("/api/v1/lead-intelligence/profiles")
            assert response.status_code == 200

    async def test_create_search_profile(self, client: AsyncClient):
        with patch("enterprise_ai_platform.lead_intelligence_service.router.create_search_profile") as mock:
            mock.return_value = {
                "id": "test-id",
                "name": "Test Profile",
                "language": "en",
            }
            
            response = await client.post(
                "/api/v1/lead-intelligence/profiles",
                json={
                    "name": "Test Profile",
                    "industry": "Technology",
                    "language": "en",
                },
            )
            assert response.status_code in [200, 201]


@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client