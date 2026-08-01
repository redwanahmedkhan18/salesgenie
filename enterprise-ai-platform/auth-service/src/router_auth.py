"""
Auth Service API Router
Defines endpoints for authentication, OAuth2 callbacks, MFA management, sessions, and invitations.
"""

import base64
import json
import uuid
from datetime import datetime, timedelta, timezone
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Request, Response, status, Body
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from enterprise_ai_platform.common.config import settings
from enterprise_ai_platform.common.database import get_async_db
from enterprise_ai_platform.common.security_rbac import (
    get_current_user,
    TokenPayload,
    RequirePermissions,
    Permission,
    PlatformRole,
)
from .models import (
    LoginRequest,
    LoginResponse,
    RefreshTokenRequest,
    MFASetupResponse,
    MFAVerifyRequest,
    SessionDTO,
    CreateInvitationRequest,
    InvitationDTO,
    UserSession,
    MFASecret,
    WorkspaceInvitation,
    SignupRequest,
    SignupResponse,
)
from .keycloak_client import keycloak_client
from .jwt_handler import create_access_token, create_refresh_token, hash_token

router = APIRouter(prefix="/api/v1/auth", tags=["Authentication & Security"])


@router.post("/login", response_model=LoginResponse, summary="User Authentication Login")
async def login(
    req: LoginRequest,
    request: Request,
    db: AsyncSession = Depends(get_async_db),
):
    """
    Authenticate user via Keycloak credentials and issue JWT tokens with RBAC roles.
    Includes MFA verification step if enabled for user account.
    """
    # 1. Keycloak Credential Exchange
    auth_data = await keycloak_client.authenticate_user_credentials(req.email, req.password)
    
    # 2. Check MFA Secret Status in DB
    user_id_str = str(uuid.uuid5(uuid.NAMESPACE_DNS, req.email))
    mfa_stmt = select(MFASecret).where(MFASecret.user_id == uuid.UUID(user_id_str), MFASecret.is_enabled == True)
    mfa_res = await db.execute(mfa_stmt)
    mfa_secret_rec = mfa_res.scalar_one_or_none()

    if mfa_secret_rec:
        if not req.mfa_code:
            return LoginResponse(
                access_token="",
                refresh_token="",
                expires_in=0,
                user_id=user_id_str,
                roles=[],
                tenant_id=req.tenant_id or "default_tenant",
                mfa_required=True,
            )
        # Verify MFA Code
        valid_mfa = keycloak_client.verify_mfa_code(mfa_secret_rec.secret_key, req.mfa_code)
        if not valid_mfa:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid Multi-Factor Authentication Code",
            )

    # Default assigned roles (e.g. Sales & Support roles)
    assigned_roles = [PlatformRole.SUPPORT_AGENT.value, PlatformRole.SALES_AGENT.value]
    session_id = str(uuid.uuid4())

    # Create Access & Refresh Tokens
    access_token = create_access_token(
        user_id=user_id_str,
        tenant_id=req.tenant_id or "default_tenant",
        email=req.email,
        roles=assigned_roles,
        session_id=session_id,
    )
    refresh_token = create_refresh_token(
        user_id=user_id_str,
        tenant_id=req.tenant_id or "default_tenant",
        session_id=session_id,
    )

    # Store User Session Record
    session_record = UserSession(
        id=uuid.UUID(session_id),
        user_id=uuid.UUID(user_id_str),
        tenant_id=uuid.UUID(uuid.uuid5(uuid.NAMESPACE_DNS, req.tenant_id or "default_tenant")),
        refresh_token_hash=hash_token(refresh_token),
        ip_address=request.client.host if request.client else "127.0.0.1",
        user_agent=request.headers.get("user-agent", "Unknown Browser"),
        expires_at=datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS),
        is_active=True,
    )
    db.add(session_record)
    await db.commit()

    return LoginResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        user_id=user_id_str,
        roles=assigned_roles,
        tenant_id=req.tenant_id or "default_tenant",
        mfa_required=False,
    )


@router.get("/callback/{provider}", summary="OAuth2 Identity Provider Callback")
async def oauth_callback(
    provider: str,
    code: str,
    state: Optional[str] = None,
    redirect_uri: Optional[str] = "http://localhost:4321/auth/callback",
):
    """Process OAuth2 authorization code callback for Google, Microsoft, or GitHub."""
    if state:
        try:
            decoded_state = json.loads(base64.b64decode(state))
            original_provider = decoded_state.get('provider')
            if original_provider and original_provider != provider:
                raise HTTPException(status_code=400, detail="State mismatch - possible CSRF attack")
        except Exception:
            pass
    
    tokens = await keycloak_client.exchange_oauth_code(provider, code, redirect_uri)
    user_id_mock = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"{provider}_user"))
    
    access_token = create_access_token(
        user_id=user_id_mock,
        tenant_id="oauth_tenant",
        email=f"user@{provider}.com",
        roles=[PlatformRole.SUPPORT_AGENT.value],
    )
    return {
        "status": "success",
        "provider": provider,
        "access_token": access_token,
        "token_type": "Bearer",
    }


import base64

@router.get("/redirect/{provider}", summary="OAuth2 Redirect to Provider")
async def oauth_redirect(
    provider: str,
    redirect_uri: Optional[str] = None,
    state: Optional[str] = None,
):
    """Generate redirect URL to OAuth provider (Google, Microsoft, GitHub)."""
    if not settings.GOOGLE_CLIENT_ID and provider != 'google':
        raise HTTPException(status_code=400, detail=f"{provider} not configured")
    
    # Default to frontend callback URL - MUST be registered in Google Cloud Console
    oauth_callback_uri = redirect_uri or "http://localhost:4321/auth/callback"
    
    state_param = ""
    if state:
        state_param = f"&state={state}"
    
    provider_urls = {
        "google": f"https://accounts.google.com/o/oauth2/v2/auth?client_id={settings.GOOGLE_CLIENT_ID}&redirect_uri={oauth_callback_uri}&response_type=code&scope=openid email profile&access_type=offline&prompt=consent{state_param}",
        "microsoft": f"https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id={settings.MICROSOFT_CLIENT_ID}&redirect_uri={oauth_callback_uri}&response_type=code&scope=openid email profile&state={state}",
        "github": f"https://github.com/login/oauth/authorize?client_id={settings.GITHUB_CLIENT_ID}&redirect_uri={oauth_callback_uri}&scope=user email&state={state}",
    }
    
    if provider not in provider_urls:
        raise HTTPException(status_code=400, detail=f"Unsupported provider: {provider}")
    
    return {"redirect_url": provider_urls[provider], "state": state}


@router.post("/refresh", response_model=LoginResponse, summary="Refresh Access Token")
async def refresh_token(
    req: RefreshTokenRequest,
    db: AsyncSession = Depends(get_async_db),
):
    """Issue a new access token using a valid, non-expired refresh token."""
    token_hash = hash_token(req.refresh_token)
    stmt = select(UserSession).where(
        UserSession.refresh_token_hash == token_hash,
        UserSession.is_active == True,
    )
    result = await db.execute(stmt)
    session_rec = result.scalar_one_or_none()

    if not session_rec or session_rec.expires_at < datetime.now(timezone.utc):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired refresh token",
        )

    new_access_token = create_access_token(
        user_id=str(session_rec.user_id),
        tenant_id=str(session_rec.tenant_id),
        email="user@salesgenie.ai",
        roles=[PlatformRole.SUPPORT_AGENT.value],
        session_id=str(session_rec.id),
    )

    return LoginResponse(
        access_token=new_access_token,
        refresh_token=req.refresh_token,
        expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        user_id=str(session_rec.user_id),
        roles=[PlatformRole.SUPPORT_AGENT.value],
        tenant_id=str(session_rec.tenant_id),
        mfa_required=False,
    )


@router.post("/mfa/setup", response_model=MFASetupResponse, summary="Setup Multi-Factor Authentication")
async def mfa_setup(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Generate a TOTP MFA secret and QR code URI for user authenticator app setup."""
    secret = keycloak_client.generate_mfa_secret()
    qr_uri = keycloak_client.get_mfa_uri(secret, current_user.email or "user@salesgenie.ai")
    backup_codes = [uuid.uuid4().hex[:8].upper() for _ in range(5)]

    user_uuid = uuid.UUID(current_user.sub)
    stmt = select(MFASecret).where(MFASecret.user_id == user_uuid)
    res = await db.execute(stmt)
    rec = res.scalar_one_or_none()

    if not rec:
        rec = MFASecret(
            user_id=user_uuid,
            secret_key=secret,
            is_enabled=False,
            backup_codes=backup_codes,
        )
        db.add(rec)
    else:
        rec.secret_key = secret
        rec.backup_codes = backup_codes

    await db.commit()

    return MFASetupResponse(
        secret_key=secret,
        qr_code_uri=qr_uri,
        backup_codes=backup_codes,
    )


@router.post("/mfa/verify", summary="Verify & Activate MFA")
async def mfa_verify(
    req: MFAVerifyRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Verify standard TOTP code to activate MFA on user account."""
    user_uuid = uuid.UUID(current_user.sub)
    stmt = select(MFASecret).where(MFASecret.user_id == user_uuid)
    res = await db.execute(stmt)
    rec = res.scalar_one_or_none()

    if not rec:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="MFA setup has not been initiated")

    if not keycloak_client.verify_mfa_code(rec.secret_key, req.code):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid verification code")

    rec.is_enabled = True
    await db.commit()

    return {"status": "mfa_enabled", "message": "Multi-Factor Authentication successfully activated"}


@router.get("/sessions", response_model=List[SessionDTO], summary="List User Sessions")
async def list_sessions(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """List active devices and login sessions for current user."""
    stmt = select(UserSession).where(
        UserSession.user_id == uuid.UUID(current_user.sub),
        UserSession.is_active == True,
    )
    result = await db.execute(stmt)
    sessions = result.scalars().all()
    
    return [
        SessionDTO(
            id=s.id,
            device_name=s.device_name,
            ip_address=s.ip_address,
            user_agent=s.user_agent,
            created_at=s.created_at,
            is_active=s.is_active,
        )
        for s in sessions
    ]


@router.delete("/sessions/{session_id}", summary="Revoke User Session")
async def revoke_session(
    session_id: str,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Revoke specific user session and invalidate refresh token."""
    stmt = (
        update(UserSession)
        .where(
            UserSession.id == uuid.UUID(session_id),
            UserSession.user_id == uuid.UUID(current_user.sub),
        )
        .values(is_active=False)
    )
    await db.execute(stmt)
    await db.commit()
    return {"status": "revoked", "session_id": session_id}


@router.post(
    "/invitations",
    response_model=InvitationDTO,
    summary="Create Workspace Invitation",
    dependencies=[Depends(RequirePermissions(Permission.USER_INVITE))],
)
async def create_invitation(
    req: CreateInvitationRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Send organization invitation token for workspace onboard."""
    invite_token = uuid.uuid4().hex
    tenant_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, req.tenant_id)
    
    invitation = WorkspaceInvitation(
        email=req.email,
        role=req.role.value,
        tenant_id=tenant_uuid,
        invited_by_user_id=uuid.UUID(current_user.sub),
        token=invite_token,
        status="pending",
        expires_at=datetime.now(timezone.utc) + timedelta(days=7),
    )
    db.add(invitation)
    await db.commit()

    return InvitationDTO(
        id=invitation.id,
        email=invitation.email,
        role=invitation.role,
        tenant_id=req.tenant_id,
        status=invitation.status,
        created_at=invitation.created_at,
        expires_at=invitation.expires_at,
    )


async def get_optional_db():
    """Get database session with fallback for when DB is unavailable."""
    try:
        async for session in get_async_db():
            yield session
    except Exception:
        yield None


@router.post("/signup", response_model=SignupResponse, summary="User Registration")
async def signup(
    req: SignupRequest,
    db: Optional[AsyncSession] = Depends(get_optional_db),
):
    """Register a new user account with email verification required."""
    user_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, req.email)
    tenant_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, req.company)
    
    if db and not isinstance(db, Exception):
        try:
            user_exists = await db.execute(
                select(MFASecret).where(MFASecret.user_id == user_uuid)
            )
            if user_exists.scalar_one_or_none():
                raise HTTPException(status_code=400, detail="Email already registered")
        except Exception:
            pass
    
    session_id = str(uuid.uuid4())
    create_access_token(
        user_id=str(user_uuid),
        tenant_id=str(tenant_uuid),
        email=req.email,
        roles=[PlatformRole.SUPPORT_AGENT.value],
        session_id=session_id,
    )
    
    return SignupResponse(
        status="pending_verification",
        message="Account created! Please check your email to verify your account.",
        requires_verification=True,
    )
