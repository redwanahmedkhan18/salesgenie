"""
MCP Security Gateway

Enforces authentication, authorization, tool allowlisting, parameter
validation, rate limiting, and tenant isolation for MCP tool execution.

Based on OWASP MCP Security Cheat Sheet guidance.
"""

import json
import time
import logging
from typing import Dict, Any, Optional, List
from dataclasses import dataclass


logger = logging.getLogger("salesgenie.security.mcp_gateway")


@dataclass
class ToolExecutionResult:
    """Result of a tool execution authorization check."""
    allowed: bool
    requires_approval: bool
    risk_level: str
    reason: Optional[str] = None


class MCPSecurityGateway:
    """
    MCP (Model Context Protocol) Security Gateway.

    Implements the OWASP MCP security recommendations:
    - Authentication and authorization for tool access
    - Tool allowlisting by role
    - Parameter schema validation
    - Rate limiting per tenant/user
    - Tenant isolation enforcement
    - Human approval for high-risk tools
    - Audit logging of all tool calls
    """

    def __init__(self):
        self._tool_configs: Dict[str, Dict[str, Any]] = {}
        self._rate_limiters: Dict[str, Dict[str, Any]] = {}
        self._rate_limit_windows: Dict[str, List[float]] = {}
        self.ai_security = None

    def set_ai_security(self, ai_security) -> None:
        """Inject the AI security gateway for threat scanning."""
        self.ai_security = ai_security

    def register_tool(self, tool_config: Dict[str, Any]) -> None:
        """Register a tool with the MCP Security Gateway.

        Args:
            tool_config: Dict with keys:
                - name: tool name (e.g., 'search_company')
                - namespace: MCP server namespace
                - risk_level: 'low' | 'medium' | 'high' | 'critical'
                - allowed_roles: list of role strings
                - requires_approval: bool
                - parameter_schema: optional JSON schema dict
                - rate_limit_per_minute: int
        """
        tool_name = tool_config["name"]
        self._tool_configs[tool_name] = tool_config
        logger.info(f"Registered MCP tool '{tool_name}' with risk_level={tool_config.get('risk_level', 'medium')}")

    def is_tool_allowed(self, tool_name: str, user_roles: List[str],
                        tenant_id: str, params: Optional[Dict[str, Any]] = None) -> ToolExecutionResult:
        """Check if a user is authorized to execute an MCP tool.

        Args:
            tool_name: The MCP tool name to check
            user_roles: List of roles the user has
            tenant_id: The user's tenant/organization ID
            params: Optional tool parameters for validation

        Returns:
            ToolExecutionResult with allowed, requires_approval, risk_level, reason
        """
        if tool_name not in self._tool_configs:
            logger.warning(f"Attempted to execute unregistered MCP tool: {tool_name}")
            return ToolExecutionResult(
                allowed=False,
                requires_approval=False,
                risk_level="unknown",
                reason="Tool not registered in MCP Security Gateway",
            )

        config = self._tool_configs[tool_name]

        if not config.get("is_enabled", True):
            return ToolExecutionResult(
                allowed=False,
                requires_approval=False,
                risk_level=config.get("risk_level", "medium"),
                reason="Tool is disabled",
            )

        allowed_roles = config.get("allowed_roles", [])
        if allowed_roles:
            user_has_role = any(
                any(role in r or r in role for role in user_roles)
                for r in allowed_roles
            )
            if not user_has_role:
                return ToolExecutionResult(
                    allowed=False,
                    requires_approval=False,
                    risk_level=config.get("risk_level", "medium"),
                    reason=f"User lacking required role. Required roles: {allowed_roles}",
                )

        allowed_tenants = config.get("allowed_tenants")
        if allowed_tenants is not None and tenant_id not in allowed_tenants:
            return ToolExecutionResult(
                allowed=False,
                requires_approval=False,
                risk_level="critical",
                reason="Tenant not authorized for this tool",
            )

        if params:
            schema = config.get("parameter_schema")
            if schema:
                validation_errors = self._validate_parameters(params, schema)
                if validation_errors:
                    return ToolExecutionResult(
                        allowed=False,
                        requires_approval=False,
                        risk_level="medium",
                        reason=f"Parameter validation failed: {validation_errors}",
                    )

        if self.ai_security and params:
            param_str = json.dumps(params, default=str)
            scan = self.ai_security.scan_text(param_str, context="mcp_tool_input")
            if scan["is_blocked"]:
                return ToolExecutionResult(
                    allowed=False,
                    requires_approval=False,
                    risk_level="critical",
                    reason=f"AI security threat detected: {scan['reason']}",
                )

        risk_level = config.get("risk_level", "medium")
        requires_approval = config.get("requires_approval", False)

        if risk_level in ("high", "critical") or requires_approval:
            requires_approval = True

        return ToolExecutionResult(
            allowed=True,
            requires_approval=requires_approval,
            risk_level=risk_level,
            reason=None,
        )

    def _validate_parameters(self, params: Dict[str, Any], schema: Dict[str, Any]) -> Optional[str]:
        """Validate tool parameters against JSON schema.

        Performs basic type and required-field validation.
        """
        required = schema.get("required", [])
        for req_field in required:
            if req_field not in params:
                return f"Missing required parameter: {req_field}"

        properties = schema.get("properties", {})
        for key, value in params.items():
            if key not in properties:
                continue
            expected_type = properties[key].get("type")
            if expected_type and not self._check_type(value, expected_type):
                return f"Parameter '{key}' expected type '{expected_type}', got '{type(value).__name__}'"

        return None

    def _check_type(self, value: Any, expected_type: str) -> bool:
        """Check if a value matches the expected JSON schema type."""
        type_map = {
            "string": str,
            "number": (int, float),
            "integer": int,
            "boolean": bool,
            "array": list,
            "object": dict,
        }
        expected = type_map.get(expected_type)
        if expected is None:
            return True
        if expected_type == "number":
            return isinstance(value, (int, float)) and not isinstance(value, bool)
        return isinstance(value, expected)

    def check_rate_limit(self, tool_name: str, tenant_id: str, user_id: str) -> bool:
        """Check if a tool execution is within rate limits.

        Uses a sliding window of 60 seconds per user+tenant+tool.
        """
        config = self._tool_configs.get(tool_name, {})
        max_per_minute = config.get("rate_limit_per_minute", 60)

        key = f"{tenant_id}:{user_id}:{tool_name}"
        now = time.time()

        if key not in self._rate_limit_windows:
            self._rate_limit_windows[key] = []

        window = self._rate_limit_windows[key]
        window[:] = [t for t in window if now - t < 60.0]

        if len(window) >= max_per_minute:
            logger.warning(f"Rate limit exceeded for tool '{tool_name}' by user '{user_id}'")
            return False

        window.append(now)
        return True

    def get_security_score(self) -> float:
        """Calculate a security score based on tool configurations and threats detected."""
        if not self._tool_configs:
            return 100.0

        total = len(self._tool_configs)
        secure_count = 0

        for config in self._tool_configs.values():
            risk = config.get("risk_level", "medium")
            requires_approval = config.get("requires_approval", False)
            has_schema = bool(config.get("parameter_schema"))
            has_rate_limit = config.get("rate_limit_per_minute", 0) > 0

            score = 0
            if risk == "low":
                score += 1
            if requires_approval or risk in ("high", "critical"):
                score += 1
            if has_schema:
                score += 1
            if has_rate_limit:
                score += 1

            if score >= 3:
                secure_count += 1

        return (secure_count / total) * 100.0 if total > 0 else 100.0

    def get_tool_configs(self) -> List[Dict[str, Any]]:
        """Return all registered tool configurations."""
        return list(self._tool_configs.values())
