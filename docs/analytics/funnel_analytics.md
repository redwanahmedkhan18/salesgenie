# SalesGenie — Funnel Analytics Requirements

**Document:** `funnel_analytics.md`  
**Project:** SalesGenie / FlowMind AI  
**Requirement Type:** User Requirements + System Requirements + Functional Requirements  
**Architecture:** Enterprise SaaS + Microservices + Event-Driven + Multi-Agent AI  
**Execution Modes:** AI-driven + Human-driven + Human-in-the-Loop  
**Target Scale:** 10M+ users, 500K+ concurrent conversations  
**Priority:** Enterprise / Production / FAANG-Level

---

## 1. Purpose

The Funnel Analytics subsystem SHALL provide an enterprise-grade framework for defining, tracking, analyzing, optimizing, forecasting, and continuously improving business and customer funnels across SalesGenie.

The subsystem SHALL transform raw analytics events into actionable funnel intelligence across:

- Marketing funnels
- Lead-generation funnels
- Sales funnels
- Customer-support funnels
- Product-adoption funnels
- AI-agent funnels
- Conversation funnels
- Conversion funnels
- Subscription funnels
- Revenue funnels
- Customer lifecycle funnels
- Workflow funnels
- Campaign funnels
- Onboarding funnels
- Retention funnels
- Expansion funnels

The system SHALL support both:

```text
Human-driven analysis
AI-driven analysis
AI-assisted human analysis
Automated funnel optimization
Human-approved AI actions
```

---

## 2. Scope

## 2.1 In Scope

The Funnel Analytics subsystem SHALL support:

1. Funnel definition
2. Funnel templates
3. Funnel stages
4. Event-to-stage mapping
5. Funnel entry criteria
6. Funnel exit criteria
7. Stage progression
8. Stage abandonment
9. Conversion measurement
10. Drop-off analysis
11. Time-to-convert analysis
12. Funnel segmentation
13. Cohort analysis
14. Attribution
15. Multi-touch attribution
16. Cross-channel funnel analysis
17. AI funnel analysis
18. Funnel forecasting
19. Funnel anomaly detection
20. Funnel optimization
21. Funnel recommendations
22. Funnel experimentation
23. Funnel comparison
24. Funnel benchmarking
25. Real-time funnel monitoring
26. Historical funnel analysis
27. Revenue funnel analytics
28. AI-human funnel analytics
29. Funnel alerts
30. Funnel governance
31. Funnel data quality
32. Funnel privacy
33. Funnel RBAC
34. Funnel auditability
35. Funnel reporting
36. Funnel dashboards
37. Natural-language funnel querying

---

## 3. Actors

## 3.1 Human Actors

* End User
* Customer
* Lead
* Sales Agent
* Support Agent
* Sales Manager
* Support Manager
* Marketing Manager
* Customer Success Manager
* Organization Admin
* Tenant Admin
* Super Admin
* Data Analyst
* Business Analyst
* Data Scientist
* Data Engineer
* ML Engineer
* AI Engineer
* Product Manager
* Revenue Operations Manager
* Executive
* Compliance Officer
* Auditor

## 3.2 AI Actors

* AI Sales Agent
* AI Support Agent
* AI Analytics Agent
* AI Funnel Analyst
* AI Recommendation Agent
* AI Forecasting Agent
* AI Attribution Agent
* AI Optimization Agent
* AI Anomaly Detection Agent
* AI Customer Intelligence Agent
* AI Workflow Agent
* AI Orchestrator

## 3.3 System Actors

* Analytics Events Service
* Event Bus
* Analytics Platform
* Metrics Engine
* KPI Engine
* Business Intelligence Service
* Customer Data Platform
* Data Warehouse
* Data Lake
* Workflow Engine
* AI Gateway
* RAG Service
* CRM Integrations
* Billing Service
* Subscription Service
* Marketing Integrations

---

## 4. Core Funnel Model

A funnel SHALL be represented as:

```text
Funnel
 ├── Funnel Identity
 ├── Definition
 ├── Version
 ├── Owner
 ├── Entry Criteria
 ├── Stages
 │    ├── Stage 1
 │    ├── Stage 2
 │    ├── Stage 3
 │    └── Stage N
 ├── Conversion Rules
 ├── Attribution Rules
 ├── Segmentation Rules
 ├── Time Windows
 ├── Goal
 └── Governance
```

---

## 5. Standard Funnel Example

```text
Lead Generated
      ↓
Lead Enriched
      ↓
Lead Qualified
      ↓
Lead Contacted
      ↓
Lead Responded
      ↓
Meeting Booked
      ↓
Opportunity Created
      ↓
Proposal Sent
      ↓
Deal Won
      ↓
Subscription Activated
      ↓
Expansion
```

---

## 6. User Requirements

## UR-001 — Funnel Visibility

Authorized users SHALL be able to view funnel performance across their permitted tenants, organizations, workspaces, teams, campaigns, channels, and customer segments.

---

## UR-002 — Funnel Creation

Authorized users SHALL be able to create custom funnels.

Users SHALL be able to define:

* Funnel name
* Description
* Objective
* Stages
* Events
* Conversion criteria
* Time window
* Attribution model
* Segments
* Owner
* Visibility

---

## UR-003 — Funnel Templates

The system SHALL provide reusable funnel templates.

Examples:

```text
Lead Conversion Funnel
Sales Pipeline Funnel
Customer Onboarding Funnel
AI Support Resolution Funnel
Subscription Conversion Funnel
Product Adoption Funnel
Marketing Campaign Funnel
```

---

## UR-004 — Funnel Stage Visibility

Users SHALL be able to see:

* Users entering each stage
* Users completing each stage
* Users dropping out
* Conversion rate
* Drop-off rate
* Median stage duration
* Average stage duration
* Revenue associated with the stage

---

## UR-005 — Funnel Comparison

Users SHALL be able to compare funnels by:

```text
Time
Campaign
Channel
Region
Team
Agent
AI Agent
Product
Plan
Customer segment
Lead source
Experiment
```

---

## UR-006 — Funnel Drill-Down

Users SHALL be able to drill down from:

```text
Funnel
 ↓
Stage
 ↓
Segment
 ↓
Customer
 ↓
Conversation
 ↓
Event
```

subject to access-control policies.

---

## UR-007 — Drop-Off Identification

Users SHALL be able to identify the largest funnel drop-offs.

Example:

```text
Qualified Lead → Contacted
Conversion: 83%

Contacted → Responded
Conversion: 42%

Largest bottleneck:
Contacted → Responded
```

---

## UR-008 — Funnel Trends

Users SHALL be able to analyze funnel performance over:

* Hour
* Day
* Week
* Month
* Quarter
* Custom date range

---

## UR-009 — Funnel Segmentation

Users SHALL be able to segment funnels by:

* Customer type
* Industry
* Region
* Company size
* Lead source
* Campaign
* Channel
* Subscription tier
* AI agent
* Human agent
* Product
* Device
* Experiment variant

---

## UR-010 — Customer Journey

Users SHALL be able to inspect individual customer journeys through a funnel.

---

## UR-011 — Funnel Alerts

Authorized users SHALL be able to configure alerts for:

* Conversion drops
* Abnormal abandonment
* Stage latency increases
* Revenue leakage
* Traffic spikes
* Funnel failures

---

## UR-012 — Funnel Forecast

Users SHALL be able to view predicted future funnel outcomes.

---

## UR-013 — Funnel Recommendations

Users SHALL receive AI-generated recommendations for improving funnel performance.

---

## UR-014 — Natural-Language Queries

Users SHALL be able to ask questions such as:

```text
"Why did our enterprise conversion rate fall this month?"

"Which channel generates the highest-quality leads?"

"Where are customers dropping out?"

"Which AI agent produces the highest conversion?"

"How many qualified leads are likely to become customers?"
```

---

## 7. System Requirements

## SR-001 — Centralized Funnel Engine

SalesGenie SHALL provide a centralized Funnel Analytics Engine.

```text
Analytics Events
       ↓
Event Processing
       ↓
Identity Resolution
       ↓
Funnel Engine
       ↓
Stage Evaluation
       ↓
Conversion Calculation
       ↓
Segmentation
       ↓
Attribution
       ↓
Metrics / KPIs
       ↓
AI Analysis
```

---

## SR-002 — Event-Driven Funnel Processing

The Funnel Analytics Engine SHALL consume events from the Analytics Events infrastructure.

---

## SR-003 — Funnel Definition Registry

The platform SHALL maintain a registry containing:

```text
Funnel ID
Funnel Name
Version
Owner
Stages
Stage Conditions
Entry Criteria
Exit Criteria
Conversion Window
Attribution Model
Segments
Status
Created At
Updated At
```

---

## SR-004 — Funnel Versioning

Funnel definitions SHALL be versioned.

```text
sales_funnel_v1
sales_funnel_v2
sales_funnel_v3
```

Historical analytics SHALL remain reproducible against the funnel definition that was active at the time.

---

## SR-005 — Deterministic Stage Evaluation

Stage progression SHALL be deterministic wherever business rules are deterministic.

AI SHALL NOT silently alter deterministic funnel rules.

---

## SR-006 — Identity Resolution

The system SHALL support identity resolution across:

```text
Anonymous visitor
User
Customer
Lead
Account
Contact
Conversation
Device
Session
CRM record
```

---

## SR-007 — Cross-Channel Identity

The platform SHALL correlate customer activity across:

```text
Web
Email
WhatsApp
SMS
CRM
Social
Voice
Support
Mobile
API
```

where legally and technically permitted.

---

## SR-008 — Funnel State

The system SHALL maintain funnel state for each eligible entity.

Example:

```json
{
  "entity_id": "customer_123",
  "funnel_id": "sales_funnel",
  "current_stage": "qualified",
  "previous_stage": "enriched",
  "entered_at": "2026-08-29T10:00:00Z",
  "stage_duration_seconds": 86400
}
```

---

## SR-009 — Stage Ordering

Funnels SHALL support:

* Strict sequential progression
* Non-linear progression
* Optional stages
* Re-entry
* Backward movement
* Parallel stages

---

## SR-010 — Funnel Time Windows

Funnels SHALL support:

```text
Session-based
24 hours
7 days
30 days
90 days
Custom duration
Unlimited
```

---

## SR-011 — Conversion Window

Each funnel SHALL support configurable conversion windows.

---

## SR-012 — Drop-Off Definition

The system SHALL distinguish:

```text
Natural abandonment
Timeout
Explicit rejection
Disqualification
Technical failure
Human rejection
AI rejection
Customer churn
```

---

## SR-013 — Funnel Re-Entry

The system SHALL support customers re-entering a funnel.

The system SHALL maintain separate funnel instances where required.

---

## SR-014 — Funnel Attribution

The platform SHALL support configurable attribution models.

Minimum models:

```text
First Touch
Last Touch
Linear
Time Decay
Position Based
Custom
```

---

## SR-015 — Multi-Touch Attribution

The system SHALL attribute conversion outcomes across multiple customer interactions.

---

## SR-016 — Funnel Segmentation Engine

The system SHALL support dynamic segmentation without duplicating raw event data.

---

## SR-017 — Real-Time Processing

Real-time funnel metrics SHOULD target:

```text
P50 < 2 seconds
P95 < 5 seconds
P99 < 15 seconds
```

from relevant event ingestion.

---

## SR-018 — Historical Processing

The system SHALL support large-scale historical funnel computation.

---

## SR-019 — Backfill

Authorized data engineers SHALL be able to recompute funnel results after:

* Event corrections
* Schema changes
* Funnel-definition changes
* Attribution changes
* Data-quality fixes

---

## SR-020 — Reproducibility

Historical funnel calculations SHALL be reproducible using:

```text
Event version
Funnel version
Metric version
Attribution version
Model version
```

---

## 8. Functional Requirements

## FR-001 — Create Funnel

The system SHALL allow authorized users to create funnels.

---

## FR-002 — Configure Funnel Stages

Users SHALL be able to define stage conditions using analytics events.

Example:

```text
Stage:
Lead Qualified

Condition:
lead.qualified = true
```

---

## FR-003 — Event Mapping

The system SHALL map analytics events to funnel stages.

---

## FR-004 — Stage Entry

The system SHALL record:

```text
Entity ID
Funnel ID
Stage ID
Entry timestamp
Source event
```

---

## FR-005 — Stage Completion

The system SHALL record stage completion and transition timestamps.

---

## FR-006 — Stage Abandonment

The system SHALL identify entities that fail to progress within the configured time window.

---

## FR-007 — Conversion Rate

The system SHALL calculate:

```text
Conversion Rate =
Entities Completing Stage
/
Entities Entering Stage
× 100
```

---

## FR-008 — Overall Funnel Conversion

The system SHALL calculate:

```text
Overall Conversion =
Entities Completing Final Goal
/
Entities Entering Funnel
× 100
```

---

## FR-009 — Drop-Off Rate

The system SHALL calculate:

```text
Drop-Off Rate =
1 - Stage Conversion Rate
```

---

## FR-010 — Stage Duration

The system SHALL calculate:

```text
Average Duration
Median Duration
P90 Duration
P95 Duration
P99 Duration
```

---

## FR-011 — Funnel Velocity

The system SHALL calculate how quickly entities move through funnels.

---

## FR-012 — Funnel Throughput

The system SHALL calculate:

```text
Entities entering funnel / time
Entities completing funnel / time
```

---

## FR-013 — Funnel Leakage

The system SHALL identify business leakage between stages.

Example:

```text
1000 qualified leads
↓
650 contacted
↓
300 responded
↓
100 meetings
↓
20 deals
```

The system SHALL identify significant losses at every transition.

---

## FR-014 — Funnel Comparison

Users SHALL be able to compare multiple funnel versions or segments.

---

## FR-015 — Funnel Benchmarking

The system SHALL support internal benchmarks.

Examples:

```text
Current conversion
Historical median
Best historical conversion
Team benchmark
Organization benchmark
```

External benchmarks SHALL only be used when valid, authorized data is available.

---

## 9. AI Requirements

## AI-FR-001 — AI Funnel Discovery

AI SHALL analyze event streams and recommend potential funnels.

Example:

```text
AI detects:

lead.created
→ lead.qualified
→ message.sent
→ meeting.booked
→ deal.won

Recommendation:
Create "Lead-to-Revenue Funnel".
```

---

## AI-FR-002 — AI Stage Discovery

AI MAY identify meaningful behavioral stages from event sequences.

---

## AI-FR-003 — AI Bottleneck Detection

AI SHALL identify likely funnel bottlenecks.

Example:

```text
Biggest bottleneck:
Demo Scheduled → Proposal Sent

Conversion declined 21% week-over-week.
```

---

## AI-FR-004 — AI Root-Cause Analysis

AI SHALL investigate why a funnel changed.

It SHOULD analyze:

```text
Customer segments
Channels
Agents
AI models
Campaigns
Pricing
Product changes
Support activity
System incidents
```

---

## AI-FR-005 — AI Funnel Explanation

AI SHALL produce evidence-backed explanations.

Each major AI conclusion SHOULD include:

```text
Observation
Evidence
Time period
Affected segment
Confidence
Potential cause
```

---

## AI-FR-006 — AI Funnel Forecasting

AI SHALL forecast:

```text
Future stage volume
Expected conversions
Expected revenue
Expected drop-offs
Expected pipeline
```

---

## AI-FR-007 — AI Conversion Prediction

For authorized use cases, AI SHALL estimate the probability that an entity will progress to the next funnel stage.

Example:

```json
{
  "lead_id": "lead_123",
  "next_stage": "meeting_booked",
  "probability": 0.78
}
```

Predictions SHALL be clearly distinguished from observed funnel outcomes.

---

## AI-FR-008 — AI Churn Funnel

AI SHALL identify customers moving toward churn.

```text
Reduced engagement
 ↓
Support complaints
 ↓
Feature abandonment
 ↓
Usage decline
 ↓
Cancellation intent
 ↓
Churn
```

---

## AI-FR-009 — AI Purchase Funnel

AI SHALL identify purchase-intent progression.

```text
Product viewed
 ↓
Pricing viewed
 ↓
Enterprise feature viewed
 ↓
Sales contacted
 ↓
Demo requested
 ↓
Proposal requested
 ↓
Purchase
```

---

## AI-FR-010 — AI Support Funnel

AI SHALL analyze:

```text
Issue detected
 ↓
Conversation started
 ↓
AI response
 ↓
AI resolution
 ↓
Human escalation
 ↓
Human resolution
 ↓
Customer satisfaction
```

---

## AI-FR-011 — AI Agent Funnel

The platform SHALL analyze AI-agent effectiveness.

Metrics SHALL include:

```text
AI interaction → successful resolution
AI interaction → escalation
AI interaction → conversion
AI interaction → abandonment
AI interaction → human handoff
```

---

## AI-FR-012 — AI vs Human Funnel

The system SHALL support comparison between:

```text
AI-only
Human-only
AI-assisted human
Human-assisted AI
```

---

## AI-FR-013 — AI Funnel Optimization

AI SHALL recommend potential interventions.

Examples:

```text
Increase follow-up speed
Change message timing
Improve RAG coverage
Escalate high-intent leads earlier
Change onboarding sequence
Improve pricing-page CTA
```

Recommendations SHALL require appropriate human approval before high-impact automated execution.

---

## AI-FR-014 — AI Experiment Recommendation

AI MAY recommend experiments to improve funnel conversion.

Example:

```text
Hypothesis:
Shortening lead-response time from 30 minutes
to <5 minutes may improve conversion.

Recommended experiment:
Control: current workflow
Variant: immediate AI-assisted response
```

---

## AI-FR-015 — AI Anomaly Detection

AI SHALL detect unusual funnel changes.

Examples:

```text
Conversion suddenly drops
Stage volume suddenly spikes
A channel stops converting
AI agent conversion collapses
Enterprise funnel stalls
```

---

## AI-FR-016 — AI Segmentation Discovery

AI SHALL identify high-performing and low-performing segments.

---

## AI-FR-017 — AI Natural-Language Analytics

Users SHALL be able to ask:

```text
"Show me the biggest sales funnel bottleneck."

"Why are enterprise leads converting less?"

"Which AI agent has the best conversion rate?"

"Predict how many deals we will close this month."
```

---

## 10. Human-Based Requirements

## HUMAN-FR-001 — Manual Funnel Definition

Authorized users SHALL be able to define funnels manually.

---

## HUMAN-FR-002 — Manual Stage Configuration

Users SHALL be able to modify:

* Stage names
* Conditions
* Ordering
* Time windows
* Conversion rules

---

## HUMAN-FR-003 — Funnel Approval

Production funnels SHALL support an approval workflow.

```text
Draft
 ↓
Review
 ↓
Approved
 ↓
Published
 ↓
Active
```

---

## HUMAN-FR-004 — Manual Funnel Investigation

Analysts SHALL be able to investigate funnel anomalies manually.

---

## HUMAN-FR-005 — Manual Annotation

Users SHALL be able to annotate funnel timelines.

Examples:

```text
Pricing changed
Campaign launched
AI model upgraded
Product released
Incident occurred
Sales process changed
```

---

## HUMAN-FR-006 — Manual Override

Authorized users SHALL be able to override AI recommendations.

---

## 11. AI + Human Collaboration

## HYBRID-FR-001 — AI Funnel Proposal

AI SHALL be able to propose a funnel.

```text
AI discovers behavioral pattern
        ↓
AI proposes funnel
        ↓
Analyst reviews
        ↓
Business owner approves
        ↓
Engineer validates
        ↓
Funnel published
```

---

## HYBRID-FR-002 — Human Approval

AI SHALL NOT automatically publish high-impact production funnels without configured approval.

---

## HYBRID-FR-003 — Recommendation Approval

AI recommendations SHALL support:

```text
Approve
Reject
Modify
Defer
Test
```

---

## HYBRID-FR-004 — Human Feedback

Human decisions SHALL be recorded as feedback for evaluating recommendation quality.

---

## 12. Marketing Funnel

The system SHALL support:

```text
Impression
 ↓
Visit
 ↓
Signup
 ↓
Activation
 ↓
Lead
 ↓
Qualified Lead
 ↓
Customer
```

Metrics:

* CTR
* Signup Rate
* Activation Rate
* Lead Rate
* Qualification Rate
* Customer Conversion

---

## 13. Sales Funnel

The system SHALL support:

```text
Lead
 ↓
MQL
 ↓
SQL
 ↓
Contacted
 ↓
Meeting
 ↓
Opportunity
 ↓
Proposal
 ↓
Negotiation
 ↓
Won
```

---

## 14. Customer Onboarding Funnel

The system SHALL support:

```text
Signup
 ↓
Email Verification
 ↓
Workspace Created
 ↓
Integration Connected
 ↓
First AI Interaction
 ↓
First Workflow
 ↓
First Lead
 ↓
Activation
```

---

## 15. Subscription Funnel

The system SHALL support:

```text
Pricing Viewed
 ↓
Trial Started
 ↓
Trial Activated
 ↓
Payment Added
 ↓
Subscription Started
 ↓
Upgrade
 ↓
Renewal
```

---

## 16. Revenue Funnel

The system SHALL support:

```text
Lead
 ↓
Qualified Opportunity
 ↓
Pipeline
 ↓
Proposal
 ↓
Won Deal
 ↓
Subscription
 ↓
Expansion
 ↓
Renewal
```

---

## 17. AI Support Funnel

The system SHALL support:

```text
Customer Issue
 ↓
AI Detection
 ↓
AI Response
 ↓
AI Resolution
 ↓
Customer Confirmation
```

Alternative path:

```text
AI Response
 ↓
Low Confidence
 ↓
Human Escalation
 ↓
Human Resolution
```

---

## 18. Attribution Requirements

The system SHALL support attribution at:

```text
User
Lead
Account
Campaign
Channel
Agent
AI Agent
Conversation
Opportunity
Revenue
```

---

## 19. Multi-Touch Attribution

Example:

```text
Google Search
      ↓
Website Visit
      ↓
Email Campaign
      ↓
Pricing Page
      ↓
Sales Chat
      ↓
Demo
      ↓
Deal
```

The system SHALL preserve all relevant touchpoints.

---

## 20. Cohort Funnel Analysis

The platform SHALL support cohorts based on:

```text
Signup date
First interaction
First purchase
Campaign
Region
Plan
Industry
Acquisition source
AI model
Product version
```

---

## 21. Funnel Experimentation

The system SHALL support:

```text
Control
Variant A
Variant B
Variant C
```

and calculate:

```text
Stage conversion
Overall conversion
Revenue conversion
Time-to-convert
Statistical significance
Confidence intervals
```

where statistically appropriate.

---

## 22. Real-Time Funnel Monitoring

Dashboards SHALL support near-real-time monitoring of:

```text
Active funnel entities
Stage volume
Stage conversion
Drop-offs
Revenue
AI predictions
Anomalies
Alerts
```

---

## 23. Funnel Alerts

Alerts SHALL support thresholds such as:

```text
Conversion < X%
Drop-off > X%
Stage latency > X
Revenue < X
Volume > X
AI confidence < X
```

---

## 24. Alert Channels

Alerts MAY be delivered through:

```text
Dashboard
Email
Slack
Microsoft Teams
Webhook
In-app notification
```

---

## 25. Data Quality

The Funnel Analytics Engine SHALL validate:

```text
Missing events
Duplicate events
Out-of-order events
Invalid timestamps
Invalid identities
Broken event mappings
Schema violations
Unexpected stage transitions
```

---

## 26. Funnel Integrity

The system SHALL detect impossible transitions.

Example:

```text
Deal Won
 ↓
Lead Qualified
```

Such transitions SHALL be flagged as invalid unless explicitly permitted by the funnel definition.

---

## 27. Security Requirements

The system SHALL enforce:

* Authentication
* RBAC
* ABAC where required
* Tenant isolation
* Organization isolation
* Field-level authorization
* Export controls
* Audit logging
* Encryption
* Privacy controls

---

## 28. Privacy Requirements

Funnel analytics SHALL minimize unnecessary personal data.

Users SHALL only see customer-level information permitted by their access policies.

---

## 29. AI Privacy

AI SHALL NOT receive funnel data outside the user's authorized tenant or scope.

---

## 30. AI Query Security

Natural-language queries SHALL be converted into validated structured queries.

Example:

```text
User question
     ↓
AI semantic parser
     ↓
Structured query
     ↓
Authorization check
     ↓
Query validator
     ↓
Analytics engine
     ↓
Result
```

AI SHALL NOT bypass authorization.

---

## 31. API Requirements

## Funnel APIs

```http
POST   /api/v1/analytics/funnels
GET    /api/v1/analytics/funnels
GET    /api/v1/analytics/funnels/{funnel_id}
PATCH  /api/v1/analytics/funnels/{funnel_id}
DELETE /api/v1/analytics/funnels/{funnel_id}
```

## Funnel Analysis

```http
GET /api/v1/analytics/funnels/{funnel_id}/analysis
GET /api/v1/analytics/funnels/{funnel_id}/stages
GET /api/v1/analytics/funnels/{funnel_id}/conversion
GET /api/v1/analytics/funnels/{funnel_id}/dropoffs
GET /api/v1/analytics/funnels/{funnel_id}/segments
GET /api/v1/analytics/funnels/{funnel_id}/cohorts
```

## Funnel Entities

```http
GET /api/v1/analytics/funnels/{funnel_id}/entities
GET /api/v1/analytics/funnels/{funnel_id}/entities/{entity_id}
```

## AI

```http
POST /api/v1/analytics/funnels/ai/discover
POST /api/v1/analytics/funnels/ai/analyze
POST /api/v1/analytics/funnels/ai/forecast
POST /api/v1/analytics/funnels/ai/recommend
POST /api/v1/analytics/funnels/ai/explain
```

---

## 32. Funnel Data Model

```json
{
  "funnel_id": "uuid",
  "tenant_id": "uuid",
  "organization_id": "uuid",
  "name": "Enterprise Sales Funnel",
  "version": "2.0",
  "status": "active",
  "entry_event": "lead.created",
  "conversion_event": "deal.won",
  "conversion_window_days": 90,
  "attribution_model": "multi_touch",
  "stages": [
    {
      "stage_id": "lead_created",
      "order": 1,
      "event": "lead.created"
    },
    {
      "stage_id": "qualified",
      "order": 2,
      "event": "lead.qualified"
    },
    {
      "stage_id": "meeting",
      "order": 3,
      "event": "meeting.booked"
    },
    {
      "stage_id": "opportunity",
      "order": 4,
      "event": "opportunity.created"
    },
    {
      "stage_id": "won",
      "order": 5,
      "event": "deal.won"
    }
  ]
}
```

---

## 33. Funnel Metrics

The system SHALL support:

```text
Funnel Entry Rate
Stage Entry Rate
Stage Conversion Rate
Stage Drop-Off Rate
Overall Conversion Rate
Stage Duration
Time-to-Conversion
Funnel Velocity
Funnel Throughput
Revenue per Funnel Entity
Customer Acquisition Cost
Customer Lifetime Value
Pipeline Value
Expected Revenue
Win Rate
```

---

## 34. AI Funnel Metrics

The system SHOULD support:

```text
Predicted Conversion Probability
Predicted Stage Duration
Predicted Drop-Off Probability
Predicted Revenue
AI Recommendation Impact
AI Agent Conversion Rate
AI-Assisted Conversion Lift
AI-to-Human Handoff Rate
AI Resolution Rate
```

---

## 35. AI-vs-Human Performance

The platform SHALL compare:

```text
AI conversion
Human conversion
AI-assisted human conversion
```

Metrics SHALL include:

```text
Conversion rate
Response time
Resolution rate
Revenue generated
Customer satisfaction
Escalation rate
Cost per conversion
```

---

## 36. Funnel Cost Analytics

The system SHALL calculate funnel economics where cost data is available.

Example:

```text
Acquisition Cost
+
AI Inference Cost
+
Human Labor Cost
+
Messaging Cost
+
Integration Cost
=
Funnel Cost
```

---

## 37. Funnel ROI

The system SHOULD calculate:

```text
ROI =
(Funnel-attributed Revenue - Funnel Cost)
/
Funnel Cost
× 100
```

---

## 38. Funnel Health Score

The platform MAY calculate a composite funnel health score using:

```text
Conversion
Velocity
Drop-off
Volume
Revenue
Quality
Trend
Anomaly
```

AI-generated health scores SHALL expose their methodology or contributing factors.

---

## 39. Funnel Forecasting

Forecasting SHALL support:

```text
Expected funnel entries
Expected stage transitions
Expected conversions
Expected revenue
Prediction intervals
Scenario analysis
```

---

## 40. Scenario Analysis

Users SHALL be able to model scenarios.

Example:

```text
If lead response time decreases by 50%,
what is the expected impact on conversion?
```

AI SHALL clearly label such outputs as forecasts or simulations rather than observed facts.

---

## 41. Funnel Optimization Loop

```text
Observe
   ↓
Measure
   ↓
Detect bottleneck
   ↓
Diagnose
   ↓
Generate recommendation
   ↓
Human approval
   ↓
Experiment
   ↓
Measure impact
   ↓
Learn
   ↓
Optimize
```

---

## 42. AI Optimization Guardrails

AI SHALL NOT autonomously make high-impact business changes without configured authorization.

Examples requiring approval MAY include:

* Pricing changes
* Customer communication changes
* Sales-stage changes
* Automated campaign changes
* Subscription changes
* High-volume workflow changes

---

## 43. Audit Requirements

The system SHALL audit:

* Funnel creation
* Funnel modification
* Funnel deletion
* Funnel publication
* Funnel version changes
* Attribution changes
* AI recommendations
* Human approvals
* AI overrides
* Export operations
* Backfills
* Recomputations

---

## 44. Observability

The Funnel Analytics Engine SHALL expose:

```text
funnel_events_processed_total
funnel_stage_transitions_total
funnel_conversions_total
funnel_dropoffs_total
funnel_processing_errors_total
funnel_recomputations_total
funnel_processing_latency
funnel_query_latency
funnel_prediction_latency
```

---

## 45. Reliability

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

## 46. Scalability

The Funnel Analytics Engine SHALL be designed for:

```text
10M+ users
500K+ concurrent conversations
Millions of events per minute
Large-scale funnels
Thousands of funnel definitions
Millions of active funnel entities
High-cardinality segmentation
Large historical datasets
```

---

## 47. Funnel Architecture

```text
                 ANALYTICS EVENTS
                        │
                        ▼
              ┌───────────────────┐
              │ Identity Resolution│
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │ Funnel Definition │
              │     Registry      │
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │ Stage Evaluation  │
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │ Funnel State Store │
              └─────────┬─────────┘
                        │
             ┌──────────┼───────────┐
             │          │           │
             ▼          ▼           ▼
          Metrics    Attribution   Segments
             │          │           │
             └──────────┼───────────┘
                        ▼
                 Funnel Analytics
                        │
             ┌──────────┼───────────┐
             │          │           │
             ▼          ▼           ▼
           BI         Real-Time      AI
                      Analytics   Intelligence
                                  │
                     ┌────────────┼────────────┐
                     ▼            ▼            ▼
                  Forecast     Diagnosis    Optimization
                     │            │            │
                     └────────────┼────────────┘
                                  ▼
                           Human Decision
                                  │
                                  ▼
                             Experiment
                                  │
                                  ▼
                              New Events
```

---

## 48. Definition of Done

The Funnel Analytics subsystem SHALL NOT be considered production-ready until:

* Funnel definitions are supported.
* Funnel stages are configurable.
* Event-to-stage mapping works.
* Funnel versioning works.
* Identity resolution works.
* Stage transitions are tracked.
* Conversion calculations are correct.
* Drop-off calculations are correct.
* Stage duration calculations are correct.
* Funnel re-entry works.
* Historical recomputation works.
* Attribution models are supported.
* Segmentation works.
* Cohort analysis works.
* Real-time analytics works.
* Historical analytics works.
* Funnel APIs are secured.
* Tenant isolation is verified.
* Privacy controls are verified.
* AI funnel discovery works.
* AI bottleneck detection works.
* AI forecasting works.
* AI recommendations work.
* AI explanations provide evidence.
* Human approval workflows work.
* AI-vs-human analysis works.
* Experimentation support works.
* Funnel anomaly detection works.
* Alerts work.
* Audit logging works.
* Data-quality validation works.
* Observability dashboards exist.
* Load testing passes.
* Security testing passes.
* Privacy testing passes.
* Disaster recovery is validated.
* Historical results are reproducible.

---

## 49. FAANG-Level Engineering Principles

1. Funnel definitions are versioned analytical contracts.
2. Raw events remain immutable wherever possible.
3. Funnel calculations must be reproducible.
4. Deterministic business rules take precedence over probabilistic AI.
5. AI predictions must never be confused with observed funnel outcomes.
6. Every funnel stage must have explicit semantics.
7. Every conversion must be traceable to underlying events.
8. Every major AI insight must have evidence and confidence.
9. Historical analytics must remain stable across funnel-definition changes.
10. Event identity and customer identity must be explicitly separated.
11. Funnel state must be idempotently maintained.
12. Late-arriving events must be reconciled.
13. Cross-tenant funnel leakage is unacceptable.
14. Authorization must be enforced before customer-level drill-down.
15. High-impact AI optimization requires human governance.
16. Experimentation must distinguish correlation from causal evidence.
17. Statistical uncertainty must be represented where applicable.
18. Funnel calculations must scale horizontally.
19. Consumer failures must not corrupt funnel state.
20. All administrative funnel changes must be auditable.
21. Privacy must be enforced throughout the funnel lifecycle.
22. AI-generated recommendations must be measurable through subsequent events.
23. Funnel optimization must operate as a closed feedback loop.
24. Every important funnel metric must be traceable to source events.
25. The platform must support both real-time and historical analytical workloads.

---

## 50. Final Requirement

SalesGenie's Funnel Analytics subsystem SHALL provide an enterprise-scale, AI-native funnel intelligence platform capable of transforming raw behavioral, business, AI, customer, sales, marketing, support, workflow, and subscription events into measurable customer journeys and conversion funnels.

The complete intelligence loop SHALL be:

```text
Human Activity
+
AI Activity
+
System Activity
+
Customer Activity
+
Business Events
        ↓
Analytics Events
        ↓
Identity Resolution
        ↓
Funnel Construction
        ↓
Stage Evaluation
        ↓
Conversion Measurement
        ↓
Drop-Off Analysis
        ↓
Segmentation
        ↓
Attribution
        ↓
Cohort Analysis
        ↓
AI Diagnosis
        ↓
AI Forecasting
        ↓
AI Recommendation
        ↓
Human Approval
        ↓
Experimentation
        ↓
Business / Workflow Action
        ↓
New Customer Behavior
        ↓
New Analytics Events
        ↓
Continuous Funnel Optimization
```

The resulting system SHALL enable SalesGenie to understand **where customers enter, how they progress, where they abandon, why they abandon, what predicts conversion, how AI and humans influence progression, how much revenue each funnel generates, and which interventions can measurably improve conversion and customer outcomes.**
