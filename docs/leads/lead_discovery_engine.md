# SalesGenie — FAANG-Level Lead Discovery Engine

## User Requirements, System Requirements & Functional Requirements

**Module:** `lead_discovery_engine.md`
**Platform:** SalesGenie Enterprise AI Sales & Revenue Intelligence Platform
**Processing Model:** AI-Based + Human-Assisted
**Architecture:** Multi-Tenant, Event-Driven, Microservices, Agentic AI
**Requirement Level:** Enterprise / FAANG-Level
**Version:** 1.0

---

## 1. Purpose

The Lead Discovery Engine shall be the specialized prospect-discovery subsystem of SalesGenie responsible for identifying previously unknown or insufficiently known companies, accounts, contacts, buying committees, and prospect opportunities from authorized internal and external data sources.

The engine shall transform:

```text
Business Objective
        +
ICP
        +
Market Criteria
        +
Search Intent
        +
Target Accounts
        +
Business Signals
        +
Authorized Data Sources
        ↓
AI + Human Discovery
        ↓
Candidate Prospects
        ↓
Evidence
        ↓
Confidence
        ↓
Discovery Results
```

The Lead Discovery Engine is responsible for **finding prospects**. Downstream modules shall perform enrichment, verification, qualification, scoring, segmentation, routing, assignment, nurturing, outreach, and opportunity management.

The architecture shall therefore maintain a clean domain boundary between discovery and downstream lead intelligence services. SalesGenie's existing lead-intelligence architecture already separates company discovery/search from later lead processing and applies tenant-scoped access and lead-read permissions to company search.  

---

## 2. Business Objective

The engine shall optimize for:

```text
Relevant Prospects
        ×
Discovery Accuracy
        ×
ICP Alignment
        ×
Freshness
        ×
Evidence Quality
        ×
Coverage
        ÷
Discovery Cost
```

The system shall not optimize merely for the largest number of discovered records.

The primary objective shall be:

> Discover the highest-value, highest-relevance prospect candidates with sufficient evidence and provenance while minimizing false positives, duplicate discovery, unnecessary provider usage, AI cost, and human effort.

---

## 3. Scope

## 3.1 In Scope

```text
ICP interpretation
Natural-language prospect discovery
Structured prospect discovery
Company discovery
Contact discovery
Account discovery
Buying-committee discovery
Market discovery
Geographic discovery
Industry discovery
Technology discovery
Competitor-related discovery
Intent-signal discovery
Event-triggered discovery
Search-query generation
Search-query expansion
Multi-source discovery
Source orchestration
Source ranking
Result normalization
Entity resolution
Candidate deduplication
Evidence collection
Confidence estimation
Human review
AI-assisted discovery
AI-autonomous discovery
Discovery campaigns
Scheduled discovery
Continuous discovery
Discovery analytics
Discovery cost management
Discovery auditability
```

## 3.2 Out of Scope

The discovery engine shall not directly own:

```text
Final lead qualification
Final lead scoring
Sales outreach
Email sending
Message delivery
Opportunity creation
Deal management
Billing
Payment processing
Customer support
```

Those capabilities shall be delegated to their respective SalesGenie modules.

---

## 4. Discovery Lifecycle

```text
Discovery Objective
        ↓
ICP / Target Definition
        ↓
Discovery Strategy
        ↓
Source Planning
        ↓
Query Planning
        ↓
Source Search
        ↓
Candidate Extraction
        ↓
Candidate Normalization
        ↓
Entity Resolution
        ↓
Duplicate Detection
        ↓
Evidence Collection
        ↓
Confidence Estimation
        ↓
Relevance Filtering
        ↓
Human / AI Review
        ↓
Discovery Result
        ↓
Downstream Lead Pipeline
```

---

## 5. Primary Actors

| Actor              | Responsibility                     |
| ------------------ | ---------------------------------- |
| Super Admin        | Platform-wide governance           |
| Organization Admin | Organization discovery policies    |
| Workplace Admin    | Workplace discovery configuration  |
| Sales Manager      | Discovery campaigns and strategy   |
| SDR / BDR          | Prospect discovery                 |
| Sales Agent        | Prospect research                  |
| Marketing Manager  | Market discovery                   |
| RevOps Manager     | Discovery governance and analytics |
| Data Analyst       | Discovery analysis                 |
| Compliance Manager | Data-use governance                |
| AI Discovery Agent | Autonomous discovery               |
| AI Research Agent  | Prospect research                  |
| Human Reviewer     | Candidate validation               |
| System Scheduler   | Automated discovery execution      |

---

## 6. User Requirements

## UR-001 — Create Discovery Campaign

Users shall be able to create a discovery campaign containing:

```text
Campaign Name
Objective
ICP
Target Market
Geography
Industry
Company Size
Revenue
Technology
Job Titles
Seniority
Business Events
Intent Signals
Target Accounts
Excluded Accounts
Excluded Contacts
Data Sources
Discovery Strategy
Result Limit
Confidence Threshold
Review Policy
Schedule
Budget
```

---

## UR-002 — Natural-Language Discovery

Users shall be able to describe their desired prospects in natural language.

Example:

```text
Find US-based B2B SaaS companies with
50–500 employees that recently raised funding,
are hiring engineers, and may need AI customer
support automation.
```

The AI shall convert the request into structured discovery criteria.

---

## UR-003 — Structured Discovery

Users shall be able to define discovery criteria through:

```text
Filters
Rules
Boolean Conditions
Ranges
Tags
Segments
Saved Searches
ICP Profiles
```

---

## UR-004 — Company Discovery

Users shall be able to discover previously unknown companies matching their criteria.

---

## UR-005 — Contact Discovery

Users shall be able to discover contacts associated with target companies.

---

## UR-006 — Account Discovery

Users shall be able to discover target accounts based on business characteristics.

---

## UR-007 — Buying Committee Discovery

The system shall identify potential members of a buying committee.

Supported roles:

```text
Economic Buyer
Decision Maker
Technical Buyer
Champion
Influencer
End User
Procurement
Executive Sponsor
Potential Blocker
```

---

## UR-008 — Market Discovery

Users shall be able to discover companies within a market.

---

## UR-009 — Industry Discovery

Users shall be able to discover companies by industry and sub-industry.

---

## UR-010 — Geographic Discovery

Users shall be able to discover prospects by:

```text
Country
Region
State / Province
City
Postal Area
Sales Territory
Market
```

---

## UR-011 — Firmographic Discovery

Users shall be able to filter companies by:

```text
Employee Count
Revenue
Funding
Growth
Company Age
Business Model
Industry
Location
```

---

## UR-012 — Technographic Discovery

Users shall be able to discover companies based on technologies they use.

Examples:

```text
CRM
Cloud Provider
Analytics Platform
Marketing Platform
Customer Support Platform
Programming Stack
AI Platform
E-Commerce Platform
```

---

## UR-013 — Event-Based Discovery

Users shall be able to discover companies experiencing relevant business events.

Examples:

```text
Funding
Hiring
Expansion
Acquisition
Leadership Change
Product Launch
Technology Adoption
New Office
Market Entry
Partnership
```

---

## UR-014 — Intent-Based Discovery

Users shall be able to discover prospects showing relevant intent signals.

---

## UR-015 — Competitor-Based Discovery

Users shall be able to discover prospects associated with competitor technologies or business categories where the configured data source legally and technically supports the signal.

---

## UR-016 — Target Account Discovery

Users shall be able to provide a list of strategic accounts and discover relevant contacts inside those accounts.

---

## UR-017 — Lookalike Discovery

Users shall be able to provide successful customers or accounts and ask the engine to discover similar prospects.

---

## UR-018 — Natural-Language Refinement

Users shall be able to refine an active search conversationally.

Example:

```text
User:
Find SaaS companies in the US.

AI:
Found 10,000 candidates.

User:
Only keep companies with 100–500 employees
and recent funding.

AI:
Updated discovery criteria.
```

---

## UR-019 — Search Preview

Users shall be able to preview:

```text
Estimated Result Count
Sources
Estimated Cost
Estimated Runtime
Expected Confidence
Expected Coverage
```

before execution.

---

## UR-020 — Discovery Dry Run

Users shall be able to execute a discovery plan without persisting results.

---

## UR-021 — Result Limit

Users shall be able to specify maximum candidate count.

---

## UR-022 — Minimum Confidence

Users shall be able to configure a minimum discovery-confidence threshold.

---

## UR-023 — Source Selection

Users shall be able to select authorized discovery sources.

---

## UR-024 — Source Priority

Users shall be able to specify preferred source priority.

---

## UR-025 — Source Exclusion

Users shall be able to exclude specific sources.

---

## UR-026 — Discovery Schedule

Users shall be able to schedule discovery:

```text
One-Time
Hourly
Daily
Weekly
Monthly
Custom Schedule
Event Triggered
Continuous
```

---

## UR-027 — Saved Discovery

Users shall be able to save discovery criteria as reusable searches.

---

## UR-028 — Discovery Templates

The system shall provide reusable discovery templates such as:

```text
B2B SaaS Prospecting
Enterprise Account Discovery
Startup Discovery
Funding-Based Discovery
Hiring-Based Discovery
Technology-Based Discovery
Competitor Lookalike Discovery
Geographic Expansion Discovery
ABM Discovery
```

---

## UR-029 — Human Review

Users shall be able to review candidate prospects before downstream processing.

---

## UR-030 — Human Approval

Organizations shall be able to require approval for discovered candidates.

---

## UR-031 — Human Rejection

Users shall be able to reject irrelevant candidates.

---

## UR-032 — Human Correction

Users shall be able to correct discovery metadata.

---

## UR-033 — Human Feedback

Users shall be able to provide feedback such as:

```text
Relevant
Irrelevant
Wrong Company
Wrong Contact
Duplicate
Insufficient Evidence
Out of ICP
High Value
Low Value
```

---

## UR-034 — AI Autonomous Discovery

Authorized users shall be able to allow AI agents to execute discovery autonomously.

---

## UR-035 — Hybrid Discovery

Users shall be able to configure:

```text
AI Discovery
    ↓
Human Review
    ↓
AI Research
    ↓
Human Approval
```

---

## UR-036 — Discovery Dashboard

Users shall be able to monitor:

```text
Candidates Discovered
Unique Companies
Unique Contacts
Discovery Accuracy
Confidence Distribution
Source Distribution
Discovery Cost
Human Review Queue
Accepted Candidates
Rejected Candidates
```

---

## 7. AI-Based User Requirements

## AI-UR-001 — AI Objective Interpretation

The AI shall transform natural-language discovery objectives into structured discovery plans.

---

## AI-UR-002 — AI ICP Interpretation

The AI shall interpret:

```text
Industry
Company Size
Geography
Revenue
Technology
Job Role
Seniority
Intent
Events
Business Model
```

---

## AI-UR-003 — AI Query Generation

The AI shall generate search queries optimized for the selected sources.

---

## AI-UR-004 — AI Query Expansion

The AI shall expand:

```text
Synonyms
Industry Terms
Technology Names
Job Titles
Company Categories
Related Concepts
```

---

## AI-UR-005 — AI Query Refinement

The AI shall evaluate result quality and refine queries when results are:

```text
Too Broad
Too Narrow
Low Quality
Highly Duplicated
Low Confidence
Outside ICP
```

---

## AI-UR-006 — AI Source Selection

AI shall recommend sources based on:

```text
Coverage
Quality
Freshness
Historical Performance
Cost
Availability
```

---

## AI-UR-007 — AI Source Failover

AI orchestration shall be able to select alternative authorized sources when a preferred source fails.

---

## AI-UR-008 — AI Company Discovery

AI shall identify candidate companies matching discovery criteria.

---

## AI-UR-009 — AI Contact Discovery

AI shall identify relevant contacts associated with discovered companies.

---

## AI-UR-010 — AI Buying Committee Discovery

AI shall infer likely buying-committee roles from authorized evidence.

---

## AI-UR-011 — AI Lookalike Discovery

AI shall derive common characteristics from successful accounts and use them to identify similar prospects.

---

## AI-UR-012 — AI Market Expansion

When explicitly authorized, AI shall identify adjacent markets that may contain relevant prospects.

---

## AI-UR-013 — AI Signal Detection

AI shall identify relevant business signals from authorized data.

---

## AI-UR-014 — AI Relevance Classification

Each candidate shall receive a relevance classification:

```text
HIGHLY_RELEVANT
RELEVANT
UNCERTAIN
LOW_RELEVANCE
IRRELEVANT
```

---

## AI-UR-015 — AI Confidence

The engine shall produce a confidence estimate for discovery decisions.

---

## AI-UR-016 — Explainable Discovery

AI shall explain why a candidate was discovered.

Example:

```text
Why discovered:

- Industry matches SaaS
- Employee count matches target
- Recent funding detected
- Engineering hiring detected
- Target geography matched
```

---

## AI-UR-017 — Evidence-Based Discovery

AI shall preserve evidence for important discovery claims.

---

## AI-UR-018 — Fact / Inference Separation

AI shall distinguish:

```text
Verified Fact
Observed Signal
Inference
Prediction
Recommendation
Unknown
```

SalesGenie's AI governance requirements explicitly call for separating facts, retrieved evidence, assumptions, inference, and predictions in AI outputs.

---

## AI-UR-019 — AI Candidate Ranking

AI shall rank candidates according to configured discovery objectives.

---

## AI-UR-020 — AI Search Optimization

AI shall optimize discovery strategies using historical campaign outcomes.

---

## AI-UR-021 — AI Discovery Feedback Loop

AI shall learn from:

```text
Human Approvals
Human Rejections
Duplicate Detection
Qualification Outcomes
Opportunity Creation
Conversion
Revenue
```

---

## AI-UR-022 — AI Human Escalation

AI shall request human review when:

```text
Confidence is Low
Evidence Conflicts
Candidate Value is High
Data is Ambiguous
Compliance Risk Exists
Identity is Uncertain
```

---

## AI-UR-023 — AI Hallucination Prevention

AI shall not fabricate:

```text
Company
Person
Job Title
Technology
Funding
Business Event
Contact Information
Evidence
```

---

## AI-UR-024 — AI Tool Safety

AI-generated tool parameters shall be validated against strict schemas before execution. SalesGenie's agent-security requirements explicitly require strict tool input/output validation and prohibit unauthorized tool access, privilege escalation, cross-tenant access, and secret exposure.

---

## 8. Human-Based User Requirements

## HUMAN-UR-001 — Manual Search

Users shall be able to manually search for companies and contacts.

---

## HUMAN-UR-002 — Manual Candidate Creation

Users shall be able to manually create discovery candidates.

---

## HUMAN-UR-003 — Human Research

Users shall be able to investigate candidates using authorized sources.

---

## HUMAN-UR-004 — Human Evidence Addition

Users shall be able to attach evidence to discovery results.

---

## HUMAN-UR-005 — Human Validation

Users shall be able to validate AI-generated discovery results.

---

## HUMAN-UR-006 — Human Rejection

Users shall be able to reject false positives.

---

## HUMAN-UR-007 — Human Override

Authorized users shall be able to override AI relevance and confidence classifications.

---

## HUMAN-UR-008 — Human Search Strategy

Experienced users shall be able to manually define discovery queries.

---

## HUMAN-UR-009 — Human Source Control

Authorized users shall be able to select or exclude discovery sources.

---

## HUMAN-UR-010 — Human Review Queue

The system shall provide a prioritized review queue.

---

## HUMAN-UR-011 — Human Escalation

Users shall be able to escalate uncertain candidates.

---

## HUMAN-UR-012 — Human-to-AI Handoff

Users shall be able to send selected candidates to AI research workflows.

---

## HUMAN-UR-013 — AI-to-Human Handoff

AI shall be able to submit uncertain or high-value candidates for human review.

---

## 9. System Requirements

## SR-001 — Multi-Tenant Architecture

Every discovery operation shall be tenant-scoped.

Required context:

```text
tenant_id
organization_id
workplace_id
user_id
campaign_id
discovery_job_id
```

---

## SR-002 — Tenant Isolation

No tenant shall access another tenant's discovery candidates, source results, queries, evidence, or search history.

---

## SR-003 — Organization Isolation

Organization-level access boundaries shall be enforced.

---

## SR-004 — Workplace Isolation

Workplace boundaries shall be enforced where configured.

---

## SR-005 — RBAC

The discovery engine shall integrate with centralized SalesGenie RBAC.

---

## SR-006 — Fine-Grained Permissions

Recommended permissions:

```text
lead_discovery.view
lead_discovery.search
lead_discovery.create
lead_discovery.execute
lead_discovery.pause
lead_discovery.cancel
lead_discovery.configure
lead_discovery.review
lead_discovery.approve
lead_discovery.reject
lead_discovery.export
lead_discovery.sources.read
lead_discovery.sources.configure
lead_discovery.ai_execute
lead_discovery.ai_override
lead_discovery.analytics
lead_discovery.audit
```

---

## SR-007 — Agent Permissions

Every AI discovery agent shall operate under least-privilege permissions.

---

## SR-008 — Tool Permissions

Each discovery tool shall define:

```text
Read
Write
High-Risk Write
Destructive
Financial
```

permissions.

---

## SR-009 — Source Authorization

Only explicitly authorized discovery providers may be queried.

---

## SR-010 — Provenance

Every externally derived discovery attribute shall preserve provenance metadata.

---

## SR-011 — Evidence

Discovery claims shall maintain evidence references where supported.

---

## SR-012 — Data Freshness

The system shall record:

```text
source_timestamp
retrieved_at
observed_at
freshness_status
expires_at
```

---

## SR-013 — Asynchronous Execution

Long-running discovery operations shall execute asynchronously.

SalesGenie's production audit requirements explicitly identify research, enrichment, and AI workloads as operations that should run asynchronously, with queue backpressure and job prioritization.

---

## SR-014 — Job Queue

The engine shall use distributed job queues for large discovery workloads.

---

## SR-015 — Job States

```text
DRAFT
VALIDATING
QUEUED
RUNNING
PAUSED
COMPLETED
PARTIALLY_COMPLETED
FAILED
CANCELLED
```

---

## SR-016 — Idempotency

Repeated discovery requests shall not create duplicate discovery jobs or duplicate candidate records.

---

## SR-017 — Retry

Transient provider and infrastructure failures shall support controlled retries.

---

## SR-018 — Dead Letter Queue

Repeatedly failed discovery jobs shall be routed to a dead-letter workflow.

---

## SR-019 — Circuit Breakers

Provider failures shall trigger circuit-breaker behavior.

---

## SR-020 — Rate Limiting

The engine shall enforce:

```text
Tenant Rate Limits
Organization Limits
User Limits
Campaign Limits
Provider Limits
Agent Limits
```

---

## SR-021 — Provider Quotas

Provider-specific quotas shall be tracked independently.

---

## SR-022 — Concurrency Control

Concurrent discovery jobs shall not create inconsistent candidate state.

---

## SR-023 — Distributed Locking

Distributed locking shall be used for critical operations such as:

```text
Candidate Merge
Entity Resolution
Duplicate Suppression
Quota Allocation
Campaign Execution
```

---

## 10. Functional Requirements — Discovery Engine

## FR-001 — Create Discovery Job

The system shall create a discovery job from validated criteria.

---

## FR-002 — Validate Discovery Request

The system shall validate:

```text
Authentication
Authorization
Tenant
ICP
Filters
Sources
Quota
Budget
Result Limit
Schedule
Policy
```

---

## FR-003 — Discovery Plan Generation

The system shall construct an executable discovery plan.

```text
Objective
 ↓
ICP
 ↓
Search Strategy
 ↓
Sources
 ↓
Queries
 ↓
Execution
 ↓
Candidate Processing
 ↓
Evidence
 ↓
Review
```

---

## FR-004 — Discovery Preview

The system shall estimate:

```text
Potential Results
Source Coverage
Expected Cost
Expected Runtime
Potential Duplicates
Expected Confidence
```

---

## FR-005 — Discovery Dry Run

The system shall execute discovery without persisting candidates.

---

## FR-006 — Execute Discovery

The system shall execute an approved discovery plan.

---

## FR-007 — Pause Discovery

Authorized users shall be able to pause a running job.

---

## FR-008 — Resume Discovery

Paused jobs shall resume from the last safe checkpoint.

---

## FR-009 — Cancel Discovery

Authorized users shall be able to cancel discovery jobs.

---

## 11. Query Planning Engine

## FR-010 — Query Generation

The system shall generate source-specific queries.

---

## FR-011 — Boolean Search

The engine shall support:

```text
AND
OR
NOT
()
Exact Match
Wildcards where supported
```

---

## FR-012 — Query Expansion

The engine shall support semantic query expansion.

---

## FR-013 — Query Decomposition

Complex discovery requests shall be decomposed into smaller searches.

Example:

```text
Target Market
 ├── Industry Search
 ├── Geography Search
 ├── Technology Search
 ├── Funding Search
 ├── Hiring Search
 └── Decision-Maker Search
```

---

## FR-014 — Query Deduplication

Equivalent search queries shall be detected and consolidated.

---

## FR-015 — Query Performance Tracking

The system shall track:

```text
Query
Source
Result Count
Relevant Results
Precision
Cost
Latency
```

---

## 12. Source Orchestration

## FR-016 — Multi-Source Discovery

The engine shall query multiple authorized sources.

---

## FR-017 — Source Adapter Interface

Every source shall implement a normalized adapter interface.

```text
search()
lookup_company()
lookup_contact()
get_signals()
get_metadata()
health_check()
```

---

## FR-018 — Source Normalization

Provider-specific schemas shall be transformed into canonical SalesGenie discovery objects.

---

## FR-019 — Source Ranking

Sources shall be ranked based on:

```text
Accuracy
Coverage
Freshness
Historical Precision
Cost
Latency
Availability
```

---

## FR-020 — Source Failover

The system shall automatically switch to configured fallback providers when allowed.

---

## FR-021 — Source Health

The system shall monitor:

```text
Availability
Latency
Error Rate
Quota
Cost
Result Quality
```

---

## 13. Company Discovery

## FR-022 — Company Search

The system shall support company discovery by:

```text
Industry
Location
Employees
Revenue
Keywords
Technologies
Funding
Business Model
Growth
Events
Intent
```

SalesGenie's current lead-intelligence implementation already exposes company search parameters including industry, location, employee range, revenue, technologies, keywords, and response language.

---

## FR-023 — Company Candidate

A discovered company shall contain at minimum:

```text
Candidate ID
Company Name
Domain if available
Source
Discovery Query
Discovery Timestamp
Confidence
Evidence
```

---

## FR-024 — Company Identity Resolution

The system shall resolve multiple records referring to the same organization.

---

## FR-025 — Company Domain Resolution

Domains shall be normalized.

---

## 14. Contact Discovery

## FR-026 — Contact Search

The system shall support contact discovery by:

```text
Name
Job Title
Department
Seniority
Company
Location
Professional Role
Technology Expertise
```

---

## FR-027 — Contact-to-Company Association

Every discovered contact shall be associated with the best-known company entity.

---

## FR-028 — Contact Identity Resolution

The engine shall identify probable duplicate contact identities.

---

## FR-029 — Buying Committee Mapping

The engine shall map discovered contacts to potential buying roles.

---

## 15. Account-Based Discovery

## FR-030 — Strategic Account Discovery

Users shall be able to provide target account lists.

---

## FR-031 — Account Expansion

The engine shall identify:

```text
Departments
Executives
Decision Makers
Technical Buyers
Champions
Influencers
Procurement
```

within target accounts.

---

## FR-032 — Account Coverage

The system shall calculate account-contact coverage.

Example:

```text
Account
 ├── Executive
 ├── Economic Buyer
 ├── Technical Buyer
 ├── Champion
 └── Procurement
```

---

## 16. Lookalike Discovery

## FR-033 — Reference Account Selection

Users shall be able to select successful customers or target accounts.

---

## FR-034 — Feature Extraction

AI shall identify meaningful characteristics from reference accounts.

---

## FR-035 — Lookalike Candidate Generation

The engine shall search for organizations sharing those characteristics.

---

## FR-036 — Similarity Explanation

The system shall explain why each lookalike candidate was selected.

---

## 17. Event Discovery

The system shall support discovery from:

```text
Funding
Hiring
Leadership Change
Expansion
Acquisition
Partnership
Product Launch
Technology Adoption
Market Expansion
```

---

## 18. Intent Discovery

The system shall detect configurable intent signals.

Intent evidence shall contain:

```text
Signal
Source
Timestamp
Confidence
Evidence
```

---

## 19. Candidate Normalization

The system shall normalize:

```text
Company Names
Domains
Names
Job Titles
Locations
Industries
Technology Names
Phone Formats
Email Formats
Dates
Currencies
```

---

## 20. Entity Resolution

The system shall resolve entities using a combination of:

```text
Exact Matching
Normalized Matching
Domain Matching
External IDs
Semantic Similarity
AI Reasoning
Human Review
```

---

## 21. Duplicate Discovery Prevention

The engine shall detect:

```text
Exact Duplicate
Probable Duplicate
Potential Duplicate
Existing CRM Entity
Existing Lead
Existing Account
Existing Contact
```

before creating a new candidate.

---

## 22. Discovery Candidate States

```text
DISCOVERED
NORMALIZED
RESOLVED
DUPLICATE
UNDER_REVIEW
APPROVED
REJECTED
EXPIRED
SUPPRESSED
PROMOTED_TO_LEAD
```

---

## 23. Evidence Engine

Every important discovery result should contain:

```text
Source
Source Record
URL / Reference where permitted
Observation
Timestamp
Evidence Type
Confidence
```

---

## 24. Evidence Classification

Evidence shall be classified as:

```text
DIRECT
INDIRECT
DERIVED
INFERRED
HUMAN_VALIDATED
AI_INFERRED
```

---

## 25. Confidence Engine

The engine shall calculate discovery confidence using configurable factors:

```text
Source Reliability
Evidence Strength
Entity Match Quality
ICP Match
Data Freshness
Cross-Source Agreement
AI Confidence
Human Validation
```

---

## 26. Candidate Relevance

The system shall classify candidates based on discovery objective:

```text
HIGH
MEDIUM
LOW
UNKNOWN
```

---

## 27. Human Review Engine

The system shall provide a review queue containing:

```text
Candidate
Discovery Reason
Evidence
Sources
Confidence
AI Recommendation
Potential Issues
Recommended Action
```

---

## 28. Review Actions

Humans shall be able to:

```text
Approve
Reject
Merge
Split
Correct
Request More Evidence
Send to AI Research
Promote to Lead
Suppress
```

---

## 29. AI-to-Human Workflow

```text
AI Discovery
      ↓
Confidence Evaluation
      ↓
Policy Evaluation
      ↓
Automatic Approval?
   /          \
 YES           NO
 ↓              ↓
Continue     Human Queue
                ↓
           Human Review
            /       \
       Approve      Reject
          ↓            ↓
     Downstream      Suppress
```

---

## 30. Human-to-AI Workflow

```text
Human Candidate
      ↓
AI Research Request
      ↓
AI Evidence Collection
      ↓
AI Analysis
      ↓
Human Review
      ↓
Approved Discovery Result
```

---

## 31. AI Agent Architecture

The engine shall support specialized agents:

```text
DiscoveryPlannerAgent
QueryGenerationAgent
SourceSelectionAgent
CompanyDiscoveryAgent
ContactDiscoveryAgent
AccountDiscoveryAgent
LookalikeDiscoveryAgent
SignalDiscoveryAgent
EvidenceAgent
EntityResolutionAgent
CandidateClassificationAgent
DiscoveryOptimizationAgent
```

---

## 32. Agent Tool Permissions

Example:

```text
DiscoveryPlannerAgent
├── read_icp
├── read_campaign
└── create_discovery_plan

QueryGenerationAgent
├── read_discovery_plan
└── generate_query

CompanyDiscoveryAgent
├── search_company
├── lookup_company
└── read_source_metadata

EvidenceAgent
├── retrieve_source
├── extract_evidence
└── attach_evidence

EntityResolutionAgent
├── read_candidate
├── search_existing_entities
└── propose_merge
```

No agent shall receive broader privileges than required.

---

## 33. Agent Execution Controls

Each AI discovery job shall enforce:

```text
Maximum Steps
Maximum Runtime
Maximum Tokens
Maximum Tool Calls
Maximum Provider Calls
Maximum Candidates
Maximum Cost
Maximum Retries
```

SalesGenie's agent-safety requirements explicitly call for execution budgets covering steps, time, tokens, retries, and tool calls, as well as safeguards against loops, duplicate actions, and runaway costs.

---

## 34. Prompt Injection Protection

External source content shall be treated as untrusted data.

The discovery engine shall prevent external content from:

```text
Changing System Instructions
Changing Agent Permissions
Executing Unauthorized Tools
Exfiltrating Secrets
Crossing Tenant Boundaries
Changing Discovery Policies
```

---

## 35. Discovery API

Conceptual API surface:

```http
POST   /api/v1/lead-discovery
GET    /api/v1/lead-discovery
GET    /api/v1/lead-discovery/{job_id}

POST   /api/v1/lead-discovery/{job_id}/preview
POST   /api/v1/lead-discovery/{job_id}/dry-run
POST   /api/v1/lead-discovery/{job_id}/start
POST   /api/v1/lead-discovery/{job_id}/pause
POST   /api/v1/lead-discovery/{job_id}/resume
POST   /api/v1/lead-discovery/{job_id}/cancel

GET    /api/v1/lead-discovery/{job_id}/status
GET    /api/v1/lead-discovery/{job_id}/results

POST   /api/v1/lead-discovery/companies/search
POST   /api/v1/lead-discovery/contacts/search
POST   /api/v1/lead-discovery/accounts/search
POST   /api/v1/lead-discovery/lookalike
POST   /api/v1/lead-discovery/events/search
POST   /api/v1/lead-discovery/intent/search

GET    /api/v1/lead-discovery/sources
GET    /api/v1/lead-discovery/source-health
GET    /api/v1/lead-discovery/analytics
GET    /api/v1/lead-discovery/cost
```

---

## 36. Discovery Job Data Model

```text
DiscoveryJob
├── id
├── tenant_id
├── organization_id
├── workplace_id
├── campaign_id
├── created_by
├── discovery_mode
├── discovery_strategy
├── objective
├── icp_id
├── target_criteria
├── excluded_criteria
├── sources
├── query_plan
├── confidence_threshold
├── result_limit
├── budget
├── schedule
├── approval_policy
├── status
├── progress
├── estimated_cost
├── actual_cost
├── error_state
├── created_at
├── started_at
├── completed_at
└── updated_at
```

---

## 37. Discovery Candidate Data Model

```text
DiscoveryCandidate
├── id
├── tenant_id
├── organization_id
├── workplace_id
├── discovery_job_id
├── candidate_type
├── company_id
├── contact_id
├── source
├── source_record_id
├── source_timestamp
├── discovered_at
├── relevance
├── confidence
├── evidence
├── discovery_reason
├── entity_resolution_status
├── duplicate_status
├── review_status
├── lifecycle_status
├── promoted_lead_id
└── updated_at
```

---

## 38. Discovery Evidence Model

```text
DiscoveryEvidence
├── id
├── candidate_id
├── source
├── source_record_id
├── evidence_type
├── claim
├── observation
├── timestamp
├── confidence
├── reference
├── collected_by
├── model_version
└── created_at
```

---

## 39. AI Discovery Decision Model

```text
AIDiscoveryDecision
├── id
├── candidate_id
├── agent_id
├── decision_type
├── input_context
├── recommendation
├── confidence
├── evidence
├── model
├── model_version
├── prompt_version
├── policy_version
├── human_review_required
├── human_decision
├── override_reason
├── executed_action
└── created_at
```

---

## 40. Discovery Modes

The engine shall support:

```text
MANUAL
RULE_BASED
AI_ASSISTED
AI_AUTONOMOUS
HYBRID
SCHEDULED
EVENT_TRIGGERED
CONTINUOUS
```

---

## 41. Continuous Discovery

The system shall support always-on discovery:

```text
Monitor Market
      ↓
Detect New Candidate
      ↓
Evaluate ICP
      ↓
Collect Evidence
      ↓
Estimate Confidence
      ↓
Deduplicate
      ↓
Review if Required
      ↓
Promote
```

---

## 42. Continuous Discovery Guardrails

Continuous discovery shall enforce:

```text
Maximum Daily Candidates
Maximum Provider Calls
Maximum AI Cost
Minimum Confidence
Source Restrictions
Suppression Rules
Human Review Rules
```

---

## 43. Discovery Triggers

Supported triggers shall include:

```text
New Funding
New Hiring Activity
New Executive
Technology Adoption
Product Launch
Expansion
Acquisition
Market Entry
New Target Account
New ICP
New Customer
Competitor Event
Webhook
CRM Event
Scheduled Event
```

---

## 44. Existing CRM Matching

Before promoting a candidate to a lead, the engine shall check:

```text
Existing Contact
Existing Account
Existing Lead
Existing Opportunity
Existing Deal
Existing Customer
Suppression List
```

SalesGenie's broader business-logic requirements explicitly require duplicate handling and validation of lead lifecycle transitions from discovery through CRM, outreach, opportunity, customer, retention, and upsell.

---

## 45. Promotion to Lead

A discovery candidate may be promoted only when configured conditions are satisfied.

Example:

```text
Candidate
 +
Minimum Confidence
 +
Required Evidence
 +
No Duplicate
 +
No Suppression
 +
ICP Match
 +
Human Approval if Required
        ↓
Lead
```

---

## 46. Suppression

The discovery engine shall suppress candidates matching:

```text
Opt-Out
Existing Customer
Existing Contact
Existing Opportunity
Blocked Company
Blocked Domain
Blocked Region
Compliance Policy
Organization Suppression List
```

---

## 47. Data Freshness

The system shall classify candidate freshness:

```text
FRESH
RECENT
AGING
STALE
EXPIRED
UNKNOWN
```

---

## 48. Discovery Quality Metrics

The system shall measure:

```text
Discovery Precision
Discovery Recall
Relevant Candidate Rate
False Positive Rate
Duplicate Rate
Evidence Coverage
Confidence Accuracy
Source Accuracy
Human Acceptance Rate
Lead Promotion Rate
```

---

## 49. Source Performance

Each source shall be evaluated using:

```text
Candidate Volume
Unique Candidate Rate
Relevant Candidate Rate
Verification Rate
Duplicate Rate
Promotion Rate
Opportunity Rate
Revenue
Cost
Latency
```

---

## 50. Query Performance

The system shall track:

```text
Query Precision
Result Count
Relevant Result Count
Duplicate Results
Cost
Latency
Provider
Conversion to Lead
```

---

## 51. Discovery Analytics

The dashboard shall provide:

```text
Total Candidates
Unique Companies
Unique Contacts
New Accounts
New Contacts
High-Confidence Candidates
Low-Confidence Candidates
Human Review
Approved
Rejected
Duplicates
Suppressed
Promoted
```

---

## 52. AI Analytics

The platform shall report:

```text
AI Discovery Volume
AI Precision
AI Recall
AI Confidence
Human Acceptance
Human Override
AI Error Rate
AI Tool Failure
AI Latency
AI Cost
```

---

## 53. Human Analytics

The platform shall report:

```text
Review Queue
Candidates Reviewed
Approval Rate
Rejection Rate
Override Rate
Average Review Time
SLA Compliance
Promotion Rate
```

---

## 54. Discovery Cost Management

The engine shall track:

```text
Provider API Calls
Search Calls
Research Calls
LLM Calls
Token Usage
Embedding Usage
Reranking Usage
Agent Runtime
Storage
```

SalesGenie's platform-level cost requirements specifically call for tracking LLMs, embeddings, reranking, search/data providers, MCP providers, queues, compute, and tenant-level usage.

---

## 55. Cost Optimization

The engine shall optimize:

```text
Caching
Query Reuse
Provider Selection
Model Selection
Prompt Size
Context Size
Result Deduplication
Early Termination
Batching
```

---

## 56. Discovery Budget

Each discovery campaign shall optionally enforce:

```text
Maximum Cost
Maximum API Calls
Maximum AI Tokens
Maximum Candidates
Maximum Runtime
```

---

## 57. Security Requirements

The engine shall enforce:

```text
Authentication
Authorization
RBAC
Tenant Isolation
Organization Isolation
Workplace Isolation
Encryption
Secret Management
Rate Limiting
Input Validation
Output Validation
Audit Logging
```

---

## 58. Data Governance

The engine shall maintain:

```text
Data Classification
Source Provenance
Data Ownership
Retention Policy
Deletion Policy
Suppression Policy
Third-Party Sharing Policy
Regional Policy
```

SalesGenie's data-governance requirements call for inventories of lead and customer data, provenance for external lead/market intelligence, retention/deletion controls, and minimization of data sent to third-party providers.

---

## 59. Privacy Controls

The system shall support:

```text
Data Retention
Data Deletion
Data Export
Suppression
Anonymization
Consent Tracking
Regional Restrictions
```

---

## 60. Audit Requirements

The system shall audit:

```text
Discovery Job Created
Discovery Job Modified
Discovery Job Started
Discovery Job Paused
Discovery Job Cancelled
Discovery Job Completed

Query Created
Query Executed
Source Accessed
Candidate Discovered
Candidate Merged
Candidate Rejected
Candidate Approved
Candidate Promoted

AI Decision
AI Tool Call
AI Recommendation
Human Review
Human Override

Data Export
Data Deletion
Suppression
```

Every AI tool invocation shall capture actor, tenant, tool, redacted parameters, result, latency, decision, and approval state.

---

## 61. Event Model

The system shall publish events including:

```text
DiscoveryJobCreated
DiscoveryJobStarted
DiscoveryJobPaused
DiscoveryJobResumed
DiscoveryJobCompleted
DiscoveryJobFailed

QueryGenerated
QueryExecuted
SourceSelected
SourceFailed

CompanyDiscovered
ContactDiscovered
AccountDiscovered
CandidateCreated
CandidateResolved
CandidateDeduplicated
CandidateEvidenceAdded
CandidateClassified
CandidateApproved
CandidateRejected
CandidateSuppressed
CandidatePromoted

AIResearchStarted
AIResearchCompleted
AIDecisionCreated
AIReviewRequested

HumanReviewStarted
HumanApproved
HumanRejected
HumanOverrideCreated
```

---

## 62. Event-Driven Architecture

```text
Discovery Request
      ↓
API / Gateway
      ↓
Discovery Orchestrator
      ↓
Message Broker
      ↓
Discovery Workers
      ├── Query Worker
      ├── Source Worker
      ├── Company Worker
      ├── Contact Worker
      ├── Evidence Worker
      ├── Resolution Worker
      └── Classification Worker
      ↓
Candidate Store
      ↓
Event Bus
      ↓
Lead Intelligence Pipeline
```

---

## 63. Reliability Requirements

The engine shall support:

```text
Retry
Timeout
Circuit Breaker
Provider Failover
Dead-Letter Queue
Checkpointing
Job Recovery
Idempotency
Backpressure
Graceful Degradation
```

SalesGenie's production audit specifically requires resilience when AI providers, integrations, databases, queues, or services fail.

---

## 64. Graceful Degradation

If AI is unavailable:

```text
AI Discovery
     ↓
Rule-Based Discovery
     ↓
Previously Validated Search Strategies
     ↓
Human Review
```

If an external provider is unavailable:

```text
Primary Source
     ↓
Fallback Source
     ↓
Cached Data
     ↓
Partial Result
```

---

## 65. Performance Requirements

Recommended targets:

```text
Search API P95              < 500 ms
Saved Search Retrieval P95  < 200 ms
Candidate Lookup P95        < 200 ms
Query Planning P95          < 2 sec
Standard Discovery          < 10 sec
AI Discovery                < 30 sec
Large Discovery Jobs        Asynchronous
```

---

## 66. Scalability Requirements

The system shall support:

```text
10M+ Leads
Millions of Companies
Millions of Contacts
Millions of Discovery Candidates
Thousands of Concurrent Discovery Jobs
Thousands of Organizations
Continuous Discovery
Large Bulk Searches
High-Volume Event Processing
```

The architecture shall scale horizontally.

---

## 67. Caching

The system shall cache:

```text
Repeated Queries
Source Metadata
Stable Company Data
Stable Technology Data
Discovery Plans
AI Classifications
Provider Responses
```

Cache invalidation shall respect data freshness policies.

---

## 68. Pagination

All large discovery result sets shall support cursor-based pagination.

---

## 69. Search Filtering

Users shall be able to filter results by:

```text
Industry
Location
Employee Count
Revenue
Technology
Funding
Intent
Confidence
Source
Discovery Date
Freshness
Candidate Type
```

---

## 70. Search Sorting

Supported sorting shall include:

```text
Relevance
Confidence
Freshness
Company Size
Revenue
Intent
Discovery Date
Source Quality
```

---

## 71. Search Facets

The UI shall support aggregated facets for:

```text
Industry
Geography
Company Size
Technology
Source
Confidence
Intent
Business Event
```

---

## 72. Bulk Operations

Users shall be able to:

```text
Select Candidates
Approve
Reject
Suppress
Merge
Promote
Export
Send to AI
Assign Review
```

Bulk destructive or externally consequential operations shall respect approval policies.

---

## 73. Discovery Export

Authorized users shall be able to export discovery results.

Supported formats may include:

```text
CSV
JSON
XLSX
API
CRM Sync
```

Export operations shall be permission-controlled and audited.

---

## 74. API Contract

Every API shall provide:

```text
Request Validation
Response Schema
Pagination
Filtering
Sorting
Authentication
Authorization
Rate Limits
Error Contract
Idempotency
API Version
```

SalesGenie's API audit requirements explicitly require request/response validation, pagination, filtering, consistent error formats, authorization, object ownership checks, idempotency, concurrency protection, timeouts, retries, and API versioning.

---

## 75. Error Model

Errors shall be categorized:

```text
INVALID_REQUEST
UNAUTHORIZED
FORBIDDEN
TENANT_ACCESS_DENIED
SOURCE_UNAVAILABLE
SOURCE_RATE_LIMITED
QUERY_FAILED
AI_FAILURE
TIMEOUT
QUOTA_EXCEEDED
BUDGET_EXCEEDED
DUPLICATE
CONFLICT
INTERNAL_ERROR
```

---

## 76. Observability

The engine shall expose:

```text
Metrics
Logs
Distributed Traces
Events
Health Checks
Provider Health
Queue Health
AI Health
Database Health
```

---

## 77. Operational Metrics

The system shall monitor:

```text
Discovery Throughput
Discovery Latency
Query Latency
Provider Latency
Queue Depth
Job Failure Rate
Candidate Rate
Duplicate Rate
Source Failure Rate
AI Error Rate
AI Latency
AI Cost
Human Review Queue
```

---

## 78. AI Evaluation

AI discovery shall be evaluated using:

```text
Discovery Precision
Discovery Recall
Entity Resolution Accuracy
Relevance Accuracy
Evidence Accuracy
Confidence Calibration
Tool Accuracy
Human Acceptance
False Positive Rate
```

SalesGenie's AI evaluation requirements call for measurable datasets and metrics covering retrieval quality, correctness, groundedness, tool accuracy, refusal behavior, and agent success.

---

## 79. AI Regression Testing

Every significant change to:

```text
Prompt
Model
Tool
Agent
Source Adapter
Discovery Policy
Ranking Logic
```

shall trigger relevant AI evaluation tests.

---

## 80. Automated Testing

The discovery engine shall include:

```text
Unit Tests
Integration Tests
API Tests
Database Tests
Worker Tests
End-to-End Tests
AI Evaluation Tests
Security Tests
Tenant Isolation Tests
Load Tests
Failure Tests
```

SalesGenie's testing requirements explicitly include negative tests for invalid inputs, permission failures, provider failures, duplicate events, timeouts, retries, partial outages, and cross-tenant isolation.

---

## 81. Failure Scenarios

The engine shall safely handle:

```text
Provider Timeout
Provider Rate Limit
Provider Authentication Failure
AI Timeout
AI Hallucination
AI Low Confidence
Database Failure
Queue Failure
Duplicate Event
Repeated Request
Network Failure
Partial Source Failure
Malformed Source Data
Conflicting Source Data
Tenant Deletion
User Deletion
Campaign Cancellation
Budget Exhaustion
Quota Exhaustion
```

---

## 82. Discovery Strategy Optimization

The engine shall compare historical strategies:

```text
Strategy A
Strategy B
Strategy C
```

using:

```text
Relevant Candidates
Lead Promotion
Opportunity Creation
Conversion
Revenue
Cost
```

---

## 83. Experimentation

The system shall support controlled experiments across:

```text
Discovery Query
Source
ICP
Search Strategy
AI Model
Prompt
Ranking Strategy
Candidate Threshold
```

---

## 84. A/B Testing

Each experiment shall contain:

```text
Experiment ID
Control
Variant
Traffic Allocation
Success Metric
Start Time
End Time
Sample Size
Result
Winner
```

---

## 85. Discovery Dashboard

```text
Lead Discovery
├── Active Searches
├── Completed Searches
├── Candidates Found
├── Unique Companies
├── Unique Contacts
└── Discovery Rate

Quality
├── Relevance
├── Confidence
├── Duplicate Rate
├── Evidence Coverage
└── Promotion Rate

Sources
├── Source Volume
├── Source Quality
├── Source Accuracy
├── Source Cost
└── Source Availability

AI
├── AI Candidates
├── AI Accuracy
├── AI Confidence
├── Human Override
└── AI Cost

Human
├── Review Queue
├── Approval Rate
├── Rejection Rate
├── Review SLA
└── Override Rate
```

---

## 86. End-to-End Example

```text
User:

Find 2,000 US SaaS companies with
100–1,000 employees that recently raised funding,
are hiring software engineers, and may need
enterprise AI automation.

        ↓

AI parses objective

        ↓

Creates structured discovery plan

        ↓

Identifies:
- Industry
- Geography
- Employee range
- Funding signal
- Hiring signal
- Business need

        ↓

Selects authorized sources

        ↓

Generates source-specific queries

        ↓

Executes searches

        ↓

Collects candidate companies

        ↓

Normalizes company records

        ↓

Resolves company identities

        ↓

Removes duplicate candidates

        ↓

Collects supporting evidence

        ↓

Detects funding events

        ↓

Detects hiring signals

        ↓

Evaluates ICP relevance

        ↓

Calculates confidence

        ↓

Ranks candidates

        ↓

Human review if required

        ↓

Approved candidates

        ↓

Promote to Lead Intelligence Engine

        ↓

Enrichment

        ↓

Verification

        ↓

Qualification

        ↓

Scoring

        ↓

Routing

        ↓

Sales Execution
```

---

## 87. Reference Architecture

```text
                         ┌─────────────────────────┐
                         │       SalesGenie UI     │
                         │ Human + AI Workspace    │
                         └────────────┬────────────┘
                                      │
                                      ↓
                         ┌─────────────────────────┐
                         │ API Gateway / Control   │
                         │ Plane                   │
                         └────────────┬────────────┘
                                      │
                                      ↓
                    ┌──────────────────────────────────┐
                    │ Lead Discovery Orchestrator      │
                    └────────────────┬─────────────────┘
                                     │
             ┌───────────────────────┼──────────────────────┐
             ↓                       ↓                      ↓
      ┌─────────────┐        ┌──────────────┐       ┌─────────────┐
      │ ICP Engine  │        │ Query Engine │       │ Rule Engine │
      └──────┬──────┘        └──────┬───────┘       └──────┬──────┘
             └──────────────────────┼───────────────────────┘
                                    ↓
                         ┌─────────────────────────┐
                         │ AI Agent Orchestrator   │
                         └────────────┬────────────┘
                                      │
        ┌──────────────┬─────────────┼──────────────┬──────────────┐
        ↓              ↓             ↓              ↓              ↓
   Discovery       Query         Company        Contact        Evidence
     Agent         Agent        Agent          Agent           Agent
        │              │             │              │              │
        └──────────────┴─────────────┼──────────────┴──────────────┘
                                     ↓
                         ┌─────────────────────────┐
                         │ Source Orchestrator     │
                         └────────────┬────────────┘
                                      │
             ┌────────────────────────┼────────────────────────┐
             ↓                        ↓                        ↓
      ┌─────────────┐         ┌─────────────┐          ┌─────────────┐
      │ Provider A  │         │ Provider B  │          │ Provider C  │
      └─────────────┘         └─────────────┘          └─────────────┘
             │                        │                        │
             └────────────────────────┼────────────────────────┘
                                      ↓
                         ┌─────────────────────────┐
                         │ Normalization Engine    │
                         └────────────┬────────────┘
                                      ↓
                         ┌─────────────────────────┐
                         │ Entity Resolution       │
                         └────────────┬────────────┘
                                      ↓
                         ┌─────────────────────────┐
                         │ Candidate Deduplication │
                         └────────────┬────────────┘
                                      ↓
                         ┌─────────────────────────┐
                         │ Evidence & Confidence   │
                         └────────────┬────────────┘
                                      ↓
                         ┌─────────────────────────┐
                         │ Human Review / Approval │
                         └────────────┬────────────┘
                                      ↓
                         ┌─────────────────────────┐
                         │ Discovery Candidate     │
                         │ Store                   │
                         └────────────┬────────────┘
                                      ↓
                         ┌─────────────────────────┐
                         │ Lead Intelligence       │
                         │ Pipeline                │
                         └─────────────────────────┘
```

---

## 88. Security Boundary

```text
User
 ↓
Authentication
 ↓
Authorization
 ↓
Tenant Context
 ↓
Discovery Policy
 ↓
Agent Permission
 ↓
Tool Permission
 ↓
Source Permission
 ↓
Query Execution
 ↓
Candidate Processing
```

No layer may bypass the previous authorization boundary.

---

## 89. AI Governance Boundary

```text
AI Agent
 ↓
Policy Check
 ↓
Permission Check
 ↓
Tool Schema Validation
 ↓
Execution Budget
 ↓
Tool Execution
 ↓
Untrusted Result Sanitization
 ↓
Evidence Extraction
 ↓
AI Decision
 ↓
Confidence
 ↓
Human Approval if Required
```

---

## 90. Ultimate Discovery Optimization Loop

```text
DEFINE OBJECTIVE
       ↓
INTERPRET ICP
       ↓
PLAN SEARCH
       ↓
SELECT SOURCES
       ↓
GENERATE QUERIES
       ↓
DISCOVER
       ↓
NORMALIZE
       ↓
RESOLVE
       ↓
DEDUPLICATE
       ↓
COLLECT EVIDENCE
       ↓
CLASSIFY
       ↓
CALCULATE CONFIDENCE
       ↓
HUMAN REVIEW
       ↓
PROMOTE
       ↓
MEASURE
       ↓
LEARN
       ↓
OPTIMIZE
       ↓
DISCOVER BETTER PROSPECTS
       ↺
```

---

## 91. Acceptance Criteria

* [ ] Users can create discovery campaigns.
* [ ] Users can define ICP-based discovery.
* [ ] Users can use natural-language discovery.
* [ ] Users can use structured discovery.
* [ ] Users can discover companies.
* [ ] Users can discover contacts.
* [ ] Users can discover accounts.
* [ ] Users can discover buying committees.
* [ ] Users can perform geographic discovery.
* [ ] Users can perform industry discovery.
* [ ] Users can perform firmographic discovery.
* [ ] Users can perform technographic discovery.
* [ ] Users can perform funding-based discovery.
* [ ] Users can perform hiring-based discovery.
* [ ] Users can perform event-based discovery.
* [ ] Users can perform intent-based discovery.
* [ ] Users can perform competitor-related discovery where authorized.
* [ ] Users can perform lookalike discovery.
* [ ] Users can save searches.
* [ ] Users can schedule searches.
* [ ] Users can execute continuous discovery.
* [ ] Users can preview discovery results.
* [ ] Users can execute dry runs.
* [ ] Users can select data sources.
* [ ] Users can exclude data sources.
* [ ] AI can interpret natural-language discovery objectives.
* [ ] AI can generate discovery queries.
* [ ] AI can expand queries.
* [ ] AI can refine poor queries.
* [ ] AI can select authorized sources.
* [ ] AI can perform company discovery.
* [ ] AI can perform contact discovery.
* [ ] AI can identify buying-committee candidates.
* [ ] AI can perform lookalike discovery.
* [ ] AI can identify relevant business signals.
* [ ] AI can classify candidate relevance.
* [ ] AI provides confidence scores.
* [ ] AI provides discovery explanations.
* [ ] Important AI claims preserve evidence.
* [ ] AI distinguishes facts from inference.
* [ ] AI cannot fabricate discovery evidence.
* [ ] AI cannot bypass permissions.
* [ ] AI cannot cross tenant boundaries.
* [ ] AI tool parameters are schema validated.
* [ ] AI execution budgets are enforced.
* [ ] Prompt-injection protections are implemented.
* [ ] Human review queues work.
* [ ] Human approval works.
* [ ] Human rejection works.
* [ ] Human correction works.
* [ ] Human override works.
* [ ] AI-to-human handoff works.
* [ ] Human-to-AI handoff works.
* [ ] Company entity resolution works.
* [ ] Contact entity resolution works.
* [ ] Duplicate detection works.
* [ ] Evidence provenance works.
* [ ] Freshness tracking works.
* [ ] Candidate confidence works.
* [ ] Existing CRM matching works.
* [ ] Suppression rules work.
* [ ] Promotion to lead works.
* [ ] Multi-tenant isolation works.
* [ ] Organization isolation works.
* [ ] Workplace isolation works.
* [ ] RBAC works.
* [ ] Fine-grained permissions work.
* [ ] Discovery jobs execute asynchronously.
* [ ] Discovery jobs support pause/resume/cancel.
* [ ] Discovery jobs support retries.
* [ ] Dead-letter handling works.
* [ ] Idempotency works.
* [ ] Rate limits work.
* [ ] Provider failover works.
* [ ] Circuit breakers work.
* [ ] Backpressure works.
* [ ] Discovery cost is tracked.
* [ ] AI cost is tracked.
* [ ] Provider cost is tracked.
* [ ] Campaign budgets are enforced.
* [ ] Discovery analytics work.
* [ ] Source analytics work.
* [ ] AI analytics work.
* [ ] Human review analytics work.
* [ ] Revenue attribution can be linked downstream.
* [ ] Audit logs capture discovery actions.
* [ ] AI decisions are auditable.
* [ ] Tool calls are auditable.
* [ ] Human overrides are auditable.
* [ ] Data retention policies are enforced.
* [ ] Data deletion policies are enforced.
* [ ] Export permissions are enforced.
* [ ] Discovery APIs are documented.
* [ ] API contracts are validated.
* [ ] Failure scenarios are tested.
* [ ] Cross-tenant isolation is tested.
* [ ] AI regression tests are implemented.
* [ ] Load testing covers large discovery workloads.
* [ ] The system scales horizontally.
* [ ] Large discovery jobs do not block synchronous APIs.
* [ ] Discovery results can be promoted into the Lead Intelligence pipeline.

---

## 92. FAANG-Level Success Definition

The SalesGenie Lead Discovery Engine shall provide a **continuously improving, evidence-driven, multi-source, AI-assisted and human-governed prospect discovery system**.

Its primary optimization target shall be:

```text
Discovery Quality
        ×
ICP Relevance
        ×
Evidence Strength
        ×
Freshness
        ×
Coverage
        ×
Downstream Conversion
        ÷
Discovery Cost
```

The engine shall function as a dedicated discovery layer rather than conflating prospect discovery with enrichment, qualification, scoring, or sales execution.

It shall be:

```text
Scalable
Multi-Tenant
Secure
Observable
Explainable
Evidence-Based
Cost-Aware
Fault-Tolerant
AI-Assisted
Human-Governed
Event-Driven
API-First
```

and capable of continuously discovering high-value prospects while preserving tenant isolation, authorization, provenance, data governance, AI safety, operational reliability, and downstream sales-system integrity.
