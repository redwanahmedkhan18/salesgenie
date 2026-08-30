# SalesGenie — Custom Report Builder

## FAANG-Level User Requirements, System Requirements & Functional Requirements

### AI + Human Collaborative Custom Reporting Platform

---

## 1. Module Overview

The **Custom Report Builder** is an enterprise-grade reporting composition system within SalesGenie that enables users and AI agents to create highly configurable analytical reports from multiple business data sources.

The module shall support:

- Human-created reports
- AI-generated reports
- AI-assisted report design
- Human + AI collaborative report creation
- Drag-and-drop report composition
- Natural-language report creation
- Multi-source data analysis
- Custom metrics
- Calculated fields
- Filters
- Dimensions
- Measures
- Charts
- Tables
- KPIs
- Pivot views
- Funnels
- Cohort analysis
- Time-series analysis
- Forecast visualizations
- AI-generated narratives
- AI-generated insights
- AI-generated recommendations
- Report templates
- Report versioning
- Report sharing
- Report permissions
- Report scheduling
- Report export
- Report embedding
- Real-time and asynchronous execution

The system shall integrate with SalesGenie's:

```text
Sales
Marketing
Advertising
SEO
Finance
Product
Support
Customer
Lead Intelligence
Business Intelligence
Revenue Analytics
Profitability Analytics
AI Analytics
Executive Analytics
Scheduled Reports
Report Export Engine
Dashboard System
Data Integration Layer
```

---

## 2. Primary Objectives

The Custom Report Builder shall:

1. Allow users to create reports without writing SQL.
2. Allow advanced users to construct sophisticated analytical queries.
3. Allow AI agents to generate reports from natural-language instructions.
4. Allow users to modify AI-generated reports visually.
5. Allow AI to recommend metrics and visualizations.
6. Allow reports to combine multiple authorized data sources.
7. Provide deterministic and reproducible report definitions.
8. Support reusable report templates.
9. Support organization-level report governance.
10. Support enterprise RBAC.
11. Support multi-tenant isolation.
12. Support secure data access.
13. Support calculated metrics.
14. Support custom formulas.
15. Support conditional logic.
16. Support advanced filtering.
17. Support dynamic date ranges.
18. Support interactive visualizations.
19. Support AI-generated explanations.
20. Support AI-generated anomaly detection.
21. Support AI-generated recommendations.
22. Support report versioning.
23. Support collaboration.
24. Support approval workflows.
25. Support scheduled execution.
26. Support export to enterprise formats.
27. Support report sharing and embedding.
28. Support high-volume analytical workloads.
29. Provide complete observability.
30. Provide auditable report lineage.

---

## 3. Target Users

## 3.1 Super Admin

Super Admin shall be able to:

* Manage global report policies.
* Manage report templates.
* Manage report permissions.
* View all reports subject to authorization.
* Manage tenant reporting quotas.
* Configure data-access policies.
* Configure AI report-generation policies.
* Configure sensitive-data restrictions.
* Audit report activity.
* Disable problematic reports.
* Monitor report execution performance.

---

## 3.2 Organization Admin

Organization Admin shall be able to:

* Create organization reports.
* Manage shared reports.
* Manage report permissions.
* Approve AI-generated reports.
* Publish report templates.
* Manage department-level reports.
* Control external sharing.

---

## 3.3 Business Analyst

Business analysts shall be able to:

* Build complex reports.
* Join authorized data sources.
* Create calculated metrics.
* Configure dimensions.
* Create custom formulas.
* Build charts.
* Build dashboards.
* Save reusable reports.
* Clone existing reports.
* Compare metrics.

---

## 3.4 Sales Manager

Sales managers shall be able to build:

* Sales performance reports.
* Pipeline reports.
* Lead conversion reports.
* Agent performance reports.
* Revenue reports.
* Forecast reports.
* Regional sales reports.

---

## 3.5 Marketing Manager

Marketing managers shall be able to build:

* Campaign reports.
* Channel performance reports.
* Audience reports.
* Attribution reports.
* Advertising reports.
* SEO reports.
* Marketing ROI reports.

---

## 3.6 Finance Manager

Finance users shall be able to build:

* Revenue reports.
* Expense reports.
* Profit/loss reports.
* Cash-flow reports.
* Budget reports.
* Forecast reports.
* Product profitability reports.

---

## 3.7 Executive

Executives shall be able to create or consume:

* Executive reports.
* Business health reports.
* Revenue reports.
* Profitability reports.
* Growth reports.
* Strategic KPI reports.
* AI-generated decision reports.

---

## 4. User Requirements

## 4.1 Report Creation

## UR-001

Users shall be able to create a custom report from scratch.

A report shall contain:

```text
Report Name
Description
Data Sources
Fields
Dimensions
Measures
Filters
Calculated Fields
Grouping
Sorting
Visualization
Formatting
AI Configuration
Permissions
Sharing Configuration
```

---

## 4.2 Blank Report

## UR-002

Users shall be able to start with a blank report canvas.

---

## 4.3 Template-Based Report

## UR-003

Users shall be able to create reports from:

* System templates
* Organization templates
* Personal templates
* AI-generated templates
* Existing reports

---

## 4.4 Clone Report

## UR-004

Users shall be able to clone an existing report while preserving the original report.

---

## 4.5 Natural-Language Report Creation

## UR-005

Users shall be able to describe a report using natural language.

Examples:

```text
Create a monthly sales report showing revenue,
conversion rate, pipeline value, and top-performing sales agents.

Create a marketing report comparing Facebook, Google,
LinkedIn, and TikTok campaign ROI for the last 90 days.

Show product profitability by region and identify products
whose margin decreased by more than 10%.
```

---

## 4.6 AI Report Generation

## UR-006

AI shall convert natural-language requirements into a structured report definition.

The AI shall identify:

```text
Data Sources
Metrics
Dimensions
Filters
Date Range
Grouping
Sorting
Visualization
Calculated Fields
Narrative Requirements
```

---

## 4.7 AI Report Recommendations

## UR-007

AI shall recommend:

* Relevant metrics
* Relevant dimensions
* Appropriate charts
* Filters
* Comparisons
* Date ranges
* Calculated metrics
* KPI thresholds

---

## 4.8 Human + AI Collaboration

## UR-008

Users shall be able to interactively refine AI-generated reports.

Example:

```text
User:
Create a sales report.

AI:
Creates initial report.

User:
Add conversion rate.

AI:
Adds conversion-rate metric.

User:
Group by region.

AI:
Updates report.

User:
Show the top five regions.

AI:
Adds ranking and limit.

User:
Use a bar chart.

AI:
Changes visualization.
```

---

## 4.9 Report Canvas

## UR-009

Users shall have a visual report canvas containing configurable components.

Supported components shall include:

```text
KPI Card
Table
Pivot Table
Bar Chart
Line Chart
Area Chart
Pie Chart
Donut Chart
Scatter Plot
Funnel
Heatmap
Gauge
Map
Histogram
Box Plot
Cohort Chart
Waterfall
Sankey
Text
AI Insight
AI Recommendation
```

---

## 4.10 Drag-and-Drop

## UR-010

Users shall be able to drag report components into the report canvas.

---

## 4.11 Resize Components

## UR-011

Users shall be able to resize report components.

---

## 4.12 Reorder Components

## UR-012

Users shall be able to reorder report components.

---

## 4.13 Data Sources

## UR-013

Users shall be able to select authorized data sources.

Examples:

```text
CRM
Sales
Marketing
Advertising
Finance
Support
Product
Customer
Lead Intelligence
Analytics
External Integrations
```

---

## 4.14 Multi-Source Reports

## UR-014

Users shall be able to combine multiple authorized data sources.

Example:

```text
Advertising Spend
+
Leads
+
Customers
+
Revenue
=
Campaign ROI Report
```

---

## 4.15 Field Selection

## UR-015

Users shall be able to select:

```text
Dimensions
Measures
Attributes
Identifiers
Dates
Categories
```

---

## 4.16 Search Fields

## UR-016

Users shall be able to search available fields.

---

## 4.17 Field Metadata

## UR-017

Users shall be able to view:

```text
Field Name
Description
Data Type
Source
Sensitivity
Example Value
Allowed Operations
```

---

## 4.18 Filters

## UR-018

Users shall be able to create filters.

Examples:

```text
Revenue > 100000
Country = Bangladesh
Campaign = Active
ROI < 2
Conversion Rate > 10%
Product Category = SaaS
```

---

## 4.19 Advanced Filter Logic

## UR-019

Users shall be able to create:

```text
AND
OR
NOT
Nested Conditions
```

---

## 4.20 Dynamic Filters

## UR-020

Users shall be able to configure dynamic filters.

Examples:

```text
Current User
Current Organization
Current Month
Previous Month
Current Quarter
Last 30 Days
Last 90 Days
```

---

## 4.21 Date Filters

## UR-021

Users shall be able to configure:

```text
Today
Yesterday
This Week
Last Week
This Month
Last Month
This Quarter
Last Quarter
This Year
Last Year
Custom Range
Rolling Window
```

---

## 4.22 Calculated Fields

## UR-022

Users shall be able to create calculated fields.

Examples:

```text
Profit = Revenue - Expenses

ROI = (Revenue - Cost) / Cost

Conversion Rate = Converted Leads / Total Leads

Average Deal Size = Revenue / Closed Deals
```

---

## 4.23 Formula Builder

## UR-023

Users shall be able to create formulas using:

```text
Arithmetic
Conditional Logic
Aggregation
Date Functions
String Functions
Statistical Functions
Percentage Functions
Financial Functions
```

---

## 4.24 AI Formula Generation

## UR-024

Users shall be able to ask AI to create formulas.

Example:

```text
Create a metric for customer acquisition cost.
```

AI shall generate the corresponding calculation using authorized fields.

---

## 4.25 Validation

## UR-025

The system shall validate formulas before execution.

---

## 4.26 Grouping

## UR-026

Users shall be able to group data by:

```text
Region
Country
Product
Campaign
Sales Agent
Customer Segment
Month
Quarter
Year
```

---

## 4.27 Sorting

## UR-027

Users shall be able to sort:

```text
Ascending
Descending
Top N
Bottom N
```

---

## 4.28 Ranking

## UR-028

Users shall be able to create ranked reports.

Examples:

```text
Top 10 Products
Top 5 Sales Agents
Bottom 10 Campaigns
Top 20 Customers
```

---

## 4.29 Aggregation

## UR-029

Users shall be able to use:

```text
SUM
COUNT
COUNT DISTINCT
AVERAGE
MIN
MAX
MEDIAN
PERCENTILE
STANDARD DEVIATION
```

---

## 4.30 Comparison

## UR-030

Users shall be able to compare:

```text
Current vs Previous Period
Current vs Same Period Last Year
Actual vs Target
Actual vs Forecast
Product vs Product
Region vs Region
Campaign vs Campaign
```

---

## 4.31 Visualization Configuration

## UR-031

Users shall be able to configure:

```text
Chart Type
Axis
Legend
Labels
Grouping
Aggregation
Sorting
Thresholds
Tooltips
Formatting
```

---

## 4.32 KPI Components

## UR-032

Users shall be able to create KPI cards containing:

```text
Value
Target
Variance
Percentage Change
Trend
Status
```

---

## 4.33 Conditional Formatting

## UR-033

Users shall be able to configure rules such as:

```text
Revenue < Target → Warning

ROI < 1 → Critical

Profit Margin > 30% → Positive
```

---

## 4.34 AI Narrative

## UR-034

Users shall be able to enable AI-generated report narratives.

The narrative shall explain:

```text
What happened
Why it happened
What changed
What matters
What requires attention
```

---

## 4.35 AI Insights

## UR-035

Users shall be able to add an AI Insight component to reports.

---

## 4.36 AI Recommendations

## UR-036

Users shall be able to include AI recommendations.

Example:

```text
Reduce spend on underperforming campaigns.

Increase budget for high-ROAS campaigns.

Investigate declining regional conversion rates.
```

---

## 4.37 AI Anomaly Detection

## UR-037

Users shall be able to enable anomaly detection.

---

## 4.38 AI Forecasting

## UR-038

Users shall be able to add forecasts to reports where supported.

---

## 4.39 Explainability

## UR-039

AI-generated insights shall provide:

```text
Evidence
Source Metrics
Reasoning
Confidence
Time Range
```

where applicable.

---

## 4.40 Data Provenance

## UR-040

Users shall be able to inspect where report values originated.

---

## 4.41 Report Preview

## UR-041

Users shall be able to preview reports before saving.

---

## 4.42 Query Preview

## UR-042

Advanced users shall be able to inspect the logical query generated by the builder.

---

## 4.43 SQL Transparency

## UR-043

Where supported, the system may display generated SQL or an equivalent logical query representation.

Users shall not be allowed to bypass authorization through custom query execution.

---

## 4.44 Save Report

## UR-044

Users shall be able to save reports as:

```text
Draft
Private
Shared
Published
Archived
```

---

## 4.45 Report Versioning

## UR-045

Every published report shall support versioning.

---

## 4.46 Report Collaboration

## UR-046

Authorized users shall be able to collaborate on reports.

Supported collaboration actions:

```text
View
Comment
Edit
Review
Approve
Publish
```

---

## 4.47 Approval Workflow

## UR-047

Organizations shall be able to require approval before publishing reports.

---

## 4.48 Comments

## UR-048

Users shall be able to comment on report components and report versions.

---

## 4.49 Report Sharing

## UR-049

Users shall be able to share reports according to RBAC policies.

---

## 4.50 Embedded Reports

## UR-050

Authorized users shall be able to embed reports in supported SalesGenie interfaces.

---

## 4.51 Export

## UR-051

Users shall be able to export reports to:

```text
PDF
XLSX
CSV
JSON
```

---

## 4.52 Scheduling

## UR-052

Users shall be able to send a custom report to the Scheduled Reports module.

---

## 4.53 Report Duplication

## UR-053

Users shall be able to duplicate reports without modifying the original.

---

## 4.54 Report Templates

## UR-054

Users shall be able to save custom reports as reusable templates.

---

## 4.55 Template Governance

## UR-055

Administrators shall be able to publish organization-wide templates.

---

## 4.56 Report Search

## UR-056

Users shall be able to search reports by:

```text
Name
Owner
Department
Tags
Data Source
Created Date
Modified Date
```

---

## 4.57 Report Tags

## UR-057

Users shall be able to add tags.

---

## 4.58 Report Documentation

## UR-058

Users shall be able to add:

```text
Description
Purpose
Metric Definitions
Data Sources
Business Rules
Owner
```

---

## 4.59 AI Documentation

## UR-059

AI shall be able to automatically generate report documentation.

---

## 4.60 Report Refresh

## UR-060

Users shall be able to manually refresh report data.

---

## 4.61 Auto Refresh

## UR-061

Reports shall optionally support configurable auto-refresh intervals.

---

## 4.62 Report State

## UR-062

The system shall preserve user-selected filters and view state where configured.

---

## 5. System Requirements

## 5.1 Custom Report Service

## SR-001

SalesGenie shall provide a dedicated Custom Report Service responsible for:

* Report definitions
* Report metadata
* Query planning
* Report validation
* Report execution
* Visualization metadata
* Versioning
* Permissions
* Collaboration

---

## 5.2 Architecture

```text
                         Custom Report UI
                                |
                         Report API Gateway
                                |
                     Custom Report Service
                                |
        ┌───────────────────────┼───────────────────────┐
        ↓                       ↓                       ↓
  Report Definition       Query Planner            AI Report Agent
        ↓                       ↓                       ↓
  Metadata Service       Data Access Layer       AI Validation
        └───────────────────────┼───────────────────────┘
                                ↓
                         Query Execution
                                |
                    ┌───────────┼───────────┐
                    ↓           ↓           ↓
                  Sales      Marketing    Finance
                    ↓           ↓           ↓
                 Product     Support     Advertising
                    └───────────┼───────────┘
                                ↓
                         Result Processing
                                |
                       Visualization Engine
                                |
                        AI Insight Engine
                                |
                          Report Renderer
                                |
                     Export / Dashboard / API
```

---

## 5.3 Multi-Tenant Architecture

## SR-002

Every report shall be scoped to the appropriate:

```text
Tenant
Organization
Workspace
Department
User
```

---

## 5.4 Tenant Isolation

## SR-003

The query engine shall enforce tenant and authorization boundaries at the data-access layer.

Frontend filtering shall never be considered a security boundary.

---

## 5.5 Report Definition

## SR-004

A report definition shall be represented as a versioned declarative schema.

Example:

```json
{
  "report_id": "...",
  "version": 3,
  "data_sources": [],
  "dimensions": [],
  "measures": [],
  "filters": [],
  "calculated_fields": [],
  "visualizations": [],
  "ai_configuration": {}
}
```

---

## 5.6 Immutable Versions

## SR-005

Published report versions shall be immutable.

---

## 5.7 Draft Versions

## SR-006

Users shall be able to modify draft versions without modifying published versions.

---

## 5.8 Query Planner

## SR-007

The Query Planner shall transform report definitions into an executable query plan.

---

## 5.9 Query Validation

## SR-008

The Query Planner shall validate:

```text
Field Existence
Data Types
Join Compatibility
Aggregation Rules
Filter Compatibility
Authorization
Data Classification
Resource Limits
```

---

## 5.10 Query Optimization

## SR-009

The query engine shall optimize:

```text
Predicate Pushdown
Projection Pushdown
Aggregation
Join Ordering
Partition Pruning
Caching
Materialized Results
```

where supported.

---

## 5.11 Resource Governance

## SR-010

The system shall protect against:

* Unbounded queries
* Excessive joins
* Excessive result sizes
* Expensive calculations
* Cartesian products
* Query explosions

---

## 5.12 Query Timeout

## SR-011

Every report execution shall have configurable resource and timeout limits.

---

## 5.13 Async Execution

## SR-012

Long-running reports shall execute asynchronously.

---

## 5.14 Job Queue

## SR-013

Asynchronous report execution shall use a distributed job queue.

---

## 5.15 Idempotency

## SR-014

Report execution requests shall support idempotency keys.

---

## 5.16 Duplicate Execution Prevention

## SR-015

Repeated requests shall not produce duplicate execution jobs where the same idempotency key is used.

---

## 5.17 Result Caching

## SR-016

The platform shall support configurable report-result caching.

---

## 5.18 Cache Invalidation

## SR-017

Caches shall be invalidated when underlying data changes according to freshness policy.

---

## 5.19 Data Freshness

## SR-018

Reports shall expose:

```text
Last Updated
Data Timestamp
Source Freshness
```

where available.

---

## 5.20 Data Lineage

## SR-019

The system shall track:

```text
Report
→ Dataset
→ Source
→ Field
→ Transformation
→ Calculation
→ Visualization
```

---

## 5.21 Data Classification

## SR-020

Fields shall support classifications such as:

```text
PUBLIC
INTERNAL
CONFIDENTIAL
RESTRICTED
PII
FINANCIAL
SECURITY_SENSITIVE
```

---

## 5.22 Field-Level Security

## SR-021

Unauthorized fields shall not be available to the query planner.

---

## 5.23 Row-Level Security

## SR-022

The query engine shall enforce row-level access policies.

---

## 5.24 Column-Level Security

## SR-023

The system shall support column-level access restrictions.

---

## 5.25 RBAC

## SR-024

Permissions shall include:

```text
report.create
report.read
report.update
report.delete
report.execute
report.export
report.share
report.publish
report.approve
report.clone
report.schedule
report.manage
report.ai
template.create
template.publish
```

---

## 5.26 AI Report Agent

## SR-025

The AI Report Agent shall support:

* Intent extraction
* Metric identification
* Dimension selection
* Data-source selection
* Filter generation
* Visualization recommendation
* Formula generation
* Narrative generation
* Anomaly analysis
* Report optimization

---

## 5.27 AI Structured Output

## SR-026

AI-generated report definitions shall use strict schemas.

Invalid AI output shall never be executed directly.

---

## 5.28 AI Validation Pipeline

## SR-027

The system shall validate AI-generated reports through:

```text
AI Generation
      ↓
Schema Validation
      ↓
Semantic Validation
      ↓
Authorization Validation
      ↓
Query Validation
      ↓
Cost Validation
      ↓
Human Approval if Required
      ↓
Execution
```

---

## 5.29 AI Hallucination Protection

## SR-028

AI shall not invent:

* Metrics
* Fields
* Data sources
* Values
* Business facts
* Relationships

The AI must operate against the authorized metadata catalog.

---

## 5.30 AI Grounding

## SR-029

AI-generated explanations shall be grounded in actual report results and available metadata.

---

## 5.31 AI Confidence

## SR-030

AI-generated insights shall support confidence indicators.

---

## 5.32 AI Evidence

## SR-031

AI insights shall reference the metrics, dimensions, time periods, or data evidence used to produce the insight.

---

## 5.33 Human Approval

## SR-032

Organizations shall be able to require human approval for:

```text
Financial Reports
External Reports
Restricted Data Reports
Executive Reports
AI-Generated Reports
Published Templates
```

---

## 5.34 Collaboration Service

## SR-033

The system shall support collaborative editing with optimistic concurrency controls.

---

## 5.35 Concurrency

## SR-034

Concurrent report edits shall not silently overwrite another user's changes.

---

## 5.36 Version Conflict

## SR-035

The system shall detect stale report versions and provide conflict resolution.

---

## 5.37 Visualization Engine

## SR-036

The visualization layer shall support configurable chart specifications independent of data execution.

---

## 5.38 Responsive Rendering

## SR-037

Reports shall render across:

```text
Desktop
Tablet
Mobile
Embedded Views
Exported Documents
```

---

## 5.39 Accessibility

## SR-038

Report components shall support enterprise accessibility requirements, including:

* Keyboard navigation
* Screen readers
* Semantic labels
* Accessible tables
* Chart descriptions
* Focus management

---

## 5.40 Export Engine Integration

## SR-039

Custom Report Builder shall integrate with the Report Export Engine.

---

## 5.41 Scheduled Reports Integration

## SR-040

Any published report shall optionally be schedulable through the Scheduled Reports module.

---

## 5.42 Dashboard Integration

## SR-041

Report components shall be embeddable into SalesGenie dashboards where permitted.

---

## 5.43 API Access

## SR-042

Authorized applications shall be able to retrieve report results through versioned APIs.

---

## 5.44 Webhooks

## SR-043

The system may emit report lifecycle events through secure webhooks.

---

## 5.45 Audit Logging

## SR-044

The system shall audit:

```text
Report Created
Report Updated
Report Viewed
Report Executed
Report Exported
Report Shared
Report Published
Report Deleted
Report Approved
Report Rejected
AI Report Generated
AI Insight Generated
Template Created
Template Published
```

---

## 5.46 Observability

## SR-045

The system shall expose:

```text
Report Execution Count
Success Rate
Failure Rate
Execution Latency
Query Latency
AI Latency
Export Latency
Cache Hit Rate
Query Cost
AI Token Usage
```

---

## 5.47 Distributed Tracing

## SR-046

Every execution shall have a correlation ID propagated across:

```text
API
Report Service
Query Engine
Data Services
AI Service
Export Engine
Storage
```

---

## 5.48 Rate Limiting

## SR-047

The platform shall enforce rate limits by:

```text
Tenant
Organization
User
API Client
Report
```

---

## 5.49 Report Quotas

## SR-048

Organizations shall have configurable limits for:

```text
Reports
Executions
Concurrent Queries
Result Size
Export Size
AI Generations
```

---

## 5.50 Security

## SR-049

The module shall implement:

```text
Authentication
Authorization
RBAC
Tenant Isolation
Encryption
Secret Management
Audit Logging
Least Privilege
Data Classification
```

---

## 6. Functional Requirements

## 6.1 Create Report

## FR-001

The system shall provide:

```http
POST /api/v1/reports/custom
```

The API shall validate:

* Authentication
* Authorization
* Tenant
* Report schema
* Data sources
* Fields
* Filters
* Formulas
* Visualizations

---

## 6.2 List Reports

## FR-002

```http
GET /api/v1/reports/custom
```

shall support:

```text
Search
Filtering
Sorting
Pagination
Ownership
Tags
Status
```

---

## 6.3 Get Report

## FR-003

```http
GET /api/v1/reports/custom/{report_id}
```

shall return the authorized report definition and metadata.

---

## 6.4 Update Report

## FR-004

```http
PUT /api/v1/reports/custom/{report_id}
```

shall create a new draft version where appropriate.

---

## 6.5 Delete Report

## FR-005

```http
DELETE /api/v1/reports/custom/{report_id}
```

shall enforce permissions and retention policies.

---

## 6.6 Clone Report

## FR-006

```http
POST /api/v1/reports/custom/{report_id}/clone
```

shall create an independent report.

---

## 6.7 Execute Report

## FR-007

```http
POST /api/v1/reports/custom/{report_id}/execute
```

shall:

```text
Validate
Authorize
Build Query
Execute
Process Results
Return Result
```

---

## 6.8 Preview Report

## FR-008

```http
POST /api/v1/reports/custom/preview
```

shall execute a constrained preview without publishing the report.

---

## 6.9 Validate Report

## FR-009

```http
POST /api/v1/reports/custom/validate
```

shall validate the complete report definition.

---

## 6.10 Save Draft

## FR-010

```http
POST /api/v1/reports/custom/{report_id}/draft
```

shall save a draft configuration.

---

## 6.11 Publish Report

## FR-011

```http
POST /api/v1/reports/custom/{report_id}/publish
```

shall:

```text
Validate
Authorize
Check Approval
Create Immutable Version
Publish
Audit
```

---

## 6.12 Report Version History

## FR-012

```http
GET /api/v1/reports/custom/{report_id}/versions
```

shall return version history.

---

## 6.13 Restore Version

## FR-013

```http
POST /api/v1/reports/custom/{report_id}/versions/{version}/restore
```

shall create a new draft from the selected version.

---

## 6.14 Data Source Discovery

## FR-014

The system shall provide an authorized metadata catalog.

```http
GET /api/v1/reports/data-sources
```

---

## 6.15 Field Discovery

## FR-015

```http
GET /api/v1/reports/data-sources/{source_id}/fields
```

shall return authorized fields.

---

## 6.16 Field Search

## FR-016

Users shall be able to search fields using semantic and lexical search.

---

## 6.17 Add Dimension

## FR-017

Users shall be able to add dimensions to reports.

---

## 6.18 Add Measure

## FR-018

Users shall be able to add measures.

---

## 6.19 Add Filter

## FR-019

Users shall be able to add filters.

---

## 6.20 Add Calculated Field

## FR-020

Users shall be able to create calculated fields.

---

## 6.21 Formula Validation

## FR-021

The system shall validate:

```text
Syntax
Data Types
Aggregation
Division by Zero
Null Handling
Circular References
Authorization
```

---

## 6.22 Formula Dependency Graph

## FR-022

The system shall maintain dependencies between calculated fields.

Example:

```text
Revenue
  ↓
Gross Profit
  ↓
Gross Margin
  ↓
Profitability Score
```

---

## 6.23 Circular Dependency Detection

## FR-023

The system shall reject circular calculated-field dependencies.

---

## 6.24 Chart Creation

## FR-024

Users shall be able to add visualization components.

---

## 6.25 Chart Configuration

## FR-025

Users shall be able to configure chart mappings.

Example:

```text
X Axis → Month
Y Axis → Revenue
Series → Region
Filter → Product
```

---

## 6.26 KPI Creation

## FR-026

Users shall be able to create KPI cards.

---

## 6.27 Table Creation

## FR-027

Users shall be able to create tabular report components.

---

## 6.28 Pivot Reports

## FR-028

The system shall support pivot-style reports with:

```text
Rows
Columns
Measures
Aggregations
Filters
```

---

## 6.29 Ranking

## FR-029

The system shall support:

```text
Top N
Bottom N
Rank
Dense Rank
Percentile
```

---

## 6.30 Period Comparison

## FR-030

The system shall support:

```text
MoM
QoQ
YoY
WoW
Actual vs Target
Actual vs Forecast
```

---

## 6.31 AI Report Generation

## FR-031

The system shall provide:

```http
POST /api/v1/reports/ai/generate
```

Input:

```json
{
  "prompt": "Create a report showing monthly revenue and profit by region."
}
```

The AI shall return a structured report definition.

---

## 6.32 AI Report Refinement

## FR-032

The system shall provide conversational refinement.

Examples:

```text
Add customer acquisition cost.

Remove the Europe region.

Show quarterly data instead.

Use a line chart.

Add a forecast.

Explain the revenue decline.
```

---

## 6.33 AI Report Explanation

## FR-033

The system shall allow AI to explain how a report was constructed.

---

## 6.34 AI Visualization Recommendation

## FR-034

AI shall recommend visualization types based on:

```text
Data Type
Cardinality
Temporal Structure
Comparison Objective
Distribution
Relationship
Business Context
```

---

## 6.35 AI Metric Recommendation

## FR-035

AI shall recommend related metrics based on the selected report objective.

---

## 6.36 AI Filter Recommendation

## FR-036

AI shall recommend useful filters.

---

## 6.37 AI Formula Generation

## FR-037

AI shall generate formulas using only available authorized fields.

---

## 6.38 AI Validation

## FR-038

AI-generated report definitions shall be validated before execution.

---

## 6.39 AI Hallucination Detection

## FR-039

The system shall reject AI-generated definitions containing nonexistent fields or unsupported data sources.

---

## 6.40 AI Insight Generation

## FR-040

The system shall provide:

```http
POST /api/v1/reports/{report_id}/ai/insights
```

---

## 6.41 AI Anomaly Detection

## FR-041

The system shall identify statistically or business-rule-based anomalies.

---

## 6.42 AI Forecast

## FR-042

Where forecasting is enabled, the report shall support forecast series and uncertainty information.

---

## 6.43 AI Recommendation

## FR-043

AI recommendations shall contain:

```text
Recommendation
Evidence
Expected Impact
Confidence
Risk
```

---

## 6.44 Report Lineage

## FR-044

Users shall be able to inspect the lineage of report values.

---

## 6.45 Report Metadata

## FR-045

The system shall expose:

```text
Owner
Created At
Updated At
Version
Data Sources
Refresh Time
Tags
Status
```

---

## 6.46 Save Template

## FR-046

```http
POST /api/v1/reports/templates
```

shall save a report as a reusable template.

---

## 6.47 List Templates

## FR-047

```http
GET /api/v1/reports/templates
```

shall support template discovery.

---

## 6.48 Publish Template

## FR-048

Authorized administrators shall be able to publish organization templates.

---

## 6.49 Share Report

## FR-049

The system shall support controlled report sharing.

---

## 6.50 Permission Assignment

## FR-050

Users shall be able to assign supported permissions:

```text
VIEW
COMMENT
EDIT
EXPORT
SHARE
EXECUTE
PUBLISH
ADMIN
```

---

## 6.51 Approval Workflow

## FR-051

The system shall support:

```text
Draft
 ↓
Review
 ↓
Approval
 ↓
Publish
```

---

## 6.52 Comments

## FR-052

Users shall be able to attach comments to:

```text
Report
Version
Component
Insight
```

---

## 6.53 Schedule Integration

## FR-053

The system shall allow users to schedule a published custom report.

---

## 6.54 Export Integration

## FR-054

The system shall send report definitions and execution results to the Report Export Engine.

---

## 6.55 Dashboard Integration

## FR-055

Users shall be able to add eligible report components to dashboards.

---

## 6.56 API Consumption

## FR-056

Authorized applications shall be able to consume report results through versioned APIs.

---

## 6.57 Report Execution History

## FR-057

The system shall maintain:

```text
Execution ID
Report ID
Version
Started At
Completed At
Duration
Status
Query Cost
Result Size
Error
```

---

## 6.58 Failed Execution

## FR-058

Failures shall be classified into:

```text
VALIDATION_ERROR
AUTHORIZATION_ERROR
DATA_SOURCE_ERROR
QUERY_ERROR
TIMEOUT
RESOURCE_LIMIT
AI_ERROR
EXPORT_ERROR
INTERNAL_ERROR
```

---

## 6.59 Retry

## FR-059

Retryable executions shall support controlled retries.

---

## 6.60 Cancel Execution

## FR-060

Authorized users shall be able to cancel long-running asynchronous reports.

---

## 6.61 Query Cost Estimation

## FR-061

Before executing expensive reports, the system shall optionally estimate:

```text
Execution Cost
Expected Runtime
Data Volume
Resource Consumption
```

---

## 6.62 Query Guardrails

## FR-062

The system shall prevent execution when a query violates configured resource limits.

---

## 6.63 Partial Results

## FR-063

Where supported, the system may return partial results with explicit indication that the result is incomplete.

---

## 6.64 Empty State

## FR-064

Reports returning no data shall display a meaningful empty state rather than an application error.

---

## 6.65 Data Error Handling

## FR-065

Unavailable data sources shall produce actionable errors without exposing internal infrastructure details.

---

## 7. AI + Human Workflow

## 7.1 Human-First Workflow

```text
Human
  ↓
Select Data Sources
  ↓
Select Fields
  ↓
Create Metrics
  ↓
Add Filters
  ↓
Create Visualizations
  ↓
Preview
  ↓
Validate
  ↓
Save
  ↓
Publish
```

---

## 7.2 AI-Assisted Workflow

```text
Human Request
      ↓
AI Understands Intent
      ↓
AI Selects Authorized Metadata
      ↓
AI Generates Report Definition
      ↓
Validation
      ↓
Human Review
      ↓
Human Modification
      ↓
Preview
      ↓
Publish
```

---

## 7.3 AI Autonomous Workflow

```text
Business Objective
      ↓
AI Report Agent
      ↓
Identify Required Metrics
      ↓
Identify Data Sources
      ↓
Generate Report
      ↓
Policy Validation
      ↓
Approval Policy
      ↓
Automatic Publish if Allowed
```

---

## 7.4 Conversational Editing

```text
User:
Create a revenue report.

AI:
Creates report.

User:
Group it by product.

AI:
Adds product dimension.

User:
Compare this month with last month.

AI:
Adds period comparison.

User:
Show only products with declining revenue.

AI:
Adds condition.

User:
Add an AI explanation.

AI:
Adds narrative component.
```

---

## 8. Report Builder Architecture

```text
                         USER
                           |
                 ┌─────────┴─────────┐
                 ↓                   ↓
            Visual Builder      AI Builder
                 |                   |
                 └─────────┬─────────┘
                           ↓
                   Report Definition
                           ↓
                    Schema Validator
                           ↓
                  Authorization Engine
                           ↓
                    Query Planner
                           ↓
                    Query Optimizer
                           ↓
                    Data Execution
                           ↓
                   Result Processing
                           ↓
              ┌────────────┴────────────┐
              ↓                         ↓
       Visualization Engine       AI Insight Engine
              ↓                         ↓
              └────────────┬────────────┘
                           ↓
                     Report Renderer
                           ↓
            ┌──────────────┼──────────────┐
            ↓              ↓              ↓
        Dashboard       Export         Schedule
```

---

## 9. Report Definition Model

```text
CustomReport
├── id
├── tenant_id
├── organization_id
├── workspace_id
├── owner_id
├── name
├── description
├── status
├── version
├── data_sources
├── dimensions
├── measures
├── calculated_fields
├── filters
├── grouping
├── sorting
├── visualizations
├── ai_configuration
├── permissions
├── sharing
├── tags
├── lineage
├── created_at
├── updated_at
└── published_at
```

---

## 10. Report Component Model

```text
Report
│
├── Header
│
├── KPI Section
│   ├── Revenue
│   ├── Profit
│   ├── Conversion
│   └── ROI
│
├── Visualization Section
│   ├── Line Chart
│   ├── Bar Chart
│   ├── Funnel
│   └── Heatmap
│
├── Table Section
│   └── Detailed Data
│
├── AI Section
│   ├── Summary
│   ├── Insights
│   ├── Anomalies
│   └── Recommendations
│
└── Metadata
    ├── Sources
    ├── Refresh Time
    └── Version
```

---

## 11. AI Report Generation Pipeline

```text
Natural Language Request
          ↓
Intent Classification
          ↓
Business Objective Extraction
          ↓
Metadata Retrieval
          ↓
Data Source Selection
          ↓
Metric Selection
          ↓
Dimension Selection
          ↓
Filter Generation
          ↓
Visualization Recommendation
          ↓
Report Definition Generation
          ↓
Schema Validation
          ↓
Authorization Validation
          ↓
Semantic Validation
          ↓
Cost Validation
          ↓
Human Approval if Required
          ↓
Execution
```

---

## 12. AI Guardrails

AI shall never:

* Access unauthorized fields.
* Access another tenant.
* Invent database fields.
* Invent metrics.
* Invent report results.
* Execute arbitrary SQL outside policy.
* Expose sensitive data.
* Publish restricted reports without authorization.
* Modify permissions without authorization.
* Share reports externally without authorization.

---

## 13. Security Architecture

```text
Authentication
      ↓
RBAC
      ↓
Tenant Isolation
      ↓
Report Permission
      ↓
Data Source Permission
      ↓
Field Permission
      ↓
Row-Level Security
      ↓
Data Classification
      ↓
Query Validation
      ↓
AI Validation
      ↓
Execution
```

---

## 14. Data Governance

The system shall support:

```text
Data Classification
Data Lineage
Data Ownership
Data Retention
Access Policies
Field-Level Security
Row-Level Security
Audit Logging
Consent Policies
```

---

## 15. Report Quality Controls

Before publication, the system shall validate:

```text
✓ Report Definition
✓ Data Sources
✓ Fields
✓ Metrics
✓ Formulas
✓ Filters
✓ Joins
✓ Aggregations
✓ Visualizations
✓ Permissions
✓ Data Sensitivity
✓ AI Content
✓ Performance
```

---

## 16. Performance Requirements

## NFR-001

Interactive report previews shall prioritize low latency.

## NFR-002

Large analytical reports shall execute asynchronously.

## NFR-003

The system shall support horizontal scaling of:

```text
Query Workers
AI Workers
Rendering Workers
Export Workers
```

## NFR-004

Heavy workloads from one tenant shall not monopolize shared resources.

## NFR-005

Query execution shall support cancellation.

## NFR-006

Expensive reports shall use caching or materialized results where appropriate.

---

## 17. Reliability Requirements

The system shall support:

```text
Retries
Timeouts
Circuit Breakers
Backpressure
Job Queues
Dead Letter Queues
Idempotency
Graceful Degradation
Failure Isolation
Service Failover
```

---

## 18. Observability Requirements

The platform shall expose:

```text
Report Creation Rate
Report Execution Rate
Execution Success Rate
Execution Failure Rate
Average Query Latency
P95 Query Latency
P99 Query Latency
AI Generation Latency
Export Latency
Cache Hit Ratio
Query Resource Usage
Report Size
Concurrent Queries
```

---

## 19. AI Evaluation Requirements

AI-generated reports shall be evaluated for:

```text
Intent Accuracy
Field Selection Accuracy
Metric Accuracy
Filter Accuracy
Formula Accuracy
Visualization Accuracy
Groundedness
Hallucination Rate
Authorization Compliance
Schema Validity
Execution Success Rate
Human Acceptance Rate
```

---

## 20. Testing Requirements

## Unit Tests

```text
Report Schema
Formula Engine
Filter Engine
Permission Engine
Query Planner
Visualization Configuration
AI Output Validation
```

## Integration Tests

```text
Database
CRM
Marketing
Advertising
Finance
Product
Support
AI Services
Export Engine
Scheduled Reports
```

## Security Tests

```text
Tenant Isolation
RBAC
Row-Level Security
Column-Level Security
PII Protection
AI Permission Boundaries
SQL Injection
Query Abuse
Report Sharing
```

## AI Tests

```text
Natural Language Parsing
Ambiguous Requests
Invalid Metrics
Unknown Fields
Hallucinated Fields
Incorrect Formulas
Unsafe Queries
Prompt Injection
Unauthorized Tool Requests
```

## Load Tests

```text
Concurrent Users
Concurrent Reports
Large Datasets
Large Joins
High Cardinality
Large Exports
AI Generation Bursts
```

---

## 21. Acceptance Criteria

The Custom Report Builder shall be considered production-ready when:

* Users can create reports visually.
* Users can create reports using natural language.
* AI can generate valid report definitions.
* AI-generated definitions are schema validated.
* AI cannot access unauthorized fields.
* AI cannot cross tenant boundaries.
* Users can select authorized data sources.
* Users can select dimensions.
* Users can select measures.
* Users can create calculated fields.
* Users can create formulas.
* Formula errors are detected before execution.
* Circular formulas are rejected.
* Users can create filters.
* Users can create nested AND/OR filters.
* Users can configure dynamic date ranges.
* Users can group data.
* Users can sort data.
* Users can rank data.
* Users can create KPI cards.
* Users can create charts.
* Users can create tables.
* Users can create pivot reports.
* Users can compare periods.
* Users can create conditional formatting.
* Users can add AI summaries.
* Users can add AI insights.
* Users can add AI recommendations.
* Users can add anomaly detection.
* Users can add forecasting where supported.
* AI insights are grounded in report results.
* Report lineage is available.
* Reports are versioned.
* Published versions are immutable.
* Users can clone reports.
* Users can create templates.
* Administrators can publish templates.
* Users can collaborate according to permissions.
* Approval workflows work.
* Report sharing respects RBAC.
* Report exports respect permissions.
* Custom reports can be scheduled.
* Custom reports can be embedded in dashboards.
* APIs expose authorized report results.
* Long-running reports execute asynchronously.
* Query timeouts are enforced.
* Resource limits are enforced.
* Duplicate executions are prevented.
* Failed executions can be retried.
* Report execution history is available.
* Audit logs are complete.
* Data classification is enforced.
* PII and restricted data are protected.
* Observability metrics are available.
* Distributed tracing is available.
* AI generation is measurable and evaluable.

---

## 22. FAANG-Level Product Principles

## 22.1 Declarative Report Architecture

Reports shall be represented as versioned declarative specifications rather than UI-specific implementations.

## 22.2 Security at the Data Layer

Authorization shall be enforced before query execution, not merely hidden from the frontend.

## 22.3 AI Does Not Bypass Deterministic Controls

AI may generate and recommend report configurations, but deterministic authorization and governance systems remain authoritative.

## 22.4 Human-in-the-Loop

Sensitive, financial, executive, external, and organization-controlled reports may require human approval.

## 22.5 Reproducibility

Every report version shall be reproducible using its immutable definition and execution metadata.

## 22.6 Explainability

AI-generated insights shall distinguish:

```text
Observed Facts
Retrieved Data
Calculated Metrics
Inference
Prediction
Recommendation
```

## 22.7 Multi-Tenant by Design

Tenant isolation shall be enforced throughout:

```text
API
Metadata
Query Planning
Data Access
AI Retrieval
Caching
Storage
Export
Sharing
Audit
```

## 22.8 Observable by Default

Every important operation shall produce metrics, logs, traces, and audit events.

---

## 23. Ultimate SalesGenie Custom Reporting Model

```text
                         SALES GENIE
                              |
                       Business Data
                              |
       ┌──────────────────────┼──────────────────────┐
       ↓                      ↓                      ↓
     Sales                 Marketing               Finance
       ↓                      ↓                      ↓
   Advertising              SEO                   Product
       ↓                      ↓                      ↓
   Customers              Support             Lead Intelligence
       └──────────────────────┼──────────────────────┘
                              ↓
                       Metadata Catalog
                              |
              ┌───────────────┴───────────────┐
              ↓                               ↓
       Human Report Builder             AI Report Builder
              ↓                               ↓
              └───────────────┬───────────────┘
                              ↓
                     Report Definition
                              ↓
                     Schema Validation
                              ↓
                  Authorization + Governance
                              ↓
                       Query Planner
                              ↓
                       Query Engine
                              ↓
                     Result Processing
                              ↓
               ┌──────────────┴──────────────┐
               ↓                             ↓
        Visualization Engine           AI Insight Engine
               ↓                             ↓
               └──────────────┬──────────────┘
                              ↓
                        Report Renderer
                              |
              ┌───────────────┼───────────────┐
              ↓               ↓               ↓
          Dashboard         Export         Scheduling
              ↓               ↓               ↓
              └───────────────┼───────────────┘
                              ↓
                       Secure Delivery
                              ↓
                           Audit
                              ↓
                        Analytics
                              ↓
                     AI Optimization
```

---

## 24. Final Product Objective

SalesGenie's Custom Report Builder shall evolve beyond a traditional drag-and-drop reporting interface into an **AI-native enterprise analytical report composition platform**.

The final experience shall allow:

```text
Human asks a business question
          ↓
AI understands the objective
          ↓
AI discovers authorized data
          ↓
AI proposes metrics
          ↓
AI proposes dimensions
          ↓
AI proposes calculations
          ↓
AI proposes visualizations
          ↓
Human reviews and modifies
          ↓
System validates security and correctness
          ↓
Report executes against governed data
          ↓
AI explains the results
          ↓
Human publishes the report
          ↓
Report can be:
    ├── Added to Dashboard
    ├── Exported
    ├── Scheduled
    ├── Shared
    ├── Embedded
    └── Used by Other AI Agents
```

The ultimate goal is to make SalesGenie capable of transforming:

```text
Business Question
        ↓
Data Discovery
        ↓
Report Construction
        ↓
Analysis
        ↓
Explanation
        ↓
Decision Support
        ↓
Action
```

while maintaining:

```text
Enterprise Security
Multi-Tenant Isolation
RBAC
Data Governance
AI Grounding
Human Oversight
Reproducibility
Version Control
Auditability
Scalability
Reliability
Observability
```
