# Analytics Data Model — User, System, and Functional Requirements

**Project:** SalesGenie  
**Document:** `analytics_data_model.md`  
**Classification:** Enterprise / FAANG-Level Product & Engineering Requirements  
**Scope:** Analytics Data Model for AI + Human Sales, Customer Support, Lead Intelligence, Workflow Automation, Omnichannel Engagement, and Platform Operations

---

## 1. Purpose

The SalesGenie Analytics Data Model defines the canonical analytical representation of platform data required to support:

- Product analytics
- Sales analytics
- Lead-generation analytics
- Customer-support analytics
- AI-agent analytics
- Human-agent analytics
- Omnichannel analytics
- Conversation analytics
- Workflow analytics
- Campaign analytics
- Revenue analytics
- Subscription analytics
- Usage and quota analytics
- Customer-success analytics
- Operational analytics
- Security and compliance analytics
- Executive reporting
- AI/ML analytics
- Real-time and near-real-time dashboards
- Data science and experimentation

The model MUST support both **AI-generated activity** and **human-generated activity** while preserving attribution, lineage, tenant isolation, temporal consistency, data quality, privacy, and analytical correctness.

---

## 2. Design Principles

The analytics data model MUST follow these principles:

1. **Multi-tenant by design**
2. **AI and human activity parity**
3. **Event-driven architecture**
4. **Immutable source events**
5. **Canonical analytical entities**
6. **Fact/dimension modeling**
7. **Slowly Changing Dimensions where required**
8. **Event-time correctness**
9. **Idempotent ingestion**
10. **Exactly-once analytical semantics where feasible**
11. **At-least-once ingestion tolerance**
12. **Late-arriving data support**
13. **Schema versioning**
14. **Data lineage**
15. **Data quality enforcement**
16. **Privacy-aware analytics**
17. **PII minimization**
18. **Role-aware access**
19. **Tenant-level isolation**
20. **Real-time analytical capability**
21. **Historical analytical reproducibility**
22. **Backward-compatible schema evolution**
23. **AI explainability and attribution**
24. **Human accountability**
25. **Auditability**
26. **Cost-efficient analytical storage**
27. **High-cardinality awareness**
28. **Observability**
29. **Data contract enforcement**
30. **Separation of operational and analytical workloads**

---

## 3. Scope

The Analytics Data Model covers:

- Organizations
- Tenants
- Users
- Roles
- Teams
- Sales agents
- Support agents
- AI agents
- Customers
- Leads
- Contacts
- Accounts
- Companies
- Opportunities
- Campaigns
- Conversations
- Messages
- Channels
- Sessions
- Activities
- Tasks
- Workflows
- Workflow executions
- Workflow actions
- AI model interactions
- AI tool calls
- Knowledge-base interactions
- RAG retrievals
- Recommendations
- Human interventions
- Customer interactions
- Tickets
- Calls
- Emails
- WhatsApp messages
- Social interactions
- Lead enrichment
- Lead scoring
- Conversions
- Revenue
- Subscriptions
- Usage
- Quotas
- Costs
- Experiments
- Feature usage
- Product events
- Security events
- Compliance events
- Data-quality events

---

## 4. User Requirements

## UR-001 — Executive Analytics

The system SHALL allow authorized executives to understand:

- Revenue
- Growth
- Customer acquisition
- Customer retention
- Lead generation
- Conversion rates
- Sales performance
- AI performance
- Human-agent performance
- Customer-support performance
- Product adoption
- Usage
- Cost
- Churn
- Operational health

---

## UR-002 — Sales Analytics

Sales users SHALL be able to analyze:

- Leads generated
- Leads qualified
- Leads contacted
- Leads responded
- Meetings booked
- Opportunities created
- Opportunities won
- Opportunities lost
- Pipeline value
- Conversion rates
- Sales cycle duration
- Revenue generated
- Revenue influenced by AI
- Revenue influenced by humans

---

## UR-003 — Lead Analytics

The system SHALL provide analytical visibility into the complete lead lifecycle:

```text
discovered
    ↓
enriched
    ↓
scored
    ↓
qualified
    ↓
assigned
    ↓
contacted
    ↓
engaged
    ↓
meeting_booked
    ↓
opportunity_created
    ↓
converted
    ↓
customer
```

---

## UR-004 — AI Analytics

Authorized users SHALL be able to measure:

* AI interactions
* AI-generated messages
* AI decisions
* AI recommendations
* AI tool calls
* AI workflow executions
* AI response latency
* AI success rate
* AI escalation rate
* AI intervention rate
* AI token consumption
* AI cost
* AI conversion influence
* AI hallucination indicators
* AI policy violations
* AI safety events

---

## UR-005 — Human Analytics

The system SHALL measure:

* Human activities
* Human conversations
* Human responses
* Human interventions
* Human escalations
* Human conversions
* Human resolution times
* Human productivity
* Human workload
* Human sales performance

---

## UR-006 — AI + Human Attribution

Every analytical activity SHOULD support attribution:

```text
actor_type:
    HUMAN
    AI_AGENT
    SYSTEM
    AUTOMATION
    HYBRID
```

The system SHALL distinguish:

* AI-only activity
* Human-only activity
* AI-assisted human activity
* Human-assisted AI activity
* Automated system activity

---

## UR-007 — Omnichannel Analytics

Users SHALL be able to analyze customer interactions by:

* Web
* Email
* WhatsApp
* SMS
* Voice
* Phone
* Slack
* Microsoft Teams
* Facebook
* Instagram
* LinkedIn
* Other configured channels

---

## UR-008 — Conversation Analytics

Users SHALL be able to analyze:

* Conversation volume
* Conversation duration
* Message volume
* Response time
* Resolution time
* Sentiment
* Intent
* Topic
* Escalation
* AI involvement
* Human involvement
* Conversion
* Customer satisfaction

---

## UR-009 — Workflow Analytics

Users SHALL be able to analyze:

* Workflow executions
* Workflow success
* Workflow failures
* Workflow duration
* Workflow actions
* Action latency
* Retry counts
* AI decisions
* Human approvals
* Automation outcomes

---

## UR-010 — Campaign Analytics

Users SHALL be able to analyze:

* Campaign reach
* Deliveries
* Opens
* Clicks
* Replies
* Meetings
* Conversions
* Revenue
* Cost
* ROI
* AI contribution
* Human contribution

---

## UR-011 — Customer Analytics

Users SHALL be able to analyze:

* Customer lifecycle
* Customer engagement
* Customer health
* Product usage
* Support interactions
* Revenue
* Expansion
* Contraction
* Churn risk
* Retention

---

## UR-012 — Product Analytics

Product teams SHALL be able to measure:

* Feature adoption
* Active users
* Active organizations
* Session activity
* Workflow adoption
* AI usage
* Integration usage
* Channel usage
* Retention
* Conversion
* Drop-off

---

## UR-013 — Subscription Analytics

Authorized billing users SHALL be able to analyze:

* Subscription lifecycle
* Plan adoption
* Upgrades
* Downgrades
* Cancellations
* Renewals
* Trials
* MRR
* ARR
* Expansion revenue
* Churned revenue
* Usage
* Quota consumption

---

## UR-014 — Cost Analytics

The system SHALL provide cost visibility for:

* LLM usage
* Embeddings
* Vector search
* Storage
* Compute
* Messaging
* Voice
* Email
* External APIs
* Workflow execution
* Data enrichment

---

## UR-015 — Real-Time Analytics

Authorized users SHALL be able to access near-real-time metrics for:

* Active conversations
* Active sessions
* AI agents
* Human agents
* Workflow executions
* Leads
* Messages
* Errors
* Security events
* Usage
* Quotas

---

## UR-016 — Historical Analytics

Users SHALL be able to query historical analytical data across configurable retention periods.

---

## UR-017 — Filtering

Users SHALL be able to filter analytics by:

* Tenant
* Organization
* User
* Team
* Agent
* AI agent
* Human agent
* Customer
* Lead
* Campaign
* Channel
* Geography
* Industry
* Segment
* Product
* Plan
* Date
* Time
* Event type
* Workflow
* Model
* Integration

---

## UR-018 — Drill-Down

Users SHALL be able to drill down:

```text
Metric
  ↓
Dimension
  ↓
Entity
  ↓
Event
  ↓
Source record
```

---

## UR-019 — Export

Authorized users SHALL be able to export analytical datasets in supported formats such as:

* CSV
* JSON
* XLSX
* Parquet

---

## UR-020 — Dashboard Consumption

The model SHALL support dashboards for:

* Executive
* Sales
* Marketing
* Customer Success
* Support
* AI Operations
* Product
* Finance
* Security
* Compliance
* System Operations

---

## 5. System Requirements

## SR-001 — Multi-Tenant Architecture

Every analytical fact and tenant-scoped dimension SHALL include tenant context where applicable.

Minimum tenant identifiers SHOULD include:

```text
tenant_id
organization_id
workspace_id
```

---

## SR-002 — Canonical Identifiers

All analytical entities SHALL use stable globally unique identifiers.

Required identifiers SHOULD include:

```text
event_id
tenant_id
user_id
customer_id
lead_id
account_id
contact_id
conversation_id
message_id
workflow_id
execution_id
campaign_id
subscription_id
agent_id
ai_agent_id
```

---

## SR-003 — Event Time

All events SHALL support:

```text
event_id
event_time
ingestion_time
processing_time
```

The analytical platform SHALL distinguish event time from ingestion time.

---

## SR-004 — Immutable Events

Raw analytical events SHALL be immutable after ingestion.

Corrections SHALL be represented using:

* Versioned events
* Correction events
* Reprocessing
* Backfill jobs

---

## SR-005 — Schema Versioning

Every event schema SHALL include:

```text
schema_name
schema_version
event_type
```

Schema evolution SHALL maintain backward compatibility where possible.

---

## SR-006 — Fact Tables

The analytical warehouse SHOULD use fact tables for measurable activities.

Core facts SHOULD include:

```text
fact_events
fact_leads
fact_lead_activities
fact_conversations
fact_messages
fact_calls
fact_emails
fact_workflow_executions
fact_workflow_actions
fact_ai_interactions
fact_ai_tool_calls
fact_rag_retrievals
fact_human_interactions
fact_campaign_events
fact_opportunities
fact_revenue
fact_subscriptions
fact_usage
fact_costs
fact_product_events
fact_security_events
```

---

## SR-007 — Dimension Tables

Core dimensions SHOULD include:

```text
dim_date
dim_time
dim_tenant
dim_organization
dim_user
dim_team
dim_role
dim_customer
dim_contact
dim_company
dim_lead
dim_account
dim_campaign
dim_channel
dim_agent
dim_ai_agent
dim_model
dim_workflow
dim_feature
dim_product
dim_plan
dim_subscription
dim_geography
dim_industry
```

---

## SR-008 — Slowly Changing Dimensions

The platform SHALL support SCD where historical state is analytically relevant.

Supported patterns:

* SCD Type 1
* SCD Type 2

SCD Type 2 SHOULD be used for:

* Customer segmentation
* User roles
* Organization configuration
* Subscription plans
* Lead lifecycle states
* Account ownership
* Team membership

---

## SR-009 — Data Warehouse Compatibility

The model SHALL support analytical SQL workloads and columnar analytical engines.

---

## SR-010 — Data Lake Compatibility

Raw and semi-structured events SHALL be storable in a data lake before transformation.

---

## SR-011 — Real-Time Processing

The architecture SHOULD support:

```text
Event
 ↓
Message Bus
 ↓
Stream Processor
 ↓
Real-Time Aggregation
 ↓
Analytics Store
 ↓
Dashboard/API
```

---

## SR-012 — Batch Processing

The platform SHALL support scheduled:

* ETL
* ELT
* Aggregation
* Backfill
* Reconciliation
* Data-quality jobs

---

## SR-013 — Idempotency

All analytical ingestion pipelines SHALL support deterministic idempotency keys.

Example:

```text
tenant_id + event_id
```

---

## SR-014 — Deduplication

Duplicate events SHALL be detected and prevented from corrupting analytical metrics.

---

## SR-015 — Late Events

The system SHALL support late-arriving events without silently corrupting historical aggregates.

---

## SR-016 — Time Zones

Analytics SHALL preserve:

```text
UTC timestamp
tenant timezone
user timezone where permitted
```

Business-day and reporting-period calculations SHALL use the configured reporting timezone.

---

## SR-017 — Data Quality

The system SHALL validate:

* Completeness
* Accuracy
* Consistency
* Uniqueness
* Validity
* Timeliness
* Referential integrity

---

## SR-018 — Data Lineage

Every derived analytical metric SHOULD be traceable to:

```text
source
 ↓
event
 ↓
transformation
 ↓
fact
 ↓
aggregate
 ↓
dashboard
```

---

## SR-019 — Access Control

Analytical access SHALL enforce:

* RBAC
* Tenant isolation
* Row-level security
* Column-level security where required
* Data classification
* Least privilege

---

## SR-020 — PII Protection

Analytics SHALL minimize direct storage of sensitive personal data.

Sensitive fields SHOULD be:

* Tokenized
* Hashed
* Masked
* Encrypted
* Removed from analytical datasets where unnecessary

---

## SR-021 — Performance

Common dashboard queries SHOULD meet defined latency SLOs.

Target:

```text
P50 < 1 second
P95 < 3 seconds
P99 < 10 seconds
```

for pre-aggregated analytical queries under normal production load.

---

## SR-022 — Scalability

The analytical architecture SHALL support horizontal scaling for:

* Event ingestion
* Stream processing
* ETL/ELT
* Query execution
* Storage
* Aggregation

---

## SR-023 — High Cardinality

The system SHALL prevent uncontrolled high-cardinality dimensions from degrading analytical performance.

---

## SR-024 — Analytical Consistency

Canonical metrics SHALL have one authoritative definition.

Example:

```text
qualified_lead
```

MUST have a centrally governed definition rather than independent definitions across dashboards.

---

## SR-025 — Metric Layer

SalesGenie SHOULD implement a semantic/metrics layer defining:

* Metric name
* Formula
* Dimensions
* Filters
* Grain
* Owner
* Version
* Data source
* Freshness
* Business definition

---

## 6. Functional Requirements

## FR-001 — Event Fact Model

The system SHALL maintain a canonical event fact containing at minimum:

```text
event_id
tenant_id
organization_id
event_type
event_name
event_time
ingestion_time
processing_time
actor_type
actor_id
entity_type
entity_id
session_id
conversation_id
channel_id
source_system
schema_version
correlation_id
causation_id
metadata
```

---

## FR-002 — Actor Attribution

The system SHALL identify the originator of an analytical activity.

Supported:

```text
HUMAN
AI_AGENT
SYSTEM
AUTOMATION
INTEGRATION
HYBRID
```

---

## FR-003 — Human Attribution

Human activity SHALL support:

```text
user_id
team_id
role_id
agent_id
```

---

## FR-004 — AI Attribution

AI activity SHALL support:

```text
ai_agent_id
model_id
provider
model_version
prompt_version
tool_version
agent_version
```

---

## FR-005 — AI Cost Attribution

Each AI interaction SHOULD record:

```text
input_tokens
output_tokens
total_tokens
cached_tokens
reasoning_tokens
estimated_cost
currency
```

where supported by the provider.

---

## FR-006 — AI Latency

The system SHALL capture:

```text
queue_latency
model_latency
tool_latency
total_latency
```

---

## FR-007 — AI Quality

AI interactions SHOULD support:

```text
success
failure
fallback
escalation
human_override
user_feedback
quality_score
```

---

## FR-008 — Conversation Fact

Conversation analytics SHALL support:

```text
conversation_id
tenant_id
customer_id
lead_id
channel_id
started_at
ended_at
duration
message_count
participant_count
ai_message_count
human_message_count
escalation_count
resolution_status
conversion_status
```

---

## FR-009 — Message Fact

Message analytics SHALL support:

```text
message_id
conversation_id
sender_type
sender_id
recipient_type
recipient_id
channel_id
message_type
message_status
sent_at
delivered_at
read_at
responded_at
latency
```

---

## FR-010 — Lead Fact

Lead analytics SHALL support:

```text
lead_id
tenant_id
source
created_at
qualified_at
contacted_at
engaged_at
meeting_booked_at
opportunity_created_at
converted_at
lost_at
lead_score
lead_status
conversion_status
owner_id
```

---

## FR-011 — Lead Source Attribution

The system SHALL track:

* Organic
* Paid
* Referral
* Website
* Social
* Email
* Outbound
* AI prospecting
* Human prospecting
* Import
* Integration
* API

---

## FR-012 — Opportunity Fact

Opportunity analytics SHALL support:

```text
opportunity_id
account_id
lead_id
owner_id
pipeline_id
stage
amount
currency
created_at
closed_at
won_at
lost_at
probability
source
```

---

## FR-013 — Revenue Fact

Revenue analytics SHALL support:

```text
transaction_id
tenant_id
customer_id
subscription_id
invoice_id
amount
currency
transaction_type
recognized_at
source
attribution
```

---

## FR-014 — Campaign Fact

Campaign analytics SHALL support:

```text
campaign_id
audience_id
channel_id
sent
delivered
opened
clicked
replied
meeting_booked
converted
revenue
cost
```

---

## FR-015 — Workflow Fact

Workflow execution analytics SHALL include:

```text
execution_id
workflow_id
tenant_id
trigger_type
started_at
completed_at
duration
status
retry_count
error_count
initiated_by
```

---

## FR-016 — Workflow Action Fact

Each workflow action SHALL support:

```text
action_id
execution_id
action_type
actor_type
started_at
completed_at
status
latency
retry_count
error_code
```

---

## FR-017 — Human Intervention Fact

The system SHALL record when humans intervene in AI or automated processes.

Required analytical attributes:

```text
intervention_id
conversation_id
workflow_execution_id
ai_agent_id
human_user_id
reason
timestamp
previous_state
new_state
outcome
```

---

## FR-018 — AI-to-Human Handoff Analytics

The system SHALL calculate:

```text
handoff_rate
handoff_count
handoff_latency
handoff_resolution_rate
handoff_conversion_rate
```

---

## FR-019 — Customer Support Analytics

The model SHALL support:

```text
tickets_created
tickets_resolved
first_response_time
average_resolution_time
reopen_rate
escalation_rate
CSAT
```

---

## FR-020 — Voice Analytics

Voice interactions SHALL support:

```text
call_id
caller
callee
duration
direction
recording_reference
transcription_status
sentiment
intent
resolution
conversion
ai_involvement
human_involvement
```

---

## FR-021 — RAG Analytics

RAG interactions SHALL support:

```text
retrieval_id
query
knowledge_base_id
document_id
chunk_id
retrieval_score
rank
model_id
latency
citation_used
answer_grounded
```

---

## FR-022 — Knowledge Analytics

The system SHALL identify:

* Frequently retrieved documents
* Unused documents
* Low-quality documents
* Missing knowledge
* Failed retrievals
* Retrieval latency
* Knowledge contribution to successful responses

---

## FR-023 — Product Event Analytics

The system SHALL capture:

```text
page_view
feature_view
feature_used
button_clicked
workflow_created
agent_created
integration_connected
report_generated
subscription_started
subscription_upgraded
subscription_downgraded
```

---

## FR-024 — Feature Adoption

The system SHALL calculate:

```text
DAU
WAU
MAU
feature_adoption_rate
feature_activation_rate
feature_retention_rate
feature_dropoff_rate
```

---

## FR-025 — Session Analytics

The system SHALL track:

```text
session_id
user_id
tenant_id
started_at
ended_at
duration
device
browser
platform
entry_point
exit_point
events
```

---

## FR-026 — Cohort Analytics

The platform SHALL support cohorts based on:

* Signup date
* Activation date
* Subscription date
* Industry
* Geography
* Plan
* Acquisition channel
* Lead source
* Feature usage
* AI usage

---

## FR-027 — Funnel Analytics

The platform SHALL support configurable funnels.

Example:

```text
Visitor
 ↓
Signup
 ↓
Activation
 ↓
Trial
 ↓
First AI Agent
 ↓
First Conversation
 ↓
First Lead
 ↓
First Conversion
 ↓
Paid Customer
```

---

## FR-028 — Retention Analytics

The system SHALL calculate:

* User retention
* Organization retention
* Customer retention
* Feature retention
* Revenue retention

---

## FR-029 — Churn Analytics

The system SHALL track:

```text
customer_churn
subscription_churn
revenue_churn
logo_churn
voluntary_churn
involuntary_churn
```

---

## FR-030 — Subscription Analytics

The system SHALL support:

```text
trial_started
trial_converted
subscription_started
subscription_renewed
subscription_upgraded
subscription_downgraded
subscription_paused
subscription_cancelled
subscription_expired
```

---

## FR-031 — Usage Analytics

The system SHALL measure:

* API requests
* AI requests
* Tokens
* Messages
* Conversations
* Leads
* Contacts
* Workflow executions
* Storage
* Voice minutes
* Email volume
* Integration usage

---

## FR-032 — Quota Analytics

The system SHALL calculate:

```text
quota_limit
quota_used
quota_remaining
quota_percentage
quota_exceeded
quota_reset
```

---

## FR-033 — Cost Analytics

The system SHALL calculate:

```text
cost_per_lead
cost_per_conversation
cost_per_resolution
cost_per_conversion
cost_per_customer
cost_per_AI_interaction
cost_per_workflow
```

---

## FR-034 — ROI Analytics

The system SHALL calculate:

```text
ROI =
(revenue_attributed - total_cost)
/
total_cost
```

Attribution rules SHALL be configurable and versioned.

---

## FR-035 — AI ROI

The platform SHALL support:

```text
AI_attributed_revenue
AI_cost
AI_ROI
AI_revenue_per_dollar
```

---

## FR-036 — Human ROI

The platform SHALL support:

```text
human_attributed_revenue
human_cost
human_ROI
```

---

## FR-037 — Attribution Models

The analytics engine SHOULD support:

* First-touch
* Last-touch
* Linear
* Time-decay
* Position-based
* AI-assisted
* Human-assisted
* Custom attribution

---

## FR-038 — AI/Human Hybrid Attribution

The system SHALL support attribution such as:

```text
AI generated lead
→ AI qualified lead
→ Human contacted lead
→ AI follow-up
→ Human closed deal
```

The final revenue SHALL preserve all contributing actors.

---

## FR-039 — Analytics Aggregations

The system SHALL provide precomputed aggregations for:

* Hourly
* Daily
* Weekly
* Monthly
* Quarterly
* Yearly

---

## FR-040 — Dimensional Aggregation

Metrics SHALL support aggregation by:

```text
tenant
organization
team
user
agent
AI agent
channel
campaign
industry
geography
plan
product
feature
date
```

---

## FR-041 — Data Freshness

Every analytical dataset SHALL expose:

```text
last_updated_at
data_freshness
pipeline_status
```

---

## FR-042 — Data Quality Score

Analytical datasets SHOULD expose:

```text
completeness_score
accuracy_score
consistency_score
timeliness_score
overall_quality_score
```

---

## FR-043 — Metric Definitions

Every governed metric SHALL contain:

```text
metric_id
metric_name
description
formula
grain
dimensions
owner
version
status
data_sources
last_updated
```

---

## FR-044 — Metric Versioning

Changes to metric definitions SHALL be versioned.

Historical reports SHALL remain reproducible under the metric definition applicable at the time.

---

## FR-045 — Analytical Reprocessing

Authorized operators SHALL be able to reprocess historical analytical data.

Supported:

```text
tenant
date range
event type
dataset
pipeline
```

---

## FR-046 — Backfill

The platform SHALL support controlled backfills without creating duplicate facts.

---

## FR-047 — Reconciliation

The system SHALL reconcile analytical values against operational sources.

Examples:

```text
CRM leads
↔
analytics leads

billing revenue
↔
analytics revenue

workflow executions
↔
workflow analytics
```

---

## FR-048 — Anomaly Detection

The analytics platform SHOULD detect abnormal:

* Traffic
* Conversion
* Revenue
* AI usage
* Costs
* Errors
* Latency
* Message volume
* Lead generation
* Workflow execution

---

## FR-049 — Forecasting

The system SHOULD support forecasting for:

* Revenue
* Leads
* Pipeline
* Churn
* Usage
* AI costs
* Customer growth

---

## FR-050 — Predictive Analytics

The platform SHOULD support ML features such as:

* Lead conversion probability
* Churn probability
* Customer lifetime value
* Deal probability
* Customer health
* Next-best-action
* Lead quality prediction

---

## FR-051 — Experiment Analytics

The platform SHALL support:

```text
experiment_id
variant_id
subject_id
exposure_time
conversion
revenue
retention
```

---

## FR-052 — Statistical Analysis

Experiment analytics SHOULD support:

* Control groups
* Treatment groups
* Conversion rate
* Lift
* Confidence intervals
* Statistical significance

---

## FR-053 — Security Analytics

Security analytics SHALL support:

* Login events
* Authentication failures
* Authorization failures
* Suspicious activity
* Account takeover signals
* API abuse
* Security incidents
* Administrative actions

---

## FR-054 — Compliance Analytics

The model SHALL support:

* Consent events
* Data-subject requests
* Deletion requests
* Data exports
* Retention events
* Policy violations
* Audit events

---

## FR-055 — Data Privacy Analytics

Privacy analytics SHALL track:

```text
data_access
data_export
data_deletion
consent_change
privacy_request
retention_action
```

without unnecessarily exposing sensitive personal data.

---

## FR-056 — Dashboard APIs

The analytics service SHALL expose APIs for:

```text
metrics
dimensions
timeseries
funnels
cohorts
retention
attribution
cost
usage
AI analytics
sales analytics
support analytics
```

---

## FR-057 — Pagination

Large analytical datasets SHALL support:

* Cursor pagination
* Time-window pagination
* Partition-aware retrieval

---

## FR-058 — Query Guardrails

The system SHALL protect analytical infrastructure against:

* Unbounded queries
* Cartesian joins
* Excessive aggregation
* Full-table scans
* High-cardinality explosions
* Expensive repeated queries

---

## FR-059 — Caching

Frequently accessed analytical queries SHOULD be cached.

Cache invalidation SHALL account for data freshness requirements.

---

## FR-060 — Materialized Views

The platform SHOULD use materialized views for high-volume dashboards.

---

## FR-061 — Tenant-Level Analytics

Each tenant SHALL have isolated analytical views according to authorization policies.

---

## FR-062 — Cross-Tenant Analytics

Cross-tenant analytics SHALL be restricted to authorized platform administrators and SHALL use controlled aggregation or anonymization where required.

---

## FR-063 — Super Admin Analytics

Super Admin analytics SHOULD provide:

* Total tenants
* Active tenants
* Active users
* Total conversations
* AI usage
* Human usage
* Lead volume
* Revenue
* MRR
* ARR
* Churn
* Platform cost
* System health
* Security events

---

## FR-064 — Organization Analytics

Organization administrators SHALL see analytics only for authorized organizations/workspaces.

---

## FR-065 — Team Analytics

Managers SHALL be able to compare:

* Teams
* Agents
* AI agents
* Productivity
* Conversion
* Resolution
* Revenue

---

## FR-066 — Sales Agent Analytics

Sales agents SHALL see permitted metrics for their own activities and assigned records.

---

## FR-067 — AI Agent Analytics

AI agents SHALL have machine-readable performance metrics including:

```text
task_count
success_rate
failure_rate
handoff_rate
conversion_rate
latency
cost
token_usage
```

---

## FR-068 — Explainable Metrics

The system SHOULD allow users to inspect why a metric has a particular value.

Example:

```text
Conversion Rate: 14.2%

Total qualified leads: 1,000
Converted leads: 142
Calculation: 142 / 1,000
```

---

## FR-069 — Source Traceability

Users with appropriate permissions SHOULD be able to trace a metric back to source events.

---

## FR-070 — Data Contracts

Every analytical event SHALL conform to a defined data contract.

Invalid events SHALL be:

```text
rejected
quarantined
or corrected
```

according to policy.

---

## 7. Canonical Analytical Entities

The platform SHOULD maintain canonical representations for:

```text
Tenant
Organization
Workspace
User
Team
Role
Customer
Contact
Company
Account
Lead
Opportunity
Campaign
Conversation
Message
Session
Ticket
Call
Email
Channel
Workflow
Workflow Execution
Workflow Action
AI Agent
Human Agent
AI Model
Tool
Knowledge Base
Document
Retrieval
Subscription
Plan
Invoice
Payment
Usage
Quota
Cost
Experiment
Feature
Event
Security Event
Compliance Event
```

---

## 8. Canonical Event Envelope

All analytical events SHOULD conform to a common envelope:

```json
{
  "event_id": "uuid",
  "event_type": "lead.created",
  "schema_version": "1.0",
  "tenant_id": "uuid",
  "organization_id": "uuid",
  "workspace_id": "uuid",
  "actor": {
    "type": "AI_AGENT",
    "id": "uuid"
  },
  "entity": {
    "type": "LEAD",
    "id": "uuid"
  },
  "event_time": "2026-08-28T12:00:00Z",
  "ingestion_time": "2026-08-28T12:00:01Z",
  "correlation_id": "uuid",
  "causation_id": "uuid",
  "source_system": "lead_intelligence",
  "metadata": {}
}
```

---

## 9. Recommended Fact Table Grain

| Fact                       | Grain                        |
| -------------------------- | ---------------------------- |
| `fact_events`              | One event                    |
| `fact_leads`               | One lead lifecycle           |
| `fact_lead_activities`     | One lead activity            |
| `fact_conversations`       | One conversation             |
| `fact_messages`            | One message                  |
| `fact_calls`               | One call                     |
| `fact_workflow_executions` | One workflow execution       |
| `fact_workflow_actions`    | One workflow action          |
| `fact_ai_interactions`     | One AI interaction           |
| `fact_ai_tool_calls`       | One AI tool call             |
| `fact_rag_retrievals`      | One retrieval                |
| `fact_human_interactions`  | One human activity           |
| `fact_opportunities`       | One opportunity lifecycle    |
| `fact_revenue`             | One revenue transaction      |
| `fact_subscriptions`       | One subscription event/state |
| `fact_usage`               | One usage measurement        |
| `fact_costs`               | One cost allocation          |
| `fact_product_events`      | One product event            |
| `fact_security_events`     | One security event           |

---

## 10. Recommended Core Dimensions

```text
dim_date
dim_time
dim_tenant
dim_organization
dim_workspace
dim_user
dim_team
dim_role
dim_customer
dim_contact
dim_company
dim_account
dim_lead
dim_campaign
dim_channel
dim_agent
dim_ai_agent
dim_model
dim_workflow
dim_feature
dim_product
dim_plan
dim_subscription
dim_geography
dim_industry
dim_source
```

---

## 11. Metric Categories

## Sales Metrics

```text
leads_generated
qualified_leads
contact_rate
response_rate
meeting_rate
opportunity_rate
win_rate
sales_cycle
pipeline_value
revenue
```

## AI Metrics

```text
ai_requests
ai_success_rate
ai_failure_rate
ai_handoff_rate
ai_conversion_rate
ai_latency
ai_tokens
ai_cost
ai_ROI
```

## Human Metrics

```text
human_interactions
human_response_time
human_resolution_time
human_conversion_rate
human_revenue
human_productivity
```

## Customer Metrics

```text
active_customers
retention
churn
CLV
engagement
support_volume
CSAT
```

## Product Metrics

```text
DAU
WAU
MAU
activation
feature_adoption
retention
conversion
```

## Financial Metrics

```text
MRR
ARR
ARPU
LTV
CAC
gross_revenue
net_revenue
expansion_revenue
churned_revenue
```

## Operational Metrics

```text
latency
error_rate
throughput
availability
queue_depth
processing_lag
```

---

## 12. Non-Functional Requirements

## NFR-001 — Availability

Analytics APIs SHALL target high availability appropriate to the SalesGenie production SLA.

---

## NFR-002 — Durability

Analytical source events SHALL be durably persisted.

---

## NFR-003 — Reliability

Pipeline failures SHALL not silently result in data loss.

---

## NFR-004 — Observability

Analytics pipelines SHALL expose:

* Logs
* Metrics
* Traces
* Pipeline health
* Data freshness
* Processing lag
* Error rates

---

## NFR-005 — Disaster Recovery

Analytical data SHALL support:

* Backup
* Restore
* Recovery
* Cross-region strategy where required

---

## NFR-006 — Security

All analytical access SHALL follow SalesGenie's security architecture and least-privilege principles.

---

## NFR-007 — Privacy

Analytics SHALL follow applicable privacy requirements and data minimization principles.

---

## NFR-008 — Auditability

Changes to:

* Metric definitions
* Schemas
* Pipelines
* Access policies
* Analytical datasets

SHALL be auditable.

---

## 13. AI-Specific Requirements

## AI-REQ-001

AI-generated events SHALL be analytically distinguishable from human events.

## AI-REQ-002

AI agent versions SHALL be captured.

## AI-REQ-003

LLM provider and model versions SHALL be captured.

## AI-REQ-004

Prompt/template versions SHALL be tracked where permitted.

## AI-REQ-005

AI tool usage SHALL be separately measurable.

## AI-REQ-006

AI failures SHALL be analytically classified.

## AI-REQ-007

AI-human handoffs SHALL be measurable.

## AI-REQ-008

AI-assisted human work SHALL preserve both actor identities.

## AI-REQ-009

AI costs SHALL be attributable to tenant, agent, workflow, feature, and activity where possible.

## AI-REQ-010

AI analytical data SHALL support model-performance comparison.

---

## 14. Human-Specific Requirements

## HUMAN-REQ-001

Human actions SHALL have accountable user attribution.

## HUMAN-REQ-002

Human actions SHALL respect RBAC.

## HUMAN-REQ-003

Human intervention in AI decisions SHALL be recorded.

## HUMAN-REQ-004

Human sales activity SHALL be attributable to revenue.

## HUMAN-REQ-005

Human support activity SHALL support productivity and quality analytics.

---

## 15. Data Governance Requirements

## GOV-001

Every analytical field SHALL have a defined owner.

## GOV-002

Sensitive fields SHALL have classifications.

Example:

```text
PUBLIC
INTERNAL
CONFIDENTIAL
RESTRICTED
SENSITIVE
```

## GOV-003

Critical metrics SHALL have documented definitions.

## GOV-004

Data lineage SHALL be maintained.

## GOV-005

Schema changes SHALL follow change-management procedures.

## GOV-006

Data retention policies SHALL apply to analytical datasets.

## GOV-007

Deleted source records SHALL trigger appropriate analytical deletion/anonymization workflows.

## GOV-008

Analytics SHALL not become an unauthorized secondary source of retained personal data.

---

## 16. Data Quality Rules

The platform SHALL enforce:

```text
event_id IS NOT NULL
tenant_id IS NOT NULL
event_time IS NOT NULL
event_type IS NOT NULL
schema_version IS NOT NULL
```

Additional rules:

```text
event_id UNIQUE
foreign keys valid
timestamps valid
currency valid
enum values valid
numeric ranges valid
tenant isolation valid
duplicate rate within threshold
freshness within SLA
```

---

## 17. Data Quality Thresholds

Recommended production thresholds:

```text
Completeness >= 99.5%
Uniqueness >= 99.9%
Schema validity >= 99.9%
Pipeline success >= 99.9%
Critical metric accuracy >= 99.9%
Freshness SLA compliance >= 99%
```

Thresholds SHALL be configurable by dataset criticality.

---

## 18. Analytics Pipeline

Recommended architecture:

```text
Operational Services
        │
        ▼
Event Producers
        │
        ▼
Event Bus
        │
        ├──────────────► Raw Data Lake
        │
        ▼
Stream Processing
        │
        ▼
Validated Events
        │
        ▼
Transformation Layer
        │
        ├──────────────► Fact Tables
        │
        └──────────────► Dimension Tables
                         │
                         ▼
                   Metric Layer
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
         Dashboards    APIs       ML/AI
```

---

## 19. Analytical Lifecycle

```text
SOURCE EVENT
    ↓
VALIDATION
    ↓
DEDUPLICATION
    ↓
NORMALIZATION
    ↓
ENRICHMENT
    ↓
IDENTITY RESOLUTION
    ↓
FACT/DI​MENSION MAPPING
    ↓
AGGREGATION
    ↓
METRIC COMPUTATION
    ↓
QUALITY VALIDATION
    ↓
SERVING
    ↓
DASHBOARD / API / ML
```

---

## 20. Acceptance Criteria

The implementation SHALL be considered complete when:

* [ ] Every critical platform event has an analytical schema.
* [ ] AI and human activity are separately attributable.
* [ ] Tenant isolation is enforced.
* [ ] Canonical fact tables are implemented.
* [ ] Canonical dimensions are implemented.
* [ ] Event time and ingestion time are preserved.
* [ ] Duplicate events are safely handled.
* [ ] Late-arriving events are supported.
* [ ] Schema versions are tracked.
* [ ] Data lineage is available.
* [ ] Data-quality checks are automated.
* [ ] Metric definitions are centralized.
* [ ] Historical reporting is reproducible.
* [ ] Real-time metrics are available for critical workloads.
* [ ] Batch analytical workloads are supported.
* [ ] AI usage and cost are measurable.
* [ ] Human activity is measurable.
* [ ] AI-human attribution is supported.
* [ ] Lead lifecycle analytics are available.
* [ ] Conversation analytics are available.
* [ ] Workflow analytics are available.
* [ ] Revenue attribution is available.
* [ ] Subscription analytics are available.
* [ ] Usage/quota analytics are available.
* [ ] Product analytics are available.
* [ ] Security analytics are available.
* [ ] Compliance analytics are available.
* [ ] RBAC and tenant-level authorization are enforced.
* [ ] PII minimization is implemented.
* [ ] Analytical APIs support pagination and filtering.
* [ ] Dashboard query performance meets defined SLOs.
* [ ] Backfill and reprocessing are supported.
* [ ] Operational-to-analytical reconciliation exists.
* [ ] Analytics infrastructure is observable.
* [ ] Critical datasets have freshness monitoring.
* [ ] Metric changes are versioned.
* [ ] Analytical data retention is enforced.

---

## 21. Definition of Done

`analytics_data_model.md` is considered implemented when SalesGenie has a production-grade analytical model that can reliably answer:

```text
WHO
    performed an action?

WHAT
    happened?

WHEN
    did it happen?

WHERE
    did it happen?

WHY
    did it happen?

HOW
    did it happen?

WAS IT AI OR HUMAN
    who contributed?

WHAT WAS THE OUTCOME
    success / failure / conversion?

WHAT DID IT COST
    operational + AI + human cost?

WHAT REVENUE DID IT GENERATE
    direct / influenced / attributed?

WHAT DATA PRODUCED THE RESULT
    lineage?

CAN WE TRUST THE METRIC
    data quality?

CAN WE AUDIT IT
    governance + security?

CAN WE REPRODUCE IT
    versioned metrics + immutable events?
```

The final analytical platform SHALL provide a **single, governed, scalable, privacy-aware source of analytical truth** for SalesGenie's AI agents, human users, customers, administrators, business intelligence systems, machine-learning systems, and executive decision-making.
