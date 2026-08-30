# SalesGenie — Enterprise Data Warehouse Requirements

**Document:** `data_warehouse.md`  
**Project:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Requirement Level:** FAANG / Enterprise Grade  
**Scope:** Human + AI Data Warehouse Operations  
**Architecture:** Multi-Tenant + Microservices + Event-Driven + AI-Native + Cloud-Native + Zero-Trust

---

## 1. Purpose

The SalesGenie Data Warehouse shall provide a governed, scalable, secure, high-performance analytical data platform for transforming operational, customer, sales, support, marketing, billing, workflow, AI, and product data into trusted analytical datasets.

The Data Warehouse shall support:

- Executive analytics
- Business intelligence
- Sales analytics
- Lead analytics
- Customer analytics
- Customer 360
- Support analytics
- Agent performance analytics
- AI-agent analytics
- Workflow analytics
- Marketing analytics
- Product analytics
- Billing analytics
- Revenue analytics
- Subscription analytics
- Usage analytics
- Cohort analysis
- Funnel analysis
- Forecasting
- ML feature generation
- AI analytics
- Compliance reporting
- Security analytics
- Operational reporting

The Data Warehouse shall complement the SalesGenie Data Lake:

```text
Operational Systems
       |
       v
Data Ingestion
       |
       v
Data Lake
       |
       v
Transformation / ELT
       |
       v
Enterprise Data Warehouse
       |
       +------------------+
       |                  |
       v                  v
BI / Analytics        AI / ML
       |
       v
Applications / Decisions
```

The Data Warehouse shall be optimized for trusted analytical workloads rather than serving as the primary transactional database.

---

## 2. Goals

The SalesGenie Data Warehouse shall:

1. Provide a centralized analytical source of truth.
2. Support enterprise-scale analytical workloads.
3. Support multi-tenant analytics.
4. Maintain strict tenant isolation.
5. Integrate data from all major SalesGenie domains.
6. Provide governed dimensional and analytical models.
7. Support historical analysis.
8. Support slowly changing dimensions.
9. Support fact and dimension modeling.
10. Support real-time or near-real-time analytics where required.
11. Support batch analytical workloads.
12. Support AI-driven analytics.
13. Support human-driven analytics.
14. Support semantic querying.
15. Support natural-language analytics.
16. Support BI dashboards.
17. Support ad-hoc analysis.
18. Support forecasting.
19. Support anomaly detection.
20. Support data-quality controls.
21. Support lineage.
22. Support metadata management.
23. Support security and privacy controls.
24. Support regulatory reporting.
25. Support data retention and deletion policies.
26. Support disaster recovery.
27. Support high availability.
28. Support horizontal scalability.
29. Support cost optimization.
30. Provide reproducible analytical results.

---

## 3. Non-Goals

The Data Warehouse shall not replace:

* OLTP databases
* Authentication databases
* Payment processors
* Object storage
* Vector databases
* Message brokers
* Primary application databases
* Operational caches

The Data Warehouse shall not become the authoritative source for transactional state unless explicitly designed for a specific analytical workflow.

---

## 4. Actors

## 4.1 Human Actors

* End User
* Customer
* Sales Agent
* Support Agent
* Sales Manager
* Support Manager
* Marketing Manager
* Organization Admin
* Business Analyst
* Data Analyst
* Data Engineer
* Analytics Engineer
* ML Engineer
* AI Engineer
* Data Scientist
* Product Manager
* Finance Analyst
* Security Administrator
* Compliance Officer
* Data Steward
* Auditor
* Super Admin
* Executive

## 4.2 AI Actors

* AI Analytics Agent
* AI Data Analyst Agent
* AI BI Agent
* AI Forecasting Agent
* AI Anomaly Detection Agent
* AI Customer Intelligence Agent
* AI Sales Intelligence Agent
* AI Support Intelligence Agent
* AI Revenue Intelligence Agent
* AI Product Analytics Agent
* AI Data Quality Agent
* AI Governance Agent
* AI Data Modeling Agent
* AI SQL Generation Agent
* AI Report Generation Agent
* Multi-Agent Orchestrator

---

## 5. User Requirements

## UR-001 — View Analytics

Authorized users shall be able to view analytical dashboards according to their roles and tenant permissions.

---

## UR-002 — Query Business Data

Authorized users shall be able to query approved analytical datasets.

---

## UR-003 — Filter Analytics

Users shall be able to filter analytical data by:

* Time
* Tenant
* Organization
* Workspace
* Customer
* Company
* Lead
* Sales agent
* Support agent
* Product
* Subscription
* Region
* Industry
* Channel
* Campaign
* Workflow
* AI agent

---

## UR-004 — Drill Down

Users shall be able to drill from aggregated metrics into authorized underlying dimensions.

---

## UR-005 — Drill Up

Users shall be able to aggregate analytical information across supported dimensions.

---

## UR-006 — Compare Periods

Users shall be able to compare:

* Day over day
* Week over week
* Month over month
* Quarter over quarter
* Year over year

---

## UR-007 — Export Analytics

Authorized users shall be able to export analytical results according to:

* RBAC
* ABAC
* DLP
* Export limits
* Privacy policies
* Tenant policies

---

## UR-008 — Schedule Reports

Authorized users shall be able to schedule analytical reports.

---

## UR-009 — Subscribe to Reports

Users shall be able to subscribe to authorized dashboards and reports.

---

## UR-010 — Create Custom Reports

Authorized users shall be able to create custom reports using approved datasets and metrics.

---

## UR-011 — Save Queries

Authorized users shall be able to save analytical queries.

---

## UR-012 — Share Analytics

Users shall be able to share authorized dashboards and reports within permitted organizational boundaries.

---

## UR-013 — Manage Dashboards

Authorized users shall be able to create, update, clone, archive, and delete dashboards.

---

## 6. AI User Requirements

## AI-UR-001 — Natural Language Analytics

Users shall be able to ask questions such as:

```text
"How many qualified leads did we generate this month?"
```

---

## AI-UR-002 — Natural Language SQL

The AI shall translate approved natural-language questions into analytical queries.

Generated SQL shall be:

* Validated
* Authorized
* Tenant-scoped
* Resource-limited
* Auditable

---

## AI-UR-003 — Explain Metrics

AI shall explain business metrics in human-readable language.

---

## AI-UR-004 — Explain Trends

AI shall identify significant trends in authorized datasets.

---

## AI-UR-005 — AI Dashboard Generation

Authorized users shall be able to request dashboards from natural-language requirements.

---

## AI-UR-006 — AI Report Generation

AI shall generate reports from approved warehouse datasets.

---

## AI-UR-007 — AI Forecasting

AI shall support forecasting for approved business metrics.

Potential metrics include:

* Revenue
* Leads
* Conversion
* Churn
* Support volume
* Customer growth
* Usage
* Subscription growth

---

## AI-UR-008 — AI Anomaly Detection

AI shall detect unusual changes in approved metrics.

---

## AI-UR-009 — AI Root-Cause Analysis

AI shall identify potential contributors to detected anomalies using authorized data.

---

## AI-UR-010 — AI Customer Intelligence

AI shall provide authorized customer-level analytical insights.

---

## AI-UR-011 — AI Sales Intelligence

AI shall provide authorized insights regarding:

* Pipeline
* Lead quality
* Conversion
* Sales performance
* Revenue
* Deal velocity

---

## AI-UR-012 — AI Support Intelligence

AI shall provide authorized insights regarding:

* Ticket volume
* Resolution time
* Customer satisfaction
* Agent performance
* Escalations
* Support trends

---

## AI-UR-013 — AI Revenue Intelligence

AI shall analyze:

* MRR
* ARR
* ARPU
* Churn
* Expansion
* Contraction
* Refunds
* Discounts
* Subscription upgrades
* Subscription downgrades

---

## AI-UR-014 — Human Approval

AI-generated business-critical decisions shall require human approval where configured.

---

## 7. System Requirements

## 7.1 Warehouse Architecture

## SR-001 — Analytical Separation

The Data Warehouse shall be logically separated from transactional workloads.

---

## SR-002 — Multi-Tenant Architecture

Every warehouse record containing tenant-specific data shall maintain tenant identity.

Required identifiers shall include, where applicable:

```text
tenant_id
organization_id
workspace_id
```

---

## SR-003 — Tenant Isolation

Warehouse queries shall prevent unauthorized cross-tenant access.

---

## SR-004 — Environment Isolation

The platform shall support:

```text
development
testing
staging
production
```

with appropriate isolation.

---

## 8. Warehouse Layers

The Data Warehouse should implement logical layers:

```text
SOURCE
   |
   v
STAGING
   |
   v
INTEGRATION
   |
   v
CORE
   |
   v
MART
   |
   v
SEMANTIC
   |
   v
BI / AI
```

---

## SR-005 — Staging Layer

The staging layer shall contain source-aligned analytical ingestion data.

---

## SR-006 — Integration Layer

The integration layer shall normalize and integrate data from multiple sources.

---

## SR-007 — Core Warehouse

The core warehouse shall contain governed enterprise analytical entities.

---

## SR-008 — Data Marts

The platform shall support domain-specific data marts.

Potential marts:

```text
sales_mart
lead_mart
customer_mart
support_mart
marketing_mart
billing_mart
subscription_mart
product_mart
ai_mart
workflow_mart
security_mart
compliance_mart
```

---

## SR-009 — Semantic Layer

The platform shall provide a governed semantic layer for business metrics and dimensions.

---

## 9. Data Modeling

## SR-010 — Dimensional Modeling

The warehouse shall support dimensional modeling.

---

## SR-011 — Fact Tables

The system shall support fact tables for measurable business events.

Examples:

```text
fact_lead
fact_sales_activity
fact_deal
fact_customer_interaction
fact_support_ticket
fact_ai_interaction
fact_workflow_execution
fact_subscription
fact_invoice
fact_payment
fact_usage
fact_refund
fact_campaign_event
```

---

## SR-012 — Dimension Tables

The system shall support dimensions including:

```text
dim_customer
dim_company
dim_user
dim_sales_agent
dim_support_agent
dim_product
dim_plan
dim_subscription
dim_date
dim_time
dim_region
dim_industry
dim_channel
dim_campaign
dim_ai_agent
dim_model
dim_workflow
```

---

## 10. Slowly Changing Dimensions

## SR-013 — SCD Support

The warehouse shall support slowly changing dimensions.

Supported patterns should include:

```text
SCD Type 1
SCD Type 2
```

---

## SR-014 — Historical Attributes

Historical business attributes shall be preserved where required.

Example:

```text
Customer
  |
  +-- Plan = Starter
  |
  +-- Plan = Professional
  |
  +-- Plan = Enterprise
```

---

## 11. Fact Table Requirements

## SR-015 — Event Grain

Every fact table shall have an explicitly documented grain.

---

## SR-016 — Event Timestamp

Facts shall contain appropriate event timestamps.

---

## SR-017 — Event Identity

Business events shall have stable identifiers where available.

---

## SR-018 — Idempotency

Repeated source events shall not produce unintended duplicate analytical facts.

---

## 12. Data Warehouse Core Entities

## Customer

```text
customer_key
customer_id
tenant_id
organization_id
customer_name
customer_type
industry
region
country
created_at
updated_at
status
```

---

## Company

```text
company_key
company_id
tenant_id
company_name
industry
company_size
revenue_band
country
region
created_at
updated_at
```

---

## Lead

```text
lead_key
lead_id
tenant_id
company_key
source
lead_status
lead_score
intent_score
created_at
qualified_at
converted_at
```

---

## Sales Activity

```text
sales_activity_key
activity_id
tenant_id
lead_key
customer_key
sales_agent_key
activity_type
channel
timestamp
duration
outcome
```

---

## Support Interaction

```text
support_interaction_key
interaction_id
tenant_id
customer_key
support_agent_key
channel
issue_type
priority
created_at
resolved_at
resolution_time
satisfaction_score
```

---

## AI Interaction

```text
ai_interaction_key
interaction_id
tenant_id
customer_key
agent_key
model_key
channel
request_timestamp
response_timestamp
latency
input_tokens
output_tokens
cost
success
```

---

## Workflow Execution

```text
workflow_execution_key
execution_id
tenant_id
workflow_id
workflow_version
trigger_type
status
started_at
completed_at
duration
action_count
error_count
```

---

## 13. Sales Analytics Requirements

## SR-019 — Sales Funnel

The warehouse shall support:

```text
Lead
→ MQL
→ SQL
→ Opportunity
→ Proposal
→ Negotiation
→ Won
```

---

## SR-020 — Conversion Metrics

The warehouse shall calculate:

* Lead conversion rate
* Opportunity conversion rate
* Win rate
* Pipeline conversion
* Customer conversion

---

## SR-021 — Sales Velocity

The warehouse shall support:

* Deal velocity
* Lead response time
* Sales cycle duration
* Time to qualification

---

## SR-022 — Sales Performance

The system shall support:

* Revenue per agent
* Deals per agent
* Conversion per agent
* Average deal size
* Sales activity volume

---

## 14. Lead Intelligence

## SR-023 — Lead Scoring Analytics

The warehouse shall store historical lead scores.

---

## SR-024 — Lead Score Evolution

The platform shall support analysis of lead score changes over time.

---

## SR-025 — Lead Source Attribution

The warehouse shall support attribution by:

* Source
* Campaign
* Channel
* Referral
* Partner
* Organic
* Paid

---

## 15. Customer Analytics

## SR-026 — Customer 360

The warehouse shall support integrated customer analytics across:

```text
Sales
+
Support
+
Product
+
Billing
+
Marketing
+
AI
+
Workflow
```

---

## SR-027 — Customer Lifetime Value

The warehouse shall support configurable CLV calculations.

---

## SR-028 — Customer Segmentation

The warehouse shall support segmentation by:

* Industry
* Company size
* Geography
* Plan
* Revenue
* Engagement
* Usage
* Customer lifecycle

---

## 16. Support Analytics

## SR-029 — Ticket Analytics

The warehouse shall support:

* Ticket volume
* Resolution time
* First response time
* Escalation rate
* Reopen rate
* SLA compliance

---

## SR-030 — Agent Analytics

The warehouse shall support:

* Tickets handled
* Average handling time
* Resolution rate
* Customer satisfaction
* Escalation rate

---

## 17. AI Analytics

## SR-031 — AI Usage

The warehouse shall track AI usage by:

* Tenant
* Organization
* User
* Agent
* Model
* Provider
* Feature
* Channel

---

## SR-032 — AI Cost

The warehouse shall calculate AI cost from metered usage and configured pricing.

---

## SR-033 — AI Latency

The warehouse shall track:

* Request latency
* Time to first token where available
* Completion latency
* Queue latency

---

## SR-034 — AI Quality

The warehouse shall support:

* Success rate
* Failure rate
* User feedback
* Evaluation score
* Groundedness score where available
* Retrieval quality where available

---

## 18. Billing Analytics

## SR-035 — Revenue Analytics

The warehouse shall support:

* Gross revenue
* Net revenue
* Recurring revenue
* MRR
* ARR
* ARPU

---

## SR-036 — Subscription Analytics

The warehouse shall support:

* New subscriptions
* Renewals
* Upgrades
* Downgrades
* Cancellations
* Reactivations
* Trial conversions

---

## SR-037 — Payment Analytics

The warehouse shall support:

* Successful payments
* Failed payments
* Payment retries
* Refunds
* Chargebacks where available

---

## SR-038 — Discount Analytics

The warehouse shall support:

* Coupon usage
* Discount amount
* Discount rate
* Revenue impact

---

## 19. Usage Analytics

## SR-039 — Usage Metering

The warehouse shall store analytical usage events for:

```text
AI requests
Tokens
Messages
Conversations
Leads
Contacts
Storage
Workflow executions
API requests
Voice minutes
Documents
Vector operations
Exports
```

---

## SR-040 — Usage by Tenant

Usage shall be analyzable by tenant.

---

## SR-041 — Usage by Subscription

Usage shall be analyzable by subscription plan and billing period.

---

## 20. Product Analytics

## SR-042 — Feature Adoption

The warehouse shall support analysis of feature adoption.

---

## SR-043 — User Engagement

The system shall support:

* DAU
* WAU
* MAU
* Session frequency
* Session duration
* Feature usage

---

## SR-044 — Funnel Analytics

The platform shall support:

```text
Signup
→ Activation
→ Engagement
→ Conversion
→ Retention
```

---

## SR-045 — Cohort Analysis

The warehouse shall support cohort analysis by:

* Signup month
* Subscription month
* Acquisition source
* Industry
* Plan

---

## 21. Marketing Analytics

## SR-046 — Campaign Analytics

The warehouse shall support:

* Impressions where available
* Clicks where available
* Leads
* Qualified leads
* Conversions
* Revenue attribution

---

## SR-047 — Campaign ROI

The system shall support campaign ROI analysis using configured attribution rules.

---

## 22. Workflow Analytics

## SR-048 — Workflow Performance

The warehouse shall analyze:

* Workflow executions
* Success rate
* Failure rate
* Execution duration
* Actions executed
* Retry count

---

## SR-049 — Workflow ROI

The system should support estimating business impact from workflow automation.

---

## 23. Data Ingestion

## SR-050 — Batch Loading

The warehouse shall support batch data loading.

---

## SR-051 — Incremental Loading

The warehouse shall support incremental loading.

---

## SR-052 — CDC

The platform shall support Change Data Capture where appropriate.

---

## SR-053 — Streaming Analytics

Near-real-time analytical ingestion shall be supported for selected workloads.

---

## 24. ELT / Transformation

## SR-054 — Transformation Framework

The platform shall support SQL and programmatic transformation workflows.

---

## SR-055 — Transformation Versioning

Transformations shall be version-controlled.

---

## SR-056 — Reproducibility

Warehouse datasets shall be reproducible from documented source versions and transformation versions where feasible.

---

## 25. Data Quality

## SR-057 — Quality Validation

Warehouse pipelines shall validate:

* Completeness
* Accuracy
* Consistency
* Uniqueness
* Validity
* Referential integrity
* Freshness

---

## SR-058 — Quality Gates

Critical datasets shall not be published when mandatory quality gates fail.

---

## SR-059 — Quality Score

Datasets shall have configurable quality scores.

---

## 26. Data Reconciliation

## SR-060 — Source Reconciliation

Warehouse totals shall be reconcilable with source systems.

---

## SR-061 — Record Reconciliation

The platform shall detect:

* Missing records
* Duplicate records
* Unexpected records
* Count mismatches
* Amount mismatches

---

## 27. Data Lineage

## SR-062 — Table Lineage

The system shall track source-to-target table lineage.

---

## SR-063 — Column Lineage

The platform should support column-level lineage.

---

## SR-064 — Metric Lineage

Business metrics shall be traceable to their underlying datasets and transformations.

---

## SR-065 — AI Query Lineage

AI-generated analytical responses shall retain references to:

```text
dataset
table
column
query
query_version
timestamp
agent_id
model_id
```

---

## 28. Semantic Layer

## SR-066 — Metric Definitions

Business metrics shall have centralized definitions.

---

## SR-067 — Metric Governance

Only authorized users shall be able to modify governed metrics.

---

## SR-068 — Metric Versioning

Critical metric definitions shall be versioned.

---

## SR-069 — Metric Consistency

Dashboards and AI analytics shall use the same governed metric definitions where applicable.

---

## 29. Natural Language Querying

## SR-070 — AI SQL Generation

The AI SQL agent shall generate queries from natural-language requests.

---

## SR-071 — Query Validation

Generated queries shall be validated before execution.

---

## SR-072 — Query Authorization

Generated queries shall inherit the requesting user's authorization context.

---

## SR-073 — Query Cost Control

Generated queries shall enforce:

* Execution timeout
* Scan limits
* Result limits
* Resource quotas

---

## SR-074 — Query Audit

AI-generated queries shall be logged.

---

## 30. AI Guardrails

## SR-075 — No Authorization Escalation

AI shall never increase the user's data access privileges.

---

## SR-076 — Sensitive Data Protection

AI responses shall respect:

* PII policies
* DLP policies
* Tenant policies
* Field-level policies
* Data classification

---

## SR-077 — Prompt Injection Defense

Warehouse-connected AI agents shall treat retrieved data as untrusted content.

---

## SR-078 — SQL Injection Defense

Natural-language SQL generation shall use safe query construction and validation.

---

## 31. Security

## SR-079 — Encryption at Rest

Warehouse data shall be encrypted at rest.

---

## SR-080 — Encryption in Transit

Warehouse connections shall use secure transport.

---

## SR-081 — Secret Management

Database credentials and service secrets shall never be embedded in source code.

---

## SR-082 — Least Privilege

Warehouse services shall receive only required permissions.

---

## 32. Access Control

## SR-083 — RBAC

Warehouse access shall support role-based access control.

---

## SR-084 — ABAC

Sensitive analytical datasets should support attribute-based access control.

---

## SR-085 — Row-Level Security

Tenant-sensitive datasets shall support row-level security or an equivalent authorization mechanism.

---

## SR-086 — Column-Level Security

Sensitive fields shall support masking or restricted access.

---

## SR-087 — Export Authorization

Exports shall require appropriate authorization.

---

## 33. Privacy

## SR-088 — Data Minimization

Analytical models shall avoid unnecessary sensitive data.

---

## SR-089 — PII Classification

Sensitive fields shall be classified.

---

## SR-090 — PII Masking

Sensitive fields shall support masking.

---

## SR-091 — Privacy-Aware Analytics

Analytics shall avoid exposing unauthorized individual-level data.

---

## 34. Retention

## SR-092 — Warehouse Retention

Warehouse datasets shall support configurable retention policies.

---

## SR-093 — Historical Retention

Business-critical historical datasets shall retain history according to policy.

---

## SR-094 — Legal Hold

Data subject to legal hold shall not be automatically removed.

---

## 35. Deletion

## SR-095 — Deletion Propagation

Applicable privacy deletion events shall propagate from authoritative systems into analytical datasets.

---

## SR-096 — Deletion Audit

Deletion operations shall be auditable.

---

## SR-097 — Derived Data Handling

Derived analytical datasets containing deleted personal information shall be identified and processed according to applicable policies.

---

## 36. Backup and Recovery

## SR-098 — Backup

Critical warehouse metadata and datasets shall have appropriate backups.

---

## SR-099 — Point-in-Time Recovery

The warehouse should support point-in-time recovery where supported by the selected technology.

---

## SR-100 — Disaster Recovery

The warehouse shall support defined:

```text
RPO
RTO
Recovery Region
Backup Frequency
```

---

## 37. High Availability

## SR-101 — Control Plane Availability

Critical warehouse services shall avoid single points of failure.

---

## SR-102 — Metadata Availability

Warehouse metadata shall use highly available storage.

---

## 38. Scalability

## SR-103 — Horizontal Scalability

The platform shall support scaling of analytical compute independently from storage where supported.

---

## SR-104 — Concurrent Queries

The system shall support concurrent analytical workloads.

---

## SR-105 — Workload Isolation

The platform should support workload isolation for:

```text
BI
Ad-Hoc
ETL / ELT
AI
ML
Reporting
Administrative
```

---

## 39. Performance

## SR-106 — Query Performance

Critical dashboards shall have defined query-performance SLOs.

---

## SR-107 — Partitioning

Large fact tables shall support appropriate partitioning.

---

## SR-108 — Clustering

The platform shall support clustering, sorting, indexing, or equivalent optimization mechanisms where applicable.

---

## SR-109 — Materialization

Frequently accessed analytical queries shall support materialized views or equivalent optimizations.

---

## SR-110 — Caching

Appropriate analytical results may be cached subject to freshness requirements.

---

## 40. Workload Management

## SR-111 — Query Prioritization

The platform shall support workload prioritization.

---

## SR-112 — Resource Quotas

Warehouse workloads shall support resource quotas.

---

## SR-113 — Query Timeout

Expensive queries shall be terminated according to configurable policies.

---

## SR-114 — Cost Guardrails

Users and AI agents shall be prevented from unintentionally executing uncontrolled expensive queries.

---

## 41. Data Freshness

## SR-115 — Freshness SLA

Datasets shall define freshness expectations.

Examples:

```text
REAL_TIME
NEAR_REAL_TIME
HOURLY
DAILY
WEEKLY
ON_DEMAND
```

---

## SR-116 — Freshness Monitoring

The system shall detect stale datasets.

---

## 42. Metadata Catalog

## SR-117 — Dataset Catalog

The warehouse shall expose searchable metadata for analytical datasets.

---

## SR-118 — Schema Catalog

The platform shall maintain schema metadata.

---

## SR-119 — Metric Catalog

The platform shall maintain governed business metrics.

---

## SR-120 — Ownership Metadata

Production datasets shall have an owner and steward where required.

---

## 43. Observability

## SR-121 — Pipeline Metrics

The platform shall expose:

```text
pipeline_success_rate
pipeline_failure_rate
pipeline_duration
records_processed
records_failed
data_freshness
```

---

## SR-122 — Query Metrics

The platform shall expose:

```text
query_count
query_latency
query_failure_rate
bytes_scanned
compute_usage
result_size
```

---

## SR-123 — Warehouse Metrics

The platform shall expose:

```text
storage_usage
compute_usage
concurrency
queue_time
cost
```

---

## 44. Audit Logging

The system shall audit:

```text
WAREHOUSE_CREATED
DATASET_CREATED
DATASET_UPDATED
DATASET_DELETED
TABLE_CREATED
TABLE_UPDATED
TABLE_DELETED
SCHEMA_CHANGED
QUERY_EXECUTED
QUERY_FAILED
QUERY_DENIED
DATA_EXPORTED
DASHBOARD_CREATED
DASHBOARD_UPDATED
DASHBOARD_SHARED
REPORT_GENERATED
AI_QUERY_EXECUTED
AI_QUERY_DENIED
METRIC_CREATED
METRIC_UPDATED
POLICY_CHANGED
ACCESS_GRANTED
ACCESS_DENIED
```

Audit records shall include:

```text
event_id
tenant_id
organization_id
actor_id
actor_type
resource_id
action
timestamp
result
trace_id
correlation_id
```

---

## 45. Cost Management

## SR-124 — Storage Cost

The platform shall track warehouse storage cost.

---

## SR-125 — Compute Cost

The platform shall track analytical compute cost.

---

## SR-126 — Query Cost

The platform shall identify expensive analytical queries.

---

## SR-127 — Tenant Cost

Where supported, analytical consumption shall be attributable to:

```text
tenant
organization
workspace
user
workload
```

---

## SR-128 — AI Analytics Cost

AI-generated analytical queries shall be associated with AI usage and cost telemetry.

---

## 46. Billing Integration

Warehouse analytics shall integrate with SalesGenie's billing and usage systems.

The warehouse shall support analytical datasets for:

```text
subscriptions
plans
usage
quotas
credits
payments
invoices
refunds
coupons
discounts
upgrades
downgrades
churn
revenue
```

---

## 47. Functional Requirements

## 47.1 Warehouse Management

## FR-001 — Create Analytical Dataset

The system shall create governed analytical datasets.

---

## FR-002 — Register Dataset

The system shall register dataset metadata.

---

## FR-003 — Register Schema

The system shall register table and column schemas.

---

## FR-004 — Version Dataset

The system shall maintain dataset versions where required.

---

## 47.2 Data Loading

## FR-005 — Load Batch Data

The system shall load batch data into staging or integration layers.

---

## FR-006 — Load Incremental Data

The system shall load only changed records when incremental loading is configured.

---

## FR-007 — Process CDC

The system shall process CDC streams where supported.

---

## FR-008 — Validate Loaded Data

The system shall validate loaded data before promotion.

---

## 47.3 Transformation

## FR-009 — Execute Transformation

The system shall execute approved transformation jobs.

---

## FR-010 — Version Transformation

The system shall associate transformation versions with generated datasets.

---

## FR-011 — Retry Transformation

Retryable transformation failures shall be retried according to policy.

---

## FR-012 — Quarantine Failed Data

Critical transformation failures shall route affected data to an appropriate failure or quarantine mechanism.

---

## 47.4 Dimensional Modeling

## FR-013 — Create Dimension

Authorized engineers shall be able to create dimensions.

---

## FR-014 — Create Fact

Authorized engineers shall be able to create fact tables.

---

## FR-015 — Maintain SCD

The system shall maintain configured slowly changing dimensions.

---

## FR-016 — Maintain Historical Facts

The system shall preserve historical facts according to retention policy.

---

## 47.5 Data Marts

## FR-017 — Create Data Mart

Authorized users shall be able to create governed data marts.

---

## FR-018 — Refresh Data Mart

The system shall refresh marts according to configured schedules.

---

## FR-019 — Monitor Mart Freshness

The system shall detect stale data marts.

---

## 47.6 Business Metrics

## FR-020 — Define Metric

Authorized users shall be able to define governed metrics.

---

## FR-021 — Version Metric

Metric definitions shall support versioning.

---

## FR-022 — Validate Metric

Metric definitions shall be validated against approved warehouse models.

---

## FR-023 — Use Metric

Dashboards and AI analytics shall consume governed metrics where applicable.

---

## 47.7 Query

## FR-024 — Execute Query

Authorized users shall be able to execute approved analytical queries.

---

## FR-025 — Validate Query

Queries shall be validated before execution.

---

## FR-026 — Enforce Query Limits

The system shall enforce:

```text
timeout
row_limit
scan_limit
resource_limit
concurrency_limit
```

---

## FR-027 — Cache Query

Eligible query results may be cached.

---

## FR-028 — Cancel Query

Authorized users shall be able to cancel their running queries.

---

## 47.8 Natural Language Analytics

## FR-029 — Accept Natural Language Query

The AI analytics interface shall accept natural-language questions.

---

## FR-030 — Generate SQL

The AI shall generate SQL or equivalent analytical queries.

---

## FR-031 — Validate Generated Query

The platform shall validate AI-generated queries.

---

## FR-032 — Execute Authorized Query

Only authorized queries shall execute.

---

## FR-033 — Explain Result

The AI shall provide a concise explanation of the analytical result.

---

## FR-034 — Provide Provenance

AI analytical responses shall expose appropriate dataset or metric provenance.

---

## 47.9 Dashboard

## FR-035 — Create Dashboard

Authorized users shall be able to create dashboards.

---

## FR-036 — Add Visualization

Users shall be able to add approved visualizations.

---

## FR-037 — Configure Filters

Users shall be able to configure dashboard filters.

---

## FR-038 — Schedule Refresh

Dashboards shall support configurable refresh schedules.

---

## FR-039 — Share Dashboard

Authorized users shall be able to share dashboards according to policy.

---

## 47.10 Reporting

## FR-040 — Generate Report

The platform shall generate reports from governed datasets.

---

## FR-041 — Schedule Report

Reports shall support scheduling.

---

## FR-042 — Export Report

Authorized users shall be able to export reports.

---

## FR-043 — Audit Report Access

Sensitive report access shall be audited.

---

## 47.11 Sales Analytics

## FR-044 — Calculate Pipeline

The system shall calculate sales pipeline metrics.

---

## FR-045 — Calculate Conversion

The system shall calculate configurable conversion metrics.

---

## FR-046 — Calculate Sales Velocity

The system shall calculate sales-cycle and pipeline velocity metrics.

---

## 47.12 Customer Analytics

## FR-047 — Build Customer 360

The platform shall combine authorized customer data into analytical Customer 360 views.

---

## FR-048 — Calculate Customer Metrics

The system shall calculate configurable customer metrics.

---

## FR-049 — Segment Customers

The platform shall support analytical customer segmentation.

---

## 47.13 Support Analytics

## FR-050 — Calculate Support Metrics

The system shall calculate support KPIs.

---

## FR-051 — Calculate SLA Metrics

The system shall calculate SLA compliance metrics.

---

## FR-052 — Analyze Agent Performance

The platform shall calculate support-agent performance metrics.

---

## 47.14 AI Analytics

## FR-053 — Track AI Requests

The warehouse shall store AI interaction analytics.

---

## FR-054 — Track Token Usage

The system shall store token usage where available.

---

## FR-055 — Track AI Cost

The system shall calculate AI cost using configured provider pricing.

---

## FR-056 — Track AI Quality

The system shall store AI evaluation metrics.

---

## 47.15 Subscription Analytics

## FR-057 — Calculate MRR

The system shall calculate Monthly Recurring Revenue according to configured business rules.

---

## FR-058 — Calculate ARR

The system shall calculate Annual Recurring Revenue according to configured business rules.

---

## FR-059 — Calculate Churn

The system shall calculate configurable customer and revenue churn.

---

## FR-060 — Analyze Upgrades

The system shall analyze subscription upgrades.

---

## FR-061 — Analyze Downgrades

The system shall analyze subscription downgrades.

---

## 47.16 Usage Analytics

## FR-062 — Aggregate Usage

The system shall aggregate usage by:

```text
tenant
organization
workspace
user
feature
plan
billing_period
```

---

## FR-063 — Compare Usage

The platform shall support usage comparison across periods.

---

## FR-064 — Detect Usage Anomalies

AI shall identify unusual usage patterns.

---

## 47.17 Marketing Analytics

## FR-065 — Track Campaign Performance

The system shall track campaign performance.

---

## FR-066 — Calculate Attribution

The platform shall calculate configurable attribution models.

---

## FR-067 — Calculate Campaign ROI

The system shall calculate campaign ROI using configured inputs.

---

## 47.18 Workflow Analytics

## FR-068 — Track Workflow Executions

The system shall record workflow executions.

---

## FR-069 — Calculate Workflow Success Rate

The system shall calculate workflow success rates.

---

## FR-070 — Analyze Workflow Failures

The system shall identify workflow failure patterns.

---

## 47.19 Forecasting

## FR-071 — Generate Forecast

Authorized AI services shall generate forecasts using approved datasets.

---

## FR-072 — Store Forecast

Forecasts shall be versioned and stored.

---

## FR-073 — Compare Forecast

The system shall compare forecast versus actual results.

---

## FR-074 — Measure Forecast Accuracy

The platform shall calculate configured forecasting accuracy metrics.

---

## 47.20 Anomaly Detection

## FR-075 — Detect Metric Anomalies

The system shall identify statistically or model-detected anomalies.

---

## FR-076 — Generate Alert

The system shall generate alerts for configured anomaly thresholds.

---

## FR-077 — Explain Anomaly

AI shall provide potential contributing factors using authorized datasets.

---

## 47.21 Data Quality

## FR-078 — Execute Quality Rules

The system shall execute warehouse data-quality rules.

---

## FR-079 — Record Quality Result

The system shall store quality results.

---

## FR-080 — Block Failed Publication

Critical quality failures shall prevent dataset publication.

---

## 47.22 Reconciliation

## FR-081 — Reconcile Counts

The system shall compare source and warehouse record counts.

---

## FR-082 — Reconcile Financial Values

Financial datasets shall support amount reconciliation.

---

## FR-083 — Report Reconciliation Failure

The system shall generate alerts for material reconciliation failures.

---

## 47.23 Lineage

## FR-084 — Record Source Lineage

The system shall record source-to-warehouse lineage.

---

## FR-085 — Record Transformation Lineage

The system shall record transformations.

---

## FR-086 — Display Lineage

Authorized users shall be able to inspect dataset lineage.

---

## 47.24 Security

## FR-087 — Authenticate

Users and services shall authenticate before warehouse access.

---

## FR-088 — Authorize

The system shall authorize every protected warehouse operation.

---

## FR-089 — Enforce Tenant Isolation

Unauthorized cross-tenant access shall be rejected.

---

## FR-090 — Mask Sensitive Fields

Sensitive fields shall be masked according to policy.

---

## FR-091 — Audit Access

Sensitive warehouse access shall be logged.

---

## 47.25 Privacy

## FR-092 — Apply Data Minimization

Analytical transformations shall minimize unnecessary personal data.

---

## FR-093 — Process Deletion Events

Applicable deletion events shall trigger warehouse processing.

---

## FR-094 — Enforce Retention

Warehouse retention policies shall be enforced.

---

## 47.26 Export

## FR-095 — Validate Export

The system shall validate export authorization.

---

## FR-096 — Apply DLP

Sensitive exports shall undergo DLP checks where configured.

---

## FR-097 — Audit Export

Exports shall generate audit events.

---

## 47.27 Cost

## FR-098 — Track Warehouse Usage

The system shall track analytical resource usage.

---

## FR-099 — Identify Expensive Queries

The system shall identify expensive queries.

---

## FR-100 — Generate Cost Recommendations

AI shall recommend:

* Query optimization
* Partitioning
* Materialization
* Caching
* Workload isolation
* Storage optimization

---

## 48. AI Analytics Workflow

```text
Human Question
       |
       v
AI Analytics Agent
       |
       v
Intent Classification
       |
       v
Authorization Context
       |
       v
Semantic Metric Discovery
       |
       v
Schema Discovery
       |
       v
SQL Generation
       |
       v
SQL Validation
       |
       v
Security / Policy Validation
       |
       v
Cost Estimation
       |
       v
Query Execution
       |
       v
Result Validation
       |
       v
Statistical / AI Analysis
       |
       v
Explanation
       |
       v
Provenance
       |
       v
Human / Application
```

---

## 49. Human Analytics Workflow

```text
Human
  |
  v
Dashboard / Query Interface
  |
  v
Authentication
  |
  v
Authorization
  |
  v
Semantic Layer
  |
  v
Query Engine
  |
  v
Warehouse
  |
  v
Result
  |
  v
Visualization / Report
```

---

## 50. AI + Human Collaborative Workflow

```text
Human
  |
  v
Business Question
  |
  v
AI Analysis
  |
  +----> Dataset Discovery
  |
  +----> Metric Discovery
  |
  +----> Query Generation
  |
  +----> Statistical Analysis
  |
  +----> Anomaly Detection
  |
  v
AI Recommendation
  |
  v
Human Validation
  |
  +----> Approve
  |
  +----> Modify
  |
  +----> Reject
  |
  v
Final Analytical Output
```

---

## 51. Recommended Data Warehouse Marts

## Sales Mart

```text
fact_sales_activity
fact_deal
fact_opportunity
dim_sales_agent
dim_company
dim_customer
dim_date
```

## Lead Mart

```text
fact_lead
fact_lead_event
fact_lead_score
dim_lead_source
dim_company
dim_industry
dim_date
```

## Customer Mart

```text
fact_customer_interaction
fact_customer_usage
fact_customer_revenue
dim_customer
dim_company
dim_plan
dim_region
```

## Support Mart

```text
fact_support_ticket
fact_support_interaction
fact_escalation
dim_support_agent
dim_channel
dim_issue
dim_customer
```

## Billing Mart

```text
fact_invoice
fact_payment
fact_refund
fact_subscription
fact_usage
dim_plan
dim_customer
dim_billing_period
```

## AI Mart

```text
fact_ai_interaction
fact_ai_token_usage
fact_ai_cost
fact_ai_evaluation
fact_ai_latency
dim_ai_agent
dim_model
dim_provider
dim_feature
```

## Product Mart

```text
fact_product_event
fact_feature_usage
fact_session
fact_activation
dim_user
dim_customer
dim_feature
dim_product
dim_date
```

## Workflow Mart

```text
fact_workflow_execution
fact_workflow_action
fact_workflow_error
dim_workflow
dim_action
dim_user
dim_customer
```

---

## 52. Data Warehouse Naming Standards

Tables should use explicit prefixes where appropriate:

```text
fact_*
dim_*
bridge_*
stg_*
int_*
mart_*
agg_*
snapshot_*
```

Examples:

```text
fact_lead
fact_payment
dim_customer
dim_plan
stg_salesforce_contact
int_customer_360
mart_sales_performance
agg_daily_revenue
snapshot_subscription
```

---

## 53. Data Warehouse State Model

```text
REGISTERED
    |
    v
LOADING
    |
    v
VALIDATING
    |
    v
TRANSFORMING
    |
    v
QUALITY_CHECK
    |
    v
PUBLISHED
    |
    v
SERVING
```

Alternative states:

```text
FAILED
BLOCKED
QUARANTINED
STALE
DEPRECATED
ARCHIVED
DELETED
```

---

## 54. Data Freshness State

```text
FRESH
   |
   v
AGING
   |
   v
STALE
   |
   v
CRITICAL_STALE
```

The thresholds shall be dataset-specific.

---

## 55. Warehouse Data Contracts

Each critical dataset shall define:

```text
dataset_id
owner
business_definition
grain
schema
primary_key
foreign_keys
freshness_slo
quality_slo
retention_policy
security_classification
lineage
consumer_contract
```

---

## 56. Business Metric Contracts

Each governed metric shall define:

```text
metric_id
metric_name
description
business_definition
formula
grain
dimensions
filters
source_tables
owner
version
effective_from
effective_until
```

Example:

```text
metric:
  name: monthly_recurring_revenue

  definition:
    recurring subscription revenue
    recognized according to configured
    SalesGenie billing rules

  dimensions:
    tenant
    plan
    region
    customer_segment
    billing_period
```

---

## 57. Data Quality Rules

Examples:

```text
lead_id IS NOT NULL
customer_id IS NOT NULL
tenant_id IS NOT NULL
event_timestamp IS NOT NULL
subscription_id IS NOT NULL
invoice_id IS NOT NULL
payment_amount >= 0
refund_amount >= 0
conversion_rate BETWEEN 0 AND 1
```

Critical constraints shall fail the corresponding quality gate when violated.

---

## 58. AI Model Analytics

The warehouse shall support model-level analytics:

```text
model_id
provider
model_version
request_count
success_rate
error_rate
input_tokens
output_tokens
latency
cost
quality_score
user_feedback
evaluation_score
```

---

## 59. AI Agent Analytics

The warehouse shall support:

```text
agent_id
agent_version
agent_type
execution_count
success_rate
failure_rate
average_latency
tool_calls
token_usage
cost
human_escalations
user_feedback
quality_score
```

---

## 60. AI Decision Governance

AI analytical decisions shall retain:

```text
decision_id
agent_id
model_id
model_version
input_reference
query
query_version
dataset_version
result_reference
confidence
timestamp
human_review_required
review_status
reviewer_id
```

---

## 61. Human Override

Authorized users shall be able to:

```text
APPROVE
REJECT
MODIFY
ESCALATE
```

AI analytical recommendations.

Every override shall preserve:

```text
previous_result
new_result
reviewer
reason
timestamp
```

---

## 62. Data Warehouse API Requirements

The platform should expose APIs for:

```text
/datasets
/schemas
/tables
/queries
/metrics
/dashboards
/reports
/lineage
/quality
/forecasting
/anomalies
/usage
/cost
```

All APIs shall enforce:

* Authentication
* Authorization
* Tenant isolation
* Rate limiting
* Validation
* Audit logging

---

## 63. Event Integration

The Data Warehouse shall consume relevant events such as:

```text
USER_CREATED
CUSTOMER_CREATED
LEAD_CREATED
LEAD_QUALIFIED
LEAD_CONVERTED
DEAL_CREATED
DEAL_WON
SUPPORT_TICKET_CREATED
SUPPORT_TICKET_RESOLVED
AI_REQUEST_COMPLETED
WORKFLOW_EXECUTED
SUBSCRIPTION_CREATED
SUBSCRIPTION_UPGRADED
SUBSCRIPTION_DOWNGRADED
SUBSCRIPTION_CANCELLED
PAYMENT_SUCCEEDED
PAYMENT_FAILED
REFUND_CREATED
COUPON_APPLIED
USAGE_RECORDED
```

Events shall be processed idempotently.

---

## 64. Failure Handling

Failures shall be categorized as:

```text
INGESTION_FAILURE
SCHEMA_FAILURE
TRANSFORMATION_FAILURE
QUALITY_FAILURE
RECONCILIATION_FAILURE
QUERY_FAILURE
AUTHORIZATION_FAILURE
PRIVACY_FAILURE
SECURITY_FAILURE
AI_FAILURE
RESOURCE_FAILURE
COST_LIMIT_FAILURE
```

Retryable failures shall use controlled retry policies.

Non-retryable failures shall be surfaced to operators.

---

## 65. Dead-Letter Processing

Failed analytical events shall support dead-letter handling.

Each failed event shall preserve:

```text
event_id
tenant_id
pipeline_id
execution_id
failure_stage
error_code
retryable
attempt_count
timestamp
trace_id
```

Sensitive payloads shall not be written to logs unnecessarily.

---

## 66. Performance Optimization

The warehouse shall support, where applicable:

* Partition pruning
* Predicate pushdown
* Column pruning
* Clustering
* Sorting
* Materialized views
* Aggregate tables
* Result caching
* Query caching
* Incremental models
* Parallel execution
* Workload management

---

## 67. BI Integration

The Data Warehouse shall support integration with approved BI tools through:

* SQL
* APIs
* JDBC/ODBC
* Semantic models
* Export interfaces

BI consumers shall only access governed datasets.

---

## 68. Machine Learning Integration

The warehouse shall provide approved datasets for:

* Feature engineering
* Model training
* Model evaluation
* Forecasting
* Classification
* Ranking
* Recommendation
* Churn prediction
* Lead scoring
* Customer segmentation

ML datasets shall retain lineage to source data.

---

## 69. Compliance

The warehouse shall support controls relevant to applicable:

* GDPR
* CCPA/CPRA
* SOC 2
* ISO 27001
* Contractual data requirements
* Industry-specific requirements where applicable

Compliance applicability shall be configurable per tenant, deployment, dataset, and jurisdiction where appropriate.

---

## 70. Security Monitoring

The warehouse shall support monitoring of:

* Unusual query patterns
* Excessive exports
* Unauthorized access
* Cross-tenant access attempts
* Sensitive-data queries
* Privilege changes
* AI query anomalies
* Credential misuse
* Abnormal resource consumption

---

## 71. Cost Optimization

AI-assisted cost optimization shall identify:

```text
EXPENSIVE_QUERY
DUPLICATE_MODEL
UNUSED_TABLE
UNUSED_COLUMN
STALE_MATERIALIZATION
OVER_PARTITIONING
UNDER_PARTITIONING
EXCESSIVE_SCAN
EXCESSIVE_REFRESH
UNUSED_DASHBOARD
```

Recommendations shall be explainable and reviewable.

---

## 72. Capacity Planning

The platform shall monitor:

```text
storage_growth
query_growth
compute_growth
concurrency_growth
dataset_growth
tenant_growth
AI_analytics_growth
```

The system shall support capacity forecasting.

---

## 73. SLO Requirements

Critical analytical datasets shall define:

```text
Freshness SLO
Availability SLO
Query Latency SLO
Quality SLO
Recovery SLO
```

Example:

```text
Critical Revenue Dataset
  Freshness: <= 15 minutes
  Availability: >= 99.9%
  Quality: >= configured threshold
```

Actual targets shall be configurable according to workload criticality.

---

## 74. Security Acceptance Criteria

The warehouse shall not be considered production-ready until:

* [ ] Tenant isolation has been tested.
* [ ] Row-level security has been tested where applicable.
* [ ] Sensitive-field masking has been tested.
* [ ] RBAC has been tested.
* [ ] ABAC has been tested where configured.
* [ ] Export controls have been tested.
* [ ] AI query authorization has been tested.
* [ ] Prompt injection defenses have been tested.
* [ ] SQL-generation safeguards have been tested.
* [ ] Encryption has been verified.
* [ ] Secret management has been verified.
* [ ] Audit logging has been verified.

---

## 75. Data Quality Acceptance Criteria

* [ ] Critical datasets have documented schemas.
* [ ] Dataset grain is documented.
* [ ] Primary keys are validated.
* [ ] Foreign-key relationships are validated where applicable.
* [ ] Null constraints are tested.
* [ ] Duplicate detection works.
* [ ] Freshness monitoring works.
* [ ] Reconciliation works.
* [ ] Quality gates work.
* [ ] Failed datasets cannot silently become trusted datasets.

---

## 76. AI Acceptance Criteria

* [ ] Natural-language analytics works.
* [ ] AI-generated SQL is validated.
* [ ] AI queries inherit user authorization.
* [ ] AI cannot bypass tenant isolation.
* [ ] AI cannot access unauthorized datasets.
* [ ] AI cannot escalate privileges.
* [ ] AI query costs are controlled.
* [ ] AI responses contain appropriate provenance.
* [ ] AI analytical decisions are auditable.
* [ ] Human review works for configured high-risk workflows.
* [ ] AI anomalies are explainable enough for operational review.
* [ ] AI-generated forecasts are versioned.
* [ ] AI model metadata is preserved.

---

## 77. Reliability Acceptance Criteria

* [ ] Batch loading works.
* [ ] Incremental loading works.
* [ ] CDC works where configured.
* [ ] Pipeline retries work.
* [ ] Dead-letter handling works.
* [ ] Idempotency works.
* [ ] Pipeline recovery works.
* [ ] Dataset reconciliation works.
* [ ] Backup works.
* [ ] Restore works.
* [ ] Disaster recovery has been tested.

---

## 78. Performance Acceptance Criteria

* [ ] Critical dashboard queries meet defined SLOs.
* [ ] Large fact tables are optimized.
* [ ] Partitioning strategy is validated.
* [ ] Expensive queries are detected.
* [ ] Query limits are enforced.
* [ ] Concurrent workloads are tested.
* [ ] AI-generated query workloads are tested.
* [ ] Multi-tenant workloads are tested.
* [ ] Capacity limits are documented.

---

## 79. Enterprise Data Warehouse Lifecycle

```text
SOURCE SYSTEMS
      |
      v
INGESTION
      |
      v
STAGING
      |
      v
DATA VALIDATION
      |
      v
INTEGRATION
      |
      v
CORE WAREHOUSE
      |
      v
DATA MARTS
      |
      v
SEMANTIC LAYER
      |
      +-----------------------+
      |                       |
      v                       v
BI / REPORTING            AI / ML
      |                       |
      +-----------+-----------+
                  |
                  v
             BUSINESS USE
                  |
                  v
            GOVERNANCE
                  |
                  v
        RETENTION / ARCHIVE
                  |
                  v
               DELETE
```

---

## 80. Definition of Done

A SalesGenie Data Warehouse capability shall be considered production-ready only when:

```text
SOURCE
  ↓
INGESTION
  ↓
STAGING
  ↓
VALIDATION
  ↓
INTEGRATION
  ↓
CORE WAREHOUSE
  ↓
DIMENSIONAL MODEL
  ↓
DATA MART
  ↓
SEMANTIC MODEL
  ↓
BI / AI / ML
```

is fully observable, secure, governed, auditable, and recoverable.

The implementation shall additionally provide:

* [ ] Multi-tenant isolation.
* [ ] RBAC.
* [ ] ABAC where required.
* [ ] Row-level security.
* [ ] Column-level protection.
* [ ] Encryption.
* [ ] Data-quality controls.
* [ ] Data reconciliation.
* [ ] Data lineage.
* [ ] Metric governance.
* [ ] Schema governance.
* [ ] Historical modeling.
* [ ] SCD support.
* [ ] Batch ingestion.
* [ ] Incremental ingestion.
* [ ] CDC where applicable.
* [ ] Data marts.
* [ ] Semantic layer.
* [ ] BI integration.
* [ ] Natural-language analytics.
* [ ] AI SQL generation.
* [ ] AI query validation.
* [ ] AI authorization.
* [ ] AI anomaly detection.
* [ ] AI forecasting.
* [ ] AI cost tracking.
* [ ] Human-in-the-loop controls.
* [ ] Privacy controls.
* [ ] Retention controls.
* [ ] Deletion workflows.
* [ ] Backup and recovery.
* [ ] Disaster recovery.
* [ ] Performance monitoring.
* [ ] Cost monitoring.
* [ ] Audit logging.
* [ ] Security monitoring.
* [ ] Capacity planning.
* [ ] Production load testing.
* [ ] Security testing.
* [ ] Failure testing.
* [ ] Disaster-recovery testing.

---

## 81. Engineering Principles

The SalesGenie Data Warehouse shall follow these principles:

1. **The warehouse is an analytical system, not an OLTP replacement.**
2. **Every analytical dataset has a defined grain.**
3. **Every critical metric has a governed definition.**
4. **Every production dataset has an owner.**
5. **Tenant isolation is mandatory.**
6. **Authorization is enforced at query execution time.**
7. **AI agents never receive privileges beyond their authorization context.**
8. **AI-generated SQL is untrusted until validated.**
9. **Sensitive data is minimized.**
10. **Critical data transformations are version-controlled.**
11. **Analytical results must be reproducible where required.**
12. **Source-to-report lineage must be traceable.**
13. **Data quality failures cannot silently propagate.**
14. **Historical business states must be preserved where required.**
15. **Business metrics must have a single governed definition.**
16. **Financial analytics must be reconcilable to authoritative billing data.**
17. **AI-generated insights must retain provenance.**
18. **High-impact AI recommendations must support human oversight.**
19. **Expensive queries must be controlled.**
20. **Analytical workloads must be observable.**
21. **Critical datasets must be recoverable.**
22. **Privacy deletion requirements must propagate into analytical systems where applicable.**
23. **Security events must be auditable.**
24. **Warehouse compute and storage must be cost-aware.**
25. **The architecture must scale independently across storage, compute, ingestion, BI, and AI workloads.**
26. **The warehouse shall provide trusted data products rather than an uncontrolled collection of tables.**
27. **Human and AI consumers shall use the same governed analytical definitions whenever possible.**
28. **The system shall fail safely rather than silently return misleading analytical results.**

---

## 82. Final Enterprise Data Warehouse Architecture

```text
                         SALES GENIE
                              |
       +----------------------+----------------------+
       |                      |                      |
       v                      v                      v
 Operational Systems     Data Lake              Event Platform
       |                      |                      |
       +----------------------+----------------------+
                              |
                              v
                       ELT / ETL Layer
                              |
                              v
                    +-------------------+
                    |  STAGING LAYER    |
                    +---------+---------+
                              |
                              v
                    +-------------------+
                    | INTEGRATION LAYER |
                    +---------+---------+
                              |
                              v
                    +-------------------+
                    |   CORE WAREHOUSE  |
                    +---------+---------+
                              |
             +----------------+----------------+
             |                |                |
             v                v                v
        SALES MART       CUSTOMER MART     BILLING MART
             |                |                |
             +----------------+----------------+
                              |
             +----------------+----------------+
             |                |                |
             v                v                v
       SUPPORT MART       AI MART        PRODUCT MART
             |                |                |
             +----------------+----------------+
                              |
                              v
                     SEMANTIC LAYER
                              |
            +-----------------+------------------+
            |                 |                  |
            v                 v                  v
       BI / REPORTING     AI ANALYTICS        ML / DS
            |                 |                  |
            +-----------------+------------------+
                              |
                              v
                     BUSINESS DECISIONS
                              |
                              v
                 GOVERNANCE / SECURITY / AUDIT
                              |
                              v
                 RETENTION / ARCHIVE / DELETE
```

The SalesGenie Data Warehouse shall therefore function as the **governed analytical system of record for enterprise business intelligence**, integrating operational and Data Lake data into trusted, historical, secure, multi-tenant, AI-accessible analytical datasets for both human decision-makers and AI agents.
