# SalesGenie — Plan Limits Requirements

**Document:** `plan_limits.md`  
**Product:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Requirement Level:** FAANG-Level / Production-Grade  
**Scope:** Plan limit definition, entitlement enforcement, quota management, usage metering, AI/human capacity management, soft/hard limits, overages, alerts, enforcement, forecasting, governance, and administration  
**Actors:** End Users, Sales Agents, Support Agents, Organization Admins, Billing Admins, Super Admins, AI Agents, Human Operators, Billing Service, Entitlement Service, Usage Metering Service, Policy Engine, Workflow Engine, MCP Platform, Integration Platform

---

## 1. Purpose

The Plan Limits module defines how SalesGenie controls, measures, exposes, and enforces resource limits associated with subscription plans.

The system SHALL support limits for:

- Users
- Human-agent seats
- AI agents
- AI conversations
- AI messages
- AI tokens
- LLM requests
- Voice minutes
- Workflow executions
- MCP tool executions
- API requests
- Lead generation
- Lead enrichment
- RAG storage
- Knowledge-base documents
- File storage
- Integrations
- Webhook events
- Automation executions
- Campaigns
- Contacts
- CRM records
- Concurrent sessions
- Concurrent AI conversations
- Concurrent workflows
- Model usage
- Compute-intensive operations
- Billing-related resources

The module MUST support both **AI-operated** and **human-operated** workflows.

---

## 2. Product Context

SalesGenie is a multi-tenant enterprise AI platform supporting:

- AI customer support
- AI sales agents
- Human customer support
- Human sales teams
- Multi-agent orchestration
- RAG knowledge management
- Lead generation
- Lead intelligence
- Omnichannel communication
- Workflow automation
- MCP tools
- Third-party integrations
- AI voice
- Analytics
- CRM automation
- Document intelligence

Plan limits SHALL provide the control layer between purchased subscription entitlements and actual platform consumption.

---

## 3. Core Principle

The system SHALL distinguish between:

```text
Plan
  ↓
Entitlement
  ↓
Limit Policy
  ↓
Usage Meter
  ↓
Enforcement Decision
  ↓
Platform Access
```

The system MUST NOT treat frontend UI restrictions as authoritative limits.

All enforceable limits MUST be evaluated server-side.

---

## 4. Limit Types

SalesGenie SHALL support the following limit classes.

## 4.1 Quantity Limits

Examples:

```text
Maximum users
Maximum AI agents
Maximum human agents
Maximum workflows
Maximum integrations
Maximum knowledge bases
```

---

## 4.2 Usage Limits

Examples:

```text
AI messages/month
AI tokens/month
Voice minutes/month
Workflow executions/month
MCP calls/month
API requests/month
Lead generation credits/month
```

---

## 4.3 Storage Limits

Examples:

```text
Total storage
RAG storage
Document storage
Knowledge-base storage
Conversation storage
```

---

## 4.4 Concurrency Limits

Examples:

```text
Concurrent conversations
Concurrent AI agents
Concurrent workflows
Concurrent API requests
Concurrent voice calls
```

---

## 4.5 Rate Limits

Examples:

```text
Requests/second
Requests/minute
Messages/minute
Workflow executions/minute
MCP calls/minute
```

---

## 4.6 Financial Limits

Examples:

```text
Maximum monthly overage
Maximum usage-based spend
Maximum credit consumption
Maximum automated billing amount
```

---

## 5. User Requirements

## UR-LIMIT-001 — Limit Visibility

Authorized users SHALL be able to view all limits applicable to their organization.

The UI SHALL display:

* Limit name
* Current usage
* Included amount
* Remaining amount
* Usage percentage
* Reset date
* Limit type
* Enforcement mode
* Overage status

---

## UR-LIMIT-002 — Clear Usage Indicators

Users SHALL be able to understand resource consumption without requiring technical knowledge.

Example:

```text
AI Messages
8,420 / 10,000 used
84.2%
1,580 remaining
Resets in 12 days
```

---

## UR-LIMIT-003 — Limit Warnings

Users SHALL receive warnings before reaching configurable limits.

Default thresholds SHOULD include:

```text
50%
75%
80%
90%
95%
100%
```

---

## UR-LIMIT-004 — Limit Exhaustion Transparency

When a limit is reached, users SHALL receive a clear explanation:

* Which resource was exhausted
* Current usage
* Allowed usage
* Reset date
* Available alternatives
* Upgrade option
* Overage option where applicable

---

## UR-LIMIT-005 — Upgrade Recommendation

When a user repeatedly approaches a limit, SalesGenie SHOULD recommend an appropriate higher-tier plan.

The recommendation SHOULD be based on:

* Historical usage
* Current usage
* Projected usage
* Required features
* Organization size
* Growth trend

---

## UR-LIMIT-006 — Human-Agent Limit Management

Authorized organization admins SHALL be able to:

* Add agents
* Remove agents
* Assign seats
* Reassign seats
* View seat utilization
* View unused seats

The system MUST prevent active seat assignments beyond purchased limits unless overage or temporary expansion is enabled.

---

## UR-LIMIT-007 — AI-Agent Limit Management

Authorized users SHALL be able to:

* Create AI agents
* Delete AI agents
* Activate/deactivate agents
* View AI-agent usage
* View AI-agent limits

The platform MUST enforce plan-specific AI-agent limits.

---

## UR-LIMIT-008 — Usage Dashboard

The platform SHALL provide a consolidated usage dashboard.

The dashboard SHOULD include:

```text
Users
Human Agents
AI Agents
AI Messages
AI Tokens
Voice Minutes
Workflows
MCP Calls
API Requests
Leads
Enrichment
Storage
Integrations
Concurrent Sessions
```

---

## UR-LIMIT-009 — Limit Forecasting

Users SHOULD be able to view projected resource exhaustion.

Example:

```text
Current usage: 82%
Average daily consumption: 2.4%
Projected exhaustion: 7 days
```

---

## UR-LIMIT-010 — Human Support

Users SHALL be able to contact human support when a limit creates an operational problem.

Support agents SHALL be able to inspect limit state without accessing unauthorized billing information.

---

## 6. System Requirements

## SR-LIMIT-001 — Centralized Limit Engine

SalesGenie SHALL provide a centralized Plan Limit Engine.

The Limit Engine SHALL be authoritative for:

* Limit definitions
* Limit policies
* Enforcement modes
* Quota state
* Limit overrides
* Limit inheritance
* Limit evaluation

---

## SR-LIMIT-002 — Tenant Isolation

Every limit SHALL be associated with a tenant.

```text
tenant_id
organization_id
subscription_id
plan_id
plan_version
```

Cross-tenant limit access MUST be impossible.

---

## SR-LIMIT-003 — Server-Side Enforcement

All limits affecting platform access MUST be enforced server-side.

Frontend checks SHALL only provide UX feedback.

---

## SR-LIMIT-004 — Versioned Limit Policies

Limit policies MUST be versioned.

Existing subscriptions SHALL retain the correct historical policy according to the applicable subscription contract.

---

## SR-LIMIT-005 — Atomic Usage Reservation

For concurrency-sensitive resources, the system SHALL support atomic reservation.

Example:

```text
Check available capacity
        ↓
Reserve capacity
        ↓
Execute operation
        ↓
Commit usage
        ↓
Release unused reservation
```

---

## SR-LIMIT-006 — Idempotent Usage Accounting

Usage events SHALL support idempotency.

Duplicate usage events MUST NOT cause double charging or double consumption.

---

## SR-LIMIT-007 — Event-Driven Usage Architecture

Usage SHOULD be propagated through durable events.

Example:

```text
AI Request
   ↓
Usage Event
   ↓
Usage Meter
   ↓
Limit Engine
   ↓
Billing Ledger
   ↓
Analytics
```

---

## SR-LIMIT-008 — Strong Consistency for Critical Limits

The platform SHALL use strongly consistent enforcement for limits where exceeding the limit creates:

* Financial exposure
* Security risk
* Resource exhaustion
* Contractual violations

---

## SR-LIMIT-009 — Eventual Consistency for Analytics

Usage dashboards MAY use eventually consistent aggregates provided that authoritative enforcement remains correct.

---

## 7. Functional Requirements

## 7.1 Limit Definition

## FR-LIMIT-001

Super Admins SHALL be able to define plan limits.

Each limit SHALL include:

```text
limit_id
plan_id
plan_version
resource_key
limit_type
limit_value
unit
period
enforcement_mode
overage_policy
warning_thresholds
status
effective_from
effective_until
```

---

## FR-LIMIT-002

The system SHALL support unlimited resources.

Example:

```text
limit_value = NULL
limit_type = UNLIMITED
```

---

## FR-LIMIT-003

Unlimited resources MUST NOT be incorrectly treated as zero.

---

## 7.2 Limit Categories

## FR-LIMIT-004

The system SHALL support:

```text
COUNT
USAGE
STORAGE
RATE
CONCURRENCY
CREDIT
FINANCIAL
```

---

## 7.3 Periods

## FR-LIMIT-005

Limits SHALL support:

```text
MINUTE
HOUR
DAY
WEEK
MONTH
BILLING_PERIOD
YEAR
LIFETIME
```

---

## FR-LIMIT-006

The system SHALL support annual subscriptions with either:

### Annual Pool

```text
100,000 AI messages/year
```

### Monthly Allocation

```text
10,000 AI messages/month
```

### Hybrid Allocation

```text
10,000/month
+
20,000 annual reserve
```

---

## 7.4 Enforcement Modes

## FR-LIMIT-007

The system SHALL support:

```text
HARD_LIMIT
SOFT_LIMIT
OVERAGE
THROTTLE
QUEUE
WARN_ONLY
UNLIMITED
```

---

## FR-LIMIT-008 — Hard Limit

When a hard limit is reached:

```text
usage >= limit
```

the operation MUST be rejected.

---

## FR-LIMIT-009 — Soft Limit

When a soft limit is reached, the operation MAY continue while generating:

* Warning
* Notification
* Analytics event
* Upgrade recommendation

---

## FR-LIMIT-010 — Overage

Where overages are enabled, usage SHALL continue and generate billable usage events.

---

## FR-LIMIT-011 — Throttling

The platform SHALL be able to reduce operation frequency after rate limits are reached.

---

## FR-LIMIT-012 — Queueing

The platform SHOULD support queue-based enforcement for resource-intensive operations.

---

## 8. Default Limit Dimensions

SalesGenie SHOULD support configurable limits for the following resources.

## FR-LIMIT-013 — User Limit

```text
max_users
```

---

## FR-LIMIT-014 — Human-Agent Limit

```text
max_human_agents
```

---

## FR-LIMIT-015 — AI-Agent Limit

```text
max_ai_agents
```

---

## FR-LIMIT-016 — Conversation Limit

```text
max_conversations
```

---

## FR-LIMIT-017 — AI Message Limit

```text
ai_messages
```

---

## FR-LIMIT-018 — Token Limit

```text
input_tokens
output_tokens
total_tokens
```

---

## FR-LIMIT-019 — Voice Limit

```text
voice_minutes
voice_calls
concurrent_voice_calls
```

---

## FR-LIMIT-020 — Workflow Limit

```text
workflow_executions
active_workflows
workflow_steps
```

---

## FR-LIMIT-021 — MCP Limit

```text
mcp_tool_calls
mcp_server_connections
mcp_execution_time
```

---

## FR-LIMIT-022 — API Limit

```text
api_requests
api_requests_per_minute
api_concurrent_requests
```

---

## FR-LIMIT-023 — Lead Generation Limit

```text
lead_generation_credits
lead_enrichment_credits
company_searches
contact_searches
```

---

## FR-LIMIT-024 — RAG Limit

```text
knowledge_bases
documents
chunks
embedding_operations
rag_storage
```

---

## FR-LIMIT-025 — Storage Limit

```text
file_storage
document_storage
conversation_storage
```

---

## FR-LIMIT-026 — Integration Limit

```text
active_integrations
integration_operations
webhook_events
sync_operations
```

---

## 9. AI-Based Requirements

## AI-LIMIT-001 — AI Usage Monitoring

AI agents SHALL be able to retrieve authoritative usage information.

---

## AI-LIMIT-002 — AI Limit Explanation

The AI SHALL explain:

* Current usage
* Remaining quota
* Reset date
* Limit policy
* Overage policy

---

## AI-LIMIT-003 — AI Forecasting

AI SHOULD predict when limits will be exhausted.

Inputs MAY include:

```text
historical_usage
recent_usage
seasonality
growth_rate
active_users
active_ai_agents
workflow_volume
```

---

## AI-LIMIT-004 — AI Optimization

AI SHOULD identify opportunities to reduce resource consumption.

Examples:

```text
Use smaller LLM
Reduce unnecessary context
Cache repeated responses
Optimize RAG retrieval
Reduce workflow executions
Batch API requests
Disable unused integrations
```

---

## AI-LIMIT-005 — AI Upgrade Recommendation

AI MAY recommend a higher plan when projected usage exceeds current limits.

The recommendation MUST be based on authoritative plan and usage data.

---

## AI-LIMIT-006 — AI Guardrails

AI agents MUST NOT:

* Change limits without authorization
* Increase quotas without permission
* Disable enforcement
* Modify billing limits
* Bypass rate limits
* Consume hidden quota
* Access another tenant's usage
* Falsify usage
* Create unauthorized overage

---

## 10. Human-Based Requirements

## HUMAN-LIMIT-001 — Admin Limit Dashboard

Organization admins SHALL have access to:

```text
Current Plan
Limit Configuration
Current Usage
Remaining Capacity
Projected Usage
Alerts
Overages
Overrides
```

---

## HUMAN-LIMIT-002 — Super Admin Configuration

Super Admins SHALL be able to configure limits globally.

---

## HUMAN-LIMIT-003 — Temporary Overrides

Authorized Super Admins MAY create temporary limit overrides.

Each override SHALL include:

```text
override_id
tenant_id
limit_id
previous_value
new_value
reason
created_by
approved_by
start_time
end_time
```

---

## HUMAN-LIMIT-004 — Override Expiration

Temporary overrides MUST expire automatically.

---

## HUMAN-LIMIT-005 — Approval Workflow

High-risk limit overrides SHOULD require dual approval.

```text
Operator
   ↓
Override Request
   ↓
Approver
   ↓
Policy Validation
   ↓
Activation
```

---

## 11. Limit Evaluation Engine

## FR-LIMIT-027

Every limit-sensitive operation SHALL pass through the Limit Evaluation Engine where applicable.

```text
Request
  ↓
Authentication
  ↓
Authorization
  ↓
Tenant Resolution
  ↓
Plan Resolution
  ↓
Entitlement Resolution
  ↓
Limit Evaluation
  ↓
Usage Reservation
  ↓
Operation
  ↓
Usage Commit
```

---

## FR-LIMIT-028

The engine SHALL return a deterministic decision.

Example:

```json
{
  "allowed": true,
  "resource": "ai_messages",
  "limit": 10000,
  "used": 8420,
  "remaining": 1580,
  "enforcement": "HARD_LIMIT"
}
```

---

## 12. Pre-Flight Limit Checks

## FR-LIMIT-029

The platform SHOULD support pre-flight checks before expensive operations.

Examples:

```text
Can I execute this workflow?
Can I call this MCP tool?
Can I generate this lead?
Can I process this document?
Can I initiate this voice call?
Can I create another AI agent?
```

---

## FR-LIMIT-030

Pre-flight checks MUST NOT replace authoritative post-operation accounting.

---

## 13. Usage Accounting

## FR-LIMIT-031

Every billable or quota-consuming action SHALL generate a usage event.

Example:

```text
usage_event_id
tenant_id
subscription_id
resource_key
quantity
unit
source_service
actor_type
actor_id
workflow_id
agent_id
integration_id
timestamp
request_id
idempotency_key
```

---

## FR-LIMIT-032

Usage events SHALL be immutable.

---

## FR-LIMIT-033

Usage events MUST be traceable to the originating operation.

---

## 14. Concurrency Limits

## FR-LIMIT-034

The system SHALL support concurrent-resource limits.

Examples:

```text
max_concurrent_ai_conversations
max_concurrent_voice_calls
max_concurrent_workflows
max_concurrent_api_requests
```

---

## FR-LIMIT-035

Concurrency reservations SHALL have expiration protection.

If a worker crashes, reservations MUST eventually be released.

---

## 15. Rate Limiting

## FR-LIMIT-036

The system SHALL support configurable rate limits.

Example:

```text
100 API requests/minute
20 MCP calls/minute
50 workflow executions/minute
```

---

## FR-LIMIT-037

Rate limiting SHOULD use distributed infrastructure for horizontally scaled services.

---

## 16. Storage Limits

## FR-LIMIT-038

Storage usage SHALL be calculated from authoritative storage metadata.

---

## FR-LIMIT-039

Storage limits SHALL support:

```text
warning
soft_limit
hard_limit
overage
```

---

## FR-LIMIT-040

The system MUST prevent storage writes when a hard storage limit is reached.

---

## 17. AI Token Limits

## FR-LIMIT-041

AI usage SHALL track:

```text
input_tokens
output_tokens
cached_tokens
reasoning_tokens
total_tokens
```

where supported by the model provider.

---

## FR-LIMIT-042

Token usage MUST be associated with:

```text
tenant_id
agent_id
model
provider
request_id
workflow_id
```

---

## FR-LIMIT-043

The system SHOULD support model-specific cost and quota policies.

---

## 18. Workflow Limits

## FR-LIMIT-044

Workflow execution SHALL check limits before execution.

---

## FR-LIMIT-045

Long-running workflows SHALL maintain usage reservations where required.

---

## FR-LIMIT-046

Failed workflow executions SHALL follow configurable consumption policies.

Example:

```text
COUNT_ALL_ATTEMPTS
COUNT_SUCCESS_ONLY
COUNT_STARTED
COUNT_BILLABLE_STEPS
```

---

## 19. MCP Limits

## FR-LIMIT-047

MCP tool execution SHALL enforce:

* Tool-call quotas
* Rate limits
* Concurrent-call limits
* Server connection limits
* Execution-time limits

---

## FR-LIMIT-048

Unauthorized MCP calls MUST be rejected before tool execution.

---

## 20. Lead Generation Limits

## FR-LIMIT-049

Lead-generation operations SHALL consume the appropriate quota.

Examples:

```text
company_search
contact_search
lead_generation
lead_enrichment
email_discovery
intent_analysis
```

---

## FR-LIMIT-050

Lead-generation quotas SHALL be tenant-scoped.

---

## 21. Integration Limits

## FR-LIMIT-051

Integration operations SHALL support configurable limits.

Examples:

```text
Gmail operations
Salesforce operations
HubSpot operations
Slack operations
Zendesk operations
Jira operations
Notion operations
Google Drive operations
Microsoft Teams operations
```

---

## FR-LIMIT-052

Each integration SHOULD support:

```text
requests/minute
operations/month
concurrent_operations
sync_records
webhook_events
```

---

## 22. Soft Limit Workflow

```text
Usage
  ↓
75%
  ↓
Warning
  ↓
90%
  ↓
High Usage Alert
  ↓
95%
  ↓
Critical Alert
  ↓
100%
  ↓
Configured Enforcement
```

---

## 23. Hard Limit Workflow

```text
Request
  ↓
Limit Check
  ↓
Usage >= Limit
  ↓
Reject Request
  ↓
Return LimitExceeded
  ↓
Notify User
  ↓
Offer Upgrade / Overage
```

---

## 24. Overage Workflow

```text
Request
  ↓
Limit Check
  ↓
Quota Exhausted
  ↓
Overage Enabled?
  |
  +---- NO ----> Reject
  |
  +---- YES
          ↓
   Financial Policy Check
          ↓
   Spend Cap Check
          ↓
   Record Overage Usage
          ↓
   Continue Operation
          ↓
   Billing Ledger
          ↓
   Customer Notification
```

---

## 25. AI + Human Limit Override Workflow

```text
AI Detects Limit Problem
        ↓
AI Explains Situation
        ↓
AI Recommends Resolution
        ↓
Customer/Admin Approval
        ↓
Authorization Check
        ↓
High-Risk?
   /           \
 YES            NO
 |              |
Human Approval  Automated Policy
 |              |
 +------┬-------+
        ↓
Limit Override
        ↓
Audit Event
        ↓
Expiration Scheduler
```

---

## 26. Plan Upgrade Workflow

```text
Usage Monitoring
      ↓
Limit Approaching
      ↓
AI Recommendation
      ↓
Plan Comparison
      ↓
Customer Confirmation
      ↓
Pricing Engine
      ↓
Payment
      ↓
Subscription Update
      ↓
Entitlement Update
      ↓
Limit Update
      ↓
Usage Access Restored
```

---

## 27. Data Model Requirements

## FR-LIMIT-053 — PlanLimit

```text
PlanLimit
---------
id
plan_id
plan_version
resource_key
limit_type
limit_value
unit
period
enforcement_mode
overage_enabled
overage_rate
warning_thresholds
status
effective_from
effective_until
created_at
updated_at
```

---

## FR-LIMIT-054 — TenantLimit

```text
TenantLimit
-----------
id
tenant_id
subscription_id
plan_limit_id
effective_limit
current_usage
remaining_usage
period_start
period_end
override_id
status
```

---

## FR-LIMIT-055 — UsageEvent

```text
UsageEvent
----------
id
tenant_id
subscription_id
resource_key
quantity
unit
source_service
actor_type
actor_id
agent_id
workflow_id
integration_id
request_id
idempotency_key
timestamp
```

---

## FR-LIMIT-056 — LimitOverride

```text
LimitOverride
-------------
id
tenant_id
limit_id
previous_value
new_value
reason
requested_by
approved_by
created_at
starts_at
expires_at
status
```

---

## FR-LIMIT-057 — LimitAlert

```text
LimitAlert
----------
id
tenant_id
limit_id
threshold
usage
limit_value
notification_channel
sent_at
acknowledged_at
status
```

---

## 28. API Requirements

## FR-LIMIT-058

The platform SHALL provide APIs including:

```http
GET    /api/v1/billing/limits
GET    /api/v1/billing/limits/{limit_id}
GET    /api/v1/billing/usage
GET    /api/v1/billing/usage/{resource_key}
POST   /api/v1/billing/limits/check
POST   /api/v1/billing/usage/events
GET    /api/v1/billing/limits/alerts
GET    /api/v1/billing/limits/forecast
POST   /api/v1/admin/limits/overrides
PATCH  /api/v1/admin/limits/overrides/{override_id}
DELETE /api/v1/admin/limits/overrides/{override_id}
```

---

## 29. Error Requirements

The API SHALL return deterministic error codes.

Examples:

```text
LIMIT_EXCEEDED
QUOTA_EXHAUSTED
RATE_LIMIT_EXCEEDED
CONCURRENCY_LIMIT_EXCEEDED
STORAGE_LIMIT_EXCEEDED
OVERAGE_NOT_ALLOWED
SPEND_CAP_EXCEEDED
RESOURCE_NOT_ENTITLED
PLAN_LIMIT_NOT_FOUND
LIMIT_POLICY_INVALID
LIMIT_OVERRIDE_NOT_AUTHORIZED
```

---

## 30. Security Requirements

## SEC-LIMIT-001

All limit APIs MUST require authentication.

---

## SEC-LIMIT-002

All limit modifications MUST require authorization.

---

## SEC-LIMIT-003

Users MUST NOT modify their own authoritative limits.

---

## SEC-LIMIT-004

Tenant isolation MUST be enforced at:

* API layer
* Service layer
* Database layer
* Cache layer
* Event layer

---

## SEC-LIMIT-005

Limit overrides MUST be audited.

---

## SEC-LIMIT-006

AI agents MUST operate under explicit tool permissions.

---

## SEC-LIMIT-007

Limit-related secrets MUST NOT be exposed to:

* End users
* Frontend bundles
* AI prompts
* Logs
* Analytics payloads

---

## 31. Audit Requirements

Every limit-changing operation SHALL record:

```text
actor_id
actor_type
tenant_id
action
resource_key
previous_limit
new_limit
reason
timestamp
request_id
correlation_id
approval_id
```

---

## 32. Observability Requirements

The platform SHALL expose metrics such as:

```text
plan_limit_checks_total
plan_limit_denials_total
plan_limit_warnings_total
plan_limit_overages_total
plan_limit_overrides_total
usage_events_total
usage_event_failures_total
usage_reservation_failures_total
concurrency_limit_denials_total
rate_limit_denials_total
storage_limit_denials_total
quota_exhaustion_total
```

---

## 33. Alerting Requirements

Alerts SHALL be configurable for:

* Abnormal quota consumption
* Sudden usage spikes
* Excessive limit violations
* Unexpected overages
* High financial exposure
* Usage-metering failures
* Reservation leaks
* Limit-engine failures
* Cross-service usage discrepancies
* Billing reconciliation mismatches

---

## 34. Reliability Requirements

## REL-LIMIT-001

Limit enforcement MUST remain operational during partial service failures.

---

## REL-LIMIT-002

The system SHALL define fail-open versus fail-closed behavior per resource.

Financially sensitive limits SHOULD default to fail-closed.

---

## REL-LIMIT-003

Usage events SHALL be durably persisted before being considered successfully acknowledged.

---

## REL-LIMIT-004

Failed usage events SHALL be retried.

---

## REL-LIMIT-005

The system SHALL provide dead-letter handling for permanently failed usage events.

---

## 35. Performance Requirements

## PERF-LIMIT-001

Simple limit checks SHOULD target:

```text
P95 < 100 ms
```

excluding unavoidable downstream dependencies.

---

## PERF-LIMIT-002

Distributed rate-limit checks SHOULD target:

```text
P95 < 50 ms
```

under normal production conditions.

---

## PERF-LIMIT-003

Usage aggregation MUST NOT block latency-sensitive AI requests.

---

## 36. Scalability Requirements

The system SHALL support:

* Millions of tenants
* Millions of subscriptions
* Billions of usage events
* High-volume AI requests
* High-frequency workflow executions
* Large MCP workloads
* Large integration workloads
* Horizontally scaled application services

Usage aggregation SHOULD use partitioning and pre-aggregation.

---

## 37. Caching Requirements

The system MAY cache:

* Plan definitions
* Static limit policies
* Entitlement metadata

The system MUST NOT rely on stale cache data for financial enforcement where consistency is required.

Cache invalidation SHALL occur when:

```text
Plan changes
Subscription changes
Limit changes
Override changes
Entitlement changes
```

---

## 38. Disaster Recovery

The system SHALL support recovery of:

* Plan limits
* Tenant limits
* Usage events
* Usage aggregates
* Overrides
* Alerts
* Audit records

Usage accounting MUST be reconstructable from durable events where feasible.

---

## 39. Reconciliation

The platform SHALL periodically reconcile:

```text
Plan Configuration
       ↕
Subscription
       ↕
Entitlements
       ↕
Plan Limits
       ↕
Usage Events
       ↕
Usage Aggregates
       ↕
Billing Ledger
```

The reconciliation engine SHALL detect:

* Missing usage events
* Duplicate usage
* Incorrect quotas
* Incorrect remaining balances
* Invalid overrides
* Entitlement mismatches
* Billing discrepancies

---

## 40. Limit Governance

Super Admins SHALL be able to define organizational policies for:

* Maximum override duration
* Maximum financial exposure
* Maximum overage
* Approval requirements
* Warning thresholds
* Grace periods
* Resource-specific enforcement
* Emergency shutdown

---

## 41. Emergency Controls

The system SHALL support emergency controls.

Examples:

```text
Disable all AI usage
Disable specific AI model
Disable expensive workflows
Disable MCP execution
Disable external integrations
Reduce API rate limits
Suspend overages
Suspend tenant
```

Emergency controls SHALL require appropriate authorization and SHALL be audited.

---

## 42. AI Safety Controls

AI agents SHALL NOT be able to:

```text
Increase quotas
Disable hard limits
Modify billing limits
Grant unlimited usage
Remove spend caps
Modify another tenant
Create financial exposure
```

unless an explicit authorized workflow grants the capability.

---

## 43. Human Safety Controls

Human operators SHALL NOT be able to bypass limit controls without:

* Proper RBAC
* Valid reason
* Audit trail
* Approval where required

---

## 44. Example Plan Limit Configuration

```yaml
plan:
  id: salesgenie_pro
  version: 3

limits:

  users:
    type: COUNT
    value: 25
    period: BILLING_PERIOD
    enforcement: HARD_LIMIT

  human_agents:
    type: COUNT
    value: 15
    period: BILLING_PERIOD
    enforcement: HARD_LIMIT

  ai_agents:
    type: COUNT
    value: 10
    period: BILLING_PERIOD
    enforcement: HARD_LIMIT

  ai_messages:
    type: USAGE
    value: 50000
    unit: messages
    period: MONTH
    enforcement: OVERAGE

  ai_tokens:
    type: USAGE
    value: 10000000
    unit: tokens
    period: MONTH
    enforcement: OVERAGE

  voice_minutes:
    type: USAGE
    value: 1000
    unit: minutes
    period: MONTH
    enforcement: HARD_LIMIT

  workflow_executions:
    type: USAGE
    value: 10000
    unit: executions
    period: MONTH
    enforcement: OVERAGE

  mcp_tool_calls:
    type: USAGE
    value: 25000
    unit: calls
    period: MONTH
    enforcement: HARD_LIMIT

  api_requests:
    type: RATE
    value: 100
    unit: requests_per_minute
    period: MINUTE
    enforcement: THROTTLE

  storage:
    type: STORAGE
    value: 100
    unit: GB
    period: BILLING_PERIOD
    enforcement: HARD_LIMIT
```

---

## 45. End-to-End AI Request Limit Workflow

```text
User
  ↓
AI Agent
  ↓
Authentication
  ↓
Authorization
  ↓
Tenant Resolution
  ↓
Plan Resolution
  ↓
Entitlement Resolution
  ↓
Limit Engine
  ↓
AI Token / Message Limit Check
  ↓
Quota Available?
  |
  +---- NO ----> Limit Response
  |                  ↓
  |              AI Explanation
  |                  ↓
  |          Upgrade / Overage
  |
  +---- YES
          ↓
    Reserve Usage
          ↓
      LLM Gateway
          ↓
      AI Response
          ↓
      Usage Event
          ↓
     Commit Usage
          ↓
   Billing / Analytics
```

---

## 46. Human Agent Seat Workflow

```text
Organization Admin
        ↓
Add Human Agent
        ↓
Authorization
        ↓
Seat Limit Check
        ↓
Available?
   /           \
 YES            NO
 |              |
Assign Seat     Reject
 |              |
Update Usage    Explain Limit
 |
Audit Event
```

---

## 47. Workflow Limit Workflow

```text
Workflow Request
      ↓
Authorization
      ↓
Plan Entitlement
      ↓
Workflow Limit Check
      ↓
Concurrency Check
      ↓
Reserve Execution
      ↓
Execute Workflow
      ↓
Record Usage
      ↓
Release Reservation
      ↓
Analytics
```

---

## 48. MCP Limit Workflow

```text
AI Agent
   ↓
MCP Tool Request
   ↓
Authorization
   ↓
MCP Entitlement
   ↓
Rate Limit
   ↓
Concurrency Limit
   ↓
Usage Quota
   ↓
Allowed?
 /      \
NO       YES
|         |
Reject    Execute Tool
          ↓
       Meter Usage
          ↓
       Commit Event
```

---

## 49. Acceptance Criteria

## AC-LIMIT-001

Plan limits can be configured by authorized Super Admins.

## AC-LIMIT-002

Plan limits are versioned.

## AC-LIMIT-003

Tenant limits are derived correctly from subscription entitlements.

## AC-LIMIT-004

Server-side enforcement prevents unauthorized usage.

## AC-LIMIT-005

Frontend manipulation cannot bypass limits.

## AC-LIMIT-006

Hard limits reject requests after quota exhaustion.

## AC-LIMIT-007

Soft limits generate warnings without unauthorized blocking.

## AC-LIMIT-008

Overage-enabled limits continue usage and record billable consumption.

## AC-LIMIT-009

Overage-disabled limits reject usage after exhaustion.

## AC-LIMIT-010

Rate limits throttle excessive requests.

## AC-LIMIT-011

Concurrency limits prevent capacity exhaustion.

## AC-LIMIT-012

Usage events are idempotent.

## AC-LIMIT-013

Duplicate events do not double-count usage.

## AC-LIMIT-014

Usage is correctly associated with the tenant and subscription.

## AC-LIMIT-015

AI agents cannot bypass limits.

## AC-LIMIT-016

Human operators require appropriate authorization for overrides.

## AC-LIMIT-017

Temporary overrides automatically expire.

## AC-LIMIT-018

Limit warnings are generated at configured thresholds.

## AC-LIMIT-019

Usage forecasting correctly estimates quota exhaustion.

## AC-LIMIT-020

Plan upgrades update applicable limits.

## AC-LIMIT-021

Plan downgrades validate existing usage against new limits.

## AC-LIMIT-022

Annual plans correctly support annual and monthly quota models.

## AC-LIMIT-023

All limit modifications are audited.

## AC-LIMIT-024

Cross-tenant limit access is impossible.

## AC-LIMIT-025

Usage can be reconciled against billing records.

---

## 50. Definition of Done

The `plan_limits.md` implementation SHALL be considered complete when:

* [ ] Plan limits are configurable
* [ ] Limit policies are versioned
* [ ] Tenant isolation is enforced
* [ ] Server-side enforcement is implemented
* [ ] Count limits work
* [ ] Usage limits work
* [ ] Storage limits work
* [ ] Rate limits work
* [ ] Concurrency limits work
* [ ] Credit limits work
* [ ] Financial limits work
* [ ] Hard limits work
* [ ] Soft limits work
* [ ] Overage limits work
* [ ] Throttling works
* [ ] Queue-based enforcement works where required
* [ ] AI usage is metered
* [ ] Human-agent seats are enforced
* [ ] AI-agent capacity is enforced
* [ ] Workflow usage is metered
* [ ] MCP usage is metered
* [ ] API usage is metered
* [ ] Lead-generation usage is metered
* [ ] RAG usage is metered
* [ ] Storage usage is metered
* [ ] Integration usage is metered
* [ ] Usage warnings work
* [ ] Usage forecasting works
* [ ] AI recommendations work
* [ ] Human override workflows work
* [ ] Approval workflows work
* [ ] Usage events are idempotent
* [ ] Usage events are durable
* [ ] Failed events are recoverable
* [ ] Reconciliation works
* [ ] Audit logging works
* [ ] Security controls are validated
* [ ] RBAC is enforced
* [ ] Observability is implemented
* [ ] Alerts are implemented
* [ ] Disaster recovery is tested
* [ ] Load testing is completed
* [ ] End-to-end tests pass
* [ ] Production monitoring is enabled

---

## 51. Architectural Invariant

SalesGenie's Plan Limit system MUST maintain the following invariant:

```text
A request MAY execute only when:

Authentication
    AND
Authorization
    AND
Tenant Isolation
    AND
Feature Entitlement
    AND
Plan Limit Policy
    AND
Usage Availability
    AND
Rate/Concurrency Policy
    AND
Financial Policy
```

are all satisfied.

The system MUST ensure:

```text
AI cannot bypass limits.
Human users cannot bypass limits.
Frontend code cannot bypass limits.
Integrations cannot bypass limits.
MCP tools cannot bypass limits.
Workflows cannot bypass limits.
API clients cannot bypass limits.
```

All limit-sensitive operations SHALL ultimately be governed by the centralized entitlement and limit-enforcement architecture.
