# SalesGenie — FAANG-Level Lead Generation Engine

## User Requirements, System Requirements & Functional Requirements

**Module:** `lead_generation_engine.md`  
**Platform:** SalesGenie Enterprise AI Sales & Revenue Intelligence Platform  
**Processing Model:** AI-Based + Human-Assisted  
**Architecture:** Multi-Tenant, Event-Driven, Microservices, Multi-Agent AI  
**Requirement Level:** Enterprise / FAANG-Level  
**Version:** 1.0

---

## 1. Purpose

The Lead Generation Engine shall be the core orchestration layer responsible for transforming an organization's Ideal Customer Profile (ICP), market criteria, business objectives, and authorized data sources into verified, enriched, qualified, scored, segmented, prioritized, routed, and actionable sales leads.

The engine shall support both:

- AI-autonomous lead generation
- Human-controlled lead generation
- AI + human collaborative workflows
- Rule-based generation
- Event-triggered generation
- Scheduled generation
- Continuous lead discovery
- Account-based lead generation
- Campaign-based lead generation

The engine shall integrate with SalesGenie's:

- Lead Discovery
- Lead Enrichment
- Lead Verification
- Lead Deduplication
- Lead Qualification
- Lead Scoring
- Lead Segmentation
- Lead Routing
- Lead Assignment
- Lead Nurturing
- Outreach Automation
- Sales Sequences
- Sales Workflows
- Sales Analytics
- Sales Forecasting
- CRM
- AI Agent Platform

---

## 2. Core Business Objective

The Lead Generation Engine shall optimize for:

```text
High-Quality Leads
        +
High ICP Fit
        +
High Buying Intent
        +
High Conversion Probability
        +
High Revenue Potential
        -
Low Acquisition Cost
        -
Low Data Risk
        -
Low Human Effort
```

The engine shall optimize for **revenue-generating opportunities**, not merely lead volume.

---

## 3. Lead Generation Engine Lifecycle

```text
ICP Definition
      ↓
Generation Strategy
      ↓
Target Market Definition
      ↓
Source Selection
      ↓
Discovery
      ↓
Data Collection
      ↓
Normalization
      ↓
Identity Resolution
      ↓
Deduplication
      ↓
Enrichment
      ↓
Verification
      ↓
AI Research
      ↓
ICP Matching
      ↓
Qualification
      ↓
Scoring
      ↓
Intent Detection
      ↓
Segmentation
      ↓
Prioritization
      ↓
Human Review
      ↓
Routing
      ↓
Assignment
      ↓
Nurturing
      ↓
Outreach
      ↓
Engagement
      ↓
Opportunity
      ↓
Deal
      ↓
Revenue Attribution
      ↓
Feedback
      ↓
Continuous Optimization
```

---

## 4. Primary Actors

| Actor                    | Responsibilities                        |
| ------------------------ | --------------------------------------- |
| Super Admin              | Platform-wide governance                |
| Organization Admin       | Organization-level configuration        |
| Workplace Admin          | Workplace-level configuration           |
| Sales Manager            | Lead generation strategy and governance |
| Sales Agent              | Lead processing and conversion          |
| SDR / BDR                | Prospecting and qualification           |
| Marketing Manager        | Campaign and ICP management             |
| RevOps Manager           | Revenue operations                      |
| Data Analyst             | Analytics and reporting                 |
| Compliance Manager       | Data and outreach governance            |
| AI Lead Generation Agent | Autonomous generation                   |
| AI Research Agent        | Prospect research                       |
| AI Qualification Agent   | Qualification                           |
| AI Scoring Agent         | Scoring                                 |
| AI Routing Agent         | Routing                                 |
| AI Sales Agent           | Automated sales activities              |

---

## 5. User Requirements

## UR-001 — Create Lead Generation Campaign

Users shall be able to create a lead-generation campaign.

A campaign shall support:

```text
Campaign Name
Objective
ICP
Target Market
Target Accounts
Target Contacts
Geography
Industry
Company Size
Revenue
Job Titles
Seniority
Technology
Intent
Lead Sources
Generation Strategy
Qualification Rules
Scoring Rules
Routing Rules
Assignment Rules
Approval Policy
Schedule
Budget
```

---

## UR-002 — Natural Language Lead Generation

Users shall be able to describe their desired prospects using natural language.

Example:

```text
Find decision makers at B2B SaaS companies
with 50–500 employees in the United States,
who recently raised funding and are hiring
engineering leaders.
```

The engine shall convert the request into structured generation criteria.

---

## UR-003 — Structured Lead Generation

Users shall be able to configure lead-generation criteria through forms, filters, rules, and advanced conditions.

---

## UR-004 — ICP-Based Generation

Users shall be able to generate leads exclusively matching a configured ICP.

---

## UR-005 — Multiple ICP Support

Organizations shall be able to maintain multiple ICPs simultaneously.

---

## UR-006 — ICP Versioning

The engine shall preserve historical ICP versions used by previous campaigns.

---

## UR-007 — Market-Based Generation

Users shall be able to target:

```text
Industry
Country
Region
City
Market
Business Model
Company Size
Revenue
Growth Stage
Funding Stage
```

---

## UR-008 — Contact-Based Generation

Users shall be able to target:

```text
Job Title
Department
Seniority
Decision-Making Role
Professional Function
Technical Expertise
Language
```

---

## UR-009 — Account-Based Generation

Users shall be able to specify target companies and generate relevant contacts within those accounts.

---

## UR-010 — Competitor-Based Generation

The engine shall support prospect generation based on organizations using competitors or competing solutions, where permitted by configured data sources.

---

## UR-011 — Technology-Based Generation

Users shall be able to generate leads based on technology adoption.

---

## UR-012 — Trigger-Based Generation

Users shall be able to generate leads when business events occur.

Supported triggers may include:

```text
Funding
Hiring
Expansion
Leadership Change
Product Launch
Acquisition
Partnership
Technology Adoption
Market Entry
Company Growth
New Office
New Website
New Product
```

---

## UR-013 — Intent-Based Generation

Users shall be able to generate leads based on buying-intent signals.

---

## UR-014 — Bulk Lead Generation

Users shall be able to request generation of large lead datasets.

---

## UR-015 — Scheduled Lead Generation

Users shall be able to schedule lead-generation jobs.

Supported schedules:

```text
One-Time
Hourly
Daily
Weekly
Monthly
Custom Cron
Event-Triggered
Continuous
```

---

## UR-016 — Recurring Generation

The engine shall support recurring prospect discovery without creating duplicate records.

---

## UR-017 — Lead Generation Preview

Users shall be able to preview expected generation results before execution.

---

## UR-018 — Lead Generation Approval

Organizations shall be able to require human approval before a campaign executes.

---

## UR-019 — AI Autonomous Generation

Authorized users shall be able to allow AI agents to execute lead-generation campaigns autonomously.

---

## UR-020 — Human-Controlled Generation

Users shall be able to execute the entire generation workflow manually.

---

## UR-021 — Hybrid Generation

Users shall be able to configure:

```text
AI Discovery
      ↓
Human Review
      ↓
AI Enrichment
      ↓
Human Approval
      ↓
AI Qualification
      ↓
Human Assignment
```

---

## UR-022 — Lead Source Selection

Users shall be able to select which authorized data sources the engine can use.

---

## UR-023 — Source Priority

Users shall be able to prioritize preferred data sources.

---

## UR-024 — Source Exclusion

Users shall be able to exclude specific sources.

---

## UR-025 — Lead Quantity Target

Users shall be able to specify the target number of leads.

---

## UR-026 — Lead Quality Target

Users shall be able to specify minimum:

```text
ICP Score
Verification Score
Lead Score
Intent Score
Confidence
```

---

## UR-027 — Minimum Qualification

Users shall be able to define minimum qualification requirements.

---

## UR-028 — Human Review Queue

Users shall be able to review AI-generated leads requiring approval.

---

## UR-029 — AI Recommendations

The engine shall recommend which leads should be prioritized.

---

## UR-030 — Lead Generation Analytics

Users shall be able to monitor:

```text
Leads Generated
Verified Leads
Qualified Leads
High-Intent Leads
Sales-Ready Leads
Opportunities
Deals
Revenue
```

---

## 6. AI-Based User Requirements

## AI-UR-001 — AI Prospect Discovery

The AI shall discover prospects matching configured generation objectives.

---

## AI-UR-002 — AI Search Strategy

The AI shall generate and optimize prospecting queries.

---

## AI-UR-003 — AI Market Expansion

When authorized, AI shall identify adjacent markets likely to contain high-value prospects.

---

## AI-UR-004 — AI ICP Interpretation

AI shall convert natural-language ICP descriptions into structured criteria.

---

## AI-UR-005 — AI ICP Optimization

AI shall identify patterns in successful leads and recommend ICP improvements.

---

## AI-UR-006 — AI Company Research

AI shall research companies using authorized sources.

---

## AI-UR-007 — AI Contact Discovery

AI shall identify relevant contacts within target organizations.

---

## AI-UR-008 — AI Buying Committee Discovery

AI shall identify potential:

```text
Economic Buyer
Decision Maker
Technical Buyer
Champion
Influencer
End User
Procurement
Blocker
```

---

## AI-UR-009 — AI Enrichment

AI shall enrich incomplete lead records.

---

## AI-UR-010 — AI Verification

AI shall evaluate whether collected lead information is reliable.

---

## AI-UR-011 — AI Entity Resolution

AI shall identify whether records represent the same person or organization.

---

## AI-UR-012 — AI Deduplication

AI shall detect probable duplicate leads.

---

## AI-UR-013 — AI Qualification

AI shall determine whether a prospect satisfies configured qualification criteria.

---

## AI-UR-014 — AI Lead Scoring

AI shall calculate lead-quality scores.

---

## AI-UR-015 — AI Intent Detection

AI shall identify potential buying signals.

---

## AI-UR-016 — AI Conversion Prediction

AI shall estimate the probability of lead conversion.

---

## AI-UR-017 — AI Revenue Potential

AI shall estimate potential commercial value when sufficient evidence exists.

---

## AI-UR-018 — AI Lead Prioritization

AI shall rank prospects according to:

```text
ICP Fit
Intent
Engagement
Conversion Probability
Potential Revenue
Recency
Company Value
```

---

## AI-UR-019 — AI Next-Best-Action

AI shall recommend the next action for each lead.

---

## AI-UR-020 — AI Generation Optimization

AI shall analyze historical campaign performance and recommend better discovery strategies.

---

## AI-UR-021 — AI Source Optimization

AI shall identify which sources produce the highest-quality leads.

---

## AI-UR-022 — AI Campaign Optimization

AI shall recommend changes to:

```text
ICP
Search Criteria
Sources
Filters
Scoring
Qualification
Routing
```

---

## AI-UR-023 — AI Confidence

Every consequential AI prediction shall provide a confidence score.

---

## AI-UR-024 — Explainable AI

AI-generated decisions shall provide understandable evidence and explanations.

---

## AI-UR-025 — AI Evidence

AI shall associate important claims with source evidence whenever available.

---

## AI-UR-026 — AI Human Escalation

AI shall request human intervention when:

```text
Confidence is Low
Data Conflicts Exist
Lead Value is High
Compliance Risk Exists
Sensitive Data is Detected
Multiple Decisions are Possible
Required Information is Missing
```

---

## AI-UR-027 — AI Guardrails

AI shall never:

```text
Bypass Permissions
Bypass Tenant Isolation
Bypass Consent
Fabricate Lead Data
Fabricate Evidence
Invent Contact Information
Ignore Suppression Rules
Execute Unauthorized Outreach
Modify Protected Data
Export Restricted Data
```

---

## 7. Human-Based User Requirements

## HUMAN-UR-001 — Manual Prospect Discovery

Human users shall be able to research and add prospects.

---

## HUMAN-UR-002 — Manual Lead Creation

Authorized users shall be able to create lead records.

---

## HUMAN-UR-003 — Manual Enrichment

Users shall be able to add or correct lead information.

---

## HUMAN-UR-004 — AI Review

Users shall be able to review AI-generated research.

---

## HUMAN-UR-005 — AI Override

Authorized users shall be able to override AI decisions.

---

## HUMAN-UR-006 — Lead Approval

Users shall be able to approve generated leads.

---

## HUMAN-UR-007 — Lead Rejection

Users shall be able to reject generated leads.

---

## HUMAN-UR-008 — Manual Qualification

Users shall be able to qualify leads manually.

---

## HUMAN-UR-009 — Manual Scoring

Authorized users shall be able to modify AI-generated scores.

---

## HUMAN-UR-010 — Manual Routing

Managers shall be able to route leads manually.

---

## HUMAN-UR-011 — Manual Assignment

Managers shall be able to assign leads to sales agents.

---

## HUMAN-UR-012 — Human Research Notes

Users shall be able to add notes and evidence.

---

## HUMAN-UR-013 — Merge Approval

Users shall be able to approve AI-recommended duplicate merges.

---

## HUMAN-UR-014 — AI-to-Human Handoff

AI agents shall be able to create human review tasks.

---

## HUMAN-UR-015 — Human-to-AI Handoff

Humans shall be able to return eligible leads to AI workflows.

---

## 8. System Requirements

## SR-001 — Multi-Tenant Architecture

The Lead Generation Engine shall operate as a multi-tenant service.

Every lead-generation operation shall be associated with:

```text
tenant_id
organization_id
workplace_id
user_id
campaign_id
```

---

## SR-002 — Tenant Isolation

No tenant shall be able to access another tenant's lead-generation data.

---

## SR-003 — Organization Isolation

Organization-level boundaries shall be enforced.

---

## SR-004 — Workplace Isolation

Workplace-level boundaries shall be enforced where configured.

---

## SR-005 — RBAC

The engine shall integrate with SalesGenie's centralized RBAC system.

---

## SR-006 — Fine-Grained Permissions

The system shall support permissions such as:

```text
lead_engine.view
lead_engine.create
lead_engine.execute
lead_engine.pause
lead_engine.cancel
lead_engine.configure
lead_engine.approve
lead_engine.reject
lead_engine.export
lead_engine.enrich
lead_engine.verify
lead_engine.qualify
lead_engine.score
lead_engine.route
lead_engine.assign
lead_engine.analytics
lead_engine.audit
lead_engine.ai_execute
lead_engine.ai_override
```

---

## SR-007 — AI Agent Authorization

Every AI agent shall operate under an explicit permission scope.

---

## SR-008 — Data Source Authorization

Only configured and authorized sources shall be accessible.

---

## SR-009 — Source Provenance

Every externally sourced attribute shall maintain provenance metadata.

---

## SR-010 — Evidence Tracking

AI-generated claims shall preserve evidence references whenever applicable.

---

## SR-011 — Event-Driven Processing

The engine shall support asynchronous event-driven processing.

---

## SR-012 — Job Queue

Large lead-generation workloads shall be executed through distributed job queues.

---

## SR-013 — Job State Management

Jobs shall support:

```text
DRAFT
QUEUED
RUNNING
PAUSED
COMPLETED
PARTIALLY_COMPLETED
FAILED
CANCELLED
```

---

## SR-014 — Idempotency

Repeated requests or events shall not generate duplicate leads.

---

## SR-015 — Retry Management

Transient failures shall support controlled retries.

---

## SR-016 — Dead Letter Queue

Failed jobs that exceed retry limits shall enter a dead-letter workflow.

---

## SR-017 — Rate Limiting

The engine shall enforce:

```text
Tenant Limits
Organization Limits
User Limits
Provider Limits
AI Agent Limits
Campaign Limits
```

---

## SR-018 — Concurrency Control

The system shall prevent conflicting lead-generation jobs from corrupting shared state.

---

## SR-019 — Distributed Locking

Distributed locks shall be used where necessary for:

```text
Campaign Execution
Lead Assignment
Deduplication
Merge
Quota Enforcement
```

---

## SR-020 — Transaction Integrity

Critical lead-state changes shall be atomic.

---

## 9. Functional Requirements — Engine Core

## FR-001 — Generation Engine Initialization

The engine shall validate:

```text
Tenant
Organization
Workplace
User
Permissions
Campaign
ICP
Sources
Quota
Budget
Policy
```

before execution.

---

## FR-002 — Generation Plan Creation

The engine shall convert campaign requirements into an executable generation plan.

Example:

```text
ICP
 ↓
Search Strategy
 ↓
Sources
 ↓
Discovery
 ↓
Enrichment
 ↓
Verification
 ↓
Qualification
 ↓
Scoring
 ↓
Routing
```

---

## FR-003 — Generation Plan Validation

The system shall validate the plan before execution.

---

## FR-004 — Dry Run

The engine shall support a dry-run mode.

Dry runs shall estimate:

```text
Expected Leads
Estimated Cost
Estimated Runtime
Expected Source Usage
Expected AI Usage
Expected Human Review
```

---

## FR-005 — Campaign Execution

The engine shall execute approved generation plans.

---

## FR-006 — Parallel Processing

Independent processing stages shall support parallel execution.

---

## FR-007 — Pipeline Processing

The engine shall support streaming or batched processing.

---

## FR-008 — Backpressure

The system shall prevent downstream services from being overwhelmed.

---

## 10. Discovery Engine

## FR-009 — Prospect Discovery

The discovery engine shall identify potential companies and contacts.

---

## FR-010 — Query Generation

AI shall generate optimized discovery queries.

---

## FR-011 — Query Expansion

The engine shall expand synonyms, related terms, and relevant search concepts.

---

## FR-012 — Query Refinement

The engine shall refine queries based on result quality.

---

## FR-013 — Source Aggregation

Results from multiple sources shall be aggregated.

---

## FR-014 — Source Normalization

Different provider schemas shall be converted into SalesGenie's canonical lead schema.

---

## FR-015 — Source Ranking

Sources shall be ranked according to:

```text
Reliability
Freshness
Coverage
Historical Accuracy
Cost
Conversion Quality
```

---

## 11. Lead Normalization

The system shall normalize:

```text
Names
Job Titles
Companies
Domains
Locations
Industries
Phone Numbers
Emails
Technologies
Dates
Currencies
Company Sizes
```

---

## 12. Entity Resolution

## FR-016 — Person Resolution

The system shall identify whether multiple records represent the same individual.

---

## FR-017 — Company Resolution

The system shall identify whether multiple records represent the same company.

---

## FR-018 — Domain Resolution

Company domains shall be normalized and matched.

---

## FR-019 — External Identity Mapping

External provider identifiers shall be mapped to internal identifiers.

---

## 13. Deduplication Engine

The deduplication engine shall evaluate:

```text
Exact Email
Normalized Email
Phone
Company Domain
Company Name
Contact Name
Professional Identity
External ID
AI Similarity
```

Duplicate confidence shall be classified as:

```text
UNIQUE
POSSIBLE_DUPLICATE
PROBABLE_DUPLICATE
CONFIRMED_DUPLICATE
```

---

## 14. Enrichment Engine

The engine shall support:

```text
Company Enrichment
Contact Enrichment
Firmographic Enrichment
Technographic Enrichment
Financial Enrichment
Intent Enrichment
Hiring Enrichment
Funding Enrichment
Business Event Enrichment
```

---

## 15. Verification Engine

The system shall verify supported attributes.

Verification status:

```text
VERIFIED
PARTIALLY_VERIFIED
UNVERIFIED
INVALID
STALE
CONFLICTING
```

---

## 16. Qualification Engine

The qualification engine shall support:

```text
Rule-Based Qualification
AI-Based Qualification
Human Qualification
Hybrid Qualification
```

Qualification frameworks may include:

```text
BANT
MEDDIC
MEDDPICC
CHAMP
Custom Framework
```

---

## 17. Scoring Engine

The engine shall support:

```text
ICP Score
Fit Score
Intent Score
Engagement Score
Company Score
Contact Score
Revenue Potential
Conversion Probability
Overall Lead Score
```

---

## 18. Dynamic Scoring

Scores shall be recalculated when significant events occur.

Examples:

```text
Funding Event
+
Relevant Hiring
+
High-Intent Activity
=
Score Increase
```

```text
Job Change
+
Email Invalid
+
No Recent Intent
=
Score Decrease
```

---

## 19. Intent Engine

The intent engine shall detect:

```text
Product Research
Pricing Research
Competitor Research
Technology Research
Hiring
Funding
Expansion
Website Changes
Product Launch
Direct Inquiry
Demo Request
Content Engagement
```

---

## 20. Lead Segmentation Engine

The system shall support:

```text
Static Segments
Dynamic Segments
AI Segments
Rule-Based Segments
Behavioral Segments
Intent Segments
ICP Segments
Account Segments
```

---

## 21. Prioritization Engine

Lead priority shall be calculated using configurable weights.

Example:

```text
Priority =
ICP Fit
+ Intent
+ Conversion Probability
+ Revenue Potential
+ Engagement
+ Recency
```

---

## 22. Routing Engine

The engine shall support:

```text
Territory Routing
Geographic Routing
Industry Routing
Account Routing
Product Routing
Skill-Based Routing
Capacity-Based Routing
Round Robin
Weighted Round Robin
Revenue-Based Routing
AI Routing
```

---

## 23. Assignment Engine

Leads shall be assignable to:

```text
Sales Agent
SDR
BDR
Sales Team
AI Sales Agent
AI Research Agent
Queue
Account Owner
```

---

## 24. AI Routing

AI routing shall evaluate:

```text
Lead Requirements
Agent Expertise
Historical Conversion
Industry Experience
Territory
Language
Product Expertise
Current Capacity
Account Ownership
```

---

## 25. Human Approval Engine

The platform shall support configurable approval levels:

```text
No Approval
Sampling
Approval for Low Confidence
Approval for High-Value Leads
Approval for Sensitive Leads
Approval for All Leads
```

---

## 26. AI Agent Orchestration

The Lead Generation Engine shall support specialized agents:

```text
LeadGenerationAgent
DiscoveryAgent
ResearchAgent
EnrichmentAgent
VerificationAgent
DeduplicationAgent
QualificationAgent
ScoringAgent
IntentAgent
SegmentationAgent
RoutingAgent
AssignmentAgent
OptimizationAgent
```

Agents shall communicate through controlled orchestration mechanisms.

---

## 27. Agent Tool Permissions

Each agent shall have an explicit tool allowlist.

Example:

```text
DiscoveryAgent
├── search
├── company_lookup
└── contact_lookup

QualificationAgent
├── lead_read
├── company_read
└── scoring_service

RoutingAgent
├── team_read
├── capacity_read
└── assignment_write
```

---

## 28. Agent Execution Policy

Every AI execution shall evaluate:

```text
Permission
Policy
Tenant
Data Scope
Action Scope
Budget
Rate Limit
Risk Level
Human Approval
```

---

## 29. Human-in-the-Loop Workflow

```text
AI Generates Lead
        ↓
Confidence Evaluation
        ↓
Policy Evaluation
        ↓
Automatic Approval?
     /       \
   YES        NO
   ↓          ↓
Continue   Human Queue
              ↓
        Human Review
          /       \
      Approve     Reject
         ↓          ↓
      Continue    Stop
```

---

## 30. Lead Generation State Machine

```text
DISCOVERED
    ↓
NORMALIZED
    ↓
RESOLVED
    ↓
DEDUPLICATED
    ↓
ENRICHED
    ↓
VERIFIED
    ↓
QUALIFIED
    ↓
SCORED
    ↓
SEGMENTED
    ↓
PRIORITIZED
    ↓
APPROVED
    ↓
ROUTED
    ↓
ASSIGNED
    ↓
NURTURED
    ↓
OUTREACHED
    ↓
SALES_READY
    ↓
OPPORTUNITY
    ↓
DEAL
    ↓
CUSTOMER
```

Terminal/alternative states:

```text
REJECTED
DISQUALIFIED
DUPLICATE
INVALID
STALE
SUPPRESSED
UNSUBSCRIBED
ARCHIVED
```

---

## 31. Event Requirements

The engine shall publish events including:

```text
LeadGenerationCampaignCreated
LeadGenerationStarted
LeadGenerationPaused
LeadGenerationResumed
LeadGenerationCompleted
LeadGenerationFailed

LeadDiscovered
LeadNormalized
LeadResolved
LeadDeduplicated
LeadEnriched
LeadVerified
LeadQualified
LeadScoreUpdated
LeadIntentDetected
LeadSegmented
LeadPrioritized
LeadRouted
LeadAssigned

AIResearchStarted
AIResearchCompleted
AIDecisionCreated
AIRecommendationCreated
AIReviewRequested

HumanReviewStarted
HumanApproved
HumanRejected
HumanOverrideCreated

OpportunityCreated
DealCreated
RevenueAttributed
```

---

## 32. Lead Generation API

Conceptual API surface:

```http
POST   /api/v1/lead-generation
GET    /api/v1/lead-generation
GET    /api/v1/lead-generation/{generation_id}

POST   /api/v1/lead-generation/{generation_id}/preview
POST   /api/v1/lead-generation/{generation_id}/dry-run
POST   /api/v1/lead-generation/{generation_id}/start
POST   /api/v1/lead-generation/{generation_id}/pause
POST   /api/v1/lead-generation/{generation_id}/resume
POST   /api/v1/lead-generation/{generation_id}/cancel

GET    /api/v1/lead-generation/{generation_id}/status
GET    /api/v1/lead-generation/{generation_id}/results

POST   /api/v1/lead-generation/discover
POST   /api/v1/lead-generation/enrich
POST   /api/v1/lead-generation/verify
POST   /api/v1/lead-generation/qualify
POST   /api/v1/lead-generation/score
POST   /api/v1/lead-generation/segment
POST   /api/v1/lead-generation/route
POST   /api/v1/lead-generation/assign

GET    /api/v1/lead-generation/analytics
GET    /api/v1/lead-generation/cost
GET    /api/v1/lead-generation/performance
```

---

## 33. Data Model

## LeadGenerationJob

```text
LeadGenerationJob
├── id
├── tenant_id
├── organization_id
├── workplace_id
├── campaign_id
├── created_by
├── generation_strategy
├── icp_id
├── target_criteria
├── sources
├── enrichment_policy
├── qualification_policy
├── scoring_policy
├── routing_policy
├── approval_policy
├── target_quantity
├── budget
├── schedule
├── status
├── progress
├── error_state
├── created_at
├── started_at
├── completed_at
└── updated_at
```

---

## 34. Generated Lead Model

```text
GeneratedLead
├── id
├── tenant_id
├── organization_id
├── workplace_id
├── generation_job_id
├── campaign_id
├── company_id
├── contact_id
├── source
├── source_record_id
├── source_timestamp
├── verification_status
├── qualification_status
├── icp_score
├── fit_score
├── intent_score
├── lead_score
├── conversion_probability
├── revenue_potential
├── lifecycle_stage
├── priority
├── assigned_to
├── assigned_agent_type
├── approval_status
├── consent_status
├── suppression_status
├── created_at
└── updated_at
```

---

## 35. AI Intelligence Record

```text
LeadIntelligence
├── lead_id
├── company_summary
├── contact_summary
├── icp_analysis
├── buying_signals
├── pain_points
├── business_events
├── technology_signals
├── intent
├── buying_stage
├── recommended_action
├── confidence
├── evidence
├── model
├── model_version
├── prompt_version
├── generated_at
└── expires_at
```

---

## 36. AI Decision Record

```text
AIDecision
├── id
├── tenant_id
├── lead_id
├── agent_id
├── decision_type
├── input_context
├── recommendation
├── confidence
├── evidence
├── policy_version
├── model_version
├── human_review_required
├── human_decision
├── override_reason
├── executed_action
└── created_at
```

---

## 37. Human Review Record

```text
HumanReview
├── id
├── lead_id
├── reviewer_id
├── review_type
├── AI_recommendation
├── human_decision
├── override
├── reason
├── notes
├── reviewed_at
└── audit_id
```

---

## 38. Generation Strategy Types

The engine shall support:

```text
ICP_PROSPECTING
ACCOUNT_BASED
MARKET_BASED
COMPETITOR_BASED
TECHNOLOGY_BASED
INTENT_BASED
EVENT_BASED
FUNDING_BASED
HIRING_BASED
JOB_CHANGE_BASED
GEOGRAPHIC
INDUSTRY
ROLE_BASED
AI_AUTONOMOUS
CUSTOM
```

---

## 39. Generation Modes

```text
MANUAL
RULE_BASED
AI_ASSISTED
AI_AUTONOMOUS
HYBRID
EVENT_TRIGGERED
SCHEDULED
CONTINUOUS
```

---

## 40. Continuous Lead Generation

Organizations shall be able to configure always-on generation.

```text
Target Market
      ↓
Monitor Signals
      ↓
Detect New Prospect
      ↓
Generate Lead
      ↓
Enrich
      ↓
Verify
      ↓
Qualify
      ↓
Score
      ↓
Route
      ↓
Assign
      ↓
Notify
```

---

## 41. Trigger Engine

The engine shall support generation triggers such as:

```text
New Funding
New Executive
New Job Posting
Company Expansion
New Technology
New Product
Competitor Adoption
Website Event
High Intent
Inbound Inquiry
CRM Event
Marketing Event
Webhook
External Event
```

---

## 42. Rule Engine

Users shall be able to define conditions.

Example:

```text
IF
company.employee_count >= 50
AND
company.employee_count <= 500
AND
company.industry = "SaaS"
AND
company.funding_recent = true
AND
contact.seniority IN ["VP", "C-Level"]
THEN
generate_lead = true
```

---

## 43. AI + Rules Hybrid

The system shall allow:

```text
Deterministic Rules
+
Machine Learning
+
LLM Reasoning
+
Human Validation
```

to jointly determine lead quality.

---

## 44. Evidence-Based AI

AI shall distinguish between:

```text
Observed Fact
Inferred Signal
Prediction
Recommendation
Unknown
```

AI shall not represent an inference as a verified fact.

---

## 45. Data Freshness

The engine shall track freshness for individual attributes.

Example:

```text
Company Size
├── Last Verified: 2026-08-20
└── Freshness: HIGH

Job Title
├── Last Verified: 2026-08-22
└── Freshness: HIGH

Funding
├── Last Verified: 2026-07-10
└── Freshness: MEDIUM
```

---

## 46. Lead Quality Control

The engine shall identify:

```text
Invalid Lead
Duplicate Lead
Stale Lead
Incomplete Lead
Low ICP Match
Low Intent
Conflicting Data
Unverified Data
High-Risk Data
Low Confidence
```

---

## 47. Lead Suppression

The engine shall exclude leads matching:

```text
Suppression Lists
Opt-Out Lists
Existing Customers
Existing Opportunities
Existing Contacts
Blocked Domains
Blocked Companies
Blocked Regions
Compliance Restrictions
```

unless explicitly overridden by authorized policy.

---

## 48. Existing CRM Matching

Before creating a lead, the engine shall check existing:

```text
Contacts
Accounts
Leads
Opportunities
Deals
Customers
```

to prevent unnecessary duplicates.

---

## 49. Account-Level Intelligence

The engine shall support account-level lead generation.

```text
Target Account
      ↓
Account Intelligence
      ↓
Identify Relevant Departments
      ↓
Identify Buying Committee
      ↓
Discover Contacts
      ↓
Score Contacts
      ↓
Prioritize
```

---

## 50. Multi-Contact Generation

For strategic accounts, the engine shall generate multiple relevant contacts rather than relying on a single prospect.

---

## 51. Lead Generation Optimization

The engine shall calculate:

```text
Lead Volume
Lead Quality
ICP Match Rate
Verification Rate
Qualification Rate
Intent Rate
Conversion Rate
Opportunity Rate
Revenue Rate
Cost per Lead
Cost per Qualified Lead
ROI
```

---

## 52. Source Quality Score

Each lead source shall receive a quality score based on:

```text
Accuracy
Freshness
Coverage
Verification Rate
Qualification Rate
Conversion Rate
Revenue
Cost
```

---

## 53. Campaign Performance

Campaign analytics shall include:

```text
Total Leads
Unique Leads
Duplicates
Verified Leads
Qualified Leads
High-Intent Leads
Sales-Ready Leads
Opportunities
Deals
Revenue
Cost
ROI
```

---

## 54. AI Performance

The system shall measure:

```text
AI Lead Precision
AI Lead Recall
Qualification Accuracy
Scoring Accuracy
Intent Accuracy
Duplicate Detection Accuracy
Enrichment Accuracy
Verification Accuracy
Routing Accuracy
Conversion Prediction Accuracy
Human Override Rate
Human Acceptance Rate
```

---

## 55. Human Performance

The system shall measure:

```text
Review Volume
Review SLA
Approval Rate
Rejection Rate
Override Rate
Lead Conversion
Revenue
Average Processing Time
```

---

## 56. AI Cost Management

The engine shall track:

```text
LLM Calls
Token Usage
Embedding Calls
Search Calls
Research Calls
Enrichment Calls
Verification Calls
Agent Runtime
Provider Costs
Cost per Lead
Cost per Qualified Lead
```

The engine shall support configurable AI budgets.

---

## 57. Budget Governance

Campaigns shall support:

```text
Maximum AI Cost
Maximum Provider Cost
Maximum Lead Count
Maximum Runtime
Maximum API Calls
Maximum Token Usage
```

When limits are reached, the engine shall pause or terminate execution according to policy.

---

## 58. Security Requirements

The engine shall enforce:

```text
Authentication
Authorization
RBAC
Tenant Isolation
Organization Isolation
Workplace Isolation
Encryption
API Security
Secret Management
Rate Limiting
Input Validation
Output Validation
Audit Logging
```

---

## 59. AI Security Requirements

The AI layer shall defend against:

```text
Prompt Injection
Data Exfiltration
Tool Abuse
Unauthorized Actions
Cross-Tenant Retrieval
Malicious External Content
Instruction Hijacking
Data Poisoning
```

External content shall be treated as untrusted input.

---

## 60. Privacy Requirements

The system shall support configurable:

```text
Data Retention
Data Deletion
Data Export
Data Correction
Suppression
Anonymization
Consent
Regional Policies
```

---

## 61. Audit Requirements

The engine shall record:

```text
Campaign Creation
Campaign Modification
Campaign Execution
Campaign Pause
Campaign Cancellation

Lead Discovery
Lead Enrichment
Lead Verification
Lead Qualification
Lead Scoring
Lead Routing
Lead Assignment

AI Decisions
AI Recommendations
AI Tool Calls
Human Approvals
Human Rejections
Human Overrides

Data Export
Data Deletion
Data Merge
Data Suppression
```

---

## 62. Observability

The engine shall expose:

```text
Metrics
Logs
Traces
Events
Health Checks
Provider Health
AI Health
Queue Health
Database Health
```

---

## 63. Operational Metrics

The platform shall monitor:

```text
Generation Throughput
Generation Latency
Queue Depth
Job Failure Rate
Provider Failure Rate
Enrichment Success
Verification Success
Duplicate Rate
Qualification Rate
AI Latency
AI Error Rate
AI Cost
Human Review Queue
Routing Latency
Assignment Success
```

---

## 64. Scalability Requirements

The engine shall be designed to support:

```text
10M+ Leads
Millions of Accounts
Millions of Contacts
Millions of Daily Events
Thousands of Concurrent Jobs
Thousands of Organizations
Large Bulk Campaigns
Continuous Lead Generation
High-Volume AI Processing
```

The engine shall scale horizontally.

---

## 65. Performance Targets

Recommended production targets:

```text
Campaign API P95       < 500 ms
Lead Lookup P95        < 200 ms
Routing P95            < 500 ms
Scoring P95            < 1 sec
Standard Enrichment    < 5 sec
AI Research P95        < 10 sec
```

Bulk operations shall execute asynchronously.

---

## 66. Reliability

The system shall provide:

```text
99.9%+ Availability Target
Retry Policies
Circuit Breakers
Dead-Letter Queues
Idempotency
Checkpointing
Job Recovery
Provider Failover
Graceful Degradation
Data Reconciliation
```

---

## 67. Graceful AI Degradation

When AI services are unavailable:

```text
AI Processing
     ↓
Deterministic Rules
     ↓
Previously Validated Data
     ↓
Human Review
```

The platform shall continue essential lead operations whenever possible.

---

## 68. Notification Requirements

Users shall receive notifications for:

```text
Generation Started
Generation Completed
Generation Failed
High-Value Lead Found
High-Intent Lead Found
Human Review Required
Quota Reached
Budget Reached
Provider Failure
AI Failure
Assignment Completed
```

---

## 69. Human Review SLA

Organizations shall be able to define review SLAs.

Example:

```text
High-Value Lead:
15 minutes

High-Intent Lead:
30 minutes

Normal Lead:
4 hours

Low-Priority Lead:
24 hours
```

---

## 70. Lead Generation Dashboard

The dashboard shall provide:

```text
Generation Overview
├── Leads Generated
├── Verified Leads
├── Qualified Leads
├── High-Intent Leads
├── Sales-Ready Leads
├── Opportunities
├── Deals
└── Revenue

Quality
├── ICP Match Rate
├── Verification Rate
├── Duplicate Rate
├── Qualification Rate
└── Average Lead Score

AI
├── AI Generated
├── AI Accuracy
├── AI Acceptance
├── AI Override
└── AI Cost

Human
├── Review Queue
├── Approval Rate
├── Rejection Rate
├── Override Rate
└── Review SLA

Sources
├── Top Sources
├── Source Quality
├── Source Conversion
└── Source ROI
```

---

## 71. Revenue Attribution

Lead generation shall connect:

```text
Lead
 ↓
Qualified Lead
 ↓
Opportunity
 ↓
Deal
 ↓
Revenue
```

Revenue shall be attributable to:

```text
Campaign
ICP
Lead Source
Generation Strategy
AI Agent
Human Agent
Channel
Market
Segment
```

---

## 72. Feedback Loop

The engine shall learn from:

```text
Approved Leads
Rejected Leads
Qualified Leads
Disqualified Leads
Human Overrides
Outreach Responses
Meetings
Opportunities
Deals
Revenue
```

---

## 73. Continuous Optimization

```text
Generate
   ↓
Measure
   ↓
Evaluate
   ↓
Learn
   ↓
Optimize
   ↓
Generate Better Leads
```

The optimization system shall not automatically modify production policies without authorization.

---

## 74. Experimentation

The engine shall support controlled experiments for:

```text
ICP
Search Strategy
Data Source
Discovery Query
Enrichment Strategy
Qualification Model
Scoring Model
Routing Strategy
AI Agent
```

---

## 75. A/B Testing

Each experiment shall support:

```text
Experiment ID
Control
Variant
Traffic Allocation
Success Metric
Sample Size
Start Time
End Time
Statistical Evaluation
Winner
```

---

## 76. AI Agent Governance

Every AI agent shall have:

```text
Agent ID
Agent Type
Model
Model Version
Prompt Version
Allowed Tools
Allowed Data
Allowed Actions
Tenant Scope
Organization Scope
Permission Scope
Budget
Rate Limit
Approval Policy
Risk Level
```

---

## 77. AI Decision Governance

Every consequential AI decision shall record:

```text
Decision
Input Context
Evidence
Confidence
Model
Model Version
Prompt Version
Policy Version
Human Approval
Human Override
Executed Action
Timestamp
```

---

## 78. Human Authority

Humans shall remain authoritative over AI for:

```text
High-Risk Actions
Compliance Decisions
Sensitive Data
High-Value Accounts
Strategic Accounts
Data Merges
Permanent Deletion
Unauthorized Outreach Prevention
Production Policy Changes
```

---

## 79. End-to-End Example

```text
User:

Find 1,000 SaaS prospects in the US
with 50–500 employees,
recent funding,
active engineering hiring,
and VP/C-level technology decision makers.

        ↓

AI interprets request

        ↓

Creates structured ICP

        ↓

Selects authorized sources

        ↓

Generates discovery queries

        ↓

Discovers companies

        ↓

Discovers relevant contacts

        ↓

Normalizes data

        ↓

Resolves identities

        ↓

Removes duplicates

        ↓

Enriches companies and contacts

        ↓

Verifies available information

        ↓

Analyzes company signals

        ↓

Analyzes buying intent

        ↓

Calculates ICP score

        ↓

Calculates lead score

        ↓

Predicts conversion probability

        ↓

Segments leads

        ↓

Prioritizes high-value prospects

        ↓

Requests human approval when required

        ↓

Routes leads

        ↓

Assigns leads to SDRs / AI agents

        ↓

Starts approved nurture workflow

        ↓

Initiates outreach

        ↓

Tracks engagement

        ↓

Creates opportunities

        ↓

Attributes revenue

        ↓

Feeds outcomes back into optimization
```

---

## 80. Acceptance Criteria

* [ ] Users can create lead-generation campaigns.
* [ ] Users can define ICPs.
* [ ] Users can maintain multiple ICPs.
* [ ] ICP versions are preserved.
* [ ] Natural-language prospecting works.
* [ ] Structured prospecting works.
* [ ] Account-based generation works.
* [ ] Market-based generation works.
* [ ] Intent-based generation works.
* [ ] Trigger-based generation works.
* [ ] Technology-based generation works.
* [ ] Funding-based generation works.
* [ ] Hiring-based generation works.
* [ ] Competitor-based generation works where authorized.
* [ ] Bulk generation works.
* [ ] Scheduled generation works.
* [ ] Recurring generation works.
* [ ] Continuous generation works.
* [ ] Campaign dry runs work.
* [ ] Campaign previews work.
* [ ] Campaign budgets are enforced.
* [ ] Campaign quotas are enforced.
* [ ] Authorized data sources can be configured.
* [ ] Source ranking works.
* [ ] Source provenance is preserved.
* [ ] Data normalization works.
* [ ] Entity resolution works.
* [ ] Deduplication works.
* [ ] Enrichment works.
* [ ] Verification works.
* [ ] Qualification works.
* [ ] AI scoring works.
* [ ] Human scoring overrides work.
* [ ] Intent detection works.
* [ ] Conversion prediction works.
* [ ] Revenue potential estimation works where sufficient evidence exists.
* [ ] Dynamic segmentation works.
* [ ] Lead prioritization works.
* [ ] AI routing works.
* [ ] Rule-based routing works.
* [ ] Manual routing works.
* [ ] Automatic assignment works.
* [ ] Manual assignment works.
* [ ] AI-to-human handoff works.
* [ ] Human-to-AI handoff works.
* [ ] Human approval policies work.
* [ ] AI confidence scores are available.
* [ ] AI decisions are explainable.
* [ ] AI evidence is preserved.
* [ ] AI agent permissions are enforced.
* [ ] AI cannot bypass tenant isolation.
* [ ] AI cannot bypass authorization.
* [ ] AI cannot fabricate verified facts.
* [ ] AI cannot perform unauthorized outreach.
* [ ] Prompt-injection defenses are implemented.
* [ ] Suppression rules are enforced.
* [ ] Consent policies are enforced.
* [ ] Existing CRM records are checked.
* [ ] Duplicate CRM records are prevented.
* [ ] Multi-tenant isolation works.
* [ ] Organization isolation works.
* [ ] Workplace isolation works.
* [ ] RBAC works.
* [ ] Fine-grained permissions work.
* [ ] Asynchronous processing works.
* [ ] Job retry works.
* [ ] Dead-letter handling works.
* [ ] Idempotency works.
* [ ] Rate limiting works.
* [ ] Backpressure works.
* [ ] Distributed locking works where required.
* [ ] Campaign recovery works.
* [ ] AI degradation works.
* [ ] Provider failure handling works.
* [ ] Observability works.
* [ ] Audit logging works.
* [ ] AI decision auditing works.
* [ ] Human override auditing works.
* [ ] Source analytics work.
* [ ] Campaign analytics work.
* [ ] Lead-quality analytics work.
* [ ] AI performance analytics work.
* [ ] Human performance analytics work.
* [ ] AI cost analytics work.
* [ ] Revenue attribution works.
* [ ] ROI calculation works.
* [ ] Feedback loops work.
* [ ] Experimentation works.
* [ ] A/B testing works.
* [ ] Continuous optimization is governed.
* [ ] High-value accounts receive configurable human oversight.
* [ ] The system can scale horizontally.
* [ ] Large campaigns do not block synchronous APIs.
* [ ] Lead-generation failures can be recovered without corrupting lead state.

---

## 81. FAANG-Level Reference Architecture

```text
                         ┌──────────────────────┐
                         │     SalesGenie UI    │
                         │ Human + AI Workspace  │
                         └──────────┬───────────┘
                                    │
                                    ↓
                         ┌──────────────────────┐
                         │ API / Control Plane  │
                         └──────────┬───────────┘
                                    │
                                    ↓
                    ┌──────────────────────────────┐
                    │ Lead Generation Orchestrator │
                    └──────────────┬───────────────┘
                                   │
             ┌─────────────────────┼─────────────────────┐
             ↓                     ↓                     ↓
      ┌─────────────┐       ┌─────────────┐       ┌─────────────┐
      │ ICP Engine  │       │ Rule Engine │       │ Trigger     │
      │             │       │             │       │ Engine      │
      └──────┬──────┘       └──────┬──────┘       └──────┬──────┘
             └─────────────────────┼─────────────────────┘
                                   ↓
                         ┌──────────────────────┐
                         │ AI Agent Orchestrator │
                         └──────────┬───────────┘
                                    │
          ┌────────────┬────────────┼────────────┬────────────┐
          ↓            ↓            ↓            ↓            ↓
      Discovery    Research    Enrichment   Qualification   Scoring
        Agent       Agent        Agent          Agent         Agent
          │            │            │              │             │
          └────────────┴────────────┼──────────────┴─────────────┘
                                    ↓
                         ┌──────────────────────┐
                         │ Data Normalization   │
                         └──────────┬───────────┘
                                    ↓
                         ┌──────────────────────┐
                         │ Entity Resolution    │
                         └──────────┬───────────┘
                                    ↓
                         ┌──────────────────────┐
                         │ Deduplication        │
                         └──────────┬───────────┘
                                    ↓
                         ┌──────────────────────┐
                         │ Verification         │
                         └──────────┬───────────┘
                                    ↓
                         ┌──────────────────────┐
                         │ Intent Intelligence  │
                         └──────────┬───────────┘
                                    ↓
                         ┌──────────────────────┐
                         │ Segmentation         │
                         └──────────┬───────────┘
                                    ↓
                         ┌──────────────────────┐
                         │ Prioritization       │
                         └──────────┬───────────┘
                                    ↓
                    ┌───────────────┴───────────────┐
                    ↓                               ↓
           ┌─────────────────┐             ┌─────────────────┐
           │ Human Review    │             │ AI Governance   │
           │ & Approval      │             │ & Policy Engine │
           └────────┬────────┘             └────────┬────────┘
                    └───────────────┬───────────────┘
                                    ↓
                         ┌──────────────────────┐
                         │ Routing & Assignment │
                         └──────────┬───────────┘
                                    ↓
                       ┌────────────┴────────────┐
                       ↓                         ↓
                ┌─────────────┐           ┌─────────────┐
                │ Human Sales │           │ AI Sales    │
                │ Agents      │           │ Agents      │
                └──────┬──────┘           └──────┬──────┘
                       └────────────┬─────────────┘
                                    ↓
                         ┌──────────────────────┐
                         │ Nurturing / Outreach │
                         └──────────┬───────────┘
                                    ↓
                         ┌──────────────────────┐
                         │ CRM / Opportunity   │
                         └──────────┬───────────┘
                                    ↓
                         ┌──────────────────────┐
                         │ Deals / Revenue      │
                         └──────────┬───────────┘
                                    ↓
                         ┌──────────────────────┐
                         │ Analytics & Feedback │
                         └──────────┬───────────┘
                                    ↓
                         ┌──────────────────────┐
                         │ Optimization Engine  │
                         └──────────┬───────────┘
                                    │
                                    └──────→ Better Generation
```

---

## 82. Ultimate Lead Generation Engine Loop

```text
DEFINE
  ↓
UNDERSTAND
  ↓
DISCOVER
  ↓
NORMALIZE
  ↓
RESOLVE
  ↓
DEDUPLICATE
  ↓
ENRICH
  ↓
VERIFY
  ↓
RESEARCH
  ↓
MATCH
  ↓
QUALIFY
  ↓
SCORE
  ↓
DETECT INTENT
  ↓
SEGMENT
  ↓
PRIORITIZE
  ↓
REVIEW
  ↓
ROUTE
  ↓
ASSIGN
  ↓
NURTURE
  ↓
OUTREACH
  ↓
ENGAGE
  ↓
CONVERT
  ↓
ATTRIBUTE
  ↓
LEARN
  ↓
OPTIMIZE
  ↓
GENERATE BETTER LEADS
  ↺
```

---

## 83. Product-Level Success Definition

The SalesGenie Lead Generation Engine shall not optimize merely for the number of leads generated.

The primary optimization objective shall be:

```text
Verified Lead Quality
        ×
ICP Fit
        ×
Buying Intent
        ×
Conversion Probability
        ×
Revenue Potential
        ×
Sales Capacity
        ÷
Generation Cost
```

The final system shall provide a **scalable, explainable, secure, multi-tenant, AI-powered and human-governed lead-generation engine** capable of continuously discovering and prioritizing high-value prospects while maintaining strict authorization, provenance, privacy, compliance, reliability, observability, cost control, and human oversight.
