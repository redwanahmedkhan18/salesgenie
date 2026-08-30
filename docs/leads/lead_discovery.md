# Lead Discovery — FAANG-Level User, System & Functional Requirements

## 1. Purpose

The **Lead Discovery** module of SalesGenie shall provide an enterprise-grade AI + human-assisted prospect discovery engine for identifying, researching, validating, prioritizing, and importing high-potential companies, contacts, and prospects.

The module shall support:

* AI-powered lead discovery
* Human-driven prospect research
* AI-assisted human discovery
* Human verification of AI-discovered leads
* Company discovery
* Contact discovery
* Account discovery
* ICP-based discovery
* Persona-based discovery
* Firmographic discovery
* Technographic discovery
* Intent-based discovery
* Geographic discovery
* Industry discovery
* Keyword-based discovery
* Competitor-based discovery
* Similar-company discovery
* Event-triggered discovery
* CRM-based discovery
* External-data discovery
* MCP/tool-based discovery
* Natural-language prospect search
* Bulk lead discovery
* Continuous lead discovery
* Duplicate detection
* Entity resolution
* Lead validation
* Lead scoring integration
* Lead enrichment integration
* Human approval workflows
* Evidence and provenance tracking

The existing SalesGenie lead-intelligence architecture already defines company discovery/search capabilities with tenant-scoped access and filters such as industry, location, employee count, revenue, technologies, and keywords.

---

## 2. Business Objectives

SalesGenie Lead Discovery shall:

1. Reduce manual prospect research.
2. Discover high-fit accounts at scale.
3. Identify relevant decision-makers.
4. Increase qualified-lead volume.
5. Improve ICP matching.
6. Improve prospecting precision.
7. Reduce irrelevant leads.
8. Discover previously unknown prospects.
9. Identify buying signals.
10. Identify companies matching configurable business criteria.
11. Identify contacts matching configurable personas.
12. Support account-based prospecting.
13. Support territory-based prospecting.
14. Support campaign-specific prospect discovery.
15. Support sales-representative prospect discovery.
16. Support AI-generated discovery strategies.
17. Support human-controlled discovery strategies.
18. Provide evidence for discovered leads.
19. Maintain source provenance.
20. Prevent cross-tenant discovery.
21. Prevent duplicate lead creation.
22. Integrate discovery with enrichment, qualification, scoring, outreach, and CRM.

---

## 3. Discovery Architecture

```text
User / Sales Agent
        |
        v
Discovery Workspace
        |
        +-----------------------+
        |                       |
        v                       v
Human Discovery          AI Discovery Agent
        |                       |
        +-----------+-----------+
                    |
                    v
            Discovery Planner
                    |
                    v
             Source Router
                    |
        +-----------+-----------+
        |           |           |
        v           v           v
 CRM / DB       Search       MCP / APIs
        |           |           |
        +-----------+-----------+
                    |
                    v
             Candidate Leads
                    |
                    v
             Entity Resolution
                    |
                    v
              Deduplication
                    |
                    v
              Validation
                    |
                    v
            Evidence Analysis
                    |
                    v
             ICP Evaluation
                    |
                    v
             Lead Scoring
                    |
                    v
          Human Verification
                    |
                    v
             Lead Enrichment
                    |
                    v
          SalesGenie Lead Pool
                    |
                    v
       Qualification / Outreach
```

---

## 4. Supported Actors

## Human Actors

```text
Super Admin
Platform Admin
Organization Admin
Workplace Admin

Chief Revenue Officer
VP Sales
Sales Director
Sales Manager
Revenue Operations Manager
Sales Operations Manager

Account Executive
Sales Representative
SDR
BDR
Account Manager

Sales Analyst
Research Analyst
Data Steward
Lead Operations Specialist
```

## AI Actors

```text
AI Lead Discovery Agent
AI Company Discovery Agent
AI Contact Discovery Agent
AI ICP Matching Agent
AI Persona Matching Agent
AI Intent Discovery Agent
AI Similarity Discovery Agent
AI Competitor Discovery Agent
AI Research Agent
AI Verification Agent
AI Entity Resolution Agent
AI Duplicate Detection Agent
AI Lead Scoring Agent
AI Recommendation Agent
AI Discovery Optimization Agent
```

---

## 5. Discovery Modes

The platform shall support:

```text
MANUAL_DISCOVERY
AI_DISCOVERY
AI_ASSISTED_DISCOVERY
HUMAN_VERIFIED_DISCOVERY
HYBRID_DISCOVERY
BATCH_DISCOVERY
CONTINUOUS_DISCOVERY
EVENT_DRIVEN_DISCOVERY
CRM_DISCOVERY
CAMPAIGN_DISCOVERY
ACCOUNT_BASED_DISCOVERY
TERRITORY_DISCOVERY
```

---

## 6. Lead Discovery Lifecycle

```text
DISCOVERY_REQUESTED
        ↓
DISCOVERY_PLANNED
        ↓
SOURCE_SELECTION
        ↓
SEARCH_EXECUTION
        ↓
CANDIDATE_COLLECTION
        ↓
ENTITY_RESOLUTION
        ↓
DEDUPLICATION
        ↓
VALIDATION
        ↓
ICP_MATCHING
        ↓
PERSONA_MATCHING
        ↓
INTENT_ANALYSIS
        ↓
CONFIDENCE_SCORING
        ↓
HUMAN_REVIEW
        ↓
ENRICHMENT
        ↓
QUALIFICATION
        ↓
LEAD_CREATED
        ↓
ROUTING
        ↓
OUTREACH
```

---

## 7. Discovery States

```text
DRAFT
QUEUED
PLANNING
SEARCHING
COLLECTING
RESOLVING
VALIDATING
SCORING
REVIEW_REQUIRED
APPROVED
REJECTED
IMPORTED
DUPLICATE
INVALID
FAILED
PARTIAL
CANCELLED
COMPLETED
```

---

## 8. User Requirements

## UR-001 — Discovery Dashboard

Authorized users shall be able to view:

```text
Active Discovery Jobs
Completed Jobs
Failed Jobs
Candidates Found
Qualified Leads
Rejected Leads
Duplicates
Pending Verification
High-Intent Leads
High-ICP-Fit Leads
Recently Discovered Accounts
Recently Discovered Contacts
Discovery Cost
Discovery Success Rate
Source Performance
```

---

## 9. Discovery Workspace

Users shall have a dedicated discovery workspace containing:

```text
Search Builder
AI Discovery
Saved Searches
Discovery History
Discovery Jobs
Candidate Results
Verification Queue
Lead Import Queue
Discovery Analytics
Source Configuration
ICP Configuration
Persona Configuration
```

---

## 10. Manual Lead Discovery

Users shall be able to manually search for companies and prospects.

The search interface shall support:

```text
Industry
Sub-Industry
Location
Country
City
Employee Count
Revenue
Technology
Keywords
Company Name
Company Domain
Job Title
Department
Seniority
Business Model
Funding Stage
Funding
Growth Stage
Intent
Hiring Signals
Technology Adoption
```

The current SalesGenie lead-intelligence API already supports company-search parameters including industry, location, employee count, revenue, technologies, and keywords.

---

## 11. Company Discovery

The system shall discover companies matching:

```text
Industry
Sub-Industry
Company Size
Revenue
Geography
Technology Stack
Business Model
Funding
Growth
Hiring
Keywords
Products
Services
Market
Customer Segment
```

---

## 12. Contact Discovery

The system shall discover relevant contacts associated with target accounts.

Supported attributes:

```text
First Name
Last Name
Job Title
Department
Seniority
Role
Email
Phone
Professional Profile
Location
Company
```

---

## 13. Decision-Maker Discovery

The system shall identify potential:

```text
Decision Makers
Economic Buyers
Technical Buyers
Business Buyers
Champions
Influencers
Executive Sponsors
Procurement Contacts
Gatekeepers
End Users
```

The system shall distinguish **potential role classification** from verified factual information.

---

## 14. Persona-Based Discovery

Users shall be able to specify:

```text
Persona
Job Title
Department
Seniority
Industry
Company Size
Geography
Technology
Business Need
```

Example:

```text
Find CTOs at SaaS companies
with 200–2,000 employees
in the United States
using cloud infrastructure
and actively hiring engineers.
```

---

## 15. ICP-Based Discovery

The system shall support configurable Ideal Customer Profiles.

An ICP shall contain:

```text
Industry
Sub-Industry
Company Size
Revenue
Location
Technology
Business Model
Funding
Growth
Market
Use Case
Customer Segment
Intent
Strategic Fit
```

---

## 16. ICP Discovery

The system shall rank discovered companies against the configured ICP.

Example:

```text
ICP Match

Industry: 95%
Company Size: 88%
Revenue: 91%
Technology: 84%
Location: 100%
Growth: 93%

Overall ICP Fit: 92%
```

---

## 17. Natural-Language Discovery

Users shall be able to enter natural-language queries.

Examples:

```text
"Find SaaS companies with more than 500 employees."

"Find CTOs at recently funded technology companies."

"Find companies using Salesforce that are hiring salespeople."

"Find companies similar to our top five customers."

"Find companies likely to need AI customer support automation."
```

The AI shall translate the request into structured discovery criteria.

---

## 18. AI Discovery Planner

The AI Discovery Agent shall:

1. Interpret the user's objective.
2. Identify required filters.
3. Identify missing constraints.
4. Generate a discovery plan.
5. Select authorized sources.
6. Select appropriate tools.
7. Execute discovery.
8. Normalize results.
9. Resolve entities.
10. Remove duplicates.
11. Validate candidates.
12. Calculate ICP fit.
13. Calculate confidence.
14. Recommend top prospects.
15. Request human review when required.

---

## 19. AI Discovery Strategy

AI shall dynamically select discovery strategies such as:

```text
FILTER_FIRST
SEARCH_FIRST
ACCOUNT_FIRST
CONTACT_FIRST
ICP_FIRST
TECHNOLOGY_FIRST
INTENT_FIRST
SIMILARITY_FIRST
COMPETITOR_FIRST
SIGNAL_FIRST
TERRITORY_FIRST
```

---

## 20. AI Discovery Reasoning

The AI shall explain:

```text
Why the lead was discovered
Which criteria matched
Which evidence supports the match
Which information is inferred
Which information is missing
Why the lead was prioritized
```

---

## 21. AI Discovery Evidence

Every important AI discovery result shall include:

```text
Finding
Source
Evidence
Confidence
Observed / Inferred
Timestamp
```

AI shall not present unsupported assumptions as verified facts.

---

## 22. Source Discovery

The platform shall support configurable sources including:

```text
Internal CRM
Internal Lead Database
Customer Accounts
Authorized Search APIs
Authorized Business Data Providers
Company Websites
Authorized Public Sources
Professional Data Providers
Technology Data Providers
Intent Providers
MCP Servers
Internal Knowledge Base
```

External-source usage shall comply with provider terms and organizational policies.

---

## 23. Source Router

The Discovery Orchestrator shall determine:

```text
Which source to use
Why the source is appropriate
Source priority
Source availability
Source cost
Source coverage
Source confidence
Fallback source
```

---

## 24. Provider Failover

```text
Primary Source
      ↓
Failure
      ↓
Retry
      ↓
Secondary Source
      ↓
Failure
      ↓
Alternative Source
      ↓
Human Research
```

Provider failure shall never silently generate fabricated lead information.

---

## 25. Source Reliability

Administrators shall configure source priorities based on:

```text
Accuracy
Freshness
Coverage
Cost
Latency
Geographic Availability
Industry Availability
Field Availability
Historical Performance
```

---

## 26. MCP-Based Lead Discovery

The system shall support authorized MCP servers for:

```text
Company Search
Contact Search
Business Research
Technology Research
Intent Research
Market Research
CRM Search
Internal Data Search
```

Each MCP tool shall have:

```text
Tool ID
Tool Name
Description
Input Schema
Output Schema
Permission
Tenant Scope
Rate Limit
Cost
Approval Requirement
Audit Policy
```

---

## 27. MCP Tool Security

AI agents shall:

* Use only explicitly authorized tools.
* Operate within tenant boundaries.
* Validate all tool inputs.
* Validate all tool outputs.
* Enforce execution budgets.
* Prevent recursive tool loops.
* Prevent unauthorized external actions.
* Detect indirect prompt injection.
* Redact sensitive data.
* Log tool execution.

SalesGenie's production audit requirements explicitly call for least-privilege agent/tool permissions, strict tool schemas, protection against prompt injection, execution budgets, and human approval for high-impact actions.

---

## 28. Human Lead Discovery

Humans shall be able to:

```text
Search
Filter
Research
Compare
Inspect
Verify
Reject
Approve
Save
Tag
Assign
Import
Enrich
```

---

## 29. Human Research Mode

Users shall be able to open a candidate and manually investigate:

```text
Company
Website
Leadership
Products
Industry
Technology
Location
Business Model
Growth
Hiring
Funding
Potential Need
```

---

## 30. AI-Assisted Human Research

A user shall be able to ask:

```text
"Research this company."

"Find relevant decision-makers."

"Find similar companies."

"Explain why this company matches our ICP."

"Find evidence for this lead."

"Find missing information."

"Compare this company with our ICP."
```

AI shall provide research assistance without silently modifying authoritative CRM records.

---

## 31. Human Verification Queue

The system shall create review tasks for:

```text
Low-Confidence Leads
Conflicting Sources
Potential Duplicates
High-Value Accounts
Sensitive Records
Ambiguous Entity Matches
Potential Decision Makers
AI-Uncertain Results
Policy-Restricted Data
```

---

## 32. Candidate Review

Reviewers shall be able to:

```text
Approve
Reject
Edit
Merge
Request Research
Request Enrichment
Mark Duplicate
Mark Invalid
Assign
Add Notes
Add Tags
```

---

## 33. Candidate Comparison

Users shall be able to compare prospects using:

```text
Company
Industry
Revenue
Employees
Technology
Location
ICP Fit
Intent
Growth
Funding
Contacts
Confidence
Evidence
```

---

## 34. Similar-Company Discovery

Users shall be able to select an existing company and request:

```text
Find Similar Companies
```

Similarity may use:

```text
Industry
Company Size
Revenue
Technology
Business Model
Products
Customer Segment
Geography
Growth
Market
```

---

## 35. Lookalike Discovery

The system shall support discovery based on:

```text
Best Customers
Won Deals
High-Value Accounts
High-Converting Leads
Successful Opportunities
```

AI shall derive configurable lookalike characteristics.

---

## 36. Competitor-Based Discovery

Users shall be able to discover:

```text
Competitors
Competitor Customers
Competitor Alternatives
Companies Using Competitor Technologies
Companies Evaluating Competitor Products
```

Where evidence is insufficient, the system shall label the relationship as uncertain.

---

## 37. Technology-Based Discovery

Users shall be able to search for companies using:

```text
CRM
ERP
Cloud
CMS
Marketing Automation
Customer Support
Analytics
AI
Data Platforms
Security
DevOps
E-commerce
Payment Platforms
```

---

## 38. Technology Opportunity Discovery

AI shall identify prospects based on technology signals such as:

```text
Legacy Technology
Missing Technology
Technology Migration
Technology Expansion
New Technology Adoption
Integration Opportunity
```

These shall be treated as intelligence signals rather than definitive purchasing intent unless verified.

---

## 39. Intent-Based Discovery

The system shall support discovery using:

```text
Buying Intent
Product Intent
Category Intent
Research Intent
Competitive Intent
Technology Intent
Expansion Intent
```

---

## 40. Business-Signal Discovery

The platform shall discover companies associated with:

```text
New Funding
Leadership Changes
Executive Hiring
Rapid Hiring
Market Expansion
New Product Launch
Acquisition
Merger
Office Expansion
Technology Migration
Strategic Partnership
```

---

## 41. Hiring-Based Discovery

The system shall support discovery based on:

```text
Hiring Volume
Relevant Job Openings
Technology Hiring
Sales Hiring
Marketing Hiring
Leadership Hiring
Geographic Hiring
```

---

## 42. Funding-Based Discovery

Users shall be able to search for companies based on:

```text
Funding Stage
Funding Amount
Funding Date
Investors
Recent Funding
Funding Growth
```

---

## 43. Geographic Discovery

The system shall support:

```text
Country
Region
State / Province
City
Postal Area
Territory
Sales Region
Timezone
```

Users shall be able to create geographic prospecting territories.

---

## 44. Industry Discovery

The system shall support:

```text
Industry
Sub-Industry
Vertical
Market Segment
Business Category
```

Industry taxonomy shall be configurable.

---

## 45. Keyword Discovery

Users shall be able to search using:

```text
Company Keywords
Product Keywords
Service Keywords
Technology Keywords
Business Need Keywords
Market Keywords
Job Description Keywords
```

---

## 46. Semantic Discovery

AI shall support semantic matching beyond exact keyword matches.

Example:

```text
Query:
"Companies looking for customer support automation."

Potential matches may contain:
- AI support
- conversational support
- contact-center modernization
- helpdesk automation
- customer service transformation
```

Semantic matches shall include relevance and confidence.

---

## 47. Boolean Discovery

Users shall be able to create advanced expressions:

```text
AND
OR
NOT
EXACT MATCH
RANGE
IN
NOT IN
```

Example:

```text
Industry = SaaS
AND Employees >= 200
AND Location = USA
AND Technology = Salesforce
AND NOT Customer = Existing Account
```

---

## 48. Discovery Templates

The platform shall provide templates such as:

```text
SaaS Prospecting
Enterprise Prospecting
SMB Prospecting
Startup Prospecting
Decision Maker Discovery
Technology-Based Prospecting
Competitor-Based Prospecting
Account-Based Prospecting
Territory Prospecting
High-Intent Prospecting
Funding-Based Prospecting
Hiring-Based Prospecting
```

---

## 49. Saved Searches

Users shall be able to:

```text
Save Search
Rename Search
Duplicate Search
Edit Search
Share Search
Schedule Search
Delete Search
```

---

## 50. Scheduled Discovery

Users shall be able to schedule:

```text
Daily Discovery
Weekly Discovery
Monthly Discovery
Event-Triggered Discovery
Continuous Discovery
```

---

## 51. Continuous Lead Discovery

The platform shall continuously search for new prospects matching a saved discovery profile.

Example:

```text
ICP
 ↓
Continuous Search
 ↓
New Candidate
 ↓
Deduplication
 ↓
Validation
 ↓
Scoring
 ↓
Notification
 ↓
Human Review
```

---

## 52. Event-Driven Discovery

Discovery may be triggered by:

```text
New Funding
New Hiring
New Product
New Market Entry
Leadership Change
Technology Change
Intent Signal
CRM Event
Campaign Launch
```

---

## 53. Discovery Exclusions

Users shall be able to exclude:

```text
Existing Customers
Existing Leads
Existing Contacts
Existing Opportunities
Existing Accounts
Competitors
Suppressed Companies
Suppressed Contacts
Previous Rejected Leads
Specific Domains
Specific Industries
Specific Countries
```

---

## 54. Global Suppression

Administrators shall be able to maintain organization-wide suppression lists.

Suppression shall be checked before lead creation.

---

## 55. Existing Customer Protection

The discovery engine shall prevent accidental prospecting of:

```text
Existing Customers
Active Opportunities
Protected Strategic Accounts
Suppressed Accounts
```

unless explicitly overridden by policy.

---

## 56. Duplicate Detection

The system shall identify:

```text
Exact Duplicate
Probable Duplicate
Possible Duplicate
Related Entity
Unrelated Entity
```

Matching signals may include:

```text
Email
Phone
Company
Domain
Name
Address
Professional Profile
External Identifier
CRM ID
```

---

## 57. Entity Resolution

The system shall resolve:

```text
Company
Organization
Account
Contact
Person
Domain
Subsidiary
Parent Company
```

The system shall avoid creating separate records for the same entity when a sufficiently reliable match exists.

---

## 58. Duplicate Handling

Users shall be able to:

```text
Merge
Reject Match
Keep Both
Select Primary Record
```

All merges shall be auditable.

---

## 59. Lead Validation

Discovered candidates shall be validated for:

```text
Company Existence
Domain
Contact Identity
Business Relevance
Location
Industry
Duplicate Status
Data Completeness
Source Reliability
```

---

## 60. Confidence Scoring

Every discovered candidate shall receive:

```text
Discovery Confidence
Entity Confidence
ICP Confidence
Source Confidence
Contact Confidence
Intent Confidence
Overall Confidence
```

---

## 61. Lead Discovery Score

The system shall calculate a configurable score:

```text
Discovery Score =
ICP Fit
+ Data Confidence
+ Intent
+ Business Relevance
+ Contact Relevance
+ Source Reliability
+ Freshness
```

Weights shall be organization-configurable.

---

## 62. AI Lead Prioritization

AI shall classify prospects into:

```text
PRIORITY_1
PRIORITY_2
PRIORITY_3
LOW_PRIORITY
REVIEW_REQUIRED
```

AI shall explain the reason for prioritization.

---

## 63. Evidence Requirements

Every high-impact discovery recommendation shall expose:

```text
Matched Criterion
Evidence
Source
Timestamp
Confidence
Observed / Inferred
```

---

## 64. Observed vs Inferred

The platform shall distinguish:

```text
OBSERVED
Directly supported by evidence.

VERIFIED
Confirmed by authorized human or trusted source.

INFERRED
Derived from available evidence.

PREDICTED
Generated by a predictive model.

UNKNOWN
Insufficient evidence.
```

---

## 65. AI Hallucination Controls

The discovery system shall:

```text
Require evidence for factual claims
Validate structured outputs
Separate facts from inference
Track source provenance
Track confidence
Reject unsupported claims
Escalate uncertain discoveries
```

SalesGenie's AI audit requirements explicitly require separation of facts, retrieved evidence, assumptions, inference, and predictions in intelligence workflows.

---

## 66. Discovery Research Report

For important discovery jobs, the system shall generate:

```text
Discovery Objective
Search Strategy
Sources Used
Companies Found
Contacts Found
ICP Matches
Intent Signals
Top Prospects
Rejected Candidates
Duplicate Candidates
Confidence
Evidence
Recommended Next Actions
```

---

## 67. Human Research Notes

Users shall be able to add:

```text
Research Notes
Lead Context
Business Need
Potential Opportunity
Verification Notes
Contact Notes
Follow-Up Notes
```

---

## 68. AI Research Summary

AI shall summarize discovered prospects using:

```text
Company Overview
Why It Matches
Potential Business Need
Relevant Contacts
Buying Signals
Technology Signals
Risk Factors
Evidence
Recommended Action
```

---

## 69. Lead Import

Users shall be able to import discovered candidates into SalesGenie as:

```text
Lead
Contact
Account
Prospect
Opportunity Candidate
```

---

## 70. Import Modes

```text
MANUAL_IMPORT
APPROVED_IMPORT
AUTO_IMPORT
BATCH_IMPORT
AI_RECOMMENDED_IMPORT
```

Automatic import shall require configured policy.

---

## 71. Pre-Import Validation

Before import, the system shall verify:

```text
Tenant
Permissions
Duplicate Status
Required Fields
Source
Confidence
Suppression
Compliance Rules
```

---

## 72. Discovery-to-Enrichment Flow

```text
Discovery
   ↓
Candidate
   ↓
Validation
   ↓
Enrichment
   ↓
Verification
   ↓
Lead Creation
```

The enrichment module shall receive discovery metadata and preserve discovery provenance.

---

## 73. Discovery-to-Qualification Flow

```text
Discovery
   ↓
Enrichment
   ↓
ICP Match
   ↓
Intent
   ↓
Lead Qualification
   ↓
Lead Score
   ↓
Routing
```

---

## 74. Discovery-to-Outreach Flow

```text
Discovery
   ↓
Enrichment
   ↓
Qualification
   ↓
Personalization
   ↓
Sales Sequence
   ↓
Outreach
```

---

## 75. Discovery-to-Opportunity Flow

```text
Discovery
   ↓
Lead
   ↓
Qualification
   ↓
Opportunity
   ↓
Deal
   ↓
Forecast
```

---

## 76. AI + Human Collaboration

The system shall support:

```text
AI Finds
 ↓
Human Reviews
 ↓
Human Corrects
 ↓
AI Re-evaluates
 ↓
Human Approves
 ↓
System Imports
```

---

## 77. Human Override

Authorized users shall be able to override:

```text
ICP Classification
Lead Priority
Entity Match
Duplicate Decision
Discovery Result
Source Selection
Import Decision
```

Overrides shall require:

```text
User
Timestamp
Previous Value
New Value
Reason
```

---

## 78. AI Discovery Approval

Organizations shall configure autonomy levels:

```text
LEVEL 0
AI suggests searches only.

LEVEL 1
AI finds candidates for human review.

LEVEL 2
AI finds and validates low-risk candidates.

LEVEL 3
AI automatically imports candidates meeting strict rules.

LEVEL 4
AI continuously discovers and routes prospects under
organization-defined policies, budgets, permissions,
confidence thresholds, and approval controls.
```

---

## 79. Discovery Permissions

The platform shall support permissions including:

```text
lead_discovery.read
lead_discovery.create
lead_discovery.update
lead_discovery.delete

lead_discovery.search
lead_discovery.execute
lead_discovery.bulk_execute
lead_discovery.schedule

lead_discovery.review
lead_discovery.verify
lead_discovery.approve
lead_discovery.reject
lead_discovery.import

lead_discovery.ai.read
lead_discovery.ai.search
lead_discovery.ai.research
lead_discovery.ai.recommend

lead_discovery.provider.read
lead_discovery.provider.configure

lead_discovery.analytics.read
lead_discovery.audit.read
```

---

## 80. AI Permissions

AI agents shall operate under least privilege:

```text
ai.lead_discovery.search
ai.company.search
ai.contact.search
ai.account.search
ai.research.execute
ai.entity.resolve
ai.duplicate.detect
ai.icp.evaluate
ai.intent.evaluate
ai.lead.score
ai.recommendation.create
```

---

## 81. Tenant Isolation

Discovery shall enforce isolation by:

```text
Tenant
Organization
Workplace
User
Campaign
Resource
```

A discovery query must never return another tenant's private records.

SalesGenie's architecture requires tenant-scoped lead intelligence access and the current discovery implementation explicitly filters company records by tenant ownership.

---

## 82. Discovery Job Architecture

Each discovery job shall contain:

```text
Job ID
Tenant ID
Organization ID
Workplace ID
Created By
Discovery Objective
Search Criteria
AI Strategy
Sources
Tools
Status
Progress
Candidates Found
Qualified Candidates
Rejected Candidates
Duplicates
Cost
Started At
Completed At
Error
```

---

## 83. Asynchronous Discovery

Long-running discovery operations shall execute asynchronously.

Examples:

```text
Large Company Search
Large Contact Search
AI Research
Multi-Source Discovery
Similarity Search
Competitor Research
Continuous Discovery
Bulk Discovery
```

SalesGenie's architecture should keep long-running AI, enrichment, research, and workflow jobs asynchronous to avoid blocking API operations.

---

## 84. Real-Time Discovery

Lightweight operations may execute synchronously:

```text
Database Search
Cached Company Lookup
Basic Filtering
Saved Search Execution
```

---

## 85. Discovery Queue

The queue shall support:

```text
Priority
Tenant
User
Campaign
Job Type
Created Time
Estimated Cost
Expected Duration
```

---

## 86. Job Prioritization

High-priority jobs may include:

```text
Enterprise Campaign
High-Value Account Search
Time-Sensitive Campaign
Executive Prospecting
High-Intent Discovery
```

---

## 87. Retry Policy

The system shall support:

```text
Exponential Backoff
Maximum Retry Count
Provider-Specific Retry
Circuit Breaker
Dead-Letter Queue
Partial Completion
Human Fallback
```

---

## 88. Idempotency

Repeated discovery requests shall not unintentionally create:

```text
Duplicate Leads
Duplicate Contacts
Duplicate Accounts
Duplicate Provider Charges
Duplicate Notifications
Duplicate CRM Records
```

---

## 89. Discovery Caching

The system shall cache eligible discovery results using configurable:

```text
TTL
Tenant Scope
Source
Query
Freshness
Data Sensitivity
```

Caching shall not bypass authorization.

---

## 90. Cost Optimization

The Discovery Orchestrator shall optimize:

```text
Search API Cost
Provider Cost
AI Token Cost
MCP Cost
Database Cost
Research Cost
```

Strategies shall include:

```text
Caching
Deduplication
Batch Requests
Query Optimization
Provider Routing
Model Routing
Early Termination
Result Reuse
```

SalesGenie's cost audit explicitly calls for cost-per-lead measurement, caching repeated research, tenant quotas, runaway-agent safeguards, and task-based model routing.

---

## 91. Discovery Budgets

Organizations shall be able to configure:

```text
Daily Discovery Budget
Monthly Discovery Budget
AI Token Budget
Provider Budget
Maximum Results
Maximum Search Depth
Maximum Agent Steps
Maximum Tool Calls
```

---

## 92. Rate Limiting

The system shall enforce:

```text
Tenant Limits
User Limits
Provider Limits
API Limits
AI Limits
MCP Limits
Batch Limits
```

---

## 93. Discovery Analytics

The platform shall measure:

```text
Discovery Volume
Companies Discovered
Contacts Discovered
Qualified Leads
ICP Match Rate
Duplicate Rate
Invalid Rate
Verification Rate
Import Rate
Conversion Rate
Source Success Rate
Provider Accuracy
AI Accuracy
Human Correction Rate
Cost Per Lead
Cost Per Qualified Lead
Discovery Latency
```

---

## 94. Source Analytics

For each source:

```text
Source
Queries
Candidates
Valid Candidates
Qualified Candidates
Duplicates
Rejected
Conversion
Cost
Latency
Success Rate
```

---

## 95. AI Discovery Analytics

The platform shall measure:

```text
AI Discovery Jobs
Candidates Found
Candidates Accepted
Candidates Rejected
Human Corrections
AI Confidence
Human Agreement
False Positive Rate
False Negative Rate
Tool Success
Average Cost
Average Latency
```

---

## 96. Human Discovery Analytics

The platform shall measure:

```text
Searches
Research Tasks
Candidates Reviewed
Candidates Approved
Candidates Rejected
Corrections
Average Review Time
Verification Accuracy
Import Rate
```

---

## 97. Discovery Experimentation

Administrators shall be able to test:

```text
Discovery Strategy A vs B
AI Model A vs B
Provider A vs B
ICP Weight A vs B
Search Query A vs B
Human Review vs Automated Review
```

---

## 98. AI Model Versioning

Every AI discovery model shall maintain:

```text
Model ID
Model Version
Prompt Version
Tool Version
Input Schema
Output Schema
Evaluation Dataset
Quality Metrics
Published At
Approved By
```

---

## 99. Prompt Versioning

Discovery prompts shall support:

```text
DRAFT
TESTING
APPROVED
PUBLISHED
DEPRECATED
ROLLBACK
```

---

## 100. Structured AI Output

AI discovery results shall conform to strict schemas.

Example:

```json
{
  "company": {
    "name": "Example Corp",
    "domain": "example.com"
  },
  "match": {
    "icp_score": 0.94,
    "confidence": 0.91
  },
  "evidence": [],
  "classification": "observed"
}
```

Invalid outputs shall be rejected before persistence.

---

## 101. Discovery Evidence Graph

The system should maintain relationships such as:

```text
Company
 ├── Source
 ├── Industry
 ├── Technology
 ├── Contact
 ├── Funding
 ├── Hiring Signal
 ├── Intent Signal
 ├── ICP Match
 └── Discovery Job
```

This enables explainable prospect discovery.

---

## 102. Discovery History

The system shall preserve:

```text
Search Query
Filters
Sources
Results
Scores
AI Decisions
Human Decisions
Import Decisions
Timestamp
```

---

## 103. Search Reproducibility

Users shall be able to rerun a previous search using the stored:

```text
Query
Filters
ICP Version
Persona Version
Source Configuration
AI Strategy
```

Results may differ due to changing external data and shall therefore retain execution timestamps.

---

## 104. Discovery Notifications

Users may receive notifications for:

```text
New High-Fit Lead
High-Intent Lead
High-Value Account
New Executive Contact
New Funding Signal
New Hiring Signal
New Technology Signal
Discovery Job Completed
Discovery Job Failed
Human Review Required
```

---

## 105. Lead Assignment

Discovered leads may be automatically assigned based on:

```text
Territory
Industry
Company Size
Account Ownership
Sales Representative
Campaign
Round-Robin
Workload
Specialization
```

---

## 106. Lead Routing

Routing shall occur only after:

```text
Validation
Duplicate Detection
Suppression Check
Permission Check
Qualification Policy
```

---

## 107. Campaign Integration

Users shall be able to associate discovery jobs with:

```text
Campaign
Sales Sequence
Outreach Workflow
Sales Playbook
Territory
Product
Market Segment
```

---

## 108. Discovery Templates by Campaign

A campaign may define:

```text
Target Industry
Target Geography
Target Company Size
Target Persona
Target Technology
Target Intent
Target Revenue
Exclusions
Maximum Leads
Discovery Frequency
```

---

## 109. Discovery Quality Gate

A lead shall not enter the production lead pool unless configurable minimum criteria are met.

Example:

```text
Company Valid = TRUE
Duplicate = FALSE
Suppressed = FALSE
ICP Score >= Threshold
Confidence >= Threshold
Required Evidence = TRUE
```

---

## 110. Human Quality Gate

For configurable high-risk or high-value records:

```text
AI Discovery
    ↓
Human Verification
    ↓
Approval
    ↓
Lead Creation
```

---

## 111. Discovery Rejection Reasons

The system shall support standardized rejection reasons:

```text
Wrong Industry
Wrong Company Size
Wrong Geography
Wrong Persona
Duplicate
Invalid Company
Invalid Contact
Insufficient Evidence
Low ICP Fit
Existing Customer
Competitor
Suppressed
Out of Territory
Low Intent
Low Confidence
```

---

## 112. Feedback Loop

Humans shall be able to label discovery results:

```text
Correct
Incorrect
Relevant
Irrelevant
Duplicate
Wrong Entity
Wrong Persona
Wrong Industry
Insufficient Evidence
Outdated
```

---

## 113. AI Improvement Loop

```text
Discovery
 ↓
Human Feedback
 ↓
Evaluation Dataset
 ↓
Model / Prompt Evaluation
 ↓
Optimization
 ↓
Approval
 ↓
Production
```

Production behavior shall not change automatically without configured governance.

---

## 114. Discovery API

Core APIs shall include:

```text
POST /api/v1/lead-intelligence/discovery
GET  /api/v1/lead-intelligence/discovery/{job_id}
POST /api/v1/lead-intelligence/discovery/{job_id}/cancel
POST /api/v1/lead-intelligence/discovery/{job_id}/retry
GET  /api/v1/lead-intelligence/discovery/{job_id}/results
```

---

## 115. Company Discovery API

```text
POST /api/v1/lead-intelligence/companies/search
GET  /api/v1/lead-intelligence/companies/{company_id}
```

The existing SalesGenie implementation exposes `/api/v1/lead-intelligence/companies/search` and applies permission checks before executing tenant-scoped company queries.

---

## 116. Contact Discovery API

```text
POST /api/v1/lead-intelligence/contacts/search
GET  /api/v1/lead-intelligence/contacts/{contact_id}
```

---

## 117. AI Discovery APIs

```text
POST /api/v1/lead-intelligence/ai/discover
POST /api/v1/lead-intelligence/ai/research
POST /api/v1/lead-intelligence/ai/find-companies
POST /api/v1/lead-intelligence/ai/find-contacts
POST /api/v1/lead-intelligence/ai/find-similar
POST /api/v1/lead-intelligence/ai/find-lookalikes
POST /api/v1/lead-intelligence/ai/evaluate-icp
POST /api/v1/lead-intelligence/ai/recommend
```

---

## 118. Saved Search APIs

```text
POST   /api/v1/lead-intelligence/search-profiles
GET    /api/v1/lead-intelligence/search-profiles
GET    /api/v1/lead-intelligence/search-profiles/{id}
PUT    /api/v1/lead-intelligence/search-profiles/{id}
DELETE /api/v1/lead-intelligence/search-profiles/{id}
POST   /api/v1/lead-intelligence/search-profiles/{id}/execute
```

The existing lead-intelligence service already models `SearchProfile` and `SearchProfileDTO`, providing a natural extension point for persistent discovery profiles.

---

## 119. Discovery Import API

```text
POST /api/v1/lead-intelligence/discovery/{job_id}/import
POST /api/v1/lead-intelligence/discovery/{job_id}/import-selected
```

---

## 120. Verification APIs

```text
POST /api/v1/lead-intelligence/discovery/{candidate_id}/approve
POST /api/v1/lead-intelligence/discovery/{candidate_id}/reject
POST /api/v1/lead-intelligence/discovery/{candidate_id}/verify
POST /api/v1/lead-intelligence/discovery/{candidate_id}/request-research
```

---

## 121. Analytics APIs

```text
GET /api/v1/lead-intelligence/discovery/analytics
GET /api/v1/lead-intelligence/discovery/sources
GET /api/v1/lead-intelligence/discovery/performance
GET /api/v1/lead-intelligence/discovery/cost
```

---

## 122. Event-Driven Architecture

The system shall emit:

```text
lead.discovery.started
lead.discovery.completed
lead.discovery.failed
lead.discovery.partial

lead.candidate.found
lead.candidate.validated
lead.candidate.rejected
lead.candidate.approved

lead.duplicate.detected
lead.entity.resolved
lead.suppression.detected

lead.icp.matched
lead.icp.rejected
lead.intent.detected

lead.import.started
lead.import.completed
lead.import.failed

lead.human_review.required
lead.human_review.completed

lead.discovery.source_failed
lead.discovery.source_recovered
```

---

## 123. Security Requirements

Every discovery request shall validate:

```text
Authentication
Tenant
Organization
Workplace
Resource Ownership
Permission
Source Authorization
AI Authorization
Export Permission
```

Frontend restrictions shall never be treated as the security boundary.

SalesGenie's backend audit requirements explicitly require authentication, authorization, ownership, tenant/workspace boundaries, and idempotency to be enforced server-side.

---

## 124. Privacy Requirements

Lead discovery shall support:

```text
Data Minimization
Purpose Limitation
Consent / Lawful-Use Controls Where Required
Suppression
Retention
Deletion
Export Controls
Source Provenance
Third-Party Data Policies
```

SalesGenie's data-governance requirements call for provenance of external lead and market-intelligence data and controls over what third-party AI/data providers receive.

---

## 125. Data Governance

Every discovered lead shall maintain:

```text
Source
Source Type
Source Identifier
Discovered At
Last Verified
Discovery Query
Discovery Job
AI Model
AI Prompt Version
Confidence
Human Verification
```

---

## 126. Data Retention

Administrators shall configure retention for:

```text
Discovery Results
Search History
Research Results
AI Outputs
Source Evidence
Audit Logs
Rejected Candidates
Deleted Candidates
```

---

## 127. Deletion

Deletion shall propagate according to policy across:

```text
Lead Records
Search Index
Vector Store
AI Memory
Caches
Analytics
Discovery History
Research Data
```

---

## 128. Observability

The system shall expose:

```text
Discovery Request Rate
Discovery Latency
Search Latency
Provider Latency
AI Latency
Queue Latency
Candidates Per Job
Qualified Leads Per Job
Duplicate Rate
Failure Rate
Cost Per Job
Cost Per Lead
```

---

## 129. Reliability

The discovery platform shall support:

```text
Retries
Timeouts
Circuit Breakers
Provider Failover
Queue Recovery
Dead-Letter Queues
Partial Results
Graceful Degradation
Idempotency
Human Fallback
```

---

## 130. Performance

The system shall:

* Use indexed database queries.
* Avoid unbounded queries.
* Paginate large result sets.
* Cache repeated searches where appropriate.
* Execute long-running research asynchronously.
* Use connection pooling.
* Use queue backpressure.
* Support parallel discovery workers.
* Avoid duplicate provider calls.
* Limit AI tool execution.
* Limit expensive searches.

SalesGenie's performance audit specifically identifies unbounded queries, repeated API calls, blocking work, queue backpressure, retry storms, and synchronous long-running AI/enrichment/research jobs as critical concerns.

---

## 131. Scalability

The discovery system shall scale independently across:

```text
API Workers
Search Workers
AI Workers
Research Workers
Provider Workers
MCP Workers
Validation Workers
Scoring Workers
Import Workers
Analytics Workers
```

---

## 132. Testing Requirements

Testing shall include:

```text
Unit Tests
API Tests
Integration Tests
Database Tests
Search Tests
Provider Tests
MCP Tests
AI Evaluation Tests
Entity Resolution Tests
Duplicate Tests
Permission Tests
Tenant Isolation Tests
Load Tests
Failure Tests
End-to-End Tests
```

Critical scenarios shall include:

```text
Company Discovery
Contact Discovery
AI Discovery
Human Verification
Duplicate Discovery
Cross-Tenant Access
Provider Failure
AI Failure
MCP Failure
Large Batch Discovery
Repeated Discovery
Suppressed Lead
Existing Customer
Conflicting Sources
```

SalesGenie's test strategy requires negative tests for permission failures, provider failures, duplicate events, timeouts, retries, partial outages, and cross-tenant isolation.

---

## 133. AI Evaluation

AI discovery shall be evaluated for:

```text
Candidate Precision
Candidate Recall
ICP Accuracy
Persona Accuracy
Entity Resolution Accuracy
Duplicate Detection Accuracy
Evidence Groundedness
Source Selection Accuracy
Tool Selection Accuracy
Hallucination Rate
Human Acceptance Rate
Human Correction Rate
```

---

## 134. AI Regression Dataset

The evaluation dataset shall include:

```text
Simple Searches
Complex Searches
Ambiguous Queries
Incomplete Queries
Conflicting Data
Duplicate Companies
Duplicate Contacts
Similar Companies
Low-Information Companies
High-Value Accounts
Adversarial Inputs
Prompt Injection Attempts
Cross-Tenant Access Attempts
```

---

## 135. Agent Execution Controls

Each AI discovery job shall have configurable:

```text
Maximum Steps
Maximum Tool Calls
Maximum Search Depth
Maximum Tokens
Maximum Runtime
Maximum Cost
Maximum Results
Maximum Retries
```

---

## 136. Infinite Loop Protection

The system shall detect and stop:

```text
Recursive Discovery
Repeated Search
Repeated Provider Calls
Repeated MCP Calls
Repeated Candidate Processing
Recursive Agent Handoffs
Runaway Research
```

---

## 137. Human Approval for High-Impact Actions

Human approval shall be configurable before:

```text
Bulk Lead Import
Bulk CRM Update
Bulk Outreach
Sensitive Data Collection
Large External Data Purchases
Large Discovery Jobs
High-Cost AI Research
External Side Effects
```

---

## 138. Lead Discovery UX

The interface shall provide:

```text
Search
Filters
Natural Language Search
AI Suggestions
Results
Map / Geography
Company View
Contact View
Evidence
Confidence
ICP Score
Intent
Verification
Import
```

The frontend shall provide coherent loading, empty, error, retry, partial-data, filtering, pagination, and permission states rather than exposing disconnected dashboards.

---

## 139. Search Result Card

Each candidate should display:

```text
Company / Contact
Industry
Location
Employees
Revenue
Technology
ICP Score
Intent
Confidence
Source
Verification
Reason for Match
```

---

## 140. AI Discovery Result

AI results should display:

```text
Why Found
ICP Match
Potential Need
Relevant Signal
Evidence
Confidence
Recommended Action
```

---

## 141. Bulk Operations

Users shall be able to:

```text
Select All
Select Individual
Approve
Reject
Import
Enrich
Assign
Tag
Export
Add to Campaign
```

Bulk operations shall enforce permissions and approval policies.

---

## 142. Search Export

Authorized users shall be able to export discovery results in:

```text
CSV
JSON
Excel
API
```

Export shall respect:

```text
Tenant
Permission
Data Classification
Suppression
Privacy
Export Limits
Audit Policy
```

---

## 143. Discovery Audit Log

The system shall record:

```text
Search Created
Search Executed
AI Agent Executed
Provider Called
MCP Tool Called
Candidate Found
Candidate Rejected
Candidate Approved
Candidate Imported
Candidate Merged
Human Override
Bulk Operation
Export
```

Each event shall include:

```text
Event ID
Actor
Actor Type
Tenant
Organization
Workplace
Job ID
Candidate ID
Source
Tool
Decision
Timestamp
Latency
Cost
Approval State
```

---

## 144. Functional Requirements

## FR-001 — Create Discovery Job

The system shall allow an authorized user or authorized AI agent to create a discovery job.

## FR-002 — Define Search Criteria

The system shall support structured and natural-language search criteria.

## FR-003 — Execute Company Search

The system shall discover companies matching configured criteria.

## FR-004 — Execute Contact Search

The system shall discover contacts associated with target companies.

## FR-005 — Execute AI Search

The system shall interpret natural-language discovery requests.

## FR-006 — Execute Human Search

The system shall support manual search and filtering.

## FR-007 — Execute Hybrid Search

The system shall allow AI to generate candidates while humans review and approve them.

## FR-008 — Apply ICP

The system shall calculate configurable ICP fit.

## FR-009 — Apply Persona

The system shall identify potential target personas.

## FR-010 — Apply Intent

The system shall incorporate available intent signals.

## FR-011 — Apply Technology Filters

The system shall filter prospects based on technology criteria.

## FR-012 — Apply Geographic Filters

The system shall filter prospects geographically.

## FR-013 — Apply Company Filters

The system shall filter by employee count, revenue, industry, funding, and other firmographic attributes.

## FR-014 — Apply Exclusions

The system shall exclude customers, duplicates, competitors, suppressed entities, and other configured exclusions.

## FR-015 — Resolve Entities

The system shall resolve candidate identities before creating records.

## FR-016 — Detect Duplicates

The system shall detect duplicate candidates.

## FR-017 — Validate Candidates

The system shall validate candidate quality.

## FR-018 — Calculate Confidence

The system shall calculate field, entity, and overall confidence.

## FR-019 — Preserve Evidence

The system shall preserve discovery evidence and provenance.

## FR-020 — Request Human Review

The system shall route low-confidence or policy-sensitive candidates to human reviewers.

## FR-021 — Approve Candidate

Authorized humans shall approve candidates.

## FR-022 — Reject Candidate

Authorized humans shall reject candidates.

## FR-023 — Modify Candidate

Authorized users shall correct candidate data.

## FR-024 — Import Candidate

Authorized users shall import approved candidates.

## FR-025 — Bulk Import

Authorized users shall bulk-import approved candidates.

## FR-026 — Enrich Candidate

The system shall pass discovered candidates to lead enrichment.

## FR-027 — Qualify Candidate

The system shall pass discovered candidates to lead qualification.

## FR-028 — Score Candidate

The system shall calculate or request lead scoring.

## FR-029 — Route Candidate

The system shall route candidates to appropriate sales users.

## FR-030 — Add to Campaign

Users shall add discovered leads to campaigns.

## FR-031 — Add to Sales Sequence

Users shall add discovered leads to sales sequences.

## FR-032 — Generate Research

AI shall generate evidence-backed research summaries.

## FR-033 — Find Similar Companies

The system shall perform similarity-based discovery.

## FR-034 — Find Lookalikes

The system shall discover accounts similar to successful customers or deals.

## FR-035 — Find Competitors

The system shall discover competitive accounts where sufficient evidence exists.

## FR-036 — Discover Intent

The system shall identify configured intent signals.

## FR-037 — Discover Business Events

The system shall identify configured business events.

## FR-038 — Schedule Search

Users shall schedule recurring searches.

## FR-039 — Continuous Search

The system shall continuously discover new matching prospects.

## FR-040 — Deduplicate Results

The system shall avoid repeatedly producing the same candidate.

## FR-041 — Cache Results

The system shall cache eligible discovery results.

## FR-042 — Retry Failed Jobs

The system shall retry transient failures.

## FR-043 — Fail Over Providers

The system shall use configured fallback providers.

## FR-044 — Track Discovery Cost

The system shall meter discovery costs.

## FR-045 — Enforce Quotas

The system shall enforce tenant and user quotas.

## FR-046 — Enforce Permissions

The system shall enforce authorization on every discovery operation.

## FR-047 — Enforce Tenant Isolation

The system shall prevent cross-tenant discovery.

## FR-048 — Audit Operations

The system shall audit discovery operations.

## FR-049 — Support Natural-Language Search

The system shall translate natural-language requests into authorized structured discovery queries.

## FR-050 — Explain AI Decisions

The system shall provide evidence-backed explanations for AI discovery decisions.

## FR-051 — Prevent Unsupported Claims

The system shall prevent unsupported AI-generated facts from being persisted as verified data.

## FR-052 — Support AI Autonomy

Administrators shall configure AI discovery autonomy.

## FR-053 — Support Human Override

Authorized humans shall override AI discovery decisions.

## FR-054 — Collect Human Feedback

The system shall collect human labels and corrections.

## FR-055 — Evaluate AI

The system shall measure AI discovery quality.

## FR-056 — Version AI

The system shall version models, prompts, schemas, and tools.

## FR-057 — Monitor Agents

The system shall monitor AI agent execution.

## FR-058 — Control Agent Execution

The system shall enforce agent step, token, time, cost, and tool limits.

## FR-059 — Protect MCP

The system shall enforce MCP tool permissions and schemas.

## FR-060 — Prevent Prompt Injection

The system shall detect and mitigate indirect prompt injection through external discovery sources.

## FR-061 — Support Partial Results

The system shall preserve successful results when some sources fail.

## FR-062 — Support Recovery

The system shall recover interrupted discovery jobs.

## FR-063 — Support Reproducibility

The system shall preserve search criteria and execution metadata.

## FR-064 — Support Analytics

The system shall provide discovery performance analytics.

## FR-065 — Support Source Analytics

The system shall measure source performance.

## FR-066 — Support Human Analytics

The system shall measure human discovery and verification performance.

## FR-067 — Support AI Analytics

The system shall measure AI discovery accuracy and acceptance.

## FR-068 — Support Enterprise Governance

Administrators shall configure discovery policies, sources, quotas, approvals, and retention.

---

## 145. End-to-End AI Discovery Example

```text
User:
"Find 500 SaaS companies in the US with 200–2,000 employees,
using Salesforce, hiring engineers, and likely to need
customer-support automation."

AI:
1. Parse intent.
2. Generate structured criteria.
3. Validate permissions.
4. Check tenant ICP.
5. Select authorized sources.
6. Search company database.
7. Search authorized external providers.
8. Search technology signals.
9. Search hiring signals.
10. Identify customer-support signals.
11. Resolve companies.
12. Remove duplicates.
13. Validate records.
14. Calculate ICP score.
15. Calculate discovery confidence.
16. Rank candidates.
17. Present evidence.
18. Send low-confidence candidates to human review.
19. Import approved leads.
20. Trigger enrichment.
21. Trigger qualification.
22. Trigger lead scoring.
23. Route leads.
```

---

## 146. End-to-End Human Discovery Example

```text
Sales Representative
        ↓
Creates Search
        ↓
Selects:
Industry = SaaS
Employees = 200–2,000
Location = USA
Technology = Salesforce
        ↓
Runs Search
        ↓
Reviews Candidates
        ↓
Checks Evidence
        ↓
Rejects Duplicates
        ↓
Approves Candidates
        ↓
Imports Leads
        ↓
Enrichment
        ↓
Qualification
        ↓
Outreach
```

---

## 147. End-to-End Hybrid Discovery Example

```text
Human:
Defines ICP

AI:
Creates discovery strategy

AI:
Searches authorized sources

AI:
Finds 2,000 candidates

System:
Deduplicates

System:
Validates

AI:
Scores candidates

System:
Selects top 300

Human:
Reviews 50 low-confidence candidates

Human:
Approves 240

System:
Imports 240

Enrichment:
Completes missing data

Qualification:
Scores leads

Outreach:
Starts personalized sequence
```

---

## 148. Enterprise Acceptance Criteria

* [ ] Company discovery is supported.
* [ ] Contact discovery is supported.
* [ ] Account discovery is supported.
* [ ] Manual discovery is supported.
* [ ] AI discovery is supported.
* [ ] AI-assisted human discovery is supported.
* [ ] Human verification is supported.
* [ ] Hybrid discovery is supported.
* [ ] Natural-language discovery is supported.
* [ ] Structured discovery is supported.
* [ ] Boolean discovery is supported.
* [ ] Semantic discovery is supported.
* [ ] ICP-based discovery is supported.
* [ ] Persona-based discovery is supported.
* [ ] Firmographic discovery is supported.
* [ ] Technographic discovery is supported.
* [ ] Geographic discovery is supported.
* [ ] Industry discovery is supported.
* [ ] Keyword discovery is supported.
* [ ] Intent-based discovery is supported.
* [ ] Funding-based discovery is supported.
* [ ] Hiring-based discovery is supported.
* [ ] Business-signal discovery is supported.
* [ ] Competitor-based discovery is supported.
* [ ] Similar-company discovery is supported.
* [ ] Lookalike discovery is supported.
* [ ] Account-based discovery is supported.
* [ ] Territory-based discovery is supported.
* [ ] Campaign-based discovery is supported.
* [ ] Saved searches are supported.
* [ ] Scheduled searches are supported.
* [ ] Continuous discovery is supported.
* [ ] Event-driven discovery is supported.
* [ ] Existing customers can be excluded.
* [ ] Suppression lists are enforced.
* [ ] Duplicate detection is implemented.
* [ ] Entity resolution is implemented.
* [ ] Candidate validation is implemented.
* [ ] ICP scoring is implemented.
* [ ] Confidence scoring is implemented.
* [ ] Evidence is preserved.
* [ ] Source provenance is preserved.
* [ ] Observed and inferred information is separated.
* [ ] AI-generated unsupported claims are rejected.
* [ ] Human review is supported.
* [ ] Human override is supported.
* [ ] AI autonomy is configurable.
* [ ] AI agents operate under least privilege.
* [ ] MCP tools are permission-controlled.
* [ ] MCP inputs and outputs are schema-validated.
* [ ] Prompt injection protections are implemented.
* [ ] Agent execution budgets are enforced.
* [ ] Infinite agent loops are prevented.
* [ ] Provider failover is supported.
* [ ] Discovery jobs support retries.
* [ ] Discovery jobs support partial completion.
* [ ] Discovery jobs are idempotent.
* [ ] Long-running discovery is asynchronous.
* [ ] Discovery cost is tracked.
* [ ] Provider cost is tracked.
* [ ] AI token usage is tracked.
* [ ] Tenant quotas are enforced.
* [ ] Rate limiting is implemented.
* [ ] Search caching is implemented where appropriate.
* [ ] Cross-tenant access is prevented.
* [ ] Backend authorization is authoritative.
* [ ] Discovery history is preserved.
* [ ] Search execution is reproducible.
* [ ] Discovery results can be imported.
* [ ] Discovery integrates with lead enrichment.
* [ ] Discovery integrates with lead qualification.
* [ ] Discovery integrates with lead scoring.
* [ ] Discovery integrates with lead routing.
* [ ] Discovery integrates with sales sequences.
* [ ] Discovery integrates with outreach automation.
* [ ] Discovery integrates with CRM.
* [ ] Discovery analytics are available.
* [ ] Source performance is measurable.
* [ ] AI discovery accuracy is measurable.
* [ ] Human verification performance is measurable.
* [ ] Human feedback is captured.
* [ ] AI evaluation datasets are maintained.
* [ ] AI model versions are tracked.
* [ ] Prompt versions are tracked.
* [ ] Tool versions are tracked.
* [ ] Discovery operations are auditable.
* [ ] High-impact actions can require human approval.
* [ ] Data retention policies are configurable.
* [ ] Data deletion policies are enforced.
* [ ] Export permissions are enforced.
* [ ] Privacy and lawful-use policies are enforceable.
* [ ] Discovery evidence is traceable.
* [ ] High-value prospects can be prioritized.
* [ ] The discovery engine can operate continuously.
* [ ] The discovery engine can recover from provider failures.
* [ ] The discovery engine can scale horizontally.
* [ ] The discovery engine provides deterministic fallback behavior when AI is unavailable.
* [ ] The discovery engine integrates into the complete SalesGenie prospect-to-revenue lifecycle.
