# SalesGenie — AI-Based Product Loss Analysis

## FAANG-Level User Requirements, System Requirements & Functional Requirements

> **Module:** AI-Based Product Loss Analysis
> **Platform:** SalesGenie Enterprise AI Platform
> **Execution Model:** AI-first financial intelligence with deterministic financial calculations and human governance
> **Primary Objective:** Identify, quantify, explain, predict, and reduce product-level losses across products, SKUs, customers, channels, markets, campaigns, subscriptions, and operational activities.

---

## 1. Module Overview

The AI-Based Product Loss Analysis module shall provide an enterprise-grade system for detecting and analyzing products that generate financial losses or materially threaten future profitability.

The module shall analyze:

- Product losses
- SKU losses
- Gross losses
- Contribution losses
- Operating losses
- Net losses
- Loss per unit
- Loss by customer
- Loss by segment
- Loss by channel
- Loss by geography
- Loss by campaign
- Loss by subscription plan
- Loss caused by discounts
- Loss caused by returns and refunds
- Loss caused by excessive support costs
- Loss caused by infrastructure costs
- Loss caused by acquisition costs
- Loss caused by pricing
- Loss caused by cost increases
- Loss caused by low utilization
- Loss caused by customer mix
- Loss caused by operational inefficiencies
- Historical loss trends
- Current loss exposure
- Forecast losses
- Potential future losses
- Loss scenarios
- Loss prevention opportunities
- AI-generated root-cause analysis
- AI-generated remediation recommendations
- Human financial review and approval

---

## 2. Core Business Objective

SalesGenie shall answer:

```text
Which products are currently losing money?

How much money is each product losing?

Why is the product losing money?

Is the loss caused by price, cost, volume, discounts, customers, channels, returns, support, infrastructure, marketing, or another factor?

Which products have the highest financial risk?

Which products are becoming unprofitable?

Which products may become loss-making in the future?

Which products should be optimized?

Which products should be repriced?

Which products require cost reduction?

Which products should receive less marketing spend?

Which products should be redesigned or repositioned?

Which products should be discontinued?

How much loss could be avoided by taking a specific action?

What is the expected financial impact of each remediation strategy?
```

---

## 3. Loss Analysis Architecture

```text
                    BUSINESS DATA
                         ↓
               DATA INGESTION LAYER
                         ↓
                DATA NORMALIZATION
                         ↓
                 DATA QUALITY ENGINE
                         ↓
             REVENUE/COST RECONCILIATION
                         ↓
             DETERMINISTIC LOSS ENGINE
                         ↓
                LOSS CLASSIFICATION
                         ↓
             PRODUCT LOSS ANALYSIS
                         ↓
          CUSTOMER/CHANNEL/SEGMENT ANALYSIS
                         ↓
              ROOT-CAUSE ANALYSIS
                         ↓
               LOSS FORECASTING
                         ↓
             SCENARIO SIMULATION
                         ↓
                AI LOSS AGENT
                         ↓
             RISK + OPPORTUNITY ENGINE
                         ↓
             AI RECOMMENDATIONS
                         ↓
              HUMAN GOVERNANCE
                         ↓
             REMEDIATION TRACKING
```

---

## 4. User Roles

## 4.1 Super Admin

The Super Admin shall be able to:

* Configure platform-level loss-analysis capabilities.
* Configure AI policies.
* Configure AI execution limits.
* Monitor AI usage.
* Monitor AI costs.
* Monitor service health.
* Configure global governance policies.
* Review platform-level audit events.

The Super Admin shall not automatically receive unrestricted access to tenant financial information.

---

## 4.2 Workplace Admin

The Workplace Admin shall be able to:

* Configure workplace loss-analysis settings.
* Configure reporting periods.
* Configure loss thresholds.
* Configure alert policies.
* Configure authorized users.
* Manage workspace-level dashboards.

---

## 4.3 Organization Admin

The Organization Admin shall be able to:

* Configure products.
* Configure SKUs.
* Configure product categories.
* Configure loss thresholds.
* Configure cost allocation policies.
* Configure financial reporting rules.
* Configure loss alerts.
* Review product loss dashboards.

---

## 4.4 CFO / Finance Executive

The CFO shall be able to:

* Review total product loss.
* Review loss-making products.
* Review loss trends.
* Review loss forecasts.
* Review root causes.
* Review AI recommendations.
* Approve material remediation strategies.
* Review potential financial exposure.
* Export loss-analysis reports.

---

## 4.5 Finance Manager

The Finance Manager shall be able to:

* Reconcile revenue and cost data.
* Validate loss calculations.
* Review cost allocation.
* Review loss anomalies.
* Review product-level financial losses.
* Correct financial classifications.
* Approve financial remediation recommendations.

---

## 4.6 Product Manager

The Product Manager shall be able to:

* Identify loss-making products.
* Analyze product loss drivers.
* Analyze product pricing.
* Analyze cost structure.
* Analyze customer profitability.
* Simulate pricing changes.
* Simulate cost changes.
* Review AI recommendations.

---

## 4.7 Sales Manager

The Sales Manager shall be able to:

* Analyze loss by customer.
* Analyze loss by sales channel.
* Analyze discount-related losses.
* Analyze low-margin deals.
* Identify unprofitable customers.
* Identify unprofitable sales patterns.

---

## 4.8 Marketing Manager

The Marketing Manager shall be able to:

* Analyze product losses including acquisition costs.
* Analyze campaign-generated losses.
* Analyze CAC contribution to product loss.
* Identify campaigns generating low-quality or unprofitable customers.

---

## 4.9 Business Analyst

The Business Analyst shall be able to:

* Analyze product losses.
* Compare loss-making products.
* Investigate loss drivers.
* Build scenarios.
* Analyze historical trends.
* Validate AI findings.

---

## 4.10 End User / Client

Authorized clients shall be able to:

* View permitted loss dashboards.
* Ask the AI loss-analysis assistant questions.
* Review loss insights.
* Review forecasts.
* Review recommendations.

---

## 5. User Requirements

## UR-001 — Product Loss Dashboard

Users shall be able to view:

```text
Total Product Loss
Gross Loss
Contribution Loss
Operating Loss
Net Loss
Loss Per Unit
Loss Rate
Loss-Producing Products
Loss-Producing SKUs
Loss Growth
Loss Exposure
```

---

## UR-002 — Loss-Making Product Identification

The system shall identify products that are:

* Gross-loss generating
* Contribution-loss generating
* Operating-loss generating
* Net-loss generating

---

## UR-003 — Loss Ranking

Users shall be able to rank products by:

```text
Absolute Loss
Loss Per Unit
Loss Percentage
Loss Growth
Cumulative Loss
Forecast Loss
Loss Risk Score
Recoverable Loss
```

---

## UR-004 — Product Loss Comparison

Users shall be able to compare multiple products by:

```text
Revenue
Units Sold
Price
Cost
Gross Loss
Contribution Loss
Operating Loss
Net Loss
Loss Per Unit
Loss Rate
Discount Rate
Return Rate
Support Cost
Infrastructure Cost
CAC
```

---

## UR-005 — Loss Trend Analysis

Users shall be able to analyze:

* Daily loss
* Weekly loss
* Monthly loss
* Quarterly loss
* Annual loss

---

## UR-006 — Loss Driver Analysis

The AI shall identify major loss drivers.

Example:

```text
Product:
Enterprise Plan

Current Loss:
-$84,000/month

Primary Drivers:

Infrastructure Cost:
+31%

Support Cost:
+22%

Discounting:
+15%

Customer Acquisition Cost:
+12%

Low Utilization:
+9%
```

---

## UR-007 — Gross Loss Analysis

The system shall calculate:

```text
Gross Loss =
COGS - Net Revenue
```

when COGS exceeds net revenue.

---

## UR-008 — Contribution Loss Analysis

The system shall identify products where:

```text
Variable Costs > Net Revenue
```

---

## UR-009 — Operating Loss Analysis

The system shall identify products where product-attributed operating expenses exceed the configured operating contribution.

---

## UR-010 — Net Loss Analysis

Where sufficient financial data exists, the system shall calculate product-attributed net loss.

---

## UR-011 — Loss Per Unit

The system shall calculate:

```text
Loss Per Unit =
Total Product Loss / Units Sold
```

---

## UR-012 — Loss Percentage

The system shall calculate configurable loss ratios.

Example:

```text
Loss Rate =
Absolute Loss / Net Revenue × 100
```

---

## UR-013 — Loss by Customer

Users shall be able to identify customers causing:

* Direct product losses
* Low-margin revenue
* Negative contribution
* Excessive support costs
* Excessive discounts
* High returns
* High refunds

---

## UR-014 — Loss by Customer Segment

Users shall be able to analyze product loss by:

```text
Enterprise
SMB
Startup
Consumer
Strategic Account
Custom Segment
```

---

## UR-015 — Loss by Channel

The system shall analyze product losses by:

```text
Direct Sales
Partner
Reseller
Marketplace
Affiliate
Organic
Paid Advertising
Social
Other Channels
```

---

## UR-016 — Geographic Loss

Users shall be able to identify loss by:

```text
Country
Region
City
Market
Sales Territory
```

---

## UR-017 — Campaign Loss

The system shall identify campaigns contributing to product losses.

---

## UR-018 — Discount Loss

Users shall be able to determine:

```text
Discount Amount
Margin Lost
Revenue Generated
Incremental Volume
Incremental Profit/Loss
```

---

## UR-019 — Return and Refund Loss

The system shall quantify loss caused by:

```text
Returns
Refunds
Credits
Chargebacks
Warranty Claims
```

---

## UR-020 — Support-Cost Loss

The system shall identify products where support costs materially exceed acceptable thresholds.

---

## UR-021 — Infrastructure Loss

For digital products and SaaS products, the system shall identify losses caused by:

```text
Compute
Storage
Bandwidth
Database
LLM Usage
API Usage
Vector Search
Third-Party Services
```

---

## UR-022 — Acquisition-Cost Loss

The system shall identify products whose profitability becomes negative after customer acquisition costs.

---

## UR-023 — Pricing Loss

The system shall identify products where pricing is insufficient to cover applicable costs.

---

## UR-024 — Cost Increase Loss

The system shall detect products becoming loss-making due to:

* Supplier cost increases
* Infrastructure cost increases
* Labor cost increases
* Support cost increases
* Distribution cost increases
* Marketing cost increases

---

## UR-025 — Loss Forecast

The AI shall forecast potential future product losses.

---

## UR-026 — Loss Risk Detection

The AI shall identify products likely to become loss-making.

---

## UR-027 — Loss Prevention

The system shall estimate preventable or recoverable loss.

---

## UR-028 — AI Root-Cause Analysis

The AI shall explain:

```text
What happened?
When did it happen?
How large is the loss?
Why did it happen?
Which factors contributed?
Which factors are controllable?
What should be done?
```

---

## UR-029 — AI Recommendation

The AI shall recommend:

```text
REPRICE
REDUCE COST
REDUCE DISCOUNT
REDUCE CAC
OPTIMIZE SUPPORT
OPTIMIZE INFRASTRUCTURE
CHANGE CHANNEL
CHANGE TARGET SEGMENT
CHANGE PACKAGING
BUNDLE
REPOSITION
RESTRUCTURE
RETAIN
REVIEW
RETIRE
```

---

## UR-030 — Human Override

Authorized users shall be able to:

* Reject AI conclusions.
* Correct financial classifications.
* Modify assumptions.
* Override loss thresholds.
* Approve remediation.
* Reject remediation.
* Add comments.

---

## UR-031 — Loss Analysis Chat

Users shall be able to ask:

```text
Which products are losing money?

Which product is losing the most money?

Why is Product A losing money?

Which products are becoming unprofitable?

What caused the loss increase this month?

How much loss is caused by discounts?

Which customers are unprofitable?

Which channels generate product losses?

What happens if we increase Product A's price by 10%?

How much loss can we recover?

Which product should we discontinue?
```

---

## 6. System Requirements

## SR-001 — Multi-Tenant Architecture

All loss-analysis data shall be tenant-scoped.

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
ProductCost
CostComponent
CostAllocation
ProductRevenue
ProductTransaction
ProductLoss
ProductLossComponent
ProductLossDriver
ProductLossRisk
ProductLossForecast
ProductLossScenario
ProductLossInsight
ProductLossRecommendation
LossThreshold
LossAlert
LossRemediation
LossAuditEvent
```

---

## SR-003 — Revenue Model

The system shall distinguish:

```text
Gross Revenue
Discounts
Refunds
Returns
Credits
Chargebacks
Net Revenue
```

---

## SR-004 — Cost Model

The system shall distinguish:

```text
COGS
Direct Costs
Variable Costs
Fixed Costs
Indirect Costs
Allocated Costs
Unallocated Costs
Operational Costs
Marketing Costs
Sales Costs
Support Costs
Infrastructure Costs
```

---

## SR-005 — Deterministic Loss Engine

Authoritative loss calculations shall be performed by deterministic services.

The LLM shall not be the source of truth for financial calculations.

---

## SR-006 — Loss Calculation Layer

The engine shall calculate:

```text
Net Revenue
COGS
Gross Profit
Gross Loss
Contribution Profit
Contribution Loss
Operating Profit
Operating Loss
Net Profit
Net Loss
Loss Per Unit
Loss Rate
```

---

## SR-007 — Cost Allocation Engine

The system shall support:

```text
Revenue-Based
Unit-Based
Usage-Based
Activity-Based
Headcount-Based
Time-Based
Transaction-Based
Custom
```

allocation methodologies.

---

## SR-008 — Allocation Transparency

Every allocated cost shall retain:

```text
Source Cost
Allocation Rule
Allocation Driver
Allocation Amount
Period
Product
Allocation Version
```

---

## SR-009 — SaaS Loss Analysis

For SaaS products, the system shall support:

```text
Infrastructure Cost
LLM Cost
API Cost
Support Cost
CAC
Hosting Cost
Storage Cost
Bandwidth Cost
Payment Processing
```

---

## SR-010 — Subscription Loss Analysis

The system shall support:

```text
Monthly Plans
Annual Plans
Usage-Based Plans
Seat-Based Plans
Tiered Plans
Hybrid Plans
```

---

## SR-011 — Customer-Level Loss Attribution

The system shall support:

```text
Customer Revenue
Customer Discounts
Customer COGS
Customer Support Cost
Customer Infrastructure Cost
Customer CAC
Customer Contribution
Customer Loss
```

---

## SR-012 — Channel-Level Loss Attribution

The system shall support product-loss attribution by acquisition and sales channel.

---

## SR-013 — Campaign-Level Loss Attribution

Where attribution data exists, marketing costs shall be connected to product loss.

---

## SR-014 — Forecasting Engine

The system shall support:

* Time-series forecasting
* Regression
* Machine learning
* Ensemble models
* Scenario-based forecasting

---

## SR-015 — Forecast Uncertainty

Every loss forecast shall support:

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

## SR-016 — AI Loss Agent

The AI agent shall support:

```text
Intent Detection
Permission Validation
Entity Resolution
Data Retrieval
Loss Calculation
Loss Analysis
Root-Cause Analysis
Anomaly Detection
Forecasting
Scenario Simulation
Recommendation Generation
Human Escalation
```

---

## SR-017 — AI Grounding

AI conclusions shall be grounded in:

```text
Revenue Data
Cost Data
Product Data
Customer Data
Sales Data
Marketing Data
Support Data
Infrastructure Data
Calculated Loss Metrics
Forecast Results
```

---

## SR-018 — Fact / Assumption Separation

AI responses shall distinguish:

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

## SR-019 — AI Hallucination Protection

The AI shall never fabricate:

* Revenue
* Costs
* Loss
* Profit
* Pricing
* Customer losses
* Forecasts
* Transactions
* Cost allocations

---

## SR-020 — AI Tool Governance

AI tools shall be classified as:

```text
READ_ONLY
LOW_RISK_WRITE
HIGH_RISK_WRITE
FINANCIAL
DESTRUCTIVE
```

---

## SR-021 — Human-in-the-Loop

Human approval shall be required for configured material actions including:

```text
Product Retirement
Material Price Changes
Major Cost Changes
Financial Policy Changes
Large Budget Changes
Product-Level Financial Data Changes
```

---

## SR-022 — Auditability

The system shall record:

```text
Actor
Tenant
Organization
Product
Data Source
Calculation Version
AI Agent
AI Model
Model Version
Recommendation
Approval
Override
Timestamp
```

---

## 7. Functional Requirements

## FR-001 — Product Loss Registration

The system shall create and maintain loss records for products and SKUs.

---

## FR-002 — Revenue Ingestion

The system shall ingest product revenue from supported:

* CRM systems
* Billing systems
* Payment platforms
* ERP systems
* E-commerce systems
* Subscription systems

---

## FR-003 — Cost Ingestion

The system shall ingest product-related costs.

---

## FR-004 — Product Mapping

Transactions shall be mapped to products using:

```text
Product ID
SKU
Order ID
Subscription ID
Invoice ID
Transaction ID
```

and other configured identifiers.

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
Chargebacks
```

---

## FR-008 — Gross Loss Calculation

The system shall calculate:

```text
Gross Loss =
COGS - Net Revenue
```

when COGS exceeds net revenue.

---

## FR-009 — Contribution Loss Calculation

The system shall calculate:

```text
Contribution Loss =
Variable Costs - Net Revenue
```

when variable costs exceed net revenue.

---

## FR-010 — Operating Loss Calculation

The system shall calculate product-attributed operating losses according to configured allocation rules.

---

## FR-011 — Net Loss Calculation

Where sufficient data exists, the system shall calculate product-attributed net losses.

---

## FR-012 — Loss Per Unit

The system shall calculate:

```text
Loss Per Unit =
Absolute Product Loss / Units Sold
```

and preserve loss sign separately.

---

## FR-013 — Loss Rate

The system shall calculate:

```text
Loss Rate =
Absolute Loss / Net Revenue × 100
```

---

## FR-014 — Product Loss Ranking

Products shall be rankable by:

```text
Absolute Loss
Loss Per Unit
Loss Rate
Loss Growth
Forecast Loss
Recoverable Loss
Risk Score
```

---

## FR-015 — Loss Trend Detection

The system shall detect:

* Increasing losses
* Decreasing losses
* Stable losses
* Sudden loss spikes
* Persistent losses
* Recurring losses

---

## FR-016 — Loss Anomaly Detection

The AI shall detect unusual:

* Cost spikes
* Revenue drops
* Price changes
* Discount increases
* Return spikes
* Refund spikes
* Support-cost increases
* Infrastructure-cost increases
* Customer-mix changes
* Channel-mix changes

---

## FR-017 — Root-Cause Analysis

The AI shall rank contributing factors based on available evidence.

Example:

```text
Product Loss Increase: $42,000

Estimated Drivers:

Infrastructure Cost:
38%

Support Cost:
24%

Discounting:
17%

CAC:
12%

Returns:
9%
```

The system shall clearly label estimates versus deterministic calculations.

---

## FR-018 — Loss Attribution

The system shall attribute loss across:

```text
Product
SKU
Customer
Customer Segment
Channel
Campaign
Geography
Salesperson
Subscription Plan
```

where sufficient data exists.

---

## FR-019 — Pricing Loss Analysis

The system shall identify products where price does not sufficiently cover applicable costs.

---

## FR-020 — Discount Loss Analysis

The system shall calculate the financial impact of discounts.

---

## FR-021 — Return Loss Analysis

The system shall calculate loss resulting from product returns.

---

## FR-022 — Refund Loss Analysis

The system shall calculate refund-related product losses.

---

## FR-023 — Support Loss Analysis

The system shall calculate loss associated with product support activity.

---

## FR-024 — Infrastructure Loss Analysis

The system shall calculate product-level infrastructure losses for digital products.

---

## FR-025 — Acquisition Loss Analysis

The system shall incorporate CAC into configurable product-loss analysis.

---

## FR-026 — Customer Loss Analysis

The system shall identify customers generating negative contribution for specific products.

---

## FR-027 — Channel Loss Analysis

The system shall identify sales and acquisition channels that generate negative product contribution.

---

## FR-028 — Geographic Loss Analysis

The system shall identify geographic markets where products are loss-making.

---

## FR-029 — Campaign Loss Analysis

The system shall identify marketing campaigns associated with product losses where attribution data is available.

---

## FR-030 — Loss Forecast

The system shall forecast future:

```text
Product Loss
Loss Rate
Loss Per Unit
Cumulative Loss
```

---

## FR-031 — Loss Risk Forecast

The system shall identify products with a high probability of becoming loss-making.

---

## FR-032 — Break-Even Analysis

The system shall calculate the conditions required for a loss-making product to reach break-even.

---

## FR-033 — Break-Even Units

Where applicable:

```text
Break-Even Units =
Fixed Costs /
Contribution Margin Per Unit
```

---

## FR-034 — Price Recovery Simulation

Users shall be able to simulate price increases required to reduce or eliminate loss.

---

## FR-035 — Cost Reduction Simulation

Users shall be able to simulate:

```text
COGS Reduction
Support Cost Reduction
Infrastructure Cost Reduction
Marketing Cost Reduction
CAC Reduction
```

---

## FR-036 — Volume Simulation

Users shall be able to simulate changes in sales volume.

---

## FR-037 — Discount Simulation

Users shall be able to simulate different discount levels.

---

## FR-038 — Combined Loss Scenario

The system shall support combined scenarios:

```text
Price
Volume
Cost
Discount
CAC
Support Cost
Infrastructure Cost
Return Rate
Refund Rate
```

---

## FR-039 — Loss Recovery Estimation

The system shall estimate potentially recoverable loss.

Example:

```text
Current Annual Loss:
$1,200,000

Estimated Recoverable Loss:
$680,000

Recovery Opportunities:

Pricing:
$260,000

Infrastructure:
$180,000

Support:
$110,000

Discount Optimization:
$90,000

Confidence:
82%
```

---

## FR-040 — Product Retirement Analysis

The AI may recommend product retirement when configured conditions are met.

The system shall compare:

```text
Current Loss
Expected Future Loss
Retirement Cost
Customer Impact
Contractual Impact
Strategic Value
Migration Cost
Expected Savings
```

---

## FR-041 — Product Repricing Recommendation

The AI shall recommend pricing changes based on:

```text
Current Loss
Unit Economics
Cost Structure
Demand Data
Historical Pricing
Customer Sensitivity
Competitive Data
```

where available.

---

## FR-042 — Cost Optimization Recommendation

The AI shall identify cost-reduction opportunities.

---

## FR-043 — Channel Optimization Recommendation

The AI shall recommend shifting product sales toward channels with stronger contribution economics.

---

## FR-044 — Customer Optimization Recommendation

The AI shall identify:

```text
High-Loss Customers
Low-Margin Customers
High-Support Customers
High-Discount Customers
High-Return Customers
```

---

## FR-045 — Product Packaging Recommendation

The AI may recommend:

```text
Bundle
Unbundle
Change Features
Change Usage Limits
Change Service Tier
Change Support Level
Change Pricing Model
```

---

## FR-046 — AI Loss Chat

The AI shall answer natural-language loss-analysis questions.

---

## FR-047 — AI Query Planning

The AI shall translate user requests into validated analytical operations.

---

## FR-048 — Permission Enforcement

All AI queries shall enforce:

```text
Authentication
Authorization
Tenant Isolation
Organization Scope
Product Permissions
Financial Permissions
```

---

## FR-049 — Loss Alerts

Users shall be able to configure alerts for:

```text
Product Becomes Loss-Making
Loss Exceeds Threshold
Loss Increases by X%
Margin Falls Below Threshold
Cost Increases by X%
Loss Forecast Exceeds Threshold
Loss Risk Becomes High
```

---

## FR-050 — Alert Severity

Alerts shall support:

```text
INFO
LOW
MEDIUM
HIGH
CRITICAL
```

---

## FR-051 — Loss Reports

The system shall generate:

```text
Product Loss Report
SKU Loss Report
Loss Driver Report
Loss Trend Report
Customer Loss Report
Channel Loss Report
Campaign Loss Report
Geographic Loss Report
Loss Forecast Report
Loss Risk Report
Loss Recovery Report
Loss Scenario Report
AI Recommendation Report
```

---

## FR-052 — Scheduled Reports

Users shall be able to schedule:

```text
Daily Loss Summary
Weekly Loss Report
Monthly Product Loss Report
Quarterly Loss Review
Monthly Loss Risk Report
Monthly Loss Recovery Report
```

---

## FR-053 — Export

Authorized users shall be able to export:

* Loss records
* Loss metrics
* Product rankings
* Forecasts
* Scenarios
* AI insights
* Recommendations

---

## FR-054 — Human Approval Workflow

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

## FR-055 — Remediation Tracking

Each approved remediation shall support:

```text
Owner
Action
Deadline
Expected Loss Reduction
Actual Loss Reduction
Status
Outcome
Variance
```

---

## FR-056 — Recommendation Outcome Tracking

The system shall compare:

```text
Expected Loss Reduction
Actual Loss Reduction
Expected Margin Improvement
Actual Margin Improvement
Expected Revenue Impact
Actual Revenue Impact
```

---

## 8. AI Product Loss Analysis Agent

## Agent Responsibilities

The AI Product Loss Analysis Agent shall:

1. Understand loss-related questions.
2. Resolve products and SKUs.
3. Validate permissions.
4. Retrieve financial data.
5. Invoke deterministic calculations.
6. Detect loss patterns.
7. Identify root causes.
8. Forecast future losses.
9. Simulate remediation scenarios.
10. Generate evidence-backed recommendations.
11. Escalate material decisions.
12. Track recommendation outcomes.

---

## 9. AI Agent Workflow

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
Revenue/Cost Reconciliation
     ↓
Deterministic Loss Calculation
     ↓
Loss Attribution
     ↓
Trend Analysis
     ↓
Anomaly Detection
     ↓
Root-Cause Analysis
     ↓
Forecasting
     ↓
Scenario Simulation
     ↓
AI Recommendation
     ↓
Evidence Validation
     ↓
Human Approval
     ↓
Remediation
     ↓
Outcome Measurement
```

---

## 10. MCP Tools

The Product Loss Agent may expose:

```text
loss.search_products
loss.get_product
loss.get_product_loss
loss.get_product_revenue
loss.get_product_costs
loss.get_product_cogs
loss.get_variable_costs
loss.get_fixed_costs
loss.get_allocated_costs

loss.calculate_gross_loss
loss.calculate_contribution_loss
loss.calculate_operating_loss
loss.calculate_net_loss
loss.calculate_loss_per_unit
loss.calculate_loss_rate

loss.compare_products
loss.get_loss_trends
loss.detect_loss_anomalies
loss.analyze_loss_drivers
loss.analyze_customer_loss
loss.analyze_channel_loss
loss.analyze_campaign_loss
loss.analyze_geographic_loss

loss.forecast_loss
loss.calculate_break_even
loss.create_loss_scenario
loss.compare_loss_scenarios
loss.estimate_recoverable_loss

loss.generate_loss_insight
loss.generate_recommendation
loss.generate_report
```

All write-capable tools shall require explicit authorization.

---

## 11. AI Guardrails

## AI-GR-001 — No Fabricated Loss

The AI shall never fabricate:

```text
Revenue
Costs
Loss
Margins
Customers
Transactions
Forecasts
Financial Events
```

---

## AI-GR-002 — Deterministic Calculations

All authoritative loss calculations shall originate from deterministic financial services.

---

## AI-GR-003 — Evidence Grounding

Every material AI conclusion shall be supported by:

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

AI-generated analysis shall expose:

```text
Confidence
Data Completeness
Data Freshness
Evidence Strength
Forecast Uncertainty
```

when applicable.

---

## AI-GR-005 — Fact and Inference Separation

The interface shall distinguish:

```text
ACTUAL
CALCULATED
ESTIMATED
FORECAST
AI INFERENCE
SCENARIO
RECOMMENDATION
```

---

## AI-GR-006 — Financial Action Restrictions

The AI shall not independently:

* Retire products.
* Change financial records.
* Change accounting policies.
* Change production pricing.
* Modify major budgets.
* Approve financial adjustments.

without appropriate authorization.

---

## 12. Product Loss Risk Engine

The system shall calculate loss risk using:

```text
Current Loss
Loss Growth
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
Customer Concentration
Channel Concentration
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
  "loss_risk_score": 0.91,
  "risk_level": "CRITICAL",
  "current_monthly_loss": 84000,
  "forecast_annual_loss": 1050000,
  "primary_drivers": [
    "infrastructure_cost_growth",
    "discounting",
    "support_cost_growth"
  ],
  "recoverable_loss_estimate": 620000,
  "human_review_required": true
}
```

---

## 13. Loss Classification Framework

## Critical Loss Product

```text
High Current Loss
High Future Loss
High Loss Growth
```

Recommended action:

```text
IMMEDIATE REVIEW
```

---

## Structural Loss Product

```text
Persistent Negative Contribution
```

Recommended action:

```text
RESTRUCTURE
REPRICE
REDUCE COST
```

---

## Temporary Loss Product

```text
Short-Term Loss
Strong Recovery Indicators
```

Recommended action:

```text
MONITOR
OPTIMIZE
```

---

## Strategic Loss Product

```text
Current Loss
High Strategic Value
High Future Potential
```

Recommended action:

```text
INVESTIGATE
CONTROL LOSS
RETAIN
```

---

## 14. Loss Recovery Intelligence

The platform shall identify loss-recovery opportunities.

```text
Current Loss
     ↓
Loss Drivers
     ↓
Controllable Drivers
     ↓
Recovery Opportunities
     ↓
Scenario Simulation
     ↓
Expected Loss Reduction
     ↓
Implementation Cost
     ↓
Net Recovery
```

The system shall prioritize recovery opportunities by:

```text
Expected Loss Reduction
Implementation Cost
Time to Impact
Confidence
Risk
Strategic Impact
```

---

## 15. Loss Scenario Engine

The scenario engine shall support:

```text
PRICE INCREASE
PRICE DECREASE
COST REDUCTION
COST INCREASE
DISCOUNT REDUCTION
VOLUME INCREASE
VOLUME DECREASE
CAC REDUCTION
SUPPORT COST REDUCTION
INFRASTRUCTURE COST REDUCTION
RETURN RATE REDUCTION
REFUND RATE REDUCTION
CHANNEL MIX CHANGE
CUSTOMER MIX CHANGE
```

Example:

```text
Current Annual Loss:
-$1,000,000

Scenario:
Price +8%
Discount -3%
Infrastructure Cost -10%

Projected Annual Loss:
-$310,000

Estimated Loss Reduction:
$690,000

Confidence:
79%
```

Scenario results shall not modify actual financial records.

---

## 16. Product Loss Forecasting

The system shall forecast:

```text
Future Monthly Loss
Future Quarterly Loss
Future Annual Loss
Cumulative Loss
Loss Probability
Loss Rate
Loss Per Unit
```

Every forecast shall contain:

```text
Model
Model Version
Training Window
Forecast Horizon
Prediction Interval
Assumptions
Confidence
Generated At
```

---

## 17. Forecast Evaluation

The platform shall monitor:

```text
MAE
RMSE
MAPE
Forecast Bias
Prediction Interval Coverage
Forecast Stability
```

---

## 18. Data Quality Requirements

The system shall detect:

```text
Missing Product Mapping
Missing Revenue
Missing Costs
Duplicate Transactions
Duplicate Revenue
Incorrect Product Mapping
Invalid Pricing
Invalid Cost
Negative Cost Anomalies
Missing Currency
Stale Data
Revenue/Payment Mismatch
Cost/Invoice Mismatch
Unallocated Costs
Incomplete Customer Attribution
Incomplete Campaign Attribution
```

Material data-quality issues shall reduce analytical confidence.

---

## 19. Product Loss Data Lineage

Users shall be able to drill down:

```text
AI Recommendation
       ↓
Loss Insight
       ↓
Loss Metric
       ↓
Loss Calculation
       ↓
Revenue + Cost Components
       ↓
Transactions
       ↓
Original Source
```

---

## 20. Multi-Agent Collaboration

The Product Loss Analysis Agent shall integrate with:

```text
Product Profitability Agent
Revenue Analytics Agent
Expense Tracking Agent
Cash Flow Analysis Agent
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
Revenue Analytics Agent
        ↓
Revenue increased 12%

Expense Tracking Agent
        ↓
Infrastructure cost increased 34%

Marketing Analytics Agent
        ↓
CAC increased 21%

Customer Intelligence Agent
        ↓
New customers have significantly higher support requirements

        ↓

Product Loss Agent
        ↓

Contribution loss increased 18%.

        ↓

AI Strategy Agent
        ↓

Recommend pricing, support, and infrastructure optimization.
```

---

## 21. API-Level Functional Domains

The service shall expose logically separated API domains:

```text
/products/{product_id}/loss
/products/{product_id}/loss/trends
/products/{product_id}/loss/drivers
/products/{product_id}/loss/risks
/products/{product_id}/loss/forecast
/products/{product_id}/loss/scenarios
/products/{product_id}/loss/recovery
/products/{product_id}/loss/recommendations

/loss/overview
/loss/products
/loss/customers
/loss/segments
/loss/channels
/loss/campaigns
/loss/geographies
/loss/anomalies
/loss/forecasts
/loss/scenarios
/loss/recovery
/loss/reports
```

Every endpoint shall enforce:

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

## 22. Observability Requirements

The system shall monitor:

```text
Loss Calculation Latency
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
AI Agent
Tool Calls
Database Queries
Loss Calculations
AI Calls
Final Response
```

---

## 23. Reliability Requirements

The module shall support:

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

If AI services become unavailable, deterministic loss calculations and standard loss reporting shall remain operational whenever the required financial data is available.

---

## 24. Performance Requirements

Interactive operations shall prioritize low latency for:

```text
Product Loss Dashboard
Loss-Making Product Search
Loss Rankings
Current Loss Metrics
Standard Loss Queries
```

Asynchronous processing shall be used for:

```text
Large Historical Analysis
Portfolio Loss Analysis
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

AI agents shall never access financial information beyond the execution identity's permissions.

---

## 26. Audit Requirements

Every material loss-analysis action shall record:

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

SalesGenie shall evaluate the Product Loss Agent using:

```text
Loss Calculation Accuracy
Revenue Attribution Accuracy
Cost Attribution Accuracy
Loss Driver Accuracy
Loss Classification Accuracy
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

## 28. Loss Recommendation Framework

Every recommendation shall contain:

```text
Recommendation ID
Product ID
Recommendation Type
Current Loss
Loss Driver
Evidence
Root Cause
Recommended Action
Expected Loss Reduction
Expected Revenue Impact
Expected Cost Impact
Expected Margin Impact
Implementation Cost
Time to Impact
Confidence
Risk
Assumptions
Owner
Approval Requirement
Status
Created At
```

Example:

```text
Recommendation:
Reduce infrastructure cost for Product A.

Current Annual Loss:
$840,000

Primary Evidence:
Infrastructure cost per active customer increased 31%.

Recommended Action:
Optimize infrastructure utilization and expensive workloads.

Expected Annual Loss Reduction:
$210,000

Expected Remaining Loss:
$630,000

Confidence:
88%

Risk:
LOW

Owner:
Engineering + Product + Finance

Approval:
Finance Manager
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

## 30. Remediation Management

Approved remediation actions shall support:

```text
Remediation ID
Product ID
Loss Problem
Root Cause
Action
Owner
Deadline
Expected Loss Reduction
Actual Loss Reduction
Expected Cost
Actual Cost
Expected ROI
Actual ROI
Status
Outcome
Variance
```

---

## 31. Product Retirement Decision Framework

Before recommending retirement, the AI shall analyze:

```text
Current Annual Loss
Forecast Annual Loss
Loss Growth
Strategic Value
Customer Dependency
Contractual Obligations
Migration Cost
Support Cost
Retirement Cost
Expected Savings
Revenue Cannibalization
Alternative Products
```

The AI shall not autonomously retire a product.

---

## 32. Product Loss KPI Framework

The platform shall support:

```text
Total Product Loss
Gross Loss
Contribution Loss
Operating Loss
Net Loss
Loss Per Unit
Loss Rate
Loss Growth
Cumulative Loss
Forecast Loss
Loss Exposure
Recoverable Loss
Loss Recovery Rate
Loss Risk Score
Loss-Making Product Count
Loss-Making SKU Count
Loss Concentration
Loss by Customer
Loss by Segment
Loss by Channel
Loss by Geography
Loss by Campaign
Discount-Driven Loss
Return-Driven Loss
Refund-Driven Loss
Support-Driven Loss
Infrastructure-Driven Loss
CAC-Driven Loss
```

---

## 33. FAANG-Level Decision Framework

SalesGenie shall convert product-loss data into a continuous loss-management system:

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
                 SUPPORT DATA
                        +
              INFRASTRUCTURE DATA
                        ↓
                  DATA QUALITY
                        ↓
                 RECONCILIATION
                        ↓
             DETERMINISTIC LOSS ENGINE
                        ↓
                LOSS CLASSIFICATION
                        ↓
              PRODUCT LOSS ANALYSIS
                        ↓
          CUSTOMER / CHANNEL / SEGMENT
                    ANALYSIS
                        ↓
                TREND ANALYSIS
                        ↓
              ANOMALY DETECTION
                        ↓
              ROOT-CAUSE ANALYSIS
                        ↓
                LOSS FORECASTING
                        ↓
              SCENARIO SIMULATION
                        ↓
             AI LOSS INTELLIGENCE
                        ↓
            RECOVERY OPPORTUNITIES
                        ↓
           AI RECOMMENDATIONS
                        ↓
              HUMAN APPROVAL
                        ↓
               REMEDIATION
                        ↓
              OUTCOME TRACKING
                        ↓
               AI EVALUATION
```

---

## 34. Acceptance Criteria

The module shall be considered production-ready only when:

* [ ] Products and SKUs can be registered.
* [ ] Product revenue can be ingested.
* [ ] Product costs can be ingested.
* [ ] Product transactions can be mapped.
* [ ] Revenue can be reconciled.
* [ ] Costs can be classified.
* [ ] Costs can be allocated.
* [ ] Gross loss can be calculated deterministically.
* [ ] Contribution loss can be calculated deterministically.
* [ ] Operating loss can be calculated.
* [ ] Net loss can be calculated where sufficient data exists.
* [ ] Loss per unit can be calculated.
* [ ] Loss rate can be calculated.
* [ ] Loss-making products can be identified.
* [ ] Loss-making SKUs can be identified.
* [ ] Products can be ranked by loss.
* [ ] Product loss trends can be analyzed.
* [ ] Loss anomalies can be detected.
* [ ] Loss drivers can be identified.
* [ ] Loss can be analyzed by customer.
* [ ] Loss can be analyzed by segment.
* [ ] Loss can be analyzed by channel.
* [ ] Loss can be analyzed by geography.
* [ ] Loss can be analyzed by campaign where attribution exists.
* [ ] Discount-driven loss can be analyzed.
* [ ] Return-driven loss can be analyzed.
* [ ] Refund-driven loss can be analyzed.
* [ ] Support-driven loss can be analyzed.
* [ ] Infrastructure-driven loss can be analyzed.
* [ ] CAC-driven loss can be analyzed.
* [ ] Product loss forecasting is supported.
* [ ] Loss risk forecasting is supported.
* [ ] Break-even analysis is supported.
* [ ] Loss recovery estimation is supported.
* [ ] Price recovery scenarios are supported.
* [ ] Cost reduction scenarios are supported.
* [ ] Volume scenarios are supported.
* [ ] Discount scenarios are supported.
* [ ] Combined scenarios are supported.
* [ ] Scenario calculations cannot modify actual financial records.
* [ ] AI loss analysis is grounded in actual data.
* [ ] AI cannot fabricate financial values.
* [ ] Deterministic calculations remain authoritative.
* [ ] AI distinguishes actuals, calculations, estimates, forecasts, and recommendations.
* [ ] AI recommendations contain evidence.
* [ ] AI recommendations contain expected financial impact.
* [ ] AI recommendations contain confidence and risk.
* [ ] Material financial actions require human approval.
* [ ] Loss remediation can be tracked.
* [ ] Expected versus actual loss recovery can be measured.
* [ ] Product retirement analysis is supported.
* [ ] AI tool permissions are enforced.
* [ ] Tenant isolation is enforced.
* [ ] RBAC is enforced server-side.
* [ ] MCP tools are schema validated.
* [ ] AI execution budgets are enforced.
* [ ] All material financial operations are audited.
* [ ] Complete loss-data lineage is available.
* [ ] Forecast model versions are tracked.
* [ ] AI model versions are tracked.
* [ ] AI cost and latency are observable.
* [ ] Data-quality issues are detectable.
* [ ] Financial ingestion is idempotent.
* [ ] Integration failures are recoverable.
* [ ] Deterministic loss reporting remains available during AI-provider failures.
* [ ] Unit tests cover loss calculations.
* [ ] Integration tests cover financial data flows.
* [ ] Security tests cover tenant isolation.
* [ ] AI evaluation tests cover grounding and hallucination resistance.
* [ ] Load tests cover high-volume product-loss analysis.
* [ ] Auditability tests pass.
* [ ] Human approval workflows are tested.
* [ ] Loss-remediation outcome tracking is tested.

---

## 35. Core Product Principle

> **SalesGenie's AI-Based Product Loss Analysis module shall not merely identify products with negative profit. It shall determine the magnitude, persistence, source, controllability, and future risk of product losses; connect those losses to revenue, pricing, costs, customers, channels, campaigns, support, infrastructure, and operational behavior; use deterministic financial services as the source of truth; use AI for root-cause analysis, forecasting, scenario modeling, risk detection, and optimization; and maintain human control over material financial decisions.**
