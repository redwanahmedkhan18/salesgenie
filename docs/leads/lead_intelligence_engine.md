# SalesGenie — Lead Intelligence Engine

## FAANG-Level User Requirements, System Requirements & Functional Requirements

> **Module:** Lead Intelligence Engine  
> **Product:** SalesGenie  
> **Architecture:** Enterprise SaaS + Multi-Tenant + AI-Assisted + Human-in-the-Loop + Event-Driven Microservices  
> **Primary Service:** `lead-intelligence-service`  
> **API Prefix:** `/api/v1/lead-intelligence`  
> **Current Service Port:** `8022`  
> **AI Capability:** Lead discovery, company intelligence, contact intelligence, enrichment, qualification, research, scoring, recommendations, and outreach assistance.

---

## 1. Executive Objective

The SalesGenie Lead Intelligence Engine shall transform fragmented company, contact, behavioral, technological, financial, growth, and market information into actionable sales intelligence.

The system shall combine:

- AI-based lead discovery
- Company intelligence
- Contact intelligence
- Lead enrichment
- AI lead scoring
- ICP matching
- Decision-maker identification
- Buying-signal detection
- Growth-signal analysis
- Technology-stack intelligence
- Funding and financial intelligence
- Business research
- Qualification analysis
- Opportunity assessment
- Recommended sales strategy
- AI-generated outreach recommendations
- Human review and approval
- CRM synchronization
- Multi-tenant data isolation
- Explainable AI
- Confidence scoring
- Provenance tracking
- Continuous intelligence refresh
- Event-driven intelligence updates

The engine shall not merely return a list of companies. It shall answer:

1. **Who should we target?**
2. **Why should we target them?**
3. **Who should we contact?**
4. **How valuable is this account?**
5. **How likely are they to buy?**
6. **What signals indicate buying intent?**
7. **What problems are they likely experiencing?**
8. **What solution should SalesGenie recommend?**
9. **What evidence supports the recommendation?**
10. **What should the salesperson do next?**
11. **What should AI do automatically?**
12. **What requires human approval?**

---

## 2. Product Scope

## 2.1 Core Intelligence Domains

The engine shall support:

- Company intelligence
- Contact intelligence
- Firmographic intelligence
- Technographic intelligence
- Financial intelligence
- Growth intelligence
- Funding intelligence
- Hiring intelligence
- Market intelligence
- News intelligence
- Social intelligence
- Digital presence intelligence
- Behavioral intelligence
- Intent intelligence
- ICP intelligence
- Sales-fit intelligence
- Opportunity intelligence
- Competitive intelligence
- Outreach intelligence

---

## 3. User Personas

## 3.1 Super Admin

The Super Admin shall:

- Configure platform-wide intelligence policies.
- Manage AI providers.
- Configure data-provider integrations.
- Configure global intelligence policies.
- Monitor intelligence-service health.
- Monitor AI usage and cost.
- Configure platform-level quotas.
- Review audit events.
- Manage global feature flags.
- Configure system-wide security controls.

---

## 3.2 Organization Admin

The Organization Admin shall:

- Configure organizational ICPs.
- Configure scoring rules.
- Configure qualification criteria.
- Manage organization-level lead intelligence settings.
- Configure enrichment policies.
- Manage team access.
- Configure AI autonomy levels.
- Review intelligence usage.
- Review team performance.

---

## 3.3 Workplace Admin

The Workplace Admin shall:

- Configure workplace-level sales policies.
- Manage sales teams.
- Configure lead ownership.
- Configure intelligence workflows.
- Configure approval policies.
- Monitor lead intelligence activity.

---

## 3.4 Sales Manager

The Sales Manager shall:

- Define ICPs.
- Create lead-search profiles.
- Review AI-generated lead lists.
- Review AI scores.
- Review qualification reports.
- Analyze sales opportunities.
- Approve AI-generated outreach.
- Monitor sales-agent activity.
- Configure team-level scoring policies.

---

## 3.5 Sales Agent

The Sales Agent shall:

- Search for target companies.
- Review company intelligence.
- Review contacts.
- View AI lead scores.
- View qualification reports.
- View buying signals.
- View opportunity assessments.
- Request AI research.
- Generate outreach drafts.
- Modify AI recommendations.
- Approve outreach.
- Add leads to CRM.
- Assign leads.
- Create opportunities.

---

## 3.6 AI Sales Agent

The AI Sales Agent shall:

- Discover potential accounts.
- Enrich company records.
- Enrich contacts.
- Analyze ICP fit.
- Calculate lead scores.
- Detect buying signals.
- Generate research briefs.
- Recommend sales strategies.
- Recommend contacts.
- Generate outreach drafts.
- Recommend next actions.
- Monitor changes.
- Trigger approved workflows.

The AI agent shall never bypass authorization, tenant isolation, approval policies, or tool permissions.

---

## 3.7 End User / Client

The End User shall:

- Access permitted lead intelligence.
- Review recommended companies.
- Review relevant contacts.
- View intelligence reports.
- Configure permitted search profiles.
- Review AI recommendations.
- Approve permitted actions.

---

## 4. User Requirements

## UR-001 — Company Discovery

The system shall allow users to discover companies based on:

- Industry
- Location
- Country
- State
- City
- Employee count
- Revenue
- Technology
- Keywords
- Funding stage
- Growth signals
- Business characteristics
- ICP attributes
- Custom filters

---

## UR-002 — Intelligent Search

Users shall be able to perform natural-language searches such as:

> "Find SaaS companies in the United States with 100–1000 employees using Salesforce and showing rapid growth."

The AI shall translate natural-language intent into structured search criteria.

---

## UR-003 — Advanced Filtering

Users shall be able to combine multiple filters using:

- AND
- OR
- NOT
- Range conditions
- Exact matching
- Partial matching
- Semantic matching
- AI-generated conditions

---

## UR-004 — Company Intelligence

Users shall receive a consolidated company intelligence profile containing:

- Company name
- Domain
- Industry
- Description
- Employee count
- Estimated revenue
- Location
- Country
- Technology stack
- Funding stage
- Funding amount
- Growth signals
- News mentions
- Website
- LinkedIn
- Social profiles
- Data sources
- Confidence score
- Last enrichment time

---

## UR-005 — Contact Intelligence

Users shall be able to identify relevant contacts within a company.

The system shall provide:

- Full name
- Job title
- Department
- Seniority
- Email
- Phone
- Decision-maker status
- Decision influence
- Company relationship
- Contact confidence
- Data provenance

---

## UR-006 — Decision-Maker Detection

AI shall identify likely:

- Economic buyers
- Decision makers
- Champions
- Influencers
- Technical evaluators
- Procurement stakeholders
- Executives

The system shall provide an explainable reason for each classification.

---

## UR-007 — AI Lead Scoring

The system shall automatically calculate lead scores based on configurable criteria.

Scoring may consider:

- Company size
- Industry fit
- Revenue fit
- Geographic fit
- Technology fit
- Funding
- Growth
- Decision-maker availability
- Business need
- Buying intent
- Engagement
- Strategic relevance
- Data confidence

---

## UR-008 — Explainable Lead Score

Users shall be able to understand why a lead received its score.

The system shall show:

- Positive factors
- Negative factors
- Missing information
- Evidence
- Confidence
- Score components
- Model/version used
- Timestamp
- Recommended action

---

## UR-009 — ICP Matching

Users shall define an Ideal Customer Profile.

The AI shall determine:

- ICP match percentage
- Strong matches
- Weak matches
- Missing attributes
- Contradictory attributes
- Recommended priority

---

## UR-010 — Buying Intent Intelligence

The system shall identify potential buying signals from permitted data sources.

Signals may include:

- Hiring growth
- Funding events
- Product launches
- Technology adoption
- Technology replacement
- Executive changes
- Expansion
- Website activity
- Relevant news
- Market changes
- Business growth
- Job postings
- Public announcements

---

## UR-011 — Growth Intelligence

The system shall identify indicators of company growth.

Examples:

- Employee growth
- Funding
- Expansion
- New offices
- Hiring
- New products
- Market expansion
- Partnerships
- Increased technology adoption

---

## UR-012 — Technology Intelligence

The system shall identify technologies used by a company where legally and technically permitted.

The system shall support:

- Technology detection
- Technology categories
- Technology confidence
- Technology changes
- Technology adoption signals
- Technology replacement opportunities

---

## UR-013 — AI Research Brief

Users shall be able to request an AI-generated company research brief.

The report shall include:

- Company overview
- Business model
- Industry
- Products
- Target customers
- Growth indicators
- Technology profile
- Potential business challenges
- Potential SalesGenie use cases
- Opportunity assessment
- Recommended pitch
- Recommended contacts
- Evidence
- Confidence
- Data freshness

---

## UR-014 — Opportunity Assessment

AI shall estimate:

- Potential business fit
- Sales relevance
- Potential pain points
- Potential use cases
- Opportunity strength
- Buying likelihood
- Strategic value
- Recommended next action

---

## UR-015 — AI Sales Recommendation

The system shall recommend an appropriate sales approach.

Recommendations may include:

- Contact executive
- Contact technical stakeholder
- Start with business-value messaging
- Start with operational pain
- Start with ROI
- Offer demo
- Conduct discovery
- Nurture
- Wait for additional buying signals

---

## UR-016 — Outreach Assistance

Users shall be able to generate outreach drafts for:

- Email
- LinkedIn
- WhatsApp
- Other approved channels

AI-generated content shall be based on verified intelligence and configured organizational messaging policies.

---

## UR-017 — Human Approval

Users shall be able to:

- Approve
- Reject
- Edit
- Regenerate
- Send to workflow
- Save as draft

AI shall not autonomously execute high-impact outreach without an applicable approval policy.

---

## UR-018 — Search Profiles

Users shall be able to create reusable search profiles.

A search profile shall contain:

- Name
- ICP criteria
- Filters
- Keywords
- Geographic scope
- Employee range
- Revenue range
- Technology requirements
- Industry requirements
- Search frequency
- Language
- Status
- Owner

---

## UR-019 — Scheduled Intelligence

Users shall be able to configure recurring intelligence jobs.

The system shall support:

- One-time execution
- Daily
- Weekly
- Monthly
- Custom schedules

---

## UR-020 — Continuous Intelligence

The system shall detect meaningful changes in existing accounts.

Examples:

- Funding change
- Employee growth
- Leadership change
- New technology
- New product
- Expansion
- New hiring
- New news signal

---

## 5. System Requirements

## SR-001 — Multi-Tenant Architecture

The system shall enforce tenant isolation at:

- API layer
- Service layer
- Database layer
- Cache layer
- Queue layer
- Vector layer
- Object storage layer
- AI context layer
- Search layer
- Logs
- Analytics
- Audit records

No tenant shall be able to access another tenant's intelligence data.

---

## SR-002 — Authentication

Every protected endpoint shall require authenticated access.

The system shall support:

- JWT authentication
- Token expiration
- Token validation
- Session validation
- Service authentication
- Machine-to-machine authentication where required

---

## SR-003 — Authorization

The system shall implement:

- RBAC
- Permission-based authorization
- Tenant-level permissions
- Organization-level permissions
- Workplace-level permissions
- Resource-level authorization
- AI-agent permissions
- Tool-level permissions

---

## SR-004 — Least Privilege

Every human and AI actor shall operate using the minimum permissions required.

AI agents shall not inherit unrestricted user privileges.

---

## SR-005 — AI Governance

Every AI intelligence operation shall support:

- Model identification
- Prompt version
- Model version
- Input provenance
- Output provenance
- Confidence
- Timestamp
- Evaluation metadata
- Human approval status

---

## SR-006 — AI Explainability

Important AI decisions shall provide structured explanations.

The system shall distinguish:

- Facts
- Retrieved evidence
- Inference
- Prediction
- Assumption
- Recommendation

---

## SR-007 — Data Provenance

Each intelligence field should maintain provenance where available.

The system shall track:

- Source
- Source type
- Retrieval timestamp
- Last verification
- Confidence
- Freshness
- Transformation history

---

## SR-008 — Data Freshness

The system shall support freshness policies.

Each data object may have:

- Created timestamp
- Updated timestamp
- Last enriched timestamp
- Last verified timestamp
- Expiration timestamp

---

## SR-009 — Data Quality

The system shall validate:

- Email syntax
- Domain syntax
- URL syntax
- Numeric ranges
- Company identifiers
- Contact relationships
- Duplicate records
- Source consistency
- Confidence thresholds

---

## SR-010 — Duplicate Prevention

The system shall detect duplicate:

- Companies
- Contacts
- Intelligence records
- Research reports
- Search profiles
- Outreach drafts

Duplicate detection shall support deterministic and AI-assisted matching.

---

## SR-011 — API Architecture

The service shall expose versioned APIs under:

```text
/api/v1/lead-intelligence
```

API contracts shall be documented through OpenAPI.

---

## SR-012 — Existing API Compatibility

The implementation shall support the existing Lead Intelligence API design, including capabilities corresponding to:

```text
POST /companies/search
GET  /companies/{company_id}
GET  /companies/{company_id}/contacts
POST /companies/{company_id}/qualify
POST /companies/{company_id}/research
POST /companies/{company_id}/outreach
GET  /profiles
POST /profiles
```

---

## SR-013 — Service Isolation

The Lead Intelligence Engine shall operate as an independently deployable service.

Current architecture:

```text
Frontend
   |
API Gateway / AI Gateway
   |
Lead Intelligence Service
   |
+-----------------------------+
| PostgreSQL                  |
| Redis                       |
| Search Services             |
| AI Gateway                  |
| External Intelligence APIs  |
| CRM                         |
| Workflow Engine             |
| Notification Service        |
+-----------------------------+
```

---

## SR-014 — Asynchronous Processing

Long-running operations shall execute asynchronously.

Examples:

* Bulk enrichment
* Company research
* Contact discovery
* Large-scale scoring
* Intelligence refresh
* External API collection
* AI research
* Batch qualification

The API shall not block on long-running workloads.

---

## SR-015 — Job Management

Every asynchronous intelligence job shall support:

* Job ID
* Tenant ID
* Owner
* Status
* Progress
* Start time
* End time
* Retry count
* Error information
* Cancellation
* Result reference

---

## SR-016 — Retry Architecture

The system shall implement:

* Exponential backoff
* Retry limits
* Idempotency
* Dead-letter queues
* Provider-specific retry policies
* Failure classification

---

## SR-017 — Rate Limiting

The system shall support:

* User-level limits
* Tenant-level limits
* API-level limits
* Provider-level limits
* AI-agent limits
* Batch-job limits

---

## SR-018 — AI Cost Management

The system shall monitor:

* LLM calls
* Tokens
* Embeddings
* Search calls
* Enrichment calls
* Research calls
* Agent execution
* External provider costs

Usage shall be attributable to:

* Tenant
* Organization
* User
* AI agent
* Feature
* Workflow

---

## SR-019 — Caching

The system shall cache suitable intelligence data while respecting:

* Tenant isolation
* Data freshness
* Privacy
* Invalidation rules
* Source expiration

---

## SR-020 — Observability

The service shall expose:

* Health endpoint
* Readiness endpoint
* Metrics
* Structured logs
* Distributed traces
* Error monitoring

The system shall monitor:

* API latency
* Error rate
* AI latency
* Provider latency
* Queue depth
* Job failures
* Database performance
* Cache performance
* Enrichment throughput

---

## 6. Functional Requirements

## 6.1 Company Discovery

## FR-001 — Search Companies

The system shall allow authorized users to search companies using structured filters.

Supported inputs:

```yaml
industry:
location:
min_employee_count:
max_employee_count:
min_revenue_usd:
max_revenue_usd:
technologies:
keywords:
funding_stage:
country:
state:
city:
language:
```

---

## FR-002 — Search Ranking

Search results shall be ranked using:

* Relevance
* ICP fit
* Confidence
* Data completeness
* Business priority
* User-defined weighting

---

## FR-003 — Natural Language Search

The AI shall convert natural-language requests into structured filters.

Example:

```text
Find fintech companies in Europe with more than 200 employees,
using Salesforce, and showing strong growth.
```

Expected interpretation:

```yaml
industry: fintech
region: Europe
min_employee_count: 200
technology: Salesforce
growth_signal: strong
```

---

## 6.2 Company Intelligence

## FR-004 — Company Profile

Each company profile shall provide:

```yaml
company:
  id:
  tenant_id:
  name:
  domain:
  industry:
  description:
  employee_count:
  estimated_revenue:
  headquarters:
  country:
  state:
  city:
  technologies:
  funding_stage:
  funding_amount:
  growth_signals:
  news_mentions:
  website:
  linkedin:
  twitter:
  source:
  confidence:
  language:
  created_at:
  updated_at:
  last_enriched_at:
```

---

## FR-005 — Company Timeline

The system shall maintain an intelligence timeline containing:

* Funding
* Hiring
* Leadership
* Product
* Technology
* Expansion
* News
* Business events

---

## 6.3 Contact Intelligence

## FR-006 — Contact Retrieval

The system shall return contacts associated with a company.

Each contact shall support:

```yaml
contact:
  id:
  company_id:
  full_name:
  email:
  phone:
  job_title:
  seniority_level:
  department:
  is_decision_maker:
  decision_influence:
  confidence:
```

---

## FR-007 — Contact Ranking

Contacts shall be ranked according to:

* Decision-making authority
* Department relevance
* Seniority
* ICP relationship
* Business need
* Contact confidence

---

## 6.4 AI Qualification

## FR-008 — AI Qualification

The system shall provide an AI qualification operation.

Example:

```text
POST /api/v1/lead-intelligence/companies/{company_id}/qualify
```

The qualification engine shall evaluate:

* Company size
* Industry
* Revenue
* Technology
* Business need
* Growth
* Decision-maker availability
* Potential use cases
* Intent
* Strategic fit

---

## FR-009 — Qualification Score

The qualification system shall generate:

```yaml
qualification:
  total_score:
  fit_score:
  intent_score:
  company_size_match:
  industry_match:
  technology_match:
  revenue_match:
  geographic_match:
  decision_maker_match:
  growth_score:
  confidence:
```

---

## FR-010 — Score Thresholds

Organizations shall be able to define:

```yaml
A:
  min_score: 80

B:
  min_score: 60

C:
  min_score: 40

D:
  min_score: 0
```

Thresholds shall be configurable per organization.

---

## 6.5 Research Intelligence

## FR-011 — Generate Research Brief

The system shall provide:

```text
POST /api/v1/lead-intelligence/companies/{company_id}/research
```

The generated report shall include:

```yaml
company_summary:
business_model:
market_position:
products:
target_customers:
technology:
growth_signals:
business_challenges:
potential_pain_points:
potential_use_cases:
opportunity_assessment:
recommended_pitch:
recommended_contacts:
recommended_next_action:
evidence:
confidence:
```

---

## FR-012 — Research Grounding

AI research shall use available verified data and retrieved evidence.

The system shall avoid presenting unsupported assumptions as facts.

---

## FR-013 — Research Confidence

Each research section shall have an appropriate confidence indicator.

Example:

```yaml
confidence:
  company_profile: 0.96
  technology: 0.91
  growth_signal: 0.82
  pain_point_inference: 0.71
  opportunity_prediction: 0.64
```

---

## 6.6 Opportunity Intelligence

## FR-014 — Opportunity Detection

AI shall detect potential opportunities based on:

* Company characteristics
* Growth
* Technology
* Business model
* Industry
* Market signals
* Hiring
* Funding
* News
* Product expansion

---

## FR-015 — Opportunity Assessment

The system shall generate:

```yaml
opportunity:
  score:
  urgency:
  potential_value:
  strategic_fit:
  estimated_buying_likelihood:
  primary_problem:
  secondary_problems:
  recommended_solution:
  recommended_contact:
  recommended_action:
```

---

## 6.7 Outreach Intelligence

## FR-016 — Outreach Draft Generation

The system shall generate personalized drafts using verified company intelligence.

Supported channels:

```text
Email
LinkedIn
WhatsApp
CRM Notes
Sales Tasks
```

---

## FR-017 — Personalized Messaging

Outreach generation shall consider:

* Company
* Industry
* Role
* Business context
* Technology
* Growth signals
* Potential pain points
* Relevant SalesGenie capabilities

---

## FR-018 — Human Review

AI-generated outreach shall support:

```text
Draft
Edit
Regenerate
Approve
Reject
Save
Schedule
Send
```

---

## FR-019 — Claim Validation

AI-generated outreach shall not invent:

* Customer relationships
* Company achievements
* Product usage
* Statistics
* Business facts
* Personal relationships

Unsupported claims shall be flagged.

---

## 6.8 Search Profiles

## FR-020 — Create Search Profile

Authorized users shall be able to create reusable profiles.

Example:

```yaml
profile:
  name: "US Enterprise SaaS"
  industry:
    - SaaS
    - Enterprise Software
  employees:
    min: 500
  revenue:
    min: 50000000
  geography:
    - United States
  technologies:
    - Salesforce
    - HubSpot
  growth_signals:
    required: true
```

---

## FR-021 — Execute Search Profile

Users shall be able to manually or automatically execute profiles.

---

## FR-022 — Schedule Search Profile

Profiles shall support recurring execution.

---

## FR-023 — Profile Ownership

Each profile shall maintain:

* Owner
* Organization
* Workplace
* Created timestamp
* Updated timestamp
* Status
* Execution history

---

## 6.9 Continuous Intelligence

## FR-024 — Change Detection

The system shall detect meaningful account changes.

---

## FR-025 — Intelligence Refresh

The system shall support:

```text
Manual refresh
Scheduled refresh
Event-triggered refresh
AI-triggered refresh
```

---

## FR-026 — Stale Data Detection

Records exceeding configured freshness limits shall be marked:

```text
Fresh
Aging
Stale
Expired
Unknown
```

---

## 6.10 AI Agent Requirements

## FR-027 — Lead Intelligence Agent

The AI agent shall be capable of:

```text
Discover
Search
Enrich
Analyze
Score
Qualify
Research
Recommend
Draft
Monitor
Notify
```

---

## FR-028 — Agent Planning

For complex tasks, the agent shall:

1. Understand objective.
2. Determine required information.
3. Select authorized tools.
4. Retrieve data.
5. Validate data.
6. Analyze evidence.
7. Produce structured intelligence.
8. Calculate confidence.
9. Recommend next action.
10. Request human approval where required.

---

## FR-029 — Tool Authorization

The agent shall verify permission before every protected tool invocation.

---

## FR-030 — Agent Execution Limits

The system shall enforce:

* Maximum steps
* Maximum tool calls
* Maximum tokens
* Maximum runtime
* Maximum retries
* Maximum external requests
* Maximum estimated cost

---

## FR-031 — Prompt Injection Protection

External lead data shall be treated as untrusted input.

The agent shall not execute instructions embedded inside:

* Websites
* Company descriptions
* Social content
* Search results
* Documents
* External API responses
* CRM records

---

## 6.11 Human-in-the-Loop

## FR-032 — Approval Policies

Organizations shall define which AI actions require approval.

Examples:

```yaml
lead_creation:
  approval_required: false

lead_scoring:
  approval_required: false

research:
  approval_required: false

outreach_generation:
  approval_required: false

bulk_outreach:
  approval_required: true

CRM_update:
  approval_required: configurable

data_export:
  approval_required: true
```

---

## FR-033 — Approval Queue

Users with appropriate permissions shall see:

* Pending actions
* AI recommendation
* Evidence
* Risk level
* Proposed action
* Generated content
* Approve
* Reject
* Edit

---

## 6.12 Security

## FR-034 — Tenant Authorization

Every query shall be scoped to the authenticated tenant.

---

## FR-035 — Resource Authorization

Access shall verify:

```text
User
Tenant
Organization
Workplace
Role
Permission
Resource ownership
```

---

## FR-036 — Permission Enforcement

Lead intelligence operations shall require appropriate permissions.

Examples:

```text
LEADS_READ
LEADS_WRITE
LEADS_EXPORT
LEADS_DELETE
LEADS_ENRICH
LEADS_SCORE
LEADS_RESEARCH
LEADS_OUTREACH
```

---

## 6.13 Auditability

## FR-037 — Audit Events

The system shall log:

* Search
* Lead access
* Lead creation
* Enrichment
* Scoring
* Qualification
* Research
* Outreach generation
* AI action
* Human approval
* Export
* Delete
* Configuration change

---

## FR-038 — AI Audit Trail

AI operations shall record:

```yaml
actor_type:
actor_id:
tenant_id:
agent_id:
model:
model_version:
prompt_version:
tool:
input_hash:
output_hash:
confidence:
approval_status:
timestamp:
latency:
token_usage:
cost:
```

---

## 6.14 Analytics

## FR-039 — Intelligence Metrics

The system shall calculate:

* Leads discovered
* Leads enriched
* Leads qualified
* High-score leads
* ICP matches
* Decision makers found
* Research reports generated
* Outreach drafts generated
* Approved outreach
* AI actions
* Human-approved actions
* Conversion rates

---

## FR-040 — Intelligence Performance

The system shall measure:

```text
Discovery → Enrichment
Enrichment → Qualification
Qualification → Outreach
Outreach → Response
Response → Opportunity
Opportunity → Deal
```

---

## 6.15 Reliability

## FR-041 — Provider Failure

If an intelligence provider fails, the system shall:

1. Detect failure.
2. Apply timeout.
3. Retry according to policy.
4. Attempt fallback provider if configured.
5. Record provider failure.
6. Preserve partial results.
7. Notify the user when required.

---

## FR-042 — Partial Intelligence

The system shall support partial results.

A company shall not be rejected merely because one intelligence source is unavailable.

---

## FR-043 — Idempotency

Repeated requests shall not create duplicate:

* Companies
* Contacts
* Scores
* Reports
* Outreach drafts
* Jobs

---

## 7. AI Intelligence Architecture

```text
                         ┌──────────────────────┐
                         │      SalesGenie UI   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │     API Gateway      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                  ┌─────────────────────────────────┐
                  │ Lead Intelligence Service       │
                  │ Port: 8022                      │
                  └───────────────┬─────────────────┘
                                  │
          ┌───────────────────────┼────────────────────────┐
          ▼                       ▼                        ▼
┌─────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│ Discovery Engine│     │ Enrichment Engine│     │ Scoring Engine   │
└────────┬────────┘     └────────┬─────────┘     └────────┬─────────┘
         │                       │                        │
         └───────────────────────┼────────────────────────┘
                                 ▼
                       ┌────────────────────┐
                       │ Intelligence Layer│
                       └─────────┬──────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              ▼                  ▼                  ▼
       ┌────────────┐    ┌─────────────┐    ┌──────────────┐
       │ AI Gateway │    │ Search/RAG   │    │ Data Sources │
       └─────┬──────┘    └──────┬──────┘    └──────┬───────┘
             │                  │                  │
             └──────────────────┼──────────────────┘
                                ▼
                       ┌──────────────────┐
                       │ Research Engine  │
                       └────────┬─────────┘
                                ▼
                       ┌──────────────────┐
                       │ Recommendation   │
                       │ Engine            │
                       └────────┬─────────┘
                                ▼
                       ┌──────────────────┐
                       │ Human Approval   │
                       └────────┬─────────┘
                                ▼
                       ┌──────────────────┐
                       │ CRM / Workflow   │
                       └──────────────────┘
```

---

## 8. Data Model Requirements

## 8.1 Company

```yaml
Company:
  id: UUID
  tenant_id: UUID
  name: string
  domain: string
  industry: string
  description: text
  employee_count: integer
  estimated_revenue_usd: float
  headquarters_location: string
  country: string
  state: string
  city: string
  technologies: JSON
  funding_stage: string
  funding_amount_usd: float
  growth_signals: JSON
  news_mentions: integer
  website_url: string
  linkedin_url: string
  twitter_url: string
  source: string
  confidence_score: float
  language: string
  last_enriched_at: datetime
  created_at: datetime
  updated_at: datetime
```

---

## 8.2 Contact

```yaml
Contact:
  id: UUID
  tenant_id: UUID
  company_id: UUID
  full_name: string
  email: string
  phone: string
  job_title: string
  seniority_level: string
  department: string
  is_decision_maker: boolean
  decision_influence: integer
  confidence_score: float
  source: string
  last_verified_at: datetime
  created_at: datetime
  updated_at: datetime
```

---

## 8.3 Lead Score

```yaml
LeadScore:
  id: UUID
  tenant_id: UUID
  company_id: UUID
  total_score: float
  fit_score: float
  intent_score: float
  company_size_match: integer
  industry_match: integer
  technology_match: integer
  revenue_match: integer
  geographic_match: integer
  decision_maker_match: integer
  growth_score: integer
  confidence_score: float
  reasons: JSON
  negative_factors: JSON
  evidence: JSON
  model: string
  model_version: string
  created_at: datetime
  updated_at: datetime
```

---

## 8.4 Qualification Report

```yaml
QualificationReport:
  id: UUID
  tenant_id: UUID
  company_id: UUID
  business_summary: text
  opportunity_assessment: text
  pain_points: JSON
  use_cases: JSON
  recommended_pitch: text
  recommended_contact: JSON
  recommended_next_action: string
  evidence: JSON
  confidence_score: float
  model: string
  created_at: datetime
```

---

## 8.5 Outreach Draft

```yaml
OutreachDraft:
  id: UUID
  tenant_id: UUID
  company_id: UUID
  channel: string
  subject: string
  body: text
  personalization_factors: JSON
  evidence: JSON
  confidence_score: float
  approval_status: string
  created_by: string
  created_at: datetime
```

---

## 8.6 Search Profile

```yaml
SearchProfile:
  id: UUID
  tenant_id: UUID
  name: string
  description: text
  filters: JSON
  keywords: JSON
  geographic_scope: JSON
  technology_requirements: JSON
  scoring_policy: JSON
  schedule: JSON
  status: string
  owner_id: UUID
  last_run_at: datetime
  next_run_at: datetime
  created_at: datetime
  updated_at: datetime
```

---

## 9. API Requirements

## 9.1 Search

```http
POST /api/v1/lead-intelligence/companies/search
```

---

## 9.2 Company Details

```http
GET /api/v1/lead-intelligence/companies/{company_id}
```

---

## 9.3 Company Contacts

```http
GET /api/v1/lead-intelligence/companies/{company_id}/contacts
```

---

## 9.4 AI Qualification

```http
POST /api/v1/lead-intelligence/companies/{company_id}/qualify
```

---

## 9.5 AI Research

```http
POST /api/v1/lead-intelligence/companies/{company_id}/research
```

---

## 9.6 Outreach Generation

```http
POST /api/v1/lead-intelligence/companies/{company_id}/outreach
```

---

## 9.7 Search Profiles

```http
GET  /api/v1/lead-intelligence/profiles
POST /api/v1/lead-intelligence/profiles
```

---

## 10. AI Decision Pipeline

```text
User Objective
      ↓
Natural Language Understanding
      ↓
Intent Extraction
      ↓
Search Strategy Generation
      ↓
Company Discovery
      ↓
Data Collection
      ↓
Entity Resolution
      ↓
Deduplication
      ↓
Data Validation
      ↓
Enrichment
      ↓
Signal Detection
      ↓
ICP Matching
      ↓
Lead Scoring
      ↓
Contact Identification
      ↓
AI Qualification
      ↓
Research
      ↓
Opportunity Assessment
      ↓
Recommendation
      ↓
Confidence Evaluation
      ↓
Risk Evaluation
      ↓
Human Approval
      ↓
CRM / Workflow Action
      ↓
Outcome Tracking
      ↓
Model Evaluation
```

---

## 11. AI Scoring Model

The scoring engine should support configurable weighted scoring.

Example:

```text
Lead Score =
    20% ICP Fit
  + 15% Industry Fit
  + 10% Company Size Fit
  + 10% Revenue Fit
  + 10% Technology Fit
  + 10% Geographic Fit
  + 10% Intent
  + 5% Growth
  + 5% Decision-Maker Availability
  + 5% Data Confidence
```

The weights shall be configurable by authorized administrators.

---

## 12. Lead Priority Classification

```yaml
Priority:
  HOT:
    score: 80-100
    action: "Immediate sales attention"

  WARM:
    score: 60-79
    action: "Prioritized outreach"

  QUALIFIED:
    score: 40-59
    action: "Nurture / research"

  LOW:
    score: 20-39
    action: "Low-priority nurture"

  DISQUALIFIED:
    score: 0-19
    action: "Do not prioritize"
```

The actual thresholds shall be configurable.

---

## 13. Human + AI Responsibility Model

| Capability                   |                      AI |                     Human |
| ---------------------------- | ----------------------: | ------------------------: |
| Company discovery            |                     Yes |                       Yes |
| Data enrichment              |                     Yes |                       Yes |
| Lead scoring                 |                     Yes |                       Yes |
| ICP matching                 |                     Yes |                       Yes |
| Intent detection             |                     Yes |                       Yes |
| Research                     |                     Yes |                       Yes |
| Opportunity assessment       |                     Yes |                       Yes |
| Contact recommendation       |                     Yes |                       Yes |
| Outreach drafting            |                     Yes |                       Yes |
| Outreach approval            |               Recommend | Required where configured |
| Bulk outreach                |                 Propose |                   Approve |
| CRM modification             |                 Propose |      Approve/configurable |
| Data export                  | No autonomous authority |                  Required |
| Lead deletion                | No autonomous authority |                  Required |
| Security-policy modification |                      No |                  Required |
| Model configuration          |               Recommend |  Authorized administrator |
| Scoring policy changes       |               Recommend |  Authorized administrator |

---

## 14. AI Safety Requirements

## AI-001

AI shall never treat external content as trusted instructions.

## AI-002

AI shall never cross tenant boundaries.

## AI-003

AI shall never bypass RBAC.

## AI-004

AI shall never expose secrets.

## AI-005

AI shall never fabricate company information.

## AI-006

AI shall identify uncertain information.

## AI-007

AI shall distinguish facts from predictions.

## AI-008

AI shall provide evidence for important recommendations.

## AI-009

AI shall require human approval for configured high-risk actions.

## AI-010

AI execution shall have cost and execution budgets.

---

## 15. Non-Functional Requirements

## Performance

* Search API target: p95 < 500 ms for cached/local searches.
* Company profile API target: p95 < 300 ms where data is locally available.
* AI research shall execute asynchronously.
* Bulk enrichment shall use workers.
* Search shall support pagination.
* Database queries shall use appropriate indexes.

---

## Scalability

The system shall support:

* Horizontal service scaling
* Worker scaling
* Queue-based processing
* Database connection pooling
* Redis caching
* Partitionable workloads
* Provider-level concurrency controls

The architecture shall be capable of scaling from:

```text
1 organization
        ↓
1,000 organizations
        ↓
10,000+ organizations
```

without redesigning the core domain model.

---

## Availability

Target production availability:

```text
99.9% minimum
99.95% preferred
```

Critical intelligence APIs shall support graceful degradation.

---

## Reliability

The system shall provide:

* Retry
* Timeout
* Circuit breaker
* Fallback
* Idempotency
* Dead-letter queues
* Partial-result preservation
* Health checks

---

## Security

The system shall support:

* Encryption in transit
* Encryption at rest
* Secret management
* RBAC
* Least privilege
* Audit logging
* Rate limiting
* Input validation
* Output validation
* Secure headers
* Tenant isolation

---

## 16. Data Governance

The system shall maintain a clear lifecycle:

```text
Discovery
   ↓
Collection
   ↓
Validation
   ↓
Normalization
   ↓
Enrichment
   ↓
Scoring
   ↓
Analysis
   ↓
Recommendation
   ↓
Retention
   ↓
Refresh
   ↓
Deletion / Archival
```

External intelligence data shall maintain provenance.

Sensitive data shall only be collected and processed where legally and contractually permitted.

---

## 17. Observability Requirements

## Metrics

```text
lead_search_total
lead_search_latency
lead_enrichment_total
lead_enrichment_failures
lead_score_total
lead_qualification_total
lead_research_total
outreach_generation_total
ai_token_usage
ai_cost
provider_error_rate
provider_latency
queue_depth
job_failure_rate
database_latency
cache_hit_rate
```

---

## 18. Audit Requirements

Every important action shall be traceable to:

```text
Who
What
When
Where
Why
Tenant
Organization
Resource
AI/Human
Permission
Model
Tool
Decision
Approval
Result
```

---

## 19. Event-Driven Requirements

The Lead Intelligence Engine shall publish and consume events such as:

```text
lead.discovered
lead.enriched
lead.scored
lead.qualified
lead.updated
lead.intent_detected
lead.research_completed
lead.outreach_generated
lead.approval_required
lead.approved
lead.rejected
lead.assigned
lead.converted
company.updated
contact.updated
intelligence.refresh_requested
intelligence.refresh_completed
```

Events shall support:

* Unique event IDs
* Tenant IDs
* Correlation IDs
* Causation IDs
* Timestamps
* Schema versions
* Idempotent processing

---

## 20. Integration Requirements

The engine shall be designed to integrate with:

```text
CRM
Sales Service
AI Gateway
Search Service
Workflow Service
Notification Service
Analytics Service
Knowledge Service
Vector Service
Email Service
WhatsApp Service
LinkedIn-related integrations where permitted
External company intelligence providers
External enrichment providers
Search providers
```

Provider integrations shall use adapter interfaces so providers can be replaced without changing core business logic.

---

## 21. AI Provider Abstraction

The system shall not hard-code business logic to a single LLM provider.

The AI layer shall support:

```text
Provider Router
      ↓
Model Selection
      ↓
Task Complexity
      ↓
Quality Requirement
      ↓
Latency Requirement
      ↓
Cost Constraint
      ↓
Fallback Provider
```

---

## 22. AI Evaluation Requirements

The Lead Intelligence Engine shall maintain evaluation datasets for:

* Company classification
* ICP matching
* Lead scoring
* Decision-maker identification
* Intent detection
* Research accuracy
* Opportunity assessment
* Outreach personalization

Metrics shall include:

```text
Precision
Recall
F1
Calibration
Ranking quality
Groundedness
Factual accuracy
Hallucination rate
Tool accuracy
Human approval rate
Conversion correlation
```

---

## 23. AI Feedback Loop

The system shall learn from business outcomes.

```text
AI Recommendation
       ↓
Human Decision
       ↓
Sales Action
       ↓
Customer Response
       ↓
Opportunity
       ↓
Deal
       ↓
Won/Lost
       ↓
Outcome Dataset
       ↓
Model Evaluation
       ↓
Scoring Optimization
```

Human feedback shall be captured explicitly.

---

## 24. Recommended Database Indexes

The database should provide indexes for:

```text
tenant_id
company_id
domain
company_name
industry
employee_count
estimated_revenue_usd
country
state
city
funding_stage
confidence_score
last_enriched_at
contact.email
contact.company_id
lead_score.company_id
search_profile.tenant_id
```

Composite indexes shall be introduced based on measured query patterns.

---

## 25. Search Result Requirements

Search responses shall support:

```yaml
results:
  - company_id
  - company_name
  - domain
  - industry
  - employee_count
  - revenue
  - technology
  - location
  - funding
  - growth_signals
  - ICP_score
  - lead_score
  - confidence
  - data_freshness
  - recommended_action
```

---

## 26. Enterprise UX Requirements

The Lead Intelligence interface shall contain:

## Dashboard

* Total discovered leads
* Qualified leads
* Hot leads
* ICP matches
* Intent signals
* New opportunities
* Enrichment status
* AI activity
* Human approval queue

## Search

* Natural-language search
* Advanced filters
* Saved searches
* Search profiles
* Sorting
* Pagination
* Bulk selection

## Company Profile

* Overview
* Firmographics
* Technology
* Funding
* Growth
* News
* Contacts
* AI score
* Qualification
* Research
* Opportunity
* Outreach
* Timeline

## AI Intelligence Panel

* Why this lead?
* Why this score?
* Evidence
* Confidence
* Recommended next action
* Risks
* Missing data

---

## 27. Bulk Operations

Authorized users shall be able to:

* Bulk enrich
* Bulk score
* Bulk qualify
* Bulk export
* Bulk assign
* Bulk add to CRM
* Bulk generate research
* Bulk generate outreach drafts

High-risk bulk actions shall require approval.

---

## 28. Export Requirements

Supported formats may include:

```text
CSV
XLSX
JSON
```

Exports shall enforce:

* Tenant permissions
* Field-level restrictions
* Rate limits
* Audit logging
* Export limits
* Approval policies

---

## 29. Compliance Requirements

The platform shall be designed to support applicable privacy and data-protection requirements.

The system shall support:

* Data provenance
* Consent tracking where applicable
* Data retention
* Data deletion
* Data export
* Access control
* Auditability
* Third-party data controls
* Subprocessor tracking

The platform shall not claim legal compliance automatically; compliance status shall depend on deployment, jurisdiction, contracts, policies, and legal review.

---

## 30. Error Handling

Standard error responses shall include:

```yaml
error:
  code:
  message:
  request_id:
  correlation_id:
  timestamp:
  retryable:
```

Internal implementation details and secrets shall never be exposed to end users.

---

## 31. Security Threat Model

The engine shall defend against:

* Broken access control
* Cross-tenant access
* Prompt injection
* Indirect prompt injection
* Data poisoning
* API abuse
* Credential theft
* Excessive data exposure
* Unauthorized exports
* Agent privilege escalation
* SSRF
* SQL injection
* XSS
* CSRF where applicable
* Replay attacks
* Duplicate execution
* Runaway agents
* Runaway API costs

---

## 32. Acceptance Criteria

The Lead Intelligence Engine shall be considered production-ready only when:

* [ ] Multi-tenant isolation is verified.
* [ ] RBAC is enforced server-side.
* [ ] Company discovery works.
* [ ] Company profiles work.
* [ ] Contact intelligence works.
* [ ] Lead scoring works.
* [ ] ICP matching works.
* [ ] AI qualification works.
* [ ] AI research works.
* [ ] Opportunity assessment works.
* [ ] Outreach generation works.
* [ ] Human approval works.
* [ ] Search profiles work.
* [ ] Scheduled intelligence works.
* [ ] Data provenance works.
* [ ] Confidence scoring works.
* [ ] AI outputs are validated.
* [ ] Prompt injection protections are implemented.
* [ ] AI agents cannot escalate privileges.
* [ ] AI agents cannot cross tenants.
* [ ] Rate limiting works.
* [ ] Retry and timeout policies work.
* [ ] Provider failures are handled.
* [ ] Async jobs work.
* [ ] Dead-letter handling works.
* [ ] Audit logging works.
* [ ] Metrics are available.
* [ ] Distributed tracing is available.
* [ ] AI cost tracking works.
* [ ] Data deletion propagates correctly.
* [ ] Duplicate detection works.
* [ ] API contracts are documented.
* [ ] Unit tests pass.
* [ ] Integration tests pass.
* [ ] Security tests pass.
* [ ] Cross-tenant isolation tests pass.
* [ ] AI evaluation tests pass.
* [ ] Load tests pass.
* [ ] Failure-mode tests pass.
* [ ] Production deployment is reproducible.
* [ ] Rollback procedures are validated.

---

## 33. FAANG-Level Engineering Principles

The implementation shall follow these principles:

1. **Security is enforced server-side, never only in the UI.**
2. **AI is an intelligence layer, not an authorization layer.**
3. **Human approval is mandatory for configured high-impact actions.**
4. **Every important AI decision must be explainable.**
5. **Every important external fact should have provenance.**
6. **Uncertainty must be represented explicitly.**
7. **No tenant may access another tenant's data.**
8. **AI-generated data must be distinguishable from verified source data.**
9. **Long-running intelligence operations must be asynchronous.**
10. **All external providers must be replaceable through adapters.**
11. **All important operations must be observable.**
12. **All important AI actions must be auditable.**
13. **All external content must be treated as untrusted.**
14. **AI agents must operate under explicit tool permissions.**
15. **AI execution must have cost and runtime limits.**
16. **Business-critical workflows must have deterministic fallbacks.**
17. **Partial failure must not corrupt authoritative CRM data.**
18. **All state-changing operations must be idempotent.**
19. **Performance optimizations must be evidence-driven.**
20. **The architecture must support horizontal scaling.**

---

## 34. Target End-to-End Experience

```text
Sales Manager
      │
      ▼
Define ICP
      │
      ▼
"Find companies matching my ICP"
      │
      ▼
AI Search Interpretation
      │
      ▼
Company Discovery
      │
      ▼
Data Validation
      │
      ▼
Company Enrichment
      │
      ▼
Contact Discovery
      │
      ▼
Decision-Maker Detection
      │
      ▼
Intent + Growth Signal Detection
      │
      ▼
AI Lead Scoring
      │
      ▼
ICP Matching
      │
      ▼
AI Qualification
      │
      ▼
Research Brief
      │
      ▼
Opportunity Assessment
      │
      ▼
Recommended Sales Strategy
      │
      ▼
Personalized Outreach Draft
      │
      ▼
Human Approval
      │
      ▼
CRM / Sales Workflow
      │
      ▼
Engagement
      │
      ▼
Opportunity
      │
      ▼
Deal
      │
      ▼
Outcome Feedback
      │
      ▼
AI Evaluation & Optimization
```

---

## 35. Definition of Done

The Lead Intelligence Engine is **FAANG-level production ready** when it behaves as a continuously operating intelligence platform rather than a basic lead-search API.

The final system shall provide:

```text
DISCOVER
    +
ENRICH
    +
UNDERSTAND
    +
SCORE
    +
QUALIFY
    +
RESEARCH
    +
PREDICT
    +
RECOMMEND
    +
PERSONALIZE
    +
HUMAN REVIEW
    +
AUTOMATE
    +
MEASURE
    +
LEARN
```

The system's primary output shall therefore be:

```text
Not:
"Here are 100 companies."

But:

"Here are the highest-value accounts,
why they match your ICP,
who you should contact,
what signals indicate potential demand,
what evidence supports the assessment,
how confident the system is,
what problem they may have,
what SalesGenie capability is relevant,
what action should happen next,
and whether AI is authorized to execute that action."
```
