# SalesGenie — Master Data Management (MDM) Requirements

**Document:** `master_data_management.md`  
**Project:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Requirement Level:** FAANG / Enterprise SaaS  
**Scope:** Human + AI-driven Master Data Management  
**Architecture:** Multi-Tenant, Microservices, Event-Driven, AI-Native, Zero-Trust  
**Primary Domains:** Customer, Lead, Contact, Account, Company, Product, Service, Agent, Organization, Identity, Conversation, Channel, Campaign, Subscription, Billing, Integration

---

## 1. Purpose

Master Data Management (MDM) provides SalesGenie with a centralized, governed, auditable, tenant-isolated system for creating, identifying, matching, deduplicating, enriching, validating, survivorship-managing, distributing, and monitoring critical business entities.

The MDM platform MUST establish authoritative master records while allowing operational services, AI agents, human users, external systems, and integrations to consume synchronized master data.

MDM MUST support:

- Human-created master data
- AI-generated master data
- AI-assisted data matching
- AI-assisted deduplication
- AI-assisted entity resolution
- Human approval workflows
- Automated survivorship rules
- Cross-system identity resolution
- Golden-record creation
- Data quality enforcement
- Data lineage
- Data stewardship
- Tenant isolation
- Versioning
- Auditability
- Event-driven synchronization
- Conflict resolution
- Privacy controls
- Regulatory requirements
- Real-time and batch synchronization
- Integration with CRM, support, marketing, billing, analytics, and AI systems

---

## 2. MDM Objectives

## 2.1 Business Objectives

SalesGenie MDM MUST:

1. Establish a trusted source of master data.
2. Reduce duplicate customer, lead, contact, company, and account records.
3. Maintain a canonical representation of critical business entities.
4. Improve data quality across all platform services.
5. Synchronize trusted master data across connected systems.
6. Enable AI agents to operate on consistent entity identities.
7. Prevent conflicting records from propagating across systems.
8. Provide human data stewards with controlled remediation capabilities.
9. Provide complete lineage for master-data changes.
10. Support enterprise-scale multi-tenant data governance.

---

## 3. Master Data Domains

SalesGenie MUST support the following master-data domains.

## 3.1 Customer

Attributes MAY include:

- Customer ID
- External customer IDs
- Name
- Email
- Phone
- Address
- Country
- Organization
- Customer status
- Customer lifecycle stage
- Preferred language
- Preferred channel
- Consent status
- Account owner
- Customer segment
- Industry
- Source
- Creation timestamp
- Last updated timestamp
- Data quality score

---

## 3.2 Lead

Attributes MAY include:

- Lead ID
- Name
- Email
- Phone
- Company
- Job title
- Industry
- Location
- Source
- Campaign
- Lead score
- Lead status
- Lifecycle stage
- Assigned agent
- Assigned salesperson
- AI qualification status
- Human verification status
- Created timestamp
- Updated timestamp

---

## 3.3 Contact

Attributes MAY include:

- Contact ID
- Full name
- Email addresses
- Phone numbers
- Job title
- Department
- Company
- Account
- Social identifiers
- Location
- Contact status
- Communication preferences
- Consent information
- Source systems

---

## 3.4 Company / Organization

Attributes MAY include:

- Organization ID
- Legal name
- Trading name
- Domain
- Website
- Industry
- Employee count
- Revenue range
- Headquarters
- Locations
- Country
- Registration identifiers
- Parent organization
- Subsidiaries
- Account ownership
- CRM identifiers
- Enrichment data
- Verification status

---

## 3.5 Account

The system MUST support:

- Account ID
- Customer association
- Organization association
- Account owner
- Account status
- Account tier
- Account lifecycle
- Billing association
- Subscription association
- CRM identifiers
- Risk status

---

## 3.6 Product

Product master data MUST support:

- Product ID
- SKU
- Product name
- Description
- Category
- Product family
- Price
- Currency
- Availability
- Status
- Version
- Region
- Product metadata
- External product identifiers

---

## 3.7 Service

The system MUST support:

- Service ID
- Service name
- Service category
- Description
- Availability
- SLA
- Supported channels
- Pricing
- Region
- Status
- Version

---

## 3.8 Agent

Agent master records MAY represent:

- Human sales agents
- Human support agents
- AI agents
- AI agent versions
- Specialized agents
- Supervisor agents
- Workflow agents

Required attributes SHOULD include:

- Agent ID
- Agent type
- Name
- Role
- Capabilities
- Permissions
- Organization
- Status
- Model configuration
- Version
- Availability
- Owner

---

## 3.9 Campaign

Campaign master data MUST support:

- Campaign ID
- Name
- Type
- Channel
- Owner
- Start date
- End date
- Target segment
- Status
- Source
- Attribution metadata

---

## 4. User Requirements

## UR-MDM-001 — Master Record Creation

Users MUST be able to create master records for supported entities.

The system MUST support:

- Manual creation
- API creation
- Bulk import
- Integration-based creation
- AI-assisted creation
- Workflow-based creation

---

## UR-MDM-002 — AI-Assisted Record Creation

AI agents SHOULD be able to propose master records from:

- Conversations
- Emails
- CRM records
- Support tickets
- Forms
- Documents
- Web data
- Marketing interactions
- Sales activities
- Uploaded files

AI-generated records MUST be clearly identified as AI-generated or AI-assisted.

---

## UR-MDM-003 — Master Record Search

Users MUST be able to search master records using:

- Exact matching
- Partial matching
- Fuzzy matching
- Semantic search
- Identifier search
- Email
- Phone
- Domain
- Company name
- Customer name
- External system ID

---

## UR-MDM-004 — Golden Record Access

Authorized users MUST be able to view the canonical golden record for an entity.

The golden record MUST display:

- Canonical attributes
- Source systems
- Confidence scores
- Data quality status
- Duplicate relationships
- Match history
- Merge history
- Change history
- Ownership
- Stewardship status

---

## UR-MDM-005 — Duplicate Detection

The system MUST automatically detect potentially duplicate records.

Users MUST be able to:

- Review duplicate candidates
- Compare records
- Confirm duplicates
- Reject duplicate suggestions
- Merge records
- Split incorrectly merged records
- Provide feedback

---

## UR-MDM-006 — AI Duplicate Detection

AI MUST be capable of identifying duplicate entities using:

- Name similarity
- Email similarity
- Phone similarity
- Address similarity
- Domain similarity
- Organization similarity
- Behavioral similarity
- Semantic similarity
- Cross-system identifiers
- Historical relationships

AI MUST return an explainable match confidence.

---

## UR-MDM-007 — Human Approval

High-risk MDM operations MUST support human approval.

Examples include:

- High-impact merges
- Customer identity consolidation
- Legal entity changes
- Account ownership changes
- Sensitive attribute modifications
- Cross-tenant operations
- Large-scale bulk updates

---

## UR-MDM-008 — Data Stewardship

Authorized data stewards MUST be able to:

- Review data-quality issues
- Resolve duplicates
- Correct master attributes
- Approve AI recommendations
- Reject AI recommendations
- Override survivorship decisions
- Investigate lineage
- Review source-system conflicts

---

## UR-MDM-009 — Record Versioning

Users MUST be able to inspect historical versions of master records.

The system MUST retain:

- Previous value
- New value
- Actor
- Timestamp
- Source
- Reason
- Approval state
- Correlation ID

---

## UR-MDM-010 — Data Provenance

Every important master-data attribute SHOULD expose its provenance.

Users SHOULD be able to determine:

> Where did this value originate?

The system SHOULD display:

- Source system
- Source record
- Source timestamp
- Transformation
- Enrichment provider
- AI model
- Human actor
- Confidence score

---

## UR-MDM-011 — Conflict Resolution

Users MUST be able to review conflicting values from multiple systems.

The system MUST identify:

- Conflicting attributes
- Source systems
- Source reliability
- Last updated time
- Confidence
- Survivorship decision

---

## UR-MDM-012 — Master Data Import

Users MUST be able to import master data through:

- CSV
- JSON
- REST APIs
- Supported integrations
- Batch pipelines

Imports MUST support validation, preview, error reporting, and rollback where technically feasible.

---

## UR-MDM-013 — Bulk Operations

Authorized users MUST be able to perform controlled bulk:

- Create
- Update
- Merge
- Delete
- Archive
- Reassign
- Enrich
- Validate

operations.

---

## UR-MDM-014 — AI Data Enrichment

AI and enrichment services MAY propose:

- Company information
- Industry
- Job title
- Company size
- Location
- Contact classification
- Lead attributes
- Account segmentation

AI-enriched attributes MUST include provenance and confidence.

---

## UR-MDM-015 — Data Quality Visibility

Users MUST be able to view:

- Completeness
- Accuracy indicators
- Consistency
- Validity
- Uniqueness
- Timeliness
- Confidence
- Duplicate rate

---

## UR-MDM-016 — Entity Relationships

Users MUST be able to view relationships between:

- Customer ↔ Contact
- Contact ↔ Company
- Lead ↔ Company
- Account ↔ Organization
- Customer ↔ Subscription
- Customer ↔ Conversation
- Customer ↔ Campaign
- Company ↔ Parent company
- Company ↔ Subsidiary
- Product ↔ Product family

---

## UR-MDM-017 — External Identity Mapping

Users MUST be able to see mappings between canonical records and external identifiers.

Examples:

- Salesforce ID
- HubSpot ID
- Zendesk ID
- Gmail identity
- Microsoft identity
- Internal database ID
- External CRM ID

---

## UR-MDM-018 — Auditability

Every material MDM operation MUST be auditable.

Audit records MUST be immutable or tamper-evident.

---

## UR-MDM-019 — Tenant Isolation

Users MUST only access master data belonging to their authorized tenant or organizational scope.

---

## UR-MDM-020 — Privacy

Users MUST be able to exercise applicable privacy operations involving master records, including:

- Access
- Correction
- Restriction
- Deletion
- Anonymization
- Consent withdrawal
- Data export

---

## 5. AI User Requirements

## UR-AI-MDM-001 — AI Entity Resolution

AI agents SHOULD resolve whether records from different systems represent the same real-world entity.

---

## UR-AI-MDM-002 — AI Match Confidence

AI matching MUST provide a confidence score.

Example:

```text
Match Confidence: 97.8%
Decision: Likely Duplicate
Reason:
- Same company domain
- Similar company name
- Matching phone number
- Matching address
```

---

## UR-AI-MDM-003 — Explainable Matching

AI MUST provide machine-readable and human-readable explanations for high-impact matching decisions.

---

## UR-AI-MDM-004 — AI Merge Recommendations

AI SHOULD recommend:

* Merge
* Do not merge
* Review manually

AI MUST NOT automatically perform high-risk merges without configured authorization.

---

## UR-AI-MDM-005 — AI Survivorship Recommendation

AI MAY recommend which source value should survive during consolidation.

---

## UR-AI-MDM-006 — AI Data Quality Detection

AI SHOULD identify:

* Suspicious values
* Inconsistent attributes
* Invalid formats
* Contradictory records
* Missing attributes
* Potential duplicates
* Stale information

---

## UR-AI-MDM-007 — AI Steward Assistant

The platform SHOULD provide an MDM AI assistant capable of answering questions such as:

```text
"Find duplicate customers."
"Show all conflicting company records."
"Why was this customer merged?"
"Which source is authoritative for phone numbers?"
"Show records with low confidence."
"Find companies with conflicting domains."
```

---

## 6. System Requirements

## SR-MDM-001 — Multi-Tenant Architecture

The MDM system MUST enforce tenant isolation at:

* API layer
* Service layer
* Database layer
* Cache layer
* Event layer
* Search layer
* AI layer
* Storage layer

---

## SR-MDM-002 — Canonical Data Model

The platform MUST define canonical schemas for all supported master entities.

Canonical schemas MUST be:

* Versioned
* Backward compatible where feasible
* Machine-readable
* API-accessible
* Validatable

---

## SR-MDM-003 — Golden Record Architecture

The system MUST maintain a canonical golden record for entities requiring master-data management.

---

## SR-MDM-004 — Source-of-Record Registry

The system MUST maintain configurable source-of-record policies.

Example:

```text
Email:
Primary Source = CRM
Secondary Source = Support Platform

Phone:
Primary Source = CRM
Secondary Source = Customer Portal

Company Revenue:
Primary Source = Enrichment Provider
Secondary Source = CRM
```

---

## SR-MDM-005 — Entity Resolution Engine

The system MUST provide a scalable entity-resolution engine supporting:

* Deterministic matching
* Probabilistic matching
* Fuzzy matching
* Rule-based matching
* ML-based matching
* Embedding-based similarity
* Hybrid matching

---

## SR-MDM-006 — Deduplication Engine

The system MUST provide automated duplicate detection and controlled consolidation.

---

## SR-MDM-007 — Survivorship Engine

The platform MUST provide configurable survivorship rules.

Rules MAY use:

* Source priority
* Recency
* Confidence
* Verification status
* Completeness
* Human approval
* AI confidence
* Attribute-specific priority

---

## SR-MDM-008 — Data Validation Engine

Master records MUST be validated before becoming authoritative.

Validation SHOULD include:

* Schema validation
* Type validation
* Format validation
* Referential validation
* Business-rule validation
* Privacy validation
* Tenant validation
* Security validation

---

## SR-MDM-009 — Data Quality Engine

The system MUST calculate data-quality metrics at:

* Record level
* Attribute level
* Entity level
* Tenant level
* Source-system level
* Dataset level

---

## SR-MDM-010 — Event-Driven Architecture

MDM changes MUST generate domain events where applicable.

Examples:

```text
master.customer.created
master.customer.updated
master.customer.merged
master.customer.unmerged
master.customer.deleted
master.customer.enriched
master.customer.verified

master.company.created
master.company.updated
master.company.merged

master.contact.created
master.contact.updated
```

---

## SR-MDM-011 — Event Reliability

Events MUST support:

* At-least-once delivery
* Idempotency
* Ordering where required
* Retry
* Dead-letter handling
* Replay
* Correlation IDs
* Tenant context

---

## SR-MDM-012 — API Architecture

The MDM platform MUST expose secure APIs for:

* Entity creation
* Entity retrieval
* Entity update
* Entity deletion
* Search
* Matching
* Deduplication
* Merge
* Unmerge
* Enrichment
* Validation
* Quality scoring
* Lineage
* Audit
* External identity mapping

---

## SR-MDM-013 — Idempotency

Create and mutation APIs SHOULD support idempotency keys.

Repeated requests MUST NOT create unintended duplicate master records.

---

## SR-MDM-014 — Optimistic Concurrency

Master-data mutations MUST support concurrency control.

The system SHOULD use:

* Version numbers
* ETags
* Revision IDs
* Compare-and-swap semantics

---

## SR-MDM-015 — Distributed Transaction Safety

Cross-service MDM operations MUST avoid unsafe distributed transactions where possible.

The system SHOULD use:

* Transactional outbox
* Saga patterns
* Idempotent consumers
* Eventual consistency
* Compensating actions

---

## 7. Functional Requirements

## FR-MDM-001 — Create Master Entity

The system MUST allow authorized actors to create supported master entities.

### Inputs

* Tenant ID
* Entity type
* Entity attributes
* Source
* External ID
* Actor
* Request ID

### Processing

1. Validate request.
2. Validate tenant context.
3. Normalize attributes.
4. Search for potential duplicates.
5. Calculate confidence.
6. Apply matching policy.
7. Create or route for review.
8. Generate master ID.
9. Persist source mapping.
10. Generate audit event.
11. Publish master-data event.

### Outputs

* Master entity
* Master ID
* Version
* Data quality score
* Match status
* Audit metadata

---

## 8. Entity Matching

## FR-MDM-010 — Deterministic Matching

The system MUST support exact matching based on trusted identifiers.

Examples:

```text
Exact email
Exact CRM ID
Exact customer ID
Exact registration number
Exact domain
Exact phone number
```

---

## FR-MDM-011 — Fuzzy Matching

The system MUST support fuzzy matching for appropriate attributes.

Algorithms MAY include:

* Levenshtein distance
* Jaro-Winkler
* Token similarity
* N-gram similarity
* Phonetic matching

---

## FR-MDM-012 — Semantic Matching

The platform SHOULD support embedding-based entity similarity.

Semantic matching MAY be used for:

* Company names
* Addresses
* Product descriptions
* Organization descriptions
* Contact information

---

## FR-MDM-013 — Hybrid Entity Resolution

The preferred matching strategy SHOULD combine:

```text
Deterministic Rules
        +
Fuzzy Matching
        +
Semantic Similarity
        +
Business Rules
        +
Source Reliability
        +
Historical Evidence
```

---

## 9. Match Decision Policy

The system SHOULD support configurable thresholds.

Example:

```text
Confidence >= 0.98
    → Automatic duplicate classification

0.90 <= Confidence < 0.98
    → Human review

Confidence < 0.90
    → Treat as separate entity
```

Thresholds MUST be configurable per:

* Tenant
* Entity
* Attribute
* Source
* Risk class

---

## 10. Duplicate Management

## FR-MDM-020 — Duplicate Candidate Generation

The system MUST generate duplicate candidates with:

* Candidate IDs
* Match score
* Matching attributes
* Non-matching attributes
* Sources
* Explanation
* Risk level

---

## FR-MDM-021 — Duplicate Review

Human reviewers MUST be able to compare candidate records side-by-side.

---

## FR-MDM-022 — Merge

Authorized users MUST be able to merge duplicate records.

Merge operations MUST:

1. Validate permissions.
2. Lock relevant records.
3. Determine survivorship.
4. Preserve source lineage.
5. Create merge history.
6. Update relationships.
7. Generate a canonical record.
8. Publish merge event.
9. Create audit record.

---

## FR-MDM-023 — Unmerge

Where technically and legally permissible, the platform SHOULD support controlled unmerge operations.

Unmerge MUST preserve:

* Original records
* Merge history
* Actor
* Timestamp
* Reason
* Related events

---

## 11. Golden Record

## FR-MDM-030 — Golden Record Generation

The system MUST generate a canonical golden record from trusted source data.

---

## FR-MDM-031 — Attribute-Level Survivorship

Survivorship MUST operate at attribute level where appropriate.

Example:

```text
Customer Name
    → CRM

Email
    → Verified Customer Portal

Phone
    → CRM

Company Industry
    → Enrichment Provider

Preferred Language
    → Customer Preference Service
```

---

## FR-MDM-032 — Golden Record Versioning

Every golden-record modification MUST create a new version.

---

## 12. Data Normalization

## FR-MDM-040 — Attribute Normalization

The system MUST normalize master data before matching and persistence.

Examples:

```text
Phone:
+8801712345678

Email:
USER@EXAMPLE.COM → user@example.com

Company:
Acme Ltd.
ACME LIMITED
Acme Limited
```

---

## FR-MDM-041 — Address Normalization

The system SHOULD normalize:

* Country
* State/province
* City
* Postal code
* Street
* Address abbreviations

---

## 13. Data Quality

## FR-MDM-050 — Quality Scoring

Each master record SHOULD receive a quality score.

Example:

```text
Completeness: 96%
Validity: 99%
Uniqueness: 100%
Consistency: 94%
Freshness: 87%

Overall Quality: 95%
```

---

## FR-MDM-051 — Quality Rules

Administrators MUST be able to configure validation rules.

---

## FR-MDM-052 — Quality Alerts

The system MUST generate alerts when quality falls below configured thresholds.

---

## 14. Source System Management

## FR-MDM-060 — Source Registry

The system MUST maintain metadata for connected source systems.

Each source SHOULD include:

* Source ID
* Name
* Type
* Owner
* Reliability score
* Priority
* Data domains
* Supported entities
* Last synchronization
* Status

---

## FR-MDM-061 — Source Reliability

The platform SHOULD maintain source reliability scores.

Example:

```text
CRM:
Reliability = 0.98

Support Platform:
Reliability = 0.91

AI Enrichment:
Reliability = 0.84
```

---

## 15. Cross-System Identity Resolution

## FR-MDM-070 — External Identifier Mapping

The system MUST maintain mappings such as:

```text
master_customer_id
    ├── Salesforce ID
    ├── HubSpot ID
    ├── Zendesk ID
    ├── Internal CRM ID
    └── Support Platform ID
```

---

## FR-MDM-071 — Identity Graph

The system SHOULD maintain an entity-relationship graph.

The graph MAY represent:

```text
Customer
   ↓
Contact
   ↓
Company
   ↓
Account
   ↓
Subscription
   ↓
Conversations
   ↓
Campaigns
```

---

## 16. AI MDM Architecture

## FR-AI-MDM-001 — AI Entity Resolution

AI models MUST be able to produce entity-match candidates.

---

## FR-AI-MDM-002 — AI Confidence

AI output MUST contain:

```json
{
  "match_score": 0.973,
  "decision": "LIKELY_DUPLICATE",
  "confidence": 0.973
}
```

---

## FR-AI-MDM-003 — AI Explanation

AI matching responses MUST include explainability metadata.

---

## FR-AI-MDM-004 — AI Human-in-the-Loop

The platform MUST route uncertain or high-risk AI decisions to human reviewers.

---

## FR-AI-MDM-005 — AI Feedback Loop

Human decisions SHOULD be captured as feedback.

Examples:

```text
AI said duplicate → Human confirmed
AI said duplicate → Human rejected
AI said separate → Human merged
```

This feedback MAY be used for model evaluation and improvement.

---

## 17. Human MDM Architecture

## FR-HUMAN-MDM-001 — Data Steward Dashboard

The platform MUST provide an MDM stewardship interface.

Dashboard SHOULD show:

* Duplicate queue
* Data-quality queue
* Conflicts
* Pending merges
* AI recommendations
* Failed imports
* Synchronization errors
* Privacy requests
* High-risk changes

---

## FR-HUMAN-MDM-002 — Review Queue

Review queues MUST support:

* Priority
* Risk
* Entity type
* Tenant
* Source
* Confidence
* Age
* Assigned steward
* Status

---

## FR-HUMAN-MDM-003 — Approval Workflow

Workflow states SHOULD include:

```text
PENDING
IN_REVIEW
APPROVED
REJECTED
ESCALATED
COMPLETED
CANCELLED
```

---

## 18. Synchronization

## FR-MDM-090 — Outbound Synchronization

Approved master-data changes MUST be distributable to downstream services.

---

## FR-MDM-091 — Inbound Synchronization

The system MUST accept updates from authorized source systems.

---

## FR-MDM-092 — Conflict Detection

Conflicting source updates MUST be detected before overwriting authoritative values.

---

## FR-MDM-093 — Synchronization Retry

Failed synchronization operations MUST support:

* Retry
* Backoff
* Dead-letter queues
* Manual replay
* Error classification

---

## 19. Data Lineage

## FR-MDM-100 — Attribute Lineage

The system MUST track where important attributes originated.

---

## FR-MDM-101 — Transformation Lineage

The system SHOULD track transformations applied to master data.

---

## FR-MDM-102 — AI Lineage

AI-generated or AI-enriched values MUST record:

* Model
* Model version
* Prompt/workflow identifier where appropriate
* Timestamp
* Input source
* Confidence
* Human approval

---

## 20. Audit Logging

## FR-MDM-110 — MDM Audit Events

The platform MUST log:

```text
CREATE
READ
UPDATE
DELETE
MERGE
UNMERGE
ENRICH
VALIDATE
APPROVE
REJECT
EXPORT
IMPORT
SYNC
OVERRIDE
```

---

## FR-MDM-111 — Tamper Evidence

Audit logs MUST be protected from unauthorized modification.

---

## 21. Access Control

## FR-MDM-120 — RBAC

MDM permissions MUST support roles such as:

```text
SUPER_ADMIN
TENANT_ADMIN
DATA_STEWARD
SALES_MANAGER
SALES_AGENT
SUPPORT_MANAGER
SUPPORT_AGENT
AI_AGENT
AUDITOR
READ_ONLY
```

---

## FR-MDM-121 — ABAC

The platform SHOULD support attribute-based policies using:

* Tenant
* Organization
* Role
* Entity type
* Data classification
* Risk
* Region
* Ownership

---

## FR-MDM-122 — Least Privilege

Users and AI agents MUST receive only the permissions necessary for their assigned tasks.

---

## 22. AI Agent Permissions

AI agents MUST NOT automatically receive unrestricted MDM privileges.

AI agents SHOULD have explicit capabilities such as:

```text
mdm.read
mdm.search
mdm.match
mdm.propose_merge
mdm.enrich
mdm.create
mdm.update
mdm.delete
```

High-risk capabilities SHOULD require additional authorization:

```text
mdm.merge
mdm.unmerge
mdm.bulk_update
mdm.bulk_delete
mdm.export
```

---

## 23. Privacy Requirements

## FR-MDM-130 — Data Subject Association

Master records MUST support association with privacy identities.

---

## FR-MDM-131 — Deletion Propagation

Approved deletion requests MUST propagate to applicable systems.

---

## FR-MDM-132 — Anonymization

Where deletion is not technically or legally appropriate, the platform MAY support anonymization or pseudonymization.

---

## FR-MDM-133 — Consent-Aware Processing

The MDM system MUST respect applicable consent restrictions.

---

## 24. Security Requirements

## SR-MDM-020 — Encryption

Master data MUST be encrypted:

* In transit
* At rest
* In backups
* In replicated storage

Sensitive fields SHOULD support field-level encryption.

---

## SR-MDM-021 — Secrets

Credentials and integration secrets MUST NOT be stored in source code or plaintext configuration.

---

## SR-MDM-022 — Zero Trust

Every MDM request MUST be authenticated and authorized.

Trust MUST NOT be granted solely based on:

* Network location
* Internal service
* IP address
* Service identity

---

## SR-MDM-023 — AI Security

AI agents MUST be protected against:

* Prompt injection
* Tool abuse
* Unauthorized record access
* Data exfiltration
* Excessive permissions
* Cross-tenant data leakage

---

## 25. Performance Requirements

## NFR-MDM-001 — API Latency

For standard master-data operations:

```text
Target p50 < 100 ms
Target p95 < 300 ms
Target p99 < 750 ms
```

excluding external provider latency.

---

## NFR-MDM-002 — Search

Standard entity searches SHOULD return within:

```text
p95 < 500 ms
```

under normal operating conditions.

---

## NFR-MDM-003 — Scalability

The MDM platform MUST horizontally scale across:

* API workers
* Matching workers
* Data-quality workers
* Event consumers
* Search nodes
* AI workers

---

## 26. Reliability Requirements

## NFR-MDM-010 — Availability

Critical MDM APIs SHOULD target:

```text
99.9%+
```

monthly availability.

---

## NFR-MDM-011 — No Silent Data Loss

The system MUST NOT silently discard master-data changes.

---

## NFR-MDM-012 — Disaster Recovery

The system MUST support:

* Backup
* Restore
* Point-in-time recovery where supported
* Event replay
* Recovery validation

---

## 27. Observability

## NFR-MDM-020 — Metrics

The system MUST expose:

* Master records created
* Master records updated
* Duplicate candidates
* Duplicate resolution rate
* Merge rate
* Unmerge rate
* Data-quality score
* Import success rate
* Synchronization success rate
* Synchronization failure rate
* AI match confidence
* Human approval rate
* API latency
* Event lag

---

## NFR-MDM-021 — Distributed Tracing

MDM operations MUST support distributed tracing.

Every request SHOULD carry:

```text
trace_id
span_id
correlation_id
tenant_id
request_id
actor_id
```

---

## 28. Event Model

Example master-data event:

```json
{
  "event_id": "evt_123",
  "event_type": "master.customer.updated",
  "event_version": "1.0",
  "tenant_id": "tenant_123",
  "master_id": "cust_123",
  "entity_type": "customer",
  "version": 12,
  "actor_type": "human",
  "actor_id": "user_123",
  "source": "crm",
  "timestamp": "2026-08-28T12:00:00Z",
  "correlation_id": "corr_123",
  "changes": {
    "phone": {
      "old": "+8801700000000",
      "new": "+8801800000000"
    }
  }
}
```

---

## 29. MDM State Machine

```text
                    ┌──────────────┐
                    │   DISCOVERED │
                    └──────┬───────┘
                           ↓
                    ┌──────────────┐
                    │   VALIDATING │
                    └──────┬───────┘
                           ↓
                 ┌─────────┴─────────┐
                 ↓                   ↓
        ┌────────────────┐   ┌───────────────┐
        │   UNIQUE       │   │ POSSIBLE_DUP  │
        └───────┬────────┘   └───────┬───────┘
                │                    ↓
                │            ┌──────────────┐
                │            │ HUMAN REVIEW │
                │            └──────┬───────┘
                │                   ↓
                │          ┌────────┴────────┐
                │          ↓                 ↓
                │      DUPLICATE          UNIQUE
                │          ↓                 ↓
                │       MERGE ←──────────────┘
                │          ↓
                └──────→ GOLDEN RECORD
                            ↓
                      DISTRIBUTION
                            ↓
                      SYNCHRONIZED
```

---

## 30. Master Data Lifecycle

```text
SOURCE
  ↓
INGESTION
  ↓
NORMALIZATION
  ↓
VALIDATION
  ↓
ENTITY RESOLUTION
  ↓
DUPLICATE DETECTION
  ↓
SURVIVORSHIP
  ↓
HUMAN/AI APPROVAL
  ↓
GOLDEN RECORD
  ↓
QUALITY SCORING
  ↓
DISTRIBUTION
  ↓
MONITORING
  ↓
ENRICHMENT
  ↓
VERSIONING
  ↓
RETENTION / DELETION
```

---

## 31. Data Quality Rules

The system SHOULD implement configurable rules including:

```text
Email must be syntactically valid.
Phone must follow supported country formats.
Company domain must be normalized.
Customer ID must be unique within tenant.
External source IDs must be unique per source.
Required fields must not be null.
Referenced organizations must exist.
Deleted entities must not be reused.
Master records must have valid lifecycle states.
Sensitive attributes must satisfy access policies.
```

---

## 32. Business Rules

## BR-MDM-001

A record MUST NOT become authoritative until mandatory validation succeeds.

## BR-MDM-002

Duplicate candidates MUST NOT be automatically merged if the confidence score is below the configured threshold.

## BR-MDM-003

High-risk merges MUST require human approval.

## BR-MDM-004

Cross-tenant matching MUST be prohibited unless explicitly authorized by platform policy.

## BR-MDM-005

Master IDs MUST remain stable across normal attribute changes.

## BR-MDM-006

Merge operations MUST preserve lineage.

## BR-MDM-007

External identifiers MUST NOT be silently reassigned.

## BR-MDM-008

Deleted records MUST remain represented in audit history according to retention policy.

## BR-MDM-009

AI-generated data MUST remain distinguishable from human-verified data.

## BR-MDM-010

AI confidence MUST NOT be treated as equivalent to human verification unless explicitly configured.

---

## 33. API Requirements

Representative APIs:

```text
POST   /api/v1/mdm/entities
GET    /api/v1/mdm/entities/{id}
PATCH  /api/v1/mdm/entities/{id}
DELETE /api/v1/mdm/entities/{id}

POST   /api/v1/mdm/search
POST   /api/v1/mdm/match
POST   /api/v1/mdm/deduplicate

POST   /api/v1/mdm/merge
POST   /api/v1/mdm/unmerge

GET    /api/v1/mdm/entities/{id}/lineage
GET    /api/v1/mdm/entities/{id}/history
GET    /api/v1/mdm/entities/{id}/sources

POST   /api/v1/mdm/import
POST   /api/v1/mdm/export

GET    /api/v1/mdm/quality
GET    /api/v1/mdm/conflicts

POST   /api/v1/mdm/enrichment
POST   /api/v1/mdm/verify

GET    /api/v1/mdm/stewardship/queue
POST   /api/v1/mdm/stewardship/{id}/approve
POST   /api/v1/mdm/stewardship/{id}/reject
```

---

## 34. Database Requirements

The MDM data model SHOULD contain logical structures for:

```text
master_entities
master_entity_versions
master_entity_attributes
golden_records
source_records
source_systems
external_identifiers
entity_matches
duplicate_candidates
merge_operations
unmerge_operations
survivorship_rules
data_quality_scores
data_quality_issues
entity_relationships
entity_lineage
enrichment_records
verification_records
stewardship_tasks
mdm_audit_logs
mdm_events
```

---

## 35. Caching Requirements

Caching MAY be used for:

* Frequently accessed golden records
* Entity metadata
* Source configuration
* Matching configuration
* Survivorship rules
* Permission policies

Cache invalidation MUST occur when authoritative master data changes.

Tenant isolation MUST apply to all cache keys.

---

## 36. Search Requirements

Search MUST support:

* Exact search
* Prefix search
* Fuzzy search
* Semantic search
* Faceted search
* Tenant filtering
* Entity filtering
* Source filtering
* Quality filtering
* Confidence filtering

Search indexes MUST NOT expose unauthorized tenant data.

---

## 37. Bulk Processing

Bulk MDM operations MUST support:

```text
Batch validation
Batch matching
Batch deduplication
Batch enrichment
Batch merge recommendations
Batch quality assessment
Batch synchronization
```

Large jobs SHOULD execute asynchronously.

Users MUST receive:

* Job ID
* Progress
* Success count
* Failure count
* Skipped count
* Error report

---

## 38. Error Handling

The system MUST distinguish between:

```text
VALIDATION_ERROR
AUTHORIZATION_ERROR
TENANT_ACCESS_ERROR
DUPLICATE_DETECTED
CONFLICT_ERROR
SOURCE_SYSTEM_ERROR
INTEGRATION_ERROR
MATCHING_ERROR
MERGE_ERROR
SYNC_ERROR
AI_ERROR
RATE_LIMIT_ERROR
CONCURRENCY_ERROR
SYSTEM_ERROR
```

Errors MUST be observable and actionable.

---

## 39. AI/Human Decision Matrix

| Operation                    |        AI |                          Human |    Automatic |
| ---------------------------- | --------: | -----------------------------: | -----------: |
| Entity search                |       Yes |                            Yes |          Yes |
| Candidate matching           |       Yes |                            Yes |          Yes |
| Duplicate detection          |       Yes |                            Yes |          Yes |
| Low-risk merge               | Recommend |                       Optional | Configurable |
| High-risk merge              | Recommend |                       Required |           No |
| Data enrichment              |       Yes |                         Review | Configurable |
| Golden-record recommendation |       Yes |                            Yes |          Yes |
| Golden-record override       |        No |                            Yes |           No |
| Sensitive-field modification | Recommend |                       Required |           No |
| Bulk deletion                |        No |                       Required |           No |
| Privacy deletion             |    Assist | Required where policy requires |   Controlled |
| Data-quality detection       |       Yes |                            Yes |          Yes |
| Data-quality remediation     | Recommend |                            Yes | Configurable |

---

## 40. Acceptance Criteria

## AC-MDM-001

Given two identical customer records, the system detects them as duplicates.

## AC-MDM-002

Given two similar but distinct customers, the system does not automatically merge them when confidence is below the configured threshold.

## AC-MDM-003

Given a high-confidence duplicate, the system produces a merge recommendation with explainable evidence.

## AC-MDM-004

Given a human-approved merge, the system creates one golden record and preserves source lineage.

## AC-MDM-005

Given an unauthorized user, the system prevents access to another tenant's master data.

## AC-MDM-006

Given a master-data update, downstream subscribers receive the corresponding event.

## AC-MDM-007

Given a synchronization failure, the system retries according to policy and records the failure.

## AC-MDM-008

Given an AI-generated attribute, the system records model and provenance metadata.

## AC-MDM-009

Given conflicting source values, the system identifies the conflict and applies configured survivorship rules.

## AC-MDM-010

Given a privacy deletion request, the system identifies all applicable master-data relationships and downstream propagation requirements.

---

## 41. Enterprise MDM KPIs

SalesGenie SHOULD monitor:

```text
Master Data Accuracy
Master Data Completeness
Duplicate Rate
Duplicate Detection Precision
Duplicate Detection Recall
False Merge Rate
False Non-Merge Rate
Golden Record Coverage
Entity Resolution Accuracy
AI Match Precision
AI Match Recall
Human Approval Rate
Human Override Rate
Data Quality Score
Source Reliability
Synchronization Success Rate
Synchronization Latency
MDM API Latency
Merge Processing Time
Stewardship Queue Age
Unresolved Conflict Count
Master Data Freshness
Privacy Request Completion Rate
```

---

## 42. Recommended Enterprise Architecture

```text
                    ┌──────────────────────────┐
                    │     SalesGenie Clients   │
                    │ Web / Mobile / Admin UI  │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │       API Gateway        │
                    │ Auth / RBAC / RateLimit  │
                    └────────────┬─────────────┘
                                 │
                ┌────────────────┴────────────────┐
                │                                 │
                ▼                                 ▼
      ┌──────────────────┐             ┌──────────────────┐
      │   MDM API        │             │   MDM AI Layer   │
      │ CRUD / Search    │             │ Entity Resolver  │
      │ Workflow         │             │ Deduplication    │
      └────────┬─────────┘             │ Enrichment       │
               │                       └────────┬─────────┘
               │                                │
               └────────────────┬───────────────┘
                                ▼
                    ┌──────────────────────────┐
                    │ Entity Resolution Engine │
                    │ Rules + Fuzzy + ML + AI  │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │ Survivorship Engine       │
                    │ Golden Record Generator   │
                    └────────────┬─────────────┘
                                 │
               ┌─────────────────┼─────────────────┐
               │                 │                 │
               ▼                 ▼                 ▼
       ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
       │ MDM Database │  │ Search Index │  │ Entity Graph │
       └──────────────┘  └──────────────┘  └──────────────┘
               │                 │                 │
               └─────────────────┼─────────────────┘
                                 ▼
                    ┌──────────────────────────┐
                    │ Event Bus / Streaming    │
                    └────────────┬─────────────┘
                                 │
             ┌───────────────────┼────────────────────┐
             ▼                   ▼                    ▼
      ┌────────────┐      ┌────────────┐      ┌────────────┐
      │ CRM        │      │ Support    │      │ Marketing  │
      │ Salesforce │      │ Zendesk    │      │ Campaigns  │
      └────────────┘      └────────────┘      └────────────┘
             │                   │                    │
             └───────────────────┼────────────────────┘
                                 ▼
                    ┌──────────────────────────┐
                    │ Data Platform / Lakehouse│
                    │ Analytics / BI / ML      │
                    └──────────────────────────┘
```

---

## 43. FAANG-Level Design Principles

SalesGenie MDM MUST follow these principles:

1. **Single logical source of truth, not necessarily a single physical database.**
2. **Golden records MUST be explainable.**
3. **Every master-data mutation MUST be attributable.**
4. **AI MUST augment human stewardship rather than bypass governance.**
5. **High-impact automated decisions MUST be risk-aware.**
6. **Tenant isolation MUST be enforced at every layer.**
7. **Master identifiers MUST remain stable.**
8. **Source provenance MUST be preserved.**
9. **Data quality MUST be measurable.**
10. **Duplicate resolution MUST be reversible where possible.**
11. **Events MUST be idempotent.**
12. **External systems MUST NOT be allowed to silently overwrite authoritative data.**
13. **AI-generated data MUST include confidence and provenance.**
14. **Security policies MUST apply equally to humans and AI agents.**
15. **Privacy requirements MUST be integrated into the MDM lifecycle.**
16. **Operational services SHOULD consume canonical master data rather than independently redefining identities.**
17. **MDM decisions MUST be observable and auditable.**
18. **The architecture MUST support eventual consistency without sacrificing correctness of authoritative records.**
19. **Configuration MUST be tenant-aware and version-controlled.**
20. **The platform MUST degrade safely when AI, integrations, or external enrichment services fail.**

---

## 44. Definition of Done

Master Data Management is considered production-ready when:

* [ ] Canonical entity schemas are implemented.
* [ ] Golden records are supported.
* [ ] Entity resolution is implemented.
* [ ] Duplicate detection is implemented.
* [ ] Merge and controlled unmerge are implemented.
* [ ] Survivorship rules are implemented.
* [ ] Source-system registry is implemented.
* [ ] External identifier mapping is implemented.
* [ ] Data-quality scoring is implemented.
* [ ] Human stewardship workflows are implemented.
* [ ] AI-assisted MDM workflows are implemented.
* [ ] AI confidence and explainability are implemented.
* [ ] Human-in-the-loop controls are implemented.
* [ ] Master-data lineage is implemented.
* [ ] Version history is implemented.
* [ ] Audit logging is implemented.
* [ ] RBAC/ABAC controls are implemented.
* [ ] Tenant isolation is verified.
* [ ] Encryption is enabled.
* [ ] Event-driven synchronization is implemented.
* [ ] Retry and dead-letter handling are implemented.
* [ ] Idempotency is implemented.
* [ ] Concurrency protection is implemented.
* [ ] Search infrastructure is implemented.
* [ ] Bulk processing is implemented.
* [ ] Data privacy workflows are integrated.
* [ ] Monitoring and alerting are implemented.
* [ ] Distributed tracing is implemented.
* [ ] Disaster recovery is tested.
* [ ] Security testing is completed.
* [ ] Performance testing is completed.
* [ ] AI safety testing is completed.
* [ ] Cross-tenant isolation testing is completed.
* [ ] Merge/unmerge integrity testing is completed.
* [ ] Production runbooks are documented.
* [ ] MDM SLIs/SLOs are defined.
* [ ] Audit and compliance evidence is exportable.

---

## 45. Final Requirement

SalesGenie MUST treat Master Data Management as a **platform-level data governance capability**, not merely a CRUD module.

The MDM system MUST provide a trusted identity and canonical-data layer connecting human users, AI agents, CRM systems, support systems, marketing systems, billing systems, integrations, workflows, analytics, and the SalesGenie data platform.

The target operating model is:

```text
Every important entity
        ↓
Has one canonical identity
        ↓
Has a governed golden record
        ↓
Has measurable data quality
        ↓
Has complete provenance
        ↓
Has controlled lifecycle
        ↓
Can be resolved across systems
        ↓
Can be safely consumed by humans and AI
        ↓
Can be synchronized through reliable events
        ↓
Can be audited, governed, secured, and deleted
        ↓
Without violating tenant isolation or privacy requirements
```
