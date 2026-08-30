# SalesGenie — Lead Quality Engine

## FAANG-Level User Requirements, System Requirements & Functional Requirements

> **Module:** Lead Quality Engine  
> **Product:** SalesGenie  
> **Purpose:** Evaluate, validate, classify, monitor, and continuously improve the quality, usability, reliability, completeness, authenticity, relevance, and commercial readiness of leads using deterministic rules, AI/ML models, external intelligence, and authorized human judgment.

---

## 1. Executive Objective

The SalesGenie Lead Quality Engine shall determine whether a lead is:

- Valid
- Authentic
- Complete
- Relevant
- ICP-aligned
- Contactable
- Engaged
- Commercially viable
- Sales-ready
- Nurture-ready
- Potentially fraudulent
- Duplicate
- Stale
- Incomplete
- Low-quality
- Disqualified

The engine shall evaluate lead quality across multiple dimensions rather than relying on a single score.

The system shall answer:

1. Is this lead real?
2. Is the contact information valid?
3. Does the person actually belong to the company?
4. Does the company exist?
5. Does the company match the ICP?
6. Is the contact relevant to the product?
7. Is the lead reachable?
8. Is the lead engaged?
9. Is the lead showing buying intent?
10. Is the available information complete?
11. Is the information fresh?
12. Is the lead duplicated?
13. Is the lead suspicious or fraudulent?
14. Is the lead sales-ready?
15. What evidence supports the quality assessment?
16. How confident is the assessment?
17. What information is missing?
18. What should AI do next?
19. What should a human salesperson do next?
20. Should the lead be accepted, enriched, verified, routed, nurtured, or rejected?

---

## 2. Core Principles

The Lead Quality Engine shall follow these principles:

1. Quality shall be multi-dimensional.
2. AI shall not fabricate lead-quality evidence.
3. Human decisions shall be auditable.
4. Automated decisions shall follow organizational policies.
5. Unknown data shall not automatically be treated as bad data.
6. External information shall have provenance.
7. Stale information shall reduce confidence where appropriate.
8. Duplicate detection shall be independent from quality scoring.
9. Verification shall be independent from qualification.
10. A valid lead is not necessarily a qualified lead.
11. A qualified lead is not necessarily sales-ready.
12. AI recommendations shall be distinguishable from authoritative human decisions.
13. Human overrides shall preserve the original AI/system assessment.
14. All quality changes shall be versioned.
15. All tenants shall remain strictly isolated.
16. Quality assessments shall be explainable.
17. High-impact automated actions shall be policy-controlled.
18. Quality models shall be continuously evaluated.
19. Model drift shall be monitored.
20. Feedback shall be used to improve future quality assessment.

---

## 3. Lead Quality Dimensions

The engine shall support at least:

```text
Identity Quality
Contactability
Company Validity
Contact Validity
Data Completeness
Data Freshness
Data Consistency
ICP Fit
Role Relevance
Firmographic Fit
Technographic Fit
Engagement Quality
Intent Quality
Behavioral Quality
Source Quality
Verification Quality
Duplicate Risk
Fraud Risk
Spam Risk
Commercial Readiness
Sales Readiness
Overall Lead Quality
```

---

## 4. User Personas

## 4.1 Super Admin

The Super Admin shall be able to:

* Configure global quality-engine capabilities.
* Manage quality models.
* Manage AI/ML providers.
* Configure platform-wide quality policies.
* Monitor quality-engine health.
* Monitor model performance.
* Monitor AI costs.
* Review platform-level audit logs.
* Configure global feature flags.
* Configure quality thresholds.
* Configure system-wide safety controls.

---

## 4.2 Organization Admin

The Organization Admin shall be able to:

* Configure lead-quality policies.
* Configure quality dimensions.
* Configure scoring weights.
* Configure thresholds.
* Configure verification policies.
* Configure AI automation policies.
* Configure human-review requirements.
* Review quality analytics.
* Manage quality models.
* Configure data-retention policies.

---

## 4.3 Workplace Admin

The Workplace Admin shall be able to:

* Configure team-specific quality policies.
* Configure quality thresholds.
* Configure verification workflows.
* Configure human-review queues.
* Review quality reports.

---

## 4.4 Sales Manager

The Sales Manager shall be able to:

* View lead-quality scores.
* Review low-quality leads.
* Review high-quality leads.
* Configure quality criteria.
* Approve/reject AI recommendations.
* Override quality classifications.
* Review quality trends.
* Analyze quality by lead source.
* Analyze quality by sales agent.
* Analyze quality by campaign.
* Analyze quality by segment.

---

## 4.5 Sales Agent

The Sales Agent shall be able to:

* View lead-quality status.
* View quality score.
* View quality dimensions.
* View verification results.
* View missing data.
* View stale data.
* View duplicate warnings.
* View risk indicators.
* Provide feedback.
* Request verification.
* Request enrichment.
* Request rescoring.
* Override quality where authorized.

---

## 4.6 AI Sales Agent

The AI Sales Agent shall be able to:

* Evaluate lead quality.
* Analyze structured data.
* Analyze unstructured lead information.
* Detect inconsistencies.
* Identify missing information.
* Identify suspicious patterns.
* Recommend enrichment.
* Recommend verification.
* Recommend qualification.
* Recommend rejection.
* Generate quality explanations.

The AI Sales Agent shall operate only within explicit permissions.

---

## 5. User Requirements

## UR-001 — Lead Quality Visibility

Users shall be able to view:

* Overall quality score
* Quality classification
* Confidence
* Identity quality
* Contact quality
* Company quality
* Data completeness
* Data freshness
* ICP fit
* Engagement quality
* Intent quality
* Verification status
* Duplicate status
* Fraud risk
* Spam risk
* Sales readiness
* Missing information

---

## UR-002 — Quality Classification

The system shall support configurable classifications such as:

```text
EXCELLENT
HIGH
GOOD
MEDIUM
LOW
POOR
INVALID
SUSPICIOUS
DISQUALIFIED
```

Organizations shall be able to configure their own classifications.

---

## UR-003 — Lead Validity

Users shall be able to determine whether:

* Lead exists
* Company exists
* Contact exists
* Email appears valid
* Phone appears valid
* Domain appears valid
* Contact-company relationship appears valid

---

## UR-004 — Data Completeness

Users shall be able to identify:

* Missing email
* Missing phone
* Missing company
* Missing title
* Missing industry
* Missing location
* Missing revenue
* Missing employee count
* Missing website
* Missing buying context

---

## UR-005 — Data Freshness

The system shall display freshness of:

* Contact information
* Company information
* Job title
* Technology data
* Intent signals
* Engagement signals
* Firmographic information

---

## UR-006 — Contactability

The system shall determine whether a lead is reasonably contactable.

It shall evaluate:

* Email validity
* Email deliverability indicators
* Phone validity
* Contact status
* Opt-out status
* Bounce history
* Communication restrictions

---

## UR-007 — Company Quality

The system shall evaluate:

* Company existence
* Website availability
* Industry
* Company size
* Revenue
* Growth
* Location
* Business model
* Technology
* Market relevance

---

## UR-008 — Contact Quality

The system shall evaluate:

* Name validity
* Job title
* Seniority
* Department
* Decision-making relevance
* Company association
* Contact information
* Role relevance

---

## UR-009 — ICP Quality

The system shall evaluate how closely a lead matches the organization's ICP.

---

## UR-010 — Engagement Quality

The system shall evaluate whether engagement represents meaningful interest.

Examples:

* Demo request
* Product-page visits
* Pricing-page visits
* Email reply
* Meeting booking
* Content download
* Trial activity

---

## UR-011 — Intent Quality

The system shall distinguish between:

```text
Low Intent
Moderate Intent
High Intent
Buying Intent
Unknown Intent
```

---

## UR-012 — Source Quality

The system shall evaluate the quality of the lead source.

Supported sources may include:

* Website
* Organic search
* Paid advertising
* Referral
* CRM import
* Manual entry
* API
* Partner
* Campaign
* Event
* Lead-generation provider
* AI discovery
* External data provider

---

## UR-013 — Duplicate Detection

Users shall be informed when:

* Lead duplicates another lead.
* Contact duplicates another contact.
* Company duplicates another company.
* Email already exists.
* Domain already exists.
* Phone already exists.

---

## UR-014 — Fraud and Spam Risk

The system shall identify suspicious patterns.

Examples:

* Disposable email
* Suspicious domain
* Fake company information
* Repeated submissions
* Bot-like behavior
* Impossible data combinations
* High-volume automated activity
* Known spam patterns

---

## UR-015 — Quality Explanation

Users shall be able to see why a lead was classified as high or low quality.

Example:

```text
Quality Score: 91/100

Positive:
+ Verified company
+ Verified professional email
+ Strong ICP match
+ Relevant decision-maker
+ Recent product engagement

Negative:
- Phone number not verified

Confidence: 94%
```

---

## UR-016 — Evidence

Users shall be able to inspect supporting evidence for major quality decisions.

---

## UR-017 — Missing Information

The system shall explicitly identify information required to improve quality.

Example:

```text
Missing:
- Annual revenue
- Employee count
- Technology stack
```

---

## UR-018 — Quality Improvement Recommendations

The engine shall recommend:

* Enrich lead
* Verify email
* Verify phone
* Verify company
* Research contact
* Detect duplicate
* Request human review
* Nurture
* Disqualify

---

## UR-019 — Human Review

Users shall be able to review AI-generated quality decisions.

The review interface shall display:

* Current quality
* AI recommendation
* Evidence
* Confidence
* Risk
* Missing data
* Recommended action

---

## UR-020 — Human Override

Authorized users shall be able to override:

* Quality score
* Quality classification
* Verification state
* Disqualification state
* Risk classification

Overrides shall require reasons where configured.

---

## UR-021 — Quality History

Users shall be able to inspect how lead quality changed over time.

---

## UR-022 — Quality Alerts

Users shall be able to receive alerts when:

* Quality drops.
* Quality improves.
* Verification fails.
* Fraud risk increases.
* Duplicate is detected.
* Lead becomes sales-ready.
* Important data becomes stale.

---

## UR-023 — Bulk Quality Evaluation

Users shall be able to evaluate:

* Single lead
* Multiple leads
* Segment
* Campaign
* Entire organization

---

## UR-024 — Quality Filtering

Users shall be able to filter leads by:

* Quality score
* Quality classification
* Verification status
* Completeness
* Freshness
* Fraud risk
* Duplicate risk
* ICP fit
* Intent
* Source

---

## UR-025 — Quality Comparison

Users shall be able to compare lead quality across:

* Sources
* Campaigns
* Industries
* Regions
* Teams
* Sales agents
* Segments
* Time periods

---

## UR-026 — Quality Feedback

Users shall be able to report:

```text
Correct
Incorrect
Too High
Too Low
Invalid Lead
Wrong Contact
Wrong Company
Duplicate
Spam
Missing Information
Incorrect Classification
```

---

## 6. System Requirements

## SR-001 — Multi-Tenant Isolation

The engine shall enforce tenant isolation for:

* Leads
* Contacts
* Companies
* Scores
* Features
* Models
* Quality policies
* AI context
* Verification results
* Audit logs
* Feedback
* Analytics

---

## SR-002 — Authentication

All protected endpoints shall require authentication.

Supported mechanisms may include:

* JWT
* OAuth
* Service-to-service authentication
* API credentials
* Machine identity

---

## SR-003 — Authorization

The system shall support:

* RBAC
* Permission-based access
* Resource-level permissions
* Organization-level permissions
* Workplace-level permissions
* AI-agent permissions

---

## SR-004 — Least Privilege

AI agents shall receive only the permissions required for their assigned task.

---

## SR-005 — Quality Engine Architecture

```text
                     Lead Quality Engine
                              |
          +-------------------+-------------------+
          |                   |                   |
          ▼                   ▼                   ▼
   Validation Engine    Intelligence Engine   AI Engine
          |                   |                   |
          ▼                   ▼                   ▼
   Data Quality         Enrichment/Signals   LLM Reasoning
          |                   |                   |
          +-------------------+-------------------+
                              |
                              ▼
                    Quality Scoring Engine
                              |
                              ▼
                     Risk Classification
                              |
                              ▼
                    Confidence Engine
                              |
                              ▼
                    Explainability Engine
                              |
                              ▼
                   Recommendation Engine
                              |
                  +-----------+-----------+
                  ▼                       ▼
             Human Review           Automation
```

---

## SR-006 — Validation Engine

The system shall validate:

* Required fields
* Email structure
* Phone structure
* Domain structure
* URL validity
* Data types
* Enumerations
* Field relationships

---

## SR-007 — Verification Integration

The engine shall support integration with authorized verification providers.

Verification results shall contain:

* Provider
* Result
* Confidence
* Timestamp
* Source
* Expiration
* Provider response reference

---

## SR-008 — Enrichment Integration

The engine shall be able to request additional data from authorized enrichment systems.

---

## SR-009 — AI Evaluation

The AI engine shall evaluate:

* Unstructured information
* Context
* Contradictions
* Relevance
* Suspicious patterns
* Business intent
* Contact relevance

---

## SR-010 — ML Quality Models

The system shall support ML models for:

* Lead quality classification
* Lead validity prediction
* Conversion-quality prediction
* Spam detection
* Fraud-risk prediction
* Duplicate-risk prediction
* Contactability prediction

---

## SR-011 — Rule Engine

The system shall support deterministic rules.

Example:

```text
IF email_status = invalid
THEN contactability_score = 0

IF duplicate_probability > threshold
THEN duplicate_risk = HIGH

IF company_verified = false
THEN company_quality <= configured_limit
```

---

## SR-012 — Quality Score Fusion

The final quality score shall combine multiple dimensions.

Example:

```text
Data Quality
+
Identity Quality
+
Contactability
+
Company Quality
+
ICP Fit
+
Engagement
+
Intent
+
Verification
-
Risk Penalties
```

---

## SR-013 — Score Normalization

Default quality score:

```text
0–100
```

---

## SR-014 — Quality Confidence

Every AI/ML quality assessment shall contain confidence.

---

## SR-015 — Model Versioning

Every model-based assessment shall record:

```yaml
model_name:
model_version:
feature_version:
policy_version:
prompt_version:
```

---

## SR-016 — Explainability

The engine shall retain feature contributions and evidence.

---

## SR-017 — Data Provenance

Every external quality signal shall record:

```yaml
source:
source_type:
retrieved_at:
verified_at:
expires_at:
confidence:
```

---

## SR-018 — Freshness Management

The engine shall classify data as:

```text
Fresh
Aging
Stale
Expired
Unknown
```

---

## SR-019 — Unknown State

Missing or unverifiable information shall be represented as:

```text
UNKNOWN
```

rather than automatically being classified as:

```text
INVALID
```

---

## SR-020 — Conflict Detection

The system shall identify conflicting information.

Example:

```text
CRM:
CEO

External Source:
VP Sales
```

The engine shall preserve both values and determine the authoritative value according to configured source priority.

---

## SR-021 — Event-Driven Architecture

The system shall process events such as:

```text
lead.created
lead.updated
lead.enriched
contact.updated
company.updated
email.verified
email.bounced
phone.verified
website.updated
lead.engaged
intent.detected
duplicate.detected
fraud.detected
```

---

## SR-022 — Idempotency

Repeated events shall not produce duplicate quality records.

---

## SR-023 — Asynchronous Processing

Expensive operations shall be asynchronous.

Examples:

* External verification
* AI analysis
* Batch evaluation
* Enrichment
* Deep research

---

## SR-024 — Queue Architecture

The system shall support:

* Job queues
* Retry queues
* Dead-letter queues
* Priority queues
* Delayed queues

---

## SR-025 — Retry Policy

The system shall implement:

* Exponential backoff
* Maximum retry count
* Error classification
* Provider fallback
* Dead-letter handling

---

## SR-026 — Circuit Breaker

External providers shall be protected using circuit breakers.

---

## SR-027 — Rate Limiting

Rate limits shall support:

* User
* Tenant
* Organization
* API
* Provider
* AI agent
* Batch job

---

## SR-028 — AI Cost Tracking

The system shall track:

* LLM calls
* Tokens
* Model
* Provider
* Enrichment calls
* Verification calls
* Estimated cost

---

## SR-029 — Observability

The service shall expose:

* Health checks
* Readiness checks
* Metrics
* Structured logs
* Distributed tracing
* Error monitoring

---

## SR-030 — Correlation

Every quality operation shall support:

```text
request_id
correlation_id
trace_id
tenant_id
lead_id
```

---

## 7. Functional Requirements

## 7.1 Lead Quality Evaluation

## FR-001 — Evaluate Lead Quality

The system shall evaluate a lead across all enabled quality dimensions.

---

## FR-002 — Calculate Overall Quality Score

The system shall calculate:

```yaml
quality:
  overall: 91
  identity: 98
  contactability: 94
  company: 96
  completeness: 87
  freshness: 89
  consistency: 93
  icp_fit: 92
  engagement: 82
  intent: 88
  verification: 95
  duplicate_risk: 2
  fraud_risk: 1
```

---

## 7.2 Identity Quality

## FR-003 — Contact Identity Validation

The system shall validate:

* Name
* Email
* Phone
* Company
* Job title

---

## FR-004 — Company Identity Validation

The system shall evaluate:

* Company name
* Domain
* Website
* Business presence
* Company consistency

---

## 7.3 Contactability

## FR-005 — Email Quality

The engine shall support:

```text
Valid
Invalid
Risky
Disposable
Role-Based
Unknown
```

---

## FR-006 — Phone Quality

The system shall support:

```text
Valid
Invalid
Unknown
Unverified
Verified
```

---

## FR-007 — Communication Eligibility

The system shall check:

* Opt-out status
* Suppression list
* Bounce history
* Communication restrictions

The engine shall not recommend outreach when organizational policies prohibit it.

---

## 7.4 Data Completeness

## FR-008 — Completeness Calculation

Example:

```text
Required fields:
10

Available:
9

Completeness:
90%
```

---

## FR-009 — Field-Level Completeness

The engine shall identify missing fields individually.

---

## 7.5 Data Freshness

## FR-010 — Freshness Calculation

The system shall calculate freshness using configurable time windows.

---

## FR-011 — Stale Data Detection

The engine shall flag data that exceeds configured freshness limits.

---

## 7.6 Data Consistency

## FR-012 — Cross-Field Validation

The system shall identify impossible or suspicious combinations.

Examples:

```text
Company size = 1
Revenue = $5B

Title = CEO
Department = Engineering

Country = Bangladesh
Phone country code = United States
```

Such combinations shall be flagged for review rather than automatically rejected unless a deterministic policy says otherwise.

---

## 7.7 Company Quality

## FR-013 — Company Verification

The engine shall evaluate whether the company appears authentic and relevant.

---

## FR-014 — Company Profile Quality

The system shall evaluate:

```text
Industry
Revenue
Employees
Location
Growth
Funding
Technology
Business model
Website
Market
```

---

## 7.8 Contact Quality

## FR-015 — Role Relevance

The engine shall evaluate whether the contact's role is relevant to the target product.

---

## FR-016 — Seniority

The engine shall classify:

```text
Founder
C-Level
VP
Director
Manager
Individual Contributor
Other
Unknown
```

---

## 7.9 ICP Fit

## FR-017 — ICP Evaluation

The engine shall compare lead attributes against the organization's ICP.

---

## FR-018 — ICP Mismatch Detection

The engine shall identify:

* Wrong industry
* Wrong geography
* Wrong company size
* Wrong business model
* Wrong technology
* Wrong use case

---

## 7.10 Engagement Quality

## FR-019 — Engagement Analysis

The system shall analyze:

* Frequency
* Recency
* Depth
* Intent relevance
* Channel
* Interaction quality

Repeated low-value activity shall not necessarily equal high-quality engagement.

---

## 7.11 Intent Quality

## FR-020 — Intent Validation

The engine shall distinguish:

```text
Activity
Interest
Intent
Buying Intent
```

---

## FR-021 — Intent Freshness

Intent signals shall decay over time.

---

## 7.12 Duplicate Detection

## FR-022 — Duplicate Risk

The system shall evaluate:

* Exact email
* Exact phone
* Domain
* Name
* Company
* Fuzzy identity
* Contact-company relationships

---

## FR-023 — Duplicate Confidence

The engine shall provide:

```yaml
duplicate:
  probability: 0.94
  matched_lead_id:
  reasons:
    - email_match
    - company_match
    - name_similarity
```

---

## 7.13 Fraud and Spam

## FR-024 — Fraud Risk

The system shall calculate fraud risk using authorized signals.

---

## FR-025 — Spam Detection

The engine shall detect:

* Bot-like activity
* Repeated submissions
* Suspicious email patterns
* Disposable domains
* Automated behavior
* Spam indicators

---

## 7.14 Quality Scoring

## FR-026 — Weighted Quality Model

Example:

```text
Identity Quality          15%
Contactability            15%
Company Quality           15%
Data Completeness         10%
Data Freshness             5%
Data Consistency           5%
ICP Fit                   15%
Engagement                10%
Intent                     5%
Verification               5%
```

Organizations shall be able to configure weights.

---

## 7.15 Risk Penalties

## FR-027 — Risk Adjustment

The engine shall support configurable penalties for:

```text
Fraud risk
Spam risk
Duplicate risk
Invalid contact
Invalid company
Stale data
Policy violation
```

---

## 7.16 Quality Classification

## FR-028 — Classification

Example:

```yaml
EXCELLENT:
  min: 90

HIGH:
  min: 75

GOOD:
  min: 60

MEDIUM:
  min: 40

LOW:
  min: 20

POOR:
  min: 0
```

---

## 7.17 Confidence

## FR-029 — Confidence Calculation

Confidence shall depend on:

* Data availability
* Data freshness
* Verification quality
* Source reliability
* Model confidence
* Signal consistency

---

## 7.18 Quality Explanation

## FR-030 — Generate Explanation

The system shall generate structured explanations.

```yaml
explanation:
  summary:
  positive_factors:
  negative_factors:
  risks:
  missing_data:
  evidence:
  confidence:
  recommended_actions:
```

---

## 7.19 Evidence

## FR-031 — Evidence Linking

Each important quality factor should link to its source.

---

## 7.20 Quality Recommendations

## FR-032 — Recommend Improvement

The engine shall recommend the most effective next quality-improvement action.

Example:

```text
Current Quality: 62

Recommended:
1. Verify company
2. Enrich employee count
3. Verify phone
4. Confirm contact role
```

---

## 7.21 AI Quality Agent

## FR-033 — AI Evaluation

The AI agent shall evaluate complex cases.

---

## FR-034 — AI Contradiction Detection

The AI shall identify contradictory information.

---

## FR-035 — AI Missing-Data Analysis

The AI shall identify which missing data has the highest expected value.

---

## 7.22 Human Review

## FR-036 — Review Queue

The system shall create review cases when:

* Confidence is low.
* Fraud risk is high.
* Data conflicts.
* AI is uncertain.
* Duplicate probability is ambiguous.
* High-value lead has questionable data.
* Policy requires approval.

---

## FR-037 — Review Actions

Humans shall be able to:

```text
Approve
Reject
Modify
Verify
Request Enrichment
Request Rescore
Mark Duplicate
Mark Valid
Mark Invalid
```

---

## 7.23 Human Override

## FR-038 — Override Quality

Authorized humans may override quality decisions.

The system shall preserve:

```yaml
original_assessment:
human_assessment:
reason:
actor:
timestamp:
```

---

## 7.24 Quality History

## FR-039 — Store Quality Versions

Each quality evaluation shall store:

```yaml
version:
score:
classification:
model_version:
policy_version:
feature_version:
created_at:
```

---

## 7.25 Quality Change Detection

## FR-040 — Detect Quality Changes

The engine shall detect:

```text
Score increase
Score decrease
Classification change
Risk increase
Risk decrease
Verification change
Data-quality change
```

---

## 7.26 Event Processing

## FR-041 — Process Lead Events

The engine shall process:

```text
lead.created
lead.updated
lead.enriched
lead.verified
contact.updated
company.updated
email.verified
email.bounced
phone.verified
lead.engaged
intent.detected
duplicate.detected
fraud.detected
```

---

## 7.27 Event Publishing

## FR-042 — Publish Quality Events

The system shall publish:

```text
lead.quality.updated
lead.quality.improved
lead.quality.degraded
lead.quality.high
lead.quality.low
lead.quality.invalid
lead.quality.review_required
lead.quality.duplicate
lead.quality.fraud_risk
lead.quality.verified
```

---

## 7.28 Batch Evaluation

## FR-043 — Batch Quality Evaluation

The system shall support asynchronous batch evaluation.

---

## FR-044 — Batch Progress

Users shall be able to monitor:

```yaml
job:
  total:
  processed:
  successful:
  failed:
  percentage:
  status:
```

---

## 7.29 API Requirements

## FR-045 — Evaluate Lead

```http
POST /api/v1/lead-quality/leads/{lead_id}/evaluate
```

---

## FR-046 — Get Quality

```http
GET /api/v1/lead-quality/leads/{lead_id}
```

---

## FR-047 — Get Explanation

```http
GET /api/v1/lead-quality/leads/{lead_id}/explanation
```

---

## FR-048 — Get Quality History

```http
GET /api/v1/lead-quality/leads/{lead_id}/history
```

---

## FR-049 — Request Verification

```http
POST /api/v1/lead-quality/leads/{lead_id}/verify
```

---

## FR-050 — Request Enrichment

```http
POST /api/v1/lead-quality/leads/{lead_id}/enrich
```

---

## FR-051 — Submit Feedback

```http
POST /api/v1/lead-quality/leads/{lead_id}/feedback
```

---

## FR-052 — Override Quality

```http
POST /api/v1/lead-quality/leads/{lead_id}/override
```

---

## FR-053 — Batch Evaluation

```http
POST /api/v1/lead-quality/batch
```

---

## 8. Quality Engine Pipeline

```text
Lead Created
     ↓
Identity Validation
     ↓
Contact Validation
     ↓
Company Validation
     ↓
Duplicate Detection
     ↓
Fraud/Spam Analysis
     ↓
Data Completeness
     ↓
Data Freshness
     ↓
Data Consistency
     ↓
ICP Evaluation
     ↓
Engagement Evaluation
     ↓
Intent Evaluation
     ↓
Verification
     ↓
ML Quality Prediction
     ↓
AI Contextual Evaluation
     ↓
Score Fusion
     ↓
Risk Adjustment
     ↓
Confidence Calculation
     ↓
Explanation Generation
     ↓
Quality Classification
     ↓
Human Review if Required
     ↓
Quality Decision
     ↓
Recommended Action
     ↓
Workflow / Routing
     ↓
Store Quality Version
```

---

## 9. Recommended Architecture

```text
                         SALES GENIE
                              |
                              ▼
                      API / Event Gateway
                              |
                              ▼
                    Lead Quality Service
                              |
       +----------------------+----------------------+
       |                      |                      |
       ▼                      ▼                      ▼
Validation Service     Intelligence Service      AI Service
       |                      |                      |
       ▼                      ▼                      ▼
Email/Phone           Enrichment/Intent        LLM Reasoning
Verification          Company/Contact          Explanation
       |                      |                      |
       +----------------------+----------------------+
                              |
                              ▼
                    Quality Feature Engine
                              |
                              ▼
                     ML Quality Models
                              |
                              ▼
                     Quality Score Fusion
                              |
                              ▼
                       Risk Engine
                              |
                              ▼
                     Confidence Engine
                              |
                              ▼
                  Explainability Engine
                              |
                              ▼
                 Recommendation Engine
                              |
                    +---------+---------+
                    ▼                   ▼
              Human Review        Automation
                    |                   |
                    +---------+---------+
                              |
                              ▼
                     SalesGenie Workflow
                              |
              +---------------+---------------+
              ▼               ▼               ▼
           CRM            Routing          Nurturing
```

---

## 10. Quality Score Example

```yaml
lead_quality:
  overall_score: 91

  dimensions:
    identity: 98
    contactability: 94
    company_quality: 96
    completeness: 87
    freshness: 89
    consistency: 93
    icp_fit: 92
    engagement: 82
    intent: 88
    verification: 95

  risks:
    duplicate: 0.02
    fraud: 0.01
    spam: 0.03

  confidence: 94

  classification: EXCELLENT
```

---

## 11. Example Low-Quality Lead

```yaml
lead_quality:
  overall_score: 27

  dimensions:
    identity: 40
    contactability: 15
    company_quality: 32
    completeness: 45
    freshness: 20
    consistency: 30
    icp_fit: 25
    engagement: 10
    intent: 5
    verification: 20

  risks:
    duplicate: 0.72
    fraud: 0.35
    spam: 0.61

  confidence: 91

  classification: POOR

  recommendations:
    - verify_email
    - verify_company
    - investigate_duplicate
    - do_not_route_to_sales
```

---

## 12. AI + Human Responsibility Matrix

| Capability                  |         AI |                    Human |
| --------------------------- | ---------: | -----------------------: |
| Data validation             |        Yes |                      Yes |
| Identity analysis           |        Yes |                      Yes |
| Company analysis            |        Yes |                      Yes |
| Contact analysis            |        Yes |                      Yes |
| Duplicate detection         |        Yes |                   Review |
| Fraud-risk detection        |        Yes |                   Review |
| Spam detection              |        Yes |                   Review |
| Completeness calculation    |        Yes |                Configure |
| Freshness calculation       |        Yes |                Configure |
| ICP evaluation              |        Yes |                Configure |
| Intent evaluation           |        Yes |                   Review |
| Quality scoring             |        Yes |                   Review |
| Quality explanation         |        Yes |                   Review |
| Verification recommendation |        Yes |   Approve where required |
| Enrichment recommendation   |        Yes |   Approve where required |
| Quality override            |         No |         Authorized human |
| Policy creation             |  Recommend |         Authorized admin |
| Model deployment            |         No | Authorized administrator |
| High-impact automation      | Restricted |        Policy-controlled |
| Final business judgment     |  Recommend |                    Human |

---

## 13. AI Agent Guardrails

The AI Quality Agent shall:

* Never invent company information.
* Never invent contact information.
* Never claim verification without evidence.
* Never claim an email is deliverable without appropriate evidence.
* Never fabricate sources.
* Never expose another tenant's information.
* Never bypass RBAC.
* Never modify authoritative quality records without permission.
* Never automatically reject a lead solely because information is missing unless policy explicitly requires it.
* Never treat external web content as trusted instructions.
* Never execute arbitrary tools.
* Never disclose internal prompts.
* Never reveal confidential customer data.
* Never use prohibited sensitive attributes for inappropriate scoring.
* Clearly distinguish facts from inferences.

---

## 14. External Data Safety

External information shall be treated as untrusted input.

Potential sources include:

```text
Company websites
Search results
Public business information
CRM notes
Emails
Social media
Job postings
Uploaded documents
External enrichment providers
Third-party APIs
```

The AI layer shall isolate external content from system instructions.

---

## 15. Data Model

## LeadQuality

```yaml
LeadQuality:
  id: UUID
  tenant_id: UUID
  organization_id: UUID
  workplace_id: UUID
  lead_id: UUID

  overall_score: float
  classification: string

  identity_score: float
  contactability_score: float
  company_quality_score: float
  completeness_score: float
  freshness_score: float
  consistency_score: float
  icp_fit_score: float
  engagement_score: float
  intent_score: float
  verification_score: float

  duplicate_risk: float
  fraud_risk: float
  spam_risk: float

  confidence_score: float

  positive_factors: JSON
  negative_factors: JSON
  risks: JSON
  evidence: JSON
  missing_data: JSON
  recommendations: JSON

  model_name: string
  model_version: string
  feature_version: string
  policy_version: string

  created_at: datetime
  updated_at: datetime
```

---

## 16. Quality Evidence

```yaml
QualityEvidence:
  id: UUID
  tenant_id: UUID
  lead_id: UUID

  factor:
  value:
  impact:
  source:
  source_type:
  confidence:
  collected_at:
  verified_at:
  expires_at:

  created_at:
```

---

## 17. Human Override

```yaml
QualityOverride:
  id: UUID
  tenant_id: UUID
  lead_id: UUID

  previous_score:
  new_score:
  previous_classification:
  new_classification:

  reason:
  evidence:

  created_by:
  created_at:
  expires_at:
```

---

## 18. Quality Policy

```yaml
QualityPolicy:
  id: UUID
  tenant_id: UUID
  organization_id: UUID

  name:
  version:
  status:

  weights:
    identity:
    contactability:
    company:
    completeness:
    freshness:
    consistency:
    icp_fit:
    engagement:
    intent:
    verification:

  thresholds:
  risk_penalties:
  freshness_policy:
  verification_policy:
  human_review_policy:
  ai_automation_policy:

  created_by:
  created_at:
  updated_at:
```

---

## 19. Quality Analytics

The system shall provide:

## Overall Metrics

* Average lead quality
* Median lead quality
* Quality distribution
* Excellent leads
* High-quality leads
* Low-quality leads
* Invalid leads
* Suspicious leads

## Data Quality Metrics

* Completeness
* Freshness
* Validity
* Verification rate
* Duplicate rate
* Missing-field rate

## Business Metrics

* Quality-to-MQL conversion
* Quality-to-SQL conversion
* Quality-to-opportunity conversion
* Quality-to-deal conversion
* Revenue by quality band
* Win rate by quality band

## Source Metrics

* Quality by source
* Quality by campaign
* Quality by provider
* Quality by channel

---

## 20. Lead Source Quality

The system shall calculate source-level quality.

Example:

```text
Source                  Avg Quality
------------------------------------
Organic Search              88
Referral                    91
Website Demo                94
Partner                     86
Paid Campaign               71
Imported Database           54
AI Discovery                76
Manual Entry                63
```

Actual values shall be calculated from real data.

---

## 21. Model Evaluation

The engine shall evaluate:

* Accuracy
* Precision
* Recall
* F1
* ROC-AUC
* PR-AUC
* Calibration
* Brier score
* False-positive rate
* False-negative rate

---

## 22. Quality Model Drift

The system shall monitor:

```text
Feature drift
Prediction drift
Data-quality drift
Source drift
Conversion drift
Calibration drift
Segment performance
```

---

## 23. Feedback Learning

Human feedback shall be used for:

* Model evaluation
* Rule refinement
* Threshold optimization
* Dataset creation
* Error analysis
* Model retraining

Human feedback shall not automatically retrain production models without appropriate validation and deployment controls.

---

## 24. Active Learning

The system may prioritize uncertain examples for human review.

Examples:

```text
Low confidence
High business value
Conflicting evidence
Unusual lead
Model disagreement
Human/AI disagreement
```

---

## 25. AI/ML Model Selection

The engine shall support model routing.

Example:

```text
Simple validation
      ↓
Rules

Structured prediction
      ↓
ML Model

Complex unstructured analysis
      ↓
LLM

High-risk decision
      ↓
Human Review
```

---

## 26. Quality Improvement Loop

```text
Lead
 ↓
Evaluate
 ↓
Quality Score
 ↓
Identify Problems
 ↓
Recommend Enrichment / Verification
 ↓
Execute Approved Action
 ↓
Receive New Data
 ↓
Recalculate Quality
 ↓
Compare Before/After
 ↓
Measure Business Outcome
 ↓
Learn
```

---

## 27. Lead Quality Lifecycle

```text
DISCOVERED
    ↓
RAW
    ↓
VALIDATING
    ↓
VERIFIED
    ↓
ENRICHED
    ↓
QUALITY_ASSESSED
    ↓
QUALIFIED
    ↓
SALES_READY
    ↓
CONVERTED
```

Alternative outcomes:

```text
DUPLICATE
INVALID
SPAM
FRAUD_RISK
DISQUALIFIED
NURTURE
```

---

## 28. Workflow Integration

Example:

```text
Lead Quality >= 85
        ↓
Verified?
   ┌────┴────┐
  Yes        No
   ↓          ↓
Sales       Verify
Routing     Contact
   ↓
Sales Sequence
```

---

## 29. Lead Routing Integration

The quality engine shall provide:

```yaml
routing_signal:
  lead_id:
  quality_score:
  classification:
  confidence:
  sales_ready:
  verification_status:
  risk_level:
  recommended_team:
```

---

## 30. Lead Qualification Integration

Quality and qualification shall remain separate concepts.

```text
Lead Quality
      +
ICP Fit
      +
Intent
      +
Engagement
      ↓
Lead Qualification
```

A lead may therefore be:

```text
High Quality + Low Intent
```

or:

```text
High Intent + Low Quality
```

The system shall preserve these distinctions.

---

## 31. Sales Sequence Integration

Recommended sequence behavior:

```text
EXCELLENT + VERIFIED
        ↓
High-priority personalized outreach

HIGH + VERIFIED
        ↓
Personalized sequence

GOOD
        ↓
Standard sequence

MEDIUM
        ↓
Nurture / research

LOW
        ↓
Enrichment

POOR / INVALID
        ↓
Do not contact
```

All actions shall remain subject to organization policies and applicable communication permissions.

---

## 32. CRM Integration

The system shall synchronize:

* Quality score
* Quality classification
* Verification status
* Contactability
* Risk level
* Completeness
* ICP fit
* Intent
* Recommended action
* Last quality evaluation
* Model version

---

## 33. Notification Requirements

Notifications may be triggered for:

```text
Excellent lead detected
Quality improved
Quality degraded
Fraud risk increased
Duplicate detected
Verification failed
High-value lead requires review
Quality data became stale
```

Supported channels may include:

* In-app
* Email
* Slack
* Microsoft Teams

---

## 34. Human Review Queue

The review queue shall contain:

```text
Lead
Quality Score
Classification
Confidence
Verification
Risks
Evidence
Missing Data
AI Recommendation
Recommended Action
Review Reason
```

Review actions:

```text
Approve
Reject
Modify
Verify
Enrich
Mark Duplicate
Mark Invalid
Request Rescore
```

---

## 35. Performance Requirements

Target:

```text
Cached quality retrieval:
p95 < 100 ms

Deterministic quality evaluation:
p95 < 300 ms

Real-time event evaluation:
p95 < 750 ms

External verification:
Asynchronous

AI evaluation:
Asynchronous when latency is non-critical
```

Targets shall be validated under realistic production load.

---

## 36. Scalability Requirements

The engine shall support:

* Horizontal API scaling
* Horizontal worker scaling
* Queue-based processing
* Distributed feature processing
* Batch evaluation
* Partitioned historical data
* Distributed caching
* Model-serving scaling

---

## 37. Reliability Requirements

The engine shall implement:

* Retries
* Timeouts
* Circuit breakers
* Dead-letter queues
* Idempotency
* State reconciliation
* Provider fallback
* Graceful degradation

---

## 38. Graceful Degradation

If external verification is unavailable:

```text
External Verification
        ↓ unavailable
Internal validation
        ↓
Existing verified data
        ↓
Rule-based assessment
        ↓
Confidence reduction
```

If AI is unavailable:

```text
AI unavailable
      ↓
ML model
      ↓
Rules
      ↓
Basic validation
```

The system shall indicate which evaluation methods were used.

---

## 39. Security Requirements

The engine shall protect against:

* SQL injection
* XSS
* CSRF where applicable
* Broken access control
* Tenant data leakage
* API abuse
* Credential theft
* Prompt injection
* Tool abuse
* Agent privilege escalation
* Unauthorized quality modification
* Unauthorized exports
* Data poisoning

---

## 40. Audit Requirements

The engine shall audit:

* Quality calculations
* Verification requests
* Enrichment requests
* AI evaluations
* Human reviews
* Human overrides
* Policy changes
* Model changes
* Threshold changes
* Feedback
* Exports
* Administrative actions

Audit records shall include:

```yaml
actor_type:
actor_id:
tenant_id:
organization_id:
workplace_id:
lead_id:
action:
previous_state:
new_state:
reason:
model_version:
policy_version:
request_id:
correlation_id:
timestamp:
```

---

## 41. Data Retention

The system shall support configurable retention for:

* Current quality
* Quality history
* Verification records
* Evidence
* AI evaluations
* Human reviews
* Audit logs
* Feedback

---

## 42. Export Requirements

Authorized users shall be able to export:

```text
CSV
XLSX
JSON
```

Exports shall respect:

* Tenant boundaries
* RBAC
* Field permissions
* Data-retention rules
* Privacy requirements

All exports shall be audited.

---

## 43. Quality Governance

The organization shall be able to define:

```yaml
governance:
  minimum_quality_for_sales:
  minimum_quality_for_automation:
  minimum_confidence:
  verification_required:
  human_review_required:
  duplicate_policy:
  fraud_policy:
  stale_data_policy:
```

---

## 44. AI + Human Decision Hierarchy

Recommended hierarchy:

```text
Security / Compliance Policy
          ↓
Organization Policy
          ↓
Authorized Human Decision
          ↓
Deterministic Validation
          ↓
ML Prediction
          ↓
AI Recommendation
```

AI recommendations shall not override higher-priority controls.

---

## 45. Example End-to-End Scenario

```text
AI discovers a lead
        ↓
Lead enters SalesGenie
        ↓
Email validation
        ↓
Company verification
        ↓
Duplicate detection
        ↓
Contact enrichment
        ↓
ICP evaluation
        ↓
Intent analysis
        ↓
Engagement analysis
        ↓
Fraud/spam assessment
        ↓
Quality scoring
        ↓
Quality = 89
        ↓
Confidence = 94%
        ↓
Classification = HIGH
        ↓
Human review not required
        ↓
Lead Routing Engine
        ↓
Enterprise Sales Team
        ↓
Approved Sales Sequence
        ↓
Sales Engagement
        ↓
Outcome captured
        ↓
Quality model evaluation
```

---

## 46. Example Quality Explanation

```yaml
quality_score: 89
classification: HIGH
confidence: 94

positive_factors:
  - factor: "Verified company"
    contribution: 15
  - factor: "Professional email"
    contribution: 12
  - factor: "Strong ICP match"
    contribution: 15
  - factor: "Relevant decision-maker"
    contribution: 10
  - factor: "Recent product engagement"
    contribution: 9

negative_factors:
  - factor: "Phone not verified"
    contribution: -5
  - factor: "Some firmographic data is stale"
    contribution: -4

risks:
  duplicate: 0.03
  fraud: 0.01
  spam: 0.02

missing_data:
  - annual_revenue

recommendation:
  action: "verify_phone"
  priority: "medium"
```

---

## 47. Quality Improvement Recommendation Engine

The system shall prioritize improvement actions based on expected impact.

Example:

```text
Current Score: 67

Potential Improvements:

1. Verify company
   Expected impact: +10

2. Verify contact
   Expected impact: +8

3. Enrich employee count
   Expected impact: +5

4. Confirm decision-maker role
   Expected impact: +7
```

The AI shall clearly distinguish predicted improvement from guaranteed improvement.

---

## 48. Quality-vs-Conversion Analytics

The system shall evaluate whether quality actually predicts business outcomes.

Example:

```text
Quality Band     Conversion Rate
90–100           42%
80–89            35%
70–79            27%
60–69            18%
50–59            11%
<50               4%
```

Actual values shall come from production data.

---

## 49. Acceptance Criteria

The Lead Quality Engine shall be considered production-ready when:

* [ ] Lead quality can be calculated.
* [ ] Quality dimensions are independently available.
* [ ] Identity quality works.
* [ ] Contact quality works.
* [ ] Company quality works.
* [ ] Contactability works.
* [ ] Data completeness works.
* [ ] Data freshness works.
* [ ] Data consistency works.
* [ ] ICP fit works.
* [ ] Engagement quality works.
* [ ] Intent quality works.
* [ ] Verification integration works.
* [ ] Duplicate detection works.
* [ ] Fraud-risk detection works.
* [ ] Spam detection works.
* [ ] Quality scoring works.
* [ ] Risk penalties work.
* [ ] Confidence calculation works.
* [ ] AI evaluation works.
* [ ] ML evaluation works.
* [ ] Rule-based evaluation works.
* [ ] Score explanations work.
* [ ] Evidence provenance works.
* [ ] Missing-data detection works.
* [ ] Quality recommendations work.
* [ ] Human review works.
* [ ] Human overrides work.
* [ ] Override reasons are captured.
* [ ] Quality history works.
* [ ] Quality versions are immutable.
* [ ] Model versions are tracked.
* [ ] Feature versions are tracked.
* [ ] Policy versions are tracked.
* [ ] Real-time evaluation works.
* [ ] Batch evaluation works.
* [ ] Async jobs work.
* [ ] Retry handling works.
* [ ] Dead-letter handling works.
* [ ] Idempotency works.
* [ ] Multi-tenant isolation is verified.
* [ ] RBAC is enforced server-side.
* [ ] AI permissions are isolated.
* [ ] Prompt-injection protection is implemented.
* [ ] AI cost tracking works.
* [ ] Observability is available.
* [ ] Audit logging works.
* [ ] Quality analytics work.
* [ ] Model evaluation works.
* [ ] Drift monitoring works.
* [ ] CRM integration works.
* [ ] Lead routing integration works.
* [ ] Sales sequence integration works.
* [ ] Workflow integration works.
* [ ] Notification integration works.
* [ ] Export controls work.
* [ ] Security testing passes.
* [ ] Load testing passes.
* [ ] Failure-mode testing passes.
* [ ] AI evaluation testing passes.
* [ ] Production rollback is validated.

---

## 50. FAANG-Level Quality Intelligence Loop

```text
                    ┌──────────────────┐
                    │   Lead Sources   │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Data Validation  │
                    └────────┬─────────┘
                             ↓
              ┌──────────────┴──────────────┐
              ↓                             ↓
      Verification                    Enrichment
              ↓                             ↓
              └──────────────┬──────────────┘
                             ↓
                    ┌──────────────────┐
                    │ Quality Features │
                    └────────┬─────────┘
                             ↓
             ┌───────────────┼───────────────┐
             ↓               ↓               ↓
          Rules             ML              AI
             └───────────────┼───────────────┘
                             ↓
                    ┌──────────────────┐
                    │ Score Fusion     │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Risk Assessment  │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Confidence       │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Explainability   │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Human Review     │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Quality Decision │
                    └────────┬─────────┘
                             ↓
              ┌──────────────┼──────────────┐
              ↓              ↓              ↓
           Routing        Nurturing      Enrichment
              ↓              ↓              ↓
              └──────────────┼──────────────┘
                             ↓
                       Sales Outcome
                             ↓
                     Human Feedback
                             ↓
                     Model Evaluation
                             ↓
                       Model Update
                             ↓
                     Better Quality
```

---

## 51. Definition of Done

The SalesGenie Lead Quality Engine shall not be considered complete merely because it generates a quality score.

It shall be considered complete when the platform can:

```text
DISCOVER
   ↓
VALIDATE
   ↓
VERIFY
   ↓
ENRICH
   ↓
DETECT DUPLICATES
   ↓
DETECT RISK
   ↓
MEASURE COMPLETENESS
   ↓
MEASURE FRESHNESS
   ↓
MEASURE CONSISTENCY
   ↓
EVALUATE ICP FIT
   ↓
EVALUATE ENGAGEMENT
   ↓
EVALUATE INTENT
   ↓
PREDICT QUALITY
   ↓
EXPLAIN QUALITY
   ↓
CALCULATE CONFIDENCE
   ↓
REQUEST HUMAN REVIEW WHEN NECESSARY
   ↓
APPLY AUTHORIZED HUMAN JUDGMENT
   ↓
CLASSIFY LEAD
   ↓
RECOMMEND ACTION
   ↓
ROUTE / NURTURE / ENRICH / VERIFY
   ↓
CAPTURE BUSINESS OUTCOME
   ↓
LEARN FROM HUMAN + BUSINESS FEEDBACK
```

The final system shall provide a **continuously improving, explainable, multi-tenant, AI + ML + deterministic + human-in-the-loop lead-quality intelligence layer** for SalesGenie.

It shall distinguish **lead validity, data quality, lead quality, lead qualification, buying intent, and sales readiness** rather than collapsing these concepts into a single opaque score.
