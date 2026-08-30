# SalesGenie — Cohort Analysis Requirements

**Document:** `cohort_analysis.md`  
**Project:** SalesGenie / FlowMind AI  
**Requirement Type:** User Requirements + System Requirements + Functional Requirements  
**Architecture:** Enterprise SaaS + Microservices + Event-Driven + Multi-Agent AI  
**Execution Modes:** AI-driven + Human-driven + Human-in-the-Loop  
**Target Scale:** 10M+ users, 500K+ concurrent conversations  
**Priority:** Enterprise / Production / FAANG-Level

---

## 1. Purpose

The Cohort Analysis subsystem SHALL provide an enterprise-grade framework for grouping users, customers, leads, organizations, accounts, conversations, and other business entities into analytically meaningful cohorts and measuring their behavior, conversion, retention, engagement, revenue, support, AI usage, and lifecycle outcomes over time.

The subsystem SHALL enable SalesGenie to answer:

- How do users acquired in different periods behave over time?
- Which acquisition channels produce the highest-quality customers?
- Which customer cohorts retain the longest?
- Which cohorts generate the highest lifetime value?
- Which cohorts adopt AI features fastest?
- Which cohorts convert from trial to paid subscription?
- Which cohorts churn fastest?
- Which AI agents perform best for specific cohorts?
- Which product releases improve or harm cohort behavior?
- Which customer segments require intervention?
- What future outcomes are likely for each cohort?

The system SHALL support:

```text
Human-driven cohort analysis
AI-driven cohort analysis
AI-assisted analyst workflows
Automated cohort monitoring
Predictive cohort intelligence
Human-approved AI interventions
```

---

## 2. Scope

## 2.1 In Scope

The system SHALL support:

1. Cohort definition
2. Cohort creation
3. Cohort templates
4. Cohort types
5. Cohort dimensions
6. Cohort membership
7. Cohort lifecycle
8. Cohort retention
9. Cohort conversion
10. Cohort engagement
11. Cohort revenue
12. Cohort churn
13. Cohort expansion
14. Cohort activation
15. Cohort behavior
16. Cohort funnel performance
17. Cohort segmentation
18. Cohort comparison
19. Cohort benchmarking
20. Cohort forecasting
21. Cohort anomaly detection
22. AI cohort discovery
23. AI cohort explanation
24. AI cohort recommendations
25. Cohort experimentation
26. Cohort attribution
27. Cohort profitability
28. Cohort health scoring
29. Cohort alerts
30. Cohort reporting
31. Cohort dashboards
32. Real-time cohort monitoring
33. Historical cohort analysis
34. Natural-language cohort queries
35. Privacy-aware cohort analysis
36. Tenant-aware cohort isolation
37. Cohort governance
38. Cohort auditability

---

## 3. Actors

## 3.1 Human Actors

* End User
* Customer
* Lead
* Sales Agent
* Support Agent
* Customer Success Manager
* Sales Manager
* Marketing Manager
* Product Manager
* Revenue Operations Manager
* Organization Admin
* Tenant Admin
* Super Admin
* Data Analyst
* Business Analyst
* Data Scientist
* Data Engineer
* ML Engineer
* AI Engineer
* Executive
* Compliance Officer
* Auditor

## 3.2 AI Actors

* AI Analytics Agent
* AI Cohort Analyst
* AI Customer Intelligence Agent
* AI Segmentation Agent
* AI Forecasting Agent
* AI Recommendation Agent
* AI Churn Prediction Agent
* AI Revenue Intelligence Agent
* AI Experimentation Agent
* AI Anomaly Detection Agent
* AI Orchestrator

## 3.3 System Actors

* Analytics Events Service
* Event Bus
* Funnel Analytics Engine
* Metrics Engine
* KPI Engine
* Analytics Platform
* Customer Data Platform
* Data Warehouse
* Data Lake
* AI Gateway
* Billing Service
* Subscription Service
* CRM Integrations
* Workflow Engine
* Marketing Integrations
* Support Services

---

## 4. Cohort Definition

A cohort SHALL represent a group of entities sharing a common qualifying characteristic, event, time period, behavioral pattern, acquisition source, lifecycle state, or business condition.

Example:

```text
Users whose first successful login occurred
during August 2026.
```

---

## 5. Cohort Model

```text
Cohort
├── Cohort ID
├── Tenant ID
├── Organization ID
├── Name
├── Description
├── Cohort Type
├── Membership Rule
├── Entry Event
├── Entry Date
├── Dimensions
├── Filters
├── Time Window
├── Metrics
├── Owner
├── Version
├── Status
└── Governance Policy
```

---

## 6. Cohort Types

The platform SHALL support:

```text
Time-Based Cohorts
Acquisition Cohorts
Behavioral Cohorts
Lifecycle Cohorts
Revenue Cohorts
Subscription Cohorts
Product Cohorts
Feature Adoption Cohorts
Campaign Cohorts
Channel Cohorts
Geographic Cohorts
Industry Cohorts
Lead Cohorts
Sales Cohorts
Support Cohorts
AI Usage Cohorts
AI Agent Cohorts
Experiment Cohorts
Churn Cohorts
Custom Cohorts
```

---

## 7. Time-Based Cohorts

Examples:

```text
January 2026 Signup Cohort
February 2026 Signup Cohort
March 2026 Signup Cohort
```

The system SHALL support:

```text
Daily
Weekly
Monthly
Quarterly
Yearly
Custom periods
```

---

## 8. User Requirements

## UR-001 — Cohort Visibility

Authorized users SHALL be able to view cohorts within their permitted tenant, organization, workspace, and data-access scope.

---

## UR-002 — Cohort Creation

Authorized users SHALL be able to create cohorts using:

* Events
* Attributes
* Dates
* Behavioral conditions
* Business conditions
* Subscription state
* Product usage
* AI usage
* Revenue
* Funnel stages

---

## UR-003 — Cohort Templates

The system SHALL provide reusable cohort templates.

Examples:

```text
New User Cohort
Trial Cohort
Paid Customer Cohort
Churned Customer Cohort
High-Value Customer Cohort
AI Power User Cohort
Enterprise Customer Cohort
High-Intent Lead Cohort
```

---

## UR-004 — Cohort Membership

Authorized users SHALL be able to determine which entities belong to a cohort and why.

---

## UR-005 — Cohort Comparison

Users SHALL be able to compare multiple cohorts.

Example:

```text
August 2026 users
vs
July 2026 users
```

---

## UR-006 — Cohort Retention

Users SHALL be able to measure retention over time.

---

## UR-007 — Cohort Conversion

Users SHALL be able to measure conversion rates across cohorts.

---

## UR-008 — Cohort Revenue

Users SHALL be able to analyze revenue generated by each cohort.

---

## UR-009 — Cohort Engagement

Users SHALL be able to analyze:

* Sessions
* Conversations
* Feature usage
* AI interactions
* Workflow execution
* Support interactions
* Integrations

---

## UR-010 — Cohort Churn

Users SHALL be able to identify cohorts with elevated churn.

---

## UR-011 — Cohort Lifetime Value

Users SHALL be able to analyze customer lifetime value by cohort.

---

## UR-012 — Cohort Funnel Analysis

Users SHALL be able to evaluate funnel performance for individual cohorts.

---

## UR-013 — Cohort Segmentation

Users SHALL be able to subdivide cohorts by:

```text
Region
Industry
Company size
Plan
Channel
Campaign
Agent
AI agent
Product
Feature
```

---

## UR-014 — Cohort Trends

Users SHALL be able to visualize cohort behavior across time.

---

## UR-015 — Cohort Heatmaps

The platform SHALL provide cohort heatmaps for:

* Retention
* Revenue
* Engagement
* Conversion
* Feature adoption

---

## UR-016 — Cohort Alerts

Authorized users SHALL be able to configure alerts for abnormal cohort behavior.

---

## UR-017 — Cohort Forecasts

Users SHALL be able to view predicted cohort outcomes.

---

## UR-018 — Natural-Language Cohort Analysis

Users SHALL be able to ask:

```text
"Compare the last six signup cohorts."

"Which cohort has the highest retention?"

"Why did the August cohort churn faster?"

"Which acquisition channel creates the highest-LTV customers?"

"Which cohort is most likely to upgrade?"
```

---

## 9. System Requirements

## SR-001 — Centralized Cohort Engine

SalesGenie SHALL provide a centralized Cohort Analysis Engine.

```text
Analytics Events
       ↓
Identity Resolution
       ↓
Cohort Definition Engine
       ↓
Membership Evaluation
       ↓
Cohort State
       ↓
Metric Computation
       ↓
Cohort Analytics
       ↓
AI Intelligence
```

---

## SR-002 — Event Integration

The cohort engine SHALL consume events from the Analytics Events subsystem.

---

## SR-003 — Customer Data Integration

The cohort engine SHALL integrate with the Customer Data Platform for authorized customer attributes.

---

## SR-004 — Funnel Integration

The cohort engine SHALL integrate with Funnel Analytics.

---

## SR-005 — Metrics Integration

The cohort engine SHALL consume metrics from the Metrics Engine.

---

## SR-006 — KPI Integration

Cohort-specific KPIs SHALL be consumable by the KPI Engine.

---

## SR-007 — Cohort Registry

The platform SHALL maintain a registry containing:

```text
Cohort ID
Name
Type
Owner
Definition
Version
Membership Rule
Dimensions
Metrics
Status
Created At
Updated At
```

---

## SR-008 — Cohort Versioning

Cohort definitions SHALL be versioned.

```text
enterprise_users_v1
enterprise_users_v2
enterprise_users_v3
```

Historical results SHALL remain reproducible.

---

## SR-009 — Membership Determinism

Deterministic cohort rules SHALL produce deterministic membership.

---

## SR-010 — Dynamic Cohorts

The system SHALL support dynamic cohorts whose membership changes as new events arrive.

---

## SR-011 — Static Cohorts

The system SHALL support frozen cohorts for historical experimentation and reporting.

---

## SR-012 — Cohort Snapshots

The system SHALL support point-in-time cohort snapshots.

---

## SR-013 — Cohort Recalculation

Authorized users SHALL be able to recalculate cohorts after:

* Event corrections
* Identity resolution changes
* Definition changes
* Data-quality corrections

---

## SR-014 — Cohort Reproducibility

Every analytical result SHALL be traceable to:

```text
Cohort Version
Event Version
Metric Version
Attribution Version
Model Version
Data Snapshot
```

---

## SR-015 — Identity Resolution

The platform SHALL support identity resolution across:

```text
Anonymous Visitor
User
Lead
Customer
Account
Organization
Conversation
Session
CRM Contact
```

---

## SR-016 — Cross-Channel Identity

The system SHALL support authorized cross-channel identity resolution.

---

## SR-017 — Tenant Isolation

Cohort data SHALL be isolated by:

```text
Tenant
Organization
Workspace
```

---

## SR-018 — Cohort Query Performance

Common cohort queries SHOULD target:

```text
P50 < 1 second
P95 < 3 seconds
P99 < 10 seconds
```

for precomputed or optimized analytical queries.

---

## SR-019 — Real-Time Cohort Updates

Real-time cohort membership updates SHOULD be available within:

```text
P50 < 2 seconds
P95 < 5 seconds
P99 < 15 seconds
```

after relevant event ingestion.

---

## SR-020 — Scalability

The system SHALL be designed for:

```text
10M+ users
500K+ concurrent conversations
Millions of events per minute
Millions of cohort memberships
Thousands of cohort definitions
High-cardinality dimensions
Large historical datasets
```

---

## 10. Functional Requirements

## FR-001 — Create Cohort

The system SHALL allow authorized users to create cohorts.

---

## FR-002 — Define Membership Rules

Users SHALL be able to define rules such as:

```text
Signup date >= 2026-08-01
AND
subscription = "pro"
```

---

## FR-003 — Event-Based Membership

The system SHALL support event-based membership.

Example:

```text
Users who triggered:

conversation.created
AND
lead.qualified
AND
meeting.booked
```

---

## FR-004 — Behavioral Membership

The system SHALL support behavioral conditions.

Example:

```text
Users with:
>10 AI conversations
AND
>3 workflows
```

---

## FR-005 — Attribute-Based Membership

The system SHALL support:

```text
Industry
Region
Plan
Company size
Role
Acquisition source
```

where permitted.

---

## FR-006 — Temporal Membership

The system SHALL support:

```text
Before event
After event
Within N days
Between dates
First occurrence
Last occurrence
Repeated occurrence
```

---

## FR-007 — Cohort Entry

The system SHALL record cohort entry timestamp.

---

## FR-008 — Cohort Exit

The system SHALL support cohort exit conditions where applicable.

---

## FR-009 — Cohort Re-Entry

The system SHALL support configurable re-entry behavior.

---

## FR-010 — Cohort Size

The system SHALL calculate:

```text
Total Members
Active Members
Inactive Members
Converted Members
Churned Members
```

---

## 11. Retention Analysis

## FR-011 — Retention Rate

The system SHALL calculate:

```text
Retention Rate =
Returning Active Members
/
Original Cohort Members
× 100
```

---

## FR-012 — Retention Periods

The system SHALL support:

```text
Day 1
Day 7
Day 14
Day 30
Day 60
Day 90
Month 3
Month 6
Month 12
Custom
```

---

## FR-013 — Retention Heatmap

The system SHALL provide cohort retention matrices.

Example:

```text
Cohort      M0     M1     M2     M3     M4
Jan 2026   100%    62%    48%    41%    37%
Feb 2026   100%    67%    51%    45%    40%
Mar 2026   100%    71%    56%    49%    44%
```

---

## 12. Conversion Analysis

## FR-014 — Cohort Conversion

The system SHALL calculate conversion rates by cohort.

---

## FR-015 — Funnel Conversion

The system SHALL calculate conversion at every funnel stage for each cohort.

---

## FR-016 — Time-to-Conversion

The system SHALL calculate:

```text
Average
Median
P90
P95
P99
```

time-to-conversion.

---

## 13. Revenue Analysis

## FR-017 — Cohort Revenue

The system SHALL calculate revenue generated by cohorts.

---

## FR-018 — Revenue Retention

The system SHALL support:

```text
Gross Revenue Retention
Net Revenue Retention
Expansion Revenue
Contraction Revenue
```

where applicable.

---

## FR-019 — Cohort ARPU

The system SHALL calculate:

```text
ARPU =
Cohort Revenue
/
Cohort Customers
```

---

## FR-020 — Cohort LTV

The system SHALL support customer lifetime value analysis by cohort.

---

## FR-021 — Cohort Payback

The platform SHOULD calculate CAC payback by cohort when acquisition-cost data is available.

---

## 14. Engagement Analysis

## FR-022 — Activity Analysis

The system SHALL analyze:

```text
Sessions
Messages
Conversations
Workflows
Integrations
Features
AI interactions
```

---

## FR-023 — Feature Adoption

The system SHALL measure feature adoption by cohort.

Example:

```text
August cohort:

RAG adoption: 71%
Workflow adoption: 63%
AI Sales Agent adoption: 54%
WhatsApp adoption: 41%
```

---

## FR-024 — Product Adoption Curves

The system SHALL calculate the time between cohort entry and feature adoption.

---

## 15. Subscription Cohorts

The platform SHALL support:

```text
Trial Cohorts
Free Cohorts
Starter Cohorts
Professional Cohorts
Enterprise Cohorts
Upgrade Cohorts
Downgrade Cohorts
Cancellation Cohorts
Renewal Cohorts
```

---

## 16. Trial Cohort Analysis

The system SHALL analyze:

```text
Trial activation
Trial engagement
Trial-to-paid conversion
Time-to-conversion
Trial abandonment
Feature adoption
```

---

## 17. Churn Cohorts

The system SHALL identify cohorts based on churn periods.

Example:

```text
Customers who cancelled in August 2026.
```

The system SHALL analyze:

* Previous engagement
* Feature usage
* Support activity
* AI usage
* Subscription history
* Revenue
* Churn reason

---

## 18. AI Usage Cohorts

The system SHALL support cohorts such as:

```text
AI Power Users
AI Casual Users
AI-Only Users
AI + Human Users
Human-Only Users
AI Sales Users
AI Support Users
```

---

## 19. AI-vs-Human Cohort Analysis

The system SHALL compare cohorts based on operational model:

```text
AI-only
Human-only
AI-assisted human
Human-assisted AI
```

Metrics SHALL include:

```text
Conversion
Retention
Revenue
Resolution
Response time
Customer satisfaction
Cost
```

---

## 20. Acquisition Cohorts

The platform SHALL support cohort analysis by:

```text
Google
Organic
Referral
Email
Social
Partner
Outbound
Sales team
Campaign
CRM source
```

subject to available attribution data.

---

## 21. Channel Cohorts

The system SHALL compare cohorts by communication channel:

```text
Web
Email
WhatsApp
SMS
Voice
CRM
Mobile
API
```

---

## 22. Campaign Cohorts

The system SHALL support campaign-based cohorts.

Example:

```text
Customers acquired from:
Campaign X
during August 2026.
```

---

## 23. Geographic Cohorts

The system MAY support:

```text
Country
Region
Market
Timezone
```

subject to privacy and authorization.

---

## 24. Industry Cohorts

The platform SHALL support B2B cohort analysis by:

```text
Industry
Company size
Revenue band
Business model
Customer tier
```

where such data is available and authorized.

---

## 25. Funnel + Cohort Integration

The system SHALL support:

```text
Cohort
   ↓
Funnel
   ↓
Stage
   ↓
Conversion
```

Example:

```text
August Enterprise Cohort

Lead → Qualified → Demo → Proposal → Won

Conversion:
8.2%
```

---

## 26. Cohort Comparison

The system SHALL support comparisons based on:

```text
Time
Acquisition source
Plan
Industry
Region
Campaign
AI agent
Human agent
Product version
Feature
Experiment
```

---

## 27. Benchmarking

The system SHALL calculate:

```text
Current cohort
Historical cohort median
Best-performing cohort
Worst-performing cohort
Organization benchmark
Team benchmark
```

---

## 28. AI Requirements

## AI-FR-001 — AI Cohort Discovery

AI SHALL identify potentially meaningful cohorts from behavioral and business data.

Example:

```text
AI detects:

Users with >20 AI interactions
have 2.4x higher retention.

Recommendation:
Create "AI Power User" cohort.
```

---

## AI-FR-002 — AI Cohort Recommendation

AI SHALL recommend cohorts that may provide business value.

---

## AI-FR-003 — AI Cohort Explanation

AI SHALL explain why a cohort differs from another.

---

## AI-FR-004 — AI Retention Analysis

AI SHALL identify patterns associated with retention and churn.

---

## AI-FR-005 — AI Churn Analysis

AI SHALL identify cohort characteristics associated with elevated churn.

---

## AI-FR-006 — AI Conversion Analysis

AI SHALL identify characteristics associated with higher conversion.

---

## AI-FR-007 — AI Revenue Analysis

AI SHALL identify high-value cohorts.

---

## AI-FR-008 — AI Feature Adoption Analysis

AI SHALL identify features associated with:

```text
Retention
Conversion
Expansion
Engagement
```

AI SHALL distinguish correlation from demonstrated causation.

---

## AI-FR-009 — AI Cohort Forecasting

AI SHALL forecast:

```text
Retention
Conversion
Revenue
Churn
Expansion
Engagement
```

---

## AI-FR-010 — AI Cohort Health

The system MAY generate a cohort health score based on:

```text
Retention
Engagement
Conversion
Revenue
Churn
Support activity
AI adoption
Trend
Anomaly
```

---

## AI-FR-011 — AI Anomaly Detection

AI SHALL detect abnormal cohort behavior.

Examples:

```text
Unexpected retention decline
Unusual churn spike
Sudden engagement collapse
Unexpected revenue increase
Abnormal feature adoption
```

---

## AI-FR-012 — AI Root-Cause Analysis

AI SHALL analyze differences between cohorts using available evidence.

---

## AI-FR-013 — AI Natural-Language Queries

Users SHALL be able to ask:

```text
"Why is the August cohort worse than July?"

"Which cohort has the highest LTV?"

"Which features predict retention?"

"Which customer cohort is most likely to upgrade?"
```

---

## AI-FR-014 — AI Segmentation

AI SHALL identify latent behavioral segments where appropriate.

AI-generated segments SHALL be clearly distinguished from deterministic business cohorts.

---

## AI-FR-015 — AI Experiment Recommendations

AI MAY recommend experiments based on cohort differences.

Example:

```text
Observation:
Customers using RAG within 7 days
show higher retention.

Recommendation:
Test early RAG onboarding.
```

---

## 29. AI Prediction Governance

AI predictions SHALL include:

```text
Prediction
Probability
Model
Model Version
Prediction Timestamp
Feature Set Version
Confidence / Uncertainty
```

Predictions SHALL NOT be represented as guaranteed outcomes.

---

## 30. Human-Based Requirements

## HUMAN-FR-001 — Manual Cohort Creation

Authorized users SHALL be able to manually create cohorts.

---

## HUMAN-FR-002 — Manual Cohort Editing

Users SHALL be able to modify cohort definitions subject to permissions.

---

## HUMAN-FR-003 — Cohort Approval

Production cohorts SHALL support:

```text
Draft
Review
Approved
Published
Active
Deprecated
Archived
```

---

## HUMAN-FR-004 — Manual Cohort Investigation

Analysts SHALL be able to investigate individual cohort differences.

---

## HUMAN-FR-005 — Manual Cohort Annotation

Users SHALL be able to annotate important cohort events.

Examples:

```text
Pricing changed
Campaign launched
Product released
AI model changed
Major incident occurred
Onboarding redesigned
```

---

## 31. AI + Human Collaboration

## HYBRID-FR-001 — AI Cohort Proposal

```text
AI detects pattern
       ↓
AI proposes cohort
       ↓
Analyst reviews
       ↓
Business owner validates
       ↓
Cohort published
```

---

## HYBRID-FR-002 — Human Override

Humans SHALL be able to:

* Reject AI cohorts
* Modify AI cohorts
* Approve AI cohorts
* Disable AI monitoring
* Override AI recommendations

---

## HYBRID-FR-003 — Feedback Loop

Human decisions SHALL be recorded for evaluating AI cohort recommendations.

---

## 32. Cohort Experimentation

The system SHALL support cohort-based experiments.

```text
Cohort
   ↓
Control
   ↓
Treatment
   ↓
Outcome
```

The platform SHALL measure:

```text
Conversion
Retention
Revenue
Engagement
Churn
Feature adoption
```

---

## 33. Statistical Requirements

The system SHALL support appropriate statistical analysis including:

```text
Sample size
Mean
Median
Variance
Percentiles
Confidence intervals
Effect size
Conversion difference
Retention difference
```

Where experimentation is involved, the system SHOULD support appropriate statistical significance testing.

---

## 34. Statistical Guardrails

The system SHALL warn users when:

* Sample size is too small.
* Results are statistically unstable.
* Cohorts overlap unexpectedly.
* Selection bias may exist.
* Survivorship bias may exist.
* Multiple comparisons may inflate false positives.

---

## 35. Cohort Overlap

The system SHALL identify whether entities belong to multiple cohorts.

Overlap SHALL be configurable as:

```text
Allowed
Disallowed
Exclusive
```

---

## 36. Cohort Exclusivity

Users SHALL be able to create mutually exclusive cohorts.

Example:

```text
Control
Treatment A
Treatment B
```

---

## 37. Cohort Membership History

The system SHALL preserve membership history where required.

Example:

```text
Customer entered cohort
2026-08-01

Customer exited cohort
2026-08-20

Reason:
Subscription downgrade
```

---

## 38. Cohort Data Quality

The platform SHALL detect:

```text
Missing events
Duplicate events
Incorrect timestamps
Identity collisions
Unexpected membership changes
Invalid cohort definitions
Data gaps
```

---

## 39. Privacy Requirements

Cohort analysis SHALL enforce:

* Tenant isolation
* RBAC
* ABAC where required
* Data minimization
* Consent requirements
* PII restrictions
* Data retention
* Data deletion

---

## 40. Small Cohort Protection

The platform SHOULD prevent or restrict reporting of sufficiently small cohorts when disclosure risk exists.

The threshold SHALL be configurable according to organizational privacy requirements.

---

## 41. AI Privacy

AI SHALL only access cohort data authorized for the requesting user and tenant.

---

## 42. Natural-Language Query Security

The query pipeline SHALL be:

```text
User Question
      ↓
AI Parser
      ↓
Structured Query
      ↓
Authorization
      ↓
Privacy Check
      ↓
Query Validation
      ↓
Cohort Engine
      ↓
Result
      ↓
AI Explanation
```

AI SHALL NOT bypass access controls.

---

## 43. Cohort APIs

## Cohort Management

```http
POST   /api/v1/analytics/cohorts
GET    /api/v1/analytics/cohorts
GET    /api/v1/analytics/cohorts/{cohort_id}
PATCH  /api/v1/analytics/cohorts/{cohort_id}
DELETE /api/v1/analytics/cohorts/{cohort_id}
```

## Cohort Analysis

```http
GET /api/v1/analytics/cohorts/{cohort_id}/members
GET /api/v1/analytics/cohorts/{cohort_id}/retention
GET /api/v1/analytics/cohorts/{cohort_id}/conversion
GET /api/v1/analytics/cohorts/{cohort_id}/revenue
GET /api/v1/analytics/cohorts/{cohort_id}/engagement
GET /api/v1/analytics/cohorts/{cohort_id}/churn
GET /api/v1/analytics/cohorts/{cohort_id}/adoption
```

## Comparison

```http
GET /api/v1/analytics/cohorts/compare
```

## AI

```http
POST /api/v1/analytics/cohorts/ai/discover
POST /api/v1/analytics/cohorts/ai/analyze
POST /api/v1/analytics/cohorts/ai/explain
POST /api/v1/analytics/cohorts/ai/forecast
POST /api/v1/analytics/cohorts/ai/recommend
```

---

## 44. Cohort Data Model

```json
{
  "cohort_id": "uuid",
  "tenant_id": "uuid",
  "organization_id": "uuid",
  "name": "August 2026 Enterprise Customers",
  "type": "acquisition",
  "version": "1.0",
  "status": "active",
  "entity_type": "customer",
  "membership_rule": {
    "event": "subscription.created",
    "date_range": {
      "start": "2026-08-01",
      "end": "2026-08-31"
    },
    "plan": "enterprise"
  },
  "metrics": [
    "retention",
    "conversion",
    "revenue",
    "engagement",
    "churn"
  ]
}
```

---

## 45. Cohort Metrics

The platform SHALL support:

```text
Cohort Size
Activation Rate
Engagement Rate
Retention Rate
Conversion Rate
Churn Rate
Expansion Rate
Upgrade Rate
Downgrade Rate
Revenue
ARPU
ARPA
LTV
CAC
CAC Payback
Gross Revenue Retention
Net Revenue Retention
Feature Adoption
AI Adoption
Support Resolution Rate
```

---

## 46. AI Cohort Metrics

The platform SHOULD support:

```text
Predicted Retention
Predicted Churn
Predicted Conversion
Predicted LTV
Predicted Expansion
Predicted Revenue
Cohort Health Score
Anomaly Score
AI Recommendation Impact
```

---

## 47. Cohort Heatmaps

The platform SHALL support visual matrices for:

```text
Retention
Revenue
Conversion
Engagement
Feature Adoption
```

---

## 48. Cohort Lifecycle

```text
Draft
  ↓
Review
  ↓
Approved
  ↓
Active
  ↓
Monitoring
  ↓
Deprecated
  ↓
Archived
```

---

## 49. Cohort Monitoring

The system SHALL continuously monitor:

```text
Cohort size
Retention
Conversion
Revenue
Churn
Engagement
Feature adoption
AI usage
Anomalies
```

---

## 50. Cohort Alerts

Alerts SHALL support:

```text
Retention ↓
Conversion ↓
Churn ↑
Revenue ↓
Engagement ↓
Feature adoption ↓
Anomaly score ↑
```

---

## 51. Alert Destinations

Alerts MAY be delivered through:

```text
Dashboard
Email
Slack
Microsoft Teams
Webhook
In-App Notification
```

---

## 52. Cohort Forecasting

The platform SHALL forecast:

```text
Future retention
Future conversions
Future churn
Future revenue
Future upgrades
Future expansion
```

Forecasts SHOULD provide uncertainty ranges where applicable.

---

## 53. Scenario Analysis

Users SHALL be able to ask:

```text
"What happens to the August cohort
if onboarding completion increases by 15%?"
```

AI SHALL distinguish:

```text
Observed Data
Forecast
Simulation
Hypothesis
```

---

## 54. Cohort Optimization

The system SHALL support an optimization loop:

```text
Measure
   ↓
Compare
   ↓
Detect Difference
   ↓
Diagnose
   ↓
Generate Hypothesis
   ↓
Design Experiment
   ↓
Human Approval
   ↓
Execute
   ↓
Measure
   ↓
Update Cohort Intelligence
```

---

## 55. AI Recommendation Safety

AI SHALL NOT autonomously perform high-impact customer or business actions unless explicitly authorized.

Potentially high-impact actions include:

* Pricing changes
* Customer communication changes
* Subscription changes
* Mass campaign changes
* Automated customer targeting
* Workflow changes

---

## 56. Cohort Cost Analytics

Where cost data is available, the platform SHALL calculate:

```text
Acquisition Cost
AI Cost
Human Support Cost
Messaging Cost
Infrastructure Cost
Integration Cost
Total Cohort Cost
```

---

## 57. Cohort Profitability

The system SHOULD calculate:

```text
Cohort Profit =
Cohort Revenue
-
Cohort Attributable Costs
```

---

## 58. AI-vs-Human Cohort Economics

The system SHOULD compare:

```text
AI-only cohort cost
Human-only cohort cost
AI-assisted cohort cost
```

against:

```text
Conversion
Revenue
Retention
Resolution
Customer Satisfaction
```

---

## 59. Cohort Attribution

The system SHALL support attribution by:

```text
Campaign
Channel
Lead Source
Sales Agent
AI Agent
Product
Feature
Experiment
```

---

## 60. Cohort Lineage

Every cohort result SHALL be traceable to:

```text
Source Events
Source Attributes
Identity Resolution
Cohort Definition
Cohort Version
Metric Definition
Data Transformation
AI Model
```

---

## 61. Audit Logging

The platform SHALL audit:

* Cohort creation
* Cohort modification
* Cohort deletion
* Cohort publication
* Cohort version changes
* Membership-rule changes
* AI-generated cohorts
* AI recommendations
* Human approvals
* Cohort exports
* Recomputations
* Backfills

---

## 62. Observability

The Cohort Analysis Engine SHALL expose:

```text
cohort_membership_evaluations_total
cohort_membership_changes_total
cohort_queries_total
cohort_query_errors_total
cohort_recomputations_total
cohort_ai_analysis_total
cohort_ai_prediction_total
cohort_processing_latency
cohort_query_latency
cohort_data_quality_errors
```

---

## 63. Reliability

The system SHALL support:

* Horizontal scaling
* Retry
* Idempotency
* Checkpointing
* Backpressure
* Dead-letter processing
* Event replay
* Failure isolation
* Graceful degradation

---

## 64. Disaster Recovery

The cohort system SHALL support:

```text
Backup
Restore
Point-in-time recovery
Recomputation
Event replay
Definition recovery
Historical reproducibility
```

---

## 65. Performance Requirements

The system SHALL support:

```text
10M+ users
500K+ concurrent conversations
Millions of events per minute
Millions of cohort members
Thousands of active cohorts
Large-scale cohort comparisons
High-cardinality segmentation
Historical cohort computation
```

---

## 66. Reference Architecture

```text
                       ANALYTICS EVENTS
                              │
                              ▼
                    Identity Resolution
                              │
                              ▼
                    Customer Data Platform
                              │
                              ▼
                    ┌───────────────────┐
                    │ Cohort Definition │
                    │      Engine       │
                    └─────────┬─────────┘
                              │
                              ▼
                    Membership Evaluation
                              │
                    ┌─────────┴─────────┐
                    │                   │
                    ▼                   ▼
              Static Cohorts       Dynamic Cohorts
                    │                   │
                    └─────────┬─────────┘
                              ▼
                       Cohort State
                              │
              ┌───────────────┼───────────────┐
              │               │               │
              ▼               ▼               ▼
          Retention       Conversion       Revenue
              │               │               │
              └───────────────┼───────────────┘
                              ▼
                       Cohort Analytics
                              │
              ┌───────────────┼────────────────┐
              │               │                │
              ▼               ▼                ▼
             BI          Real-Time             AI
                        Monitoring         Intelligence
                                              │
                         ┌────────────────────┼──────────────────┐
                         │                    │                  │
                         ▼                    ▼                  ▼
                    Discovery            Forecasting       Optimization
                         │                    │                  │
                         └────────────────────┼──────────────────┘
                                              ▼
                                       Human Approval
                                              │
                                              ▼
                                         Experiment
                                              │
                                              ▼
                                        New Events
```

---

## 67. End-to-End AI Cohort Intelligence

```text
Customer Events
       ↓
Identity Resolution
       ↓
Behavioral Analysis
       ↓
Cohort Discovery
       ↓
Cohort Definition
       ↓
Human Validation
       ↓
Cohort Activation
       ↓
Retention / Conversion / Revenue Analysis
       ↓
AI Pattern Detection
       ↓
AI Root-Cause Analysis
       ↓
AI Forecasting
       ↓
AI Recommendation
       ↓
Human Approval
       ↓
Experiment
       ↓
Outcome Measurement
       ↓
Continuous Learning
```

---

## 68. Definition of Done

The Cohort Analysis subsystem SHALL NOT be considered production-ready until:

* Cohort creation works.
* Cohort definitions are versioned.
* Static cohorts work.
* Dynamic cohorts work.
* Cohort membership is deterministic where applicable.
* Cohort snapshots work.
* Cohort re-entry works.
* Identity resolution works.
* Retention analysis works.
* Conversion analysis works.
* Revenue analysis works.
* Churn analysis works.
* Engagement analysis works.
* Feature adoption analysis works.
* Funnel integration works.
* Cohort comparison works.
* Cohort heatmaps work.
* Cohort segmentation works.
* Attribution works.
* Cohort forecasting works.
* AI cohort discovery works.
* AI cohort analysis works.
* AI anomaly detection works.
* AI explanations provide evidence.
* AI recommendations work.
* Human approval workflows work.
* AI-vs-human cohort analysis works.
* Experimentation support works.
* Statistical guardrails work.
* Privacy protections work.
* Small-cohort disclosure protection works.
* Tenant isolation is verified.
* Cohort APIs are secured.
* Audit logging works.
* Data lineage works.
* Data quality monitoring works.
* Real-time monitoring works.
* Historical recomputation works.
* Disaster recovery is validated.
* Load testing passes.
* Security testing passes.
* Privacy testing passes.

---

## 69. FAANG-Level Engineering Principles

1. Cohort definitions are versioned analytical contracts.
2. Cohort membership must be reproducible.
3. Raw events remain immutable wherever possible.
4. Historical cohort results must remain reproducible.
5. Deterministic cohort rules take precedence over probabilistic AI.
6. AI-generated cohorts must be explicitly labeled.
7. AI predictions must be distinguished from observed behavior.
8. Cohort membership must be traceable to source evidence.
9. Identity resolution must be deterministic and auditable.
10. Cohort calculations must be idempotent.
11. Dynamic cohorts must support incremental computation.
12. Static cohorts must support immutable snapshots.
13. Late-arriving events must be reconciled.
14. Cohort overlap must be explicitly defined.
15. Statistical uncertainty must be represented.
16. Correlation must not automatically be presented as causation.
17. Small cohorts must be protected against privacy leakage.
18. Tenant boundaries must be enforced at every layer.
19. AI queries must never bypass authorization.
20. High-impact AI recommendations require appropriate human governance.
21. Cohort analytics must support both real-time and historical workloads.
22. Cohort computation must scale horizontally.
23. Consumer failures must not corrupt cohort state.
24. Every AI recommendation must be measurable through subsequent events.
25. All administrative operations must be auditable.
26. Privacy must be enforced throughout the cohort lifecycle.
27. Data quality must be continuously monitored.
28. Cohort definitions must have clear ownership.
29. Experiment analysis must account for statistical validity.
30. Cohort intelligence must operate as a closed measurement-and-learning loop.

---

## 70. Final Requirement

SalesGenie's Cohort Analysis subsystem SHALL provide an enterprise-scale, AI-native analytical foundation capable of transforming raw customer, user, lead, sales, support, AI, product, subscription, workflow, and revenue events into meaningful longitudinal cohorts.

The complete intelligence loop SHALL be:

```text
Human Activity
+
AI Activity
+
Customer Activity
+
Product Activity
+
Business Activity
+
System Events
        ↓
Analytics Events
        ↓
Identity Resolution
        ↓
Cohort Construction
        ↓
Cohort Membership
        ↓
Retention Analysis
        ↓
Conversion Analysis
        ↓
Engagement Analysis
        ↓
Revenue Analysis
        ↓
Churn Analysis
        ↓
Feature Adoption
        ↓
Funnel Analysis
        ↓
Attribution
        ↓
AI Pattern Discovery
        ↓
AI Root-Cause Analysis
        ↓
AI Forecasting
        ↓
AI Recommendation
        ↓
Human Validation
        ↓
Experimentation
        ↓
Business / Product Action
        ↓
Outcome Measurement
        ↓
New Analytics Events
        ↓
Continuous Cohort Intelligence
```

The resulting system SHALL enable SalesGenie to understand **who its customers are, when they entered the platform, how their behavior evolves, which cohorts convert and retain, which cohorts generate revenue, which cohorts churn, how AI and human interactions affect outcomes, which product behaviors correlate with long-term success, and which validated interventions can improve customer and business outcomes over time.**
