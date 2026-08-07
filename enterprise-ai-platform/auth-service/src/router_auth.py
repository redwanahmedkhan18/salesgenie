"""
Auth Service API Router
Defines endpoints for authentication, OAuth2 callbacks, MFA management, sessions, and invitations.
"""

import base64
import json
import uuid
import smtplib
import traceback
from datetime import datetime, timedelta, timezone
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Optional, AsyncGenerator

from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from sqlalchemy import String, Boolean, DateTime

from enterprise_ai_platform.common.config import settings
from enterprise_ai_platform.common.database import get_async_db
from enterprise_ai_platform.common.models_base import Base, UUIDPrimaryKeyMixin, TimestampMixin
from enterprise_ai_platform.common.security_rbac import (
  get_current_user,
  TokenPayload,
  RequirePermissions,
  Permission,
  PlatformRole,
)
from enterprise_ai_platform.auth_service.src.models import (
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
    ForgotPasswordRequest,
    ResetPasswordRequest,
    PasswordResetToken,
    UserVerificationToken,
    User,
)
from enterprise_ai_platform.auth_service.src.keycloak_client import keycloak_client
from enterprise_ai_platform.auth_service.src.jwt_handler import create_access_token, create_refresh_token, hash_token

router = APIRouter(prefix="/api/v1/auth", tags=["Authentication & Security"])


async def get_optional_db() -> AsyncGenerator[Optional[AsyncSession], None]:
    """Get database session with fallback for when DB is unavailable."""
    try:
        async for session in get_async_db():
            yield session
            return
    except Exception:
        yield None
        return


@router.post("/login", response_model=LoginResponse, summary="User Authentication Login")
async def login(
    req: LoginRequest,
    request: Request,
    db: AsyncSession = Depends(get_async_db),
):
    """
    Authenticate user via Keycloak credentials and issue JWT tokens with RBAC roles.
    Includes MFA verification step if enabled for user account.
    Falls back to local bcrypt password verification when Keycloak is unavailable.
    """
    user_id_str = str(uuid.uuid5(uuid.NAMESPACE_DNS, req.email))
    auth_success = False

    try:
        auth_data = await keycloak_client.authenticate_user_credentials(req.email, req.password)
        if auth_data and auth_data.get("access_token"):
            auth_success = True
    except HTTPException:
        pass
    except Exception:
        pass

    if not auth_success:
        if db and not isinstance(db, Exception):
            try:
                user_stmt = select(User).where(User.email == req.email)
                user_result = await db.execute(user_stmt)
                user = user_result.scalar_one_or_none()

                if user is None:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Invalid email or password credentials",
                    )

                if not user.verify_password(req.password):
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Invalid email or password credentials",
                    )

                if not user.is_active:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Account is deactivated",
                    )

                user_id_str = str(user.id)
                auth_success = True
            except HTTPException:
                raise
            except Exception:
                pass

    if not auth_success:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password credentials",
        )

    mfa_record_exists = False
    try:
        mfa_stmt = select(MFASecret).where(MFASecret.user_id == uuid.UUID(user_id_str), MFASecret.is_enabled == True)
        mfa_res = await db.execute(mfa_stmt)
        mfa_secret_rec = mfa_res.scalar_one_or_none()
        if mfa_secret_rec:
            mfa_record_exists = True
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
            valid_mfa = keycloak_client.verify_mfa_code(mfa_secret_rec.secret_key, req.mfa_code)
            if not valid_mfa:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid Multi-Factor Authentication Code",
                )
    except HTTPException:
        raise
    except Exception:
        pass

    assigned_roles = [PlatformRole.SUPPORT_AGENT.value, PlatformRole.SALES_AGENT.value]
    session_id = str(uuid.uuid4())

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

    try:
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
    except Exception:
        pass

    return LoginResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        user_id=user_id_str,
        roles=assigned_roles,
        tenant_id=req.tenant_id or "default_tenant",
        mfa_required=False,
    )


@router.post("/signup", response_model=SignupResponse, summary="User Registration with Email Verification")
async def signup(
    req: SignupRequest,
    db: Optional[AsyncSession] = Depends(get_optional_db),
):
    """Register a new user account with email verification required."""
    from sqlalchemy import text
    from enterprise_ai_platform.auth_service.src.models import Organization
    
    user_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, req.email)
    tenant_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, req.company)

    verification_token = uuid.uuid4().hex
    expires_at = datetime.now(timezone.utc) + timedelta(hours=24)

    org_id = None
    if db and not isinstance(db, Exception):
        try:
            existing = await db.execute(
                select(User).where(User.email == req.email)
            )
            if existing.scalar_one_or_none():
                raise HTTPException(status_code=409, detail="An account with this email already exists")
        except HTTPException:
            raise
        except Exception:
            pass

        try:
            org_result = await db.execute(
                select(Organization).where(Organization.name == req.company)
            )
            organization = org_result.scalar_one_or_none()
            
            if not organization:
                org_id = tenant_uuid
                org_stmt = text(
                    "INSERT INTO organizations (id, name, domain, is_active, created_at, updated_at) "
                    "VALUES (:id, :name, :domain, true, now(), now())"
                )
                await db.execute(org_stmt, {"id": org_id, "name": req.company, "domain": req.company.lower().replace(" ", "-")})
            else:
                org_id = organization.id
            
            org_id_value = org_id if org_id else organization.id

            user = User(
                id=user_uuid,
                organization_id=org_id_value,
                email=req.email,
                full_name=req.full_name,
                company=req.company,
                is_verified=False,
                is_active=True,
            )
            user.set_password(req.password)
            db.add(user)

            verification_record = UserVerificationToken(
                user_id=user_uuid,
                email=req.email,
                token=verification_token,
                expires_at=expires_at,
                is_verified=False,
            )
            db.add(verification_record)
            await db.commit()
        except HTTPException:
            raise
        except Exception:
            traceback.print_exc()
            await db.rollback()
            raise

    email_sent = send_verification_email(req.email, verification_token)

    if email_sent:
        return SignupResponse(
            status="pending_verification",
            message="Account created! Please check your email to verify your account.",
            requires_verification=True,
        )
    else:
        return SignupResponse(
            status="error",
            message="Account created but verification email could not be sent. Please contact support.",
            requires_verification=False,
        )


@router.post("/forgot-password", response_model=dict, summary="Request Password Reset")
async def forgot_password(
    req: ForgotPasswordRequest,
    db: Optional[AsyncSession] = Depends(get_optional_db),
):
    """Request password reset link sent to email."""
    user_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, req.email)
    
    if db and not isinstance(db, Exception):
        try:
            user_exists = await db.execute(
                select(MFASecret).where(MFASecret.user_id == user_uuid)
            )
            if not user_exists.scalar_one_or_none():
                return {"success": True, "message": "If the email exists, a reset link has been sent"}
        except Exception:
            pass
    
    reset_token = uuid.uuid4().hex
    expires_at = datetime.now(timezone.utc) + timedelta(hours=1)
    
    if db and not isinstance(db, Exception):
        try:
            reset_record = PasswordResetToken(
                user_id=user_uuid,
                email=req.email,
                token=reset_token,
                expires_at=expires_at,
            )
            db.add(reset_record)
            await db.commit()
        except Exception as e:
            print(f"Failed to create reset token: {e}")
    
    send_password_reset_email(req.email, reset_token)
    
    return {"success": True, "message": "If the email exists, a reset link has been sent"}


@router.post("/reset-password", summary="Reset Password with Token")
async def reset_password(
    req: ResetPasswordRequest,
    db: Optional[AsyncSession] = Depends(get_optional_db),
    request: Request = None,
):
    if req.new_password != req.confirm_password:
        return {"success": False, "message": "Passwords do not match"}
    
    if len(req.new_password) < 8:
        return {"success": False, "message": "Password must be at least 8 characters"}
    
    reset_email = None
    
    if db and not isinstance(db, Exception):
        try:
            stmt = select(PasswordResetToken).where(
                PasswordResetToken.token == req.token,
                PasswordResetToken.is_used == False,
            )
            result = await db.execute(stmt)
            reset_record = result.scalar_one_or_none()
            
            if not reset_record:
                return {"success": False, "message": "Invalid or expired token"}
            
            if reset_record.expires_at < datetime.now(timezone.utc):
                return {"success": False, "message": "Token has expired"}
            
            reset_email = reset_record.email
            
            reset_record.is_used = True
            db.add(reset_record)
            await db.commit()
        except Exception as e:
            return {"success": False, "message": f"Reset failed: {str(e)}"}
    
    if reset_email is None:
        return {"success": False, "message": "Invalid token or database unavailable"}
    
    try:
        await keycloak_client.update_user_password(reset_email, req.new_password)
    except Exception:
        pass
    
    device_info = request.headers.get("user-agent", "Unknown") if request else "Unknown"
    ip_address = request.client.host if request and request.client else "unknown"
    
    send_password_updated_email(reset_email, device_info, ip_address)
    
    return {"success": True, "message": "Password updated successfully"}


@router.post("/verify-email", summary="Verify Email Address")
async def verify_email(
    body: dict,
    db: AsyncSession = Depends(get_async_db),
):
    """Verify user email address using the verification token from signup."""
    token = body.get("token", "")
    
    if not token:
        return {"success": False, "message": "Verification token is required"}
    
    try:
        stmt = select(UserVerificationToken).where(
            UserVerificationToken.token == token,
            UserVerificationToken.is_verified == False,
        )
        result = await db.execute(stmt)
        verification = result.scalar_one_or_none()
        
        if not verification:
            return {"success": False, "message": "Invalid or expired verification token"}
        
        if verification.expires_at < datetime.now(timezone.utc):
            return {"success": False, "message": "Verification token has expired"}
        
        verification.is_verified = True
        await db.commit()
        
        return {"success": True, "message": "Email verified successfully! You can now log in."}
    except Exception as e:
        return {"success": False, "message": f"Verification failed: {str(e)}"}


@router.get("/sessions", response_model=List[SessionDTO], summary="Get User Sessions")
async def get_sessions(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get all active sessions for the current user."""
    user_uuid = uuid.UUID(current_user.sub)
    
    stmt = select(UserSession).where(
        UserSession.user_id == user_uuid,
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


@router.post("/mfa/setup", response_model=MFASetupResponse, summary="Setup MFA")
async def setup_mfa(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Generate MFA secret and QR code for user."""
    user_uuid = uuid.UUID(current_user.sub)
    
    stmt = select(MFASecret).where(MFASecret.user_id == user_uuid)
    result = await db.execute(stmt)
    existing_mfa = result.scalars().first()
    
    if existing_mfa:
        qr_code_uri = keycloak_client.get_mfa_uri(existing_mfa.secret_key, current_user.email)
        return MFASetupResponse(
            secret_key=existing_mfa.secret_key,
            qr_code_uri=qr_code_uri,
            backup_codes=existing_mfa.backup_codes,
        )
    
    mfa_secret = MFASecret(
        user_id=user_uuid,
        secret_key=keycloak_client.generate_mfa_secret(),
        is_enabled=False,
        backup_codes=[uuid.uuid4().hex for _ in range(10)],
    )
    db.add(mfa_secret)
    await db.commit()
    
    qr_code_uri = keycloak_client.get_mfa_uri(mfa_secret.secret_key, current_user.email)
    
    return MFASetupResponse(
        secret_key=mfa_secret.secret_key,
        qr_code_uri=qr_code_uri,
        backup_codes=mfa_secret.backup_codes,
    )


@router.post("/mfa/verify", summary="Verify MFA Code")
async def verify_mfa(
    body: dict,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Verify and enable MFA for user."""
    code = body.get("code", "")
    user_uuid = uuid.UUID(current_user.sub)
    
    stmt = select(MFASecret).where(MFASecret.user_id == user_uuid)
    result = await db.execute(stmt)
    mfa_secret = result.scalar_one_or_none()
    
    if not mfa_secret:
        return {"success": False, "message": "MFA not set up"}
    
    if keycloak_client.verify_mfa_code(mfa_secret.secret_key, code):
        mfa_secret.is_enabled = True
        await db.commit()
        return {"success": True, "message": "MFA enabled successfully"}
    
    return {"success": False, "message": "Invalid MFA code"}


def send_verification_email(email: str, token: str, verification_url: str = None) -> bool:
    """Send verification email via SMTP (Mailpit in development)."""
    if verification_url is None:
        frontend_url = settings.FRONTEND_BASE_URL.rstrip('/')
        verification_url = f"{frontend_url}/verify-email?token={token}"
        if not verification_url.startswith(('http://', 'https://')):
            verification_url = f"https://{verification_url}"
    
    msg = MIMEMultipart()
    msg["From"] = settings.SMTP_FROM_ADDRESS or "noreply@salesgenie.local"
    msg["To"] = email
    msg["Subject"] = "Verify your SalesGenie Account"

    body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
        <div style="background: #0f1117; color: white; padding: 20px; text-align: center;">
            <h1>SalesGenie Enterprise</h1>
        </div>
        <div style="padding: 20px;">
            <h2 style="color: #333;">Verify Your Email</h2>
            <p>Thank you for signing up! Please click the button below to verify your email address.</p>
            <a href="{verification_url}" 
               style="display: inline-block; background: #FF6B00; color: white; padding: 12px 24px; 
                      text-decoration: none; border-radius: 6px; font-weight: bold;">
                Verify Email Address
            </a>
            <p style="margin-top: 20px; color: #666; font-size: 12px;">
                Or copy this link: {verification_url}
            </p>
            <p style="margin-top: 20px; color: #666; font-size: 12px;">
                This link will expire in 24 hours.
            </p>
        </div>
    </body>
    </html>
    """

    msg.attach(MIMEText(body, "html"))

    try:
        with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
            if settings.SMTP_USERNAME and settings.SMTP_PASSWORD:
                server.starttls()
                server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"Failed to send verification email: {e}")
        return False


def send_password_reset_email(email: str, token: str) -> bool:
    """Send password reset email via SMTP."""
    frontend_url = settings.FRONTEND_BASE_URL.rstrip('/')
    reset_path = settings.PASSWORD_RESET_PATH.lstrip('/')
    reset_url = f"{frontend_url}/{reset_path}?token={token}"
    
    if not reset_url.startswith(('http://', 'https://')):
        reset_url = f"https://{reset_url}"
    
    msg = MIMEMultipart()
    msg["From"] = settings.SMTP_FROM_ADDRESS or "noreply@salesgenie.local"
    msg["To"] = email
    msg["Subject"] = "Reset Your SalesGenie Password"

    body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
        <div style="background: #0f1117; color: white; padding: 20px; text-align: center;">
            <h1>SalesGenie Password Reset</h1>
        </div>
        <div style="padding: 20px;">
            <h2>Reset Your Password</h2>
            <p>Click the button below to reset your password:</p>
            <a href="{reset_url}" 
               style="display: inline-block; background: #FF6B00; color: white; padding: 12px 24px; 
                      text-decoration: none; border-radius: 6px; font-weight: bold;">
                Reset Password
            </a>
            <p style="margin-top: 20px; color: #666; font-size: 12px;">
                Or copy this link: {reset_url}
            </p>
            <p style="margin-top: 20px; color: #666; font-size: 12px;">
                This link will expire in 1 hour.
            </p>
        </div>
    </body>
    </html>
    """

    msg.attach(MIMEText(body, "html"))

    try:
        with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
            if settings.SMTP_USERNAME and settings.SMTP_PASSWORD:
                server.starttls()
                server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"Failed to send password reset email: {e}")
        return False


def send_password_updated_email(email: str, device_info: str, ip_address: str) -> bool:
    """Send notification that password was updated."""
    
    msg = MIMEMultipart()
    msg["From"] = settings.SMTP_FROM_ADDRESS or "noreply@salesgenie.local"
    msg["To"] = email
    msg["Subject"] = "Password Updated - SalesGenie"

    body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
        <div style="background: #0f1117; color: white; padding: 20px; text-align: center;">
            <h1>SalesGenie - Password Updated</h1>
        </div>
        <div style="padding: 20px;">
            <h2>Password Successfully Updated</h2>
            <p>Your password has been updated successfully.</p>
            <h3>Security Details:</h3>
            <ul style="text-align: left;">
                <li><strong>Time:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}</li>
                <li><strong>Location:</strong> Password Reset Flow</li>
                <li><strong>Device:</strong> {device_info[:100]}</li>
                <li><strong>IP Address:</strong> {ip_address}</li>
            </ul>
            <p style="color: #666; font-size: 12px;">
                If you didn't request this change, please contact support immediately.
            </p>
        </div>
    </body>
    </html>
    """

    msg.attach(MIMEText(body, "html"))

    try:
        with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
            if settings.SMTP_USERNAME and settings.SMTP_PASSWORD:
                server.starttls()
                server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"Failed to send password update email: {e}")
        return False