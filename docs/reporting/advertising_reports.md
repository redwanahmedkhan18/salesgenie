# SalesGenie — Advertising Reports

## FAANG-Level User Requirements, System Requirements & Functional Requirements

> **Module:** Advertising Reports & Intelligence
> **Platform:** SalesGenie
> **Operating Model:** AI + Human Collaboration
> **Architecture:** Enterprise Multi-Tenant SaaS + Microservices + Event-Driven + Multi-Agent AI
> **Primary Objective:** Provide a unified advertising intelligence and reporting platform that converts multi-channel advertising data into accurate performance analysis, business insights, forecasts, recommendations, and human-governed optimization decisions.

---

## 1. Module Overview

The SalesGenie Advertising Reports module shall provide a centralized advertising intelligence layer for collecting, normalizing, analyzing, explaining, forecasting, and reporting paid advertising performance across multiple advertising platforms.

The module shall support advertising data from:

- Google Ads
- Facebook Ads
- Instagram Ads
- LinkedIn Ads
- TikTok Ads
- YouTube Ads
- WhatsApp Ads
- Other supported advertising providers
- CRM systems
- E-commerce systems
- Sales systems
- Analytics systems
- SalesGenie campaign data
- SalesGenie lead data
- SalesGenie conversion data
- SalesGenie revenue data

The system shall transform advertising data into:

1. Advertising performance reports
2. Campaign reports
3. Ad-set reports
4. Ad reports
5. Platform comparison reports
6. Spend reports
7. Revenue reports
8. ROI reports
9. ROAS reports
10. Conversion reports
11. Audience reports
12. Demographic reports
13. Product advertising reports
14. Attribution reports
15. Budget reports
16. Creative performance reports
17. Funnel reports
18. Forecasting reports
19. Executive reports
20. AI-generated advertising intelligence
21. AI-generated recommendations
22. Human-reviewed optimization decisions

The system shall clearly distinguish:

- Source facts
- Calculated metrics
- Statistical analysis
- AI interpretation
- AI prediction
- AI recommendation
- Human decision
- Human override
- External data
- Estimated data
- Incomplete data

---

## 2. Core Objectives

The Advertising Reports module shall:

- Centralize advertising intelligence.
- Eliminate fragmented advertising reporting.
- Provide cross-platform campaign visibility.
- Connect advertising spend to business outcomes.
- Connect advertising activity to leads and revenue.
- Detect campaign anomalies.
- Explain performance changes.
- Identify inefficient spending.
- Identify profitable campaigns.
- Identify high-value audiences.
- Identify high-performing products.
- Forecast advertising outcomes.
- Recommend budget allocation.
- Provide executive-level intelligence.
- Support AI-assisted decision making.
- Maintain human control over consequential decisions.

---

## 3. User Roles

## 3.1 Super Admin

The Super Admin shall be able to:

- Configure global advertising reporting capabilities.
- Configure supported advertising providers.
- Configure provider credentials and integrations.
- Configure AI models.
- Configure AI model routing.
- Configure report templates.
- Configure global KPI definitions.
- Configure system-wide reporting policies.
- Monitor tenant advertising usage.
- Monitor report generation.
- Monitor AI usage and cost.
- Monitor provider health.
- Configure feature flags.
- Configure data retention.
- Review system-wide audit logs.
- Configure global rate limits.
- Configure provider failover.
- Manage platform-wide advertising analytics settings.

---

## 3.2 Workplace Admin

The Workplace Admin shall be able to:

- Manage advertising reporting across the workplace.
- Create advertising projects.
- Manage organizations.
- Configure shared advertising data sources.
- Configure report templates.
- Assign advertising projects.
- Manage team permissions.
- Review organizational advertising performance.
- Approve high-impact AI recommendations.
- Manage report distribution.
- Monitor advertising budgets.

---

## 3.3 Organization Admin

The Organization Admin shall be able to:

- Connect advertising platforms.
- Create advertising projects.
- Add advertising accounts.
- Configure campaigns.
- Configure reporting periods.
- Configure advertising KPIs.
- Configure business goals.
- Configure conversion goals.
- Configure revenue goals.
- Configure report schedules.
- Configure recipients.
- Configure dashboards.
- Review AI-generated insights.
- Approve or reject AI recommendations.
- Export advertising reports.
- Configure alerts.

---

## 3.4 Marketing Manager

The Marketing Manager shall be able to:

- Monitor advertising performance.
- Compare campaigns.
- Compare advertising platforms.
- Analyze spend.
- Analyze revenue.
- Analyze ROI.
- Analyze ROAS.
- Analyze conversions.
- Analyze audiences.
- Analyze demographics.
- Analyze products.
- Analyze creatives.
- Review AI insights.
- Review AI recommendations.
- Generate marketing reports.
- Monitor campaign risks.
- Monitor budget utilization.

---

## 3.5 Advertising Specialist

The Advertising Specialist shall be able to:

- Analyze campaign performance.
- Analyze ad-set performance.
- Analyze individual ads.
- Analyze targeting.
- Analyze audience performance.
- Analyze creative performance.
- Analyze conversion funnels.
- Analyze attribution.
- Identify inefficient campaigns.
- Identify scaling opportunities.
- Review AI recommendations.
- Override AI recommendations.
- Create custom reports.
- Assign optimization tasks.

---

## 3.6 Sales Agent

The Sales Agent shall be able to:

- View advertising-generated leads.
- View campaign-generated opportunities.
- View advertising-attributed customers.
- View advertising-attributed revenue.
- Identify high-value lead sources.
- Access approved campaign reports.
- Understand advertising contribution to sales.

---

## 3.7 Support Agent

The Support Agent shall be able to:

- View authorized advertising reports.
- Investigate report-generation problems.
- Investigate advertising integration problems.
- View data synchronization status.
- Escalate advertising data issues.

---

## 3.8 End User / Client

The End User shall be able to:

- View authorized advertising dashboards.
- View advertising reports.
- View campaign performance.
- View advertising spend.
- View revenue.
- View ROAS.
- View ROI.
- View conversion metrics.
- Review AI insights.
- Review recommendations.
- Download reports.
- Receive scheduled reports.
- Share approved reports.

---

## 4. User Requirements

## UR-001 — Advertising Project Management

The system shall allow authorized users to create and manage advertising projects.

Each project shall support:

- Project name
- Business name
- Website
- Industry
- Target market
- Target countries
- Target regions
- Target cities
- Target audience
- Business objectives
- Advertising objectives
- Revenue objectives
- Conversion objectives
- Budget
- Currency
- Advertising platforms
- Reporting frequency
- KPI configuration
- Project owners

---

## UR-002 — Advertising Account Management

Users shall be able to:

- Connect advertising accounts.
- Disconnect accounts.
- Reauthorize accounts.
- View connection status.
- View account identifiers.
- View account currency.
- View account timezone.
- View last synchronization.
- View synchronization failures.
- View provider quotas.
- Configure synchronization schedules.

---

## UR-003 — Multi-Platform Advertising Reporting

The system shall provide a unified reporting interface across advertising platforms.

Users shall be able to compare:

- Google Ads
- Facebook Ads
- Instagram Ads
- LinkedIn Ads
- TikTok Ads
- YouTube Ads
- WhatsApp Ads
- Other supported providers

---

## UR-004 — Advertising Executive Dashboard

The dashboard shall display:

- Total advertising spend
- Total impressions
- Total reach
- Total clicks
- CTR
- CPC
- CPM
- Conversions
- Conversion rate
- CPA
- Revenue
- ROAS
- ROI
- Profit contribution
- Cost per lead
- Cost per customer
- Campaign count
- Active campaigns
- Paused campaigns
- Budget utilization
- Forecast
- AI opportunity score
- Advertising health score

---

## UR-005 — Campaign Reporting

Users shall be able to analyze:

- Campaign spend
- Campaign impressions
- Campaign reach
- Campaign clicks
- CTR
- CPC
- CPM
- Conversions
- Conversion rate
- CPA
- Revenue
- ROAS
- ROI
- Profit
- Campaign status
- Budget utilization
- Performance trends

---

## UR-006 — Ad Set Reporting

Users shall be able to compare ad sets based on:

- Spend
- Reach
- Impressions
- Frequency
- Clicks
- CTR
- CPC
- CPM
- Conversions
- CPA
- Revenue
- ROAS
- ROI
- Audience
- Placement
- Device
- Geography

---

## UR-007 — Individual Ad Reporting

Users shall be able to analyze:

- Ad spend
- Impressions
- Reach
- Clicks
- CTR
- CPC
- CPM
- Engagement
- Video views
- Conversion
- CPA
- Revenue
- ROAS
- ROI
- Creative type
- Creative version
- Headline
- Copy
- CTA
- Landing page

---

## UR-008 — Platform Comparison

The system shall compare advertising platforms using:

- Spend
- Reach
- Impressions
- Clicks
- CTR
- CPC
- CPM
- Conversions
- CPA
- Revenue
- ROAS
- ROI
- Profit
- Customer acquisition cost
- Lead quality
- Customer value

---

## UR-009 — Advertising Spend Reporting

Users shall be able to analyze:

- Total spend
- Spend by platform
- Spend by campaign
- Spend by ad set
- Spend by ad
- Spend by product
- Spend by audience
- Spend by geography
- Spend by device
- Spend by date
- Spend by objective

---

## UR-010 — Revenue Reporting

The system shall report:

- Advertising-attributed revenue
- Revenue by platform
- Revenue by campaign
- Revenue by ad set
- Revenue by ad
- Revenue by product
- Revenue by audience
- Revenue by geography
- Revenue by customer segment

---

## UR-011 — ROI Reporting

The system shall calculate advertising ROI using configurable business definitions.

The system shall support:

- Campaign ROI
- Platform ROI
- Product ROI
- Audience ROI
- Channel ROI
- Customer ROI
- Overall advertising ROI

---

## UR-012 — ROAS Reporting

The system shall calculate:

```text
ROAS = Attributed Revenue / Advertising Spend
```

Users shall be able to view:

* Overall ROAS
* Platform ROAS
* Campaign ROAS
* Ad-set ROAS
* Ad ROAS
* Product ROAS
* Audience ROAS
* Geographic ROAS
* Time-period ROAS

---

## UR-013 — Conversion Reporting

The system shall report:

* Impressions
* Clicks
* Leads
* Qualified leads
* Opportunities
* Customers
* Purchases
* Revenue
* Conversion rate
* Cost per conversion
* Cost per lead
* Cost per customer

---

## UR-014 — Funnel Reporting

The system shall visualize:

```text
Impression
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
```

Users shall be able to identify funnel drop-off points.

---

## UR-015 — Audience Reporting

Users shall be able to analyze:

* Audience segments
* Audience size
* Reach
* Frequency
* Engagement
* CTR
* CPC
* Conversion rate
* CPA
* Revenue
* ROAS
* ROI
* Customer value

---

## UR-016 — Demographic Reporting

Where supported by source data, reports shall include:

* Age
* Gender
* Location
* Device
* Language
* Household characteristics
* Job-related attributes
* Industry
* Seniority
* Education
* Other provider-supported demographic attributes

The system shall respect platform privacy restrictions.

---

## UR-017 — Geographic Reporting

Users shall be able to analyze:

* Country
* Region
* State/province
* City
* Postal region where available

Metrics shall include:

* Spend
* Reach
* Clicks
* Conversions
* CPA
* Revenue
* ROAS
* ROI

---

## UR-018 — Product Advertising Reporting

Users shall be able to evaluate:

* Product advertising spend
* Product revenue
* Product conversions
* Product ROAS
* Product ROI
* Product CPA
* Product margin
* Product profitability
* Product demand
* Product advertising contribution

---

## UR-019 — Creative Reporting

Users shall be able to compare creatives using:

* Impressions
* Reach
* Engagement
* CTR
* CPC
* Video completion
* Conversion rate
* CPA
* Revenue
* ROAS
* ROI

---

## UR-020 — Attribution Reporting

Users shall be able to analyze advertising contribution using configurable attribution models.

Supported models shall include:

* First-touch
* Last-touch
* Linear
* Position-based
* Time-decay
* Data-driven where supported
* Custom attribution

---

## UR-021 — AI Advertising Insights

The AI shall identify:

* Winning campaigns
* Losing campaigns
* Spend inefficiencies
* Performance anomalies
* Scaling opportunities
* Audience opportunities
* Creative opportunities
* Platform opportunities
* Geographic opportunities
* Product opportunities
* Budget risks
* Conversion bottlenecks
* Revenue opportunities

---

## UR-022 — AI Root-Cause Analysis

When performance changes materially, AI shall investigate:

* Spend changes
* Audience changes
* Creative changes
* Budget changes
* Bid changes
* Platform changes
* Conversion changes
* Landing page changes
* Seasonal effects
* Market changes
* Attribution changes
* Tracking problems

---

## UR-023 — AI Recommendations

AI shall generate recommendations including:

* Increase budget
* Decrease budget
* Pause campaign
* Scale campaign
* Reallocate budget
* Change targeting
* Change creative
* Change bidding strategy
* Change platform allocation
* Improve landing page
* Improve conversion funnel
* Investigate tracking
* Improve audience segmentation

Each recommendation shall contain:

* Recommendation
* Evidence
* Expected impact
* Confidence
* Cost
* Risk
* Effort
* Priority
* Dependencies
* Recommended owner

---

## UR-024 — Human Review

Authorized users shall be able to:

* Approve AI recommendations.
* Reject AI recommendations.
* Edit recommendations.
* Change priorities.
* Assign recommendations.
* Add comments.
* Override AI decisions.
* Mark actions as completed.
* Reopen actions.

---

## UR-025 — AI-Human Collaboration

The system shall support:

```text
AI Detects Problem
        ↓
AI Investigates
        ↓
AI Explains
        ↓
AI Recommends
        ↓
Human Reviews
        ↓
Human Approves / Rejects / Edits
        ↓
Action Executed
        ↓
Performance Measured
        ↓
AI Evaluates Outcome
```

---

## UR-026 — Advertising Forecasting

Users shall receive forecasts for:

* Spend
* Impressions
* Clicks
* Conversions
* CPA
* Revenue
* ROAS
* ROI
* Customer acquisition
* Budget utilization

Forecasts shall provide:

* Forecast period
* Expected value
* Confidence interval
* Confidence score
* Assumptions
* Risk factors

---

## UR-027 — Budget Reporting

Users shall be able to monitor:

* Allocated budget
* Actual spend
* Remaining budget
* Budget utilization
* Daily burn rate
* Monthly burn rate
* Forecast spend
* Projected overspend
* Projected underspend

---

## UR-028 — Executive Advertising Report

The executive report shall summarize:

* Advertising health
* Spend
* Revenue
* ROAS
* ROI
* Conversion performance
* Top campaigns
* Worst campaigns
* Major risks
* Major opportunities
* Forecast
* AI recommendations
* Human decisions

---

## UR-029 — Custom Reports

Users shall be able to configure:

* Metrics
* Dimensions
* Filters
* Date ranges
* Charts
* Tables
* Comparisons
* AI summaries
* Branding
* Report sections

---

## UR-030 — Scheduled Reports

Users shall be able to schedule:

* Daily reports
* Weekly reports
* Monthly reports
* Quarterly reports
* Annual reports
* Custom reports

---

## UR-031 — Report Distribution

Reports shall support distribution through authorized channels including:

* Email
* Dashboard
* Download
* API
* Webhook
* Approved communication integrations

---

## UR-032 — Report Export

Reports shall support:

* PDF
* CSV
* XLSX
* JSON
* HTML
* Markdown

---

## 5. System Requirements

## SR-001 — Multi-Tenant Architecture

The advertising reporting system shall enforce strict isolation between:

* Tenants
* Workspaces
* Organizations
* Advertising projects
* Advertising accounts
* Reports
* AI insights
* Recommendations

No tenant shall access another tenant's advertising data.

---

## SR-002 — Identity and Access Management

The system shall support:

* OAuth2
* OIDC
* SSO
* MFA
* RBAC
* Fine-grained permissions
* API authentication
* Service-to-service authentication
* Session management

---

## SR-003 — Permission Hierarchy

The permission model shall support:

```text
Tenant
 └── Workspace
      └── Organization
           └── Advertising Project
                ├── Advertising Accounts
                ├── Campaigns
                ├── Ad Sets
                ├── Ads
                ├── Audiences
                ├── Products
                ├── Reports
                ├── AI Insights
                └── Recommendations
```

---

## SR-004 — Advertising Data Model

The system shall maintain normalized entities for:

* Advertising accounts
* Platforms
* Campaigns
* Ad sets
* Ads
* Creatives
* Audiences
* Demographics
* Placements
* Keywords
* Products
* Spend
* Impressions
* Reach
* Clicks
* Conversions
* Revenue
* Customers
* Attribution
* Reports
* AI insights
* Recommendations
* Forecasts
* Budgets
* Alerts
* Audit events

---

## SR-005 — Data Warehouse

The advertising analytics platform shall use analytical storage optimized for:

* Time-series analysis
* Campaign aggregation
* Cross-platform comparison
* Historical reporting
* Cohort analysis
* Attribution
* Forecasting
* Large-scale dashboards

---

## SR-006 — Data Synchronization

The system shall support:

* Initial synchronization
* Incremental synchronization
* Scheduled synchronization
* Event-driven synchronization
* Retry
* Backoff
* Deduplication
* Idempotency
* Data validation
* Provider failover

---

## SR-007 — Data Freshness

Every advertising metric shall maintain:

* Source timestamp
* Collection timestamp
* Processing timestamp
* Last successful synchronization
* Data freshness status

---

## SR-008 — Data Provenance

Advertising metrics shall be traceable through:

```text
Advertising Provider
        ↓
Account
        ↓
Campaign
        ↓
Ad Set
        ↓
Ad
        ↓
Metric
        ↓
Calculation
        ↓
AI Analysis
        ↓
Recommendation
```

---

## SR-009 — AI Architecture

The system shall support:

* LLM reasoning
* Structured output
* Function calling
* Tool calling
* RAG
* Multi-agent workflows
* Prompt versioning
* Model routing
* Model fallback
* AI evaluation
* Confidence scoring
* Guardrails

---

## SR-010 — Advertising AI Agents

The platform shall support specialized agents:

```text
Advertising Orchestrator Agent
        |
        ├── Advertising Reporting Agent
        ├── Campaign Intelligence Agent
        ├── Ad Intelligence Agent
        ├── Audience Intelligence Agent
        ├── Demographic Intelligence Agent
        ├── Creative Intelligence Agent
        ├── Conversion Intelligence Agent
        ├── Attribution Intelligence Agent
        ├── Spend Analytics Agent
        ├── Revenue Analytics Agent
        ├── ROI Agent
        ├── ROAS Agent
        ├── Budget Intelligence Agent
        ├── Forecasting Agent
        └── Recommendation Agent
```

---

## SR-011 — AI Orchestration

The orchestrator shall:

* Understand the reporting request.
* Decompose complex tasks.
* Select appropriate agents.
* Select appropriate tools.
* Manage execution state.
* Validate agent outputs.
* Resolve conflicts.
* Merge results.
* Calculate confidence.
* Generate final intelligence.

---

## SR-012 — MCP Integration

The platform shall support controlled MCP access to:

* Advertising platforms
* Analytics systems
* CRM
* E-commerce
* Revenue systems
* Reporting systems
* Internal SalesGenie services

Every MCP tool shall have:

* Tool ID
* Permission scope
* Input schema
* Output schema
* Timeout
* Rate limit
* Audit logging
* Approval policy

---

## SR-013 — AI Safety

The AI system shall prevent:

* Unauthorized advertising account access
* Cross-tenant data access
* Unauthorized campaign modifications
* Unauthorized budget changes
* Unauthorized external actions
* Secret exposure
* Prompt injection
* Indirect prompt injection
* Infinite tool loops
* Excessive API usage
* Excessive AI cost

---

## SR-014 — Human Approval Policy

Human approval shall be configurable for:

* Budget modifications
* Campaign pausing
* Campaign activation
* Large budget increases
* Large budget decreases
* Targeting changes
* Bid changes
* External advertising actions
* Bulk changes
* High-cost AI workflows

---

## SR-015 — Report Generation Pipeline

Advertising reports shall be generated asynchronously.

```text
Report Request
      ↓
Authorization
      ↓
Job Creation
      ↓
Data Retrieval
      ↓
Data Validation
      ↓
Metric Calculation
      ↓
Statistical Analysis
      ↓
AI Analysis
      ↓
Insight Generation
      ↓
Recommendation Generation
      ↓
Validation
      ↓
Report Rendering
      ↓
Storage
      ↓
Distribution
```

---

## SR-016 — Report Versioning

Each report shall maintain:

* Report ID
* Version
* Template version
* Data period
* Data source versions
* Calculation version
* AI model
* Prompt version
* Generation timestamp

---

## SR-017 — Report Reproducibility

Historical reports shall be reproducible using:

* Historical data snapshots
* Calculation versions
* Report template versions
* AI prompt versions
* Model versions
* Configuration snapshots

---

## SR-018 — Performance

The system shall use:

* Caching
* Query optimization
* Batch processing
* Pre-aggregated metrics
* Asynchronous jobs
* Distributed workers
* Connection pooling
* Pagination

---

## SR-019 — Reliability

The platform shall support:

* Retries
* Exponential backoff
* Circuit breakers
* Dead-letter queues
* Provider failover
* Graceful degradation
* Job replay
* Idempotency
* Failure recovery

---

## SR-020 — Observability

The system shall expose:

* API latency
* API errors
* Provider latency
* Provider failures
* Synchronization status
* Report generation latency
* Report failures
* AI latency
* AI error rate
* Token usage
* AI cost
* Tool usage
* Queue depth
* Worker health

---

## SR-021 — Distributed Tracing

Tracing shall cover:

```text
User Request
→ API Gateway
→ Advertising Service
→ Provider API
→ Data Pipeline
→ Queue
→ Worker
→ AI Agent
→ MCP Tool
→ Analytics Database
→ Report Renderer
→ Notification Service
```

---

## SR-022 — Security

The system shall implement:

* Encryption in transit
* Encryption at rest
* Secret management
* Token rotation
* Least privilege
* Server-side authorization
* API rate limiting
* Input validation
* Output validation
* Secure exports
* Audit logging

---

## SR-023 — Privacy

The system shall support:

* Data minimization
* Data retention policies
* Data deletion
* Data export
* Consent management
* Provider privacy controls
* Tenant-level privacy isolation

---

## SR-024 — Scalability

The following components shall scale independently:

* Advertising APIs
* Data ingestion
* Analytics workers
* AI workers
* Report workers
* Forecasting workers
* Export workers
* Notification workers

---

## 6. Functional Requirements

## FR-001 — Advertising Project Creation

The system shall allow authorized users to create advertising projects.

Required fields:

```text
project_name
business_name
website
industry
target_market
business_objective
advertising_objective
currency
timezone
```

Optional fields:

```text
monthly_budget
annual_budget
conversion_goals
revenue_goals
target_audience
target_locations
products
competitors
report_schedule
```

---

## FR-002 — Advertising Account Connection

The system shall:

1. Allow provider selection.
2. Authenticate the user.
3. Request required permissions.
4. Validate account access.
5. Store secure credentials/tokens.
6. Retrieve account metadata.
7. Start synchronization.
8. Display connection health.

---

## FR-003 — Campaign Synchronization

The system shall synchronize:

* Campaigns
* Ad sets
* Ads
* Creatives
* Audiences
* Budgets
* Targeting
* Placements
* Performance metrics

---

## FR-004 — Data Normalization

The system shall normalize provider-specific metrics into a unified SalesGenie schema.

Example:

```text
Provider-specific metric
        ↓
Normalization Layer
        ↓
SalesGenie Canonical Metric
```

---

## FR-005 — Advertising KPI Calculation

The system shall calculate:

### Spend Metrics

* Total spend
* Daily spend
* Monthly spend
* Spend growth
* Spend distribution

### Traffic Metrics

* Impressions
* Reach
* Clicks
* CTR
* CPC
* CPM

### Conversion Metrics

* Leads
* Qualified leads
* Opportunities
* Customers
* Conversions
* Conversion rate
* CPA

### Financial Metrics

* Revenue
* ROAS
* ROI
* Profit contribution
* CAC
* Revenue per customer

---

## FR-006 — Historical Comparison

The system shall support:

* Day-over-day
* Week-over-week
* Month-over-month
* Quarter-over-quarter
* Year-over-year
* Custom-period comparisons

---

## FR-007 — Campaign Ranking

The system shall rank campaigns according to configurable metrics.

Examples:

* Highest ROAS
* Highest ROI
* Lowest CPA
* Highest revenue
* Highest conversion rate
* Highest profit
* Highest growth
* Lowest efficiency

---

## FR-008 — Campaign Performance Classification

Campaigns shall be classified using configurable rules:

```text
Excellent
Strong
Healthy
Average
Underperforming
Critical
```

Classification shall be explainable.

---

## FR-009 — Campaign Trend Detection

The system shall identify:

* Growth
* Decline
* Stability
* Volatility
* Sudden changes
* Sustained changes

---

## FR-010 — Ad Set Analysis

The system shall compare ad sets using:

* Spend
* Audience
* Placement
* Device
* Geography
* CTR
* CPC
* CPM
* Conversion
* CPA
* Revenue
* ROAS
* ROI

---

## FR-011 — Individual Ad Analysis

The system shall compare ads using:

* Creative
* Copy
* Headline
* CTA
* Format
* Impressions
* Reach
* Engagement
* CTR
* CPC
* Conversion
* CPA
* Revenue
* ROAS

---

## FR-012 — Creative Fatigue Detection

The AI shall detect potential creative fatigue using signals such as:

* Declining CTR
* Increasing CPC
* Increasing CPA
* Increasing frequency
* Declining conversion rate
* Declining engagement

The system shall explain the evidence behind the detection.

---

## FR-013 — Audience Performance Analysis

The system shall rank audiences based on:

* Spend
* CTR
* CPC
* Conversion rate
* CPA
* Revenue
* ROAS
* ROI
* Customer value

---

## FR-014 — Demographic Analysis

The system shall analyze provider-supported demographic data.

The system shall identify:

* Best-performing demographics
* Worst-performing demographics
* High-cost demographics
* High-conversion demographics
* High-revenue demographics
* Demographic trends

---

## FR-015 — Geographic Analysis

The system shall identify:

* High-performing regions
* Low-performing regions
* High-cost regions
* High-ROAS regions
* High-revenue regions
* Geographic growth opportunities

---

## FR-016 — Placement Analysis

Where provider data supports it, the system shall analyze:

* Placement
* Device
* Network
* Position
* Spend
* CTR
* CPC
* Conversion
* CPA
* ROAS
* ROI

---

## FR-017 — Product Advertising Analysis

The system shall calculate:

```text
Product Ad Spend
Product Revenue
Product Conversions
Product CPA
Product ROAS
Product ROI
Product Profit
```

---

## FR-018 — Cross-Platform Comparison

The system shall compare platforms using normalized metrics.

Example:

```text
Google Ads
Facebook Ads
Instagram Ads
LinkedIn Ads
TikTok Ads
YouTube Ads
WhatsApp Ads
```

Comparison shall account for:

* Currency
* Attribution differences
* Metric definitions
* Reporting windows
* Data freshness

---

## FR-019 — Spend Analysis

The system shall identify:

* Spending trends
* Overspending
* Underspending
* Budget leakage
* Inefficient campaigns
* High-cost audiences
* High-cost platforms
* High-cost geographies

---

## FR-020 — Revenue Analysis

The system shall calculate:

* Advertising revenue
* Revenue growth
* Revenue by platform
* Revenue by campaign
* Revenue by product
* Revenue by audience
* Revenue by geography
* Revenue by customer

---

## FR-021 — ROI Analysis

The system shall calculate:

```text
ROI =
(Net Advertising Profit / Advertising Cost) × 100
```

The exact financial definition shall be configurable by organization.

---

## FR-022 — ROAS Analysis

The system shall calculate:

```text
ROAS =
Attributed Revenue / Advertising Spend
```

The system shall support:

* Gross ROAS
* Net ROAS
* Campaign ROAS
* Platform ROAS
* Product ROAS
* Audience ROAS

where required business data is available.

---

## FR-023 — Conversion Analysis

The system shall identify:

* Conversion rate changes
* Conversion volume changes
* CPA changes
* Conversion bottlenecks
* Campaign conversion leaders
* Campaign conversion laggards

---

## FR-024 — Attribution Analysis

The system shall calculate advertising contribution according to configured attribution models.

Each report shall identify:

* Attribution model
* Attribution window
* Source data
* Limitations
* Revenue attributed

---

## FR-025 — AI Anomaly Detection

The AI shall detect anomalies involving:

* Spend
* Impressions
* Reach
* Clicks
* CTR
* CPC
* CPM
* Conversions
* CPA
* Revenue
* ROAS
* ROI

---

## FR-026 — AI Root-Cause Investigation

When an anomaly is detected, AI shall investigate related dimensions.

Example:

```text
ROAS ↓ 28%
      ↓
Conversion Rate ↓
      ↓
CPA ↑
      ↓
Audience Segment B deteriorated
      ↓
Creative Version 4 underperformed
      ↓
Landing Page Conversion ↓
      ↓
Potential Root Cause
```

The AI shall label conclusions as:

```text
Observed
Calculated
Likely
Possible
Unknown
```

---

## FR-027 — AI Opportunity Detection

The AI shall identify opportunities such as:

* Scale high-ROAS campaigns
* Reduce inefficient spend
* Reallocate budget
* Expand high-value audiences
* Retarget high-value users
* Improve creatives
* Improve landing pages
* Expand high-performing regions
* Reduce low-performing placements

---

## FR-028 — AI Budget Recommendation

AI shall recommend budget allocation based on:

* Historical performance
* Marginal efficiency
* Conversion capacity
* Revenue contribution
* Forecast
* Business objectives
* Risk
* Budget constraints

---

## FR-029 — AI Campaign Recommendation

Each recommendation shall contain:

```text
recommendation_id
campaign_id
recommendation_type
reason
evidence
expected_impact
confidence
risk
estimated_effort
priority
recommended_owner
```

---

## FR-030 — Human Recommendation Review

Human users shall be able to:

```text
Approve
Reject
Edit
Defer
Assign
Comment
Override
Complete
```

---

## FR-031 — Recommendation State Machine

Recommendations shall follow:

```text
GENERATED
    ↓
REVIEW_REQUIRED
    ↓
APPROVED
    ↓
ASSIGNED
    ↓
IN_PROGRESS
    ↓
COMPLETED
    ↓
VERIFIED
```

Alternative:

```text
GENERATED
    ↓
REJECTED
```

---

## FR-032 — Outcome Measurement

After an approved optimization is implemented, the system shall compare:

```text
Before
vs
After
```

Metrics shall include:

* Spend
* CTR
* CPC
* Conversion rate
* CPA
* Revenue
* ROAS
* ROI

---

## FR-033 — AI Learning Loop

The platform shall maintain:

```text
Observation
→ Analysis
→ Recommendation
→ Human Decision
→ Execution
→ Measurement
→ Outcome
→ AI Evaluation
→ Future Recommendation
```

---

## FR-034 — Advertising Health Score

The system shall calculate an advertising health score using configurable dimensions:

```text
Campaign Efficiency
Budget Efficiency
Conversion Performance
Revenue Performance
ROAS
ROI
Audience Quality
Creative Performance
Platform Diversification
Tracking Health
```

---

## FR-035 — Advertising Risk Score

The system shall identify risks such as:

* Excessive spend
* Declining ROAS
* Increasing CPA
* Campaign volatility
* Audience saturation
* Creative fatigue
* Platform dependency
* Tracking failures
* Revenue decline

---

## FR-036 — Advertising Forecasting

The forecasting engine shall predict:

* Spend
* Impressions
* Clicks
* Conversions
* CPA
* Revenue
* ROAS
* ROI

---

## FR-037 — Scenario Modeling

Users shall be able to ask:

```text
What happens if:
- Budget increases by 20%?
- Budget decreases by 15%?
- Campaign A is paused?
- Campaign B receives additional budget?
- CPA improves by 10%?
- Conversion rate improves by 15%?
- ROAS target increases?
```

The AI shall provide estimated outcomes with assumptions and confidence.

---

## FR-038 — Budget Utilization

The system shall calculate:

```text
Allocated Budget
Actual Spend
Remaining Budget
Utilization %
Daily Burn Rate
Projected Spend
Projected Variance
```

---

## FR-039 — Budget Alerting

The system shall generate alerts when:

* Spend exceeds threshold.
* Budget utilization is unusually high.
* Budget utilization is unusually low.
* Forecasted spend exceeds budget.
* Campaign efficiency deteriorates.
* High-value campaign is underfunded.

---

## FR-040 — Executive Report Generation

The executive report shall contain:

```text
Executive Summary
Advertising Health
Spend
Revenue
ROAS
ROI
Conversions
Top Campaigns
Worst Campaigns
Platform Comparison
Audience Performance
Creative Performance
Budget Status
Major Risks
Major Opportunities
Forecast
AI Recommendations
Human Decisions
```

---

## FR-041 — Platform Report

Each advertising platform report shall contain:

```text
Platform Overview
Account Overview
Campaign Performance
Ad Set Performance
Ad Performance
Audience Performance
Spend
Conversions
Revenue
ROAS
ROI
Trends
Anomalies
AI Insights
Recommendations
```

---

## FR-042 — Campaign Report

Each campaign report shall contain:

```text
Campaign Summary
Spend
Impressions
Reach
Clicks
CTR
CPC
CPM
Conversions
CPA
Revenue
ROAS
ROI
Audience
Creative
Placement
Trend
Forecast
AI Analysis
Recommendations
```

---

## FR-043 — Spend Report

The spend report shall contain:

* Total spend
* Spend by platform
* Spend by campaign
* Spend by audience
* Spend by product
* Spend by geography
* Spend trend
* Budget utilization
* Spend forecast
* Overspend risk

---

## FR-044 — Revenue Report

The revenue report shall contain:

* Advertising revenue
* Revenue by platform
* Revenue by campaign
* Revenue by product
* Revenue by audience
* Revenue by geography
* Revenue growth
* Revenue forecast

---

## FR-045 — ROI Report

The ROI report shall contain:

* Advertising cost
* Revenue
* Profit
* ROI
* ROI by platform
* ROI by campaign
* ROI by product
* ROI by audience
* ROI trend
* ROI forecast

---

## FR-046 — ROAS Report

The ROAS report shall contain:

* Overall ROAS
* Platform ROAS
* Campaign ROAS
* Ad-set ROAS
* Ad ROAS
* Product ROAS
* Audience ROAS
* ROAS trend
* ROAS forecast

---

## FR-047 — Conversion Report

The conversion report shall contain:

* Impressions
* Clicks
* Leads
* Qualified leads
* Opportunities
* Customers
* Conversion rate
* CPA
* Revenue
* Conversion trend

---

## FR-048 — Audience Report

The audience report shall contain:

* Audience size
* Reach
* Frequency
* Spend
* CTR
* CPC
* Conversion
* CPA
* Revenue
* ROAS
* ROI
* Customer value

---

## FR-049 — Demographic Report

The demographic report shall contain provider-supported:

* Age analysis
* Gender analysis
* Geographic analysis
* Language analysis
* Professional attributes
* Device analysis
* Performance comparisons

---

## FR-050 — Product Advertising Report

The product report shall contain:

* Product spend
* Product impressions
* Product clicks
* Product conversions
* Product revenue
* Product CPA
* Product ROAS
* Product ROI
* Product profitability

---

## FR-051 — Attribution Report

The attribution report shall contain:

* Attribution model
* Attribution window
* Touchpoints
* Campaign contribution
* Platform contribution
* Revenue contribution
* Conversion contribution
* Attribution limitations

---

## FR-052 — AI Intelligence Report

The AI report shall contain:

```text
Major Findings
Performance Changes
Root Causes
Opportunities
Risks
Forecast
Recommended Actions
Expected Impact
Confidence
Evidence
```

---

## FR-053 — Custom Report Builder

Users shall be able to construct reports using:

* Metrics
* Dimensions
* Filters
* Date ranges
* Segments
* Charts
* Tables
* Comparisons
* AI narrative
* Recommendations
* Branding

---

## FR-054 — Report Scheduling

The system shall support:

```text
Daily
Weekly
Biweekly
Monthly
Quarterly
Yearly
Custom Schedule
```

---

## FR-055 — Report Distribution

The system shall record:

* Recipient
* Channel
* Report ID
* Version
* Delivery time
* Delivery status
* Failure reason
* Retry count

---

## FR-056 — Report Comparison

Users shall be able to compare reports across:

* Time periods
* Platforms
* Campaigns
* Products
* Audiences
* Geographies

The system shall identify:

* Improvements
* Declines
* New risks
* Resolved problems
* New opportunities

---

## FR-057 — AI Narrative Generation

The AI shall convert advertising data into business-oriented narratives.

AI narratives shall be:

* Evidence-based
* Numerically consistent
* Concise
* Explainable
* Confidence-aware
* Grounded in source data

---

## FR-058 — Fact and Inference Separation

Every AI report shall distinguish:

```text
Observed Fact
Calculated Metric
AI Interpretation
Hypothesis
Prediction
Recommendation
```

---

## FR-059 — AI Confidence

AI findings shall include:

```text
Very High
High
Medium
Low
Very Low
```

Confidence shall reflect evidence quality and uncertainty.

---

## FR-060 — AI Hallucination Prevention

The system shall validate:

* Numerical claims
* Campaign identifiers
* Platform identifiers
* Spend values
* Revenue values
* Conversion values
* ROAS
* ROI
* Forecasts
* Recommendations

The AI shall never fabricate missing advertising data.

---

## FR-061 — Missing Data Handling

Reports shall explicitly identify:

```text
Complete
Partially Complete
Data Delayed
Data Unavailable
Provider Error
Tracking Error
```

The system shall never silently replace unavailable values with fabricated values.

---

## FR-062 — Data Quality Validation

The system shall detect:

* Duplicate records
* Missing records
* Invalid timestamps
* Invalid campaign IDs
* Currency inconsistencies
* Attribution discrepancies
* Impossible metric combinations
* Unexpected metric discontinuities
* Provider inconsistencies

---

## FR-063 — Advertising Benchmarking

The system shall support benchmarking against:

* Historical performance
* Internal targets
* Campaign targets
* Platform benchmarks
* Industry benchmarks where valid data is available

Benchmark sources shall be identified.

---

## FR-064 — Advertising Opportunity Scoring

The platform shall score opportunities using configurable dimensions:

```text
Expected Revenue Impact
+
Expected Conversion Impact
+
Expected Efficiency Gain
+
Confidence
+
Strategic Importance
-
Effort
-
Risk
```

---

## FR-065 — AI Cost Tracking

The platform shall track:

* AI input tokens
* AI output tokens
* Model usage
* Tool usage
* Provider API usage
* AI cost
* Cost per report
* Cost per insight
* Cost per tenant
* Cost per project

---

## FR-066 — Prompt Versioning

The system shall maintain:

```text
prompt_id
prompt_version
model
configuration
created_at
updated_at
evaluation_score
```

---

## FR-067 — AI Model Routing

The system shall route AI workloads according to:

* Task complexity
* Accuracy requirements
* Latency requirements
* Cost
* Data sensitivity
* Availability

---

## FR-068 — AI Evaluation

AI outputs shall be evaluated for:

* Factual accuracy
* Numerical accuracy
* Groundedness
* Recommendation quality
* Completeness
* Consistency
* Hallucination rate
* Tool-use correctness

---

## FR-069 — Audit Logging

The system shall log:

* Report creation
* Report generation
* Report export
* Report sharing
* Account connection
* Account disconnection
* Synchronization
* AI analysis
* AI recommendation
* Recommendation approval
* Recommendation rejection
* Human override
* Configuration changes

---

## FR-070 — Audit Event Schema

Each audit event shall contain:

```text
event_id
tenant_id
workspace_id
organization_id
user_id
actor_type
action
resource_type
resource_id
timestamp
ip_address
user_agent
metadata
```

Sensitive information shall be redacted.

---

## FR-071 — Alerts

The platform shall generate alerts for:

* Spend spikes
* Revenue drops
* ROAS drops
* ROI drops
* CPA increases
* Conversion drops
* Budget exhaustion
* Budget overspending
* Campaign anomalies
* Platform failures
* Data synchronization failures
* Tracking failures

---

## FR-072 — Configurable Alerts

Users shall be able to configure rules such as:

```text
ROAS decrease > 20%
CPA increase > 25%
Revenue decrease > 15%
Spend increase > 30%
Conversion decrease > 20%
Budget utilization > 90%
```

---

## FR-073 — API

The advertising reporting service shall expose versioned APIs for:

```text
Advertising Projects
Advertising Accounts
Platforms
Campaigns
Ad Sets
Ads
Creatives
Audiences
Demographics
Products
Spend
Conversions
Revenue
ROI
ROAS
Attribution
Reports
Report Templates
AI Insights
Recommendations
Forecasts
Budgets
Alerts
Data Sources
```

---

## FR-074 — API Requirements

APIs shall support where applicable:

* Authentication
* Authorization
* Pagination
* Filtering
* Sorting
* Search
* Validation
* Idempotency
* Rate limiting
* Consistent errors
* API versioning
* OpenAPI documentation

---

## FR-075 — Webhooks

The system shall support events such as:

```text
advertising.account.connected
advertising.account.disconnected
advertising.data.updated
advertising.sync.failed
advertising.report.generated
advertising.report.failed
advertising.anomaly.detected
advertising.budget.warning
advertising.roas.changed
advertising.recommendation.created
advertising.recommendation.approved
advertising.recommendation.completed
```

---

## FR-076 — Background Jobs

Long-running tasks shall execute asynchronously:

* Advertising synchronization
* Historical data ingestion
* Report generation
* AI analysis
* Forecasting
* Attribution calculation
* Large exports
* Cross-platform aggregation

---

## FR-077 — Idempotency

The system shall prevent duplicate processing for:

* Data synchronization
* Report generation
* Webhooks
* AI workflows
* Scheduled reports
* Export jobs

---

## FR-078 — Failure Recovery

When a provider fails, the system shall:

1. Detect failure.
2. Record failure.
3. Retry.
4. Apply exponential backoff.
5. Attempt provider fallback where available.
6. Preserve existing valid data.
7. Mark data as stale when appropriate.
8. Notify authorized users.
9. Resume processing after recovery.

---

## FR-079 — Partial Report Handling

When some data sources fail, reports shall clearly indicate affected sections.

Example:

```text
Platform A — Complete
Platform B — Complete
Platform C — Data Delayed
Platform D — Provider Error
```

The system shall not fabricate missing results.

---

## FR-080 — Advertising Command Center

The system shall provide a unified advertising command center containing:

```text
Advertising Health
Performance
Spend
Revenue
ROI
ROAS
Conversions
Campaigns
Platforms
Audiences
Demographics
Creatives
Products
Attribution
Budgets
Forecasts
AI Insights
Opportunities
Recommendations
Alerts
Reports
```

---

## 7. Non-Functional Requirements

## NFR-001 — Availability

Critical advertising reporting services shall target enterprise-grade availability according to the SalesGenie SLA.

---

## NFR-002 — Performance

Interactive dashboards shall use:

* Caching
* Pre-aggregation
* Query optimization
* Pagination
* Incremental loading

Long-running reports shall execute asynchronously.

---

## NFR-003 — Scalability

The system shall horizontally scale:

* APIs
* Data ingestion workers
* AI workers
* Report workers
* Forecasting workers
* Export workers
* Notification workers

---

## NFR-004 — Reliability

The platform shall tolerate:

* Provider outages
* API throttling
* Network failures
* AI model failures
* Worker failures
* Queue failures
* Partial data failures

---

## NFR-005 — Security

The platform shall implement:

* Zero-trust principles
* Least privilege
* Tenant isolation
* Secure secrets management
* Encryption
* Strong authentication
* Server-side authorization

---

## NFR-006 — Observability

The system shall provide:

* Logs
* Metrics
* Traces
* Error tracking
* Audit events
* AI telemetry
* Provider telemetry

---

## NFR-007 — Maintainability

The architecture shall use:

* Modular services
* Typed contracts
* Versioned APIs
* Automated testing
* CI/CD
* Infrastructure as code
* Configuration management
* Documentation

---

## NFR-008 — Accessibility

The advertising dashboard shall support:

* Keyboard navigation
* Screen readers
* Semantic HTML
* Accessible forms
* Accessible charts
* Appropriate contrast
* Focus management

---

## NFR-009 — Internationalization

The system should support:

* Multiple languages
* Multiple currencies
* Multiple timezones
* Multiple countries
* Regional reporting

---

## 8. Recommended Service Architecture

```text
                         SalesGenie Platform
                                |
                           API Gateway
                                |
                    Advertising Intelligence
                              Gateway
                                |
       ┌────────────────────────┼────────────────────────┐
       │                        │                        │
 Advertising Service     Advertising Data Service    Report Service
       │                        │                        │
       │                ┌───────┼────────┐              │
       │                │       │        │              │
       │              Google  Meta    LinkedIn          │
       │              TikTok  YouTube  Other APIs       │
       └────────────────┴───────┴────────┴──────────────┘
                                |
                          Event Bus / Queue
                                |
                       AI Advertising
                         Orchestrator
                                |
       ┌────────────────────────┼─────────────────────────┐
       │                        │                         │
 Campaign Agent          Audience Agent           Creative Agent
       │                        │                         │
 Spend Agent              Revenue Agent           Conversion Agent
       │                        │                         │
 ROI Agent                ROAS Agent              Attribution Agent
       │                        │                         │
 Budget Agent             Forecast Agent          Reporting Agent
       └────────────────────────┼─────────────────────────┘
                                |
                       Recommendation Engine
                                |
                       Human Approval Layer
                                |
                     Workflow / Task Engine
                                |
                      Outcome Measurement
                                |
                       Analytics Warehouse
```

---

## 9. Core Data Entities

```text
Tenant
Workspace
Organization
User
Role
Permission

AdvertisingProject
AdvertisingAccount
AdvertisingPlatform
Campaign
AdSet
Ad
Creative

Audience
AudienceSegment
Demographic
GeographicSegment
Placement
Device

Product
Keyword
SearchTerm

SpendMetric
ImpressionMetric
ClickMetric
ConversionMetric
RevenueMetric

ROIMetric
ROASMetric
CPAMetric
CPCMetric
CPMMetric
CTRMetric

AttributionModel
AttributionTouchpoint
AttributionResult

Budget
BudgetAllocation
BudgetForecast

AdvertisingHealthScore
AdvertisingRiskScore
AdvertisingOpportunity
AdvertisingAnomaly
AdvertisingForecast

AIInsight
AIRecommendation
AIEvaluation
AIExecution

Report
ReportTemplate
ReportVersion
ReportSection
ReportSchedule
ReportDelivery

DataSource
Integration
SyncJob
SyncError

Alert
Notification
AuditEvent
```

---

## 10. AI Advertising Intelligence Pipeline

```text
Advertising Data
        ↓
Data Ingestion
        ↓
Schema Validation
        ↓
Normalization
        ↓
Deduplication
        ↓
Historical Aggregation
        ↓
KPI Calculation
        ↓
Statistical Analysis
        ↓
Anomaly Detection
        ↓
AI Investigation
        ↓
Evidence Retrieval
        ↓
Root-Cause Analysis
        ↓
Opportunity Detection
        ↓
Impact Estimation
        ↓
Recommendation Generation
        ↓
Confidence Evaluation
        ↓
Human Review
        ↓
Action
        ↓
Outcome Measurement
        ↓
AI Evaluation
        ↓
Learning Loop
```

---

## 11. AI Guardrails

The AI shall never:

* Invent advertising spend.
* Invent revenue.
* Invent conversions.
* Invent ROAS.
* Invent ROI.
* Invent campaign performance.
* Invent audience data.
* Invent demographic data.
* Invent attribution results.
* Claim a campaign was changed when it was not.
* Change advertising budgets without authorization.
* Pause campaigns without authorization.
* Access another tenant's advertising account.
* Expose advertising credentials.
* Execute unauthorized external actions.

The AI shall explicitly report:

* Missing data
* Stale data
* Provider failures
* Attribution limitations
* Uncertainty
* Low-confidence conclusions
* Estimated values
* Forecast assumptions

---

## 12. Report Quality Gates

Every advertising report shall pass:

```text
✓ Authorization Validation
✓ Tenant Isolation Validation
✓ Data Freshness Validation
✓ Data Completeness Validation
✓ Metric Validation
✓ Currency Validation
✓ Attribution Validation
✓ Numerical Consistency Validation
✓ AI Schema Validation
✓ Evidence Validation
✓ Recommendation Validation
✓ Forecast Validation
✓ Report Rendering Validation
✓ Export Validation
```

---

## 13. Enterprise Advertising Report Structure

```text
1. Executive Summary
2. Advertising Health Score
3. KPI Overview
4. Advertising Spend
5. Revenue
6. ROI
7. ROAS
8. Conversion Performance
9. Campaign Performance
10. Ad Set Performance
11. Ad Performance
12. Platform Comparison
13. Audience Performance
14. Demographic Performance
15. Geographic Performance
16. Placement Performance
17. Device Performance
18. Creative Performance
19. Product Performance
20. Attribution Analysis
21. Budget Performance
22. Anomalies
23. AI Insights
24. Forecast
25. Opportunities
26. Recommended Actions
27. Human Decisions
28. Previous Period Comparison
29. Data Quality
30. Methodology
31. Data Sources
```

---

## 14. Executive Decision Support

The advertising reporting system shall enable executives to answer:

* How much are we spending?
* Where are we spending it?
* How much revenue are we generating?
* Which platform is most profitable?
* Which campaign is most profitable?
* Which campaign is wasting money?
* Which audience is most valuable?
* Which demographic is most profitable?
* Which geography is most profitable?
* Which product generates the highest advertising return?
* Which creative performs best?
* What is our ROAS?
* What is our ROI?
* What is our CPA?
* Are conversions improving?
* Why did performance change?
* What risks exist?
* Where should budget be moved?
* What should we scale?
* What should we reduce?
* What is likely to happen next?
* What action should the marketing team take first?

---

## 15. AI + Human Decision Governance

The system shall implement three operating modes.

## Mode A — AI Insight Only

```text
AI analyzes
    ↓
AI explains
    ↓
Human decides
```

Use for:

* Executive reporting
* Performance analysis
* Forecasting
* Competitor interpretation
* Strategic insights

---

## Mode B — AI Recommendation + Human Approval

```text
AI analyzes
    ↓
AI recommends
    ↓
Human reviews
    ↓
Human approves
    ↓
Action
```

Use for:

* Budget changes
* Campaign optimization
* Audience changes
* Creative changes
* Bid strategy recommendations

---

## Mode C — Controlled AI Automation

```text
AI detects
    ↓
Policy Validation
    ↓
Risk Validation
    ↓
Pre-approved rule
    ↓
AI executes
    ↓
Monitoring
    ↓
Rollback if necessary
```

This mode shall only be enabled for explicitly approved low-risk actions.

---

## 16. Recommendation Priority Framework

Each recommendation shall receive:

```text
Impact
Confidence
Urgency
Effort
Risk
Strategic Value
```

Priority levels:

```text
P0 — Critical
P1 — High
P2 — Medium
P3 — Low
```

Example scoring:

```text
Opportunity Score =
(Expected Business Impact × Confidence × Strategic Value)
/
(Effort × Risk)
```

The scoring formula shall be configurable by organization.

---

## 17. Advertising Health Framework

The Advertising Health Score shall be composed of configurable dimensions:

```text
Campaign Efficiency
        +
Budget Efficiency
        +
Conversion Efficiency
        +
Revenue Performance
        +
ROAS
        +
ROI
        +
Audience Quality
        +
Creative Quality
        +
Tracking Health
        +
Platform Diversification
```

The system shall provide:

* Overall score
* Component scores
* Historical trend
* Benchmark
* Major weaknesses
* Major strengths
* AI explanation
* Recommended improvements

---

## 18. Advertising Intelligence Learning Loop

```text
Historical Data
      ↓
Performance Analysis
      ↓
AI Insight
      ↓
AI Recommendation
      ↓
Human Decision
      ↓
Implementation
      ↓
Performance Measurement
      ↓
Expected vs Actual Comparison
      ↓
Outcome Evaluation
      ↓
AI Feedback
      ↓
Recommendation Quality Improvement
```

The system shall retain outcome information for evaluating recommendation effectiveness.

---

## 19. Enterprise Acceptance Criteria

The Advertising Reports module shall be considered production-ready only when:

* Multi-tenant isolation is verified.
* Server-side RBAC is enforced.
* Advertising account authorization is secure.
* Provider integrations are resilient.
* Data synchronization is idempotent.
* Data freshness is visible.
* Data provenance is available.
* Cross-platform normalization is reliable.
* Currency handling is correct.
* Attribution methodology is explicit.
* KPI calculations are deterministic.
* Historical reporting is reproducible.
* AI outputs are schema validated.
* AI insights are grounded in source data.
* AI hallucination controls are operational.
* AI confidence is available.
* Human approval is available for high-impact actions.
* Unauthorized advertising changes are prevented.
* Report generation is asynchronous.
* Scheduled reports work reliably.
* Partial provider failures are handled safely.
* Exported reports are validated.
* Audit logging is operational.
* Distributed tracing is operational.
* AI cost tracking is operational.
* Automated tests cover critical workflows.
* Security tests pass.
* Cross-tenant access tests pass.
* Load tests pass defined SLOs.
* Failure recovery is documented.
* Data retention policies are implemented.
* Data deletion workflows are implemented.
* AI evaluation metrics are tracked.
* No unsupported advertising claims are presented as facts.

---

## 20. Final Product Objective

SalesGenie's Advertising Reports module shall not function as a conventional static advertising reporting dashboard.

The target operating model shall be:

```text
REPORTING
    ↓
UNIFIED DATA
    ↓
ANALYTICS
    ↓
INTELLIGENCE
    ↓
ANOMALY DETECTION
    ↓
ROOT-CAUSE ANALYSIS
    ↓
FORECASTING
    ↓
OPPORTUNITY DISCOVERY
    ↓
AI RECOMMENDATION
    ↓
HUMAN DECISION
    ↓
CONTROLLED EXECUTION
    ↓
OUTCOME MEASUREMENT
    ↓
AI EVALUATION
    ↓
CONTINUOUS OPTIMIZATION
```

The ultimate objective is to make SalesGenie an enterprise-grade AI-powered advertising intelligence and decision-support platform that enables organizations to understand advertising performance, connect advertising spend to business outcomes, identify profitable growth opportunities, reduce inefficient spending, forecast future performance, and continuously improve advertising decisions while preserving human governance over consequential actions.
