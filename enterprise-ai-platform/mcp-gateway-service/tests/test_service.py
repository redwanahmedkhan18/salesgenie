"""
Test suite for MCP Gateway Service business logic.
Tests tool registration, execution, audit logging, and statistics.
"""

import pytest
import uuid
from datetime import datetime, timezone
from unittest.mock import MagicMock, AsyncMock, patch


@pytest.fixture
def mock_current_user():
    """Mock authenticated user token payload with knowledge_manager role."""
    return MagicMock(
        sub=str(uuid.uuid4()),
        tenant_id="salesgenie-tenant",
        email="manager@salesgenie.ai",
        roles=["knowledge_manager"],
        permissions=["knowledge:read", "knowledge:write", "mcp:execute"],
        exp=int(datetime.now(timezone.utc).timestamp()) + 3600,
    )


@pytest.fixture
def mock_current_user_no_perms():
    """Mock user without registration permissions."""
    return MagicMock(
        sub=str(uuid.uuid4()),
        tenant_id="salesgenie-tenant",
        email="agent@salesgenie.ai",
        roles=["support_agent"],
        permissions=["mcp:execute"],
        exp=int(datetime.now(timezone.utc).timestamp()) + 3600,
    )


@pytest.fixture
def mock_db_session():
    """Mock async database session."""
    session = AsyncMock()
    session.commit = AsyncMock()
    session.rollback = AsyncMock()
    session.close = AsyncMock()
    session.execute = AsyncMock()
    session.add = MagicMock()
    session.flush = AsyncMock()
    session.refresh = AsyncMock()
    return session


class TestMCPModels:
    """Test MCP gateway models."""

    def test_mcp_tool_registration(self):
        from enterprise_ai_platform.mcp_gateway_service.src.models import MCPToolRegistration
        req = MCPToolRegistration(
            name="web_search",
            description="Search the web for information",
            category="search",
            server_url="http://localhost:9000/sse",
            server_name="web-search-server",
        )
        assert req.name == "web_search"
        assert req.category == "search"
        assert req.enabled is True
        assert req.timeout_seconds == 30

    def test_mcp_tool_registration_defaults(self):
        from enterprise_ai_platform.mcp_gateway_service.src.models import MCPToolRegistration
        req = MCPToolRegistration(
            name="test_tool",
            description="Test tool",
            server_url="http://localhost:9000",
            server_name="test-server",
        )
        assert req.visibility == "tenant"
        assert req.category == "custom"
        assert req.timeout_seconds == 30

    def test_mcp_tool_call_request(self):
        from enterprise_ai_platform.mcp_gateway_service.src.models import MCPToolCallRequest
        req = MCPToolCallRequest(
            tool_id=str(uuid.uuid4()),
            arguments={"query": "salesgenie ai platform"},
        )
        assert req.arguments == {"query": "salesgenie ai platform"}

    def test_mcp_tool_call_result(self):
        from enterprise_ai_platform.mcp_gateway_service.src.models import MCPToolCallResult
        result = MCPToolCallResult(
            tool_id="tool-1",
            tool_name="web_search",
            success=True,
            result={"results": ["item1", "item2"]},
            latency_ms=150.5,
            executed_at=datetime.now(timezone.utc),
            request_id="req-123",
        )
        assert result.success is True
        assert result.tool_name == "web_search"

    def test_mcp_tool_stats_dto(self):
        from enterprise_ai_platform.mcp_gateway_service.src.models import MCPToolStatsDTO
        stats = MCPToolStatsDTO(
            tool_id="tool-1",
            tool_name="web_search",
            category="search",
            execution_count=100,
            success_count=95,
            error_count=5,
            success_rate=95.0,
            avg_latency_ms=120.5,
            p99_latency_ms=500.0,
            last_used_at=None,
            most_common_error="Timeout error",
        )
        assert stats.execution_count == 100
        assert stats.success_rate == 95.0


class TestMCPRouter:
    """Test MCP gateway API router endpoints."""

    @pytest.fixture
    def router(self):
        from enterprise_ai_platform.mcp_gateway_service.src.router_mcp import router
        return router

    def test_router_prefix(self, router):
        assert router.prefix == "/api/v1/mcp"

    def test_router_has_tool_management_endpoints(self, router):
        route_paths = [r.path for r in router.routes if hasattr(r, "path")]
        assert "/api/v1/mcp/tools" in route_paths  # POST (register) + GET (list)
        assert "/api/v1/mcp/tools/{tool_id}" in route_paths  # GET, PATCH, DELETE

    def test_router_has_execution_endpoints(self, router):
        route_paths = [r.path for r in router.routes if hasattr(r, "path")]
        assert "/api/v1/mcp/tools/{tool_id}/execute" in route_paths
        assert "/api/v1/mcp/execute" in route_paths

    def test_router_has_audit_endpoints(self, router):
        route_paths = [r.path for r in router.routes if hasattr(r, "path")]
        assert "/api/v1/mcp/logs" in route_paths
        assert "/api/v1/mcp/stats" in route_paths

    def test_register_tool_callable(self, router):
        from enterprise_ai_platform.mcp_gateway_service.src.router_mcp import register_tool
        assert callable(register_tool)

    def test_list_tools_callable(self, router):
        from enterprise_ai_platform.mcp_gateway_service.src.router_mcp import list_tools
        assert callable(list_tools)

    def test_execute_tool_callable(self, router):
        from enterprise_ai_platform.mcp_gateway_service.src.router_mcp import execute_tool
        assert callable(execute_tool)

    def test_get_tool_stats_callable(self, router):
        from enterprise_ai_platform.mcp_gateway_service.src.router_mcp import get_tool_stats
        assert callable(get_tool_stats)


class TestMCPEnums:
    """Test MCP gateway enum values."""

    def test_tool_visibility_values(self):
        from enterprise_ai_platform.mcp_gateway_service.src.models import ToolVisibility
        assert ToolVisibility.PUBLIC == "public"
        assert ToolVisibility.TENANT == "tenant"
        assert ToolVisibility.ROLE == "role"
        assert ToolVisibility.PRIVATE == "private"

    def test_tool_category_values(self):
        from enterprise_ai_platform.mcp_gateway_service.src.models import ToolCategory
        assert ToolCategory.SEARCH == "search"
        assert ToolCategory.RESEARCH == "research"
        assert ToolCategory.CRM == "crm"
        assert ToolCategory.COMMUNICATION == "communication"
        assert ToolCategory.DATA_ENRICHMENT == "data_enrichment"
        assert ToolCategory.ANALYTICS == "analytics"
        assert ToolCategory.DATABASE == "database"
        assert ToolCategory.FILE == "file"
        assert ToolCategory.WEBHOOK == "webhook"
        assert ToolCategory.CUSTOM == "custom"

    def test_tool_status_values(self):
        from enterprise_ai_platform.mcp_gateway_service.src.models import ToolStatus
        assert ToolStatus.ACTIVE == "active"
        assert ToolStatus.DISABLED == "disabled"
        assert ToolStatus.ERROR == "error"


class TestProductIntelligenceTenantIsolation:
    """Test tenant isolation logic in MCP gateway."""

    def test_get_tenant_uuid(self, mock_current_user):
        from enterprise_ai_platform.mcp_gateway_service.src.router_mcp import _get_tenant_uuid
        result = _get_tenant_uuid(mock_current_user)
        assert isinstance(result, uuid.UUID)

    def test_tool_to_dto(self, mock_current_user):
        from enterprise_ai_platform.mcp_gateway_service.src.router_mcp import MCPTool, _tool_to_dto

        tenant_uuid = uuid.uuid4()
        tool = MCPTool(
            id=uuid.uuid4(),
            tenant_id=tenant_uuid,
            name="web_search",
            description="Search the web",
            category="search",
            server_name="search-server",
            server_url="http://localhost:9000",
            visibility="tenant",
            timeout_seconds=30,
            enabled=True,
            status="active",
            execution_count=5,
            total_errors=0,
            avg_latency_ms=120.5,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        dto = _tool_to_dto(tool)
        assert dto.name == "web_search"
        assert dto.api_key_configured is False
        assert dto.enabled is True
        assert dto.tenant_id == str(tenant_uuid)
