# SalesGenie — Lead Scoring Engine

## FAANG-Level User Requirements, System Requirements & Functional Requirements

> **Module:** Lead Scoring Engine  
> **Product:** SalesGenie  
> **Architecture:** Enterprise Multi-Tenant SaaS + AI/ML + Human-in-the-Loop + Event-Driven Microservices  
> **Primary Responsibility:** Convert lead, account, contact, behavioral, intent, engagement, firmographic, technographic, and sales data into explainable, configurable, continuously updated lead-priority scores.

---

## 1. Executive Objective

The SalesGenie Lead Scoring Engine shall determine the sales priority and commercial potential of every lead using a combination of:

- Deterministic rules
- Configurable scoring models
- Machine learning
- LLM-based reasoning
- Behavioral intelligence
- Firmographic intelligence
- Technographic intelligence
- Intent intelligence
- Engagement intelligence
- Historical conversion data
- Account intelligence
- Contact intelligence
- Sales-agent feedback
- Human-defined business rules

The engine shall answer:

1. How valuable is this lead?
2. How closely does the lead match the organization's ICP?
3. How likely is the lead to engage?
4. How likely is the lead to become an opportunity?
5. How likely is the lead to convert?
6. Why did the lead receive this score?
7. Which factors increased or decreased the score?
8. How confident is the system?
9. What information is missing?
10. What should the sales team do next?
11. Should AI act automatically or require human approval?
12. How should the score change as new information arrives?

The scoring engine shall be a **decision-support and prioritization system**, not an opaque black-box number generator.

---

## 2. Core Design Principles

The Lead Scoring Engine shall follow these principles:

1. Every score must be explainable.
2. Every score must be reproducible from its inputs and model version.
3. AI-generated scores must be distinguishable from deterministic scores.
4. Human-defined scoring policies must override AI recommendations where configured.
5. AI must never bypass authorization.
6. Score calculations must be tenant-isolated.
7. Scoring must support real-time and batch execution.
8. Scores must have confidence values.
9. Scores must maintain historical versions.
10. Score changes must be auditable.
11. New evidence must be able to trigger rescoring.
12. Human feedback must be captured.
13. Model performance must be continuously evaluated.
14. Scoring policies must be configurable without code changes.
15. High-impact automated actions must require configured approval.
16. Missing data must not automatically be treated as negative evidence.
17. Conflicting evidence must be explicitly represented.
18. External data must retain provenance.
19. AI must not fabricate scoring evidence.
20. The architecture must support horizontal scaling.

---

## 3. User Personas

## 3.1 Super Admin

The Super Admin shall be able to:

- Configure platform-level scoring capabilities.
- Manage AI/ML providers.
- Manage scoring model versions.
- Configure global scoring safeguards.
- Configure global feature flags.
- Monitor scoring infrastructure.
- Monitor scoring costs.
- Review scoring-system audit logs.
- Monitor model quality.
- Configure global rate limits.
- Configure AI autonomy policies.

---

## 3.2 Organization Admin

The Organization Admin shall be able to:

- Configure organization-level scoring models.
- Define ICP criteria.
- Configure score weights.
- Define score thresholds.
- Configure AI scoring policies.
- Configure human approval requirements.
- Configure scoring fields.
- Configure lead-priority classifications.
- Review scoring analytics.
- Manage model access.

---

## 3.3 Workplace Admin

The Workplace Admin shall be able to:

- Configure workplace-level scoring policies.
- Configure team scoring rules.
- Manage scoring thresholds.
- Configure routing based on score.
- Configure AI/human scoring responsibilities.
- Review scoring activity.

---

## 3.4 Sales Manager

The Sales Manager shall be able to:

- Define ICPs.
- Configure scoring criteria.
- Configure weights.
- Review high-priority leads.
- Review score explanations.
- Override scores where authorized.
- Approve/reject AI recommendations.
- Analyze scoring performance.
- Compare scoring models.
- Monitor score-to-conversion performance.
- Configure team-specific scoring strategies.

---

## 3.5 Sales Agent

The Sales Agent shall be able to:

- View lead scores.
- View score explanations.
- View positive and negative factors.
- View confidence.
- View intent signals.
- View missing information.
- Provide feedback.
- Request rescoring.
- Add human score adjustments where authorized.
- Accept/reject AI recommendations.
- View recommended next actions.

---

## 3.6 AI Sales Agent

The AI Sales Agent shall be able to:

- Calculate lead scores.
- Analyze lead attributes.
- Evaluate ICP fit.
- Analyze intent.
- Analyze engagement.
- Identify buying signals.
- Recommend priority.
- Explain scoring decisions.
- Request additional enrichment.
- Recommend next actions.
- Detect score changes.
- Trigger configured workflows.

The AI Sales Agent shall operate only through explicitly authorized tools.

---

## 4. User Requirements

## UR-001 — Lead Score Visibility

Users shall be able to see a lead's:

- Overall score
- Score category
- Score confidence
- Fit score
- Intent score
- Engagement score
- Conversion probability
- Priority
- Positive factors
- Negative factors
- Missing data
- Score history
- Last calculation time
- Model version

---

## UR-002 — Explainable Scoring

Users shall be able to understand why a lead received its score.

The interface shall show:

```text
Score: 87/100

Positive Factors:
+ Strong ICP match
+ Enterprise company size
+ Relevant technology stack
+ High-intent behavior
+ Decision maker identified

Negative Factors:
- Geographic fit slightly below target

Confidence:
92%

Recommended Action:
Prioritize for immediate sales engagement
```

---

## UR-003 — ICP-Based Scoring

Users shall be able to define an Ideal Customer Profile containing:

* Industry
* Geography
* Employee count
* Revenue
* Business model
* Technology
* Company stage
* Funding
* Department
* Job title
* Seniority
* Use case
* Market segment

The scoring engine shall calculate ICP fit against these attributes.

---

## UR-004 — Behavioral Scoring

The system shall score behavioral activities such as:

* Website visits
* Product-page visits
* Pricing-page visits
* Demo requests
* Form submissions
* Email opens
* Email clicks
* Email replies
* Content downloads
* Webinar participation
* Trial activity
* Product usage
* Meeting attendance

Behavioral scoring shall support configurable weights.

---

## UR-005 — Intent Scoring

The system shall evaluate signals indicating potential buying intent.

Signals may include:

* Pricing-page activity
* Product research
* Technology research
* Competitor research
* Funding
* Hiring
* Expansion
* Product launch
* Executive changes
* Technology adoption
* Technology replacement
* Relevant business events

---

## UR-006 — Firmographic Scoring

The system shall evaluate:

* Industry
* Employee count
* Revenue
* Location
* Company age
* Growth rate
* Funding
* Business model
* Market segment

---

## UR-007 — Technographic Scoring

The system shall score technology compatibility.

Examples:

* Salesforce
* HubSpot
* Zendesk
* Slack
* Microsoft Teams
* Jira
* Notion
* Existing AI systems
* Existing CRM
* Existing support platforms

The scoring engine shall support:

* Required technologies
* Preferred technologies
* Excluded technologies
* Technology migration signals
* Technology gaps

---

## UR-008 — Contact Scoring

The engine shall score contacts based on:

* Job title
* Department
* Seniority
* Decision-making authority
* Influence
* Role relevance
* Contact confidence
* Relationship with account

---

## UR-009 — Account-Level Scoring

The engine shall support account-level scoring independently of individual contact scoring.

Account score factors may include:

* Company fit
* Market fit
* Growth
* Intent
* Technology
* Financial capacity
* Strategic value
* Existing relationship

---

## UR-010 — Lead-Level Scoring

The system shall combine account, contact, behavioral, intent, and engagement signals into a lead score.

---

## UR-011 — Opportunity Score

The system shall optionally calculate an opportunity score representing potential commercial value.

---

## UR-012 — Conversion Probability

The ML scoring system shall estimate:

* Probability of qualification
* Probability of opportunity creation
* Probability of conversion
* Probability of deal closure

Probabilities shall be calibrated where sufficient historical data exists.

---

## UR-013 — Priority Classification

Leads shall be classified into configurable priority levels:

```text
HOT
WARM
QUALIFIED
NURTURE
LOW
DISQUALIFIED
```

Organizations shall be able to configure their own categories.

---

## UR-014 — Human Override

Authorized humans shall be able to override AI/deterministic scores.

Every override shall require:

* User ID
* Reason
* Previous score
* New score
* Timestamp
* Optional evidence
* Expiration date if applicable

---

## UR-015 — AI Recommendation Approval

Users shall be able to:

* Approve
* Reject
* Modify
* Request more evidence
* Request enrichment
* Recalculate

AI recommendations shall not automatically become authoritative when approval is required.

---

## UR-016 — Score History

Users shall be able to inspect historical score changes.

Example:

```text
Aug 24 10:00 — 52
Aug 24 11:15 — 61
Aug 24 12:30 — 78
Aug 24 14:00 — 87
```

Each change shall show the reason.

---

## UR-017 — Score Alerts

Users shall be able to receive alerts when:

* Score crosses a threshold.
* Lead becomes HOT.
* Intent increases significantly.
* Score decreases significantly.
* New buying signals appear.
* Lead becomes qualified.
* AI detects a high-value opportunity.

---

## UR-018 — Bulk Scoring

Authorized users shall be able to score:

* One lead
* Multiple leads
* Entire segments
* Entire accounts
* Entire organizations

---

## UR-019 — Scheduled Scoring

Users shall be able to configure:

* Real-time scoring
* Hourly scoring
* Daily scoring
* Weekly scoring
* Custom schedules

---

## UR-020 — Scoring Feedback

Sales users shall be able to provide feedback:

```text
Correct
Incorrect
Too High
Too Low
Missing Signal
Wrong ICP
Wrong Intent
Wrong Priority
```

---

## UR-021 — AI Explanation

The AI shall explain:

* Which signals mattered.
* How each signal affected the score.
* Which evidence supports the signal.
* Which evidence conflicts.
* What information is missing.
* How confident the model is.

---

## UR-022 — Recommended Next Action

The scoring engine shall recommend actions such as:

* Contact immediately
* Call decision maker
* Send personalized email
* Request enrichment
* Perform additional research
* Add to sequence
* Nurture
* Wait for intent
* Disqualify

---

## UR-023 — Score Comparison

Users shall be able to compare:

* Leads
* Accounts
* Segments
* Scoring models
* Historical periods
* Sales teams

---

## UR-024 — Segment-Level Intelligence

Users shall be able to analyze scoring distributions across:

* Industry
* Geography
* Company size
* Campaign
* Sales agent
* Source
* Lead segment
* Account segment

---

## 5. System Requirements

## SR-001 — Multi-Tenant Isolation

The scoring engine shall enforce strict tenant isolation across:

* Database
* Cache
* Queue
* Feature store
* Model inputs
* Model outputs
* Analytics
* Audit logs
* Events
* AI context

---

## SR-002 — Authentication

All protected scoring APIs shall require valid authentication.

Supported mechanisms shall include:

* JWT
* Service authentication
* Internal service credentials
* Machine-to-machine authentication

---

## SR-003 — Authorization

The system shall support:

* RBAC
* Permission-based authorization
* Tenant permissions
* Organization permissions
* Workplace permissions
* Resource-level permissions
* AI-agent permissions

---

## SR-004 — Least Privilege

AI agents shall not inherit unrestricted human permissions.

Every scoring-related tool shall have an explicit permission boundary.

---

## SR-005 — Scoring Architecture

The engine shall support multiple scoring strategies:

```text
                    Lead Scoring Engine
                           |
        +------------------+------------------+
        |                  |                  |
        ▼                  ▼                  ▼
   Rule Engine       ML Scoring Engine   AI Reasoning
        |                  |                  |
        +------------------+------------------+
                           |
                           ▼
                  Score Fusion Engine
                           |
                           ▼
                  Confidence Engine
                           |
                           ▼
                 Explanation Engine
                           |
                           ▼
                Recommendation Engine
```

---

## SR-006 — Deterministic Rule Engine

The system shall support deterministic rules such as:

```text
IF industry = "SaaS"
THEN score +10

IF employees > 500
THEN score +10

IF pricing_page_visit = true
THEN score +15

IF email_bounce = true
THEN score -20
```

Rules shall be configurable.

---

## SR-007 — Machine Learning Engine

The system shall support ML models for:

* Qualification prediction
* Opportunity prediction
* Conversion prediction
* Intent classification
* Lead ranking

Models shall support versioning.

---

## SR-008 — AI Reasoning Engine

LLM-based scoring may be used for:

* Unstructured lead analysis
* Research interpretation
* Signal extraction
* Contextual scoring
* Explanation generation
* Recommendation generation

LLM output shall not automatically override authoritative deterministic constraints.

---

## SR-009 — Score Fusion

The engine shall combine:

```text
Rule Score
+
ML Score
+
AI Score
+
Behavioral Score
+
Intent Score
+
Human Adjustment
```

according to configurable policies.

---

## SR-010 — Score Normalization

Different scoring models shall normalize scores into a common range.

Default:

```text
0–100
```

---

## SR-011 — Probability Calibration

Probability-based models shall support calibration methods such as:

* Platt scaling
* Isotonic regression
* Calibration curves

---

## SR-012 — Model Versioning

Every ML/AI score shall contain:

```yaml
model_name:
model_version:
model_type:
feature_version:
prompt_version:
scoring_policy_version:
created_at:
```

---

## SR-013 — Feature Versioning

Input features shall be versioned to ensure score reproducibility.

---

## SR-014 — Score Reproducibility

Given the same:

* Lead state
* Feature version
* Model version
* Rule version
* Policy version

the system shall be capable of reproducing the scoring decision where deterministic execution is supported.

---

## SR-015 — Feature Store

The architecture should support a feature store for:

* Firmographic features
* Behavioral features
* Engagement features
* Intent features
* Account features
* Contact features
* Historical features

---

## SR-016 — Real-Time Scoring

The engine shall support event-driven score updates.

Example:

```text
pricing_page_viewed
        ↓
event bus
        ↓
scoring worker
        ↓
feature update
        ↓
score calculation
        ↓
threshold evaluation
        ↓
notification/workflow
```

---

## SR-017 — Batch Scoring

The engine shall support large-scale batch scoring using asynchronous workers.

---

## SR-018 — Idempotency

Repeated scoring events shall not create duplicate scoring records or inconsistent score states.

---

## SR-019 — Event Ordering

Where event ordering affects scoring, the system shall support:

* Event timestamps
* Sequence IDs
* Version numbers
* Idempotency keys
* State reconciliation

---

## SR-020 — Retry

The engine shall implement:

* Exponential backoff
* Maximum retries
* Dead-letter queues
* Provider-specific retry policies
* Failure classification

---

## SR-021 — Circuit Breaker

External AI/ML/data providers shall be protected using circuit-breaker mechanisms.

---

## SR-022 — Rate Limiting

Rate limits shall be configurable per:

* User
* Tenant
* Organization
* API
* AI agent
* Model
* Provider
* Batch job

---

## SR-023 — AI Cost Management

The engine shall track:

* Input tokens
* Output tokens
* Model calls
* Embeddings
* AI scoring calls
* Research calls
* External provider calls
* Estimated cost

Costs shall be attributable to:

* Tenant
* Organization
* User
* AI agent
* Feature
* Workflow

---

## SR-024 — Observability

The service shall provide:

* Health endpoint
* Readiness endpoint
* Metrics
* Structured logging
* Distributed tracing
* Error tracking

---

## SR-025 — Data Provenance

Scoring evidence shall retain:

* Source
* Source type
* Retrieval timestamp
* Verification timestamp
* Confidence
* Data freshness
* Transformation history

---

## SR-026 — Data Freshness

Features shall contain freshness metadata.

Example:

```yaml
feature:
  value:
  source:
  collected_at:
  verified_at:
  expires_at:
  freshness_status:
```

---

## SR-027 — Missing Data Handling

The engine shall distinguish:

```text
Positive Evidence
Negative Evidence
Unknown
Not Applicable
Conflicting Evidence
Stale Evidence
```

Unknown shall not automatically equal negative.

---

## SR-028 — Conflict Resolution

If data sources disagree, the system shall:

1. Detect the conflict.
2. Rank sources according to configured trust.
3. Preserve conflicting values.
4. Select the authoritative value.
5. Record the resolution.
6. Reduce confidence where appropriate.

---

## 6. Functional Requirements

## 6.1 Lead Scoring

## FR-001 — Calculate Lead Score

The system shall calculate a lead score using configurable features.

Example:

```yaml
lead_score:
  fit: 32
  intent: 24
  engagement: 18
  account_value: 8
  contact_quality: 5
  data_confidence: 5
  total: 92
```

---

## FR-002 — Score Range

Default score range:

```text
0–100
```

Organizations may configure alternative scales where supported.

---

## FR-003 — Score Classification

Example:

```yaml
HOT:
  min: 80

WARM:
  min: 60

QUALIFIED:
  min: 40

NURTURE:
  min: 20

LOW:
  min: 0
```

Thresholds shall be configurable.

---

## 6.2 Fit Scoring

## FR-004 — ICP Fit Score

The system shall calculate ICP fit using:

```text
Industry
Company Size
Revenue
Location
Business Model
Technology
Company Stage
Target Market
Use Case
```

---

## FR-005 — Firmographic Score

The system shall calculate:

```yaml
firmographic_score:
  industry:
  employee_count:
  revenue:
  geography:
  growth:
  funding:
```

---

## 6.3 Behavioral Scoring

## FR-006 — Activity Score

The system shall assign configurable values to activities.

Example:

```yaml
pricing_page_view:
  score: +15

demo_request:
  score: +30

email_reply:
  score: +25

content_download:
  score: +5

email_bounce:
  score: -20

unsubscribe:
  score: -50
```

---

## FR-007 — Activity Decay

Behavioral signals shall support time decay.

Example:

```text
Recent activity = high weight
Older activity = reduced weight
Expired activity = ignored
```

---

## 6.4 Intent Scoring

## FR-008 — Intent Detection

The engine shall identify high-intent signals.

---

## FR-009 — Intent Weighting

Each intent signal shall have configurable:

* Weight
* Confidence
* Freshness
* Priority
* Expiration

---

## FR-010 — Intent Decay

Intent signals shall decay over time unless refreshed.

---

## 6.5 Engagement Scoring

## FR-011 — Engagement Score

The system shall evaluate:

* Email engagement
* Website engagement
* Meeting engagement
* Product engagement
* Content engagement
* Sales interaction

---

## 6.6 Contact Scoring

## FR-012 — Contact Relevance

The engine shall evaluate:

```text
Role relevance
+
Seniority
+
Department
+
Decision authority
+
Contact confidence
```

---

## FR-013 — Decision-Maker Score

The system shall calculate a decision-maker score.

Example:

```text
CEO / Founder      → Very High
VP / C-Level       → High
Director           → High
Manager            → Medium
Individual         → Low
```

Actual weights shall be configurable by organization.

---

## 6.7 Account Scoring

## FR-014 — Account Score

Account scoring shall include:

* ICP fit
* Revenue
* Employee count
* Growth
* Funding
* Technology
* Strategic relevance
* Intent
* Market potential

---

## 6.8 AI Scoring

## FR-015 — AI Lead Evaluation

The AI shall evaluate unstructured information.

Inputs may include:

* Company description
* Website information
* Public business information
* News
* Product information
* Job postings
* Technology information
* CRM notes
* Sales notes

---

## FR-016 — AI Score Explanation

AI shall produce structured explanations.

```yaml
explanation:
  summary:
  positive_factors:
  negative_factors:
  evidence:
  assumptions:
  missing_information:
  confidence:
```

---

## 6.9 ML Scoring

## FR-017 — Predictive Score

ML models shall estimate conversion-related probabilities where sufficient historical data exists.

Example:

```yaml
prediction:
  qualification_probability: 0.87
  opportunity_probability: 0.72
  conversion_probability: 0.58
```

---

## FR-018 — Cold-Start Handling

When insufficient historical data exists, the system shall fall back to:

* Rules
* ICP scoring
* Industry benchmarks where permitted
* AI reasoning
* Organization-defined priors

The system shall explicitly mark cold-start predictions.

---

## 6.10 Score Fusion

## FR-019 — Combine Scoring Sources

Example:

```text
Final Score =
    35% Rule Score
  + 30% ML Score
  + 20% Intent Score
  + 10% Behavioral Score
  + 5% AI Context Score
```

Weights shall be configurable.

---

## FR-020 — Human Adjustment

A human adjustment may be represented as:

```yaml
human_adjustment:
  value: +8
  reason: "Strategic enterprise account"
  user_id:
  created_at:
  expires_at:
```

Human adjustments shall be separately stored from raw model scores.

---

## 6.11 Confidence

## FR-021 — Score Confidence

Every score shall contain:

```yaml
confidence:
  value:
  level:
  factors:
  missing_data:
  stale_data:
```

---

## FR-022 — Confidence Categories

Default:

```text
90–100 → Very High
75–89  → High
50–74  → Medium
25–49  → Low
0–24   → Very Low
```

---

## 6.12 Explainability

## FR-023 — Feature Contribution

The engine shall identify major contributors.

Example:

```text
+18 Enterprise company size
+15 Strong ICP industry match
+12 Pricing-page activity
+10 Salesforce technology fit
+8 Decision maker identified
-5 Geographic mismatch
```

---

## FR-024 — Evidence

Each major scoring factor should reference evidence where available.

---

## 6.13 Score History

## FR-025 — Store Score Versions

Each scoring event shall generate a versioned record.

```yaml
score_version:
  version:
  score:
  model:
  model_version:
  policy_version:
  features_version:
  reason:
  created_at:
```

---

## 6.14 Score Change Detection

## FR-026 — Significant Score Change

The system shall detect configurable score changes.

Example:

```text
Previous: 54
Current: 82
Change: +28
```

The engine may trigger:

* Notification
* Lead routing
* Sales task
* Workflow
* Human approval

according to policy.

---

## 6.15 Human Override

## FR-027 — Override Score

Authorized users shall be able to override a score.

---

## FR-028 — Override Expiration

Human overrides may optionally expire.

Example:

```yaml
override:
  score: 90
  expires_at: 2026-09-30T23:59:59
```

After expiration, the authoritative scoring policy shall resume.

---

## 6.16 Feedback

## FR-029 — Collect Feedback

Users shall be able to submit:

```text
Correct
Incorrect
Too High
Too Low
Missing Factor
Wrong ICP
Wrong Intent
Wrong Classification
```

---

## FR-030 — Feedback Dataset

Feedback shall be stored as structured evaluation data.

---

## 6.17 Scoring Policies

## FR-031 — Create Scoring Policy

Authorized users shall be able to define:

```yaml
policy:
  name:
  description:
  enabled:
  weights:
  rules:
  thresholds:
  decay:
  model:
  approval_policy:
```

---

## FR-032 — Version Policies

Every policy modification shall create a new version.

Existing scores shall retain the policy version used during calculation.

---

## 6.18 Real-Time Scoring

## FR-033 — Event Triggered Scoring

The engine shall consume events such as:

```text
lead.created
lead.updated
contact.updated
company.updated
email.opened
email.clicked
email.replied
website.visited
pricing_page.visited
demo.requested
meeting.booked
funding.detected
hiring.detected
technology.changed
intent.detected
```

---

## 6.19 Batch Scoring

## FR-034 — Bulk Score Job

Bulk scoring shall support:

```yaml
job:
  job_id:
  tenant_id:
  total:
  processed:
  successful:
  failed:
  progress:
  started_at:
  completed_at:
```

---

## 6.20 API Requirements

## FR-035 — Calculate Score

```http
POST /api/v1/lead-scoring/leads/{lead_id}/score
```

---

## FR-036 — Get Score

```http
GET /api/v1/lead-scoring/leads/{lead_id}
```

---

## FR-037 — Explain Score

```http
GET /api/v1/lead-scoring/leads/{lead_id}/explanation
```

---

## FR-038 — Score History

```http
GET /api/v1/lead-scoring/leads/{lead_id}/history
```

---

## FR-039 — Override Score

```http
POST /api/v1/lead-scoring/leads/{lead_id}/override
```

---

## FR-040 — Submit Feedback

```http
POST /api/v1/lead-scoring/leads/{lead_id}/feedback
```

---

## FR-041 — Batch Score

```http
POST /api/v1/lead-scoring/batch
```

---

## FR-042 — Scoring Policies

```http
GET  /api/v1/lead-scoring/policies
POST /api/v1/lead-scoring/policies
PUT  /api/v1/lead-scoring/policies/{policy_id}
```

---

## 7. Scoring Architecture

```text
                    ┌─────────────────────┐
                    │   SalesGenie UI     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ API Gateway         │
                    └──────────┬──────────┘
                               │
                               ▼
                  ┌───────────────────────────┐
                  │ Lead Scoring Service      │
                  └─────────────┬─────────────┘
                                │
        ┌───────────────────────┼────────────────────────┐
        │                       │                        │
        ▼                       ▼                        ▼
┌──────────────┐       ┌───────────────┐       ┌───────────────┐
│ Rule Engine  │       │ Feature Engine│       │ AI Engine     │
└──────┬───────┘       └───────┬───────┘       └──────┬────────┘
       │                       │                       │
       ▼                       ▼                       ▼
┌──────────────┐       ┌───────────────┐       ┌───────────────┐
│ Rule Scores  │       │ Feature Store │       │ LLM/AI Models │
└──────┬───────┘       └───────┬───────┘       └──────┬────────┘
       │                       │                       │
       └───────────────────────┼───────────────────────┘
                               ▼
                     ┌────────────────────┐
                     │ ML Prediction      │
                     │ Engine             │
                     └──────────┬─────────┘
                                │
                                ▼
                     ┌────────────────────┐
                     │ Score Fusion       │
                     └──────────┬─────────┘
                                │
                                ▼
                     ┌────────────────────┐
                     │ Confidence Engine  │
                     └──────────┬─────────┘
                                │
                                ▼
                     ┌────────────────────┐
                     │ Explainability     │
                     └──────────┬─────────┘
                                │
                                ▼
                     ┌────────────────────┐
                     │ Recommendation     │
                     └──────────┬─────────┘
                                │
                     ┌──────────┴──────────┐
                     ▼                     ▼
              Human Approval         Automated Workflow
```

---

## 8. Score Calculation Pipeline

```text
Lead Created
      ↓
Collect Lead Data
      ↓
Collect Account Data
      ↓
Collect Contact Data
      ↓
Collect Behavioral Data
      ↓
Collect Intent Data
      ↓
Collect Engagement Data
      ↓
Validate Data
      ↓
Normalize Features
      ↓
Apply Freshness
      ↓
Apply Time Decay
      ↓
Calculate Rule Score
      ↓
Calculate ML Score
      ↓
Calculate AI Context Score
      ↓
Calculate Intent Score
      ↓
Calculate Engagement Score
      ↓
Calculate Account Score
      ↓
Calculate Contact Score
      ↓
Fuse Scores
      ↓
Calculate Confidence
      ↓
Generate Explanation
      ↓
Apply Human Override
      ↓
Classify Priority
      ↓
Recommend Next Action
      ↓
Evaluate Automation Policy
      ↓
Trigger Workflow / Human Review
      ↓
Store Score Version
```

---

## 9. Recommended Scoring Model

The default model may use:

```text
ICP Fit                  25%
Intent                   20%
Engagement               15%
Company Value            10%
Contact Quality           10%
Behavioral Signals        10%
Technology Fit             5%
Data Confidence             5%
```

Total:

```text
100%
```

Organizations shall be able to modify the weights.

---

## 10. Multi-Dimensional Scoring

The engine should maintain separate scores rather than relying exclusively on one number.

```yaml
scores:
  overall: 87
  fit: 91
  intent: 88
  engagement: 79
  account_value: 84
  contact_quality: 93
  technology_fit: 90
  behavioral: 81
  data_confidence: 95
  conversion_probability: 72
```

---

## 11. Lead Priority Engine

```text
                    Lead Score
                        |
            +-----------+-----------+
            |           |           |
            ▼           ▼           ▼
         HOT          WARM       QUALIFIED
          |             |            |
          ▼             ▼            ▼
    Immediate       Priority      Nurture /
    Engagement      Outreach      Research
```

---

## 12. Dynamic Score Decay

The system shall support configurable decay.

Example:

```text
Pricing-page visit
Day 0 → +20
Day 7 → +15
Day 14 → +10
Day 30 → +5
Day 60 → +0
```

Decay policies shall be configurable by signal type.

---

## 13. Negative Scoring

The engine shall support negative factors.

Examples:

```text
Unsubscribed              -50
Invalid email             -40
Competitor                -30
Outside target geography -20
Wrong industry            -30
Very small company        -10
No engagement             -5
```

Negative scoring shall be configurable.

---

## 14. Score Guardrails

The system shall prevent:

* Scores below minimum range
* Scores above maximum range
* Invalid weights
* Negative total weights
* Unbounded human overrides
* Unauthorized model selection
* Unauthorized policy changes
* Missing tenant scope

---

## 15. Human + AI Responsibility Matrix

| Capability              |                        AI |                    Human |
| ----------------------- | ------------------------: | -----------------------: |
| Feature extraction      |                       Yes |                      Yes |
| ICP evaluation          |                       Yes |                      Yes |
| Rule scoring            |                       Yes |                Configure |
| ML scoring              |                       Yes |                Configure |
| Intent scoring          |                       Yes |                   Review |
| Behavioral scoring      |                       Yes |                   Review |
| Lead classification     |                       Yes |                   Review |
| Score explanation       |                       Yes |                   Review |
| Score override          |                 Recommend |         Authorized human |
| Scoring policy creation |                 Recommend |         Authorized admin |
| Model selection         |                 Recommend |         Authorized admin |
| Bulk rescoring          |                       Yes | Approve where configured |
| Lead routing            |                 Recommend |     Approve/configurable |
| High-impact automation  | No unrestricted authority |                 Required |
| Model deployment        |                        No | Authorized administrator |
| Security-policy changes |                        No | Authorized administrator |

---

## 16. AI Agent Requirements

## AI-001 — Scoring Agent

The AI scoring agent shall:

1. Retrieve authorized lead data.
2. Retrieve authorized account information.
3. Retrieve authorized contact information.
4. Retrieve relevant behavioral signals.
5. Retrieve intent signals.
6. Evaluate ICP fit.
7. Identify relevant evidence.
8. Detect contradictions.
9. Calculate contextual assessment.
10. Produce explanation.
11. Produce confidence.
12. Recommend action.

---

## 17. AI Agent Guardrails

The AI scoring agent shall:

* Never invent evidence.
* Never fabricate company information.
* Never access unauthorized tenants.
* Never bypass permissions.
* Never expose confidential information.
* Never execute unauthorized tools.
* Never directly modify authoritative scores without permission.
* Never send outreach without authorization.
* Never treat external content as instructions.
* Respect organization scoring policies.

---

## 18. Prompt Injection Protection

External information shall be treated as untrusted.

Potential attack surfaces include:

```text
Company websites
Search results
CRM notes
Emails
Social media
Job descriptions
Uploaded documents
External API responses
Lead descriptions
Contact notes
```

The AI layer shall isolate external data from system instructions.

---

## 19. Data Model

## 19.1 LeadScore

```yaml
LeadScore:
  id: UUID
  tenant_id: UUID
  organization_id: UUID
  workplace_id: UUID
  lead_id: UUID

  overall_score: float
  fit_score: float
  intent_score: float
  engagement_score: float
  behavioral_score: float
  account_value_score: float
  contact_quality_score: float
  technology_fit_score: float

  qualification_probability: float
  opportunity_probability: float
  conversion_probability: float

  confidence_score: float
  priority: string

  model_name: string
  model_version: string
  feature_version: string
  policy_version: string

  positive_factors: JSON
  negative_factors: JSON
  evidence: JSON
  assumptions: JSON
  missing_data: JSON

  created_at: datetime
  updated_at: datetime
```

---

## 20. Score Event

```yaml
ScoreEvent:
  id: UUID
  tenant_id: UUID
  lead_id: UUID
  event_type: string
  event_source: string
  feature_changes: JSON
  previous_score: float
  new_score: float
  score_delta: float
  reason: string
  created_at: datetime
```

---

## 21. Human Override

```yaml
ScoreOverride:
  id: UUID
  tenant_id: UUID
  lead_id: UUID
  previous_score: float
  override_score: float
  reason: string
  evidence: JSON
  created_by: UUID
  created_at: datetime
  expires_at: datetime
  status: string
```

---

## 22. Scoring Policy

```yaml
ScoringPolicy:
  id: UUID
  tenant_id: UUID
  organization_id: UUID
  name: string
  version: integer
  status: string

  weights:
    fit: float
    intent: float
    engagement: float
    behavioral: float
    account_value: float
    contact_quality: float
    technology_fit: float

  rules: JSON
  thresholds: JSON
  decay_policy: JSON
  approval_policy: JSON

  created_by: UUID
  created_at: datetime
  updated_at: datetime
```

---

## 23. API Requirements

## Score Lead

```http
POST /api/v1/lead-scoring/leads/{lead_id}/score
```

## Retrieve Score

```http
GET /api/v1/lead-scoring/leads/{lead_id}
```

## Retrieve Explanation

```http
GET /api/v1/lead-scoring/leads/{lead_id}/explanation
```

## Retrieve History

```http
GET /api/v1/lead-scoring/leads/{lead_id}/history
```

## Override Score

```http
POST /api/v1/lead-scoring/leads/{lead_id}/override
```

## Feedback

```http
POST /api/v1/lead-scoring/leads/{lead_id}/feedback
```

## Batch Scoring

```http
POST /api/v1/lead-scoring/batch
```

## Policies

```http
GET /api/v1/lead-scoring/policies
POST /api/v1/lead-scoring/policies
GET /api/v1/lead-scoring/policies/{policy_id}
PUT /api/v1/lead-scoring/policies/{policy_id}
```

---

## 24. Event Architecture

The engine shall consume:

```text
lead.created
lead.updated
lead.enriched
contact.created
contact.updated
company.updated
email.opened
email.clicked
email.replied
email.bounced
website.visited
pricing_page.visited
demo.requested
meeting.booked
content.downloaded
funding.detected
hiring.detected
technology.detected
technology.changed
intent.detected
```

The engine shall publish:

```text
lead.scored
lead.score_changed
lead.priority_changed
lead.hot
lead.qualified
lead.disqualified
lead.scoring_failed
lead.review_required
lead.high_intent
lead.high_conversion_probability
```

---

## 25. Scoring Analytics

The system shall provide:

## Overall Metrics

* Average score
* Median score
* Score distribution
* HOT leads
* WARM leads
* Qualified leads
* Low-quality leads
* Disqualified leads

## Model Metrics

* Precision
* Recall
* F1
* ROC-AUC
* PR-AUC
* Calibration
* Brier score
* Lift
* Gain

## Business Metrics

* Score-to-opportunity conversion
* Score-to-deal conversion
* Revenue by score band
* Win rate by score band
* Average deal size by score band
* Sales-cycle length by score band

---

## 26. Model Evaluation

The system shall evaluate scoring models against historical outcomes.

Example:

```text
Lead Score Band      Opportunity Rate
90–100               45%
80–89                38%
70–79                29%
60–69                19%
50–59                12%
<50                   5%
```

The exact values shall be derived from actual organizational data.

---

## 27. Model Drift Detection

The system shall monitor:

* Feature distribution drift
* Prediction drift
* Conversion-rate drift
* Calibration drift
* Data-quality drift
* Segment-specific performance degradation

The system shall alert administrators when configured thresholds are exceeded.

---

## 28. Bias and Fairness Monitoring

Where applicable, the scoring engine shall monitor whether scoring behavior creates unintended systematic disparities.

The system shall:

* Monitor model behavior across relevant business segments.
* Identify suspicious score distributions.
* Detect unexpected feature dependence.
* Allow model review.
* Maintain model documentation.

The system shall not use prohibited sensitive attributes for scoring unless there is a legitimate, legally reviewed basis and explicit organizational policy.

---

## 29. Cost Optimization

The engine shall avoid unnecessary LLM calls.

Recommended strategy:

```text
Cheap deterministic rules
        ↓
Feature-based scoring
        ↓
ML prediction
        ↓
LLM reasoning only when necessary
```

LLM reasoning may be triggered when:

* Data is ambiguous.
* Unstructured context is important.
* Evidence conflicts.
* Human explanation is requested.
* Complex qualification is required.

---

## 30. Caching Requirements

Suitable scoring inputs may be cached.

Cache keys shall include tenant context.

Example:

```text
tenant_id:
lead_id:
feature_version:
model_version:
policy_version:
```

Cross-tenant cache collisions shall be impossible.

---

## 31. Database Requirements

Recommended indexes:

```text
tenant_id
lead_id
organization_id
workplace_id
overall_score
priority
confidence_score
created_at
updated_at
model_version
policy_version
```

Composite indexes shall be introduced according to measured production query patterns.

---

## 32. Performance Requirements

Target performance:

```text
Single deterministic score:
p95 < 200 ms

Cached score retrieval:
p95 < 100 ms

Real-time event scoring:
p95 < 500 ms

AI-assisted scoring:
Asynchronous where latency is non-critical

Bulk scoring:
Horizontally scalable
```

Performance targets shall be validated through load testing.

---

## 33. Scalability Requirements

The system shall support:

* Horizontal API scaling
* Horizontal worker scaling
* Queue-based processing
* Database connection pooling
* Redis caching
* Feature-store scaling
* Partitionable score history
* Batch processing
* Model-serving scaling

The architecture shall support growth from:

```text
1 organization
        ↓
1,000 organizations
        ↓
10,000+ organizations
```

without fundamental redesign.

---

## 34. Reliability Requirements

The scoring system shall implement:

* Timeouts
* Retries
* Circuit breakers
* Dead-letter queues
* Idempotency
* State reconciliation
* Partial-result preservation
* Provider fallback
* Graceful degradation

---

## 35. Graceful Degradation

If the ML or LLM provider becomes unavailable:

```text
AI Score unavailable
        ↓
ML Score if available
        ↓
Rule Score
        ↓
Basic ICP Score
```

The system shall clearly indicate which scoring method was used.

---

## 36. Security Requirements

The scoring engine shall protect against:

* SQL injection
* XSS
* CSRF where applicable
* Broken access control
* Cross-tenant data leakage
* API abuse
* Credential theft
* Prompt injection
* Tool abuse
* Agent privilege escalation
* Unauthorized score manipulation
* Unauthorized data export

---

## 37. Audit Requirements

The engine shall audit:

* Score calculation
* Score recalculation
* Score override
* Policy changes
* Model changes
* Feature changes
* AI decisions
* Human feedback
* Approval decisions
* Batch jobs
* Export operations
* Configuration changes

Audit records shall include:

```yaml
actor_type:
actor_id:
tenant_id:
organization_id:
lead_id:
action:
previous_state:
new_state:
reason:
model:
model_version:
policy_version:
timestamp:
request_id:
correlation_id:
```

---

## 38. Data Retention

Score history shall support configurable retention.

The system shall support:

* Active score
* Historical scores
* Archived scores
* Deletion requests
* Tenant-specific retention policies

---

## 39. Export Requirements

Authorized users shall be able to export scoring information in:

```text
CSV
XLSX
JSON
```

Exports shall include only permitted fields.

Every export shall be auditable.

---

## 40. Workflow Integration

Score changes shall be able to trigger SalesGenie workflows.

Example:

```text
Score > 80
    ↓
Lead becomes HOT
    ↓
Create sales task
    ↓
Notify sales agent
    ↓
Add to approved sequence
```

Another example:

```text
Score drops below 40
    ↓
Remove from high-priority queue
    ↓
Move to nurture
```

---

## 41. Lead Routing Integration

The scoring engine shall provide routing signals to the Lead Routing Engine.

Example:

```yaml
routing_signal:
  lead_id:
  priority: HOT
  score: 92
  recommended_team: Enterprise Sales
  recommended_agent:
  reason:
```

The scoring engine shall recommend routing but shall not bypass routing authorization.

---

## 42. Sales Sequence Integration

The scoring engine shall provide signals to Sales Sequence automation.

Examples:

```text
HOT → Immediate sequence
WARM → Personalized sequence
QUALIFIED → Standard sequence
NURTURE → Nurture sequence
LOW → Low-touch sequence
```

Execution shall remain subject to organizational policy.

---

## 43. CRM Integration

The engine shall support synchronization of:

* Lead score
* Priority
* Fit score
* Intent score
* Conversion probability
* Recommended action
* Score timestamp
* Model version

CRM writes shall be idempotent.

---

## 44. Notification Requirements

Notifications may be generated for:

```text
High score
Score increase
Score decrease
High intent
New buying signal
High conversion probability
Model anomaly
Scoring failure
Human review required
```

Channels may include:

* In-app
* Email
* Slack
* Microsoft Teams
* Other configured channels

---

## 45. Human Review Queue

The system shall provide an approval queue containing:

```text
Lead
Current score
Previous score
AI recommendation
Evidence
Confidence
Risk
Recommended action
Reason approval is required
```

Users shall be able to:

```text
Approve
Reject
Edit
Request More Data
Request Rescore
Assign
```

---

## 46. AI + Human Score Governance

The authoritative score hierarchy shall be configurable.

Recommended default:

```text
Security / Compliance Rules
        ↓
Organization Policy
        ↓
Human Approved Override
        ↓
Deterministic Rules
        ↓
ML Prediction
        ↓
AI Contextual Recommendation
```

AI shall not override higher-priority policy constraints.

---

## 47. Example End-to-End Scoring

```text
Lead:
Enterprise SaaS company
1,200 employees
Uses Salesforce
Recently raised funding
Visited pricing page 3 times
Downloaded enterprise report
VP Sales identified
Opened recent email
```

Scoring:

```text
ICP Fit                 +24
Enterprise Size         +10
Technology Fit           +8
Funding Signal            +8
Pricing Activity         +15
Content Engagement        +6
Decision Maker            +8
Email Engagement          +4
Data Confidence           +5
--------------------------------
Final Score               88
```

Classification:

```text
HOT
```

Recommendation:

```text
Prioritize immediate personalized outreach to the VP Sales.
```

---

## 48. Example Explainability Output

```yaml
score: 88

classification: HOT

confidence: 94

positive_factors:
  - factor: "Strong ICP match"
    contribution: 24
  - factor: "Enterprise company size"
    contribution: 10
  - factor: "Relevant technology stack"
    contribution: 8
  - factor: "Recent funding"
    contribution: 8
  - factor: "High-intent pricing activity"
    contribution: 15
  - factor: "Decision maker identified"
    contribution: 8

negative_factors: []

missing_information:
  - "Exact annual revenue"

recommended_action:
  type: "personalized_outreach"
  priority: "immediate"

evidence:
  - source: "behavioral_activity"
  - source: "company_intelligence"
  - source: "contact_intelligence"
```

---

## 49. Acceptance Criteria

The Lead Scoring Engine shall be considered production-ready when:

* [ ] Lead scores can be calculated.
* [ ] Scores are normalized.
* [ ] ICP scoring works.
* [ ] Firmographic scoring works.
* [ ] Technographic scoring works.
* [ ] Behavioral scoring works.
* [ ] Intent scoring works.
* [ ] Engagement scoring works.
* [ ] Account scoring works.
* [ ] Contact scoring works.
* [ ] Rule-based scoring works.
* [ ] ML-based scoring works.
* [ ] AI-assisted scoring works.
* [ ] Score fusion works.
* [ ] Confidence scoring works.
* [ ] Score explanations work.
* [ ] Evidence is traceable.
* [ ] Score history works.
* [ ] Score changes are detected.
* [ ] Score decay works.
* [ ] Negative scoring works.
* [ ] Human overrides work.
* [ ] Override reasons are mandatory where configured.
* [ ] Override expiration works.
* [ ] Feedback collection works.
* [ ] Scoring policies are configurable.
* [ ] Scoring policies are versioned.
* [ ] Models are versioned.
* [ ] Features are versioned.
* [ ] Cold-start handling works.
* [ ] Real-time scoring works.
* [ ] Batch scoring works.
* [ ] Async jobs work.
* [ ] Retry mechanisms work.
* [ ] Dead-letter queues work.
* [ ] Idempotency works.
* [ ] Multi-tenant isolation is verified.
* [ ] RBAC is enforced server-side.
* [ ] AI agents cannot escalate privileges.
* [ ] AI agents cannot cross tenants.
* [ ] Prompt injection protections are implemented.
* [ ] AI cost tracking works.
* [ ] Audit logging works.
* [ ] Metrics are available.
* [ ] Distributed tracing is available.
* [ ] Model evaluation works.
* [ ] Model drift detection works.
* [ ] CRM integration works.
* [ ] Lead routing integration works.
* [ ] Sales sequence integration works.
* [ ] Workflow integration works.
* [ ] Notification integration works.
* [ ] Export controls work.
* [ ] Security tests pass.
* [ ] Load tests pass.
* [ ] Failure-mode tests pass.
* [ ] AI evaluation tests pass.
* [ ] Production rollback is validated.

---

## 50. FAANG-Level Target Architecture

```text
                         SALES GENIE
                             |
                             ▼
                     ┌───────────────┐
                     │ API Gateway   │
                     └───────┬───────┘
                             |
                             ▼
                  ┌─────────────────────┐
                  │ Lead Scoring Engine │
                  └──────────┬──────────┘
                             |
       ┌─────────────────────┼──────────────────────┐
       |                     |                      |
       ▼                     ▼                      ▼
┌─────────────┐       ┌─────────────┐       ┌──────────────┐
│ Rule Engine │       │ Feature     │       │ AI Reasoning │
│             │       │ Engine      │       │ Engine       │
└──────┬──────┘       └──────┬──────┘       └──────┬───────┘
       |                     |                      |
       └─────────────────────┼──────────────────────┘
                             ▼
                    ┌─────────────────┐
                    │ ML Model Server │
                    └────────┬────────┘
                             |
                             ▼
                    ┌─────────────────┐
                    │ Score Fusion     │
                    └────────┬────────┘
                             |
                             ▼
                    ┌─────────────────┐
                    │ Confidence       │
                    └────────┬────────┘
                             |
                             ▼
                    ┌─────────────────┐
                    │ Explainability   │
                    └────────┬────────┘
                             |
                             ▼
                    ┌─────────────────┐
                    │ Recommendation   │
                    └────────┬────────┘
                             |
                 ┌───────────┴───────────┐
                 ▼                       ▼
          Human Approval          Automation Engine
                 |                       |
                 └───────────┬───────────┘
                             ▼
                     CRM / Sales / Workflow
                             |
                             ▼
                       Business Outcome
                             |
                             ▼
                     Feedback / Analytics
                             |
                             ▼
                    Model Evaluation
                             |
                             ▼
                     Model Improvement
```

---

## 51. Definition of Done

The SalesGenie Lead Scoring Engine shall not be considered complete merely because it produces a numeric score.

It shall be considered complete when it can:

```text
COLLECT
   ↓
NORMALIZE
   ↓
VALIDATE
   ↓
UNDERSTAND
   ↓
SCORE
   ↓
PREDICT
   ↓
EXPLAIN
   ↓
CALCULATE CONFIDENCE
   ↓
INCORPORATE HUMAN JUDGMENT
   ↓
RECOMMEND
   ↓
ROUTE
   ↓
AUTOMATE
   ↓
MEASURE
   ↓
LEARN
```

The final output shall answer:

```text
Who should SalesGenie prioritize?

Why should they be prioritized?

How strong is their ICP fit?

How strong is their buying intent?

How engaged are they?

How valuable is the account?

Who is the right decision maker?

What evidence supports the score?

How confident is the model?

What information is missing?

What changed the score?

What should the salesperson do next?

Should AI act automatically?

If AI acts, what permissions does it have?

Did the recommendation produce a positive business outcome?
```

The Lead Scoring Engine shall therefore function as a **continuously learning, explainable, multi-dimensional, policy-governed AI + ML + deterministic + human sales-prioritization system**, rather than a simple rule-based scoring table.
