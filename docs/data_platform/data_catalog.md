# SalesGenie — Data Catalog Requirements Specification

**Document:** `data_catalog.md`  
**Project:** SalesGenie / FlowMind AI  
**Requirement Level:** FAANG / Enterprise SaaS  
**Scope:** Human-operated and AI-operated data discovery, metadata management, governance, lineage, classification, quality, access control, compliance, and intelligent data cataloging.

---

## 1. Purpose

The SalesGenie Data Catalog shall provide a centralized, searchable, governed, machine-readable inventory of all organizational data assets generated, ingested, transformed, stored, consumed, or exposed by the platform.

The catalog shall enable:

- Humans to discover, understand, govern, access, monitor, and manage data assets.
- AI agents to discover and safely reason over approved data assets.
- Data engineers to understand schemas, dependencies, lineage, quality, and ownership.
- Administrators to enforce governance, RBAC, tenant isolation, and compliance.
- Security teams to identify sensitive and regulated data.
- Compliance teams to map data assets to privacy and regulatory requirements.
- Product and sales teams to understand available customer, lead, conversation, campaign, and business intelligence data.
- AI systems to select appropriate data sources without bypassing authorization or governance controls.
- Platform operators to monitor catalog freshness, metadata quality, and discovery coverage.

---

## 2. Scope

The Data Catalog shall cover metadata and governance for:

- Relational databases
- PostgreSQL databases
- Data warehouses
- Data lakes
- Object storage
- Vector databases
- RAG knowledge bases
- Document stores
- Search indexes
- Redis-backed datasets where cataloging is applicable
- Event streams
- Message queues
- Kafka topics
- Webhook data
- CRM data
- Sales lead data
- Customer data
- Contact data
- Organization data
- Conversation data
- Support tickets
- Email data
- WhatsApp data
- Slack data
- Microsoft Teams data
- HubSpot data
- Salesforce data
- Zendesk data
- Jira data
- Notion data
- Google Drive data
- AI-generated data
- AI inference outputs
- Agent execution data
- Workflow execution data
- Billing data
- Subscription data
- Usage data
- Analytics data
- Audit data
- Security data
- Compliance data
- Human-generated datasets
- AI-generated datasets
- Derived datasets
- Feature datasets
- ML training datasets
- ML evaluation datasets
- Data products
- API-exposed datasets

---

## 3. Actors

## 3.1 Human Actors

### H-001 — Super Admin

The system shall allow Super Admins to:

- View the global data catalog.
- Configure catalog policies.
- Manage metadata governance.
- Define classification rules.
- Assign data ownership.
- Manage catalog access.
- Review sensitive-data findings.
- Review lineage.
- Configure retention metadata.
- Configure compliance mappings.
- Approve or reject data asset publication.
- Review catalog audit logs.
- Manage AI catalog permissions.

### H-002 — Organization Admin

The system shall allow Organization Admins to:

- View organization-scoped assets.
- Manage organization metadata.
- Assign data owners.
- Configure organization-level classifications.
- Review quality reports.
- Request access.
- Approve authorized access where permitted.
- View organization lineage.

### H-003 — Data Engineer

The system shall allow Data Engineers to:

- Register datasets.
- Connect data sources.
- Import schemas.
- Update metadata.
- Inspect lineage.
- Monitor metadata synchronization.
- Investigate data-quality issues.
- Configure ingestion metadata.
- Manage technical metadata.

### H-004 — Data Analyst

The system shall allow Data Analysts to:

- Search data assets.
- Inspect schemas.
- View business definitions.
- View data quality.
- View lineage.
- Request access.
- Bookmark assets.
- Create collections.
- Compare datasets.

### H-005 — Data Scientist / ML Engineer

The system shall allow ML users to:

- Discover datasets.
- Inspect feature metadata.
- Identify training datasets.
- Identify evaluation datasets.
- Inspect data lineage.
- Review dataset quality.
- Determine dataset freshness.
- Identify sensitive attributes.
- Verify permitted usage.

### H-006 — Security Administrator

The system shall allow Security Administrators to:

- Identify sensitive datasets.
- Review classification results.
- Monitor unauthorized access.
- Review catalog security events.
- Inspect asset-level access policies.
- Audit metadata modifications.

### H-007 — Compliance Officer

The system shall allow Compliance Officers to:

- Map data assets to regulatory requirements.
- Review personal-data classifications.
- Inspect retention requirements.
- Review processing purposes.
- Track data ownership.
- Review data-subject-related assets.
- Export governance reports.

### H-008 — Business User

The system shall allow authorized business users to:

- Search approved business datasets.
- View business descriptions.
- Understand dataset ownership.
- View approved usage.
- Request access.

---

## 4. AI Actors

## 4.1 AI Data Discovery Agent

The system shall allow AI agents to:

- Search catalog metadata.
- Discover relevant datasets.
- Rank candidate data assets.
- Explain why a dataset is relevant.
- Respect authorization boundaries.
- Exclude restricted datasets.
- Identify sensitive data.
- Inspect schema metadata.
- Inspect lineage metadata.
- Evaluate freshness.
- Evaluate data quality.
- Recommend approved data sources.

## 4.2 AI Data Governance Agent

The system shall allow AI agents to:

- Detect missing metadata.
- Recommend classifications.
- Detect schema anomalies.
- Detect stale metadata.
- Recommend owners.
- Identify duplicate datasets.
- Recommend business descriptions.
- Detect inconsistent terminology.
- Recommend tags.
- Recommend retention metadata.
- Identify potential compliance risks.

## 4.3 AI Data Quality Agent

The system shall allow AI agents to:

- Analyze data-quality metadata.
- Detect quality degradation.
- Identify anomalous distributions.
- Detect schema drift.
- Detect missing documentation.
- Recommend remediation.
- Generate quality summaries.

## 4.4 AI Lineage Agent

The system shall allow AI agents to:

- Traverse data lineage.
- Explain upstream dependencies.
- Explain downstream impact.
- Identify affected assets after schema changes.
- Determine transformation paths.
- Detect incomplete lineage.

## 4.5 AI Catalog Assistant

The platform shall provide a natural-language interface allowing authorized users and agents to ask questions such as:

- "Which datasets contain customer information?"
- "Where does this lead score come from?"
- "Which dataset is the freshest?"
- "Which sources contain email addresses?"
- "What downstream systems depend on this table?"
- "Which datasets can I access?"
- "Which datasets contain GDPR-relevant personal data?"
- "Which data source should I use for sales analytics?"

The AI assistant shall never disclose metadata or asset information beyond the caller's authorization scope.

---

## 5. User Requirements

## UR-001 — Centralized Data Discovery

Users shall have a centralized catalog containing discoverable organizational data assets.

## UR-002 — Searchability

Users shall be able to search assets using:

- Dataset name
- Table name
- Column name
- Business term
- Description
- Owner
- Domain
- Tags
- Classification
- Source system
- Data type
- Data quality
- Freshness
- Compliance status

## UR-003 — Human-Readable Metadata

Every published asset shall expose understandable metadata appropriate to the user's authorization level.

## UR-004 — Technical Metadata

Authorized technical users shall be able to inspect:

- Schema
- Columns
- Data types
- Constraints
- Index information
- Partitioning
- Storage information
- Update timestamps
- Source information

## UR-005 — Business Metadata

Users shall be able to view:

- Business definition
- Business purpose
- Domain
- Owner
- Steward
- Usage guidance
- Restrictions
- Approved use cases

## UR-006 — Data Ownership

Every production data asset shall have an assigned owner or explicitly documented ownership state.

## UR-007 — Data Stewardship

The system shall support assignment of data stewards responsible for metadata quality and governance.

## UR-008 — Data Classification

Users shall be able to determine whether an asset contains:

- Public data
- Internal data
- Confidential data
- Restricted data
- Personal data
- Sensitive personal data
- Financial data
- Authentication data
- Security data
- Regulated data

## UR-009 — Data Quality Visibility

Users shall be able to view data-quality indicators associated with cataloged assets.

## UR-010 — Data Freshness

Users shall be able to determine when an asset was last synchronized and when the underlying data was last updated.

## UR-011 — Data Lineage

Authorized users shall be able to trace assets through upstream and downstream dependencies.

## UR-012 — Access Transparency

Users shall be able to determine whether they are authorized to access a dataset and how access can be requested.

## UR-013 — Compliance Visibility

Authorized users shall be able to determine applicable privacy and regulatory classifications.

## UR-014 — Asset Documentation

Users shall be able to create and maintain documentation for approved data assets.

## UR-015 — Dataset Versioning

Users shall be able to identify metadata and schema versions.

## UR-016 — Change Awareness

Users shall be notified of important schema or metadata changes where applicable.

## UR-017 — Dataset Comparison

Authorized users shall be able to compare datasets based on:

- Schema
- Freshness
- Quality
- Ownership
- Classification
- Availability
- Business purpose

## UR-018 — Favorites and Collections

Users shall be able to bookmark frequently used assets and organize them into collections.

## UR-019 — Access Requests

Users shall be able to request access to restricted assets through a governed workflow.

## UR-020 — AI-Assisted Discovery

Users shall be able to discover relevant data using natural-language queries.

## UR-021 — AI Governance

AI agents shall only discover and recommend assets permitted by the requesting identity and tenant policy.

## UR-022 — Metadata Quality

Users shall be able to identify incomplete, stale, inconsistent, or conflicting metadata.

## UR-023 — Duplicate Detection

Users shall be able to identify potentially duplicated or overlapping datasets.

## UR-024 — Regulatory Data Mapping

Compliance users shall be able to map assets to relevant regulatory requirements.

## UR-025 — Auditability

All security-sensitive catalog operations shall be auditable.

---

## 6. System Requirements

## SR-001 — Multi-Tenant Architecture

The catalog shall support strict tenant isolation.

Metadata belonging to one organization shall not be exposed to another organization unless explicitly configured through a trusted cross-tenant mechanism.

## SR-002 — Metadata Repository

The platform shall maintain a centralized metadata repository containing:

- Asset metadata
- Schema metadata
- Ownership metadata
- Classification metadata
- Quality metadata
- Lineage metadata
- Governance metadata
- Access metadata
- Compliance metadata

## SR-003 — Metadata Model

The metadata model shall support:

```text
Organization
 ├── Domain
 │    ├── Data Product
 │    │    ├── Dataset
 │    │    │    ├── Table
 │    │    │    │    ├── Column
 │    │    │    │    └── Constraint
 │    │    │    └── Schema
 │    │    └── Pipeline
 │    └── Data Owner
 └── Policy
```

## SR-004 — Asset Identity

Every catalog asset shall have a globally unique immutable identifier.

Example:

```text
catalog://tenant/{tenant_id}/dataset/{dataset_id}
```

## SR-005 — Asset Types

The system shall support cataloging of:

```text
DATABASE
SCHEMA
TABLE
VIEW
COLUMN
DATASET
DATA_PRODUCT
OBJECT
DOCUMENT
VECTOR_COLLECTION
STREAM
EVENT_TOPIC
API_DATASET
FEATURE_SET
MODEL_DATASET
PIPELINE
DASHBOARD
REPORT
```

## SR-006 — Metadata Versioning

The system shall preserve metadata versions and support historical inspection.

## SR-007 — Schema Versioning

Schema changes shall be versioned independently from business metadata where appropriate.

## SR-008 — Source Connectors

The catalog shall support metadata extraction from configured sources including:

* PostgreSQL
* Data warehouses
* Object storage
* Data lakes
* Vector stores
* Kafka
* CRM systems
* SaaS applications
* Internal APIs

## SR-009 — Metadata Synchronization

The system shall support:

* Scheduled synchronization
* Event-driven synchronization
* Manual synchronization
* Incremental synchronization
* Full synchronization

## SR-010 — Idempotency

Repeated metadata ingestion shall not create duplicate assets.

## SR-011 — Search Index

Catalog metadata shall be indexed for low-latency search.

## SR-012 — Full-Text Search

The catalog shall support full-text and semantic search.

## SR-013 — Semantic Search

The platform shall support embedding-based semantic retrieval for AI-assisted discovery.

## SR-014 — RBAC

Catalog access shall integrate with SalesGenie's RBAC system.

## SR-015 — ABAC

The system should support attribute-based access decisions using attributes such as:

```text
tenant_id
organization_id
role
department
data_classification
asset_owner
purpose
region
environment
agent_identity
```

## SR-016 — Policy Enforcement

Catalog APIs shall enforce authorization server-side.

Client-side filtering shall never be considered a security boundary.

## SR-017 — Sensitive Metadata Protection

Sensitive metadata shall itself be protected.

The catalog shall not expose:

* Credentials
* API keys
* Passwords
* Tokens
* Encryption keys
* Secret values

## SR-018 — Encryption

Catalog metadata shall be encrypted:

* In transit
* At rest
* During authorized service-to-service communication

## SR-019 — Audit Logging

The system shall record security-relevant catalog events.

## SR-020 — Observability

The system shall expose:

* Metrics
* Logs
* Traces
* Synchronization status
* Search latency
* Catalog coverage
* Metadata freshness

## SR-021 — Availability

Catalog services shall be designed for high availability and graceful degradation.

## SR-022 — Fault Isolation

Failure of an individual metadata connector shall not bring down the entire catalog.

## SR-023 — Retry Strategy

Metadata synchronization shall use bounded retries with exponential backoff.

## SR-024 — Dead-Letter Handling

Repeatedly failing metadata ingestion jobs shall be isolated into a recoverable failure state.

## SR-025 — Event-Driven Architecture

Catalog changes should produce domain events such as:

```text
AssetDiscovered
AssetUpdated
AssetDeleted
SchemaChanged
OwnerChanged
ClassificationChanged
QualityChanged
LineageUpdated
AccessPolicyChanged
MetadataSyncFailed
```

## SR-026 — API Architecture

The catalog shall expose authenticated APIs for:

* Asset discovery
* Asset retrieval
* Search
* Metadata management
* Classification
* Lineage
* Quality
* Access requests
* Governance

## SR-027 — AI Gateway Integration

AI agents shall access catalog capabilities through a governed AI gateway rather than directly accessing catalog storage.

## SR-028 — Prompt Security

Natural-language catalog queries shall be protected against prompt injection and indirect instruction attacks.

## SR-029 — AI Authorization

An AI agent shall inherit or receive an explicit authorization context before retrieving catalog information.

## SR-030 — Tenant Context

Every catalog request shall carry an authoritative tenant context.

## SR-031 — Data Residency

The catalog shall support configurable regional metadata storage where required.

## SR-032 — Disaster Recovery

Catalog metadata shall support backup, recovery, and restoration procedures.

## SR-033 — Scalability

The catalog shall support horizontal scaling for:

* Metadata ingestion
* Search
* Lineage processing
* Classification
* AI discovery
* API traffic

---

## 7. Functional Requirements

## 7.1 Asset Registration

## FR-001 — Automatic Asset Discovery

The system shall automatically discover configured data assets.

## FR-002 — Manual Registration

Authorized users shall be able to manually register assets.

## FR-003 — Asset Deduplication

The system shall detect duplicate asset identities during registration.

## FR-004 — Asset Lifecycle

Assets shall support lifecycle states:

```text
DISCOVERED
PENDING_REVIEW
ACTIVE
DEPRECATED
ARCHIVED
DELETED
```

## FR-005 — Asset Deletion

Deleting an underlying source shall not automatically erase historical catalog metadata unless configured by retention policy.

---

## 7.2 Metadata Management

## FR-006 — Metadata CRUD

Authorized users and services shall be able to create, read, update, and archive metadata.

## FR-007 — Metadata Ownership

The system shall allow owners and stewards to be assigned.

## FR-008 — Business Description

Authorized users shall be able to add business descriptions.

## FR-009 — Technical Description

Technical metadata shall be automatically populated where possible.

## FR-010 — Tags

Users shall be able to assign controlled and custom tags.

## FR-011 — Glossary Terms

Catalog assets shall be associated with business glossary terms.

## FR-012 — Metadata Validation

The system shall validate required metadata fields before publishing an asset.

## FR-013 — Metadata Approval

Organizations shall optionally require approval before metadata becomes officially published.

---

## 7.3 Schema Cataloging

## FR-014 — Schema Extraction

The system shall extract source schemas automatically where supported.

## FR-015 — Column Cataloging

The system shall catalog:

* Column name
* Data type
* Nullable status
* Description
* Default value metadata
* Classification
* Business meaning

## FR-016 — Constraint Cataloging

The system shall capture supported:

* Primary keys
* Foreign keys
* Unique constraints
* Check constraints

## FR-017 — Schema Drift Detection

The system shall detect:

* Added columns
* Removed columns
* Renamed columns
* Type changes
* Constraint changes

## FR-018 — Breaking Change Detection

The system shall identify potentially breaking schema changes.

---

## 7.4 Search and Discovery

## FR-019 — Keyword Search

Users shall be able to search by keyword.

## FR-020 — Advanced Search

The system shall support filtering by:

```text
owner
domain
classification
source
asset_type
quality
freshness
tenant
environment
compliance
status
```

## FR-021 — Semantic Search

The system shall support natural-language semantic discovery.

## FR-022 — Search Ranking

Search ranking should consider:

* Relevance
* Ownership
* Popularity
* Freshness
* Quality
* Trust score
* User permissions

## FR-023 — Permission-Aware Search

Unauthorized assets shall not appear in search results unless metadata visibility is explicitly permitted.

## FR-024 — Search Explainability

AI-assisted search should explain why an asset was recommended.

---

## 7.5 Data Classification

## FR-025 — Classification Categories

The system shall support:

```text
PUBLIC
INTERNAL
CONFIDENTIAL
RESTRICTED
PERSONAL_DATA
SENSITIVE_PERSONAL_DATA
FINANCIAL_DATA
AUTHENTICATION_DATA
SECURITY_DATA
REGULATED_DATA
```

## FR-026 — Automatic Classification

AI-assisted classification shall analyze metadata and schema information to recommend classifications.

## FR-027 — Human Review

Human reviewers shall be able to approve, reject, or override AI classifications.

## FR-028 — Classification Confidence

AI classifications shall include confidence scores.

## FR-029 — Classification Evidence

The system shall preserve evidence explaining why a classification was proposed.

## FR-030 — Classification Versioning

Classification decisions shall be versioned and auditable.

---

## 7.6 PII Discovery

## FR-031 — PII Detection

The platform shall identify potential fields such as:

```text
email
phone
name
address
IP address
user identifier
customer identifier
government identifier
financial identifier
```

## FR-032 — Sensitive Data Detection

The system shall support detection of sensitive data categories appropriate to organizational policy.

## FR-033 — AI-Assisted Detection

AI models may assist with semantic detection of sensitive fields.

## FR-034 — Human Validation

High-impact classifications shall support human validation.

---

## 7.7 Data Quality Metadata

## FR-035 — Quality Score

Each supported dataset may have a computed quality score.

## FR-036 — Quality Dimensions

The system shall support:

```text
completeness
accuracy
consistency
validity
uniqueness
timeliness
freshness
availability
```

## FR-037 — Quality History

Quality measurements shall be historically tracked.

## FR-038 — Quality Alerts

Users shall be notified when quality falls below configured thresholds.

---

## 7.8 Data Freshness

## FR-039 — Last Updated Timestamp

The system shall record the latest known data-update timestamp.

## FR-040 — Metadata Freshness

The system shall separately track metadata synchronization time.

## FR-041 — Freshness SLA

Assets may define freshness expectations.

## FR-042 — Freshness Violations

The system shall detect and report freshness SLA violations.

---

## 7.9 Data Lineage

## FR-043 — Upstream Lineage

Users shall be able to identify upstream dependencies.

## FR-044 — Downstream Lineage

Users shall be able to identify downstream consumers.

## FR-045 — Column-Level Lineage

Where supported, the system shall maintain column-level lineage.

## FR-046 — Pipeline Lineage

The system shall associate transformations with pipelines.

## FR-047 — Impact Analysis

Users shall be able to determine potential downstream impact before making schema changes.

## FR-048 — AI Lineage Explanation

AI shall be able to explain lineage in natural language.

---

## 7.10 Data Ownership and Stewardship

## FR-049 — Owner Assignment

Authorized administrators shall assign asset owners.

## FR-050 — Steward Assignment

Authorized administrators shall assign data stewards.

## FR-051 — Ownership Transfer

Ownership shall be transferable with audit history.

## FR-052 — Ownership Validation

The system shall detect assets without valid owners.

## FR-053 — Ownership Notifications

Owners may receive notifications about:

* Quality failures
* Metadata expiration
* Schema changes
* Access requests
* Compliance issues

---

## 7.11 Access Management

## FR-054 — Access Status

The catalog shall show whether the current identity can access an asset.

## FR-055 — Access Request

Users shall be able to request access.

## FR-056 — Approval Workflow

Access requests shall support configurable approval workflows.

## FR-057 — Temporary Access

The system should support time-bound access.

## FR-058 — Purpose-Based Access

Organizations may require users to provide a business purpose.

## FR-059 — AI Access

AI agents shall follow the same authorization policies as human users unless explicitly granted a different controlled service identity.

---

## 7.12 Data Governance

## FR-060 — Governance Policies

Administrators shall define asset governance requirements.

## FR-061 — Required Metadata

Policies shall define mandatory metadata.

## FR-062 — Governance Status

Assets shall expose governance states:

```text
COMPLIANT
NON_COMPLIANT
PENDING_REVIEW
EXEMPT
```

## FR-063 — Policy Violation Detection

The system shall detect assets violating governance rules.

## FR-064 — Remediation Tracking

Governance violations shall support remediation workflows.

---

## 7.13 Compliance

## FR-065 — Regulatory Mapping

Assets shall support mapping to applicable regulatory frameworks.

Potential mappings include:

```text
GDPR
CCPA/CPRA
SOC 2
ISO 27001
HIPAA
PCI DSS
```

Applicability shall depend on organizational scope and legal requirements.

## FR-066 — Processing Purpose

The catalog shall support recording the approved purpose for data processing.

## FR-067 — Retention Metadata

Assets shall include retention-policy metadata where applicable.

## FR-068 — Deletion Requirements

Assets may be associated with deletion requirements.

## FR-069 — Data Subject Mapping

The catalog shall support mapping datasets to data-subject-related processing activities.

---

## 7.14 Dataset Trust

## FR-070 — Trust Score

The system may calculate an asset trust score using:

```text
quality
freshness
ownership
documentation
governance
usage
lineage completeness
security classification
compliance status
```

## FR-071 — Certification

Authorized users shall be able to certify trusted datasets.

## FR-072 — Certification Expiration

Certifications may expire and require revalidation.

## FR-073 — AI Trust Filtering

AI agents shall prefer approved and trusted assets when configured.

---

## 7.15 Dataset Popularity

## FR-074 — Usage Tracking

The system may track authorized catalog usage metrics.

## FR-075 — Popularity Ranking

Search results may consider usage popularity.

## FR-076 — Popularity Privacy

Usage analytics shall not expose sensitive user behavior beyond authorized administrative visibility.

---

## 7.16 Duplicate and Similar Dataset Detection

## FR-077 — Duplicate Detection

The system shall identify potentially duplicate assets.

## FR-078 — Similarity Detection

AI shall identify semantically similar datasets.

## FR-079 — Consolidation Recommendations

The system may recommend consolidation where duplicate datasets create unnecessary complexity.

---

## 7.17 AI Metadata Generation

## FR-080 — AI Descriptions

AI may generate draft dataset descriptions.

## FR-081 — AI Column Descriptions

AI may generate draft semantic column descriptions.

## FR-082 — AI Tags

AI may recommend tags.

## FR-083 — AI Glossary Mapping

AI may recommend business glossary mappings.

## FR-084 — Human Approval

AI-generated metadata shall be clearly identified and may require human approval.

## FR-085 — AI Provenance

The system shall record:

* AI model
* Model version
* Generation timestamp
* Input metadata scope
* Confidence
* Reviewer
* Approval status

---

## 7.18 AI Data Discovery

## FR-086 — Natural-Language Discovery

Authorized users shall be able to ask:

```text
Find customer datasets containing email addresses.
```

## FR-087 — Constraint-Aware Discovery

AI discovery shall respect:

```text
tenant
role
classification
region
purpose
environment
access policy
compliance restrictions
```

## FR-088 — Candidate Ranking

AI shall rank candidate datasets.

## FR-089 — Recommendation Explanation

AI shall provide reasons for recommendations without exposing restricted metadata.

## FR-090 — Safe Retrieval

AI shall retrieve only metadata and data explicitly permitted by policy.

---

## 7.19 AI Agent Governance

## FR-091 — Agent Identity

Every AI agent request shall have an identifiable service or delegated identity.

## FR-092 — Agent Authorization

The catalog shall authorize AI requests before returning metadata.

## FR-093 — Tool-Level Authorization

AI agents shall have permission controls for:

```text
search_catalog
read_asset
read_schema
read_lineage
read_quality
read_classification
request_access
modify_metadata
approve_metadata
```

## FR-094 — Agent Auditability

All AI catalog operations shall be logged.

## FR-095 — Agent Rate Limiting

Catalog AI APIs shall support agent-specific rate limits.

## FR-096 — Agent Abuse Detection

The system shall detect abnormal catalog enumeration by AI agents.

---

## 7.20 Catalog APIs

## FR-097 — Asset API

The platform shall provide APIs for retrieving asset metadata.

## FR-098 — Search API

The platform shall provide authenticated search APIs.

## FR-099 — Lineage API

The platform shall provide lineage APIs.

## FR-100 — Classification API

The platform shall provide classification APIs.

## FR-101 — Quality API

The platform shall provide quality metadata APIs.

## FR-102 — Governance API

The platform shall provide governance metadata APIs.

## FR-103 — Access API

The platform shall provide access-request APIs.

---

## 7.21 Audit Logging

## FR-104 — Catalog Audit Events

The system shall record:

```text
ASSET_CREATED
ASSET_UPDATED
ASSET_DELETED
ASSET_VIEWED
SEARCH_EXECUTED
METADATA_UPDATED
OWNER_CHANGED
CLASSIFICATION_CHANGED
LINEAGE_CHANGED
ACCESS_REQUESTED
ACCESS_APPROVED
ACCESS_DENIED
POLICY_CHANGED
AI_QUERY_EXECUTED
AI_RECOMMENDATION_GENERATED
AI_METADATA_GENERATED
EXPORT_CREATED
```

## FR-105 — Audit Context

Audit records shall include where applicable:

```text
event_id
timestamp
actor_id
actor_type
tenant_id
asset_id
action
result
source_ip
user_agent
request_id
trace_id
```

---

## 7.22 Metadata Export

## FR-106 — Export

Authorized users shall be able to export catalog metadata.

Supported formats may include:

```text
JSON
CSV
Parquet
```

## FR-107 — Export Authorization

Exports shall be subject to the same or stronger authorization controls as interactive access.

## FR-108 — Export Auditing

All sensitive metadata exports shall be logged.

---

## 7.23 Notifications

## FR-109 — Schema Change Notification

Authorized stakeholders may receive notifications about material schema changes.

## FR-110 — Quality Notification

Owners may receive quality alerts.

## FR-111 — Governance Notification

Owners may receive governance violation notifications.

## FR-112 — Access Request Notification

Approvers may receive access-request notifications.

---

## 8. Data Catalog Metadata Model

A catalog asset should support at least the following metadata:

```yaml
asset:
  id: string
  name: string
  fully_qualified_name: string
  asset_type: string
  description: string
  tenant_id: string
  organization_id: string
  domain: string
  environment: string

ownership:
  owner_id: string
  steward_id: string
  team_id: string

source:
  system: string
  connector_type: string
  source_identifier: string
  location: string

schema:
  version: string
  schema_hash: string
  columns: []

classification:
  sensitivity: string
  pii_detected: boolean
  sensitive_data_detected: boolean
  classification_confidence: float

quality:
  score: float
  completeness: float
  accuracy: float
  consistency: float
  validity: float
  uniqueness: float
  freshness: float

lineage:
  upstream_assets: []
  downstream_assets: []
  pipelines: []

governance:
  status: string
  certified: boolean
  certification_expiry: timestamp
  approved_purposes: []

compliance:
  frameworks: []
  retention_policy: string
  deletion_policy: string
  processing_purpose: string

access:
  access_level: string
  policy_id: string
  access_request_required: boolean

lifecycle:
  status: string
  discovered_at: timestamp
  updated_at: timestamp
  deprecated_at: timestamp

ai:
  ai_generated_metadata: boolean
  model_id: string
  model_version: string
  confidence: float
  human_approved: boolean
```

---

## 9. Human Workflow

```text
Human User
    |
    v
Catalog Search
    |
    v
Permission Check
    |
    +---- Denied ----> Access Request
    |
    v
Asset Metadata
    |
    +---- Schema
    +---- Quality
    +---- Lineage
    +---- Classification
    +---- Governance
    +---- Compliance
    |
    v
Authorized Usage
```

---

## 10. AI Workflow

```text
AI Agent
    |
    v
Agent Identity
    |
    v
Authorization Context
    |
    v
Natural Language Query
    |
    v
Prompt / Query Safety Validation
    |
    v
Catalog Semantic Search
    |
    v
Permission Filtering
    |
    v
Candidate Ranking
    |
    v
Quality + Freshness + Trust Evaluation
    |
    v
Recommended Assets
    |
    v
Explain Recommendation
    |
    v
Audit Event
```

---

## 11. Metadata Ingestion Workflow

```text
Data Source
    |
    v
Connector
    |
    v
Metadata Extraction
    |
    v
Normalization
    |
    v
Schema Detection
    |
    v
Classification
    |
    v
Quality Metadata
    |
    v
Lineage Extraction
    |
    v
Metadata Validation
    |
    v
Deduplication
    |
    v
Catalog Repository
    |
    v
Search Index
    |
    v
Governance / Analytics
```

---

## 12. AI + Human Governance Workflow

```text
AI Detection / Recommendation
          |
          v
    Confidence Check
          |
     +----+----+
     |         |
  High       Low
Confidence  Confidence
     |         |
     v         v
Auto Apply   Human Review
     |         |
     +----+----+
          |
          v
     Policy Validation
          |
          v
       Published
          |
          v
       Audit Log
```

---

## 13. Non-Functional Requirements

## NFR-001 — Performance

Catalog search should provide low-latency responses under normal operating conditions.

## NFR-002 — Scalability

The system shall horizontally scale to support millions of catalog assets and high-volume metadata updates.

## NFR-003 — Reliability

Metadata ingestion failures shall not corrupt existing catalog metadata.

## NFR-004 — Consistency

Asset identity and authorization metadata shall maintain strong consistency where security decisions depend on them.

## NFR-005 — Availability

Catalog APIs shall be designed for enterprise-grade availability.

## NFR-006 — Security

The catalog shall follow SalesGenie's zero-trust security architecture.

## NFR-007 — Privacy

Sensitive metadata shall be minimized and exposed only to authorized identities.

## NFR-008 — Observability

All critical catalog services shall expose structured logs, metrics, and traces.

## NFR-009 — Explainability

AI-generated classifications and recommendations shall provide explainable evidence.

## NFR-010 — Reproducibility

AI-generated metadata shall be reproducible or traceable to the model and metadata version used.

## NFR-011 — Disaster Recovery

Catalog metadata shall support defined backup and disaster-recovery objectives.

## NFR-012 — Backward Compatibility

Catalog APIs shall maintain backward compatibility through versioned API contracts.

---

## 14. Security Requirements

## SEC-001 — Zero Trust

No catalog request shall be trusted solely because it originates from an internal service.

## SEC-002 — Authentication

Every protected catalog API shall require authenticated identity.

## SEC-003 — Authorization

Every asset retrieval operation shall perform authorization.

## SEC-004 — Tenant Isolation

Cross-tenant metadata access shall be explicitly prohibited by default.

## SEC-005 — Least Privilege

Users and AI agents shall receive only the minimum catalog permissions required.

## SEC-006 — Sensitive Metadata Protection

The catalog shall not expose secrets or credential material.

## SEC-007 — Encryption

Sensitive catalog metadata shall be encrypted at rest and in transit.

## SEC-008 — Auditability

Security-relevant catalog actions shall be immutable or tamper-evident.

## SEC-009 — Enumeration Protection

The platform shall prevent unauthorized users or AI agents from enumerating restricted assets.

## SEC-010 — Export Controls

Bulk metadata exports shall require authorization and auditing.

## SEC-011 — AI Isolation

AI agents shall not bypass catalog authorization through direct database access.

## SEC-012 — Prompt Injection Defense

Catalog AI interfaces shall treat retrieved metadata as untrusted content and shall prevent metadata from overriding system or security instructions.

---

## 15. Data Quality Requirements

## DQ-001

Required catalog metadata shall be validated before publication.

## DQ-002

The system shall detect stale metadata.

## DQ-003

The system shall detect orphaned assets.

## DQ-004

The system shall detect assets without owners.

## DQ-005

The system shall detect assets without classifications where classification is mandatory.

## DQ-006

The system shall detect incomplete lineage.

## DQ-007

The system shall detect inconsistent business definitions.

## DQ-008

The system shall support configurable metadata-quality thresholds.

## DQ-009

The system shall expose catalog-health metrics.

---

## 16. Governance Requirements

## GOV-001

Every production dataset shall have an owner.

## GOV-002

Sensitive datasets shall have appropriate classification metadata.

## GOV-003

Restricted assets shall have access policies.

## GOV-004

Regulated datasets shall have applicable compliance metadata.

## GOV-005

Deprecated assets shall be clearly marked.

## GOV-006

Certified datasets shall maintain certification metadata.

## GOV-007

AI-generated metadata shall be distinguishable from human-approved metadata.

## GOV-008

Governance exceptions shall have documented justification and expiration.

---

## 17. AI Safety Requirements

## AISEC-001 — Authorization-Aware Retrieval

AI systems shall filter catalog retrieval according to authorization before generation.

## AISEC-002 — Retrieval Isolation

Retrieved metadata shall be treated as untrusted context.

## AISEC-003 — Prompt Injection Resistance

Catalog content shall not be allowed to override AI system instructions.

## AISEC-004 — Sensitive Metadata Redaction

AI responses shall redact unauthorized sensitive metadata.

## AISEC-005 — Hallucination Prevention

AI assistants shall not fabricate nonexistent datasets, schemas, owners, or lineage.

## AISEC-006 — Citation / Provenance

AI-generated answers should identify the catalog assets supporting the answer.

## AISEC-007 — Confidence

AI recommendations should expose confidence when uncertainty is material.

## AISEC-008 — Human Escalation

High-impact governance decisions shall support human approval.

## AISEC-009 — Agent Monitoring

AI catalog usage shall be monitored for abnormal behavior.

## AISEC-010 — Model Governance

AI catalog models shall be versioned and governed.

---

## 18. Compliance Requirements

The Data Catalog shall integrate with SalesGenie's broader compliance architecture and support metadata required for:

```text
GDPR
CCPA / CPRA
SOC 2
ISO 27001
HIPAA
PCI DSS
```

where applicable.

The system shall support:

* Data classification
* Processing-purpose metadata
* Retention metadata
* Deletion metadata
* Data-owner metadata
* Data-steward metadata
* Data-subject mappings
* Cross-border transfer metadata
* Consent-related metadata where applicable
* Regulatory control mappings
* Audit evidence

---

## 19. Metrics and KPIs

The system should measure:

## Catalog Coverage

```text
cataloged_assets / discovered_assets
```

## Metadata Completeness

```text
completed_required_fields / total_required_fields
```

## Ownership Coverage

```text
assets_with_owner / total_production_assets
```

## Classification Coverage

```text
classified_assets / applicable_assets
```

## Lineage Coverage

```text
assets_with_lineage / lineage_applicable_assets
```

## Quality Coverage

```text
assets_with_quality_metadata / applicable_assets
```

## Metadata Freshness

```text
fresh_metadata_assets / total_assets
```

## Search Success Rate

```text
successful_discovery_sessions / total_search_sessions
```

## AI Recommendation Acceptance

```text
accepted_recommendations / total_recommendations
```

## AI Classification Precision

```text
correct_ai_classifications / reviewed_ai_classifications
```

## Governance Compliance

```text
compliant_assets / governed_assets
```

---

## 20. Recommended Catalog Trust Model

The platform may calculate:

```text
TrustScore =
    0.20 * QualityScore
  + 0.15 * FreshnessScore
  + 0.15 * OwnershipScore
  + 0.15 * DocumentationScore
  + 0.10 * GovernanceScore
  + 0.10 * LineageScore
  + 0.10 * CertificationScore
  + 0.05 * UsageReliabilityScore
```

The weights shall be configurable by organization and shall not override authorization policies.

A high trust score shall never grant access to an otherwise unauthorized asset.

---

## 21. API-Level Functional Requirements

Representative APIs:

```text
GET    /api/v1/catalog/assets
GET    /api/v1/catalog/assets/{asset_id}
POST   /api/v1/catalog/assets
PATCH  /api/v1/catalog/assets/{asset_id}
DELETE /api/v1/catalog/assets/{asset_id}

GET    /api/v1/catalog/search
POST   /api/v1/catalog/search/semantic

GET    /api/v1/catalog/assets/{asset_id}/schema
GET    /api/v1/catalog/assets/{asset_id}/lineage
GET    /api/v1/catalog/assets/{asset_id}/quality
GET    /api/v1/catalog/assets/{asset_id}/classification
GET    /api/v1/catalog/assets/{asset_id}/governance
GET    /api/v1/catalog/assets/{asset_id}/compliance

POST   /api/v1/catalog/assets/{asset_id}/access-request

GET    /api/v1/catalog/owners
PATCH  /api/v1/catalog/assets/{asset_id}/owner

POST   /api/v1/catalog/sync
GET    /api/v1/catalog/sync/status

POST   /api/v1/catalog/classification
POST   /api/v1/catalog/lineage/rebuild

GET    /api/v1/catalog/glossary
POST   /api/v1/catalog/glossary

GET    /api/v1/catalog/audit
```

All endpoints shall require appropriate authentication, authorization, tenant isolation, rate limiting, validation, and audit controls.

---

## 22. Database-Level Requirements

The catalog persistence layer should support entities including:

```text
catalog_assets
catalog_asset_versions
catalog_schemas
catalog_columns
catalog_domains
catalog_owners
catalog_stewards
catalog_tags
catalog_glossary_terms
catalog_classifications
catalog_quality_metrics
catalog_lineage_edges
catalog_pipelines
catalog_governance_policies
catalog_compliance_mappings
catalog_access_policies
catalog_access_requests
catalog_certifications
catalog_metadata_sources
catalog_sync_jobs
catalog_sync_errors
catalog_ai_recommendations
catalog_ai_classifications
catalog_audit_events
```

Every tenant-scoped entity shall include an authoritative tenant/organization relationship.

---

## 23. Event Requirements

The catalog should publish events including:

```text
catalog.asset.discovered
catalog.asset.created
catalog.asset.updated
catalog.asset.deprecated
catalog.asset.deleted

catalog.schema.created
catalog.schema.changed
catalog.schema.breaking_change

catalog.classification.created
catalog.classification.updated

catalog.quality.updated
catalog.quality.threshold_breached

catalog.lineage.updated

catalog.governance.violation
catalog.governance.remediated

catalog.access.requested
catalog.access.approved
catalog.access.denied

catalog.ai.recommendation.created
catalog.ai.classification.created

catalog.sync.started
catalog.sync.completed
catalog.sync.failed
```

Events shall contain correlation identifiers and tenant context.

---

## 24. Failure Handling

The system shall:

* Retry transient metadata-source failures.
* Prevent duplicate ingestion.
* Preserve the last known valid metadata state.
* Mark stale metadata explicitly.
* Record connector failures.
* Support dead-letter processing.
* Alert responsible operators.
* Prevent failed ingestion from corrupting catalog state.
* Maintain auditability of failed operations.

---

## 25. Disaster Recovery

The catalog shall support:

* Automated backups
* Point-in-time recovery where supported
* Metadata restoration
* Search-index reconstruction
* Lineage reconstruction
* Configuration backup
* Audit-log preservation
* Cross-region recovery where required

Recovery procedures shall be periodically tested.

---

## 26. Definition of Done

The Data Catalog feature shall be considered production-ready when:

* All supported asset types can be cataloged.
* Assets have immutable identifiers.
* Metadata is searchable.
* Semantic discovery works for authorized users.
* Tenant isolation is enforced.
* RBAC/ABAC authorization is enforced server-side.
* Sensitive metadata is protected.
* PII classification is available.
* Schema versions are tracked.
* Schema drift is detected.
* Lineage is available for supported pipelines.
* Data-quality metadata is available.
* Ownership is enforceable.
* Governance status is visible.
* Compliance mappings are supported.
* Access-request workflows are functional.
* AI recommendations are permission-aware.
* AI-generated metadata is auditable.
* Prompt-injection protections are implemented.
* Catalog actions are audited.
* Metadata synchronization failures are recoverable.
* Catalog APIs are observable.
* Backup and recovery procedures are tested.
* Security testing has passed.
* Performance testing has passed.
* Multi-tenant isolation testing has passed.
* Human and AI workflows have been validated.

---

## 27. Acceptance Criteria

## AC-001 — Discovery

Given an authorized user, when they search for a dataset, the system shall return only assets visible to that user.

## AC-002 — Tenant Isolation

Given two organizations, an identity from Organization A shall never retrieve private catalog metadata belonging to Organization B.

## AC-003 — Schema

Given a registered database, the catalog shall automatically discover supported schemas, tables, and columns.

## AC-004 — Classification

Given a dataset containing identifiable personal-data fields, the system shall identify potential sensitive fields and provide classification metadata.

## AC-005 — Human Review

Given an AI-generated classification, an authorized reviewer shall be able to approve or reject it.

## AC-006 — Lineage

Given a supported transformation pipeline, the catalog shall expose upstream and downstream relationships.

## AC-007 — Quality

Given configured quality metrics, the catalog shall expose quality measurements and historical changes.

## AC-008 — Access Request

Given a restricted dataset, an unauthorized user shall be able to submit an access request instead of directly retrieving the asset.

## AC-009 — AI Discovery

Given an authorized AI agent, the agent shall discover relevant datasets without bypassing access controls.

## AC-010 — AI Security

Given malicious instructions embedded inside dataset metadata, the AI assistant shall treat them as untrusted data and shall not execute them.

## AC-011 — Audit

Given a sensitive catalog operation, the system shall produce an auditable event containing the required actor, tenant, asset, action, and timestamp information.

## AC-012 — Metadata Freshness

Given a failed metadata synchronization job, the catalog shall preserve the last valid metadata and mark the synchronization state appropriately.

## AC-013 — Schema Drift

Given a breaking schema change, the system shall detect the change and make the impact available to authorized users.

## AC-014 — Governance

Given an asset without required governance metadata, the system shall identify it as non-compliant or pending review according to policy.

## AC-015 — AI Provenance

Given AI-generated metadata, the catalog shall preserve model/version and generation metadata sufficient for audit and review.

---

## 28. FAANG-Level Design Principles

The implementation shall follow these principles:

1. **Security is enforced at the service boundary.**
2. **Authorization is evaluated before metadata disclosure.**
3. **Tenant isolation is mandatory.**
4. **Metadata is treated as a first-class data product.**
5. **Every important asset has an owner.**
6. **Every important transformation has lineage.**
7. **Sensitive data is classified automatically and reviewable by humans.**
8. **AI recommendations never override authorization.**
9. **AI-generated metadata is treated as probabilistic until governed.**
10. **Human approval is required for high-impact governance decisions.**
11. **Catalog state is versioned and auditable.**
12. **Metadata ingestion is idempotent.**
13. **Catalog failures are isolated from production data systems.**
14. **Search is permission-aware by design.**
15. **Data quality and freshness are first-class catalog attributes.**
16. **Compliance metadata is machine-readable.**
17. **AI agents consume catalog capabilities through controlled APIs/tools.**
18. **No secret or credential belongs in the catalog.**
19. **Observability is mandatory for every critical catalog operation.**
20. **The catalog is the governed discovery layer, not an authorization bypass.**

---

## 29. Final Requirement

SalesGenie's Data Catalog shall function as the authoritative metadata and governed discovery layer for the platform, providing a unified interface through which humans and AI agents can discover, understand, evaluate, govern, and safely consume data assets while maintaining strict tenant isolation, authorization, security, privacy, compliance, lineage, quality, provenance, and auditability.
