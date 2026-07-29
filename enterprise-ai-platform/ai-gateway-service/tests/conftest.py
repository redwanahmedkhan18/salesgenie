import pytest
import uuid
from datetime import datetime, timezone
from unittest.mock import MagicMock, AsyncMock


@pytest.fixture
def event_loop():
    """Create an event loop for async tests."""
    import asyncio
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def mock_db_session():
    """Create a mock database session for async tests."""
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
    """Create a mock current user for tests."""
    user = MagicMock()
    user.sub = str(uuid.uuid4())
    user.tenant_id = "test-tenant"
    user.email = "test@example.com"
    user.roles = ["admin"]
    user.permissions = ["full_access"]
    return user
