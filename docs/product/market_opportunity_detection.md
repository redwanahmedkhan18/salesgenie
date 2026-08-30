# Market Opportunity Detection — User Requirements, System Requirements & Functional Requirements

**Document:** `market_opportunity_detection.md`  
**Product:** SalesGenie / Enterprise AI Sales, Marketing & Growth Intelligence Platform  
**Capability:** AI + Humanized Market Opportunity Detection  
**Execution Model:** AI-Based + Human-in-the-Loop + Humanized Expert Analysis  
**Requirement Level:** FAANG-Level / Enterprise-Grade  
**Version:** 1.0  
**Status:** Production Specification

---

## 1. Purpose

The `market_opportunity_detection` module shall identify, validate, prioritize, monitor, and operationalize market opportunities for an organization's products, services, campaigns, sales strategy, and go-to-market initiatives.

The system shall combine:

- AI-powered market intelligence
- Market trend analysis
- Customer demand analysis
- Competitor intelligence
- Product intelligence
- Search intelligence
- Sales intelligence
- Customer feedback
- Pricing intelligence
- Geographic intelligence
- Industry intelligence
- Human expert analysis
- Human validation
- Continuous opportunity monitoring

The system shall convert heterogeneous market signals into evidence-backed opportunities.

The core pipeline shall be:

```text
Market Signals
      ↓
Data Collection
      ↓
Data Validation
      ↓
Signal Extraction
      ↓
Trend Detection
      ↓
Demand Analysis
      ↓
Competitor Analysis
      ↓
Opportunity Detection
      ↓
Opportunity Scoring
      ↓
Opportunity Validation
      ↓
Human Review When Required
      ↓
Strategic Recommendation
      ↓
Action Plan
      ↓
Continuous Monitoring
```

The system shall explicitly distinguish between:

```text
VERIFIED
SUPPORTED
INFERRED
PREDICTED
ESTIMATED
CONFLICTING
STALE
UNKNOWN
```

AI-generated opportunities shall never be represented as guaranteed business outcomes.

---

## 2. Business Objectives

The system shall:

* Discover emerging market opportunities.
* Identify underserved customer segments.
* Identify unmet customer needs.
* Identify emerging demand.
* Detect market gaps.
* Detect competitor weaknesses that create opportunities.
* Detect technology-driven opportunities.
* Detect geographic opportunities.
* Detect pricing opportunities.
* Detect product opportunities.
* Detect marketing opportunities.
* Detect SEO opportunities.
* Detect sales opportunities.
* Detect partnership opportunities.
* Detect expansion opportunities.
* Detect product-launch opportunities.
* Estimate opportunity attractiveness.
* Estimate market potential.
* Estimate competitive intensity.
* Estimate execution difficulty.
* Prioritize opportunities.
* Recommend actions.
* Continuously monitor opportunities.
* Allow human experts to validate AI findings.
* Support executive decision-making.

---

## 3. Scope

## 3.1 In Scope

The system shall support:

* Market opportunity discovery
* Opportunity identification
* Opportunity classification
* Market gap detection
* Demand-signal detection
* Customer pain-point analysis
* Customer segment discovery
* Emerging trend detection
* Competitor-gap analysis
* Competitor weakness analysis
* Product opportunity detection
* Feature opportunity detection
* Pricing opportunity detection
* Geographic opportunity detection
* Industry opportunity detection
* Technology opportunity detection
* AI opportunity detection
* Marketing opportunity detection
* SEO opportunity detection
* Sales opportunity detection
* Partnership opportunity detection
* Distribution opportunity detection
* Cross-sell opportunity detection
* Upsell opportunity detection
* New-market opportunity detection
* Product-launch opportunity detection
* Opportunity scoring
* Opportunity ranking
* Opportunity validation
* Human review
* Opportunity lifecycle management
* Opportunity alerts
* Opportunity forecasting
* Opportunity reports
* Executive dashboards
* Opportunity APIs
* Event-driven processing
* Audit logging
* Multi-tenant isolation
* RBAC
* ABAC
* AI governance

---

## 4. Out of Scope

The system shall not:

* Guarantee market success.
* Guarantee revenue.
* Fabricate market demand.
* Present AI predictions as factual market data.
* Access unauthorized private information.
* Circumvent authentication or security controls.
* Conduct unauthorized competitor penetration testing.
* Manipulate markets.
* Generate deceptive market intelligence.
* Automatically make irreversible strategic decisions without authorization.
* Publish external market claims without appropriate approval.

---

## 5. Core Design Principles

The system shall follow:

```text
Evidence Before Assertion
Human Oversight for High-Impact Decisions
Explainability by Default
Source Provenance
Continuous Revalidation
Tenant Isolation
Least Privilege
Fail-Safe Automation
Configurable Opportunity Models
Explicit Uncertainty
Versioned Intelligence
Auditability
```

---

## 6. AI-Based Execution Model

The AI engine shall:

* Analyze market data.
* Detect patterns.
* Identify demand signals.
* Identify unmet needs.
* Detect market gaps.
* Analyze competitor weaknesses.
* Analyze customer sentiment.
* Detect emerging trends.
* Identify potentially underserved segments.
* Generate opportunity hypotheses.
* Score opportunities.
* Rank opportunities.
* Predict potential opportunity momentum.
* Recommend validation actions.
* Generate strategic recommendations.

AI shall produce structured outputs rather than unrestricted prose whenever possible.

---

## 7. Humanized Execution Model

Authorized human experts shall be able to:

* Review AI opportunities.
* Validate evidence.
* Reject false opportunities.
* Modify opportunity scores.
* Add proprietary business knowledge.
* Add customer intelligence.
* Add sales intelligence.
* Add market knowledge.
* Change opportunity priority.
* Add strategic context.
* Approve opportunities.
* Assign opportunity research tasks.
* Request additional evidence.
* Lock validated opportunity assessments.

---

## 8. Hybrid AI + Human Workflow

```text
AI Discovery
      ↓
Signal Collection
      ↓
Signal Validation
      ↓
Opportunity Hypothesis
      ↓
AI Scoring
      ↓
Confidence Assessment
      ↓
Risk Assessment
      ↓
Human Review
      ↓
Approved Opportunity
      ↓
Strategic Recommendation
      ↓
Execution Plan
      ↓
Continuous Monitoring
```

---

## 9. User Roles

## 9.1 Organization Owner

The Organization Owner shall be able to:

* View organization-wide opportunities.
* Configure opportunity policies.
* Approve strategic opportunities.
* Configure opportunity thresholds.
* Access executive intelligence.
* Control sensitive opportunity data.

---

## 9.2 Organization Admin

The Organization Admin shall be able to:

* Configure opportunity permissions.
* Manage opportunity sources.
* Manage integrations.
* Configure opportunity workflows.
* Review audit logs.

---

## 9.3 Workplace Admin

The Workplace Admin shall be able to:

* Configure workspace opportunity monitoring.
* Manage opportunity access.
* Configure workspace data sources.
* Review workspace opportunity activity.

---

## 9.4 Product Manager

The Product Manager shall be able to:

* Discover product opportunities.
* Identify feature gaps.
* Identify unmet customer needs.
* Analyze product-market gaps.
* Prioritize product opportunities.

---

## 9.5 Marketing Manager

The Marketing Manager shall be able to:

* Identify marketing opportunities.
* Detect emerging audiences.
* Detect messaging opportunities.
* Identify content opportunities.
* Identify campaign opportunities.

---

## 9.6 Marketing Specialist

The Marketing Specialist shall be able to:

* Analyze specific opportunity segments.
* Research customer needs.
* Validate marketing opportunities.
* Build opportunity-specific campaigns.

---

## 9.7 SEO Manager

The SEO Manager shall be able to:

* Identify search-demand opportunities.
* Detect keyword gaps.
* Detect content gaps.
* Detect emerging search trends.
* Prioritize SEO opportunities.

---

## 9.8 Sales Manager

The Sales Manager shall be able to:

* Identify new customer segments.
* Detect sales opportunities.
* Identify competitor gaps.
* Analyze buying signals.
* Prioritize sales opportunities.

---

## 9.9 Sales Agent

The Sales Agent shall be able to:

* Submit customer opportunity signals.
* Report customer pain points.
* Report competitor gaps.
* Submit field intelligence.
* View approved opportunities.

---

## 9.10 Business Analyst

The Business Analyst shall be able to:

* Analyze opportunity models.
* Validate opportunity evidence.
* Compare opportunity scenarios.
* Build opportunity reports.
* Perform opportunity research.

---

## 9.11 Finance Manager

The Finance Manager shall be able to:

* Review financial opportunity potential.
* Analyze estimated economics.
* Evaluate cost implications.
* Review revenue assumptions.

---

## 9.12 AI Agent

The AI Agent shall be able to:

* Execute opportunity discovery workflows.
* Analyze permitted data.
* Generate opportunity hypotheses.
* Score opportunities.
* Request human validation.
* Monitor opportunity changes.

---

## 10. User Requirements

## UR-001 — Opportunity Discovery

Users shall be able to discover potential market opportunities based on:

* Product
* Industry
* Geography
* Customer segment
* Market
* Keywords
* Trends
* Competitors
* Customer problems
* Technology
* Business model

---

## UR-002 — Opportunity Search

Users shall be able to search opportunities using:

```text
Product
Industry
Segment
Region
Opportunity Type
Priority
Score
Confidence
Status
Date
```

---

## UR-003 — Opportunity Profile

Each opportunity shall contain:

```text
Opportunity ID
Title
Description
Opportunity Type
Market
Industry
Customer Segment
Geography
Evidence
Demand Signals
Market Size Indicators
Competitive Landscape
Customer Pain
Business Impact
Opportunity Score
Confidence
Risk
Priority
Status
Owner
Created Date
Last Updated
```

---

## UR-004 — Unmet Need Detection

The system shall identify unmet or underserved customer needs.

Examples:

```text
High customer demand
+
Limited existing solutions
=
Potential market opportunity
```

---

## UR-005 — Market Gap Detection

The system shall identify gaps between:

```text
Customer Need
vs
Available Solutions
```

---

## UR-006 — Competitor Gap Detection

The system shall identify opportunities created by:

```text
Competitor Weakness
+
Customer Demand
+
Organization Capability
```

---

## UR-007 — Emerging Trend Detection

Users shall be able to identify emerging trends that may create future opportunities.

The system shall classify trends as:

```text
Emerging
Growing
Established
Declining
Uncertain
```

---

## UR-008 — Demand Signal Detection

The system shall detect demand signals from permitted sources.

Examples:

```text
Search demand
Customer questions
Customer complaints
Sales inquiries
Product requests
Review trends
Social discussions
Market reports
Industry developments
```

---

## UR-009 — Customer Pain Analysis

The system shall identify recurring:

* Problems
* Complaints
* Feature requests
* Service gaps
* Pricing concerns
* Workflow inefficiencies
* Product limitations

---

## UR-010 — Customer Segment Opportunities

The system shall identify potentially underserved:

* Enterprise customers
* Mid-market customers
* SMBs
* Startups
* Developers
* Professionals
* Specific industries
* Geographic segments
* Demographic segments where legally and ethically appropriate

---

## UR-011 — Geographic Opportunity

The system shall identify potential opportunities by:

* Country
* Region
* City
* Market
* Economic zone

---

## UR-012 — Industry Opportunity

The system shall identify opportunities within:

* SaaS
* E-commerce
* Healthcare
* Finance
* Education
* Manufacturing
* Logistics
* Real estate
* Retail
* Professional services
* Other configurable industries

---

## UR-013 — Product Opportunity

The system shall identify:

* New products
* Product extensions
* New features
* Product bundles
* Product improvements
* New use cases

---

## UR-014 — Pricing Opportunity

The system shall identify potential:

* Premium pricing opportunities
* Value pricing opportunities
* Lower-cost opportunities
* Usage-based opportunities
* Bundling opportunities
* Freemium opportunities
* Enterprise pricing opportunities

All pricing recommendations shall be presented as analytical recommendations rather than guaranteed optimal prices.

---

## UR-015 — Marketing Opportunity

The system shall identify:

* New audiences
* New messaging
* New channels
* New campaigns
* New content themes
* New positioning opportunities

---

## UR-016 — SEO Opportunity

The system shall identify:

* Keyword gaps
* Emerging search demand
* Content gaps
* Competitor keyword gaps
* Long-tail opportunities
* Search intent gaps

---

## UR-017 — Sales Opportunity

The system shall identify:

* New account segments
* Buying signals
* Industry opportunities
* Geographic expansion
* Cross-sell opportunities
* Upsell opportunities
* Competitive displacement opportunities

---

## UR-018 — Partnership Opportunity

The system shall identify potential opportunities involving:

* Technology partners
* Distribution partners
* Channel partners
* Strategic partnerships
* Integration partnerships

---

## UR-019 — Technology Opportunity

The system shall identify market opportunities created by:

* AI
* Automation
* Cloud
* APIs
* Data platforms
* Emerging technologies
* Workflow transformation

---

## UR-020 — Opportunity Classification

The system shall classify opportunities as:

```text
PRODUCT
FEATURE
MARKETING
SEO
SALES
PRICING
GEOGRAPHIC
INDUSTRY
TECHNOLOGY
PARTNERSHIP
DISTRIBUTION
CROSS_SELL
UPSELL
NEW_MARKET
PRODUCT_LAUNCH
CUSTOMER_EXPERIENCE
```

---

## UR-021 — Opportunity Score

Each opportunity shall receive a configurable score based on:

```text
Market Demand
Market Potential
Customer Pain
Competitive Gap
Strategic Fit
Organization Capability
Execution Difficulty
Risk
Timing
```

---

## UR-022 — Opportunity Confidence

The system shall provide:

```text
Very High
High
Medium
Low
Very Low
```

confidence levels.

---

## UR-023 — Opportunity Priority

The system shall classify opportunities:

```text
P0 — Critical
P1 — High
P2 — Medium
P3 — Low
```

---

## UR-024 — Opportunity Ranking

Users shall be able to rank opportunities based on:

* Score
* Market potential
* Revenue potential
* Strategic fit
* Confidence
* Urgency
* Execution feasibility

---

## UR-025 — Opportunity Comparison

Users shall be able to compare multiple opportunities.

Example:

```text
Opportunity A
vs
Opportunity B
vs
Opportunity C
```

---

## UR-026 — Opportunity Evidence

Each opportunity shall contain:

```text
Evidence
Source
Source Type
Source Date
Evidence Quality
Confidence
Corroboration
Verification Status
```

---

## UR-027 — Human Validation

Users shall be able to:

```text
Approve
Reject
Modify
Request Evidence
Reassign
Escalate
Archive
```

---

## UR-028 — Human Override

Authorized humans shall be able to override:

* Opportunity score
* Opportunity priority
* Opportunity category
* Confidence
* Business impact
* Recommendation

The original AI result shall remain preserved.

---

## UR-029 — Opportunity Recommendations

The system shall recommend:

```text
Build
Launch
Test
Validate
Invest
Monitor
Partner
Expand
Reposition
Price
Bundle
Market
Do Not Pursue
```

---

## UR-030 — Opportunity Validation Plan

For high-value opportunities, the system shall generate validation plans containing:

```text
Hypothesis
Target Segment
Problem
Proposed Solution
Validation Method
Success Metric
Required Sample
Timeframe
Budget
Decision Threshold
```

---

## UR-031 — Opportunity Alerts

Users shall receive alerts when:

* Opportunity score increases.
* Demand increases.
* Competitor weakness emerges.
* Market trend accelerates.
* Customer pain increases.
* Market conditions change.
* Opportunity confidence changes.

---

## UR-032 — Opportunity Lifecycle

Users shall manage:

```text
DISCOVERED
UNDER_ANALYSIS
VALIDATION_REQUIRED
VALIDATION_IN_PROGRESS
VALIDATED
APPROVED
IN_EXECUTION
MONITORING
DECLINED
EXPIRED
ARCHIVED
```

---

## UR-033 — Opportunity Ownership

Each opportunity shall have:

```text
Owner
Team
Priority
Deadline
Status
Approver
```

---

## UR-034 — Opportunity Reports

Users shall be able to generate:

* Market opportunity reports
* Executive opportunity reports
* Product opportunity reports
* Sales opportunity reports
* Marketing opportunity reports
* SEO opportunity reports
* Geographic opportunity reports
* Competitive opportunity reports

---

## UR-035 — Opportunity Export

Authorized users shall be able to export:

```text
PDF
CSV
XLSX
JSON
Markdown
```

---

## 11. System Requirements

## SR-001 — Distributed Architecture

The service shall support:

```text
Frontend
    ↓
API Gateway
    ↓
Market Opportunity Service
    ↓
Opportunity Orchestrator
    ├── Signal Engine
    ├── Demand Engine
    ├── Trend Engine
    ├── Market Gap Engine
    ├── Competitor Gap Engine
    ├── Customer Pain Engine
    ├── Segment Engine
    ├── Opportunity Scoring Engine
    ├── Forecast Engine
    └── Recommendation Engine
    ↓
AI Gateway
    ├── Groq
    ├── Gemini / Google AI
    ├── Mistral
    └── Other Approved Providers
    ↓
Data Platform
```

---

## SR-002 — AI Provider Abstraction

All LLM operations shall use a provider-independent AI Gateway.

Business logic shall not be tightly coupled to Groq, Gemini, Mistral, or any single provider.

---

## SR-003 — AI Routing

The AI Gateway shall support:

* Model selection
* Provider selection
* Capability routing
* Failover
* Retry
* Rate limiting
* Cost controls
* Latency optimization
* Provider health checks

---

## SR-004 — Structured AI Output

AI output shall use strict schemas.

Invalid output shall be:

```text
Rejected
Retried
Corrected
or
Escalated
```

---

## SR-005 — Evidence Grounding

Opportunity claims shall be linked to evidence.

The system shall distinguish:

```text
Raw Evidence
Fact
Signal
Inference
Prediction
Recommendation
```

---

## SR-006 — No Hallucinated Opportunities

When evidence is insufficient, the system shall return:

```text
INSUFFICIENT EVIDENCE
```

or:

```text
LOW CONFIDENCE — HUMAN VALIDATION REQUIRED
```

---

## SR-007 — Opportunity Data Model

The system shall maintain:

```text
Opportunity
OpportunityEvidence
MarketSignal
DemandSignal
CustomerPainPoint
MarketGap
CompetitorGap
MarketTrend
CustomerSegment
GeographicMarket
IndustryMarket
OpportunityScore
OpportunityForecast
OpportunityRecommendation
ValidationPlan
OpportunityReview
OpportunityChange
OpportunityAlert
OpportunityExperiment
OpportunityDecision
AuditEvent
```

---

## SR-008 — Opportunity Schema

```text
opportunity_id
tenant_id
organization_id
workspace_id
title
description
type
market
industry
segment
geography
evidence_ids
signal_ids
demand_score
market_potential_score
competitive_gap_score
strategic_fit_score
execution_score
risk_score
overall_score
confidence
priority
status
owner_id
created_at
updated_at
```

---

## SR-009 — Evidence Provenance

Evidence shall include:

```text
source
source_type
source_reference
retrieved_at
published_at
content_hash
evidence_excerpt
quality_score
confidence
verification_status
```

---

## SR-010 — Historical Versioning

Opportunity assessments shall be versioned.

Previous scores shall never be silently overwritten.

---

## SR-011 — Opportunity Scoring Engine

Scoring shall be configurable by:

* Organization
* Industry
* Product
* Market
* Customer segment
* Opportunity type

---

## SR-012 — Data Quality Engine

The system shall evaluate:

```text
Completeness
Recency
Source Reliability
Specificity
Corroboration
Consistency
Verification
```

---

## 12. Functional Requirements

## FR-001 — Create Opportunity

The system shall support:

```http
POST /api/v1/market-opportunities
```

Example:

```json
{
  "title": "AI automation opportunity for SMB sales teams",
  "type": "PRODUCT",
  "market": "B2B SaaS",
  "segment": "SMB"
}
```

---

## FR-002 — Discover Opportunities

The system shall support:

```http
POST /api/v1/market-opportunities/discover
```

The request shall support:

```json
{
  "product_id": "PROD-001",
  "market": "SaaS",
  "regions": ["US", "UK", "EU"],
  "segments": ["SMB", "MID_MARKET"]
}
```

---

## FR-003 — Market Signal Extraction

The system shall extract:

```text
Demand
Pain
Growth
Decline
Search
Customer Intent
Competitive Change
Technology Change
Pricing Change
```

signals.

---

## FR-004 — Demand Signal Detection

The system shall detect demand using configurable signals.

Example:

```text
Search demand ↑
Customer requests ↑
Sales inquiries ↑
Competitor demand ↑
Industry interest ↑
```

---

## FR-005 — Market Gap Detection

The system shall calculate potential gaps between:

```text
Customer Demand
-
Available Market Supply
```

The calculation shall clearly indicate its methodology and limitations.

---

## FR-006 — Unmet Need Detection

The AI engine shall cluster customer pain points and identify recurring unmet needs.

---

## FR-007 — Competitor Gap Detection

The system shall consume approved competitor intelligence and identify gaps between:

```text
Competitor Capability
vs
Customer Requirement
```

---

## FR-008 — Product Opportunity Detection

The system shall identify potential:

* Products
* Features
* Extensions
* Bundles
* Integrations
* Services

---

## FR-009 — Segment Opportunity Detection

The system shall identify potentially underserved customer segments.

Each finding shall contain supporting evidence.

---

## FR-010 — Geographic Opportunity Detection

The system shall compare markets using:

```text
Demand
Competition
Market Growth
Customer Fit
Pricing
Distribution
Regulatory Complexity
Execution Difficulty
```

---

## FR-011 — Industry Opportunity Detection

The system shall identify industries exhibiting:

* Growing demand
* Operational pain
* Technology adoption
* Competitive gaps
* Regulatory changes
* Digital transformation needs

---

## FR-012 — Trend-Based Opportunity Detection

The system shall connect emerging trends to potential commercial opportunities.

Example:

```text
Trend:
AI Agent Adoption ↑

Potential Opportunity:
AI-powered workflow automation for SMBs
```

---

## FR-013 — Customer Pain Clustering

The system shall cluster related customer problems.

Example:

```text
Cluster:
Manual lead qualification

Frequency:
High

Severity:
High

Potential Opportunity:
AI lead qualification automation
```

---

## FR-014 — Opportunity Scoring

The system shall calculate an opportunity score using configurable weighted factors.

Example:

```text
Opportunity Score =
Market Potential
×
Demand
×
Strategic Fit
×
Competitive Gap
×
Organization Capability
×
Timing
```

Risk and execution difficulty shall be incorporated as configurable modifiers.

---

## FR-015 — Market Potential Estimation

The system may estimate:

```text
TAM
SAM
SOM
Growth Potential
Customer Count
Revenue Potential
```

All estimates shall include:

* Methodology
* Assumptions
* Evidence
* Confidence

---

## FR-016 — Opportunity Confidence

Confidence shall consider:

```text
Evidence Quality
Source Reliability
Recency
Corroboration
Model Agreement
Data Completeness
Human Validation
```

---

## FR-017 — Opportunity Ranking

The system shall rank opportunities using configurable business criteria.

---

## FR-018 — Opportunity Portfolio

The system shall display opportunities by:

```text
High Value / Low Risk
High Value / High Risk
Low Value / Low Risk
Low Value / High Risk
```

---

## FR-019 — Opportunity Matrix

The system shall support:

| Opportunity | Market Potential | Demand | Competition | Execution Difficulty | Score |
| ----------- | ---------------: | -----: | ----------: | -------------------: | ----: |
| A           |               90 |     87 |          65 |                   40 |    86 |
| B           |               78 |     91 |          82 |                   55 |    77 |
| C           |               69 |     74 |          45 |                   30 |    81 |

Scores shall be generated using the configured scoring model.

---

## FR-020 — Opportunity Forecast

The system may forecast:

```text
Demand Growth
Market Momentum
Competitive Pressure
Opportunity Window
```

Predictions shall be clearly labeled as forecasts.

---

## FR-021 — Opportunity Window

The system shall estimate:

```text
Immediate
Short-Term
Medium-Term
Long-Term
Uncertain
```

opportunity windows.

---

## FR-022 — Opportunity Timing

The system shall identify timing signals such as:

* Rising demand
* New technology adoption
* Competitor weakness
* Market expansion
* Regulatory changes
* Seasonal demand

---

## FR-023 — Opportunity Recommendation

The system shall recommend actions such as:

```text
Validate
Prototype
Launch
Expand
Partner
Invest
Monitor
Defer
Reject
```

---

## FR-024 — Validation Plan

For a high-value opportunity, the system shall generate:

```text
Hypothesis
Target Customer
Problem
Proposed Solution
Experiment
Success Metric
Failure Metric
Sample Size
Duration
Budget
Decision Rule
```

---

## FR-025 — Opportunity Experiment

Users shall be able to create validation experiments.

Example:

```json
{
  "opportunity_id": "OPP-001",
  "experiment": "Landing page demand test",
  "success_metric": "Qualified signup rate",
  "threshold": 0.08
}
```

---

## FR-026 — Human Review Queue

The system shall require human review when:

```text
Confidence < configured threshold
OR
Evidence conflict exists
OR
Strategic impact = HIGH
OR
Financial impact = HIGH
OR
External publication = TRUE
OR
AI uncertainty = HIGH
```

---

## FR-027 — Human Approval

Reviewers shall be able to:

```text
Approve
Reject
Modify
Request More Evidence
Escalate
Assign
```

---

## FR-028 — Human Override

Human changes shall preserve:

```text
AI Assessment
Human Assessment
Reviewer
Timestamp
Reason
Evidence
```

---

## FR-029 — Opportunity Lifecycle

The system shall support:

```text
DISCOVERED
ANALYZING
VALIDATION_REQUIRED
VALIDATING
VALIDATED
APPROVED
EXECUTING
MONITORING
DECLINED
EXPIRED
ARCHIVED
```

---

## FR-030 — Opportunity Ownership

The system shall assign:

```text
Owner
Team
Approver
Deadline
Priority
```

---

## FR-031 — Opportunity Change Detection

The system shall detect:

```text
Score Increase
Score Decrease
Demand Increase
Demand Decrease
Market Expansion
Market Contraction
Competitive Pressure Increase
Opportunity Expiration
```

---

## FR-032 — Opportunity Alerts

Example:

```text
Opportunity:
AI Sales Automation for SMBs

Opportunity Score:
84 → 92

Reason:
Demand increased 18%
Competitive gap increased
Customer pain frequency increased

Impact:
HIGH

Action:
Review validation plan
```

---

## FR-033 — Opportunity Recommendations by Department

The system shall generate department-specific recommendations.

### Product

```text
Build feature
Improve product
Launch MVP
```

### Marketing

```text
Target segment
Create campaign
Change messaging
```

### SEO

```text
Target keywords
Create content
Build topic cluster
```

### Sales

```text
Target accounts
Create sales play
Prioritize segment
```

### Finance

```text
Evaluate economics
Model pricing
Estimate investment
```

---

## FR-034 — Executive Opportunity Summary

The system shall provide:

```text
Top Opportunity
Opportunity Score
Market Potential
Customer Demand
Competitive Pressure
Required Investment
Risk
Recommended Action
Confidence
```

---

## FR-035 — Opportunity Comparison

Users shall be able to compare multiple opportunities using the same scoring framework.

---

## FR-036 — Opportunity History

The system shall provide:

```text
Initial Score
Score Changes
Evidence Changes
Confidence Changes
Human Decisions
Status Changes
Recommendation Changes
```

---

## FR-037 — Opportunity Expiration

Opportunities shall support expiration dates.

When evidence becomes stale, the system shall mark the opportunity:

```text
STALE
```

or:

```text
REVALIDATION_REQUIRED
```

---

## FR-038 — Revalidation

The AI engine shall periodically revalidate important opportunities.

---

## FR-039 — Opportunity Merging

Authorized users shall be able to merge duplicate opportunities.

The system shall preserve the provenance of merged records.

---

## FR-040 — Opportunity Splitting

A broad opportunity may be split into:

```text
Product Opportunity
+
Marketing Opportunity
+
SEO Opportunity
+
Sales Opportunity
```

---

## FR-041 — Opportunity Dependencies

The system shall support dependencies.

Example:

```text
Market Opportunity
      ↓
Product Opportunity
      ↓
Marketing Opportunity
      ↓
Sales Opportunity
```

---

## FR-042 — Opportunity-to-Roadmap Integration

Validated product opportunities shall be exportable to:

```text
Product Roadmap
Product Launch Intelligence
Product Management
```

---

## FR-043 — Opportunity-to-Campaign Integration

Marketing opportunities shall be exportable to:

```text
Campaign Management
Marketing Platform
AI Digital Marketing Platform
```

---

## FR-044 — Opportunity-to-SEO Integration

SEO opportunities shall be exportable to:

```text
SEO Platform
Keyword Intelligence
Technical SEO
SEO Analytics
```

---

## FR-045 — Opportunity-to-Sales Integration

Sales opportunities shall integrate with:

```text
Lead Generation
Lead Intelligence
Lead Scoring
CRM
Sales Pipeline
Sales Automation
```

---

## FR-046 — Opportunity-to-GTM Integration

Validated opportunities shall be available to:

```text
Product Positioning
Go-To-Market Strategy
Marketing Strategy
Sales Strategy
Pricing Strategy
```

---

## 13. AI Reasoning and Governance Requirements

## AI-001 — Evidence-First Reasoning

The AI shall prioritize evidence-backed conclusions.

---

## AI-002 — Uncertainty Representation

The AI shall explicitly represent uncertainty.

Example:

```json
{
  "opportunity": "Enterprise AI workflow automation",
  "confidence": 0.81,
  "confidence_label": "HIGH",
  "evidence_quality": "STRONG",
  "status": "REQUIRES_HUMAN_VALIDATION"
}
```

---

## AI-003 — Source Attribution

Every material AI conclusion shall reference its source evidence.

---

## AI-004 — Contradiction Detection

The AI shall identify conflicting evidence instead of silently selecting one source.

---

## AI-005 — Model Agreement

The platform may use multiple AI models to improve robustness.

Example:

```text
Gemini
+
Mistral
+
Groq-hosted model
```

Model disagreement shall be surfaced when material.

---

## AI-006 — Prompt Injection Defense

External market content shall be treated as untrusted data.

The system shall prevent external content from:

* Modifying system instructions
* Accessing tools
* Accessing tenant data
* Changing permissions
* Executing arbitrary actions

---

## AI-007 — Recommendation Guardrails

AI recommendations shall not automatically:

* Spend money
* Launch campaigns
* Change pricing
* Modify products
* Contact external parties

unless an authorized workflow explicitly permits the action.

---

## 14. Security Requirements

## SEC-001 — Authentication

All APIs shall require authenticated access.

---

## SEC-002 — Authorization

Authorization shall evaluate:

```text
Identity
+
Role
+
Tenant
+
Organization
+
Workspace
+
Resource
+
Action
+
Context
```

---

## SEC-003 — Multi-Tenant Isolation

Opportunity intelligence shall be isolated across:

```text
API
Database
Cache
Search
Vector Store
Object Storage
Events
Logs
```

---

## SEC-004 — Least Privilege

Users shall access only the opportunity information required by their role.

---

## SEC-005 — Sensitive Opportunity Data

The system shall protect:

* Internal strategy
* Unreleased product opportunities
* Pricing opportunities
* Revenue assumptions
* Customer intelligence
* Sales intelligence
* Strategic recommendations

---

## SEC-006 — Export Security

Exports shall enforce:

* RBAC
* ABAC
* Tenant isolation
* Data classification
* Audit logging

---

## SEC-007 — Data Encryption

Sensitive data shall be encrypted:

```text
In Transit
At Rest
```

---

## 15. Human-in-the-Loop Risk Engine

```text
LOW RISK
→ AI can analyze automatically

MEDIUM RISK
→ AI analysis + optional review

HIGH RISK
→ Human approval required

CRITICAL
→ Multi-person approval required
```

Critical opportunities may include:

* Major investment recommendations
* Major pricing changes
* Major market expansion
* High-value product launches
* External strategic claims

---

## 16. Event-Driven Requirements

The service shall publish:

```text
MarketSignalDetected
DemandSignalDetected
MarketTrendDetected
MarketGapDetected
CustomerPainDetected
OpportunityDiscovered
OpportunityAnalyzing
OpportunityScored
OpportunityValidated
OpportunityRejected
OpportunityApproved
OpportunityChanged
OpportunityScoreChanged
OpportunityExpired
OpportunityRevalidationRequired
OpportunityAlertCreated
OpportunityExperimentCreated
OpportunityExperimentCompleted
HumanReviewRequired
HumanReviewCompleted
OpportunityRecommendationGenerated
```

---

## 17. Event Example

```json
{
  "event_type": "MarketOpportunityDetected",
  "event_id": "evt_001",
  "tenant_id": "tenant_001",
  "opportunity_id": "OPP-001",
  "type": "PRODUCT",
  "score": 88,
  "confidence": 0.84,
  "priority": "P1",
  "verification_status": "REQUIRES_REVIEW",
  "detected_at": "2026-08-23T00:00:00Z"
}
```

---

## 18. Observability Requirements

The system shall monitor:

```text
Opportunity Detection Latency
AI Latency
Evidence Processing Rate
Opportunity Precision
Opportunity Recall
False Positive Rate
False Negative Rate
Human Review Rate
Human Rejection Rate
Recommendation Acceptance Rate
Provider Availability
API Latency
Queue Latency
Alert Latency
Data Freshness
```

---

## 19. AI Quality Metrics

The system shall measure:

```text
Opportunity Detection Precision
Opportunity Detection Recall
Evidence Grounding Rate
Hallucination Rate
Human Override Rate
False Opportunity Rate
Confidence Calibration
Recommendation Acceptance
Model Agreement
```

---

## 20. Scalability Requirements

The system shall support:

```text
Millions of market signals
Millions of evidence records
Thousands of opportunities
Large historical datasets
Continuous market monitoring
Thousands of concurrent AI jobs
Multi-tenant workloads
Horizontal scaling
```

---

## 21. Reliability Requirements

The system shall support:

* Retry
* Circuit breaker
* Dead-letter queues
* Idempotency
* Event replay
* Job recovery
* Provider failover
* Graceful degradation
* Partial failure recovery

---

## 22. Data Retention

The system shall support configurable retention for:

```text
Market Signals
Evidence
Opportunity Assessments
Opportunity Scores
Forecasts
Recommendations
Human Reviews
Experiments
Alerts
Audit Logs
```

Historical opportunity assessments shall remain immutable.

---

## 23. Integration Requirements

The module shall integrate with:

```text
Product Vision
Product Scope
Product Roadmap
Product Launch Intelligence
Market Analysis Engine
Market Trend Analysis
Competitor Analysis
Competitor Product Analysis
Competitor Pricing Analysis
Competitor Strength/Weakness
Product Positioning
Go-To-Market Strategy
Marketing Platform
AI Digital Marketing Platform
Campaign Management
Marketing Analytics
SEO Platform
Keyword Intelligence
Technical SEO
SEO Analytics
Lead Generation
Lead Intelligence
Lead Scoring
CRM
Sales Pipeline
Sales Automation
Business Analyst
Finance Manager
AI Agent Builder
Workflow Automation
```

---

## 24. Cross-Module Opportunity Pipeline

```text
Market Signals
        ↓
Market Trend Analysis
        ↓
Competitor Analysis
        ↓
Competitor Strength/Weakness
        ↓
Customer Pain Analysis
        ↓
Market Gap Detection
        ↓
Market Opportunity Detection
        ↓
Opportunity Scoring
        ↓
Product Positioning
        ↓
Product Roadmap
        ↓
Product Launch Intelligence
        ↓
Go-To-Market Strategy
        ↓
Marketing Campaigns
        ↓
SEO Strategy
        ↓
Lead Generation
        ↓
CRM
        ↓
Sales Pipeline
        ↓
Sales Automation
        ↓
Revenue Monitoring
        ↓
Feedback Loop
        ↓
Opportunity Reassessment
```

---

## 25. Opportunity Dashboard

## Executive Overview

The dashboard shall display:

* Total opportunities
* New opportunities
* High-priority opportunities
* Validated opportunities
* Opportunities in execution
* Expiring opportunities
* Opportunity score changes
* Market growth indicators

## Opportunity Categories

```text
Product
Marketing
SEO
Sales
Pricing
Geographic
Industry
Technology
Partnership
New Market
```

## Opportunity Health

```text
High Potential
Medium Potential
Low Potential
High Risk
Stale
Requires Validation
```

---

## 26. Opportunity Heatmap

| Opportunity | Market Potential | Demand | Competition | Strategic Fit | Execution Difficulty | Score |
| ----------- | ---------------: | -----: | ----------: | ------------: | -------------------: | ----: |
| A           |               92 |     89 |          55 |            91 |                   42 |    88 |
| B           |               81 |     94 |          78 |            85 |                   60 |    79 |
| C           |               76 |     72 |          40 |            89 |                   35 |    82 |

All scores shall be generated from configurable scoring logic.

---

## 27. Opportunity Portfolio

The system shall classify opportunities into:

```text
High Value / Low Risk
High Value / High Risk
Low Value / Low Risk
Low Value / High Risk
```

This shall help management balance:

```text
Quick Wins
Strategic Bets
Long-Term Investments
Low-Priority Experiments
```

---

## 28. Example AI Opportunity

```json
{
  "opportunity_id": "OPP-001",
  "title": "AI Sales Automation for SMBs",
  "type": "PRODUCT",
  "market": "B2B SaaS",
  "segment": "SMB",
  "signals": [
    "Growing AI adoption",
    "Increasing demand for sales automation",
    "Recurring complaints about manual qualification",
    "Competitor enterprise pricing"
  ],
  "market_potential_score": 89,
  "demand_score": 92,
  "competitive_gap_score": 84,
  "strategic_fit_score": 91,
  "execution_difficulty_score": 48,
  "risk_score": 34,
  "overall_score": 88,
  "confidence": 0.84,
  "priority": "P1",
  "status": "REQUIRES_HUMAN_VALIDATION"
}
```

---

## 29. Example Human Review

```json
{
  "opportunity_id": "OPP-001",
  "ai_score": 88,
  "human_score": 81,
  "ai_priority": "P1",
  "human_priority": "P1",
  "decision": "APPROVED_WITH_MODIFICATION",
  "reviewer_id": "USER-001",
  "reason": "Market demand is strong, but the addressable segment estimate requires additional validation."
}
```

---

## 30. Opportunity Validation Framework

The system shall support:

## Problem Validation

```text
Does the customer problem exist?
How frequently does it occur?
How severe is it?
```

## Demand Validation

```text
Are customers actively searching?
Are customers requesting solutions?
Are customers willing to pay?
```

## Competitive Validation

```text
Who already solves the problem?
How well do they solve it?
Where are their gaps?
```

## Economic Validation

```text
Can the opportunity produce viable economics?
What is estimated acquisition cost?
What is estimated customer value?
```

## Execution Validation

```text
Can the organization build and deliver the solution?
```

---

## 31. Opportunity Decision Framework

The system shall support:

```text
PURSUE
        ↓
VALIDATE
        ↓
BUILD
        ↓
LAUNCH
        ↓
SCALE
```

or:

```text
MONITOR
        ↓
REVALIDATE
```

or:

```text
REJECT
        ↓
ARCHIVE
```

---

## 32. Testing Requirements

## Unit Tests

Test:

* Signal extraction
* Demand scoring
* Opportunity scoring
* Confidence calculation
* Market gap detection
* Opportunity ranking
* Risk scoring
* Timing estimation

## Integration Tests

Test:

* AI Gateway
* Database
* Redis
* Search
* Vector database
* Event bus
* Notification service

## Security Tests

Test:

* Tenant isolation
* RBAC
* ABAC
* Unauthorized access
* Data leakage
* Export restrictions
* Prompt injection
* Tool abuse

## AI Tests

Test:

* Hallucination
* Evidence grounding
* Opportunity classification
* Confidence calibration
* False positives
* False negatives
* Contradictory evidence
* Model disagreement

## End-to-End Test

```text
Market Signal
→ Evidence
→ AI Analysis
→ Opportunity
→ Score
→ Human Review
→ Validation
→ Recommendation
→ Execution
→ Monitoring
→ Revalidation
```

---

## 33. Performance Requirements

The system shall:

* Return cached opportunity summaries with low latency.
* Process long analyses asynchronously.
* Support batch analysis.
* Parallelize independent AI analysis tasks.
* Provide analysis progress.
* Avoid blocking interactive requests.

---

## 34. API Requirements

The module shall expose APIs such as:

```text
POST   /api/v1/market-opportunities
GET    /api/v1/market-opportunities

GET    /api/v1/market-opportunities/{id}

POST   /api/v1/market-opportunities/discover
POST   /api/v1/market-opportunities/analyze

GET    /api/v1/market-opportunities/signals
GET    /api/v1/market-opportunities/trends
GET    /api/v1/market-opportunities/gaps

GET    /api/v1/market-opportunities/scores
GET    /api/v1/market-opportunities/rankings

GET    /api/v1/market-opportunities/opportunities
GET    /api/v1/market-opportunities/threats

POST   /api/v1/market-opportunities/{id}/validate
POST   /api/v1/market-opportunities/{id}/approve
POST   /api/v1/market-opportunities/{id}/reject

POST   /api/v1/market-opportunities/{id}/experiments

GET    /api/v1/market-opportunities/{id}/history
GET    /api/v1/market-opportunities/alerts
```

---

## 35. API Security

Every API shall enforce:

```text
Authentication
Authorization
Tenant Validation
Input Validation
Schema Validation
Rate Limiting
Audit Logging
Request Tracing
Idempotency
```

---

## 36. Opportunity Intelligence Quality Gates

Before an opportunity becomes `VALIDATED`, the system shall verify:

```text
✓ Evidence Exists
✓ Evidence Is Relevant
✓ Evidence Is Recent Enough
✓ Demand Signal Exists
✓ Competitive Context Exists
✓ Opportunity Logic Is Explainable
✓ Confidence Is Calculated
✓ Assumptions Are Explicit
✓ Risks Are Identified
✓ Human Review Completed When Required
```

---

## 37. Humanized Decision Support

The system shall allow human experts to contribute knowledge unavailable in public datasets, including:

```text
Customer conversations
Sales objections
Win/loss insights
Internal product knowledge
Internal pricing knowledge
Partner feedback
Strategic priorities
Operational constraints
```

Such information shall be explicitly marked as:

```text
INTERNAL_BUSINESS_INTELLIGENCE
```

and protected using tenant-level authorization.

---

## 38. AI + Human Conflict Resolution

If AI and human assessments disagree:

```text
AI Assessment
      ↓
Human Review
      ↓
Evidence Comparison
      ↓
Human Decision
```

The system shall preserve both assessments.

Human approval shall not erase the AI reasoning history.

---

## 39. Opportunity Audit Trail

Every material change shall record:

```text
Who
What
When
Why
Previous Value
New Value
Evidence
AI/Human Origin
Approval Status
```

---

## 40. Business Intelligence Feedback Loop

The system shall learn from:

```text
Opportunity Detected
        ↓
Opportunity Validated
        ↓
Opportunity Executed
        ↓
Actual Results
        ↓
Revenue
        ↓
Customer Acquisition
        ↓
Conversion
        ↓
Retention
        ↓
Outcome
        ↓
Opportunity Model Evaluation
```

This feedback shall be used to evaluate the accuracy of opportunity detection models.

---

## 41. Opportunity Model Evaluation

The platform shall measure:

```text
Predicted Opportunity
vs
Actual Market Outcome
```

Metrics may include:

* Revenue generated
* Customer acquisition
* Conversion rate
* Retention
* Market adoption
* Experiment success
* Forecast error
* Opportunity precision
* Opportunity recall

---

## 42. Continuous Learning

The system may use historical outcomes to improve:

* Opportunity scoring
* Signal weighting
* Confidence estimation
* Market segmentation
* Recommendation quality

Model updates shall be versioned and auditable.

---

## 43. Model Governance

Each AI model used for opportunity detection shall have:

```text
Model ID
Provider
Model Version
Prompt Version
Scoring Version
Evaluation Metrics
Deployment Date
Retirement Date
Known Limitations
```

---

## 44. Fail-Safe Behavior

If:

```text
AI provider unavailable
OR
Market data unavailable
OR
Evidence quality insufficient
OR
Scoring model unavailable
```

the system shall:

```text
Fail Gracefully
+
Preserve Existing Intelligence
+
Mark Analysis Incomplete
+
Notify Appropriate Users
+
Avoid Fabricating Results
```

---

## 45. Acceptance Criteria

The module shall be considered production-ready when:

* Market signals can be collected.
* Signals can be validated.
* Demand can be analyzed.
* Customer pain can be identified.
* Market gaps can be detected.
* Competitor gaps can be detected.
* Emerging trends can be connected to opportunities.
* Product opportunities can be detected.
* Marketing opportunities can be detected.
* SEO opportunities can be detected.
* Sales opportunities can be detected.
* Pricing opportunities can be detected.
* Geographic opportunities can be detected.
* Industry opportunities can be detected.
* Technology opportunities can be detected.
* Partnership opportunities can be detected.
* Opportunities can be scored.
* Opportunities can be ranked.
* Confidence can be calculated.
* Evidence provenance is maintained.
* Historical assessments are preserved.
* Human experts can validate AI findings.
* Human overrides are fully audited.
* High-risk opportunities require appropriate human approval.
* Opportunities can be converted into validation experiments.
* Opportunities can be connected to product roadmaps.
* Opportunities can be connected to campaigns.
* Opportunities can be connected to SEO workflows.
* Opportunities can be connected to sales workflows.
* Opportunities can be connected to GTM strategy.
* Opportunity changes can trigger alerts.
* Stale opportunities can be revalidated.
* AI hallucination controls are implemented.
* Prompt injection defenses are implemented.
* RBAC is enforced.
* ABAC is enforced.
* Multi-tenant isolation is enforced.
* APIs are secured.
* Events are emitted correctly.
* AI provider failover works.
* The service scales horizontally.
* All important decisions are explainable and auditable.

---

## 46. FAANG-Level Engineering Principles

The implementation shall follow:

1. Evidence Before Assertion
2. AI-Assisted, Human-Governed Decision Making
3. Explicit Uncertainty
4. Source Provenance
5. Continuous Revalidation
6. Multi-Tenant Isolation
7. Zero-Trust Security
8. Least-Privilege Access
9. Immutable Historical Intelligence
10. Explainable Opportunity Scoring
11. Configurable Business Models
12. Event-Driven Architecture
13. Provider-Agnostic AI
14. Horizontal Scalability
15. Fault-Tolerant Processing
16. Human Approval for High-Impact Decisions
17. AI Output Validation
18. Prompt-Injection Resistance
19. Continuous Model Evaluation
20. Outcome-Based Learning
21. Separation of Evidence and Interpretation
22. Separation of Recommendation and Execution
23. Fail-Safe Automation
24. Observability by Default
25. Auditability by Default

---

## 47. Definition of Done

`market_opportunity_detection.md` shall be considered complete when SalesGenie can transform:

```text
Market Signals
+
Customer Demand
+
Customer Pain
+
Competitor Intelligence
+
Market Trends
+
Product Intelligence
+
Pricing Intelligence
+
SEO Intelligence
+
Sales Intelligence
+
Geographic Intelligence
+
Industry Intelligence
```

into:

```text
Market Gaps
        +
Opportunity Hypotheses
        +
Opportunity Scores
        +
Opportunity Confidence
        +
Opportunity Rankings
        +
Validation Plans
        +
Human-Validated Opportunities
        +
Strategic Recommendations
        +
Execution Plans
        +
Continuous Opportunity Monitoring
```

and connect validated opportunities to:

```text
Product Management
        ↓
Product Roadmap
        ↓
Product Launch Intelligence
        ↓
Product Positioning
        ↓
Go-To-Market Strategy
        ↓
Marketing Platform
        ↓
Campaign Management
        ↓
SEO Platform
        ↓
Lead Generation
        ↓
Lead Intelligence
        ↓
Lead Scoring
        ↓
CRM
        ↓
Sales Pipeline
        ↓
Sales Automation
        ↓
Finance
        ↓
Business Analytics
        ↓
Actual Business Outcomes
        ↓
Opportunity Intelligence Feedback Loop
```

while maintaining:

```text
Security
+
Privacy
+
Tenant Isolation
+
RBAC
+
ABAC
+
Evidence Provenance
+
AI Governance
+
Human Oversight
+
Auditability
+
Reliability
+
Scalability
+
Explainability
+
Continuous Learning
```
