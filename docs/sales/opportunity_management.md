# Opportunity Management — FAANG-Level Requirements Specification

## 1. Document Overview

### 1.1 Purpose

The Opportunity Management module shall provide an enterprise-grade system for identifying, creating, qualifying, managing, forecasting, advancing, closing, and analyzing sales opportunities across the complete revenue lifecycle.

The system shall support:

* Human-driven opportunity management
* AI-driven opportunity management
* Hybrid AI + human workflows
* B2B and B2C sales opportunities
* Multiple pipelines
* Multiple sales stages
* Account and contact relationships
* Opportunity scoring
* AI opportunity qualification
* AI win-probability prediction
* AI next-best-action recommendations
* Revenue forecasting
* Pipeline analytics
* Competitive intelligence
* Risk detection
* Deal collaboration
* Approval workflows
* Automated sales workflows
* Enterprise RBAC
* Multi-tenant isolation
* Complete auditability

The module shall operate as the central opportunity intelligence layer connecting accounts, contacts, leads, sales activities, products, pricing, proposals, contracts, billing, customer success, marketing, and AI agents.

---

## 2. Opportunity Management Objectives

The system shall:

1. Create and manage opportunities.
2. Support configurable sales pipelines.
3. Track opportunity lifecycle.
4. Associate opportunities with accounts and contacts.
5. Manage opportunity ownership.
6. Support opportunity teams.
7. Track deal value and revenue.
8. Track opportunity products.
9. Manage sales stages.
10. Calculate opportunity scores.
11. Predict opportunity win probability.
12. Detect deal risks.
13. Recommend next-best actions.
14. Forecast revenue.
15. Identify stalled opportunities.
16. Detect competitive threats.
17. Identify expansion opportunities.
18. Automate opportunity workflows.
19. Support human sales representatives.
20. Support AI sales agents.
21. Provide complete opportunity timelines.
22. Provide enterprise-grade governance and security.

---

## 3. User Requirements

## UR-001 — Opportunity Creation

Authorized users shall be able to create opportunities manually.

An opportunity may contain:

* Opportunity ID
* Opportunity name
* Account
* Primary contact
* Pipeline
* Sales stage
* Opportunity type
* Opportunity source
* Owner
* Sales team
* Currency
* Deal value
* Recurring value
* One-time value
* Probability
* Expected close date
* Products
* Competitors
* Customer requirements
* Business pain points
* Decision criteria
* Decision process
* Next action
* Notes
* Tags
* Custom fields

---

## UR-002 — AI Opportunity Creation

The system shall be able to create opportunities from qualified signals including:

* Qualified leads
* Inbound requests
* Website activity
* Product usage
* Contact interactions
* Email conversations
* Meeting outcomes
* CRM activity
* Marketing campaigns
* Customer expansion signals
* AI-detected buying intent

AI-created opportunities shall require configurable validation or human approval.

---

## UR-003 — Opportunity Search

Users shall be able to search opportunities using:

* Opportunity name
* Account
* Contact
* Owner
* Pipeline
* Stage
* Value
* Probability
* Close date
* Opportunity source
* Industry
* Product
* Competitor
* Health
* Risk
* Score
* Tags

---

## UR-004 — Opportunity Profile

The opportunity profile shall provide a unified view containing:

* Opportunity information
* Account
* Contacts
* Stakeholders
* Pipeline
* Stage
* Deal value
* Products
* Pricing
* Competitors
* Activities
* Communications
* Meetings
* Tasks
* Documents
* Proposals
* Contracts
* Risks
* AI insights
* AI recommendations
* Forecast
* Audit history

---

## UR-005 — Opportunity Ownership

Authorized users shall be able to assign:

* Opportunity owner
* Account executive
* Sales engineer
* Sales manager
* Customer-success representative
* Technical representative
* AI sales agent
* Opportunity team

---

## UR-006 — Opportunity Team

Multiple users shall be able to collaborate on an opportunity.

Supported roles may include:

* Account Executive
* Sales Development Representative
* Sales Engineer
* Solutions Architect
* Customer Success Manager
* Legal Representative
* Finance Representative
* Executive Sponsor
* Sales Manager
* AI Sales Agent

---

## UR-007 — Opportunity Pipelines

Users shall be able to create and manage multiple pipelines.

Examples:

```text
New Business
Enterprise Sales
SMB Sales
Partner Sales
Renewal
Expansion
Cross-Sell
Upsell
```

---

## UR-008 — Opportunity Stages

Each pipeline shall support configurable stages.

Example:

```text
Prospecting
    ↓
Qualification
    ↓
Discovery
    ↓
Solution Fit
    ↓
Proposal
    ↓
Negotiation
    ↓
Legal / Procurement
    ↓
Commit
    ↓
Closed Won / Closed Lost
```

---

## UR-009 — Opportunity Stage Movement

Users shall be able to move opportunities between stages.

The system shall validate stage requirements before allowing transitions where configured.

---

## UR-010 — Opportunity Value

Users shall be able to define:

* Total contract value
* Annual recurring revenue
* Monthly recurring revenue
* One-time value
* Expansion value
* Discount
* Tax
* Expected revenue
* Weighted revenue

---

## UR-011 — Opportunity Products

Users shall be able to associate:

* Products
* Services
* Plans
* Add-ons
* Licenses
* Usage packages
* Professional services

with opportunities.

---

## UR-012 — Opportunity Contacts

Users shall be able to associate multiple contacts with different roles.

Example:

```text
Economic Buyer
Decision Maker
Champion
Technical Evaluator
Procurement
Legal
End User
Influencer
```

---

## UR-013 — Opportunity Timeline

The system shall provide a chronological timeline of:

* Opportunity creation
* Stage changes
* Emails
* Calls
* Meetings
* Notes
* Tasks
* Proposals
* Product changes
* Pricing changes
* Competitor events
* AI decisions
* Human decisions
* Approvals
* Contract events

---

## 4. Opportunity Lifecycle Requirements

## UR-014 — Opportunity Lifecycle

The system shall support configurable lifecycle states.

```text
Created
   ↓
Qualified
   ↓
Discovery
   ↓
Solution Validation
   ↓
Proposal
   ↓
Negotiation
   ↓
Commit
   ↓
Closed Won
```

Alternative terminal state:

```text
Closed Lost
```

---

## UR-015 — Closed-Lost Reason

Closed-lost opportunities shall support structured reasons:

* Price
* Competitor
* Product gap
* Timing
* No budget
* No decision
* Poor fit
* Internal priority
* Procurement
* Technical limitation
* Customer churn
* Other

---

## UR-016 — Closed-Won Processing

Closed-won opportunities shall optionally trigger:

* Contract creation
* Subscription creation
* Billing workflow
* Customer onboarding
* Customer-success assignment
* Product provisioning
* Welcome workflow
* Revenue recognition workflow

---

## 5. AI-Based User Requirements

## AI-UR-001 — AI Opportunity Qualification

AI shall evaluate opportunities using:

* ICP fit
* Account quality
* Business need
* Buying intent
* Budget indicators
* Authority
* Timeline
* Product fit
* Engagement
* Historical patterns

AI shall produce:

```text
Qualification Score
Qualification Status
Supporting Signals
Missing Information
Confidence
```

---

## AI-UR-002 — AI Opportunity Scoring

The system shall calculate an opportunity score based on configurable signals.

Example:

```text
Account Fit
+
Intent
+
Engagement
+
Budget
+
Authority
+
Timeline
+
Product Fit
+
Historical Win Patterns
=
Opportunity Score
```

---

## AI-UR-003 — AI Win Probability

AI shall predict:

* Probability of winning
* Probability of losing
* Probability of no decision
* Expected close date
* Confidence interval
* Key positive signals
* Key negative signals

---

## AI-UR-004 — AI Deal Health

AI shall calculate deal health using:

* Activity frequency
* Stakeholder engagement
* Stage duration
* Response time
* Meeting frequency
* Product fit
* Competitive pressure
* Pricing discussions
* Champion strength
* Executive engagement
* Next-step clarity

---

## AI-UR-005 — AI Deal Risk Detection

AI shall identify:

* Stalled deal
* Weak champion
* Missing decision maker
* Pricing risk
* Competitive threat
* Procurement risk
* Legal risk
* Technical risk
* Product-fit risk
* Timeline risk
* Low engagement
* Single-threaded relationship
* No-next-step risk

---

## AI-UR-006 — AI Next-Best-Action

AI shall recommend actions such as:

* Contact decision maker
* Strengthen champion
* Schedule technical workshop
* Send case study
* Schedule executive meeting
* Resolve product objection
* Re-engage inactive contact
* Escalate pricing approval
* Schedule follow-up
* Update opportunity stage
* Introduce customer reference

---

## AI-UR-007 — AI Deal Coaching

AI shall provide opportunity-specific coaching.

Example:

```text
Current Stage: Negotiation

Detected Risks:
- Procurement has not engaged.
- Economic buyer engagement is low.
- Competitor X is active.

Recommended Actions:
1. Engage procurement.
2. Reconfirm business value.
3. Schedule executive alignment meeting.
```

---

## AI-UR-008 — AI Stakeholder Mapping

AI shall identify probable:

* Economic buyer
* Champion
* Decision maker
* Influencer
* Technical evaluator
* Procurement
* Legal
* End user

---

## AI-UR-009 — AI Relationship Strength

AI shall estimate relationship strength between opportunity stakeholders and the sales team.

Factors may include:

* Communication frequency
* Response rate
* Meeting participation
* Seniority
* Positive sentiment
* Historical engagement
* Champion behavior

---

## AI-UR-010 — AI Competitive Intelligence

AI shall identify potential competitive threats based on authorized data.

The system shall provide:

* Competitor
* Evidence
* Threat level
* Competitive strengths
* Competitive weaknesses
* Recommended response

---

## AI-UR-011 — AI Objection Detection

AI shall identify objections involving:

* Price
* Product
* Security
* Integration
* Performance
* Procurement
* Implementation
* Contract
* Competition

---

## AI-UR-012 — AI Objection Recommendation

For detected objections, AI shall recommend:

* Response strategy
* Supporting evidence
* Product documentation
* Case studies
* Customer references
* Pricing strategy
* Escalation path

---

## AI-UR-013 — AI Forecasting

AI shall forecast:

* Expected bookings
* Expected revenue
* Weighted pipeline
* Commit revenue
* Best-case revenue
* Worst-case revenue
* Expected close dates

---

## AI-UR-014 — AI Forecast Confidence

Forecasts shall include:

```text
Prediction
Confidence
Prediction Range
Supporting Evidence
Model Version
Generated At
```

---

## AI-UR-015 — AI Pipeline Prioritization

AI shall prioritize opportunities using:

```text
Expected Revenue
+
Win Probability
+
Urgency
+
Strategic Value
+
Customer Intent
-
Deal Risk
-
Stagnation
```

---

## AI-UR-016 — AI Stagnation Detection

AI shall detect opportunities that:

* Remain too long in one stage
* Have declining activity
* Have no next action
* Have declining engagement
* Have inactive stakeholders

---

## AI-UR-017 — AI Opportunity Summary

AI shall generate an executive opportunity summary containing:

* Account
* Deal value
* Current stage
* Customer need
* Key stakeholders
* Products
* Competition
* Recent activity
* Risks
* Win probability
* Forecast
* Recommended actions

---

## AI-UR-018 — AI Opportunity Forecasting by Segment

AI shall forecast opportunities by:

* Sales representative
* Team
* Region
* Industry
* Product
* Pipeline
* Customer segment
* Geography

---

## AI-UR-019 — AI Opportunity Expansion Detection

For existing customers, AI shall identify:

* Upsell
* Cross-sell
* Additional licenses
* New departments
* New geographic markets
* New products
* Increased usage

---

## AI-UR-020 — AI Opportunity Creation from Customer Signals

AI shall detect opportunity signals from:

* Increased usage
* Feature usage
* Support requests
* Product inquiries
* Customer emails
* Account activity
* Marketing engagement

and recommend opportunity creation.

---

## 6. Human-Based User Requirements

## HUMAN-UR-001 — Sales Representative Workspace

Sales representatives shall have access to:

* Assigned opportunities
* Pipeline
* Tasks
* Activities
* Contacts
* Deal health
* AI recommendations
* Risks
* Forecast
* Next actions

---

## HUMAN-UR-002 — Manual Opportunity Qualification

Humans shall be able to review and modify:

* Qualification
* Score
* Probability
* Stage
* Value
* Close date
* Opportunity owner

---

## HUMAN-UR-003 — Human Approval

Configurable actions shall require human approval.

Examples:

* Large discounts
* Deal closure
* Forecast overrides
* Pricing exceptions
* Contract exceptions
* AI-generated customer communications
* Opportunity reassignment

---

## HUMAN-UR-004 — Human Override

Authorized humans shall be able to override AI:

* Score
* Probability
* Forecast
* Risk
* Stage recommendation
* Next-best-action
* Qualification

The override reason shall be recorded.

---

## HUMAN-UR-005 — Human-AI Collaboration

Sales users shall be able to ask:

```text
Why is this opportunity at risk?

Why did the win probability decrease?

What should I do next?

Which stakeholder should I contact?

What is blocking this deal?

Which opportunities should I prioritize today?

What is my forecast for this quarter?
```

---

## 7. System Requirements

## SR-001 — Opportunity Service

The system shall provide a dedicated Opportunity Management Service responsible for:

* Opportunity CRUD
* Pipelines
* Stages
* Ownership
* Products
* Contacts
* Scoring
* Forecasting
* Opportunity health
* Risk detection
* Opportunity intelligence

---

## SR-002 — Multi-Tenant Architecture

Every opportunity shall be associated with appropriate tenant boundaries:

```text
tenant_id
organization_id
workplace_id
```

Cross-tenant access shall be prohibited unless explicitly authorized.

---

## SR-003 — Opportunity Identifier

Every opportunity shall have an immutable globally unique identifier.

```text
opportunity_id = UUID
```

---

## SR-004 — Opportunity Number

The system may expose a human-readable opportunity number.

Example:

```text
OPP-2026-000123
```

---

## SR-005 — Pipeline Engine

The pipeline engine shall support:

* Multiple pipelines
* Configurable stages
* Stage probability
* Stage requirements
* Stage validation
* Stage automation
* Pipeline-specific permissions

---

## SR-006 — Stage Transition Engine

The system shall support:

```text
Stage Entered
Stage Exited
Stage Duration
Required Fields
Required Activities
Approval Requirements
Automation
```

---

## SR-007 — Opportunity State Machine

Opportunity lifecycle transitions shall be governed by a state machine.

Invalid transitions shall be rejected.

---

## SR-008 — Opportunity Event System

The platform shall publish events including:

```text
OpportunityCreated
OpportunityUpdated
OpportunityAssigned
OpportunityStageChanged
OpportunityValueChanged
OpportunityProbabilityChanged
OpportunityRiskDetected
OpportunityHealthChanged
OpportunityForecastChanged
OpportunityWon
OpportunityLost
OpportunityReopened
OpportunityMerged
```

---

## SR-009 — Event Processing

Event processing shall support:

* Idempotency
* Retry
* Dead-letter queues
* Event replay
* Event versioning
* Ordering where required

---

## SR-010 — Opportunity Intelligence Service

AI capabilities shall be exposed through a dedicated intelligence layer.

```text
Opportunity Service
        ↓
Opportunity Intelligence Service
        ↓
AI Model Router
        ↓
ML / LLM Models
```

---

## SR-011 — AI Metadata

AI-generated opportunity intelligence shall include:

```text
value
confidence
source
model_id
model_version
generated_at
expires_at
```

---

## SR-012 — Forecast Engine

The forecasting engine shall support:

* Rule-based forecasting
* Statistical forecasting
* ML forecasting
* AI-assisted forecasting
* Human overrides

---

## SR-013 — Ownership Engine

Opportunity assignment shall support:

* Manual assignment
* Territory assignment
* Round-robin
* Workload balancing
* Skill-based assignment
* AI-based assignment

---

## SR-014 — Approval Engine

The approval system shall support configurable approval chains.

Example:

```text
Discount > 10%
      ↓
Sales Manager

Discount > 20%
      ↓
Sales Director

Discount > 30%
      ↓
Executive Approval
```

---

## 8. Functional Requirements

## FR-001 — Opportunity CRUD

The system shall support:

```text
Create
Read
Update
Archive
Restore
Close
Reopen
```

subject to authorization and lifecycle rules.

---

## FR-002 — Bulk Opportunity Operations

The system shall support:

```text
Bulk Update
Bulk Assign
Bulk Reassign
Bulk Stage Change
Bulk Tag
Bulk Archive
Bulk Export
Bulk AI Analysis
```

Large operations shall execute asynchronously.

---

## FR-003 — Opportunity Creation Workflow

The opportunity creation workflow shall support:

```text
Account Selection
        ↓
Contact Selection
        ↓
Pipeline Selection
        ↓
Opportunity Details
        ↓
Products
        ↓
Value
        ↓
Expected Close Date
        ↓
Qualification
        ↓
Owner
        ↓
Save
```

---

## FR-004 — AI Opportunity Creation Workflow

```text
Signal Detected
      ↓
AI Validation
      ↓
Account Resolution
      ↓
Contact Resolution
      ↓
Opportunity Generation
      ↓
Qualification
      ↓
Score
      ↓
Human Approval if Required
      ↓
Opportunity Created
```

---

## FR-005 — Opportunity Search

The system shall provide:

```text
GET /opportunities
GET /opportunities/{opportunity_id}
GET /opportunities/search
GET /opportunities/{opportunity_id}/contacts
GET /opportunities/{opportunity_id}/activities
GET /opportunities/{opportunity_id}/timeline
GET /opportunities/{opportunity_id}/forecast
GET /opportunities/{opportunity_id}/risks
GET /opportunities/{opportunity_id}/insights
```

---

## FR-006 — Opportunity Profile

The profile shall return:

```text
Opportunity
Account
Contacts
Stakeholders
Pipeline
Stage
Value
Products
Activities
Risks
Health
Score
Probability
Forecast
AI Insights
Recommendations
```

---

## FR-007 — Pipeline Management

Authorized administrators shall be able to:

* Create pipelines
* Rename pipelines
* Archive pipelines
* Create stages
* Reorder stages
* Configure probabilities
* Configure requirements
* Configure automation

---

## FR-008 — Stage Management

Each stage shall support:

* Name
* Description
* Probability
* Required fields
* Required activities
* Entry automation
* Exit automation
* SLA
* Approval requirements

---

## FR-009 — Stage Transition Validation

Before stage transition, the system shall validate configured requirements.

Example:

```text
Proposal Stage

Required:
✓ Opportunity value
✓ Primary contact
✓ Decision criteria
✓ Proposal document
✓ Expected close date
```

---

## FR-010 — Opportunity Scoring

The scoring engine shall calculate configurable opportunity scores.

---

## FR-011 — Score Explainability

Example:

```text
Opportunity Score: 84

Positive:
+18 Strong account fit
+15 High buying intent
+12 Executive engagement
+10 Product fit

Negative:
-8 Competitive pressure
-5 Procurement uncertainty
```

---

## FR-012 — Win Probability

The system shall calculate and display:

```text
Win Probability
Loss Probability
No-Decision Probability
Confidence
Prediction Timestamp
```

---

## FR-013 — Opportunity Health

Opportunity health shall support:

```text
Healthy
Warning
At Risk
Critical
```

---

## FR-014 — Health Explanation

The system shall explain health status.

Example:

```text
Health: At Risk

Reasons:
- 21 days without customer interaction
- Decision maker not engaged
- Close date approaching
- Competitor detected
```

---

## FR-015 — Opportunity Risk Management

The system shall maintain structured risks.

Each risk shall contain:

```text
risk_id
risk_type
severity
probability
impact
description
owner
mitigation
status
created_at
resolved_at
```

---

## FR-016 — Risk Mitigation

Users shall be able to:

* Create mitigation actions
* Assign owners
* Set deadlines
* Track status
* Resolve risks

---

## FR-017 — Next-Best-Action Engine

The system shall generate recommended actions with:

```text
Action
Reason
Priority
Expected Impact
Confidence
Required User
Deadline
```

---

## FR-018 — Action Approval

AI-recommended actions shall support:

```text
Approve
Reject
Modify
Defer
Execute
```

---

## FR-019 — Opportunity Tasks

Users shall be able to create:

* Calls
* Emails
* Meetings
* Follow-ups
* Demos
* Technical workshops
* Proposal reviews
* Negotiation tasks
* Renewal tasks

---

## FR-020 — AI Task Generation

AI shall generate tasks based on:

* Opportunity stage
* Deal health
* Risk
* Customer behavior
* Next-best-action
* Close date

---

## FR-021 — Activity Tracking

The system shall record:

* Calls
* Emails
* Meetings
* Notes
* Tasks
* Documents
* Customer interactions
* AI interactions

---

## FR-022 — Opportunity Timeline

Every material event shall be displayed chronologically.

---

## FR-023 — Product Management

Users shall be able to:

* Add products
* Remove products
* Change quantities
* Change prices
* Apply discounts
* Calculate totals

---

## FR-024 — Pricing Approval

Pricing exceptions shall support configurable approval thresholds.

---

## FR-025 — Competitor Management

Users shall be able to associate competitors with opportunities.

The system shall track:

* Competitor
* Competitive position
* Strength
* Weakness
* Threat level
* Customer preference
* Sales response

---

## FR-026 — AI Competitor Detection

AI shall detect competitor mentions in authorized communications and recommend updating the opportunity.

---

## FR-027 — Forecast Categories

The system shall support:

```text
Pipeline
Best Case
Commit
Most Likely
Closed Won
Closed Lost
```

---

## FR-028 — Forecast Overrides

Authorized users shall be able to override AI or calculated forecasts.

Overrides shall require a reason.

---

## FR-029 — Forecast Analytics

The system shall provide:

* Pipeline value
* Weighted pipeline
* Commit value
* Best-case value
* Forecast value
* Actual bookings
* Forecast variance

---

## FR-030 — Forecast by Dimensions

Forecasts shall be filterable by:

* Team
* Sales representative
* Region
* Industry
* Product
* Pipeline
* Account segment
* Time period

---

## FR-031 — AI Forecast Analysis

AI shall identify:

* Forecast risk
* Over-forecasting
* Under-forecasting
* Pipeline gaps
* Stalled deals
* Unreliable opportunities
* Expected forecast changes

---

## FR-032 — Opportunity Prioritization

The system shall provide ranked opportunity lists.

Example:

```text
Priority 1 — $500K — 82% Win Probability
Priority 2 — $250K — 74% Win Probability
Priority 3 — $120K — 91% Win Probability
```

---

## FR-033 — AI Opportunity Prioritization

AI shall prioritize opportunities using configurable business objectives.

---

## FR-034 — Opportunity Collaboration

Users shall be able to:

* Mention team members
* Assign tasks
* Share notes
* Comment
* Review AI recommendations
* Request approvals

---

## FR-035 — Opportunity Documents

The system shall associate:

* Proposals
* Quotes
* Contracts
* Presentations
* Product documents
* Security documents

with opportunities.

---

## FR-036 — Opportunity Approval Workflow

Approval workflows shall support:

```text
Discount Approval
Pricing Approval
Contract Approval
Forecast Approval
Opportunity Closure
Exception Approval
```

---

## FR-037 — Opportunity Automation

The system shall support triggers such as:

```text
Opportunity Created
Stage Changed
Value Changed
Risk Detected
Health Changed
Close Date Approaching
No Activity
Probability Changed
```

Actions may include:

```text
Create Task
Send Notification
Assign User
Update Field
Invoke AI Agent
Call Webhook
Start Workflow
Request Approval
```

---

## FR-038 — AI Opportunity Automation

AI shall be able to initiate configured workflows based on authorized signals.

High-impact actions shall support human approval.

---

## FR-039 — Natural Language Opportunity Search

Users shall be able to ask:

```text
Show me all opportunities above $100K closing this quarter.

Which deals are at risk?

Which opportunities have no decision maker?

Which opportunities have been stalled for more than 14 days?

Which deals should I focus on today?

What is likely to close this month?
```

---

## FR-040 — AI Query Authorization

Natural-language queries shall be executed only against data the requesting user is authorized to access.

---

## FR-041 — Opportunity Briefing

AI shall generate:

```text
Deal Overview
Customer Need
Stakeholders
Products
Deal Value
Stage
Win Probability
Health
Risks
Competition
Recent Activity
Next Actions
Forecast
```

---

## FR-042 — Sales Manager Dashboard

The dashboard shall provide:

* Pipeline value
* Opportunities
* Win rate
* Loss rate
* Average deal size
* Average sales cycle
* Conversion rates
* Forecast
* Pipeline coverage
* At-risk deals
* Stalled deals
* AI recommendations

---

## FR-043 — Sales Representative Dashboard

The dashboard shall provide:

* My opportunities
* Today's tasks
* Upcoming meetings
* At-risk deals
* High-priority opportunities
* AI recommendations
* Pipeline
* Forecast

---

## FR-044 — Opportunity Analytics

The system shall provide:

### Pipeline Metrics

* Total opportunities
* Pipeline value
* Weighted pipeline
* Average deal size
* Pipeline coverage

### Conversion Metrics

* Stage conversion rate
* Win rate
* Loss rate
* No-decision rate

### Velocity Metrics

* Average sales cycle
* Stage duration
* Time-to-first-response
* Time-to-close

### Revenue Metrics

* New revenue
* Expansion revenue
* Recurring revenue
* Forecast revenue

---

## FR-045 — Cohort Analysis

Opportunity analytics shall support cohorts by:

* Creation period
* Sales team
* Product
* Industry
* Region
* Lead source
* Customer segment

---

## FR-046 — AI Opportunity Analytics

AI shall identify:

* Pipeline bottlenecks
* Low-performing stages
* High-performing sales representatives
* Revenue risks
* Win-rate changes
* Sales-cycle changes
* Product trends
* Competitive trends

---

## FR-047 — Closed-Lost Analysis

AI shall analyze closed-lost opportunities and identify:

* Common loss reasons
* Competitor impact
* Pricing impact
* Product gaps
* Sales-stage bottlenecks
* Industry patterns
* Representative patterns

---

## FR-048 — Win Analysis

AI shall analyze closed-won opportunities to identify:

* Winning patterns
* Common stakeholders
* Successful products
* Successful sales motions
* Successful industries
* Successful pricing patterns

---

## FR-049 — AI Sales Coaching

The system shall provide sales representatives with opportunity-specific recommendations.

---

## FR-050 — AI Communication Assistance

AI shall assist in generating:

* Follow-up emails
* Meeting agendas
* Proposal summaries
* Objection responses
* Executive briefings
* Negotiation preparation
* Meeting summaries

Human approval shall be configurable before external communication.

---

## FR-051 — Opportunity Reopening

Authorized users shall be able to reopen closed opportunities.

The system shall record:

* Previous state
* Reopening reason
* Actor
* Timestamp

---

## FR-052 — Opportunity Merge

Authorized users shall be able to merge duplicate opportunities.

The system shall preserve:

* Timeline
* Activities
* Products
* Contacts
* Notes
* Audit records

---

## FR-053 — Opportunity Archive

Archived opportunities shall remain retrievable according to retention policies.

---

## FR-054 — Audit Logging

Every material operation shall record:

```text
Actor
Actor Type
Action
Timestamp
Object
Before State
After State
Reason
Source
```

Actor types:

```text
Human
AI Agent
System
Integration
```

---

## FR-055 — AI Audit Trail

AI actions shall additionally record:

```text
AI Agent
Model ID
Model Version
Policy Version
Input References
Decision
Confidence
Action
Execution Result
Human Approval
```

---

## FR-056 — APIs

The system shall expose APIs for:

* Opportunity CRUD
* Search
* Pipelines
* Stages
* Products
* Scoring
* Qualification
* Forecasting
* Risk management
* AI insights
* Tasks
* Activities
* Analytics

---

## FR-057 — Webhooks

The system shall support:

```text
opportunity.created
opportunity.updated
opportunity.assigned
opportunity.stage_changed
opportunity.value_changed
opportunity.risk_detected
opportunity.health_changed
opportunity.forecast_changed
opportunity.won
opportunity.lost
opportunity.reopened
```

---

## 9. AI + Human Operating Model

## 9.1 AI-Only Workflow

```text
Signal Detected
      ↓
AI Qualification
      ↓
AI Account Resolution
      ↓
AI Opportunity Creation
      ↓
AI Scoring
      ↓
AI Win Probability
      ↓
AI Risk Detection
      ↓
AI Next-Best-Action
      ↓
Automated Workflow
```

---

## 9.2 Human-Only Workflow

```text
Opportunity Created
      ↓
Human Qualification
      ↓
Human Discovery
      ↓
Human Stakeholder Mapping
      ↓
Human Proposal
      ↓
Human Negotiation
      ↓
Human Closure
```

---

## 9.3 Hybrid AI + Human Workflow

```text
Opportunity Created
      ↓
AI Qualification
      ↓
AI Scoring
      ↓
AI Deal Health
      ↓
AI Risk Detection
      ↓
Human Review
      ↓
AI Recommendation
      ↓
Human Approval
      ↓
Automated Execution
      ↓
Human Monitoring
      ↓
AI Continuous Analysis
```

---

## 10. Security Requirements

## SEC-001 — Authentication

All protected opportunity operations shall require authenticated access.

---

## SEC-002 — Authorization

Every opportunity operation shall validate:

```text
User
+
Role
+
Permission
+
Tenant
+
Organization
+
Workplace
+
Resource
```

---

## SEC-003 — Opportunity-Level Access

The platform shall support:

* Owner-based access
* Team-based access
* Organization-level access
* Workplace-level access
* Role-based access
* Attribute-based access

---

## SEC-004 — Field-Level Security

Sensitive fields such as:

* Pricing
* Discounts
* Margin
* Forecast
* Commission
* Contract value

shall support field-level permissions.

---

## SEC-005 — Tenant Isolation

Opportunities shall never be exposed across tenants without explicit authorization.

---

## SEC-006 — Encryption

Sensitive opportunity information shall be encrypted:

* In transit
* At rest
* In backups where applicable

---

## SEC-007 — Rate Limiting

Rate limits shall apply to:

* Search
* Bulk operations
* AI analysis
* Forecasting
* Export
* API access

---

## 11. Non-Functional Requirements

## NFR-001 — Performance

Normal opportunity queries should target sub-second response times under expected production load.

---

## NFR-002 — Scalability

The architecture shall support millions to billions of opportunity-related records through horizontal scaling.

---

## NFR-003 — Availability

Critical opportunity services should target:

```text
99.9%+
```

availability.

---

## NFR-004 — Reliability

The system shall support:

* Transaction integrity
* Idempotency
* Retry
* Failure recovery
* Event replay
* Dead-letter processing

---

## NFR-005 — Observability

The system shall expose:

* Metrics
* Logs
* Distributed traces
* API latency
* AI latency
* Forecast latency
* Event-processing latency
* Queue depth
* Workflow failures
* Model failures

---

## NFR-006 — Explainability

AI decisions affecting opportunity management shall provide:

* Reasoning factors
* Supporting signals
* Confidence
* Model version
* Timestamp

---

## NFR-007 — Maintainability

Opportunity services shall use modular components and versioned APIs.

---

## NFR-008 — Extensibility

The system shall support additional:

* AI models
* ML models
* Sales methodologies
* CRM integrations
* Data providers
* Forecasting models
* Workflow engines
* Sales agents

without major architectural changes.

---

## 12. Core Data Model

```text
Tenant
Organization
Workplace
User
Team

Opportunity
OpportunityNumber
OpportunityPipeline
OpportunityStage
OpportunityLifecycle

OpportunityOwner
OpportunityTeam
OpportunityRole

OpportunityAccount
OpportunityContact
OpportunityStakeholder
OpportunityRelationship

OpportunityProduct
OpportunityPrice
OpportunityDiscount
OpportunityQuote

OpportunityValue
OpportunityRevenue
OpportunityForecast

OpportunityScore
OpportunityQualification
OpportunityHealth
OpportunityRisk
OpportunityIntent

OpportunityCompetitor
OpportunityObjection

OpportunityActivity
OpportunityInteraction
OpportunityTask
OpportunityNote

OpportunityDocument
OpportunityProposal
OpportunityContract

OpportunityApproval
OpportunityWorkflow

OpportunityPrediction
OpportunityInsight
OpportunityRecommendation

OpportunityAuditEvent
OpportunityWebhookEvent

AIInsight
AIRecommendation
AIExecution
AIApproval
```

---

## 13. Example End-to-End Workflow

```text
Qualified Lead
      ↓
Account Resolution
      ↓
Contact Resolution
      ↓
Opportunity Creation
      ↓
AI Qualification
      ↓
AI Opportunity Score
      ↓
Pipeline Assignment
      ↓
Opportunity Owner Assignment
      ↓
Discovery
      ↓
Stakeholder Mapping
      ↓
AI Intent Analysis
      ↓
Solution Validation
      ↓
AI Risk Detection
      ↓
Proposal
      ↓
AI Competitive Analysis
      ↓
Negotiation
      ↓
AI Win Probability
      ↓
Forecast
      ↓
Human Approval
      ↓
Closed Won
      ↓
Contract
      ↓
Billing
      ↓
Customer Onboarding
```

---

## 14. Acceptance Criteria

* [ ] Users can create opportunities.
* [ ] AI can recommend or create opportunities from qualified signals.
* [ ] Users can edit opportunities.
* [ ] Users can archive and restore opportunities.
* [ ] Users can close opportunities.
* [ ] Users can reopen opportunities according to authorization.
* [ ] Multiple pipelines are supported.
* [ ] Pipeline stages are configurable.
* [ ] Stage transition rules are supported.
* [ ] Stage requirements are enforced.
* [ ] Opportunities can be associated with accounts.
* [ ] Opportunities can be associated with contacts.
* [ ] Stakeholder roles are supported.
* [ ] Opportunity ownership is supported.
* [ ] Opportunity teams are supported.
* [ ] Opportunity products are supported.
* [ ] Opportunity values are supported.
* [ ] Recurring and one-time revenue are supported.
* [ ] Competitor tracking is supported.
* [ ] Opportunity risks are supported.
* [ ] Opportunity health is supported.
* [ ] AI opportunity qualification is supported.
* [ ] AI opportunity scoring is supported.
* [ ] AI win probability is supported.
* [ ] AI deal-health analysis is supported.
* [ ] AI risk detection is supported.
* [ ] AI next-best-action recommendations are supported.
* [ ] AI stakeholder mapping is supported.
* [ ] AI competitive intelligence is supported.
* [ ] AI objection detection is supported.
* [ ] AI forecasting is supported.
* [ ] Forecast confidence is available.
* [ ] Human forecast overrides are supported.
* [ ] AI opportunity prioritization is supported.
* [ ] Stalled opportunity detection is supported.
* [ ] Opportunity expansion detection is supported.
* [ ] Human approval workflows are supported.
* [ ] Human overrides of AI decisions are supported.
* [ ] AI-only workflows are supported.
* [ ] Human-only workflows are supported.
* [ ] Hybrid AI + human workflows are supported.
* [ ] Opportunity tasks are supported.
* [ ] Opportunity activities are tracked.
* [ ] Opportunity timelines are available.
* [ ] AI-generated opportunity briefings are supported.
* [ ] Natural-language opportunity search is supported.
* [ ] AI queries respect RBAC and tenant isolation.
* [ ] Sales dashboards are supported.
* [ ] Pipeline analytics are supported.
* [ ] Forecast analytics are supported.
* [ ] Win/loss analysis is supported.
* [ ] Closed-lost analysis is supported.
* [ ] AI sales coaching is supported.
* [ ] AI communication assistance is supported.
* [ ] APIs are available.
* [ ] Webhooks are supported.
* [ ] Bulk operations are supported.
* [ ] Audit logs capture human, AI, system, and integration actions.
* [ ] AI model metadata is recorded.
* [ ] Tenant isolation is enforced.
* [ ] RBAC/ABAC is enforced.
* [ ] Field-level security is supported.
* [ ] Sensitive data is encrypted.
* [ ] Rate limiting is implemented.
* [ ] Distributed observability is implemented.
* [ ] Event processing supports retry and idempotency.
* [ ] The architecture supports horizontal scaling.
