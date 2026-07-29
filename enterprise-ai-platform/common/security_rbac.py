"""
RBAC & Security Engine
Enforces 10-role granular permission validation middleware and JWT parsing across all platform services.
"""

from enum import Enum
from typing import List, Set, Optional, Dict, Any
from datetime import datetime, timezone
import jwt
from fastapi import Depends, HTTPException, Security, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, Field

from .config import settings

security_bearer = HTTPBearer(auto_error=True)


class PlatformRole(str, Enum):
    """Platform RBAC Roles (10 Tiers)"""
    SUPER_ADMIN = "super_admin"
    WORKSPACE_ADMIN = "workspace_admin"
    ORG_ADMIN = "org_admin"
    SALES_MANAGER = "sales_manager"
    SALES_AGENT = "sales_agent"
    SUPPORT_MANAGER = "support_manager"
    SUPPORT_AGENT = "support_agent"
    KNOWLEDGE_MANAGER = "knowledge_manager"
    AUDITOR = "auditor"
    END_USER = "end_user"


class Permission(str, Enum):
    """Platform Fine-Grained Permissions"""
    # System Administration
    SYSTEM_MANAGE = "system:manage"
    SYSTEM_AUDIT_READ = "system:audit:read"
    
    # Workspace & Organization
    ORG_READ = "org:read"
    ORG_WRITE = "org:write"
    ORG_DELETE = "org:delete"
    TENANT_MANAGE = "tenant:manage"
    
    # User Management
    USER_READ = "user:read"
    USER_WRITE = "user:write"
    USER_DELETE = "user:delete"
    USER_INVITE = "user:invite"
    
    # AI & Agents
    AGENT_READ = "agent:read"
    AGENT_WRITE = "agent:write"
    AGENT_EXECUTE = "agent:execute"
    PROMPT_MANAGE = "prompt:manage"
    
    # Knowledge Base & RAG
    KNOWLEDGE_READ = "knowledge:read"
    KNOWLEDGE_WRITE = "knowledge:write"
    KNOWLEDGE_DELETE = "knowledge:delete"
    VECTOR_MANAGE = "vector:manage"
    
    # Sales & CRM
    LEADS_READ = "leads:read"
    LEADS_WRITE = "leads:write"
    DEALS_MANAGE = "deals:manage"
    COUPON_MANAGE = "coupon:manage"
    
    # Support & Tickets
    TICKET_READ = "ticket:read"
    TICKET_WRITE = "ticket:write"
    TICKET_ASSIGN = "ticket:assign"
    TICKET_REFUND = "ticket:refund"
    LIVE_HANDOFF = "live:handoff"
    
    # Analytics & Workflows
    ANALYTICS_READ = "analytics:read"
    WORKFLOW_MANAGE = "workflow:manage"
    BILLING_READ = "billing:read"
    BILLING_MANAGE = "billing:manage"


# Role to Permission Matrix
ROLE_PERMISSIONS_MAP: Dict[PlatformRole, Set[Permission]] = {
    PlatformRole.SUPER_ADMIN: set(Permission),  # Full access to everything
    
    PlatformRole.WORKSPACE_ADMIN: {
        Permission.ORG_READ, Permission.ORG_WRITE, Permission.TENANT_MANAGE,
        Permission.USER_READ, Permission.USER_WRITE, Permission.USER_INVITE,
        Permission.AGENT_READ, Permission.AGENT_WRITE, Permission.AGENT_EXECUTE, Permission.PROMPT_MANAGE,
        Permission.KNOWLEDGE_READ, Permission.KNOWLEDGE_WRITE, Permission.KNOWLEDGE_DELETE, Permission.VECTOR_MANAGE,
        Permission.LEADS_READ, Permission.LEADS_WRITE, Permission.DEALS_MANAGE, Permission.COUPON_MANAGE,
        Permission.TICKET_READ, Permission.TICKET_WRITE, Permission.TICKET_ASSIGN, Permission.TICKET_REFUND, Permission.LIVE_HANDOFF,
        Permission.ANALYTICS_READ, Permission.WORKFLOW_MANAGE, Permission.BILLING_READ, Permission.BILLING_MANAGE,
    },
    
    PlatformRole.ORG_ADMIN: {
        Permission.ORG_READ, Permission.USER_READ, Permission.USER_WRITE, Permission.USER_INVITE,
        Permission.AGENT_READ, Permission.AGENT_WRITE, Permission.AGENT_EXECUTE, Permission.PROMPT_MANAGE,
        Permission.KNOWLEDGE_READ, Permission.KNOWLEDGE_WRITE,
        Permission.LEADS_READ, Permission.LEADS_WRITE, Permission.DEALS_MANAGE,
        Permission.TICKET_READ, Permission.TICKET_WRITE, Permission.TICKET_ASSIGN, Permission.LIVE_HANDOFF,
        Permission.ANALYTICS_READ, Permission.WORKFLOW_MANAGE, Permission.BILLING_READ,
    },
    
    PlatformRole.SALES_MANAGER: {
        Permission.USER_READ, Permission.AGENT_READ, Permission.AGENT_EXECUTE,
        Permission.KNOWLEDGE_READ,
        Permission.LEADS_READ, Permission.LEADS_WRITE, Permission.DEALS_MANAGE, Permission.COUPON_MANAGE,
        Permission.ANALYTICS_READ,
    },
    
    PlatformRole.SALES_AGENT: {
        Permission.USER_READ, Permission.AGENT_READ, Permission.AGENT_EXECUTE,
        Permission.KNOWLEDGE_READ,
        Permission.LEADS_READ, Permission.LEADS_WRITE,
    },
    
    PlatformRole.SUPPORT_MANAGER: {
        Permission.USER_READ, Permission.AGENT_READ, Permission.AGENT_EXECUTE,
        Permission.KNOWLEDGE_READ, Permission.KNOWLEDGE_WRITE,
        Permission.TICKET_READ, Permission.TICKET_WRITE, Permission.TICKET_ASSIGN, Permission.TICKET_REFUND, Permission.LIVE_HANDOFF,
        Permission.ANALYTICS_READ,
    },
    
    PlatformRole.SUPPORT_AGENT: {
        Permission.USER_READ, Permission.AGENT_READ, Permission.AGENT_EXECUTE,
        Permission.KNOWLEDGE_READ,
        Permission.TICKET_READ, Permission.TICKET_WRITE, Permission.LIVE_HANDOFF,
    },
    
    PlatformRole.KNOWLEDGE_MANAGER: {
        Permission.AGENT_READ, Permission.PROMPT_MANAGE,
        Permission.KNOWLEDGE_READ, Permission.KNOWLEDGE_WRITE, Permission.KNOWLEDGE_DELETE, Permission.VECTOR_MANAGE,
    },
    
    PlatformRole.AUDITOR: {
        Permission.SYSTEM_AUDIT_READ, Permission.ORG_READ, Permission.USER_READ,
        Permission.ANALYTICS_READ, Permission.BILLING_READ,
    },
    
    PlatformRole.END_USER: {
        Permission.AGENT_EXECUTE, Permission.KNOWLEDGE_READ, Permission.TICKET_READ, Permission.TICKET_WRITE,
    },
}


class TokenPayload(BaseModel):
    sub: str = Field(..., description="Subject / User ID")
    tenant_id: str = Field(..., description="Organization Tenant ID")
    email: Optional[str] = None
    roles: List[PlatformRole] = Field(default_factory=list)
    permissions: List[Permission] = Field(default_factory=list)
    session_id: Optional[str] = None
    exp: int


def verify_jwt_token(token: str) -> TokenPayload:
    """Verifies JWT signature and extracts user payload with roles and tenant isolation info."""
    try:
        if settings.JWT_PUBLIC_KEY:
            payload = jwt.decode(token, settings.JWT_PUBLIC_KEY, algorithms=["RS256"])
        else:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])

        # Validate Expiration
        exp = payload.get("exp")
        if not exp or datetime.fromtimestamp(exp, tz=timezone.utc) < datetime.now(timezone.utc):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired",
                headers={"WWW-Authenticate": "Bearer"},
            )

        roles = [PlatformRole(r) for r in payload.get("roles", []) if r in PlatformRole._value2member_map_]
        
        # Derive effective permissions from roles
        effective_permissions: Set[Permission] = set()
        for role in roles:
            effective_permissions.update(ROLE_PERMISSIONS_MAP.get(role, set()))

        return TokenPayload(
            sub=payload.get("sub"),
            tenant_id=payload.get("tenant_id", "default_tenant"),
            email=payload.get("email"),
            roles=roles,
            permissions=list(effective_permissions),
            session_id=payload.get("session_id"),
            exp=exp,
        )

    except jwt.PyJWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid authentication token: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"},
        )


def get_current_user(credentials: HTTPAuthorizationCredentials = Security(security_bearer)) -> TokenPayload:
    """Dependency that extracts and validates current authenticated user token."""
    return verify_jwt_token(credentials.credentials)


class RequirePermissions:
    """FastAPI Dependency enforcing required permissions for route access."""

    def __init__(self, *required_permissions: Permission):
        self.required_permissions = set(required_permissions)

    def __call__(self, user: TokenPayload = Depends(get_current_user)) -> TokenPayload:
        user_perms = set(user.permissions)
        missing = self.required_permissions - user_perms
        if missing and PlatformRole.SUPER_ADMIN not in user.roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Insufficient permissions. Required: {[p.value for p in missing]}",
            )
        return user
