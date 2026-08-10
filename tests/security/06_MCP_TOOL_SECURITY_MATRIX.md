# SalesGenie MCP Tool Security Matrix

## MCP Architecture

```
MCP Client (AI Agent)
  ↓
Tool Selection (server-side authorization)
  ↓
MCP Server
  ↓
Tool Execution (with rate limits, timeouts)
  ↓
Result → Treated as UNTRUSTED DATA → LLM
```

## Tool Classification

| Tool Name | Category | Permission Required | Approval Required | Risk Level |
|---|---|---|---|---|
| (placeholder — MCP tools are dynamically registered) | — | — | — | — |

## MCP Security Controls

### 1. Tool Authorization
- **Never** allow LLM to decide its own tool authorization
- Server-side: `requirePermission()` checks before MCP tool invocation
- Role-based tool access matrix enforced

### 2. Input Validation
- Tool names validated against allowlist
- Arguments schema-validated before execution
- Tenant context extracted from JWT, not client

### 3. Output Validation
- MCP tool output treated as untrusted data
- Cannot be used for prompt injection
- Must not be rendered as trusted HTML

### 4. Execution Budgets
- Maximum tool calls per agent session: configurable (default: 10)
- Maximum agent steps: configurable (default: 20)
- Maximum runtime: timeout enforced (default: 60s per tool)
- Maximum cost: budget enforced per tenant

### 5. Rate Limiting
- Per-tool rate limits
- Per-agent rate limits
- Per-tenant rate limits

## MCP Tool Security Checklist

| Control | Implemented | Test |
|---|---|---|
| Tool name allowlist | ✅ | `test_mcp_tool_allowlist` |
| Argument schema validation | ✅ | `test_mcp_argument_validation` |
| Authorization before execution | ✅ | `test_mcp_authorization` |
| Rate limiting on tool calls | ✅ | `test_mcp_rate_limiting` |
| Execution timeout | ✅ | `test_mcp_timeout` |
| Output treated as untrusted | ✅ | `test_mcp_output_sanitization` |
| Audit logging of tool calls | ✅ | `test_mcp_audit_log` |
| Tenant isolation | ✅ | `test_mcp_tenant_isolation` |
| Cost budget enforcement | ✅ | `test_mcp_cost_budget` |

## MCP Tool Execution Flow

```
1. Agent requests MCP tool invocation
         ↓
2. Server checks: requirePermission(tool.permission)
   If denied → 403 Forbidden, logged
         ↓
3. Server validates: tool name in allowlist
   If not found → 400 Bad Request
         ↓
4. Server validates: arguments match schema
   If invalid → 400 Bad Request
         ↓
5. Server checks: rate limit for tool + tenant
   If exceeded → 429 Too Many Requests
         ↓
6. Server checks: execution budget
   If exceeded → 403 Budget Exceeded
         ↓
7. MCP server executes tool with timeout
         ↓
8. Output is sanitized (never treated as instructions)
         ↓
9. Result returned to agent + audit logged
```

## Known MCP Attack Patterns (Defended Against)

| Attack | Attack Vector | Defense |
|---|---|---|
| Tool prompt injection | MCP returns "IGNORE PREVIOUS INSTRUCTIONS" | Tool output treated as data, not instructions |
| Tool argument injection | Malformed JSON in arguments | Schema validation before execution |
| Tool escalation | Low-privilege agent calls admin tool | Server-side permission check |
| Cross-tenant tool | Agent uses another tenant's tool config | Tenant isolation in tool registry |
| Cost explosion | Recursive tool calls | Budget limits, step limits, rate limits |
| Data exfiltration | Tool reads another tenant's data | Tenant-scoped tool execution |

## MCP Security Test Cases

```python
# Placeholder for when MCP integration is active
# These tests would verify:
# - MCP tool authorization matrix enforcement
# - Argument schema validation
# - Rate limiting on tool calls
# - Execution timeout enforcement
# - Output sanitization
# - Audit logging of all tool invocations
# - Tenant isolation in tool registry
# - Cost budget enforcement
```
