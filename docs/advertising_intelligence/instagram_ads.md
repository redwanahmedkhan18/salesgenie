# SalesGenie — AI-Powered Instagram Ads Platform

## User Requirements, System Requirements & Functional Requirements

**Document Type:** Enterprise Product & Engineering Requirements  
**Module:** AI-Based Instagram Ads  
**Project:** SalesGenie  
**Architecture:** Multi-Tenant Enterprise SaaS + Microservices + Event-Driven + Multi-Agent AI  
**Operating Model:** AI-Assisted + Human-Controlled + Human-in-the-Loop + Controlled Autonomous  
**Primary Platform:** Instagram / Meta Advertising Ecosystem  
**Requirement Level:** FAANG-Level / Production-Grade

---

## 1. Module Overview

The Instagram Ads module shall provide SalesGenie with an enterprise-grade AI advertising platform capable of planning, generating, launching, monitoring, optimizing, analyzing, and automating Instagram advertising campaigns.

The platform shall support:

- AI campaign planning
- AI audience discovery
- AI audience segmentation
- AI creative generation
- AI copy generation
- AI Reel concepts
- AI Story concepts
- AI carousel concepts
- AI image/video creative recommendations
- AI budget optimization
- AI bid strategy recommendations
- AI placement optimization
- AI campaign optimization
- AI performance prediction
- AI anomaly detection
- AI creative fatigue detection
- AI audience saturation detection
- Human campaign management
- Human approvals
- Human overrides
- Human creative editing
- Human budget control
- Instagram professional-account integration
- Meta advertising account integration
- Instagram content intelligence
- Instagram engagement intelligence
- Lead generation
- Instagram Direct/Messaging campaign support where supported
- Conversion tracking
- CRM synchronization
- Attribution
- ROAS/ROI analysis
- Revenue attribution
- Profitability analysis
- A/B testing
- Automated experimentation
- Campaign automation
- Closed-loop marketing optimization

The module shall integrate with SalesGenie's broader intelligence ecosystem:

```text
ICP Engine
Persona Engine
Customer Persona
Audience Management
Audience Segmentation
Lead Intelligence
Lead Generation
Lead Recommendation
Buying Signal Detection
Intent Detection
Competitive Intelligence
Marketing Strategy
Marketing Campaigns
Campaign Automation
Content Marketing
Social Media Marketing
Email Marketing
Marketing Analytics
Marketing ROI
Marketing Budget Optimization
AI Marketing Agent
AI Campaign Agent
AI Content Agent
AI Social Media Agent
AI Advertising Agent
AI Audience Agent
AI Marketing Analytics Agent
AI Marketing Strategy Agent
AI Marketing Workflow Builder
Marketing Agent Orchestration
CRM
Sales Intelligence
Financial Analytics
Business Intelligence
Profitability Intelligence
```

---

## 2. Product Goals

The Instagram Ads module shall:

1. Reduce the time required to create Instagram advertising campaigns.
2. Allow non-technical users to launch sophisticated campaigns.
3. Give professional marketers granular campaign control.
4. Use AI to transform business objectives into advertising strategies.
5. Generate Instagram-native creative concepts.
6. Optimize campaigns according to business outcomes.
7. Minimize wasted advertising expenditure.
8. Maximize qualified leads.
9. Maximize conversions.
10. Maximize profitable revenue.
11. Improve ROAS and ROI.
12. Detect campaign problems automatically.
13. Detect creative fatigue automatically.
14. Detect audience saturation automatically.
15. Connect Instagram advertising to SalesGenie CRM.
16. Connect advertising activity to qualified leads and revenue.
17. Provide explainable AI recommendations.
18. Provide human approval and override capabilities.
19. Support controlled autonomous optimization.
20. Maintain complete auditability.
21. Support enterprise multi-tenancy.
22. Support multiple Meta advertising accounts.
23. Create a closed-loop advertising intelligence system.

---

## 3. User Roles

## 3.1 Super Admin

The Super Admin shall be able to:

* Manage platform-wide Instagram advertising capabilities.
* Configure Meta integration policies.
* Configure advertising policies.
* Configure AI policies.
* Configure AI execution limits.
* Configure tenant-level advertising limits.
* Monitor advertising activity across tenants.
* Monitor API usage.
* Monitor advertising-related security events.
* Review audit logs.
* Suspend abusive advertising activity.
* Configure global feature flags.
* Configure platform-level AI guardrails.
* Configure platform-level compliance rules.

---

## 3.2 Workplace Admin

The Workplace Admin shall be able to:

* Manage advertising access for a workplace.
* Configure workplace advertising policies.
* Assign advertising permissions.
* Manage marketing teams.
* Review advertising activity.
* Review campaign budgets.
* Review AI actions.
* Configure campaign approval policies.

---

## 3.3 Organization Admin

The Organization Admin shall be able to:

* Connect Meta Business assets.
* Connect Instagram professional accounts.
* Connect Meta advertising accounts.
* Configure advertising permissions.
* Configure campaign budgets.
* Configure approval workflows.
* Configure AI automation.
* Configure autonomous execution limits.
* Review campaign performance.
* Approve high-risk AI actions.
* Manage advertising teams.

---

## 3.4 Marketing Manager

The Marketing Manager shall be able to:

* Create campaigns.
* Create ad sets.
* Create ads.
* Generate AI campaign strategies.
* Generate AI creatives.
* Generate Instagram captions.
* Generate Reel concepts.
* Generate Story concepts.
* Generate carousel concepts.
* Configure audiences.
* Configure budgets.
* Configure placements.
* Launch campaigns.
* Pause campaigns.
* Duplicate campaigns.
* Run experiments.
* Review AI recommendations.
* Approve AI actions.
* Configure automation.

---

## 3.5 Marketing Analyst

The Marketing Analyst shall be able to:

* Analyze campaign performance.
* Analyze audience performance.
* Analyze creative performance.
* Analyze Instagram engagement.
* Analyze conversions.
* Analyze ROAS.
* Analyze ROI.
* Analyze CPL.
* Analyze CPA.
* Analyze CAC.
* Analyze revenue.
* Analyze profit.
* Detect anomalies.
* Compare campaigns.
* Generate reports.
* Evaluate AI recommendations.

---

## 3.6 Sales Agent

The Sales Agent shall be able to:

* View Instagram-generated leads.
* View campaign attribution.
* View ad attribution.
* View audience information.
* View lead quality.
* Follow up with leads.
* Update CRM records.
* Qualify leads.
* Mark leads as converted or lost.
* Provide lead-quality feedback to AI.

---

## 3.7 Support Agent

The Support Agent shall be able to:

* View authorized advertising integration status.
* Assist users with Instagram advertising issues.
* View synchronization failures.
* View campaign errors.
* Escalate technical issues.

---

## 3.8 End User / Client

The End User shall be able to:

* Connect Instagram/Meta assets.
* Create campaigns.
* Generate AI campaigns.
* Create audiences.
* Generate creatives.
* Configure budgets.
* Review AI recommendations.
* Approve campaigns.
* Launch campaigns.
* Monitor campaign performance.
* Pause campaigns.
* Configure automation.
* View analytics.
* Export reports.

---

## 4. User Requirements

## UR-IG-001 — Instagram Account Connection

The user shall be able to securely connect an eligible Instagram professional account.

The system shall support discovery and management of available authorized Instagram assets.

---

## UR-IG-002 — Meta Advertising Account Connection

The user shall be able to connect an authorized Meta advertising account.

The system shall display:

* Ad account
* Business account
* Associated Instagram assets
* Facebook assets where applicable
* Available tracking assets
* Available campaign assets

---

## UR-IG-003 — Advertising Workspace

The system shall provide a centralized Instagram Ads workspace containing:

* Campaigns
* Ad sets
* Ads
* Creatives
* Audiences
* Budgets
* Recommendations
* Experiments
* Automations
* Analytics
* Attribution
* Reports
* Alerts
* Audit logs

---

## UR-IG-004 — AI Campaign Creation

The user shall be able to describe a campaign using natural language.

Example:

```text
Create an Instagram campaign for our AI customer-support SaaS.
Target B2B SaaS companies in the United States.
Generate qualified demo leads with a $5,000 monthly budget.
```

The AI shall generate:

* Campaign objective
* Audience strategy
* Persona
* Messaging strategy
* Creative strategy
* Reel concepts
* Story concepts
* Carousel concepts
* CTA
* Budget recommendation
* Testing strategy
* Measurement strategy

---

## UR-IG-005 — Human Campaign Creation

Users shall be able to manually configure campaigns without AI.

AI assistance shall remain optional.

---

## UR-IG-006 — AI + Human Collaboration

The platform shall support:

### AI Assist

AI recommends actions.

### Human-in-the-Loop

AI proposes actions and humans approve them.

### Controlled Autonomous

AI executes predefined actions within strict policies.

### Human Only

AI automation can be completely disabled.

---

## UR-IG-007 — Campaign Objectives

The system shall map business objectives to supported Instagram/Meta advertising objectives.

Supported business goals shall include:

* Awareness
* Reach
* Traffic
* Engagement
* Leads
* Messaging
* App promotion
* Sales
* Conversions
* Retargeting

---

## UR-IG-008 — Instagram-Native Creative Strategy

AI shall distinguish between:

* Feed advertisements
* Story advertisements
* Reel advertisements
* Carousel advertisements
* Video advertisements
* Image advertisements
* Messaging-oriented advertisements

AI shall recommend the appropriate creative format based on campaign objective and audience behavior.

---

## UR-IG-009 — AI Audience Recommendation

AI shall recommend audiences using:

```text
ICP
+
Persona
+
Customer Data
+
Intent
+
Buying Signals
+
Historical Campaigns
+
CRM Outcomes
+
Engagement
+
Conversion Data
+
Revenue Data
```

---

## UR-IG-010 — Audience Segmentation

The system shall support segmentation based on:

* Demographics
* Geography
* Industry
* Job role
* Company size
* Customer lifecycle
* Funnel stage
* Engagement
* Intent
* Buying signals
* Customer value
* Previous interactions

---

## UR-IG-011 — Custom Audience Strategy

The system shall support authorized audience sources including:

* Customer lists
* Website activity
* Lead activity
* Engagement activity
* CRM data
* Previous campaign interactions
* Conversion events

---

## UR-IG-012 — Lookalike Audience Strategy

The AI shall recommend seed populations based on:

* Customers
* High-value customers
* Qualified leads
* Converted leads
* Revenue cohorts
* High-LTV customers

---

## UR-IG-013 — Retargeting

The platform shall support retargeting strategies based on:

* Website visitors
* Product viewers
* Pricing-page visitors
* Instagram engagement
* Video viewers
* Lead-form interaction
* Previous campaign engagement
* CRM activity
* Abandoned conversion journeys

---

## UR-IG-014 — Audience Exclusion

Users shall be able to exclude:

* Existing customers
* Converted leads
* Employees
* Disqualified leads
* Competitors
* Low-value users
* Previously converted audiences
* Specific regions
* Specific audience segments

---

## 5. AI Creative Requirements

## UR-IG-015 — AI Instagram Copy Generation

AI shall generate:

* Primary text
* Headlines
* Captions
* CTAs
* Hooks
* Value propositions
* Benefit statements
* Social proof variants
* Urgency variants
* Educational variants
* Promotional variants

---

## UR-IG-016 — AI Hook Generation

AI shall generate multiple hooks for testing.

Example:

```text
Hook A:
"Your support team shouldn't spend hours answering the same questions."

Hook B:
"Turn customer conversations into automated revenue."

Hook C:
"What if your support team could handle 10x more conversations?"
```

---

## UR-IG-017 — AI Reel Generation

AI shall generate:

* Reel concepts
* Scripts
* Hooks
* Scene structures
* Voiceover scripts
* CTA
* On-screen text
* B-roll suggestions
* Editing instructions
* Duration recommendations

---

## UR-IG-018 — AI Story Generation

AI shall generate:

* Story sequences
* Story hooks
* Poll concepts
* Question concepts
* CTA sequences
* Promotional sequences
* Lead-generation sequences
* Retargeting sequences

---

## UR-IG-019 — AI Carousel Generation

AI shall generate:

* Slide structure
* Slide headlines
* Slide descriptions
* Visual concepts
* CTA
* Storytelling sequence

Example:

```text
Slide 1 → Problem
Slide 2 → Why it happens
Slide 3 → Cost of the problem
Slide 4 → Solution
Slide 5 → Product
Slide 6 → Proof
Slide 7 → CTA
```

---

## UR-IG-020 — Creative Personalization

AI shall personalize creative according to:

* Persona
* Industry
* Geography
* Funnel stage
* Pain point
* Customer maturity
* Product
* Campaign objective
* Audience segment

---

## UR-IG-021 — Human Creative Editing

Humans shall be able to edit:

* Copy
* Captions
* Hooks
* Images
* Videos
* Reels
* Stories
* Carousels
* CTA
* Landing pages

AI shall not overwrite human-approved content without authorization.

---

## UR-IG-022 — Creative Approval

Organizations shall be able to require approval before:

* Publishing
* Launching
* Replacing creatives
* Increasing budgets
* Expanding audiences
* Activating automation

---

## 6. Budget Requirements

## UR-IG-023 — Budget Configuration

Users shall be able to configure:

* Daily budget
* Lifetime budget
* Campaign budget
* Ad-set budget
* Monthly budget
* Maximum spend
* Maximum automated increase
* Maximum automated decrease

---

## UR-IG-024 — AI Budget Recommendation

AI shall recommend budgets using:

* Historical ROAS
* CPL
* CPA
* Conversion rate
* Revenue
* Profit
* Customer value
* Audience size
* Campaign maturity
* Creative performance
* Business objective

---

## UR-IG-025 — Budget Reallocation

AI shall recommend reallocating budget from:

```text
Low-performing campaigns
        ↓
High-performing campaigns
```

Autonomous execution shall require explicit permission.

---

## UR-IG-026 — Budget Safety

The system shall enforce:

* Daily spend limits
* Monthly spend limits
* Tenant limits
* Campaign limits
* AI execution limits
* Emergency stop thresholds

---

## 7. Instagram Creative Intelligence

## UR-IG-027 — Creative Performance Analysis

The system shall compare:

* Image vs video
* Reel vs Story
* Carousel vs single image
* Hook performance
* Caption performance
* CTA performance
* Creative theme
* Creative length
* Visual style

---

## UR-IG-028 — Creative Fatigue Detection

AI shall detect:

* Rising frequency
* Falling CTR
* Falling engagement
* Falling conversion rate
* Increasing CPL
* Increasing CPA

and recommend creative refreshes.

---

## UR-IG-029 — Creative Winner Detection

AI shall identify winning:

* Hooks
* Headlines
* Visual concepts
* Reels
* Stories
* Carousels
* CTAs
* Messaging styles

---

## UR-IG-030 — Creative Variant Generation

When a creative performs well, AI shall generate controlled variants.

Example:

```text
Winning Creative
       ↓
Hook Variant
       ↓
Visual Variant
       ↓
CTA Variant
       ↓
Persona Variant
       ↓
New Experiment
```

---

## 8. Instagram Campaign Analytics

## UR-IG-031 — Campaign Metrics

The system shall track available campaign metrics including:

* Impressions
* Reach
* Frequency
* Clicks
* CTR
* CPC
* CPM
* Spend
* Leads
* CPL
* Conversions
* CPA
* Revenue
* ROAS
* ROI
* CAC
* Profit

---

## UR-IG-032 — Instagram Engagement Analytics

The system shall analyze applicable:

* Likes
* Comments
* Shares
* Saves
* Video views
* Video completion
* Profile interactions
* Engagement rate

---

## UR-IG-033 — Reel Analytics

The system shall analyze applicable Reel performance including:

* Views
* Watch behavior
* Engagement
* Shares
* Saves
* Click-through behavior
* Conversion performance

---

## UR-IG-034 — Story Analytics

The system shall analyze applicable Story performance including:

* Reach
* Views
* Exits
* Interactions
* Link interactions
* Conversion behavior

---

## UR-IG-035 — Carousel Analytics

The system shall analyze:

* Carousel engagement
* Slide performance where available
* CTR
* Conversion
* Saves
* Shares

---

## 9. AI Performance Intelligence

## UR-IG-036 — AI Campaign Diagnosis

AI shall answer:

* Why is the campaign performing well?
* Why is it underperforming?
* Which audience is responsible?
* Which creative is responsible?
* Which placement is responsible?
* Should budget increase?
* Should budget decrease?
* Should creative be replaced?
* Should targeting change?

---

## UR-IG-037 — AI Recommendation

Every recommendation shall contain:

```text
Recommendation
Reason
Evidence
Confidence
Expected Impact
Risk
Required Approval
```

---

## UR-IG-038 — Explainable AI

Example:

```text
Recommendation:
Increase Campaign A budget by 15%.

Evidence:
- ROAS is 34% above account median.
- Qualified-lead rate is 21% above baseline.
- Creative fatigue is low.
- Audience saturation is below threshold.

Confidence:
88%

Expected impact:
+10–17% qualified leads.

Risk:
Medium.

Approval:
Required.
```

---

## UR-IG-039 — Anomaly Detection

AI shall detect:

* Spend spikes
* CPM spikes
* CPC spikes
* CTR drops
* Conversion drops
* CPL spikes
* CPA spikes
* ROAS collapse
* Tracking failures
* Audience-size anomalies
* Lead-quality anomalies

---

## UR-IG-040 — Root Cause Analysis

AI shall estimate the contribution of potential causes.

Example:

```text
ROAS decreased by 29%.

Potential causes:

Creative fatigue        41%
Audience saturation     27%
CPM increase            19%
Landing-page decline    13%
```

---

## 10. Campaign Automation

## UR-IG-041 — Automation Rules

Users shall create rules such as:

```text
IF ROAS < 1.5
FOR 24 HOURS
THEN recommend budget reduction
```

```text
IF CPL > target CPL by 30%
THEN recommend pausing weak creatives
```

```text
IF ROAS > target ROAS by 25%
THEN recommend budget increase
```

---

## UR-IG-042 — Autonomous Optimization

When explicitly enabled, AI may:

* Pause advertisements
* Adjust budgets
* Reallocate budgets
* Rotate creatives
* Recommend audience expansion
* Launch pre-approved creative variants
* Modify predefined campaign parameters

All actions shall respect organizational policies.

---

## UR-IG-043 — Emergency Kill Switch

Users shall be able to:

* Pause all Instagram campaigns
* Pause selected campaigns
* Disable AI automation
* Disable budget automation
* Disable creative automation

---

## 11. Experimentation

## UR-IG-044 — A/B Testing

The system shall support:

* Hook tests
* Creative tests
* Reel tests
* Story tests
* Carousel tests
* Audience tests
* CTA tests
* Landing-page tests
* Budget tests

---

## UR-IG-045 — AI Experiment Designer

AI shall:

1. Identify performance uncertainty.
2. Generate a hypothesis.
3. Select variables.
4. Generate variants.
5. Recommend traffic allocation.
6. Estimate sample requirements.
7. Monitor results.
8. Evaluate statistical evidence.
9. Recommend a winner.
10. Feed results back into the AI learning system.

---

## 12. Lead Generation Requirements

## UR-IG-046 — Instagram Lead Capture

The system shall support authorized Instagram/Meta lead-generation mechanisms applicable to the selected campaign configuration.

---

## UR-IG-047 — Lead Attribution

Every advertising lead shall preserve:

```text
Campaign ID
Ad Set ID
Ad ID
Creative ID
Audience
Placement
Timestamp
Source
Medium
Campaign Metadata
Conversion Event
```

---

## UR-IG-048 — CRM Synchronization

Instagram-generated leads shall synchronize with SalesGenie's CRM.

The system shall support:

* Lead creation
* Lead enrichment
* Lead scoring
* Lead assignment
* Lead status updates
* Qualification
* Conversion tracking
* Revenue attribution

---

## UR-IG-049 — Lead Quality Feedback

Sales agents shall classify leads as:

```text
High Quality
Medium Quality
Low Quality
Qualified
Disqualified
Converted
Lost
```

AI shall use this feedback for future optimization.

---

## 13. Instagram Messaging Advertising

## UR-IG-050 — Messaging Campaign Support

Where supported by the connected Meta configuration, the platform shall support advertising flows that initiate or route conversations through Instagram messaging.

---

## UR-IG-051 — AI Conversation Integration

Advertising-generated conversations shall be integrated with SalesGenie's:

* AI Customer Support
* AI Sales Agent
* Conversation Engine
* Lead Intelligence
* CRM
* Human Support

---

## UR-IG-052 — AI-to-Human Handoff

The system shall support:

```text
Instagram Ad
     ↓
Instagram Conversation
     ↓
AI Sales Agent
     ↓
Lead Qualification
     ↓
Human Sales Agent
     ↓
CRM
     ↓
Opportunity
```

---

## 14. Attribution Requirements

## UR-IG-053 — Attribution

The platform shall support:

* First-touch attribution
* Last-touch attribution
* Multi-touch attribution
* Campaign attribution
* Ad-set attribution
* Ad attribution
* Creative attribution

---

## UR-IG-054 — Revenue Attribution

The system shall connect:

```text
Instagram Ad
      ↓
Lead
      ↓
Qualified Lead
      ↓
Opportunity
      ↓
Customer
      ↓
Revenue
      ↓
Profit
```

---

## UR-IG-055 — Profitability Optimization

AI shall optimize toward:

```text
Qualified Revenue
+
Profit
+
Customer Lifetime Value
```

instead of optimizing exclusively for:

```text
Likes
Clicks
Views
Impressions
```

---

## 15. AI Instagram Advertising Agent

## AI-IG-001

The AI Advertising Agent shall understand natural-language advertising objectives.

## AI-IG-002

The agent shall retrieve relevant SalesGenie intelligence before making recommendations.

## AI-IG-003

The agent shall use:

* ICP
* Persona
* Audience
* Intent
* Buying signals
* Customer history
* Campaign history
* CRM outcomes
* Revenue
* Profitability

## AI-IG-004

The agent shall distinguish:

```text
Observed Facts
Predictions
Recommendations
Assumptions
```

## AI-IG-005

The agent shall not represent predictions as guaranteed results.

## AI-IG-006

The agent shall explain recommendations.

## AI-IG-007

The agent shall expose confidence.

## AI-IG-008

The agent shall expose evidence.

## AI-IG-009

The agent shall expose risk.

## AI-IG-010

The agent shall respect organizational policies.

## AI-IG-011

The agent shall respect budget limits.

## AI-IG-012

The agent shall request human approval for high-risk actions.

## AI-IG-013

The agent shall maintain an action history.

## AI-IG-014

The agent shall learn from:

* Campaign outcomes
* Human approvals
* Human rejections
* Human modifications
* Sales outcomes
* Conversion outcomes
* Revenue outcomes

---

## 16. System Requirements

## SR-IG-001 — Architecture

The Instagram Ads module shall use an enterprise microservices architecture.

Recommended architecture:

```text
Frontend
   ↓
API Gateway
   ↓
Instagram Advertising Service
   ├── Meta Integration Service
   ├── Instagram Asset Service
   ├── Campaign Service
   ├── Ad Set Service
   ├── Ad Service
   ├── Creative Service
   ├── Audience Service
   ├── Budget Service
   ├── Optimization Service
   ├── Analytics Service
   ├── Attribution Service
   ├── Experiment Service
   ├── Automation Service
   ├── Lead Integration Service
   └── AI Advertising Agent
```

---

## SR-IG-002 — API Gateway

The API Gateway shall provide:

* Authentication
* Authorization
* Tenant resolution
* Rate limiting
* Request validation
* API versioning
* Audit logging
* Request tracing

---

## SR-IG-003 — Meta Integration Layer

The integration layer shall isolate Meta-specific implementation from SalesGenie business logic.

It shall support:

* Authentication
* Account discovery
* Asset discovery
* Campaign management
* Ad-set management
* Ad management
* Audience management
* Insights retrieval
* Conversion integration
* Webhooks where applicable

---

## SR-IG-004 — Adapter Architecture

SalesGenie shall implement a provider adapter abstraction:

```text
AdvertisingProvider
       |
       +── MetaProvider
       |
       +── FutureGoogleAdsProvider
       |
       +── FutureLinkedInAdsProvider
       |
       +── FutureTikTokAdsProvider
```

This prevents Instagram-specific logic from contaminating the core advertising domain.

---

## 17. Credential Security

## SR-IG-005

Meta credentials shall:

* Never be stored in plaintext.
* Be encrypted at rest.
* Be encrypted in transit.
* Be stored in a secure secrets system.
* Use least-privilege permissions.
* Support revocation.
* Support rotation.
* Never appear in logs.

---

## SR-IG-006

System-user and access-token management shall be isolated from application business logic.

---

## 18. Identity and Access Management

## SR-IG-007

The system shall implement:

* RBAC
* Tenant isolation
* Resource-level authorization
* Team permissions
* Campaign permissions
* Budget permissions
* Approval permissions
* Automation permissions
* AI execution permissions

---

## SR-IG-008 — AI Tool Permissions

AI shall interact with the platform through explicit tools.

Example:

```text
READ_ACCOUNT
READ_CAMPAIGN
READ_ADSET
READ_AD
READ_AUDIENCE
READ_INSIGHTS

CREATE_DRAFT_CAMPAIGN
CREATE_DRAFT_CREATIVE
CREATE_DRAFT_AUDIENCE

RECOMMEND_BUDGET_CHANGE
RECOMMEND_AUDIENCE_CHANGE
RECOMMEND_CREATIVE_CHANGE

EXECUTE_BUDGET_CHANGE
PAUSE_CAMPAIGN
PAUSE_AD
LAUNCH_CAMPAIGN
```

High-risk tools shall require approval.

---

## 19. Human-in-the-Loop Architecture

## SR-IG-009

The platform shall implement:

```text
AI Recommendation
        ↓
Policy Validation
        ↓
Risk Assessment
        ↓
Approval Required?
        ↓
Human Review
        ↓
Approve / Reject / Modify
        ↓
Execution
        ↓
Monitoring
```

---

## 20. Event-Driven Architecture

## SR-IG-010

The platform shall publish advertising events.

Example:

```text
instagram.account.connected
instagram.account.disconnected

campaign.created
campaign.updated
campaign.approved
campaign.launched
campaign.paused
campaign.completed

adset.created
adset.updated
adset.paused

ad.created
ad.updated
ad.approved
ad.rejected

creative.created
creative.approved
creative.rejected
creative.fatigue_detected

audience.created
audience.updated
audience.saturated

budget.changed
budget.threshold_reached

lead.generated
lead.qualified
lead.disqualified
lead.converted

conversion.recorded
revenue.attributed

performance.anomaly_detected

ai.recommendation.created
ai.recommendation.approved
ai.recommendation.rejected
ai.action.executed
```

---

## 21. Data Architecture

## SR-IG-011 — PostgreSQL

PostgreSQL shall store:

```text
Tenant
Organization
User
Team

InstagramAccount
MetaBusinessAccount
MetaAdAccount

Campaign
AdSet
Ad
Creative
CreativeVersion

Audience
CustomAudience
LookalikeAudience
RetargetingAudience

Budget
BidStrategy
Placement

Lead
Opportunity
Customer
Revenue

CampaignMetric
AdSetMetric
AdMetric
AudienceMetric
CreativeMetric

Recommendation
RecommendationEvidence
Approval

AutomationRule
Experiment

AIAction
AIExecution
AuditEvent
Alert
```

---

## SR-IG-012 — Redis

Redis shall support:

* Caching
* Rate limiting
* Distributed locks
* Job coordination
* Short-lived provider data
* Session state
* Idempotency keys

---

## SR-IG-013 — Object Storage

Object storage shall support:

* Images
* Videos
* Reels
* Creative assets
* Generated reports
* Export files
* AI-generated artifacts

---

## SR-IG-014 — Vector Storage

Vector storage shall support:

* Creative embeddings
* Campaign knowledge
* Audience intelligence
* Marketing knowledge
* Historical campaign intelligence
* Semantic campaign search
* Creative similarity detection

---

## 22. Analytics Architecture

## SR-IG-015

Large-scale advertising analytics shall be separated from transactional workloads.

```text
Meta
 ↓
Ingestion Layer
 ↓
Event Bus
 ↓
Data Processing
 ↓
Data Warehouse
 ↓
Feature Store
 ↓
ML/AI
 ↓
Analytics API
 ↓
Dashboard
```

---

## 23. Synchronization

## SR-IG-016

The system shall synchronize:

* Campaign status
* Ad-set status
* Ad status
* Spend
* Performance metrics
* Conversion metrics
* Audience data
* Creative data
* Lead data

---

## SR-IG-017 — Data Freshness

The synchronization engine shall support configurable intervals.

High-priority information shall be synchronized with higher frequency.

---

## 24. Reliability

## SR-IG-018 — Idempotency

Meta write operations shall be idempotent.

The system shall prevent duplicate:

* Campaigns
* Ad sets
* Ads
* Audiences
* Conversion events
* Leads

---

## SR-IG-019 — Retry

Provider failures shall support:

* Exponential backoff
* Jitter
* Retry budgets
* Circuit breakers
* Dead-letter queues

---

## SR-IG-020 — Rate Limiting

The platform shall enforce:

* User-level limits
* Tenant-level limits
* Ad-account-level limits
* Provider API limits
* AI execution limits

---

## 25. Observability

## SR-IG-021

The module shall provide:

* Structured logs
* Metrics
* Distributed tracing
* Error tracking
* API latency monitoring
* Provider API monitoring
* Synchronization monitoring
* AI execution monitoring
* Campaign publication monitoring

---

## SR-IG-022

Each important operation shall contain:

```text
Trace ID
Request ID
Tenant ID
Organization ID
User ID
Ad Account ID
Campaign ID
Operation ID
Timestamp
Status
Error
```

---

## 26. AI Safety

## SR-IG-023

AI shall never:

* Exceed configured budgets.
* Bypass approval policies.
* Access another tenant.
* Modify unauthorized campaigns.
* Publish prohibited content.
* Disable security controls.
* Remove audit records.
* Expose credentials.

---

## SR-IG-024 — AI Guardrail Pipeline

```text
AI Agent
   ↓
Tool Permission Engine
   ↓
Policy Engine
   ↓
Budget Guard
   ↓
Risk Engine
   ↓
Approval Engine
   ↓
Execution Engine
   ↓
Audit Log
```

---

## 27. Functional Requirements

## FR-IG-001 — Instagram Authentication

The system shall provide secure authentication and authorization for supported Instagram professional-account integrations.

---

## FR-IG-002 — Asset Discovery

After authorization, the system shall discover accessible:

* Instagram accounts
* Meta business assets
* Ad accounts
* Pages
* Tracking assets
* Campaign assets

---

## FR-IG-003 — Campaign CRUD

The system shall support:

```text
Create Campaign
Read Campaign
Update Campaign
Delete Campaign
Duplicate Campaign
Archive Campaign
Pause Campaign
Resume Campaign
```

---

## FR-IG-004 — Ad Set CRUD

The system shall support:

```text
Create
Read
Update
Delete
Duplicate
Pause
Resume
```

---

## FR-IG-005 — Ad CRUD

The system shall support:

```text
Create
Read
Update
Delete
Duplicate
Preview
Approve
Reject
Pause
Resume
```

---

## 28. AI Campaign Planner

## FR-IG-006

Input:

```json
{
  "business_goal": "Generate qualified B2B SaaS leads",
  "product": "AI Customer Support Platform",
  "market": "United States",
  "monthly_budget": 5000,
  "duration": "30 days"
}
```

Output:

```json
{
  "objective": "LEADS",
  "audience_strategy": "...",
  "creative_strategy": "...",
  "reel_strategy": "...",
  "story_strategy": "...",
  "carousel_strategy": "...",
  "budget_strategy": "...",
  "testing_strategy": "...",
  "measurement_strategy": "..."
}
```

---

## 29. AI Campaign Drafting

## FR-IG-007

The AI shall transform a marketing objective into a campaign draft containing:

* Campaign
* Ad sets
* Audience
* Creative
* Copy
* CTA
* Budget
* Schedule
* Tracking
* Optimization strategy

---

## 30. AI Audience Builder

## FR-IG-008

The AI shall construct audience recommendations from:

```text
ICP
+
Persona
+
Intent
+
Buying Signals
+
Historical Customers
+
Campaign History
+
CRM
+
Revenue
```

---

## 31. Audience Scoring

## FR-IG-009

Every AI audience recommendation shall contain:

```text
Audience Score
Relevance
Estimated Size
Conversion Probability
Expected CPL
Expected ROAS
Confidence
Risk
```

---

## 32. AI Creative Engine

## FR-IG-010

The creative engine shall generate:

```text
Image Concepts
Video Concepts
Reel Scripts
Story Sequences
Carousel Concepts
Captions
Hooks
Headlines
CTAs
```

---

## 33. Creative Scoring

## FR-IG-011

AI shall score creatives based on:

* Persona alignment
* Audience relevance
* Hook strength
* Message clarity
* CTA strength
* Historical performance
* Predicted engagement
* Predicted conversion
* Creative fatigue risk

---

## 34. Creative Versioning

## FR-IG-012

Every creative modification shall create a new version.

```text
Creative v1
    ↓
Creative v2
    ↓
Creative v3
    ↓
Creative v4
```

Users shall be able to restore previous versions.

---

## 35. Campaign Validation

## FR-IG-013

Before publication, the platform shall validate:

* Required configuration
* Audience
* Budget
* Creative
* Destination
* Tracking
* Permissions
* Internal policy
* Provider constraints
* Automation policy

---

## 36. Campaign Risk Score

## FR-IG-014

The system shall calculate:

```text
Campaign Risk Score
```

using:

* Budget risk
* Audience risk
* Creative risk
* Tracking risk
* Compliance risk
* Performance uncertainty
* Automation risk

---

## 37. Campaign State Machine

## FR-IG-015

Campaign states shall include:

```text
DRAFT
PENDING_REVIEW
APPROVED
SCHEDULED
ACTIVE
OPTIMIZING
PAUSED
FAILED
COMPLETED
ARCHIVED
```

---

## 38. AI Optimization Loop

## FR-IG-016

```text
Collect Data
      ↓
Normalize
      ↓
Calculate Metrics
      ↓
Detect Patterns
      ↓
Detect Anomalies
      ↓
Generate Recommendations
      ↓
Estimate Impact
      ↓
Risk Assessment
      ↓
Human Approval
      ↓
Execution
      ↓
Measure Results
      ↓
Learn
```

---

## 39. Campaign Health Score

## FR-IG-017

The campaign health score shall consider:

* CTR
* CPC
* CPM
* CPL
* CPA
* Conversion rate
* ROAS
* Frequency
* Budget utilization
* Lead quality
* Creative fatigue
* Audience saturation

---

## 40. Creative Health Score

## FR-IG-018

Each creative shall receive:

```text
Engagement Score
Conversion Score
Audience Relevance
Creative Fatigue
Predicted Performance
Overall Health
```

---

## 41. Audience Health Score

## FR-IG-019

Audience health shall consider:

* Audience size
* Reach
* Frequency
* CTR
* Conversion rate
* CPL
* CPA
* Lead quality
* Saturation

---

## 42. Budget Health

## FR-IG-020

The platform shall monitor:

* Planned budget
* Actual spend
* Remaining budget
* Spend velocity
* Budget utilization
* Forecasted spend
* Forecasted revenue
* Forecasted profit

---

## 43. Spend Anomaly Detection

## FR-IG-021

Example:

```text
Expected daily spend: $150
Projected spend: $290

Anomaly:
93% above expected spend.

Action:
Alert Marketing Manager.
```

---

## 44. Performance Anomaly Detection

## FR-IG-022

The system shall detect statistically meaningful changes in:

* CTR
* CPC
* CPM
* CPL
* CPA
* Conversion rate
* ROAS
* Revenue
* Profit

---

## 45. AI Root-Cause Analysis

## FR-IG-023

When performance changes significantly, AI shall identify probable causes.

```text
ROAS decreased by 31%.

Likely causes:

Creative fatigue       43%
Audience saturation    27%
CPM increase           18%
Conversion decline     12%
```

---

## 46. Autonomous Optimization

## FR-IG-024

The platform shall allow authorized autonomous optimization.

Possible actions:

```text
Pause Ad
Pause Campaign
Adjust Budget
Rotate Creative
Activate Approved Variant
Adjust Predefined Parameter
```

---

## 47. Autonomous Execution Limits

## FR-IG-025

Organizations shall configure:

```text
Maximum Budget Increase
Maximum Budget Decrease
Maximum Daily Spend
Maximum Monthly Spend
Maximum Automated Actions
Maximum Audience Expansion
Maximum Campaign Changes
```

---

## 48. Approval Thresholds

## FR-IG-026

Example:

```text
Budget change < 5%
    → AI may execute

Budget change 5–15%
    → Marketing Manager approval

Budget change > 15%
    → Organization Admin approval
```

All thresholds shall be configurable.

---

## 49. Experiment Engine

## FR-IG-027

The experiment engine shall support:

```text
Hypothesis
    ↓
Variable Selection
    ↓
Variant Creation
    ↓
Traffic Allocation
    ↓
Measurement
    ↓
Statistical Evaluation
    ↓
Winner Recommendation
    ↓
Deployment
```

---

## 50. Audience Overlap Detection

## FR-IG-028

The system shall identify overlapping audiences across campaigns and ad sets.

---

## 51. Audience Cannibalization

## FR-IG-029

AI shall detect when multiple campaigns compete for substantially similar audiences.

AI shall recommend:

* Consolidation
* Segmentation
* Exclusion
* Budget redistribution

---

## 52. Instagram Content Intelligence

## FR-IG-030

The platform shall analyze authorized Instagram content to identify:

* High-performing topics
* High-performing formats
* High-performing hooks
* Engagement patterns
* Audience interests
* Content themes
* Content fatigue

---

## 53. Organic-to-Paid Intelligence

## FR-IG-031

The AI shall identify high-performing organic content that may be suitable for paid amplification.

Example:

```text
Organic Reel
     ↓
High Engagement
     ↓
High Saves
     ↓
High Shares
     ↓
Strong Audience Relevance
     ↓
AI Recommendation:
Test as Paid Creative
```

---

## 54. Paid-to-Organic Intelligence

## FR-IG-032

AI shall identify successful advertising concepts that may be converted into:

* Organic Reels
* Stories
* Carousels
* Posts
* Educational content

---

## 55. Funnel Analytics

## FR-IG-033

The system shall provide:

```text
Impression
    ↓
Reach
    ↓
Engagement
    ↓
Click
    ↓
Landing Page
    ↓
Lead
    ↓
Qualified Lead
    ↓
Opportunity
    ↓
Customer
    ↓
Revenue
    ↓
Profit
```

---

## 56. Marketing-to-Sales Feedback

## FR-IG-034

Sales outcomes shall feed back into advertising intelligence.

Example:

```text
Instagram Campaign
      ↓
100 Leads
      ↓
25 Qualified
      ↓
7 Opportunities
      ↓
3 Customers
      ↓
$30,000 Revenue
```

The system shall use this information to identify high-value campaign patterns.

---

## 57. AI Lead Quality Model

## FR-IG-035

Lead-quality models shall use:

* Historical conversions
* Sales feedback
* Customer value
* Industry
* Company size
* Persona
* Campaign
* Audience
* Creative
* Engagement
* Revenue

---

## 58. Recommendation Lifecycle

## FR-IG-036

Every recommendation shall follow:

```text
CREATED
   ↓
REVIEWED
   ↓
APPROVED / REJECTED
   ↓
EXECUTED
   ↓
MEASURED
   ↓
LEARNED
```

---

## 59. Recommendation Feedback

## FR-IG-037

Humans shall be able to:

* Approve
* Reject
* Modify
* Snooze
* Ignore
* Provide rejection reason

AI shall use feedback to improve future recommendations.

---

## 60. AI Confidence

## FR-IG-038

Every AI recommendation shall expose:

```text
Confidence
Evidence
Expected Impact
Risk
Data Quality
Model Version
```

---

## 61. Data Quality

## FR-IG-039

The system shall detect:

* Missing conversions
* Missing attribution
* Tracking failures
* Delayed events
* Duplicate events
* Duplicate leads
* Missing campaign metadata
* Inconsistent campaign identifiers

---

## 62. Tracking Health

## FR-IG-040

The system shall monitor:

* Event delivery
* Event duplication
* Event delay
* Attribution coverage
* Conversion tracking
* Server-side tracking
* Browser-side tracking
* CRM conversion synchronization

---

## 63. Campaign Reporting

## FR-IG-041

The system shall generate:

* Daily reports
* Weekly reports
* Monthly reports
* Campaign reports
* Audience reports
* Creative reports
* Reel reports
* Story reports
* Carousel reports
* ROI reports
* ROAS reports
* Revenue reports
* Profitability reports
* Executive reports

---

## 64. AI Executive Summary

## FR-IG-042

AI shall generate executive summaries containing:

* Total spend
* Revenue
* Profit
* ROAS
* ROI
* CAC
* Qualified leads
* Conversion rate
* Major opportunities
* Major risks
* Recommended actions

---

## 65. Multi-Account Management

## FR-IG-043

Enterprise customers shall be able to manage multiple:

* Organizations
* Meta Business accounts
* Ad accounts
* Instagram professional accounts
* Campaigns
* Audiences
* Creative libraries

from one SalesGenie environment.

---

## 66. Multi-Tenant Isolation

## FR-IG-044

Each tenant shall have isolated:

* Credentials
* Campaigns
* Audiences
* Creatives
* Analytics
* Leads
* Revenue data
* AI context
* AI actions
* Automation rules

---

## 67. Auditability

## FR-IG-045

The system shall record:

* Human actions
* AI recommendations
* AI decisions
* AI executions
* Campaign changes
* Audience changes
* Creative changes
* Budget changes
* Approvals
* Rejections
* Rollbacks
* Automation events

---

## 68. Data Model

```text
Tenant
Organization
Workplace
User
Team

InstagramAccount
MetaBusinessAccount
MetaAdAccount

Campaign
AdSet
Ad

Creative
CreativeVersion
CreativeAsset
ReelConcept
StoryConcept
CarouselConcept

Audience
CustomAudience
LookalikeAudience
RetargetingAudience

Budget
BidStrategy
Placement

CampaignMetric
AdSetMetric
AdMetric
CreativeMetric
AudienceMetric

Lead
Opportunity
Customer
Revenue
Profit

ConversionEvent
AttributionEvent

Recommendation
RecommendationEvidence
Approval

Experiment
ExperimentVariant

AutomationRule
AIAction
AIExecution

Alert
AuditEvent
```

---

## 69. Example AI Recommendation Object

```json
{
  "recommendation_id": "ig_rec_001",
  "tenant_id": "tenant_001",
  "campaign_id": "ig_campaign_001",
  "type": "CREATIVE_REFRESH",
  "severity": "MEDIUM",
  "confidence": 0.89,
  "reason": "Creative fatigue detected",
  "evidence": [
    "Frequency increased 31%",
    "CTR decreased 18%",
    "CPL increased 24%"
  ],
  "recommendation": {
    "action": "replace_underperforming_creatives",
    "number_of_variants": 4
  },
  "expected_impact": {
    "ctr": "+8-15%",
    "cpl": "-5-12%"
  },
  "risk": "LOW",
  "approval_required": true,
  "status": "PENDING_APPROVAL"
}
```

---

## 70. Example Autonomous Policy

```yaml
policy:
  name: conservative_instagram_scaling

  conditions:
    minimum_campaign_age_hours: 72
    minimum_spend: 100
    minimum_conversions: 10
    minimum_roas: 2.5

  actions:
    budget_increase:
      maximum_percentage: 15

  safety:
    maximum_daily_budget: 1000
    maximum_monthly_budget: 10000
    require_human_approval_above_percentage: 15
    emergency_stop_enabled: true
```

---

## 71. AI Decision Pipeline

```text
Business Objective
        ↓
Market Intelligence
        ↓
ICP
        ↓
Persona
        ↓
Audience Intelligence
        ↓
Intent
        ↓
Buying Signals
        ↓
Customer Intelligence
        ↓
Marketing Strategy
        ↓
Instagram Campaign Planner
        ↓
AI Audience Agent
        ↓
AI Content Agent
        ↓
AI Advertising Agent
        ↓
Campaign Draft
        ↓
Risk Engine
        ↓
Policy Engine
        ↓
Human Approval
        ↓
Instagram / Meta Ads
        ↓
Performance Data
        ↓
AI Marketing Analytics
        ↓
Lead Intelligence
        ↓
CRM
        ↓
Revenue
        ↓
Profitability Intelligence
        ↓
AI Optimization
        ↓
Experimentation
        ↓
Learning
        ↓
Next Campaign
```

---

## 72. Human + AI Operating Modes

## Mode 1 — Human Only

```text
Human
  ↓
Campaign
  ↓
Instagram / Meta
  ↓
Human Analysis
```

## Mode 2 — AI Assisted

```text
Human
  ↓
AI Recommendation
  ↓
Human Decision
  ↓
Instagram / Meta
```

## Mode 3 — Human-in-the-Loop

```text
AI
  ↓
Recommendation
  ↓
Risk Evaluation
  ↓
Human Approval
  ↓
Execution
```

## Mode 4 — Controlled Autonomous

```text
AI
  ↓
Policy Engine
  ↓
Permission Engine
  ↓
Budget Guard
  ↓
Risk Engine
  ↓
Automatic Execution
  ↓
Monitoring
  ↓
Human Escalation
```

---

## 73. Functional Permission Matrix

| Capability        |     End User | Sales Agent | Marketing Manager |  Analyst | Org Admin | Super Admin |
| ----------------- | -----------: | ----------: | ----------------: | -------: | --------: | ----------: |
| View Campaigns    |          Yes |     Limited |               Yes |      Yes |       Yes |         Yes |
| Create Campaign   |          Yes |          No |               Yes | Optional |       Yes |         Yes |
| Edit Campaign     |          Yes |          No |               Yes | Optional |       Yes |         Yes |
| Launch Campaign   | Configurable |          No |               Yes |       No |       Yes |         Yes |
| Pause Campaign    | Configurable |          No |               Yes |       No |       Yes |         Yes |
| Change Budget     | Configurable |          No |      Configurable |       No |       Yes |         Yes |
| Connect Instagram |          Yes |          No |               Yes |       No |       Yes |         Yes |
| Create Audience   |          Yes |          No |               Yes |      Yes |       Yes |         Yes |
| Generate Creative |          Yes |          No |               Yes |      Yes |       Yes |         Yes |
| Generate Reel     |          Yes |          No |               Yes |      Yes |       Yes |         Yes |
| Generate Story    |          Yes |          No |               Yes |      Yes |       Yes |         Yes |
| Generate Carousel |          Yes |          No |               Yes |      Yes |       Yes |         Yes |
| Approve AI Action | Configurable |          No |               Yes | Optional |       Yes |         Yes |
| Autonomous AI     | Configurable |          No |      Configurable |       No |       Yes |         Yes |
| View Revenue      | Configurable |     Limited |               Yes |      Yes |       Yes |         Yes |
| View Profit       | Configurable |          No |               Yes |      Yes |       Yes |         Yes |
| View Audit Logs   |           No |          No |           Limited |  Limited |       Yes |         Yes |

---

## 74. Non-Functional Requirements

## NFR-IG-001 — Performance

Target:

```text
Cached Dashboard API:
p50 < 300ms

Standard Analytics API:
p95 < 1s

Complex Analytics:
p95 < 3s
```

---

## NFR-IG-002 — Availability

Critical advertising services shall target enterprise-grade availability.

The system shall degrade gracefully when Meta services are unavailable.

---

## NFR-IG-003 — Scalability

The system shall horizontally scale with:

* Tenants
* Instagram accounts
* Ad accounts
* Campaigns
* Ads
* Creative assets
* Events
* AI requests
* Analytics volume

---

## NFR-IG-004 — Security

The module shall implement:

* Encryption
* Least privilege
* Secure credential storage
* RBAC
* Tenant isolation
* Audit logging
* Secure webhooks
* Input validation
* Output validation

---

## NFR-IG-005 — Privacy

The platform shall support applicable:

* Privacy requirements
* Consent requirements
* Data retention policies
* Data deletion workflows
* Data access controls

---

## NFR-IG-006 — Observability

Every critical operation shall provide:

```text
Trace ID
Request ID
Tenant ID
User ID
Account ID
Campaign ID
Operation ID
Timestamp
Status
Error
```

---

## NFR-IG-007 — Disaster Recovery

The platform shall support:

* Automated backups
* Database recovery
* Event replay
* Failed-job recovery
* Idempotent synchronization
* Disaster recovery procedures

---

## 75. Success Metrics

## Advertising Metrics

* CPM
* CPC
* CTR
* Reach
* Frequency
* Impressions
* Spend

## Lead Metrics

* Leads
* Qualified leads
* CPL
* Qualified CPL
* Lead-to-opportunity rate
* Lead-to-customer rate

## Revenue Metrics

* Revenue
* ROAS
* ROI
* CAC
* LTV
* LTV:CAC
* Profit

## Creative Metrics

* Hook performance
* Reel performance
* Story performance
* Carousel performance
* Creative fatigue
* Creative conversion rate

## AI Metrics

* Recommendation acceptance rate
* Recommendation rejection rate
* Recommendation accuracy
* AI prediction accuracy
* AI action success rate
* Human override rate
* Autonomous action failure rate
* AI optimization lift

## Operational Metrics

* API success rate
* Synchronization latency
* Webhook processing latency
* Campaign publication success rate
* Event processing success rate
* AI execution latency

---

## 76. FAANG-Level Acceptance Criteria

The module shall be considered production-ready only when:

* Instagram professional-account integration works reliably.
* Meta advertising-account integration works reliably.
* Multiple advertising accounts can be managed.
* Campaign CRUD is reliable.
* Ad-set CRUD is reliable.
* Ad CRUD is reliable.
* Audience management is reliable.
* Creative management is reliable.
* Instagram-native creative workflows are supported.
* AI can generate complete campaign drafts.
* AI can generate Reel concepts.
* AI can generate Story concepts.
* AI can generate carousel concepts.
* AI can generate advertising copy.
* AI can recommend audiences.
* AI can recommend budgets.
* AI can detect creative fatigue.
* AI can detect audience saturation.
* AI can detect campaign anomalies.
* AI can explain recommendations.
* AI recommendations contain confidence and evidence.
* AI high-risk actions require approval.
* Autonomous AI respects hard budget limits.
* Emergency campaign shutdown works.
* Campaign synchronization is idempotent.
* Meta API failures are handled gracefully.
* Duplicate campaigns cannot be accidentally created.
* CRM attribution works.
* Lead quality feedback reaches the AI optimization system.
* Revenue can be attributed to advertising activity.
* Profit can be attributed to advertising activity.
* A/B testing is supported.
* Experiment results feed back into AI intelligence.
* Human approval workflows work.
* Human overrides work.
* AI automation can be disabled instantly.
* Complete AI and human audit trails exist.
* Tenant data is isolated.
* Advertising credentials are securely stored.
* Dashboard data is consistent with backend data.
* Campaign state transitions are reliable.
* Failed operations can be retried safely.
* AI can operate in human-only mode.
* AI can operate in assistive mode.
* AI can operate in human-in-the-loop mode.
* AI can operate in controlled autonomous mode.

---

## 77. Strategic Product Architecture

SalesGenie shall not implement Instagram Ads as merely an advertising dashboard.

It shall operate as an:

## AI-Powered Instagram Advertising Intelligence, Automation and Revenue Optimization Platform

The complete closed-loop system shall be:

```text
                    BUSINESS OBJECTIVE
                           ↓
                  MARKET INTELLIGENCE
                           ↓
                         ICP
                           ↓
                       PERSONA
                           ↓
                 AUDIENCE INTELLIGENCE
                           ↓
                   INTENT + SIGNALS
                           ↓
                  MARKETING STRATEGY
                           ↓
                 INSTAGRAM CAMPAIGN
                           ↓
             ┌─────────────┼─────────────┐
             ↓             ↓             ↓
          REELS         STORIES       CAROUSELS
             ↓             ↓             ↓
                 PAID INSTAGRAM ADS
                           ↓
                       ENGAGEMENT
                           ↓
                         LEADS
                           ↓
                    AI SALES AGENT
                           ↓
                    HUMAN SALES AGENT
                           ↓
                         CRM
                           ↓
                      QUALIFIED
                           ↓
                      OPPORTUNITY
                           ↓
                       CUSTOMER
                           ↓
                       REVENUE
                           ↓
                        PROFIT
                           ↓
                 MARKETING ANALYTICS
                           ↓
                   AI OPTIMIZATION
                           ↓
                    EXPERIMENTATION
                           ↓
                    AI LEARNING LOOP
                           ↓
                  NEXT CAMPAIGN CYCLE
```

The primary optimization target shall therefore be:

```text
Incremental Qualified Revenue
        +
Profitability
        +
Customer Lifetime Value
        +
Sustainable Customer Acquisition
```

rather than vanity metrics such as:

```text
Likes
Views
Followers
Impressions
Clicks
```

---

## 78. Product-Level Design Principle

The Instagram Ads module shall form one component of SalesGenie's larger autonomous marketing operating system:

```text
                    SALES GENIE
                         |
        ┌────────────────┼────────────────┐
        ↓                ↓                ↓
   INTELLIGENCE       CREATION         EXECUTION
        |                |                |
        ↓                ↓                ↓
      ICP             Content          Campaigns
      Persona         Creative         Instagram Ads
      Intent          Reels            Facebook Ads
      Signals         Stories          Email
      Audience        Carousels        Social
      Competition     Copy             Automation
        |                |                |
        └────────────────┼────────────────┘
                         ↓
                    OPTIMIZATION
                         |
                         ↓
                   LEAD GENERATION
                         |
                         ↓
                       SALES
                         |
                         ↓
                       CRM
                         |
                         ↓
                     REVENUE
                         |
                         ↓
                     PROFIT
                         |
                         ↓
                 BUSINESS INTELLIGENCE
                         |
                         ↓
                  AI DECISION ENGINE
                         |
                         ↓
                CONTINUOUS LEARNING
```

The Instagram Ads module shall therefore operate as a **closed-loop AI advertising and revenue optimization subsystem**, while remaining fully controllable by authorized human users.
