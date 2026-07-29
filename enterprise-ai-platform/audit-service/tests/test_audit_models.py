"""
Unit Tests for Audit Service Models
"""

import pytest
import uuid
from datetime import datetime
from unittest.mock import MagicMock

from audit_service.src.models import (
    AuditLog,
    AuditLogDTO,
    AuditLogCreateRequest,
    AuditLogResponse,
    AuditSearchRequest,
    AuditSearchResponse,
    AuditStatsDTO,
    AuditOverviewDTO,
    AuditEventType,
    AuditSeverity,
)


class TestAuditEventType:
    def test_event_type_values(self):
        assert AuditEventType.USER_LOGIN == "user_login"
        assert AuditEventType.USER_LOGOUT == "user_logout"
        assert AuditEventType.USER_CREATED == "user_created"
        assert AuditEventType.CUSTOMER_CREATED == "customer_created"
        assert AuditEventType.TICKET_CREATED == "ticket_created"
        assert AuditEventType.DOCUMENT_INDEXED == "document_indexed"
        assert AuditEventType.API_CALL == "api_call"
        assert AuditEventType.SYSTEM_EVENT == "system_event"
        assert AuditEventType.DATA_EXPORT == "data_export"
        assert AuditEventType.PERMISSION_GRANTED == "permission_granted"
        assert AuditEventType.CONFIG_CHANGED == "config_changed"
        assert AuditEventType.SECURITY_ALERT == "security_alert"
        assert AuditEventType.COMPLIANCE_VIOLATION == "compliance_violation"


class TestAuditSeverity:
    def test_severity_values(self):
        assert AuditSeverity.INFO == "info"
        assert AuditSeverity.WARNING == "warning"
        assert AuditSeverity.ERROR == "error"
        assert AuditSeverity.CRITICAL == "critical"


class TestAuditLogCreateRequest:
    def test_defaults(self):
        req = AuditLogCreateRequest(
            event_type="user_login",
            action="login",
            description="User logged in successfully",
        )
        assert req.event_type == "user_login"
        assert req.severity == "info"
        assert req.actor_type == "user"
        assert req.is_compliance is False
        assert req.retention_days == 365
        assert req.resource_type is None
        assert req.metadata is None

    def test_with_values(self):
        req = AuditLogCreateRequest(
            event_type="customer_updated",
            severity="warning",
            actor_id="user_123",
            actor_type="user",
            resource_type="customer",
            resource_id="cust_456",
            action="update",
            description="Customer profile updated",
            ip_address="192.168.1.1",
            user_agent="Mozilla/5.0",
            request_id="req_abc123",
            metadata={"field": "email", "old": "old@test.com", "new": "new@test.com"},
            is_compliance=True,
            retention_days=730,
        )
        assert req.severity == "warning"
        assert req.actor_id == "user_123"
        assert req.is_compliance is True
        assert req.retention_days == 730
        assert req.metadata == {"field": "email", "old": "old@test.com", "new": "new@test.com"}


class TestAuditSearchRequest:
    def test_defaults(self):
        req = AuditSearchRequest(query="login")
        assert req.query == "login"
        assert req.size == 50
        assert req.from_ == 0
        assert req.sort_by == "created_at"
        assert req.sort_order == "desc"

    def test_with_filters(self):
        req = AuditSearchRequest(
            query="customer",
            event_types=["customer_created", "customer_updated"],
            severities=["info", "warning"],
            actor_ids=["user_1", "user_2"],
            resource_types=["customer"],
            actions=["create", "update"],
            is_compliance=True,
            size=100,
            from_=10,
            sort_by="created_at",
            sort_order="asc",
        )
        assert req.event_types == ["customer_created", "customer_updated"]
        assert req.severities == ["info", "warning"]
        assert req.is_compliance is True
        assert req.size == 100
        assert req.from_ == 10
        assert req.sort_order == "asc"


class TestAuditLogDTO:
    def test_dto(self):
        now = datetime.now()
        dto = AuditLogDTO(
            id="audit_123",
            event_type="user_login",
            severity="info",
            actor_id="user_456",
            actor_type="user",
            resource_type=None,
            resource_id=None,
            action="login",
            description="User logged in",
            ip_address="192.168.1.1",
            user_agent="Mozilla/5.0",
            request_id="req_abc",
            metadata={"session": "sess_1"},
            is_compliance=False,
            retention_days=365,
            tenant_id="tenant_1",
            created_at=now,
        )
        assert dto.id == "audit_123"
        assert dto.event_type == "user_login"
        assert dto.severity == "info"
        assert dto.is_compliance is False


class TestAuditLogResponse:
    def test_response(self):
        resp = AuditLogResponse(id="audit_123", status="created")
        assert resp.id == "audit_123"
        assert resp.status == "created"


class TestAuditSearchResponse:
    def test_response(self):
        hit = AuditLogDTO(
            id="audit_1",
            event_type="user_login",
            severity="info",
            actor_type="user",
            action="login",
            description="Login",
            is_compliance=False,
            retention_days=365,
            tenant_id="tenant_1",
            created_at=datetime.now(),
        )
        resp = AuditSearchResponse(
            total_hits=1,
            hits=[hit],
            took_ms=15,
        )
        assert resp.total_hits == 1
        assert len(resp.hits) == 1
        assert resp.took_ms == 15


class TestAuditStatsDTO:
    def test_stats_dto(self):
        dto = AuditStatsDTO(
            event_type="user_login",
            count=150,
            percentage=25.5,
        )
        assert dto.event_type == "user_login"
        assert dto.count == 150
        assert dto.percentage == 25.5


class TestAuditOverviewDTO:
    def test_overview_dto(self):
        dto = AuditOverviewDTO(
            total_events=1000,
            events_today=50,
            events_by_severity={"info": 800, "warning": 150, "error": 50},
            events_by_type={"user_login": 200, "customer_created": 100},
            top_actors=[{"actor_id": "user_1", "count": 50}],
            compliance_events=10,
            security_alerts=5,
            retention_summary={"365": 990, "730": 10},
        )
        assert dto.total_events == 1000
        assert dto.events_today == 50
        assert dto.compliance_events == 10
        assert dto.security_alerts == 5