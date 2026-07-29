"""
Test Configuration
Shared pytest fixtures and configuration for audit service tests.
"""

import pytest
import asyncio
from unittest.mock import AsyncMock, MagicMock


@pytest.fixture
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def mock_db_session():
    session = AsyncMock()
    session.commit = AsyncMock()
    session.rollback = AsyncMock()
    session.close = AsyncMock()
    session.execute = AsyncMock()
    session.add = MagicMock()
    session.flush = AsyncMock()
    session.refresh = AsyncMock()
    return session


@pytest.fixture
def mock_current_user():
    return MagicMock(
        sub="123e4567-e89b-12d3-a456-426614174000",
        tenant_id="salesgenie-tenant",
        email="test@salesgenie.ai",
        roles=["admin"],
        permissions=["audit:read", "audit:write"],
    )