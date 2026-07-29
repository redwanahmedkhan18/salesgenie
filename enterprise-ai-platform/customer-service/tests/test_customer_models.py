"""
Unit Tests for Customer Service
Tests customer CRUD operations, segments, tags, and analytics.
"""

import pytest
import uuid
from unittest.mock import AsyncMock, MagicMock, patch
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from customer_service.src.models import (
    Customer,
    CustomerSegment,
    CustomerTag,
    CustomerNote,
    CustomerOrder,
    CreateCustomerRequest,
    UpdateCustomerRequest,
    CreateSegmentRequest,
    CreateTagRequest,
    CreateNoteRequest,
)
from customer_service.src.router_customer import (
    _get_tenant_uuid,
    _customer_to_dto,
)


@pytest.fixture
def mock_token_payload():
    """Mock JWT token payload."""
    return MagicMock(
        sub="123e4567-e89b-12d3-a456-426614174000",
        tenant_id="tenant-123",
        roles=["sales_agent"],
        permissions=["customer:read", "customer:write"],
    )


@pytest.fixture
def mock_db():
    """Mock async database session."""
    return AsyncMock(spec=AsyncSession)


@pytest.fixture
def sample_customer():
    """Sample customer model."""
    return Customer(
        id=uuid.uuid4(),
        tenant_id=uuid.uuid4(),
        email="john@example.com",
        phone_number="+15551234567",
        full_name="John Doe",
        company_name="Acme Corp",
        lead_status="warm",
        lead_score=75,
        lifetime_value=1500.00,
        total_orders=3,
        is_active=True,
    )


class TestTenantExtraction:
    """Tests for tenant UUID extraction from token."""

    def test_get_tenant_uuid(self, mock_token_payload):
        """Test tenant UUID extraction."""
        result = _get_tenant_uuid(mock_token_payload)
        assert isinstance(result, uuid.UUID)


class TestCustomerDTO:
    """Tests for customer DTO conversion."""

    def test_customer_to_dto(self, sample_customer):
        """Test customer model to DTO conversion."""
        tenant_uuid = sample_customer.tenant_id
        dto = _customer_to_dto(sample_customer, tenant_uuid)

        assert dto.id == sample_customer.id
        assert dto.email == sample_customer.email
        assert dto.full_name == sample_customer.full_name
        assert dto.lead_status == sample_customer.lead_status
        assert dto.lead_score == sample_customer.lead_score
        assert dto.lifetime_value == float(sample_customer.lifetime_value)
        assert dto.total_orders == sample_customer.total_orders
        assert dto.is_active == sample_customer.is_active


class TestCreateCustomerRequest:
    """Tests for CreateCustomerRequest model."""

    def test_create_request_defaults(self):
        """Test default values in create request."""
        req = CreateCustomerRequest(full_name="Jane Doe")
        assert req.full_name == "Jane Doe"
        assert req.lead_status == "cold"
        assert req.lead_score == 0
        assert req.email is None
        assert req.segment_ids == []
        assert req.tag_ids == []

    def test_create_request_with_values(self):
        """Test create request with all values."""
        req = CreateCustomerRequest(
            email="jane@example.com",
            phone_number="+15559876543",
            full_name="Jane Doe",
            company_name="Beta Inc",
            lead_status="hot",
            lead_score=90,
            segment_ids=[uuid.uuid4()],
            tag_ids=[uuid.uuid4()],
        )
        assert req.email == "jane@example.com"
        assert req.lead_status == "hot"
        assert req.lead_score == 90
        assert len(req.segment_ids) == 1
        assert len(req.tag_ids) == 1


class TestUpdateCustomerRequest:
    """Tests for UpdateCustomerRequest model."""

    def test_update_request_defaults(self):
        """Test default values in update request."""
        req = UpdateCustomerRequest()
        assert req.email is None
        assert req.full_name is None
        assert req.lead_status is None
        assert req.is_active is None
        assert req.segment_ids is None
        assert req.tag_ids is None

    def test_update_request_with_values(self):
        """Test update request with values."""
        req = UpdateCustomerRequest(
            full_name="Updated Name",
            lead_status="qualified",
            lead_score=85,
            is_active=False,
        )
        assert req.full_name == "Updated Name"
        assert req.lead_status == "qualified"
        assert req.lead_score == 85
        assert req.is_active is False


class TestCreateSegmentRequest:
    """Tests for CreateSegmentRequest model."""

    def test_create_segment_defaults(self):
        """Test default values in segment request."""
        req = CreateSegmentRequest(name="VIP Customers")
        assert req.name == "VIP Customers"
        assert req.color == "#6b7280"
        assert req.description is None

    def test_create_segment_with_values(self):
        """Test segment request with values."""
        req = CreateSegmentRequest(
            name="Enterprise",
            description="Enterprise accounts",
            color="#ff0000",
        )
        assert req.name == "Enterprise"
        assert req.description == "Enterprise accounts"
        assert req.color == "#ff0000"


class TestCreateTagRequest:
    """Tests for CreateTagRequest model."""

    def test_create_tag_defaults(self):
        """Test default values in tag request."""
        req = CreateTagRequest(name="Priority")
        assert req.name == "Priority"
        assert req.color == "#6b7280"

    def test_create_tag_with_values(self):
        """Test tag request with values."""
        req = CreateTagRequest(name="Urgent", color="#ff0000")
        assert req.name == "Urgent"
        assert req.color == "#ff0000"


class TestCreateNoteRequest:
    """Tests for CreateNoteRequest model."""

    def test_create_note_defaults(self):
        """Test default values in note request."""
        req = CreateNoteRequest(
            customer_id=uuid.uuid4(),
            content="Follow up next week",
        )
        assert req.is_internal is True

    def test_create_note_with_values(self):
        """Test note request with values."""
        req = CreateNoteRequest(
            customer_id=uuid.uuid4(),
            content="Called customer",
            is_internal=False,
        )
        assert req.is_internal is False
        assert req.content == "Called customer"