# SalesGenie — Metered Billing

## FAANG-Level User Requirements, System Requirements & Functional Requirements

**Document:** `metered_billing.md`  
**Product:** SalesGenie — Enterprise AI Customer Support, Sales, Lead Generation & Workflow Automation Platform  
**Scope:** Meter definition, usage event collection, consumption measurement, usage aggregation, rating, tiered pricing, quotas, overages, credits, AI consumption, workflow execution, API usage, integrations, communications, voice, storage, document processing, MCP usage, billing periods, invoices, reconciliation, monitoring, AI-assisted billing, human billing operations, and enterprise controls.

---

## 1. Purpose

SalesGenie SHALL provide a production-grade metered billing subsystem that measures billable resource consumption and converts validated usage into deterministic financial charges.

The system SHALL support:

- Real-time metering
- Near-real-time metering
- Batch metering
- Event-based metering
- API-based metering
- Time-based metering
- Quantity-based metering
- Duration-based metering
- Storage metering
- Token metering
- Request metering
- Execution metering
- Message metering
- Call/minute metering
- Seat/user metering
- Custom enterprise meters

The system SHALL support both:

1. Human-operated metering and billing workflows
2. AI-assisted metering analysis and billing workflows

AI SHALL never become the authoritative source of financial truth. Authoritative usage SHALL originate from trusted SalesGenie services and validated usage events.

---

## 2. Metering Principles

The metering architecture SHALL follow:

1. Accuracy
2. Determinism
3. Idempotency
4. Immutability
5. Traceability
6. Tenant isolation
7. Strong attribution
8. Versioned meters
9. Versioned pricing
10. Event-driven processing
11. Fault tolerance
12. Replayability
13. Auditability
14. Reconciliation
15. Horizontal scalability
16. Low-latency usage visibility
17. Financial safety
18. AI safety
19. Least privilege
20. Backward compatibility

---

## 3. Actors

| Actor | Responsibilities |
|---|---|
| End User | Consume metered SalesGenie resources |
| Sales Agent | Generate leads and customer interactions |
| Support Agent | Handle customer conversations |
| Organization Owner | Manage organization usage |
| Customer Admin | Configure usage policies |
| Finance Admin | Manage billing and metering disputes |
| Super Admin | Monitor platform-wide usage |
| AI Agent | Consume metered resources |
| AI Billing Agent | Analyze usage |
| AI Sales Agent | Recommend usage optimization |
| Workflow Engine | Generate execution usage |
| MCP Runtime | Generate tool usage |
| AI Gateway | Generate model/token usage |
| Integration Services | Generate integration usage |
| Usage Metering Service | Collect and validate usage |
| Aggregation Service | Aggregate usage |
| Pricing Engine | Rate usage |
| Billing Service | Generate charges |
| Invoice Service | Generate invoices |
| Payment Service | Collect payment |
| Reconciliation Engine | Verify financial consistency |
| Audit Service | Record financial activity |

---

## 4. USER REQUIREMENTS

## UR-METER-001 — View Metered Usage

Users SHALL be able to view consumption for every enabled billable meter.

The dashboard SHALL display:

- Meter name
- Current quantity
- Included quantity
- Billable quantity
- Unit
- Unit price
- Estimated charge
- Actual charge
- Remaining allowance
- Overage quantity
- Billing period

---

## UR-METER-002 — Meter Dashboard

SalesGenie SHALL provide a centralized metering dashboard.

Example:

```text
Current Billing Period

AI Tokens
4.2M / 5M included
84%

Workflow Executions
8,420 / 10,000
84%

API Requests
92,300 / 100,000
92%

Voice Minutes
1,240 / 2,000
62%
```

---

## UR-METER-003 — Meter Details

Users SHALL be able to inspect:

* Meter description
* Measurement unit
* Aggregation method
* Pricing model
* Included quantity
* Overage rate
* Current consumption
* Historical consumption
* Pricing version
* Meter version

---

## UR-METER-004 — Usage by Dimension

Authorized users SHALL be able to break usage down by:

```text
Organization
Department
Team
User
Agent
Workflow
Workflow Version
Integration
Channel
Project
Model
Provider
API Key
MCP Server
MCP Tool
Date
Hour
Region
```

---

## UR-METER-005 — Usage History

Users SHALL be able to inspect historical usage.

Supported ranges:

```text
Current period
Previous period
Last 7 days
Last 30 days
Last 90 days
Last 12 months
Custom range
```

---

## UR-METER-006 — Usage Comparison

Users SHALL be able to compare usage between billing periods.

Example:

```text
AI Token Usage

Previous Month: 2.8M
Current Month:  4.2M
Change:         +50%
```

---

## UR-METER-007 — Cost Visibility

Users SHALL be able to see estimated financial impact of current metered usage.

---

## UR-METER-008 — Usage Alerts

Users SHALL be able to configure alerts for:

* Quantity threshold
* Percentage threshold
* Cost threshold
* Rate-of-growth threshold
* Budget threshold

---

## UR-METER-009 — Custom Thresholds

Authorized users SHALL be able to define custom thresholds.

Example:

```text
Alert when:
AI tokens > 4,000,000
OR
Monthly spend > $400
OR
Workflow executions > 90,000
```

---

## UR-METER-010 — Usage Budgets

Users SHALL be able to configure:

* Organization budget
* Department budget
* User budget
* Agent budget
* Workflow budget
* Integration budget
* Project budget

---

## UR-METER-011 — Quota Visibility

Users SHALL be able to see:

```text
Included
Consumed
Remaining
Overage
```

for every quota-enabled meter.

---

## UR-METER-012 — Overage Visibility

Users SHALL be clearly informed when usage exceeds included limits.

---

## UR-METER-013 — Overage Policy

Authorized users SHALL be able to configure:

```text
Allow
Warn
Throttle
Require approval
Block
Auto-upgrade
Use prepaid credits
```

---

## UR-METER-014 — Usage-Based Invoice

Invoices SHALL show metered usage in understandable line items.

Example:

```text
AI Tokens
1,250,000 billable tokens
× $0.00001
= $12.50

Workflow Executions
3,400 executions
× $0.002
= $6.80
```

---

## UR-METER-015 — Usage Export

Authorized users SHALL be able to export metering information in:

* CSV
* JSON
* PDF

---

## UR-METER-016 — Usage Dispute

Users SHALL be able to dispute an individual metered charge or group of charges.

---

## UR-METER-017 — Metering Explanation

Users SHALL be able to understand how SalesGenie calculated a charge.

The explanation SHALL identify:

```text
Meter
Quantity
Unit
Pricing Version
Rate
Included Quantity
Billable Quantity
Discount
Credit
Tax
Final Charge
```

---

## UR-METER-018 — AI Usage Assistant

Users SHALL be able to ask AI:

```text
"What have we consumed this month?"

"Which resource costs the most?"

"Which workflow is generating the most usage?"

"Why did our bill increase?"

"Which model is consuming the most tokens?"

"How much remaining quota do we have?"
```

---

## 5. SYSTEM REQUIREMENTS

## SR-METER-001 — Meter Registry

SalesGenie SHALL maintain a centralized Meter Registry.

Each meter SHALL have:

```text
meter_id
meter_name
description
unit
meter_type
aggregation_method
dimensions
pricing_model
meter_version
status
effective_from
effective_until
created_at
updated_at
```

---

## SR-METER-002 — Meter Types

The system SHALL support at minimum:

```text
COUNT
QUANTITY
TOKEN
REQUEST
EXECUTION
DURATION
TIME
STORAGE
DATA_TRANSFER
MESSAGE
CALL
MINUTE
SEAT
DISTINCT_ENTITY
CUSTOM
```

---

## SR-METER-003 — Meter Versioning

Every production meter SHALL be versioned.

A meter modification SHALL create a new version rather than modifying historical semantics.

---

## SR-METER-004 — Meter Lifecycle

Meters SHALL support:

```text
DRAFT
ACTIVE
DEPRECATED
RETIRED
```

---

## SR-METER-005 — Meter Event Schema

Every usage event SHALL contain:

```text
usage_event_id
tenant_id
organization_id
subscription_id
meter_id
meter_version
quantity
unit
event_timestamp
source_service
source_type
user_id
agent_id
workflow_id
workflow_version
integration_id
channel
project_id
model
provider
mcp_server_id
mcp_tool_id
api_key_id
request_id
correlation_id
idempotency_key
metadata
created_at
```

---

## SR-METER-006 — Authoritative Usage Source

Usage SHALL be generated by authoritative domain services.

Examples:

```text
AI Gateway
Workflow Engine
MCP Runtime
Lead Intelligence
Integration Services
Communication Services
Document Intelligence
Storage Service
API Gateway
```

Frontend clients SHALL NOT be trusted as authoritative metering sources.

---

## SR-METER-007 — Event Validation

The Usage Metering Service SHALL validate:

* Authentication context
* Tenant
* Meter
* Meter version
* Unit
* Quantity
* Timestamp
* Source service
* Idempotency key
* Authorization
* Required dimensions

---

## SR-METER-008 — Quantity Validation

The system SHALL reject invalid quantities such as:

```text
NaN
Infinity
negative quantities
unsupported precision
invalid units
overflow values
```

unless explicitly supported by the meter definition.

---

## SR-METER-009 — Idempotency

Every billable usage event SHALL have a unique idempotency key.

Repeated submission of the same event SHALL not produce duplicate billable usage.

---

## SR-METER-010 — Deduplication

The system SHALL support deduplication based on:

```text
idempotency_key
usage_event_id
provider_event_id
request_id
source_event_id
```

---

## SR-METER-011 — Immutable Raw Usage

Raw usage events SHALL be append-only.

The system SHALL NOT silently overwrite historical usage.

---

## SR-METER-012 — Usage Corrections

Corrections SHALL use adjustment events.

Example:

```text
Original:
+100 units

Correction:
-20 units

Net:
80 units
```

---

## SR-METER-013 — Unit Normalization

The metering service SHALL normalize compatible units.

Example:

```text
seconds → minutes
bytes → GB
milliseconds → seconds
tokens → million tokens
```

The original quantity SHALL remain traceable.

---

## SR-METER-014 — Multi-Dimensional Metering

The system SHALL support multiple dimensions on the same meter.

Example:

```text
Meter:
AI_TOKENS

Dimensions:
tenant
user
agent
workflow
model
provider
```

---

## SR-METER-015 — Aggregation

The metering system SHALL support:

```text
SUM
COUNT
DISTINCT_COUNT
MAX
MIN
AVERAGE
DURATION
WEIGHTED_SUM
CUSTOM
```

---

## SR-METER-016 — Aggregation Windows

The system SHALL support:

```text
real-time
minute
hour
day
billing-period
custom
```

---

## SR-METER-017 — Late Events

The system SHALL support delayed usage events.

Late events SHALL be classified according to configurable policies.

---

## SR-METER-018 — Out-of-Order Events

The system SHALL support out-of-order event arrival without corrupting aggregate usage.

---

## SR-METER-019 — Event Replay

Authorized operators SHALL be able to replay usage events safely.

Replay SHALL remain idempotent.

---

## SR-METER-020 — Dead-Letter Queue

Invalid or repeatedly failing usage events SHALL be routed to a dead-letter queue.

---

## SR-METER-021 — Usage Reconciliation

The system SHALL compare:

```text
Source Consumption
       ↓
Usage Events
       ↓
Aggregates
       ↓
Rated Usage
       ↓
Invoice Items
```

---

## SR-METER-022 — Pricing Integration

The metering platform SHALL integrate with the Pricing Engine.

The Pricing Engine SHALL determine financial value from validated usage.

---

## SR-METER-023 — Pricing Version

Every rated usage record SHALL reference the pricing version used.

---

## SR-METER-024 — Historical Pricing

Historical usage SHALL remain associated with the pricing rules applicable at the time of billing.

---

## SR-METER-025 — Included Usage

Meters SHALL support included quantities.

Example:

```text
Included:
1,000,000 tokens

Actual:
1,250,000 tokens

Billable:
250,000 tokens
```

---

## SR-METER-026 — Overage

The metering system SHALL expose overage quantity to the billing system.

```text
overage_quantity =
max(0, actual_quantity - included_quantity)
```

---

## SR-METER-027 — Tiered Metering

The system SHALL support:

```text
volume pricing
graduated pricing
threshold pricing
package pricing
custom enterprise pricing
```

---

## SR-METER-028 — Budget Enforcement

Metered usage SHALL integrate with the Budget Engine.

---

## SR-METER-029 — Quota Enforcement

Metered usage SHALL integrate with the Entitlement/Quota Service.

---

## SR-METER-030 — Real-Time Enforcement

For high-risk resource consumption, the platform SHALL support synchronous or near-real-time quota checks.

---

## SR-METER-031 — Async Metering

Non-critical usage processing SHOULD be asynchronous.

---

## SR-METER-032 — Metering Reliability

A temporary billing outage SHALL NOT result in permanent usage loss.

---

## SR-METER-033 — Metering Storage

The system SHALL maintain durable storage for raw usage events.

---

## SR-METER-034 — Aggregated Storage

The system SHALL maintain optimized aggregate storage for dashboards and reporting.

---

## SR-METER-035 — Tenant Isolation

All usage records SHALL contain tenant context.

Cross-tenant usage access SHALL be prohibited.

---

## 6. FUNCTIONAL REQUIREMENTS

## FR-METER-001 — Create Meter

Authorized administrators SHALL be able to create a meter.

```http
POST /api/v1/meters
```

Example:

```json
{
  "name": "ai_tokens",
  "unit": "tokens",
  "meter_type": "TOKEN",
  "aggregation_method": "SUM"
}
```

---

## FR-METER-002 — Retrieve Meter

```http
GET /api/v1/meters/{meter_id}
```

The response SHALL contain current meter metadata and version.

---

## FR-METER-003 — List Meters

```http
GET /api/v1/meters
```

Supported filters:

```text
status
type
unit
tenant
product
```

---

## FR-METER-004 — Create Meter Version

```http
POST /api/v1/meters/{meter_id}/versions
```

---

## FR-METER-005 — Activate Meter

```http
POST /api/v1/meters/{meter_id}/activate
```

Activation SHALL require appropriate authorization.

---

## FR-METER-006 — Deprecate Meter

```http
POST /api/v1/meters/{meter_id}/deprecate
```

Historical records SHALL remain readable.

---

## FR-METER-007 — Record Usage

```http
POST /api/v1/usage/events
```

Example:

```json
{
  "meter_id": "ai_tokens",
  "meter_version": 3,
  "quantity": 18500,
  "unit": "tokens",
  "event_timestamp": "2026-08-28T06:00:00Z",
  "source_service": "ai_gateway",
  "agent_id": "agent_123",
  "workflow_id": "workflow_456",
  "model": "grok",
  "provider": "xai",
  "idempotency_key": "req_987"
}
```

---

## FR-METER-008 — Validate Usage

The service SHALL validate every event before accepting it into the authoritative usage stream.

---

## FR-METER-009 — Deduplicate Usage

If an identical event is received twice:

```text
First Event:
ACCEPTED

Second Event:
DUPLICATE
```

Only the first event SHALL contribute to billable usage.

---

## FR-METER-010 — Get Current Metered Usage

```http
GET /api/v1/usage/current
```

The response SHALL include:

```text
meter
quantity
unit
included
remaining
overage
estimated_cost
```

---

## FR-METER-011 — Get Metered Usage History

```http
GET /api/v1/usage/history
```

Supported filters:

```text
date
meter
user
agent
workflow
integration
channel
model
provider
project
```

---

## FR-METER-012 — Get Usage by User

```http
GET /api/v1/usage/users
```

---

## FR-METER-013 — Get Usage by Agent

```http
GET /api/v1/usage/agents
```

---

## FR-METER-014 — Get Usage by Workflow

```http
GET /api/v1/usage/workflows
```

---

## FR-METER-015 — Get Usage by Integration

```http
GET /api/v1/usage/integrations
```

The platform SHALL support usage attribution for:

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

---

## FR-METER-016 — Get Usage by Model

```http
GET /api/v1/usage/models
```

---

## FR-METER-017 — Get Usage by MCP Tool

```http
GET /api/v1/usage/mcp-tools
```

The system SHALL support:

```text
MCP Server
MCP Tool
Tool Execution
Execution Duration
External API Calls
```

---

## FR-METER-018 — Get Usage by API Key

```http
GET /api/v1/usage/api-keys
```

Sensitive key material SHALL never be returned.

---

## 7. AI TOKEN METERING

## FR-METER-019

The AI Gateway SHALL emit token usage events.

Supported dimensions:

```text
input_tokens
output_tokens
cached_tokens
total_tokens
model
provider
agent
workflow
tenant
user
```

---

## FR-METER-020

The platform SHALL support different pricing for:

```text
input tokens
output tokens
cached tokens
reasoning tokens
embedding tokens
```

where applicable.

---

## FR-METER-021

Token usage SHALL be attributable to the originating AI request.

---

## 8. AI REQUEST METERING

## FR-METER-022

Every billable AI request SHALL generate a metering event.

The event SHALL include:

```text
request_id
model
provider
agent
workflow
duration
status
token_usage
```

---

## 9. WORKFLOW METERING

## FR-METER-023

Every billable workflow execution SHALL generate usage.

The event SHOULD contain:

```text
workflow_id
workflow_version
execution_id
trigger_type
duration
steps_executed
tool_calls
external_calls
status
```

---

## FR-METER-024

The system SHALL support meters for:

```text
workflow_executions
workflow_steps
workflow_duration
workflow_tool_calls
workflow_external_api_calls
```

---

## 10. LEAD GENERATION METERING

## FR-METER-025

SalesGenie SHALL support metering for:

```text
leads_generated
companies_discovered
contacts_discovered
leads_enriched
contacts_enriched
external_searches
lead_verifications
```

---

## 11. COMMUNICATION METERING

## FR-METER-026

SalesGenie SHALL support:

```text
emails_sent
emails_received
messages_sent
messages_received
WhatsApp_messages
SMS_messages
voice_calls
voice_minutes
```

---

## 12. DOCUMENT INTELLIGENCE METERING

## FR-METER-027

SalesGenie SHALL support:

```text
documents_processed
pages_processed
OCR_pages
embeddings_generated
RAG_queries
vector_searches
document_extractions
```

---

## 13. STORAGE METERING

## FR-METER-028

SalesGenie SHALL support:

```text
GB_storage
file_count
file_operations
data_transfer
```

---

## 14. API METERING

## FR-METER-029

The API Gateway SHALL support:

```text
api_requests
successful_requests
failed_requests
requests_by_endpoint
requests_by_api_key
requests_by_user
```

---

## 15. INTEGRATION METERING

## FR-METER-030

Integration services SHALL emit metering events for billable external operations.

Examples:

```text
CRM API Calls
Email API Calls
Calendar API Calls
Storage API Calls
Social Media API Calls
Support API Calls
Messaging API Calls
```

---

## 16. USAGE AGGREGATION

## FR-METER-031

The system SHALL aggregate raw events into optimized usage windows.

```text
Raw Events
    ↓
Minute Aggregates
    ↓
Hourly Aggregates
    ↓
Daily Aggregates
    ↓
Billing Period Aggregates
```

---

## FR-METER-032

Aggregation SHALL be deterministic.

Running the same event set through the aggregation engine SHALL produce the same result.

---

## FR-METER-033

Aggregates SHALL remain traceable to source events.

---

## 17. METERED PRICING

## FR-METER-034

The pricing engine SHALL calculate:

```text
Billable Quantity
×
Applicable Unit Price
=
Usage Charge
```

---

## FR-METER-035

The pricing engine SHALL support:

```text
flat unit pricing
tiered pricing
graduated pricing
volume pricing
threshold pricing
package pricing
custom enterprise pricing
```

---

## FR-METER-036

Example graduated pricing:

```text
First 10,000 units
→ $0.01/unit

Next 90,000 units
→ $0.008/unit

Next 900,000 units
→ $0.005/unit
```

---

## 18. INCLUDED USAGE

## FR-METER-037

Plans SHALL support included usage.

Example:

```text
Plan:
Professional

Included:
2,000,000 AI tokens

Actual:
2,700,000

Billable:
700,000
```

---

## 19. OVERAGE

## FR-METER-038

The system SHALL calculate overage independently.

```text
overage =
max(actual_usage - included_usage, 0)
```

---

## FR-METER-039

Overage SHALL be clearly visible to customers.

---

## 20. BILLING PERIOD FINALIZATION

## FR-METER-040

Metered usage SHALL progress through:

```text
OPEN
 ↓
CLOSING
 ↓
FINALIZING
 ↓
FINALIZED
 ↓
RATED
 ↓
INVOICED
```

---

## FR-METER-041

Finalized usage SHALL not be silently changed.

---

## FR-METER-042

Late events after finalization SHALL create controlled adjustments.

---

## 21. USAGE ADJUSTMENTS

## FR-METER-043

Authorized users SHALL be able to create adjustments.

Adjustment records SHALL contain:

```text
adjustment_id
original_usage_event
quantity_change
reason
actor
approval
timestamp
audit_id
```

---

## FR-METER-044

Financially significant adjustments SHALL require approval.

---

## 22. BUDGET AND QUOTA INTEGRATION

## FR-METER-045

Every usage event SHALL be eligible for budget/quota evaluation.

---

## FR-METER-046

Budget evaluation SHALL support:

```text
organization
department
team
user
agent
workflow
integration
project
```

---

## FR-METER-047

Quota enforcement SHALL support:

```text
ALLOW
WARN
THROTTLE
BLOCK
REQUIRE_APPROVAL
AUTO_UPGRADE
```

---

## 23. USAGE ALERTING

## FR-METER-048

The system SHALL generate alerts when usage crosses configured thresholds.

---

## FR-METER-049

Duplicate threshold notifications SHALL be prevented.

---

## FR-METER-050

Alerts SHALL support:

```text
email
in-app
Slack
Microsoft Teams
webhook
SMS
```

subject to configured integrations.

---

## 24. AI-BASED METERING MANAGEMENT

## AI-METER-001 — AI Usage Analysis

AI SHALL analyze authoritative metering data.

---

## AI-METER-002 — AI Usage Questions

The AI SHALL support questions such as:

```text
"How many tokens did our support agents use?"

"Which workflow generated the most usage?"

"Why is API usage increasing?"

"Which integration consumes the most resources?"

"How much overage are we generating?"

"Which department is spending the most?"
```

---

## AI-METER-003 — AI Usage Forecasting

AI MAY estimate:

```text
future usage
future overage
future quota exhaustion
future spend
budget exhaustion date
```

---

## AI-METER-004 — AI Metering Anomaly Detection

AI MAY detect:

```text
usage spikes
unexpected growth
duplicate usage
abnormal agent behavior
abnormal workflow executions
unusual API traffic
unexpected integration usage
```

---

## AI-METER-005 — AI Meter Optimization

AI MAY recommend:

```text
model optimization
workflow optimization
caching
batch processing
rate limiting
quota adjustment
budget adjustment
integration optimization
```

---

## AI-METER-006 — AI Meter Configuration

AI MAY prepare a meter configuration proposal.

Example:

```text
AI Proposal

Meter:
lead_enrichment

Unit:
lead

Suggested price:
$0.03/lead

Reason:
Current external provider cost averages $0.021/lead.

Status:
Awaiting human approval
```

AI SHALL NOT activate financially impactful pricing changes without authorization.

---

## 25. HUMAN-BASED METERING MANAGEMENT

## HUMAN-METER-001 — Customer Admin

Customer Admin SHALL be able to:

* View meters
* View usage
* Configure alerts
* Configure budgets
* Configure quotas
* Configure overage behavior
* Export usage
* Review invoices

---

## HUMAN-METER-002 — Finance Admin

Finance Admin SHALL be able to:

* Investigate usage
* Review rated charges
* Approve adjustments
* Review disputes
* Apply authorized credits
* Review reconciliation
* Review billing anomalies

---

## HUMAN-METER-003 — Super Admin

Super Admin SHALL be able to:

* Create meters
* Version meters
* Activate/deprecate meters
* View platform-wide usage
* Monitor metering health
* Investigate anomalies
* Review reconciliation failures

---

## 26. AI + HUMAN WORKFLOW

```text
Usage Generated
      ↓
Metering Service
      ↓
Usage Validation
      ↓
Aggregation
      ↓
AI Analysis
      ↓
Recommendation
      ↓
Human Review
      ↓
Policy Engine
      ↓
Authorized Execution
      ↓
Billing
      ↓
Audit
```

---

## 27. AI FINANCIAL SAFETY REQUIREMENTS

AI SHALL NOT directly:

* Delete usage events
* Rewrite historical usage
* Change finalized usage
* Change finalized invoices
* Modify pricing without authorization
* Grant unrestricted credits
* Issue unauthorized refunds
* Disable billing controls
* Disable quotas
* Bypass tenant isolation
* Bypass RBAC
* Bypass approval workflows
* Modify payment credentials
* Manipulate metering events

---

## 28. AI TOOL REQUIREMENTS

AI billing agents SHALL use controlled tools such as:

```text
get_meter
get_meter_version
get_current_usage
get_usage_history
get_usage_by_user
get_usage_by_agent
get_usage_by_workflow
get_usage_by_integration
get_usage_by_model
get_usage_by_mcp_tool
get_usage_forecast
get_usage_anomalies
get_budget
get_quota
get_overage
get_pricing
get_invoice
create_meter_proposal
create_usage_adjustment_request
create_billing_review_request
```

Financial mutation tools SHALL require explicit authorization.

---

## 29. API REQUIREMENTS

## Meter APIs

```text
GET    /api/v1/meters
POST   /api/v1/meters
GET    /api/v1/meters/{meter_id}
PATCH  /api/v1/meters/{meter_id}
POST   /api/v1/meters/{meter_id}/versions
POST   /api/v1/meters/{meter_id}/activate
POST   /api/v1/meters/{meter_id}/deprecate
```

---

## Usage APIs

```text
POST   /api/v1/usage/events
GET    /api/v1/usage/current
GET    /api/v1/usage/history
GET    /api/v1/usage/summary
GET    /api/v1/usage/users
GET    /api/v1/usage/agents
GET    /api/v1/usage/workflows
GET    /api/v1/usage/integrations
GET    /api/v1/usage/models
GET    /api/v1/usage/mcp-tools
GET    /api/v1/usage/api-keys
GET    /api/v1/usage/export
```

---

## Usage Adjustment APIs

```text
POST   /api/v1/usage/adjustments
GET    /api/v1/usage/adjustments
GET    /api/v1/usage/adjustments/{id}
POST   /api/v1/usage/adjustments/{id}/approve
POST   /api/v1/usage/adjustments/{id}/reject
```

---

## 30. EVENT REQUIREMENTS

SalesGenie SHALL publish events including:

```text
usage.recorded
usage.validated
usage.rejected
usage.duplicate_detected
usage.normalized
usage.aggregated
usage.adjusted
usage.finalized

meter.created
meter.version_created
meter.activated
meter.deprecated

usage.threshold_reached
usage.budget_warning
usage.budget_exceeded
usage.quota_exhausted
usage.overage_started

usage.anomaly_detected
usage.forecast_generated

usage.rated
usage.rating_failed

billing.usage_invoice_generated
billing.usage_invoice_finalized

billing.adjustment_requested
billing.adjustment_approved
billing.adjustment_rejected

billing.reconciliation_started
billing.reconciliation_completed
billing.reconciliation_failed
```

---

## 31. DATABASE REQUIREMENTS

Minimum entities:

```text
meters
meter_versions
meter_dimensions

usage_events
usage_event_metadata
usage_event_sources
usage_event_adjustments

usage_minute_aggregates
usage_hourly_aggregates
usage_daily_aggregates
usage_billing_period_aggregates

pricing_models
pricing_versions
pricing_tiers
pricing_rules

rated_usage
usage_charges
usage_charge_items

budgets
budget_rules
budget_events

quotas
quota_events

usage_alerts
usage_threshold_events

usage_forecasts
usage_anomalies

billing_periods
invoices
invoice_items

reconciliation_runs
reconciliation_records

approval_requests
audit_logs
```

---

## 32. DATA MODEL

```text
Meter
├── meter_id
├── name
├── description
├── type
├── unit
├── aggregation_method
├── dimensions
├── status
└── versions
```

```text
MeterVersion
├── meter_version_id
├── meter_id
├── version
├── configuration
├── effective_from
├── effective_until
├── created_by
└── created_at
```

```text
UsageEvent
├── usage_event_id
├── tenant_id
├── organization_id
├── subscription_id
├── meter_id
├── meter_version
├── quantity
├── unit
├── timestamp
├── source_service
├── source_type
├── user_id
├── agent_id
├── workflow_id
├── workflow_version
├── integration_id
├── channel
├── project_id
├── model
├── provider
├── mcp_server_id
├── mcp_tool_id
├── api_key_id
├── request_id
├── correlation_id
├── idempotency_key
├── metadata
└── created_at
```

---

## 33. RATING MODEL

```text
Validated Usage
       ↓
Meter Version
       ↓
Pricing Version
       ↓
Included Quantity
       ↓
Billable Quantity
       ↓
Tier Selection
       ↓
Unit Price
       ↓
Discount
       ↓
Credit
       ↓
Tax
       ↓
Final Charge
```

---

## 34. USAGE-TO-BILLING WORKFLOW

```text
RESOURCE CONSUMED
        ↓
DOMAIN SERVICE
        ↓
USAGE EVENT
        ↓
AUTHENTICATION
        ↓
SCHEMA VALIDATION
        ↓
METER VALIDATION
        ↓
TENANT VALIDATION
        ↓
IDEMPOTENCY
        ↓
DEDUPLICATION
        ↓
UNIT NORMALIZATION
        ↓
ENRICHMENT
        ↓
AGGREGATION
        ↓
METER FINALIZATION
        ↓
PRICING ENGINE
        ↓
RATING
        ↓
BILLING
        ↓
INVOICE
        ↓
PAYMENT
        ↓
RECONCILIATION
        ↓
AUDIT
```

---

## 35. REAL-TIME METERING WORKFLOW

```text
AI / WORKFLOW / API / INTEGRATION
             ↓
       Usage Event
             ↓
        Event Bus
             ↓
      Metering Service
             ↓
     Validation Layer
             ↓
     Deduplication
             ↓
       Aggregator
             ↓
      Usage Database
             ↓
      Cost Estimator
             ↓
       Budget Engine
             ↓
       Quota Engine
             ↓
       Alert Engine
             ↓
      Customer UI
```

---

## 36. METERED QUOTA ENFORCEMENT

```text
RESOURCE REQUEST
       ↓
IDENTITY
       ↓
TENANT
       ↓
METER
       ↓
CURRENT USAGE
       ↓
QUOTA CHECK
       ↓
      ┌───────────────┐
      │               │
   ALLOWED          EXCEEDED
      │               │
      ↓               ↓
 EXECUTE        POLICY ENGINE
                      ↓
             ┌────────┼────────┐
             ↓        ↓        ↓
           WARN    THROTTLE   BLOCK
```

---

## 37. Overage WORKFLOW

```text
Usage
 ↓
Current Period Aggregate
 ↓
Included Quantity Check
 ↓
Usage > Included?
 ↓
YES
 ↓
Calculate Overage
 ↓
Apply Overage Price
 ↓
Create Usage Charge
 ↓
Notify Customer
 ↓
Continue / Throttle / Block
```

---

## 38. USAGE ADJUSTMENT WORKFLOW

```text
Usage Discrepancy
       ↓
Investigation
       ↓
Adjustment Request
       ↓
Authorization Check
       ↓
Approval Required?
       ↓
YES
       ↓
Human Approval
       ↓
Adjustment Event
       ↓
Recalculate Aggregate
       ↓
Recalculate Charge
       ↓
Invoice Adjustment
       ↓
Audit
       ↓
Reconciliation
```

---

## 39. USAGE RECONCILIATION

The reconciliation engine SHALL compare:

```text
Source Metrics
      ↕
Usage Events
      ↕
Aggregates
      ↕
Rated Usage
      ↕
Invoice Items
      ↕
Invoice Total
```

Any mismatch SHALL produce a reconciliation exception.

---

## 40. RECONCILIATION EXCEPTION

Example:

```text
Meter:
AI_TOKENS

Source Service:
4,250,000 tokens

Metering:
4,250,000 tokens

Aggregate:
4,250,000 tokens

Rated:
4,150,000 tokens

Difference:
100,000 tokens

Status:
RECONCILIATION_FAILURE
```

The system SHALL prevent silent financial discrepancies.

---

## 41. SECURITY REQUIREMENTS

## SEC-METER-001

All metering APIs SHALL require authentication.

## SEC-METER-002

All tenant-scoped queries SHALL enforce tenant authorization.

## SEC-METER-003

Meter administration SHALL require elevated privileges.

## SEC-METER-004

Financially impactful meter changes SHALL require appropriate approval.

## SEC-METER-005

Usage events SHALL be protected against tampering.

## SEC-METER-006

Sensitive metadata SHALL be encrypted where required.

## SEC-METER-007

API keys SHALL never be stored or exposed in plaintext.

## SEC-METER-008

Usage events SHALL support source authentication.

## SEC-METER-009

AI tools SHALL use least-privilege access.

## SEC-METER-010

Administrative usage adjustments SHALL always be audited.

---

## 42. RELIABILITY REQUIREMENTS

The metering subsystem SHALL support:

```text
idempotent processing
durable event storage
retries
dead-letter queues
event replay
checkpointing
backpressure
failure recovery
reconciliation
```

---

## 43. PERFORMANCE REQUIREMENTS

The metering subsystem SHALL:

* Support horizontal scaling.
* Support burst traffic.
* Support asynchronous event processing.
* Support low-latency usage reads.
* Avoid blocking primary application workflows.
* Support high-cardinality dimensions.
* Support efficient aggregation.
* Support asynchronous exports.
* Support backpressure.

---

## 44. OBSERVABILITY REQUIREMENTS

The platform SHALL expose:

```text
meter_events_received_total
meter_events_processed_total
meter_events_rejected_total
meter_events_duplicate_total

meter_processing_latency
meter_processing_lag

meter_aggregation_latency
meter_aggregation_failures

meter_rating_latency
meter_rating_failures

meter_adjustments_total
meter_adjustment_failures

meter_overage_events_total
meter_quota_exhaustion_total
meter_budget_events_total

meter_reconciliation_mismatch_total
```

---

## 45. MONITORING

Operators SHALL be able to monitor:

```text
Event throughput
Processing latency
Processing backlog
Duplicate rate
Rejection rate
Dead-letter queue size
Aggregation lag
Rating failures
Meter configuration errors
Usage anomalies
Quota violations
Budget violations
Reconciliation failures
```

---

## 46. ENTERPRISE METERING

Enterprise customers SHALL support:

```text
custom meters
custom units
custom dimensions
custom pricing
custom aggregation
committed usage
minimum spend
maximum spend
spending pools
department allocation
cost centers
project allocation
contract pricing
custom billing periods
```

---

## 47. COST ALLOCATION

Metered usage SHALL support cost attribution by:

```text
Organization
Department
Team
User
Agent
Workflow
Integration
Project
Channel
Cost Center
```

Example:

```text
Sales
    AI Usage       $1,420
    Workflow       $680
    Enrichment     $920

Support
    AI Usage       $2,180
    Voice          $740
    Messaging      $430
```

---

## 48. METERING ANOMALY DETECTION

The platform SHOULD identify:

```text
unexpected usage spike
unusual growth
duplicate events
abnormal token consumption
abnormal workflow frequency
abnormal API traffic
unusual MCP activity
unusual integration activity
unexpected voice usage
```

---

## 49. AI ANOMALY EXPLANATION

Example:

```text
Metering Anomaly Detected

Meter:
workflow_executions

Current usage:
9,420

Expected usage:
3,100

Increase:
+203%

Primary contributor:
Lead Enrichment Workflow

Likely cause:
Workflow schedule changed from hourly to every 15 minutes.

Estimated additional usage:
6,320 executions

Recommended action:
Review workflow schedule.
```

AI SHALL distinguish between observed facts and inferred causes.

---

## 50. DATA RETENTION

The platform SHALL define retention policies for:

```text
raw usage events
usage aggregates
meter versions
pricing references
rated usage
adjustments
reconciliation records
audit logs
usage forecasts
anomaly records
```

Historical billing records SHALL remain accessible according to applicable retention requirements.

---

## 51. TEST REQUIREMENTS

## Unit Tests

The platform SHALL test:

```text
meter validation
quantity validation
unit conversion
aggregation
deduplication
idempotency
meter versioning
pricing selection
included usage
overage calculation
tier calculation
budget evaluation
quota evaluation
adjustment calculation
```

---

## Integration Tests

The platform SHALL test:

```text
AI Gateway → Metering
Workflow Engine → Metering
MCP Runtime → Metering
Integration Services → Metering
API Gateway → Metering

Metering → Aggregator
Aggregator → Pricing
Pricing → Billing
Billing → Invoice
Invoice → Payment
Billing → Reconciliation
```

---

## Failure Tests

The system SHALL test:

```text
duplicate events
late events
out-of-order events
missing events
replayed events
event-bus outage
database outage
aggregation failure
pricing failure
billing failure
payment failure
network timeout
dead-letter processing
```

---

## Security Tests

The system SHALL test:

```text
tenant isolation
IDOR
RBAC bypass
ABAC bypass
privilege escalation
usage-event forgery
replay attacks
API-key abuse
meter manipulation
pricing manipulation
AI tool abuse
approval bypass
```

---

## AI Tests

The AI metering system SHALL test:

```text
usage hallucination
pricing hallucination
wrong tenant access
incorrect usage explanation
incorrect forecasting
incorrect anomaly diagnosis
unauthorized meter modification
unauthorized pricing modification
unauthorized credit
unauthorized refund
prompt injection
tool abuse
```

---

## 52. FINANCIAL INVARIANTS

The platform SHALL guarantee:

```text
1. Every billable event belongs to exactly one tenant.

2. Every billable event references a valid meter version.

3. Duplicate events cannot create duplicate charges.

4. Historical raw usage cannot be silently modified.

5. Historical pricing cannot be silently changed.

6. Aggregation is deterministic.

7. Rated usage is traceable to usage records.

8. Invoice items are traceable to rated usage.

9. Adjustments are explicitly represented.

10. Credits cannot be consumed more than once.

11. Refunds cannot exceed eligible amounts.

12. AI cannot bypass billing authorization.

13. Frontend state cannot override server-side metering.

14. Quotas cannot be bypassed by client-side manipulation.

15. Budget enforcement is server-side.

16. Every financial adjustment has an actor.

17. Every high-risk adjustment has an approval record.

18. Every meter configuration change is auditable.

19. Every pricing reference is versioned.

20. Reconciliation detects material discrepancies.
```

---

## 53. FAANG-LEVEL METERING ARCHITECTURE

```text
                         ┌──────────────────────────┐
                         │       SalesGenie UI      │
                         └────────────┬─────────────┘
                                      │
                                      ↓
                         ┌──────────────────────────┐
                         │       API Gateway        │
                         └────────────┬─────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────┐
        ↓                             ↓                             ↓
┌─────────────────┐         ┌─────────────────┐          ┌──────────────────┐
│   AI Gateway    │         │ Workflow Engine │          │ Integration Svcs │
└────────┬────────┘         └────────┬────────┘          └────────┬─────────┘
         │                           │                            │
         └───────────────────────────┼────────────────────────────┘
                                     ↓
                         ┌──────────────────────────┐
                         │     Usage Event Bus      │
                         └────────────┬─────────────┘
                                      ↓
                         ┌──────────────────────────┐
                         │ Usage Metering Service   │
                         └────────────┬─────────────┘
                                      ↓
                         ┌──────────────────────────┐
                         │ Validation + Dedup       │
                         └────────────┬─────────────┘
                                      ↓
                         ┌──────────────────────────┐
                         │   Usage Aggregator       │
                         └────────────┬─────────────┘
                                      ↓
                    ┌─────────────────┴─────────────────┐
                    ↓                                   ↓
          ┌──────────────────┐                ┌──────────────────┐
          │ Budget / Quota   │                │ Pricing Engine   │
          │ Engine           │                │                  │
          └────────┬─────────┘                └────────┬─────────┘
                   │                                   │
                   └─────────────────┬─────────────────┘
                                     ↓
                            ┌─────────────────┐
                            │ Billing Service │
                            └────────┬────────┘
                                     ↓
                            ┌─────────────────┐
                            │ Invoice Service │
                            └────────┬────────┘
                                     ↓
                            ┌─────────────────┐
                            │ Payment Service │
                            └─────────────────┘

Cross-Cutting:

┌─────────────┐
│ Audit       │
└─────────────┘

┌─────────────┐
│ Monitoring  │
└─────────────┘

┌─────────────┐
│ Reconcile   │
└─────────────┘

┌─────────────┐
│ AI Guardrail│
└─────────────┘
```

---

## 54. END-TO-END METERING WORKFLOW

```text
RESOURCE CONSUMPTION
        ↓
AUTHORITATIVE DOMAIN EVENT
        ↓
USAGE EVENT
        ↓
AUTHENTICATION
        ↓
TENANT VALIDATION
        ↓
METER VALIDATION
        ↓
UNIT VALIDATION
        ↓
IDEMPOTENCY CHECK
        ↓
DEDUPLICATION
        ↓
ENRICHMENT
        ↓
NORMALIZATION
        ↓
AGGREGATION
        ↓
QUOTA CHECK
        ↓
BUDGET CHECK
        ↓
THRESHOLD CHECK
        ↓
METER FINALIZATION
        ↓
PRICING ENGINE
        ↓
INCLUDED USAGE
        ↓
OVERAGE
        ↓
TIER CALCULATION
        ↓
DISCOUNT
        ↓
CREDIT
        ↓
TAX
        ↓
RATED USAGE
        ↓
INVOICE ITEM
        ↓
INVOICE
        ↓
PAYMENT
        ↓
RECONCILIATION
        ↓
AUDIT
```

---

## 55. PRODUCTION ACCEPTANCE CRITERIA

The metered billing subsystem SHALL be considered production-ready when:

* [ ] Meter Registry is implemented.
* [ ] Meter versions are supported.
* [ ] Meter lifecycle is supported.
* [ ] Usage events are durable.
* [ ] Usage events are validated.
* [ ] Usage events are idempotent.
* [ ] Duplicate events are detected.
* [ ] Usage is tenant-isolated.
* [ ] Usage is attributable to users.
* [ ] Usage is attributable to AI agents.
* [ ] Usage is attributable to workflows.
* [ ] Usage is attributable to integrations.
* [ ] Usage is attributable to models.
* [ ] Usage is attributable to MCP tools.
* [ ] Usage is attributable to API keys.
* [ ] Token metering is supported.
* [ ] Request metering is supported.
* [ ] Workflow metering is supported.
* [ ] Lead-generation metering is supported.
* [ ] Communication metering is supported.
* [ ] Voice metering is supported.
* [ ] Document processing metering is supported.
* [ ] Storage metering is supported.
* [ ] API metering is supported.
* [ ] Usage aggregation is deterministic.
* [ ] Late events are supported.
* [ ] Out-of-order events are supported.
* [ ] Replay is supported.
* [ ] Dead-letter processing is supported.
* [ ] Included usage is supported.
* [ ] Overage is supported.
* [ ] Tiered pricing is supported.
* [ ] Usage budgets are supported.
* [ ] Usage quotas are supported.
* [ ] Usage alerts are supported.
* [ ] Usage exports are supported.
* [ ] Usage history is supported.
* [ ] Usage forecasting is supported.
* [ ] Usage anomaly detection is supported.
* [ ] Usage adjustments are audited.
* [ ] Billing reconciliation is implemented.
* [ ] Financial invariants are enforced.
* [ ] AI can explain usage using authoritative data.
* [ ] AI cannot modify financial records without authorization.
* [ ] Human approval exists for high-risk billing changes.
* [ ] Tenant isolation is tested.
* [ ] Security controls are tested.
* [ ] Failure recovery is tested.
* [ ] Metering observability is implemented.
* [ ] Super Admin monitoring is implemented.
* [ ] Enterprise custom meters are supported.

---

## 56. FINAL REQUIREMENT

SalesGenie's Metered Billing subsystem SHALL function as the authoritative consumption-measurement layer between platform resource consumption and the billing system.

The canonical architecture SHALL be:

```text
                 SALES GENIE RESOURCE
                         ↓
             ┌───────────────────────┐
             │ AI / Workflow / API   │
             │ MCP / Integration     │
             └───────────┬───────────┘
                         ↓
                AUTHORITATIVE EVENT
                         ↓
                USAGE METERING
                         ↓
             VALIDATION + IDEMPOTENCY
                         ↓
                   AGGREGATION
                         ↓
                 BUDGET / QUOTA
                         ↓
                  METER FINALIZE
                         ↓
                   PRICING/RATING
                         ↓
                    BILLING
                         ↓
                    INVOICE
                         ↓
                    PAYMENT
                         ↓
                 RECONCILIATION
                         ↓
                       AUDIT
```

AI-assisted metering SHALL follow:

```text
USER
  ↓
AI BILLING ASSISTANT
  ↓
AUTHORIZED TOOL
  ↓
AUTHORITATIVE METER DATA
  ↓
AI ANALYSIS
  ↓
EXPLANATION / RECOMMENDATION
  ↓
USER CONFIRMATION
  ↓
HUMAN APPROVAL WHEN REQUIRED
  ↓
AUTHORIZED DOMAIN SERVICE
  ↓
METER / BILLING CHANGE
  ↓
AUDIT
  ↓
RECONCILIATION
```

The metering subsystem SHALL remain the **single authoritative source of measured consumption**, while the Pricing Engine remains responsible for monetary rating and the Billing Service remains responsible for financial lifecycle management.

No frontend application, AI agent, workflow, MCP server, integration, API client, webhook, or external provider SHALL be permitted to bypass authoritative metering, authorization, quota, budget, billing, audit, and reconciliation controls.
