```markdown
# SALESGENIE — SEO_SPECIALIST.md

> **Document Type:** Role-Specific User Requirements + System Requirements + Functional Requirements
> **Project:** SalesGenie — Enterprise AI Sales, Marketing, Customer Support, SEO, Growth & Business Intelligence SaaS Platform
> **Role:** SEO Specialist
> **Version:** 1.0.0
> **Status:** Production-Grade / FAANG-Level Specification
> **Execution Model:** AI SEO Specialist + Human SEO Specialist + Human-in-the-Loop
> **Primary Objective:** Execute high-quality, evidence-driven SEO analysis, optimization, content, technical SEO, search-intelligence, and growth operations under the strategic governance of the SEO Manager.

---

# 1. ROLE OVERVIEW

The **SEO Specialist** is an execution-focused SEO intelligence role within SalesGenie.

The SEO Specialist operates under the strategic direction of the:

- Organization Owner
- Organization Admin
- Workplace Admin
- Marketing Manager
- SEO Manager

and collaborates with:

- Marketing Specialists
- Content Specialists
- Developers
- Sales Managers
- Sales Agents
- Support Agents
- AI Agents

The SEO Specialist may operate as:

```text
Human SEO Specialist
        +
AI SEO Specialist
        +
Human-in-the-Loop Governance
```

The AI SEO Specialist must be capable of performing repetitive and analytical SEO work while escalating strategic, high-risk, ambiguous, or destructive operations to an authorized human.

---

# 2. PRIMARY MISSION

The SEO Specialist shall help clients increase:

```text
Search Visibility
      ↓
Organic Traffic
      ↓
Qualified Visitors
      ↓
Leads
      ↓
Customers
      ↓
Revenue
      ↓
Profit
```

The SEO Specialist shall therefore optimize for **business outcomes**, not rankings alone.

The platform must avoid treating:

* keyword rankings,
* impressions,
* traffic,
* domain authority,
* backlinks

as the final objective.

These are intermediate indicators.

---

# 3. SEO SPECIALIST OPERATING MODEL

```text
                 SEO MANAGER
                     │
                     ▼
             SEO STRATEGY
                     │
                     ▼
              SEO SPECIALIST
                     │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
Technical SEO    Content SEO    Keyword SEO
      │              │              │
      └──────────────┼──────────────┘
                     ▼
             Optimization Tasks
                     │
                     ▼
               AI Analysis
                     │
                     ▼
              Human Review
                     │
                     ▼
                 Execution
                     │
                     ▼
                Monitoring
                     │
                     ▼
                Reporting
                     │
                     ▼
                Optimization
```

---

# 4. AI + HUMAN EXECUTION MODES

SalesGenie shall support three modes.

## 4.1 Human Mode

```text
SEO Specialist
      ↓
Manual Analysis
      ↓
Manual Decision
      ↓
Manual Execution
```

---

## 4.2 AI-Assisted Mode

```text
SEO Specialist
      ↓
AI Analysis
      ↓
AI Recommendation
      ↓
Human Review
      ↓
Execution
```

---

## 4.3 AI-Autonomous Mode

```text
AI SEO Specialist
      ↓
Observe
      ↓
Analyze
      ↓
Recommend
      ↓
Policy Check
      ↓
Auto Execute Low-Risk Tasks
      ↓
Monitor
      ↓
Escalate High-Risk Tasks
```

AI autonomy must be configurable by:

* Organization
* Workspace
* Website
* SEO Project
* Action type
* Subscription tier
* Risk level

---

# 5. USER REQUIREMENTS

# UR-SEO-S-001 — SEO SPECIALIST DASHBOARD

The SEO Specialist shall have a dedicated dashboard containing:

* SEO health
* Active projects
* Assigned tasks
* Technical issues
* Keyword opportunities
* Ranking changes
* Content tasks
* Competitor changes
* SEO alerts
* AI recommendations
* Pending approvals
* Completed tasks
* Organic traffic
* Organic conversions
* Organic revenue

---

# UR-SEO-S-002 — SPECIALIST WORK QUEUE

The system shall provide a prioritized work queue.

Example:

```text
Priority    Task                         Status
------------------------------------------------
Critical    Fix indexing issue          Pending
High        Optimize product page       In Progress
High        Refresh declining article   Pending
Medium      Internal linking            Pending
Low         Metadata optimization       Pending
```

---

# UR-SEO-S-003 — TASK ASSIGNMENT

SEO Managers shall be able to assign tasks to:

* Human SEO Specialists
* AI SEO Specialists
* Specialist teams

Tasks shall include:

```text
Task ID
Website
Project
Objective
Description
Priority
SEO Impact
Business Impact
Expected Result
Deadline
Owner
Dependencies
Approval Requirement
Status
```

---

# UR-SEO-S-004 — WEBSITE ANALYSIS

The SEO Specialist shall be able to analyze a website.

The analysis shall include:

```text
Technical SEO
On-Page SEO
Content
Internal Linking
Indexation
Performance
Structured Data
Mobile SEO
International SEO
Local SEO
```

---

# UR-SEO-S-005 — BUSINESS CONTEXT

Before performing SEO recommendations, the system shall understand:

* Business type
* Products
* Services
* Target market
* Target customers
* Customer pain points
* Revenue model
* Business objectives
* Geographic market
* Competitors
* Brand guidelines

---

# UR-SEO-S-006 — PRODUCT SEO ANALYSIS

The specialist shall analyze individual products.

For each product:

```text
Product
   ↓
Customer Problem
   ↓
Search Demand
   ↓
Keywords
   ↓
Search Intent
   ↓
Competitors
   ↓
Content Gap
   ↓
SEO Opportunity
```

---

# UR-SEO-S-007 — MARKET SEO ANALYSIS

The system shall analyze:

* Market demand
* Search trends
* Customer questions
* Emerging topics
* Market saturation
* Competitor strength
* Keyword opportunities
* Search intent
* Seasonal trends

---

# UR-SEO-S-008 — KEYWORD RESEARCH

The SEO Specialist shall be able to:

* Discover keywords
* Expand keyword lists
* Cluster keywords
* Identify long-tail keywords
* Identify commercial keywords
* Identify transactional keywords
* Identify informational keywords
* Identify branded keywords
* Identify non-branded keywords
* Identify local keywords

---

# UR-SEO-S-009 — KEYWORD METRICS

The platform shall display available metrics such as:

```text
Keyword
Search Volume
Keyword Difficulty
Competition
CPC
Search Intent
Trend
Current Position
Traffic
CTR
Conversion Potential
Opportunity Score
```

Unavailable metrics must not be fabricated.

---

# UR-SEO-S-010 — SEARCH INTENT

The system shall classify keywords into:

```text
Informational
Navigational
Commercial
Transactional
Local
Branded
Non-Branded
Comparison
Problem/Solution
Product
```

The specialist must be able to override AI classification.

---

# UR-SEO-S-011 — KEYWORD CLUSTERING

The AI shall cluster keywords based on:

* Semantic relationship
* Search intent
* SERP similarity
* Topic
* Product relationship
* User journey

Output:

```text
Pillar Topic
 ├── Cluster A
 │    ├── Keyword 1
 │    ├── Keyword 2
 │    └── Keyword 3
 │
 ├── Cluster B
 │    ├── Keyword 4
 │    └── Keyword 5
```

---

# UR-SEO-S-012 — KEYWORD CANNIBALIZATION

The system shall detect cases where multiple pages compete for the same search intent.

It shall recommend:

```text
Merge
Redirect
Differentiate
Re-optimize
Change Search Intent
Create Separate Content
```

---

# UR-SEO-S-013 — KEYWORD OPPORTUNITY

The AI shall calculate an opportunity score using configurable factors:

```text
Search Demand
Business Relevance
Conversion Potential
Competition
Ranking Difficulty
Current Position
Trend
Content Gap
```

---

# UR-SEO-S-014 — COMPETITOR KEYWORD ANALYSIS

The system shall identify:

* Keywords competitors rank for
* Keywords client ranks for
* Keywords neither ranks strongly for
* Competitor keyword gaps
* High-value missed opportunities

---

# UR-SEO-S-015 — CONTENT GAP ANALYSIS

The specialist shall identify:

* Missing topics
* Missing pages
* Weak pages
* Outdated content
* Missing FAQs
* Missing comparisons
* Missing use cases
* Missing product content

---

# UR-SEO-S-016 — CONTENT BRIEF GENERATION

AI shall generate SEO content briefs containing:

```text
Primary Keyword
Secondary Keywords
Search Intent
Target Audience
Customer Problem
Content Goal
Recommended Title
Recommended Structure
Required Topics
Questions
Entities
Internal Links
External References
CTA
Conversion Objective
```

---

# UR-SEO-S-017 — AI CONTENT ASSISTANCE

The AI Specialist may generate:

* Titles
* Headings
* Outlines
* Meta descriptions
* FAQs
* Product descriptions
* Content drafts
* Content improvements
* Content refresh suggestions

Publishing must follow configured approval policies.

---

# UR-SEO-S-018 — CONTENT OPTIMIZATION

The specialist shall analyze existing content for:

* Search intent
* Topic coverage
* Keyword usage
* Readability
* Structure
* Internal links
* External references
* Conversion opportunities
* Content freshness

---

# UR-SEO-S-019 — CONTENT DECAY

The system shall detect declining pages.

Signals:

```text
Traffic ↓
Rankings ↓
CTR ↓
Conversions ↓
Revenue ↓
```

The AI shall recommend:

```text
Refresh
Expand
Rewrite
Merge
Redirect
Repurpose
Monitor
```

---

# UR-SEO-S-020 — ON-PAGE SEO

The specialist shall optimize:

* Title tags
* Meta descriptions
* H1
* H2/H3
* URLs
* Canonical tags
* Images
* Alt attributes
* Internal links
* Anchor text
* Structured data

---

# UR-SEO-S-021 — TECHNICAL SEO AUDIT

The system shall identify:

```text
404 Errors
5xx Errors
Redirect Chains
Redirect Loops
Broken Links
Duplicate Pages
Duplicate Titles
Missing Titles
Missing Descriptions
Canonical Problems
Robots Issues
Sitemap Issues
Indexation Problems
Orphan Pages
Slow Pages
Mobile Problems
Structured Data Problems
```

---

# UR-SEO-S-022 — TECHNICAL ISSUE PRIORITIZATION

Each issue shall contain:

```text
Issue
Severity
Affected URLs
SEO Impact
Business Impact
Estimated Effort
Recommended Fix
Priority
Owner
Approval Requirement
```

---

# UR-SEO-S-023 — TECHNICAL FIX RECOMMENDATIONS

AI shall produce implementation guidance for developers.

Example:

```text
Problem:
Duplicate canonical URLs.

Cause:
Multiple URL parameters generate identical pages.

Recommendation:
Normalize canonical URLs and configure parameter handling.

Impact:
High.

Risk:
Medium.

Human Approval:
Required.
```

---

# UR-SEO-S-024 — INTERNAL LINKING

The system shall identify:

* Orphan pages
* Weak internal links
* Important pages with few links
* Relevant linking opportunities
* Anchor-text opportunities

---

# UR-SEO-S-025 — INTERNAL LINK RECOMMENDATION

Output:

```text
Source Page
Target Page
Suggested Anchor
Relationship
SEO Benefit
Confidence
```

---

# UR-SEO-S-026 — SITE ARCHITECTURE

The specialist shall analyze:

```text
Homepage
 ↓
Category
 ↓
Subcategory
 ↓
Product / Service
 ↓
Supporting Content
```

The AI shall identify:

* Deep pages
* Poor hierarchy
* Topic fragmentation
* Navigation problems
* Internal authority distribution problems

---

# UR-SEO-S-027 — SITEMAP MANAGEMENT

The system shall:

* Discover XML sitemaps
* Validate sitemap URLs
* Detect errors
* Compare indexed URLs
* Detect missing pages
* Detect stale URLs

---

# UR-SEO-S-028 — ROBOTS ANALYSIS

The system shall analyze robots directives.

Any modification to robots rules shall require configurable approval because incorrect changes can affect large portions of a website.

---

# UR-SEO-S-029 — CANONICAL ANALYSIS

The system shall detect:

* Missing canonical
* Incorrect canonical
* Self-canonical
* Cross-domain canonical
* Canonical conflicts
* Canonicalized pages with unexpected indexing behavior

---

# UR-SEO-S-030 — STRUCTURED DATA

The system shall analyze available structured data including appropriate schema types.

It shall detect:

* Missing schema
* Invalid schema
* Inconsistent schema
* Unsupported implementation

The system must not generate fabricated business/product information.

---

# UR-SEO-S-031 — CORE WEB VITALS

The system shall monitor available performance metrics including:

* LCP
* INP
* CLS

It shall identify pages requiring performance optimization.

---

# UR-SEO-S-032 — MOBILE SEO

The specialist shall monitor:

* Mobile usability
* Responsive layout
* Mobile performance
* Content parity
* Navigation
* Mobile indexing signals

---

# UR-SEO-S-033 — INTERNATIONAL SEO

The system shall support:

* Country targeting
* Language targeting
* hreflang
* Localized keywords
* Regional landing pages
* International competitors

---

# UR-SEO-S-034 — LOCAL SEO

The system shall support:

* Local keywords
* Location pages
* Local content
* Business profile optimization
* NAP consistency
* Review monitoring

The platform shall never create fake reviews or fabricated local business information.

---

# UR-SEO-S-035 — E-COMMERCE SEO

The system shall support:

* Product page optimization
* Category pages
* Product schema
* Product keywords
* Merchant data
* Product availability
* Review content
* Faceted-navigation analysis

---

# UR-SEO-S-036 — PROGRAMMATIC SEO

The specialist shall be able to identify opportunities for scalable pages.

Examples:

```text
Location
Product
Industry
Use Case
Integration
Comparison
Category
```

The system shall prevent low-value page generation.

---

# UR-SEO-S-037 — RANK TRACKING

The system shall track:

* Keyword
* Search engine
* Country
* Language
* Device
* Position
* Position change
* SERP feature
* URL

---

# UR-SEO-S-038 — SERP ANALYSIS

The system shall analyze available search-result information such as:

* Ranking URLs
* Search-result features
* Content formats
* Search intent
* Competitor presence
* Featured-result opportunities

---

# UR-SEO-S-039 — RANKING CHANGE ALERTS

Alerts:

```text
Major Gain
Major Loss
New Ranking
Lost Ranking
Top 3 Entry
Top 10 Entry
Top 10 Exit
```

---

# UR-SEO-S-040 — ORGANIC TRAFFIC ANALYSIS

The specialist shall view:

* Sessions
* Users
* Landing pages
* Countries
* Devices
* Traffic trends
* Traffic sources

---

# UR-SEO-S-041 — SEARCH CONSOLE ANALYSIS

Where authorized, the system shall analyze:

* Queries
* Clicks
* Impressions
* CTR
* Average position
* Pages
* Devices
* Countries

---

# UR-SEO-S-042 — ORGANIC CONVERSION ANALYSIS

The system shall connect:

```text
Organic Search
      ↓
Landing Page
      ↓
Engagement
      ↓
Lead
      ↓
Customer
      ↓
Revenue
```

---

# UR-SEO-S-043 — SEO REVENUE ATTRIBUTION

The system shall display, where data is available:

```text
Organic Leads
Organic Customers
Organic Revenue
SEO Cost
SEO ROI
```

Attribution methodology must be transparent.

---

# UR-SEO-S-044 — SEO PROFIT ANALYSIS

For products:

```text
Organic Traffic
+
Organic Leads
+
Customers
+
Revenue
-
SEO Cost
=
Estimated Profit Contribution
```

The system shall clearly identify estimated values and attribution assumptions.

---

# UR-SEO-S-045 — SEO ANOMALY DETECTION

AI shall detect unusual changes in:

* Traffic
* Rankings
* Clicks
* Impressions
* CTR
* Conversions
* Revenue
* Indexation

---

# UR-SEO-S-046 — LOSS INVESTIGATION

When traffic declines, AI shall investigate possible causes.

Example:

```text
Traffic Loss
    ↓
Technical Check
    ↓
Indexation Check
    ↓
Ranking Check
    ↓
Content Check
    ↓
Competitor Check
    ↓
Seasonality Check
    ↓
Tracking Check
```

The system must distinguish:

```text
Confirmed Evidence
Probable Cause
Possible Cause
Unknown
```

---

# UR-SEO-S-047 — SEO OPPORTUNITY ENGINE

The AI shall continuously discover:

* Quick wins
* Ranking opportunities
* Content gaps
* Internal-link opportunities
* Technical improvements
* Content refresh opportunities
* Conversion opportunities

---

# UR-SEO-S-048 — QUICK-WIN DETECTION

Examples:

```text
Position 4–10 keyword
High impressions
Low CTR
Strong conversion intent
```

Recommended action:

```text
Improve title
Improve description
Improve content
Improve internal linking
Strengthen intent alignment
```

---

# UR-SEO-S-049 — SEO TASK CREATION

The specialist shall create tasks for:

* Developers
* Content team
* Designers
* Marketing team
* SEO team

Tasks shall support:

```text
Owner
Priority
Deadline
Dependency
Status
Evidence
Comments
Approval
```

---

# UR-SEO-S-050 — AI TASK CREATION

AI may automatically create low-risk tasks.

Example:

```text
Detected:
37 orphan pages.

AI Action:
Create internal-linking task.

Approval:
Not required.
```

---

# UR-SEO-S-051 — SEO REPORTING

The specialist shall generate:

### Daily

```text
Ranking changes
Traffic changes
Critical issues
SEO alerts
```

### Weekly

```text
SEO health
Keyword performance
Content performance
Technical issues
Opportunities
```

### Monthly

```text
Organic traffic
Leads
Customers
Revenue
ROI
Keyword growth
Technical health
Competitor movement
```

---

# UR-SEO-S-052 — EXCEL EXPORT

The system shall generate Excel reports containing:

## Sheet 1 — SEO Overview

```text
Date
Organic Traffic
Clicks
Impressions
CTR
Average Position
Leads
Customers
Revenue
SEO Cost
ROI
```

## Sheet 2 — Keywords

```text
Keyword
Intent
Volume
Difficulty
Position
Change
URL
Traffic
Conversions
Opportunity Score
```

## Sheet 3 — Technical Issues

```text
URL
Issue
Severity
Impact
Recommendation
Status
```

## Sheet 4 — Content

```text
URL
Topic
Keyword
Traffic
Ranking
Conversions
Revenue
Content Status
```

## Sheet 5 — Competitors

```text
Competitor
Keyword
Position
Visibility
Keyword Gap
Content Gap
```

---

# UR-SEO-S-053 — SEO ANALYTICS DASHBOARD

Charts shall include:

```text
Organic Traffic
Keyword Growth
Ranking Distribution
CTR
Impressions
Conversions
Revenue
SEO ROI
Technical Health
Content Performance
Competitor Visibility
```

---

# UR-SEO-S-054 — AI RECOMMENDATIONS

Each recommendation shall contain:

```text
Recommendation
Reason
Evidence
Expected Impact
Business Value
Risk
Confidence
Required Action
Approval Requirement
```

---

# UR-SEO-S-055 — HUMAN OVERRIDE

Human specialists shall be able to:

* Modify AI recommendations
* Reject recommendations
* Approve recommendations
* Change priorities
* Edit generated content
* Override keyword classification
* Override search intent
* Pause automation

---

# UR-SEO-S-056 — AI ESCALATION

AI must escalate when:

* Data is incomplete
* Evidence conflicts
* Confidence is low
* Action is destructive
* Thousands of pages are affected
* Indexation may be affected
* Revenue impact is material
* Brand/legal risk exists
* Technical changes are risky

---

# UR-SEO-S-057 — SEO EXPERIMENTS

The specialist shall be able to create experiments for:

* Titles
* Meta descriptions
* Content
* Internal links
* Landing pages
* CTAs
* Page templates

Each experiment shall define:

```text
Hypothesis
Control
Variant
Metric
Expected Result
Duration
Risk
Owner
```

---

# 6. SYSTEM REQUIREMENTS

# SR-SEO-S-001 — SERVICE ARCHITECTURE

The SEO Specialist module shall operate as part of the SEO service architecture.

```text
                    API GATEWAY
                         │
                         ▼
                  SEO SERVICE
                         │
      ┌──────────────────┼──────────────────┐
      ▼                  ▼                  ▼
SEO Intelligence   Technical SEO      Content SEO
      │                  │                  │
      ▼                  ▼                  ▼
Keyword Engine     Audit Engine       Content Engine
      │                  │                  │
      └──────────────────┼──────────────────┘
                         ▼
                  AI SEO ENGINE
                         │
                         ▼
                 WORKFLOW ENGINE
                         │
                         ▼
                  HUMAN APPROVAL
```

---

# SR-SEO-S-002 — MULTI-TENANCY

Every SEO resource shall be tenant-isolated.

Required identifiers:

```text
tenant_id
organization_id
workspace_id
website_id
project_id
user_id
```

Cross-tenant access shall be denied by default.

---

# SR-SEO-S-003 — DATABASE ENTITIES

Required entities:

```text
SEOSpecialist
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
ContentBrief
SEOContent
SEOPage
SEORecommendation
SEOApproval
SEOTask
SEOExperiment
RankSnapshot
OrganicMetric
SEOAttribution
SEOAlert
SEOReport
SEOIntegration
SEOWorkflow
SEOExecution
```

---

# SR-SEO-S-004 — WEBSITE CRAWLER

The crawler shall support:

```text
URL discovery
HTML parsing
Metadata extraction
Heading extraction
Link extraction
Image extraction
Structured-data extraction
Canonical extraction
Robots analysis
Sitemap discovery
HTTP status analysis
```

The crawler must respect applicable:

* robots directives
* crawl limits
* authentication boundaries
* provider policies
* applicable terms

---

# SR-SEO-S-005 — DISTRIBUTED CRAWLING

Crawler jobs shall use:

```text
URL Queue
      ↓
Worker Pool
      ↓
Fetcher
      ↓
Parser
      ↓
SEO Analyzer
      ↓
Issue Engine
```

---

# SR-SEO-S-006 — JOB PROCESSING

Long-running operations shall be asynchronous.

Examples:

```text
Website Crawl
Technical Audit
Keyword Research
Competitor Analysis
Content Analysis
Report Generation
Forecasting
```

Required mechanisms:

* Queue
* Retry
* Backoff
* Timeout
* Idempotency
* Dead-letter queue
* Job status

---

# SR-SEO-S-007 — EXTERNAL PROVIDER ABSTRACTION

SEO data providers shall use adapter interfaces.

```text
SearchProvider
AnalyticsProvider
RankProvider
CMSProvider
CrawlProvider
```

This prevents vendor lock-in.

---

# SR-SEO-S-008 — ANALYTICS INTEGRATION

The system shall support authorized integrations with:

```text
Google Search Console
Google Analytics
Bing Webmaster Tools
CRM
CMS
E-commerce systems
```

The implementation shall use official or authorized APIs where available.

---

# SR-SEO-S-009 — CMS INTEGRATION

Potential integrations:

```text
WordPress
Shopify
Webflow
Headless CMS
Custom CMS
```

---

# SR-SEO-S-010 — API DESIGN

Example:

```http
GET    /api/v1/seo/specialist/dashboard

GET    /api/v1/seo/specialist/tasks
POST   /api/v1/seo/specialist/tasks

POST   /api/v1/seo/specialist/audit
GET    /api/v1/seo/specialist/audit/issues

POST   /api/v1/seo/specialist/keywords/research
POST   /api/v1/seo/specialist/keywords/cluster
POST   /api/v1/seo/specialist/keywords/intent

POST   /api/v1/seo/specialist/content/analyze
POST   /api/v1/seo/specialist/content/brief
POST   /api/v1/seo/specialist/content/optimize

POST   /api/v1/seo/specialist/internal-links/analyze

GET    /api/v1/seo/specialist/rankings
GET    /api/v1/seo/specialist/analytics

GET    /api/v1/seo/specialist/recommendations
POST   /api/v1/seo/specialist/recommendations/{id}/approve
POST   /api/v1/seo/specialist/recommendations/{id}/reject

POST   /api/v1/seo/specialist/reports/export
```

---

# SR-SEO-S-011 — EVENT-DRIVEN ARCHITECTURE

Events shall include:

```text
website.connected
crawl.started
crawl.completed
seo.issue.detected

keyword.created
keyword.rank.changed
keyword.opportunity.detected

content.analysis.completed
content.brief.created
content.updated
content.approved

competitor.changed
seo.anomaly.detected

seo.recommendation.created
seo.approval.requested
seo.approval.completed

seo.task.created
seo.task.completed
seo.report.generated
```

---

# SR-SEO-S-012 — AI TOOLING

The AI Specialist shall have access only to approved tools.

Example:

```text
crawl_website
analyze_website
research_keywords
cluster_keywords
classify_intent
analyze_serp
analyze_competitor
analyze_content
analyze_internal_links
create_task
generate_content_brief
generate_metadata
generate_report
request_approval
```

The model shall never receive unrestricted infrastructure access.

---

# SR-SEO-S-013 — AI MODEL ROUTING

```text
                  AI ROUTER
                     │
           ┌─────────┼─────────┐
           ▼         ▼         ▼
       Fast Model  Reasoning  Long Context
                     Model        Model
```

Routing factors:

* Task complexity
* Accuracy requirement
* Context length
* Latency
* Cost
* Provider availability

---

# SR-SEO-S-014 — AI MEMORY

The AI shall maintain controlled context including:

```text
Business Profile
SEO Strategy
Website Structure
Keyword Strategy
Brand Guidelines
Competitor List
Historical Performance
Previous Decisions
Approved Recommendations
Rejected Recommendations
```

Sensitive information shall not be unnecessarily included in prompts.

---

# 7. SECURITY REQUIREMENTS

# SR-SEO-S-015 — RBAC

SEO Specialist permissions shall be granular.

Example:

```text
View SEO Data              ALLOW
Run Audit                  ALLOW
Keyword Research           ALLOW
Create Recommendation      ALLOW
Generate Content           ALLOW
Edit Content               ALLOW
Publish Content            CONFIGURABLE
Modify Robots.txt          RESTRICTED
Modify Redirects           RESTRICTED
Delete Pages               RESTRICTED
Change Integrations        ADMIN
```

---

# SR-SEO-S-016 — AUTHENTICATION

Support:

* OAuth2/OIDC
* JWT
* MFA
* SSO
* Session management
* Token rotation

---

# SR-SEO-S-017 — CREDENTIAL SECURITY

API credentials must be:

* Encrypted
* Stored in a secrets manager
* Rotatable
* Least-privilege
* Never exposed to frontend
* Never included in LLM context

---

# SR-SEO-S-018 — AI SECURITY

The platform shall defend against:

```text
Prompt Injection
Indirect Prompt Injection
Malicious Web Content
Tool Abuse
Credential Leakage
Cross-Tenant Data Leakage
Unauthorized Publishing
Unauthorized Website Modification
```

---

# SR-SEO-S-019 — UNTRUSTED WEBSITE CONTENT

Website content must be treated as untrusted input.

The crawler must not execute arbitrary website code with privileged access.

---

# SR-SEO-S-020 — AUDIT LOGGING

Every meaningful SEO operation shall log:

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
AI/Human
Approval
Timestamp
```

---

# 8. AI GOVERNANCE

# SR-SEO-S-021 — AI CONFIDENCE

AI recommendations shall include:

```text
Confidence
Evidence
Assumptions
Expected Impact
Risk
```

---

# SR-SEO-S-022 — AI DECISION CLASSES

```text
LOW RISK
Generate report
Generate keyword list
Generate content outline
Create task

MEDIUM RISK
Modify metadata
Internal-link recommendations
Content changes

HIGH RISK
Publish content
Change canonical
Change robots
Change redirects
Delete pages
Mass URL modifications
```

---

# SR-SEO-S-023 — APPROVAL ENGINE

Approval workflow:

```text
AI Recommendation
       ↓
Risk Classification
       ↓
Policy Evaluation
       ↓
Auto Execute?
    /        \
  YES        NO
   ↓          ↓
Execute     Approval
             ↓
       SEO Specialist
             ↓
       SEO Manager
             ↓
          Execute
```

---

# SR-SEO-S-024 — HUMAN OVERRIDE

Human specialists shall always be able to:

* Stop automation
* Reject AI decisions
* Edit AI output
* Change priorities
* Request re-analysis
* Roll back supported changes

---

# 9. FUNCTIONAL REQUIREMENTS

## FR-SEO-S-001

The system shall authenticate SEO Specialists.

## FR-SEO-S-002

The system shall authorize SEO Specialist permissions.

## FR-SEO-S-003

The system shall display an SEO Specialist dashboard.

## FR-SEO-S-004

The system shall display assigned SEO tasks.

## FR-SEO-S-005

The system shall support SEO task creation.

## FR-SEO-S-006

The system shall support task assignment.

## FR-SEO-S-007

The system shall support task prioritization.

## FR-SEO-S-008

The system shall support website onboarding.

## FR-SEO-S-009

The system shall crawl websites.

## FR-SEO-S-010

The system shall perform technical SEO audits.

## FR-SEO-S-011

The system shall identify technical SEO issues.

## FR-SEO-S-012

The system shall prioritize technical issues.

## FR-SEO-S-013

The system shall analyze robots directives.

## FR-SEO-S-014

The system shall analyze XML sitemaps.

## FR-SEO-S-015

The system shall analyze canonicalization.

## FR-SEO-S-016

The system shall analyze redirects.

## FR-SEO-S-017

The system shall detect broken links.

## FR-SEO-S-018

The system shall detect orphan pages.

## FR-SEO-S-019

The system shall analyze structured data.

## FR-SEO-S-020

The system shall analyze Core Web Vitals where data is available.

## FR-SEO-S-021

The system shall analyze mobile SEO.

## FR-SEO-S-022

The system shall perform keyword research.

## FR-SEO-S-023

The system shall cluster keywords.

## FR-SEO-S-024

The system shall classify search intent.

## FR-SEO-S-025

The system shall detect keyword cannibalization.

## FR-SEO-S-026

The system shall identify keyword opportunities.

## FR-SEO-S-027

The system shall analyze competitor keywords.

## FR-SEO-S-028

The system shall perform content-gap analysis.

## FR-SEO-S-029

The system shall generate content briefs.

## FR-SEO-S-030

The system shall analyze existing content.

## FR-SEO-S-031

The system shall detect content decay.

## FR-SEO-S-032

The system shall generate metadata recommendations.

## FR-SEO-S-033

The system shall analyze internal linking.

## FR-SEO-S-034

The system shall identify internal-link opportunities.

## FR-SEO-S-035

The system shall support local SEO.

## FR-SEO-S-036

The system shall support international SEO.

## FR-SEO-S-037

The system shall support e-commerce SEO.

## FR-SEO-S-038

The system shall support programmatic SEO analysis.

## FR-SEO-S-039

The system shall monitor keyword rankings.

## FR-SEO-S-040

The system shall detect ranking changes.

## FR-SEO-S-041

The system shall integrate search-performance data.

## FR-SEO-S-042

The system shall analyze organic traffic.

## FR-SEO-S-043

The system shall analyze organic conversions.

## FR-SEO-S-044

The system shall attribute organic revenue where data is available.

## FR-SEO-S-045

The system shall calculate SEO ROI.

## FR-SEO-S-046

The system shall detect SEO anomalies.

## FR-SEO-S-047

The system shall investigate SEO losses.

## FR-SEO-S-048

The system shall generate SEO recommendations.

## FR-SEO-S-049

The system shall provide recommendation evidence.

## FR-SEO-S-050

The system shall provide AI confidence.

## FR-SEO-S-051

The system shall create SEO tasks from AI recommendations.

## FR-SEO-S-052

The system shall support human approval.

## FR-SEO-S-053

The system shall support human rejection.

## FR-SEO-S-054

The system shall support human override.

## FR-SEO-S-055

The system shall support configurable AI autonomy.

## FR-SEO-S-056

The system shall support SEO experiments.

## FR-SEO-S-057

The system shall generate daily SEO reports.

## FR-SEO-S-058

The system shall generate weekly SEO reports.

## FR-SEO-S-059

The system shall generate monthly SEO reports.

## FR-SEO-S-060

The system shall export SEO data to Excel.

## FR-SEO-S-061

The system shall display SEO analytics charts.

## FR-SEO-S-062

The system shall enforce tenant isolation.

## FR-SEO-S-063

The system shall maintain audit logs.

## FR-SEO-S-064

The system shall secure external credentials.

## FR-SEO-S-065

The system shall protect AI tool execution.

---

# 10. SEO SPECIALIST WORKFLOW

```text
LOGIN
  ↓
SEO SPECIALIST DASHBOARD
  ↓
SELECT WEBSITE / PROJECT
  ↓
LOAD BUSINESS CONTEXT
  ↓
CHECK CURRENT SEO STATE
  ↓
MARKET ANALYSIS
  ↓
KEYWORD ANALYSIS
  ↓
COMPETITOR ANALYSIS
  ↓
TECHNICAL AUDIT
  ↓
CONTENT AUDIT
  ↓
OPPORTUNITY DISCOVERY
  ↓
TASK PRIORITIZATION
  ↓
AI RECOMMENDATION
  ↓
RISK CLASSIFICATION
  ↓
┌─────────────────────┐
│ Human Approval?     │
└─────────┬───────────┘
          │
     ┌────┴────┐
     ▼         ▼
    YES        NO
     │         │
 HUMAN REVIEW  POLICY CHECK
     │         │
     └────┬────┘
          ▼
       EXECUTION
          ↓
       MONITORING
          ↓
       ANALYTICS
          ↓
       REPORTING
          ↓
      OPTIMIZATION
```

---

# 11. SEO SPECIALIST AI DECISION ENGINE

The AI Specialist shall follow:

```text
STEP 1
Understand business objective

STEP 2
Understand product

STEP 3
Understand target customer

STEP 4
Analyze market

STEP 5
Analyze search demand

STEP 6
Analyze competitors

STEP 7
Analyze website

STEP 8
Identify SEO problems

STEP 9
Identify SEO opportunities

STEP 10
Prioritize opportunities

STEP 11
Generate recommendations

STEP 12
Calculate confidence and risk

STEP 13
Request human approval where required

STEP 14
Execute permitted actions

STEP 15
Monitor results

STEP 16
Compare against baseline

STEP 17
Generate new recommendations
```

---

# 12. EXAMPLE — NEW PRODUCT SEO

Suppose the client launches:

```text
AI Customer Support Platform
```

The AI SEO Specialist shall perform:

```text
Product Analysis
       ↓
Target Customer Analysis
       ↓
Market Analysis
       ↓
Competitor Analysis
       ↓
Search Demand Analysis
       ↓
Keyword Discovery
       ↓
Search Intent
       ↓
SERP Analysis
       ↓
Content Gap
       ↓
Technical Website Audit
       ↓
SEO Strategy
```

Then recommend:

```text
Product Landing Page
        +
Use-Case Pages
        +
Industry Pages
        +
Comparison Pages
        +
Educational Content
        +
Case Studies
        +
FAQ Content
```

---

# 13. EXAMPLE — SEO PROBLEM INVESTIGATION

Problem:

```text
Organic Traffic ↓ 38%
```

AI workflow:

```text
Traffic Analysis
       ↓
Ranking Analysis
       ↓
Indexation Analysis
       ↓
Technical Audit
       ↓
Content Decay
       ↓
Competitor Movement
       ↓
Seasonality
       ↓
Tracking Validation
```

Output:

```text
Finding:
62% of traffic loss is associated with ranking declines
across 14 high-value pages.

Confidence:
High

Additional Possible Causes:
Content freshness
Competitor improvements

Recommended Actions:
Refresh affected pages
Analyze competitor changes
Improve internal linking
Validate technical indexation
```

---

# 14. SEO SPECIALIST COLLABORATION

The SEO Specialist shall communicate with other SalesGenie modules.

```text
SEO Specialist
     │
     ├── Marketing Manager
     │
     ├── Marketing Specialist
     │
     ├── Content Team
     │
     ├── Sales Manager
     │
     ├── Sales Agent
     │
     ├── Product Team
     │
     ├── Developer
     │
     └── AI Agents
```

Example:

```text
SEO Specialist
      ↓
Detects high-value keyword
      ↓
Marketing Specialist
      ↓
Creates campaign
      ↓
Sales Agent
      ↓
Uses resulting leads
      ↓
CRM
      ↓
Revenue
      ↓
SEO Attribution
```

---

# 15. SEO + SALES INTEGRATION

The SEO Specialist shall be able to identify:

```text
Keyword
   ↓
Landing Page
   ↓
Lead
   ↓
Sales Opportunity
   ↓
Customer
   ↓
Revenue
```

This enables the system to identify keywords that produce actual business value.

Example:

```text
Keyword A
Traffic: 10,000
Leads: 20
Customers: 1

Keyword B
Traffic: 2,000
Leads: 100
Customers: 15

AI Recommendation:
Prioritize Keyword B.
```

The platform shall therefore optimize for **qualified demand**, not traffic volume alone.

---

# 16. SEO + MARKETING INTEGRATION

The SEO Specialist shall exchange data with:

```text
Marketing Manager
Marketing Specialist
Campaign Manager
Content Engine
Advertising Engine
Social Media Engine
```

This enables:

```text
SEO Trends
     +
Advertising Trends
     +
Social Trends
     +
Customer Data
     ↓
Unified Growth Intelligence
```

---

# 17. SEO + BUSINESS ANALYTICS

The specialist shall be able to investigate:

```text
Which products receive the most organic traffic?
Which products generate the most leads?
Which products generate the most customers?
Which products generate the most revenue?
Which keywords generate the highest-value customers?
Which pages generate losses?
```

The system shall provide evidence-based answers wherever sufficient data exists.

---

# 18. SEO QUALITY CONTROL

Every AI-generated SEO recommendation shall pass:

```text
Data Validation
      ↓
Tenant Validation
      ↓
Policy Validation
      ↓
SEO Validation
      ↓
Business Validation
      ↓
Risk Classification
      ↓
Human Approval if Required
```

---

# 19. SEO ANTI-SPAM REQUIREMENTS

The platform shall explicitly prevent or flag:

* Keyword stuffing
* Automatically generated low-value pages
* Duplicate content at scale
* Hidden text
* Manipulative redirects
* Fake reviews
* Artificial engagement
* Deceptive backlinks
* Cloaking
* Malicious structured data
* Automatically generated spam

The system shall prioritize sustainable search visibility over manipulative short-term tactics.

---

# 20. PERFORMANCE REQUIREMENTS

Dashboard targets:

```text
P50 < 300 ms
P95 < 1 second
P99 < 2 seconds
```

Long-running jobs shall be asynchronous.

Examples:

```text
Large Crawl
Keyword Research
Competitor Analysis
Content Analysis
Report Generation
```

---

# 21. RELIABILITY REQUIREMENTS

The system shall implement:

* Retry
* Exponential backoff
* Circuit breaker
* Timeout
* Idempotency
* Dead-letter queue
* Provider fallback
* Partial failure recovery

---

# 22. OBSERVABILITY

The system shall expose:

```text
API Metrics
Crawler Metrics
AI Metrics
Queue Metrics
Integration Metrics
Error Metrics
Latency Metrics
```

AI metrics:

```text
AI Tasks
AI Success Rate
AI Failure Rate
AI Cost
AI Latency
Human Escalations
Recommendation Acceptance Rate
Recommendation Rejection Rate
```

---

# 23. AI COST MANAGEMENT

The system shall track:

```text
LLM Tokens
Embedding Usage
Search API Usage
Crawler Usage
Total AI Cost
Cost Per Website
Cost Per SEO Project
Cost Per Customer
```

---

# 24. SUBSCRIPTION INTEGRATION

SEO Specialist capabilities shall respect SalesGenie subscription limits.

Possible limits:

```text
Websites
Tracked Keywords
Tracked Competitors
Crawled URLs
AI Credits
Reports
Automation
Users
API Calls
```

The system shall prevent unauthorized resource consumption.

---

# 25. ACCEPTANCE CRITERIA

The SEO Specialist module shall not be considered production-ready until:

* [ ] SEO Specialist dashboard works
* [ ] Task queue works
* [ ] Task assignment works
* [ ] Website onboarding works
* [ ] Website crawling works
* [ ] Technical SEO auditing works
* [ ] Keyword research works
* [ ] Keyword clustering works
* [ ] Search-intent classification works
* [ ] Keyword opportunity scoring works
* [ ] Competitor analysis works
* [ ] Content gap analysis works
* [ ] Content analysis works
* [ ] Content briefs work
* [ ] On-page optimization works
* [ ] Internal-link analysis works
* [ ] Sitemap analysis works
* [ ] Robots analysis works
* [ ] Canonical analysis works
* [ ] Structured-data analysis works
* [ ] Mobile SEO analysis works
* [ ] International SEO works
* [ ] Local SEO works
* [ ] E-commerce SEO works
* [ ] Programmatic SEO analysis works
* [ ] Rank tracking works
* [ ] Organic traffic analytics works
* [ ] Conversion analytics works
* [ ] Revenue attribution works
* [ ] SEO ROI works
* [ ] SEO anomaly detection works
* [ ] SEO loss analysis works
* [ ] SEO opportunity engine works
* [ ] AI recommendations work
* [ ] AI confidence works
* [ ] Human review works
* [ ] Human override works
* [ ] AI autonomy controls work
* [ ] SEO experiments work
* [ ] Daily reports work
* [ ] Weekly reports work
* [ ] Monthly reports work
* [ ] Excel exports work
* [ ] Analytics charts work
* [ ] RBAC works
* [ ] Tenant isolation works
* [ ] Audit logging works
* [ ] Credential security works
* [ ] Prompt-injection defenses work
* [ ] AI tool permissions work
* [ ] Subscription limits work
* [ ] Failure recovery works
* [ ] Observability works
* [ ] Load testing passes
* [ ] Security testing passes
* [ ] Disaster recovery testing passes

---

# 26. FAANG-LEVEL DESIGN PRINCIPLES

The SalesGenie SEO Specialist shall follow:

1. **Business outcome over vanity metrics**
2. **Evidence before recommendation**
3. **Search intent before keyword volume**
4. **Customer problem before content**
5. **Market analysis before optimization**
6. **Competitor intelligence before strategic execution**
7. **Revenue attribution before ROI claims**
8. **AI automation for repetitive operations**
9. **Human control for high-risk operations**
10. **Explainable AI**
11. **Configurable autonomy**
12. **Tenant isolation**
13. **Security by design**
14. **Privacy by design**
15. **Continuous monitoring**
16. **Continuous experimentation**
17. **Continuous optimization**
18. **Provider abstraction**
19. **Failure-tolerant architecture**
20. **No guaranteed ranking claims**
21. **No fabricated SEO metrics**
22. **No deceptive SEO practices**
23. **No uncontrolled mass publishing**
24. **Human override at every high-impact decision point**
25. **SEO must ultimately contribute to measurable business growth**

---

# 27. FINAL SEO SPECIALIST OBJECTIVE

The SalesGenie SEO Specialist shall function as an intelligent SEO execution layer between the organization's SEO strategy and measurable business outcomes.

The complete operating loop shall be:

```text
              BUSINESS OBJECTIVE
                      ↓
                  PRODUCT
                      ↓
                   MARKET
                      ↓
               SEARCH DEMAND
                      ↓
                 KEYWORDS
                      ↓
              SEARCH INTENT
                      ↓
                COMPETITORS
                      ↓
                 WEBSITE
                      ↓
             TECHNICAL AUDIT
                      ↓
               CONTENT AUDIT
                      ↓
             SEO OPPORTUNITIES
                      ↓
              PRIORITIZATION
                      ↓
             AI RECOMMENDATION
                      ↓
               RISK ANALYSIS
                      ↓
          ┌───────────┴───────────┐
          ▼                       ▼
     LOW RISK                 HIGH RISK
          │                       │
   AI AUTO-EXECUTE          HUMAN REVIEW
          │                       │
          └───────────┬───────────┘
                      ▼
                  EXECUTION
                      ↓
                 MONITORING
                      ↓
                 ANALYTICS
                      ↓
                  LEADS
                      ↓
                 CUSTOMERS
                      ↓
                  REVENUE
                      ↓
                   PROFIT
                      ↓
              LEARNING ENGINE
                      ↓
                OPTIMIZATION
                      ↺
```

The final objective is not merely:

```text
"Improve SEO."
```

It is:

```text
UNDERSTAND THE CLIENT
        ↓
UNDERSTAND THE PRODUCT
        ↓
UNDERSTAND THE MARKET
        ↓
UNDERSTAND SEARCH BEHAVIOR
        ↓
UNDERSTAND COMPETITORS
        ↓
IDENTIFY HIGH-VALUE SEO OPPORTUNITIES
        ↓
EXECUTE TECHNICAL + CONTENT + ON-PAGE SEO
        ↓
MEASURE ORGANIC TRAFFIC
        ↓
MEASURE QUALIFIED LEADS
        ↓
MEASURE CUSTOMERS
        ↓
MEASURE REVENUE
        ↓
MEASURE PROFIT
        ↓
LEARN FROM RESULTS
        ↓
CONTINUOUSLY OPTIMIZE
        ↓
SCALE CLIENT GROWTH
```

**SalesGenie SEO Specialist = AI-powered SEO execution + human expertise + technical SEO intelligence + search intelligence + content optimization + competitive intelligence + measurable revenue growth.**

```
