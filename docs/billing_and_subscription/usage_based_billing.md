# SalesGenie — Usage-Based Billing

## FAANG-Level User Requirements, System Requirements & Functional Requirements

**Document:** `usage_based_billing.md`  
**Product:** SalesGenie — Enterprise AI Customer Support, Sales, Lead Generation & Workflow Automation Platform  
**Scope:** Metered billing, usage measurement, usage aggregation, pricing, quotas, overages, credits, AI consumption, workflow execution, API consumption, communication usage, storage, voice usage, billing cycles, invoicing, payment collection, usage forecasting, AI-assisted billing, human-controlled financial operations, auditability, reconciliation, and enterprise administration.

---

## 1. Purpose

SalesGenie SHALL provide a production-grade usage-based billing platform that allows customers to pay according to measurable consumption of platform resources.

The system SHALL support usage-based billing for resources including, but not limited to:

- AI model tokens
- AI requests
- AI inference units
- Agent executions
- Workflow executions
- API requests
- Conversations
- Messages
- WhatsApp messages
- SMS messages
- Email messages
- Voice minutes
- Voice calls
- Lead enrichment
- Lead generation
- External data-source queries
- Knowledge-base retrieval
- Vector-search operations
- Document processing
- OCR
- Storage
- File processing
- Webhook events
- MCP tool executions
- Integration API calls
- Human-agent interactions
- Seats/users where applicable
- Custom enterprise meters

The system SHALL support both:

1. **Human-operated billing workflows**
2. **AI-assisted billing workflows**

AI SHALL assist with billing analysis and recommendations while remaining subject to authentication, authorization, policy, financial controls, and human approval requirements.

---

## 2. Product Principles

The usage-based billing platform SHALL follow:

1. Financial correctness
2. Deterministic metering
3. Accurate usage attribution
4. Idempotent usage ingestion
5. Immutable usage records
6. Immutable financial records
7. Tenant isolation
8. Least-privilege authorization
9. Transparent pricing
10. Explainable billing
11. Real-time or near-real-time usage visibility
12. Reliable aggregation
13. Horizontal scalability
14. Event-driven processing
15. Strong observability
16. Reconciliation
17. AI safety
18. Human-in-the-loop financial controls
19. Fault tolerance
20. Backward-compatible meter and pricing versioning

---

## 3. Actors

| Actor | Responsibility |
|---|---|
| End User | Consume SalesGenie resources |
| Organization Owner | Manage organization billing |
| Customer Admin | Manage usage and billing settings |
| Finance Admin | Manage financial operations |
| Sales Agent | Recommend plans and usage strategies |
| Support Agent | Investigate billing issues |
| Super Admin | Manage platform-wide billing |
| AI Billing Agent | Analyze usage and billing |
| AI Sales Agent | Recommend plans and upgrades |
| AI Support Agent | Explain usage and charges |
| Workflow Engine | Generate metered usage |
| AI Agent Runtime | Generate AI consumption |
| Usage Metering Service | Capture usage |
| Usage Aggregator | Aggregate usage |
| Pricing Engine | Calculate cost |
| Billing Service | Generate charges |
| Invoice Service | Generate invoices |
| Payment Service | Collect payments |
| Entitlement Service | Enforce quotas |
| Integration Services | Produce integration usage |
| Audit Service | Record billing activity |
| Reconciliation Engine | Verify financial consistency |

---

## 4. USER REQUIREMENTS

## UR-USAGE-001 — View Current Usage

Users SHALL be able to view their current resource consumption.

The dashboard SHALL display:

- Current billing period
- Total usage
- Usage by meter
- Usage by user
- Usage by AI agent
- Usage by workflow
- Usage by integration
- Usage by channel
- Usage by project
- Usage by date
- Estimated cost
- Actual billed cost
- Remaining quota
- Overage usage

---

## UR-USAGE-002 — Usage Dashboard

Customers SHALL have a dedicated usage dashboard.

Example:

```text
AI Tokens
████████████████░░░░ 78%

Workflow Executions
██████████████░░░░░░ 68%

Voice Minutes
████████████░░░░░░░░ 57%

API Requests
██████████████████░░ 89%
```

---

## UR-USAGE-003 — Meter Breakdown

Users SHALL be able to inspect usage by meter.

Supported dimensions MAY include:

```text
meter
tenant
organization
user
agent
workflow
integration
channel
project
model
provider
region
date
hour
```

---

## UR-USAGE-004 — Real-Time Usage

Where technically supported, usage SHALL be reflected in the dashboard in real time or near real time.

The system SHALL clearly distinguish:

```text
REAL-TIME
NEAR_REAL_TIME
ESTIMATED
FINALIZED
```

---

## UR-USAGE-005 — Usage Cost Estimate

Users SHALL be able to view estimated costs before the billing period ends.

Example:

```text
Current usage:
AI Tokens: 4.2M
Estimated AI cost: $31.40

Workflow executions: 8,420
Estimated workflow cost: $16.84

Projected monthly bill: $71.25
```

---

## UR-USAGE-006 — Usage-Based Pricing Transparency

Customers SHALL be able to understand:

* Meter definition
* Unit
* Unit price
* Included quota
* Overage price
* Minimum charge
* Maximum charge
* Billing frequency
* Discounts
* Credits
* Taxes

---

## UR-USAGE-007 — View Pricing

Customers SHALL be able to view usage-based pricing.

Each meter SHALL define:

```text
meter_name
unit
price_per_unit
currency
included_quantity
overage_price
pricing_model
effective_date
```

---

## UR-USAGE-008 — Usage Alerts

Customers SHALL be able to configure usage alerts.

Supported thresholds SHOULD include:

```text
50%
75%
80%
90%
95%
100%
```

Custom thresholds SHALL also be supported.

---

## UR-USAGE-009 — Budget Limits

Authorized customers SHALL be able to configure spending limits.

Example:

```text
Monthly budget: $500
Alert at: $400
Soft limit: $500
Hard limit: $550
```

---

## UR-USAGE-010 — Overage Control

Customers SHALL be able to select supported overage policies:

* Allow overage
* Warn before overage
* Require approval
* Throttle
* Block
* Automatically upgrade
* Use prepaid credits

---

## UR-USAGE-011 — Usage-Based Billing History

Customers SHALL be able to view historical usage.

The system SHALL support:

```text
Current period
Previous period
Last 3 months
Last 6 months
Last 12 months
Custom date range
```

---

## UR-USAGE-012 — Download Usage Report

Authorized users SHALL be able to export usage reports.

Supported formats MAY include:

* CSV
* JSON
* PDF

---

## UR-USAGE-013 — View Usage Invoice

Invoices SHALL clearly show usage-based charges.

Example:

```text
AI Token Usage
4,250,000 units × $0.00001
= $42.50

Workflow Executions
8,420 × $0.002
= $16.84

Voice Minutes
120 × $0.08
= $9.60
```

---

## UR-USAGE-014 — Usage by AI Model

Customers SHALL be able to view usage by model.

Example:

```text
Grok
Gemini
Mistral
```

The system SHALL support model/provider-level attribution where supported.

---

## UR-USAGE-015 — AI Usage Optimization

The AI SHALL identify opportunities to reduce cost.

Examples:

* High-token prompts
* Repeated queries
* Expensive model usage
* Inefficient workflows
* Excessive API calls
* Duplicate document processing
* Unnecessary retrieval operations

---

## UR-USAGE-016 — AI Cost Recommendation

The AI MAY recommend:

* Cheaper models
* Prompt optimization
* Caching
* Batch processing
* Workflow optimization
* Usage limits
* Plan changes
* Budget controls

AI recommendations SHALL not automatically change financial configuration without authorization.

---

## UR-USAGE-017 — Ask AI About Usage

Users SHALL be able to ask:

```text
"How much AI have we used?"

"Which workflow costs the most?"

"Why is this month's bill higher?"

"Which agent uses the most tokens?"

"How much will we spend this month?"

"How much did our Salesforce integration cost?"

"How can we reduce our usage cost?"
```

---

## UR-USAGE-018 — Human Billing Support

Human support agents SHALL be able to investigate:

* Unexpected charges
* Missing usage
* Duplicate usage
* Incorrect pricing
* Usage disputes
* Refund requests
* Credit requests
* Metering issues

---

## UR-USAGE-019 — Usage Dispute

Customers SHALL be able to dispute usage charges.

A dispute SHALL include:

```text
dispute_id
invoice_id
usage_record_ids
reason
requested_adjustment
supporting_information
status
```

---

## UR-USAGE-020 — Credits

Customers SHALL be able to receive authorized credits.

Credits MAY be:

* Promotional
* Compensation
* Service recovery
* Prepaid
* Contractual
* Administrative

---

## 5. SYSTEM REQUIREMENTS

## SR-USAGE-001 — Usage Metering Service

SalesGenie SHALL provide a dedicated Usage Metering Service responsible for collecting authoritative consumption events.

---

## SR-USAGE-002 — Usage Event Schema

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
timestamp
source_service
source_type
user_id
agent_id
workflow_id
integration_id
channel
model
provider
region
request_id
correlation_id
idempotency_key
metadata
created_at
```

---

## SR-USAGE-003 — Immutable Usage Records

Raw usage records SHALL be append-only.

Corrections SHALL be represented using adjustment events rather than destructive mutation.

---

## SR-USAGE-004 — Usage Event Idempotency

Every usage event SHALL have an idempotency key.

Duplicate events SHALL NOT result in duplicate billable usage.

---

## SR-USAGE-005 — Usage Attribution

Usage SHALL be attributable to the correct:

```text
tenant
organization
subscription
user
agent
workflow
integration
channel
model
provider
```

---

## SR-USAGE-006 — Meter Registry

The system SHALL maintain a centralized meter registry.

Each meter SHALL define:

```text
meter_id
name
description
unit
aggregation_method
pricing_model
pricing_version
effective_from
effective_until
status
dimensions
```

---

## SR-USAGE-007 — Meter Versioning

Meters SHALL be versioned.

Existing historical usage SHALL remain associated with the meter version under which it was recorded.

---

## SR-USAGE-008 — Supported Aggregation Methods

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

## SR-USAGE-009 — Usage Dimensions

The system SHALL support multidimensional usage aggregation.

Example:

```text
tenant
    ↓
organization
    ↓
user
    ↓
AI agent
    ↓
workflow
    ↓
AI model
    ↓
usage meter
```

---

## SR-USAGE-010 — Usage Pipeline

The usage pipeline SHALL support:

```text
Producer
   ↓
Event Bus
   ↓
Usage Ingestion
   ↓
Validation
   ↓
Deduplication
   ↓
Normalization
   ↓
Enrichment
   ↓
Aggregation
   ↓
Pricing
   ↓
Billing
```

---

## SR-USAGE-011 — Event Ordering

The system SHALL tolerate delayed and out-of-order usage events.

---

## SR-USAGE-012 — Late Usage

Late usage SHALL be handled using configurable policies.

Possible policies:

```text
CURRENT_PERIOD_ADJUSTMENT
PREVIOUS_PERIOD_ADJUSTMENT
NEXT_INVOICE_ADJUSTMENT
MANUAL_REVIEW
```

---

## SR-USAGE-013 — Usage Finalization

Billing periods SHALL transition through:

```text
OPEN
CLOSING
FINALIZING
FINALIZED
INVOICED
```

Finalized usage SHALL require controlled adjustment procedures.

---

## SR-USAGE-014 — Pricing Engine

The pricing engine SHALL calculate charges using:

* Meter
* Meter version
* Pricing version
* Quantity
* Tier
* Discounts
* Credits
* Contract rules
* Currency
* Tax

---

## SR-USAGE-015 — Pricing Models

The pricing engine SHALL support:

```text
FLAT_RATE
PER_UNIT
VOLUME_TIER
GRADUATED_TIER
STAIR_STEP
THRESHOLD
PACKAGE
PREPAID_CREDIT
HYBRID
CUSTOM_ENTERPRISE
```

---

## SR-USAGE-016 — Tiered Pricing

Example:

```text
0–10,000 units      → $0.01/unit
10,001–100,000      → $0.008/unit
100,001–1,000,000   → $0.005/unit
1,000,001+          → $0.003/unit
```

The system SHALL clearly define whether tiers are volume-based or graduated.

---

## SR-USAGE-017 — Included Usage

Plans SHALL support included usage.

Example:

```text
Included AI tokens: 1,000,000
Actual usage:       1,350,000
Billable overage:     350,000
```

---

## SR-USAGE-018 — Overage Pricing

Overage pricing SHALL be independently configurable from included usage.

---

## SR-USAGE-019 — Hybrid Billing

The system SHALL support plans combining:

```text
base_subscription_fee
+
included_usage
+
usage_overage
+
optional_addons
```

---

## SR-USAGE-020 — Budget Enforcement

The platform SHALL enforce:

* Soft budget
* Hard budget
* User-level budget
* Organization-level budget
* Agent-level budget
* Workflow-level budget

---

## SR-USAGE-021 — Quota Enforcement

Quota enforcement SHALL operate independently from billing calculation.

This prevents financial calculations from being coupled directly to feature availability.

---

## SR-USAGE-022 — Real-Time Cost Calculation

Where required, the pricing engine SHALL provide low-latency estimated cost calculation.

---

## SR-USAGE-023 — Financial Calculation Precision

Financial calculations SHALL use decimal-safe arithmetic.

Floating-point arithmetic SHALL NOT be used for final monetary calculations.

---

## SR-USAGE-024 — Currency

Every charge SHALL contain:

```text
currency
subtotal
discount
credit
tax
total
```

---

## SR-USAGE-025 — Tax

The billing system SHALL support configurable tax calculation.

---

## SR-USAGE-026 — Billing Period

Usage billing SHALL support:

```text
monthly
yearly
weekly
daily
custom
```

depending on the customer's billing configuration.

---

## SR-USAGE-027 — Usage-Based Invoicing

The Invoice Service SHALL generate invoices from finalized usage.

---

## SR-USAGE-028 — Invoice Immutability

Finalized invoices SHALL be immutable.

Corrections SHALL use:

* Credit notes
* Debit notes
* Adjustments
* Refunds

---

## SR-USAGE-029 — Payment Integration

Usage-based invoices SHALL integrate with the Payment Service.

---

## SR-USAGE-030 — Payment Failure

Payment failure SHALL NOT corrupt usage records.

---

## SR-USAGE-031 — Reconciliation

The system SHALL reconcile:

```text
Usage Events
     ↕
Aggregated Usage
     ↕
Rated Usage
     ↕
Invoice Items
     ↕
Invoice Total
     ↕
Payment
```

---

## SR-USAGE-032 — Tenant Isolation

Usage data SHALL be isolated by tenant.

No tenant SHALL access another tenant's usage.

---

## SR-USAGE-033 — Authorization

Access to usage data SHALL be controlled through RBAC/ABAC.

---

## SR-USAGE-034 — AI Access Control

AI agents SHALL access usage information only through authorized tools.

---

## SR-USAGE-035 — Auditability

All billing-affecting operations SHALL be audited.

---

## SR-USAGE-036 — Observability

The platform SHALL provide:

* Metrics
* Logs
* Traces
* Usage pipeline monitoring
* Billing monitoring
* Pricing monitoring
* Reconciliation monitoring

---

## 6. FUNCTIONAL REQUIREMENTS

## FR-USAGE-001 — Record Usage Event

```http
POST /api/v1/usage/events
```

Example:

```json
{
  "meter_id": "ai_tokens",
  "quantity": 12500,
  "unit": "tokens",
  "timestamp": "2026-08-28T06:00:00Z",
  "source_service": "ai_gateway",
  "agent_id": "agent_123",
  "workflow_id": "workflow_456",
  "model": "grok",
  "provider": "xai",
  "idempotency_key": "req_789"
}
```

---

## FR-USAGE-002 — Validate Usage Event

The system SHALL validate:

* Tenant
* Meter
* Meter version
* Quantity
* Unit
* Timestamp
* Source
* Authorization
* Idempotency key

Invalid events SHALL be rejected or quarantined.

---

## FR-USAGE-003 — Deduplicate Usage

The system SHALL identify duplicate events using:

```text
idempotency_key
usage_event_id
request_id
provider_event_id
```

---

## FR-USAGE-004 — Get Current Usage

```http
GET /api/v1/usage/current
```

The response SHALL contain usage grouped by meter.

---

## FR-USAGE-005 — Get Usage History

```http
GET /api/v1/usage/history
```

The API SHALL support:

* Date range
* Meter
* User
* Agent
* Workflow
* Integration
* Model
* Channel

---

## FR-USAGE-006 — Usage Aggregation

The system SHALL aggregate raw usage into billing dimensions.

Example:

```text
Raw Events
   ↓
Hourly Aggregates
   ↓
Daily Aggregates
   ↓
Billing-Period Aggregate
```

---

## FR-USAGE-007 — Usage Cost Estimate

```http
GET /api/v1/usage/cost-estimate
```

The response SHALL contain:

```text
estimated_usage
estimated_cost
current_cost
projected_cost
currency
```

---

## FR-USAGE-008 — Usage by User

```http
GET /api/v1/usage/users
```

The API SHALL provide per-user usage.

---

## FR-USAGE-009 — Usage by Agent

```http
GET /api/v1/usage/agents
```

The API SHALL provide AI-agent-level usage.

---

## FR-USAGE-010 — Usage by Workflow

```http
GET /api/v1/usage/workflows
```

The API SHALL provide workflow-level usage.

---

## FR-USAGE-011 — Usage by Integration

The system SHALL expose usage for:

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

## FR-USAGE-012 — AI Token Metering

The AI Gateway SHALL emit usage events containing, where available:

```text
input_tokens
output_tokens
cached_tokens
total_tokens
model
provider
request_id
agent_id
workflow_id
```

---

## FR-USAGE-013 — AI Request Metering

The platform SHALL support metering AI requests independently from token usage.

---

## FR-USAGE-014 — Workflow Metering

Every billable workflow execution SHALL generate a usage event.

The event SHOULD identify:

```text
workflow_id
workflow_version
execution_id
trigger
duration
status
steps_executed
tool_calls
```

---

## FR-USAGE-015 — MCP Tool Metering

MCP tool calls MAY be metered.

Example:

```text
mcp_tool_calls
mcp_server_calls
external_api_calls
```

---

## FR-USAGE-016 — Lead Generation Metering

The platform SHALL support meters for:

```text
leads_generated
leads_enriched
companies_discovered
contacts_enriched
external_searches
```

---

## FR-USAGE-017 — Communication Metering

The system SHALL support:

```text
emails_sent
messages_sent
whatsapp_messages
sms_messages
voice_minutes
voice_calls
```

---

## FR-USAGE-018 — Document Intelligence Metering

The platform SHALL support:

```text
documents_processed
pages_processed
ocr_pages
embeddings_generated
vector_searches
rag_queries
```

---

## FR-USAGE-019 — Storage Metering

The system SHALL support:

```text
GB_storage
files_stored
file_operations
data_transfer
```

---

## FR-USAGE-020 — API Metering

The platform SHALL meter:

```text
api_requests
api_requests_by_endpoint
api_requests_by_user
api_requests_by_key
```

---

## FR-USAGE-021 — Webhook Metering

The platform MAY meter:

```text
webhooks_received
webhooks_sent
webhook_retries
```

---

## FR-USAGE-022 — Usage Alerts

```http
POST /api/v1/usage/alerts
```

Example:

```json
{
  "meter_id": "ai_tokens",
  "threshold_type": "percentage",
  "threshold": 90,
  "action": "notify"
}
```

---

## FR-USAGE-023 — Budget Configuration

```http
POST /api/v1/billing/budgets
```

Supported configuration:

```text
monthly_budget
daily_budget
user_budget
agent_budget
workflow_budget
hard_limit
soft_limit
```

---

## FR-USAGE-024 — Overage Configuration

```http
POST /api/v1/billing/overage-policy
```

Supported policies:

```text
ALLOW
WARN
THROTTLE
BLOCK
REQUIRE_APPROVAL
AUTO_UPGRADE
```

---

## FR-USAGE-025 — Rate Usage

The Pricing Engine SHALL transform usage into monetary charges.

```text
Usage
 ↓
Meter
 ↓
Pricing Version
 ↓
Tier Calculation
 ↓
Discount
 ↓
Credit
 ↓
Tax
 ↓
Charge
```

---

## FR-USAGE-026 — Generate Usage Invoice

```http
POST /api/v1/billing/invoices/generate
```

The invoice SHALL contain usage line items.

---

## FR-USAGE-027 — Invoice Line Item

Each usage invoice item SHALL include:

```text
meter
quantity
unit
unit_price
tier
subtotal
discount
tax
total
pricing_version
usage_period
```

---

## FR-USAGE-028 — Billing Preview

Customers SHALL be able to preview estimated billing before invoice finalization.

---

## FR-USAGE-029 — Billing Finalization

At period close:

```text
OPEN
 ↓
CLOSING
 ↓
USAGE_FINALIZATION
 ↓
RATING
 ↓
INVOICE_GENERATION
 ↓
INVOICED
```

---

## FR-USAGE-030 — Late Usage Adjustment

Late usage SHALL create an adjustment rather than silently changing finalized historical usage.

---

## FR-USAGE-031 — Usage Correction

Authorized administrators SHALL be able to submit usage corrections.

Corrections SHALL require:

```text
reason
affected_usage
requested_change
actor
approval
audit_record
```

---

## FR-USAGE-032 — Credit Application

Credits SHALL be applied according to configured priority.

Example:

```text
promotional_credit
 ↓
service_credit
 ↓
prepaid_credit
```

---

## FR-USAGE-033 — Refund

Refunds SHALL be processed through the Billing Service.

AI SHALL NOT directly execute refunds.

---

## FR-USAGE-034 — Usage Dispute Workflow

```text
CUSTOMER DISPUTE
      ↓
SUPPORT REVIEW
      ↓
USAGE INVESTIGATION
      ↓
METER VALIDATION
      ↓
PRICING VALIDATION
      ↓
DECISION
      ↓
ADJUSTMENT / CREDIT / REJECTION
      ↓
AUDIT
```

---

## 7. USAGE-BASED BILLING MODELS

## MODEL-001 — Pure Usage

```text
Total Charge = Usage × Unit Price
```

---

## MODEL-002 — Included Usage + Overage

```text
Billable Usage
=
max(0, Actual Usage - Included Usage)

Charge
=
Billable Usage × Overage Price
```

---

## MODEL-003 — Hybrid Subscription

```text
Total
=
Base Subscription
+
Usage Charge
+
Overage
+
Add-ons
-
Credits
+
Tax
```

---

## MODEL-004 — Tiered Usage

```text
Usage
 ↓
Tier Selection
 ↓
Tier Pricing
 ↓
Charge
```

---

## MODEL-005 — Prepaid Credits

```text
Customer
 ↓
Purchases Credits
 ↓
Usage Consumes Credits
 ↓
Credit Balance Decreases
 ↓
Low Balance Alert
 ↓
Recharge / Billing
```

---

## 8. AI-BASED USAGE MANAGEMENT

## AI-USAGE-001 — AI Usage Assistant

The AI SHALL answer usage-related questions using authoritative usage tools.

---

## AI-USAGE-002 — Usage Tools

Minimum tools:

```text
get_current_usage
get_usage_history
get_usage_by_user
get_usage_by_agent
get_usage_by_workflow
get_usage_by_integration
get_usage_by_model
get_cost_estimate
get_invoice
get_budget
get_quota
get_overage_status
get_pricing
get_usage_forecast
```

---

## AI-USAGE-003 — AI Cost Analysis

AI SHALL identify:

* Highest-cost resource
* Fastest-growing resource
* Unexpected spikes
* Waste patterns
* Duplicate operations
* Expensive workflows
* Expensive models

---

## AI-USAGE-004 — AI Usage Forecast

AI MAY estimate:

```text
projected_usage
projected_cost
projected_overage
projected_budget_exhaustion
projected_quota_exhaustion
```

---

## AI-USAGE-005 — AI Optimization

AI MAY recommend:

```text
model_switch
prompt_optimization
caching
batch_processing
workflow_optimization
rate_limiting
quota_adjustment
budget_adjustment
plan_upgrade
```

---

## AI-USAGE-006 — AI Billing Explanation

AI SHALL explain invoices using actual billing records.

It SHALL distinguish:

```text
ACTUAL
ESTIMATED
PROJECTED
ADJUSTED
```

---

## AI-USAGE-007 — AI Billing Hallucination Prevention

AI SHALL NOT invent:

* Usage
* Pricing
* Credits
* Discounts
* Refunds
* Invoice values
* Quotas
* Payment status

If authoritative data is unavailable, AI SHALL explicitly state that it cannot verify the value.

---

## 9. HUMAN-BASED USAGE MANAGEMENT

## HUMAN-USAGE-001 — Customer Admin

Customer Admin SHALL be able to:

* View usage
* Configure alerts
* Configure budgets
* Configure overage policy
* View invoices
* Export reports
* Investigate usage
* Request credits
* Request refunds

---

## HUMAN-USAGE-002 — Finance Admin

Finance Admin SHALL be able to:

* Investigate charges
* Approve adjustments
* Approve credits
* Review disputes
* Review invoices
* Reconcile usage
* Review payment failures

---

## HUMAN-USAGE-003 — Support Agent

Support agents SHALL be able to:

* View authorized customer usage
* Inspect usage events
* Investigate discrepancies
* Create disputes
* Escalate billing issues

---

## HUMAN-USAGE-004 — Super Admin

Super Admin SHALL have platform-level observability subject to authorization and audit policies.

---

## 10. HUMAN + AI COLLABORATION

```text
Customer
   ↓
AI Billing Assistant
   ↓
Usage Investigation
   ↓
AI Recommendation
   ↓
Customer Confirmation
   ↓
Policy Evaluation
   ↓
Human Approval if Required
   ↓
Billing Service
   ↓
Usage/Financial Adjustment
   ↓
Audit
```

---

## 11. AI FINANCIAL SAFETY

AI SHALL NOT:

* Modify usage records directly.
* Delete usage records.
* Alter finalized invoices.
* Change prices without authorization.
* Grant unlimited credits.
* Approve its own financial request.
* Bypass budget limits.
* Disable quotas.
* Access another tenant.
* Modify payment credentials.
* Create unauthorized refunds.
* Override tax calculations.
* Circumvent billing policies.

---

## 12. API REQUIREMENTS

## Usage APIs

```text
POST   /api/v1/usage/events
GET    /api/v1/usage/current
GET    /api/v1/usage/history
GET    /api/v1/usage/summary
GET    /api/v1/usage/cost-estimate
GET    /api/v1/usage/users
GET    /api/v1/usage/agents
GET    /api/v1/usage/workflows
GET    /api/v1/usage/integrations
GET    /api/v1/usage/models
GET    /api/v1/usage/export
```

## Meter APIs

```text
GET    /api/v1/meters
GET    /api/v1/meters/{meter_id}
POST   /api/v1/meters
PATCH  /api/v1/meters/{meter_id}
```

Meter modifications SHALL be versioned.

## Pricing APIs

```text
GET    /api/v1/pricing/usage
POST   /api/v1/pricing/preview
GET    /api/v1/pricing/meters/{meter_id}
```

## Budget APIs

```text
GET    /api/v1/billing/budgets
POST   /api/v1/billing/budgets
PATCH  /api/v1/billing/budgets/{id}
DELETE /api/v1/billing/budgets/{id}
```

---

## 13. EVENT MODEL

The platform SHALL publish events such as:

```text
usage.recorded
usage.validated
usage.rejected
usage.deduplicated
usage.aggregated
usage.adjusted
usage.finalized

usage.threshold_reached
usage.quota_exhausted
usage.budget_warning
usage.budget_exceeded

usage.cost_calculated
usage.cost_estimated
usage.forecast_generated

billing.usage_rated
billing.invoice_generated
billing.invoice_finalized
billing.payment_requested
billing.payment_succeeded
billing.payment_failed

billing.credit_applied
billing.refund_requested
billing.refund_approved
billing.refund_completed

billing.dispute_created
billing.dispute_resolved

billing.reconciliation_started
billing.reconciliation_completed
billing.reconciliation_failed
```

---

## 14. USAGE BILLING WORKFLOW

```text
RESOURCE CONSUMED
       ↓
USAGE EVENT CREATED
       ↓
USAGE INGESTION
       ↓
SCHEMA VALIDATION
       ↓
TENANT VALIDATION
       ↓
METER VALIDATION
       ↓
IDEMPOTENCY CHECK
       ↓
DEDUPLICATION
       ↓
USAGE ENRICHMENT
       ↓
USAGE AGGREGATION
       ↓
PRICING ENGINE
       ↓
DISCOUNT/CREDIT
       ↓
TAX
       ↓
BILLABLE CHARGE
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

## 15. REAL-TIME USAGE WORKFLOW

```text
AI / WORKFLOW / API / INTEGRATION
              ↓
        Usage Event
              ↓
          Event Bus
              ↓
       Usage Metering
              ↓
       Aggregation Layer
              ↓
       Cost Calculation
              ↓
        Usage Dashboard
              ↓
       Threshold Engine
              ↓
     Notification / Enforcement
```

---

## 16. BUDGET ENFORCEMENT WORKFLOW

```text
USAGE EVENT
     ↓
COST CALCULATION
     ↓
CURRENT SPEND
     ↓
BUDGET CHECK
     ↓
 ┌───────────────┐
 │               │
UNDER LIMIT   OVER LIMIT
 │               │
 ↓               ↓
ALLOW        POLICY ENGINE
                 ↓
       ┌─────────┼──────────┐
       ↓         ↓          ↓
     WARN     THROTTLE     BLOCK
```

---

## 17. USAGE ALERT WORKFLOW

```text
USAGE
 ↓
AGGREGATION
 ↓
THRESHOLD CHECK
 ↓
THRESHOLD REACHED?
 ↓
YES
 ↓
CREATE ALERT
 ↓
NOTIFICATION
 ↓
AUDIT
```

The alert engine SHALL prevent duplicate notifications for the same threshold event.

---

## 18. USAGE FORECASTING WORKFLOW

```text
HISTORICAL USAGE
       ↓
CURRENT USAGE
       ↓
USAGE TREND
       ↓
SEASONAL/BEHAVIORAL SIGNALS
       ↓
FORECAST MODEL
       ↓
PROJECTED USAGE
       ↓
PRICING MODEL
       ↓
PROJECTED COST
       ↓
BUDGET COMPARISON
       ↓
AI RECOMMENDATION
```

---

## 19. USAGE DISPUTE WORKFLOW

```text
CUSTOMER
   ↓
DISPUTE
   ↓
SUPPORT AGENT
   ↓
USAGE EVENT INSPECTION
   ↓
METER VALIDATION
   ↓
PRICING VALIDATION
   ↓
INVOICE VALIDATION
   ↓
DECISION
   ↓
┌───────────────┬───────────────┐
↓               ↓               ↓
VALID         ADJUSTMENT       CREDIT
CHARGE
↓               ↓               ↓
REJECT       APPROVAL        APPROVAL
                ↓               ↓
             EXECUTE         EXECUTE
                ↓               ↓
                └──────┬────────┘
                       ↓
                     AUDIT
```

---

## 20. DATABASE REQUIREMENTS

Minimum entities:

```text
tenants
organizations
subscriptions

meters
meter_versions
meter_dimensions

usage_events
usage_event_metadata
usage_adjustments

usage_hourly_aggregates
usage_daily_aggregates
usage_billing_period_aggregates

pricing_models
pricing_versions
pricing_tiers
pricing_rules

usage_charges
usage_charge_items

budgets
budget_rules
budget_events

usage_alerts
usage_threshold_events

credits
credit_transactions

invoices
invoice_items

payments
payment_attempts
refunds

billing_disputes
billing_adjustments

usage_forecasts

reconciliation_runs
reconciliation_records

approval_requests
audit_logs
```

---

## 21. USAGE DATA MODEL

Example:

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
├── integration_id
├── channel
├── model
├── provider
├── region
├── request_id
├── correlation_id
├── idempotency_key
├── metadata
└── created_at
```

---

## 22. BILLING DATA MODEL

```text
UsageCharge
├── charge_id
├── tenant_id
├── subscription_id
├── meter_id
├── meter_version
├── pricing_version
├── usage_quantity
├── billable_quantity
├── unit_price
├── subtotal
├── discount
├── credit
├── tax
├── total
├── currency
├── billing_period_start
├── billing_period_end
└── status
```

---

## 23. FINANCIAL INVARIANTS

The system SHALL enforce:

```text
1. Every billable usage event belongs to exactly one tenant.

2. Every billable usage event references a valid meter version.

3. Duplicate usage events cannot create duplicate charges.

4. Finalized usage cannot be silently modified.

5. Finalized invoices cannot be silently modified.

6. Usage charge totals must reconcile with invoice line items.

7. Invoice totals must reconcile with payment amounts.

8. Refunds cannot exceed eligible refundable amounts.

9. Credits cannot be consumed more than once.

10. Pricing changes cannot retroactively alter historical billing.

11. Tenant A cannot access Tenant B's usage.

12. AI cannot bypass billing authorization.

13. Budget enforcement cannot be bypassed by changing client-side state.

14. Quota enforcement cannot depend solely on frontend validation.

15. Usage adjustments must be auditable.

16. Every financial mutation must have an actor.

17. Every AI financial recommendation must have a traceable source.

18. Every high-risk financial action must have an approval record.

19. Usage aggregation must be deterministic.

20. Reconciliation must detect discrepancies between usage,
    rating, invoicing, and payment.
```

---

## 24. SECURITY REQUIREMENTS

## SEC-USAGE-001

All usage APIs SHALL require authentication.

## SEC-USAGE-002

Authorization SHALL be evaluated for every tenant-scoped operation.

## SEC-USAGE-003

Usage APIs SHALL enforce tenant isolation.

## SEC-USAGE-004

Usage events SHALL not contain unnecessary sensitive information.

## SEC-USAGE-005

Sensitive metadata SHALL be encrypted where appropriate.

## SEC-USAGE-006

API keys SHALL not be stored in plaintext.

## SEC-USAGE-007

AI usage tools SHALL use least-privilege permissions.

## SEC-USAGE-008

Financial mutation endpoints SHALL require elevated authorization.

## SEC-USAGE-009

Usage ingestion SHALL support request authentication and source verification.

## SEC-USAGE-010

Administrative adjustments SHALL require audit records.

---

## 25. PERFORMANCE REQUIREMENTS

## PERF-USAGE-001

The usage ingestion system SHALL support horizontal scaling.

## PERF-USAGE-002

Usage ingestion SHALL be asynchronous where appropriate.

## PERF-USAGE-003

Usage processing SHALL tolerate burst traffic.

## PERF-USAGE-004

Usage dashboards SHALL use pre-aggregated data where necessary.

## PERF-USAGE-005

Billing calculations SHALL not block primary user workflows.

## PERF-USAGE-006

Usage event processing SHALL support backpressure.

## PERF-USAGE-007

Large usage exports SHALL be processed asynchronously.

---

## 26. RELIABILITY REQUIREMENTS

The platform SHALL support:

```text
idempotent ingestion
retry-safe processing
dead-letter queues
replayable events
checkpointing
backpressure
event persistence
reconciliation
failure recovery
```

A temporary outage in billing SHALL NOT cause loss of usage events.

---

## 27. OBSERVABILITY REQUIREMENTS

The platform SHALL expose metrics including:

```text
usage_events_received_total
usage_events_processed_total
usage_events_rejected_total
usage_events_duplicate_total

usage_processing_latency
usage_processing_lag

usage_aggregation_latency
usage_rating_latency

billing_calculations_total
billing_calculation_failures_total

invoice_generation_total
invoice_generation_failures_total

budget_threshold_events_total
quota_exhaustion_total

payment_success_total
payment_failure_total

usage_disputes_total
usage_adjustments_total

reconciliation_mismatch_total
```

---

## 28. ALERTING REQUIREMENTS

The platform SHALL alert operators about:

* Usage ingestion failures
* Usage processing backlog
* Event duplication spikes
* Meter configuration errors
* Pricing calculation failures
* Unexpected usage spikes
* Budget enforcement failures
* Quota enforcement failures
* Invoice generation failures
* Payment failures
* Reconciliation mismatches
* Abnormal credit issuance
* Abnormal refunds
* Cross-tenant authorization failures
* AI billing-tool failures

---

## 29. SUPER ADMIN REQUIREMENTS

Super Admin SHALL be able to view:

```text
Total billable usage
Usage by tenant
Usage by plan
Usage by meter
Usage by model
Usage by provider
Usage by integration
Usage by AI agent
Usage by workflow

Total usage revenue
Usage-based revenue
Overage revenue
Credit volume
Refund volume
Disputed charges
Budget violations
Quota violations
```

Super Admin SHALL be able to investigate usage anomalies while respecting authorization and audit policies.

---

## 30. USAGE ANOMALY DETECTION

The platform SHOULD detect:

```text
sudden usage spike
unusual token consumption
abnormal workflow execution
unexpected API traffic
duplicate usage
unusual integration traffic
unexpected voice usage
unexpected lead-enrichment activity
```

The AI MAY generate an anomaly explanation.

Example:

```text
AI Analysis:

API usage increased 340% compared with the previous
billing period.

Primary contributor:
Lead Intelligence Workflow

Cause:
The workflow execution frequency increased from
2,100 to 9,400 executions.

Estimated additional cost:
$73.20
```

---

## 31. AI + HUMAN COST OPTIMIZATION

```text
USAGE ANALYTICS
       ↓
AI COST ANALYSIS
       ↓
OPTIMIZATION RECOMMENDATION
       ↓
CUSTOMER REVIEW
       ↓
HUMAN APPROVAL IF REQUIRED
       ↓
POLICY ENGINE
       ↓
CONFIGURATION CHANGE
       ↓
MONITORING
       ↓
COST IMPACT MEASUREMENT
```

---

## 32. ENTERPRISE REQUIREMENTS

Enterprise customers SHALL support:

* Custom meters
* Custom pricing
* Contract pricing
* Committed usage
* Minimum spend
* Maximum spend
* Spending pools
* Department-level allocation
* Cost centers
* Project-level billing
* Multi-organization billing
* Consolidated invoices
* Custom billing periods
* Purchase orders
* Manual adjustments
* Contractual credits
* Dedicated billing policies

---

## 33. COST ALLOCATION

The platform SHOULD support cost allocation by:

```text
Organization
Department
Team
User
Agent
Workflow
Project
Integration
Channel
Cost Center
```

Example:

```text
Engineering       → $1,240
Sales             → $3,480
Customer Support  → $2,190
Marketing         → $1,730
```

---

## 34. MULTI-TENANT BILLING

Each tenant SHALL have independent:

```text
meters
pricing
usage
budgets
quotas
subscriptions
credits
invoices
payments
billing policies
```

Cross-tenant aggregation SHALL only be available to authorized platform administrators.

---

## 35. DATA RETENTION

The system SHALL define retention policies for:

```text
raw usage events
aggregated usage
billing records
invoices
audit records
reconciliation records
usage forecasts
```

Financial records SHALL follow applicable regulatory and business retention requirements.

---

## 36. TEST REQUIREMENTS

## Unit Tests

The platform SHALL test:

```text
meter validation
unit conversion
aggregation
deduplication
tier calculation
included usage
overage calculation
discount calculation
credit calculation
tax calculation
budget calculation
forecast calculation
```

---

## Integration Tests

The platform SHALL test:

```text
AI Gateway → Usage Service
Workflow Engine → Usage Service
MCP → Usage Service
Integration Services → Usage Service
Usage Service → Pricing Engine
Pricing Engine → Billing Service
Billing Service → Invoice Service
Invoice Service → Payment Service
```

---

## Failure Tests

The platform SHALL test:

```text
duplicate usage
missing usage
late usage
out-of-order usage
event replay
event bus outage
database outage
pricing-service outage
billing-service outage
payment-provider outage
invoice-generation failure
```

---

## Security Tests

The platform SHALL test:

```text
tenant isolation
IDOR
RBAC bypass
ABAC bypass
AI tool authorization
API-key abuse
usage-event forgery
replay attacks
financial endpoint abuse
privilege escalation
```

---

## AI Tests

The AI test suite SHALL include:

```text
usage hallucination
pricing hallucination
wrong tenant access
incorrect cost explanation
incorrect optimization recommendation
unauthorized budget modification
unauthorized refund
unauthorized credit
prompt injection
tool abuse
approval bypass
```

---

## 37. ACCEPTANCE CRITERIA

The implementation SHALL be considered production-ready when:

* [ ] Usage events can be ingested reliably.
* [ ] Usage events are idempotent.
* [ ] Duplicate events do not create duplicate charges.
* [ ] Usage is correctly attributed to tenants.
* [ ] Usage can be aggregated by multiple dimensions.
* [ ] Meters are versioned.
* [ ] Pricing is versioned.
* [ ] Included usage is supported.
* [ ] Overage pricing is supported.
* [ ] Tiered pricing is supported.
* [ ] Hybrid subscription + usage billing is supported.
* [ ] AI token usage is metered.
* [ ] Workflow usage is metered.
* [ ] MCP tool usage can be metered.
* [ ] API usage is metered.
* [ ] Integration usage is metered.
* [ ] Voice usage is metered.
* [ ] Lead-generation usage is metered.
* [ ] Document processing usage is metered.
* [ ] Storage usage is metered.
* [ ] Users can view current usage.
* [ ] Users can view historical usage.
* [ ] Users can view estimated cost.
* [ ] Users can view projected cost.
* [ ] Usage thresholds can trigger alerts.
* [ ] Budgets can be configured.
* [ ] Overage policies can be configured.
* [ ] Quotas are enforced server-side.
* [ ] Usage invoices contain detailed line items.
* [ ] Finalized invoices are immutable.
* [ ] Late usage is handled safely.
* [ ] Usage disputes are supported.
* [ ] Credits are auditable.
* [ ] Refunds require appropriate authorization.
* [ ] AI can explain usage.
* [ ] AI can analyze usage.
* [ ] AI can forecast usage.
* [ ] AI cannot bypass billing controls.
* [ ] Human approval exists for high-risk financial operations.
* [ ] Usage is reconciled against invoices.
* [ ] Payment state is reconciled.
* [ ] Tenant isolation is enforced.
* [ ] Security events are audited.
* [ ] Billing metrics are observable.
* [ ] Usage pipeline failures are recoverable.
* [ ] Super Admin can monitor platform-wide usage.
* [ ] Automated tests cover correctness, reliability, security,
  concurrency, billing, and AI safety.

---

## 38. FAANG-LEVEL ARCHITECTURE

```text
                         ┌──────────────────────────┐
                         │       SalesGenie UI      │
                         │ Customer / Admin / AI UI │
                         └────────────┬─────────────┘
                                      │
                                      ↓
                         ┌──────────────────────────┐
                         │       API Gateway        │
                         └────────────┬─────────────┘
                                      │
          ┌───────────────────────────┼───────────────────────────┐
          ↓                           ↓                           ↓
┌──────────────────┐        ┌──────────────────┐        ┌──────────────────┐
│ AI Agent Runtime │        │ Workflow Engine  │        │ Integration Svcs │
└────────┬─────────┘        └────────┬─────────┘        └────────┬─────────┘
         │                           │                           │
         └───────────────────────────┼───────────────────────────┘
                                     ↓
                           ┌────────────────────┐
                           │   Usage Event Bus  │
                           └─────────┬──────────┘
                                     ↓
                           ┌────────────────────┐
                           │ Usage Metering Svc │
                           └─────────┬──────────┘
                                     ↓
                           ┌────────────────────┐
                           │ Usage Aggregator   │
                           └─────────┬──────────┘
                                     ↓
                           ┌────────────────────┐
                           │   Pricing Engine   │
                           └─────────┬──────────┘
                                     ↓
                           ┌────────────────────┐
                           │   Billing Service  │
                           └─────────┬──────────┘
                                     ↓
                           ┌────────────────────┐
                           │  Invoice Service   │
                           └─────────┬──────────┘
                                     ↓
                           ┌────────────────────┐
                           │  Payment Service   │
                           └────────────────────┘

Additional Control Plane:

Usage
  ↓
Budget Engine
  ↓
Quota Engine
  ↓
Alert Engine
  ↓
Notification Service

Cross-Cutting:

Audit
Observability
Reconciliation
RBAC
Tenant Isolation
Security
AI Guardrails
```

---

## 39. FINAL SYSTEM REQUIREMENT

SalesGenie's usage-based billing platform SHALL provide a **financially correct, highly scalable, multi-tenant, event-driven usage metering and billing system** capable of accurately converting platform consumption into transparent, auditable charges.

The complete control flow SHALL be:

```text
RESOURCE CONSUMPTION
        ↓
AUTHORITATIVE USAGE EVENT
        ↓
VALIDATION
        ↓
IDEMPOTENCY
        ↓
TENANT ATTRIBUTION
        ↓
METER VERSION
        ↓
AGGREGATION
        ↓
PRICING VERSION
        ↓
INCLUDED USAGE
        ↓
OVERAGE / TIER CALCULATION
        ↓
DISCOUNT
        ↓
CREDIT
        ↓
TAX
        ↓
FINAL CHARGE
        ↓
INVOICE
        ↓
PAYMENT
        ↓
RECONCILIATION
        ↓
AUDIT
```

AI-assisted billing SHALL operate through:

```text
AI REQUEST
    ↓
AUTHENTICATED USER CONTEXT
    ↓
TENANT CONTEXT
    ↓
RBAC/ABAC
    ↓
AUTHORIZED BILLING TOOLS
    ↓
AUTHORITATIVE USAGE DATA
    ↓
AI ANALYSIS
    ↓
EXPLAINABLE RECOMMENDATION
    ↓
USER CONFIRMATION
    ↓
HUMAN APPROVAL WHEN REQUIRED
    ↓
AUTHORIZED DOMAIN SERVICE
    ↓
FINANCIAL EXECUTION
    ↓
AUDIT
    ↓
RECONCILIATION
```

No frontend client, AI agent, workflow, MCP server, integration, external system, webhook, or internal service SHALL bypass the authoritative Usage Metering, Pricing, Billing, Authorization, Entitlement, Payment, Audit, and Reconciliation controls.
