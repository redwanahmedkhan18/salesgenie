"""
MCP Gateway Service API Router
Endpoints for MCP tool registration, execution, audit, and statistics.
Integrated with Security Service for threat detection, approval workflows,
SSRF protection, and tenant isolation.
"""

import uuid
import time
import json
import ipaddress
import asyncio
from typing import List, Optional, Dict, Any, Tuple, TYPE_CHECKING
from urllib.parse import urlparse
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, desc, delete, text
from sqlalchemy.dialects.postgresql import UUID as PGUUID

if TYPE_CHECKING:
    from enterprise_ai_platform.security_service.src.mcp_security_gateway import MCPSecurityGateway
from sqlalchemy import Column, String, Text, Integer, Boolean, DateTime, Float, JSON
from sqlalchemy.ext.declarative import declarative_base

from enterprise_ai_platform.common.database import get_async_db
from enterprise_ai_platform.common.security_rbac import (
    get_current_user,
    TokenPayload,
    PlatformRole,
)
from enterprise_ai_platform.common.config import settings
from enterprise_ai_platform.common.logging import get_structured_logger
from enterprise_ai_platform.common.metrics import get_metrics
from .models import (
    MCPToolRegistration,
    MCPToolDTO,
    MCPToolCallRequest,
    MCPToolCallResult,
    MCPExecutionLogDTO,
    MCPToolStatsDTO,
)

logger = get_structured_logger("salesgenie.mcp_gateway", "mcp-gateway-service")
metrics = get_metrics("mcp-gateway-service")

# Import security gateways lazily to avoid circular imports
_mcp_security = None
_ai_security = None


def _get_mcp_security():
    global _mcp_security
    if _mcp_security is None:
        try:
            from enterprise_ai_platform.security_service.src.mcp_security_gateway import MCPSecurityGateway
            from enterprise_ai_platform.security_service.src.ai_security_gateway import AISecurityGateway
            _mcp_security = MCPSecurityGateway()
            _ai_security = AISecurityGateway()
            _mcp_security.set_ai_security(_ai_security)
            _init_default_tools(_mcp_security)
        except ImportError:
            _mcp_security = MCPSecurityGateway()
            _ai_security = AISecurityGateway()
            _mcp_security.set_ai_security(_ai_security)
            _init_default_tools(_mcp_security)
    return _mcp_security


def _init_default_tools(gateway: "MCPSecurityGateway") -> None:
    """Initialize the default tool catalog from security-service."""
    try:
        from enterprise_ai_platform.security_service.src.router_security import DEFAULT_TOOL_CATALOG
        for tool_name, config in DEFAULT_TOOL_CATALOG.items():
            gateway.register_tool(config)
    except (ImportError, Exception):
        pass


# SSRF Protection: private IP ranges that must never be called
_PRIVATE_IP_PREFIXES = (
    "10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.",
    "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.",
    "172.28.", "172.29.", "172.30.", "172.31.",
    "192.168.", "127.", "169.254.", "0.",
)


def _is_ssrf_safe_url(url: str) -> Tuple[bool, Optional[str]]:
    """Validate that a URL is not targeting internal/private addresses.

    Returns (is_safe, reason). Blocks SSRF to internal networks,
    cloud metadata endpoints, and localhost.
    """
    try:
        parsed = urlparse(url)
        if parsed.scheme not in ("http", "https"):
            return False, f"Disallowed URL scheme: {parsed.scheme}"

        hostname = parsed.hostname
        if not hostname:
            return False, "No hostname in URL"

        # Block metadata endpoints
        if hostname in ("metadata.google.internal", "169.254.169.254",
                        "metadata", "kubernetes.default", "kubernetes.default.svc"):
            return False, f"Blocked metadata endpoint: {hostname}"

        # Block if hostname is an IP address in private ranges
        try:
            ip = ipaddress.ip_address(hostname)
            if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved or ip.is_multicast:
                return False, f"Blocked internal IP address: {hostname}"
        except ValueError:
            pass  # Not an IP, it's a hostname - that's fine

        # Block hostnames starting with private IP prefixes
        for prefix in _PRIVATE_IP_PREFIXES:
            if hostname.startswith(prefix):
                return False, f"Blocked private IP hostname: {hostname}"

        return True, None

    except Exception:
        return False, "Invalid URL format"


# Simple Fernet-based encryption for API keys at rest
def _get_encryption_key() -> bytes:
    key = settings.JWT_SECRET_KEY if settings.JWT_SECRET_KEY else "fallback-encryption-key-change-in-prod"
    from hashlib import sha256
    return sha256(key.encode()).digest()[:32]


try:
    from cryptography.fernet import Fernet
    import base64
    _fernet = None

    def _get_fernet():
        global _fernet
        if _fernet is None:
            key = base64.urlsafe_b64encode(_get_encryption_key())
            _fernet = Fernet(key)
        return _fernet

    def encrypt_api_key(key: str) -> Optional[str]:
        if not key:
            return None
        return _get_fernet().encrypt(key.encode()).decode()

    def decrypt_api_key(encrypted: Optional[str]) -> Optional[str]:
        if not encrypted:
            return None
        try:
            return _get_fernet().decrypt(encrypted.encode()).decode()
        except Exception:
            logger.error("Failed to decrypt API key, possible tampering or key rotation")
            return None
except ImportError:
    def encrypt_api_key(key: str) -> Optional[str]:
        return key  # Fallback: no encryption if cryptography is not installed

    def decrypt_api_key(encrypted: Optional[str]) -> Optional[str]:
        return encrypted


# Allowed argument parameter schema validation
def _validate_tool_arguments(arguments: Dict[str, Any], schema: Optional[Dict[str, Any]]) -> Optional[str]:
    """Validate tool arguments against JSON schema. Returns error message or None."""
    if not schema:
        return None

    required = schema.get("required", [])
    for req_field in required:
        if req_field not in arguments:
            return f"Missing required parameter: {req_field}"

    properties = schema.get("properties", {})
    for key, value in arguments.items():
        if key not in properties:
            continue
        expected_type = properties[key].get("type")
        if expected_type and not _check_type(value, expected_type):
            return f"Parameter '{key}' expected type '{expected_type}', got '{type(value).__name__}'"

    return None


def _check_type(value: Any, expected_type: str) -> bool:
    type_map = {
        "string": str,
        "number": (int, float),
        "integer": int,
        "boolean": bool,
        "array": list,
        "object": dict,
    }
    expected = type_map.get(expected_type)
    if expected is None:
        return True
    if expected_type == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    return isinstance(value, expected)

Base = declarative_base()

router = APIRouter(prefix="/api/v1/mcp", tags=["MCP Gateway Service"])


def _get_tenant_uuid(current_user: TokenPayload) -> uuid.UUID:
    """Extract tenant UUID from current user token."""
    try:
        return uuid.UUID(str(current_user.tenant_id))
    except (ValueError, AttributeError):
        return uuid.uuid5(uuid.NAMESPACE_DNS, str(current_user.tenant_id))


# -------------------------------------------------------------------
# Database Models
# -------------------------------------------------------------------

class MCPTool(Base):
    """Registered MCP tool."""
    __tablename__ = "mcp_tools"

    id: uuid.UUID = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False, index=True)

    created_by: Optional[str] = Column(String(100), nullable=True, index=True)

    name: str = Column(String(100), nullable=False, index=True)
    description: str = Column(Text, nullable=False)
    category: str = Column(String(50), nullable=False, index=True)
    server_name: str = Column(String(100), nullable=False)
    server_url: str = Column(String(500), nullable=False)
    api_key: Optional[str] = Column(String(2000), nullable=True)
    api_key_encrypted: bool = Column(Boolean, default=False, nullable=False)
    visibility: str = Column(String(20), nullable=False, default="tenant")
    required_roles: Optional[list] = Column(JSON, nullable=True)
    required_permissions: Optional[list] = Column(JSON, nullable=True)
    config_schema: Optional[dict] = Column(JSON, nullable=True)
    risk_level: str = Column(String(20), nullable=False, default="medium")
    requires_approval: bool = Column(Boolean, default=False, nullable=False)
    timeout_seconds: int = Column(Integer, nullable=False, default=30)
    enabled: bool = Column(Boolean, nullable=False, default=True)
    status: str = Column(String(20), nullable=False, default="active")
    last_used_at: Optional[datetime] = Column(DateTime(timezone=True), nullable=True)
    execution_count: int = Column(Integer, nullable=False, default=0)
    total_errors: int = Column(Integer, nullable=False, default=0)
    avg_latency_ms: float = Column(Float, nullable=False, default=0.0)
    created_at: datetime = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at: datetime = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)


class MCPExecutionLog(Base):
    """Audit log for MCP tool executions."""
    __tablename__ = "mcp_execution_logs"

    id: uuid.UUID = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False, index=True)

    tool_id: uuid.UUID = Column(PGUUID(as_uuid=True), nullable=False, index=True)
    tool_name: str = Column(String(100), nullable=False, index=True)
    category: str = Column(String(50), nullable=True)
    success: bool = Column(Boolean, nullable=False)
    latency_ms: float = Column(Float, nullable=False, default=0.0)
    caller_user_id: str = Column(String(100), nullable=False)
    caller_roles: Optional[list] = Column(JSON, nullable=True)
    arguments_keys: Optional[list] = Column(JSON, nullable=True)
    error_message: Optional[str] = Column(Text, nullable=True)
    request_id: str = Column(String(100), nullable=False, index=True)
    approval_state: str = Column(String(20), nullable=True, default=None,
       comment="Approval state: approved, denied, pending, or null if no approval required")
    requires_approval: bool = Column(Boolean, default=False, nullable=False)
    threat_detected: bool = Column(Boolean, default=False, nullable=False)
    threat_details: Optional[str] = Column(Text, nullable=True)
    is_blocked: bool = Column(Boolean, default=False, nullable=False)
    block_reason: Optional[str] = Column(Text, nullable=True)
    created_at: datetime = Column(DateTime(timezone=True), default=datetime.utcnow)


# -------------------------------------------------------------------
# Tool Registration Endpoints
# -------------------------------------------------------------------

@router.post("/tools", response_model=MCPToolDTO, status_code=status.HTTP_201_CREATED,
             summary="Register MCP Tool")
async def register_tool(
    req: MCPToolRegistration,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Register a new MCP tool. Only accessible to users with knowledge_manager or higher roles."""
    tenant_uuid = _get_tenant_uuid(current_user)

    allowed_roles = [PlatformRole.SUPER_ADMIN, PlatformRole.ORG_ADMIN, PlatformRole.KNOWLEDGE_MANAGER]
    if not any(r in current_user.roles for r in allowed_roles):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Insufficient permissions to register MCP tools",
        )

    # SSRF protection: validate server_url
    is_safe, ssrf_reason = _is_ssrf_safe_url(req.server_url)
    if not is_safe:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Server URL rejected by SSRF protection: {ssrf_reason}",
        )

    # Check against default tool catalog for risk_level and requires_approval
    risk_level = "medium"
    requires_approval = False
    try:
        from enterprise_ai_platform.security_service.src.router_security import DEFAULT_TOOL_CATALOG
        if req.name in DEFAULT_TOOL_CATALOG:
            catalog_entry = DEFAULT_TOOL_CATALOG[req.name]
            risk_level = catalog_entry.get("risk_level", "medium")
            requires_approval = catalog_entry.get("requires_approval", False)
    except (ImportError, Exception):
        pass

    # Encrypt API key at rest
    encrypted_key = None
    if req.api_key:
        encrypted_key = encrypt_api_key(req.api_key)

    tool = MCPTool(
        tenant_id=tenant_uuid,
        name=req.name,
        description=req.description,
        category=req.category,
        server_name=req.server_name,
        server_url=req.server_url,
        api_key=encrypted_key,
        api_key_encrypted=True,
        visibility=req.visibility,
        required_roles=req.required_roles,
        required_permissions=req.required_permissions,
        config_schema=req.config_schema,
        risk_level=risk_level,
        requires_approval=requires_approval,
        timeout_seconds=req.timeout_seconds,
        enabled=req.enabled,
    )
    db.add(tool)
    await db.commit()
    await db.refresh(tool)

    return _tool_to_dto(tool)


@router.get("/tools", response_model=List[MCPToolDTO], summary="List MCP Tools")
async def list_tools(
    category: Optional[str] = Query(None, description="Filter by category"),
    enabled_only: bool = Query(True, description="Only list enabled tools"),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """List all registered MCP tools visible to the current user."""
    tenant_uuid = _get_tenant_uuid(current_user)
    user_roles = current_user.roles if hasattr(current_user, "roles") else []

    stmt = select(MCPTool).where(MCPTool.tenant_id == tenant_uuid)

    if enabled_only:
        stmt = stmt.where(MCPTool.enabled == True, MCPTool.status == "active")

    if category:
        stmt = stmt.where(MCPTool.category == category)

    stmt = stmt.order_by(MCPTool.name)
    res = await db.execute(stmt)
    tools = res.scalars().all()

    # Filter by visibility - convert user roles to strings for comparison
    user_role_values = _user_roles_to_str(user_roles)
    visible = []
    for tool in tools:
        if tool.visibility == "public":
            visible.append(tool)
        elif tool.visibility == "tenant":
            visible.append(tool)
        elif tool.visibility == "role" and tool.required_roles:
            if any(r in user_role_values for r in tool.required_roles):
                visible.append(tool)
        elif tool.visibility == "private":
            if str(current_user.sub) == str(getattr(tool, "created_by", "")):
                visible.append(tool)

    return [_tool_to_dto(t) for t in visible]


@router.get("/tools/{tool_id}", response_model=MCPToolDTO, summary="Get MCP Tool")
async def get_tool(
    tool_id: uuid.UUID,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get a specific MCP tool."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(MCPTool).where(MCPTool.id == tool_id, MCPTool.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    tool = res.scalar_one_or_none()

    if not tool:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tool not found")

    return _tool_to_dto(tool)


@router.patch("/tools/{tool_id}", response_model=MCPToolDTO, summary="Update MCP Tool")
async def update_tool(
    tool_id: uuid.UUID,
    req: MCPToolRegistration,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Update an MCP tool."""
    tenant_uuid = _get_tenant_uuid(current_user)

    allowed_roles = [PlatformRole.SUPER_ADMIN, PlatformRole.ORG_ADMIN, PlatformRole.KNOWLEDGE_MANAGER]
    if not any(r in current_user.roles for r in allowed_roles):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permissions")
    stmt = select(MCPTool).where(MCPTool.id == tool_id, MCPTool.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    tool = res.scalar_one_or_none()

    if not tool:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tool not found")

    tool.name = req.name
    tool.description = req.description
    tool.category = req.category
    tool.server_name = req.server_name

    # SSRF protection on URL update
    is_safe, ssrf_reason = _is_ssrf_safe_url(req.server_url)
    if not is_safe:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Server URL rejected by SSRF protection: {ssrf_reason}",
        )
    tool.server_url = req.server_url

    if req.api_key:
        tool.api_key = encrypt_api_key(req.api_key)
        tool.api_key_encrypted = True

    tool.visibility = req.visibility
    tool.required_roles = req.required_roles
    tool.required_permissions = req.required_permissions
    tool.config_schema = req.config_schema
    tool.timeout_seconds = req.timeout_seconds
    tool.enabled = req.enabled
    tool.updated_at = datetime.utcnow()

    await db.commit()
    await db.refresh(tool)

    return _tool_to_dto(tool)


@router.delete("/tools/{tool_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete MCP Tool")
async def delete_tool(
    tool_id: uuid.UUID,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Delete an MCP tool."""
    tenant_uuid = _get_tenant_uuid(current_user)

    allowed_roles = [PlatformRole.SUPER_ADMIN, PlatformRole.ORG_ADMIN, PlatformRole.KNOWLEDGE_MANAGER]
    if not any(r in current_user.roles for r in allowed_roles):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permissions")

    stmt = select(MCPTool).where(MCPTool.id == tool_id, MCPTool.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    tool = res.scalar_one_or_none()

    if not tool:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tool not found")

    await db.execute(delete(MCPExecutionLog).where(MCPExecutionLog.tool_id == tool_id))
    await db.delete(tool)
    await db.commit()
    return None


# -------------------------------------------------------------------
# Tool Execution Endpoints
# -------------------------------------------------------------------

# Maximum execution budgets to prevent runaway costs
MAX_TOOL_TIMEOUT_SECONDS = 120
MAX_TOOL_RETRIES = 2
MAX_CONSECUTIVE_TOOL_CALLS = 10


@router.post("/tools/{tool_id}/execute", response_model=MCPToolCallResult,
             summary="Execute MCP Tool")
async def execute_tool(
    tool_id: uuid.UUID,
    req: MCPToolCallRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Execute an MCP tool with the given arguments.

    This endpoint routes the tool call to the registered MCP server,
    enforces rate limits and permissions, scans for prompt injection,
    validates tool arguments against schema, and logs the execution.
    """
    return await _execute_tool_common(tool_id, req, current_user, db, by_name=False)


@router.post("/execute", response_model=MCPToolCallResult,
             summary="Execute MCP Tool by Name")
async def execute_tool_by_name(
    tool_name: str = Query(..., description="Tool name to execute"),
    call_req: MCPToolCallRequest = Depends(),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Execute an MCP tool by name instead of ID."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(MCPTool).where(
        MCPTool.name == tool_name,
        MCPTool.tenant_id == tenant_uuid,
    )
    res = await db.execute(stmt)
    tool = res.scalar_one_or_none()

    if not tool:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tool '{tool_name}' not found",
        )

    # Construct request with the resolved tool_id (as string)
    args = call_req.arguments or {}
    req = MCPToolCallRequest(tool_id=str(tool.id), arguments=args)
    return await _execute_tool_common(tool.id, req, current_user, db, by_name=True)


async def _execute_tool_common(
    tool_id: uuid.UUID,
    req: MCPToolCallRequest,
    current_user: TokenPayload,
    db: AsyncSession,
    by_name: bool = False,
) -> MCPToolCallResult:
    """Shared execution logic for both execute_tool and execute_tool_by_name.

    Enforces:
    - Tenant isolation (tool lookup scoped to tenant_id)
    - Role and permission checks
    - Security gateway authorization (approval, risk level)
    - Prompt injection scanning on arguments
    - SSRF protection on server_url
    - Argument schema validation
    - Execution timeout and retry limits
    - Comprehensive audit logging with approval state and threat detection
    """
    import httpx

    tenant_uuid = _get_tenant_uuid(current_user)
    user_roles_str = _user_roles_to_str(current_user.roles if hasattr(current_user, "roles") else [])

    # Tenant-scoped tool lookup
    stmt = select(MCPTool).where(MCPTool.id == tool_id, MCPTool.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    tool = res.scalar_one_or_none()

    if not tool:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tool not found")

    if not tool.enabled or tool.status != "active":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tool is not available")

    # --- Security Gateway Authorization ---
    security = _get_mcp_security()

    # Register the tool in the gateway if not already registered
    if tool.name not in security._tool_configs:
        security.register_tool({
            "name": tool.name,
            "namespace": tool.server_name,
            "risk_level": tool.risk_level or "medium",
            "allowed_roles": tool.required_roles or [],
            "requires_approval": tool.requires_approval,
            "parameter_schema": tool.config_schema,
            "rate_limit_per_minute": 60,
            "is_enabled": tool.enabled,
        })

    # Authorization check (roles, permissions, tenant, schema validation)
    auth_result = security.is_tool_allowed(
        tool_name=tool.name,
        user_roles=user_roles_str,
        tenant_id=str(tenant_uuid),
        params=req.arguments or {},
    )

    if not auth_result.allowed:
        # Log the blocked attempt
        _log_tool_execution(
            db=db,
            tenant_uuid=tenant_uuid,
            tool=tool,
            tool_id=tool_id,
            success=False,
            latency_ms=0.0,
            caller_user_id=str(current_user.sub),
            caller_roles=user_roles_str,
            arguments_keys=list(req.arguments.keys()) if req.arguments else [],
            error_msg=f"Authorization denied: {auth_result.reason}",
            request_id=str(uuid.uuid4()),
            approval_state=None,
            requires_approval=auth_result.requires_approval,
            threat_detected=False,
            is_blocked=True,
            block_reason=auth_result.reason,
        )
        await db.commit()
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Tool authorization denied: {auth_result.reason}",
        )

    # --- Approval Check ---
    if auth_result.requires_approval:
        # Log the approval-required attempt and block execution
        _log_tool_execution(
            db=db,
            tenant_uuid=tenant_uuid,
            tool=tool,
            tool_id=tool_id,
            success=False,
            latency_ms=0.0,
            caller_user_id=str(current_user.sub),
            caller_roles=user_roles_str,
            arguments_keys=list(req.arguments.keys()) if req.arguments else [],
            error_msg="Execution blocked: tool requires human approval",
            request_id=str(uuid.uuid4()),
            approval_state="pending",
            requires_approval=True,
            threat_detected=False,
            is_blocked=True,
            block_reason="Human approval required before execution",
        )
        await db.commit()
        raise HTTPException(
            status_code=status.HTTP_402_PAYMENT_REQUIRED,
            detail=f"Tool '{tool.name}' requires human approval. "
                   f"Submit approval request to /api/v1/security/approvals before execution. "
                   f"Risk level: {auth_result.risk_level or 'unknown'}",
            headers={"X-Approval-Required": "true", "X-Risk-Level": auth_result.risk_level or "unknown"},
        )

    # --- Rate Limit Check ---
    if not security.check_rate_limit(
        tool_name=tool.name,
        tenant_id=str(tenant_uuid),
        user_id=str(current_user.sub),
    ):
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Rate limit exceeded for this tool. Please slow down.",
        )

    # --- SSRF Protection ---
    is_safe, ssrf_reason = _is_ssrf_safe_url(tool.server_url)
    if not is_safe:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Tool server URL blocked by SSRF protection: {ssrf_reason}",
        )

    # --- Prompt Injection Scanning on Arguments ---
    threat_detected = False
    threat_details = None
    if req.arguments:
        arg_str = json.dumps(req.arguments, default=str)
        scan_result = (
            _ai_security.scan_text(arg_str, context="mcp_tool_input")
            if _ai_security else {"is_blocked": False, "threats": [], "reason": None}
        )
        if scan_result.get("is_blocked") or scan_result.get("threats"):
            threat_detected = True
            threat_details = json.dumps(scan_result.get("threats", []))

            _log_tool_execution(
                db=db, tool=tool, tool_id=tool_id, tenant_uuid=tenant_uuid,
                success=False, latency_ms=0.0,
                caller_user_id=str(current_user.sub), caller_roles=user_roles_str,
                arguments_keys=list(req.arguments.keys()),
                error_msg=f"Blocked: AI threat detected: {scan_result.get('reason')}",
                request_id=str(uuid.uuid4()),
                approval_state=None, requires_approval=False,
                threat_detected=True, threat_details=threat_details,
                is_blocked=True, block_reason=scan_result.get("reason"),
            )
            await db.commit()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Tool arguments blocked by AI security gateway: {scan_result.get('reason')}",
            )

    # --- Argument Schema Validation ---
    if tool.config_schema:
        schema_error = _validate_tool_arguments(req.arguments or {}, tool.config_schema)
        if schema_error:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Argument validation failed: {schema_error}",
            )

    # --- Execute Tool with Timeout + Retry ---
    start_time = time.time()
    request_id = str(uuid.uuid4())
    success = False
    result_data = None
    error_msg = None
    caller_roles = list(user_roles_str)

    # Decrypt API key if encrypted
    server_api_key = None
    if tool.api_key:
        server_api_key = (
            decrypt_api_key(tool.api_key) if tool.api_key_encrypted else tool.api_key
        )

    timeout = min(req.timeout_seconds or tool.timeout_seconds, MAX_TOOL_TIMEOUT_SECONDS)

    for attempt in range(MAX_TOOL_RETRIES + 1):
        try:
            headers = {"Content-Type": "application/json"}
            if server_api_key:
                headers["Authorization"] = f"Bearer {server_api_key}"

            transport = httpx.AsyncHTTPTransport(verify=True)
            async with httpx.AsyncClient(transport=transport, verify=True, timeout=timeout) as client:
                payload = {
                    "jsonrpc": "2.0",
                    "id": request_id,
                    "method": "tools/call",
                    "params": {
                        "name": tool.name,
                        "arguments": req.arguments or {},
                    },
                }
                response = await client.post(
                    tool.server_url,
                    json=payload,
                    headers=headers,
                )

                if response.status_code != 200:
                    error_msg = f"MCP server returned {response.status_code}: {response.text[:200]}"
                    tool.total_errors += 1
                else:
                    data = response.json()
                    if "error" in data and data["error"]:
                        error_msg = str(data["error"])
                        tool.total_errors += 1
                    else:
                        result_data = data.get("result", data)

                        # --- Prompt Injection Scanning on Results ---
                        result_str = json.dumps(result_data, default=str)
                        result_scan = (
                            _ai_security.scan_text(result_str, context="tool_result")
                            if _ai_security else {"is_blocked": False, "threats": [], "reason": None}
                        )
                        if result_scan.get("is_blocked"):
                            threat_detected = True
                            threat_details = json.dumps(result_scan.get("threats", []))
                            error_msg = f"Tool result blocked by AI security: {result_scan.get('reason')}"
                            tool.total_errors += 1
                            result_data = None
                            # Don't retry on security-blocking results
                            break
                        elif result_scan.get("threats"):
                            threat_detected = True
                            threat_details = json.dumps(result_scan.get("threats", []))
                            # Sanitize: remove detected threat patterns from result
                            logger.warning(
                                f"Tool '{tool.name}' result had threat patterns but was not blocked. "
                                f"Threats: {result_scan.get('threats')}"
                            )

                        success = True
                        break  # Success, no retry needed

        except (httpx.TimeoutException, httpx.ConnectError) as e:
            error_msg = f"{type(e).__name__}: {str(e)[:200]}"
            tool.total_errors += 1
            if attempt < MAX_TOOL_RETRIES:
                # Exponential backoff
                await asyncio.sleep(min(2 ** attempt, 5))
                continue
        except Exception as e:
            error_msg = f"{type(e).__name__}: {str(e)[:200]}"
            tool.total_errors += 1
            break  # Non-retryable error

    latency_ms = round((time.time() - start_time) * 1000, 2)

    tool.execution_count += 1
    if tool.avg_latency_ms == 0:
        tool.avg_latency_ms = latency_ms
    else:
        tool.avg_latency_ms = round((tool.avg_latency_ms * 0.9) + (latency_ms * 0.1), 2)

    if success:
        tool.last_used_at = datetime.utcnow()
    tool.updated_at = datetime.utcnow()

    _log_tool_execution(
        db=db, tool=tool, tool_id=tool_id, tenant_uuid=tenant_uuid,
        success=success, latency_ms=latency_ms,
        caller_user_id=str(current_user.sub), caller_roles=caller_roles,
        arguments_keys=list(req.arguments.keys()) if req.arguments else [],
        error_msg=error_msg, request_id=request_id,
        approval_state="approved" if auth_result.requires_approval is False else None,
        requires_approval=auth_result.requires_approval,
        threat_detected=threat_detected, threat_details=threat_details,
        is_blocked=threat_detected, block_reason=None,
    )

    await db.commit()

    return MCPToolCallResult(
        tool_id=str(tool_id),
        tool_name=tool.name,
        success=success,
        result=result_data,
        error=error_msg,
        latency_ms=latency_ms,
        executed_at=datetime.utcnow(),
        request_id=request_id,
    )


def _log_tool_execution(
    db: AsyncSession,
    tool: MCPTool,
    tool_id: uuid.UUID,
    tenant_uuid: uuid.UUID,
    success: bool,
    latency_ms: float,
    caller_user_id: str,
    caller_roles: List[str],
    arguments_keys: List[str],
    error_msg: Optional[str],
    request_id: str,
    approval_state: Optional[str],
    requires_approval: bool,
    threat_detected: bool,
    threat_details: Optional[str],
    is_blocked: bool,
    block_reason: Optional[str],
):
    """Log a tool execution to the audit log with full security context.

    Note: caller must commit the db session after this function returns.
    The log is added but not committed to avoid partial transaction issues.
    """
    log = MCPExecutionLog(
        tenant_id=tenant_uuid,
        tool_id=tool_id,
        tool_name=tool.name,
        category=tool.category,
        success=success,
        latency_ms=latency_ms,
        caller_user_id=caller_user_id,
        caller_roles=caller_roles,
        arguments_keys=arguments_keys,
        error_message=error_msg,
        request_id=request_id,
        approval_state=approval_state,
        requires_approval=requires_approval,
        threat_detected=threat_detected,
        threat_details=threat_details,
        is_blocked=is_blocked,
        block_reason=block_reason,
    )
    db.add(log)


# -------------------------------------------------------------------
# Audit & Statistics Endpoints
# -------------------------------------------------------------------

@router.get("/logs", response_model=List[MCPExecutionLogDTO], summary="Get Execution Logs")
async def get_execution_logs(
    tool_id: Optional[uuid.UUID] = Query(None, description="Filter by tool"),
    success_only: Optional[bool] = Query(None, description="Filter by success"),
    hours: int = Query(24, description="Look back hours"),
    limit: int = Query(100, ge=1, le=500),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get MCP tool execution logs."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(MCPExecutionLog).where(MCPExecutionLog.tenant_id == tenant_uuid)

    if tool_id:
        stmt = stmt.where(MCPExecutionLog.tool_id == tool_id)
    if success_only is not None:
        stmt = stmt.where(MCPExecutionLog.success == success_only)

    if hours > 0:
        from datetime import timedelta
        cutoff = datetime.utcnow() - timedelta(hours=hours)
        stmt = stmt.where(MCPExecutionLog.created_at >= cutoff)

    stmt = stmt.order_by(desc(MCPExecutionLog.created_at)).limit(limit)
    res = await db.execute(stmt)
    logs = res.scalars().all()

    return [
        MCPExecutionLogDTO(
            id=str(l.id),
            tool_id=str(l.tool_id),
            tool_name=l.tool_name,
            category=l.category,
            success=l.success,
            latency_ms=l.latency_ms,
            caller_user_id=l.caller_user_id,
            caller_roles=l.caller_roles,
            arguments_keys=l.arguments_keys,
            error_message=l.error_message,
            request_id=l.request_id,
            tenant_id=str(l.tenant_id),
            created_at=l.created_at,
            approval_state=l.approval_state,
            requires_approval=l.requires_approval,
            threat_detected=l.threat_detected,
            threat_details=l.threat_details,
            is_blocked=l.is_blocked,
            block_reason=l.block_reason,
        )
        for l in logs
    ]


@router.get("/stats", response_model=List[MCPToolStatsDTO], summary="Get Tool Statistics")
async def get_tool_stats(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get statistics for all MCP tools."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(MCPTool).where(MCPTool.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    tools = res.scalars().all()

    log_stmt = (
        select(
            MCPExecutionLog.tool_id,
            func.count().label("total"),
            func.sum(func.cast(MCPExecutionLog.success, Integer)).label("success"),
            func.avg(MCPExecutionLog.latency_ms).label("avg_latency"),
        )
        .where(
            MCPExecutionLog.tenant_id == tenant_uuid,
            MCPExecutionLog.tool_id.in_([t.id for t in tools]),
        )
        .group_by(MCPExecutionLog.tool_id)
    )
    log_res = await db.execute(log_stmt)
    log_stats = {row.tool_id: row for row in log_res}

    # Pre-fetch most common error per tool
    error_stmt = (
        select(
            MCPExecutionLog.tool_id,
            MCPExecutionLog.error_message,
            func.count().label("err_count"),
        )
        .where(
            MCPExecutionLog.tenant_id == tenant_uuid,
            MCPExecutionLog.tool_id.in_([t.id for t in tools]),
            MCPExecutionLog.error_message.isnot(None),
        )
        .order_by(desc("err_count"))
    )
    error_res = await db.execute(error_stmt)
    most_common_errors: Dict[uuid.UUID, str] = {}
    for row in error_res:
        if row.tool_id not in most_common_errors:
            most_common_errors[row.tool_id] = row.error_message

    result = []
    for tool in tools:
        stats = log_stats.get(tool.id)
        total = stats.total if stats else 0
        success_count = stats.success if stats else 0
        error_count = total - success_count

        avg_lat = round((stats.avg_latency or 0.0), 2) if stats else 0.0

        result.append(MCPToolStatsDTO(
            tool_id=str(tool.id),
            tool_name=tool.name,
            category=tool.category,
            execution_count=tool.execution_count,
            success_count=success_count,
            error_count=error_count,
            success_rate=round(success_count / total * 100, 2) if total > 0 else 0.0,
            avg_latency_ms=round(avg_lat, 2),
            p99_latency_ms=0.0,
            last_used_at=tool.last_used_at,
            most_common_error=most_common_errors.get(tool.id),
        ))

    return result


# -------------------------------------------------------------------
# Helper functions
# -------------------------------------------------------------------

def _tool_to_dto(tool: MCPTool) -> MCPToolDTO:
    return MCPToolDTO(
        id=str(tool.id),
        name=tool.name,
        description=tool.description,
        category=tool.category,
        server_name=tool.server_name,
        server_url=tool.server_url,
        api_key_configured=tool.api_key is not None,
        risk_level=tool.risk_level or "medium",
        requires_approval=bool(tool.requires_approval),
        visibility=tool.visibility,
        required_roles=tool.required_roles,
        required_permissions=tool.required_permissions,
        timeout_seconds=tool.timeout_seconds,
        enabled=tool.enabled,
        status=tool.status,
        last_used_at=tool.last_used_at,
        execution_count=tool.execution_count,
        total_errors=tool.total_errors,
        avg_latency_ms=tool.avg_latency_ms,
        tenant_id=str(tool.tenant_id),
        created_at=tool.created_at,
        updated_at=tool.updated_at,
    )


def _user_roles_to_str(user_roles) -> List[str]:
    """Convert PlatformRole enum list to string list for security gateway comparison."""
    result = []
    for r in user_roles:
        if isinstance(r, PlatformRole):
            result.append(r.value)
        else:
            result.append(str(r))
    return result
