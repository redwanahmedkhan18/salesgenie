# SalesGenie — Usage Limits Requirements

**Document:** `usage_limits.md`  
**Product:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Requirement Level:** FAANG-Level / Production-Grade  
**Scope:** Usage quotas, resource limits, consumption enforcement, AI and human usage, tenant isolation, subscription-plan limits, real-time metering, soft/hard limits, burst handling, grace periods, overage controls, alerts, forecasting, governance, and enforcement.

---

## 1. Purpose

The Usage Limits subsystem SHALL control how much of a SalesGenie resource a tenant, user, AI agent, workflow, integration, API client, or service may consume during a defined billing or operational period.

Usage Limits SHALL be distinct from Feature Entitlements.

```text
Feature Entitlement
        ↓
"Can this capability be used?"
        ↓
Usage Limit
        ↓
"How much can it be used?"
```

The platform SHALL enforce both independently.

```text
Feature Entitled
        AND
Usage Available
        AND
Authorization Valid
        =
Execution Allowed
```

---

## 2. Product Context

SalesGenie usage limits SHALL cover:

* AI messages
* LLM tokens
* AI inference requests
* AI agents
* Human agents
* Conversations
* Leads
* Lead enrichment
* Lead generation
* Contacts
* Knowledge bases
* Documents
* Document processing
* RAG queries
* Embeddings
* Vector storage
* Workflow executions
* Workflow steps
* MCP calls
* MCP tool executions
* API requests
* Webhook events
* Email messages
* WhatsApp messages
* Social messages
* Voice calls
* Voice minutes
* Call recordings
* Storage
* Integrations
* Campaigns
* Reports
* Data exports
* Automation executions

---

## 3. Actors

The system SHALL support usage control for:

```text
End User
Sales Agent
Support Agent
Team Lead
Manager
Organization Admin
Billing Admin
Developer
Analyst
Super Admin
AI Agent
AI Supervisor
Workflow Engine
MCP Agent
API Client
Integration Service
Background Worker
System Service
```

---

## 4. Usage Limit Model

The platform SHALL calculate effective usage limits using:

```text
Plan
 +
Feature Entitlement
 +
Subscription
 +
Add-ons
 +
Tenant Overrides
 +
User / Agent Policies
 +
Billing Period
 +
Current Usage
 =
Effective Usage Policy
```

---

## 5. User Requirements

## UR-UL-001 — Usage Visibility

Authorized users SHALL be able to view current resource consumption.

---

## UR-UL-002 — Remaining Capacity

Users SHALL be able to determine remaining capacity for applicable resources.

Example:

```text
AI Messages
Used: 7,500
Limit: 10,000
Remaining: 2,500
```

---

## UR-UL-003 — Usage Percentage

The system SHALL display:

```text
Current Usage
Limit
Remaining
Percentage Used
Reset Date
```

---

## UR-UL-004 — Usage Alerts

Users SHALL receive configurable alerts when usage approaches configured thresholds.

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

## UR-UL-005 — Limit Notifications

The platform SHALL notify authorized users when a resource:

* Approaches its limit
* Reaches its limit
* Exceeds a soft limit
* Is blocked by a hard limit

---

## UR-UL-006 — Reset Visibility

Users SHALL be able to see when usage resets.

---

## UR-UL-007 — Usage History

Authorized users SHALL be able to view historical consumption.

---

## UR-UL-008 — Resource Breakdown

Usage SHALL be filterable by:

```text
Tenant
User
AI Agent
Channel
Integration
Workflow
API Key
MCP Server
MCP Tool
Resource Type
Time Range
```

---

## UR-UL-009 — Plan Awareness

Users SHALL be able to understand how their current plan affects usage limits.

---

## UR-UL-010 — Upgrade Guidance

When approaching or exceeding a limit, the platform SHOULD provide:

```text
Upgrade Plan
Purchase Add-On
Enable Overage
Wait for Reset
Contact Sales
```

where applicable.

---

## 6. System Requirements

## SR-UL-001 — Centralized Usage Limit Service

SalesGenie SHALL provide a centralized Usage Limit Service.

---

## SR-UL-002 — Server-Side Enforcement

All usage limits SHALL be enforced server-side.

Client-side counters SHALL never be authoritative.

---

## SR-UL-003 — Tenant Isolation

Usage MUST be isolated by tenant.

One tenant MUST never consume another tenant's quota.

---

## SR-UL-004 — Atomic Consumption

Usage reservation and consumption SHALL support atomic operations.

The platform MUST prevent race conditions such as:

```text
Limit = 100
Current = 99

Request A → consumes 1
Request B → consumes 1

Final usage MUST NOT incorrectly become 101
```

---

## SR-UL-005 — Distributed Enforcement

Usage enforcement SHALL work correctly across multiple service instances.

---

## SR-UL-006 — Horizontal Scalability

The usage system SHALL support horizontally scaled services.

---

## SR-UL-007 — Event-Driven Metering

Usage events SHOULD be emitted through the platform event bus.

Example:

```text
AI Request
    ↓
Usage Event
    ↓
Usage Meter
    ↓
Aggregation
    ↓
Limit Evaluation
```

---

## 7. Usage Resource Catalog

The system SHALL maintain a centralized resource catalog.

Example:

```yaml
resources:

  ai_messages:
    category: AI
    unit: message

  llm_tokens:
    category: AI
    unit: token

  voice_minutes:
    category: VOICE
    unit: minute

  leads:
    category: SALES
    unit: lead

  workflow_executions:
    category: AUTOMATION
    unit: execution

  mcp_tool_calls:
    category: MCP
    unit: call

  api_requests:
    category: API
    unit: request

  storage:
    category: STORAGE
    unit: byte
```

---

## 8. Usage Dimensions

## FR-UL-001

The usage system SHALL support multiple dimensions.

Examples:

```text
tenant_id
user_id
agent_id
workflow_id
integration_id
channel_id
api_key_id
mcp_server_id
mcp_tool_id
resource_type
plan_id
billing_period
```

---

## 9. Usage Units

## FR-UL-002

The system SHALL support:

```text
count
token
byte
kilobyte
megabyte
gigabyte
second
minute
hour
request
execution
message
conversation
lead
contact
document
record
```

---

## 10. Limit Types

## FR-UL-003

The platform SHALL support:

```text
HARD_LIMIT
SOFT_LIMIT
BURST_LIMIT
RATE_LIMIT
CONCURRENCY_LIMIT
DAILY_LIMIT
WEEKLY_LIMIT
MONTHLY_LIMIT
YEARLY_LIMIT
LIFETIME_LIMIT
```

---

## 11. Hard Limits

## FR-UL-004

A hard limit SHALL prevent additional consumption after the limit is reached.

Example:

```text
Limit = 10,000 AI messages

Usage = 10,000

Next request → DENY
```

---

## 12. Soft Limits

## FR-UL-005

A soft limit SHALL allow controlled consumption beyond a threshold.

Example:

```text
Limit = 10,000
Soft threshold = 90%

At 9,000:
    Warning

At 10,000:
    Additional policy applies
```

---

## 13. Overage

## FR-UL-006

The platform SHALL support configurable overage policies.

Possible policies:

```text
BLOCK
ALLOW_WITH_BILLING
ALLOW_WITH_CREDIT
ALLOW_WITH_APPROVAL
ALLOW_WITH_ADMIN_OVERRIDE
```

---

## 14. Rate Limits

## FR-UL-007

The platform SHALL support request-rate limits.

Example:

```text
100 API requests/minute
```

Rate limits SHALL be independent from monthly quotas.

---

## 15. Concurrency Limits

## FR-UL-008

The system SHALL support concurrent-operation limits.

Examples:

```text
Maximum active AI conversations
Maximum simultaneous voice calls
Maximum concurrent workflows
Maximum concurrent API requests
Maximum concurrent document-processing jobs
```

---

## 16. Burst Handling

## FR-UL-009

The platform SHOULD support controlled bursts.

Example:

```text
Base:
100 requests/minute

Burst:
150 requests/minute for 10 seconds
```

Burst capacity SHALL not bypass monthly usage limits.

---

## 17. AI Usage Limits

## FR-UL-010

The platform SHALL support AI-specific limits:

```text
AI requests
AI messages
Input tokens
Output tokens
Total tokens
LLM calls
AI agent executions
Agent turns
Tool calls
Reasoning operations
Embedding operations
Reranking operations
RAG queries
```

---

## 18. AI Agent Limits

## FR-UL-011

Each AI agent MAY have:

```text
Daily execution limit
Monthly execution limit
Concurrent execution limit
Token budget
Tool-call budget
MCP-call budget
Cost budget
```

---

## 19. AI-Based Usage Enforcement

## AI-UL-001

AI agents SHALL check usage availability before expensive operations.

---

## AI-UL-002

AI agents MUST NOT attempt to bypass limits by:

```text
Changing resource identifiers
Creating duplicate agents
Splitting requests
Calling alternative APIs
Calling unauthorized MCP tools
Changing tenants
Manipulating client counters
```

---

## AI-UL-003

AI agents SHOULD optimize consumption when limits are near exhaustion.

Examples:

```text
Use shorter context
Reduce unnecessary tool calls
Avoid duplicate retrieval
Summarize previous context
Use lower-cost models when policy permits
```

---

## AI-UL-004

AI agents SHALL NOT change billing or quota policy without authorization.

---

## 20. Human Usage Limits

## HUMAN-UL-001

Human users SHALL operate within tenant-defined usage policies.

---

## HUMAN-UL-002

Human users SHALL receive warnings before resource exhaustion where configured.

---

## HUMAN-UL-003

Administrators MAY configure user-level limits if supported by the plan.

---

## HUMAN-UL-004

Human users MUST NOT bypass usage controls by creating unauthorized API keys, workflows, agents, or integrations.

---

## 21. Conversation Limits

## FR-UL-012

The system SHALL support:

```text
Monthly conversations
Daily conversations
Active conversations
Messages per conversation
AI turns per conversation
Human handoffs
```

---

## 22. Lead Limits

## FR-UL-013

SalesGenie SHALL support:

```text
Lead generation
Lead enrichment
Lead imports
Lead exports
Lead scoring
Contact discovery
Company discovery
```

as separately measurable resources.

---

## 23. Workflow Limits

## FR-UL-014

The system SHALL support:

```text
Workflow executions
Workflow steps
Scheduled executions
Parallel branches
AI workflow runs
Webhook-triggered executions
MCP workflow actions
```

---

## 24. MCP Usage Limits

## FR-UL-015

MCP usage SHALL support:

```text
MCP requests
MCP server calls
MCP tool calls
MCP resource reads
MCP prompt executions
MCP concurrent executions
```

---

## FR-UL-016

MCP tool limits MAY be defined independently.

Example:

```yaml
mcp:
  total_calls: 10000
  server_calls:
    crm: 5000
    analytics: 2000
  tool_calls:
    create_lead: 1000
```

---

## 25. Integration Usage Limits

## FR-UL-017

The platform SHALL support integration-specific usage limits.

Examples:

```text
Gmail messages
Salesforce API calls
HubSpot API calls
Zendesk API calls
Slack messages
WhatsApp messages
Google Drive reads
LinkedIn operations
Facebook operations
Instagram operations
YouTube API requests
TikTok API requests
Jira API requests
Notion API requests
Microsoft Teams messages
```

---

## 26. API Usage Limits

## FR-UL-018

The API platform SHALL support:

```text
Requests/minute
Requests/hour
Requests/day
Requests/month
Concurrent requests
Payload limits
Bulk operation limits
Export limits
```

---

## 27. Webhook Limits

## FR-UL-019

Webhook usage SHALL support:

```text
Events/hour
Events/day
Events/month
Concurrent deliveries
Retry attempts
Payload size
```

---

## 28. Voice Usage Limits

## FR-UL-020

Voice usage SHALL support:

```text
Call count
Inbound minutes
Outbound minutes
Total minutes
Concurrent calls
Recording storage
Transcription minutes
Voice AI sessions
```

---

## 29. Storage Limits

## FR-UL-021

The system SHALL support:

```text
Document storage
Vector storage
File storage
Recording storage
Database storage
Export storage
Backup storage
```

---

## 30. Document Processing Limits

## FR-UL-022

The platform SHALL support:

```text
Documents/month
Pages/month
OCR operations
Document size
Processing jobs
Concurrent processing jobs
```

---

## 31. RAG Limits

## FR-UL-023

RAG usage SHALL support:

```text
Queries
Retrieved chunks
Embedding tokens
Embedding requests
Vector storage
Indexing jobs
Reranking operations
Documents indexed
```

---

## 32. Campaign Limits

## FR-UL-024

SalesGenie SHALL support:

```text
Campaigns
Recipients
Messages
Campaign executions
Concurrent campaigns
Scheduled campaigns
```

---

## 33. Export Limits

## FR-UL-025

The system SHALL support:

```text
Exports/day
Exports/month
Rows/export
Bytes/export
Concurrent exports
```

---

## 34. Usage Reservation

## FR-UL-026

For operations where final consumption is uncertain, the system SHALL support usage reservation.

Example:

```text
Request
  ↓
Estimate Usage
  ↓
Reserve Capacity
  ↓
Execute
  ↓
Calculate Actual Usage
  ↓
Commit Actual Usage
  ↓
Release Difference
```

---

## 35. Usage Reservation for AI

For LLM operations:

```text
Estimated tokens
        ↓
Reserve token budget
        ↓
LLM request
        ↓
Actual token usage
        ↓
Commit actual usage
        ↓
Release unused reservation
```

---

## 36. Atomic Usage Operations

The usage system SHALL provide atomic operations such as:

```text
check()
reserve()
consume()
commit()
release()
rollback()
```

---

## 37. Usage Ledger

## FR-UL-027

All billable or quota-controlled consumption SHOULD be represented in an immutable usage ledger.

Example:

```text
UsageEvent
----------
event_id
tenant_id
subject_id
resource
quantity
unit
timestamp
source
request_id
correlation_id
metadata
```

---

## 38. Idempotency

## FR-UL-028

Usage events SHALL support idempotency.

Duplicate events MUST NOT double-count consumption.

Example:

```text
event_id = abc123

First event:
+1

Duplicate event:
+0
```

---

## 39. Event Ordering

## FR-UL-029

The usage system SHALL tolerate delayed and out-of-order events.

---

## 40. Event Reconciliation

## FR-UL-030

The system SHALL periodically reconcile:

```text
Raw Usage Events
      ↓
Usage Ledger
      ↓
Aggregated Counters
      ↓
Plan Limits
      ↓
Billing Records
```

Discrepancies SHALL be detected and reported.

---

## 41. Usage Aggregation

The system SHALL support:

```text
Real-time counters
Minute aggregates
Hourly aggregates
Daily aggregates
Monthly aggregates
Billing-period aggregates
Historical aggregates
```

---

## 42. Billing Periods

## FR-UL-031

Usage limits SHALL support:

```text
Calendar day
Calendar week
Calendar month
Subscription month
Calendar year
Subscription year
Custom period
Lifetime
```

---

## 43. Subscription Billing Period

For subscription-based plans, monthly limits SHOULD normally align with the customer's subscription period rather than assuming calendar months.

---

## 44. Reset Behavior

## FR-UL-032

The system SHALL support automatic usage resets.

Example:

```text
Billing period ends
       ↓
Current period closed
       ↓
Usage archived
       ↓
New period initialized
       ↓
Counters reset
```

---

## 45. Plan Upgrade

## FR-UL-033

Plan upgrades SHALL update effective usage limits according to billing policy.

Example:

```text
Starter:
10,000 AI messages

Usage:
8,000

Upgrade → Professional:
50,000 AI messages

Remaining capacity:
42,000
```

The exact proration policy SHALL be configurable.

---

## 46. Plan Downgrade

## FR-UL-034

Downgrades SHALL handle existing usage safely.

Example:

```text
Current usage = 40,000
New plan limit = 10,000

System:
DO NOT delete usage.

Effective state:
Over-limit

Policy:
Block additional usage
OR
Allow until period reset
OR
Apply configured grace policy
```

---

## 47. Add-On Capacity

## FR-UL-035

Add-ons SHALL increase applicable limits.

Example:

```text
Base:
10,000 AI messages

Add-on:
+25,000

Effective:
35,000
```

---

## 48. Temporary Limit Overrides

## FR-UL-036

Authorized administrators SHALL be able to grant temporary capacity.

Example:

```yaml
override:
  tenant_id: tenant_123
  resource: ai_messages
  additional_capacity: 50000
  starts_at: "2026-08-28T00:00:00Z"
  expires_at: "2026-09-05T00:00:00Z"
  reason: "Enterprise pilot"
```

---

## 49. Override Governance

Temporary usage overrides SHALL require:

```text
Authorized Actor
Reason
Scope
Start Time
Expiration
Audit Record
```

High-risk overrides SHOULD require approval.

---

## 50. Usage Alert Engine

## FR-UL-037

The platform SHALL provide configurable usage alerts.

Example:

```text
80% → Informational
90% → Warning
95% → Critical
100% → Limit Reached
```

---

## 51. Alert Channels

Usage alerts MAY be delivered through:

```text
Email
In-app notifications
Slack
Microsoft Teams
Webhook
Admin dashboard
AI notification
```

---

## 52. Alert Deduplication

## FR-UL-038

The alert system MUST prevent notification storms.

For example, a tenant crossing 90% should not receive hundreds of identical alerts.

---

## 53. Usage Forecasting

## FR-UL-039

SalesGenie MAY forecast when a tenant will reach a limit.

Example:

```text
Current usage:
80%

Average daily consumption:
2,000

Estimated exhaustion:
5 days
```

---

## 54. AI Usage Forecasting

## AI-UL-005

AI analytics MAY predict:

```text
Limit exhaustion
Cost spikes
Abnormal usage
Usage growth
Plan suitability
Expected overage
```

AI predictions SHALL NOT directly change limits without authorized policy execution.

---

## 55. Anomaly Detection

## FR-UL-040

The platform SHOULD detect unusual consumption.

Examples:

```text
Sudden API spike
Unexpected AI token increase
Abnormal MCP activity
Unexpected voice usage
Large export
Rapid lead generation
```

---

## 56. Human Review of Anomalies

High-risk usage anomalies MAY trigger:

```text
Human review
Temporary restriction
Security investigation
API key suspension
Workflow suspension
AI agent suspension
```

---

## 57. Usage Limit Enforcement Workflow

```text
Request
   ↓
Authenticate
   ↓
Resolve Tenant
   ↓
Resolve Actor
   ↓
Check Feature Entitlement
   ↓
Identify Resource
   ↓
Calculate Requested Usage
   ↓
Check Current Usage
   ↓
Check Rate Limit
   ↓
Check Concurrency Limit
   ↓
Check Period Limit
   ↓
Check Overage Policy
   ↓
Reserve Capacity
   ↓
Execute
   ↓
Commit Actual Usage
   ↓
Emit Usage Event
   ↓
Update Analytics
```

---

## 58. AI Execution Workflow

```text
AI Agent
   ↓
Select Capability
   ↓
Feature Entitlement Check
   ↓
Usage Estimate
   ↓
Usage Reservation
   ↓
Model / Tool Execution
   ↓
Actual Usage
   ↓
Commit Usage
   ↓
Remaining Capacity
   ↓
Continue / Warn / Stop
```

---

## 59. Human Execution Workflow

```text
Human Agent
    ↓
Action
    ↓
Authorization
    ↓
Feature Entitlement
    ↓
Usage Limit Check
    ↓
Reserve Capacity
    ↓
Execute
    ↓
Consume Usage
    ↓
Audit
```

---

## 60. Workflow Execution Enforcement

```text
Workflow Trigger
       ↓
Tenant Validation
       ↓
Workflow Entitlement
       ↓
Execution Limit Check
       ↓
Reserve Capacity
       ↓
Execute Steps
       ↓
Per-Step Usage Check
       ↓
Commit Usage
```

---

## 61. MCP Execution Enforcement

```text
AI Agent
   ↓
MCP Tool Request
   ↓
Feature Entitlement
   ↓
Agent Authorization
   ↓
MCP Policy
   ↓
Rate Limit
   ↓
Usage Limit
   ↓
Reservation
   ↓
Tool Execution
   ↓
Usage Commit
```

---

## 62. Integration Execution Enforcement

Every integration request SHOULD pass through:

```text
Integration Entitlement
        ↓
Authentication
        ↓
Authorization
        ↓
Provider Rate Limit
        ↓
SalesGenie Usage Limit
        ↓
Execution
        ↓
Usage Meter
```

---

## 63. API Response Behavior

When a limit is reached, the API SHALL return a deterministic response.

Example:

```json
{
  "error": {
    "code": "USAGE_LIMIT_EXCEEDED",
    "resource": "ai_messages",
    "limit": 10000,
    "current_usage": 10000,
    "remaining": 0,
    "reset_at": "2026-09-28T00:00:00Z"
  }
}
```

---

## 64. Usage Error Codes

The system SHALL support:

```text
USAGE_LIMIT_EXCEEDED
USAGE_LIMIT_NEARLY_EXCEEDED
RATE_LIMIT_EXCEEDED
CONCURRENCY_LIMIT_EXCEEDED
OVERAGE_NOT_ALLOWED
INSUFFICIENT_CREDITS
USAGE_RESERVATION_FAILED
USAGE_COMMIT_FAILED
USAGE_EVENT_DUPLICATE
USAGE_RESOURCE_UNKNOWN
USAGE_PERIOD_EXPIRED
TENANT_USAGE_SUSPENDED
```

---

## 65. Grace Period

## FR-UL-041

The system MAY provide a grace period after limit exhaustion.

Example:

```text
Limit reached
    ↓
Grace capacity
    ↓
Temporary continued access
    ↓
Warning
    ↓
Hard enforcement
```

Grace capacity MUST be explicitly configured.

---

## 66. Emergency Protection

## FR-UL-042

The platform SHALL support emergency usage controls.

Super Admins MAY temporarily:

```text
Suspend resource
Reduce global limit
Suspend tenant
Suspend API key
Suspend AI agent
Suspend workflow
Suspend integration
```

Emergency actions SHALL be audited.

---

## 67. Usage Dashboard

The dashboard SHALL provide:

```text
Current Usage
Limits
Remaining
Usage Percentage
Reset Date
Historical Usage
Usage Trends
Top Consumers
Top AI Agents
Top Integrations
Top Workflows
Top API Clients
Cost Indicators
Forecast
Alerts
```

---

## 68. Tenant Usage Dashboard

Organization administrators SHALL be able to view:

```text
Tenant total
User usage
AI usage
Human usage
Integration usage
Workflow usage
MCP usage
API usage
Voice usage
Storage usage
```

---

## 69. AI vs Human Usage

The platform SHALL distinguish:

```text
AI-generated usage
Human-generated usage
Hybrid usage
System-generated usage
```

Example:

```text
AI:
75,000 messages

Human:
15,000 messages

System:
5,000 messages
```

---

## 70. Usage Attribution

Each usage event SHOULD identify its source.

Example:

```json
{
  "tenant_id": "tenant_123",
  "resource": "llm_tokens",
  "quantity": 2500,
  "actor_type": "ai_agent",
  "actor_id": "agent_456",
  "workflow_id": "workflow_789",
  "channel": "whatsapp",
  "integration": "whatsapp",
  "request_id": "req_123"
}
```

---

## 71. Hierarchical Limits

The system SHALL support hierarchical limits.

Example:

```text
Tenant:
100,000 AI tokens/day

        ↓

Team:
50,000/day

        ↓

AI Agent:
10,000/day

        ↓

Single Request:
5,000 tokens
```

A request SHALL be allowed only if all applicable constraints permit it.

---

## 72. Hierarchical Enforcement

```text
Global Policy
      ↓
Tenant Limit
      ↓
Team Limit
      ↓
User Limit
      ↓
Agent Limit
      ↓
Workflow Limit
      ↓
Request Limit
```

The strictest applicable policy SHALL apply unless explicit policy precedence states otherwise.

---

## 73. Per-User Limits

## FR-UL-043

Organizations MAY define limits for individual users.

Example:

```yaml
user_limit:
  user_id: user_123
  ai_messages_daily: 500
  api_requests_daily: 1000
```

---

## 74. Per-Agent Limits

## FR-UL-044

AI agents SHALL support configurable resource budgets.

Example:

```yaml
agent_budget:
  monthly_tokens: 1000000
  daily_tool_calls: 5000
  daily_mcp_calls: 1000
```

---

## 75. Per-Workflow Limits

## FR-UL-045

Workflows SHALL support:

```text
Executions/day
Executions/month
Steps/execution
AI calls/execution
MCP calls/execution
API calls/execution
```

---

## 76. Per-Integration Limits

## FR-UL-046

Integrations SHALL support:

```text
Requests/minute
Requests/day
Requests/month
Concurrent operations
```

---

## 77. Usage and Feature Entitlement Relationship

The system SHALL enforce:

```text
Feature Entitlement
        ↓
Resource Exists?
        ↓
Usage Limit
        ↓
Capacity Available?
        ↓
Authorization
        ↓
Execute
```

A user with:

```text
AI Voice = ENABLED
```

but:

```text
Voice Minutes = 0 remaining
```

MUST NOT initiate a billable voice operation unless overage/grace policy allows it.

---

## 78. Usage and Credits

If SalesGenie supports credits:

```text
Usage
 ↓
Credit Conversion
 ↓
Credit Deduction
 ↓
Remaining Credits
```

Credits SHALL be tracked independently from raw usage.

---

## 79. Credit Exhaustion

When credits reach zero:

```text
Feature Entitlement
        +
Credits = 0
        ↓
Apply Overage Policy
```

---

## 80. Usage and Billing

Usage data SHALL be compatible with:

```text
Subscription Billing
Usage-Based Billing
Metered Billing
Invoices
Credits
Overages
Coupons
Enterprise Contracts
```

---

## 81. Usage Ledger Integrity

Usage records used for billing SHALL be:

```text
Immutable
Auditable
Idempotent
Timestamped
Tenant-scoped
Traceable
Reconciliable
```

---

## 82. Usage Correction

Authorized billing administrators MAY issue corrections.

Corrections MUST:

```text
Never silently modify history
Create adjustment records
Reference original event
Record actor
Record reason
Create audit event
```

---

## 83. Usage Backfill

The platform SHALL support controlled usage backfills for:

```text
Service outages
Delayed events
Migration
Data reconciliation
Billing corrections
```

Backfills SHALL be idempotent.

---

## 84. Usage Retention

Usage data SHALL support configurable retention periods.

The platform SHOULD retain:

```text
Aggregated billing usage
Historical usage summaries
Audit records
```

according to organizational and regulatory policies.

---

## 85. Usage Privacy

Usage analytics SHALL avoid exposing unnecessary customer data.

Dashboards SHOULD use:

```text
Aggregated metrics
Masked identifiers
Role-based visibility
Tenant-scoped views
```

---

## 86. Security Requirements

## SEC-UL-001

Usage counters MUST NOT be client-controlled.

---

## SEC-UL-002

Usage APIs MUST require authentication.

---

## SEC-UL-003

Usage modifications MUST require authorization.

---

## SEC-UL-004

Tenant IDs MUST be validated server-side.

---

## SEC-UL-005

Users MUST NOT be able to modify:

```text
Current usage
Usage limits
Remaining quota
Billing usage
Credit balances
```

through client requests.

---

## SEC-UL-006

AI agents MUST NOT modify their own usage limits.

---

## SEC-UL-007

Workflow engines MUST NOT bypass usage enforcement.

---

## SEC-UL-008

MCP tools MUST NOT bypass usage enforcement.

---

## 87. Reliability Requirements

## REL-UL-001

Usage enforcement SHALL fail closed for security-critical resources.

---

## REL-UL-002

The platform SHALL prevent double charging or double counting.

---

## REL-UL-003

Temporary infrastructure failures SHALL NOT permanently corrupt quota counters.

---

## REL-UL-004

Usage reconciliation SHALL repair detectable counter inconsistencies.

---

## 88. Performance Requirements

## PERF-UL-001

Simple usage checks SHOULD target:

```text
P95 < 50 ms
```

under normal production conditions.

---

## PERF-UL-002

High-volume usage counters SHOULD avoid synchronous writes to expensive analytical databases.

---

## PERF-UL-003

Usage aggregation SHOULD use scalable counters and asynchronous pipelines where appropriate.

---

## 89. Scalability Requirements

The system SHALL support:

```text
10M+ users
500K+ concurrent conversations
Millions of AI agents
Millions of workflows
Billions of usage events
High-volume API traffic
High-frequency AI operations
```

The usage subsystem SHALL support horizontal scaling.

---

## 90. Rate Limiting Architecture

A recommended architecture:

```text
Client
  ↓
API Gateway
  ↓
Rate Limiter
  ↓
Authorization
  ↓
Usage Limit Service
  ↓
Application Service
  ↓
Usage Event Bus
  ↓
Usage Aggregator
```

---

## 91. Usage Data Architecture

Recommended logical architecture:

```text
                 ┌─────────────────────┐
                 │   Usage Event Bus   │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │   Usage Processor   │
                 └──────────┬──────────┘
                            ↓
              ┌─────────────┴─────────────┐
              ↓                           ↓
      Real-Time Counters          Immutable Ledger
              ↓                           ↓
      Limit Enforcement             Billing Usage
              ↓                           ↓
      Product Analytics             Invoices
```

---

## 92. Usage API

The platform SHALL expose APIs such as:

```http
GET    /api/v1/usage
GET    /api/v1/usage/current
GET    /api/v1/usage/history
GET    /api/v1/usage/limits
GET    /api/v1/usage/{resource}
POST   /api/v1/usage/check
POST   /api/v1/usage/reserve
POST   /api/v1/usage/commit
POST   /api/v1/usage/release
GET    /api/v1/usage/forecast
GET    /api/v1/admin/usage
POST   /api/v1/admin/usage/adjustments
```

---

## 93. Usage Check API

Example:

```json
{
  "tenant_id": "tenant_123",
  "resource": "ai_messages",
  "requested_quantity": 1
}
```

Response:

```json
{
  "allowed": true,
  "resource": "ai_messages",
  "requested": 1,
  "current_usage": 7499,
  "limit": 10000,
  "remaining": 2501,
  "reset_at": "2026-09-28T00:00:00Z"
}
```

---

## 94. Usage Reservation API

Example:

```json
{
  "resource": "llm_tokens",
  "quantity": 5000,
  "idempotency_key": "req_123"
}
```

Response:

```json
{
  "reserved": true,
  "reservation_id": "reservation_456",
  "expires_at": "2026-08-28T10:05:00Z"
}
```

---

## 95. Usage Commit

After execution:

```json
{
  "reservation_id": "reservation_456",
  "actual_quantity": 3275
}
```

The platform SHALL release unused capacity.

---

## 96. Usage Limit Configuration

Example:

```yaml
usage_limits:

  ai_messages:
    period: monthly
    limit: 10000
    enforcement: hard

  llm_tokens:
    period: monthly
    limit: 5000000
    enforcement: soft

  voice_minutes:
    period: monthly
    limit: 500
    enforcement: hard

  workflow_executions:
    period: monthly
    limit: 10000
    enforcement: hard

  api_requests:
    period: minute
    limit: 100
    enforcement: rate

  mcp_tool_calls:
    period: monthly
    limit: 5000
    enforcement: hard
```

---

## 97. Usage Policy Precedence

Recommended precedence:

```text
Global Safety Limit
        ↓
Tenant Contract Limit
        ↓
Subscription Plan Limit
        ↓
Add-On Capacity
        ↓
Tenant Override
        ↓
Team Limit
        ↓
User Limit
        ↓
AI Agent Limit
        ↓
Workflow Limit
        ↓
Request Limit
```

Security restrictions SHALL override capacity grants.

---

## 98. Usage Limit Conflict

If policies conflict:

```text
Security Deny
        >
Emergency Suspension
        >
Explicit Hard Limit
        >
Tenant Policy
        >
Plan Policy
        >
Add-On
        >
Default
```

The final precedence SHALL be deterministic and versioned.

---

## 99. Usage Limit Caching

The platform MAY cache:

```text
Effective limits
Current counters
Remaining capacity
Policy configuration
```

Caches SHALL have bounded TTLs.

---

## 100. Cache Invalidation

Usage-related caches SHALL be invalidated when:

```text
Plan changes
Subscription changes
Add-on purchased
Limit override created
Limit override expires
Tenant suspended
Usage correction occurs
Billing period resets
```

---

## 101. Monitoring

The platform SHALL monitor:

```text
usage_check_latency
usage_reservation_latency
usage_commit_latency
usage_events_processed
usage_events_failed
usage_event_duplicates
quota_denials
rate_limit_denials
concurrency_denials
usage_reconciliation_errors
counter_drift
usage_pipeline_lag
```

---

## 102. SLO Requirements

Recommended targets:

```text
Usage check availability: 99.99%
Usage decision P95: < 50 ms
Usage event processing: < 5 seconds
Critical quota synchronization: < 10 seconds
Billing reconciliation: 99.999% accuracy target
```

---

## 103. Observability

Every usage operation SHOULD include:

```text
request_id
trace_id
correlation_id
tenant_id
resource
actor_type
actor_id
quantity
decision
latency
service
timestamp
```

---

## 104. Anomaly Protection

If usage suddenly increases beyond configured thresholds:

```text
Detect
 ↓
Classify
 ↓
Alert
 ↓
Apply Policy
 ↓
Optional Human Review
```

The system MAY automatically restrict suspicious activity when security policy requires it.

---

## 105. AI Optimization

AI SHOULD assist with:

```text
Usage forecasting
Model selection
Context optimization
Duplicate-call detection
Tool-call optimization
Workflow optimization
Cost optimization
Capacity planning
```

AI recommendations MUST respect configured policies.

---

## 106. Human Governance

Human administrators SHALL remain responsible for:

```text
Limit policy
Enterprise overrides
Overage policies
Emergency limits
Contract-specific capacity
Security restrictions
```

AI SHOULD recommend but MUST NOT silently override these controls.

---

## 107. Enterprise Usage Policies

Enterprise tenants MAY have:

```text
Custom limits
Unlimited resources
Contract-based quotas
Custom rate limits
Dedicated capacity
Custom overage rules
Custom alert thresholds
Custom reset periods
Custom AI budgets
```

"Unlimited" SHALL still be protected by global safety and abuse controls.

---

## 108. Unlimited Plans

For an unlimited resource:

```text
Commercial Limit = Unlimited
```

does NOT imply:

```text
No rate limits
No abuse protection
No security controls
No infrastructure protection
No fair-use policy
```

---

## 109. Fair-Use Protection

The platform MAY apply fair-use policies to unlimited plans.

These policies SHALL be transparent and configurable.

---

## 110. Usage-Based Billing Integration

When usage-based billing is enabled:

```text
Usage Event
    ↓
Meter
    ↓
Aggregation
    ↓
Billable Quantity
    ↓
Pricing Engine
    ↓
Invoice
```

---

## 111. Metered Billing Integration

Metered resources SHALL expose:

```text
resource
quantity
unit
period
tenant
pricing_dimension
```

---

## 112. Usage + Subscription Cancellation

When a subscription is canceled:

```text
Cancellation
      ↓
Determine Effective End
      ↓
Apply Usage Policy
      ↓
Close Billing Period
      ↓
Finalize Usage
      ↓
Generate Billing Data
      ↓
Restrict / Revoke Access
```

---

## 113. Usage During Payment Failure

The system SHALL support configurable policies:

```text
Continue During Grace Period
Restrict High-Cost Features
Block New Consumption
Suspend Tenant
```

---

## 114. Usage During Downgrade

The system MUST NOT delete historical usage.

Instead:

```text
Existing Usage
      ↓
New Lower Limit
      ↓
Over-Limit State
      ↓
Configured Enforcement
```

---

## 115. Usage Audit

Every administrative usage modification SHALL create an audit event.

Required fields:

```text
event_id
tenant_id
resource
previous_value
new_value
actor_id
actor_type
reason
timestamp
request_id
correlation_id
approval_id
```

---

## 116. Data Model

## UsageLimit

```text
UsageLimit
----------
id
tenant_id
resource_id
scope_type
scope_id
period_type
limit_value
soft_limit
hard_limit
burst_limit
rate_limit
concurrency_limit
overage_policy
effective_from
effective_until
policy_version
created_at
updated_at
```

---

## UsageCounter

```text
UsageCounter
------------
id
tenant_id
resource_id
scope_type
scope_id
period_start
period_end
consumed
reserved
remaining
version
updated_at
```

---

## UsageEvent

```text
UsageEvent
----------
id
tenant_id
resource_id
actor_type
actor_id
quantity
unit
source
request_id
correlation_id
idempotency_key
timestamp
metadata
```

---

## UsageReservation

```text
UsageReservation
----------------
id
tenant_id
resource_id
scope_id
quantity
status
expires_at
request_id
created_at
updated_at
```

---

## UsageAdjustment

```text
UsageAdjustment
---------------
id
tenant_id
resource_id
quantity
direction
reason
reference_event_id
created_by
approved_by
created_at
```

---

## 117. Resource Hierarchy

The system SHALL support:

```text
Tenant
 ├── Teams
 │    ├── Users
 │    └── AI Agents
 │
 ├── Workflows
 │
 ├── Integrations
 │
 ├── MCP Servers
 │    └── MCP Tools
 │
 ├── API Clients
 │
 └── Channels
```

Usage SHALL be attributable at each applicable level.

---

## 118. Multi-Tenant Isolation

Usage queries MUST include tenant boundaries.

Example:

```text
WHERE tenant_id = authenticated_tenant_id
```

Administrative cross-tenant access MUST require explicit Super Admin authorization.

---

## 119. Data Consistency

The platform SHALL distinguish:

```text
Authoritative Usage Ledger
        ↓
Aggregated Counters
        ↓
Cached Usage
        ↓
Dashboard Representation
```

Dashboards MAY be eventually consistent.

Critical enforcement SHOULD use authoritative or strongly synchronized counters.

---

## 120. Failure Handling

If usage infrastructure fails:

```text
Request
   ↓
Usage Service Failure
   ↓
Determine Resource Risk
   ↓
Critical Resource?
   /          \
 YES           NO
 |              |
Fail Closed    Controlled Fallback
```

The fallback policy SHALL be resource-specific.

---

## 121. Duplicate Request Protection

Usage consumption SHALL use idempotency keys where duplicate execution is possible.

---

## 122. Retry Safety

Retries MUST NOT double-consume quota.

```text
Request
 ↓
Usage reservation
 ↓
Timeout
 ↓
Retry
 ↓
Same idempotency key
 ↓
Existing reservation detected
```

---

## 123. Batch Usage

The system SHOULD support efficient batch operations.

Example:

```text
1000 lead enrichment records
```

The platform SHOULD reserve and consume capacity efficiently rather than issuing 1000 independent quota transactions when safe.

---

## 124. Large Operation Protection

Before large operations such as:

```text
Bulk lead generation
Bulk enrichment
Bulk export
Large document ingestion
Large campaign
Mass workflow execution
```

the system SHALL estimate required capacity.

If insufficient:

```text
Reject
OR
Ask for confirmation
OR
Use partial execution
OR
Require additional capacity
```

according to policy.

---

## 125. Partial Execution

The platform MAY support partial completion.

Example:

```text
Requested:
10,000 leads

Remaining quota:
6,000

Policy:
Process 6,000
Stop
Report remaining 4,000
```

Partial execution behavior MUST be explicit.

---

## 126. Usage Limit Testing

The test suite SHALL cover:

```text
Normal usage
Exact limit
One over limit
Concurrent requests
Race conditions
Retries
Duplicate events
Out-of-order events
Plan upgrade
Plan downgrade
Add-on activation
Add-on expiration
Trial expiration
Subscription cancellation
Payment failure
Usage correction
Counter reconciliation
Cache failure
Database failure
Event bus failure
Tenant isolation
Privilege escalation
AI bypass attempts
MCP bypass attempts
Workflow bypass attempts
API bypass attempts
```

---

## 127. Load Testing

The system SHALL be tested under:

```text
High request volume
High AI token volume
High concurrent conversations
High workflow execution volume
High MCP call volume
High webhook volume
High integration traffic
Large usage-event bursts
```

---

## 128. Security Testing

Security tests SHALL verify:

```text
Cross-tenant quota access
Quota manipulation
Client-side bypass
JWT manipulation
Role escalation
AI-agent privilege escalation
Workflow bypass
MCP bypass
API-key bypass
Replay attacks
Duplicate consumption
Race-condition exploitation
```

---

## 129. Acceptance Criteria

## AC-UL-001

Usage limits are enforced server-side.

## AC-UL-002

Client-side modification cannot bypass quotas.

## AC-UL-003

AI agents cannot bypass usage limits.

## AC-UL-004

Human users cannot bypass usage limits.

## AC-UL-005

Workflows cannot bypass usage limits.

## AC-UL-006

MCP tools cannot bypass usage limits.

## AC-UL-007

Integrations cannot bypass usage limits.

## AC-UL-008

API clients cannot bypass usage limits.

## AC-UL-009

Tenant usage is strictly isolated.

## AC-UL-010

Concurrent requests cannot oversubscribe hard limits.

## AC-UL-011

Duplicate usage events do not double-count.

## AC-UL-012

Usage reservations are atomic.

## AC-UL-013

Usage commits accurately reflect actual consumption.

## AC-UL-014

Unused reservations are released.

## AC-UL-015

Usage counters reconcile with the usage ledger.

## AC-UL-016

Plan upgrades correctly update effective limits.

## AC-UL-017

Plan downgrades preserve historical usage.

## AC-UL-018

Add-ons increase applicable capacity.

## AC-UL-019

Temporary overrides expire automatically.

## AC-UL-020

Usage resets correctly at the configured period boundary.

## AC-UL-021

Rate limits operate independently from monthly quotas.

## AC-UL-022

Concurrency limits are enforced.

## AC-UL-023

Usage alerts trigger at configured thresholds.

## AC-UL-024

Alert deduplication prevents notification storms.

## AC-UL-025

Usage forecasts do not modify policy without authorization.

## AC-UL-026

Usage anomalies are detectable.

## AC-UL-027

Usage corrections are fully audited.

## AC-UL-028

Billing usage can be reconciled.

## AC-UL-029

Usage APIs return deterministic error codes.

## AC-UL-030

Usage dashboards accurately represent consumption.

---

## 130. Definition of Done

The `usage_limits.md` implementation SHALL be considered complete when:

* [ ] Centralized usage resource catalog exists
* [ ] Tenant usage isolation exists
* [ ] User-level usage tracking exists
* [ ] AI-agent usage tracking exists
* [ ] Human-agent usage tracking exists
* [ ] Workflow usage tracking exists
* [ ] MCP usage tracking exists
* [ ] Integration usage tracking exists
* [ ] API usage tracking exists
* [ ] Channel usage tracking exists
* [ ] AI token metering exists
* [ ] AI request metering exists
* [ ] Voice metering exists
* [ ] Lead metering exists
* [ ] Workflow metering exists
* [ ] Storage metering exists
* [ ] Document metering exists
* [ ] RAG metering exists
* [ ] Hard limits exist
* [ ] Soft limits exist
* [ ] Rate limits exist
* [ ] Burst limits exist
* [ ] Concurrency limits exist
* [ ] Daily limits exist
* [ ] Monthly limits exist
* [ ] Yearly limits exist
* [ ] Lifetime limits exist
* [ ] Usage reservation exists
* [ ] Atomic consumption exists
* [ ] Idempotency exists
* [ ] Usage ledger exists
* [ ] Usage aggregation exists
* [ ] Usage reconciliation exists
* [ ] Usage correction exists
* [ ] Usage reset exists
* [ ] Plan integration exists
* [ ] Add-on integration exists
* [ ] Subscription integration exists
* [ ] Billing integration exists
* [ ] Credit integration exists
* [ ] Overage policies exist
* [ ] Grace-period policies exist
* [ ] Usage alerts exist
* [ ] Usage forecasting exists
* [ ] Anomaly detection exists
* [ ] Usage dashboard exists
* [ ] AI usage governance exists
* [ ] Human usage governance exists
* [ ] MCP enforcement exists
* [ ] Workflow enforcement exists
* [ ] API enforcement exists
* [ ] Integration enforcement exists
* [ ] Security controls pass
* [ ] Tenant isolation tests pass
* [ ] Race-condition tests pass
* [ ] Load tests pass
* [ ] Failure-mode tests pass
* [ ] Billing reconciliation tests pass
* [ ] Audit logging is enabled
* [ ] Production monitoring is enabled
* [ ] SLOs are monitored

---

## 131. Architectural Invariant

SalesGenie SHALL enforce the following invariant:

```text
A resource-consuming operation MAY execute only when:

Authenticated
    AND
Tenant Valid
    AND
Feature Entitled
    AND
Actor Authorized
    AND
Resource Recognized
    AND
Rate Limit Satisfied
    AND
Concurrency Limit Satisfied
    AND
Usage Limit Available
    AND
Reservation Successful
    AND
Security Policy Allows
```

After execution:

```text
Actual Usage
    ↓
Usage Ledger
    ↓
Atomic Counter Update
    ↓
Remaining Capacity
    ↓
Billing / Analytics
    ↓
Alerts / Forecasting
```

The platform MUST guarantee:

```text
AI cannot bypass usage limits.
Humans cannot bypass usage limits.
Frontend clients cannot bypass usage limits.
API clients cannot bypass usage limits.
Workflows cannot bypass usage limits.
MCP tools cannot bypass usage limits.
Integrations cannot bypass usage limits.
Duplicate events cannot double-count usage.
Concurrent requests cannot incorrectly oversubscribe hard quotas.
Cross-tenant usage cannot occur.
Historical usage cannot be silently modified.
```

The Usage Limits subsystem SHALL remain the authoritative capacity-control layer for SalesGenie's resource consumption while integrating with Feature Entitlements, Subscription Management, Pricing, Billing, Credits, Metered Billing, MCP, Integrations, AI Agents, Workflows, and Human Operations.
