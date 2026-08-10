"""
Tests for Super Admin user management endpoints in the AI Gateway admin router.
"""

import uuid
from datetime import datetime, timezone
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import HTTPException

from enterprise_ai_platform.ai_gateway_service.src.router_admin import (
    SuperAdminUser,
    UpdateUserRoleRequest,
)
from enterprise_ai_platform.common.security_rbac import PlatformRole
from enterprise_ai_platform.notification_service.src.notifier import (
    NotificationDispatcher,
    send_role_notification,
)


def _run_async(coro):
    """Simple async runner for test environments without pytest-asyncio."""
    import asyncio
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


def test_update_user_role_request_validation():
    """UpdateUserRoleRequest should accept valid role strings."""
    req = UpdateUserRoleRequest(role="sales_manager")
    assert req.role == "sales_manager"

    req2 = UpdateUserRoleRequest(role="support_agent")
    assert req2.role == "support_agent"


def test_roles_contain_all_platform_roles():
    """Ensure all PlatformRole values are representable."""
    expected = {"end_user", "sales_agent", "sales_manager", "support_agent",
                "support_manager", "knowledge_manager", "org_admin", "super_admin"}
    actual = {r.value for r in PlatformRole}
    assert expected.issubset(actual)


def test_super_admin_user_model():
    """SuperAdminUser model should have required fields."""
    user = SuperAdminUser(
        id="test-uuid",
        email="test@example.com",
        full_name="Test User",
        role="end_user",
        is_active=True,
        created_at=datetime.now(timezone.utc),
        last_login_at=None,
        tenant_id="default_tenant",
    )
    assert user.id == "test-uuid"
    assert user.email == "test@example.com"
    assert user.role == "end_user"


def test_list_users_returns_users_from_db():
    """list_users should return SuperAdminUser objects from DB query results."""
    from enterprise_ai_platform.ai_gateway_service.src.router_admin import list_users

    mock_user = MagicMock()
    mock_user.id = "test-uuid"
    mock_user.email = "test@example.com"
    mock_user.full_name = "Test User"
    mock_user.is_active = True
    mock_user.created_at = datetime.now(timezone.utc)
    mock_user.last_login_at = None
    mock_user.organization_id = None

    call_count = [0]

    async def mock_execute(query):
        call_count[0] += 1
        mock_res = MagicMock()
        scalars_mock = MagicMock()
        scalars_mock.all = MagicMock(return_value=[mock_user] if call_count[0] == 1 else [])
        mock_res.scalars = MagicMock(return_value=scalars_mock)
        mock_res.scalar_one_or_none = MagicMock(return_value=None)
        return mock_res

    mock_db = MagicMock()
    mock_db.execute = mock_execute

    mock_token = MagicMock()
    mock_token.tenant_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, "default_tenant"))
    mock_token.sub = "admin-user-id"
    mock_token.email = "admin@salesgenie.ai"

    with patch(
        "enterprise_ai_platform.ai_gateway_service.src.router_admin.require_super_admin",
        return_value=mock_token,
    ), patch(
        "enterprise_ai_platform.ai_gateway_service.src.router_admin.select"
    ) as mock_select:
        mock_select.return_value = MagicMock()
        result = _run_async(list_users(search=None, _=mock_token, db=mock_db))

    assert len(result) == 1
    assert result[0].email == "test@example.com"
    assert result[0].role == "end_user"


def test_list_users_denied_for_non_super_admin():
    """list_users should raise 403 for non-super-admin users.

    The require_super_admin check is done via Depends, so we simulate
    by verifying that list_users raises when called with a non-super-admin token.
    """
    from enterprise_ai_platform.ai_gateway_service.src.router_admin import require_super_admin

    mock_token = MagicMock()
    mock_token.roles = ["end_user"]

    with pytest.raises(HTTPException) as exc_info:
        require_super_admin(mock_token)

    assert exc_info.value.status_code == 403


def test_assign_user_role_user_not_found():
    """assign_user_role should raise 404 if user does not exist."""
    from enterprise_ai_platform.ai_gateway_service.src.router_admin import assign_user_role

    async def mock_execute_returns_none(query, *args, **kwargs):
        mock_res = MagicMock()
        mock_res.scalar_one_or_none = MagicMock(return_value=None)
        return mock_res

    mock_db = MagicMock()
    mock_db.execute = mock_execute_returns_none

    mock_token = MagicMock()
    mock_token.sub = "admin-user-id"
    mock_token.email = "admin@salesgenie.ai"
    mock_token.roles = ["super_admin"]
    mock_token.tenant_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, "default_tenant"))

    req = UpdateUserRoleRequest(role="sales_agent")

    with patch(
        "enterprise_ai_platform.ai_gateway_service.src.router_admin.require_super_admin",
        return_value=mock_token,
    ), patch(
        "enterprise_ai_platform.ai_gateway_service.src.router_admin.uuid.UUID"
    ) as mock_uuid:
        mock_uuid.return_value = uuid.uuid5(uuid.NAMESPACE_DNS, "nonexistent-uuid")
        with pytest.raises(HTTPException) as exc_info:
            _run_async(assign_user_role(
                user_id="nonexistent-uuid",
                req=req,
                current_user=mock_token,
                db=mock_db,
            ))

    assert exc_info.value.status_code == 404


def test_notification_send_role_notification():
    """send_role_notification should construct and dispatch an email notification."""
    with patch.object(
        NotificationDispatcher, "dispatch_notification", new_callable=AsyncMock
    ) as mock_dispatch:
        mock_dispatch.return_value = {"status": "sent", "channel": "email"}
        result = _run_async(send_role_notification(
            user_email="user@example.com",
            user_name="Test User",
            old_role="end_user",
            new_role="sales_agent",
            assigned_by="admin@salesgenie.ai",
        ))

    assert result["status"] == "sent"
    mock_dispatch.assert_called_once()
    call_args = mock_dispatch.call_args
    assert call_args[0][0].recipient == "user@example.com"
    assert call_args[0][0].channel == "email"
    assert "Sales Agent" in call_args[0][0].subject
    assert call_args[0][0].metadata["old_role"] == "end_user"
    assert call_args[0][0].metadata["new_role"] == "sales_agent"


def test_notification_dispatcher_returns_sent_status():
    """NotificationDispatcher.dispatch_notification should return expected status."""
    req = type("Req", (), {
        "recipient": "test@example.com",
        "channel": "email",
        "subject": "Test",
        "body": "Hello",
        "metadata": None,
    })()

    result = _run_async(NotificationDispatcher.dispatch_notification(req))

    assert result["status"] == "sent"
    assert result["channel"] == "email"
    assert result["recipient"] == "test@example.com"
