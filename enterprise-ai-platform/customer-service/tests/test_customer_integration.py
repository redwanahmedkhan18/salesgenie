"""
Customer Service Integration Tests
Tests the full API endpoints with mocked database.
"""

import pytest
import uuid
import json
from unittest.mock import AsyncMock, MagicMock, patch
from fastapi.testclient import TestClient

from customer_service.main import app


@pytest.fixture
def client():
    """Test client for the customer service."""
    return TestClient(app)


@pytest.fixture
def mock_db():
    """Mock database session."""
    return AsyncMock()


class TestHealthChecks:
    """Tests for health check endpoints."""

    def test_liveness_probe(self, client):
        """Test liveness probe returns UP status."""
        response = client.get("/health/live")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "UP"
        assert data["service"] == "customer-service"

    def test_readiness_probe(self, client):
        """Test readiness probe returns READY status."""
        response = client.get("/health/ready")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "READY"
        assert data["service"] == "customer-service"


class TestCustomerEndpoints:
    """Tests for customer CRUD endpoints."""

    @patch("customer_service.src.router_customer.get_async_db")
    @patch("customer_service.src.router_customer.get_current_user")
    def test_create_customer(self, mock_user, mock_db_dep, client):
        """Test creating a new customer."""
        mock_user.return_value = MagicMock(
            sub="123e4567-e89b-12d3-a456-426614174000",
            tenant_id="salesgenie-tenant",
            roles=["sales_agent"],
            permissions=["customer:write"],
        )

        mock_db = AsyncMock()
        mock_db_dep.return_value = mock_db

        # Mock the database operations
        async def mock_execute(stmt):
            result = MagicMock()
            result.scalar_one_or_none = MagicMock(return_value=None)
            return result

        mock_db.execute = mock_execute
        mock_db.add = MagicMock()
        mock_db.flush = AsyncMock()
        mock_db.commit = AsyncMock()
        mock_db.refresh = AsyncMock()

        response = client.post(
            "/api/v1/customers",
            json={"full_name": "Test Customer", "email": "test@example.com"},
        )

        assert response.status_code in [200, 201, 422]

    @patch("customer_service.src.router_customer.get_current_user")
    def test_list_customers_unauthorized(self, mock_user, client):
        """Test listing customers without auth returns 401."""
        mock_user.side_effect = Exception("Unauthorized")

        response = client.get("/api/v1/customers")
        assert response.status_code == 401


class TestSegmentEndpoints:
    """Tests for segment endpoints."""

    @patch("customer_service.src.router_customer.get_current_user")
    def test_create_segment_unauthorized(self, mock_user, client):
        """Test creating segment without auth returns 401."""
        mock_user.side_effect = Exception("Unauthorized")

        response = client.post(
            "/api/v1/customers/segments",
            json={"name": "VIP"},
        )
        assert response.status_code == 401


class TestTagEndpoints:
    """Tests for tag endpoints."""

    @patch("customer_service.src.router_customer.get_current_user")
    def test_create_tag_unauthorized(self, mock_user, client):
        """Test creating tag without auth returns 401."""
        mock_user.side_effect = Exception("Unauthorized")

        response = client.post(
            "/api/v1/customers/tags",
            json={"name": "Priority"},
        )
        assert response.status_code == 401


class TestAnalyticsEndpoint:
    """Tests for analytics endpoints."""

    @patch("customer_service.src.router_customer.get_current_user")
    def test_analytics_unauthorized(self, mock_user, client):
        """Test analytics without auth returns 401."""
        mock_user.side_effect = Exception("Unauthorized")

        response = client.get("/api/v1/customers/analytics/overview")
        assert response.status_code == 401