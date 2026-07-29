"""
Unit Tests for Support Service Models
"""

import pytest
import uuid
from unittest.mock import MagicMock

from support_service.src.models import (
    Ticket,
    TicketNote,
    TicketAssignment,
    LiveHandoff,
    CreateTicketRequest,
    UpdateTicketRequest,
    AssignTicketRequest,
    CreateNoteRequest,
    CreateHandoffRequest,
    TicketStatus,
    TicketPriority,
    TicketCategory,
    TicketSource,
)


class TestTicketStatus:
    def test_ticket_status_values(self):
        assert TicketStatus.OPEN == "open"
        assert TicketStatus.IN_PROGRESS == "in_progress"
        assert TicketStatus.RESOLVED == "resolved"
        assert TicketStatus.CLOSED == "closed"


class TestTicketPriority:
    def test_ticket_priority_values(self):
        assert TicketPriority.LOW == "low"
        assert TicketPriority.MEDIUM == "medium"
        assert TicketPriority.HIGH == "high"
        assert TicketPriority.CRITICAL == "critical"


class TestTicketCategory:
    def test_ticket_category_values(self):
        assert TicketCategory.BILLING == "billing"
        assert TicketCategory.TECHNICAL == "technical"
        assert TicketCategory.SALES == "sales"


class TestCreateTicketRequest:
    def test_create_request_defaults(self):
        req = CreateTicketRequest(
            customer_id=uuid.uuid4(),
            title="Test Ticket",
            description="Test description",
        )
        assert req.priority == "medium"
        assert req.category == "general"
        assert req.source == "web"
        assert req.conversation_id is None

    def test_create_request_with_values(self):
        req = CreateTicketRequest(
            customer_id=uuid.uuid4(),
            conversation_id=uuid.uuid4(),
            title="Billing Issue",
            description="I have a question about my bill",
            priority="high",
            category="billing",
            source="chat",
        )
        assert req.priority == "high"
        assert req.category == "billing"
        assert req.source == "chat"


class TestUpdateTicketRequest:
    def test_update_request_defaults(self):
        req = UpdateTicketRequest()
        assert req.title is None
        assert req.status is None
        assert req.priority is None
        assert req.assigned_to is None

    def test_update_request_with_values(self):
        req = UpdateTicketRequest(
            title="Updated Title",
            status="resolved",
            priority="low",
            resolution_notes="Fixed the issue",
            satisfaction_score=5,
        )
        assert req.title == "Updated Title"
        assert req.status == "resolved"
        assert req.priority == "low"
        assert req.satisfaction_score == 5


class TestAssignTicketRequest:
    def test_assign_request(self):
        req = AssignTicketRequest(
            agent_id=uuid.uuid4(),
            assigned_by=uuid.uuid4(),
        )
        assert req.agent_id is not None
        assert req.assigned_by is not None


class TestCreateNoteRequest:
    def test_create_note_defaults(self):
        req = CreateNoteRequest(
            ticket_id=uuid.uuid4(),
            content="Note content",
        )
        assert req.is_internal is True

    def test_create_note_with_values(self):
        req = CreateNoteRequest(
            ticket_id=uuid.uuid4(),
            content="External note",
            is_internal=False,
        )
        assert req.is_internal is False


class TestCreateHandoffRequest:
    def test_create_handoff_defaults(self):
        req = CreateHandoffRequest(
            conversation_id=uuid.uuid4(),
            customer_id=uuid.uuid4(),
        )
        assert req.requested_by == "ai_agent"
        assert "human agent" in req.reason.lower()

    def test_create_handoff_with_values(self):
        req = CreateHandoffRequest(
            conversation_id=uuid.uuid4(),
            customer_id=uuid.uuid4(),
            requested_by="customer",
            reason="Need immediate assistance",
        )
        assert req.requested_by == "customer"
        assert req.reason == "Need immediate assistance"