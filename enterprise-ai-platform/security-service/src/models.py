"""
Security Service Data Models & Schemas
AI security, MCP security, threat detection, and tool risk level models.
"""

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
from sqlalchemy import String, Boolean, Text, Integer, Float
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column


class ToolRiskLevel(str, enum.Enum):
    """Risk levels for AI tools and MCP tools."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ThreatType(str, enum.Enum):
    """Types of security threats detectable by the AI Security Gateway."""
    PROMPT_INJECTION = "prompt_injection"
    INDIRECT_PROMPT_INJECTION = "indirect_prompt_injection"
    DATA_EXFILTRATION = "data_exfiltration"
    SYSTEM_PROMPT_LEAKAGE = "system_prompt_leakage"
    JAILBREAK = "jailbreak"
    MALICIOUS_TOOL_USE = "malicious_tool_use"
    CROSS_TENANT_ACCESS = "cross_tenant_access"
    RAG_POISONING = "rag_poisoning"
    EXCESSIVE_AGENT_AGENCY = "excessive_agent_agency"
    SENSITIVE_DATA_DISCLOSURE = "sensitive_data_disclosure"


class SecurityEventType(str, enum.Enum):
    """Types of security events tracked by the Security & Governance service."""
    THREAT_DETECTED = "threat_detected"
    TOOL_EXECUTION = "tool_execution"
    TOOL_BLOCKED = "tool_blocked"
    PROMPT_INJECTION_ATTEMPT = "prompt_injection_attempt"
    MCP_TOOL_CALL = "mcp_tool_call"
    MCP_TOOL_BLOCKED = "mcp_tool_blocked"
    HUMAN_APPROVAL_REQUESTED = "human_approval_requested"
    HUMAN_APPROVAL_GRANTED = "human_approval_granted"
    HUMAN_APPROVAL_DENIED = "human_approval_denied"
    TENANT_VIOLATION = "tenant_violation"
    RAG_ACCESS_VIOLATION = "rag_access_violation"
    RATE_LIMIT_EXCEEDED = "rate_limit_exceeded"
    SESSION_REVOKED = "session_revoked"
    SECURITY_SCORE_UPDATED = "security_score_updated"


class AlertSeverity(str, enum.Enum):
    """Severity levels for security alerts."""
    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class MCPToolConfig(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Configuration for MCP tool authorization and security controls.

    Defines which tools are allowed for which roles, their risk levels,
    and whether they require human approval.
    """
    __tablename__ = "security_mcp_tool_configs"

    tool_name: Mapped[str] = mapped_column(
        String(100), nullable=False, index=True,
        comment="Name of the MCP tool (e.g., 'search_company', 'send_whatsapp')"
    )
    tool_namespace: Mapped[str] = mapped_column(
        String(100), nullable=False, index=True,
        comment="MCP server namespace the tool belongs to"
    )
    risk_level: Mapped[str] = mapped_column(
        String(20), nullable=False, default="medium",
        comment="Risk level: low, medium, high, critical"
    )
    allowed_roles: Mapped[list] = mapped_column(
        JSONB, default=list, nullable=False,
        comment="Roles allowed to execute this tool"
    )
    requires_approval: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False,
        comment="Whether this tool requires human approval before execution"
    )
    allowed_tenants: Mapped[Optional[list]] = mapped_column(
        JSONB, nullable=True,
        comment="List of tenant IDs allowed to use this tool; null = all tenants"
    )
    parameter_schema: Mapped[Optional[dict]] = mapped_column(
        JSONB, nullable=True,
        comment="JSON Schema for parameter validation"
    )
    rate_limit_per_minute: Mapped[int] = mapped_column(
        Integer, default=60, nullable=False,
        comment="Max executions per minute for this tool"
    )
    is_enabled: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False,
        comment="Whether this tool is enabled"
    )


class AIThreatPattern(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Pattern definitions for detecting AI security threats.

    Each pattern is a regex or keyword-based detector for a specific
    threat type (prompt injection, data exfiltration, etc.).
    """
    __tablename__ = "security_ai_threat_patterns"

    threat_type: Mapped[str] = mapped_column(
        String(50), nullable=False, index=True,
        comment="Type of threat this pattern detects"
    )
    pattern_name: Mapped[str] = mapped_column(
        String(100), nullable=False,
        comment="Human-readable name for this pattern"
    )
    pattern_regex: Mapped[str] = mapped_column(
        Text, nullable=False,
        comment="Regex pattern to match against"
    )
    severity: Mapped[str] = mapped_column(
        String(20), nullable=False, default="medium",
        comment="Severity if this pattern matches"
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False,
        comment="Whether this pattern is active"
    )
    description: Mapped[Optional[str]] = mapped_column(
        Text, nullable=True,
        comment="Description of what this pattern detects"
    )


class SecurityIncident(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Records security incidents detected by the AI Security Gateway."""
    __tablename__ = "security_incidents"

    incident_type: Mapped[str] = mapped_column(
        String(50), nullable=False, index=True,
        comment="Type of security incident"
    )
    severity: Mapped[str] = mapped_column(
        String(20), nullable=False, default="medium",
        comment="Severity level"
    )
    title: Mapped[str] = mapped_column(
        String(200), nullable=False,
        comment="Short title for the incident"
    )
    description: Mapped[Text] = mapped_column(
        Text, nullable=False,
        comment="Detailed description of the incident"
    )
    actor_id: Mapped[Optional[str]] = mapped_column(
        String(100), nullable=True, index=True,
        comment="ID of the user/service that triggered the incident"
    )
    resource_type: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True,
        comment="Type of resource involved"
    )
    resource_id: Mapped[Optional[str]] = mapped_column(
        String(100), nullable=True,
        comment="ID of the resource involved"
    )
    metadata_json: Mapped[Optional[dict]] = mapped_column(
        JSONB, nullable=True,
        comment="Additional metadata about the incident"
    )
    is_resolved: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False,
        comment="Whether the incident has been resolved"
    )
    resolved_by: Mapped[Optional[str]] = mapped_column(
        String(100), nullable=True,
        comment="ID of the user who resolved the incident"
    )
    resolved_at: Mapped[Optional[datetime]] = mapped_column(
        nullable=True,
        comment="When the incident was resolved"
    )


class HumanApproval(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Tracks human approval requests for high-risk AI actions."""
    __tablename__ = "security_human_approvals"

    action_type: Mapped[str] = mapped_column(
        String(100), nullable=False,
        comment="Type of action requiring approval"
    )
    tool_name: Mapped[Optional[str]] = mapped_column(
        String(100), nullable=True,
        comment="MCP tool name if applicable"
    )
    actor_id: Mapped[str] = mapped_column(
        String(100), nullable=False, index=True,
        comment="User who requested the action"
    )
    parameters_json: Mapped[Optional[dict]] = mapped_column(
        JSONB, nullable=True,
        comment="Parameters of the action"
    )
    reason: Mapped[Optional[str]] = mapped_column(
        Text, nullable=True,
        comment="Why approval was needed"
    )
    status: Mapped[str] = mapped_column(
        String(20), default="pending", nullable=False,
        comment="Status: pending, approved, denied, expired"
    )
    approver_id: Mapped[Optional[str]] = mapped_column(
        String(100), nullable=True,
        comment="User who approved or denied"
    )
    approved_at: Mapped[Optional[datetime]] = mapped_column(
        nullable=True,
        comment="When the approval was decided"
    )
    expires_at: Mapped[Optional[datetime]] = mapped_column(
        nullable=True,
        comment="When the approval request expires"
    )


class OrgSecurityProfile(Base, UUIDPrimaryKeyMixin, TimestampMixin, TenantIsolationMixin):
    """Security profile for an organization, including security scores and policies."""
    __tablename__ = "security_org_profiles"

    security_score: Mapped[float] = mapped_column(
        Float, default=100.0, nullable=False,
        comment="Overall security score (0-100)"
    )
    last_scanned_at: Mapped[Optional[datetime]] = mapped_column(
        nullable=True,
        comment="Last security scan timestamp"
    )
    mfa_enforced: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False,
        comment="Whether MFA is enforced for this org"
    )
    session_timeout_minutes: Mapped[int] = mapped_column(
        Integer, default=30, nullable=False,
        comment="Session timeout in minutes"
    )
    max_sessions_per_user: Mapped[int] = mapped_column(
        Integer, default=5, nullable=False,
        comment="Maximum concurrent sessions per user"
    )
    data_retention_days: Mapped[int] = mapped_column(
        Integer, default=365, nullable=False,
        comment="Data retention period in days"
    )
    ai_approvals_required: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False,
        comment="Whether human approval is required for AI actions"
    )
    risk_threshold: Mapped[str] = mapped_column(
        String(20), default="high", nullable=False,
        comment="Risk threshold: low, medium, high, critical"
    )


# -------------------------------------------------------------------
# Pydantic Schemas
# -------------------------------------------------------------------

class MCPToolConfigDTO(BaseModel):
    id: str
    tool_name: str
    tool_namespace: str
    risk_level: str
    allowed_roles: List[str]
    requires_approval: bool
    allowed_tenants: Optional[List[str]] = None
    parameter_schema: Optional[Dict[str, Any]] = None
    rate_limit_per_minute: int
    is_enabled: bool
    created_at: datetime
    updated_at: datetime


class MCPToolConfigCreate(BaseModel):
    tool_name: str
    tool_namespace: str
    risk_level: str = "medium"
    allowed_roles: List[str] = Field(default_factory=list)
    requires_approval: bool = False
    allowed_tenants: Optional[List[str]] = None
    parameter_schema: Optional[Dict[str, Any]] = None
    rate_limit_per_minute: int = 60
    is_enabled: bool = True


class AIThreatPatternDTO(BaseModel):
    id: str
    threat_type: str
    pattern_name: str
    severity: str
    is_active: bool
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime


class AIThreatPatternCreate(BaseModel):
    threat_type: str
    pattern_name: str
    pattern_regex: str
    severity: str = "medium"
    is_active: bool = True
    description: Optional[str] = None


class SecurityIncidentDTO(BaseModel):
    id: str
    incident_type: str
    severity: str
    title: str
    description: str
    actor_id: Optional[str] = None
    resource_type: Optional[str] = None
    resource_id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    is_resolved: bool
    resolved_by: Optional[str] = None
    resolved_at: Optional[datetime] = None
    created_at: datetime
    tenant_id: str


class SecurityIncidentCreate(BaseModel):
    incident_type: str
    severity: str = "medium"
    title: str
    description: str
    actor_id: Optional[str] = None
    resource_type: Optional[str] = None
    resource_id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class HumanApprovalDTO(BaseModel):
    id: str
    action_type: str
    tool_name: Optional[str] = None
    actor_id: str
    parameters: Optional[Dict[str, Any]] = None
    reason: Optional[str] = None
    status: str
    approver_id: Optional[str] = None
    approved_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
    created_at: datetime
    tenant_id: str


class HumanApprovalRequest(BaseModel):
    action_type: str
    tool_name: Optional[str] = None
    parameters: Optional[Dict[str, Any]] = None
    reason: Optional[str] = None


class HumanApprovalDecision(BaseModel):
    approved: bool
    approver_id: str


class OrgSecurityProfileDTO(BaseModel):
    tenant_id: str
    security_score: float
    last_scanned_at: Optional[datetime] = None
    mfa_enforced: bool
    session_timeout_minutes: int
    max_sessions_per_user: int
    data_retention_days: int
    ai_approvals_required: bool
    risk_threshold: str


class ThreatDetectionResult(BaseModel):
    threats: List[Dict[str, Any]] = Field(default_factory=list)
    is_blocked: bool
    reason: Optional[str] = None


class ToolAuthorizationResult(BaseModel):
    allowed: bool
    requires_approval: bool
    risk_level: str
    reason: Optional[str] = None
