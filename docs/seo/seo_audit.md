# SEO Audit Engine — User Requirements, System Requirements & Functional Requirements

**Document:** `seo_audit.md`  
**Platform:** SalesGenie — Enterprise AI Sales, Marketing & Growth Intelligence Platform  
**Capability:** AI-Based SEO Audit Engine  
**Execution Model:** AI-Based  
**Requirement Standard:** FAANG-Level / Enterprise-Grade  
**Version:** 1.0  
**Status:** Production Specification

---

## 1. Purpose

The `seo_audit` module shall provide an AI-powered, enterprise-grade SEO auditing system capable of automatically discovering, crawling, analyzing, diagnosing, prioritizing, explaining, and recommending fixes for SEO issues across websites, web applications, landing pages, content systems, and digital properties.

The engine shall evaluate:

```text
Technical SEO
+
On-Page SEO
+
Content Quality
+
Keyword Optimization
+
Internal Linking
+
Crawlability
+
Indexability
+
Structured Data
+
Page Performance
+
Core Web Vitals
+
Mobile SEO
+
International SEO
+
Local SEO
+
Off-Page Signals
+
Competitor SEO
+
Search Intent
+
Content Gaps
+
AI Search Visibility
```

and transform the collected signals into:

```text
SEO AUDIT
+
ISSUE DETECTION
+
SEVERITY
+
BUSINESS IMPACT
+
ROOT CAUSE
+
EVIDENCE
+
RECOMMENDED FIX
+
AI-GENERATED EXPLANATION
+
PRIORITY
+
EFFORT ESTIMATION
+
EXPECTED IMPACT
+
VALIDATION
```

The system shall be AI-based and shall automatically analyze large quantities of SEO data while maintaining deterministic validation for technical SEO rules wherever possible.

---

## 2. Core Objective

The system shall answer:

```text
What is wrong with the website's SEO?

Why is it wrong?

How important is the issue?

What is causing the issue?

How should it be fixed?

Which issues should be fixed first?

What is the expected SEO impact?

Did the fix actually resolve the problem?
```

---

## 3. Primary Goals

The SEO Audit Engine shall:

* Detect SEO problems automatically.
* Discover technical SEO issues.
* Detect crawlability problems.
* Detect indexability problems.
* Analyze website architecture.
* Analyze metadata.
* Analyze headings.
* Analyze content quality.
* Analyze keyword targeting.
* Analyze search intent alignment.
* Analyze internal links.
* Analyze structured data.
* Analyze canonicalization.
* Analyze redirects.
* Analyze broken links.
* Analyze duplicate content.
* Analyze thin content.
* Analyze page performance.
* Analyze Core Web Vitals.
* Analyze mobile SEO.
* Analyze international SEO.
* Analyze local SEO.
* Analyze sitemap health.
* Analyze robots.txt.
* Analyze HTTPS/security-related SEO signals.
* Analyze image optimization.
* Analyze JavaScript rendering.
* Analyze competitor SEO signals.
* Identify content gaps.
* Identify ranking opportunities.
* Generate prioritized recommendations.
* Explain detected problems.
* Estimate implementation effort.
* Estimate expected impact.
* Validate fixes.
* Monitor SEO health over time.

---

## 4. Scope

## 4.1 In Scope

The system shall support:

* Website crawling.
* URL discovery.
* Sitemap analysis.
* Robots.txt analysis.
* Canonical analysis.
* Redirect analysis.
* HTTP status analysis.
* Metadata analysis.
* Heading analysis.
* Content analysis.
* Keyword analysis.
* Search-intent analysis.
* Internal-link analysis.
* External-link analysis.
* Image SEO analysis.
* Structured-data analysis.
* Schema.org validation.
* Mobile SEO analysis.
* Page-speed analysis.
* Core Web Vitals analysis.
* JavaScript rendering analysis.
* International SEO analysis.
* Local SEO analysis.
* Duplicate-content detection.
* Thin-content detection.
* Orphan-page detection.
* Crawl-depth analysis.
* Indexability analysis.
* Content freshness analysis.
* Competitor comparison.
* AI-powered diagnosis.
* AI-generated recommendations.
* Issue prioritization.
* SEO scoring.
* Fix validation.
* Historical comparison.
* Continuous monitoring.
* SEO alerts.
* Audit reporting.
* Executive reporting.
* Developer-oriented technical reports.
* Marketing-oriented SEO reports.

---

## 5. Out of Scope

The SEO Audit Engine shall not:

* Guarantee search-engine rankings.
* Guarantee traffic growth.
* Guarantee revenue.
* Automatically manipulate search-engine rankings.
* Perform black-hat SEO.
* Generate spam backlinks.
* Automatically create deceptive content.
* Automatically publish changes without authorization.
* Bypass website security controls.
* Crawl resources without respecting configured crawl policies.
* Expose private customer data.

---

## 6. SEO Audit Architecture

```text
                         SalesGenie
                             |
                       API Gateway
                             |
                     SEO Audit Service
                             |
        +--------------------+--------------------+
        |                    |                    |
     Crawler             Analyzer             AI Engine
        |                    |                    |
 URL Discovery        Technical SEO        Diagnosis
 Sitemap              On-Page SEO          Explanation
 Robots.txt           Content              Recommendations
 Rendering            Performance          Prioritization
        |                    |
        +--------------------+
                             |
                    SEO Intelligence Layer
                             |
        +--------------------+--------------------+
        |                    |                    |
 Keyword Intelligence  Competitor Analysis   SEO Analytics
        |                    |                    |
        +--------------------+--------------------+
                             |
                       Audit Engine
                             |
                    Issue Prioritization
                             |
                     Recommendation API
                             |
                        SalesGenie UI
```

---

## 7. User Roles

The SEO Audit Engine shall primarily serve:

## 7.1 SEO Manager

The SEO Manager shall be able to:

* Create audits.
* Configure crawl policies.
* View SEO health.
* Review issues.
* Prioritize issues.
* Review AI recommendations.
* Compare audits.
* Monitor improvements.
* Generate reports.

---

## 7.2 SEO Specialist

The SEO Specialist shall be able to:

* Inspect individual URLs.
* Inspect technical issues.
* Review keyword optimization.
* Review content recommendations.
* Inspect internal links.
* Review schema issues.
* Validate fixes.

---

## 7.3 Marketing Manager

The Marketing Manager shall be able to:

* View SEO health.
* View high-impact SEO issues.
* View expected marketing impact.
* Review content opportunities.
* Generate executive reports.

---

## 7.4 Product Manager

The Product Manager shall be able to:

* View product-level SEO health.
* Identify SEO-related product issues.
* Track SEO technical debt.
* Prioritize SEO improvements.

---

## 7.5 Developer

The Developer shall be able to:

* View technical SEO issues.
* Inspect affected URLs.
* View diagnostic evidence.
* View implementation recommendations.
* Validate technical fixes.

---

## 7.6 Business Analyst

The Business Analyst shall be able to:

* Analyze SEO performance.
* Compare historical audits.
* Analyze issue trends.
* Measure expected versus actual impact.

---

## 8. User Requirements

## UR-001 — Website Registration

The system shall allow authorized users to register websites for SEO auditing.

Required information may include:

```text
Website Name
Domain
Primary URL
Business Type
Target Country
Target Language
Industry
Primary Audience
```

---

## UR-002 — Audit Creation

Users shall be able to create an SEO audit.

Audit configuration shall support:

```text
Domain
Start URL
Maximum URLs
Maximum Crawl Depth
Crawl Rate
User-Agent
JavaScript Rendering
Mobile Simulation
Sitemap
Robots.txt
Authentication Requirements
Audit Scope
```

---

## UR-003 — Full Website Audit

Users shall be able to request a complete website audit.

The system shall automatically:

```text
Discover URLs
Crawl URLs
Render Pages
Collect Signals
Analyze SEO
Detect Issues
Prioritize Issues
Generate Recommendations
```

---

## UR-004 — Partial Audit

Users shall be able to audit:

```text
Single URL
URL Group
Directory
Subdomain
Sitemap
Landing Pages
Product Pages
Blog
```

---

## UR-005 — Technical SEO Audit

The system shall identify technical SEO issues including:

```text
4xx Errors
5xx Errors
Redirect Chains
Redirect Loops
Broken Links
Canonical Errors
Duplicate Canonicals
Missing Canonicals
Noindex Issues
Robots Blocking
Sitemap Errors
HTTPS Problems
Crawl Depth
Orphan Pages
Pagination Problems
JavaScript Rendering Problems
```

---

## UR-006 — On-Page SEO Audit

The system shall analyze:

```text
Title
Meta Description
H1
H2-H6
Content
Keywords
Images
Alt Text
Internal Links
External Links
URL Structure
```

---

## UR-007 — Metadata Analysis

The AI shall detect:

* Missing title tags.
* Duplicate title tags.
* Overly long title tags.
* Extremely short titles.
* Weak titles.
* Missing meta descriptions.
* Duplicate meta descriptions.
* Poorly optimized descriptions.

---

## UR-008 — Content Audit

The system shall identify:

```text
Thin Content
Duplicate Content
Near-Duplicate Content
Low-Value Content
Keyword Stuffing
Missing Topic Coverage
Poor Search Intent Alignment
Outdated Content
Low Content Depth
```

---

## UR-009 — Keyword Audit

The system shall analyze:

```text
Primary Keyword
Secondary Keywords
Keyword Placement
Keyword Coverage
Search Intent
Keyword Cannibalization
Keyword-to-Page Mapping
```

---

## UR-010 — Search Intent Analysis

The AI shall classify intent as:

```text
Informational
Navigational
Commercial Investigation
Transactional
Local
Mixed
```

The system shall determine whether page content matches the dominant search intent.

---

## UR-011 — Internal Linking Audit

The system shall identify:

```text
Broken Internal Links
Orphan Pages
Weak Internal Linking
Excessive Internal Links
Deep Pages
Poor Anchor Text
Important Pages With Few Links
```

---

## UR-012 — External Link Audit

The system shall identify:

```text
Broken External Links
Suspicious External Links
Low-Quality References
Missing Relevant References
```

---

## UR-013 — Image SEO Audit

The system shall analyze:

```text
Missing Alt Text
Duplicate Alt Text
Poor Alt Text
Oversized Images
Unsupported Formats
Missing Dimensions
Lazy Loading
Image File Names
```

---

## UR-014 — Structured Data Audit

The system shall analyze:

```text
Schema.org
JSON-LD
Microdata
RDFa
```

and identify:

```text
Missing Schema
Invalid Schema
Incomplete Schema
Conflicting Schema
Incorrect Schema Type
```

---

## UR-015 — Sitemap Audit

The system shall analyze:

```text
XML Sitemap
Sitemap Index
URL Coverage
Invalid URLs
Non-Canonical URLs
Noindex URLs
Redirected URLs
Broken URLs
Last Modification Dates
```

---

## UR-016 — Robots.txt Audit

The system shall identify:

```text
Invalid Syntax
Blocked Important Resources
Overly Broad Disallow Rules
Conflicting Directives
Sitemap Declaration Problems
```

---

## UR-017 — Canonical Audit

The system shall detect:

```text
Missing Canonical
Self-Canonical Problems
Cross-Domain Canonical
Conflicting Canonical
Canonical to Redirect
Canonical to 404
Canonical to Noindex
```

---

## UR-018 — Indexability Audit

The system shall determine whether pages are:

```text
Indexable
Non-Indexable
Blocked
Canonicalized
Noindexed
Redirected
Unavailable
```

---

## UR-019 — Crawlability Audit

The system shall analyze:

```text
Crawl Depth
Internal Link Structure
Robots Rules
Response Codes
Crawl Budget Signals
Duplicate URLs
Parameter URLs
```

---

## UR-020 — URL Audit

The system shall analyze:

```text
URL Length
URL Structure
Parameters
Special Characters
Case Sensitivity
Duplicate URLs
Trailing Slash Consistency
```

---

## 9. Performance Requirements

## UR-021 — Page Performance

The system shall analyze:

```text
LCP
INP
CLS
TTFB
FCP
Page Size
JavaScript
CSS
Images
Third-Party Resources
```

---

## UR-022 — Core Web Vitals

The system shall classify Core Web Vitals according to current supported search-engine guidance.

The engine shall store the measurement timestamp and methodology for every metric.

---

## UR-023 — Mobile SEO

The system shall evaluate:

```text
Mobile Rendering
Responsive Design
Viewport Configuration
Mobile Content Parity
Touch Targets
Mobile Performance
```

---

## 10. International SEO

The system shall audit:

```text
hreflang
Language Targeting
Country Targeting
Duplicate Localized Pages
Canonical Relationships
Language/Region Conflicts
```

---

## 11. Local SEO

Where applicable, the system shall analyze:

```text
Business Information
Location Pages
Local Keywords
NAP Consistency
Local Structured Data
Local Landing Pages
```

---

## 12. AI-Based SEO Diagnosis

The AI shall convert raw technical findings into business-oriented diagnoses.

Example:

```text
Issue:
Important product pages have excessive crawl depth.

AI Diagnosis:
The website architecture requires search-engine crawlers
to traverse too many links before reaching commercially
important pages.

Business Impact:
Potentially reduced discovery and weaker internal authority
distribution.

Priority:
HIGH
```

---

## 13. AI Root-Cause Analysis

The AI shall determine:

```text
Observed Problem
Root Cause
Affected Pages
Dependency
Business Impact
Recommended Resolution
```

---

## 14. AI Recommendation Generation

For every significant issue, the AI shall generate:

```text
Problem
Why It Matters
Recommended Fix
Implementation Guidance
Expected Impact
Estimated Effort
Priority
Confidence
```

---

## 15. Issue Severity

Issues shall be classified:

```text
CRITICAL
HIGH
MEDIUM
LOW
INFO
```

Example:

```text
CRITICAL:
Major indexability failure.

HIGH:
Large number of important pages blocked.

MEDIUM:
Duplicate metadata across many pages.

LOW:
Minor image optimization opportunity.

INFO:
Potential improvement with uncertain impact.
```

---

## 16. Issue Priority

Priority shall consider:

```text
SEO Impact
Business Impact
Number of URLs
Traffic Potential
Revenue Potential
Implementation Effort
Confidence
Urgency
```

---

## 17. SEO Issue Score

The platform shall calculate:

```text
Issue Score =
Impact
×
Affected Scope
×
Business Value
×
Confidence
÷
Implementation Effort
```

The exact scoring formula shall be configurable.

---

## 18. SEO Health Score

The system shall generate an overall SEO health score.

Example:

```text
SEO Health Score: 82/100

Technical SEO:      88
On-Page SEO:        79
Content:            84
Performance:        76
Internal Linking:   81
Structured Data:    72
Mobile SEO:         91
```

---

## 19. SEO Health Score Requirements

The score shall:

* Be reproducible.
* Store scoring methodology.
* Store audit timestamp.
* Support historical comparison.
* Support category-level scoring.
* Avoid representing the score as an official search-engine ranking factor.

---

## 20. Duplicate Content Detection

The system shall detect:

```text
Exact Duplicates
Near Duplicates
Template-Dominated Pages
Duplicate Titles
Duplicate Descriptions
Duplicate H1s
Duplicate Content Clusters
```

The AI shall determine whether duplication is likely intentional or problematic.

---

## 21. Keyword Cannibalization

The system shall identify pages competing for similar search intents.

Output:

```text
Keyword
Page A
Page B
Search Intent Similarity
Potential Cannibalization
Recommended Action
```

Recommended actions may include:

```text
Consolidate
Differentiate
Canonicalize
Redirect
Reposition
Expand
```

---

## 22. Content Gap Detection

The AI shall compare:

```text
Existing Content
Target Keywords
Search Intent
Competitor Content
Topic Coverage
Customer Questions
```

and identify content gaps.

---

## 23. Competitor SEO Audit

The system shall support competitor comparison across:

```text
Keyword Coverage
Content Coverage
Backlink Signals
Technical Health
Page Performance
Search Intent Coverage
Content Depth
Internal Linking
SERP Visibility
```

The system shall clearly distinguish observed data from AI inference.

---

## 24. AI Content Quality Evaluation

The AI shall assess:

```text
Relevance
Depth
Completeness
Clarity
Search Intent Alignment
Originality Signals
Topic Coverage
Entity Coverage
Content Freshness
```

The system shall not treat AI-generated content as inherently low quality or human-written content as inherently high quality; evaluation shall be evidence-based.

---

## 25. E-E-A-T-Oriented Analysis

Where relevant, the system shall assess observable signals associated with:

```text
Experience
Expertise
Authoritativeness
Trustworthiness
```

The engine shall not claim to directly measure Google's internal E-E-A-T score.

---

## 26. AI Search Optimization

The audit may analyze visibility opportunities for AI-powered search and answer systems.

It shall evaluate:

```text
Entity Clarity
Question Coverage
Structured Information
Content Extractability
Topical Authority
Citation-Worthy Information
```

---

## 27. JavaScript SEO Audit

The system shall support rendered-page analysis to detect:

```text
Client-Side Content Rendering
Missing Rendered Content
Rendering Errors
Blocked JavaScript
Incorrect Canonicals
Dynamic Metadata Problems
Dynamic Links
```

---

## 28. Crawl Architecture

The crawler shall support:

```text
URL Queue
Prioritization
Deduplication
Rate Limiting
Retry
Timeout
Redirect Handling
Canonical Handling
Robots Evaluation
Sitemap Discovery
Rendering Queue
```

---

## 29. Crawl Safety

The crawler shall:

* Respect configured crawl rate.
* Respect applicable robots directives according to platform policy.
* Prevent infinite crawl loops.
* Detect crawl traps.
* Limit URL explosion.
* Limit parameter combinations.
* Enforce maximum crawl depth.
* Enforce maximum URL count.
* Enforce request timeouts.

---

## 30. Crawl Budget Protection

The system shall prevent:

```text
Duplicate Parameter Crawls
Calendar Traps
Infinite Pagination
Session URL Explosion
Faceted Navigation Explosion
Redirect Loops
```

---

## 31. URL Discovery Sources

The crawler shall discover URLs through:

```text
Homepage
Internal Links
XML Sitemap
Sitemap Index
Canonical Tags
Structured Data
Configured URL Lists
```

---

## 32. HTTP Analysis

The system shall inspect:

```text
200
301
302
307
308
404
410
429
500
502
503
504
```

and other relevant HTTP status codes.

---

## 33. Redirect Audit

The system shall detect:

```text
Redirect Chains
Redirect Loops
Incorrect Redirect Targets
Temporary Redirect Misuse
Redirected Internal Links
Redirected Canonicals
```

---

## 34. Broken Link Detection

The system shall identify:

```text
Broken Internal Links
Broken External Links
Dead Pages
Soft 404 Signals
```

---

## 35. Soft 404 Detection

The AI and deterministic analyzers shall identify pages that return successful HTTP responses but appear to contain unavailable or empty content.

---

## 36. Orphan Page Detection

The system shall identify URLs present in:

```text
Sitemap
Database
Configured URL List
```

but not reachable through normal internal navigation.

---

## 37. Crawl Depth Analysis

The system shall calculate:

```text
Homepage → Page Distance
```

and identify strategically important pages with excessive crawl depth.

---

## 38. Internal Link Authority Analysis

The system shall calculate internal-link signals including:

```text
Inbound Links
Outbound Links
Anchor Text
Link Depth
Page Importance
Internal Link Distribution
```

---

## 39. Anchor Text Analysis

The system shall identify:

```text
Generic Anchor Text
Missing Anchor Text
Over-optimized Anchors
Repeated Anchors
Irrelevant Anchors
```

---

## 40. Metadata Quality Engine

The system shall evaluate:

```text
Title Length
Title Uniqueness
Title Relevance
Description Length
Description Uniqueness
Description Relevance
Keyword Alignment
Search Intent Alignment
```

---

## 41. Heading Structure Analysis

The system shall detect:

```text
Missing H1
Multiple H1
Duplicate H1
Heading Hierarchy Problems
Missing Subheadings
Keyword Misalignment
```

The engine shall distinguish semantic/structural concerns from outdated SEO myths and shall not automatically classify every multiple-H1 page as a critical SEO failure.

---

## 42. Image SEO Engine

The system shall analyze:

```text
Alt Text
Image Size
Format
Compression
Dimensions
Lazy Loading
Responsive Images
Image Filename
```

---

## 43. Structured Data Engine

The system shall:

* Extract structured data.
* Parse JSON-LD.
* Parse supported structured-data formats.
* Validate syntax.
* Validate required properties where applicable.
* Detect conflicts.
* Identify missing opportunities.

---

## 44. Page Experience Analysis

The system shall evaluate:

```text
Performance
Mobile Usability
HTTPS
Interstitial/UX Signals
Layout Stability
Interaction Responsiveness
```

---

## 45. SEO Audit Report

The system shall generate:

```text
Executive Summary
SEO Health Score
Critical Issues
High-Priority Issues
Medium Issues
Low Issues
Technical Findings
Content Findings
Keyword Findings
Performance Findings
Internal-Link Findings
Structured Data Findings
Competitor Findings
AI Recommendations
```

---

## 46. Executive Summary

The AI shall generate a concise summary:

```text
Overall SEO Health
Top 5 Problems
Top 5 Opportunities
Expected Impact
Recommended Next Actions
```

---

## 47. Developer Report

The system shall generate technical details including:

```text
URL
HTTP Status
HTML Element
Detected Problem
Evidence
Expected Behavior
Recommended Fix
Affected URLs
Severity
```

---

## 48. Marketing Report

The marketing report shall emphasize:

```text
Traffic Opportunities
Keyword Opportunities
Content Gaps
Conversion-Relevant SEO Issues
Market Opportunities
Expected Business Impact
```

---

## 49. Audit Comparison

Users shall be able to compare:

```text
Audit A
vs
Audit B
```

The system shall show:

```text
Issues Fixed
New Issues
Worsened Issues
Improved Issues
Score Changes
Category Changes
```

---

## 50. SEO Regression Detection

The system shall detect regressions such as:

```text
Previously Indexed → Noindex
200 → 404
Canonical Added → Incorrect Canonical
Good CWV → Poor CWV
Valid Schema → Invalid Schema
Healthy Sitemap → Broken Sitemap
```

---

## 51. AI Regression Diagnosis

The AI shall explain:

```text
What changed?
When did it change?
Which pages are affected?
What likely caused it?
What should be fixed?
```

---

## 52. Automated Fix Validation

After a fix, the system shall support:

```text
Re-Crawl
Re-Analyze
Compare
Validate
Close Issue
```

An issue shall only be marked resolved when the validation rules succeed.

---

## 53. Issue Lifecycle

```text
DETECTED
   ↓
TRIAGED
   ↓
ASSIGNED
   ↓
IN_PROGRESS
   ↓
FIX_SUBMITTED
   ↓
VALIDATING
   ↓
RESOLVED
```

Additional states:

```text
IGNORED
FALSE_POSITIVE
WONT_FIX
REGRESSED
```

---

## 54. AI False-Positive Detection

The AI shall identify cases where a detected technical pattern may not represent a meaningful SEO problem.

Example:

```text
Pattern:
Duplicate content.

AI Assessment:
Intentional product filtering pages.

Status:
LOW RISK / REVIEW
```

---

## 55. AI Confidence

Every AI-generated diagnosis shall include:

```text
Confidence Score
Evidence Count
Evidence Quality
Reasoning Summary
```

Confidence shall not be treated as probability of ranking improvement unless explicitly calibrated for that purpose.

---

## 56. Evidence Grounding

AI recommendations shall be grounded in:

```text
Crawl Data
Page Data
Search Data
Keyword Data
Performance Data
Historical Audits
Competitor Data
Structured Data
```

---

## 57. Hallucination Protection

The AI layer shall implement:

```text
Structured Output
Evidence Grounding
Schema Validation
Source Attribution
Fact Verification
Confidence Calibration
Contradiction Detection
```

The system shall return:

```text
INSUFFICIENT EVIDENCE
```

when the available data is inadequate.

---

## 58. SEO Recommendation Object

```json
{
  "issue_id": "SEO-001",
  "url": "https://example.com/product",
  "category": "TECHNICAL_SEO",
  "severity": "HIGH",
  "priority": "P1",
  "title": "Canonical points to redirected URL",
  "description": "The canonical target returns a redirect.",
  "root_cause": "Canonical configuration mismatch",
  "evidence": [],
  "recommended_fix": "Update canonical to the final canonical URL.",
  "expected_impact": "Improved canonical consistency",
  "effort": "LOW",
  "confidence": 0.96,
  "status": "OPEN"
}
```

---

## 59. SEO Audit Data Model

```text
audit_id
tenant_id
organization_id
workspace_id
domain_id
audit_type
status
crawl_configuration
total_urls
crawled_urls
failed_urls
seo_score
technical_score
content_score
onpage_score
performance_score
mobile_score
structured_data_score
created_at
completed_at
```

---

## 60. URL Audit Data Model

```text
audit_url_id
audit_id
url
canonical_url
status_code
indexability
crawl_depth
title
meta_description
h1
word_count
content_hash
response_time
page_size
lcp
inp
cls
internal_links
external_links
images
structured_data
issues
```

---

## 61. SEO Issue Data Model

```text
issue_id
audit_id
url_id
category
subcategory
severity
priority
title
description
root_cause
evidence
recommendation
effort
expected_impact
confidence
status
first_detected_at
last_detected_at
resolved_at
```

---

## 62. Audit API

## Create Audit

```http
POST /api/v1/seo/audits
```

## Start Audit

```http
POST /api/v1/seo/audits/{audit_id}/start
```

## Get Audit

```http
GET /api/v1/seo/audits/{audit_id}
```

## Get Issues

```http
GET /api/v1/seo/audits/{audit_id}/issues
```

## Get URL Analysis

```http
GET /api/v1/seo/audits/{audit_id}/urls/{url_id}
```

## Generate AI Recommendations

```http
POST /api/v1/seo/audits/{audit_id}/recommendations
```

## Validate Fix

```http
POST /api/v1/seo/audits/{audit_id}/issues/{issue_id}/validate
```

## Compare Audits

```http
GET /api/v1/seo/audits/compare
```

## Generate Report

```http
POST /api/v1/seo/audits/{audit_id}/report
```

---

## 63. Event-Driven Requirements

The system shall publish events including:

```text
SEOAuditCreated
SEOAuditStarted
CrawlStarted
CrawlCompleted
URLDiscovered
URLAnalyzed
SEOIssueDetected
CriticalSEOIssueDetected
AIRecommendationGenerated
SEOAuditCompleted
SEOIssueResolved
SEOIssueRegressed
SEOScoreChanged
SEORegressionDetected
```

---

## 64. Example Event

```json
{
  "event_type": "SEOIssueDetected",
  "event_id": "evt-seo-001",
  "tenant_id": "tenant-001",
  "audit_id": "audit-001",
  "issue_id": "SEO-001",
  "category": "INDEXABILITY",
  "severity": "CRITICAL",
  "url_count": 127,
  "timestamp": "2026-08-23T09:00:00Z"
}
```

---

## 65. AI Agent Integration

The SEO Audit Engine shall integrate with:

```text
SEO Manager Agent
SEO Specialist Agent
Keyword Intelligence Agent
Technical SEO Agent
SEO Analytics Agent
Marketing Manager Agent
Marketing Specialist Agent
Content Intelligence Agent
Competitor Analysis Agent
Product Launch Intelligence
```

The audit engine shall provide structured outputs to these agents.

---

## 66. SEO Manager Integration

The SEO Manager AI shall consume audit outputs to:

```text
Prioritize SEO Work
Create SEO Roadmaps
Assign SEO Priorities
Track SEO Health
Monitor SEO Risks
```

---

## 67. SEO Specialist Integration

The SEO Specialist AI shall consume audit findings to:

```text
Analyze Specific Problems
Generate Technical Recommendations
Optimize Pages
Develop Keyword Strategies
Develop Content Recommendations
```

---

## 68. Keyword Intelligence Integration

The audit engine shall send:

```text
Page
Keyword
Search Intent
Keyword Coverage
Cannibalization
Content Gap
```

to the keyword intelligence system.

---

## 69. Technical SEO Integration

The audit engine shall send:

```text
Crawlability
Indexability
Canonical
Redirect
Sitemap
Robots
Rendering
Performance
```

to the technical SEO system.

---

## 70. SEO Analytics Integration

The audit engine shall correlate audit findings with:

```text
Organic Traffic
Rankings
Conversions
CTR
Impressions
Clicks
```

where such data is available through authorized integrations.

---

## 71. Product Launch Integration

Before product launch, the system shall allow:

```text
Pre-Launch SEO Audit
Launch Readiness Audit
Post-Launch Audit
```

---

## 72. SEO Launch Readiness

The AI shall calculate:

```text
SEO Launch Readiness Score
```

based on:

```text
Technical Health
Indexability
Content Readiness
Keyword Coverage
Performance
Mobile SEO
Structured Data
Internal Linking
```

---

## 73. Continuous Monitoring

Users shall be able to configure:

```text
Daily
Weekly
Monthly
Custom
```

SEO audits.

---

## 74. SEO Alerts

The system shall generate alerts for:

```text
Critical Indexability Failure
Traffic-Relevant Pages Becoming Noindex
Large 404 Spike
Large 5xx Spike
Sitemap Failure
Robots.txt Change
Canonical Regression
CWV Regression
Major SEO Score Drop
Large Crawlability Regression
```

---

## 75. Alert Severity

```text
CRITICAL
HIGH
MEDIUM
LOW
```

---

## 76. Security Requirements

## SEC-001 — Authentication

All audit APIs shall require authentication.

## SEC-002 — Authorization

The system shall enforce:

```text
RBAC
ABAC
Tenant Isolation
Resource-Level Authorization
```

## SEC-003 — Domain Authorization

The system shall provide controls to prevent unauthorized auditing of private or restricted resources.

## SEC-004 — Credential Protection

Website credentials, if supported, shall be:

```text
Encrypted
Access-Controlled
Never Logged in Plaintext
Never Exposed to the AI Model
```

---

## 77. Crawler Security

The crawler shall defend against:

```text
SSRF
Internal Network Access
Private IP Access
Cloud Metadata Endpoints
Malicious Redirects
DNS Rebinding
Resource Exhaustion
Zip Bombs
Oversized Responses
```

---

## 78. SSRF Protection

The crawler shall validate destination addresses and prevent access to:

```text
localhost
127.0.0.0/8
Private Networks
Link-Local Networks
Cloud Metadata Services
Internal Service Addresses
```

unless explicitly and securely configured for authorized enterprise environments.

---

## 79. Resource Protection

The crawler shall enforce:

```text
Maximum Response Size
Maximum URL Count
Maximum Crawl Depth
Maximum Crawl Duration
Request Timeout
Concurrency Limits
Redirect Limits
Content-Type Restrictions
```

---

## 80. AI Security

The AI layer shall defend against:

```text
Prompt Injection
Indirect Prompt Injection
Malicious HTML
Malicious Structured Data
Untrusted External Content
Data Exfiltration
Cross-Tenant Context Leakage
Unauthorized Tool Execution
```

---

## 81. Untrusted Web Content

Webpage content shall be treated as untrusted data.

The crawler shall not allow webpage content to directly control:

```text
System Instructions
Tool Permissions
Credentials
API Calls
AI Provider Configuration
```

---

## 82. Multi-Tenant Isolation

Every audit request shall be scoped to:

```text
tenant_id
organization_id
workspace_id
user_id
```

where applicable.

No tenant shall access another tenant's:

```text
Crawl Data
Audit Data
SEO Reports
Keywords
Competitor Data
Recommendations
Credentials
```

---

## 83. Performance Requirements

The system shall support asynchronous audits.

```text
Audit Request
      ↓
Job Queue
      ↓
Crawler
      ↓
Analysis Workers
      ↓
AI Workers
      ↓
Recommendation Engine
      ↓
Report Generator
```

---

## 84. Scalability Requirements

The architecture shall support horizontal scaling of:

```text
Crawler Workers
Rendering Workers
Analysis Workers
AI Workers
Report Workers
```

The system shall support large websites without requiring a single monolithic worker.

---

## 85. Reliability Requirements

The system shall implement:

```text
Retries
Timeouts
Circuit Breakers
Idempotency
Checkpointing
Job Recovery
Dead Letter Queues
Partial Audit Recovery
Provider Failover
```

---

## 86. Crawl Checkpointing

Long audits shall persist crawl state:

```text
Discovered URLs
Processed URLs
Pending URLs
Failed URLs
Retry Count
Analysis State
```

A failed worker shall resume from the last safe checkpoint.

---

## 87. AI Provider Architecture

The SEO Audit Engine shall use the centralized SalesGenie AI Gateway.

Supported providers may include:

```text
Groq
Gemini / Google AI
Mistral AI
Other Approved Providers
```

Provider-specific logic shall remain outside the SEO Audit Engine.

---

## 88. AI Model Routing

The AI Gateway may route tasks according to:

```text
Task Complexity
Latency
Cost
Context Length
Structured Output
Provider Availability
Rate Limits
Quality
```

---

## 89. AI Failover

If the primary provider fails:

```text
Primary Model
    ↓
Retry
    ↓
Secondary Model
    ↓
Secondary Provider
    ↓
Graceful Failure
```

The system shall preserve audit state during provider failures.

---

## 90. Cost Governance

The platform shall track:

```text
Audit
URL Count
AI Requests
Provider
Model
Input Tokens
Output Tokens
Estimated Cost
Latency
```

AI analysis shall prioritize deterministic rules where AI reasoning provides little additional value.

---

## 91. Deterministic + AI Hybrid Analysis

The SEO Audit Engine shall use:

```text
Deterministic Rules
+
Statistical Analysis
+
Machine Learning
+
LLM Reasoning
```

Example:

```text
Missing title
        ↓
Deterministic Detection

Why the title is weak
        ↓
AI Analysis

How to improve it
        ↓
AI Recommendation
```

---

## 92. AI Should Not Replace Deterministic Validation

Critical technical conditions shall be validated deterministically where possible.

Examples:

```text
HTTP Status
Canonical URL
Robots Directive
Sitemap URL
Redirect Chain
HTML Presence
Meta Tag Presence
Schema Syntax
```

The AI shall provide interpretation and prioritization rather than becoming the sole source of truth.

---

## 93. Observability

The system shall expose metrics including:

```text
Audit Count
URLs Crawled
URLs Failed
Average Crawl Time
Average Audit Time
AI Latency
AI Failure Rate
Issues Detected
Critical Issues
False Positive Rate
Recommendation Acceptance
Recommendation Accuracy
```

---

## 94. Distributed Tracing

Every audit shall have a trace identifier.

Example:

```text
trace_id
audit_id
crawl_job_id
analysis_job_id
ai_job_id
report_job_id
```

---

## 95. Logging

Logs shall contain:

```text
Timestamp
Service
Tenant
Audit
URL
Job
Severity
Error
Trace ID
```

Sensitive credentials and secrets shall never be logged.

---

## 96. Audit History

The platform shall retain:

```text
Audit Version
SEO Score
Issues
Recommendations
Crawl Statistics
Performance Metrics
```

for historical comparison according to configured retention policies.

---

## 97. Recommendation Lifecycle

```text
DETECTED
   ↓
ANALYZED
   ↓
RECOMMENDED
   ↓
IMPLEMENTATION
   ↓
VALIDATION
   ↓
RESOLVED
```

---

## 98. SEO Technical Debt

The system shall calculate SEO technical debt using:

```text
Issue Severity
Issue Count
Business Impact
Affected URLs
Age
Implementation Effort
```

Output:

```text
SEO Technical Debt Score
```

---

## 99. Opportunity Detection

The AI shall distinguish:

```text
SEO Problems
```

from:

```text
SEO Opportunities
```

Example:

```text
Problem:
Missing canonical.

Opportunity:
High-value keyword page with weak internal-link support.
```

---

## 100. Opportunity Score

Opportunities shall be ranked using:

```text
Potential Traffic
Potential Conversion
Search Demand
Competition
Current Visibility
Business Value
Implementation Effort
Confidence
```

---

## 101. SEO Roadmap Generation

The audit engine shall optionally generate an AI-prioritized roadmap:

```text
Week 1:
Critical Technical Issues

Week 2:
Indexability + Internal Linking

Week 3:
Content Optimization

Week 4:
Keyword Expansion

Week 5:
Performance Optimization

Week 6:
Content Gap Expansion
```

The roadmap shall be based on detected issues and organizational constraints.

---

## 102. Executive Recommendation Example

```text
SEO HEALTH:
74/100

CRITICAL:
38 commercially important URLs are not indexable.

HIGH:
127 product pages have duplicate titles.

HIGH:
Core Web Vitals are poor on mobile.

OPPORTUNITY:
83 high-value keywords have no dedicated landing page.

AI PRIORITY:

1. Fix indexability.
2. Resolve duplicate metadata.
3. Improve mobile performance.
4. Build landing pages for high-value keyword clusters.

EXPECTED IMPACT:
High

CONFIDENCE:
91%
```

---

## 103. Developer Recommendation Example

```text
ISSUE:
Canonical points to /product-a-old

CURRENT:
301 → /product-a

RECOMMENDED:
Canonical should point directly to:

/product-a

SEVERITY:
HIGH

EFFORT:
LOW

AFFECTED URLS:
23

CONFIDENCE:
98%
```

---

## 104. AI Audit Copilot

Users shall be able to ask:

```text
What are the most serious SEO problems?

Which issues should developers fix first?

Why did my SEO score decrease?

Which pages are not indexable?

Which pages are competing for the same keywords?

Which pages have the greatest SEO opportunity?

What is causing our technical SEO problems?

Which fixes can produce the highest expected impact?

Which problems are likely to be false positives?

What changed since the previous audit?

Which SEO problems are affecting our product launch?
```

---

## 105. AI Explanation Requirements

The AI shall answer using:

```text
Finding
Evidence
Impact
Recommendation
Confidence
```

It shall avoid unsupported claims.

---

## 106. SEO Audit Quality Metrics

The system shall track:

```text
Issue Detection Precision
Issue Detection Recall
False Positive Rate
False Negative Rate
AI Recommendation Quality
Recommendation Acceptance Rate
Fix Validation Accuracy
Audit Completion Rate
Crawler Success Rate
```

---

## 107. AI Evaluation

The AI shall be evaluated against benchmark cases for:

```text
Technical SEO Diagnosis
Content Diagnosis
Search Intent Classification
Keyword Cannibalization
Duplicate Content
Internal Linking
Structured Data
Performance Diagnosis
Recommendation Quality
```

---

## 108. Regression Testing

Every change to the audit engine shall be tested against a fixed benchmark corpus containing:

```text
Healthy Websites
Technically Broken Websites
Content-Heavy Websites
E-Commerce Websites
SaaS Websites
News Websites
International Websites
JavaScript Applications
Large Websites
```

---

## 109. Data Lineage

Every AI recommendation shall retain:

```text
Audit ID
URL
Evidence
Analyzer Version
Rule Version
AI Provider
AI Model
Model Version
Prompt Version
Context Version
Recommendation Version
Timestamp
```

---

## 110. Reproducibility

The system shall make audit results reproducible by preserving:

```text
Crawler Configuration
User-Agent
Rendering Configuration
Analyzer Version
Rule Version
Data Timestamp
AI Model
AI Configuration
```

---

## 111. Audit Immutability

Completed audits shall be immutable.

Corrections shall create a new audit version rather than silently modifying historical results.

---

## 112. API Idempotency

Audit creation and execution APIs shall support idempotency keys where applicable.

Repeated requests shall not unintentionally create duplicate expensive crawl jobs.

---

## 113. Rate Limiting

The system shall enforce rate limits for:

```text
Audit Creation
Crawl Jobs
AI Analysis
Report Generation
API Requests
```

---

## 114. Quotas

Organizations may have configurable:

```text
Monthly Crawled URLs
Concurrent Audits
AI Analysis Credits
Historical Audit Retention
Report Generation
```

---

## 115. Failure Handling

If part of an audit fails, the system shall preserve successful results.

Example:

```text
Technical Audit: COMPLETE
Content Audit: COMPLETE
Performance Audit: PARTIAL
AI Recommendations: COMPLETE
```

The report shall explicitly identify partial data.

---

## 116. Graceful Degradation

If AI services become unavailable:

```text
Deterministic SEO Audit
```

shall remain available.

AI recommendations shall be marked:

```text
TEMPORARILY UNAVAILABLE
```

rather than fabricated.

---

## 117. Definition of Done

The `seo_audit.md` module shall be considered production-ready when it can:

* Crawl websites safely.
* Discover URLs.
* Analyze XML sitemaps.
* Analyze robots.txt.
* Analyze HTTP responses.
* Analyze redirects.
* Analyze canonicals.
* Analyze indexability.
* Analyze crawlability.
* Detect orphan pages.
* Detect broken links.
* Analyze metadata.
* Analyze headings.
* Analyze URLs.
* Analyze content.
* Detect duplicate content.
* Detect thin content.
* Detect keyword cannibalization.
* Analyze search intent.
* Analyze internal links.
* Analyze external links.
* Analyze images.
* Analyze structured data.
* Analyze mobile SEO.
* Analyze Core Web Vitals.
* Analyze JavaScript rendering.
* Analyze international SEO.
* Analyze local SEO.
* Analyze competitor SEO signals.
* Detect SEO opportunities.
* Generate SEO health scores.
* Detect SEO regressions.
* Generate AI diagnoses.
* Generate AI recommendations.
* Assign issue severity.
* Assign issue priority.
* Assign confidence.
* Provide evidence.
* Estimate implementation effort.
* Estimate expected impact.
* Validate fixes.
* Compare historical audits.
* Generate executive reports.
* Generate developer reports.
* Generate marketing reports.
* Support continuous monitoring.
* Generate SEO alerts.
* Preserve audit history.
* Preserve data lineage.
* Enforce tenant isolation.
* Enforce RBAC.
* Enforce ABAC.
* Protect credentials.
* Prevent SSRF.
* Protect against malicious web content.
* Protect against prompt injection.
* Validate AI outputs.
* Support AI provider failover.
* Support asynchronous crawling.
* Support horizontal scaling.
* Provide distributed tracing.
* Provide observability.
* Provide audit logging.
* Support deterministic and AI-based analysis.
* Gracefully operate when AI services are unavailable.

---

## 118. Final SEO Audit Architecture

```text
                         WEBSITE
                            |
                            v
                    ┌───────────────┐
                    │ URL DISCOVERY │
                    └───────┬───────┘
                            |
                            v
                    ┌───────────────┐
                    │    CRAWLER    │
                    └───────┬───────┘
                            |
          ┌─────────────────┼─────────────────┐
          |                 |                 |
          v                 v                 v
     HTML Analysis     HTTP Analysis     JS Rendering
          |                 |                 |
          +─────────────────+─────────────────+
                            |
                            v
                 ┌────────────────────┐
                 │ TECHNICAL SEO      │
                 │ ANALYZER           │
                 └─────────┬──────────┘
                           |
          ┌────────────────┼─────────────────┐
          |                |                 |
          v                v                 v
      ON-PAGE          CONTENT           PERFORMANCE
       SEO              SEO                 SEO
          |                |                 |
          +────────────────+─────────────────+
                           |
                           v
                ┌─────────────────────┐
                │ KEYWORD INTELLIGENCE│
                └──────────┬──────────┘
                           |
                           v
                ┌─────────────────────┐
                │ COMPETITOR ANALYSIS │
                └──────────┬──────────┘
                           |
                           v
                ┌─────────────────────┐
                │ AI DIAGNOSIS ENGINE │
                └──────────┬──────────┘
                           |
                           v
                ┌─────────────────────┐
                │ ISSUE PRIORITIZATION│
                └──────────┬──────────┘
                           |
                           v
                ┌─────────────────────┐
                │ AI RECOMMENDATIONS  │
                └──────────┬──────────┘
                           |
              ┌────────────┼────────────┐
              |            |            |
              v            v            v
          SEVERITY      IMPACT      CONFIDENCE
              |            |            |
              +────────────┼────────────+
                           |
                           v
                ┌─────────────────────┐
                │ SEO AUDIT REPORT    │
                └──────────┬──────────┘
                           |
                           v
                    SALESGenie UI
                           |
                           v
                    IMPLEMENTATION
                           |
                           v
                      RE-CRAWL
                           |
                           v
                    FIX VALIDATION
                           |
                           v
                  SEO FEEDBACK LOOP
```

## 119. Strategic Outcome

The `seo_audit` engine shall transform SalesGenie from a basic SEO reporting system into an **AI-powered SEO intelligence and diagnostic platform** capable of answering:

```text
WHAT IS WRONG?
        +
WHY IS IT WRONG?
        +
WHICH PAGES ARE AFFECTED?
        +
HOW IMPORTANT IS IT?
        +
WHAT IS THE BUSINESS IMPACT?
        +
HOW SHOULD IT BE FIXED?
        +
HOW MUCH EFFORT WILL IT REQUIRE?
        +
WHAT SHOULD BE FIXED FIRST?
        +
WHAT SEO OPPORTUNITIES EXIST?
        +
DID THE FIX WORK?
        +
DID THE WEBSITE REGRESS?
```

The engine shall serve as the **central AI-driven SEO diagnostic layer of SalesGenie**, feeding validated technical, content, keyword, performance, competitor, and opportunity intelligence into the SEO Manager, SEO Specialist, Marketing, Product Launch, Marketing Analytics, and broader AI decision-making systems.
