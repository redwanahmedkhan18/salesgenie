# SALESGENIE — SEO_MANAGER.md

> **Document Type:** Role-Specific User Requirements + System Requirements + Functional Requirements
> **Project:** SalesGenie — Enterprise AI Sales, Marketing, Customer Support, SEO, Growth & Business Intelligence SaaS Platform
> **Role:** SEO Manager
> **Version:** 1.0.0
> **Status:** Production Product Requirements Specification
> **Architecture:** FAANG-Level / Enterprise-Grade / AI-Native / Multi-Tenant / Event-Driven
> **Execution Model:** AI SEO Manager + Human SEO Manager + Human-in-the-Loop
> **Primary Objective:** Build an autonomous-but-governed SEO intelligence and execution platform that discovers search opportunities, analyzes markets and competitors, builds SEO strategies, manages technical/content/off-page SEO, executes approved automation, measures organic growth and revenue impact, and continuously optimizes SEO toward sustainable business growth.

---

## 1. PURPOSE

The SalesGenie SEO Manager is a specialized AI + Human SEO management system responsible for the complete organic-growth lifecycle.

It must not function as a simple keyword generator.

The SEO Manager must understand:

- Business
- Product
- Market
- Industry
- Target customer
- Search intent
- Competitors
- Existing website
- Existing content
- Technical architecture
- Search visibility
- Conversion behavior
- Revenue objectives
- Geographic targets
- Brand requirements

before generating an SEO strategy.

The core workflow is:

```text
Business Objective
        ↓
Business/Product Understanding
        ↓
Website Intelligence
        ↓
Market Analysis
        ↓
Search Demand Analysis
        ↓
Competitor SEO Intelligence
        ↓
Keyword Intelligence
        ↓
Search Intent Classification
        ↓
SEO Opportunity Detection
        ↓
SEO Strategy
        ↓
Technical SEO
        ↓
Content Strategy
        ↓
On-Page Optimization
        ↓
Internal Linking
        ↓
Authority / Digital PR Strategy
        ↓
Human Review Where Required
        ↓
Execution
        ↓
Search Performance
        ↓
Traffic
        ↓
Leads
        ↓
Customers
        ↓
Revenue
        ↓
Continuous Optimization
```

---

## 2. ROLE DEFINITION

## 2.1 Role

**SEO Manager**

## 2.2 Role Category

```text
Growth
+
Search Intelligence
+
Technical SEO
+
Content SEO
+
Authority Building
+
Analytics
+
Revenue Optimization
```

## 2.3 Primary Mission

The SEO Manager shall be responsible for developing and executing a data-driven SEO program that improves:

* Organic visibility
* Search rankings
* Qualified organic traffic
* Organic leads
* Organic conversions
* Customer acquisition
* Revenue
* Profitability
* Brand visibility
* Market share

while maintaining:

* Search-engine compliance
* Website quality
* Security
* Brand safety
* Human oversight
* Data privacy
* Technical integrity

---

## 3. AI + HUMAN SEO MANAGEMENT MODEL

SalesGenie shall support three primary operating modes.

```text
MODE 1
Human SEO Manager
        ↓
Manual analysis + execution

MODE 2
AI-Assisted SEO Manager
        ↓
AI analysis
        ↓
Human decision
        ↓
Execution

MODE 3
AI Autonomous SEO Manager
        ↓
AI analysis
        ↓
AI recommendation
        ↓
Policy validation
        ↓
Automatic low-risk execution
        ↓
Monitoring
```

Critical SEO changes must remain subject to configurable human approval.

---

## 4. SEO MANAGER VS SEO SPECIALIST

## SEO Manager

Responsible for:

* SEO strategy
* SEO roadmap
* SEO KPIs
* SEO budget
* Team coordination
* SEO governance
* Portfolio-level SEO
* Prioritization
* Risk management

## SEO Specialist

Responsible for:

* Keyword research
* Technical audits
* Content optimization
* On-page SEO
* Internal linking
* Competitor research
* SERP analysis
* Local SEO
* SEO execution

Architecture:

```text
SEO MANAGER
    │
    ├── SEO Strategy
    ├── Budget
    ├── Governance
    ├── KPIs
    │
    ▼
SEO SPECIALISTS
    │
    ├── Technical SEO
    ├── Content SEO
    ├── Local SEO
    ├── International SEO
    ├── Programmatic SEO
    └── Digital PR
```

---

## 5. USER REQUIREMENTS

## UR-SEO-001 — SEO MANAGER WORKSPACE

The SEO Manager shall have a dedicated dashboard containing:

* SEO health
* Organic traffic
* Search visibility
* Keyword rankings
* Organic conversions
* Organic revenue
* Technical health
* Content performance
* Competitor movements
* Backlink profile
* Crawl/indexation status
* SEO opportunities
* SEO issues
* AI recommendations
* Human tasks
* Pending approvals
* SEO alerts

---

## UR-SEO-002 — MULTI-WORKSPACE SEO

The SEO Manager shall manage SEO for:

* Organization
* Workspace
* Website
* Domain
* Subdomain
* Product
* Geographic market
* Business unit

---

## UR-SEO-003 — WEBSITE ONBOARDING

The system shall allow an SEO Manager to connect a website.

Supported configuration shall include:

```text
Domain
CMS
Website Type
Industry
Country
Language
Target Audience
Business Model
Products
Services
Competitors
Primary Goals
```

---

## UR-SEO-004 — SEO OBJECTIVE CONFIGURATION

The manager shall configure goals such as:

* Increase organic traffic
* Increase rankings
* Generate leads
* Increase organic revenue
* Increase product visibility
* Launch a new product
* Enter a new market
* Improve local visibility
* Recover traffic
* Improve technical health
* Increase conversions

---

## UR-SEO-005 — BUSINESS-FIRST SEO

SEO recommendations must be connected to business objectives.

The system must not optimize only for:

```text
Traffic
Impressions
Rankings
```

It must connect SEO to:

```text
Traffic
→ Leads
→ Customers
→ Revenue
→ Profit
```

---

## UR-SEO-006 — PRODUCT SEO ANALYSIS

For each product, the AI shall analyze:

* Product category
* Customer need
* Search demand
* Search intent
* Product keywords
* Competitor positioning
* SERP landscape
* Content requirements
* Conversion opportunities

---

## UR-SEO-007 — MARKET SEO ANALYSIS

The AI shall analyze the target market before creating a strategy.

It shall identify:

* Market demand
* Search demand
* Market trends
* Search trends
* Competitor strength
* Market gaps
* Content gaps
* Keyword opportunities
* Customer questions

---

## UR-SEO-008 — TREND ANALYSIS

The SEO Manager shall receive trend intelligence for:

* Rising keywords
* Declining keywords
* Emerging topics
* Seasonal demand
* Product demand
* Search behavior
* Competitor movements

Trend classification:

```text
Emerging
Growing
Stable
Declining
Seasonal
Volatile
High Opportunity
High Risk
```

---

## UR-SEO-009 — COMPETITOR SEO INTELLIGENCE

The system shall analyze authorized competitor information.

It shall evaluate:

* Ranking keywords
* Content strategy
* Top pages
* Search visibility
* Keyword gaps
* Topic coverage
* Internal links
* Site architecture
* Backlink patterns
* SERP presence
* Featured results
* Local visibility
* Product pages
* Content freshness

---

## UR-SEO-010 — COMPETITOR GAP ANALYSIS

The AI shall identify:

* Keywords competitors rank for but client does not
* Topics competitors cover
* Missing product pages
* Missing content
* Weak content
* Missing internal links
* Search-intent gaps
* SERP feature opportunities

---

## UR-SEO-011 — KEYWORD INTELLIGENCE

The system shall support:

* Keyword discovery
* Keyword clustering
* Search volume
* Search intent
* Competition
* Keyword difficulty
* CPC where available
* Trend
* Geographic relevance
* Commercial intent
* Conversion potential

---

## UR-SEO-012 — SEARCH INTENT

The AI shall classify search intent into configurable categories:

```text
Informational
Navigational
Commercial Investigation
Transactional
Local
Branded
Non-Branded
Comparison
Problem/Solution
Product
```

---

## UR-SEO-013 — KEYWORD OPPORTUNITY SCORE

The system shall calculate configurable opportunity scores.

Example:

```text
Search Demand             20%
Business Relevance        25%
Conversion Potential      20%
Competition               15%
Ranking Difficulty        10%
Trend Growth              10%
```

Output:

```text
Keyword
Opportunity Score
Intent
Difficulty
Expected Value
Recommended Action
```

---

## UR-SEO-014 — TOPIC CLUSTERING

The AI shall organize keywords into:

```text
Pillar Topic
    ↓
Cluster Topics
    ↓
Supporting Articles
    ↓
Product / Service Pages
    ↓
Conversion Pages
```

---

## UR-SEO-015 — TOPICAL AUTHORITY

The system shall measure:

* Topic coverage
* Content depth
* Content quality
* Internal linking
* Search visibility
* Content relevance

and identify missing topic clusters.

---

## UR-SEO-016 — CONTENT STRATEGY

The SEO Manager shall generate:

* Content roadmap
* Editorial calendar
* Topic clusters
* Content briefs
* Search intent
* Target keywords
* Internal links
* External references
* CTA strategy
* Conversion objectives

---

## UR-SEO-017 — AI CONTENT BRIEF

Every AI content brief shall include:

```text
Primary Keyword
Secondary Keywords
Search Intent
Target Audience
User Problem
Content Objective
Recommended Structure
Required Topics
Internal Links
External Sources
FAQ Opportunities
CTA
Conversion Objective
Quality Requirements
```

---

## UR-SEO-018 — AI CONTENT GENERATION

The system may generate:

* Blog posts
* Product descriptions
* Landing pages
* Category pages
* FAQs
* Guides
* Comparison pages
* Case studies
* Knowledge-base content
* Metadata
* Structured content

AI content must be reviewed according to configured publishing policies.

---

## UR-SEO-019 — HUMAN CONTENT REVIEW

Human SEO managers or designated reviewers shall be able to:

* Edit
* Approve
* Reject
* Request changes
* Add sources
* Change keywords
* Modify search intent
* Change CTA
* Request fact verification

---

## UR-SEO-020 — CONTENT QUALITY

The system shall evaluate:

* Relevance
* Search intent alignment
* Factual accuracy
* Originality
* Readability
* Topic coverage
* Internal linking
* Conversion relevance
* Brand alignment

SEO scoring must not be treated as a guarantee of search-engine ranking.

---

## UR-SEO-021 — ON-PAGE SEO

The system shall optimize:

* Title
* Meta description
* H1
* H2/H3 structure
* URL
* Canonical
* Images
* Alt text
* Internal links
* Anchor text
* Structured data
* Content structure

---

## UR-SEO-022 — TECHNICAL SEO

The system shall audit:

* Crawlability
* Indexability
* Robots directives
* XML sitemap
* Canonicalization
* Redirects
* HTTP status codes
* Duplicate content
* Broken links
* Pagination
* JavaScript rendering
* Mobile usability
* Core Web Vitals
* HTTPS
* URL structure

---

## UR-SEO-023 — TECHNICAL SEO PRIORITY

Each issue shall contain:

```text
Issue
Severity
Affected URLs
Business Impact
SEO Impact
Technical Cause
Recommended Fix
Estimated Effort
Priority
Human Approval Required
```

Severity:

```text
Critical
High
Medium
Low
Informational
```

---

## UR-SEO-024 — SEO HEALTH SCORE

The system shall calculate an SEO health score based on configurable dimensions:

```text
Technical SEO
Content
Indexation
Performance
Internal Linking
Structured Data
Mobile
Authority
Search Visibility
Conversion
```

---

## UR-SEO-025 — INTERNAL LINKING

The AI shall identify:

* Orphan pages
* Weakly linked pages
* Important pages with insufficient links
* Internal-link opportunities
* Anchor-text opportunities
* Topic-cluster relationships

---

## UR-SEO-026 — PROGRAMMATIC SEO

For suitable businesses, the platform shall support programmatic SEO.

Examples:

```text
Location Pages
Product Pages
Category Pages
Comparison Pages
Industry Pages
Integration Pages
Use-Case Pages
```

AI-generated programmatic pages must include quality controls to prevent:

* Thin content
* Duplicate content
* Low-value pages
* Spam
* Uncontrolled page generation

---

## UR-SEO-027 — LOCAL SEO

The system shall support:

* Local keyword research
* Location pages
* Business profile optimization
* Local content
* NAP consistency
* Local citations
* Review monitoring
* Local ranking monitoring

The system must not generate fake reviews or deceptive business information.

---

## UR-SEO-028 — INTERNATIONAL SEO

The system shall support:

* Country targeting
* Language targeting
* hreflang
* Regional content
* Localized keyword research
* International competitor analysis
* Regional SERP analysis

---

## UR-SEO-029 — E-COMMERCE SEO

The system shall support:

* Product SEO
* Category SEO
* Faceted navigation analysis
* Product schema
* Merchant-feed integration
* Product keyword analysis
* Review content
* Product availability signals

---

## UR-SEO-030 — SEO FOR AI SEARCH

The system shall support optimization for emerging answer and AI-search experiences.

Capabilities may include:

* Entity clarity
* Structured information
* Citation-worthy content
* Question-answer coverage
* Authoritative source structure
* Organization/entity metadata
* Content summarization readiness

The system must not claim guaranteed inclusion in any AI search engine.

---

## 6. SEO ANALYTICS

## UR-SEO-031 — ORGANIC TRAFFIC

The dashboard shall display:

* Sessions
* Users
* New users
* Organic landing pages
* Organic traffic trends
* Traffic by country
* Traffic by device
* Traffic by page
* Traffic by product

---

## UR-SEO-032 — SEARCH PERFORMANCE

The system shall track:

* Impressions
* Clicks
* CTR
* Average position
* Queries
* Pages
* Countries
* Devices

---

## UR-SEO-033 — RANK TRACKING

The system shall track keyword positions by:

* Search engine
* Country
* City where supported
* Device
* Language
* Date
* Competitor

---

## UR-SEO-034 — RANKING DISTRIBUTION

Dashboard:

```text
Top 3
Top 10
Top 20
Top 50
Top 100
Beyond 100
```

---

## UR-SEO-035 — RANKING CHANGE DETECTION

The system shall detect:

```text
Major Gain
Moderate Gain
Minor Gain
Stable
Minor Loss
Moderate Loss
Major Loss
```

---

## UR-SEO-036 — TRAFFIC ANOMALY DETECTION

AI shall detect:

* Sudden traffic loss
* Traffic spike
* Ranking collapse
* Indexation loss
* Crawl problems
* Algorithm-related correlation signals
* Tracking failures

The AI shall not falsely claim that a particular search-engine algorithm caused an event without evidence.

---

## 7. SEO REVENUE ATTRIBUTION

## UR-SEO-037 — ORGANIC LEAD ATTRIBUTION

The system shall connect organic search to:

```text
Visitor
→ Lead
→ MQL
→ SQL
→ Opportunity
→ Customer
→ Revenue
```

---

## UR-SEO-038 — ORGANIC REVENUE

The dashboard shall calculate:

```text
Organic Revenue
Organic Customers
Organic CAC
Organic Conversion Rate
Organic ROI
Organic LTV
```

---

## UR-SEO-039 — PRODUCT SEO PROFITABILITY

For each product:

```text
Organic Traffic
Organic Leads
Customers
Revenue
Estimated SEO Cost
Profit Contribution
ROI
```

---

## UR-SEO-040 — SEO ROI

The system shall calculate configurable SEO ROI models.

Example:

```text
SEO ROI =
(Attributed Organic Profit - SEO Investment)
/
SEO Investment
```

Attribution assumptions must be visible.

---

## 8. SEO FORECASTING

## UR-SEO-041 — TRAFFIC FORECAST

AI shall forecast:

* Traffic
* Clicks
* Leads
* Customers
* Revenue

Forecasts must include:

* Forecast period
* Assumptions
* Confidence
* Uncertainty range

---

## UR-SEO-042 — RANKING FORECAST

The system may estimate ranking improvement based on historical data.

It must never present predicted ranking positions as guaranteed results.

---

## UR-SEO-043 — REVENUE FORECAST

The system shall estimate potential revenue from:

```text
Search Demand
×
Expected Visibility
×
Expected CTR
×
Conversion Rate
×
Average Revenue
```

---

## 9. SEO COMPETITIVE INTELLIGENCE

## UR-SEO-044 — COMPETITOR MONITORING

The system shall monitor authorized competitor signals such as:

* New content
* Ranking changes
* New pages
* Product launches
* Content updates
* Search visibility
* Public marketing changes

---

## UR-SEO-045 — COMPETITOR ALERTS

The manager shall receive:

```text
Competitor launched new product
Competitor gained major rankings
Competitor published major content
Competitor entered target keyword
Competitor gained visibility
Competitor lost visibility
```

---

## UR-SEO-046 — COMPETITOR RESPONSE

AI may recommend:

* Create competing content
* Improve existing content
* Create comparison content
* Improve product positioning
* Target underserved keywords
* Improve internal linking

---

## 10. SEO CAMPAIGN MANAGEMENT

## UR-SEO-047 — SEO PROJECT

A manager shall create:

```text
SEO Project
├── Objective
├── Website
├── Market
├── Products
├── Keywords
├── Content
├── Technical Tasks
├── Links
├── KPIs
├── Budget
└── Deadline
```

---

## UR-SEO-048 — SEO ROADMAP

The AI shall generate a prioritized roadmap:

```text
Phase 1
Technical Foundation

Phase 2
Keyword + Market Intelligence

Phase 3
Content Expansion

Phase 4
Authority Development

Phase 5
Conversion Optimization

Phase 6
Scale + Automation
```

---

## UR-SEO-049 — SEO TASK PRIORITIZATION

Prioritization shall consider:

```text
Business Impact
SEO Impact
Revenue Potential
Effort
Risk
Urgency
Confidence
Dependencies
```

---

## UR-SEO-050 — SEO TASK MANAGEMENT

Tasks shall support:

* Assigned user
* AI owner
* Human owner
* Deadline
* Priority
* Status
* Dependencies
* Approval
* Evidence
* Result

---

## 11. SEO AUTOMATION

## UR-SEO-051 — AUTOMATION ENGINE

The system shall support automated workflows for:

* SEO auditing
* Keyword monitoring
* Ranking monitoring
* Content briefs
* Internal-link recommendations
* Technical issue detection
* Reports
* Alerts
* Content refresh recommendations

---

## UR-SEO-052 — SAFE AUTOMATION

Low-risk actions may be automated.

Examples:

```text
Generate report
Generate content brief
Detect broken links
Generate keyword clusters
Create task
Generate recommendation
```

High-risk actions require approval:

```text
Publish website content
Modify robots.txt
Change canonical rules
Change redirects
Change large URL structures
Delete pages
Change indexing rules
```

---

## UR-SEO-053 — HUMAN OVERRIDE

Humans shall be able to:

* Pause automation
* Reject AI recommendations
* Modify strategy
* Roll back approved changes
* Change thresholds
* Disable integrations
* Override AI decisions

---

## 12. AI SEO MANAGER

## UR-SEO-054 — AI SEO AGENT

The AI SEO Manager shall perform:

```text
Observe
→ Analyze
→ Plan
→ Recommend
→ Request Approval
→ Execute
→ Monitor
→ Evaluate
→ Optimize
```

---

## UR-SEO-055 — AI SEO CONTEXT

The AI shall consider:

```text
Business
Product
Website
Market
Competitors
Keywords
Content
Technical SEO
Historical Performance
Conversions
Revenue
Brand
Risk Policies
```

---

## UR-SEO-056 — AI CONFIDENCE

Every major AI recommendation shall contain:

```text
Recommendation
Evidence
Assumptions
Expected Impact
Risk
Confidence
Required Approval
```

---

## UR-SEO-057 — AI SPECIALIZATION

The system shall dynamically specialize.

Example:

```text
E-commerce
→ E-commerce SEO Agent

SaaS
→ SaaS SEO Agent

Local Business
→ Local SEO Agent

Enterprise
→ Enterprise SEO Agent

International
→ International SEO Agent

New Product
→ Product SEO Agent

Technical Problem
→ Technical SEO Agent
```

---

## 13. AI SEO SUB-AGENTS

Architecture:

```text
                    AI SEO MANAGER
                           │
       ┌───────────────────┼───────────────────┐
       ▼                   ▼                   ▼
 MARKET AGENT       COMPETITOR AGENT      KEYWORD AGENT
       │                   │                   │
       └───────────────────┼───────────────────┘
                           ▼
                    STRATEGY AGENT
                           │
       ┌───────────────────┼───────────────────┐
       ▼                   ▼                   ▼
 TECHNICAL AGENT      CONTENT AGENT      INTERNAL LINK AGENT
       │                   │                   │
       └───────────────────┼───────────────────┘
                           ▼
                    ANALYTICS AGENT
                           │
                           ▼
                   OPTIMIZATION AGENT
```

---

## 14. SYSTEM REQUIREMENTS

## SR-SEO-001 — SERVICE ARCHITECTURE

The SEO Manager shall operate as a modular platform service.

```text
Frontend
   ↓
API Gateway
   ↓
SEO Manager Service
   ├── SEO Intelligence
   ├── Keyword Service
   ├── SERP Intelligence
   ├── Technical Audit Service
   ├── Content SEO Service
   ├── Internal Link Service
   ├── Local SEO Service
   ├── International SEO Service
   ├── Competitor Service
   ├── Rank Tracking Service
   ├── Analytics Service
   ├── Attribution Service
   ├── Forecasting Service
   ├── Experiment Service
   ├── Workflow Service
   └── AI SEO Engine
```

---

## SR-SEO-002 — MULTI-TENANCY

All resources shall contain tenant boundaries.

Required logical fields:

```text
tenant_id
organization_id
workspace_id
website_id
project_id
product_id
created_by
updated_by
created_at
updated_at
```

Cross-tenant data access must be denied by default.

---

## SR-SEO-003 — CORE DATA MODEL

Entities:

```text
SEOManager
SEOProject
Website
Domain
SEOAudit
SEOIssue
Keyword
KeywordCluster
SearchIntent
SERPResult
Competitor
CompetitorKeyword
CompetitorPage
MarketTrend
SEOOpportunity
ContentBrief
SEOContent
SEOPage
SEORecommendation
SEOApproval
SEOTask
SEOExperiment
SEOReport
SEOForecast
RankSnapshot
OrganicMetric
SEOAttribution
SEOIntegration
SEOAlert
SEOWorkflow
```

---

## SR-SEO-004 — KNOWLEDGE ARCHITECTURE

The system shall support:

* Relational data
* Vector database
* Search index
* Knowledge graph where beneficial
* Historical metrics
* Website crawl data
* Structured analytics
* RAG

---

## SR-SEO-005 — WEBSITE CRAWLER

The crawler shall support:

* URL discovery
* Sitemap discovery
* robots.txt interpretation
* Canonical detection
* HTTP status
* Metadata extraction
* Heading extraction
* Links
* Images
* Structured data
* Content
* Performance signals where available

The crawler must respect:

* robots directives
* crawl rate policies
* authentication boundaries
* applicable terms
* configured crawl limits

---

## SR-SEO-006 — CRAWL QUEUE

Crawler architecture:

```text
Seed URL
   ↓
URL Queue
   ↓
Crawler Workers
   ↓
Parser
   ↓
SEO Analyzer
   ↓
Database
   ↓
Issue Engine
```

---

## SR-SEO-007 — DISTRIBUTED PROCESSING

Long-running SEO jobs shall use:

* Queue
* Workers
* Retry
* Idempotency
* Dead-letter queue
* Job status
* Progress reporting

---

## SR-SEO-008 — SEARCH DATA INGESTION

The system shall support authorized search-data providers and APIs.

Provider abstraction:

```text
SearchProvider
    ├── Provider A
    ├── Provider B
    └── Provider C
```

---

## SR-SEO-009 — ANALYTICS INTEGRATION

The system shall support authorized integrations with analytics and webmaster/search platforms.

Potential integrations:

```text
Google Search Console
Google Analytics
Bing Webmaster Tools
CRM
Advertising platforms
CMS
E-commerce platforms
```

Integrations shall be implemented through official or authorized APIs where available.

---

## SR-SEO-010 — CMS INTEGRATION

Potential CMS integrations:

```text
WordPress
Shopify
Webflow
Custom CMS
Headless CMS
```

---

## SR-SEO-011 — API DESIGN

Example APIs:

```http
GET    /api/v1/seo-manager/dashboard
GET    /api/v1/seo-manager/projects
POST   /api/v1/seo-manager/projects

POST   /api/v1/seo-manager/websites/analyze
POST   /api/v1/seo-manager/audit/run
GET    /api/v1/seo-manager/audit/issues

POST   /api/v1/seo-manager/keywords/research
POST   /api/v1/seo-manager/keywords/cluster
POST   /api/v1/seo-manager/keywords/intent

POST   /api/v1/seo-manager/competitors/analyze
POST   /api/v1/seo-manager/market/analyze
POST   /api/v1/seo-manager/trends/analyze

POST   /api/v1/seo-manager/content/brief
POST   /api/v1/seo-manager/content/generate
POST   /api/v1/seo-manager/content/optimize

POST   /api/v1/seo-manager/internal-links/analyze
POST   /api/v1/seo-manager/technical/fix-plan

GET    /api/v1/seo-manager/rankings
GET    /api/v1/seo-manager/analytics
GET    /api/v1/seo-manager/attribution
GET    /api/v1/seo-manager/forecast

GET    /api/v1/seo-manager/recommendations
POST   /api/v1/seo-manager/approvals

POST   /api/v1/seo-manager/reports/export
```

---

## SR-SEO-012 — EVENT-DRIVEN ARCHITECTURE

Events:

```text
website.connected
crawl.started
crawl.completed
seo.issue.detected

keyword.rank.changed
keyword.opportunity.detected

competitor.changed
market.trend.detected

content.created
content.updated
content.approved
content.published

organic.traffic.changed
organic.revenue.changed

seo.anomaly.detected
seo.recommendation.created
seo.approval.requested
seo.approval.completed
```

---

## SR-SEO-013 — AI TOOL CONTROL

The AI shall use controlled tools.

Example:

```text
crawl_website
analyze_keywords
analyze_serp
analyze_competitor
query_search_metrics
query_analytics
analyze_content
generate_content_brief
generate_content
analyze_internal_links
create_seo_task
generate_report
request_human_approval
```

The AI shall never receive unrestricted infrastructure access.

---

## SR-SEO-014 — MODEL ROUTING

SalesGenie shall support model abstraction.

```text
AI Router
    ↓
Task Classifier
    ↓
Model Selection
    ├── Fast Model
    ├── Reasoning Model
    ├── Long Context Model
    └── Embedding Model
```

Selection factors:

* Accuracy
* Cost
* Latency
* Context size
* Task complexity
* Availability

---

## 15. SECURITY REQUIREMENTS

## SR-SEO-015 — RBAC

Supported access levels shall include:

```text
Super Admin
Platform Admin
Security Admin
Organization Owner
Organization Admin
Workplace Admin
Marketing Manager
SEO Manager
SEO Specialist
Content Manager
Sales Manager
Sales Agent
Support Agent
End User
```

SEO-specific permissions shall be granular.

---

## SR-SEO-016 — SEO PERMISSION MATRIX

Example:

```text
View SEO Dashboard           → SEO Manager
Run Audit                    → SEO Manager / Specialist
Create Strategy              → SEO Manager
Generate Content             → SEO Manager / Specialist
Publish Content              → Configurable
Change Robots.txt            → Restricted
Change Redirects             → Restricted
Delete SEO Pages             → Restricted
Export SEO Data              → Configurable
Change Integrations          → Admin
```

---

## SR-SEO-017 — AUTHENTICATION

Support:

* OAuth2/OIDC
* JWT
* MFA
* SSO
* Session management
* Token rotation

---

## SR-SEO-018 — SECRETS

API credentials shall be stored using:

* Secrets manager
* Encryption
* Key rotation
* Least privilege

Credentials must never be exposed to LLM prompts or frontend code.

---

## SR-SEO-019 — AI SECURITY

The AI system shall protect against:

* Prompt injection
* Indirect prompt injection
* Malicious website content
* Tool abuse
* Cross-tenant data leakage
* Credential leakage
* Unauthorized publishing
* Unauthorized website modification

---

## SR-SEO-020 — WEBSITE SECURITY

The crawler shall sandbox untrusted content.

It must never execute arbitrary website code within privileged infrastructure.

---

## SR-SEO-021 — AUDIT LOGGING

Audit events shall record:

```text
Actor
Actor Type
Tenant
Organization
Workspace
Action
Resource
Previous State
New State
AI Recommendation
Human Approval
Timestamp
IP / Session Metadata where permitted
```

---

## 16. AI + HUMAN GOVERNANCE

## UR-SEO-058 — HUMAN APPROVAL QUEUE

The manager shall receive:

```text
Pending AI Recommendations
Pending Content
Pending Technical Changes
Pending Publishing
Pending Redirect Changes
Pending Indexation Changes
```

---

## UR-SEO-059 — AI ESCALATION

AI must escalate when:

* Confidence is low
* Data is contradictory
* Website architecture is risky
* Change may affect thousands of URLs
* Revenue impact is material
* Indexation could be affected
* Brand/legal risk exists
* Search-engine compliance is uncertain

---

## UR-SEO-060 — APPROVAL POLICIES

Organization administrators shall configure:

```text
Action
Risk Level
Auto Execute
Human Approval
Required Role
Rollback Available
```

---

## 17. SEO EXPERIMENTATION

## UR-SEO-061 — SEO EXPERIMENTS

The system shall support experiments involving:

* Titles
* Meta descriptions
* Content
* Internal links
* Landing pages
* CTAs
* Page templates

---

## UR-SEO-062 — EXPERIMENT CONTROL

Each experiment shall include:

```text
Hypothesis
Control
Variant
Metric
Expected Outcome
Duration
Sample
Risk
Owner
```

---

## UR-SEO-063 — EXPERIMENT ANALYSIS

The system shall evaluate:

* CTR
* Traffic
* Conversion
* Revenue
* Ranking
* Statistical confidence where appropriate

---

## 18. SEO REPORTING

## UR-SEO-064 — DAILY REPORT

Daily report:

```text
Traffic
Rankings
Critical Issues
New Opportunities
Competitor Changes
Alerts
AI Recommendations
```

---

## UR-SEO-065 — WEEKLY REPORT

Weekly report:

```text
SEO Health
Keyword Growth
Traffic Growth
Content Performance
Technical Issues
Competitor Movement
Leads
Revenue
AI Recommendations
```

---

## UR-SEO-066 — MONTHLY REPORT

Monthly report:

```text
Organic Traffic
Organic Leads
Organic Customers
Organic Revenue
SEO Investment
SEO ROI
Keyword Growth
Top Pages
Lost Pages
Competitor Performance
Technical Health
Content Performance
```

---

## UR-SEO-067 — YEARLY REPORT

Yearly report:

```text
YoY Traffic
YoY Revenue
YoY Leads
YoY Customers
SEO ROI
Market Visibility
Keyword Growth
Product Growth
Country Growth
Competitor Position
```

---

## 19. EXCEL EXPORT

## UR-SEO-068

The platform shall generate Excel workbooks containing:

### Sheet 1 — SEO Overview

```text
Date
Traffic
Clicks
Impressions
CTR
Average Position
Leads
Customers
Revenue
ROI
```

### Sheet 2 — Keywords

```text
Keyword
Intent
Volume
Difficulty
Position
Position Change
URL
Traffic
Opportunity Score
```

### Sheet 3 — Pages

```text
URL
Traffic
Clicks
Impressions
CTR
Position
Conversions
Revenue
SEO Health
```

### Sheet 4 — Technical Issues

```text
URL
Issue
Severity
Impact
Recommendation
Status
```

### Sheet 5 — Competitors

```text
Competitor
Keywords
Visibility
Top Pages
Keyword Gap
Content Gap
```

### Sheet 6 — Content

```text
Content
Keyword
Intent
Traffic
Ranking
Conversions
Revenue
Status
```

---

## 20. ANALYTICS VISUALIZATION

The dashboard shall provide:

```text
Organic Traffic Trend
Keyword Ranking Trend
Visibility Trend
CTR Trend
Conversion Funnel
Revenue Trend
SEO ROI
Keyword Distribution
Competitor Comparison
Technical Health
Content Performance
```

Example:

```text
Organic Traffic

  ^
  |                         █
  |                    █    █
  |              █     █    █
  |        █     █     █    █
  |   █    █     █     █    █
  +---------------------------->
      Jan  Feb  Mar  Apr  May
```

---

## 21. SEO FUNNEL

```text
Search Demand
      ↓
Impressions
      ↓
Clicks
      ↓
Landing Page
      ↓
Engagement
      ↓
Lead
      ↓
MQL
      ↓
SQL
      ↓
Customer
      ↓
Revenue
      ↓
Profit
```

The SEO Manager dashboard should allow drill-down through every stage where data is available.

---

## 22. SEO OPPORTUNITY ENGINE

The platform shall continuously identify opportunities.

Example:

```text
Opportunity:
"AI customer support software"

Current Position:
18

Estimated Business Value:
High

Competitor Strength:
Medium

Content Gap:
High

Recommended Action:
Create authoritative comparison + use-case content.

Expected Impact:
Potential increase in qualified organic traffic.

Confidence:
82%
```

---

## 23. SEO LOSS ANALYSIS

The AI shall investigate traffic/ranking losses.

Potential causes:

```text
Technical Issue
Content Decay
Search Intent Mismatch
Competitor Improvement
Internal Linking Weakness
Indexation Issue
Canonical Issue
Migration Issue
Seasonality
Market Decline
Tracking Error
```

The system shall rank causes by evidence.

It must not state speculative causes as confirmed facts.

---

## 24. CONTENT DECAY ENGINE

The system shall identify pages with:

* Falling traffic
* Falling rankings
* Declining conversions
* Outdated information
* Lost backlinks
* Search-intent mismatch

It shall recommend:

```text
Refresh
Expand
Merge
Redirect
Repurpose
Leave Unchanged
```

High-impact changes require human approval.

---

## 25. SEO ALERT ENGINE

Alerts:

```text
Traffic Drop > Threshold
Ranking Drop > Threshold
Revenue Drop > Threshold
Indexation Drop
Crawl Error Spike
Broken Link Spike
Competitor Ranking Gain
Keyword Opportunity
Content Decay
Technical Regression
```

Alert priority:

```text
Critical
High
Medium
Low
```

---

## 26. SEO KNOWLEDGE GRAPH

Where useful, the platform shall model relationships:

```text
Product
   ↓
Customer
   ↓
Problem
   ↓
Keyword
   ↓
Search Intent
   ↓
Topic
   ↓
Content
   ↓
Landing Page
   ↓
Lead
   ↓
Customer
   ↓
Revenue
```

This graph may be used for:

* Topic discovery
* Internal linking
* Content planning
* Product SEO
* Revenue attribution

---

## 27. SEO AI DECISION PIPELINE

```text
BUSINESS OBJECTIVE
        ↓
PRODUCT INTELLIGENCE
        ↓
MARKET INTELLIGENCE
        ↓
SEARCH INTELLIGENCE
        ↓
COMPETITOR INTELLIGENCE
        ↓
WEBSITE AUDIT
        ↓
KEYWORD INTELLIGENCE
        ↓
SEARCH INTENT
        ↓
OPPORTUNITY SCORE
        ↓
SEO ROADMAP
        ↓
CONTENT / TECHNICAL / AUTHORITY
        ↓
RISK CHECK
        ↓
HUMAN APPROVAL?
      /      \
    YES       NO
     ↓         ↓
 APPROVE    AUTO EXECUTE
     \         /
       EXECUTE
          ↓
       MONITOR
          ↓
       ANALYZE
          ↓
       OPTIMIZE
          ↺
```

---

## 28. AI SEO SPECIALIZATION EXAMPLE

Client:

```text
Product:
Enterprise AI Customer Support Platform

Goal:
Generate qualified enterprise leads

Market:
North America

Target:
B2B companies

SEO Budget:
$30,000/month
```

The AI must first perform:

```text
1. Product analysis
2. Market analysis
3. Search demand analysis
4. Competitor analysis
5. Keyword research
6. Search-intent classification
7. Content gap analysis
8. Technical audit
9. Customer pain-point analysis
10. Revenue opportunity analysis
```

Then produce:

```text
Primary SEO Strategy:
Enterprise AI customer support category ownership

Primary Topics:
AI customer support
AI customer service
Customer service automation
Enterprise AI support
AI support agents

Content Strategy:
Pillar pages
Use cases
Industry pages
Comparison pages
Case studies
Product pages

Technical Strategy:
Improve crawlability
Improve Core Web Vitals
Improve internal linking
Structured data
Indexation optimization

Conversion Strategy:
Product demos
Free trial
Enterprise consultation
```

---

## 29. AI + HUMAN OPERATING MODEL

```text
                  SEO MANAGER
                       │
             ┌─────────┴─────────┐
             │                   │
             ▼                   ▼
        HUMAN SEO             AI SEO
         MANAGER              MANAGER
             │                   │
             │             Research / Analyze
             │                   │
             │             Recommend / Draft
             │                   │
             └─────────┬─────────┘
                       ▼
                 APPROVAL ENGINE
                       │
              ┌────────┴────────┐
              ▼                 ▼
          APPROVED           REJECTED
              │                 │
              ▼                 ▼
          EXECUTION          REVISION
              │
              ▼
          MONITORING
              │
              ▼
         OPTIMIZATION
```

---

## 30. PERFORMANCE REQUIREMENTS

For normal dashboard queries:

```text
P50 < 300 ms
P95 < 1 second
P99 < 2 seconds
```

Long-running tasks shall be asynchronous:

```text
Website Crawl
Large SEO Audit
Competitor Analysis
Keyword Research
Content Generation
Report Generation
Forecasting
```

---

## 31. RELIABILITY

The platform shall implement:

* Retries
* Exponential backoff
* Circuit breakers
* Timeouts
* Idempotency
* Queue-based processing
* Dead-letter queues
* Partial failure handling
* Provider fallback

External SEO/search providers must not become single points of failure.

---

## 32. OBSERVABILITY

The SEO Manager service shall expose:

```text
Metrics
Logs
Traces
Health Checks
AI Execution Metrics
Crawler Metrics
API Metrics
Queue Metrics
Integration Metrics
```

Important metrics:

```text
Crawler Success Rate
API Failure Rate
AI Recommendation Success
Keyword Processing Rate
Audit Completion Time
Report Generation Time
```

---

## 33. AI COST MANAGEMENT

The platform shall track:

```text
LLM Tokens
Embedding Tokens
Search API Usage
Crawler Usage
AI Cost
Cost Per SEO Project
Cost Per Customer
```

Managers shall receive AI cost reports.

---

## 34. RATE LIMITING

The system shall enforce:

* Tenant limits
* User limits
* API limits
* Crawl limits
* Search provider limits
* AI limits

Limits must be configurable according to subscription tier.

---

## 35. SUBSCRIPTION INTEGRATION

SEO Manager capabilities shall integrate with SalesGenie's subscription system.

Example:

```text
Free
    ↓
Basic SEO
    ↓
Professional SEO
    ↓
Business SEO
    ↓
Enterprise SEO
```

Feature limits may include:

```text
Websites
Keywords
Tracked Competitors
Crawled URLs
AI Credits
Reports
Automation
Users
API Calls
```

---

## 36. ROLE-BASED AI AUTONOMY

Subscription and organization policies shall control:

```text
AI Analysis
AI Recommendations
AI Content Generation
AI Technical Changes
AI Publishing
AI Automation
AI Integrations
```

---

## 37. FUNCTIONAL REQUIREMENTS

## FR-SEO-001

The system shall provide an SEO Manager dashboard.

## FR-SEO-002

The system shall support website onboarding.

## FR-SEO-003

The system shall support multiple websites.

## FR-SEO-004

The system shall support SEO projects.

## FR-SEO-005

The system shall support SEO goals.

## FR-SEO-006

The system shall analyze products.

## FR-SEO-007

The system shall analyze markets.

## FR-SEO-008

The system shall analyze search trends.

## FR-SEO-009

The system shall analyze competitors.

## FR-SEO-010

The system shall perform competitor gap analysis.

## FR-SEO-011

The system shall perform keyword research.

## FR-SEO-012

The system shall cluster keywords.

## FR-SEO-013

The system shall classify search intent.

## FR-SEO-014

The system shall calculate keyword opportunities.

## FR-SEO-015

The system shall generate topic clusters.

## FR-SEO-016

The system shall generate SEO strategies.

## FR-SEO-017

The system shall generate SEO roadmaps.

## FR-SEO-018

The system shall perform technical SEO audits.

## FR-SEO-019

The system shall identify technical SEO issues.

## FR-SEO-020

The system shall prioritize technical issues.

## FR-SEO-021

The system shall generate technical fix plans.

## FR-SEO-022

The system shall analyze content.

## FR-SEO-023

The system shall generate content briefs.

## FR-SEO-024

The system shall generate AI-assisted content.

## FR-SEO-025

The system shall support human content review.

## FR-SEO-026

The system shall optimize on-page SEO.

## FR-SEO-027

The system shall analyze internal links.

## FR-SEO-028

The system shall detect orphan pages.

## FR-SEO-029

The system shall support programmatic SEO.

## FR-SEO-030

The system shall support local SEO.

## FR-SEO-031

The system shall support international SEO.

## FR-SEO-032

The system shall support e-commerce SEO.

## FR-SEO-033

The system shall monitor rankings.

## FR-SEO-034

The system shall monitor organic traffic.

## FR-SEO-035

The system shall monitor organic conversions.

## FR-SEO-036

The system shall attribute organic revenue.

## FR-SEO-037

The system shall calculate SEO ROI.

## FR-SEO-038

The system shall forecast SEO performance.

## FR-SEO-039

The system shall detect SEO anomalies.

## FR-SEO-040

The system shall detect content decay.

## FR-SEO-041

The system shall create SEO tasks.

## FR-SEO-042

The system shall prioritize SEO tasks.

## FR-SEO-043

The system shall create SEO alerts.

## FR-SEO-044

The system shall generate SEO reports.

## FR-SEO-045

The system shall generate Excel reports.

## FR-SEO-046

The system shall provide SEO analytics charts.

## FR-SEO-047

The system shall provide AI recommendations.

## FR-SEO-048

The system shall provide AI recommendation evidence.

## FR-SEO-049

The system shall provide AI confidence.

## FR-SEO-050

The system shall support human approval.

## FR-SEO-051

The system shall support human rejection.

## FR-SEO-052

The system shall support human override.

## FR-SEO-053

The system shall support configurable AI autonomy.

## FR-SEO-054

The system shall support SEO workflows.

## FR-SEO-055

The system shall support SEO experiments.

## FR-SEO-056

The system shall track SEO experiment results.

## FR-SEO-057

The system shall maintain audit logs.

## FR-SEO-058

The system shall enforce tenant isolation.

## FR-SEO-059

The system shall enforce RBAC.

## FR-SEO-060

The system shall protect SEO credentials.

## FR-SEO-061

The system shall detect malicious external content.

## FR-SEO-062

The system shall prevent unauthorized AI tool execution.

## FR-SEO-063

The system shall provide rollback for supported automated changes.

## FR-SEO-064

The system shall provide AI cost tracking.

## FR-SEO-065

The system shall enforce subscription limits.

---

## 38. NON-FUNCTIONAL REQUIREMENTS

## NFR-SEO-001 — Availability

Target:

```text
≥ 99.9%
```

for production services, subject to external provider availability.

## NFR-SEO-002 — Scalability

The system shall support horizontal scaling of:

* Crawlers
* AI workers
* Analytics workers
* Report workers
* Integration workers

## NFR-SEO-003 — Security

Enterprise-grade security controls shall protect:

* Website data
* Search data
* Customer data
* Revenue data
* SEO strategies
* API credentials

## NFR-SEO-004 — Reliability

External provider failures shall not crash the core platform.

## NFR-SEO-005 — Observability

All critical SEO workflows shall be observable.

## NFR-SEO-006 — Explainability

AI recommendations shall expose:

* Evidence
* Assumptions
* Confidence
* Risk
* Expected impact

## NFR-SEO-007 — Maintainability

The architecture shall be modular and testable.

## NFR-SEO-008 — Extensibility

New search engines, analytics providers, CMS platforms and SEO tools shall be added through provider abstractions.

## NFR-SEO-009 — Privacy

The platform shall minimize personal data collection and follow applicable privacy requirements.

## NFR-SEO-010 — Disaster Recovery

SEO projects and historical analytics shall be backed up according to enterprise RPO/RTO policies.

---

## 39. ACCEPTANCE CRITERIA

The SEO Manager module shall not be considered production-ready until:

* [ ] SEO Manager workspace exists
* [ ] Website onboarding works
* [ ] Multi-website support works
* [ ] Product analysis works
* [ ] Market analysis works
* [ ] Search trend analysis works
* [ ] Competitor analysis works
* [ ] Competitor gap analysis works
* [ ] Keyword research works
* [ ] Keyword clustering works
* [ ] Search intent classification works
* [ ] Opportunity scoring works
* [ ] Topic clustering works
* [ ] Technical SEO crawler works
* [ ] Technical audit works
* [ ] Issue prioritization works
* [ ] Content briefs work
* [ ] AI content workflow works
* [ ] Human review works
* [ ] On-page optimization works
* [ ] Internal-link analysis works
* [ ] Programmatic SEO safeguards work
* [ ] Local SEO works
* [ ] International SEO works
* [ ] E-commerce SEO works
* [ ] Rank tracking works
* [ ] Organic analytics works
* [ ] Organic conversion tracking works
* [ ] Revenue attribution works
* [ ] SEO ROI works
* [ ] Forecasting works
* [ ] Anomaly detection works
* [ ] Content decay detection works
* [ ] SEO task management works
* [ ] SEO automation works
* [ ] Human approval works
* [ ] Human override works
* [ ] AI autonomy controls work
* [ ] Excel reports work
* [ ] Analytics dashboards work
* [ ] AI explanations work
* [ ] Tenant isolation works
* [ ] RBAC works
* [ ] Audit logging works
* [ ] Credential security works
* [ ] AI security testing passes
* [ ] Integration failure recovery works
* [ ] Load testing passes
* [ ] Disaster recovery testing passes

---

## 40. FAANG-LEVEL SEO DESIGN PRINCIPLES

SalesGenie's SEO Manager shall follow these principles:

1. **Business outcome before vanity metric**
2. **Evidence before recommendation**
3. **Search intent before keyword volume**
4. **Customer need before content creation**
5. **Market intelligence before strategy**
6. **Competitor intelligence before positioning**
7. **Revenue attribution before ROI claims**
8. **Human judgment for high-risk actions**
9. **AI automation for repetitive operations**
10. **Explainable AI**
11. **Configurable autonomy**
12. **Tenant isolation**
13. **Privacy by design**
14. **Security by design**
15. **Continuous experimentation**
16. **Continuous optimization**
17. **Failure-tolerant integrations**
18. **Source-aware intelligence**
19. **Uncertainty-aware forecasting**
20. **Search-engine policy compliance**
21. **No guaranteed ranking claims**
22. **No black-box destructive automation**
23. **Rollback for supported automated changes**
24. **Human override**
25. **Revenue-focused SEO**

---

## 41. FINAL SEO MANAGER OBJECTIVE

The SalesGenie SEO Manager shall evolve SEO from a collection of isolated tools into an intelligent business-growth system.

The complete operating loop shall be:

```text
                 BUSINESS
                    │
                    ▼
                 PRODUCT
                    │
                    ▼
                  MARKET
                    │
                    ▼
              SEARCH DEMAND
                    │
                    ▼
               COMPETITORS
                    │
                    ▼
                 KEYWORDS
                    │
                    ▼
              SEARCH INTENT
                    │
                    ▼
              SEO OPPORTUNITY
                    │
                    ▼
              SEO STRATEGY
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
    TECHNICAL SEO         CONTENT SEO
          │                   │
          └─────────┬─────────┘
                    ▼
             INTERNAL LINKS
                    │
                    ▼
             AUTHORITY / PR
                    │
                    ▼
                RANKINGS
                    │
                    ▼
                 TRAFFIC
                    │
                    ▼
                  LEADS
                    │
                    ▼
                CUSTOMERS
                    │
                    ▼
                 REVENUE
                    │
                    ▼
                 PROFIT
                    │
                    ▼
              AI ANALYSIS
                    │
                    ▼
              OPTIMIZATION
                    │
                    └───────────────↺
```

The ultimate purpose of the SalesGenie SEO Manager is therefore not simply:

```text
"Get higher rankings."
```

It is:

```text
UNDERSTAND THE MARKET
        ↓
UNDERSTAND SEARCH BEHAVIOR
        ↓
UNDERSTAND THE CUSTOMER
        ↓
UNDERSTAND THE COMPETITION
        ↓
IDENTIFY HIGH-VALUE OPPORTUNITIES
        ↓
BUILD THE RIGHT SEO STRATEGY
        ↓
EXECUTE WITH AI + HUMAN CONTROL
        ↓
MEASURE TRAFFIC
        ↓
MEASURE LEADS
        ↓
MEASURE CUSTOMERS
        ↓
MEASURE REVENUE
        ↓
MEASURE PROFIT
        ↓
LEARN
        ↓
OPTIMIZE
        ↓
SCALE
```

The final product should function as an **AI-native SEO Manager capable of market intelligence, technical SEO management, keyword intelligence, content strategy, search-intent analysis, competitor intelligence, SEO automation, organic-growth analytics, revenue attribution, forecasting and continuous optimization while keeping humans in control of high-impact decisions.**
