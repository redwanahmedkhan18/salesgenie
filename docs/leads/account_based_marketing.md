# SalesGenie — Account-Based Marketing (ABM)

## FAANG-Level User Requirements, System Requirements & Functional Requirements

### AI + Human Account-Based Marketing Platform

**Project:** SalesGenie  
**Module:** Account-Based Marketing  
**Capability:** AI-assisted, human-governed, revenue-centric ABM  
**Document Type:** Product & Engineering Requirements Specification  
**Version:** 1.0  
**Status:** Production-Grade Requirements

---

## 1. Executive Overview

SalesGenie's Account-Based Marketing (ABM) module shall provide an intelligent account-centric GTM system that identifies high-value accounts, evaluates account fit and buying readiness, maps buying committees, creates account strategies, orchestrates personalized multi-channel engagement, coordinates sales and marketing actions, and measures account-level revenue impact.

The system shall treat an account as a continuously evolving business entity rather than a static CRM record.

The core operating model shall be:

```text
Account Discovery
        ↓
Account Enrichment
        ↓
ICP Evaluation
        ↓
Account Scoring
        ↓
Account Tiering
        ↓
Buying Committee Mapping
        ↓
Intent + Signal Detection
        ↓
Account Research
        ↓
Account Strategy
        ↓
Personalization
        ↓
Multi-Channel Orchestration
        ↓
Sales + Marketing Coordination
        ↓
Engagement
        ↓
Opportunity Creation
        ↓
Pipeline Acceleration
        ↓
Revenue Attribution
        ↓
Outcome Analysis
        ↓
AI Learning
```

Modern enterprise ABM requires account selection, buying-group coverage, coordinated sales/marketing execution, personalization, and account-level measurement rather than treating ABM as a simple campaign or lead-generation tactic. ([Demand Shop][1])

---

## 2. Product Vision

SalesGenie shall enable revenue teams to answer:

1. Which accounts should we target?
2. Why should we target them?
3. Which accounts are most likely to buy?
4. Which accounts have the highest revenue potential?
5. Which accounts are currently showing intent?
6. Which buying committee members matter?
7. Who is the champion?
8. Who is the economic buyer?
9. Who can block the deal?
10. Which competitors are active?
11. What business problems does the account have?
12. What technology does the account use?
13. What strategic initiatives are underway?
14. What messaging should we use?
15. Which channel should we use?
16. What content should each stakeholder receive?
17. What sales play should be activated?
18. When should AI act?
19. When should a human act?
20. What should SalesGenie do next?
21. Did the ABM program create pipeline?
22. Did it accelerate revenue?
23. Which accounts should move between tiers?
24. Which accounts should be removed?
25. What should the AI learn from the outcome?

---

## 3. ABM Philosophy

SalesGenie's ABM architecture shall follow five core principles.

## 3.1 Account-Centric

The account shall be the primary unit of ABM orchestration.

```text
Account
 ├── Contacts
 ├── Buying Committee
 ├── Opportunities
 ├── Leads
 ├── Intent Signals
 ├── Engagement
 ├── Campaigns
 ├── Content
 ├── Competitors
 ├── Technology Stack
 ├── Sales Activities
 ├── Marketing Activities
 ├── Account Plan
 └── Revenue
```

---

## 3.2 Revenue-Centric

The system shall optimize for:

* Pipeline
* Pipeline velocity
* Revenue
* ACV
* ARR
* Win rate
* Sales-cycle reduction
* Expansion
* Retention
* Account penetration

It shall not optimize primarily for:

* Impressions
* Clicks
* Raw lead volume
* MQL volume
* Email volume

---

## 3.3 Signal-Driven

ABM actions shall be triggered by account signals.

Examples:

```text
Website Visit
Pricing Page Visit
Product Page Visit
Content Engagement
Executive Hiring
Funding
New Initiative
Technology Change
Job Posting
Competitor Activity
Search Intent
Email Engagement
Event Attendance
CRM Activity
Opportunity Activity
Support Activity
Product Usage
```

---

## 3.4 AI-Augmented

AI shall perform high-volume analytical and execution tasks while humans retain strategic control over sensitive decisions.

AI shall:

* Research
* Enrich
* Score
* Segment
* Detect
* Predict
* Personalize
* Recommend
* Draft
* Orchestrate
* Summarize
* Forecast
* Analyze

Humans shall:

* Define strategy
* Approve target accounts
* Approve strategic messaging
* Validate high-impact intelligence
* Manage relationships
* Approve sensitive campaigns
* Override AI decisions

AI adoption is increasingly part of ABM execution, but disciplined governance and operational design remain critical. ([Inflexion Group][2])

---

## 4. User Roles

## 4.1 Super Admin

The Super Admin shall:

* Configure global ABM capabilities.
* Configure tenant policies.
* Configure AI policies.
* Configure data-source policies.
* Configure system-wide permissions.
* Monitor ABM infrastructure.
* Audit AI activities.
* Manage feature flags.
* Configure compliance controls.

---

## 4.2 Organization Admin

The Organization Admin shall:

* Configure organization ABM settings.
* Manage users.
* Configure roles.
* Configure account visibility.
* Configure account ownership.
* Configure approval workflows.
* Configure integrations.
* Configure organization-level AI policies.

---

## 4.3 ABM Manager

The ABM Manager shall:

* Define ABM strategy.
* Define ICP.
* Create target account lists.
* Define account tiers.
* Configure account scoring.
* Create ABM programs.
* Monitor account engagement.
* Manage account plans.
* Review AI recommendations.
* Approve campaigns.
* Analyze ABM performance.

---

## 4.4 Marketing Manager

The Marketing Manager shall:

* Create account segments.
* Design account campaigns.
* Configure personalization.
* Manage content.
* Configure channels.
* Monitor engagement.
* Review account progression.
* Measure marketing influence.

---

## 4.5 Sales Manager

The Sales Manager shall:

* Review target accounts.
* Review account ownership.
* Monitor account engagement.
* Review buying committees.
* Monitor competitive threats.
* Assign sales actions.
* Review account pipeline.
* Measure sales outcomes.

---

## 4.6 Account Executive

The Account Executive shall:

* View assigned accounts.
* View account intelligence.
* View buying committees.
* View account plans.
* View intent signals.
* Receive AI recommendations.
* Execute recommended sales plays.
* Add account intelligence.
* Update account strategy.
* Collaborate with marketing.

---

## 4.7 Sales Development Representative

The SDR shall:

* View prioritized accounts.
* View recommended contacts.
* Receive outreach recommendations.
* Execute sequences.
* Record engagement.
* Submit account intelligence.
* Escalate high-intent accounts.

---

## 4.8 Marketing User

Marketing users shall:

* Build account audiences.
* Create personalized campaigns.
* Create account-specific content.
* Monitor engagement.
* Review account analytics.

---

## 4.9 Sales Engineer

Sales Engineers shall:

* Analyze account technology.
* Analyze technical requirements.
* Review account architecture.
* Map technical stakeholders.
* Create technical account plans.

---

## 4.10 Customer Success

Customer Success users shall:

* Monitor existing strategic accounts.
* Identify expansion opportunities.
* Detect churn risks.
* Identify cross-sell opportunities.
* Participate in account plans.

---

## 4.11 AI ABM Agent

The AI ABM Agent shall:

* Discover accounts.
* Enrich accounts.
* Score accounts.
* Tier accounts.
* Research accounts.
* Map buying committees.
* Detect intent.
* Detect buying signals.
* Generate account plans.
* Recommend actions.
* Generate personalization.
* Orchestrate workflows.
* Monitor outcomes.
* Recalculate account priority.

---

## 5. ABM Models

SalesGenie shall support multiple ABM operating models.

## 5.1 One-to-One ABM

For strategic accounts.

```text
1 Account
↓
Dedicated Account Plan
↓
Dedicated Buying Committee
↓
Highly Personalized Engagement
↓
Executive Coordination
```

---

## 5.2 One-to-Few ABM

For clusters of similar accounts.

```text
Industry
+
Business Model
+
Company Size
+
Pain Point
+
Technology
=
Account Cluster
```

---

## 5.3 One-to-Many ABM

For large ICP account groups using programmatic personalization.

```text
Thousands of Accounts
↓
AI Segmentation
↓
Dynamic Personalization
↓
Automated Campaigns
```

The platform shall support differentiated treatment across account tiers instead of applying identical engagement to every target account. ([Tomba][3])

---

## 6. User Requirements

## UR-ABM-001 — Account Discovery

Users shall be able to:

* Discover target accounts.
* Import account lists.
* Search accounts.
* Generate accounts using AI.
* Discover lookalike accounts.
* Discover accounts based on ICP.
* Discover accounts based on intent.
* Discover accounts based on revenue potential.
* Discover accounts based on technology stack.

---

## UR-ABM-002 — ICP Definition

Users shall define an Ideal Customer Profile using:

* Industry
* Revenue
* Employee count
* Geography
* Business model
* Technology stack
* Growth rate
* Funding
* Product category
* Customer maturity
* Existing technology
* Buying behavior
* Historical win rate
* ACV
* Sales cycle
* Expansion potential

---

## UR-ABM-003 — Data-Driven ICP

AI shall infer ICP characteristics from:

* Closed-won accounts
* Closed-lost accounts
* Opportunity history
* Customer retention
* Expansion
* Revenue
* Sales-cycle duration
* Product adoption
* Customer lifetime value

The system shall allow users to compare manually defined ICP criteria with AI-derived ICP patterns.

---

## UR-ABM-004 — Account Qualification

The platform shall determine whether an account is:

```text
Excellent Fit
High Fit
Moderate Fit
Low Fit
Poor Fit
Disqualified
```

---

## UR-ABM-005 — Account Scoring

Users shall view an account score based on:

```text
ICP Fit
+
Revenue Potential
+
Intent
+
Engagement
+
Buying Readiness
+
Strategic Value
+
Relationship Strength
+
Competitive Position
```

---

## UR-ABM-006 — Account Tiering

The system shall support:

```text
Tier 1 — Strategic
Tier 2 — High Value
Tier 3 — Scaled
Tier 4 — Nurture
Disqualified
```

Users shall be able to configure custom tiers.

---

## UR-ABM-007 — Target Account Lists

Users shall create:

* Static lists
* Dynamic lists
* AI-generated lists
* Saved searches
* Segment-based lists
* Campaign-specific lists
* Territory-based lists
* Industry-based lists

---

## UR-ABM-008 — Account Research

Users shall receive an account intelligence profile containing:

* Company overview
* Revenue
* Employees
* Industry
* Locations
* Growth
* Funding
* Leadership
* Strategic initiatives
* Technology
* Products
* Competitors
* Hiring
* News
* Intent
* Engagement
* Opportunities
* Contacts
* Buying committee
* Account risks
* Expansion opportunities

---

## UR-ABM-009 — Account Buying Committee

The system shall identify and map:

* Economic buyer
* Champion
* Decision maker
* Technical evaluator
* Procurement
* Legal
* Security
* Finance
* Executive sponsor
* Influencer
* User
* Blocker

---

## UR-ABM-010 — Buying Committee Coverage

The system shall calculate:

```text
Buying Committee Coverage =
Engaged Relevant Stakeholders
/
Estimated Relevant Stakeholders
```

The system shall identify gaps.

---

## UR-ABM-011 — Account Intent

Users shall view intent signals at account level.

Intent sources shall include:

* Website activity
* Search behavior where legally available
* Content engagement
* Product research
* Pricing activity
* Event activity
* Email engagement
* Job postings
* Technology changes
* Public announcements
* CRM behavior

---

## UR-ABM-012 — Account Engagement

The platform shall aggregate engagement across:

* Email
* Website
* Ads
* Events
* Social channels
* Meetings
* Calls
* CRM activities
* Content
* Sales sequences

---

## UR-ABM-013 — Account Timeline

Each account shall have a chronological timeline:

```text
Signal
→ Engagement
→ Contact Activity
→ Marketing Touch
→ Sales Touch
→ Meeting
→ Opportunity
→ Campaign
→ Purchase
```

---

## UR-ABM-014 — Account Plan

Users shall create account plans containing:

* Account objectives
* Revenue goals
* Stakeholders
* Business problems
* Strategic initiatives
* Competitive landscape
* Relationship map
* Engagement strategy
* Content strategy
* Sales strategy
* Risks
* Next actions
* Owners
* Deadlines

---

## UR-ABM-015 — AI Account Plan

AI shall generate account-plan drafts from available evidence.

The plan shall clearly separate:

```text
Verified Fact
Inference
Recommendation
Prediction
```

---

## UR-ABM-016 — Account Personalization

The system shall generate personalization based on:

* Industry
* Company strategy
* Stakeholder role
* Business pain
* Technology
* Intent
* Account stage
* Previous engagement
* Competitor
* Current opportunity

---

## UR-ABM-017 — Multi-Channel Engagement

Users shall coordinate:

* Email
* LinkedIn workflows where supported and authorized
* Ads
* Website personalization
* Events
* Webinars
* Sales calls
* Sales sequences
* Content
* SMS where legally permitted
* CRM tasks

---

## UR-ABM-018 — Sales + Marketing Alignment

The platform shall provide a shared account workspace.

Sales and marketing shall see:

* Account tier
* Account score
* Intent
* Engagement
* Campaigns
* Contacts
* Buying committee
* Opportunities
* Recommended actions
* Account plan

Shared account data and cross-team coordination are core requirements for enterprise ABM. ([Salesforce][4])

---

## UR-ABM-019 — Account Alerts

Users shall receive alerts when:

* Account intent spikes.
* Executive joins.
* Buying committee member engages.
* Pricing page is visited.
* High-value content is consumed.
* Competitor activity is detected.
* Opportunity changes stage.
* Account score changes significantly.
* Strategic initiative is detected.

---

## UR-ABM-020 — Account Recommendations

AI shall recommend:

* Who to contact.
* When to contact.
* Why to contact.
* What to say.
* Which channel to use.
* Which content to send.
* Which sales play to activate.
* Which stakeholder to engage next.

---

## UR-ABM-021 — Human Account Intelligence

Humans shall be able to submit:

* Account insights
* Buyer feedback
* Relationship intelligence
* Competitive information
* Strategic initiatives
* Objections
* Account risks
* Expansion opportunities

---

## UR-ABM-022 — AI + Human Collaboration

Users shall be able to:

* Accept AI recommendations.
* Reject recommendations.
* Modify recommendations.
* Request another recommendation.
* Provide feedback.
* Override account scores.
* Lock strategic account fields.
* Approve AI-generated campaigns.

---

## UR-ABM-023 — Account Expansion

The system shall identify:

* Cross-sell
* Upsell
* New departments
* New geographies
* New business units
* New products
* New buying groups

---

## UR-ABM-024 — Account Retention

For existing customers, the system shall identify:

* Churn signals
* Engagement decline
* Executive departure
* Support issues
* Product adoption decline
* Competitor activity
* Contract expiration

---

## 7. System Requirements

## SR-ABM-001 — Multi-Tenant Architecture

The ABM platform shall provide strict tenant isolation.

Every ABM object shall contain tenant context.

```text
Tenant
 └── Organization
      └── Workplace
           ├── Users
           ├── Accounts
           ├── Contacts
           ├── Campaigns
           ├── Signals
           ├── Account Plans
           └── Opportunities
```

---

## SR-ABM-002 — Identity and Authorization

The system shall enforce:

* RBAC
* Permission-based access
* Tenant-aware authorization
* Resource-level authorization
* Account ownership
* Territory restrictions
* AI permissions
* Approval permissions

---

## SR-ABM-003 — Account Data Platform

The system shall maintain a canonical account record.

The canonical account shall combine:

```text
CRM
+
Lead Intelligence
+
Contact Intelligence
+
Company Intelligence
+
Buyer Intelligence
+
Intent
+
Engagement
+
Competitive Intelligence
+
Campaign Data
+
Opportunity Data
```

---

## SR-ABM-004 — Account Resolution

The system shall resolve duplicate accounts using:

* Domain
* Company name
* Legal name
* Address
* Registration information where available
* CRM identifiers
* External identifiers

---

## SR-ABM-005 — Account Hierarchy

The platform shall support:

```text
Parent Company
 ├── Subsidiary
 ├── Business Unit
 ├── Division
 ├── Department
 └── Regional Entity
```

ABM programs shall operate at any hierarchy level.

---

## SR-ABM-006 — Account Graph

The system shall maintain an account relationship graph:

```text
Account
 ├── People
 ├── Departments
 ├── Technologies
 ├── Competitors
 ├── Opportunities
 ├── Campaigns
 ├── Intent
 ├── Products
 └── Business Units
```

---

## SR-ABM-007 — Event-Driven Architecture

The system shall support events such as:

```text
AccountCreated
AccountUpdated
AccountTierChanged
AccountScoreChanged
IntentDetected
EngagementDetected
BuyingCommitteeUpdated
CampaignStarted
CampaignCompleted
OpportunityCreated
OpportunityAdvanced
CompetitiveThreatDetected
ExpansionOpportunityDetected
ChurnRiskDetected
AIRecommendationGenerated
HumanApprovalRequired
```

---

## SR-ABM-008 — AI Agent Architecture

The system shall support specialized agents:

```text
Account Discovery Agent
ICP Agent
Account Enrichment Agent
Account Scoring Agent
Account Tiering Agent
Account Research Agent
Buying Committee Agent
Intent Detection Agent
Engagement Agent
Account Planning Agent
Personalization Agent
Campaign Agent
Sales Orchestration Agent
Recommendation Agent
Expansion Agent
Retention Agent
Analytics Agent
Attribution Agent
```

---

## SR-ABM-009 — AI Agent Permissions

Each AI agent shall have:

```text
Agent ID
Allowed Tools
Allowed Data
Allowed Tenants
Allowed Actions
Maximum Autonomy
Approval Policy
Model
Prompt Version
Audit Policy
```

---

## SR-ABM-010 — Retrieval-Augmented Generation

AI shall use RAG for:

* Account research
* Account planning
* Personalization
* Competitive analysis
* Sales recommendations
* Content selection

---

## SR-ABM-011 — Knowledge Graph

The platform shall connect:

```text
Account
Contact
Buyer
Opportunity
Competitor
Technology
Intent
Signal
Campaign
Content
Interaction
Revenue
```

---

## SR-ABM-012 — Vector Search

The system shall support semantic retrieval across:

* Account notes
* CRM records
* Call transcripts
* Emails where authorized
* Documents
* Research
* Competitive intelligence
* Customer feedback
* Campaign content

---

## SR-ABM-013 — Hybrid Retrieval

Search shall combine:

```text
Keyword Search
+
Semantic Search
+
Metadata Filtering
+
Knowledge Graph
+
Temporal Search
```

---

## SR-ABM-014 — Temporal Account Intelligence

The system shall maintain account state over time.

```text
Account State T1
      ↓
Account State T2
      ↓
Account State T3
      ↓
Current Account State
```

AI shall identify meaningful changes.

---

## SR-ABM-015 — Data Freshness

Each intelligence attribute shall contain:

* Source
* Collection timestamp
* Last verified timestamp
* Confidence
* Freshness
* Verification status

---

## SR-ABM-016 — Confidence Model

Account intelligence shall contain:

```text
Confidence Score
Source Reliability
Recency
Cross-Source Agreement
Human Validation
```

---

## SR-ABM-017 — AI Hallucination Prevention

AI shall:

* Ground claims in evidence.
* Cite sources where appropriate.
* Separate fact from inference.
* Display uncertainty.
* Avoid unsupported company claims.
* Escalate high-impact uncertainty.

---

## SR-ABM-018 — Human-in-the-Loop

The system shall support:

```text
Automatic
AI Draft
Human Review
Manager Review
Executive Approval
```

Approval requirements shall be configurable per tenant and campaign.

---

## SR-ABM-019 — Workflow Engine

The ABM module shall integrate with SalesGenie's workflow automation engine.

Example:

```text
IF
Account Score > 85
AND
Intent > 80
AND
Buying Committee Coverage < 50%

THEN
Generate Account Plan
+
Identify Missing Stakeholders
+
Create Sales Tasks
+
Trigger Marketing Play
```

---

## SR-ABM-020 — Campaign Orchestration

Campaigns shall support:

* Triggers
* Conditions
* Actions
* Delays
* Branches
* AI decisions
* Human approval
* Exit criteria
* Retry policies
* Rate limits

---

## 8. Functional Requirements

## FR-ABM-001 — Account Import

Users shall import accounts through:

* CSV
* CRM
* API
* Manual entry
* AI discovery
* Saved searches

The system shall validate and deduplicate imported accounts.

---

## FR-ABM-002 — AI Account Discovery

AI shall generate target accounts based on:

```text
ICP
+
TAM
+
Historical Wins
+
Revenue Potential
+
Intent
+
Technology
+
Market Signals
```

---

## FR-ABM-003 — Lookalike Account Discovery

AI shall identify accounts similar to high-performing customers.

Similarity shall consider:

* Industry
* Revenue
* Employees
* Geography
* Technology
* Business model
* Growth
* Buying behavior
* Product adoption

---

## FR-ABM-004 — Account Qualification

The qualification engine shall output:

```text
Fit Score
Intent Score
Engagement Score
Revenue Potential
Strategic Value
Buying Readiness
Overall ABM Score
```

---

## FR-ABM-005 — Account Score

Example:

```text
ABM Score =
0.25 × ICP Fit
+
0.20 × Revenue Potential
+
0.20 × Intent
+
0.15 × Engagement
+
0.10 × Buying Readiness
+
0.10 × Strategic Value
```

Organizations shall be able to customize weighting.

---

## FR-ABM-006 — Dynamic Tiering

The system shall automatically recommend tier changes.

Example:

```text
Tier 3
↓
Intent Spike
↓
High Engagement
↓
New Executive Hire
↓
Open Strategic Initiative
↓
Tier 1 Recommendation
```

Humans may approve, reject, or override tier changes.

---

## FR-ABM-007 — Account Research Agent

The AI research agent shall generate:

```text
Company Overview
Business Model
Strategic Priorities
Financial Signals
Technology
Hiring
Leadership
Products
Competitors
Market Position
Potential Pain Points
Potential Buying Triggers
```

---

## FR-ABM-008 — Account Intelligence Brief

Each strategic account shall have an automatically generated brief.

```text
ACCOUNT
    ↓
Business Overview
    ↓
Strategic Priorities
    ↓
Technology
    ↓
Buying Committee
    ↓
Intent
    ↓
Competitors
    ↓
Pain Points
    ↓
Opportunity
    ↓
Recommended Strategy
```

---

## FR-ABM-009 — Buying Committee Mapping

AI shall identify potential stakeholders and assign:

```text
Role
Influence
Buying Power
Interest
Engagement
Sentiment
Relationship Strength
```

---

## FR-ABM-010 — Buying Committee Gap Analysis

The system shall identify:

```text
Missing Economic Buyer
Missing Technical Buyer
Missing Executive Sponsor
Missing Procurement
Missing Security
Missing User Champion
```

and recommend engagement actions.

---

## FR-ABM-011 — Intent Detection

The system shall detect account-level intent.

Intent shall be classified as:

```text
Low
Moderate
High
Very High
Critical
```

---

## FR-ABM-012 — Intent Spike Detection

The system shall detect abnormal changes:

```text
Baseline Intent = 42
Current Intent = 86

Intent Spike = +44
```

The system shall generate an alert when configurable thresholds are exceeded.

---

## FR-ABM-013 — Account Engagement Score

The platform shall calculate engagement using:

```text
Email
Website
Content
Meetings
Calls
Events
Ads
Social
Sales Activities
```

---

## FR-ABM-014 — Account Engagement Map

Users shall see engagement by:

* Contact
* Department
* Buying role
* Channel
* Campaign
* Time
* Content

---

## FR-ABM-015 — Account Strategy Generation

AI shall generate account strategies containing:

```text
Objective
Target Stakeholders
Business Problem
Value Proposition
Competitive Position
Messaging
Channels
Content
Sales Plays
Marketing Plays
Next Actions
Risks
```

---

## FR-ABM-016 — Personalized Messaging

AI shall generate messaging for:

```text
CEO
CFO
CTO
CIO
CMO
VP Sales
VP Marketing
Procurement
Security
Technical Buyer
End User
```

Messaging shall reflect each role's priorities.

---

## FR-ABM-017 — Dynamic Personalization

Personalization shall adapt based on:

```text
Account
+
Persona
+
Intent
+
Engagement
+
Industry
+
Pain Point
+
Sales Stage
+
Competitive Context
```

---

## FR-ABM-018 — Account Campaign Creation

Users shall create campaigns using:

```text
Campaign Name
Target Accounts
Account Tier
Objective
Channels
Content
Messaging
Schedule
Budget
Approval Workflow
Exit Criteria
```

---

## FR-ABM-019 — AI Campaign Generation

AI shall generate campaign plans based on:

* Account tier
* Account characteristics
* Intent
* Buying stage
* Stakeholders
* Historical performance

---

## FR-ABM-020 — Campaign Orchestration

The system shall coordinate:

```text
Marketing Touch
↓
Sales Touch
↓
Content
↓
Executive Outreach
↓
Event
↓
Follow-Up
```

---

## FR-ABM-021 — Account-Based Sales Sequence

The system shall generate account-specific sequences.

Example:

```text
Day 1:
Executive email

Day 3:
SDR outreach

Day 5:
Relevant case study

Day 7:
Technical stakeholder outreach

Day 10:
Executive follow-up

Day 14:
Account review
```

---

## FR-ABM-022 — AI Next-Best-Action

AI shall calculate the next-best action.

Example:

```text
Recommended Action:
Contact CTO

Reason:
Three technical stakeholders engaged with security content.

Priority:
High

Recommended Channel:
Email + Sales Call

Recommended Content:
Enterprise Security Brief

Confidence:
91%
```

---

## FR-ABM-023 — Human Approval

For high-impact accounts, users shall be able to configure mandatory approval before:

* Campaign launch
* Executive outreach
* High-volume outreach
* Pricing communication
* Sensitive personalization
* Strategic messaging

---

## FR-ABM-024 — Account Alerts

Alerts shall support:

```text
Intent Spike
Executive Engagement
Buying Committee Change
Competitor Activity
New Opportunity
Opportunity Risk
Account Score Change
Tier Change
Expansion Signal
Churn Signal
```

---

## FR-ABM-025 — Slack / Teams Alerts

The system shall send alerts to configured collaboration channels.

---

## FR-ABM-026 — CRM Synchronization

The system shall synchronize:

* Accounts
* Contacts
* Opportunities
* Activities
* Account scores
* Account tiers
* Intent
* Engagement
* Campaigns
* Account plans

---

## FR-ABM-027 — Opportunity Synchronization

When an account enters an opportunity stage, the ABM engine shall automatically update account intelligence.

---

## FR-ABM-028 — Competitive Intelligence Integration

ABM shall consume SalesGenie's Competitive Intelligence module.

```text
Account
↓
Competitor
↓
Competitive Threat
↓
Account Strategy
↓
Sales Play
```

---

## FR-ABM-029 — Lead Intelligence Integration

The ABM engine shall consume:

* Lead discovery
* Lead enrichment
* Lead scoring
* Lead verification
* Lead segmentation
* Lead qualification

---

## FR-ABM-030 — Sales Sequence Integration

ABM shall automatically recommend or activate sales sequences for qualified target accounts.

---

## FR-ABM-031 — Sales Playbook Integration

The system shall recommend account-specific playbooks.

---

## FR-ABM-032 — Account Expansion Engine

For existing customers, AI shall identify:

```text
New Department
+
New Product Need
+
New Geography
+
New Stakeholder
+
New Initiative
=
Expansion Opportunity
```

---

## FR-ABM-033 — Account Churn Detection

The system shall identify:

* Reduced engagement
* Executive departure
* Negative sentiment
* Support escalation
* Competitor engagement
* Product usage decline
* Contract expiration

---

## FR-ABM-034 — ABM Attribution

The platform shall attribute revenue to:

```text
Campaign
Account
Channel
Content
Sales Activity
Marketing Activity
AI Recommendation
Human Activity
```

---

## FR-ABM-035 — Multi-Touch Attribution

The system shall support:

```text
First Touch
Last Touch
Linear
Time Decay
Position Based
Custom
AI-Assisted
```

---

## FR-ABM-036 — Account Revenue Attribution

The system shall calculate:

```text
Pipeline Influenced
Pipeline Sourced
Revenue Influenced
Revenue Sourced
Revenue Accelerated
Expansion Revenue
```

---

## FR-ABM-037 — Account Progression

The system shall track:

```text
Target
↓
Aware
↓
Engaged
↓
Intent
↓
Buying Committee
↓
Meeting
↓
Opportunity
↓
Evaluation
↓
Negotiation
↓
Closed Won
↓
Expansion
```

---

## FR-ABM-038 — Account Health

The platform shall calculate account health using:

```text
Fit
Intent
Engagement
Relationship
Pipeline
Competitive Risk
Buying Committee Coverage
Revenue Potential
```

---

## FR-ABM-039 — Account Risk

The system shall identify:

```text
No Engagement
Weak Champion
Competitor Presence
Missing Executive Sponsor
Low Buying Committee Coverage
Low Intent
Opportunity Stagnation
Negative Sentiment
```

---

## FR-ABM-040 — AI Account Recommendations

AI shall continuously recommend:

```text
Target
Contact
Message
Channel
Content
Campaign
Sales Play
Meeting
Executive Engagement
Expansion
Retention
```

---

## 9. Account-Based Marketing Dashboard

The dashboard shall provide:

## Executive KPIs

```text
Target Accounts
Strategic Accounts
Active ABM Programs
Accounts Engaged
Accounts in Market
Pipeline
Pipeline Influenced
Revenue
Revenue Influenced
Win Rate
Average Deal Size
Sales Cycle
Account Expansion
```

---

## Account Funnel

```text
Target Accounts
      ↓
Engaged Accounts
      ↓
Intent Accounts
      ↓
Meeting Accounts
      ↓
Opportunity Accounts
      ↓
Pipeline Accounts
      ↓
Won Accounts
```

---

## Account Tier Dashboard

```text
Tier 1
Tier 2
Tier 3
Tier 4
Nurture
Disqualified
```

---

## 10. Account Intelligence Workspace

Each account shall provide a unified workspace:

```text
Overview
Intelligence
Contacts
Buying Committee
Intent
Engagement
Campaigns
Activities
Opportunities
Competitors
Technology
Content
Account Plan
AI Recommendations
Tasks
Timeline
Analytics
```

---

## 11. ABM Analytics

The platform shall provide:

## Account-Level Metrics

* Account engagement
* Account score
* Intent
* Buying committee coverage
* Pipeline
* Revenue
* Deal velocity
* Conversion rate

## Campaign Metrics

* Account reach
* Engagement
* Response
* Meetings
* Opportunities
* Pipeline
* Revenue

## Revenue Metrics

* Sourced pipeline
* Influenced pipeline
* Sourced revenue
* Influenced revenue
* Expansion revenue
* ROI

ABM measurement shall roll activity and engagement up to account and revenue outcomes rather than stopping at individual lead metrics. ([Adobe for Business][5])

---

## 12. ABM AI Agents

## 12.1 Account Discovery Agent

Responsibilities:

* Discover accounts
* Identify ICP matches
* Find lookalikes
* Recommend target accounts

---

## 12.2 Account Research Agent

Responsibilities:

* Research company
* Identify strategic initiatives
* Analyze market
* Analyze technology
* Identify business problems

---

## 12.3 Account Scoring Agent

Responsibilities:

* Calculate account fit
* Calculate intent
* Calculate engagement
* Calculate buying readiness
* Calculate revenue potential

---

## 12.4 Buying Committee Agent

Responsibilities:

* Identify stakeholders
* Classify roles
* Estimate influence
* Identify gaps
* Recommend stakeholders

---

## 12.5 Intent Agent

Responsibilities:

* Detect intent
* Detect spikes
* Classify buying stage
* Identify intent sources

---

## 12.6 Personalization Agent

Responsibilities:

* Generate messaging
* Select content
* Adapt value proposition
* Adapt channel strategy

---

## 12.7 Campaign Agent

Responsibilities:

* Build campaigns
* Select channels
* Create workflows
* Optimize campaigns

---

## 12.8 Sales Orchestration Agent

Responsibilities:

* Recommend sales actions
* Trigger sequences
* Create tasks
* Notify sales users

---

## 12.9 Account Strategy Agent

Responsibilities:

* Generate account plans
* Identify risks
* Identify opportunities
* Recommend next actions

---

## 12.10 Attribution Agent

Responsibilities:

* Analyze campaign influence
* Attribute pipeline
* Attribute revenue
* Measure ROI

---

## 13. Human + AI Decision Matrix

| Decision                   |        AI |            Human |
| -------------------------- | --------: | ---------------: |
| Account Discovery          |       Yes |         Optional |
| Account Enrichment         |       Yes |         Optional |
| Account Scoring            |       Yes |         Override |
| Tier Recommendation        |       Yes | Approve/Override |
| Buying Committee Mapping   |       Yes |         Validate |
| Intent Detection           |       Yes |           Review |
| Personalization Draft      |       Yes |          Approve |
| Campaign Draft             |       Yes |          Approve |
| Executive Outreach         | Recommend |          Approve |
| Strategic Messaging        |     Draft |          Approve |
| Account Plan               |     Draft |          Approve |
| Next Best Action           | Recommend | Execute/Override |
| Revenue Attribution        | Calculate |           Review |
| Strategic Account Decision |    Assist |            Human |
| AI Permission Changes      |        No |            Admin |

---

## 14. Workflow Examples

## Workflow 1 — New Strategic Account

```text
Account Discovered
↓
AI Enrichment
↓
ICP Score = 94
↓
Revenue Potential = $1.2M
↓
Intent = High
↓
Tier 1 Recommendation
↓
ABM Manager Approves
↓
AI Researches Account
↓
Buying Committee Identified
↓
Account Plan Generated
↓
Human Approves
↓
Campaign Created
↓
Sales Sequence Activated
```

---

## 15. Workflow 2 — Intent Spike

```text
Account Intent = 42
↓
New Activity Detected
↓
Intent = 91
↓
AI Detects Spike
↓
Account Score Recalculated
↓
Tier 2 → Tier 1 Recommendation
↓
Sales Manager Alerted
↓
AI Identifies 5 Relevant Stakeholders
↓
Next-Best-Action Generated
↓
Sales Rep Notified
```

---

## 16. Workflow 3 — Buying Committee Gap

```text
Account Opportunity
↓
AI Maps Buying Committee
↓
Champion Identified
↓
Technical Buyer Identified
↓
Economic Buyer Missing
↓
AI Generates Recommendation
↓
"Engage CFO"
↓
Recommended Message Generated
↓
Sales Rep Reviews
↓
Human Executes
```

---

## 17. Workflow 4 — Competitive ABM

```text
Target Account
↓
Competitor Detected
↓
Competitive Intelligence Retrieved
↓
Competitor Threat Score = 84
↓
Account Risk Increased
↓
AI Updates Account Plan
↓
Battlecard Retrieved
↓
Recommended Sales Play
↓
Sales + Marketing Coordination
```

---

## 18. Workflow 5 — Expansion ABM

```text
Existing Customer
↓
New Business Unit Detected
↓
AI Identifies Similar Use Case
↓
Expansion Potential = High
↓
New Stakeholders Identified
↓
Expansion Campaign Created
↓
Sales Sequence Activated
↓
Opportunity Created
↓
Revenue Attributed
```

---

## 19. Data Model

Core entities:

```text
Tenant
Organization
Workplace
User
Role
Permission

Account
AccountHierarchy
AccountSegment
AccountTier
AccountScore
AccountPlan
AccountHealth
AccountRisk

Contact
Buyer
BuyingCommittee
StakeholderRelationship

ICP
ICPVersion
TAM
TargetAccountList

IntentSignal
EngagementEvent
AccountSignal

ABMCampaign
CampaignStep
CampaignAudience
CampaignTouch

Content
PersonalizedContent
ContentRecommendation

AccountActivity
SalesActivity
MarketingActivity

Opportunity
Deal
Pipeline

Competitor
CompetitiveThreat
CompetitiveIntelligence

AccountRecommendation
NextBestAction

Attribution
RevenueEvent
PipelineEvent

AIAnalysis
AIRecommendation
HumanReview
AuditEvent
```

---

## 20. Account Data Model

```json
{
  "account_id": "ACC-UUID",
  "tenant_id": "TENANT-UUID",
  "name": "Example Corporation",
  "domain": "example.com",
  "industry": "Technology",
  "employee_count": 5000,
  "annual_revenue": 1000000000,
  "geographies": [],
  "parent_account_id": null,
  "account_tier": "tier_1",
  "icp_fit_score": 94,
  "intent_score": 87,
  "engagement_score": 79,
  "buying_readiness_score": 83,
  "revenue_potential": 1200000,
  "strategic_value_score": 91,
  "overall_abm_score": 89,
  "buying_committee_coverage": 0.72,
  "health": "high",
  "risk": "medium",
  "last_updated_at": "timestamp"
}
```

---

## 21. Account Recommendation Model

```json
{
  "recommendation_id": "REC-UUID",
  "account_id": "ACC-UUID",
  "type": "next_best_action",
  "priority": "high",
  "action": "engage_economic_buyer",
  "reason": "Economic buyer has not been engaged",
  "recommended_channel": "email",
  "recommended_content": "enterprise_roi_brief",
  "expected_impact": "increase_buying_committee_coverage",
  "confidence": 0.91,
  "evidence_ids": [],
  "requires_human_approval": true,
  "status": "pending"
}
```

---

## 22. Permissions

The system shall support permissions including:

```text
abm.view
abm.create
abm.edit
abm.delete

accounts.view
accounts.create
accounts.edit
accounts.delete

accounts.score
accounts.tier
accounts.assign

account_intelligence.view
account_intelligence.generate
account_intelligence.edit

account_plan.view
account_plan.create
account_plan.edit
account_plan.approve

buying_committee.view
buying_committee.manage

intent.view
intent.configure

abm_campaign.view
abm_campaign.create
abm_campaign.edit
abm_campaign.launch
abm_campaign.pause

abm_ai.use
abm_ai.configure
abm_ai.approve

abm_analytics.view
abm_attribution.view

abm_audit.view
```

---

## 23. Security Requirements

The platform shall implement:

* Encryption in transit
* Encryption at rest
* Tenant isolation
* RBAC
* ABAC where required
* API authentication
* API authorization
* Secret management
* Key rotation
* Audit logging
* Rate limiting
* Data retention
* Data deletion
* Secure AI tool access

---

## 24. Privacy Requirements

The system shall:

* Respect tenant data boundaries.
* Apply data minimization.
* Maintain data-source provenance.
* Support deletion workflows.
* Support retention policies.
* Restrict sensitive data access.
* Prevent unauthorized cross-account data exposure.
* Prevent AI agents from accessing unauthorized records.

---

## 25. AI Safety Requirements

AI shall not:

* Invent account facts.
* Fabricate buyer information.
* Invent intent signals.
* Invent customer relationships.
* Claim a stakeholder is a decision-maker without evidence.
* Make unsupported financial claims.
* Generate deceptive communications.
* Circumvent platform permissions.
* Access unauthorized customer data.

AI outputs shall identify uncertainty when evidence is insufficient.

---

## 26. Performance Requirements

Target performance:

```text
Standard account read:
p95 < 300 ms

Account search:
p95 < 1.5 seconds

Account dashboard:
< 2 seconds under normal load

AI account summary:
< 5 seconds

AI next-best-action:
< 5 seconds

Critical intent alert:
< 60 seconds

Batch account enrichment:
Asynchronous and horizontally scalable
```

---

## 27. Scalability Requirements

SalesGenie shall support:

```text
10M+ Users
Millions of Accounts
Hundreds of Millions of Contacts
Billions of Engagement Events
Millions of Campaigns
High-frequency Intent Signals
Large-scale AI Processing
Large Vector Indexes
Large Knowledge Graphs
Multi-region Deployment
```

---

## 28. Reliability Requirements

The system shall support:

```text
99.99% Availability
Automated Retry
Circuit Breaker
Dead Letter Queue
Idempotent Processing
Graceful Degradation
Backpressure
Fault Isolation
Disaster Recovery
Automated Failover
```

---

## 29. Observability

The platform shall monitor:

```text
Account Enrichment Latency
AI Agent Latency
AI Agent Errors
Token Usage
Model Cost
Account Processing Rate
Intent Detection Rate
Campaign Execution Rate
Email Delivery
Workflow Failures
Recommendation Acceptance
Human Override Rate
Attribution Processing
CRM Sync Health
```

---

## 30. AI Quality Metrics

The system shall measure:

## Account Scoring Accuracy

```text
High-Quality Accounts Correctly Identified
/
Total High-Quality Accounts
```

## Recommendation Acceptance

```text
Accepted Recommendations
/
Generated Recommendations
```

## Personalization Quality

```text
Human Approved Personalizations
/
Generated Personalizations
```

## Intent Precision

```text
True High-Intent Accounts
/
Predicted High-Intent Accounts
```

## Account Progression

```text
Accounts Progressing
/
Target Accounts
```

---

## 31. Business KPIs

SalesGenie shall measure:

```text
Target Account Coverage
Account Engagement
Buying Committee Coverage
Intent-to-Meeting Rate
Account-to-Opportunity Rate
Opportunity-to-Win Rate
ABM Pipeline
ABM Revenue
Pipeline Velocity
Sales Cycle
Average Contract Value
Customer Acquisition Cost
Revenue per Target Account
Expansion Revenue
Retention Rate
ABM ROI
```

---

## 32. Revenue Attribution

The platform shall support:

```text
Account-Sourced Revenue
Account-Influenced Revenue
Campaign-Sourced Revenue
Campaign-Influenced Revenue
Sales-Sourced Revenue
Marketing-Sourced Revenue
AI-Influenced Revenue
Expansion Revenue
```

---

## 33. ABM ROI

The platform shall calculate:

```text
ABM ROI =
(ABM-Attributed Revenue - ABM Program Cost)
/
ABM Program Cost
```

The system shall allow organizations to configure attribution methodology.

---

## 34. Account Progression Model

```text
IDENTIFIED
    ↓
QUALIFIED
    ↓
TARGETED
    ↓
AWARE
    ↓
ENGAGED
    ↓
INTENT
    ↓
BUYING COMMITTEE
    ↓
MEETING
    ↓
OPPORTUNITY
    ↓
EVALUATION
    ↓
NEGOTIATION
    ↓
CLOSED WON
    ↓
EXPANSION
```

The system shall support configurable lifecycle stages.

---

## 35. ABM Dashboard Requirements

## Executive Dashboard

```text
Total Target Accounts
Tier 1 Accounts
High Intent Accounts
Active Opportunities
ABM Pipeline
ABM Revenue
Pipeline Velocity
Win Rate
Revenue Influenced
ABM ROI
```

---

## ABM Manager Dashboard

```text
Accounts Requiring Attention
Intent Spikes
Tier Changes
Buying Committee Gaps
Campaign Performance
Account Progression
AI Recommendations
Human Review Queue
```

---

## Sales Dashboard

```text
My Strategic Accounts
Hot Accounts
Intent Spikes
Open Opportunities
Buying Committee Gaps
Competitive Threats
Next Best Actions
```

---

## Marketing Dashboard

```text
Target Account Reach
Account Engagement
Campaign Performance
Content Performance
Intent
Account Progression
Pipeline Influence
Revenue Influence
```

---

## 36. Account Command Center

The Account Command Center shall function as a single source of truth.

Sections:

```text
Overview
AI Summary
Account Score
Account Tier
Intent
Engagement
Buying Committee
Contacts
Account Plan
Campaigns
Content
Activities
Opportunities
Competitors
Technology
Risks
Expansion
Recommendations
Timeline
Analytics
Audit
```

---

## 37. Account Intelligence Timeline

The timeline shall display:

```text
Company Event
↓
Intent Signal
↓
Website Engagement
↓
Content Engagement
↓
Stakeholder Activity
↓
Sales Activity
↓
Marketing Activity
↓
Meeting
↓
Opportunity
↓
Competitive Event
↓
Revenue Event
```

---

## 38. AI Next-Best-Action Engine

The AI shall evaluate:

```text
Account State
+
Buyer State
+
Intent
+
Engagement
+
Opportunity
+
Competitive Context
+
Historical Outcomes
```

and produce:

```text
Next Best Action
Recommended Owner
Recommended Channel
Recommended Message
Recommended Content
Priority
Expected Impact
Confidence
```

---

## 39. Closed-Loop Learning

The ABM engine shall learn from:

```text
Recommendation
↓
Human Decision
↓
Action
↓
Buyer Response
↓
Opportunity Progression
↓
Revenue Outcome
```

The system shall use outcomes to improve:

* Account scoring
* Intent scoring
* Recommendations
* Personalization
* Tiering
* Campaign optimization

---

## 40. AI Autonomy Levels

Organizations shall configure AI autonomy.

## Level 0 — Assistive

```text
AI analyzes
Human decides
```

## Level 1 — Recommend

```text
AI recommends
Human approves
```

## Level 2 — Supervised Automation

```text
AI executes low-risk actions
Human reviews
```

## Level 3 — Conditional Automation

```text
AI executes predefined workflows
Human escalation for exceptions
```

## Level 4 — Autonomous ABM

```text
AI detects
→ plans
→ executes
→ monitors
→ escalates
```

High-risk actions shall remain subject to configurable human approval.

---

## 41. Enterprise ABM Governance

The system shall support:

* ABM program ownership
* Campaign approval
* Account ownership
* Territory governance
* Budget governance
* AI governance
* Content governance
* Messaging governance
* Data governance
* Attribution governance

---

## 42. FAANG-Level Product Principles

## Principle 1 — Account as a Living Object

The account shall continuously evolve as new signals arrive.

---

## Principle 2 — Fit + Timing

A high-fit account shall not automatically become a high-priority account.

The system shall evaluate:

```text
Fit
+
Intent
+
Engagement
+
Buying Readiness
```

---

## Principle 3 — Buying Group Coverage

ABM shall optimize for buying-committee coverage rather than relying on one contact.

Enterprise ABM commonly involves multiple stakeholders and requires coordinated engagement across the buying group. ([Abmatic AI][6])

---

## Principle 4 — Sales + Marketing as One System

Marketing and sales shall operate from the same account intelligence layer.

---

## Principle 5 — Personalization With Evidence

Personalization shall be based on verified account information.

---

## Principle 6 — AI as Execution Layer

AI shall scale account research, scoring, personalization, and orchestration while humans control strategic decisions.

---

## Principle 7 — Revenue Over Activity

The ultimate optimization target shall be:

```text
Revenue
Pipeline
Velocity
Win Rate
Expansion
Retention
```

rather than raw activity.

---

## 43. End-to-End FAANG-Level ABM Architecture

```text
                    SALES GENIE ABM
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
     DATA LAYER        INTELLIGENCE       EXECUTION
        │                  │                  │
        ▼                  ▼                  ▼
   CRM Data          Account AI          Campaigns
   Contact Data      ICP Engine           Sequences
   Lead Data         Scoring              Workflows
   Web Signals       Intent               Content
   Engagement        Buying Group         Email
   Product Data      Research             Ads
   Market Data       Recommendations      Sales
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ▼
                  ACCOUNT GRAPH
                           │
                           ▼
                  ACCOUNT COMMAND CENTER
                           │
                           ▼
                  REVENUE INTELLIGENCE
                           │
                           ▼
                     ATTRIBUTION
                           │
                           ▼
                    AI LEARNING LOOP
```

---

## 44. End-to-End Example

```text
SalesGenie discovers 100,000 companies
                    ↓
AI identifies 12,000 ICP-fit accounts
                    ↓
Revenue model identifies 2,000 high-value accounts
                    ↓
Intent engine identifies 350 active accounts
                    ↓
Engagement engine identifies 120 highly engaged accounts
                    ↓
AI identifies 50 strategic Tier-1 accounts
                    ↓
Buying Committee Agent maps stakeholders
                    ↓
Account Research Agent creates intelligence
                    ↓
Competitive Intelligence identifies active competitors
                    ↓
Account Strategy Agent creates account plans
                    ↓
Human ABM Manager approves strategy
                    ↓
Personalization Agent creates stakeholder-specific messaging
                    ↓
Campaign Agent orchestrates multi-channel engagement
                    ↓
Sales Agent receives next-best actions
                    ↓
Marketing and Sales operate from shared account workspace
                    ↓
Accounts progress into opportunities
                    ↓
Opportunity intelligence feeds back into ABM
                    ↓
Revenue attribution measures impact
                    ↓
AI learns which strategies produce revenue
                    ↓
Account scoring improves
```

---

## 45. Acceptance Criteria

The ABM module shall be production-ready when:

* Users can define ICPs.
* AI can infer ICP characteristics.
* Accounts can be discovered.
* Accounts can be enriched.
* Accounts can be deduplicated.
* Account hierarchies are supported.
* Accounts can be scored.
* Accounts can be tiered.
* Target account lists can be created.
* Dynamic account lists are supported.
* Account intelligence can be generated.
* Buying committees can be mapped.
* Buying committee gaps can be detected.
* Intent can be detected.
* Intent spikes can be detected.
* Account engagement can be calculated.
* Account timelines can be generated.
* Account plans can be generated.
* AI recommendations can be generated.
* Human users can approve recommendations.
* Human users can override AI.
* Personalized messaging can be generated.
* Account-based campaigns can be created.
* Multi-channel workflows can be orchestrated.
* Sales sequences can be integrated.
* Sales playbooks can be integrated.
* Competitive intelligence can be integrated.
* Lead intelligence can be integrated.
* Opportunities can be linked to accounts.
* Expansion opportunities can be detected.
* Churn risks can be detected.
* Account alerts can be generated.
* CRM synchronization works.
* Revenue attribution works.
* ABM ROI can be calculated.
* Account progression can be measured.
* AI agent actions are audited.
* Human actions are audited.
* Tenant isolation is enforced.
* RBAC is enforced.
* AI permissions are enforced.
* Sensitive actions support human approval.
* Account data is source-aware.
* AI outputs are evidence-grounded.
* Account dashboards work.
* Executive dashboards work.
* Sales dashboards work.
* Marketing dashboards work.
* AI quality metrics are measurable.
* Business outcomes can be measured.

---

## 46. Definition of Done

An ABM capability shall not be considered complete merely because it can:

```text
Find accounts
```

or:

```text
Send personalized emails
```

It shall be considered complete when SalesGenie supports the complete lifecycle:

```text
IDENTIFY
   ↓
QUALIFY
   ↓
SCORE
   ↓
TIER
   ↓
RESEARCH
   ↓
MAP BUYING GROUP
   ↓
DETECT INTENT
   ↓
CREATE ACCOUNT STRATEGY
   ↓
PERSONALIZE
   ↓
ORCHESTRATE
   ↓
ENGAGE
   ↓
CREATE OPPORTUNITY
   ↓
ACCELERATE DEAL
   ↓
CLOSE
   ↓
EXPAND
   ↓
ATTRIBUTE REVENUE
   ↓
LEARN
   ↓
OPTIMIZE
```

---

## 47. Final Product Capability

SalesGenie's Account-Based Marketing module shall ultimately operate as an:

> **AI-powered, human-governed, account-centric revenue orchestration system that continuously identifies the highest-value accounts, understands their business context and buying committees, detects when they are ready to engage, creates personalized strategies, coordinates sales and marketing execution, and measures the resulting pipeline and revenue impact.**

The final system shall connect ABM intelligence directly to:

```text
Account Management
Lead Discovery
Lead Enrichment
Lead Qualification
Lead Scoring
Lead Segmentation
Lead Routing
Contact Management
Buyer Intelligence
Company Intelligence
Prospect Intelligence
Intent Detection
Buying Signal Detection
Competitive Intelligence
Sales Sequences
Outreach Automation
Sales Playbooks
Sales Workflows
Opportunity Management
Deal Management
Sales Forecasting
Sales Analytics
Customer Success
Expansion
Retention
Revenue Attribution
```

The strategic objective is:

```text
RIGHT ACCOUNT
      +
RIGHT BUYING GROUP
      +
RIGHT SIGNAL
      +
RIGHT MESSAGE
      +
RIGHT CHANNEL
      +
RIGHT TIME
      +
RIGHT SALES ACTION
      =
MAXIMUM REVENUE IMPACT
```
