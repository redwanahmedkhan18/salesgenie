# SalesGenie — AI-Based Product Profitability

## FAANG-Level User Requirements, System Requirements & Functional Requirements

> **Module:** AI-Based Product Profitability Analysis
> **Platform:** SalesGenie Enterprise AI Platform
> **Execution Model:** AI-first financial intelligence with deterministic financial calculations and human governance
> **Primary Objective:** Determine the true economic profitability of every product, SKU, service, subscription, package, customer segment, channel, market, and pricing configuration, then use AI to identify profitability drivers, risks, opportunities, and optimization actions.

---

## 1. Module Overview

The AI-Based Product Profitability module shall transform raw commercial, financial, operational, sales, marketing, customer, and product data into an auditable profitability intelligence system.

The module shall support:

- Product revenue analysis
- Product cost analysis
- Product gross-profit analysis
- Product contribution-margin analysis
- Product operating-profit analysis
- Product net-profit analysis
- Unit economics
- SKU profitability
- Product-family profitability
- Subscription profitability
- Service profitability
- Bundle profitability
- Customer-product profitability
- Segment-product profitability
- Channel-product profitability
- Geographic profitability
- Market profitability
- Pricing profitability
- Discount profitability
- Promotion profitability
- Acquisition-cost impact
- Retention-cost impact
- Support-cost impact
- Fulfillment-cost impact
- Infrastructure-cost impact
- Product lifecycle profitability
- Profitability forecasting
- Profitability scenario modeling
- Product profitability benchmarking
- Profitability anomaly detection
- Margin erosion detection
- Loss-making product detection
- Profitability opportunity detection
- AI profitability recommendations
- Human financial review
- Complete financial lineage and auditability

---

## 2. Core Business Objective

SalesGenie shall answer:

```text
Which products make money?
Why are they profitable?
Which products destroy margin?
Which customers generate the highest profit?
Which channels generate the highest profit?
Which products have strong revenue but weak profitability?
Which products have low revenue but exceptional margins?
What is the true cost of serving each product?
What price maximizes profitability?
How do discounts affect profitability?
Which products should be scaled?
Which products should be optimized?
Which products should be repriced?
Which products should be discontinued?
What happens to profit if costs, price, volume, or demand change?
```

---

## 3. Profitability Intelligence Architecture

```text
                    RAW BUSINESS DATA
                           ↓
                 DATA INGESTION LAYER
                           ↓
                  DATA NORMALIZATION
                           ↓
                 DATA QUALITY ENGINE
                           ↓
              REVENUE + COST RECONCILIATION
                           ↓
              DETERMINISTIC PROFIT ENGINE
                           ↓
                 UNIT ECONOMICS ENGINE
                           ↓
               PRODUCT PROFITABILITY ENGINE
                           ↓
             SEGMENT / CHANNEL ANALYSIS
                           ↓
              PROFITABILITY FORECASTING
                           ↓
              SCENARIO SIMULATION ENGINE
                           ↓
                 AI PROFITABILITY AGENT
                           ↓
             INSIGHTS + RISK DETECTION
                           ↓
                AI RECOMMENDATIONS
                           ↓
                 HUMAN GOVERNANCE
                           ↓
              AUDITABLE BUSINESS ACTION
```

---

## 4. User Roles

## 4.1 Super Admin

The Super Admin shall be able to:

* Configure global profitability capabilities.
* Configure AI model policies.
* Configure financial-analysis policies.
* Monitor AI usage.
* Monitor AI cost.
* Monitor service health.
* Configure platform-level governance.
* Review platform-level audit events.

The Super Admin shall not automatically receive unrestricted access to tenant financial information.

---

## 4.2 Workplace Admin

The Workplace Admin shall be able to:

* Configure workplace profitability settings.
* Configure reporting periods.
* Configure profitability dashboards.
* Configure financial permissions.
* Configure alert thresholds.
* Manage authorized users.

---

## 4.3 Organization Admin

The Organization Admin shall be able to:

* Configure products.
* Configure SKUs.
* Configure product categories.
* Configure cost structures.
* Configure pricing models.
* Configure profitability rules.
* Configure allocation policies.
* Configure reporting periods.
* Configure organizational profitability targets.
* Review profitability dashboards.

---

## 4.4 CFO / Finance Executive

The CFO shall be able to:

* Review enterprise profitability.
* Review product-level profitability.
* Review gross margin.
* Review contribution margin.
* Review operating margin.
* Review product cost structures.
* Review profitability forecasts.
* Review profitability scenarios.
* Review AI recommendations.
* Approve material financial recommendations.
* Export profitability reports.

---

## 4.5 Finance Manager

The Finance Manager shall be able to:

* Review financial inputs.
* Reconcile revenue and costs.
* Configure cost allocations.
* Validate product profitability.
* Review margin anomalies.
* Review profitability forecasts.
* Correct financial classifications.
* Approve profitability calculations.

---

## 4.6 Product Manager

The Product Manager shall be able to:

* View product profitability.
* Analyze product margins.
* Compare products.
* Identify loss-making products.
* Analyze feature and service costs.
* Evaluate pricing.
* Simulate price changes.
* Simulate cost changes.
* Review AI recommendations.

---

## 4.7 Sales Manager

The Sales Manager shall be able to:

* Analyze product profitability by customer.
* Analyze discount impact.
* Analyze deal profitability.
* Analyze channel profitability.
* Identify profitable customer/product combinations.
* Identify low-margin deals.

---

## 4.8 Marketing Manager

The Marketing Manager shall be able to:

* Analyze product profitability by campaign.
* Analyze customer acquisition costs.
* Analyze marketing cost allocation.
* Analyze campaign-generated product profit.
* Compare product profitability across acquisition channels.

---

## 4.9 Business Analyst

The Business Analyst shall be able to:

* Perform profitability analysis.
* Build custom reports.
* Compare products.
* Build profitability scenarios.
* Analyze trends.
* Validate AI insights.

---

## 4.10 End User / Client

Authorized clients shall be able to:

* View permitted profitability dashboards.
* Ask the AI profitability assistant questions.
* Review product profitability.
* Review forecasts.
* Review AI insights.
* Export authorized reports.

---

## 5. User Requirements

## UR-001 — Product Profitability Dashboard

Users shall be able to view:

```text
Total Revenue
Total Cost
Gross Profit
Gross Margin
Contribution Profit
Contribution Margin
Operating Profit
Operating Margin
Net Profit
Net Margin
Units Sold
Average Selling Price
Average Cost per Unit
Profit per Unit
```

---

## UR-002 — Product Ranking

The system shall rank products by:

* Revenue
* Gross profit
* Contribution profit
* Operating profit
* Net profit
* Gross margin
* Contribution margin
* Profit per unit
* Profit growth
* Profitability score

---

## UR-003 — Product Comparison

Users shall be able to compare multiple products.

Comparison dimensions shall include:

```text
Revenue
Volume
Price
Cost
Gross Profit
Gross Margin
Contribution Margin
Operating Profit
Net Profit
Growth
Customer Count
Return Rate
Discount Rate
Support Cost
Acquisition Cost
```

---

## UR-004 — Product Revenue Analysis

Users shall be able to analyze product revenue by:

* Day
* Week
* Month
* Quarter
* Year
* Customer
* Segment
* Region
* Country
* Channel
* Salesperson
* Campaign
* Subscription plan

---

## UR-005 — Product Cost Analysis

The system shall identify:

```text
Direct Costs
Indirect Costs
Variable Costs
Fixed Costs
Manufacturing Costs
Procurement Costs
Shipping Costs
Fulfillment Costs
Marketing Costs
Sales Costs
Support Costs
Infrastructure Costs
Payment Processing Costs
Returns
Refunds
Warranty Costs
Other Allocated Costs
```

---

## UR-006 — Gross Profit

The system shall calculate:

```text
Gross Profit = Revenue - Cost of Goods Sold
```

The organization's accounting definition shall be configurable.

---

## UR-007 — Gross Margin

The system shall calculate:

```text
Gross Margin =
Gross Profit / Revenue × 100
```

---

## UR-008 — Contribution Profit

The system shall support:

```text
Contribution Profit =
Revenue - Variable Costs
```

Variable-cost definitions shall be configurable.

---

## UR-009 — Contribution Margin

The system shall calculate:

```text
Contribution Margin =
Contribution Profit / Revenue × 100
```

---

## UR-010 — Operating Profitability

The system shall support configurable operating-profit calculations incorporating applicable:

* Product costs
* Operating expenses
* Sales expenses
* Marketing expenses
* Support expenses
* Product-specific operating costs

---

## UR-011 — Net Profitability

Where sufficient accounting data exists, the system shall calculate product-attributed net profitability.

The system shall clearly distinguish directly attributable costs from allocated costs.

---

## UR-012 — Unit Economics

The system shall calculate:

```text
Revenue Per Unit
Cost Per Unit
Gross Profit Per Unit
Contribution Profit Per Unit
Variable Cost Per Unit
Average Selling Price
Discount Per Unit
```

---

## UR-013 — Product Margin Trend

Users shall be able to identify:

* Margin expansion
* Margin compression
* Stable margins
* Margin volatility
* Structural margin changes

---

## UR-014 — Margin Erosion Detection

The AI shall detect products whose profitability is deteriorating.

Example:

```text
Product:
Enterprise Plan

Gross Margin:
68% → 57%

Primary drivers:
1. Infrastructure cost +23%
2. Support cost +18%
3. Discounting +11%

Risk:
HIGH
```

---

## UR-015 — Loss-Making Product Detection

The system shall identify products that are:

* Gross-margin negative
* Contribution-margin negative
* Operating-profit negative
* Net-profit negative

---

## UR-016 — Profitability Drivers

The AI shall identify the major drivers of profitability.

Example:

```text
Profitability declined by 14%.

Drivers:

Revenue:
+8%

Unit volume:
+12%

Average selling price:
-5%

Variable cost:
+17%

Discounts:
+9%

Support cost:
+13%
```

---

## UR-017 — Pricing Analysis

Users shall be able to analyze:

* List price
* Actual selling price
* Discount
* Net price
* Cost
* Profit per unit
* Margin percentage
* Price elasticity where sufficient data exists

---

## UR-018 — Discount Impact

The system shall quantify the impact of discounts on:

```text
Revenue
Gross Profit
Contribution Profit
Gross Margin
Contribution Margin
Net Profit
```

---

## UR-019 — Price Simulation

Users shall be able to simulate:

```text
Price +5%
Price +10%
Price -5%
Price -10%
Custom Price
```

The system shall estimate the effect on:

```text
Demand
Revenue
Profit
Margin
```

when sufficient historical or modeled demand data exists.

---

## UR-020 — Cost Simulation

Users shall be able to simulate:

```text
COGS +10%
Infrastructure +20%
Support Cost +15%
Marketing Cost +25%
Payment Cost +5%
```

---

## UR-021 — Volume Simulation

Users shall be able to simulate:

```text
Units +10%
Units +25%
Units -10%
Units -25%
Custom Volume
```

---

## UR-022 — Product Profitability Forecast

The AI shall forecast:

* Revenue
* Units
* Costs
* Gross profit
* Contribution profit
* Operating profit
* Margin
* Profitability risk

---

## UR-023 — Profitability Scenario Analysis

Users shall be able to compare:

```text
Base Case
Best Case
Worst Case
Stress Case
Custom Scenario
```

---

## UR-024 — Customer-Product Profitability

The system shall determine profitability by:

```text
Customer
Product
Customer + Product
Customer Segment + Product
```

---

## UR-025 — Channel-Product Profitability

The system shall determine profitability by:

```text
Direct Sales
Partner
Reseller
Marketplace
Organic
Paid Advertising
Affiliate
Other Channels
```

---

## UR-026 — Geographic Profitability

Users shall be able to analyze profitability by:

```text
Country
Region
City
Market
Sales Territory
```

---

## UR-027 — Product Lifecycle Profitability

The system shall support:

```text
Development
Launch
Growth
Maturity
Decline
Retirement
```

and analyze profitability across the lifecycle.

---

## UR-028 — Product Portfolio Analysis

Users shall be able to view:

```text
High Revenue / High Profit
High Revenue / Low Profit
Low Revenue / High Profit
Low Revenue / Low Profit
```

---

## UR-029 — Profitability Matrix

The system shall provide a portfolio matrix based on:

```text
Revenue
Growth
Margin
Profit
Strategic Value
```

---

## UR-030 — AI Product Recommendation

The AI shall recommend whether a product should be:

```text
SCALE
OPTIMIZE
REPRICE
REDUCE COST
REPOSITION
BUNDLE
PROMOTE
RETAIN
REVIEW
RETIRE
```

Recommendations shall include evidence and confidence.

---

## UR-031 — Product Profitability Chat

Users shall be able to ask:

```text
Which product is most profitable?

Which product has the highest margin?

Which products are losing money?

Why did Product A's margin decline?

Which products should we discontinue?

What happens if we increase Product A's price by 10%?

Which products should receive more marketing budget?

Which customers are most profitable for Product A?

Which channel generates the highest product profit?
```

---

## UR-032 — AI Profitability Explanation

Every AI-generated conclusion shall explain:

```text
Conclusion
Evidence
Calculated Metrics
Assumptions
Confidence
Risks
Recommended Action
```

---

## UR-033 — Human Override

Authorized users shall be able to:

* Override cost classification.
* Override allocation.
* Correct product mapping.
* Reject AI insight.
* Modify assumptions.
* Approve recommendation.
* Reject recommendation.
* Add commentary.

---

## 6. System Requirements

## SR-001 — Multi-Tenant Architecture

All profitability entities shall be tenant-scoped.

```text
tenant_id
organization_id
workspace_id
business_unit_id
```

shall be enforced server-side.

---

## SR-002 — Core Data Model

The system shall support:

```text
Product
ProductVariant
SKU
ProductCategory
ProductFamily
ProductCost
CostComponent
CostAllocation
ProductPrice
PriceHistory
Discount
Promotion
ProductRevenue
ProductTransaction
ProductProfitability
ProductMargin
ProductUnitEconomics
ProductForecast
ProfitabilityScenario
ProfitabilityAnomaly
ProfitabilityRisk
ProfitabilityInsight
ProfitabilityRecommendation
ProfitabilityBenchmark
ProfitabilityAuditEvent
```

---

## SR-003 — Product Entity

Each product shall support:

```text
Product ID
SKU
Name
Description
Category
Product Family
Product Type
Lifecycle Stage
Currency
Status
Launch Date
Retirement Date
Cost Model
Pricing Model
Created At
Updated At
```

---

## SR-004 — Revenue Model

The system shall distinguish:

```text
Gross Revenue
Discounts
Refunds
Returns
Credits
Net Revenue
```

---

## SR-005 — Cost Model

The system shall distinguish:

```text
Direct Cost
Indirect Cost
Fixed Cost
Variable Cost
Semi-Variable Cost
Allocated Cost
Unallocated Cost
```

---

## SR-006 — Cost Allocation Engine

The system shall support configurable allocation methods:

```text
Revenue-Based
Unit-Based
Usage-Based
Headcount-Based
Time-Based
Transaction-Based
Activity-Based
Custom
```

---

## SR-007 — Cost Allocation Transparency

Every allocated cost shall retain:

```text
Allocation Rule
Allocation Basis
Source Cost
Allocated Amount
Period
Product
Allocation Version
```

---

## SR-008 — Deterministic Profitability Engine

Financial calculations shall be performed by a deterministic service.

The AI shall not be the authoritative calculator.

---

## SR-009 — Profitability Calculation Layer

The engine shall calculate:

```text
Revenue
Net Revenue
COGS
Gross Profit
Gross Margin
Variable Costs
Contribution Profit
Contribution Margin
Operating Costs
Operating Profit
Operating Margin
Allocated Costs
Net Profit
Net Margin
```

---

## SR-010 — Unit Economics Engine

The engine shall calculate:

```text
ASP
Revenue Per Unit
COGS Per Unit
Variable Cost Per Unit
Gross Profit Per Unit
Contribution Profit Per Unit
```

---

## SR-011 — Subscription Profitability

The system shall support:

```text
Monthly Subscription
Annual Subscription
Usage-Based Pricing
Seat-Based Pricing
Tiered Pricing
Hybrid Pricing
```

and calculate profitability by plan.

---

## SR-012 — SaaS Unit Economics

Where applicable, the system shall support:

```text
CAC
LTV
LTV:CAC
ARPU
Gross Margin
Contribution Margin
Retention Cost
Support Cost
Infrastructure Cost
```

---

## SR-013 — Product-Level CAC Allocation

Customer-acquisition cost may be allocated to products using configurable attribution rules.

The system shall distinguish:

```text
Directly Attributed CAC
Allocated CAC
Unallocated CAC
```

---

## SR-014 — Customer Support Cost Allocation

The system shall support allocation of support costs using:

```text
Tickets
Conversation Volume
Resolution Time
Agent Time
Usage
Custom Activity Driver
```

---

## SR-015 — Infrastructure Cost Allocation

For digital/SaaS products, the system shall support:

```text
Compute Cost
Storage Cost
Bandwidth Cost
LLM Cost
API Cost
Database Cost
Vector Search Cost
Third-Party API Cost
```

allocation.

---

## SR-016 — Marketing Cost Allocation

The system shall support product-level attribution for:

```text
Campaign Spend
Advertising Spend
Content Spend
SEO Spend
Social Spend
Influencer Spend
Affiliate Spend
```

---

## SR-017 — Sales Cost Allocation

The system shall support:

```text
Sales Commission
Sales Salaries
Sales Operations
Partner Fees
Channel Fees
```

allocation.

---

## SR-018 — Return and Refund Accounting

The profitability engine shall account for:

```text
Returns
Refunds
Credits
Chargebacks
Warranty Claims
```

where applicable.

---

## SR-019 — Currency

The system shall support:

* Multi-currency products.
* Organization base currency.
* Historical exchange rates.
* FX conversion.
* FX impact analysis.

---

## SR-020 — Profitability Forecasting Engine

The system shall support:

* Time-series models.
* Regression.
* Machine learning.
* Ensemble models.
* Scenario-based forecasting.
* Hybrid forecasting.

---

## SR-021 — Forecast Uncertainty

Forecasts shall expose:

```text
Point Estimate
Lower Bound
Upper Bound
Confidence
Forecast Horizon
Model Version
Assumptions
```

---

## SR-022 — AI Agent Architecture

The AI Product Profitability Agent shall support:

```text
Intent Detection
Permission Validation
Data Retrieval
Metric Calculation
Trend Analysis
Profitability Analysis
Forecasting
Scenario Analysis
Risk Detection
Recommendation Generation
Human Escalation
```

---

## SR-023 — AI Tool Governance

AI tools shall be classified as:

```text
READ_ONLY
LOW_RISK_WRITE
HIGH_RISK_WRITE
FINANCIAL
DESTRUCTIVE
```

Financial and high-risk tools shall require explicit authorization.

---

## SR-024 — AI Execution Budget

Agents shall enforce:

```text
Maximum Steps
Maximum Tool Calls
Maximum Tokens
Maximum Runtime
Maximum Retries
Maximum Cost
```

---

## SR-025 — AI Grounding

AI profitability conclusions shall be grounded in:

```text
Financial Transactions
Revenue Records
Cost Records
Product Data
Pricing Data
Customer Data
Campaign Data
Forecast Data
Calculated Metrics
```

---

## SR-026 — Fact / Assumption Separation

AI output shall clearly separate:

```text
FACT
CALCULATION
ASSUMPTION
INFERENCE
FORECAST
SCENARIO
RECOMMENDATION
```

---

## SR-027 — AI Hallucination Protection

The AI shall never fabricate:

* Product revenue.
* Product costs.
* Product margins.
* Customer profitability.
* Financial transactions.
* Pricing.
* Cost allocations.
* Forecast results.
* Financial events.

---

## SR-028 — Human-in-the-Loop

Human review shall be required for configured high-impact recommendations, including:

```text
Product Retirement
Material Price Changes
Major Cost Changes
Financial Policy Changes
Large Budget Changes
Financial Data Changes
```

---

## SR-029 — Auditability

The system shall record:

```text
User
Tenant
Organization
Product
Action
Input Data
Calculation Version
AI Agent
Model
Model Version
Recommendation
Approval
Override
Timestamp
```

---

## SR-030 — Data Lineage

Every profitability metric shall be traceable:

```text
AI Insight
    ↓
Profitability Metric
    ↓
Calculation
    ↓
Revenue + Cost Components
    ↓
Transactions
    ↓
Original Source
```

---

## 7. Functional Requirements

## FR-001 — Product Registration

The system shall allow authorized users and integrations to create products and SKUs.

---

## FR-002 — Product Mapping

The system shall map:

```text
Orders
Invoices
Subscriptions
Payments
Expenses
Campaigns
Support Activity
Infrastructure Usage
```

to products where sufficient identifiers exist.

---

## FR-003 — Revenue Ingestion

The system shall ingest product revenue from supported:

* CRM
* Billing
* Payment
* ERP
* E-commerce
* Subscription
* Sales systems

---

## FR-004 — Cost Ingestion

The system shall ingest product-related costs.

---

## FR-005 — Cost Classification

The system shall classify costs as:

```text
DIRECT
INDIRECT
FIXED
VARIABLE
SEMI_VARIABLE
ALLOCATED
UNALLOCATED
```

---

## FR-006 — Cost Allocation

The system shall apply configured allocation rules.

---

## FR-007 — Revenue Reconciliation

The system shall reconcile:

```text
Orders
Invoices
Payments
Revenue
Refunds
Credits
```

---

## FR-008 — Product Profitability Calculation

The system shall calculate profitability for each product and SKU.

---

## FR-009 — Gross Profit Calculation

```text
Gross Profit = Net Revenue - COGS
```

---

## FR-010 — Gross Margin Calculation

```text
Gross Margin =
Gross Profit / Net Revenue × 100
```

---

## FR-011 — Contribution Profit Calculation

```text
Contribution Profit =
Net Revenue - Variable Costs
```

---

## FR-012 — Contribution Margin Calculation

```text
Contribution Margin =
Contribution Profit / Net Revenue × 100
```

---

## FR-013 — Operating Profit Calculation

The system shall calculate operating profit using the organization's configured product-level cost allocation methodology.

---

## FR-014 — Net Profit Calculation

The system shall calculate product-attributed net profitability where sufficient financial data exists.

---

## FR-015 — Unit Profitability

The system shall calculate:

```text
Revenue / Unit
Cost / Unit
Gross Profit / Unit
Contribution Profit / Unit
```

---

## FR-016 — Product Ranking

The system shall rank products by configurable profitability metrics.

---

## FR-017 — Profitability Matrix

The system shall classify products using:

```text
High Profit / High Growth
High Profit / Low Growth
Low Profit / High Growth
Low Profit / Low Growth
```

---

## FR-018 — Margin Trend Detection

The system shall detect significant margin changes.

---

## FR-019 — Profitability Anomaly Detection

The AI shall detect unusual:

* Cost spikes.
* Revenue drops.
* Margin changes.
* Discount changes.
* Return-rate changes.
* Support-cost changes.
* Infrastructure-cost changes.
* Customer-mix changes.

---

## FR-020 — Loss-Making Product Detection

The system shall identify products whose configured profitability metric falls below zero or a defined threshold.

---

## FR-021 — Profitability Thresholds

Users shall be able to configure:

```text
Minimum Gross Margin
Minimum Contribution Margin
Minimum Product Profit
Maximum CAC
Maximum Support Cost
Maximum Discount
Maximum Return Rate
```

---

## FR-022 — Product Profitability Forecast

The system shall forecast:

```text
Revenue
Units
COGS
Variable Costs
Gross Profit
Contribution Profit
Operating Profit
Net Profit
Margin
```

---

## FR-023 — Product Demand Forecast

Where sufficient data exists, the system shall forecast product demand.

Demand forecasts shall be separate from profitability forecasts.

---

## FR-024 — Price Simulation

The system shall simulate price changes.

---

## FR-025 — Cost Simulation

The system shall simulate cost changes.

---

## FR-026 — Volume Simulation

The system shall simulate changes in sales volume.

---

## FR-027 — Discount Simulation

The system shall simulate different discount levels.

---

## FR-028 — Combined Scenario Simulation

The system shall support combined scenarios:

```text
Price
+
Volume
+
Cost
+
Discount
+
Marketing Spend
+
Support Cost
```

---

## FR-029 — Scenario Comparison

The system shall compare:

```text
Baseline
Optimistic
Pessimistic
Stress
Custom
```

---

## FR-030 — Break-Even Analysis

The system shall calculate break-even points where applicable.

Example:

```text
Break-Even Units =
Fixed Costs /
Contribution Margin Per Unit
```

---

## FR-031 — Break-Even Revenue

The system shall calculate:

```text
Break-Even Revenue =
Fixed Costs /
Contribution Margin Ratio
```

where the configured contribution-margin methodology applies.

---

## FR-032 — Margin of Safety

The system shall calculate configurable margin-of-safety metrics.

---

## FR-033 — Customer Profitability

The system shall calculate product profitability by customer.

---

## FR-034 — Segment Profitability

The system shall calculate product profitability by customer segment.

---

## FR-035 — Channel Profitability

The system shall calculate profitability by acquisition and sales channel.

---

## FR-036 — Geographic Profitability

The system shall calculate profitability by geography.

---

## FR-037 — Campaign Profitability

The system shall connect marketing campaign costs to product profitability where attribution data exists.

---

## FR-038 — Sales Deal Profitability

The system shall calculate profitability at deal level where sufficient data exists.

---

## FR-039 — Discount Profitability

The system shall determine whether discounts create sufficient incremental volume or revenue to justify lost margin.

---

## FR-040 — Bundle Profitability

The system shall calculate profitability for product bundles.

---

## FR-041 — Subscription Plan Profitability

The system shall calculate profitability by subscription plan and billing model.

---

## FR-042 — Product Lifecycle Analysis

The system shall analyze profitability across product lifecycle stages.

---

## FR-043 — AI Product Insight

The AI shall generate insights such as:

```text
Product A generates the highest revenue but ranks third in contribution profit.

The primary reason is a 19% lower contribution margin caused by infrastructure and support costs.

Product B generates 34% less revenue but 22% more contribution profit.
```

---

## FR-044 — AI Profitability Recommendation

The AI shall generate recommendations such as:

```text
Increase price.
Reduce discounting.
Renegotiate supplier costs.
Reduce infrastructure usage.
Optimize support resources.
Increase marketing allocation.
Reduce marketing allocation.
Bundle the product.
Change packaging.
Target higher-value customers.
Retire the product.
```

---

## FR-045 — Recommendation Impact

Each recommendation shall include:

```text
Estimated Profit Impact
Estimated Revenue Impact
Estimated Margin Impact
Time to Impact
Confidence
Risk
Assumptions
Owner
Approval Requirement
```

---

## FR-046 — AI Profitability Chat

The AI shall support natural-language profitability questions.

---

## FR-047 — AI Query Planning

The AI shall translate user questions into validated read-only analytical operations when possible.

---

## FR-048 — Permission Enforcement

AI-generated queries shall be:

* Tenant scoped.
* Organization scoped.
* Permission checked.
* Schema validated.
* Resource limited.
* Audited.

---

## FR-049 — Profitability Reports

The system shall generate:

```text
Product Profitability Report
SKU Profitability Report
Gross Margin Report
Contribution Margin Report
Product Portfolio Report
Customer-Product Profitability Report
Channel Profitability Report
Pricing Profitability Report
Discount Impact Report
Product Forecast Report
Profitability Risk Report
Profitability Scenario Report
AI Recommendation Report
```

---

## FR-050 — Scheduled Reporting

Users shall be able to schedule:

```text
Daily Profitability Summary
Weekly Product Margin Report
Monthly Product Profitability Report
Quarterly Portfolio Profitability Report
Monthly Pricing Analysis
Monthly Profitability Risk Report
```

---

## FR-051 — Export

Authorized users shall be able to export:

* Product profitability.
* Product costs.
* Revenue.
* Margins.
* Forecasts.
* Scenarios.
* AI insights.
* Recommendations.

---

## FR-052 — Audit Trail

The system shall preserve complete history of:

* Revenue changes.
* Cost changes.
* Allocation changes.
* Pricing changes.
* Product mapping changes.
* Forecast generation.
* Scenario generation.
* AI recommendations.
* Human overrides.
* Approvals.

---

## 8. Product Profitability KPI Framework

The platform shall support:

```text
Revenue
Net Revenue
Units Sold
Average Selling Price
COGS
Variable Cost
Fixed Cost
Allocated Cost
Gross Profit
Gross Margin
Contribution Profit
Contribution Margin
Operating Profit
Operating Margin
Net Profit
Net Margin
Profit Per Unit
Revenue Per Unit
Cost Per Unit
CAC
LTV
LTV:CAC
ARPU
Return Rate
Refund Rate
Discount Rate
Support Cost
Infrastructure Cost
Marketing Cost
Sales Cost
Break-Even Units
Break-Even Revenue
Margin of Safety
Profit Growth
Margin Growth
Profitability Score
```

---

## 9. AI Product Profitability Agent

## AI Agent Responsibilities

The AI Product Profitability Agent shall:

1. Understand profitability questions.
2. Identify the required financial dimensions.
3. Retrieve authorized data.
4. Invoke deterministic financial tools.
5. Analyze profitability.
6. Identify drivers.
7. Detect anomalies.
8. Forecast profitability.
9. Simulate scenarios.
10. Generate explanations.
11. Generate recommendations.
12. Escalate material decisions to humans.

---

## AI Agent Workflow

```text
User Request
     ↓
Intent Detection
     ↓
Permission Validation
     ↓
Entity Resolution
     ↓
Product Resolution
     ↓
Data Retrieval
     ↓
Deterministic Calculations
     ↓
Profitability Analysis
     ↓
Forecast / Scenario
     ↓
Risk Detection
     ↓
AI Reasoning
     ↓
Evidence Validation
     ↓
Recommendation
     ↓
Human Approval
```

---

## 10. MCP Tools

The Product Profitability Agent may expose controlled tools:

```text
profitability.get_product
profitability.search_products
profitability.get_revenue
profitability.get_costs
profitability.get_cogs
profitability.get_variable_costs
profitability.get_fixed_costs
profitability.get_allocated_costs
profitability.calculate_gross_profit
profitability.calculate_gross_margin
profitability.calculate_contribution_profit
profitability.calculate_contribution_margin
profitability.calculate_operating_profit
profitability.calculate_net_profit
profitability.calculate_unit_economics
profitability.calculate_break_even
profitability.get_product_profitability
profitability.compare_products
profitability.analyze_pricing
profitability.analyze_discounts
profitability.forecast_profitability
profitability.create_scenario
profitability.compare_scenarios
profitability.detect_margin_anomalies
profitability.detect_loss_making_products
profitability.get_profitability_risks
profitability.generate_insight
profitability.generate_recommendation
profitability.generate_report
```

Write-capable tools shall require explicit authorization.

---

## 11. AI Guardrails

## AI-GR-001 — No Fabricated Financial Data

The AI shall never invent:

```text
Revenue
Costs
Margins
Profit
Pricing
Transactions
Customer Profitability
Product Costs
Forecast Values
```

---

## AI-GR-002 — Deterministic Financial Calculations

Authoritative financial calculations shall be performed by deterministic services.

The LLM shall interpret and explain calculated results rather than independently becoming the financial source of truth.

---

## AI-GR-003 — Evidence Grounding

Every material AI profitability claim shall be traceable to:

```text
Source Data
Calculated Metrics
Reporting Period
Product
Cost Components
Revenue Components
```

---

## AI-GR-004 — Confidence

AI output shall include:

```text
Confidence
Data Completeness
Data Freshness
Evidence Strength
Forecast Uncertainty
```

where applicable.

---

## AI-GR-005 — Fact / Forecast Separation

The interface shall clearly distinguish:

```text
ACTUAL
ESTIMATED
FORECAST
SCENARIO
AI INFERENCE
RECOMMENDATION
```

---

## AI-GR-006 — Human Approval

The AI shall not autonomously:

* Retire products.
* Change production pricing.
* Change financial accounting policies.
* Modify financial records.
* Change major budgets.
* Execute material financial actions.

without required authorization.

---

## 12. Profitability Risk Engine

The system shall calculate profitability risk using:

```text
Revenue Volatility
Cost Volatility
Margin Volatility
Demand Volatility
Discount Rate
Return Rate
Refund Rate
CAC
Support Cost
Infrastructure Cost
Supplier Cost
Customer Concentration
Channel Concentration
Product Concentration
Forecast Uncertainty
```

---

## Risk Levels

```text
LOW
MEDIUM
HIGH
CRITICAL
```

Example:

```json
{
  "product_id": "prod_001",
  "risk_score": 0.87,
  "risk_level": "HIGH",
  "primary_drivers": [
    "margin_compression",
    "infrastructure_cost_growth",
    "discount_increase"
  ],
  "estimated_profit_impact": -185000,
  "human_review_required": true
}
```

---

## 13. Product Portfolio Intelligence

The system shall classify products into strategic groups.

## Star Products

```text
High Growth
High Profitability
```

Recommended action:

```text
SCALE
```

---

## Cash Generators

```text
Low Growth
High Profitability
```

Recommended action:

```text
OPTIMIZE
PROTECT
```

---

## Potential Products

```text
High Growth
Low Profitability
```

Recommended action:

```text
REDUCE COST
REPRICE
OPTIMIZE
```

---

## Problem Products

```text
Low Growth
Low Profitability
```

Recommended action:

```text
REVIEW
REPOSITION
RETIRE
```

---

## 14. Pricing Intelligence

The platform shall connect profitability analysis with pricing intelligence.

```text
Current Price
     ↓
Demand
     ↓
Units Sold
     ↓
Revenue
     ↓
Variable Cost
     ↓
Contribution Profit
     ↓
Margin
```

The AI shall evaluate pricing changes using historical evidence and configured assumptions.

---

## 15. Discount Optimization

The system shall analyze:

```text
List Price
Discount %
Net Price
Incremental Units
Incremental Revenue
Incremental Cost
Incremental Profit
Margin Loss
```

The AI shall identify discounts that:

* Increase profit.
* Increase revenue but reduce profit.
* Reduce both revenue and profit.
* Require additional evidence before action.

---

## 16. Product Profitability Scenario Engine

The scenario engine shall support:

```text
PRICE CHANGE
VOLUME CHANGE
COST CHANGE
DISCOUNT CHANGE
CAC CHANGE
SUPPORT COST CHANGE
MARKETING SPEND CHANGE
INFRASTRUCTURE COST CHANGE
RETURN RATE CHANGE
REFUND RATE CHANGE
CUSTOMER MIX CHANGE
CHANNEL MIX CHANGE
```

Example:

```text
Scenario:
Price +10%
Volume -4%
Variable Cost +3%
Discount -2%

Projected Result:
Revenue: +5.6%
Gross Profit: +11.2%
Contribution Margin: +4.8 percentage points
```

Scenario outputs shall clearly identify assumptions and shall not alter actual financial records.

---

## 17. Product Profitability Forecasting

The forecasting system shall estimate:

```text
Future Revenue
Future Units
Future Costs
Future Gross Profit
Future Contribution Profit
Future Operating Profit
Future Net Profit
Future Margin
```

Forecasts shall expose:

```text
Model
Model Version
Training Window
Forecast Horizon
Assumptions
Prediction Interval
Confidence
Generated At
```

---

## 18. Forecast Evaluation

The system shall measure:

```text
MAE
RMSE
MAPE
Forecast Bias
Prediction Interval Coverage
Forecast Stability
```

Forecast performance shall be monitored continuously.

---

## 19. Data Quality Requirements

The system shall detect:

```text
Missing Product Mapping
Duplicate Revenue
Duplicate Transactions
Missing Costs
Unallocated Costs
Invalid Prices
Negative Prices
Invalid Currency
Missing Product IDs
Missing SKU IDs
Incorrect Cost Classification
Stale Data
Revenue/Payment Mismatch
Cost/Invoice Mismatch
```

Data-quality problems shall reduce confidence in profitability results when material.

---

## 20. Product Profitability Data Lineage

Users shall be able to drill down:

```text
AI Recommendation
       ↓
Profitability Insight
       ↓
Profitability KPI
       ↓
Profit Calculation
       ↓
Revenue + Cost Components
       ↓
Transactions
       ↓
Original Financial Source
```

---

## 21. Multi-Agent Collaboration

The Product Profitability Agent shall integrate with:

```text
Revenue Analytics Agent
Expense Tracking Agent
Cash Flow Agent
Financial Analytics Agent
Business Intelligence Agent
Marketing Analytics Agent
Sales Analytics Agent
Customer Intelligence Agent
Pricing Intelligence Agent
Product Intelligence Agent
```

Example:

```text
Revenue Agent
      ↓
Revenue increased 15%

Expense Agent
      ↓
Product infrastructure cost increased 32%

Marketing Agent
      ↓
CAC increased 18%

Customer Agent
      ↓
High-value customers increasingly use expensive features

      ↓

Product Profitability Agent
      ↓

Contribution margin decreased 11%.

      ↓

Pricing / Strategy Agent
      ↓

Recommend pricing and packaging optimization.
```

---

## 22. Observability Requirements

The system shall monitor:

```text
Profitability Calculation Latency
Revenue Processing Latency
Cost Processing Latency
Allocation Processing Latency
Forecast Latency
Scenario Latency
AI Latency
AI Token Usage
AI Cost
Tool Calls
Recommendation Generation Rate
AI Error Rate
Forecast Accuracy
Data Freshness
Integration Health
```

Distributed tracing shall correlate:

```text
User Request
API Request
Agent
Tool Calls
Database Queries
Financial Calculations
AI Calls
Final Response
```

---

## 23. Reliability Requirements

The system shall support:

* Idempotent financial ingestion.
* Retry policies.
* Circuit breakers.
* Dead-letter queues.
* Background processing.
* Forecast-job recovery.
* Scenario-job recovery.
* AI-provider fallback.
* Partial-failure handling.
* Graceful degradation.

If AI services are unavailable, deterministic profitability calculations and standard reporting shall remain available whenever the required financial data is available.

---

## 24. Performance Requirements

Interactive operations shall prioritize low latency for:

```text
Product Profitability Dashboard
Product Search
Product Ranking
Current Margins
Standard KPI Queries
```

Asynchronous processing shall be used for:

```text
Large Historical Analysis
Portfolio Analysis
Large Cost Allocation
Forecasting
Scenario Simulation
Batch AI Analysis
Large Report Generation
```

---

## 25. Security Requirements

The module shall enforce:

```text
Tenant Isolation
Organization Isolation
RBAC
Fine-Grained Permissions
Financial Data Access Control
Encryption At Rest
Encryption In Transit
Audit Logging
AI Tool Authorization
Sensitive Data Masking
Credential Protection
```

AI agents shall never access data beyond the permissions of their execution identity.

---

## 26. Audit Requirements

Every material profitability decision shall be auditable.

The system shall record:

```text
Actor
Tenant
Organization
Product
Data Sources
Calculation Version
Allocation Rules
AI Agent
Model
Model Version
Prompt Version
Tool Calls
Recommendation
Approval
Override
Timestamp
```

---

## 27. AI Quality Metrics

SalesGenie shall evaluate the Product Profitability Agent using:

```text
Profitability Calculation Accuracy
Cost Allocation Accuracy
Product Mapping Accuracy
Revenue Attribution Accuracy
Margin Analysis Accuracy
Forecast MAE
Forecast RMSE
Forecast MAPE
Forecast Bias
Anomaly Precision
Anomaly Recall
Recommendation Accuracy
Recommendation Acceptance Rate
Recommendation Override Rate
Evidence Grounding Rate
Hallucination Rate
Tool-Call Accuracy
Permission Violation Rate
```

---

## 28. Product Profitability Recommendation Framework

Each recommendation shall contain:

```text
Recommendation ID
Product ID
Recommendation Type
Current State
Problem
Evidence
Root Cause
Recommended Action
Expected Revenue Impact
Expected Cost Impact
Expected Profit Impact
Expected Margin Impact
Time to Impact
Confidence
Risk
Assumptions
Owner
Approval Required
Status
Created At
```

Example:

```text
Recommendation:
Reduce infrastructure cost for Product A.

Evidence:
Infrastructure cost per active customer increased 31%
over the last 90 days.

Expected Impact:
Contribution margin +6.4 percentage points.

Expected Annual Profit Impact:
+$240,000.

Confidence:
91%.

Risk:
LOW.

Owner:
Product + Engineering + Finance.

Approval:
Finance Manager.
```

---

## 29. Recommendation Lifecycle

Recommendations shall support:

```text
GENERATED
UNDER_REVIEW
APPROVED
REJECTED
DEFERRED
IMPLEMENTED
FAILED
ARCHIVED
```

---

## 30. API-Level Functional Domains

The service shall expose logically separated API domains:

```text
/products
/products/{product_id}/profitability
/products/{product_id}/margins
/products/{product_id}/unit-economics
/products/{product_id}/forecast
/products/{product_id}/scenarios
/products/{product_id}/pricing
/products/{product_id}/discounts
/products/{product_id}/risks
/products/{product_id}/insights
/products/{product_id}/recommendations

/profitability/overview
/profitability/products
/profitability/customers
/profitability/channels
/profitability/segments
/profitability/geographies
/profitability/portfolio

/profitability/forecast
/profitability/scenarios
/profitability/anomalies
/profitability/reports
```

All endpoints shall enforce:

```text
Authentication
Authorization
Tenant Isolation
Input Validation
Pagination
Rate Limiting
Audit Logging
```

---

## 31. Acceptance Criteria

The module shall be considered production-ready only when:

* [ ] Products and SKUs can be registered.
* [ ] Revenue can be mapped to products.
* [ ] Costs can be mapped to products.
* [ ] Direct costs can be calculated.
* [ ] Indirect costs can be allocated.
* [ ] Fixed costs can be handled.
* [ ] Variable costs can be handled.
* [ ] Revenue can be reconciled.
* [ ] Product profitability can be calculated deterministically.
* [ ] Gross profit can be calculated.
* [ ] Gross margin can be calculated.
* [ ] Contribution profit can be calculated.
* [ ] Contribution margin can be calculated.
* [ ] Operating profit can be calculated.
* [ ] Net profitability can be calculated where data permits.
* [ ] Unit economics can be calculated.
* [ ] Product ranking is supported.
* [ ] Product comparison is supported.
* [ ] Profitability trends are supported.
* [ ] Margin erosion is detected.
* [ ] Loss-making products are detected.
* [ ] Profitability anomalies are detected.
* [ ] Customer-product profitability is supported.
* [ ] Segment-product profitability is supported.
* [ ] Channel-product profitability is supported.
* [ ] Geographic profitability is supported.
* [ ] Campaign-product profitability is supported where attribution exists.
* [ ] Pricing profitability is supported.
* [ ] Discount impact is supported.
* [ ] Price simulations are supported.
* [ ] Cost simulations are supported.
* [ ] Volume simulations are supported.
* [ ] Break-even analysis is supported.
* [ ] Product profitability forecasting is supported.
* [ ] Forecast uncertainty is exposed.
* [ ] Forecast accuracy is evaluated.
* [ ] Scenario analysis is supported.
* [ ] Product portfolio analysis is supported.
* [ ] AI profitability insights are generated.
* [ ] AI recommendations are evidence-backed.
* [ ] AI recommendations include expected financial impact.
* [ ] AI cannot fabricate financial data.
* [ ] Deterministic financial calculations remain authoritative.
* [ ] AI outputs distinguish facts from forecasts and assumptions.
* [ ] Human approval is required for material financial actions.
* [ ] Product profitability data lineage is available.
* [ ] All financial changes are auditable.
* [ ] RBAC is enforced server-side.
* [ ] Tenant isolation is enforced.
* [ ] AI tools cannot bypass permissions.
* [ ] MCP tool parameters are schema validated.
* [ ] AI execution budgets are enforced.
* [ ] Scenario calculations cannot modify actual financial records.
* [ ] Financial ingestion is idempotent.
* [ ] Data-quality issues are detectable.
* [ ] Forecast model versions are tracked.
* [ ] AI model versions are tracked.
* [ ] AI cost and latency are observable.
* [ ] Integration failures are recoverable.
* [ ] Deterministic reporting remains available during AI-provider failure.
* [ ] Automated unit tests cover profitability calculations.
* [ ] Integration tests cover financial data flows.
* [ ] Cross-tenant isolation tests pass.
* [ ] AI evaluation tests pass.
* [ ] Load tests pass.
* [ ] Security tests pass.
* [ ] Auditability tests pass.

---

## 32. FAANG-Level Product Profitability Decision Framework

SalesGenie shall convert product profitability data into an intelligent decision system:

```text
                  PRODUCT DATA
                       +
                  REVENUE DATA
                       +
                   COST DATA
                       +
                CUSTOMER DATA
                       +
                 SALES DATA
                       +
               MARKETING DATA
                       +
              OPERATIONAL DATA
                       ↓
                DATA QUALITY
                       ↓
              RECONCILIATION
                       ↓
          DETERMINISTIC PROFIT ENGINE
                       ↓
             UNIT ECONOMICS
                       ↓
          PRODUCT PROFITABILITY
                       ↓
       CUSTOMER / CHANNEL / SEGMENT
              PROFITABILITY
                       ↓
              TREND ANALYSIS
                       ↓
            ANOMALY DETECTION
                       ↓
             FORECASTING
                       ↓
          SCENARIO SIMULATION
                       ↓
           AI ROOT-CAUSE ANALYSIS
                       ↓
          AI PROFITABILITY INSIGHT
                       ↓
         AI OPTIMIZATION RECOMMENDATION
                       ↓
               HUMAN REVIEW
                       ↓
          BUSINESS DECISION
                       ↓
             OUTCOME TRACKING
                       ↓
              AI EVALUATION
```

## Core Principle

> **SalesGenie's AI-Based Product Profitability module shall not merely report which products generate revenue. It shall determine the economic value of each product by connecting revenue, direct costs, variable costs, allocated costs, customer behavior, acquisition costs, operational costs, pricing, discounts, and product usage; use deterministic financial services as the source of truth; use AI for analysis, forecasting, anomaly detection, explanation, and optimization; and keep humans in control of material financial decisions.**
