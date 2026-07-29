"""
Audit Service Data Models & Schemas
Audit log models and audit event DTOs.
"""

import uuid
from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
import enum

from enterprise_ai_platform.common.models_base import (
    Base,
    UUIDPrimaryKeyMixin,
    TimestampMixin,
    TenantIsolationMixin,
)
from sqlalchemy import Column, String, Boolean, Text, Integer, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column


class AuditEventType(str, enum.Enum):
    """Types of audit events."""
    USER_LOGIN = "user_login"
    USER_LOGOUT = "user_logout"
    USER_CREATED = "user_created"
    USER_UPDATED = "user_updated"
    USER_DELETED = "user_deleted"
    CUSTOMER_CREATED = "customer_created"
    CUSTOMER_UPDATED = "customer_updated"
    CUSTOMER_DELETED = "customer_deleted"
    TICKET_CREATED = "ticket_created"
    TICKET_UPDATED = "ticket_updated"
    TICKET_ASSIGNED = "ticket_assigned"
    TICKET_RESOLVED = "ticket_resolved"
    DOCUMENT_INDEXED = "document_indexed"
    DOCUMENT_DELETED = "document_deleted"
    API_CALL = "api_call"
    SYSTEM_EVENT = "system_event"
    DATA_EXPORT = "data_export"
    PERMISSION_GRANTED = "permission_granted"
    PERMISSION_REVOKED = "permission_revoked"
    CONFIG_CHANGED = "config_changed"
    SECURITY_ALERT = "security_alert"
    COMPLIANCE_VIOLATION = "compliance_violation"


class AuditSeverity(str, enum.Enum):
    """Severity levels for audit events."""
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


class AuditLog(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Audit log entry for tracking user actions and system events."""
    __tablename__ = "audit_logs"

    event_type: Mapped[str] = mapped_column(
        String(50), nullable=False, index=True,
        comment="Type of audit event"
    )
    severity: Mapped[str] = mapped_column(
        String(20), nullable=False, default="info",
        comment="Severity level of the event"
    )
    actor_id: Mapped[Optional[str]] = mapped_column(
        String(100), nullable=True, index=True,
        comment="ID of the user/service performing the action"
    )
    actor_type: Mapped[str] = mapped_column(
        String(20), nullable=False, default="user",
        comment="Type of actor: user, system, service"
    )
    resource_type: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, index=True,
        comment="Type of resource being acted upon"
    )
    resource_id: Mapped[Optional[str]] = mapped_column(
        String(100), nullable=True, index=True,
        comment="ID of the resource being acted upon"
    )
    action: Mapped[str] = mapped_column(
        String(50), nullable=False,
        comment="Action performed (create, read, update, delete, etc.)"
    )
    description: Mapped[str] = mapped_column(
        Text, nullable=False,
        comment="Human-readable description of the event"
    )
    ip_address: Mapped[Optional[str]] = mapped_column(
        String(45), nullable=True,
        comment="IP address of the actor"
    )
    user_agent: Mapped[Optional[str]] = mapped_column(
        Text, nullable=True,
        comment="User agent string from the request"
    )
    request_id: Mapped[Optional[str]] = mapped_column(
        String(100), nullable=True, index=True,
        comment="Correlation ID for request tracing"
    )
    metadata_json: Mapped[Optional[dict]] = mapped_column(
        JSONB, nullable=True,
        comment="Additional metadata about the event"
    )
    is_compliance: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False,
        comment="Whether this event is a compliance-relevant event"
    )
    retention_days: Mapped[int] = mapped_column(
        Integer, default=365, nullable=False,
        comment="Number of days to retain this log entry"
    )


# -------------------------------------------------------------------
# Pydantic Schemas / DTOs
# -------------------------------------------------------------------

class AuditLogDTO(BaseModel):
    id: str
    event_type: str
    severity: str
    actor_id: Optional[str] = None
    actor_type: str
    resource_type: Optional[str] = None
    resource_id: Optional[str] = None
    action: str
    description: str
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    request_id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    is_compliance: bool
    retention_days: int
    tenant_id: str
    created_at: datetime


class AuditLogCreateRequest(BaseModel):
    event_type: str
    severity: str = "info"
    actor_id: Optional[str] = None
    actor_type: str = "user"
    resource_type: Optional[str] = None
    resource_id: Optional[str] = None
    action: str
    description: str
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    request_id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    is_compliance: bool = False
    retention_days: int = 365


class AuditLogResponse(BaseModel):
    id: str
    status: str


class AuditSearchRequest(BaseModel):
    query: Optional[str] = None
    event_types: Optional[List[str]] = None
    severities: Optional[List[str]] = None
    actor_ids: Optional[List[str]] = None
    resource_types: Optional[List[str]] = None
    resource_ids: Optional[List[str]] = None
    actions: Optional[List[str]] = None
    is_compliance: Optional[bool] = None
    date_from: Optional[datetime] = None
    date_to: Optional[datetime] = None
    size: int = 50
    from_: int = 0
    sort_by: str = "created_at"
    sort_order: str = "desc"


class AuditSearchResponse(BaseModel):
    total_hits: int
    hits: List[AuditLogDTO]
    took_ms: int


class AuditStatsDTO(BaseModel):
    event_type: str
    count: int
    percentage: float


class AuditOverviewDTO(BaseModel):
    total_events: int
    events_today: int
    events_by_severity: Dict[str, int]
    events_by_type: Dict[str, int]
    top_actors: List[Dict[str, Any]]
    compliance_events: int
    security_alerts: int
    retention_summary: Dict[str, int]