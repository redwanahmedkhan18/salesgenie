# SalesGenie — AI-Powered Ad ROAS Analysis

## User Requirements, System Requirements & Functional Requirements

> **Document:** `ad_roas_analysis.md`
>
> **Platform:** SalesGenie Enterprise AI Customer Support, Sales & Marketing Platform
>
> **Capability:** AI-based Advertising ROAS Intelligence
>
> **Primary Objective:** Enable SalesGenie customers to measure, explain, predict, optimize, and continuously improve Return on Ad Spend (ROAS) across advertising channels, campaigns, audiences, creatives, products, regions, and customer segments.

---

## 1. Product Overview

SalesGenie's **AI Ad ROAS Analysis** module shall provide an enterprise-grade intelligence layer for measuring and optimizing advertising profitability.

The system shall ingest advertising spend, attributed revenue, conversions, customer, campaign, product, audience, and attribution data from supported advertising platforms and business systems.

The AI layer shall transform raw advertising data into:

- ROAS measurements
- ROAS trends
- Campaign profitability analysis
- Channel-level ROAS comparison
- Audience-level ROAS analysis
- Creative-level ROAS analysis
- Product-level ROAS analysis
- Geographic ROAS analysis
- Customer-segment ROAS analysis
- Attribution-aware revenue analysis
- Incremental ROAS analysis
- ROAS forecasting
- ROAS anomaly detection
- ROAS optimization recommendations
- Budget reallocation recommendations
- Campaign scaling recommendations
- Campaign reduction/pause recommendations
- Executive-level advertising intelligence

The system shall support both:

1. **AI-driven autonomous analysis**
2. **Human-driven analysis and decision-making**

AI recommendations shall remain explainable, auditable, configurable, and subject to organizational policies and approval workflows.

---

## 2. Business Objectives

## BO-001 — Maximize Advertising Efficiency

The platform shall help organizations maximize revenue generated for every unit of advertising spend.

## BO-002 — Improve Marketing Profitability

The system shall identify campaigns, audiences, products, channels, and creatives generating the highest economic return.

## BO-003 — Reduce Advertising Waste

The platform shall detect inefficient spending and identify areas where advertising budgets can be reduced, paused, or reallocated.

## BO-004 — Improve Budget Allocation

The AI shall recommend budget allocation across channels and campaigns based on historical and predicted performance.

## BO-005 — Improve Decision Speed

Marketing teams shall receive near-real-time intelligence rather than manually analyzing multiple advertising dashboards.

## BO-006 — Identify Growth Opportunities

The system shall identify high-ROAS opportunities that can potentially be scaled.

## BO-007 — Detect Performance Degradation

The platform shall identify statistically significant deterioration in ROAS and related advertising metrics.

## BO-008 — Support Executive Decision-Making

Executives shall receive concise, financially meaningful advertising intelligence and recommendations.

---

## 3. User Roles

## 3.1 Super Admin

The Super Admin shall:

- Configure platform-wide advertising analytics policies.
- Configure supported advertising integrations.
- Monitor system-wide advertising analytics health.
- Configure AI policies.
- Configure organizational limits.
- Monitor tenant-level usage.
- Review audit logs.
- Manage system-level permissions.

## 3.2 Organization Admin

The Organization Admin shall:

- Connect advertising accounts.
- Configure advertising data sources.
- Configure attribution settings.
- Configure ROAS calculation rules.
- Configure financial assumptions.
- Configure AI permissions.
- Configure approval requirements.
- Manage marketing users.
- Review organizational ROAS analytics.

## 3.3 Marketing Manager

The Marketing Manager shall:

- Monitor campaign ROAS.
- Compare advertising channels.
- Analyze campaign profitability.
- Review AI recommendations.
- Approve or reject AI recommendations.
- Configure campaign objectives.
- Monitor budget efficiency.
- Investigate ROAS anomalies.

## 3.4 Marketing Analyst

The Marketing Analyst shall:

- Build custom ROAS reports.
- Analyze historical performance.
- Compare campaigns.
- Segment performance.
- Perform cohort analysis.
- Export analytical datasets.
- Investigate attribution discrepancies.

## 3.5 Advertising Specialist

The Advertising Specialist shall:

- Monitor campaign-level performance.
- Analyze ad sets and creatives.
- Investigate audience performance.
- Optimize campaigns.
- Review AI-generated optimization recommendations.

## 3.6 Finance Manager

The Finance Manager shall:

- Validate advertising revenue assumptions.
- Review advertising costs.
- Analyze contribution margin.
- Compare ROAS with profitability.
- Review financial impact of advertising decisions.

## 3.7 Sales Manager

The Sales Manager shall:

- Analyze advertising-generated leads.
- Track lead-to-opportunity conversion.
- Analyze advertising-generated pipeline.
- Compare advertising spend with sales revenue.

## 3.8 Executive

The Executive shall:

- View advertising performance summaries.
- Monitor ROAS trends.
- View channel profitability.
- Review major opportunities and risks.
- Receive AI-generated strategic recommendations.

## 3.9 End User

Authorized end users shall:

- View permitted advertising analytics.
- Query the AI analytics assistant.
- Generate permitted reports.
- Review campaign performance.

---

## 4. User Requirements

## UR-001 — Advertising Account Connection

Users shall be able to connect supported advertising accounts to SalesGenie.

The system shall support integrations such as:

- Google Ads
- Facebook Ads
- Instagram Ads
- LinkedIn Ads
- TikTok Ads
- YouTube Ads
- Other supported advertising providers

Users shall be able to:

- Connect accounts.
- Disconnect accounts.
- Reauthorize accounts.
- View connection status.
- View synchronization status.
- Configure synchronization frequency.

---

## UR-002 — Unified Advertising Data

Users shall be able to view advertising performance across multiple platforms from a unified interface.

The system shall normalize:

- Spend
- Impressions
- Reach
- Clicks
- CTR
- CPC
- CPM
- Leads
- Conversions
- Conversion value
- Revenue
- ROAS
- CPA
- CAC
- Profit
- Contribution margin

---

## UR-003 — ROAS Calculation

Users shall be able to view ROAS calculated consistently across campaigns, ad sets, ads, audiences, products, and channels.

The default calculation shall be:

```text
ROAS = Attributed Revenue / Advertising Spend
```

The system shall also support configurable variants such as:

```text
Gross Revenue ROAS
Net Revenue ROAS
Contribution Margin ROAS
Profit ROAS
Incremental ROAS
```

---

## UR-004 — ROAS Dashboard

Users shall receive a centralized ROAS dashboard containing:

* Total advertising spend
* Attributed revenue
* ROAS
* ROAS change
* Conversion volume
* CPA
* CAC
* Revenue per conversion
* Profit
* Contribution margin
* Best-performing campaigns
* Worst-performing campaigns
* Best-performing channels
* ROAS anomalies
* AI recommendations

---

## UR-005 — Historical ROAS Analysis

Users shall be able to analyze ROAS historically.

Supported time ranges shall include:

* Today
* Yesterday
* Last 7 days
* Last 14 days
* Last 30 days
* Last 90 days
* Month-to-date
* Quarter-to-date
* Year-to-date
* Custom date range

Users shall be able to compare:

* Current vs previous period
* Current vs same period last year
* Campaign vs campaign
* Channel vs channel
* Product vs product
* Audience vs audience

---

## UR-006 — Campaign ROAS Analysis

Users shall be able to analyze ROAS at campaign level.

The system shall display:

* Campaign spend
* Campaign revenue
* Campaign ROAS
* Campaign profit
* Conversion volume
* CPA
* CAC
* CTR
* CPC
* CPM
* Conversion rate
* Revenue trend
* ROAS trend

---

## UR-007 — Ad Set / Audience ROAS Analysis

Users shall be able to determine which audience segments generate the highest return.

The system shall support analysis by:

* Demographics
* Geography
* Interests
* Behavioral segments
* Customer lifecycle
* Lookalike audiences
* Custom audiences
* Retargeting audiences
* Prospecting audiences
* Existing customers

---

## UR-008 — Creative ROAS Analysis

Users shall be able to compare creative performance.

The platform shall analyze:

* Images
* Videos
* Headlines
* Primary text
* CTAs
* Creative formats
* Creative themes
* Creative variants

The system shall identify:

* High-ROAS creatives
* Low-ROAS creatives
* Creative fatigue
* Creative performance decay
* Winning creative patterns

---

## UR-009 — Product ROAS Analysis

Users shall be able to determine which products generate the highest advertising return.

The system shall support:

* Product-level revenue
* Product-level advertising spend
* Product ROAS
* Product profit
* Product contribution margin
* Product CAC
* Product conversion rate

---

## UR-010 — Geographic ROAS Analysis

Users shall be able to analyze ROAS by:

* Country
* State/province
* City
* Region
* Market
* Territory

The system shall identify high-value and low-value geographic markets.

---

## UR-011 — Channel ROAS Analysis

Users shall be able to compare:

* Google Ads
* Facebook Ads
* Instagram Ads
* LinkedIn Ads
* TikTok Ads
* YouTube Ads
* Other connected advertising channels

The platform shall identify the highest-performing channels.

---

## UR-012 — Attribution-Aware ROAS

Users shall be able to configure attribution models.

Supported models may include:

* Last-click attribution
* First-click attribution
* Linear attribution
* Position-based attribution
* Time-decay attribution
* Data-driven attribution
* Custom attribution

The system shall clearly indicate which attribution model was used.

---

## UR-013 — Incremental ROAS

The system shall support incremental ROAS analysis where sufficient experimental or causal data exists.

The platform shall distinguish:

```text
Attributed ROAS
vs
Incremental ROAS
```

The AI shall warn users when incremental impact cannot be reliably established.

---

## UR-014 — AI ROAS Explanation

Users shall be able to ask the AI:

* Why did ROAS decrease?
* Why did ROAS increase?
* Which campaigns are wasting money?
* Which campaigns should be scaled?
* Which audience has the highest ROAS?
* Which channel has the best ROAS?
* Which products generate the best advertising return?
* What caused the ROAS change?
* What should we do next?

The AI shall provide evidence-backed explanations.

---

## UR-015 — AI ROAS Recommendations

The AI shall generate recommendations such as:

* Increase budget.
* Decrease budget.
* Pause campaign.
* Test new creative.
* Expand audience.
* Reduce audience.
* Shift budget to another campaign.
* Shift budget to another channel.
* Reduce spending in underperforming regions.
* Increase spending in high-performing regions.

Each recommendation shall include:

* Recommendation
* Reason
* Expected impact
* Confidence
* Supporting metrics
* Supporting data
* Risk level
* Recommended action

---

## UR-016 — Human Approval

Organizations shall be able to require human approval before AI recommendations result in operational changes.

Approval states shall include:

* Pending
* Approved
* Rejected
* Expired
* Executed
* Failed
* Rolled back

---

## UR-017 — AI Autonomy

Organizations shall be able to configure AI autonomy levels:

```text
Level 0 — Analysis Only
Level 1 — Recommendations
Level 2 — Human Approval Required
Level 3 — Conditional Automation
Level 4 — Autonomous Optimization
```

---

## UR-018 — ROAS Forecasting

Users shall be able to view predicted ROAS.

The AI shall forecast:

* Short-term ROAS
* Medium-term ROAS
* Long-term ROAS

Forecasts shall include:

* Prediction
* Confidence interval
* Key assumptions
* Influencing factors
* Risk indicators

---

## UR-019 — ROAS Anomaly Detection

The platform shall automatically detect unusual ROAS behavior.

Examples:

* Sudden ROAS collapse
* Unexpected ROAS spike
* Spend increase without revenue increase
* Revenue decrease without spend decrease
* Conversion drop
* CPA increase
* Tracking failure
* Attribution anomaly

---

## UR-020 — Budget Scenario Analysis

Users shall be able to ask:

> "What happens if I increase this campaign budget by 30%?"

The AI shall estimate:

* Additional spend
* Expected revenue
* Expected ROAS
* Expected conversions
* Expected profit
* Confidence
* Risk

---

## UR-021 — Budget Reallocation Simulation

Users shall be able to simulate budget movement between campaigns.

Example:

```text
Move $10,000 from Campaign A to Campaign B.
```

The system shall estimate the potential effect on:

* Revenue
* ROAS
* Profit
* Conversions
* CAC

---

## UR-022 — Custom ROAS Targets

Users shall be able to define:

* Minimum ROAS
* Target ROAS
* Ideal ROAS
* Campaign-specific ROAS
* Channel-specific ROAS
* Product-specific ROAS

---

## UR-023 — ROAS Alerts

Users shall be able to configure alerts for:

* ROAS below threshold
* ROAS above target
* ROAS percentage decline
* Spend anomaly
* Revenue anomaly
* CPA increase
* Conversion decline
* Campaign profitability deterioration

Alerts shall support:

* Email
* In-app notifications
* Slack
* Microsoft Teams
* Webhooks

---

## UR-024 — Custom Reporting

Users shall be able to create custom reports containing:

* ROAS
* Revenue
* Spend
* Profit
* Campaigns
* Channels
* Audiences
* Products
* Regions
* Creatives
* Attribution

Reports shall support:

* PDF
* CSV
* XLSX
* API
* Scheduled delivery

---

## UR-025 — Executive Reporting

Executives shall receive a simplified view containing:

* Advertising spend
* Advertising revenue
* ROAS
* Profit contribution
* ROAS trend
* Top opportunities
* Major risks
* AI recommendations

---

## 5. System Requirements

## SR-001 — Multi-Tenant Architecture

The system shall support strict tenant isolation.

Every advertising object shall be associated with:

```text
tenant_id
organization_id
workspace_id
advertising_account_id
```

Cross-tenant data access shall be prohibited.

---

## SR-002 — Data Ingestion

The platform shall ingest:

* Campaign metadata
* Ad group/ad set metadata
* Ad metadata
* Spend data
* Impression data
* Click data
* Conversion data
* Revenue data
* Audience data
* Product data
* Customer data

---

## SR-003 — Data Normalization

The system shall normalize provider-specific schemas into a canonical advertising model.

Example:

```text
AdvertisingAccount
Campaign
AdGroup
Ad
Creative
Audience
Spend
Impression
Click
Conversion
Revenue
AttributionEvent
```

---

## SR-004 — Data Synchronization

The platform shall support:

* Initial synchronization
* Incremental synchronization
* Scheduled synchronization
* Event-driven synchronization where supported
* Retry mechanisms
* Backoff mechanisms
* Idempotent ingestion

---

## SR-005 — Data Quality

The system shall validate:

* Missing spend
* Duplicate events
* Missing revenue
* Invalid timestamps
* Currency mismatches
* Attribution inconsistencies
* Conversion duplication
* API synchronization gaps

---

## SR-006 — Currency Normalization

The system shall support multi-currency organizations.

The system shall store:

```text
original_currency
original_amount
conversion_rate
normalized_currency
normalized_amount
rate_timestamp
```

---

## SR-007 — Attribution Engine

The system shall provide a configurable attribution engine capable of processing:

```text
Impression
Click
Lead
Opportunity
Purchase
Subscription
Renewal
Refund
Cancellation
```

---

## SR-008 — ROAS Calculation Engine

The system shall provide a deterministic ROAS calculation service.

Example:

```text
ROAS = Revenue / Ad Spend
```

The calculation engine shall support:

* Gross revenue
* Net revenue
* Contribution revenue
* Profit-based ROAS
* Incremental ROAS

---

## SR-009 — Metric Consistency

All dashboards, APIs, reports, and AI agents shall use the same canonical metric definitions.

Metric definitions shall be centrally versioned.

---

## SR-010 — Analytics Storage

The platform shall maintain analytical datasets optimized for:

* Time-series analysis
* Aggregation
* Filtering
* Segmentation
* Cohort analysis
* Attribution analysis

---

## SR-011 — Real-Time Analytics

The platform should support near-real-time processing for supported advertising providers.

The target shall be:

```text
Data ingestion → normalization → analytics
```

within a configurable low-latency SLA.

---

## SR-012 — AI Analytics Layer

The AI layer shall have access only to authorized and relevant analytical data.

AI analysis shall support:

* Natural-language querying
* Root-cause analysis
* Forecasting
* Anomaly detection
* Recommendation generation
* Scenario analysis

---

## SR-013 — AI Grounding

AI-generated financial and advertising conclusions shall be grounded in actual platform data.

The AI shall not fabricate:

* Spend
* Revenue
* ROAS
* Conversions
* Campaign performance
* Attribution results

If required data is unavailable, the AI shall explicitly state that the analysis cannot be reliably completed.

---

## SR-014 — Explainability

Every AI recommendation shall provide:

```text
Recommendation
Reason
Evidence
Metrics
Assumptions
Confidence
Risk
Expected impact
```

---

## SR-015 — Confidence Scoring

AI predictions and recommendations shall include confidence estimates.

Confidence shall consider:

* Data volume
* Data freshness
* Historical stability
* Attribution quality
* Model uncertainty
* Campaign maturity
* External factors

---

## SR-016 — Anomaly Detection Engine

The platform shall support statistical and ML-based anomaly detection.

Potential methods include:

* Z-score
* IQR
* EWMA
* Seasonal decomposition
* Isolation Forest
* Change-point detection
* Time-series forecasting residuals

---

## SR-017 — Forecasting Engine

The forecasting layer may support:

* Statistical time-series models
* Gradient boosting
* Temporal neural networks
* Bayesian models
* Ensemble forecasting

The system shall compare model performance and select appropriate models based on data characteristics.

---

## SR-018 — Recommendation Engine

The recommendation engine shall evaluate:

```text
Current ROAS
Historical ROAS
Target ROAS
Marginal ROAS
Budget
Spend velocity
Conversion rate
CPA
CAC
Revenue
Profit
Audience saturation
Creative fatigue
Seasonality
```

---

## SR-019 — Marginal ROAS

The system should calculate or estimate:

```text
mROAS = ΔRevenue / ΔAdSpend
```

This shall be used to evaluate whether additional spending is likely to remain economically efficient.

---

## SR-020 — Profit-Aware Optimization

The system shall not optimize exclusively for ROAS.

Where financial data is available, the AI shall consider:

```text
Revenue
COGS
Advertising Spend
Operating Costs
Contribution Margin
Profit
Customer Lifetime Value
```

---

## SR-021 — Role-Based Access Control

Access shall be controlled using RBAC.

Permissions shall include:

```text
advertising.read
advertising.write
roas.read
roas.export
roas.configure
roas.recommendations.read
roas.recommendations.approve
roas.automation.execute
roas.admin
```

---

## SR-022 — API Security

All APIs shall implement:

* OAuth 2.0
* JWT authentication
* RBAC
* Tenant authorization
* Rate limiting
* Audit logging
* Input validation
* Secure secret storage

---

## SR-023 — Advertising Credential Security

Advertising API credentials shall:

* Never be exposed to end users.
* Be encrypted at rest.
* Be encrypted in transit.
* Use secret rotation.
* Support token refresh.
* Support revocation.

---

## SR-024 — Auditability

The system shall log:

* Data imports
* Configuration changes
* ROAS calculations
* AI recommendations
* User approvals
* Automated actions
* Budget changes
* Campaign changes
* Export operations

---

## SR-025 — Observability

The platform shall provide monitoring for:

* Data ingestion
* API failures
* Data freshness
* ROAS computation
* AI latency
* Forecast accuracy
* Recommendation accuracy
* Integration health

---

## 6. Functional Requirements

## FR-001 — Advertising Account Management

The system shall allow authorized users to:

1. Add advertising accounts.
2. Authenticate advertising accounts.
3. Validate credentials.
4. Import account metadata.
5. Synchronize campaigns.
6. Monitor synchronization.
7. Disconnect accounts.

---

## FR-002 — Campaign Data Pipeline

The system shall:

1. Retrieve campaign data.
2. Validate provider responses.
3. Normalize provider schemas.
4. Deduplicate records.
5. Validate timestamps.
6. Normalize currencies.
7. Persist canonical records.
8. Generate analytical aggregates.

---

## FR-003 — ROAS Computation

For each eligible entity, the system shall calculate:

```text
ROAS = Attributed Revenue / Advertising Spend
```

Supported entities:

```text
Account
Channel
Campaign
Ad Group
Ad Set
Ad
Creative
Audience
Product
Region
Customer Segment
```

---

## FR-004 — ROAS Time-Series

The system shall generate:

* Daily ROAS
* Weekly ROAS
* Monthly ROAS
* Quarterly ROAS
* Custom-period ROAS

The system shall preserve historical snapshots for reproducibility.

---

## FR-005 — ROAS Comparison

The system shall compare:

```text
Campaign A vs Campaign B
Channel A vs Channel B
Audience A vs Audience B
Product A vs Product B
Region A vs Region B
Creative A vs Creative B
```

---

## FR-006 — ROAS Ranking

The platform shall rank entities by:

* ROAS
* Revenue
* Profit
* Spend
* Conversions
* CPA
* CAC
* mROAS

Users shall be able to sort ascending or descending.

---

## FR-007 — ROAS Trend Detection

The system shall determine whether ROAS is:

* Increasing
* Decreasing
* Stable
* Volatile
* Recovering
* Deteriorating

---

## FR-008 — ROAS Root-Cause Analysis

When ROAS changes materially, the AI shall investigate:

```text
Spend change
Revenue change
Conversion change
CTR change
CPC change
CPA change
Audience change
Creative change
Geographic change
Product mix change
Attribution change
Seasonality
```

The AI shall rank potential causes by evidence strength.

---

## FR-009 — ROAS Anomaly Detection

The system shall:

1. Establish historical baselines.
2. Detect deviations.
3. Estimate anomaly severity.
4. Identify affected campaigns.
5. Identify likely causes.
6. Notify authorized users.
7. Generate recommended actions.

---

## FR-010 — AI Campaign Diagnosis

The AI shall classify campaigns into categories such as:

```text
High ROAS / High Growth
High ROAS / Low Scale
Low ROAS / High Spend
Low ROAS / Low Spend
High Spend / Declining ROAS
Stable / Efficient
Insufficient Data
Tracking Risk
```

---

## FR-011 — AI Budget Recommendation

The AI shall recommend budget changes based on:

* Target ROAS
* Current ROAS
* Historical ROAS
* Marginal ROAS
* Budget utilization
* Conversion capacity
* Audience saturation
* Profitability

---

## FR-012 — AI Scaling Recommendation

The AI shall identify campaigns that may be suitable for scaling.

A recommendation shall include:

```text
Current budget
Recommended budget
Current ROAS
Expected ROAS
Expected revenue
Expected additional spend
Expected additional revenue
Confidence
Risk
```

---

## FR-013 — AI Reduction Recommendation

The AI shall identify inefficient campaigns.

Possible actions:

```text
Reduce budget
Pause campaign
Change audience
Change creative
Change offer
Change bidding strategy
Investigate tracking
```

---

## FR-014 — Budget Reallocation

The system shall allow users to simulate or execute:

```text
Campaign A → Campaign B
Channel A → Channel B
Audience A → Audience B
Region A → Region B
```

The system shall calculate expected impact before execution.

---

## FR-015 — ROAS Forecast

The AI shall forecast future ROAS using historical and contextual data.

Forecast output shall include:

```text
Forecast value
Prediction interval
Forecast horizon
Confidence
Key drivers
Assumptions
```

---

## FR-016 — Scenario Simulation

Users shall be able to create scenarios.

Example:

```text
Scenario:
Increase Campaign A budget by 25%.

Expected:
Spend: +25%
Revenue: estimated increase
ROAS: estimated change
Profit: estimated change
Risk: medium
```

---

## FR-017 — Target ROAS Monitoring

The system shall compare actual ROAS against configured targets.

Example:

```text
Actual ROAS: 3.4x
Target ROAS: 4.0x
Gap: -0.6x
```

---

## FR-018 — Automated Alerts

The system shall trigger alerts when:

```text
ROAS < threshold
ROAS decreases > threshold
Spend increases without proportional revenue
Revenue decreases unexpectedly
CPA increases significantly
Conversion rate decreases significantly
```

---

## FR-019 — AI Natural-Language Analytics

Users shall be able to ask questions such as:

```text
Which campaigns generated the highest ROAS this month?

Why did our ROAS decline last week?

Which channel should receive more budget?

Which campaigns should we pause?

What would happen if we increase the Google Ads budget by 20%?

Which audiences generate profitable customers?

Show campaigns with high spend but low ROAS.

Which products have the strongest advertising economics?
```

The AI shall translate natural language into authorized analytical queries.

---

## FR-020 — AI Analytical Query Planning

The AI shall:

1. Interpret the question.
2. Identify required metrics.
3. Identify required dimensions.
4. Determine relevant date range.
5. Validate available data.
6. Execute analytical queries.
7. Analyze results.
8. Produce a grounded response.

---

## FR-021 — AI Recommendation Evaluation

Recommendations shall be evaluated using:

```text
Expected revenue impact
Expected profit impact
Expected ROAS impact
Risk
Confidence
Data sufficiency
Historical evidence
```

---

## FR-022 — Human Approval Workflow

When approval is required:

```text
AI Recommendation
        ↓
Pending Approval
        ↓
Human Review
        ↓
Approved / Rejected
        ↓
Execution
        ↓
Verification
```

---

## FR-023 — Autonomous Optimization

For organizations allowing autonomous optimization, the system shall:

1. Detect optimization opportunity.
2. Generate recommendation.
3. Validate policy constraints.
4. Validate budget constraints.
5. Validate safety thresholds.
6. Execute the permitted change.
7. Monitor post-change performance.
8. Roll back where configured thresholds are violated.

---

## FR-024 — Guardrails

Organizations shall be able to configure:

```text
Maximum budget increase
Maximum budget decrease
Maximum daily spend
Minimum acceptable ROAS
Maximum acceptable CPA
Maximum autonomous budget change
Approval-required actions
Restricted campaigns
Restricted channels
```

---

## FR-025 — Recommendation Feedback

Users shall be able to:

* Approve recommendations.
* Reject recommendations.
* Modify recommendations.
* Mark recommendations as useful.
* Mark recommendations as incorrect.
* Provide feedback.

The feedback shall be stored for future model evaluation and recommendation-quality improvement.

---

## FR-026 — ROAS Report Generation

The system shall generate reports containing:

```text
Executive Summary
Advertising Spend
Attributed Revenue
ROAS
Profitability
Campaign Performance
Channel Performance
Audience Performance
Creative Performance
Product Performance
Geographic Performance
ROAS Trends
Anomalies
Forecasts
AI Recommendations
```

---

## FR-027 — Scheduled Reporting

Users shall be able to schedule reports:

* Daily
* Weekly
* Monthly
* Quarterly
* Custom schedule

---

## FR-028 — Data Export

Authorized users shall be able to export:

* CSV
* XLSX
* JSON
* PDF

Exports shall respect tenant and RBAC restrictions.

---

## FR-029 — API Access

SalesGenie shall expose APIs for:

```text
GET /advertising/accounts
GET /advertising/campaigns
GET /advertising/metrics
GET /advertising/roas
GET /advertising/roas/trends
GET /advertising/roas/anomalies
GET /advertising/roas/forecast
GET /advertising/roas/recommendations
POST /advertising/roas/scenarios
POST /advertising/roas/recommendations/{id}/approve
POST /advertising/roas/recommendations/{id}/reject
```

---

## 7. AI Architecture Requirements

## AI-001 — Specialized ROAS Intelligence Agent

SalesGenie shall provide a specialized **AI ROAS Intelligence Agent** responsible for:

* ROAS analysis
* Root-cause analysis
* Forecasting
* Anomaly detection
* Scenario analysis
* Optimization recommendations

---

## AI-002 — Agent Tool Access

The ROAS agent shall be able to access authorized tools such as:

```text
Advertising Analytics Tool
Campaign Analytics Tool
Revenue Analytics Tool
Financial Analytics Tool
Audience Analytics Tool
Product Analytics Tool
Attribution Tool
Forecasting Tool
Anomaly Detection Tool
Scenario Simulation Tool
Reporting Tool
```

---

## AI-003 — Multi-Agent Collaboration

The ROAS agent may collaborate with:

```text
Campaign Agent
Audience Agent
Advertising Agent
Marketing Analytics Agent
Financial AI Agent
Business AI Analyst
Marketing Strategy Agent
Budget Optimization Agent
Customer Intelligence Agent
```

---

## AI-004 — Agent Orchestration

The SalesGenie orchestration layer shall:

1. Receive the user request.
2. Determine required analytical agents.
3. Route the request.
4. Execute tools.
5. Validate returned data.
6. Aggregate agent outputs.
7. Resolve contradictions.
8. Generate final recommendations.

---

## AI-005 — Evidence-Based Reasoning

AI conclusions shall reference the underlying metrics and data used to produce the recommendation.

---

## AI-006 — Uncertainty Handling

If evidence is insufficient, the AI shall respond with:

```text
Insufficient Data
Low Confidence
Tracking Issue
Attribution Limitation
Forecast Uncertainty
```

rather than inventing a conclusion.

---

## 8. Advanced ROAS Intelligence

## ADV-001 — Marginal ROAS Optimization

The platform shall identify diminishing returns from additional advertising expenditure.

---

## ADV-002 — Saturation Detection

The AI shall detect when additional advertising spend produces progressively lower returns.

---

## ADV-003 — Creative Fatigue Impact

The AI shall estimate whether creative fatigue contributes to declining ROAS.

---

## ADV-004 — Audience Saturation

The system shall detect audience saturation and estimate its impact on ROAS.

---

## ADV-005 — Cross-Channel Cannibalization

Where sufficient data exists, the system shall identify potential cannibalization between advertising channels.

---

## ADV-006 — Customer Lifetime Value ROAS

The system shall support:

```text
LTV-based ROAS
```

when customer lifetime revenue data is available.

---

## ADV-007 — Cohort ROAS

Users shall be able to analyze ROAS by customer acquisition cohort.

---

## ADV-008 — New vs Existing Customer ROAS

The system shall distinguish:

```text
New Customer ROAS
Existing Customer ROAS
```

---

## ADV-009 — Profit-Adjusted ROAS

The system shall support profitability-aware metrics:

```text
Profit ROAS = Profit / Advertising Spend
```

and:

```text
Contribution ROAS = Contribution Margin / Advertising Spend
```

---

## 9. Dashboard Requirements

## Main ROAS Dashboard

The dashboard shall contain:

### KPI Cards

* Ad Spend
* Revenue
* ROAS
* Profit
* Conversions
* CPA
* CAC
* mROAS

### Visualizations

* ROAS over time
* Spend vs revenue
* Channel ROAS
* Campaign ROAS
* Audience ROAS
* Product ROAS
* Geographic ROAS
* Creative ROAS

### Intelligence

* AI insights
* Anomalies
* Opportunities
* Risks
* Forecasts
* Recommendations

---

## 10. AI Recommendation Interface

Each recommendation shall contain:

```text
Recommendation ID
Recommendation Type
Entity
Current Performance
Target Performance
Recommended Action
Expected Impact
Confidence
Risk
Evidence
Created At
Approval Status
Execution Status
```

---

## 11. Non-Functional Requirements

## NFR-001 — Scalability

The system shall support:

* Multi-tenant workloads
* Large advertising datasets
* High-frequency analytics
* Concurrent AI queries
* Large campaign inventories

The architecture shall scale horizontally.

---

## NFR-002 — Availability

Critical advertising analytics services should target enterprise-grade availability.

---

## NFR-003 — Performance

Standard dashboard queries should return within an acceptable low-latency SLA under normal workload.

Frequently accessed metrics shall support caching and pre-aggregation.

---

## NFR-004 — Reliability

The system shall provide:

* Retry mechanisms
* Idempotency
* Dead-letter queues
* Failure recovery
* Data reconciliation
* Integration health monitoring

---

## NFR-005 — Security

The platform shall implement:

* Encryption in transit
* Encryption at rest
* RBAC
* MFA
* OAuth
* Tenant isolation
* Secrets management
* Audit logging
* Rate limiting

---

## NFR-006 — Privacy

The platform shall minimize unnecessary storage of customer data and apply organization-level access policies.

---

## NFR-007 — Explainability

AI-generated business decisions shall be traceable to source metrics.

---

## NFR-008 — Observability

The platform shall expose:

* Logs
* Metrics
* Traces
* Integration health
* AI performance metrics
* Data freshness metrics

---

## 12. Data Model

Core entities shall include:

```text
Tenant
Organization
Workspace
AdvertisingAccount
AdvertisingChannel
Campaign
AdGroup
AdSet
Advertisement
Creative
Audience
Product
Customer
SpendEvent
ImpressionEvent
ClickEvent
ConversionEvent
RevenueEvent
AttributionEvent
ROASMetric
ROASForecast
ROASAnomaly
ROASRecommendation
ROASScenario
BudgetAllocation
Approval
AuditEvent
```

---

## 13. Key Metrics

The system shall calculate and expose:

```text
ROAS
Revenue
Ad Spend
Profit
Contribution Margin
mROAS
CPA
CAC
CPC
CPM
CTR
CVR
Conversions
Conversion Value
Revenue per Conversion
Customer LTV
LTV:CAC
Spend Growth
Revenue Growth
ROAS Growth
ROAS Volatility
```

---

## 14. Example AI Output

For a query:

> "Why did our ROAS decline this week?"

The AI should return a structured analysis such as:

```text
ROAS declined from 4.8x to 3.6x.

Primary contributors:
1. Meta prospecting ROAS decreased by 31%.
2. Advertising spend increased by 22%.
3. Conversion rate decreased by 14%.
4. Two high-performing creatives showed performance fatigue.
5. Revenue growth did not keep pace with spend growth.

Recommended actions:
1. Reduce budget on the lowest-performing prospecting campaign.
2. Shift a portion of budget toward the highest-mROAS campaign.
3. Test new creative variants.
4. Monitor conversion tracking for the affected campaign.

Confidence: High
Risk: Medium
```

---

## 15. Example Optimization Workflow

```text
Advertising Data
        ↓
Data Validation
        ↓
Data Normalization
        ↓
Attribution Processing
        ↓
ROAS Calculation
        ↓
Historical Analysis
        ↓
Anomaly Detection
        ↓
Forecasting
        ↓
Marginal ROAS Analysis
        ↓
AI Recommendation
        ↓
Policy Validation
        ↓
Human Approval / Autonomous Execution
        ↓
Advertising Platform
        ↓
Post-Execution Monitoring
        ↓
ROAS Impact Measurement
        ↓
Feedback Loop
```

---

## 16. Success Criteria

The module shall be considered successful when users can reliably:

* Connect advertising platforms.
* Consolidate advertising data.
* Calculate ROAS consistently.
* Analyze ROAS across multiple dimensions.
* Identify high-performing campaigns.
* Identify inefficient spending.
* Detect ROAS anomalies.
* Explain ROAS changes.
* Forecast future ROAS.
* Simulate budget changes.
* Receive AI optimization recommendations.
* Approve or reject recommendations.
* Automate approved optimization actions.
* Measure post-optimization impact.
* Generate executive reports.

---

## 17. Enterprise-Level Acceptance Criteria

## AC-001

Given valid advertising spend and attributed revenue, the system shall calculate ROAS deterministically according to the configured ROAS definition.

## AC-002

Given multiple advertising providers, the system shall normalize their performance data into a common analytical model.

## AC-003

Given a material ROAS decline, the AI shall identify statistically and economically relevant contributing factors when sufficient data exists.

## AC-004

Given insufficient evidence, the AI shall explicitly identify uncertainty rather than fabricate an explanation.

## AC-005

Given an optimization opportunity, the AI shall provide a recommendation with evidence, expected impact, confidence, and risk.

## AC-006

Given an organization configured for human approval, no AI-generated advertising action shall execute before authorized approval.

## AC-007

Given autonomous optimization is enabled, every automated change shall pass configured policy and budget guardrails.

## AC-008

Every recommendation and automated action shall be auditable.

## AC-009

All ROAS calculations shall be reproducible from versioned metric definitions, attribution rules, and source data.

## AC-010

All analytics and AI outputs shall respect tenant isolation and RBAC permissions.

---

## 18. Strategic Product Principle

SalesGenie's Ad ROAS Analysis should not function as a passive reporting dashboard.

It should operate as an **AI-powered advertising intelligence and optimization system**:

```text
Measure
   ↓
Understand
   ↓
Diagnose
   ↓
Predict
   ↓
Simulate
   ↓
Recommend
   ↓
Approve
   ↓
Execute
   ↓
Monitor
   ↓
Learn
   ↓
Optimize
```

The ultimate objective is not merely to report a higher ROAS number.

The objective is to help customers **allocate advertising capital toward the highest sustainable incremental business value while controlling financial, attribution, operational, and automation risk.**
