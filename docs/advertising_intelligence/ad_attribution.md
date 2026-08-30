# SalesGenie — AI-Based Advertising Attribution Intelligence

## User Requirements, System Requirements & Functional Requirements

> **Document:** `ai_ad_attribution.md`
>
> **Platform:** SalesGenie Enterprise AI Customer Support, Sales & Marketing Platform
>
> **Capability:** AI-Powered Advertising Attribution & Incrementality Intelligence
>
> **Mode:** AI-Based
>
> **Objective:** Build an enterprise-grade AI attribution system that determines how advertising touchpoints contribute to leads, qualified leads, opportunities, conversions, revenue, profit, customer lifetime value, and business growth across the complete customer journey.

---

## 1. Product Overview

SalesGenie's AI Advertising Attribution module shall provide a unified attribution intelligence layer across:

```text
Ad Impression
    ↓
Ad Click
    ↓
Landing Page
    ↓
Website Interaction
    ↓
Content Engagement
    ↓
Lead
    ↓
Qualified Lead
    ↓
Sales Interaction
    ↓
Opportunity
    ↓
Conversion
    ↓
Purchase
    ↓
Revenue
    ↓
Repeat Purchase
    ↓
Customer Lifetime Value
```

The system shall determine:

* Which channels influenced conversions.
* Which campaigns influenced revenue.
* Which ads influenced customers.
* Which touchpoints assisted conversions.
* Which audiences contributed to revenue.
* Which products were influenced by advertising.
* Which channels generate high-quality customers.
* Which advertising activities generate incremental business outcomes.
* How advertising credit should be distributed across touchpoints.
* How attribution uncertainty affects business decisions.
* How advertising budget should be optimized based on attribution intelligence.

---

## 2. Business Objectives

## BO-001 — Unified Attribution

The system shall unify advertising attribution data across:

* Google Ads
* Facebook Ads
* Instagram Ads
* LinkedIn Ads
* TikTok Ads
* YouTube Ads
* WhatsApp
* Email
* Organic Search
* Organic Social
* Referral
* Direct
* Sales activities
* CRM interactions
* Website interactions

---

## BO-002 — Customer Journey Reconstruction

The AI shall reconstruct customer journeys from the first identifiable marketing interaction through conversion and post-conversion activity.

---

## BO-003 — Multi-Touch Attribution

The platform shall assign contribution across multiple customer touchpoints rather than relying exclusively on last-click attribution.

---

## BO-004 — Revenue Attribution

The system shall connect marketing touchpoints to:

* Revenue
* Gross profit
* Contribution profit
* Subscription revenue
* Repeat revenue
* Customer lifetime value

---

## BO-005 — Conversion Attribution

The system shall attribute:

* Leads
* Qualified leads
* Opportunities
* Purchases
* Subscriptions
* Renewals
* Other configured conversion events

---

## BO-006 — Incrementality Intelligence

The AI shall distinguish between:

```text
Attributed Conversion
vs.
Incremental Conversion
```

where sufficient experimental or observational data exists.

---

## BO-007 — Attribution-Based Budget Optimization

The system shall use attribution intelligence to recommend advertising budget allocation.

---

## BO-008 — Attribution Transparency

Every attribution result shall expose:

* Attribution methodology
* Contributing touchpoints
* Evidence
* Data quality
* Confidence
* Attribution uncertainty
* Model version
* Time window

---

## 3. User Roles

## 3.1 Super Admin

The Super Admin shall be able to:

* Configure platform-wide attribution policies.
* Configure supported attribution models.
* Configure tenant-level attribution capabilities.
* Monitor attribution service health.
* Review audit logs.
* Configure data retention.
* Configure AI policies.

---

## 3.2 Organization Admin

The Organization Admin shall be able to:

* Configure attribution settings.
* Connect marketing platforms.
* Configure CRM integrations.
* Configure conversion events.
* Configure attribution windows.
* Configure business rules.
* Configure AI attribution models.

---

## 3.3 Marketing Manager

The Marketing Manager shall be able to:

* Analyze channel attribution.
* Analyze campaign attribution.
* Analyze ad attribution.
* Analyze product attribution.
* Analyze revenue attribution.
* Compare attribution models.
* Review AI attribution recommendations.

---

## 3.4 Marketing Analyst

The Marketing Analyst shall be able to:

* Build attribution reports.
* Analyze customer journeys.
* Compare attribution models.
* Investigate attribution discrepancies.
* Analyze touchpoint contribution.
* Analyze attribution confidence.

---

## 3.5 Advertising Specialist

The Advertising Specialist shall be able to:

* Analyze ad-level contribution.
* Analyze campaign contribution.
* Identify high-value touchpoints.
* Detect inefficient touchpoints.
* Review attribution-driven optimization recommendations.

---

## 3.6 Sales Manager

The Sales Manager shall be able to:

* Analyze marketing influence on opportunities.
* Analyze lead-source attribution.
* Analyze sales-assisted attribution.
* Analyze marketing-to-sales conversion paths.

---

## 3.7 Finance Manager

The Finance Manager shall be able to:

* Analyze attributed revenue.
* Analyze attributed profit.
* Analyze CAC.
* Analyze LTV:CAC.
* Analyze attributed ROAS.
* Compare marketing spend against attributed business value.

---

## 3.8 Executive

Executives shall be able to view:

* Marketing contribution to revenue.
* Marketing contribution to profit.
* Channel contribution.
* Campaign contribution.
* Customer acquisition contribution.
* Incremental revenue.
* Attribution confidence.
* Strategic marketing recommendations.

---

## 4. User Requirements

## UR-001 — Attribution Configuration

Users shall be able to configure:

* Attribution model
* Attribution window
* Conversion events
* Revenue events
* Customer journey stages
* Lookback period
* Data sources
* Business rules

---

## UR-002 — Attribution Models

The platform shall support:

```text
First Touch
Last Touch
Linear
Time Decay
Position Based
U-Shaped
W-Shaped
Data-Driven
Algorithmic
Markov Chain
Shapley Value
Custom
```

---

## UR-003 — Multi-Touch Customer Journey

Users shall be able to inspect individual customer journeys.

Example:

```text
Google Ad
   ↓
Website Visit
   ↓
Facebook Retargeting
   ↓
Email
   ↓
Sales Call
   ↓
Purchase
```

---

## UR-004 — Channel Attribution

Users shall be able to determine the contribution of:

* Paid Search
* Paid Social
* Display
* Video
* Email
* Organic Search
* Organic Social
* Referral
* Direct
* Affiliate
* Sales
* Other configured channels

---

## UR-005 — Campaign Attribution

Users shall be able to determine how campaigns contribute to:

* Leads
* Qualified leads
* Opportunities
* Customers
* Revenue
* Profit
* LTV

---

## UR-006 — Ad-Level Attribution

Users shall be able to determine which individual advertisements contributed to business outcomes.

---

## UR-007 — Creative Attribution

The system shall attribute conversion and revenue contribution to creative assets where identifiable.

---

## UR-008 — Product Attribution

The system shall determine which advertising touchpoints contribute to specific products.

---

## UR-009 — Audience Attribution

The system shall determine which audiences contribute to:

* Leads
* Customers
* Revenue
* Profit
* LTV

---

## UR-010 — Geographic Attribution

Users shall be able to analyze attribution by:

* Country
* Region
* City
* Market
* Territory

---

## UR-011 — Demographic Attribution

Where legally and technically appropriate, the system shall analyze attribution by:

* Age group
* Gender
* Language
* Other configured demographic dimensions

---

## UR-012 — Device Attribution

The system shall support:

* Desktop
* Mobile
* Tablet
* Other supported device classes

---

## UR-013 — Conversion Attribution

Users shall be able to configure and analyze attribution for:

* Form submissions
* Demo requests
* Calls
* Purchases
* Subscriptions
* Downloads
* Signups
* Renewals
* Custom conversions

---

## UR-014 — Revenue Attribution

The system shall calculate attributed revenue at:

```text
Channel
Campaign
Ad Set
Ad
Creative
Audience
Product
Customer
```

levels.

---

## UR-015 — Profit Attribution

Where cost data is available, the system shall calculate attributed:

* Gross profit
* Contribution profit
* Profit margin

---

## UR-016 — Customer Lifetime Value Attribution

The AI shall connect acquisition touchpoints with downstream customer value.

---

## UR-017 — Assisted Conversion Analysis

The system shall identify touchpoints that:

* Initiated journeys
* Assisted journeys
* Influenced consideration
* Accelerated conversion
* Closed conversions

---

## UR-018 — Attribution Path Analysis

Users shall be able to identify common paths such as:

```text
Google → Website → Email → Purchase
```

and:

```text
Instagram → Retargeting → WhatsApp → Sales Agent → Purchase
```

---

## UR-019 — Top Attribution Paths

The platform shall rank customer journeys by:

* Conversion volume
* Revenue
* Profit
* LTV
* Conversion rate
* Journey duration

---

## UR-020 — Attribution Comparison

Users shall be able to compare multiple attribution models simultaneously.

Example:

```text
Campaign X

First Touch Revenue: $100K
Last Touch Revenue: $72K
Linear Revenue: $84K
Data-Driven Revenue: $91K
```

---

## UR-021 — Attribution Discrepancy Detection

The AI shall detect significant differences between attribution models.

---

## UR-022 — Attribution Confidence

Every attribution result shall contain a confidence score based on:

* Tracking quality
* Identity resolution
* Event completeness
* Sample size
* Attribution model stability
* Cross-device coverage

---

## UR-023 — Identity Resolution

The system shall connect customer interactions across:

* Anonymous sessions
* Cookies
* User IDs
* CRM IDs
* Email
* Phone
* Device identifiers
* Authenticated sessions
* Advertising identifiers

subject to applicable privacy and platform constraints.

---

## UR-024 — Cross-Device Attribution

Where sufficient deterministic or probabilistic signals exist, the system shall connect journeys across devices.

---

## UR-025 — Cross-Channel Attribution

The system shall connect touchpoints across multiple marketing channels.

---

## UR-026 — Offline Conversion Attribution

The system shall support offline events such as:

* Phone sales
* Physical store purchases
* Sales-agent conversions
* CRM opportunities
* Offline contracts

---

## UR-027 — Delayed Conversion Attribution

The system shall support long consideration cycles where conversion occurs days or months after initial advertising exposure.

---

## UR-028 — Subscription Attribution

The system shall attribute:

* Trial signup
* Subscription
* Renewal
* Expansion
* Downgrade
* Churn

to marketing touchpoints where supported.

---

## UR-029 — AI Attribution Explanation

Users shall be able to ask:

```text
Why did this campaign receive 38% of the conversion credit?

Which touchpoint influenced this customer the most?

Why does last-click attribution overvalue this campaign?

Which channel creates the highest-value customers?

Which campaign generates incremental revenue?

Which advertising channel should receive more budget?
```

---

## UR-030 — AI Attribution Recommendations

The AI shall recommend:

* Attribution model changes
* Budget allocation changes
* Tracking improvements
* Campaign optimization
* Audience changes
* Channel strategy changes

---

## 5. System Requirements

## SR-001 — Multi-Tenant Attribution Architecture

Attribution data shall be isolated using:

```text
tenant_id
organization_id
workspace_id
customer_id
advertising_account_id
```

---

## SR-002 — Event Ingestion

The system shall ingest:

```text
Impression Events
Click Events
View Events
Website Events
Content Events
Lead Events
CRM Events
Sales Events
Conversion Events
Purchase Events
Revenue Events
Subscription Events
```

---

## SR-003 — Event Schema

Each attribution event shall support:

```text
event_id
tenant_id
anonymous_id
customer_id
session_id
timestamp
event_type
channel
source
medium
campaign_id
ad_set_id
ad_id
creative_id
product_id
conversion_id
revenue
currency
device
geography
metadata
```

---

## SR-004 — Event Ordering

The system shall maintain temporal ordering of customer events.

---

## SR-005 — Event Deduplication

The system shall detect and prevent duplicate attribution events.

---

## SR-006 — Event Identity Resolution

The platform shall maintain an identity graph connecting:

```text
Anonymous Identity
      ↓
Session Identity
      ↓
Known User
      ↓
CRM Contact
      ↓
Customer
```

---

## SR-007 — Identity Graph

The identity graph shall support deterministic and, where permitted, probabilistic identity resolution.

---

## SR-008 — Attribution Data Warehouse

The system shall maintain analytical datasets for:

* Touchpoints
* Journeys
* Conversions
* Revenue
* Attribution weights
* Attribution models
* Attribution results

---

## SR-009 — Attribution Engine

The attribution engine shall calculate contribution for every eligible touchpoint.

---

## SR-010 — Attribution Window

The system shall support configurable windows such as:

```text
1 Day
7 Days
14 Days
30 Days
60 Days
90 Days
180 Days
Custom
```

---

## SR-011 — First-Touch Attribution

The first eligible touchpoint shall receive conversion credit.

---

## SR-012 — Last-Touch Attribution

The final eligible touchpoint before conversion shall receive conversion credit.

---

## SR-013 — Linear Attribution

Conversion credit shall be distributed across eligible touchpoints.

---

## SR-014 — Time-Decay Attribution

More recent touchpoints shall receive greater weight.

---

## SR-015 — Position-Based Attribution

The system shall support configurable weighted positions.

---

## SR-016 — Data-Driven Attribution

The AI shall estimate touchpoint contribution from observed historical data.

---

## SR-017 — Algorithmic Attribution

The platform shall support machine-learning-based attribution models.

Potential techniques shall include:

```text
Logistic Regression
Gradient Boosting
Markov Chains
Shapley Value Estimation
Causal Models
Survival Models
Sequence Models
Deep Learning
```

---

## SR-018 — Incrementality Engine

The system shall support:

* Holdout analysis
* Geo experiments
* Campaign experiments
* Conversion lift
* Incremental revenue
* Incremental conversions

where appropriate data exists.

---

## SR-019 — Attribution Weight Normalization

For each conversion:

```text
Σ Attribution Weight = 1
```

unless the selected methodology explicitly specifies another normalization convention.

---

## SR-020 — Revenue Attribution

The system shall distribute eligible revenue according to attribution weights.

---

## SR-021 — Profit Attribution

The system shall calculate profit contribution using configured financial data.

---

## SR-022 — Attribution Confidence Engine

The system shall calculate confidence using:

```text
Tracking Completeness
+
Identity Resolution Quality
+
Sample Size
+
Model Stability
+
Data Freshness
+
Attribution Consistency
```

---

## SR-023 — Model Versioning

Every attribution result shall retain:

```text
Model ID
Model Version
Feature Version
Training Dataset Version
Attribution Window
Model Configuration
Inference Timestamp
```

---

## SR-024 — Attribution Reproducibility

Historical attribution results shall be reproducible using versioned inputs and model configurations.

---

## SR-025 — Attribution Data Freshness

The system shall expose:

* Last event received
* Last synchronization
* Data latency
* Missing data
* Provider health

---

## SR-026 — Privacy Controls

The platform shall support:

* Consent-aware tracking
* Data minimization
* Identity access controls
* Data deletion
* Data retention
* Tenant isolation
* Encryption

---

## SR-027 — Attribution Access Control

Permissions shall include:

```text
attribution.read
attribution.analytics
attribution.models.read
attribution.models.configure
attribution.recommendations.read
attribution.export
attribution.admin
```

---

## SR-028 — Audit Logging

The system shall log:

* Attribution model changes
* Attribution window changes
* Tracking configuration changes
* Data source changes
* AI recommendations
* Model deployments
* Attribution recalculations
* Exports

---

## 6. Functional Requirements

## FR-001 — Marketing Event Collection

The system shall:

1. Connect to supported marketing sources.
2. Collect attribution events.
3. Validate events.
4. Normalize events.
5. Deduplicate events.
6. Resolve identities.
7. Store canonical events.

---

## FR-002 — Customer Journey Construction

The system shall construct chronological journeys:

```text
Touchpoint 1
    ↓
Touchpoint 2
    ↓
Touchpoint 3
    ↓
Touchpoint N
    ↓
Conversion
```

---

## FR-003 — Attribution Model Selection

Users shall be able to select an attribution model for analysis.

---

## FR-004 — Attribution Model Comparison

The system shall calculate multiple models against the same dataset.

---

## FR-005 — Touchpoint Attribution

The system shall assign contribution weights to eligible touchpoints.

---

## FR-006 — Channel Attribution

The system shall aggregate touchpoint contribution by channel.

---

## FR-007 — Campaign Attribution

The system shall aggregate contribution by campaign.

---

## FR-008 — Ad Attribution

The system shall aggregate contribution by advertisement.

---

## FR-009 — Creative Attribution

The system shall aggregate contribution by creative.

---

## FR-010 — Product Attribution

The system shall aggregate contribution by product and SKU.

---

## FR-011 — Audience Attribution

The system shall aggregate contribution by audience.

---

## FR-012 — Customer Attribution

The system shall calculate marketing contribution at customer level.

---

## FR-013 — Revenue Attribution

The system shall calculate:

```text
Attributed Revenue =
Conversion Revenue × Attribution Weight
```

for each eligible touchpoint.

---

## FR-014 — Profit Attribution

The system shall calculate attributed profit from configured revenue and cost data.

---

## FR-015 — ROAS Attribution

The platform shall calculate:

```text
Attributed ROAS =
Attributed Revenue / Advertising Spend
```

and provide model context for the calculation.

---

## FR-016 — CAC Attribution

The system shall calculate acquisition cost based on attributed conversions.

---

## FR-017 — LTV Attribution

The system shall connect marketing touchpoints to downstream customer value.

---

## FR-018 — Assisted Conversion Analysis

The system shall distinguish:

```text
Initiating Touchpoint
Assisting Touchpoint
Converting Touchpoint
```

---

## FR-019 — Customer Journey Visualization

The UI shall display customer journeys chronologically.

Example:

```text
Google Search Ad
      ↓
Website
      ↓
Instagram Retargeting
      ↓
Email
      ↓
Sales Agent
      ↓
Purchase
```

---

## FR-020 — Attribution Path Analytics

The system shall identify common conversion paths.

---

## FR-021 — Path Ranking

Paths shall be ranked by:

* Conversion volume
* Revenue
* Profit
* Conversion rate
* LTV
* Average time to conversion

---

## FR-022 — Attribution Model Disagreement

The AI shall detect cases where attribution models produce materially different conclusions.

---

## FR-023 — Attribution Anomaly Detection

The system shall detect:

* Sudden attribution shifts
* Missing touchpoints
* Tracking failures
* Unexpected conversion concentration
* Abnormal channel contribution

---

## FR-024 — Attribution Data Quality Monitoring

The system shall detect:

```text
Missing Events
Duplicate Events
Broken Parameters
Unresolved Identities
Missing Campaign IDs
Missing Conversion IDs
Revenue Mismatches
Timestamp Errors
Currency Mismatches
```

---

## FR-025 — AI Root-Cause Analysis

The AI shall investigate attribution changes by analyzing:

```text
Channel
Campaign
Ad
Creative
Audience
Product
Device
Geography
Time
Conversion
Customer Segment
```

---

## FR-026 — AI Attribution Recommendation

The AI shall generate recommendations such as:

```text
Increase investment in Channel X.

Do not optimize exclusively for last-click conversions.

Campaign Y is receiving disproportionate last-touch credit.

Campaign Z consistently appears in high-LTV journeys.

Tracking for Campaign A appears incomplete.

Channel B produces high conversion volume but low customer value.
```

---

## FR-027 — AI Attribution Model Recommendation

The AI shall recommend an attribution model based on:

* Business model
* Customer journey length
* Data availability
* Conversion volume
* Sales cycle
* Subscription behavior
* Attribution stability

---

## FR-028 — Incrementality Analysis

The system shall estimate whether observed conversions are likely incremental rather than merely correlated with advertising exposure.

---

## FR-029 — Incremental Revenue Analysis

The platform shall estimate:

```text
Incremental Conversions
Incremental Revenue
Incremental Profit
Incremental ROAS
```

when experimental or sufficiently robust causal data is available.

---

## FR-030 — Attribution-Based Budget Optimization

The AI shall use attribution and incrementality signals to recommend:

```text
Channel Budget
Campaign Budget
Product Budget
Audience Budget
```

allocation.

---

## FR-031 — Scenario Simulation

Users shall be able to simulate:

```text
Increase Channel X Spend
Decrease Channel Y Spend
Pause Campaign Z
Increase Product X Budget
Shift Budget Between Channels
Change Attribution Model
```

---

## FR-032 — Attribution Forecasting

The AI shall forecast:

* Attributed conversions
* Attributed revenue
* Attributed profit
* CAC
* ROAS
* Incremental revenue

---

## FR-033 — Attribution-Based Product Analysis

The system shall identify which products receive the strongest advertising contribution.

---

## FR-034 — Attribution-Based Audience Analysis

The system shall identify which audiences generate the strongest attributed business outcomes.

---

## FR-035 — Attribution-Based Campaign Optimization

The AI shall recommend campaign changes based on attributed and incremental performance.

---

## FR-036 — Attribution-Based Creative Optimization

The AI shall identify creatives that influence high-value customer journeys.

---

## FR-037 — Attribution-Based Customer Quality Analysis

The system shall compare customers acquired through different marketing touchpoints using:

```text
Revenue
Profit
Retention
Repeat Purchase
LTV
Churn
```

---

## FR-038 — Natural-Language Attribution Query

Users shall be able to ask:

```text
Which channel generates the most revenue?

Which campaign receives the most conversion credit?

Which channel creates the highest-LTV customers?

Why does Facebook receive more last-click credit than first-touch credit?

Which campaigns assist conversions most frequently?

Which customer journey is most profitable?

What is our incremental ROAS?

Which channel should receive more budget?

Which campaigns are over-attributed?

Which marketing touchpoints are undervalued by last-click attribution?
```

---

## FR-039 — AI Query Planning

For each attribution query, the system shall:

1. Parse user intent.
2. Identify relevant attribution dimensions.
3. Identify conversion events.
4. Identify revenue events.
5. Determine time range.
6. Determine attribution model.
7. Validate user permissions.
8. Retrieve data.
9. Validate data quality.
10. Perform attribution analysis.
11. Generate grounded results.

---

## FR-040 — Attribution Explanation

Every AI-generated attribution conclusion shall provide:

```text
Conclusion
Evidence
Attribution Model
Data Period
Sample Size
Confidence
Uncertainty
Limitations
```

---

## FR-041 — Attribution Report Generation

The platform shall generate:

```text
Channel Attribution Report
Campaign Attribution Report
Ad Attribution Report
Product Attribution Report
Audience Attribution Report
Customer Journey Report
Revenue Attribution Report
Profit Attribution Report
Incrementality Report
Attribution Model Comparison Report
Attribution Data Quality Report
```

---

## FR-042 — Scheduled Attribution Reports

Users shall be able to schedule:

```text
Daily
Weekly
Monthly
Quarterly
Custom
```

attribution reports.

---

## FR-043 — Attribution Export

Authorized users shall be able to export:

```text
CSV
XLSX
JSON
PDF
```

---

## FR-044 — Attribution API

SalesGenie shall expose APIs such as:

```text
GET  /marketing/attribution
GET  /marketing/attribution/journeys
GET  /marketing/attribution/touchpoints
GET  /marketing/attribution/channels
GET  /marketing/attribution/campaigns
GET  /marketing/attribution/ads
GET  /marketing/attribution/products
GET  /marketing/attribution/audiences
GET  /marketing/attribution/revenue
GET  /marketing/attribution/profit
GET  /marketing/attribution/roas
GET  /marketing/attribution/models
GET  /marketing/attribution/comparison
GET  /marketing/attribution/incrementality
GET  /marketing/attribution/anomalies
GET  /marketing/attribution/recommendations

POST /marketing/attribution/models
POST /marketing/attribution/recalculate
POST /marketing/attribution/scenarios
```

---

## 7. AI Attribution Agent Architecture

## AI-001 — AI Attribution Agent

SalesGenie shall provide a specialized:

**AI Advertising Attribution Intelligence Agent**

The agent shall perform:

* Customer journey reconstruction
* Touchpoint attribution
* Channel attribution
* Campaign attribution
* Ad attribution
* Product attribution
* Audience attribution
* Revenue attribution
* Profit attribution
* Incrementality analysis
* Attribution model comparison
* Attribution anomaly detection
* Attribution forecasting
* Attribution optimization

---

## AI-002 — Agent Tools

The AI Attribution Agent shall have controlled access to:

```text
Event Analytics Tool
Customer Journey Tool
Identity Resolution Tool
Advertising Analytics Tool
Campaign Analytics Tool
Ad Analytics Tool
Creative Analytics Tool
Audience Analytics Tool
Product Analytics Tool
CRM Analytics Tool
Revenue Analytics Tool
Financial Analytics Tool
Attribution Modeling Tool
Statistical Analysis Tool
Causal Inference Tool
Forecasting Tool
Anomaly Detection Tool
Scenario Simulation Tool
Reporting Tool
```

---

## AI-003 — Multi-Agent Collaboration

The Attribution Agent shall collaborate with:

```text
AI Advertising Agent
AI Campaign Agent
AI Audience Agent
AI Demographic Agent
AI Marketing Analytics Agent
AI Marketing Strategy Agent
AI Product Performance Agent
AI Financial Agent
AI Business Analyst
AI Budget Optimization Agent
```

---

## AI-004 — Attribution Orchestration

```text
User Query
    ↓
Intent Detection
    ↓
Attribution Task Planning
    ↓
Identity Resolution
    ↓
Journey Reconstruction
    ↓
Attribution Model Selection
    ↓
Touchpoint Attribution
    ↓
Revenue / Profit Attribution
    ↓
Statistical Validation
    ↓
Incrementality Analysis
    ↓
Cross-Agent Validation
    ↓
AI Explanation
    ↓
Recommendation
```

---

## 8. Advanced AI Attribution Intelligence

## ADV-001 — Data-Driven Attribution

The AI shall learn contribution patterns from historical customer journeys.

---

## ADV-002 — Markov Chain Attribution

The system may estimate the removal effect of touchpoints by evaluating changes in conversion probability when a touchpoint is removed from a journey.

---

## ADV-003 — Shapley-Based Attribution

The system may use cooperative-game-theoretic attribution to estimate marginal contribution across touchpoints.

---

## ADV-004 — Causal Attribution

Where adequate experimental or observational data exists, the AI shall estimate causal impact rather than relying solely on correlation.

---

## ADV-005 — Incrementality Detection

The system shall distinguish:

```text
Exposure
    ↓
Observed Conversion
```

from:

```text
Advertising Exposure
    ↓
Additional Conversion That Would Not Otherwise Have Occurred
```

---

## ADV-006 — Attribution Bias Detection

The AI shall detect potential:

* Last-touch bias
* First-touch bias
* Retargeting bias
* Selection bias
* Survivorship bias
* Attribution-window bias
* Channel measurement bias

---

## ADV-007 — Retargeting Over-Attribution Detection

The system shall identify cases where retargeting receives excessive credit because users were already highly likely to convert.

---

## ADV-008 — Brand Search Over-Attribution Detection

The AI shall identify cases where branded search captures conversions generated by previous marketing activity.

---

## ADV-009 — Organic Channel Interaction

The AI shall analyze interactions between:

```text
Paid Marketing
+
Organic Marketing
+
Direct Traffic
+
Sales Activity
```

---

## ADV-010 — Marketing-to-Sales Attribution

The system shall connect marketing touchpoints to:

```text
Lead
    ↓
MQL
    ↓
SQL
    ↓
Opportunity
    ↓
Closed Won
```

---

## ADV-011 — Long Sales-Cycle Attribution

The AI shall support B2B journeys spanning weeks or months.

---

## ADV-012 — Subscription Attribution

The system shall connect acquisition marketing with:

```text
Initial Subscription
Renewal
Expansion
Upsell
Churn
Lifetime Revenue
```

---

## ADV-013 — Attribution Drift Detection

The system shall detect when attribution behavior changes over time.

---

## ADV-014 — Model Stability Analysis

The AI shall evaluate whether attribution conclusions remain stable across:

* Time periods
* Attribution models
* Customer segments
* Markets
* Products

---

## 9. Attribution Dashboard Requirements

## Executive Attribution Dashboard

### KPI Cards

```text
Total Conversions
Attributed Conversions
Incremental Conversions

Total Revenue
Attributed Revenue
Incremental Revenue

Attributed Profit
Incremental Profit

Attributed ROAS
Incremental ROAS

Average CAC
Average LTV

Attribution Confidence
Data Quality Score
```

---

## Attribution Visualizations

```text
Customer Journey Sankey
Attribution by Channel
Attribution by Campaign
Attribution by Product
Attribution by Audience

First-Touch vs Last-Touch
Last-Touch vs Data-Driven
Model Comparison

Attributed Revenue Trend
Incremental Revenue Trend
Attributed ROAS Trend
Attribution Drift

Conversion Paths
Top Assisted Touchpoints
Top Converting Touchpoints
Top Revenue Touchpoints
```

---

## 10. Attribution Journey View

Each journey shall contain:

```text
Journey ID
Customer ID
Anonymous ID
First Touch
Touchpoint Sequence
Campaigns
Ads
Creatives
Products
Channels
Sessions
Conversion
Conversion Value
Revenue
Profit
Attribution Model
Attribution Weights
Journey Duration
Attribution Confidence
```

---

## 11. Attribution Result Schema

Each attribution result shall contain:

```text
Attribution ID
Conversion ID
Touchpoint ID

Channel
Source
Medium
Campaign
Ad Set
Ad
Creative

Product
Audience
Customer

Attribution Model
Attribution Weight

Attributed Conversion Value
Attributed Revenue
Attributed Profit

Incremental Conversion
Incremental Revenue
Incremental Profit

Confidence Score
Data Quality Score

Model Version
Calculation Timestamp
```

---

## 12. Data Model

Core entities shall include:

```text
Tenant
Organization
Workspace

Customer
AnonymousUser
Identity
IdentityGraph

Session
Event
Touchpoint
Journey

AdvertisingAccount
Channel
Campaign
AdSet
Advertisement
Creative

Audience
Product
ProductCategory

Lead
MQL
SQL
Opportunity
Conversion

Order
Subscription
RevenueEvent
ProfitEvent

AttributionModel
AttributionModelVersion
AttributionWeight
AttributionResult

IncrementalityExperiment
IncrementalityResult

AttributionPath
AttributionAnomaly
AttributionRecommendation
AttributionForecast

DataQualityEvent
ConsentRecord
AuditEvent
```

---

## 13. Key Attribution Metrics

The platform shall calculate:

```text
Touchpoints
Conversions
Attributed Conversions

Attributed Revenue
Attributed Profit

Attribution Weight
Conversion Contribution

Assisted Conversions
Assisted Revenue

Conversion Rate
Customer Acquisition Cost
Attributed CAC

Attributed ROAS
Incremental ROAS

Customer Lifetime Value
LTV:CAC

Average Journey Length
Average Time to Conversion

First-Touch Contribution
Last-Touch Contribution
Multi-Touch Contribution

Incremental Conversions
Incremental Revenue
Incremental Profit

Attribution Confidence
Attribution Stability
Data Quality Score
```

---

## 14. Attribution Workflow

```text
Data Sources
    ↓
Event Collection
    ↓
Data Validation
    ↓
Event Deduplication
    ↓
Identity Resolution
    ↓
Journey Reconstruction
    ↓
Conversion Matching
    ↓
Attribution Window Filtering
    ↓
Attribution Model
    ↓
Touchpoint Weight Calculation
    ↓
Revenue Attribution
    ↓
Profit Attribution
    ↓
Incrementality Analysis
    ↓
Confidence Estimation
    ↓
Model Comparison
    ↓
AI Interpretation
    ↓
Recommendation
    ↓
Optimization
    ↓
Impact Measurement
    ↓
Continuous Learning
```

---

## 15. Attribution Quality Framework

The platform shall calculate an attribution quality score using:

```text
Tracking Completeness
        +
Identity Resolution Quality
        +
Event Integrity
        +
Conversion Matching Quality
        +
Data Freshness
        +
Model Stability
        +
Sample Size
        +
Cross-Channel Coverage
```

The system shall classify attribution quality as:

```text
Excellent
Good
Moderate
Low
Insufficient
```

---

## 16. AI Attribution Guardrails

The AI shall never present attribution estimates as causal facts unless causal evidence supports the conclusion.

The AI shall explicitly distinguish:

```text
Observed
Attributed
Predicted
Incremental
Inferred
Recommended
```

---

## AI Guardrail Example

The system shall not state:

```text
"Facebook caused 40% of your revenue."
```

when only observational attribution data exists.

Instead, it shall distinguish:

```text
"Facebook received 40% of attributed revenue under the selected
attribution model. This does not by itself establish that Facebook
caused 40% of revenue."
```

---

## 17. Natural-Language AI Examples

Users shall be able to ask:

```text
Which marketing channel deserves the most credit for revenue?

Which campaigns influence customers before they convert?

What are our top conversion paths?

Which campaigns are overvalued by last-click attribution?

Which campaigns are undervalued by last-click attribution?

Which channel creates the highest-LTV customers?

Which advertising channel has the strongest incremental impact?

How much revenue can we confidently attribute to paid social?

Why does Google receive more credit under last-click attribution?

Which campaign assists the most conversions?

Which customer journey produces the highest profit?

Which channel should receive additional budget?

How reliable is our attribution data?

How much of our reported ROAS is likely incremental?
```

---

## 18. Example AI Attribution Analysis

```text
User:
Which channel generates the highest-value customers?

AI:

Top Channel:
Paid Search

Evidence:

• Attributed conversion rate: 7.8%
• Customer conversion rate: 6.2%
• Average customer revenue: $1,240
• Average customer LTV: $3,850
• CAC: $210
• LTV:CAC: 18.3x
• Incrementality confidence: Medium
• Attribution confidence: High

Comparison:

Paid Social
• LTV: $2,740
• CAC: $245
• LTV:CAC: 11.2x

Email
• LTV: $3,100
• CAC: $74
• LTV:CAC: 41.9x

Interpretation:

Email has the strongest efficiency among identified channels,
while Paid Search contributes the highest volume of high-value
new customers.

Recommendation:

Increase investment in Paid Search selectively while protecting
Email retention and lifecycle programs.

Important limitation:

These figures represent attributed contribution. Incremental
causal impact should be validated through controlled experiments
where feasible.
```

---

## 19. Non-Functional Requirements

## NFR-001 — Scalability

The platform shall support:

* Billions of attribution events
* Millions of customer journeys
* Millions of conversions
* Large multi-channel advertising datasets
* Multiple enterprise tenants

---

## NFR-002 — Performance

The system shall support:

* Streaming event ingestion
* Batch processing
* Incremental attribution recalculation
* Cached analytics
* Distributed processing
* Pre-aggregated reporting

---

## NFR-003 — Reliability

The platform shall provide:

* Idempotent ingestion
* Retry mechanisms
* Dead-letter queues
* Provider failure recovery
* Data reconciliation
* Attribution recalculation

---

## NFR-004 — Security

The system shall implement:

* OAuth 2.0
* JWT
* RBAC
* MFA
* Encryption in transit
* Encryption at rest
* Tenant isolation
* Secure secrets management
* Audit logging

---

## NFR-005 — Privacy

The platform shall provide configurable:

* Consent management
* Data retention
* Data deletion
* Identity access controls
* Data minimization
* Privacy-aware analytics

---

## NFR-006 — Explainability

Attribution results shall be explainable through:

```text
Touchpoints
Weights
Model
Evidence
Data Quality
Confidence
Assumptions
```

---

## NFR-007 — Observability

The platform shall monitor:

```text
Event Ingestion Health
Identity Resolution Health
Conversion Matching Health
Attribution Processing Latency
Attribution Model Health
Data Freshness
Data Quality
Model Drift
Attribution Stability
API Health
Provider Health
```

---

## NFR-008 — Reproducibility

Historical attribution calculations shall be reproducible using:

```text
Dataset Version
Attribution Model Version
Configuration Version
Attribution Window
Feature Version
Calculation Timestamp
```

---

## 20. Enterprise Acceptance Criteria

## AC-001

Given valid advertising and conversion events, the platform shall reconstruct customer journeys.

## AC-002

Given a configured attribution model, the platform shall assign attribution weights to eligible touchpoints.

## AC-003

The attribution engine shall support multiple attribution methodologies.

## AC-004

The platform shall calculate attributed conversions and revenue.

## AC-005

The platform shall calculate attributed profit when cost data is available.

## AC-006

Users shall be able to compare attribution models using the same underlying dataset.

## AC-007

The platform shall identify assisted conversion touchpoints.

## AC-008

The AI shall identify significant attribution discrepancies.

## AC-009

The AI shall distinguish correlation-based attribution from causal incrementality.

## AC-010

Attribution results shall contain confidence and data-quality indicators.

## AC-011

The system shall detect missing, duplicated, or inconsistent attribution events.

## AC-012

The platform shall maintain tenant isolation.

## AC-013

All attribution model changes shall be auditable.

## AC-014

Historical attribution results shall be reproducible.

## AC-015

The AI shall not claim causal impact without appropriate evidence.

## AC-016

The system shall support offline conversion attribution where configured.

## AC-017

The platform shall support long customer journeys and delayed conversions.

## AC-018

The AI shall identify high-value customer journeys based on revenue, profit, and LTV.

## AC-019

The system shall provide attribution-driven budget recommendations.

## AC-020

All AI-generated attribution recommendations shall expose:

```text
Evidence
Attribution Model
Confidence
Uncertainty
Expected Impact
Limitations
```

---

## 21. Strategic Product Principle

SalesGenie's AI Attribution module shall not operate as a basic marketing reporting feature.

It shall function as a **closed-loop AI Marketing Attribution, Incrementality, and Optimization Intelligence System**:

```text
COLLECT
    ↓
RESOLVE
    ↓
RECONSTRUCT
    ↓
ATTRIBUTE
    ↓
VALIDATE
    ↓
COMPARE
    ↓
MEASURE INCREMENTALITY
    ↓
EXPLAIN
    ↓
PREDICT
    ↓
RECOMMEND
    ↓
OPTIMIZE
    ↓
MEASURE IMPACT
    ↓
LEARN
```

The ultimate objective is to answer:

```text
WHO
    ↓
Which customers were influenced?

WHAT
    ↓
Which touchpoints contributed?

WHERE
    ↓
Which channels and campaigns contributed?

WHEN
    ↓
When did each touchpoint influence conversion?

HOW
    ↓
How much contribution should each touchpoint receive?

WHY
    ↓
Why does the attribution model assign this contribution?

WHAT IS REAL
    ↓
Which outcomes are merely attributed versus incremental?

WHAT NEXT
    ↓
Where should SalesGenie allocate the next marketing dollar?
```

The final system shall optimize for **incremental revenue, incremental profit, qualified customer acquisition, customer lifetime value, marketing efficiency, attribution reliability, and sustainable business growth**, rather than treating attributed conversions or last-click ROAS as definitive measures of advertising effectiveness.
