# SalesGenie — Quota Management Requirements

**Document:** `quota_management.md`  
**Product:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Requirement Level:** FAANG-Level / Production-Grade  
**Scope:** Quota definition, allocation, reservation, consumption, enforcement, hierarchy, AI and human usage, tenant isolation, plan-based quotas, add-on quotas, overages, burst capacity, quota resets, alerts, forecasting, governance, reconciliation, auditability, and distributed enforcement.

---

## 1. Purpose

The Quota Management subsystem SHALL provide centralized control over finite platform resources consumed by SalesGenie tenants, users, human agents, AI agents, workflows, MCP tools, integrations, API clients, and system services.

Quota Management SHALL answer:

```text
Who can consume?
What resource can they consume?
How much can they consume?
During which period?
Under which policy?
What happens when the quota is exhausted?
```

Quota Management SHALL work together with:

```text
Feature Entitlements
Usage Limits
Subscription Management
Pricing Engine
Billing Platform
Metered Billing
Credit Management
AI Agent Platform
Workflow Engine
MCP Platform
Integration Platform
API Gateway
RBAC / Authorization
Security Platform
```

---

## 2. Core Quota Model

SalesGenie SHALL distinguish:

```text
Feature Entitlement
    ↓
Can the actor use the feature?

Quota
    ↓
How much capacity is allocated?

Usage
    ↓
How much capacity has been consumed?

Limit
    ↓
What is the maximum allowed consumption?

Billing
    ↓
How is consumption charged?
```

The core execution rule SHALL be:

```text
Authenticated
    AND
Authorized
    AND
Feature Entitled
    AND
Quota Available
    AND
Usage Limit Available
    AND
Security Policy Allows
    =
Execution Allowed
```

---

## 3. Actors

Quota Management SHALL support:

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

## 4. User Requirements

## UR-QM-001 — Quota Visibility

Authorized users SHALL be able to view their applicable quotas.

---

## UR-QM-002 — Remaining Quota

Users SHALL be able to see:

```text
Allocated Quota
Consumed Quota
Reserved Quota
Remaining Quota
Quota Percentage
Reset Date
Quota Status
```

---

## UR-QM-003 — Quota Dashboard

Organization administrators SHALL have access to a centralized quota dashboard.

The dashboard SHALL provide:

```text
Total Allocated
Total Consumed
Total Remaining
Quota Utilization
Quota Exhaustion
Overages
Top Consumers
AI Usage
Human Usage
Workflow Usage
MCP Usage
Integration Usage
API Usage
```

---

## UR-QM-004 — Quota Alerts

Authorized users SHALL receive notifications when quota utilization reaches configured thresholds.

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

## UR-QM-005 — Quota Exhaustion Notification

Users SHALL be notified when a quota becomes exhausted.

---

## UR-QM-006 — Reset Information

Users SHALL be able to determine when a quota resets.

---

## UR-QM-007 — Historical Quota Usage

Authorized users SHALL be able to view historical quota allocation and consumption.

---

## UR-QM-008 — Quota Breakdown

Usage SHALL be filterable by:

```text
Tenant
Organization
Team
User
Human Agent
AI Agent
Workflow
Integration
MCP Server
MCP Tool
API Key
Channel
Resource
Billing Period
```

---

## UR-QM-009 — Quota Explanation

The UI SHALL explain why a quota has a particular value.

Example:

```text
AI Messages

Base Plan:
10,000

Purchased Add-on:
25,000

Enterprise Override:
15,000

Effective Quota:
50,000
```

---

## UR-QM-010 — Upgrade Guidance

When a quota is nearly exhausted, SalesGenie SHOULD provide applicable actions:

```text
Upgrade Plan
Purchase Add-on
Request Increase
Enable Overage
Wait for Reset
Contact Administrator
```

---

## 5. System Requirements

## SR-QM-001 — Centralized Quota Service

SalesGenie SHALL provide a centralized Quota Management Service.

---

## SR-QM-002 — Server-Side Enforcement

Quota enforcement MUST occur server-side.

The frontend SHALL never be authoritative for quota decisions.

---

## SR-QM-003 — Tenant Isolation

Quota allocation, consumption, reservation, and enforcement MUST be tenant-scoped.

A tenant MUST NOT access or consume another tenant's quota.

---

## SR-QM-004 — Distributed Enforcement

Quota decisions SHALL remain correct when multiple service instances process requests concurrently.

---

## SR-QM-005 — Horizontal Scalability

The quota service SHALL support horizontal scaling.

---

## SR-QM-006 — Atomic Allocation

Quota allocation operations SHALL be atomic.

---

## SR-QM-007 — Atomic Consumption

Quota consumption SHALL prevent race conditions.

Example:

```text
Quota = 100
Used = 99

Request A → 1
Request B → 1

Only one request may consume the final available unit
unless burst or overage policy explicitly allows both.
```

---

## 6. Quota Resource Catalog

SalesGenie SHALL maintain a centralized resource catalog.

Example:

```yaml
resources:

  ai_messages:
    category: ai
    unit: message

  llm_tokens:
    category: ai
    unit: token

  ai_agent_executions:
    category: ai
    unit: execution

  conversations:
    category: engagement
    unit: conversation

  leads:
    category: sales
    unit: lead

  contacts:
    category: sales
    unit: contact

  workflow_executions:
    category: automation
    unit: execution

  workflow_steps:
    category: automation
    unit: step

  mcp_tool_calls:
    category: mcp
    unit: call

  api_requests:
    category: api
    unit: request

  voice_minutes:
    category: voice
    unit: minute

  storage:
    category: storage
    unit: byte

  documents:
    category: knowledge
    unit: document

  rag_queries:
    category: knowledge
    unit: query
```

---

## 7. Quota Dimensions

## FR-QM-001

The system SHALL support quota dimensions including:

```text
tenant_id
organization_id
team_id
user_id
agent_id
workflow_id
integration_id
api_key_id
mcp_server_id
mcp_tool_id
channel_id
resource_id
plan_id
subscription_id
billing_period
```

---

## 8. Quota Types

## FR-QM-002

The system SHALL support:

```text
COUNT_QUOTA
TOKEN_QUOTA
STORAGE_QUOTA
TIME_QUOTA
REQUEST_QUOTA
EXECUTION_QUOTA
MESSAGE_QUOTA
CONVERSATION_QUOTA
CONCURRENCY_QUOTA
RATE_QUOTA
CREDIT_QUOTA
```

---

## 9. Quota Periods

## FR-QM-003

The system SHALL support:

```text
Per Request
Per Minute
Per Hour
Per Day
Per Week
Per Month
Per Subscription Period
Per Year
Lifetime
Custom Period
```

---

## 10. Quota Allocation

## FR-QM-004

The platform SHALL support quota allocation from:

```text
Base Subscription
Plan
Add-on
Enterprise Contract
Promotional Grant
Administrative Override
Credit Purchase
System Grant
```

---

## 11. Effective Quota Calculation

The effective quota SHALL be calculated deterministically.

Recommended model:

```text
Effective Quota =
Base Plan Quota
+ Add-on Quota
+ Enterprise Allocation
+ Promotional Allocation
+ Approved Temporary Allocation
- Explicit Reductions
```

Security restrictions SHALL remain independent of capacity allocation.

---

## 12. Quota Precedence

The platform SHALL use deterministic policy precedence.

Recommended order:

```text
Global Safety Constraint
        ↓
Security Restriction
        ↓
Enterprise Contract
        ↓
Subscription Plan
        ↓
Add-on
        ↓
Approved Tenant Override
        ↓
Team Allocation
        ↓
User Allocation
        ↓
AI Agent Allocation
        ↓
Workflow Allocation
        ↓
Request Allocation
```

---

## 13. Hierarchical Quotas

## FR-QM-005

SalesGenie SHALL support hierarchical quota management.

Example:

```text
Tenant
 ├── Team
 │    ├── Human Users
 │    └── AI Agents
 │
 ├── Workflows
 │
 ├── Integrations
 │
 ├── MCP Servers
 │    └── MCP Tools
 │
 └── API Clients
```

---

## 14. Hierarchical Quota Enforcement

A request SHALL be permitted only when all applicable quota scopes permit consumption.

```text
Tenant Quota
    ↓
Team Quota
    ↓
User Quota
    ↓
Agent Quota
    ↓
Workflow Quota
    ↓
Request Quota
```

---

## 15. Quota Reservation

## FR-QM-006

The system SHALL support quota reservation for operations whose final consumption is uncertain.

Workflow:

```text
Request
   ↓
Estimate
   ↓
Reserve Quota
   ↓
Execute
   ↓
Measure Actual Usage
   ↓
Commit Actual Consumption
   ↓
Release Unused Reservation
```

---

## 16. Quota Reservation API

Example:

```json
{
  "tenant_id": "tenant_123",
  "resource": "llm_tokens",
  "requested_quantity": 5000,
  "idempotency_key": "request_abc123"
}
```

Response:

```json
{
  "allowed": true,
  "reservation_id": "reservation_456",
  "reserved_quantity": 5000,
  "expires_at": "2026-08-28T10:05:00Z"
}
```

---

## 17. Quota Reservation Lifecycle

A reservation SHALL support:

```text
PENDING
RESERVED
COMMITTED
RELEASED
EXPIRED
CANCELLED
FAILED
```

---

## 18. Atomic Quota Consumption

## FR-QM-007

Quota consumption SHALL be atomic.

Logical operation:

```text
if remaining_quota >= requested_quantity:
    remaining_quota -= requested_quantity
    consumed += requested_quantity
    allow
else:
    deny
```

The operation MUST be protected against concurrent updates.

---

## 19. Idempotency

## FR-QM-008

Quota operations SHALL support idempotency.

Repeated requests with the same idempotency key MUST NOT consume quota multiple times.

---

## 20. Retry Safety

The system SHALL ensure:

```text
Request
 ↓
Quota Reservation
 ↓
Network Timeout
 ↓
Retry
 ↓
Same Idempotency Key
 ↓
Existing Reservation Reused
```

---

## 21. AI-Based Quota Management

## AI-QM-001

AI agents SHALL check quota availability before executing resource-intensive actions.

---

## AI-QM-002

AI agents MUST respect:

```text
Tenant Quota
Team Quota
Agent Quota
Workflow Quota
Resource Quota
Rate Quota
Concurrency Quota
```

---

## AI-QM-003

AI agents MUST NOT:

```text
Modify Their Own Quota
Create Unauthorized Quota
Change Tenant Scope
Create Duplicate Accounts to Obtain Quota
Circumvent Rate Limits
Switch Resources to Avoid Accounting
Call Unauthorized MCP Tools
```

---

## AI-QM-004

AI agents SHOULD optimize quota consumption.

Possible strategies:

```text
Reduce redundant tool calls
Reuse retrieved context
Summarize long conversations
Avoid duplicate searches
Select efficient models
Batch compatible operations
Reduce unnecessary workflow steps
```

---

## AI-QM-005

AI systems MAY recommend quota adjustments.

AI recommendations SHALL require authorized policy execution before taking effect.

---

## 22. Human-Based Quota Management

## HUMAN-QM-001

Human users SHALL consume quota through normal product operations.

---

## HUMAN-QM-002

Human users SHALL receive clear feedback when an operation is blocked because of quota exhaustion.

---

## HUMAN-QM-003

Administrators MAY assign team or user quotas where permitted.

---

## HUMAN-QM-004

Human users MUST NOT modify quota counters directly.

---

## HUMAN-QM-005

Quota changes SHALL require appropriate RBAC permissions.

---

## 23. AI Agent Quotas

## FR-QM-009

Each AI agent MAY have dedicated quotas.

Example:

```yaml
agent_quota:
  monthly_tokens: 1000000
  daily_tool_calls: 5000
  daily_mcp_calls: 1000
  concurrent_runs: 20
```

---

## 24. AI Model Quotas

The system MAY define model-specific quotas.

Example:

```text
GPT-class models
Gemini-class models
Grok-class models
Mistral-class models
Embedding models
Reranking models
Speech models
Vision models
```

Each provider/model MAY have:

```text
Requests
Tokens
Cost
Concurrency
Rate
```

quotas.

---

## 25. AI Token Quotas

## FR-QM-010

The platform SHALL support:

```text
Input Token Quota
Output Token Quota
Total Token Quota
Context Token Quota
Embedding Token Quota
```

---

## 26. Human Agent Quotas

Human-agent quotas MAY include:

```text
Conversations
Tickets
Outbound messages
Campaign actions
Lead assignments
Exports
API actions
```

---

## 27. Conversation Quotas

## FR-QM-011

The system SHALL support:

```text
Conversations/day
Conversations/month
Active conversations
Messages/conversation
AI turns/conversation
Human handoffs
```

---

## 28. Lead Quotas

## FR-QM-012

SalesGenie SHALL support quotas for:

```text
Lead creation
Lead imports
Lead generation
Lead enrichment
Lead scoring
Company discovery
Contact discovery
Lead exports
```

---

## 29. Workflow Quotas

## FR-QM-013

Workflow quotas SHALL include:

```text
Executions
Steps
AI calls
MCP calls
API calls
Scheduled executions
Webhook-triggered executions
Concurrent executions
```

---

## 30. MCP Quotas

## FR-QM-014

MCP quotas SHALL support:

```text
MCP requests
MCP server calls
MCP tool calls
MCP resource reads
MCP prompt executions
Concurrent MCP operations
```

---

## 31. Per-Tool MCP Quotas

Example:

```yaml
mcp_quota:

  total_calls:
    monthly: 10000

  tools:
    create_lead:
      monthly: 2000

    search_company:
      monthly: 5000

    enrich_contact:
      monthly: 1000
```

---

## 32. Integration Quotas

## FR-QM-015

Integration-specific quotas SHALL support:

```text
Gmail
Google Drive
LinkedIn
Facebook
Instagram
WhatsApp
YouTube
TikTok
Slack
Zendesk
Salesforce
HubSpot
Jira
Notion
Microsoft Teams
```

Each integration MAY have independent:

```text
Request Quota
Message Quota
Daily Quota
Monthly Quota
Concurrency Quota
```

---

## 33. API Quotas

## FR-QM-016

The API platform SHALL support:

```text
Requests/minute
Requests/hour
Requests/day
Requests/month
Concurrent Requests
Bulk Operations
Export Operations
```

---

## 34. Voice Quotas

## FR-QM-017

Voice quotas SHALL support:

```text
Calls
Inbound Minutes
Outbound Minutes
Total Minutes
Concurrent Calls
Transcription Minutes
Recording Storage
Voice AI Sessions
```

---

## 35. Storage Quotas

## FR-QM-018

Storage quotas SHALL support:

```text
File Storage
Document Storage
Vector Storage
Recording Storage
Export Storage
Database Storage
```

---

## 36. Knowledge Base Quotas

## FR-QM-019

Knowledge management quotas SHALL support:

```text
Knowledge Bases
Documents
Pages
Chunks
Embeddings
RAG Queries
Vector Storage
Indexing Jobs
Reranking Requests
```

---

## 37. Campaign Quotas

## FR-QM-020

Campaign quotas SHALL support:

```text
Campaigns
Recipients
Messages
Campaign Executions
Concurrent Campaigns
Scheduled Campaigns
```

---

## 38. Export Quotas

## FR-QM-021

The system SHALL support:

```text
Exports/day
Exports/month
Rows/export
Bytes/export
Concurrent exports
```

---

## 39. Rate Quotas

Rate quotas SHALL protect platform infrastructure.

Example:

```text
100 API requests/minute
500 API requests/5 minutes
10 concurrent exports
20 concurrent AI executions
```

Rate quotas SHALL be separate from long-term allocation quotas.

---

## 40. Burst Quotas

## FR-QM-022

The system MAY support temporary burst capacity.

Example:

```text
Base quota:
100 requests/minute

Burst:
150 requests/minute

Burst duration:
10 seconds
```

Burst capacity SHALL NOT permanently increase the customer's allocated quota.

---

## 41. Concurrency Quotas

## FR-QM-023

The platform SHALL support concurrency quotas.

Examples:

```text
Maximum active AI agents
Maximum active workflows
Maximum simultaneous voice calls
Maximum concurrent exports
Maximum concurrent document processing jobs
Maximum concurrent MCP executions
```

---

## 42. Quota Exhaustion

When quota reaches zero:

```text
Quota Remaining = 0
```

the platform SHALL evaluate:

```text
Hard Block
Overage
Grace
Credits
Admin Override
Partial Execution
```

according to policy.

---

## 43. Hard Quota

A hard quota SHALL block additional consumption.

```text
Quota = 10,000
Used = 10,000

Next operation → DENY
```

---

## 44. Soft Quota

A soft quota SHALL trigger warnings while allowing additional usage under policy.

```text
Quota = 10,000

90% → Warning
100% → Overage Policy
```

---

## 45. Overage Quota

The platform SHALL support:

```text
BLOCK
ALLOW_WITH_BILLING
ALLOW_WITH_CREDITS
ALLOW_WITH_APPROVAL
ALLOW_WITH_ADMIN_OVERRIDE
```

---

## 46. Grace Quota

The platform MAY provide temporary grace capacity.

Example:

```text
Allocated:
10,000

Grace:
500

Maximum temporary usage:
10,500
```

Grace rules MUST be explicit.

---

## 47. Credit-Backed Quota

If credit management is enabled:

```text
Quota Exhausted
      ↓
Check Credits
      ↓
Credits Available?
      ↓
Consume Credits
      ↓
Allow Operation
```

---

## 48. Add-On Quota

Users SHALL be able to obtain additional capacity through supported add-ons.

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

## 49. Promotional Quota

The platform MAY grant temporary promotional quota.

Example:

```yaml
promotional_quota:
  resource: ai_messages
  quantity: 50000
  expires_at: "2026-09-30T23:59:59Z"
```

Expired promotional capacity SHALL automatically become unavailable.

---

## 50. Enterprise Quota

Enterprise tenants MAY receive:

```text
Custom quota
Dedicated quota
Contract quota
Unlimited commercial quota
Custom burst capacity
Custom rate quota
Custom concurrency quota
```

---

## 51. Unlimited Quota

An unlimited commercial quota SHALL still be subject to:

```text
Security Controls
Abuse Prevention
Infrastructure Protection
Rate Limits
Concurrency Limits
Fair-Use Policies
Global Safety Limits
```

---

## 52. Quota Upgrade

When a plan is upgraded:

```text
Existing Usage
      ↓
New Plan Resolution
      ↓
New Effective Quota
      ↓
Remaining Capacity Recalculated
```

Historical usage SHALL remain intact.

---

## 53. Quota Downgrade

When a plan is downgraded:

```text
Current Usage > New Quota
```

the system SHALL enter an explicit over-quota state.

It SHALL NOT delete historical consumption.

Possible policies:

```text
Block New Usage
Allow Until Reset
Allow Overage
Require Upgrade
```

---

## 54. Subscription Cancellation

Upon cancellation:

```text
Cancellation
     ↓
Determine Effective End
     ↓
Finalize Current Quota
     ↓
Apply Access Policy
     ↓
Archive Usage
     ↓
Revoke Expired Capacity
```

---

## 55. Subscription Suspension

If billing status causes suspension:

```text
Active
 ↓
Grace Period
 ↓
Restricted
 ↓
Suspended
```

Quota availability SHALL follow the subscription policy.

---

## 56. Temporary Quota Override

Authorized administrators SHALL be able to issue temporary quota overrides.

Example:

```yaml
quota_override:
  tenant_id: tenant_123
  resource: ai_messages
  additional_quantity: 50000
  starts_at: "2026-08-28T00:00:00Z"
  expires_at: "2026-09-05T00:00:00Z"
  reason: "Enterprise pilot"
```

---

## 57. Override Approval

High-impact quota increases SHOULD require approval.

Approval metadata SHALL include:

```text
Requester
Approver
Reason
Requested Capacity
Approved Capacity
Start Time
Expiration
Policy Version
```

---

## 58. Quota Reset

The system SHALL support automatic resets.

```text
Period Ends
    ↓
Close Quota Period
    ↓
Archive Usage
    ↓
Create New Period
    ↓
Apply Effective Allocation
    ↓
Reset Consumed Counter
```

---

## 59. Quota Carry-Over

The platform MAY support quota carry-over.

Example:

```text
Monthly quota:
10,000

Unused:
2,000

Carry-over policy:
50%

Next period:
11,000
```

Carry-over rules SHALL be configurable per resource and plan.

---

## 60. Non-Carry-Over Quotas

By default, quotas SHOULD expire at the end of their defined period unless carry-over is explicitly enabled.

---

## 61. Quota Reservation Expiration

Reservations SHALL automatically expire after their configured TTL.

```text
Reserved
   ↓
TTL
   ↓
Expired
   ↓
Capacity Released
```

---

## 62. Quota Reconciliation

The system SHALL periodically reconcile:

```text
Quota Allocation
        ↓
Reservations
        ↓
Usage Ledger
        ↓
Aggregated Counters
        ↓
Remaining Quota
```

Discrepancies SHALL be detected.

---

## 63. Quota Ledger

Quota-affecting events SHOULD be represented in an immutable ledger.

Example:

```text
QuotaEvent
----------
event_id
tenant_id
resource_id
scope_type
scope_id
event_type
quantity
unit
source
request_id
correlation_id
timestamp
metadata
```

---

## 64. Quota Event Types

Supported events SHOULD include:

```text
ALLOCATED
INCREASED
DECREASED
RESERVED
COMMITTED
RELEASED
EXPIRED
ROLLED_BACK
ADJUSTED
TRANSFERRED
RESET
SUSPENDED
RESTORED
```

---

## 65. Quota Transfer

The platform MAY support quota transfers between scopes.

Example:

```text
Team A
10,000 remaining

Transfer:
2,000

Team A:
8,000

Team B:
+2,000
```

Transfers MUST be authorized and audited.

---

## 66. Quota Pool

The platform SHOULD support shared quota pools.

Example:

```text
Team Pool:
100,000 AI messages

User A
User B
User C
AI Agent A
AI Agent B
```

All members consume from the same pool subject to individual policies.

---

## 67. Reserved Quota Pools

Organizations MAY reserve capacity for critical workloads.

Example:

```text
Tenant quota:
100,000

Critical workload reserve:
20,000

General workload:
80,000
```

---

## 68. Priority-Based Quota Allocation

The platform MAY support workload priority.

Example:

```text
P0 Critical
P1 High
P2 Normal
P3 Low
```

When capacity is constrained, higher-priority operations MAY receive reserved capacity.

---

## 69. AI Priority

AI workloads MAY be assigned priorities.

Example:

```text
Customer Support AI → P0
Sales Lead Generation → P1
Analytics → P2
Background Summarization → P3
```

AI priority MUST NOT bypass security authorization.

---

## 70. Human Priority

Human-originated operations MAY receive priority according to organization policy.

---

## 71. Quota Allocation Algorithm

A quota allocation engine SHALL evaluate:

```text
Resource
Tenant
Plan
Subscription
Add-ons
Overrides
Scope
Period
Current Usage
Reservations
Priority
Overage Policy
Security Policy
```

and return:

```text
Allowed
Denied
Partially Allowed
Requires Approval
Overage Allowed
```

---

## 72. Quota Decision Object

Example:

```json
{
  "allowed": true,
  "resource": "ai_messages",
  "requested": 1,
  "allocated": 50000,
  "consumed": 12500,
  "reserved": 100,
  "remaining": 37400,
  "decision": "ALLOW",
  "policy_version": "quota-v4",
  "reset_at": "2026-09-28T00:00:00Z"
}
```

---

## 73. Quota Denial Object

Example:

```json
{
  "allowed": false,
  "resource": "ai_messages",
  "requested": 1,
  "allocated": 10000,
  "consumed": 10000,
  "remaining": 0,
  "decision": "DENY",
  "reason": "QUOTA_EXHAUSTED",
  "reset_at": "2026-09-28T00:00:00Z"
}
```

---

## 74. API Endpoints

The platform SHALL support APIs such as:

```http
GET    /api/v1/quotas
GET    /api/v1/quotas/current
GET    /api/v1/quotas/history
GET    /api/v1/quotas/limits
GET    /api/v1/quotas/{resource}
POST   /api/v1/quotas/check
POST   /api/v1/quotas/reserve
POST   /api/v1/quotas/commit
POST   /api/v1/quotas/release
GET    /api/v1/quotas/forecast
GET    /api/v1/admin/quotas
POST   /api/v1/admin/quotas/allocate
POST   /api/v1/admin/quotas/adjust
POST   /api/v1/admin/quotas/transfer
POST   /api/v1/admin/quotas/override
```

---

## 75. Quota Check API

Request:

```json
{
  "resource": "ai_messages",
  "quantity": 1
}
```

Response:

```json
{
  "allowed": true,
  "allocated": 50000,
  "consumed": 12000,
  "reserved": 100,
  "remaining": 37900,
  "reset_at": "2026-09-28T00:00:00Z"
}
```

---

## 76. Quota Error Codes

The system SHALL support:

```text
QUOTA_EXHAUSTED
QUOTA_NEAR_LIMIT
QUOTA_NOT_FOUND
QUOTA_RESOURCE_UNKNOWN
QUOTA_RESERVATION_FAILED
QUOTA_RESERVATION_EXPIRED
QUOTA_COMMIT_FAILED
QUOTA_RELEASE_FAILED
QUOTA_OVERAGE_NOT_ALLOWED
QUOTA_GRACE_EXHAUSTED
QUOTA_SUSPENDED
QUOTA_PERIOD_EXPIRED
QUOTA_TRANSFER_DENIED
QUOTA_OVERRIDE_NOT_AUTHORIZED
QUOTA_ALLOCATION_DENIED
QUOTA_CONCURRENCY_EXCEEDED
QUOTA_RATE_EXCEEDED
```

---

## 77. Bulk Operations

For large operations:

```text
Bulk Lead Generation
Bulk Enrichment
Bulk Import
Bulk Export
Bulk Document Processing
Bulk Campaign
```

the system SHALL estimate quota requirements before execution.

---

## 78. Partial Quota Allocation

If requested capacity exceeds remaining quota, the system MAY return:

```text
FULL
PARTIAL
DENIED
```

Example:

```text
Requested:
10,000 leads

Remaining:
6,000

Decision:
PARTIAL

Approved:
6,000
```

---

## 79. Partial Execution

Partial execution SHALL provide clear reporting:

```text
Requested: 10,000
Executed: 6,000
Rejected: 4,000
Reason: QUOTA_EXHAUSTED
```

---

## 80. Quota-Aware Workflow Engine

The Workflow Engine SHALL perform quota checks:

```text
Workflow Trigger
       ↓
Quota Check
       ↓
Reservation
       ↓
Execute Step
       ↓
Step Usage
       ↓
Commit
       ↓
Next Step
```

---

## 81. Per-Step Quota Enforcement

Every expensive workflow step SHOULD be quota-aware.

Examples:

```text
LLM Call
MCP Call
CRM API Call
Email Send
Lead Enrichment
Document Processing
Voice Call
```

---

## 82. Quota-Aware MCP Engine

MCP execution SHALL follow:

```text
AI Agent
   ↓
MCP Request
   ↓
Authorization
   ↓
Feature Entitlement
   ↓
Quota Check
   ↓
Rate Check
   ↓
Concurrency Check
   ↓
Reservation
   ↓
Tool Execution
   ↓
Commit
```

---

## 83. Quota-Aware Integration Platform

Integration requests SHALL pass through:

```text
Integration Authentication
       ↓
Integration Authorization
       ↓
Provider Rate Limit
       ↓
SalesGenie Quota
       ↓
Execution
       ↓
Usage Metering
```

---

## 84. Quota-Aware API Gateway

The API gateway SHALL enforce:

```text
Authentication
Authorization
Rate Quota
Concurrency Quota
Tenant Quota
Endpoint Quota
```

before forwarding requests.

---

## 85. Quota and Feature Entitlement

A feature SHALL be usable only when:

```text
Feature Enabled
AND
Quota Available
```

Example:

```text
AI Voice = ENABLED
Voice Minutes Remaining = 0
```

Result:

```text
Operation denied
```

unless configured overage or grace policy applies.

---

## 86. Quota and Billing

Quota management SHALL integrate with billing.

```text
Quota Consumption
      ↓
Usage Event
      ↓
Billing Meter
      ↓
Billable Quantity
      ↓
Pricing Engine
      ↓
Invoice
```

---

## 87. Quota and Credits

When credits are supported:

```text
Quota
 ↓
Quota Exhausted
 ↓
Credit Check
 ↓
Credit Available
 ↓
Credit Deduction
 ↓
Continue
```

---

## 88. Quota and Subscription

Subscription changes SHALL trigger quota recalculation.

Events include:

```text
Subscription Created
Subscription Activated
Subscription Upgraded
Subscription Downgraded
Subscription Renewed
Subscription Canceled
Subscription Suspended
Subscription Resumed
```

---

## 89. Quota and Pricing Plans

Each pricing plan SHALL define:

```yaml
plan:
  name: professional

  quotas:
    ai_messages: 50000
    llm_tokens: 5000000
    leads: 10000
    workflows: 10000
    mcp_calls: 5000
    storage_bytes: 10737418240
```

---

## 90. Quota Versioning

Quota policies SHALL be versioned.

Example:

```text
quota-policy-v1
quota-policy-v2
quota-policy-v3
```

Historical quota decisions SHALL remain traceable to the policy version that produced them.

---

## 91. Quota Migration

Quota schema migrations SHALL support:

```text
Backward Compatibility
Data Validation
Dual-Read
Dual-Write
Reconciliation
Rollback
```

where required.

---

## 92. Quota Cache

The system MAY cache:

```text
Effective Quota
Current Allocation
Remaining Capacity
Policy Configuration
```

Cache entries SHALL have bounded TTLs.

---

## 93. Cache Invalidation

Quota cache SHALL be invalidated when:

```text
Plan Changes
Subscription Changes
Add-on Purchased
Override Created
Override Expired
Quota Transferred
Quota Adjusted
Tenant Suspended
Period Reset
```

---

## 94. Distributed Counter Architecture

Recommended:

```text
                ┌───────────────────┐
                │    API Gateway    │
                └─────────┬─────────┘
                          ↓
                ┌───────────────────┐
                │  Quota Service    │
                └─────────┬─────────┘
                          ↓
              ┌───────────┴───────────┐
              ↓                       ↓
       Atomic Counters          Reservation Store
              ↓                       ↓
              └───────────┬───────────┘
                          ↓
                    Usage Event Bus
                          ↓
                  Immutable Ledger
                          ↓
                    Aggregation
                          ↓
                  Billing / Analytics
```

---

## 95. Event-Driven Quota Updates

Quota-affecting events SHOULD be published through an event bus.

Example:

```text
quota.allocated
quota.increased
quota.decreased
quota.reserved
quota.consumed
quota.released
quota.expired
quota.reset
quota.exhausted
quota.overage
quota.adjusted
```

---

## 96. Event Idempotency

Quota events SHALL include idempotency identifiers.

Duplicate events MUST NOT alter quota more than once.

---

## 97. Event Ordering

The system SHALL tolerate delayed and out-of-order events.

Where ordering is required, events SHALL use:

```text
Sequence Number
Version
Timestamp
Partition Key
```

or equivalent mechanisms.

---

## 98. Quota Reconciliation

A reconciliation worker SHALL compare:

```text
Quota Ledger
+
Usage Ledger
+
Reservations
+
Aggregated Counters
=
Expected Remaining Quota
```

Any discrepancy SHALL generate an operational event.

---

## 99. Quota Drift Detection

The system SHALL detect:

```text
Counter Drift
Negative Remaining Quota
Unexpected Allocation
Missing Consumption
Duplicate Consumption
Expired Reservation Leakage
Incorrect Reset
Cross-Tenant Consumption
```

---

## 100. Negative Quota

Negative remaining quota SHALL NOT occur for hard-enforced resources except when explicitly representing an approved overage state.

---

## 101. Quota Adjustment

Authorized administrators MAY adjust quota.

Every adjustment SHALL include:

```text
Previous Allocation
New Allocation
Difference
Actor
Reason
Timestamp
Reference
Approval
```

---

## 102. Quota Audit

All quota mutations SHALL be auditable.

Audit events SHALL include:

```text
event_id
tenant_id
resource_id
scope_type
scope_id
action
previous_value
new_value
actor_id
actor_type
reason
timestamp
request_id
correlation_id
policy_version
```

---

## 103. Security Requirements

## SEC-QM-001

Quota counters MUST NOT be client-controlled.

---

## SEC-QM-002

Quota allocation APIs MUST require authentication.

---

## SEC-QM-003

Quota mutation APIs MUST require authorization.

---

## SEC-QM-004

Tenant identifiers MUST be validated server-side.

---

## SEC-QM-005

AI agents MUST NOT modify their own quotas.

---

## SEC-QM-006

Workflow engines MUST NOT bypass quota enforcement.

---

## SEC-QM-007

MCP tools MUST NOT bypass quota enforcement.

---

## SEC-QM-008

API clients MUST NOT bypass quota enforcement through alternative endpoints.

---

## SEC-QM-009

Cross-tenant quota access MUST be prevented.

---

## 104. Quota Abuse Prevention

The platform SHOULD detect attempts to bypass quota through:

```text
Multiple API Keys
Multiple AI Agents
Duplicate Workflows
Multiple Sessions
Resource Switching
Tenant Switching
Replay Attacks
Concurrent Requests
Bulk Request Splitting
```

---

## 105. Quota Anomaly Detection

The platform SHOULD identify:

```text
Sudden Consumption Spike
Unexpected Agent Consumption
Unexpected MCP Consumption
Abnormal API Activity
Unexpected Integration Traffic
Rapid Quota Exhaustion
```

---

## 106. AI Quota Forecasting

AI analytics MAY predict:

```text
Quota Exhaustion
Expected Daily Consumption
Expected Monthly Consumption
Expected Overage
Plan Suitability
Capacity Requirements
```

AI forecasts SHALL be advisory unless an explicit automation policy is enabled.

---

## 107. Human Approval for AI Quota Actions

AI-generated quota recommendations SHALL support:

```text
Approve
Reject
Modify
Schedule
```

before high-impact quota changes are applied.

---

## 108. Quota Alerts

Alerts SHALL support:

```text
Threshold Reached
Quota Exhausted
Quota Increased
Quota Reduced
Quota Suspended
Unexpected Consumption
Quota Reset
Overage Started
```

---

## 109. Alert Channels

Alerts MAY be delivered through:

```text
In-App
Email
Slack
Microsoft Teams
Webhook
Admin Dashboard
```

---

## 110. Alert Deduplication

The platform MUST prevent repeated identical alerts from generating notification storms.

---

## 111. Quota Forecasting

The dashboard MAY display:

```text
Current Usage
Average Consumption
Projected Usage
Projected Exhaustion
Expected Overage
Recommended Capacity
```

---

## 112. Quota Recommendation Engine

The system MAY recommend:

```text
Upgrade Plan
Purchase Add-on
Increase Team Allocation
Reduce AI Consumption
Optimize Workflow
Reduce MCP Calls
Switch Model
Increase Quota
```

Recommendations SHALL be explainable.

---

## 113. Human vs AI Consumption

The system SHALL distinguish:

```text
Human Consumption
AI Consumption
Hybrid Consumption
System Consumption
```

Example:

```text
AI:
75,000

Human:
15,000

System:
5,000
```

---

## 114. Usage Attribution

Quota consumption SHALL be attributable to its source.

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

## 115. Resource Cost Awareness

Quota management MAY incorporate estimated infrastructure cost.

Example:

```text
Resource:
LLM Tokens

Consumption:
100,000 tokens

Estimated Cost:
$X

Quota Impact:
100,000 tokens
```

Cost estimation MUST NOT alter quota unless explicitly configured.

---

## 116. Critical Workload Protection

Organizations MAY reserve quota for:

```text
Customer Support
Production AI Agents
Critical Workflows
Emergency Communications
Security Workflows
Enterprise SLA Workloads
```

---

## 117. Quota Preemption

The system MAY support quota preemption for low-priority workloads.

Example:

```text
Capacity constrained

P0 workload:
Allowed

P3 workload:
Delayed
```

Preemption policies SHALL be explicit.

---

## 118. Queue-Based Quota Enforcement

For asynchronous workloads:

```text
Request
 ↓
Quota Check
 ↓
Queue
 ↓
Capacity Available
 ↓
Reservation
 ↓
Execution
```

This SHALL prevent uncontrolled resource bursts.

---

## 119. Backpressure

When quotas or infrastructure capacity are constrained, services SHALL apply backpressure.

Possible actions:

```text
Queue
Throttle
Delay
Reject
Prioritize
Partial Execute
```

---

## 120. Quota-Aware Scheduling

Scheduled jobs SHALL check quota availability before execution.

```text
Scheduled Job
      ↓
Quota Check
      ↓
Available?
 /       \
Yes       No
 |         |
Run       Reschedule / Reject
```

---

## 121. Quota-Aware Campaigns

Campaign execution SHALL stop or throttle when configured quota thresholds are reached.

---

## 122. Quota-Aware Voice Calls

Before initiating a billable voice call:

```text
Voice Entitlement
      ↓
Voice Quota
      ↓
Concurrent Call Quota
      ↓
Provider Limits
      ↓
Execute
```

---

## 123. Quota-Aware Document Processing

Before large ingestion:

```text
Document Count
Page Count
OCR Usage
Embedding Usage
Storage
```

SHALL be estimated and validated.

---

## 124. Quota-Aware RAG

RAG operations SHALL account for:

```text
Embedding Requests
Embedding Tokens
Vector Storage
Queries
Retrieved Chunks
Reranking
```

---

## 125. Quota-Aware Lead Generation

Lead-generation workflows SHALL account for:

```text
Company Search
Contact Discovery
Lead Enrichment
Verification
AI Scoring
External Data API Calls
Exports
```

---

## 126. Quota-Aware Social Operations

Social integrations SHALL enforce quotas for supported actions.

Examples:

```text
Messages
API Requests
Posts
Comments
Campaign Operations
Data Retrieval
```

The system SHALL also respect provider-specific policies and limits.

---

## 127. Quota-Aware Email

Email operations SHALL support:

```text
Emails Sent
Emails Received
API Requests
Bulk Sends
Campaign Recipients
Attachments
```

---

## 128. Quota-Aware CRM Operations

CRM integrations SHALL support quotas for:

```text
API Requests
Records Created
Records Updated
Records Read
Bulk Operations
Synchronization
```

---

## 129. Quota Policy Configuration

Example:

```yaml
quota_policy:

  ai_messages:
    allocation:
      monthly: 50000

    enforcement:
      type: hard

    alerts:
      - 75
      - 90
      - 95
      - 100

    overage:
      enabled: false

  llm_tokens:
    allocation:
      monthly: 5000000

    enforcement:
      type: soft

    overage:
      enabled: true
```

---

## 130. Quota Data Model

## QuotaDefinition

```text
QuotaDefinition
---------------
id
resource_id
name
description
unit
period_type
default_value
hard_limit
soft_limit
burst_limit
rate_limit
concurrency_limit
carry_over_policy
overage_policy
version
created_at
updated_at
```

---

## QuotaAllocation

```text
QuotaAllocation
---------------
id
tenant_id
scope_type
scope_id
resource_id
allocated_quantity
source_type
source_id
effective_from
effective_until
priority
policy_version
created_at
updated_at
```

---

## QuotaCounter

```text
QuotaCounter
------------
id
tenant_id
scope_type
scope_id
resource_id
period_start
period_end
allocated
consumed
reserved
remaining
version
updated_at
```

---

## QuotaReservation

```text
QuotaReservation
----------------
id
tenant_id
scope_type
scope_id
resource_id
quantity
status
idempotency_key
request_id
expires_at
created_at
updated_at
```

---

## QuotaAdjustment

```text
QuotaAdjustment
---------------
id
tenant_id
scope_type
scope_id
resource_id
previous_value
new_value
delta
reason
created_by
approved_by
created_at
```

---

## 131. Quota Pool Data Model

```text
QuotaPool
---------
id
tenant_id
name
resource_id
allocated
consumed
reserved
remaining
period_start
period_end
policy_version
created_at
updated_at
```

---

## 132. Quota Transfer Model

```text
QuotaTransfer
-------------
id
tenant_id
resource_id
source_scope
source_scope_id
destination_scope
destination_scope_id
quantity
status
requested_by
approved_by
reason
created_at
completed_at
```

---

## 133. Quota Decision Engine

The decision engine SHALL evaluate:

```text
Identity
Tenant
Authorization
Feature Entitlement
Resource
Quota Allocation
Current Consumption
Reservations
Rate
Concurrency
Priority
Overage
Grace
Credits
Security
```

Output:

```text
ALLOW
DENY
PARTIAL
QUEUE
REQUIRE_APPROVAL
```

---

## 134. Quota Decision Workflow

```text
Incoming Request
       ↓
Authenticate
       ↓
Resolve Tenant
       ↓
Resolve Actor
       ↓
Authorize
       ↓
Resolve Feature Entitlement
       ↓
Resolve Resource
       ↓
Resolve Quota Hierarchy
       ↓
Calculate Effective Quota
       ↓
Check Current Consumption
       ↓
Check Reservations
       ↓
Check Rate Quota
       ↓
Check Concurrency Quota
       ↓
Check Overage / Grace
       ↓
Check Security Policy
       ↓
Reserve
       ↓
Execute
       ↓
Commit Actual Usage
       ↓
Publish Event
       ↓
Update Analytics
```

---

## 135. Quota Decision for AI

```text
AI Agent
   ↓
Intent
   ↓
Required Resource Estimate
   ↓
Feature Entitlement
   ↓
Agent Quota
   ↓
Tenant Quota
   ↓
Model Quota
   ↓
MCP / Tool Quota
   ↓
Reservation
   ↓
Execution
   ↓
Actual Consumption
   ↓
Commit
```

---

## 136. Quota Decision for Human

```text
Human Agent
    ↓
Action
    ↓
Authentication
    ↓
Authorization
    ↓
Feature Entitlement
    ↓
User Quota
    ↓
Team Quota
    ↓
Tenant Quota
    ↓
Reservation
    ↓
Execution
    ↓
Consumption
    ↓
Audit
```

---

## 137. Quota Decision for Workflow

```text
Workflow
    ↓
Trigger
    ↓
Workflow Quota
    ↓
Tenant Quota
    ↓
Reserve
    ↓
Execute Step
    ↓
Step Quota
    ↓
Commit
```

---

## 138. Quota Decision for MCP

```text
AI Agent
    ↓
MCP Server
    ↓
MCP Tool
    ↓
Authorization
    ↓
Tool Entitlement
    ↓
Agent Quota
    ↓
Tenant Quota
    ↓
MCP Quota
    ↓
Rate / Concurrency
    ↓
Execute
```

---

## 139. Failure Handling

If quota infrastructure fails:

```text
Quota Service Failure
        ↓
Identify Resource Risk
        ↓
Critical?
     /       \
   Yes        No
   ↓           ↓
Fail Closed  Controlled Fallback
```

Critical billable or security-sensitive resources SHOULD fail closed.

---

## 140. Availability

The quota service SHALL be highly available because quota enforcement is a platform control-plane dependency.

Recommended target:

```text
Quota Decision Availability:
99.99%+
```

---

## 141. Performance Requirements

Simple quota checks SHOULD target:

```text
P50 < 20 ms
P95 < 50 ms
P99 < 100 ms
```

under normal production conditions.

---

## 142. Scalability Requirements

The architecture SHALL support:

```text
10M+ Users
500K+ Concurrent Conversations
Millions of AI Agents
Millions of Workflows
Billions of Quota/Usage Events
High API Traffic
High MCP Traffic
High Integration Traffic
```

---

## 143. Monitoring

The platform SHALL monitor:

```text
quota_check_latency
quota_reservation_latency
quota_commit_latency
quota_denials
quota_exhaustions
quota_overages
quota_reservation_failures
quota_commit_failures
quota_release_failures
quota_event_lag
quota_reconciliation_errors
quota_counter_drift
quota_cache_hit_rate
quota_cache_staleness
```

---

## 144. Observability

Every quota operation SHOULD include:

```text
request_id
trace_id
correlation_id
tenant_id
scope_type
scope_id
resource
requested_quantity
allocated_quantity
consumed_quantity
reserved_quantity
decision
policy_version
latency
timestamp
```

---

## 145. Distributed Tracing

Quota decisions SHALL propagate:

```text
Trace ID
Span ID
Correlation ID
Request ID
Tenant ID
```

across:

```text
API Gateway
Quota Service
AI Gateway
Workflow Engine
MCP Service
Integration Service
Billing Service
Usage Service
```

---

## 146. Quota Metrics

The platform SHOULD expose:

```text
quota_allocated_total
quota_consumed_total
quota_reserved_total
quota_remaining
quota_denied_total
quota_overage_total
quota_exhausted_total
quota_reset_total
quota_adjustment_total
quota_transfer_total
quota_reconciliation_errors
```

---

## 147. Quota Security Monitoring

Security systems SHOULD monitor:

```text
Quota Manipulation
Quota Escalation
Cross-Tenant Access
Unauthorized Allocation
Abnormal Transfers
Repeated Denials
Quota Bypass Attempts
```

---

## 148. Administrative Dashboard

Super Admins SHALL be able to view:

```text
Tenant Quota
Plan Quota
Allocated Capacity
Consumed Capacity
Remaining Capacity
Overages
Quota Overrides
Quota Transfers
Quota Adjustments
Quota Suspensions
Quota Anomalies
```

---

## 149. Organization Admin Dashboard

Organization admins SHALL be able to manage applicable:

```text
Team Quotas
User Quotas
AI Agent Quotas
Workflow Quotas
Integration Quotas
MCP Quotas
API Quotas
```

subject to their authorization.

---

## 150. Billing Admin Dashboard

Billing admins SHALL be able to view:

```text
Allocated Quota
Billable Usage
Overage
Add-on Capacity
Quota Adjustments
Quota Forecast
Invoice Impact
```

---

## 151. AI Governance Dashboard

The platform MAY provide:

```text
AI Agent Quota
Model Quota
Token Quota
Tool Quota
MCP Quota
Agent Cost
Quota Forecast
AI Optimization Recommendations
```

---

## 152. Data Privacy

Quota analytics SHALL minimize unnecessary customer-data exposure.

Access SHALL be controlled through RBAC.

---

## 153. Tenant Data Isolation

All quota queries SHALL enforce tenant scope.

Cross-tenant access SHALL require explicit Super Admin privileges.

---

## 154. Audit Retention

Quota mutation and administrative audit records SHALL follow configured retention policies.

---

## 155. Testing Requirements

The test suite SHALL cover:

```text
Quota Allocation
Quota Consumption
Quota Reservation
Quota Release
Quota Reset
Quota Exhaustion
Soft Quota
Hard Quota
Overage
Grace
Carry-over
Plan Upgrade
Plan Downgrade
Add-on
Enterprise Override
Quota Transfer
Quota Pool
Concurrent Requests
Race Conditions
Retries
Duplicate Requests
Out-of-Order Events
Reconciliation
Counter Drift
Cache Failure
Database Failure
Event Bus Failure
Tenant Isolation
RBAC
AI Bypass
MCP Bypass
Workflow Bypass
API Bypass
Integration Bypass
```

---

## 156. AI Testing

AI-specific tests SHALL verify:

```text
AI cannot modify its quota
AI cannot change tenant scope
AI cannot create unauthorized quota
AI cannot bypass quotas with tools
AI cannot bypass quotas through MCP
AI cannot bypass quotas through workflows
AI respects token budgets
AI respects tool-call budgets
AI respects concurrency quotas
AI receives correct remaining capacity
AI handles quota exhaustion correctly
```

---

## 157. Human Testing

Human-specific tests SHALL verify:

```text
Unauthorized quota changes fail
Authorized quota changes succeed
Human users cannot manipulate counters
Users receive quota warnings
Users receive exhaustion notifications
User quotas respect team quotas
Team quotas respect tenant quotas
```

---

## 158. Security Testing

Security testing SHALL verify:

```text
Cross-Tenant Quota Access
Privilege Escalation
Quota Manipulation
Replay Attacks
Idempotency Bypass
Race Conditions
Quota Transfer Abuse
Quota Override Abuse
API Bypass
MCP Bypass
Workflow Bypass
Client-Side Manipulation
```

---

## 159. Load Testing

Load tests SHALL simulate:

```text
Millions of quota checks
High-frequency AI requests
Concurrent workflow executions
Large MCP traffic
Large integration traffic
Large API traffic
Mass quota resets
Large event bursts
```

---

## 160. Disaster Recovery

Quota data SHALL support:

```text
Backup
Restore
Replication
Reconciliation
Event Replay
Counter Reconstruction
```

The authoritative ledger SHALL permit reconstruction of derived counters.

---

## 161. Disaster Recovery Invariant

After recovery:

```text
Authoritative Quota Allocation
+
Committed Usage
+
Active Reservations
=
Correct Remaining Quota
```

---

## 162. Quota Integrity Invariants

The system SHALL guarantee:

```text
Remaining Quota >= 0
```

for hard quotas.

Also:

```text
Consumed + Remaining + Reserved
≈
Allocated
```

subject to explicitly approved overage and accounting states.

---

## 163. Quota and Billing Integrity

For billable resources:

```text
Committed Usage
=
Billable Meter Input
```

unless an explicit billing adjustment exists.

---

## 164. Quota and Usage Relationship

The platform SHALL distinguish:

```text
Quota:
Allocated capacity

Usage:
Actual consumption

Reservation:
Temporarily held capacity

Remaining:
Available capacity
```

Example:

```text
Allocated = 50,000
Consumed = 20,000
Reserved = 5,000

Remaining =
50,000 - 20,000 - 5,000
= 25,000
```

---

## 165. Quota State Machine

Quota allocation SHALL support:

```text
CREATED
ACTIVE
DEPLETED
OVERAGE
SUSPENDED
EXPIRED
RESET
CANCELLED
```

---

## 166. Quota Lifecycle

```text
Plan Created
    ↓
Quota Defined
    ↓
Quota Allocated
    ↓
Quota Activated
    ↓
Usage Begins
    ↓
Quota Consumption
    ↓
Quota Warning
    ↓
Quota Exhaustion
    ↓
Overage / Grace / Block
    ↓
Period Reset
    ↓
Quota Reallocated
```

---

## 167. Quota Governance

Quota policy SHALL be governed through:

```text
RBAC
Policy Versioning
Approval Workflows
Audit Logs
Tenant Isolation
Change Management
```

---

## 168. Change Management

Production quota-policy changes SHALL support:

```text
Draft
Review
Approval
Scheduled Activation
Activation
Monitoring
Rollback
```

---

## 169. Canary Quota Policies

The platform MAY support gradual rollout of quota policies.

Example:

```text
1% tenants
    ↓
10%
    ↓
25%
    ↓
50%
    ↓
100%
```

---

## 170. Feature Flags

Quota behavior MAY be controlled through feature flags for safe rollout.

---

## 171. Backward Compatibility

Quota API changes SHALL preserve compatibility for supported API versions.

---

## 172. API Versioning

Quota APIs SHALL support versioning:

```text
/api/v1/quotas
/api/v2/quotas
```

when breaking changes are introduced.

---

## 173. Documentation

Quota APIs and policies SHALL be documented.

Documentation SHALL explain:

```text
Quota Types
Resource Definitions
Allocation
Consumption
Reservation
Overage
Reset
Errors
Authentication
Authorization
Rate Limits
```

---

## 174. Acceptance Criteria

## AC-QM-001

Quota allocation is tenant-isolated.

## AC-QM-002

Quota consumption is server-enforced.

## AC-QM-003

Frontend changes cannot bypass quota enforcement.

## AC-QM-004

AI agents cannot bypass quotas.

## AC-QM-005

Human users cannot bypass quotas.

## AC-QM-006

Workflows cannot bypass quotas.

## AC-QM-007

MCP tools cannot bypass quotas.

## AC-QM-008

Integrations cannot bypass quotas.

## AC-QM-009

API clients cannot bypass quotas.

## AC-QM-010

Quota reservations are atomic.

## AC-QM-011

Quota consumption is atomic.

## AC-QM-012

Duplicate requests do not double-consume quota.

## AC-QM-013

Retries remain idempotent.

## AC-QM-014

Concurrent requests cannot incorrectly oversubscribe hard quotas.

## AC-QM-015

Quota hierarchy is correctly enforced.

## AC-QM-016

Plan upgrades correctly increase effective quota.

## AC-QM-017

Plan downgrades preserve historical usage.

## AC-QM-018

Add-ons correctly increase capacity.

## AC-QM-019

Temporary quota overrides expire automatically.

## AC-QM-020

Quota resets occur at the correct period boundary.

## AC-QM-021

Quota transfers are authorized and audited.

## AC-QM-022

Quota pools correctly track shared consumption.

## AC-QM-023

Quota exhaustion generates correct notifications.

## AC-QM-024

Overage policy is correctly enforced.

## AC-QM-025

Grace capacity is correctly enforced.

## AC-QM-026

Carry-over rules work correctly.

## AC-QM-027

Quota events are idempotent.

## AC-QM-028

Quota counters reconcile with the ledger.

## AC-QM-029

Quota mutations are fully audited.

## AC-QM-030

Quota APIs return deterministic error codes.

## AC-QM-031

Quota dashboards display accurate capacity.

## AC-QM-032

AI quota forecasts do not silently modify policy.

## AC-QM-033

Quota anomalies are detectable.

## AC-QM-034

Critical quota operations fail safely.

## AC-QM-035

Quota data can be reconstructed after disaster recovery.

---

## 175. Definition of Done

The `quota_management.md` implementation SHALL be considered complete when:

* [ ] Centralized quota service exists
* [ ] Resource catalog exists
* [ ] Tenant quotas exist
* [ ] Team quotas exist
* [ ] User quotas exist
* [ ] Human-agent quotas exist
* [ ] AI-agent quotas exist
* [ ] Workflow quotas exist
* [ ] MCP quotas exist
* [ ] MCP tool quotas exist
* [ ] Integration quotas exist
* [ ] API quotas exist
* [ ] Voice quotas exist
* [ ] Storage quotas exist
* [ ] Knowledge-base quotas exist
* [ ] RAG quotas exist
* [ ] Lead-generation quotas exist
* [ ] Campaign quotas exist
* [ ] Export quotas exist
* [ ] Rate quotas exist
* [ ] Concurrency quotas exist
* [ ] Hard quotas exist
* [ ] Soft quotas exist
* [ ] Burst quotas exist
* [ ] Grace quotas exist
* [ ] Overage policies exist
* [ ] Quota reservation exists
* [ ] Atomic consumption exists
* [ ] Idempotency exists
* [ ] Retry safety exists
* [ ] Hierarchical quotas exist
* [ ] Quota pools exist
* [ ] Quota transfers exist
* [ ] Quota adjustments exist
* [ ] Temporary overrides exist
* [ ] Promotional quotas exist
* [ ] Add-on quotas exist
* [ ] Enterprise quotas exist
* [ ] Unlimited-plan safeguards exist
* [ ] Carry-over policy exists
* [ ] Automatic reset exists
* [ ] Quota ledger exists
* [ ] Usage integration exists
* [ ] Billing integration exists
* [ ] Subscription integration exists
* [ ] Credit integration exists
* [ ] Pricing-plan integration exists
* [ ] Feature-entitlement integration exists
* [ ] AI quota enforcement exists
* [ ] Human quota enforcement exists
* [ ] Workflow quota enforcement exists
* [ ] MCP quota enforcement exists
* [ ] Integration quota enforcement exists
* [ ] API quota enforcement exists
* [ ] Quota alerts exist
* [ ] Quota forecasting exists
* [ ] Anomaly detection exists
* [ ] Quota dashboard exists
* [ ] Administrative controls exist
* [ ] RBAC enforcement exists
* [ ] Audit logging exists
* [ ] Reconciliation exists
* [ ] Counter-drift detection exists
* [ ] Distributed enforcement exists
* [ ] Load testing passes
* [ ] Race-condition testing passes
* [ ] Security testing passes
* [ ] Disaster recovery testing passes
* [ ] Observability is enabled
* [ ] Production SLOs are monitored
* [ ] API documentation exists

---

## 176. Architectural Invariants

SalesGenie SHALL enforce these invariants:

```text
1. Quota decisions are server-authoritative.

2. A client cannot directly modify quota state.

3. AI cannot modify its own quota.

4. Human users cannot bypass quota policy.

5. Workflows cannot bypass quota policy.

6. MCP tools cannot bypass quota policy.

7. Integrations cannot bypass quota policy.

8. API clients cannot bypass quota policy.

9. Cross-tenant quota access is prohibited.

10. Hard quotas cannot be exceeded through race conditions.

11. Duplicate requests cannot double-consume quota.

12. Reservations cannot permanently leak capacity.

13. Historical quota events cannot be silently rewritten.

14. Every administrative quota mutation is auditable.

15. Effective quota calculation is deterministic.

16. Subscription and plan changes trigger quota recalculation.

17. Quota resets preserve historical records.

18. Billing usage remains reconcilable with committed consumption.

19. Security restrictions always override capacity grants.

20. Unlimited commercial quotas remain subject to platform safety controls.
```

---

## 177. Final Quota Control Architecture

```text
                    ┌──────────────────────┐
                    │       Clients        │
                    │ Human + AI + API     │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │    API / Gateway     │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │ Authentication       │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │ Authorization / RBAC  │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │ Feature Entitlement  │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │   Quota Decision     │
                    │       Engine         │
                    └──────────┬───────────┘
                               ↓
             ┌─────────────────┼──────────────────┐
             ↓                 ↓                  ↓
       Tenant Quota       Team/User Quota     AI/Workflow
             ↓                 ↓               /MCP Quota
             └─────────────────┼──────────────────┘
                               ↓
                    ┌──────────────────────┐
                    │ Rate / Concurrency   │
                    │      Controls        │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │ Quota Reservation    │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │ Resource Execution   │
                    │ AI / Human / MCP /   │
                    │ Workflow / API / CRM │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │ Actual Usage Meter   │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │  Quota Commit        │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │ Immutable Usage /    │
                    │ Quota Ledger         │
                    └──────────┬───────────┘
                               ↓
              ┌────────────────┼─────────────────┐
              ↓                ↓                 ↓
          Billing          Analytics          Alerts
              ↓                ↓                 ↓
          Invoices        Forecasting       Notifications
```

The Quota Management subsystem SHALL serve as the authoritative capacity-allocation and capacity-enforcement layer for SalesGenie, while remaining tightly integrated with usage tracking, feature entitlements, subscriptions, pricing, billing, credits, AI agents, human agents, workflows, MCP, integrations, APIs, and platform security.
