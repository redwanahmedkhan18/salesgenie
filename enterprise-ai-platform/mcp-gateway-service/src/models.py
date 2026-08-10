"""
MCP Gateway Service Data Models & Schemas
Models for MCP tool registration, tool execution, and audit logging.
"""

import uuid
from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
import enum


class ToolVisibility(str, enum.Enum):
    """Visibility levels for MCP tools."""
    PUBLIC = "public"
    TENANT = "tenant"
    ROLE = "role"
    PRIVATE = "private"


class ToolCategory(str, enum.Enum):
    """Categories of MCP tools."""
    SEARCH = "search"
    RESEARCH = "research"
    CRM = "crm"
    COMMUNICATION = "communication"
    DATA_ENRICHMENT = "data_enrichment"
    ANALYTICS = "analytics"
    DATABASE = "database"
    FILE = "file"
    WEBHOOK = "webhook"
    CUSTOM = "custom"


class ToolStatus(str, enum.Enum):
    """Status of an MCP tool."""
    ACTIVE = "active"
    DISABLED = "disabled"
    ERROR = "error"


class MCPToolRegistration(BaseModel):
    """Request to register an MCP tool."""
    name: str = Field(..., description="Unique tool name")
    description: str = Field(..., description="Tool description")
    category: str = Field(default=ToolCategory.CUSTOM.value)
    server_url: str = Field(..., description="URL of the MCP server")
    server_name: str = Field(..., description="Name of the MCP server")
    api_key: Optional[str] = Field(None, description="Optional API key for authentication")
    visibility: str = Field(default=ToolVisibility.TENANT.value)
    required_roles: Optional[List[str]] = Field(default_factory=list)
    required_permissions: Optional[List[str]] = Field(default_factory=list)
    config_schema: Optional[Dict[str, Any]] = Field(None, description="JSON schema for tool configuration")
    timeout_seconds: int = Field(default=30, ge=1, le=300)
    enabled: bool = Field(default=True)
    metadata_json: Optional[Dict[str, Any]] = None


class MCPToolDTO(BaseModel):
    """MCP tool data transfer object."""
    id: str
    name: str
    description: str
    category: str
    server_name: str
    server_url: str
    api_key_configured: bool
    risk_level: str = Field(default="medium", description="Risk level: low, medium, high, critical")
    requires_approval: bool = Field(default=False, description="Whether human approval is required before execution")
    visibility: str
    required_roles: Optional[List[str]]
    required_permissions: Optional[List[str]]
    timeout_seconds: int
    enabled: bool
    status: str
    last_used_at: Optional[datetime]
    execution_count: int
    total_errors: int
    avg_latency_ms: float
    tenant_id: str
    created_at: datetime
    updated_at: datetime


class MCPToolCallRequest(BaseModel):
    """Request to execute an MCP tool."""
    tool_id: str
    arguments: Dict[str, Any] = Field(default_factory=dict)
    timeout_seconds: Optional[int] = Field(None, description="Override tool timeout")


class MCPToolCallResult(BaseModel):
    """Result of an MCP tool execution."""
    tool_id: str
    tool_name: str
    success: bool
    result: Optional[Any] = None
    error: Optional[str] = None
    latency_ms: float
    executed_at: datetime
    request_id: str
    evidence_type: Optional[str] = None


class MCPExecutionLogDTO(BaseModel):
    """Audit log for MCP tool execution."""
    id: str
    tool_id: str
    tool_name: str
    category: str
    success: bool
    latency_ms: float
    caller_user_id: str
    caller_roles: List[str]
    arguments_keys: Optional[List[str]]
    error_message: Optional[str]
    request_id: str
    tenant_id: str
    created_at: datetime
    approval_state: Optional[str] = None
    requires_approval: bool = False
    threat_detected: bool = False
    threat_details: Optional[str] = None
    is_blocked: bool = False
    block_reason: Optional[str] = None


class MCPToolStatsDTO(BaseModel):
    """Statistics for an MCP tool."""
    tool_id: str
    tool_name: str
    category: str
    execution_count: int
    success_count: int
    error_count: int
    success_rate: float
    avg_latency_ms: float
    p99_latency_ms: float
    last_used_at: Optional[datetime]
    most_common_error: Optional[str]
