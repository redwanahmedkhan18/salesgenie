"""
Security Service API Router
Endpoints for AI security, MCP security, threat detection, and governance.
"""

import uuid
from typing import List, Optional, Dict, Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import datetime, timezone

from enterprise_ai_platform.common.database import get_async_db
from enterprise_ai_platform.common.security_rbac import (
    get_current_user,
    TokenPayload,
    PlatformRole,
)
from .models import (
    MCPToolConfig,
    MCPToolConfigDTO,
    MCPToolConfigCreate,
    AIThreatPattern,
    AIThreatPatternDTO,
    SecurityIncident,
    SecurityIncidentDTO,
    SecurityIncidentCreate,
    HumanApproval,
    HumanApprovalDTO,
    HumanApprovalRequest,
    HumanApprovalDecision,
    OrgSecurityProfile,
    OrgSecurityProfileDTO,
)
from .ai_security_gateway import AISecurityGateway
from .mcp_security_gateway import MCPSecurityGateway


router = APIRouter(prefix="/api/v1/security", tags=["Security & Governance"])

_ai_gateway = AISecurityGateway()
_mcp_gateway = MCPSecurityGateway()
_mcp_gateway.set_ai_security(_ai_gateway)


def _get_tenant_uuid(current_user: TokenPayload) -> uuid.UUID:
    return uuid.uuid5(uuid.NAMESPACE_DNS, current_user.tenant_id)


def _has_super_or_org_admin(current_user: TokenPayload) -> bool:
    return (
        PlatformRole.SUPER_ADMIN in current_user.roles
        or PlatformRole.WORKSPACE_ADMIN in current_user.roles
        or PlatformRole.ORG_ADMIN in current_user.roles
    )


# -------------------------------------------------------------------
# AI Security Gateway
# -------------------------------------------------------------------

@router.post("/scan", summary="Scan text for AI security threats")
async def scan_text(
    text: str,
    context: Optional[str] = None,
    current_user: TokenPayload = Depends(get_current_user),
):
    """Scan text (prompt, document content, tool input) for AI security threats.

    Detects prompt injection, data exfiltration, jailbreak attempts, and
    other AI-specific threats based on OWASP GenAI guidelines.
    """
    results = _ai_gateway.scan_text(text, context)
    return {
        "threats_detected": len(results["threats"]),
        "is_blocked": results["is_blocked"],
        "reason": results.get("reason"),
        "threats": results["threats"],
    }


@router.post("/scan/agent-action", summary="Scan AI agent action for threats")
async def scan_agent_action(
    action: str,
    parameters: Dict[str, Any],
    tool_name: Optional[str] = None,
    current_user: TokenPayload = Depends(get_current_user),
):
    """Scan an AI agent action for security threats."""
    results = _ai_gateway.scan_agent_action(action, parameters, tool_name)
    return {
        "threats_detected": len(results["threats"]),
        "is_blocked": results["is_blocked"],
        "reason": results.get("reason"),
        "threats": results["threats"],
    }


# -------------------------------------------------------------------
# MCP Security Gateway
# -------------------------------------------------------------------

@router.post("/mcp/tools/register", response_model=MCPToolConfigDTO, summary="Register MCP Tool")
async def register_mcp_tool(
    req: MCPToolConfigCreate,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Register a new MCP tool with the security gateway."""
    if not _has_super_or_org_admin(current_user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only super_admin or org_admin can register MCP tools",
        )

    tenant_uuid = _get_tenant_uuid(current_user)

    config = MCPToolConfig(
        tenant_id=tenant_uuid,
        tool_name=req.tool_name,
        tool_namespace=req.tool_namespace,
        risk_level=req.risk_level,
        allowed_roles=req.allowed_roles,
        requires_approval=req.requires_approval,
        allowed_tenants=req.allowed_tenants,
        parameter_schema=req.parameter_schema,
        rate_limit_per_minute=req.rate_limit_per_minute,
        is_enabled=req.is_enabled,
    )
    db.add(config)
    await db.commit()
    await db.refresh(config)

    _mcp_gateway.register_tool({
        "name": req.tool_name,
        "namespace": req.tool_namespace,
        "risk_level": req.risk_level,
        "allowed_roles": req.allowed_roles,
        "requires_approval": req.requires_approval,
        "parameter_schema": req.parameter_schema,
        "rate_limit_per_minute": req.rate_limit_per_minute,
        "is_enabled": req.is_enabled,
    })

    return MCPToolConfigDTO(
        id=str(config.id),
        tool_name=config.tool_name,
        tool_namespace=config.tool_namespace,
        risk_level=config.risk_level,
        allowed_roles=config.allowed_roles,
        requires_approval=config.requires_approval,
        allowed_tenants=config.allowed_tenants,
        parameter_schema=config.parameter_schema,
        rate_limit_per_minute=config.rate_limit_per_minute,
        is_enabled=config.is_enabled,
        created_at=config.created_at,
        updated_at=config.updated_at,
    )


@router.post("/mcp/authorize", summary="Authorize MCP tool execution")
async def authorize_mcp_tool(
    tool_name: str = Query(..., description="Tool to authorize"),
    parameters: Optional[Dict[str, Any]] = None,
    current_user: TokenPayload = Depends(get_current_user),
):
    """Check if a user is authorized to execute an MCP tool.

    Returns whether execution is allowed and if it requires human approval.
    """
    tenant_uuid = _get_tenant_uuid(current_user)
    user_roles = current_user.roles

    allowed_tenants = None
    config = _mcp_gateway._tool_configs.get(tool_name)
    if config:
        allowed_tenants = config.get("allowed_tenants")

    if allowed_tenants is not None and str(tenant_uuid) not in allowed_tenants:
        return {
            "allowed": False,
            "requires_approval": False,
            "risk_level": "critical",
            "reason": "Tenant not authorized for this tool",
        }

    result = _mcp_gateway.is_tool_allowed(
        tool_name=tool_name,
        user_roles=user_roles,
        tenant_id=str(tenant_uuid),
        params=parameters or {},
    )

    within_rate = _mcp_gateway.check_rate_limit(
        tool_name=tool_name,
        tenant_id=str(tenant_uuid),
        user_id=str(current_user.sub),
    )

    if not within_rate:
        result.allowed = False
        result.reason = "Rate limit exceeded"

    return {
        "allowed": result.allowed,
        "requires_approval": result.requires_approval,
        "risk_level": result.risk_level,
        "reason": result.reason,
    }


@router.get("/mcp/tools", response_model=List[MCPToolConfigDTO], summary="List MCP Tool Configs")
async def list_mcp_tools(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """List all MCP tool configurations for the current tenant."""
    if not _has_super_or_org_admin(current_user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admins can list MCP tool configurations",
        )

    tenant_uuid = _get_tenant_uuid(current_user)
    stmt = select(MCPToolConfig).where(MCPToolConfig.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    configs = res.scalars().all()

    return [
        MCPToolConfigDTO(
            id=str(c.id),
            tool_name=c.tool_name,
            tool_namespace=c.tool_namespace,
            risk_level=c.risk_level,
            allowed_roles=c.allowed_roles,
            requires_approval=c.requires_approval,
            allowed_tenants=c.allowed_tenants,
            parameter_schema=c.parameter_schema,
            rate_limit_per_minute=c.rate_limit_per_minute,
            is_enabled=c.is_enabled,
            created_at=c.created_at,
            updated_at=c.updated_at,
        )
        for c in configs
    ]


# -------------------------------------------------------------------
# Threat Detection & Incidents
# -------------------------------------------------------------------

@router.get("/threats/patterns", response_model=List[AIThreatPatternDTO], summary="List Threat Patterns")
async def list_threat_patterns(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """List all AI threat detection patterns."""
    if not _has_super_or_org_admin(current_user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admins can manage threat patterns",
        )

    stmt = select(AIThreatPattern).where(AIThreatPattern.is_active == True)
    res = await db.execute(stmt)
    patterns = res.scalars().all()

    return [
        AIThreatPatternDTO(
            id=str(p.id),
            threat_type=p.threat_type,
            pattern_name=p.pattern_name,
            severity=p.severity,
            is_active=p.is_active,
            description=p.description,
            created_at=p.created_at,
            updated_at=p.updated_at,
        )
        for p in patterns
    ]


@router.post("/incidents", response_model=Dict[str, Any], summary="Create Security Incident")
async def create_incident(
    req: SecurityIncidentCreate,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Record a security incident detected by the AI Security Gateway."""
    tenant_uuid = _get_tenant_uuid(current_user)

    incident = SecurityIncident(
        tenant_id=tenant_uuid,
        incident_type=req.incident_type,
        severity=req.severity,
        title=req.title,
        description=req.description,
        actor_id=req.actor_id,
        resource_type=req.resource_type,
        resource_id=req.resource_id,
        metadata_json=req.metadata,
    )
    db.add(incident)
    await db.commit()

    return {"id": str(incident.id), "status": "recorded", "incident_type": incident.incident_type}


@router.get("/incidents", response_model=List[SecurityIncidentDTO], summary="List Security Incidents")
async def list_incidents(
    severity: Optional[str] = Query(None, description="Filter by severity"),
    incident_type: Optional[str] = Query(None, description="Filter by incident type"),
    is_resolved: Optional[bool] = Query(None, description="Filter by resolved status"),
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """List security incidents for the current tenant."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(SecurityIncident).where(SecurityIncident.tenant_id == tenant_uuid)
    if severity:
        stmt = stmt.where(SecurityIncident.severity == severity)
    if incident_type:
        stmt = stmt.where(SecurityIncident.incident_type == incident_type)
    if is_resolved is not None:
        stmt = stmt.where(SecurityIncident.is_resolved == is_resolved)

    stmt = stmt.order_by(SecurityIncident.created_at.desc()).limit(100)
    res = await db.execute(stmt)
    incidents = res.scalars().all()

    return [
        SecurityIncidentDTO(
            id=str(i.id),
            incident_type=i.incident_type,
            severity=i.severity,
            title=i.title,
            description=i.description,
            actor_id=i.actor_id,
            resource_type=i.resource_type,
            resource_id=i.resource_id,
            metadata=i.metadata_json,
            is_resolved=i.is_resolved,
            resolved_by=i.resolved_by,
            resolved_at=i.resolved_at,
            created_at=i.created_at,
            tenant_id=str(i.tenant_id),
        )
        for i in incidents
    ]


# -------------------------------------------------------------------
# Human Approval Workflow
# -------------------------------------------------------------------

@router.post("/approvals", response_model=HumanApprovalDTO, summary="Request Human Approval")
async def request_approval(
    req: HumanApprovalRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Request human approval for a high-risk AI/MCP action."""
    from datetime import timedelta  # noqa: F811

    tenant_uuid = _get_tenant_uuid(current_user)

    approval = HumanApproval(
        tenant_id=tenant_uuid,
        action_type=req.action_type,
        tool_name=req.tool_name,
        actor_id=str(current_user.sub),
        parameters_json=req.parameters,
        reason=req.reason,
        status="pending",
        expires_at=datetime.now(datetime.now().astimezone().tzinfo) + timedelta(hours=24),
    )
    db.add(approval)
    await db.commit()
    await db.refresh(approval)

    return HumanApprovalDTO(
        id=str(approval.id),
        action_type=approval.action_type,
        tool_name=approval.tool_name,
        actor_id=approval.actor_id,
        parameters=approval.parameters_json,
        reason=approval.reason,
        status=approval.status,
        approver_id=approval.approver_id,
        approved_at=approval.approved_at,
        expires_at=approval.expires_at,
        created_at=approval.created_at,
        tenant_id=str(approval.tenant_id),
    )


@router.patch("/approvals/{approval_id}/decision", response_model=HumanApprovalDTO, summary="Approve/Deny Request")
async def make_decision(
    approval_id: str,
    decision: HumanApprovalDecision,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Make an approval decision on a pending approval request."""
    if not _has_super_or_org_admin(current_user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admins can approve security requests",
        )

    stmt = select(HumanApproval).where(HumanApproval.id == uuid.UUID(approval_id))
    res = await db.execute(stmt)
    approval = res.scalar_one_or_none()

    if not approval:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Approval request not found",
        )

    if approval.status != "pending":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Approval already {approval.status}",
        )

    approval.status = "approved" if decision.approved else "denied"
    approval.approver_id = decision.approver_id
    approval.approved_at = datetime.now(timezone.utc)

    await db.commit()
    await db.refresh(approval)

    return HumanApprovalDTO(
        id=str(approval.id),
        action_type=approval.action_type,
        tool_name=approval.tool_name,
        actor_id=approval.actor_id,
        parameters=approval.parameters_json,
        reason=approval.reason,
        status=approval.status,
        approver_id=approval.approver_id,
        approved_at=approval.approved_at,
        expires_at=approval.expires_at,
        created_at=approval.created_at,
        tenant_id=str(approval.tenant_id),
    )


@router.get("/approvals/pending", response_model=List[HumanApprovalDTO], summary="List Pending Approvals")
async def list_pending_approvals(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """List pending approval requests for the current tenant."""
    if not _has_super_or_org_admin(current_user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admins can view approval requests",
        )

    tenant_uuid = _get_tenant_uuid(current_user)
    stmt = (
        select(HumanApproval)
        .where(
            HumanApproval.tenant_id == tenant_uuid,
            HumanApproval.status == "pending",
        )
        .order_by(HumanApproval.created_at.desc())
        .limit(50)
    )
    res = await db.execute(stmt)
    approvals = res.scalars().all()

    return [
        HumanApprovalDTO(
            id=str(a.id),
            action_type=a.action_type,
            tool_name=a.tool_name,
            actor_id=a.actor_id,
            parameters=a.parameters_json,
            reason=a.reason,
            status=a.status,
            approver_id=a.approver_id,
            approved_at=a.approved_at,
            expires_at=a.expires_at,
            created_at=a.created_at,
            tenant_id=str(a.tenant_id),
        )
        for a in approvals
    ]


# -------------------------------------------------------------------
# Security Profile & Score
# -------------------------------------------------------------------

@router.get("/profile", response_model=OrgSecurityProfileDTO, summary="Get Security Profile")
async def get_security_profile(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get the security profile for the current organization."""
    tenant_uuid = _get_tenant_uuid(current_user)

    stmt = select(OrgSecurityProfile).where(OrgSecurityProfile.tenant_id == tenant_uuid)
    res = await db.execute(stmt)
    profile = res.scalar_one_or_none()

    if not profile:
        profile = OrgSecurityProfile(
            tenant_id=tenant_uuid,
            security_score=_mcp_gateway.get_security_score(),
        )
        db.add(profile)
        await db.commit()
        await db.refresh(profile)

    return OrgSecurityProfileDTO(
        tenant_id=str(profile.tenant_id),
        security_score=profile.security_score,
        last_scanned_at=profile.last_scanned_at,
        mfa_enforced=profile.mfa_enforced,
        session_timeout_minutes=profile.session_timeout_minutes,
        max_sessions_per_user=profile.max_sessions_per_user,
        data_retention_days=profile.data_retention_days,
        ai_approvals_required=profile.ai_approvals_required,
        risk_threshold=profile.risk_threshold,
    )


@router.get("/score", summary="Get Organization Security Score")
async def get_security_score(
    current_user: TokenPayload = Depends(get_current_user),
):
    """Get the current security score and breakdown."""
    score = _mcp_gateway.get_security_score()
    registered_tools = len(_mcp_gateway._tool_configs)

    return {
        "security_score": round(score, 1),
        "registered_mcp_tools": registered_tools,
        "active_threat_patterns": len(_ai_gateway._compiled_patterns),
        "risk_distribution": {
            "low": sum(1 for t in _mcp_gateway._tool_configs.values() if t.get("risk_level") == "low"),
            "medium": sum(1 for t in _mcp_gateway._tool_configs.values() if t.get("risk_level") == "medium"),
            "high": sum(1 for t in _mcp_gateway._tool_configs.values() if t.get("risk_level") == "high"),
            "critical": sum(1 for t in _mcp_gateway._tool_configs.values() if t.get("risk_level") == "critical"),
        },
    }


# -------------------------------------------------------------------
# Predefined MCP Tool Catalog
# -------------------------------------------------------------------

DEFAULT_TOOL_CATALOG = {
    "search_company": {
        "name": "search_company",
        "namespace": "lead_intel",
        "risk_level": "low",
        "allowed_roles": ["sales_agent", "sales_manager", "super_admin", "workspace_admin", "org_admin"],
        "requires_approval": False,
        "rate_limit_per_minute": 120,
    },
    "calculate_lead_score": {
        "name": "calculate_lead_score",
        "namespace": "lead_intel",
        "risk_level": "low",
        "allowed_roles": ["sales_agent", "sales_manager", "super_admin", "workspace_admin", "org_admin"],
        "requires_approval": False,
        "rate_limit_per_minute": 300,
    },
    "summarize_document": {
        "name": "summarize_document",
        "namespace": "knowledge",
        "risk_level": "low",
        "allowed_roles": ["knowledge_manager", "sales_agent", "support_agent", "super_admin", "org_admin"],
        "requires_approval": False,
        "rate_limit_per_minute": 60,
    },
    "create_lead": {
        "name": "create_lead",
        "namespace": "crm",
        "risk_level": "medium",
        "allowed_roles": ["sales_agent", "sales_manager", "super_admin", "org_admin"],
        "requires_approval": False,
        "rate_limit_per_minute": 30,
    },
    "update_crm": {
        "name": "update_crm",
        "namespace": "crm",
        "risk_level": "medium",
        "allowed_roles": ["sales_agent", "sales_manager", "support_agent", "super_admin", "org_admin"],
        "requires_approval": False,
        "rate_limit_per_minute": 30,
    },
    "create_ticket": {
        "name": "create_ticket",
        "namespace": "support",
        "risk_level": "medium",
        "allowed_roles": ["support_agent", "support_manager", "super_admin", "org_admin"],
        "requires_approval": False,
        "rate_limit_per_minute": 30,
    },
    "search_knowledge": {
        "name": "search_knowledge",
        "namespace": "rag",
        "risk_level": "low",
        "allowed_roles": ["sales_agent", "support_agent", "knowledge_manager", "super_admin", "org_admin"],
        "requires_approval": False,
        "rate_limit_per_minute": 120,
    },
    "research_company": {
        "name": "research_company",
        "namespace": "product_intel",
        "risk_level": "low",
        "allowed_roles": ["sales_agent", "sales_manager", "knowledge_manager", "super_admin", "org_admin"],
        "requires_approval": False,
        "rate_limit_per_minute": 30,
    },
    "send_email": {
        "name": "send_email",
        "namespace": "communication",
        "risk_level": "high",
        "allowed_roles": ["sales_manager", "support_manager", "super_admin", "org_admin"],
        "requires_approval": True,
        "rate_limit_per_minute": 10,
    },
    "send_whatsapp": {
        "name": "send_whatsapp",
        "namespace": "communication",
        "risk_level": "high",
        "allowed_roles": ["sales_manager", "support_manager", "super_admin", "org_admin"],
        "requires_approval": True,
        "rate_limit_per_minute": 10,
    },
    "delete_lead": {
        "name": "delete_lead",
        "namespace": "crm",
        "risk_level": "critical",
        "allowed_roles": ["sales_manager", "super_admin", "org_admin"],
        "requires_approval": True,
        "rate_limit_per_minute": 5,
    },
    "export_customers": {
        "name": "export_customers",
        "namespace": "crm",
        "risk_level": "critical",
        "allowed_roles": ["sales_manager", "super_admin", "org_admin"],
        "requires_approval": True,
        "rate_limit_per_minute": 3,
    },
    "change_security_settings": {
        "name": "change_security_settings",
        "namespace": "admin",
        "risk_level": "critical",
        "allowed_roles": ["super_admin"],
        "requires_approval": True,
        "rate_limit_per_minute": 1,
    },
}


@router.get("/mcp/catalog", summary="Get Default MCP Tool Catalog")
async def get_mcp_catalog(
    current_user: TokenPayload = Depends(get_current_user),
):
    """Get the default MCP tool catalog with risk levels and role requirements."""
    user_roles = current_user.roles
    catalog = []

    for tool_name, config in DEFAULT_TOOL_CATALOG.items():
        allowed_roles = config["allowed_roles"]
        user_has_access = any(
            any(role in r or r in role for role in user_roles)
            for r in allowed_roles
        )
        catalog.append({
            "tool_name": tool_name,
            "namespace": config["namespace"],
            "risk_level": config["risk_level"],
            "requires_approval": config["requires_approval"],
            "allowed_roles": allowed_roles,
            "user_has_access": user_has_access,
            "rate_limit_per_minute": config["rate_limit_per_minute"],
        })

    return {"tools": catalog}
