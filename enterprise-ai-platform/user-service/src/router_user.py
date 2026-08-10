"""
User Service API Router
Endpoints for user profiles, preferences, avatar management, and user queries.
"""

import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from enterprise_ai_platform.common.database import get_async_db
from enterprise_ai_platform.common.security_rbac import (
    get_current_user,
    TokenPayload,
)
from enterprise_ai_platform.common.logging import get_structured_logger
from enterprise_ai_platform.common.data_governance import data_governance
from .models import (
    UserProfileDTO,
    UpdateProfileRequest,
    UserPreferencesDTO,
    UpdatePreferencesRequest,
    UserProfile,
    UserPreferences,
)
from enterprise_ai_platform.auth_service.src.models import User as AuthUser

logger = get_structured_logger("salesgenie.user", "user-service")

router = APIRouter(prefix="/api/v1/users", tags=["User Profiles & Settings"])


@router.get("/me", response_model=UserProfileDTO, summary="Get Current User Profile")
async def get_my_profile(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Retrieve profile details for current authenticated user."""
    user_uuid = uuid.UUID(current_user.sub)
    
    user_stmt = select(AuthUser).where(AuthUser.id == user_uuid)
    user_result = await db.execute(user_stmt)
    auth_user = user_result.scalar_one_or_none()
    
    if not auth_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    stmt = select(UserProfile).where(UserProfile.id == user_uuid)
    res = await db.execute(stmt)
    p = res.scalar_one_or_none()

    if not p:
        org_uuid = uuid.UUID(str(auth_user.organization_id)) if auth_user.organization_id else uuid.uuid5(uuid.NAMESPACE_DNS, "default")
        p = UserProfile(
            id=user_uuid,
            email=auth_user.email,
            full_name=auth_user.full_name,
            tenant_id=uuid.uuid5(uuid.NAMESPACE_DNS, str(org_uuid)),
        )
        db.add(p)
        await db.commit()

    return UserProfileDTO(
        id=p.id,
        email=p.email,
        full_name=p.full_name,
        phone_number=p.phone_number,
        avatar_url=p.avatar_url,
        job_title=p.job_title,
        department=p.department,
        tenant_id=p.tenant_id,
        is_active=p.is_active,
        created_at=p.created_at,
    )


@router.put("/me", response_model=UserProfileDTO, summary="Update Current User Profile")
async def update_my_profile(
    req: UpdateProfileRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Update profile attributes for current user."""
    user_uuid = uuid.UUID(current_user.sub)
    
    user_stmt = select(AuthUser).where(AuthUser.id == user_uuid)
    user_result = await db.execute(user_stmt)
    auth_user = user_result.scalar_one_or_none()
    
    if not auth_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    stmt = select(UserProfile).where(UserProfile.id == user_uuid)
    res = await db.execute(stmt)
    p = res.scalar_one_or_none()

    if not p:
        org_uuid = uuid.UUID(str(auth_user.organization_id)) if auth_user.organization_id else uuid.uuid5(uuid.NAMESPACE_DNS, "default")
        p = UserProfile(
            id=user_uuid,
            email=auth_user.email,
            full_name=auth_user.full_name,
            tenant_id=uuid.uuid5(uuid.NAMESPACE_DNS, str(org_uuid)),
        )
        db.add(p)

    if req.full_name:
        p.full_name = req.full_name
    if req.phone_number:
        p.phone_number = req.phone_number
    if req.avatar_url:
        p.avatar_url = req.avatar_url
    if req.job_title:
        p.job_title = req.job_title
    if req.department:
        p.department = req.department

    await db.commit()

    return UserProfileDTO(
        id=p.id,
        email=p.email,
        full_name=p.full_name,
        phone_number=p.phone_number,
        avatar_url=p.avatar_url,
        job_title=p.job_title,
        department=p.department,
        tenant_id=p.tenant_id,
        is_active=p.is_active,
        created_at=p.created_at,
    )


@router.get("/me/preferences", response_model=UserPreferencesDTO, summary="Get User Preferences")
async def get_preferences(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Get theme, language, and notification preferences."""
    user_uuid = uuid.UUID(current_user.sub)
    stmt = select(UserPreferences).where(UserPreferences.user_id == user_uuid)
    res = await db.execute(stmt)
    pref = res.scalar_one_or_none()

    if not pref:
        return UserPreferencesDTO(
            user_id=user_uuid,
            theme="dark",
            language="en",
            email_notifications=True,
            slack_notifications=False,
            keyboard_shortcuts=True,
        )

    return UserPreferencesDTO(
        user_id=pref.user_id,
        theme=pref.theme,
        language=pref.language,
        email_notifications=pref.email_notifications,
        slack_notifications=pref.slack_notifications,
        keyboard_shortcuts=pref.keyboard_shortcuts,
    )


@router.put("/me/preferences", response_model=UserPreferencesDTO, summary="Update User Preferences")
async def update_preferences(
    req: UpdatePreferencesRequest,
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Update theme and application UI preferences."""
    user_uuid = uuid.UUID(current_user.sub)
    stmt = select(UserPreferences).where(UserPreferences.user_id == user_uuid)
    res = await db.execute(stmt)
    pref = res.scalar_one_or_none()

    if not pref:
        pref = UserPreferences(user_id=user_uuid)
        db.add(pref)

    if req.theme:
        pref.theme = req.theme
    if req.language:
        pref.language = req.language
    if req.email_notifications is not None:
        pref.email_notifications = req.email_notifications
    if req.slack_notifications is not None:
        pref.slack_notifications = req.slack_notifications
    if req.keyboard_shortcuts is not None:
        pref.keyboard_shortcuts = req.keyboard_shortcuts

    await db.commit()

    return UserPreferencesDTO(
        user_id=pref.user_id,
        theme=pref.theme,
        language=pref.language,
        email_notifications=pref.email_notifications,
        slack_notifications=pref.slack_notifications,
        keyboard_shortcuts=pref.keyboard_shortcuts,
    )


@router.post("/me/export", summary="Export Personal Data (GDPR Article 20)")
async def export_my_data(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Export all personal data for the current user in machine-readable format."""
    user_uuid = uuid.UUID(current_user.sub)
    tenant_id = current_user.tenant_id

    logger.info(
        "GDPR data portability request",
        extra={"user_id": str(user_uuid), "tenant_id": tenant_id}
    )

    export = data_governance.export_user_data(tenant_id, str(user_uuid))
    export["personal_data"]["user_profile"] = {
        "email": current_user.email,
        "full_name": current_user.full_name,
        "tenant_id": tenant_id,
        "roles": getattr(current_user, "roles", []),
    }
    return export


@router.delete("/me", status_code=status.HTTP_200_OK, summary="Delete Account (GDPR Article 17)")
async def delete_my_account(
    current_user: TokenPayload = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """Delete the current user account and all associated personal data (right to erasure)."""

    user_uuid = uuid.UUID(current_user.sub)
    tenant_id = current_user.tenant_id

    logger.warning(
        "GDPR right-to-erasure request (account deletion)",
        extra={"user_id": str(user_uuid), "tenant_id": tenant_id}
    )

    profile_stmt = select(UserProfile).where(UserProfile.id == user_uuid)
    profile_res = await db.execute(profile_stmt)
    profile = profile_res.scalar_one_or_none()
    if profile:
        profile.is_active = False
        profile.email = f"deleted_{user_uuid.hex[:8]}@deleted.salesgenie.ai"
        profile.full_name = "[DELETED]"
        profile.phone_number = None
        profile.avatar_url = None

    auth_stmt = select(AuthUser).where(AuthUser.id == user_uuid)
    auth_res = await db.execute(auth_stmt)
    auth_user = auth_res.scalar_one_or_none()
    if auth_user:
        auth_user.is_active = False

    await db.commit()

    logger.info(
        "Account deleted successfully",
        extra={"user_id": str(user_uuid), "tenant_id": tenant_id}
    )

    return {
        "status": "deleted",
        "message": "Your account and PII have been deleted. "
                   "Billing, audit, and analytics records retained per legal requirements.",
        "retained_categories": [
            "billing_records",
            "audit_logs",
            "usage_analytics",
            "support_tickets",
        ],
    }


@router.get("/me/consent", summary="Get Consent Preferences")
async def get_consent(
    current_user: TokenPayload = Depends(get_current_user),
):
    """Get user consent status for marketing, analytics, and AI training."""
    tenant_id = current_user.tenant_id
    user_id = current_user.sub
    return {
        "marketing": data_governance.check_consent(tenant_id, user_id, "marketing"),
        "analytics": data_governance.check_consent(tenant_id, user_id, "analytics"),
        "ai_training": data_governance.check_consent(tenant_id, user_id, "ai_training"),
        "data_sharing": data_governance.check_consent(tenant_id, user_id, "data_sharing"),
    }


@router.post("/me/consent", summary="Update Consent Preferences")
async def update_consent(
    consent_type: str,
    granted: bool,
    current_user: TokenPayload = Depends(get_current_user),
):
    """Set or revoke consent for a specific data processing purpose."""
    if consent_type not in ("marketing", "analytics", "ai_training", "data_sharing"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid consent type. Must be one of: marketing, analytics, ai_training, data_sharing",
        )
    record = data_governance.record_consent(
        tenant_id=current_user.tenant_id,
        user_id=current_user.sub,
        consent_type=consent_type,
        granted=granted,
    )
    return {
        "consent_type": consent_type,
        "granted": record.granted,
        "granted_at": record.granted_at,
        "revoked_at": record.revoked_at,
    }
