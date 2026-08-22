```markdown
# SALESGENIE — EXTERNAL_CLIENT.md

> **Document Type:** User Requirements + System Requirements + Functional Requirements
> **Module:** External Client / External Stakeholder Portal
> **Project:** SalesGenie — Enterprise AI Sales, Marketing, SEO, Customer Support, Business Intelligence & Growth Automation SaaS
> **Version:** 1.0.0
> **Status:** FAANG-Level Production Specification
> **Execution Model:** AI-First + Human-Assisted + Human Escalation
> **Primary Actor:** External Client
> **Security Classification:** Tenant-Isolated / Least-Privilege / Zero-Trust
> **Purpose:** Provide authorized external stakeholders with controlled access to specific business data, reports, campaigns, projects, deliverables, analytics, communications, and AI-generated recommendations without exposing internal organizational resources.

---

# 1. ROLE DEFINITION

An **External Client** is an external stakeholder who is granted controlled access to selected SalesGenie resources by an authorized organization/workplace administrator.

An External Client is **not** an internal employee and shall not automatically receive access to:

- Internal organization administration
- Internal employee information
- Internal sales pipelines
- Internal security controls
- Internal billing administration
- Internal audit infrastructure
- Other customers
- Other organizations
- Internal AI configuration
- Internal system configuration
- Internal workforce management

The External Client shall only access explicitly authorized resources.

---

# 2. EXTERNAL CLIENT OBJECTIVE

The External Client portal shall allow a customer/stakeholder to:

```text
View Business Performance
        ↓
View Assigned Projects
        ↓
Monitor Marketing
        ↓
Monitor SEO
        ↓
Monitor Leads
        ↓
Monitor Advertising
        ↓
Review Product Performance
        ↓
Review Financial Insights
        ↓
Receive AI Recommendations
        ↓
Approve/Reject Selected Actions
        ↓
Communicate With AI
        ↓
Escalate to Human Experts
        ↓
Review Reports
        ↓
Download Deliverables
```

---

# 3. CORE DESIGN PRINCIPLES

The External Client module shall follow:

```text
Least Privilege
Zero Trust
Tenant Isolation
Explicit Authorization
Human Oversight
AI Transparency
Data Minimization
Auditability
Privacy by Design
Secure Collaboration
```

---

# 4. USER REQUIREMENTS

## UR-EC-001 — External Client Invitation

Authorized administrators shall be able to invite external clients.

Invitation shall contain:

```text
Client Name
Email
Organization
Project
Role
Access Scope
Expiration
Inviting Administrator
```

---

## UR-EC-002 — Invitation Acceptance

The client shall be able to accept an invitation securely.

The invitation shall:

* Be uniquely identifiable
* Be time-limited
* Be single-use where appropriate
* Be invalidated after acceptance
* Be revocable by authorized administrators

---

## UR-EC-003 — Secure Registration

An invited external client shall be able to establish an account.

---

## UR-EC-004 — Authentication

The client shall authenticate securely.

Supported mechanisms may include:

```text
Email + Password
OTP
MFA
Enterprise SSO
Passwordless Authentication
```

Availability shall depend on platform configuration and subscription tier.

---

# 5. CLIENT ONBOARDING

## UR-EC-005 — Client Profile

The client shall manage:

```text
Name
Company
Designation
Email
Phone
Country
Time Zone
Profile Picture
Communication Preferences
```

---

## UR-EC-006 — Client Business Profile

Where authorized, the client shall provide:

```text
Business Name
Industry
Website
Products
Services
Target Market
Business Goals
Primary Markets
```

---

## UR-EC-007 — Onboarding Questionnaire

SalesGenie shall collect requirements necessary to configure the client's project.

Example:

```text
Business Objective
Revenue Goal
Lead Goal
Marketing Goal
SEO Goal
Product Launch Goal
Customer Support Goal
Target Audience
Budget
Timeline
```

---

# 6. CLIENT DASHBOARD

## UR-EC-008 — Executive Dashboard

The client shall receive a personalized dashboard.

Example:

```text
┌────────────────────────────────────────────────────────────┐
│ CLIENT BUSINESS OVERVIEW                                   │
├────────────────────────────────────────────────────────────┤
│ Revenue       Leads       Conversion      Growth            │
│ $125K         4,820       8.4%            +18.6%            │
├────────────────────────────────────────────────────────────┤
│ PROJECT PERFORMANCE                                         │
│ Marketing     SEO        Lead Gen        Advertising       │
│   92%         87%           81%               89%           │
├────────────────────────────────────────────────────────────┤
│ AI BUSINESS INSIGHTS                                        │
│ • Product A is generating the highest margin.               │
│ • Campaign B has declining ROAS.                            │
│ • Organic traffic increased 21%.                            │
├────────────────────────────────────────────────────────────┤
│ ACTIONS                                                     │
│ Review Recommendations | Reports | Support | Projects       │
└────────────────────────────────────────────────────────────┘
```

---

# 7. PROJECT MANAGEMENT

## UR-EC-009 — Assigned Projects

Clients shall view projects assigned to them.

Each project may contain:

```text
Project Name
Description
Objective
Owner
Status
Start Date
Deadline
Budget
Progress
Deliverables
Tasks
Milestones
```

---

## UR-EC-010 — Project Status

Project status shall support:

```text
Not Started
Planning
In Progress
Under Review
Client Approval
Completed
Paused
Cancelled
```

---

## UR-EC-011 — Project Timeline

Clients shall view project timelines.

---

## UR-EC-012 — Milestone Tracking

Clients shall track milestones.

---

## UR-EC-013 — Client Approval

Clients shall approve or reject designated project milestones.

---

# 8. CLIENT REQUIREMENT MANAGEMENT

## UR-EC-014 — Requirement Submission

Clients shall submit business requirements.

---

## UR-EC-015 — Requirement Modification

Clients shall request changes to existing requirements.

---

## UR-EC-016 — Requirement Approval

Clients shall approve finalized requirements.

---

## UR-EC-017 — Requirement History

The system shall maintain requirement versions.

```text
Version 1
    ↓
Client Feedback
    ↓
Version 2
    ↓
Client Approval
```

---

# 9. BUSINESS GROWTH ANALYTICS

## UR-EC-018 — Monthly Business Growth

Clients shall view monthly:

```text
Revenue
Expenses
Profit
Loss
Customers
Leads
Orders
Conversion Rate
Advertising Spend
Marketing Spend
ROI
```

---

## UR-EC-019 — Yearly Business Growth

Clients shall view yearly:

```text
Revenue Growth
Profit Growth
Customer Growth
Lead Growth
Conversion Growth
Expense Growth
Marketing Growth
Advertising Growth
```

---

## UR-EC-020 — Period Comparison

Clients shall compare:

```text
Month vs Month
Quarter vs Quarter
Year vs Year
Campaign vs Campaign
Product vs Product
Channel vs Channel
```

---

# 10. PRODUCT ANALYTICS

## UR-EC-021 — Product Performance

Clients shall view authorized product metrics:

```text
Revenue
Units Sold
Cost
Gross Profit
Net Profit
Margin
Growth
Conversion
Advertising Spend
Marketing Spend
```

---

## UR-EC-022 — Product Ranking

The platform shall rank products by:

```text
Revenue
Profit
Growth
ROI
Margin
Demand
Customer Retention
```

---

## UR-EC-023 — Loss-Making Product

The AI shall identify products that are underperforming.

---

## UR-EC-024 — Product Improvement

AI shall recommend:

```text
Pricing Changes
Marketing Changes
Audience Changes
Product Improvements
Advertising Changes
Positioning Changes
Retention Strategies
```

---

# 11. MARKET INTELLIGENCE

## UR-EC-025 — Market Analysis

Clients shall request market analysis for an authorized product/project.

The system shall analyze available current market information.

Potential analysis:

```text
Market Demand
Market Growth
Market Trends
Competitors
Pricing
Customer Behavior
Market Opportunities
Market Risks
```

---

## UR-EC-026 — Competitor Analysis

Clients shall view authorized competitor intelligence.

Potential information:

```text
Competitor Products
Pricing
Positioning
Marketing
Advertising
SEO
Strengths
Weaknesses
Market Presence
```

---

## UR-EC-027 — Market Opportunity

AI shall identify:

```text
Market Gaps
Emerging Demand
Underserved Segments
Pricing Opportunities
Product Opportunities
Marketing Opportunities
```

---

# 12. NEW PRODUCT LAUNCH

## UR-EC-028 — Product Launch Request

Clients shall request a product-launch analysis.

---

## UR-EC-029 — Launch Research

The AI shall analyze:

```text
Market
Competitors
Similar Launches
Pricing
Audience
Demand
Channels
Marketing
SEO
Advertising
```

---

## UR-EC-030 — Launch Strategy

The system shall generate:

```text
Target Market
Positioning
Pricing
Messaging
Marketing
SEO
Advertising
Sales
Support
Launch Timeline
```

---

## UR-EC-031 — Launch Risk

AI shall identify:

```text
Demand Risk
Competition Risk
Pricing Risk
Financial Risk
Marketing Risk
Operational Risk
```

---

# 13. LEAD GENERATION

## UR-EC-032 — Lead Dashboard

Clients shall view authorized lead metrics.

```text
Total Leads
Qualified Leads
Opportunities
Customers
Conversion Rate
Lead Sources
Lead Quality
```

---

## UR-EC-033 — Lead Search Request

Clients shall be able to submit lead-generation requirements.

Example:

```text
Industry: SaaS
Location: United States
Company Size: 50–500
Role: CTO
Intent: High
```

---

## UR-EC-034 — AI Lead Generation

AI shall generate or identify qualified leads using authorized data sources and integrations.

---

## UR-EC-035 — Lead Scoring

Leads shall be scored based on:

```text
Fit
Intent
Engagement
Potential Value
Conversion Probability
```

---

## UR-EC-036 — Lead Segmentation

Clients shall view segments.

---

# 14. SALES PERFORMANCE

## UR-EC-037 — Sales Dashboard

Clients shall view:

```text
Pipeline
Opportunities
Deals
Conversion
Revenue
Average Deal Size
Sales Cycle
```

---

## UR-EC-038 — Sales Recommendations

AI shall identify sales opportunities.

---

## UR-EC-039 — Sales Forecast

Where sufficient data exists, AI shall provide forecasts with uncertainty indicators.

---

# 15. MARKETING MANAGEMENT

## UR-EC-040 — Marketing Dashboard

Clients shall view:

```text
Campaigns
Reach
Engagement
Conversions
Cost
Revenue
ROI
```

---

## UR-EC-041 — Marketing Campaign Review

Clients shall review assigned campaigns.

---

## UR-EC-042 — AI Marketing Recommendations

AI shall recommend:

```text
Audience
Creative
Messaging
Channel
Budget Allocation
Campaign Timing
```

---

## UR-EC-043 — Campaign Approval

Clients shall approve campaigns before execution where approval is configured.

---

# 16. ADVERTISING ANALYTICS

## UR-EC-044 — Ad Platform Integration

Where configured, the system may connect supported platforms such as:

```text
Google Ads
Meta Ads
Facebook
Instagram
WhatsApp
YouTube
TikTok
LinkedIn
```

---

## UR-EC-045 — Ad Spend

Clients shall view:

```text
Daily Spend
Monthly Spend
Yearly Spend
Campaign Spend
Product Spend
Channel Spend
```

---

## UR-EC-046 — Ad Revenue

Where reliable attribution data exists, the client shall view:

```text
Attributed Revenue
ROAS
ROI
CAC
Conversion Rate
Profit Contribution
```

---

## UR-EC-047 — Audience Analysis

Clients shall view available audience insights:

```text
Age
Gender
Location
Device
Interest
Audience Segment
```

---

## UR-EC-048 — Product-Audience Analysis

AI shall identify which products perform best for available audience segments.

---

# 17. SEO CLIENT PORTAL

## UR-EC-049 — SEO Dashboard

Clients shall view:

```text
Organic Traffic
Keywords
Rankings
CTR
Backlinks
Technical Issues
Content Performance
```

---

## UR-EC-050 — SEO Recommendations

AI shall recommend:

```text
Keywords
Content
Technical Improvements
Internal Linking
Metadata
Schema
Page Optimization
```

---

## UR-EC-051 — Competitor SEO

Clients shall view authorized competitor SEO insights.

---

# 18. AI-GENERATED DIGITAL MARKETING PLATFORM

## UR-EC-052 — AI Marketing Automation

Clients shall request AI-generated marketing automations.

---

## UR-EC-053 — Campaign Generator

AI shall generate campaign plans based on:

```text
Product
Audience
Goal
Budget
Market
Competition
Historical Performance
```

---

## UR-EC-054 — Content Generator

AI may generate:

```text
Blog
Social Media
Email
Ad Copy
Landing Page
Product Description
Video Script
SEO Content
```

---

## UR-EC-055 — Human Review

The client may require human review before publishing.

---

# 19. SUPPORT SYSTEM

## UR-EC-056 — AI Support

Clients shall receive AI assistance.

---

## UR-EC-057 — Human Support

Clients shall request human assistance.

---

## UR-EC-058 — AI-to-Human Escalation

AI shall escalate when:

```text
Client Requests Human
Confidence Is Low
Issue Is Complex
Billing Issue
Security Issue
Technical Issue
Complaint
High-Priority Issue
```

---

## UR-EC-059 — Support Ticket

Clients shall create tickets.

---

## UR-EC-060 — Ticket Tracking

Clients shall see:

```text
Ticket ID
Status
Priority
Assigned Team
SLA
Messages
Attachments
Resolution
```

---

# 20. AI BUSINESS ADVISOR

## UR-EC-061 — Business Questions

Clients shall ask questions such as:

```text
Why did my profit decrease?

Which product is performing best?

Which campaign should we stop?

Which audience generates the highest ROI?

How can we reduce CAC?

What should we improve next month?
```

---

## UR-EC-062 — Evidence-Based Answers

AI responses shall provide relevant evidence where available.

---

## UR-EC-063 — Recommendation Confidence

Important recommendations should include confidence/evidence indicators.

---

## UR-EC-064 — Human Escalation

Clients shall be able to request a human expert review of AI recommendations.

---

# 21. REPORTING

## UR-EC-065 — Client Reports

Clients shall view authorized reports.

---

## UR-EC-066 — Excel Reports

Clients shall generate/download authorized Excel reports.

Reports may contain:

```text
Sales
Revenue
Profit
Loss
Products
Marketing
Advertising
SEO
Leads
Customers
Campaigns
```

---

## UR-EC-067 — PDF Reports

Where supported, clients shall download PDF reports.

---

## UR-EC-068 — Scheduled Reports

Clients may receive:

```text
Weekly
Monthly
Quarterly
Yearly
```

reports.

---

# 22. ANALYTICS VISUALIZATION

## UR-EC-069 — Interactive Charts

Clients shall view:

```text
Revenue Trend
Profit Trend
Expense Trend
Lead Funnel
Customer Growth
Product Profitability
Advertising ROI
SEO Growth
Marketing ROI
```

---

## UR-EC-070 — Filtering

Charts shall support authorized filters:

```text
Date
Product
Campaign
Channel
Market
Customer Segment
```

---

## UR-EC-071 — AI Chart Explanation

AI shall explain meaningful changes.

---

# 23. CLIENT COMMUNICATION

## UR-EC-072 — Client Inbox

Clients shall access communications related to their projects.

---

## UR-EC-073 — Team Communication

Where enabled, clients shall communicate with assigned teams.

---

## UR-EC-074 — AI Communication

Clients shall communicate with authorized AI agents.

---

## UR-EC-075 — Human Communication

Clients shall communicate with assigned human specialists.

---

# 24. DOCUMENT MANAGEMENT

## UR-EC-076 — Document Portal

Clients shall access authorized documents.

---

## UR-EC-077 — Document Upload

Clients shall upload project documents.

---

## UR-EC-078 — Document Versioning

The platform shall maintain document versions.

---

## UR-EC-079 — Document Approval

Clients shall approve/reject documents where configured.

---

## UR-EC-080 — Document Security

Documents shall be accessible only to authorized users.

---

# 25. AI KNOWLEDGE BASE

## UR-EC-081 — Client Knowledge Base

Clients shall upload authorized business information.

Potential documents:

```text
Product Documentation
Company Information
Pricing
Policies
FAQs
Marketing Materials
Brand Guidelines
Technical Documentation
```

---

## UR-EC-082 — AI Knowledge Search

AI shall use authorized knowledge to answer client questions.

---

## UR-EC-083 — Knowledge Isolation

Client knowledge shall never be exposed to another tenant.

---

# 26. APPROVAL CENTER

## UR-EC-084 — Approval Queue

Clients shall have a centralized approval center.

Example:

```text
┌───────────────────────────────────────────────┐
│ APPROVAL CENTER                               │
├───────────────────────────────────────────────┤
│ Marketing Campaign          [Review]          │
│ SEO Strategy                [Review]          │
│ Product Launch Plan         [Review]          │
│ AI Recommendation           [Review]          │
│ Advertising Change          [Review]          │
└───────────────────────────────────────────────┘
```

---

## UR-EC-085 — Approve

Client shall approve authorized actions.

---

## UR-EC-086 — Reject

Client shall reject actions.

---

## UR-EC-087 — Request Modification

Client shall request modifications.

---

# 27. AI ACTION GOVERNANCE

The client shall be able to configure whether AI may:

```text
Analyze
Recommend
Draft
Request Approval
Execute
```

Example:

```text
AI Analysis       → Automatic
AI Recommendation → Automatic
Ad Creation       → Approval Required
Ad Publishing     → Approval Required
Budget Change     → Human Approval
Financial Action  → Human Approval
```

---

# 28. CLIENT NOTIFICATIONS

## UR-EC-088 — Business Alerts

Clients shall receive:

```text
Revenue Alert
Profit Alert
Loss Alert
Lead Alert
Campaign Alert
SEO Alert
Advertising Alert
Product Alert
```

---

## UR-EC-089 — Project Alerts

Clients shall receive:

```text
Milestone Completed
Deadline Approaching
Approval Required
Task Delayed
Project Completed
```

---

## UR-EC-090 — Support Alerts

Clients shall receive:

```text
Ticket Created
Agent Reply
AI Escalation
SLA Warning
Ticket Resolved
```

---

# 29. BILLING

## UR-EC-091 — Subscription View

Clients shall view their subscription.

---

## UR-EC-092 — Plan Upgrade

Clients shall upgrade eligible subscriptions.

---

## UR-EC-093 — Plan Downgrade

Clients shall downgrade according to billing policy.

---

## UR-EC-094 — Payment

Clients shall securely make payments.

---

## UR-EC-095 — Invoice

Clients shall view invoices.

---

## UR-EC-096 — Billing History

Clients shall view:

```text
Payments
Invoices
Refunds
Credits
Subscription Changes
```

---

# 30. USAGE MANAGEMENT

## UR-EC-097 — Usage Dashboard

Clients shall view:

```text
AI Requests
Tokens
Leads
Workflows
Storage
Reports
Agents
API Calls
```

---

## UR-EC-098 — Usage Limits

The system shall clearly communicate subscription limits.

---

## UR-EC-099 — Usage Alerts

Clients shall receive warnings when approaching limits.

---

# 31. SECURITY REQUIREMENTS

## SR-EC-001 — Zero Trust

Every external-client request shall be authenticated and authorized.

---

## SR-EC-002 — Tenant Isolation

External clients shall never access another tenant's data.

---

## SR-EC-003 — Project-Level Isolation

Clients shall only access assigned projects.

---

## SR-EC-004 — Object-Level Authorization

Authorization shall be enforced at the resource/object level.

Example:

```text
Client A
  ↓
Organization A
  ↓
Project A
  ↓
Campaign A
  ↓
Allowed

Client A
  ↓
Project B
  ↓
DENIED
```

---

## SR-EC-005 — Least Privilege

External client permissions shall be minimal by default.

---

## SR-EC-006 — Backend Authorization

Security checks shall occur server-side.

---

## SR-EC-007 — MFA

MFA shall be supported.

---

## SR-EC-008 — Session Security

The system shall support:

```text
Session Expiration
Session Revocation
Device Tracking
Suspicious Login Detection
```

---

## SR-EC-009 — Encryption

Sensitive information shall be encrypted in transit and at rest.

---

## SR-EC-010 — Secure File Access

Documents shall use authorized temporary access mechanisms where appropriate.

---

## SR-EC-011 — Secure Download

Downloads shall verify authorization before issuing access.

---

## SR-EC-012 — API Security

External API requests shall require appropriate authentication and authorization.

---

## SR-EC-013 — Rate Limiting

The external client API shall be rate-limited.

---

## SR-EC-014 — Abuse Detection

The system shall detect:

```text
Credential Abuse
Brute Force
API Abuse
Scraping
Spam
Automated Attacks
Suspicious Sessions
```

---

## SR-EC-015 — Audit Logging

Important external-client events shall be logged.

Examples:

```text
Login
Logout
File Download
File Upload
Approval
Rejection
AI Action
Report Generation
Subscription Change
Permission Change
```

---

# 32. AI SECURITY

## SR-EC-016 — AI Data Isolation

AI agents shall only receive authorized client information.

---

## SR-EC-017 — Prompt Injection Protection

The system shall mitigate prompt injection.

---

## SR-EC-018 — Retrieved Content Isolation

Untrusted documents shall not automatically override system policies.

---

## SR-EC-019 — Tool Authorization

Every AI tool shall require explicit authorization.

---

## SR-EC-020 — High-Risk Actions

The following shall require additional authorization:

```text
Financial Transactions
Data Deletion
Mass Messaging
Advertising Budget Changes
Production Changes
Security Changes
```

---

## SR-EC-021 — AI Auditability

AI actions shall record:

```text
User
Agent
Model
Request
Tool
Action
Timestamp
Result
Approval
```

where appropriate and subject to privacy policies.

---

# 33. DATA PRIVACY

## SR-EC-022 — Data Minimization

Only necessary client information shall be processed.

---

## SR-EC-023 — Consent

Applicable consent requirements shall be supported.

---

## SR-EC-024 — Data Export

Authorized client data shall be exportable.

---

## SR-EC-025 — Data Deletion

Eligible data shall support deletion workflows.

---

## SR-EC-026 — Retention

Data retention shall follow configured policies.

---

# 34. PERFORMANCE REQUIREMENTS

## SR-EC-027 — Dashboard Performance

Frequently accessed dashboard data should load within an agreed performance budget under normal conditions.

---

## SR-EC-028 — Pagination

Large datasets shall use pagination or equivalent efficient retrieval.

---

## SR-EC-029 — Async Processing

Heavy operations shall execute asynchronously.

Examples:

```text
Excel Generation
Large Reports
AI Research
Market Analysis
Competitor Analysis
Bulk Lead Generation
```

---

## SR-EC-030 — Caching

Frequently requested non-sensitive data may use controlled caching.

---

# 35. RELIABILITY

## SR-EC-031 — Retry

Transient failures shall support controlled retries.

---

## SR-EC-032 — Idempotency

Critical operations shall use idempotency controls.

---

## SR-EC-033 — Failure Recovery

The system shall provide recovery mechanisms for:

```text
Workflow Failures
Integration Failures
Payment Failures
Report Failures
AI Failures
```

---

# 36. FUNCTIONAL REQUIREMENTS

## FR-EC-001 — Invitation

The system shall allow authorized administrators to invite external clients.

## FR-EC-002 — Registration

The system shall allow invited clients to register.

## FR-EC-003 — Authentication

The system shall authenticate clients.

## FR-EC-004 — MFA

The system shall support MFA.

## FR-EC-005 — Client Profile

Clients shall manage their profiles.

## FR-EC-006 — Dashboard

Clients shall view personalized dashboards.

## FR-EC-007 — Project Access

Clients shall view assigned projects.

## FR-EC-008 — Project Timeline

Clients shall view project timelines.

## FR-EC-009 — Milestones

Clients shall track milestones.

## FR-EC-010 — Requirements

Clients shall submit requirements.

## FR-EC-011 — Requirement Approval

Clients shall approve requirements.

## FR-EC-012 — Analytics

Clients shall view authorized analytics.

## FR-EC-013 — Monthly Analytics

Clients shall view monthly performance.

## FR-EC-014 — Yearly Analytics

Clients shall view yearly performance.

## FR-EC-015 — Profit Analysis

Clients shall view profitability.

## FR-EC-016 — Loss Analysis

Clients shall view losses.

## FR-EC-017 — Product Analysis

Clients shall analyze products.

## FR-EC-018 — Market Analysis

Clients shall request market research.

## FR-EC-019 — Competitor Analysis

Clients shall view competitor intelligence.

## FR-EC-020 — Product Launch Analysis

Clients shall analyze new products.

## FR-EC-021 — Launch Strategy

The system shall generate launch strategies.

## FR-EC-022 — Lead Generation

Clients shall request lead generation.

## FR-EC-023 — Lead Scoring

The system shall score leads.

## FR-EC-024 — Sales Analytics

Clients shall view sales performance.

## FR-EC-025 — Marketing Analytics

Clients shall view marketing performance.

## FR-EC-026 — Campaign Review

Clients shall review campaigns.

## FR-EC-027 — Campaign Approval

Clients shall approve configured campaigns.

## FR-EC-028 — Advertising Analytics

Clients shall view advertising metrics.

## FR-EC-029 — Advertising Spend

Clients shall view advertising spend.

## FR-EC-030 — Advertising Revenue

Clients shall view attributed revenue where available.

## FR-EC-031 — Audience Analysis

Clients shall view available audience analytics.

## FR-EC-032 — SEO Analytics

Clients shall view SEO metrics.

## FR-EC-033 — SEO Recommendations

AI shall provide SEO recommendations.

## FR-EC-034 — AI Marketing

Clients shall use AI marketing features.

## FR-EC-035 — Content Generation

Clients shall generate content.

## FR-EC-036 — Support

Clients shall access AI support.

## FR-EC-037 — Human Support

Clients shall access human support.

## FR-EC-038 — Ticketing

Clients shall create and track tickets.

## FR-EC-039 — AI Business Advisor

Clients shall interact with the AI Business Advisor.

## FR-EC-040 — AI Recommendations

Clients shall receive recommendations.

## FR-EC-041 — Human Review

Clients shall request human review.

## FR-EC-042 — Reports

Clients shall access reports.

## FR-EC-043 — Excel Export

Clients shall generate Excel reports.

## FR-EC-044 — PDF Export

Clients shall generate PDF reports where supported.

## FR-EC-045 — Notifications

Clients shall receive notifications.

## FR-EC-046 — Documents

Clients shall upload and access documents.

## FR-EC-047 — Knowledge Base

Clients shall manage authorized knowledge.

## FR-EC-048 — Approval Center

Clients shall approve/reject designated actions.

## FR-EC-049 — Billing

Clients shall manage billing.

## FR-EC-050 — Subscription

Clients shall manage eligible subscriptions.

## FR-EC-051 — Usage

Clients shall monitor usage.

## FR-EC-052 — Security

Clients shall manage security settings.

## FR-EC-053 — Sessions

Clients shall manage sessions.

## FR-EC-054 — Data Export

Clients shall export eligible data.

## FR-EC-055 — Data Deletion

Clients shall initiate eligible deletion requests.

---

# 37. CLIENT → AI → HUMAN WORKFLOW

```text
CLIENT
  │
  ▼
AI ASSISTANT
  │
  ├── High Confidence
  │       │
  │       ▼
  │    ANSWER/ACTION
  │
  └── Low Confidence / Sensitive
          │
          ▼
      HUMAN REVIEW
          │
          ▼
     CLIENT RESPONSE
```

---

# 38. CLIENT → PROJECT → BUSINESS GROWTH WORKFLOW

```text
CLIENT
  │
  ▼
BUSINESS REQUIREMENTS
  │
  ▼
PROJECT CREATION
  │
  ▼
MARKET ANALYSIS
  │
  ▼
COMPETITOR ANALYSIS
  │
  ▼
PRODUCT STRATEGY
  │
  ▼
MARKETING + SEO
  │
  ▼
ADVERTISING
  │
  ▼
LEAD GENERATION
  │
  ▼
SALES
  │
  ▼
REVENUE
  │
  ▼
FINANCE ANALYSIS
  │
  ▼
AI OPTIMIZATION
  │
  ▼
BUSINESS GROWTH
```

---

# 39. CLIENT APPROVAL WORKFLOW

```text
AI / TEAM
    │
    ▼
DRAFT
    │
    ▼
INTERNAL REVIEW
    │
    ▼
CLIENT REVIEW
    │
    ├─────────────┐
    ▼             ▼
 APPROVE        REJECT
    │             │
    ▼             ▼
 EXECUTE       MODIFY
                  │
                  ▼
             CLIENT REVIEW
```

---

# 40. EXTERNAL CLIENT DATA FLOW

```text
                    EXTERNAL CLIENT
                           │
                           ▼
                    API GATEWAY
                           │
                    AUTHENTICATION
                           │
                    AUTHORIZATION
                           │
                           ▼
                    TENANT CONTEXT
                           │
                           ▼
                  PROJECT PERMISSION
                           │
                           ▼
                    DATA SERVICE
                           │
             ┌─────────────┼──────────────┐
             ▼             ▼              ▼
          ANALYTICS      PROJECT       SUPPORT
             │             │              │
             └─────────────┼──────────────┘
                           ▼
                       RESPONSE
```

---

# 41. AI BUSINESS INSIGHT FLOW

```text
CLIENT DATA
    │
    ▼
DATA INGESTION
    │
    ▼
DATA VALIDATION
    │
    ▼
ANALYTICS ENGINE
    │
    ▼
AI BUSINESS BRAIN
    │
    ├──────────────┬──────────────┐
    ▼              ▼              ▼
 PROFIT          MARKETING       SALES
 ANALYSIS        ANALYSIS        ANALYSIS
    │              │              │
    └──────────────┼──────────────┘
                   ▼
             AI RECOMMENDATION
                   │
                   ▼
              CLIENT REVIEW
                   │
                   ▼
                 ACTION
```

---

# 42. EXTERNAL CLIENT REPORTING

A report may contain:

```text
EXECUTIVE SUMMARY

Business Performance
├── Revenue
├── Expenses
├── Profit
├── Loss
└── Growth

Sales
├── Leads
├── Opportunities
├── Customers
└── Conversion

Marketing
├── Campaigns
├── Reach
├── Engagement
└── ROI

Advertising
├── Spend
├── Revenue
├── ROAS
└── Audience

SEO
├── Traffic
├── Keywords
├── Rankings
└── Growth

Products
├── Revenue
├── Profit
├── Margin
└── Growth

AI Recommendations
├── Priority
├── Reason
├── Expected Impact
└── Action
```

---

# 43. CLIENT EXPERIENCE LEVELS

The portal shall support different service levels.

```text
FREE
 │
 ├── Limited Dashboard
 ├── Limited AI
 ├── Limited Reports
 └── Limited Leads

PRO
 │
 ├── Advanced AI
 ├── Lead Generation
 ├── Marketing
 ├── SEO
 └── Analytics

BUSINESS
 │
 ├── Advanced Automation
 ├── Advanced Analytics
 ├── Multiple Users
 ├── Integrations
 └── Advanced Reports

ENTERPRISE
 │
 ├── Custom AI
 ├── Advanced Security
 ├── SSO
 ├── Dedicated Support
 ├── Custom Integrations
 └── Custom Governance
```

Exact features shall be configurable by the platform billing configuration.

---

# 44. CLIENT SUCCESS METRICS

SalesGenie should measure client outcomes including:

```text
Revenue Growth
Profit Growth
Lead Growth
Conversion Growth
Customer Growth
CAC Reduction
ROAS Improvement
SEO Growth
Marketing ROI
Automation Adoption
Support Satisfaction
```

---

# 45. AI CLIENT SUCCESS ENGINE

The AI shall identify clients who may require assistance.

Example:

```text
OBSERVATION
Revenue decreased 15%.

POSSIBLE CAUSES
• Paid traffic decreased.
• Product B conversion decreased.
• CAC increased.

RECOMMENDATION
Review Product B pricing and campaign targeting.

PRIORITY
High

EXPECTED IMPACT
Potential recovery of conversion efficiency.

HUMAN REVIEW
Available
```

---

# 46. CLIENT EXPERIENCE REQUIREMENTS

The portal shall be:

```text
Fast
Simple
Professional
Transparent
Responsive
Accessible
Secure
Explainable
AI-Assisted
Human-Assisted
```

The client shall not need to understand:

```text
Microservices
Queues
Databases
AI Models
Vector Databases
Event Brokers
Infrastructure
```

to use the platform.

---

# 47. ACCEPTANCE CRITERIA

The External Client module shall not be considered production-ready until:

* [ ] External invitation works
* [ ] Secure registration works
* [ ] Authentication works
* [ ] MFA works
* [ ] Client profile works
* [ ] Client onboarding works
* [ ] Client dashboard works
* [ ] Project access works
* [ ] Project isolation works
* [ ] Requirement submission works
* [ ] Requirement approval works
* [ ] Monthly analytics work
* [ ] Yearly analytics work
* [ ] Revenue analytics work
* [ ] Profit analytics work
* [ ] Loss analytics work
* [ ] Product analytics work
* [ ] Market analysis works
* [ ] Competitor analysis works
* [ ] Product launch analysis works
* [ ] Lead generation works
* [ ] Lead scoring works
* [ ] Sales analytics work
* [ ] Marketing analytics work
* [ ] Advertising analytics work
* [ ] Ad spend analytics work
* [ ] Revenue attribution works where supported
* [ ] Audience analytics work where supported
* [ ] SEO analytics work
* [ ] AI marketing works
* [ ] AI content generation works
* [ ] AI support works
* [ ] Human support works
* [ ] AI-to-human escalation works
* [ ] Ticketing works
* [ ] Document management works
* [ ] Knowledge base works
* [ ] Approval center works
* [ ] AI recommendations work
* [ ] Human review works
* [ ] Excel generation works
* [ ] Report generation works
* [ ] Notifications work
* [ ] Billing works
* [ ] Subscription management works
* [ ] Usage tracking works
* [ ] Session management works
* [ ] Security controls work
* [ ] Audit logging works
* [ ] Tenant isolation passes security tests
* [ ] Object-level authorization passes security tests
* [ ] AI data isolation passes security tests
* [ ] Prompt-injection defenses are tested
* [ ] High-risk AI actions require appropriate approval
* [ ] Backup/recovery is tested
* [ ] Performance testing passes
* [ ] Accessibility testing passes
* [ ] Security testing passes

---

# 48. FINAL EXTERNAL CLIENT VISION

The External Client module shall transform SalesGenie from a conventional SaaS dashboard into a secure **client-facing business growth command center**.

The intended experience is:

```text
                         CLIENT
                           │
                           ▼
                  CLIENT COMMAND CENTER
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
      SALES             MARKETING            SEO
        │                  │                  │
        ▼                  ▼                  ▼
      LEADS             CAMPAIGNS          ORGANIC
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ▼
                     AI BUSINESS BRAIN
                           │
       ┌───────────────────┼───────────────────┐
       ▼                   ▼                   ▼
     FINANCE             PRODUCT            SUPPORT
       │                   │                   │
       ▼                   ▼                   ▼
   P&L / ROI         PROFITABILITY       AI + HUMAN
       │                   │                   │
       └───────────────────┼───────────────────┘
                           ▼
                    AI RECOMMENDATIONS
                           │
                           ▼
                      CLIENT APPROVAL
                           │
                           ▼
                       EXECUTION
                           │
                           ▼
                      MEASUREMENT
                           │
                           ▼
                    CONTINUOUS GROWTH
```

The External Client portal shall ultimately provide:

```text
TRANSPARENCY
     +
CONTROL
     +
AI INTELLIGENCE
     +
HUMAN EXPERTISE
     +
BUSINESS ANALYTICS
     +
AUTOMATION
     +
SECURITY
     =
TRUSTED CLIENT GROWTH PLATFORM
```

The client remains the owner of business decisions.

SalesGenie provides the intelligence, automation, analytics, recommendations, collaboration, and human expertise necessary to help the client make better decisions and achieve measurable business growth.

```
