"""
Notification Service API Router
Endpoints for dispatching system alerts, emails, Slack notifications, and webhook triggers.
"""

from fastapi import APIRouter, Depends, HTTPException, status

from enterprise_ai_platform.common.security_rbac import (
    get_current_user,
    TokenPayload,
)
from .notifier import notification_dispatcher, NotificationRequestDTO

router = APIRouter(prefix="/api/v1/notifications", tags=["Multi-Channel Notifications"])


@router.post("/send", summary="Send Multi-Channel Notification")
async def send_notification(req: NotificationRequestDTO):
    """Dispatch system alert or email notification."""
    result = await notification_dispatcher.dispatch_notification(req)
    return result
