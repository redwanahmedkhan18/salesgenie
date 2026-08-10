"""
Test Configuration
Shared pytest fixtures and configuration for MCP gateway service tests.
"""

import pytest
import asyncio
import uuid
from datetime import datetime, timezone
from unittest.mock import AsyncMock, MagicMock


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
        sub=str(uuid.uuid4()),
        tenant_id="salesgenie-tenant",
        email="manager@salesgenie.ai",
        roles=["knowledge_manager"],
        permissions=["knowledge:read", "knowledge:write", "mcp:execute"],
        exp=int(datetime.now(timezone.utc).timestamp()) + 3600,
    )
