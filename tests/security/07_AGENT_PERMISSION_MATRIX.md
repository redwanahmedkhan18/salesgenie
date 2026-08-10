# SalesGenie Agent Permission Matrix

## Agent Permission Model

```
Agent → Role → Permissions → Authorized Actions
```

## Agent Types and Permissions

| Agent Type | Role | Can Execute Tools | Can Access Data | Max Steps | Requires Approval |
|---|---|---|---|---|---|
| Sales Representative | sales_agent | ✅ Internal tools only | Own tenant data | 20 | For deals > $10k |
| Support Agent | support_agent | ✅ Ticket tools only | Own tenant tickets | 15 | For refunds |
| HR Assistant | knowledge_manager | ✅ Knowledge search only | Tenant knowledge base | 10 | No |
| Booking Agent | sales_agent | ✅ Calendar tools only | Scheduling data | 10 | No |
| Refund Agent | support_agent | ✅ Refund tools only | Transaction data | 10 | ✅ Yes, always |
| Super Admin Agent | super_admin | ✅ All tools | All tenant data | 50 | For destructive actions |

## Permission-to-Action Mapping

| Permission | Actions Allowed | Approval Required |
|---|---|---|
| `agent:execute` | Run AI agent workflows | No |
| `agent:execute:dangerous` | Run agents with external actions | ✅ Yes |
| `knowledge:read` | Retrieve documents from knowledge base | No |
| `knowledge:write` | Add documents to knowledge base | ✅ For sensitive docs |
| `leads:read` | View leads for own tenant | No |
| `leads:write` | Create/update leads | No |
| `deals:manage` | Manage deals/pipeline | ✅ For large deals |
| `ticket:read` | View support tickets | No |
| `ticket:write` | Respond to tickets | No |
| `ticket:assign` | Assign tickets to agents | ✅ For escalation |
| `analytics:read` | View analytics dashboards | No |
| `analytics:export` | Export data reports | ✅ For bulk exports |
| `billing:read` | View billing info | No |
| `billing:charge` | Process payments | ✅ Always |
| `workflow:manage` | Create/edit workflows | ✅ For production |
| `org:read` | View org settings | No |
| `org:write` | Modify org settings | ✅ Always |
| `user:manage` | Manage users/roles | ✅ Always |
| `system:audit:read` | Read audit logs | ✅ Always |

## Agent Execution Constraints

### Maximum Limits (Server-Side)
| Constraint | Default | Enforced By |
|---|---|---|
| Max tool calls per session | 10 | `auth-middleware.ts` |
| Max agent steps | 20 | Agent orchestrator |
| Max execution time | 300s | Timeout middleware |
| Max token budget | 100k | Token counter |
| Max financial actions | $0 (unless approved) | Approval workflow |
| Max external API calls | 50 | Rate limiter |

### Authorization Re-evaluation
- **Before each high-risk action:** Re-check `requirePermission()` and tenant membership
- **After session expiration:** Stop agent, require re-authentication
- **After authorization revocation:** Terminate agent immediately

## Agent Attack Vectors (Defended Against)

| Attack | Scenario | Defense |
|---|---|---|
| Tool chaining escalation | Low-permission tools chained to high-risk action | Each tool call re-checks permissions |
| Stale credential abuse | Agent continues after token expires | JWT expiration enforced on every call |
| Cross-tenant actions | Agent accesses another tenant's data | Tenant_id from JWT, not client |
| Approval bypass | Agent skips approval for expensive actions | Server-side approval required for financial/destructive actions |
| Infinite loop | Agent recursively calls tools | Step limit, token budget, timeout |
| Cost explosion | Agent makes unlimited API calls | Rate limiting, budget limits |
| Data exfiltration | Agent exports all data | Export authorization check, audit logging |

## Agent Safety Flow

```
Agent Session Start
        ↓
Extract JWT → Validate → Extract tenant_id + roles + permissions
        ↓
Initialize Budget (tokens, steps, cost)
        ↓
Tool Call Requested
        ↓
requirePermission(tool.permission)  ← Server-side check
        ↓
Tenant Membership Verified          ← From JWT, not client
        ↓
Budget Check (steps, tokens, cost)   ← Server-side counter
        ↓
Rate Limit Check                     ← Per IP/tenant/tool
        ↓
Execute Tool (with timeout)
        ↓
Output Treated as DATA (not instructions)
        ↓
Audit Log Entry
        ↓
Return to Agent
        ↓
[Repeat until budget exhausted or done]
```
