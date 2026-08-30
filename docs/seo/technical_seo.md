# SALESGENIE — TECHNICAL SEO

## FAANG-Level User Requirements, System Requirements & Functional Requirements

**Document:** `technical_seo.md`  
**Product:** SalesGenie  
**Module:** AI-Powered + Humanized Technical SEO Platform  
**Version:** 1.0.0  
**Status:** Production Requirements Baseline  
**Architecture:** Enterprise SaaS · Multi-Tenant · Microservices · Event-Driven · AI + Human-in-the-Loop

---

## 1. PURPOSE

The Technical SEO module is a core component of SalesGenie's SEO and digital growth platform.

Its purpose is to continuously analyze, diagnose, prioritize, remediate, monitor, and optimize the technical health of customer websites and digital properties.

The system shall combine:

- AI-based technical SEO analysis;
- deterministic rule-based SEO validation;
- automated website crawling;
- search-engine accessibility analysis;
- performance analysis;
- structured-data validation;
- JavaScript rendering analysis;
- mobile usability analysis;
- international SEO analysis;
- crawl-budget analysis;
- indexation analysis;
- internal-link analysis;
- URL architecture analysis;
- sitemap analysis;
- robots.txt analysis;
- canonical analysis;
- redirect analysis;
- HTTP status analysis;
- Core Web Vitals analysis;
- security-related SEO checks;
- accessibility-related SEO signals where relevant;
- competitor technical benchmarking;
- human SEO specialist review;
- automated recommendations;
- controlled remediation;
- continuous monitoring.

The system must not merely report SEO errors.

It must determine:

> **What is wrong → why it matters → how severe it is → what caused it → how to fix it → whether AI can safely fix it → whether human approval is required → whether the fix actually improved the business outcome.**

---

## 2. PRODUCT OBJECTIVE

SalesGenie's Technical SEO engine shall transform technical website data into prioritized business actions.

The primary workflow is:

```text
Website
   ↓
Technical Crawl
   ↓
Rendering
   ↓
SEO Signal Extraction
   ↓
Validation
   ↓
Issue Detection
   ↓
Root-Cause Analysis
   ↓
Business Impact Analysis
   ↓
Prioritization
   ↓
AI Recommendation
   ↓
Human Review
   ↓
Remediation
   ↓
Validation
   ↓
Monitoring
   ↓
Performance Feedback
```

---

## 3. CORE PRODUCT PRINCIPLES

The module shall follow:

1. **Business-impact-first SEO**
2. **Search-engine accessibility**
3. **Evidence-based diagnosis**
4. **AI-assisted decision making**
5. **Human control**
6. **Safe automation**
7. **Continuous monitoring**
8. **Explainability**
9. **Tenant isolation**
10. **Security by design**
11. **Performance by design**
12. **Reversible automation**
13. **Observability**
14. **Auditability**
15. **No blind AI changes**

---

## 4. SUPPORTED USERS

The module shall support:

* Super Admin
* Platform Admin
* Security Admin
* Organization Owner
* Organization Admin
* Workplace Admin
* Team Manager
* SEO Manager
* SEO Specialist
* Marketing Manager
* Marketing Specialist
* Product Manager
* Business Analyst
* Developer
* AI Agent Builder
* Sales Manager
* Sales Agent
* Support Manager
* Support Agent
* End User / Client
* External Consultant
* Human SEO Expert

Permissions shall be determined through RBAC + ABAC.

---

## 5. USER REQUIREMENTS

## UR-001 — Website Registration

Users shall be able to register websites for technical SEO monitoring.

Required information may include:

```text
Website URL
Project Name
Business Type
Industry
Target Countries
Target Languages
Primary Domain
Competitors
CMS
Technology Stack
SEO Goals
```

---

## UR-002 — Website Verification

The platform shall support website ownership verification using appropriate methods such as:

* DNS;
* HTML file;
* HTML meta tag;
* supported analytics integrations;
* search-console integrations.

---

## UR-003 — Crawl Configuration

Users shall be able to configure:

* crawl frequency;
* maximum URLs;
* crawl depth;
* URL patterns;
* excluded paths;
* allowed paths;
* user-agent;
* JavaScript rendering;
* sitemap discovery;
* robots.txt handling;
* crawl concurrency where permitted.

---

## UR-004 — Automated Technical Audit

Users shall be able to launch a complete technical SEO audit.

The audit shall evaluate:

```text
Crawlability
Indexability
Performance
Mobile SEO
Architecture
Internal Linking
Canonicalization
Redirects
HTTP Status
Sitemaps
Robots.txt
Structured Data
Metadata
JavaScript SEO
International SEO
URL Structure
Content Accessibility
Security-related SEO signals
```

---

## UR-005 — Continuous Technical Monitoring

Users shall be able to configure recurring audits.

Example:

```text
Daily
Weekly
Biweekly
Monthly
Custom
```

The platform shall compare current results against historical results.

---

## UR-006 — Technical SEO Health Score

The system shall calculate an overall Technical SEO Health Score.

Example:

```text
Technical SEO Health
        ↓
Crawlability
Indexability
Performance
Mobile
Architecture
Structured Data
Internal Links
International SEO
Security
        ↓
Weighted Health Score
```

The scoring model must be transparent and configurable.

---

## UR-007 — Severity Classification

Technical issues shall be categorized as:

```text
Critical
High
Medium
Low
Informational
```

---

## UR-008 — Business Impact Classification

Issues shall also be classified according to business impact:

```text
Revenue Impact
Traffic Impact
Conversion Impact
Visibility Impact
Crawl Impact
UX Impact
Security Impact
Low Impact
```

---

## UR-009 — Crawlability Analysis

The system shall identify issues affecting search-engine crawling.

Examples:

* robots.txt blocking;
* excessive redirects;
* crawl traps;
* infinite URL spaces;
* broken links;
* inaccessible resources;
* server errors;
* malformed URLs.

---

## UR-010 — Indexability Analysis

The system shall detect:

* noindex directives;
* conflicting directives;
* canonical conflicts;
* inaccessible pages;
* duplicate URLs;
* soft 404s;
* indexing inconsistencies;
* unexpected indexable pages.

---

## UR-011 — Robots.txt Analysis

The system shall analyze:

```text
Syntax
Rules
Allow directives
Disallow directives
Sitemap declarations
Potential accidental blocks
```

AI shall explain the business impact of dangerous rules.

---

## UR-012 — XML Sitemap Analysis

The system shall validate:

* sitemap accessibility;
* XML validity;
* URL format;
* duplicate URLs;
* broken URLs;
* canonical consistency;
* indexable URL coverage;
* last modification information where available;
* sitemap index structure.

---

## UR-013 — Sitemap Coverage Analysis

The platform shall compare:

```text
Sitemap URLs
vs
Crawled URLs
vs
Indexable URLs
vs
Canonical URLs
```

and identify discrepancies.

---

## UR-014 — HTTP Status Analysis

The crawler shall identify:

```text
200
3xx
4xx
5xx
Soft 404
Timeout
DNS failure
TLS failure
```

and classify their SEO significance.

---

## UR-015 — Redirect Analysis

The system shall detect:

* redirect chains;
* redirect loops;
* excessive redirects;
* incorrect redirects;
* HTTP → HTTPS issues;
* legacy URL problems;
* temporary vs permanent redirect inconsistencies.

---

## UR-016 — Canonical Analysis

The system shall analyze:

* canonical tags;
* canonical consistency;
* self-referencing canonicals;
* cross-domain canonicals where applicable;
* canonical loops;
* conflicting canonical signals;
* canonicalized pages that remain internally linked.

---

## UR-017 — Duplicate URL Detection

The platform shall identify technically duplicated URLs caused by:

* query parameters;
* trailing slashes;
* capitalization;
* URL encoding;
* HTTP/HTTPS;
* www/non-www;
* session identifiers;
* tracking parameters.

---

## UR-018 — URL Structure Analysis

The system shall evaluate:

* URL readability;
* hierarchy;
* excessive depth;
* parameter usage;
* duplicate paths;
* invalid characters;
* inconsistent structures.

AI shall recommend structural improvements.

---

## UR-019 — Internal Link Analysis

The platform shall analyze:

* internal links;
* orphan pages;
* dead-end pages;
* excessive click depth;
* broken internal links;
* weakly linked pages;
* important pages with insufficient internal links.

---

## UR-020 — Orphan Page Detection

The system shall identify pages that:

* exist in sitemap;
* are externally accessible;
* but have insufficient or no internal links.

---

## UR-021 — Crawl Depth Analysis

The system shall calculate page depth.

Example:

```text
Homepage = Depth 0
Category = Depth 1
Product = Depth 2
Article = Depth 3
```

The system shall identify commercially important pages buried too deeply.

---

## UR-022 — Page Performance Analysis

The system shall analyze performance signals such as:

* loading performance;
* response time;
* rendering performance;
* resource size;
* image optimization;
* script overhead;
* CSS overhead;
* caching behavior;
* Core Web Vitals where measurable.

---

## UR-023 — Core Web Vitals

Where supported, the platform shall monitor:

* LCP;
* INP;
* CLS.

The system shall distinguish:

```text
Good
Needs Improvement
Poor
```

and recommend remediation.

---

## UR-024 — PageSpeed Intelligence

The system shall identify performance bottlenecks such as:

* render-blocking resources;
* large images;
* unused JavaScript;
* unused CSS;
* excessive third-party scripts;
* poor caching;
* slow server response;
* oversized resources.

---

## UR-025 — Mobile SEO

The system shall analyze:

* responsive behavior;
* viewport configuration;
* mobile rendering;
* mobile usability;
* mobile performance;
* content parity;
* hidden content;
* navigation usability.

---

## UR-026 — JavaScript SEO

The system shall analyze JavaScript-heavy websites.

It shall evaluate:

```text
Server HTML
↓
Client-rendered HTML
↓
Rendered DOM
↓
Search-accessible Content
```

The platform shall detect content that may depend excessively on client-side execution.

---

## UR-027 — JavaScript Rendering

The crawler shall support headless-browser rendering where required.

Potential technology:

```text
Chromium
Playwright
Puppeteer
```

The implementation shall be configurable.

---

## UR-028 — Rendered vs Raw HTML Comparison

The system shall compare:

```text
Raw HTML
vs
Rendered DOM
```

and detect:

* missing content;
* missing links;
* missing metadata;
* altered canonical tags;
* dynamically generated directives.

---

## UR-029 — Metadata Analysis

The system shall inspect:

* title tags;
* meta descriptions;
* robots meta;
* viewport;
* language metadata;
* duplicate metadata;
* missing metadata;
* excessively long metadata;
* empty metadata.

---

## UR-030 — Heading Structure

The system shall analyze:

* H1 presence;
* duplicate H1;
* heading hierarchy;
* empty headings;
* skipped hierarchy;
* excessive heading structures.

The platform shall distinguish technical anomalies from contextually valid structures.

---

## UR-031 — Structured Data

The platform shall detect supported structured-data implementations.

It shall validate:

* syntax;
* required properties;
* recommended properties;
* consistency;
* duplication;
* malformed structured data.

---

## UR-032 — Schema Intelligence

AI shall recommend appropriate structured-data opportunities based on:

* page type;
* business type;
* content;
* entities;
* product information.

---

## UR-033 — International SEO

The system shall analyze:

* hreflang;
* language declarations;
* regional variants;
* duplicate international pages;
* incorrect language targeting;
* hreflang conflicts;
* missing return links.

---

## UR-034 — Hreflang Validation

The system shall validate:

```text
Language
Region
Target URL
Return Links
Canonical Relationship
```

---

## UR-035 — HTTPS Analysis

The system shall identify:

* HTTP pages;
* mixed content;
* invalid TLS;
* certificate problems;
* insecure resource loading;
* HTTP/HTTPS duplication.

---

## UR-036 — Security-SEO Intersection

The system shall detect technical conditions that may negatively affect SEO and user trust, including:

* insecure HTTP;
* malicious redirects where detectable;
* compromised pages;
* injected spam patterns;
* suspicious URL structures;
* unsafe third-party resources.

Security incidents shall be escalated to the security subsystem.

---

## UR-037 — Server Analysis

The system shall analyze server-level signals where authorized.

Potential signals:

* TTFB;
* response codes;
* availability;
* timeout rate;
* server errors;
* DNS failures.

---

## UR-038 — CDN Analysis

Where detectable, the platform may identify:

* CDN usage;
* caching behavior;
* static asset delivery;
* geographic performance.

---

## UR-039 — Image SEO

The system shall identify:

* oversized images;
* missing alt attributes;
* inappropriate formats;
* poor compression;
* lazy-loading opportunities;
* responsive image issues.

---

## UR-040 — Video SEO

Where applicable, the system shall analyze:

* video metadata;
* video discoverability;
* structured data;
* thumbnails;
* embedded video accessibility.

---

## UR-041 — Faceted Navigation

For ecommerce websites, the platform shall detect potentially problematic:

* filters;
* parameters;
* faceted URLs;
* duplicate combinations;
* crawl traps.

---

## UR-042 — Ecommerce Technical SEO

The system shall analyze:

* product URLs;
* category hierarchy;
* pagination;
* variants;
* canonicalization;
* inventory states;
* structured data;
* product discoverability.

---

## UR-043 — CMS Detection

The platform may identify technologies such as:

```text
WordPress
Shopify
WooCommerce
Magento
Drupal
Next.js
React
Astro
Vue
Custom
```

Recommendations shall be adapted to the detected technology.

---

## UR-044 — Technology-Aware Recommendations

The AI shall generate recommendations appropriate for the customer's technology stack.

Example:

```text
Issue:
Large client-side JavaScript bundle

Technology:
Next.js

Recommendation:
Evaluate server-side rendering/static generation,
code splitting and route-level bundle reduction.
```

---

## UR-045 — Competitor Technical Benchmarking

Users shall be able to compare technical SEO health against competitors.

Comparison areas:

```text
Performance
Architecture
Indexability
Structured Data
Internal Links
Mobile
Page Experience
```

---

## UR-046 — Technical SEO Gap Analysis

The system shall identify where competitors have stronger technical implementation.

---

## UR-047 — Automated Root-Cause Analysis

AI shall attempt to identify root causes.

Example:

```text
Observed:
Large number of pages not indexed.

Possible cause:
Canonical points to unrelated URLs.

Confidence:
91%

Recommended action:
Review canonical generation logic.
```

---

## UR-048 — AI Technical SEO Recommendations

Every issue shall receive:

```text
Issue
Severity
Business Impact
Root Cause
Evidence
Recommendation
Implementation Steps
Expected Outcome
Risk
Confidence
```

---

## UR-049 — AI Remediation

AI may generate remediation proposals.

Examples:

* robots.txt modification;
* sitemap correction;
* metadata changes;
* canonical fixes;
* redirect mappings;
* structured-data changes;
* internal-link recommendations;
* configuration suggestions.

---

## UR-050 — Human Approval

Production-impacting changes shall support mandatory human approval.

---

## UR-051 — Safe Automated Remediation

AI automation shall support:

```text
Preview
Diff
Validation
Approval
Backup
Deployment
Post-deployment Verification
Rollback
```

---

## UR-052 — Human-Only Mode

Organizations shall be able to disable AI automation.

---

## UR-053 — AI-Assisted Mode

AI shall generate recommendations while humans execute changes.

---

## UR-054 — AI-Controlled Mode

Organizations may allow predefined low-risk changes to be automatically implemented.

Examples may include:

* metadata optimization;
* structured-data formatting;
* selected internal-link improvements.

High-risk changes should require approval.

---

## UR-055 — Issue Prioritization

Issues shall be prioritized using:

```text
Severity
×
Business Impact
×
Affected URLs
×
Likelihood of SEO Impact
×
Fix Confidence
```

---

## UR-056 — Technical Debt

The system shall maintain a Technical SEO Debt score.

---

## UR-057 — SEO Regression Detection

After deployment, the system shall compare:

```text
Before
vs
After
```

and detect regressions.

---

## UR-058 — Deployment Monitoring

The system shall detect significant technical SEO changes after:

* website deployment;
* CMS update;
* plugin update;
* infrastructure migration;
* domain migration.

---

## UR-059 — Website Migration Assistant

The platform shall support migration planning.

Example:

```text
Old URLs
   ↓
Redirect Mapping
   ↓
Canonical Validation
   ↓
Sitemap Update
   ↓
Internal Link Update
   ↓
Pre-Launch Crawl
   ↓
Launch
   ↓
Post-Launch Crawl
```

---

## UR-060 — Emergency SEO Monitoring

Users shall be able to configure high-priority monitoring for:

* sudden traffic loss;
* mass 404;
* indexing collapse;
* robots.txt changes;
* sitemap failure;
* widespread canonical changes.

---

## UR-061 — Notifications

Notifications shall support:

* dashboard;
* email;
* webhook;
* Slack/Teams where integrated;
* configurable alert channels.

---

## UR-062 — Reporting

The system shall generate:

* audit reports;
* executive reports;
* developer reports;
* SEO specialist reports;
* migration reports;
* performance reports.

---

## UR-063 — Excel Export

Users shall be able to export technical SEO data to Excel.

Sheets may include:

```text
Executive Summary
Technical Issues
Critical Issues
Crawlability
Indexability
Performance
Core Web Vitals
Redirects
Canonicals
Sitemaps
Robots
Internal Links
Structured Data
Mobile SEO
International SEO
JavaScript SEO
Recommendations
Tasks
```

---

## UR-064 — API Access

Authorized customers shall be able to consume technical SEO data through APIs.

---

## UR-065 — Collaboration

Users shall be able to:

* assign issues;
* comment;
* mention users;
* add notes;
* change status;
* attach evidence;
* approve fixes.

---

## UR-066 — Developer Handoff

SEO specialists shall be able to create developer-ready tickets.

Each ticket shall include:

```text
Problem
Affected URLs
Root Cause
Evidence
Recommended Fix
Implementation Notes
Priority
Acceptance Criteria
```

---

## UR-067 — AI Developer Assistance

AI shall translate SEO recommendations into technical implementation guidance.

The AI must clearly distinguish:

```text
Verified Fact
Recommendation
Suggested Code
Assumption
```

---

## UR-068 — Client-Friendly Explanation

Complex technical issues shall have a simplified business explanation.

Example:

```text
Technical Problem:
Redirect chain.

Business Explanation:
Visitors and search engines must pass through multiple
URLs before reaching the final page, creating unnecessary
latency and reducing crawl efficiency.
```

---

## UR-069 — Technical SEO Chat Assistant

Users shall be able to ask questions such as:

```text
Why did my SEO score decrease?

Which technical issue is most dangerous?

Why are my product pages not indexed?

Which pages are slow?

What should my developer fix first?
```

---

## UR-070 — AI + Human Support

Users shall be able to escalate technical SEO questions from AI to human specialists.

---

## 6. SYSTEM REQUIREMENTS

## SR-001 — Multi-Tenant Architecture

Every resource shall contain tenant context.

```text
tenant_id
organization_id
workspace_id
project_id
website_id
```

---

## SR-002 — Isolation

Cross-tenant access shall be cryptographically and logically prevented.

---

## SR-003 — Distributed Crawler

The crawler shall support horizontal scaling.

```text
Crawl Scheduler
      ↓
Queue
      ↓
Crawler Workers
      ↓
Rendering Workers
      ↓
Analysis Workers
```

---

## SR-004 — Crawl Queue

The crawler shall support:

* priority;
* retries;
* rate limits;
* robots policies;
* deduplication;
* cancellation.

---

## SR-005 — Crawl Politeness

The crawler shall respect:

* robots directives where applicable;
* configured rate limits;
* domain concurrency limits;
* customer authorization.

---

## SR-006 — Crawl Budget

Each tenant shall have configurable crawl quotas.

---

## SR-007 — Headless Rendering

JavaScript rendering shall be isolated from ordinary HTTP crawling.

This prevents expensive rendering workloads from exhausting crawler capacity.

---

## SR-008 — Browser Pool

Rendering workers should reuse controlled browser instances to improve efficiency.

---

## SR-009 — Resource Limits

Rendering jobs shall enforce:

* CPU limits;
* memory limits;
* timeout;
* maximum page resources;
* maximum script execution time.

---

## SR-010 — URL Canonicalization

The crawler shall normalize URLs consistently.

---

## SR-011 — Deduplication

The system shall prevent duplicate crawling of equivalent URLs.

---

## SR-012 — Crawl Storage

The system shall retain crawl information according to tenant retention policies.

---

## SR-013 — Historical Snapshots

Each audit shall create a versioned snapshot.

---

## SR-014 — Differential Analysis

The platform shall compare snapshots.

```text
Audit N
vs
Audit N+1
```

---

## SR-015 — Search Infrastructure

High-volume URL and issue searches shall use an optimized search/indexing system.

---

## SR-016 — Analytics Infrastructure

Large historical analytics queries should use an analytical datastore or warehouse.

---

## SR-017 — Event-Driven Processing

Events shall include:

```text
crawl.started
crawl.completed
crawl.failed
url.discovered
url.analyzed
seo.issue.detected
seo.issue.resolved
seo.regression.detected
seo.recommendation.created
seo.recommendation.approved
seo.fix.deployed
seo.fix.rolled_back
```

---

## SR-018 — Idempotency

Crawl and remediation jobs shall be idempotent.

---

## SR-019 — Retry System

Transient failures shall support exponential backoff.

---

## SR-020 — Dead Letter Queue

Repeatedly failed jobs shall enter a DLQ for investigation.

---

## SR-021 — AI Provider Abstraction

The system shall support multiple AI providers.

Potential providers include:

```text
Groq
Google Gemini
Mistral
Other approved providers
Self-hosted/open-source models
```

The application must not depend directly on one provider.

---

## SR-022 — AI Routing

The AI gateway shall select models according to:

* task;
* latency;
* cost;
* context size;
* provider availability;
* quality requirements.

---

## SR-023 — AI Failover

Provider failure shall trigger fallback routing.

---

## SR-024 — AI Cost Controls

AI usage shall be tracked per:

```text
Tenant
Organization
Workspace
User
Agent
Task
Provider
Model
```

---

## SR-025 — Deterministic SEO Rules

Critical technical checks shall use deterministic validation rather than relying exclusively on LLM interpretation.

Examples:

```text
HTTP status
Canonical existence
robots syntax
sitemap XML validity
redirect chains
URL duplication
hreflang reciprocity
```

---

## SR-026 — AI Reasoning Layer

LLMs shall be used primarily for:

* contextual interpretation;
* prioritization;
* explanation;
* root-cause hypotheses;
* strategy generation.

---

## SR-027 — Evidence Grounding

AI recommendations shall reference the underlying technical evidence.

---

## SR-028 — Confidence

AI recommendations shall have confidence indicators.

---

## SR-029 — Hallucination Prevention

The system shall validate generated recommendations against actual crawl data before presenting them as facts.

---

## SR-030 — Security

Security controls shall include:

```text
TLS
Encryption at Rest
RBAC
ABAC
MFA
Secret Management
API Authentication
Audit Logging
Rate Limiting
WAF
Network Segmentation
```

---

## SR-031 — Safe Remediation

Automated changes shall support:

```text
Versioning
Diff
Preview
Approval
Backup
Rollback
Verification
```

---

## SR-032 — Git Integration

Where appropriate, remediation may integrate with Git-based workflows.

Example:

```text
AI Fix
 ↓
Git Branch
 ↓
Pull Request
 ↓
Human Review
 ↓
CI Tests
 ↓
Merge
 ↓
Deployment
 ↓
SEO Verification
```

---

## SR-033 — CI/CD Integration

Technical SEO checks may execute during CI/CD.

Example:

```text
Code Commit
 ↓
Build
 ↓
Technical SEO Tests
 ↓
Pass / Fail
 ↓
Deployment
```

---

## SR-034 — API Gateway

All external APIs shall pass through centralized gateway controls.

---

## SR-035 — Rate Limiting

Rate limits shall exist for:

* crawling;
* API;
* AI;
* exports;
* remediation;
* integrations.

---

## SR-036 — Observability

Required telemetry:

```text
Logs
Metrics
Traces
Crawler Health
Rendering Health
AI Health
Queue Health
Database Health
Integration Health
```

---

## SR-037 — SLA Monitoring

The platform shall track service-level objectives for critical components.

---

## SR-038 — Availability

Production services should target at least 99.9% availability, subject to final infrastructure architecture.

---

## SR-039 — Disaster Recovery

The platform shall maintain:

* backups;
* recovery procedures;
* restore testing;
* service recovery procedures.

---

## SR-040 — Data Retention

Tenants shall be able to configure retention where permitted by product policy.

---

## 7. FUNCTIONAL REQUIREMENTS

## FR-001 — Technical SEO Dashboard

The dashboard shall show:

```text
Overall SEO Health
Critical Issues
High Issues
Resolved Issues
New Issues
SEO Regressions
Crawl Status
Indexability
Performance
Core Web Vitals
```

---

## FR-002 — Health Score Visualization

Example:

```text
Technical SEO Health
        87 / 100

Crawlability      92
Indexability      81
Performance       84
Mobile            94
Architecture      89
Structured Data   76
Internal Links    91
```

---

## FR-003 — Issue Explorer

Users shall be able to filter issues by:

```text
Severity
Category
URL
Page Type
Business Impact
Status
Assignee
Detected Date
```

---

## FR-004 — Issue Lifecycle

Each issue shall have:

```text
Detected
Investigating
Planned
In Progress
Pending Review
Resolved
Reopened
Ignored
```

---

## FR-005 — Issue Detail

Each issue shall display:

```text
Issue
Description
Affected URLs
Evidence
Severity
Business Impact
Root Cause
Recommendation
AI Confidence
Assigned User
Status
History
```

---

## FR-006 — Crawl Visualization

Users shall be able to visualize website architecture.

Example:

```text
Homepage
 ├── Product
 │    ├── Product A
 │    └── Product B
 ├── Services
 ├── Blog
 └── Documentation
```

---

## FR-007 — Orphan Page Report

The system shall provide a dedicated orphan-page report.

---

## FR-008 — Broken Link Report

The system shall list:

```text
Source URL
Broken URL
Status Code
Anchor Text
Link Type
Priority
```

---

## FR-009 — Redirect Report

The report shall display:

```text
Source
Destination
Status
Chain Length
Loop
Recommendation
```

---

## FR-010 — Canonical Report

The system shall display:

```text
URL
Canonical
Self Canonical
Canonical Status
Conflict
Recommendation
```

---

## FR-011 — Robots Report

The system shall show:

```text
Rule
Path
Allow/Disallow
Affected URLs
Risk
Recommendation
```

---

## FR-012 — Sitemap Report

The system shall show:

```text
Sitemap
URLs
Valid URLs
Invalid URLs
Indexable URLs
Canonical URLs
Missing URLs
```

---

## FR-013 — Performance Report

The platform shall display:

```text
LCP
INP
CLS
TTFB
Page Size
Request Count
JS Size
CSS Size
Image Size
```

where the corresponding measurements are available.

---

## FR-014 — Mobile Report

The platform shall identify mobile-specific technical problems.

---

## FR-015 — JavaScript SEO Report

The system shall show differences between:

```text
HTML Response
Rendered DOM
```

---

## FR-016 — Structured Data Report

The platform shall identify:

```text
Valid
Invalid
Missing
Incomplete
Conflicting
```

structured-data implementations.

---

## FR-017 — International SEO Report

The platform shall visualize:

```text
Language
Region
URL
hreflang
Canonical
Return Link
Status
```

---

## FR-018 — Competitor Technical Report

The system shall compare technical health against selected competitors.

---

## FR-019 — Recommendation Center

The system shall maintain a prioritized recommendation queue.

Example:

```text
P0 — Fix robots.txt blocking product pages
P0 — Resolve mass 500 errors
P1 — Remove redirect chains
P1 — Fix canonical conflicts
P2 — Optimize large images
P2 — Improve internal linking
```

---

## FR-020 — AI Explanation

The system shall allow:

> "Explain this issue."

AI shall respond with a concise technical and business explanation.

---

## FR-021 — AI Fix Proposal

The system shall allow:

> "How should I fix this?"

AI shall produce implementation guidance based on available evidence.

---

## FR-022 — AI Code Proposal

Where appropriate, AI may produce implementation examples.

Generated code shall be labeled as:

```text
AI Generated
Requires Review
```

---

## FR-023 — Human Approval Queue

Human experts shall have a dedicated approval queue.

---

## FR-024 — Remediation Diff

Before applying changes, the user shall see:

```text
Before
After
Affected Resources
Potential Impact
Rollback Plan
```

---

## FR-025 — Automated Validation

After a fix, the system shall rerun relevant technical checks.

---

## FR-026 — Regression Detection

If a fix introduces new problems:

```text
Detect
 ↓
Alert
 ↓
Block Further Automation
 ↓
Recommend Rollback
```

---

## FR-027 — Migration Mode

The platform shall provide a dedicated migration workflow for:

* domain changes;
* HTTP → HTTPS;
* CMS migration;
* URL restructuring;
* site redesign.

---

## FR-028 — Pre-Deployment Audit

Users shall be able to crawl staging environments where authorized.

---

## FR-029 — Production Comparison

The system shall compare:

```text
Staging
vs
Production
```

for technical SEO signals.

---

## FR-030 — SEO CI Checks

The platform shall allow configurable pass/fail rules.

Example:

```text
Fail deployment if:
Critical SEO issues > 0
```

---

## FR-031 — Alert Rules

Users shall define rules such as:

```text
Alert when:
500 errors > 1%
Organic indexable URLs decrease > 10%
Core Web Vital failure increases > 15%
Robots.txt changes
Sitemap becomes unavailable
```

---

## FR-032 — Report Scheduling

Users shall schedule reports.

---

## FR-033 — Executive Reports

Executive reports shall focus on:

```text
Business Risk
Traffic Risk
Revenue Risk
SEO Health
Priority Actions
```

rather than excessive technical detail.

---

## FR-034 — Developer Reports

Developer reports shall focus on:

```text
Affected URLs
Technical Evidence
Root Cause
Implementation
Acceptance Criteria
```

---

## FR-035 — SEO Specialist Reports

SEO reports shall include:

```text
Issue Distribution
Priority
Keyword Impact
Crawl Impact
Indexation Impact
Recommendations
```

---

## FR-036 — Excel Generation

Large exports shall execute asynchronously.

---

## FR-037 — CSV Export

Users may export issue and URL data as CSV.

---

## FR-038 — API Webhooks

The system shall send webhooks for critical events.

---

## FR-039 — Integration with Search Console

Where authorized, the platform shall combine technical crawl data with search performance data.

---

## FR-040 — Integration with Analytics

Technical issues shall be correlated with:

* sessions;
* conversions;
* revenue;
* engagement.

---

## FR-041 — Integration with CRM

Technical SEO performance may be correlated with:

```text
Organic Lead
→ CRM Opportunity
→ Customer
→ Revenue
```

---

## FR-042 — Integration with SalesGenie Keyword Intelligence

Technical SEO shall consume keyword priorities to determine which technical issues affect the most valuable search opportunities.

---

## FR-043 — Integration with Marketing Platform

Technical SEO shall identify landing pages that support campaigns.

---

## FR-044 — Integration with AI Digital Marketing

Technical SEO shall provide optimization signals to AI-generated campaigns.

---

## FR-045 — Integration with Lead Generation

Pages associated with high-value lead-generation keywords shall receive higher remediation priority where justified.

---

## 8. AI DECISION ENGINE

The AI decision system shall combine:

```text
Technical Severity
+
Affected URLs
+
Search Visibility
+
Keyword Value
+
Traffic
+
Conversions
+
Revenue
+
Business Priority
+
Fix Confidence
```

to determine remediation priority.

---

## 9. TECHNICAL SEO PRIORITY MODEL

Example:

```text
Priority Score =
Technical Severity
×
Business Impact
×
Search Visibility
×
Affected URL Weight
×
Revenue Exposure
×
Confidence
```

The production implementation shall be configurable.

---

## 10. AI/HUMAN DECISION MATRIX

| Action                    | AI Suggest | AI Execute | Human Approval |
| ------------------------- | ---------: | ---------: | -------------: |
| Identify issue            |        Yes |        Yes |             No |
| Explain issue             |        Yes |        Yes |             No |
| Generate report           |        Yes |        Yes |             No |
| Metadata recommendation   |        Yes |   Optional |   Configurable |
| robots.txt change         |        Yes | Restricted |            Yes |
| Canonical change          |        Yes | Restricted |            Yes |
| Redirect change           |        Yes | Restricted |            Yes |
| Sitemap change            |        Yes |   Optional |   Configurable |
| Large URL migration       |        Yes |         No |            Yes |
| Infrastructure change     |        Yes |         No |            Yes |
| Security-sensitive change |        Yes |         No |            Yes |
| SEO strategy              |        Yes |         No |            Yes |

---

## 11. AUTOMATED REMEDIATION SAFETY

No high-risk change shall be directly applied without authorization.

The safe workflow is:

```text
AI Proposal
 ↓
Impact Analysis
 ↓
Diff
 ↓
Validation
 ↓
Human Approval
 ↓
Backup
 ↓
Deployment
 ↓
Post-Deployment Crawl
 ↓
Verification
 ↓
Rollback if Required
```

---

## 12. TECHNICAL SEO KNOWLEDGE GRAPH

The system may maintain relationships such as:

```text
Website
 ↓
Page
 ↓
URL
 ↓
Keyword
 ↓
Search Intent
 ↓
Traffic
 ↓
Lead
 ↓
Customer
 ↓
Revenue
```

and:

```text
Page
 ↓
Technical Issue
 ↓
Root Cause
 ↓
Recommendation
 ↓
Fix
 ↓
Outcome
```

This enables SalesGenie to move from isolated SEO auditing to contextual business intelligence.

---

## 13. BUSINESS IMPACT MODEL

The system shall distinguish between:

### Technical Severity

How technically serious is the issue?

### Search Impact

How likely is it to affect search visibility?

### Business Impact

How likely is it to affect:

* leads;
* sales;
* conversions;
* revenue?

Example:

```text
Issue:
Canonical conflict

Affected URLs:
25,000

Affected pages:
High-value product pages

Technical Severity:
High

Business Impact:
Critical

Priority:
P0
```

---

## 14. PERFORMANCE REQUIREMENTS

The system shall target:

```text
Dashboard queries:
Low-latency interactive response

Small audits:
Near-real-time status updates

Large audits:
Asynchronous execution

Large crawls:
Horizontally scalable workers
```

Exact SLAs shall be established during implementation based on infrastructure capacity.

---

## 15. BILLING AND USAGE

Technical SEO usage shall be metered by configurable dimensions.

Examples:

```text
Tracked Websites
Crawl URLs
Rendering Jobs
Audit Frequency
Historical Data
AI Analyses
Automated Remediation
API Calls
Exports
```

Usage shall be associated with tenant billing.

---

## 16. SUBSCRIPTION ENTITLEMENTS

Example:

```text
FREE
- Limited website
- Limited crawl
- Basic audit
- Limited reports

MONTHLY
- More websites
- Advanced crawling
- AI analysis
- Monitoring
- Competitor benchmarking

YEARLY
- Higher quotas
- Advanced automation
- Extended historical data
- Advanced integrations

ENTERPRISE
- Custom quotas
- API
- Advanced security
- SSO
- Dedicated infrastructure options
- Custom retention
- Human SEO support
```

Exact limits must remain configurable.

---

## 17. SECURITY AND COMPLIANCE

The platform shall implement:

```text
Zero Trust
Least Privilege
Tenant Isolation
Encryption
MFA
RBAC
ABAC
Audit Logging
Secrets Management
Secure APIs
Rate Limiting
Threat Monitoring
```

Sensitive customer credentials shall never be stored in plaintext.

---

## 18. DATA MODEL

Core entities may include:

```text
Website
Project
Crawl
CrawlURL
URLSnapshot
SEOIssue
SEORecommendation
SEOFix
Redirect
Canonical
Sitemap
RobotsRule
StructuredData
PagePerformance
InternalLink
Keyword
Competitor
Audit
AuditSnapshot
Task
Assignment
Approval
Deployment
Alert
```

---

## 19. AUDIT TRAIL

Every important action shall record:

```text
Actor
Actor Type
Timestamp
Tenant
Organization
Workspace
Resource
Action
Previous State
New State
IP / Device Context where appropriate
Result
```

AI-generated actions shall be explicitly identified.

---

## 20. OBSERVABILITY

Required metrics include:

```text
crawl_jobs_total
crawl_jobs_failed
crawl_latency
crawl_urls_total
render_jobs_total
render_failures
seo_issues_detected
seo_issues_resolved
seo_regressions
ai_recommendations
ai_acceptance_rate
ai_override_rate
ai_cost
remediation_success_rate
rollback_rate
```

---

## 21. END-TO-END ARCHITECTURE

```text
                         CLIENT
                           │
                           ▼
                  ┌─────────────────┐
                  │ SalesGenie UI   │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ API Gateway     │
                  └────────┬────────┘
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
   Crawl Service     SEO Service      AI Gateway
          │                │                │
          ▼                ▼                ▼
   Crawl Queue       Rule Engine      AI Providers
          │                │
          ▼                ▼
   Crawl Workers     Analysis Engine
          │                │
          └────────┬───────┘
                   ▼
             Event Bus
                   │
      ┌────────────┼─────────────┐
      ▼            ▼             ▼
 Analytics      Alerting       Reports
      │            │             │
      └────────────┼─────────────┘
                   ▼
              Data Layer
                   │
                   ▼
          Business Intelligence
                   │
                   ▼
             Human Review
                   │
                   ▼
             Remediation
                   │
                   ▼
             Verification
```

---

## 22. EVENT MODEL

Example event:

```json
{
  "event_type": "seo.issue.detected",
  "event_id": "uuid",
  "tenant_id": "uuid",
  "organization_id": "uuid",
  "workspace_id": "uuid",
  "website_id": "uuid",
  "crawl_id": "uuid",
  "issue_id": "uuid",
  "severity": "critical",
  "business_impact": "high",
  "timestamp": "ISO-8601"
}
```

---

## 23. HUMAN + AI SUPPORT MODEL

The platform shall provide three primary operating modes:

```text
AI-FIRST
```

AI performs analysis and recommendations.

```text
AI-ASSISTED
```

AI performs analysis while humans make decisions.

```text
HUMAN-FIRST
```

Human specialists control the process while AI provides assistance.

Organizations may configure different modes by:

* workspace;
* project;
* action;
* risk level.

---

## 24. ESCALATION ENGINE

AI shall escalate to humans when:

```text
Confidence is low
OR
Data conflicts
OR
Business impact is high
OR
SEO migration is involved
OR
Security risk exists
OR
Infrastructure changes are required
OR
Potential traffic loss is significant
OR
Customer explicitly requests human support
```

---

## 25. SUCCESS METRICS

## Technical Metrics

```text
Crawl Success Rate
Issue Detection Accuracy
False Positive Rate
False Negative Rate
Audit Completion Time
```

## SEO Metrics

```text
Indexability Improvement
Crawl Efficiency
Ranking Improvement
Organic Traffic Improvement
Core Web Vital Improvement
```

## Business Metrics

```text
Organic Leads
Organic Conversions
Revenue
Revenue per Organic Visit
SEO ROI
```

## AI Metrics

```text
Recommendation Accuracy
Human Acceptance Rate
Human Override Rate
AI Cost
AI Latency
Escalation Rate
```

---

## 26. QUALITY GATES

Production readiness requires:

* [ ] Crawl accuracy validated.
* [ ] URL deduplication validated.
* [ ] robots.txt parser validated.
* [ ] sitemap parser validated.
* [ ] redirect detection validated.
* [ ] canonical detection validated.
* [ ] indexability checks validated.
* [ ] JavaScript rendering tested.
* [ ] Core Web Vitals integration tested.
* [ ] structured-data validation tested.
* [ ] hreflang validation tested.
* [ ] mobile testing validated.
* [ ] large-site crawling tested.
* [ ] AI recommendations evaluated.
* [ ] false-positive rates measured.
* [ ] human approval workflow tested.
* [ ] rollback tested.
* [ ] tenant isolation tested.
* [ ] authorization tested.
* [ ] audit logging tested.
* [ ] rate limiting tested.
* [ ] disaster recovery tested.
* [ ] load testing completed.
* [ ] security testing completed.

---

## 27. ACCEPTANCE CRITERIA

The Technical SEO module is production-ready when:

* [ ] Customers can add and verify websites.
* [ ] Customers can configure crawls.
* [ ] The crawler can discover URLs.
* [ ] Robots rules are evaluated.
* [ ] Sitemaps are analyzed.
* [ ] HTTP statuses are analyzed.
* [ ] Redirect chains are detected.
* [ ] Canonical conflicts are detected.
* [ ] Duplicate URLs are detected.
* [ ] Orphan pages are detected.
* [ ] Internal links are analyzed.
* [ ] Crawl depth is calculated.
* [ ] JavaScript rendering is supported.
* [ ] Raw HTML and rendered DOM can be compared.
* [ ] Metadata is analyzed.
* [ ] Structured data is analyzed.
* [ ] International SEO is analyzed.
* [ ] Mobile SEO is analyzed.
* [ ] Performance signals are analyzed.
* [ ] Core Web Vitals are supported where data is available.
* [ ] Technical SEO issues are prioritized.
* [ ] Business impact is calculated.
* [ ] Competitor technical benchmarking works.
* [ ] AI root-cause analysis works.
* [ ] AI recommendations are evidence-grounded.
* [ ] Human review works.
* [ ] AI automation can be restricted.
* [ ] High-risk changes require human approval.
* [ ] Remediation supports rollback.
* [ ] Post-fix verification works.
* [ ] SEO regressions are detected.
* [ ] Alerts work.
* [ ] Excel reports work.
* [ ] Executive reports work.
* [ ] Developer reports work.
* [ ] APIs work.
* [ ] Webhooks work.
* [ ] Search/analytics integrations work where configured.
* [ ] Billing limits are enforced.
* [ ] Tenant isolation is verified.
* [ ] Audit logs are immutable or tamper-evident.
* [ ] AI provider failover works.
* [ ] Observability is implemented.
* [ ] Disaster recovery is tested.

---

## 28. FINAL SALES­GENIE TECHNICAL SEO INTELLIGENCE LOOP

```text
                  WEBSITE
                     │
                     ▼
             TECHNICAL CRAWLER
                     │
                     ▼
              RAW SEO SIGNALS
                     │
        ┌────────────┼─────────────┐
        ▼            ▼             ▼
   Crawlability  Indexability  Performance
        │            │             │
        └────────────┼─────────────┘
                     ▼
             TECHNICAL ANALYSIS
                     │
                     ▼
              ISSUE DETECTION
                     │
                     ▼
             ROOT-CAUSE ANALYSIS
                     │
                     ▼
          BUSINESS IMPACT ANALYSIS
                     │
                     ▼
             PRIORITY ENGINE
                     │
                     ▼
              AI RECOMMENDATION
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
    LOW-RISK ACTION        HIGH-RISK ACTION
          │                     │
          ▼                     ▼
   AI AUTOMATION           HUMAN REVIEW
          │                     │
          └──────────┬──────────┘
                     ▼
                 REMEDIATION
                     │
                     ▼
             POST-FIX CRAWL
                     │
                     ▼
              VALIDATION
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
       SUCCESS               REGRESSION
          │                     │
          ▼                     ▼
     PERFORMANCE             ROLLBACK
       MONITORING                │
          │                      │
          └──────────┬───────────┘
                     ▼
              BUSINESS OUTCOME
                     │
                     ▼
              AI LEARNING LOOP
                     │
                     ▼
             NEXT BEST ACTION
```

---

## 29. STRATEGIC OUTCOME

SalesGenie's Technical SEO platform shall evolve beyond conventional SEO auditing.

The intended system is:

```text
Technical SEO Audit
        +
AI Diagnosis
        +
Business Impact Analysis
        +
Competitor Intelligence
        +
Keyword Intelligence
        +
Revenue Intelligence
        +
Human SEO Expertise
        +
Safe Automation
        +
Continuous Monitoring
```

The final objective is:

> **Detect technical problems before they become business problems, identify their root causes, recommend the highest-value remediation, safely execute approved changes, verify the outcome, and continuously optimize the website through an AI + human closed-loop system.**

This makes Technical SEO a foundational intelligence layer connecting **website infrastructure → search visibility → qualified traffic → leads → sales → revenue → business growth** inside SalesGenie.
