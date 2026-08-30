# SalesGenie — AI-Based Lead Scoring

## User Requirements, System Requirements & Functional Requirements

### File: `AI_based_lead_scoring.md`

**Document Version:** 1.0.0  
**Product:** SalesGenie  
**Module:** AI-Based Lead Scoring Engine  
**Document Type:** URS + SRS + FRS  
**Architecture:** Enterprise SaaS / Multi-Tenant / Microservices / Event-Driven / AI-Augmented  
**Operating Model:** AI Autonomous + AI-Assisted + Human-in-the-Loop  
**Security Model:** Zero Trust / RBAC / ABAC / Tenant Isolation  
**Primary Objective:** Predict lead quality, buying probability, conversion probability, revenue potential, urgency, and recommended sales priority.

---

## 1. PURPOSE

The AI-Based Lead Scoring module is the predictive decision engine of SalesGenie.

Its purpose is to transform raw lead, account, behavioral, firmographic, technographic, intent, engagement, historical sales, marketing, and revenue data into explainable and continuously improving scores.

The system shall answer:

```text
Is this lead worth pursuing?
        ↓
How good is the business fit?
        ↓
How strong is the buying intent?
        ↓
How engaged is the prospect?
        ↓
How likely is the prospect to convert?
        ↓
How much revenue could this lead generate?
        ↓
How urgent is the opportunity?
        ↓
What is the risk?
        ↓
Should AI act automatically or request human review?
        ↓
What should the sales team do next?
```

The scoring engine shall not rely on a single static numerical score.

It shall produce a multi-dimensional intelligence profile.

---

## 2. BUSINESS OBJECTIVE

SalesGenie shall prioritize leads based on expected business value rather than simple lead volume.

The system shall optimize:

```text
Lead Quality
+
ICP Fit
+
Buying Intent
+
Engagement
+
Buying Signals
+
Revenue Potential
+
Conversion Probability
+
Urgency
+
Data Confidence
-
Risk
-
Staleness
-
Invalidity
=
Business Priority
```

The objective is to help customers:

* reduce wasted sales effort,
* identify high-value prospects,
* increase conversion rates,
* shorten sales cycles,
* improve sales productivity,
* increase revenue,
* improve marketing efficiency,
* identify hidden opportunities,
* automate lead prioritization,
* provide explainable recommendations.

---

## 3. SCOPE

## 3.1 In Scope

The module shall support:

* rule-based scoring,
* weighted scoring,
* ML-based scoring,
* AI-assisted scoring,
* predictive scoring,
* real-time score updates,
* batch score updates,
* account scoring,
* contact scoring,
* opportunity scoring,
* ICP scoring,
* intent scoring,
* engagement scoring,
* buying-signal scoring,
* conversion prediction,
* revenue prediction,
* urgency scoring,
* risk scoring,
* data-confidence scoring,
* lead prioritization,
* score explanation,
* score history,
* score comparison,
* score simulation,
* score calibration,
* score thresholds,
* automated routing,
* human review,
* human override,
* feedback learning,
* model versioning,
* model evaluation,
* drift detection,
* A/B testing,
* score analytics,
* CRM synchronization,
* API access,
* event-driven updates,
* audit logging.

---

## 4. OUT OF SCOPE

The scoring engine shall not:

* fabricate prospect information,
* invent buying intent,
* guarantee conversion,
* make unauthorized decisions using sensitive personal information,
* override organization policies,
* automatically execute high-risk actions without authorization,
* access private systems without authorization,
* bypass security controls.

---

## 5. USERS

The module shall support:

| Role                 | Primary Usage                              |
| -------------------- | ------------------------------------------ |
| Super Admin          | Platform-wide scoring governance           |
| Platform Admin       | Platform configuration                     |
| Security Admin       | Security and scoring access controls       |
| Organization Owner   | Organization scoring policy                |
| Organization Admin   | Organization configuration                 |
| Workplace Admin      | Workplace-level configuration              |
| Team Manager         | Team scoring configuration                 |
| Sales Manager        | Sales prioritization                       |
| Sales Agent          | Lead prioritization                        |
| Marketing Manager    | Marketing qualification                    |
| Marketing Specialist | Campaign optimization                      |
| SEO Manager          | SEO lead quality                           |
| SEO Specialist       | Search-driven scoring                      |
| Product Manager      | Product-fit intelligence                   |
| Finance Manager      | Revenue intelligence                       |
| Business Analyst     | Scoring analytics                          |
| Support Manager      | Customer/account scoring                   |
| AI Agent Builder     | AI scoring-agent configuration             |
| Developer            | APIs and integrations                      |
| End User / Client    | Business-level scoring and recommendations |

---

## 6. SCORING PHILOSOPHY

SalesGenie shall use multiple scoring dimensions rather than one opaque score.

Minimum scoring dimensions:

```text
ICP Fit Score
Company Fit Score
Contact Fit Score
Intent Score
Engagement Score
Buying Signal Score
Product Fit Score
Technology Fit Score
Conversion Probability
Revenue Potential
Urgency Score
Data Confidence Score
Risk Score
Lead Health Score
Overall Lead Score
```

---

## 7. USER REQUIREMENTS

## UR-001 — Lead Score Visibility

Users shall be able to view the current score of every authorized lead.

Example:

```text
Lead Score: 91/100
Priority: P0 — Immediate
Conversion Probability: 84%
Revenue Potential: $75,000
Intent: 93/100
ICP Fit: 96/100
Engagement: 87/100
Risk: 12/100
Confidence: 94%
```

---

## UR-002 — Explainable Scoring

Users shall understand why a lead received a specific score.

Example:

```text
Overall Score: 91

Positive Factors:
+ Excellent ICP match
+ Executive decision maker
+ High product relevance
+ Strong recent engagement
+ Pricing-page activity
+ High buying intent
+ Similar customers converted successfully

Negative Factors:
- Budget unknown
- Contact verification incomplete
```

The system shall never present an important score as an unexplained black box.

---

## UR-003 — Multi-Dimensional Scoring

Users shall be able to inspect individual score dimensions.

Minimum:

```text
ICP Fit
Intent
Engagement
Buying Signals
Company Quality
Product Fit
Technology Fit
Conversion Probability
Revenue Potential
Urgency
Risk
Confidence
```

---

## UR-004 — Lead Ranking

Users shall be able to rank leads according to:

* overall score,
* conversion probability,
* revenue potential,
* intent,
* urgency,
* ICP fit,
* engagement,
* risk,
* score change.

---

## UR-005 — Automatic Prioritization

The system shall automatically classify leads.

Example:

```text
P0 — Immediate
P1 — Very High
P2 — High
P3 — Medium
P4 — Low
P5 — Nurture
```

Priority shall be configurable by organization.

---

## UR-006 — Real-Time Score Updates

The user shall see score changes when important events occur.

Example:

```text
Lead Score

Before:
71

Event:
Prospect requested a demo.

After:
88
```

---

## UR-007 — Score History

Users shall be able to see how a lead's score changed over time.

Example:

```text
Aug 01 → 54
Aug 05 → 62
Aug 10 → 70
Aug 15 → 79
Aug 22 → 91
```

---

## UR-008 — Score Change Explanation

Whenever a significant score change occurs, the system shall explain the cause.

Example:

```text
Score increased by 17 points.

Reasons:
+12 Demo request
+4 Pricing-page engagement
+3 New decision-maker identified
-2 Data confidence decreased
```

---

## UR-009 — Conversion Probability

Users shall be able to see predicted conversion probability.

Example:

```text
Conversion Probability: 82%
Confidence: 91%
```

---

## UR-010 — Revenue Potential

Users shall be able to view estimated:

* deal value,
* expected revenue,
* probability-adjusted revenue,
* customer lifetime value potential,
* expansion potential.

---

## UR-011 — Lead Comparison

Users shall compare multiple leads.

Example:

```text
                Lead A   Lead B   Lead C
Overall Score     92       86       79
Intent            94       81       72
Revenue           $90K     $45K     $120K
Conversion         82%      71%      54%
Risk               10%      15%      28%
```

---

## UR-012 — ICP-Based Scoring

Organizations shall define their own ICP.

The scoring engine shall evaluate leads against:

* industry,
* geography,
* company size,
* revenue,
* employee count,
* business model,
* technology,
* growth stage,
* job role,
* seniority,
* product need,
* budget,
* business problem.

---

## UR-013 — Custom Scoring

Authorized users shall be able to configure scoring criteria.

Example:

```text
Industry Match = +20
Company Size Match = +15
Technology Match = +15
Decision Maker = +10
High Intent = +20
Demo Request = +15
Invalid Email = -20
Stale Data = -10
```

---

## UR-014 — AI-Based Scoring

Users shall be able to activate AI-powered scoring.

The AI shall analyze relationships between multiple signals rather than only fixed rules.

---

## UR-015 — Human Override

Authorized users shall be able to override scores.

Override shall require:

```text
Reason
Reviewer
Timestamp
Previous Score
New Score
```

---

## UR-016 — Human Review

The system shall route cases to humans when:

* AI confidence is low,
* data conflicts exist,
* score is unusually high,
* score changes dramatically,
* revenue potential exceeds threshold,
* model uncertainty is high,
* policy requires approval.

---

## UR-017 — AI Recommendation

The scoring system shall recommend the next action.

Examples:

```text
Contact immediately
Schedule demo
Assign senior sales representative
Send case study
Start nurture sequence
Perform additional enrichment
Request human review
Do not pursue
```

---

## UR-018 — Score Thresholds

Users shall configure thresholds.

Example:

```text
Score >= 85 → Hot
70–84 → Warm
50–69 → Nurture
<50 → Low Priority
```

---

## UR-019 — Dynamic Segmentation

Users shall create segments using scores.

Example:

```text
High Score + High Intent
High Score + Low Engagement
Low Score + High Revenue
High Intent + Low ICP Fit
```

---

## UR-020 — Score Alerts

Users shall receive alerts when:

* score crosses a threshold,
* score drops significantly,
* conversion probability increases,
* buying intent spikes,
* high-value lead appears.

---

## UR-021 — Natural Language Scoring Queries

Users shall be able to ask:

```text
"Show me leads with a score above 85."

"Why is this lead ranked first?"

"Which leads became hotter this week?"

"Which high-value leads are being ignored?"

"Which leads have high intent but low engagement?"
```

---

## UR-022 — Score Simulation

Authorized users shall be able to simulate score changes.

Example:

```text
Current:
72

If:
Decision Maker = Yes
Intent = High
Company Revenue = $50M

Predicted:
89
```

Simulation shall not modify production data.

---

## UR-023 — Score Configuration Versioning

Users shall be able to see:

* current scoring configuration,
* previous configuration,
* effective date,
* creator,
* change reason.

---

## UR-024 — Score Quality Monitoring

Users shall be able to monitor:

* scoring accuracy,
* conversion lift,
* precision,
* recall,
* false positives,
* false negatives,
* calibration.

---

## UR-025 — Business Outcome Tracking

Users shall be able to determine whether high-scored leads actually converted.

---

## 8. SYSTEM REQUIREMENTS

## SR-001 — Dedicated Scoring Service

The scoring engine shall operate as an independently scalable microservice.

Suggested service:

```text
lead-scoring-service
```

---

## SR-002 — Scoring Architecture

```text
                 ┌──────────────────────┐
                 │ Lead Intelligence    │
                 └──────────┬───────────┘
                            ↓
                 ┌──────────────────────┐
                 │ Feature Engineering  │
                 └──────────┬───────────┘
                            ↓
        ┌───────────────────┼───────────────────┐
        ↓                   ↓                   ↓
   Rule Engine         ML Model            AI Reasoner
        │                   │                   │
        └───────────────────┼───────────────────┘
                            ↓
                 ┌──────────────────────┐
                 │ Score Aggregator     │
                 └──────────┬───────────┘
                            ↓
                 ┌──────────────────────┐
                 │ Calibration Layer    │
                 └──────────┬───────────┘
                            ↓
                 ┌──────────────────────┐
                 │ Explanation Engine    │
                 └──────────┬───────────┘
                            ↓
                 ┌──────────────────────┐
                 │ Priority Engine      │
                 └──────────┬───────────┘
                            ↓
                 ┌──────────────────────┐
                 │ Recommendation Engine│
                 └──────────────────────┘
```

---

## SR-003 — Multi-Tenant Isolation

Every score shall be associated with:

```text
platform_id
organization_id
workplace_id
team_id
lead_id
```

Tenant boundaries shall be enforced at:

* API,
* service,
* database,
* cache,
* event,
* vector-search,
* AI-context layers.

---

## SR-004 — Feature Store

The system shall maintain reusable scoring features.

Examples:

```text
company_size
company_revenue
industry_match
geographic_match
technology_fit
decision_maker_probability
intent_frequency
engagement_rate
website_activity
pricing_page_visits
demo_request
email_engagement
historical_conversion_rate
average_deal_size
customer_similarity
```

---

## SR-005 — Feature Versioning

Every feature transformation shall be versioned.

```text
feature_name
feature_version
source
transformation
timestamp
```

---

## SR-006 — Training Data Pipeline

The system shall support:

```text
Historical Leads
        ↓
Historical Outcomes
        ↓
Feature Generation
        ↓
Training Dataset
        ↓
Validation
        ↓
Model Training
        ↓
Evaluation
        ↓
Approval
        ↓
Deployment
```

---

## SR-007 — ML Model Support

The platform shall support:

* Logistic Regression,
* Random Forest,
* XGBoost,
* LightGBM,
* CatBoost,
* neural networks,
* transformer-based models.

The architecture shall not hard-code a single model.

---

## SR-008 — AI Model Support

The AI layer shall support multiple providers through an AI Gateway.

Supported provider categories include:

* Groq,
* Google Gemini / Google AI,
* Mistral AI,
* other authorized providers,
* self-hosted models.

Provider selection shall be configurable.

---

## SR-009 — Model Routing

Model routing shall consider:

```text
Task
Model Quality
Latency
Cost
Context Length
Provider Availability
Rate Limits
Tenant Policy
Data Sensitivity
```

---

## SR-010 — Rule Engine

The system shall support deterministic rules.

Example:

```text
IF
industry = target_industry
AND company_size >= 100
AND intent_score >= 80

THEN
increase_score_by(15)
```

---

## SR-011 — Hybrid Scoring

The system shall combine:

```text
Rules
+
Statistical Models
+
Machine Learning
+
AI Reasoning
+
Historical Outcomes
```

---

## SR-012 — Score Calibration

Raw model probabilities shall be calibrated before being shown as business probabilities.

Supported approaches may include:

* Platt scaling,
* isotonic regression,
* calibration curves.

---

## SR-013 — Confidence Estimation

Every score shall have confidence.

Example:

```json
{
  "score": 91,
  "confidence": 0.94
}
```

---

## SR-014 — Uncertainty Detection

The system shall identify uncertain predictions.

Example:

```text
Score: 74
Confidence: 42%
Status: HUMAN_REVIEW_REQUIRED
```

---

## SR-015 — Batch Scoring

The system shall support scoring:

* individual leads,
* lead lists,
* accounts,
* entire organizations.

---

## SR-016 — Real-Time Scoring

The system shall recalculate scores when relevant events occur.

---

## SR-017 — Event-Driven Scoring

Events may include:

```text
lead.created
lead.updated
lead.enriched
lead.verified
lead.intent.detected
lead.signal.detected
lead.engagement.changed
lead.demo_requested
lead.pricing_viewed
lead.email_clicked
lead.account_changed
opportunity.created
deal.won
deal.lost
```

---

## SR-018 — Idempotency

Repeated events shall not produce duplicate score updates.

---

## SR-019 — Score History Storage

The system shall maintain historical versions.

---

## SR-020 — Score Auditability

Every production score shall be traceable to:

```text
Input Features
Rules
Model
Model Version
AI Provider
Prompt Version
Output
Confidence
Timestamp
```

---

## SR-021 — Model Registry

The platform shall maintain a model registry.

Each model shall contain:

```text
model_id
version
type
training_dataset
feature_version
metrics
status
owner
created_at
deployed_at
```

---

## SR-022 — Model Deployment

The system shall support:

```text
Development
→ Staging
→ Shadow
→ Canary
→ Production
```

---

## SR-023 — Shadow Mode

New models shall be testable without affecting production scores.

---

## SR-024 — Canary Deployment

New scoring models shall be deployable to a limited percentage of traffic.

---

## SR-025 — Automatic Rollback

The system shall support rollback when:

* error rate increases,
* latency increases,
* model performance decreases,
* abnormal scoring distribution occurs.

---

## SR-026 — Model Drift Detection

The system shall detect:

* feature drift,
* prediction drift,
* outcome drift,
* concept drift.

---

## SR-027 — Data Drift

The system shall detect changes in:

```text
Industry Distribution
Company Size
Lead Sources
Intent Distribution
Conversion Distribution
Feature Values
```

---

## SR-028 — Explainability Framework

The system shall support explainability techniques appropriate to the model.

Examples:

* SHAP,
* feature importance,
* contribution analysis,
* rule trace,
* evidence retrieval.

---

## SR-029 — AI Explanation

AI explanations shall be generated only from verified scoring evidence.

The AI shall not invent reasons.

---

## SR-030 — Security

The scoring engine shall implement:

```text
Zero Trust
RBAC
ABAC
MFA
Encryption
Tenant Isolation
Secrets Management
Audit Logging
Rate Limiting
```

---

## SR-031 — AI Security

The AI scoring pipeline shall defend against:

* prompt injection,
* malicious lead content,
* poisoned data,
* unauthorized tool use,
* cross-tenant context leakage,
* sensitive-data leakage.

---

## SR-032 — Observability

The service shall expose:

```text
Score Latency
Inference Latency
Queue Depth
Model Error Rate
Prediction Distribution
Feature Drift
AI Cost
Provider Failures
Human Override Rate
```

---

## SR-033 — Scalability

The architecture shall support horizontal scaling of:

```text
API Workers
Scoring Workers
ML Inference Workers
AI Workers
Feature Workers
Event Consumers
```

---

## SR-034 — Caching

Frequently accessed scoring data may be cached using Redis or equivalent technology.

Cache invalidation shall occur when scores materially change.

---

## SR-035 — Persistence

PostgreSQL or an equivalent transactional datastore shall maintain authoritative score records.

Analytics workloads should be separated from transactional workloads.

---

## SR-036 — Search

The platform shall support fast filtering by:

```text
score
intent
conversion_probability
revenue
priority
industry
location
company_size
```

---

## 9. FUNCTIONAL REQUIREMENTS

## FR-001 — Create Lead Score

The system shall calculate a score for every eligible lead.

---

## FR-002 — Calculate ICP Score

The system shall calculate:

```text
ICP Fit Score = 0–100
```

---

## FR-003 — Calculate Intent Score

The system shall calculate:

```text
Intent Score = 0–100
```

---

## FR-004 — Calculate Engagement Score

The system shall analyze engagement signals.

Example:

```text
Email Open
Email Click
Website Visit
Pricing Visit
Demo Request
Content Download
Campaign Interaction
```

---

## FR-005 — Calculate Buying Signal Score

The system shall calculate buying-signal strength based on:

* recency,
* frequency,
* signal type,
* business relevance,
* historical conversion association.

---

## FR-006 — Calculate Company Fit

The system shall evaluate:

* industry,
* revenue,
* employee count,
* geography,
* growth,
* business model.

---

## FR-007 — Calculate Contact Fit

The system shall evaluate:

* job title,
* seniority,
* department,
* decision-making probability,
* product relevance.

---

## FR-008 — Calculate Product Fit

The system shall determine how closely the prospect's likely needs match the organization's products.

---

## FR-009 — Calculate Technology Fit

The system shall evaluate technology compatibility.

---

## FR-010 — Calculate Conversion Probability

The system shall generate a calibrated probability:

```text
0.00–1.00
```

Example:

```text
0.84 = 84% predicted probability
```

---

## FR-011 — Calculate Revenue Potential

The system shall estimate:

```text
Potential Deal Value
Expected Revenue
Probability-Adjusted Revenue
```

---

## FR-012 — Calculate Urgency

The system shall estimate whether the opportunity requires immediate action.

---

## FR-013 — Calculate Risk

Risk factors may include:

* data uncertainty,
* poor fit,
* low intent,
* churn history,
* competitive pressure,
* stale information.

---

## FR-014 — Calculate Data Confidence

The system shall calculate confidence based on:

```text
Completeness
Verification
Freshness
Source Reliability
Cross-Source Agreement
```

---

## FR-015 — Calculate Overall Score

The system shall combine the dimensions using configurable scoring logic.

Example:

```text
Overall Score =
ICP Fit × W1
+
Intent × W2
+
Engagement × W3
+
Buying Signals × W4
+
Product Fit × W5
+
Revenue Potential × W6
+
Data Confidence × W7
-
Risk × W8
```

Weights shall be configurable.

---

## FR-016 — Organization-Specific Scoring

Each organization shall be able to define its own scoring model.

---

## FR-017 — Role-Specific Scoring Views

Sales users may prioritize:

```text
Conversion
Revenue
Urgency
```

Marketing users may prioritize:

```text
Engagement
Intent
Campaign Fit
```

Finance users may prioritize:

```text
Revenue
Expected Value
ROI
```

---

## FR-018 — Dynamic Score Recalculation

The system shall recalculate scores when relevant features change.

---

## FR-019 — Score Decay

The system shall support time decay.

Example:

```text
Old engagement
↓
Lower relevance
↓
Lower score contribution
```

Decay rates shall be configurable by signal type.

---

## FR-020 — Signal Recency

Recent signals shall generally receive higher weight than stale signals, subject to organization configuration.

---

## FR-021 — Frequency Analysis

Repeated engagement shall be analyzed.

Example:

```text
1 pricing visit → moderate signal

5 pricing visits in 3 days → strong signal
```

---

## FR-022 — Signal Combination

The engine shall identify combinations of signals.

Example:

```text
High ICP Fit
+
Pricing Activity
+
Decision Maker
+
Demo Request
=
Very High Conversion Probability
```

---

## FR-023 — Negative Signals

The scoring engine shall support negative signals.

Examples:

```text
Invalid Contact
Poor ICP Fit
No Engagement
Long-Term Inactivity
Disqualification
Competitor Customer
```

---

## FR-024 — Score Caps

Organizations may define maximum or minimum contribution from specific signals to prevent one feature from dominating the score.

---

## FR-025 — Score Normalization

The system shall normalize scores to a consistent range.

Default:

```text
0–100
```

---

## FR-026 — Score Distribution Monitoring

The system shall detect abnormal distributions.

Example:

```text
If 95% of all leads suddenly receive >90,
trigger model-quality alert.
```

---

## FR-027 — Score Explanation API

The system shall provide structured explanations.

Example:

```json
{
  "overall_score": 91,
  "confidence": 0.94,
  "positive_factors": [
    {
      "factor": "ICP Fit",
      "contribution": 18
    },
    {
      "factor": "Demo Request",
      "contribution": 15
    }
  ],
  "negative_factors": [
    {
      "factor": "Data Freshness",
      "contribution": -3
    }
  ]
}
```

---

## FR-028 — Score History API

The system shall expose score history.

---

## FR-029 — Score Comparison API

The system shall allow authorized users to compare scores.

---

## FR-030 — Score Simulation API

The system shall support non-production scoring simulations.

---

## FR-031 — Bulk Scoring

The system shall support asynchronous bulk scoring.

Example:

```text
1,000,000 leads
        ↓
Distributed scoring workers
        ↓
Batch completion
        ↓
Analytics
```

---

## FR-032 — Priority Assignment

The system shall map scores to business priorities.

---

## FR-033 — Lead Routing

The system shall route high-priority leads to appropriate sales teams.

Example:

```text
Enterprise + High Score
        ↓
Enterprise Sales Team

SMB + Medium Score
        ↓
SMB Sales Team
```

---

## FR-034 — AI Recommended Action

The system shall produce:

```text
Action
Reason
Expected Outcome
Confidence
Urgency
```

---

## FR-035 — Automated Workflow Trigger

Authorized organizations may configure workflows.

Example:

```text
IF score >= 90
AND intent >= 85

THEN
create sales task
+
notify manager
+
request human review
```

---

## FR-036 — Human Approval Workflow

High-risk automation shall require human approval.

---

## FR-037 — Human Override

The system shall preserve original AI scores even after human override.

Example:

```text
AI Score: 88
Human Score: 74
Reason: Budget information indicates low purchasing capacity
```

---

## FR-038 — Override Analytics

The system shall measure:

```text
AI Score
Human Override
Override Direction
Override Reason
Final Outcome
```

---

## FR-039 — Feedback Learning

Human corrections shall be incorporated into model evaluation and future model training where permitted.

---

## FR-040 — Conversion Feedback

When a lead:

```text
Converts
Does Not Convert
Becomes Opportunity
Is Disqualified
```

the outcome shall be recorded for model evaluation.

---

## FR-041 — Win/Loss Analysis

The system shall identify scoring patterns associated with:

* wins,
* losses,
* long sales cycles,
* fast conversions.

---

## FR-042 — Model Performance

The platform shall calculate:

```text
Precision
Recall
F1
ROC-AUC
PR-AUC
Brier Score
Calibration Error
Lift
Gain
Conversion Lift
Revenue Lift
```

---

## FR-043 — Threshold Optimization

The system shall recommend optimal scoring thresholds based on business objectives.

Example:

```text
Objective:
Maximize qualified opportunities.

Recommended threshold:
82
```

---

## FR-044 — Cost-Sensitive Scoring

The system shall support optimization based on different costs.

Example:

```text
False Positive Cost
vs
False Negative Cost
```

An enterprise sales team may prefer fewer false positives.

A high-volume SMB sales operation may prefer greater recall.

---

## FR-045 — Revenue-Weighted Scoring

Organizations shall optionally optimize scoring against expected revenue instead of only conversion.

Example:

```text
Lead A
Conversion: 90%
Deal Value: $5K

Lead B
Conversion: 70%
Deal Value: $100K

Revenue-aware system:
Lead B may receive higher business priority.
```

---

## FR-046 — Time-to-Conversion Prediction

The system shall estimate:

```text
Expected Conversion Time
```

---

## FR-047 — Lead Momentum

The system shall calculate whether lead quality is:

```text
Accelerating
Stable
Declining
```

---

## FR-048 — Score Trend

Users shall view score trends:

```text
Daily
Weekly
Monthly
Quarterly
```

---

## FR-049 — Segment Analytics

Users shall compare score distributions by:

* industry,
* geography,
* source,
* campaign,
* product,
* sales team,
* account size.

---

## FR-050 — Source-Based Scoring Analytics

The system shall determine whether specific lead sources produce high-quality leads.

---

## FR-051 — Campaign Scoring Analytics

Marketing users shall determine:

```text
Campaign
→ Lead Quality
→ Intent
→ Conversion
→ Revenue
```

---

## FR-052 — Product-Based Scoring

The system shall determine which products attract the highest-quality prospects.

---

## FR-053 — Account-Level Score

The system shall calculate an account score based on multiple contacts and signals.

---

## FR-054 — Buying Committee Score

The system shall consider multiple stakeholders.

Example:

```text
CEO       → 80
CTO       → 95
CFO       → 72
Procurement → 61

Account Buying Committee Score → 87
```

---

## FR-055 — Lookalike Scoring

The system shall compare leads against successful customers.

---

## FR-056 — Similarity Score

The system shall calculate similarity between:

```text
Lead
vs
Successful Customer Cohort
```

---

## FR-057 — Competitive Scoring

The system may reduce or increase priority based on competitive conditions where supported by reliable evidence.

---

## FR-058 — Score Expiration

Scores shall support validity periods where appropriate.

---

## FR-059 — Stale Score Detection

The system shall identify scores based on outdated information.

---

## FR-060 — Re-Scoring Scheduler

The system shall support:

```text
Real-Time
Hourly
Daily
Weekly
Monthly
Event-Based
```

scoring modes.

---

## 10. SCORING PIPELINE

```text
                    Lead
                     │
                     ↓
             Data Validation
                     │
                     ↓
             Feature Extraction
                     │
        ┌────────────┼────────────┐
        ↓            ↓            ↓
    Firmographic  Behavioral   Technographic
        │            │            │
        └────────────┼────────────┘
                     ↓
              Intent Engine
                     │
                     ↓
             Signal Detection
                     │
                     ↓
              ICP Matching
                     │
                     ↓
              Product Fit
                     │
                     ↓
            Historical Models
                     │
                     ↓
             ML Prediction
                     │
                     ↓
             AI Reasoning
                     │
                     ↓
             Score Aggregator
                     │
                     ↓
              Calibration
                     │
                     ↓
             Confidence Model
                     │
                     ↓
             Explainability
                     │
                     ↓
              Priority Engine
                     │
                     ↓
          Human Review if Required
                     │
                     ↓
             Final Business Score
                     │
                     ↓
             Next-Best-Action
```

---

## 11. HYBRID AI + HUMAN SCORING MODEL

```text
                         Lead
                           │
                           ↓
                    Scoring Engine
                           │
            ┌──────────────┼──────────────┐
            ↓              ↓              ↓
          Rules            ML             AI
            │              │              │
            └──────────────┼──────────────┘
                           ↓
                     Score Fusion
                           │
                           ↓
                     Confidence
                           │
              ┌────────────┴────────────┐
              ↓                         ↓
       High Confidence            Low Confidence
              │                         │
              ↓                         ↓
       AI Recommendation           Human Review
              │                         │
              └────────────┬────────────┘
                           ↓
                     Final Decision
                           │
                           ↓
                     Sales Action
                           │
                           ↓
                       Outcome
                           │
                           ↓
                    Model Feedback
```

---

## 12. SCORING FORMULA

A configurable default model may be:

```text
Overall Score =
(
    ICP Fit × 0.20
  + Company Fit × 0.10
  + Contact Fit × 0.08
  + Intent × 0.18
  + Engagement × 0.10
  + Buying Signals × 0.12
  + Product Fit × 0.08
  + Technology Fit × 0.04
  + Revenue Potential × 0.05
  + Data Confidence × 0.05
)
-
(
    Risk × 0.10
)
```

The actual production weights shall be configurable.

The system shall support organization-specific models.

---

## 13. SCORE DIMENSIONS

## 13.1 ICP Fit

Measures how closely the lead matches the organization's ideal customer profile.

---

## 13.2 Company Fit

Measures company-level suitability.

---

## 13.3 Contact Fit

Measures whether the contact is relevant to the buying process.

---

## 13.4 Intent

Measures demonstrated interest in relevant products or solutions.

---

## 13.5 Engagement

Measures interaction with:

* website,
* campaigns,
* email,
* content,
* product,
* sales representatives.

---

## 13.6 Buying Signals

Measures business events indicating potential purchasing activity.

---

## 13.7 Product Fit

Measures compatibility between the prospect's likely problem and the organization's product.

---

## 13.8 Technology Fit

Measures technology compatibility.

---

## 13.9 Revenue Potential

Measures expected economic value.

---

## 13.10 Urgency

Measures how quickly the opportunity should be pursued.

---

## 13.11 Risk

Measures factors that may reduce the likelihood or value of conversion.

---

## 13.12 Data Confidence

Measures confidence in the underlying data.

---

## 14. AI EXPLANATION ARCHITECTURE

```text
                Final Score
                    │
                    ↓
             Contribution Model
                    │
        ┌───────────┼───────────┐
        ↓           ↓           ↓
     Positive    Negative     Neutral
     Factors     Factors      Factors
        │           │           │
        └───────────┼───────────┘
                    ↓
              Evidence Layer
                    │
                    ↓
            Explanation Engine
                    │
                    ↓
             Human Readable
               Explanation
```

The explanation shall distinguish:

```text
Observed Fact
Predicted Result
AI Inference
Human Input
```

---

## 15. MODEL TRAINING ARCHITECTURE

```text
Historical CRM Data
        +
Marketing Data
        +
Sales Data
        +
Engagement Data
        +
Revenue Data
        ↓
Data Validation
        ↓
Feature Engineering
        ↓
Training Dataset
        ↓
Train / Validation / Test
        ↓
Model Training
        ↓
Evaluation
        ↓
Calibration
        ↓
Bias / Quality Checks
        ↓
Approval
        ↓
Shadow Deployment
        ↓
Canary
        ↓
Production
```

---

## 16. TRAINING TARGETS

Possible targets:

```text
Lead Qualification
Opportunity Creation
Deal Conversion
Revenue Generation
Time-to-Conversion
Customer Lifetime Value
```

The platform shall support separate models for separate objectives.

---

## 17. MODEL EVALUATION

Minimum evaluation:

```text
Precision
Recall
F1
ROC-AUC
PR-AUC
Calibration
Lift
Gain
Conversion Lift
Revenue Lift
```

For revenue prediction:

```text
MAE
RMSE
MAPE
R²
```

where appropriate.

---

## 18. MODEL MONITORING

The platform shall continuously monitor:

```text
Input Distribution
Score Distribution
Prediction Distribution
Conversion Distribution
Revenue Distribution
Model Latency
Model Errors
Human Overrides
Actual Outcomes
```

---

## 19. DRIFT MANAGEMENT

```text
Data Drift
     ↓
Detection
     ↓
Impact Assessment
     ↓
Model Evaluation
     ↓
Retraining Decision
     ↓
Retraining
     ↓
Validation
     ↓
Approval
     ↓
Deployment
```

---

## 20. AI PROVIDER ROUTING

SalesGenie shall use an AI abstraction layer.

Example:

```text
                  AI Gateway
                      │
        ┌─────────────┼─────────────┐
        ↓             ↓             ↓
      Groq         Gemini        Mistral
        │             │             │
        └─────────────┼─────────────┘
                      ↓
                 AI Response
```

The system shall select providers based on:

* task,
* availability,
* latency,
* cost,
* quality,
* rate limits,
* privacy policy.

The scoring engine shall remain functional even when an external LLM provider is unavailable.

---

## 21. API REQUIREMENTS

Suggested APIs:

```text
POST /api/v1/scoring/leads/{lead_id}/score
GET  /api/v1/scoring/leads/{lead_id}
GET  /api/v1/scoring/leads/{lead_id}/history
GET  /api/v1/scoring/leads/{lead_id}/explanation

POST /api/v1/scoring/bulk
POST /api/v1/scoring/simulate

GET  /api/v1/scoring/models
GET  /api/v1/scoring/models/{model_id}
GET  /api/v1/scoring/models/{model_id}/performance

GET  /api/v1/scoring/configuration
PUT  /api/v1/scoring/configuration

GET  /api/v1/scoring/segments
POST /api/v1/scoring/segments

GET  /api/v1/scoring/analytics
GET  /api/v1/scoring/alerts
```

---

## 22. EVENT CONTRACTS

## LeadScoreUpdated

```json
{
  "event": "lead.score.updated",
  "lead_id": "uuid",
  "organization_id": "uuid",
  "previous_score": 72,
  "new_score": 91,
  "confidence": 0.94,
  "model_id": "lead-scoring-model",
  "model_version": "3.4.0",
  "timestamp": "ISO-8601"
}
```

---

## LeadPriorityChanged

```json
{
  "event": "lead.priority.changed",
  "lead_id": "uuid",
  "previous_priority": "P2",
  "new_priority": "P0",
  "reason": "high_intent_detected"
}
```

---

## HumanReviewRequired

```json
{
  "event": "lead.scoring.review_required",
  "lead_id": "uuid",
  "reason": "low_model_confidence",
  "confidence": 0.42,
  "recommended_action": "human_review"
}
```

---

## 23. DATABASE REQUIREMENTS

## Lead Score

```text
lead_score_id
lead_id
organization_id
workplace_id
overall_score
icp_score
company_fit_score
contact_fit_score
intent_score
engagement_score
buying_signal_score
product_fit_score
technology_fit_score
conversion_probability
revenue_potential
urgency_score
risk_score
data_confidence
priority
model_id
model_version
created_at
updated_at
```

---

## Score History

```text
score_history_id
lead_id
previous_score
new_score
score_delta
trigger_event
reason
model_version
confidence
created_at
```

---

## Score Explanation

```text
explanation_id
lead_id
score_id
positive_factors
negative_factors
evidence
confidence
model_version
created_at
```

---

## 24. SECURITY REQUIREMENTS

The scoring engine shall enforce:

```text
Authentication
Authorization
RBAC
ABAC
Tenant Isolation
Encryption
Audit Logging
Rate Limiting
Secrets Management
API Validation
```

---

## 25. AI SECURITY REQUIREMENTS

The scoring system shall treat all externally supplied lead content as untrusted.

The system shall protect against:

```text
Prompt Injection
Indirect Prompt Injection
Data Poisoning
Malicious Content
Unauthorized Tool Invocation
Cross-Tenant Data Leakage
Sensitive Information Exposure
Model Manipulation
```

AI-generated scoring shall never bypass authorization.

---

## 26. PRIVACY REQUIREMENTS

The system shall:

* minimize data collection,
* track source provenance,
* enforce retention policies,
* support deletion,
* support export,
* enforce tenant-specific policies,
* restrict access to authorized personnel.

---

## 27. PERFORMANCE REQUIREMENTS

## Interactive

Target:

```text
Cached score retrieval:
< 300 ms

Standard score calculation:
< 2 seconds

Complex AI scoring:
Asynchronous where necessary
```

These targets shall be validated through production-like load testing.

---

## 28. SCALABILITY REQUIREMENTS

The architecture shall support:

```text
10M+ leads
1M+ accounts
High-volume events
Distributed scoring
Horizontal workers
Batch scoring
Real-time scoring
Multi-region deployment
```

Exact production capacity shall be validated through benchmark testing.

---

## 29. RELIABILITY

The service shall support:

* retries,
* idempotency,
* circuit breakers,
* dead-letter queues,
* provider failover,
* graceful degradation,
* score persistence,
* recovery from worker failure.

If AI providers become unavailable:

```text
AI unavailable
      ↓
Use ML model
      ↓
Use deterministic rules
      ↓
Mark AI explanation unavailable
      ↓
Continue scoring
```

---

## 30. GRACEFUL DEGRADATION

The scoring engine shall have the following fallback hierarchy:

```text
Level 1:
AI + ML + Rules

Level 2:
ML + Rules

Level 3:
Rules

Level 4:
Last Known Valid Score

Level 5:
Human Review
```

The system shall never silently fabricate a score.

---

## 31. OBSERVABILITY

Required metrics:

```text
score_requests_total
score_success_total
score_failure_total
score_latency_ms
model_latency_ms
ai_latency_ms
model_error_rate
ai_provider_error_rate
human_override_rate
prediction_accuracy
conversion_lift
revenue_lift
score_distribution
confidence_distribution
```

---

## 32. AUDIT LOGGING

Critical actions shall create immutable audit events.

Example:

```text
Who:
Sales Manager

Action:
Changed Lead Score

Lead:
L-10293

Old Score:
76

New Score:
88

Reason:
Confirmed enterprise budget

Timestamp:
ISO-8601

Source:
Human Override
```

---

## 33. ROLE-BASED CAPABILITIES

## Super Admin

Can:

* manage global scoring policies,
* manage scoring infrastructure,
* inspect system-wide model performance,
* configure global safety policies.

---

## Organization Admin

Can:

* configure organization scoring,
* define ICP,
* configure thresholds,
* manage team scoring policies.

---

## Sales Manager

Can:

* view team scores,
* configure sales thresholds,
* override scores,
* inspect performance.

---

## Sales Agent

Can:

* view assigned scores,
* view explanations,
* view recommendations,
* provide feedback.

---

## Marketing Manager

Can:

* analyze lead quality,
* evaluate campaigns,
* configure marketing scoring dimensions.

---

## Business Analyst

Can:

* analyze score distributions,
* evaluate model performance,
* analyze revenue correlation.

---

## Finance Manager

Can:

* inspect revenue-weighted scores,
* analyze expected revenue,
* evaluate ROI.

---

## 34. SCORE LIFECYCLE

```text
Lead Created
     ↓
Initial Score
     ↓
Enrichment
     ↓
Score Updated
     ↓
Behavior Detected
     ↓
Intent Updated
     ↓
Score Updated
     ↓
Opportunity Created
     ↓
Score Updated
     ↓
Deal Won/Lost
     ↓
Outcome Recorded
     ↓
Model Feedback
```

---

## 35. SCORE STATE MACHINE

```text
                  ┌──────────────┐
                  │   CREATED    │
                  └──────┬───────┘
                         ↓
                  ┌──────────────┐
                  │    SCORED    │
                  └──────┬───────┘
                         ↓
             ┌───────────┴───────────┐
             ↓                       ↓
         LOW SCORE               HIGH SCORE
             ↓                       ↓
         NURTURE                PRIORITY
                                     ↓
                              HUMAN REVIEW?
                               /          \
                             YES           NO
                             ↓              ↓
                         REVIEWED       AUTOMATION
                             \              /
                              └──────┬───────┘
                                     ↓
                                  OUTCOME
                                     ↓
                                MODEL FEEDBACK
```

---

## 36. BUSINESS ANALYTICS

The system shall calculate:

```text
Lead Score → Qualification Rate
Lead Score → Opportunity Rate
Lead Score → Conversion Rate
Lead Score → Revenue
```

Example:

```text
Score 90–100
Conversion = 31%

Score 80–89
Conversion = 21%

Score 70–79
Conversion = 12%

Score 60–69
Conversion = 7%

Score <60
Conversion = 2%
```

Actual values shall come from the customer's historical data.

---

## 37. REVENUE-AWARE PRIORITIZATION

The system shall support expected value:

```text
Expected Revenue =
Conversion Probability × Potential Deal Value
```

Example:

```text
Lead A
Conversion Probability = 90%
Deal Value = $10,000

Expected Revenue = $9,000
```

```text
Lead B
Conversion Probability = 60%
Deal Value = $50,000

Expected Revenue = $30,000
```

The system may prioritize Lead B despite its lower conversion probability.

---

## 38. TIME-AWARE PRIORITIZATION

The scoring engine shall optionally consider:

```text
Expected Revenue
×
Urgency
×
Probability
```

to identify immediate opportunities.

---

## 39. LEAD MOMENTUM

The system shall calculate score momentum.

Example:

```text
Current Score: 88
Previous Score: 65

Momentum: +23
Status: Accelerating
```

Momentum shall be available for:

* daily,
* weekly,
* monthly

time windows.

---

## 40. AI RECOMMENDATION EXAMPLE

```text
Lead:
Enterprise SaaS Company

Overall Score:
93

Conversion Probability:
86%

Expected Revenue:
$42,000

Intent:
95

Why:
- Strong ICP fit
- CTO identified
- High pricing-page engagement
- Recent technology migration
- Similar customers converted successfully

Recommendation:
Assign to senior enterprise sales representative.

Priority:
P0

Recommended Timing:
Immediate

Confidence:
92%
```

---

## 41. NATURAL LANGUAGE ANALYTICS

Users may ask:

```text
"Which leads should my sales team contact today?"

"Which leads have the highest expected revenue?"

"Why did this lead lose priority?"

"Show me leads whose score increased by more than 20 points."

"Which campaigns produce the highest scoring leads?"

"Which industries have the highest conversion rate for high-score leads?"
```

The system shall translate natural-language requests into authorized analytical operations.

---

## 42. SCORE GOVERNANCE

Every scoring model shall have:

```text
Owner
Purpose
Training Data
Features
Weights
Thresholds
Model Version
Approval Status
Effective Date
Review Date
Performance Metrics
Rollback Version
```

---

## 43. MODEL APPROVAL

Production deployment shall require configurable approval.

Example:

```text
Developer
   ↓
ML Engineer
   ↓
Business Analyst
   ↓
Sales/Business Owner
   ↓
Security Review
   ↓
Production
```

---

## 44. MODEL CHANGE MANAGEMENT

Every model change shall record:

```text
Old Model
New Model
Reason
Expected Impact
Validation Results
Approver
Deployment Time
Rollback Plan
```

---

## 45. A/B TESTING

The system shall support experiments such as:

```text
Model A → 50%
Model B → 50%
```

Evaluation:

```text
Conversion Rate
Revenue
Sales Productivity
False Positive Rate
False Negative Rate
```

---

## 46. ACCEPTANCE CRITERIA

The module shall be considered production-ready when:

* every eligible lead can receive a score,
* score dimensions are available,
* scoring is explainable,
* scores update from events,
* score history is maintained,
* custom scoring is supported,
* ML scoring is supported,
* AI-assisted scoring is supported,
* conversion probability is available,
* revenue potential is available,
* human overrides work,
* human review works,
* model versions are tracked,
* model performance is measurable,
* model drift is detectable,
* tenant isolation is enforced,
* audit logs are available,
* API access is secured,
* batch scoring works,
* real-time scoring works,
* provider failure does not destroy scoring availability,
* score simulations do not modify production data,
* CRM synchronization works,
* dashboards provide actionable intelligence.

---

## 47. TESTING REQUIREMENTS

The module shall include:

## Unit Testing

* scoring calculations,
* rule evaluation,
* normalization,
* threshold logic,
* score aggregation.

## Integration Testing

* CRM,
* lead intelligence,
* event bus,
* AI gateway,
* feature store,
* database.

## ML Testing

* accuracy,
* calibration,
* drift,
* bias,
* robustness.

## Security Testing

* tenant isolation,
* authorization,
* API security,
* prompt injection,
* data leakage.

## Load Testing

* concurrent scoring,
* batch scoring,
* event throughput,
* AI provider failure.

## Chaos Testing

Test:

```text
AI provider unavailable
Database unavailable
Redis unavailable
Event broker unavailable
Scoring worker failure
Network failure
```

---

## 48. END-TO-END EXAMPLE

```text
Lead Created
     ↓
Company = B2B SaaS
     ↓
Company Size = 500
     ↓
Industry = Target
     ↓
CTO Identified
     ↓
Technology Fit = High
     ↓
Pricing Page Viewed 5 Times
     ↓
Demo Requested
     ↓
Intent = 94
     ↓
ICP Fit = 96
     ↓
Engagement = 91
     ↓
Buying Signal = 89
     ↓
Revenue Potential = $80K
     ↓
ML Conversion Probability = 84%
     ↓
Risk = 10%
     ↓
Data Confidence = 95%
     ↓
Overall Score = 93
     ↓
Priority = P0
     ↓
AI Recommendation:
"Assign enterprise sales representative immediately."
     ↓
Human Approval
     ↓
Sales Action
     ↓
Opportunity Created
     ↓
Deal Won
     ↓
Revenue Recorded
     ↓
Model Feedback
```

---

## 49. FINAL ARCHITECTURE

```text
                         SALESGENIE
                              │
                              ↓
                     Lead Intelligence
                              │
                              ↓
                    Feature Engineering
                              │
        ┌─────────────────────┼─────────────────────┐
        ↓                     ↓                     ↓
   Firmographic           Behavioral          Technographic
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              ↓
                         Intent Engine
                              │
                              ↓
                       Signal Engine
                              │
                              ↓
                         ICP Engine
                              │
                              ↓
                       Product Fit
                              │
                              ↓
                    ┌──────────────────┐
                    │ Scoring Platform │
                    └────────┬─────────┘
                             │
              ┌──────────────┼──────────────┐
              ↓              ↓              ↓
            Rules            ML             AI
              │              │              │
              └──────────────┼──────────────┘
                             ↓
                      Score Aggregator
                             ↓
                       Calibration
                             ↓
                       Confidence
                             ↓
                      Explainability
                             ↓
                      Priority Engine
                             ↓
                 Next-Best-Action Engine
                             ↓
                 Human Review if Needed
                             ↓
                       Sales / CRM
                             ↓
                         Outcome
                             ↓
                    Revenue Analytics
                             ↓
                       Model Feedback
                             ↓
                     Continuous Learning
```

---

## 50. FINAL PRODUCT PRINCIPLE

SalesGenie's AI-Based Lead Scoring system shall not be a simple:

```text
Lead → Number
```

system.

It shall be:

```text
Lead
 ↓
Evidence
 ↓
Features
 ↓
Context
 ↓
Intent
 ↓
Behavior
 ↓
Business Fit
 ↓
Prediction
 ↓
Confidence
 ↓
Explainability
 ↓
Priority
 ↓
Action
 ↓
Outcome
 ↓
Learning
```

The ultimate goal is:

```text
              Better Lead Selection
                       ↓
              Better Sales Prioritization
                       ↓
              Better Sales Decisions
                       ↓
              Less Wasted Effort
                       ↓
              Higher Conversion
                       ↓
              Higher Revenue
                       ↓
              Better Customer ROI
```

SalesGenie shall therefore treat lead scoring as a **continuous revenue-intelligence system**, not a static CRM field.

**End of `AI_based_lead_scoring.md`**
