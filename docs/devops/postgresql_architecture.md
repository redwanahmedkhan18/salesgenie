# SalesGenie — PostgreSQL Architecture Requirements

## 1. Document Purpose

This document defines the **User Requirements (UR)**, **System Requirements (SR)**, and **Functional Requirements (FR)** for the PostgreSQL architecture of **SalesGenie**, an enterprise-grade AI-powered customer support, sales, lead intelligence, workflow automation, analytics, and multi-agent platform.

The PostgreSQL architecture must support:

- Multi-tenant SaaS architecture
- AI and human workflows
- Customer support operations
- Sales and CRM operations
- Lead intelligence
- Multi-agent AI orchestration
- RAG and knowledge management metadata
- Omnichannel conversations
- Workflow automation
- Analytics and event processing
- Billing and subscriptions
- RBAC and authorization
- Developer APIs and service accounts
- Audit and compliance
- Notifications
- Enterprise search metadata
- High availability and disaster recovery
- Horizontal application scaling
- Large-scale transactional workloads

---

## 2. Product Context

SalesGenie is an enterprise AI platform where organizations can:

1. Register and manage organizations.
2. Create teams, departments, and workspaces.
3. Manage users, roles, and permissions.
4. Configure AI agents.
5. Deploy human and AI customer-support agents.
6. Manage leads, contacts, accounts, opportunities, and sales pipelines.
7. Connect external communication channels.
8. Manage conversations and messages.
9. Execute AI and human workflows.
10. Store operational metadata.
11. Manage knowledge bases and RAG resources.
12. Generate analytics and business intelligence.
13. Manage subscriptions, invoices, quotas, and usage.
14. Integrate with external systems.
15. Expose APIs, webhooks, SDKs, and developer resources.
16. Maintain security, audit, compliance, and governance records.

PostgreSQL is the authoritative transactional database for the platform.

---

## 3. Architectural Principles

The PostgreSQL architecture SHALL follow these principles:

- Multi-tenancy by design
- Strong transactional consistency
- Explicit data ownership
- Referential integrity
- Least-privilege access
- Defense in depth
- Schema normalization for transactional data
- Controlled denormalization for read-heavy workloads
- Immutable audit records
- Idempotent writes
- Optimistic concurrency where appropriate
- Explicit transaction boundaries
- Online migration capability
- High availability
- Point-in-time recovery
- Encryption in transit and at rest
- Horizontal application scalability
- Read/write workload separation
- Partitioning for high-volume tables
- Observability-first database operations
- Zero-trust database access
- Disaster recovery readiness
- Backward-compatible schema evolution

---

## 4. User Requirements

## UR-001 — Organization Data Isolation

The system SHALL allow every organization to securely store and access its own PostgreSQL data without unauthorized access to another organization.

## UR-002 — User Management

Authorized administrators SHALL be able to create, update, deactivate, and manage users whose operational data is persisted in PostgreSQL.

## UR-003 — Role Management

Administrators SHALL be able to define and assign roles and permissions.

Supported roles SHOULD include:

- Super Admin
- Organization Admin
- Security Admin
- Billing Admin
- Sales Manager
- Sales Agent
- Support Manager
- Support Agent
- AI Agent Manager
- Workflow Manager
- Analyst
- Developer
- Auditor
- Read-only User
- Custom Enterprise Role

## UR-004 — Customer Management

Users SHALL be able to manage:

- Customers
- Contacts
- Companies
- Accounts
- Leads
- Opportunities
- Deals
- Customer attributes
- Customer interaction history

## UR-005 — Conversation Persistence

Users SHALL be able to access persistent conversation records across supported communication channels.

## UR-006 — Omnichannel Data

The platform SHALL persist metadata for interactions originating from channels such as:

- Web chat
- Email
- SMS
- WhatsApp
- Voice
- Social channels
- API
- Mobile applications
- Internal agent interfaces

## UR-007 — AI Agent Management

Authorized users SHALL be able to create, configure, activate, deactivate, and monitor AI agents.

## UR-008 — Human Agent Management

Managers SHALL be able to assign conversations, leads, tickets, and tasks to human agents.

## UR-009 — Hybrid AI-Human Operations

Users SHALL be able to transition work between:

- AI agent → human agent
- Human agent → AI agent
- AI agent → AI agent
- Human agent → human agent

## UR-010 — Lead Management

Sales users SHALL be able to create and manage lead records, lead statuses, lead scores, sources, ownership, and lifecycle stages.

## UR-011 — Pipeline Management

Sales managers SHALL be able to manage sales pipelines, stages, opportunities, values, probability, ownership, and historical changes.

## UR-012 — Workflow Persistence

Users SHALL be able to create, configure, execute, pause, resume, and monitor workflows.

## UR-013 — Knowledge Base Metadata

Authorized users SHALL be able to manage:

- Knowledge bases
- Documents
- Document versions
- Chunks
- Embedding metadata
- Sources
- Permissions
- Ingestion status

## UR-014 — Analytics Data

Authorized users SHALL be able to retrieve operational and analytical metrics derived from platform activity.

## UR-015 — KPI Management

Business users SHALL be able to define and monitor KPIs.

## UR-016 — Billing Data

Billing administrators SHALL be able to manage:

- Plans
- Subscriptions
- Invoices
- Payments metadata
- Usage
- Limits
- Entitlements

## UR-017 — Developer Access

Developers SHALL be able to manage:

- API keys
- Service accounts
- OAuth clients
- Webhooks
- API usage
- Developer projects

## UR-018 — Auditability

Security and compliance users SHALL be able to inspect historical security-sensitive activities.

## UR-019 — Search

Authorized users SHALL be able to search platform data according to their permissions.

## UR-020 — Data Export

Authorized users SHALL be able to export organization-owned data subject to authorization policies.

## UR-021 — Data Retention

Administrators SHALL be able to configure retention policies according to organizational requirements.

## UR-022 — Data Recovery

Platform operators SHALL be able to recover database data following infrastructure or application failures.

## UR-023 — Enterprise Reliability

Users SHALL experience database-backed services with minimal disruption during routine infrastructure operations.

## UR-024 — Consistent Transactions

Users SHALL receive consistent results when performing operations involving multiple related records.

## UR-025 — Historical Data

Users SHALL be able to inspect relevant historical state, activity, and audit information without modifying immutable historical records.

---

## 5. System Requirements

## 5.1 Database Platform

### SR-001

The system SHALL use PostgreSQL as the primary relational transactional database.

### SR-002

The PostgreSQL deployment SHALL use a supported production-grade PostgreSQL version.

### SR-003

Database configuration SHALL be version-controlled through infrastructure-as-code and deployment configuration.

### SR-004

Development, staging, and production databases SHALL be logically isolated.

### SR-005

Production credentials SHALL never be embedded in source code.

---

## 6. Multi-Tenant Database Requirements

## SR-006 — Tenant Identification

Core tenant-owned tables SHALL contain an organization/tenant identifier.

Recommended field:

```text
organization_id UUID NOT NULL
```

## SR-007 — Tenant Isolation

Application queries SHALL enforce tenant boundaries.

## SR-008 — Row-Level Security

PostgreSQL Row-Level Security SHOULD be used for high-risk tenant-owned tables where operationally appropriate.

## SR-009 — Tenant Context

Database sessions MAY establish a trusted tenant context for RLS enforcement.

Example conceptual context:

```text
app.organization_id
app.user_id
app.role
```

## SR-010 — Cross-Tenant Access

Cross-tenant queries SHALL be prohibited by default.

Only explicitly authorized platform-level services SHALL access multiple tenants.

## SR-011 — Super Admin Isolation

Super Admin operations SHALL use explicitly authorized platform-level database access paths rather than bypassing tenant isolation accidentally.

---

## 7. Database Schema Requirements

## SR-012 — Schema Organization

The database SHOULD use logical PostgreSQL schemas for bounded domains where appropriate.

Recommended domains:

```text
identity
organizations
crm
conversations
support
sales
agents
workflows
knowledge
analytics
billing
notifications
integrations
developers
security
audit
platform
```

## SR-013 — Domain Ownership

Each database domain SHALL have an identifiable service or team owner.

## SR-014 — Foreign Keys

Relationships requiring strong referential integrity SHALL use foreign keys.

## SR-015 — UUIDs

Distributed entities SHOULD use UUID/UUIDv7-compatible identifiers where appropriate.

## SR-016 — Timestamps

Transactional entities SHALL maintain timestamps such as:

```text
created_at
updated_at
```

Time SHALL be stored in UTC.

## SR-017 — Soft Deletion

Entities requiring recoverability SHOULD use controlled soft deletion:

```text
deleted_at
deleted_by
```

Hard deletion SHALL be restricted.

## SR-018 — Versioning

Mutable business-critical entities SHOULD maintain version information for optimistic concurrency.

---

## 8. Core Entity Requirements

The architecture SHOULD support entities including:

```text
organizations
organization_settings
users
user_profiles
teams
departments
roles
permissions
role_permissions
user_roles

customers
contacts
companies
accounts
leads
lead_scores
lead_sources
opportunities
deals
pipelines
pipeline_stages

conversations
conversation_participants
conversation_assignments
messages
message_attachments
conversation_events

ai_agents
ai_agent_versions
agent_configs
agent_sessions
agent_runs
agent_actions

workflows
workflow_versions
workflow_nodes
workflow_edges
workflow_runs
workflow_tasks
workflow_events

knowledge_bases
documents
document_versions
document_chunks
embedding_metadata

tickets
ticket_comments
ticket_assignments
ticket_events

campaigns
campaign_members
marketing_events

analytics_events
metric_definitions
metric_values
kpi_definitions
kpi_results

subscriptions
plans
entitlements
usage_records
invoices

notifications
notification_templates
notification_preferences
notification_deliveries

api_keys
service_accounts
oauth_clients
webhooks
webhook_deliveries
api_usage

integrations
integration_connections
integration_credentials_metadata

audit_logs
security_events
compliance_events
```

---

## 9. Functional Requirements

## FR-001 — Organization Creation

The system SHALL create a unique organization record when a new tenant is provisioned.

## FR-002 — Organization Lifecycle

The system SHALL support:

```text
pending
active
suspended
restricted
deleted
```

organization states.

## FR-003 — User Persistence

The system SHALL persist user identity metadata and organization membership.

## FR-004 — User Status

Users SHALL support lifecycle states such as:

```text
invited
active
suspended
deactivated
deleted
```

## FR-005 — Role Assignment

The system SHALL persist user-role assignments with organization scope.

## FR-006 — Permission Evaluation

The authorization layer SHALL resolve effective permissions using PostgreSQL-backed RBAC metadata.

## FR-007 — Customer Creation

The system SHALL persist customer records with organization ownership.

## FR-008 — Contact Management

The system SHALL support multiple contacts associated with a customer/company.

## FR-009 — Lead Creation

The system SHALL persist lead information including:

```text
lead_id
organization_id
source
status
owner_id
score
created_at
updated_at
```

## FR-010 — Lead History

Lead status, owner, score, and lifecycle changes SHALL be historically trackable.

## FR-011 — Opportunity Management

The system SHALL persist opportunity lifecycle and sales pipeline information.

## FR-012 — Pipeline Stages

The system SHALL support configurable organization-specific sales pipeline stages.

## FR-013 — Conversation Creation

The system SHALL create persistent conversation records.

## FR-014 — Message Persistence

The system SHALL persist message metadata and content according to configured retention policies.

## FR-015 — Message Ordering

The system SHALL maintain deterministic ordering for messages within conversations.

## FR-016 — Message Idempotency

Duplicate message submissions SHALL be prevented through idempotency mechanisms.

## FR-017 — Human Assignment

The system SHALL persist human agent assignments.

## FR-018 — AI Assignment

The system SHALL persist AI-agent assignments and ownership states.

## FR-019 — Assignment History

Conversation assignment changes SHALL be historically recorded.

## FR-020 — AI Agent Configuration

The system SHALL persist:

```text
agent identity
agent version
model provider
model identifier
system configuration
tools
policies
knowledge sources
temperature/configuration metadata
status
```

Sensitive credentials SHALL NOT be stored directly in ordinary configuration tables.

## FR-021 — AI Agent Versioning

AI agent configurations SHALL support immutable versions.

## FR-022 — AI Execution Records

The system SHALL persist AI execution metadata including:

```text
run_id
agent_id
conversation_id
model
status
started_at
completed_at
latency
token_usage
error_code
```

## FR-023 — AI-Human Handoff

The system SHALL persist AI-to-human and human-to-AI handoff events.

## FR-024 — Workflow Definition

The system SHALL persist workflow definitions independently from workflow executions.

## FR-025 — Workflow Versioning

Published workflow versions SHALL be immutable.

## FR-026 — Workflow Execution

The system SHALL persist workflow execution state.

Supported states SHOULD include:

```text
queued
running
paused
waiting
completed
failed
cancelled
timed_out
```

## FR-027 — Workflow Idempotency

Workflow tasks SHALL support idempotency keys.

## FR-028 — Workflow Retry

The system SHALL persist retry metadata.

## FR-029 — Knowledge Base Management

The system SHALL persist knowledge-base metadata and document lifecycle states.

## FR-030 — Document Versioning

Documents SHALL support immutable versions.

## FR-031 — Chunk Metadata

The database SHALL store metadata necessary to locate and authorize document chunks.

Large vector data SHOULD be managed using an appropriate vector database or PostgreSQL vector extension depending on deployment scale.

## FR-032 — Ticket Management

The system SHALL persist customer-support tickets and their lifecycle.

## FR-033 — Ticket Assignment

Tickets SHALL support AI and human assignment.

## FR-034 — Ticket History

Ticket lifecycle transitions SHALL be historically persisted.

---

## 10. Analytics Requirements

## FR-035 — Analytics Event Storage

The system SHALL support persistence of analytics events.

Example:

```text
event_id
organization_id
actor_id
event_type
entity_type
entity_id
timestamp
metadata
source
session_id
```

## FR-036 — High-Volume Event Partitioning

Large analytics/event tables SHALL support time-based partitioning.

Example:

```text
analytics_events_2026_01
analytics_events_2026_02
analytics_events_2026_03
```

## FR-037 — Metric Definitions

The system SHALL persist reusable metric definitions.

## FR-038 — KPI Definitions

The system SHALL persist configurable KPI definitions.

## FR-039 — Aggregated Metrics

Frequently requested analytics SHOULD use pre-aggregated tables/materialized views rather than repeatedly scanning raw transactional tables.

## FR-040 — Analytics Isolation

Heavy analytics workloads SHALL NOT unnecessarily degrade transactional workloads.

Read replicas, analytical stores, materialized views, or dedicated warehouses SHOULD be used as scale requires.

---

## 11. Billing Requirements

## FR-041 — Plan Management

The system SHALL persist subscription plan metadata.

## FR-042 — Subscription Management

The system SHALL support subscription lifecycle states.

## FR-043 — Usage Tracking

The system SHALL persist usage information for billable resources.

Examples:

```text
AI tokens
API requests
messages
conversations
workflow executions
storage
voice minutes
knowledge documents
seats
```

## FR-044 — Quota Enforcement

The platform SHALL support database-backed quota configuration and enforcement metadata.

## FR-045 — Invoice Records

Invoice metadata SHALL be persisted with immutable identifiers.

## FR-046 — Billing Auditability

Billing state changes SHALL be auditable.

---

## 12. Notification Requirements

## FR-047 — Notification Persistence

The system SHALL persist notification records.

## FR-048 — Notification Preferences

Users SHALL have configurable notification preferences.

## FR-049 — Notification Delivery

The system SHALL persist delivery attempts and statuses.

Supported states:

```text
queued
processing
sent
delivered
failed
cancelled
```

## FR-050 — Notification Idempotency

Duplicate notifications SHALL be prevented where required.

---

## 13. Developer Platform Requirements

## FR-051 — API Key Storage

The system SHALL persist API key metadata.

Raw API secrets SHALL NOT be stored in plaintext.

## FR-052 — API Key Hashing

API secrets SHALL be securely hashed or represented using an equivalent one-way mechanism.

## FR-053 — Service Accounts

The system SHALL support service-account records.

## FR-054 — Webhooks

The system SHALL persist webhook configurations.

## FR-055 — Webhook Delivery

Webhook delivery attempts SHALL be persisted for observability and retry processing.

## FR-056 — API Usage

The system SHALL persist API usage metadata.

## FR-057 — API Versioning

API consumers SHALL be associated with supported API versions where required.

---

## 14. Audit and Security Requirements

## FR-058 — Audit Logging

Security-sensitive operations SHALL generate audit records.

Examples:

```text
login
logout
failed_login
role_change
permission_change
api_key_created
api_key_revoked
user_suspended
organization_suspended
billing_change
data_export
data_deletion
configuration_change
```

## FR-059 — Immutable Audit Logs

Audit records SHALL be append-only from the application perspective.

## FR-060 — Actor Attribution

Audit records SHALL identify:

```text
actor_id
organization_id
action
resource_type
resource_id
timestamp
request_id
ip_metadata
user_agent_metadata
result
```

## FR-061 — AI Auditability

AI-generated business actions SHALL be distinguishable from human actions.

Example:

```text
actor_type = ai
actor_id = agent_uuid
```

## FR-062 — Human Auditability

Human actions SHALL preserve the responsible user identity.

## FR-063 — System Actions

Automated background jobs SHALL be represented using system/service identities.

---

## 15. AI-Specific Database Requirements

## FR-064 — AI Attribution

Every AI-generated business action SHOULD contain:

```text
agent_id
agent_version_id
model_provider
model_id
execution_id
```

## FR-065 — AI Decision Metadata

Where legally and operationally appropriate, the platform SHALL persist metadata explaining the source and context of AI actions.

## FR-066 — AI Tool Calls

Tool invocation metadata SHALL be persistable.

## FR-067 — AI Execution State

AI execution records SHALL support:

```text
queued
running
completed
failed
cancelled
timed_out
```

## FR-068 — Token Usage

AI execution metadata SHOULD support:

```text
input_tokens
output_tokens
total_tokens
cached_tokens
reasoning_tokens
```

where supplied by the model provider.

## FR-069 — AI Cost Attribution

AI execution records SHOULD support estimated cost attribution.

## FR-070 — AI-Human Collaboration

The database SHALL support correlation between AI actions and subsequent human actions.

---

## 16. Transaction Requirements

## SR-019 — ACID Transactions

Critical business operations SHALL use PostgreSQL ACID transactions.

## SR-020 — Transaction Boundaries

Transactions SHALL be short-lived and scoped to a single business operation where possible.

## SR-021 — Isolation

The platform SHALL use an appropriate PostgreSQL transaction isolation level.

Default behavior SHOULD use:

```text
READ COMMITTED
```

Higher isolation levels SHALL be used only where business correctness requires them.

## SR-022 — Deadlock Handling

The application SHALL detect and retry safe transactions affected by transient deadlocks.

## SR-023 — Idempotency

Critical externally triggered operations SHALL support idempotency keys.

---

## 17. Indexing Requirements

## SR-024 — Primary Keys

All major entities SHALL have indexed primary keys.

## SR-025 — Tenant Indexing

Tenant-owned high-volume tables SHALL include indexes beginning with:

```text
organization_id
```

where appropriate.

## SR-026 — Time-Series Indexing

Event tables SHALL support indexes optimized for:

```text
organization_id
timestamp
event_type
```

## SR-027 — Foreign-Key Indexing

Foreign-key columns used in joins and filters SHALL be appropriately indexed.

## SR-028 — Composite Indexes

Composite indexes SHALL reflect actual production query patterns.

## SR-029 — Partial Indexes

Partial indexes SHOULD be used for frequently queried subsets.

Example:

```text
WHERE deleted_at IS NULL
```

## SR-030 — JSONB Indexes

JSONB columns SHALL use GIN or specialized indexes only where query patterns justify them.

## SR-031 — Index Governance

Unused and redundant indexes SHALL be periodically identified and removed.

---

## 18. PostgreSQL Data Types

## SR-032

The architecture SHALL use PostgreSQL-native types where they improve correctness.

Preferred examples:

```text
UUID
TIMESTAMPTZ
DATE
BOOLEAN
INTEGER
BIGINT
NUMERIC
TEXT
JSONB
BYTEA
ARRAY
ENUM
```

## SR-033

Financial values SHALL use `NUMERIC` rather than floating-point types.

## SR-034

Time-sensitive records SHALL use `TIMESTAMPTZ`.

## SR-035

Flexible metadata SHALL use JSONB only when schema flexibility is genuinely required.

---

## 19. JSONB Requirements

## FR-071

The system MAY store extensible metadata using JSONB.

Examples:

```text
event_metadata
integration_metadata
provider_metadata
custom_fields
ai_metadata
workflow_metadata
```

## FR-072

Core business attributes SHALL NOT be hidden inside JSONB when they require:

* Referential integrity
* Frequent filtering
* Sorting
* Unique constraints
* Strong typing
* Reporting

## FR-073

JSONB indexes SHALL be created only for demonstrated query patterns.

---

## 20. Database Constraints

## FR-074 — NOT NULL Constraints

Mandatory fields SHALL use `NOT NULL`.

## FR-075 — Unique Constraints

Uniqueness-critical fields SHALL use database-level unique constraints.

## FR-076 — Check Constraints

Business invariants that can safely be enforced at the database layer SHOULD use CHECK constraints.

## FR-077 — Referential Integrity

Critical entity relationships SHALL use foreign keys.

## FR-078 — Cascading Deletes

Cascading deletes SHALL be used cautiously and prohibited for critical historical records.

---

## 21. Concurrency Requirements

## FR-079

The system SHALL support concurrent updates from multiple users, AI agents, workers, and integrations.

## FR-080

Optimistic locking SHOULD be implemented for frequently edited business objects.

Example:

```text
version
updated_at
```

## FR-081

Pessimistic locking SHALL be used only for operations where concurrent execution could corrupt business state.

## FR-082

Distributed workers SHALL use safe locking mechanisms for shared jobs.

PostgreSQL advisory locks MAY be used where appropriate.

---

## 22. Connection Management

## SR-036

Application services SHALL use connection pooling.

## SR-037

Each microservice SHALL avoid maintaining excessive independent database connections.

## SR-038

PgBouncer SHOULD be used for high-connection environments.

## SR-039

Connection limits SHALL be configured based on:

```text
database capacity
CPU
RAM
connection pool size
service count
worker count
replica count
```

## SR-040

Database connections SHALL have appropriate:

```text
connect_timeout
statement_timeout
idle_in_transaction_session_timeout
```

settings.

---

## 23. Microservices Database Architecture

## SR-041

SalesGenie microservices SHALL NOT freely modify each other's database tables.

## SR-042

Each bounded service SHOULD own its database schema or logical data domain.

## SR-043

Cross-service data access SHOULD occur through:

* APIs
* Events
* Read models
* Controlled database interfaces

rather than uncontrolled table access.

## SR-044

Shared database access SHALL NOT create hidden coupling between independent services.

## SR-045

Service ownership SHALL be documented for every production table.

---

## 24. Event-Driven Integration

## FR-083

Database state changes that require asynchronous processing SHALL generate domain events.

Examples:

```text
lead.created
lead.updated
conversation.created
message.received
ticket.created
ticket.assigned
workflow.started
workflow.completed
agent.run.completed
subscription.updated
invoice.created
user.created
```

## FR-084

Event publishing SHALL support reliable delivery.

## FR-085

The system SHOULD use an Outbox Pattern for transactional event publication.

## FR-086

Outbox records SHALL support:

```text
event_id
aggregate_type
aggregate_id
event_type
payload
created_at
published_at
attempt_count
status
```

## FR-087

Consumers SHALL support idempotent event processing.

---

## 25. High Availability Requirements

## SR-046

Production PostgreSQL SHALL support high availability.

## SR-047

The architecture SHOULD use:

```text
Primary
   |
   +---- Read Replica
   |
   +---- Standby / Failover Replica
```

## SR-048

Automatic failover SHOULD be supported.

## SR-049

Database health SHALL be continuously monitored.

## SR-050

Failover procedures SHALL be tested periodically.

---

## 26. Read Replica Requirements

## FR-088

Read-heavy workloads MAY use PostgreSQL read replicas.

Candidate workloads:

```text
analytics
dashboards
search
reporting
admin dashboards
historical queries
BI
```

## FR-089

Strongly consistent workflows SHALL read from the primary when required.

## FR-090

The application SHALL account for replication lag.

---

## 27. Partitioning Requirements

## SR-051

High-volume tables SHALL be evaluated for partitioning.

Potential candidates:

```text
analytics_events
audit_logs
message_events
workflow_events
ai_execution_logs
api_usage
notification_deliveries
webhook_deliveries
```

## SR-052

Time-based partitioning SHOULD be preferred for append-heavy historical data.

## SR-053

Partition retention SHALL be automated where legally permissible.

## SR-054

Partition maintenance SHALL not interrupt production workloads.

---

## 28. Archival Requirements

## FR-091

Historical records exceeding hot-storage requirements SHALL support archival.

## FR-092

Archived data SHALL retain tenant ownership and security metadata.

## FR-093

Archival SHALL preserve data integrity.

## FR-094

Archived records SHALL remain recoverable according to retention policy.

---

## 29. Backup Requirements

## SR-055

Production databases SHALL have automated backups.

## SR-056

Backups SHALL include:

```text
full backups
incremental/WAL backups
configuration metadata
```

where supported.

## SR-057

Point-in-time recovery SHALL be supported.

## SR-058

Backup retention SHALL comply with organizational policy.

## SR-059

Backups SHALL be encrypted.

## SR-060

Backup access SHALL follow least privilege.

## SR-061

Restore procedures SHALL be tested periodically.

---

## 30. Disaster Recovery Requirements

## SR-062

The database architecture SHALL define:

```text
RPO
RTO
```

targets per environment and service criticality.

## SR-063

Production SHALL support recovery from:

* Database corruption
* Instance failure
* Availability-zone failure
* Region-level failure where required
* Accidental deletion
* Application-level data corruption

## SR-064

Disaster recovery SHALL include documented runbooks.

---

## 31. Security Requirements

## SR-065 — Encryption in Transit

All production database connections SHALL use TLS.

## SR-066 — Encryption at Rest

Production database storage and backups SHALL be encrypted at rest.

## SR-067 — Least Privilege

Applications SHALL receive only the database permissions they require.

## SR-068 — Separate Credentials

Services SHALL use separate database credentials.

## SR-069 — Credential Rotation

Database credentials SHALL support automated rotation.

## SR-070 — Secret Management

Credentials SHALL be stored in a dedicated secrets-management system.

## SR-071 — Administrative Access

Direct production database access SHALL be restricted to authorized personnel.

## SR-072 — Audit Database Access

Privileged database operations SHALL be auditable.

---

## 32. Row-Level Security Requirements

## FR-095

RLS policies SHALL enforce tenant isolation for selected high-risk tables.

Conceptual policy:

```sql
organization_id = current_setting('app.organization_id')::uuid
```

## FR-096

RLS SHALL distinguish:

```text
tenant users
service accounts
platform administrators
background workers
auditors
```

## FR-097

RLS policies SHALL be tested against cross-tenant access scenarios.

## FR-098

No application feature SHALL depend on disabling RLS accidentally.

---

## 33. Migration Requirements

## FR-099

All schema changes SHALL be version-controlled.

## FR-100

Database migrations SHALL be deterministic.

## FR-101

Migrations SHALL support:

```text
development
testing
staging
production
```

## FR-102

Destructive migrations SHALL require explicit review.

## FR-103

Production migrations SHOULD follow expand-and-contract patterns.

## FR-104

Large table migrations SHALL avoid long blocking locks.

## FR-105

Migration failures SHALL have a recovery strategy.

---

## 34. Zero-Downtime Migration Pattern

Production schema changes SHOULD follow:

```text
Phase 1:
Add new nullable structure

Phase 2:
Deploy backward-compatible application

Phase 3:
Backfill data

Phase 4:
Enable new application behavior

Phase 5:
Validate data

Phase 6:
Remove legacy structure
```

---

## 35. Data Integrity Requirements

## FR-106

The database SHALL enforce critical invariants.

## FR-107

Duplicate customer identifiers SHALL be prevented according to tenant-specific business rules.

## FR-108

Duplicate external integration identifiers SHALL be prevented where applicable.

## FR-109

Billing records SHALL maintain immutable financial identifiers.

## FR-110

Audit records SHALL preserve original event timestamps.

## FR-111

AI execution records SHALL preserve immutable execution identifiers.

---

## 36. External Integration Requirements

## FR-112

Integration records SHALL support external system identifiers.

Examples:

```text
hubspot_contact_id
salesforce_account_id
zendesk_ticket_id
gmail_thread_id
slack_channel_id
notion_page_id
```

## FR-113

External IDs SHALL support tenant-scoped uniqueness where appropriate.

## FR-114

Synchronization state SHALL be persisted.

Example:

```text
last_synced_at
sync_cursor
sync_status
sync_error
```

## FR-115

Integration synchronization SHALL be idempotent.

---

## 37. Search Requirements

## FR-116

PostgreSQL SHALL support basic structured search.

## FR-117

Full-text search MAY use PostgreSQL capabilities for appropriate workloads.

## FR-118

Enterprise-scale semantic search SHALL use an appropriate search/vector infrastructure when PostgreSQL alone becomes insufficient.

## FR-119

Search indexes SHALL respect tenant and RBAC boundaries.

---

## 38. Performance Requirements

## SR-073

Common OLTP queries SHOULD normally complete within low tens of milliseconds under normal production load.

## SR-074

Database query latency SHALL be monitored using percentile metrics:

```text
P50
P95
P99
P99.9
```

## SR-075

Slow queries SHALL be identifiable.

## SR-076

Production SHALL monitor:

```text
CPU
RAM
IOPS
disk latency
connections
locks
deadlocks
cache hit ratio
replication lag
WAL generation
transaction rate
query latency
```

## SR-077

Query plans SHALL be analyzed for critical queries.

---

## 39. Query Optimization Requirements

## FR-120

The platform SHALL identify slow queries using PostgreSQL monitoring tooling.

## FR-121

Critical queries SHALL be analyzed with:

```text
EXPLAIN
EXPLAIN ANALYZE
```

## FR-122

The application SHALL avoid:

```text
N+1 queries
unbounded SELECT *
large OFFSET pagination
unindexed tenant scans
unbounded joins
long-running transactions
```

## FR-123

Cursor/keyset pagination SHOULD be used for large datasets.

---

## 40. Caching Integration

## FR-124

Frequently accessed, rarely changing database data MAY be cached in Redis.

Candidates include:

```text
permissions
organization configuration
feature flags
plan metadata
agent configuration
workflow configuration
```

## FR-125

Database SHALL remain the authoritative source for persistent state.

## FR-126

Cache invalidation SHALL occur when authoritative records change.

---

## 41. PostgreSQL + Redis Consistency

## FR-127

Redis SHALL NOT be treated as the source of truth for transactional records.

## FR-128

Cache writes SHALL not commit business state independently from PostgreSQL unless explicitly designed.

## FR-129

Critical state transitions SHALL be committed to PostgreSQL before asynchronous cache propagation.

---

## 42. Observability Requirements

## SR-078

Database observability SHALL include:

```text
database availability
query latency
query throughput
connection utilization
lock contention
deadlocks
replication lag
disk usage
WAL growth
checkpoint behavior
vacuum health
autovacuum activity
table bloat
index bloat
```

## SR-079

Database metrics SHALL integrate with the platform observability stack.

## SR-080

Alerts SHALL be configured for critical database conditions.

---

## 43. Logging Requirements

## FR-130

Database-related application logs SHALL include:

```text
request_id
trace_id
organization_id
service_name
operation
duration
status
```

## FR-131

Sensitive data SHALL never appear in SQL or application logs.

## FR-132

Database errors SHALL be mapped to safe application-level errors.

---

## 44. PostgreSQL Maintenance Requirements

## SR-081

Autovacuum SHALL be enabled and appropriately configured.

## SR-082

Analyze operations SHALL maintain planner statistics.

## SR-083

High-write tables SHALL receive appropriate vacuum tuning.

## SR-084

Table and index bloat SHALL be monitored.

## SR-085

Unused indexes SHALL be periodically reviewed.

---

## 45. Data Retention Requirements

## FR-133

Retention policies SHALL be configurable per data category.

Example:

```text
conversation data
analytics events
audit logs
AI execution metadata
API usage
webhook deliveries
notification history
```

## FR-134

Retention jobs SHALL be idempotent.

## FR-135

Retention deletion SHALL respect legal holds and compliance policies.

## FR-136

Deletion operations SHALL themselves be auditable.

---

## 46. Privacy Requirements

## FR-137

Sensitive customer data SHALL be protected using appropriate access controls.

## FR-138

Personally identifiable information SHALL be classified.

## FR-139

Sensitive fields MAY require encryption or tokenization.

## FR-140

Data exports SHALL enforce organization and user permissions.

## FR-141

Deletion requests SHALL propagate to dependent systems where required.

---

## 47. Human + AI Authorization Requirements

## FR-142

The authorization system SHALL distinguish human and AI actors.

Actor types:

```text
human
ai_agent
service_account
system
integration
```

## FR-143

AI agents SHALL operate under explicit permissions.

## FR-144

AI agents SHALL NOT inherit unrestricted administrator privileges.

## FR-145

AI actions SHALL be constrained by:

```text
organization
agent
role
tool
workflow
resource
policy
```

## FR-146

High-risk AI operations SHOULD require human approval.

Examples:

```text
refund
delete customer
change billing plan
export customer data
modify permissions
send high-impact communication
close account
```

---

## 48. Human Approval Requirements

## FR-147

The system SHALL support approval records.

Example:

```text
approval_id
organization_id
request_id
requested_by
requested_action
resource_type
resource_id
approved_by
status
created_at
approved_at
```

## FR-148

Approval state SHALL support:

```text
pending
approved
rejected
expired
cancelled
```

---

## 49. Data Lineage Requirements

## FR-149

Critical analytics and AI-derived records SHOULD preserve lineage.

Example:

```text
source_event_id
source_entity_id
source_agent_run_id
source_model_version
generated_at
```

## FR-150

Analytics metrics SHOULD be traceable to source data where feasible.

---

## 50. Testing Requirements

## FR-151

Database migrations SHALL be automatically tested.

## FR-152

Schema constraints SHALL have automated tests.

## FR-153

Tenant-isolation tests SHALL be mandatory.

## FR-154

RBAC database-access tests SHALL be mandatory.

## FR-155

Concurrency tests SHALL cover high-risk workflows.

## FR-156

Backup restoration SHALL be tested periodically.

## FR-157

Disaster recovery procedures SHALL be tested.

## FR-158

Performance tests SHALL use production-representative data volumes.

---

## 51. Security Test Requirements

The system SHALL test:

```text
cross-tenant reads
cross-tenant writes
privilege escalation
RLS bypass
SQL injection
unauthorized exports
unauthorized deletion
API key exposure
service-account abuse
audit-log tampering
credential leakage
```

---

## 52. Capacity Requirements

The PostgreSQL architecture SHALL be designed for SalesGenie's target platform scale.

Target architectural considerations SHOULD include:

```text
10M+ registered users
large multi-tenant organizations
500K+ concurrent conversations
millions of daily events
millions of messages
millions of analytics records
high API request volume
large workflow execution volume
large AI execution volume
```

The transactional database SHALL NOT be expected to serve every analytical workload directly at extreme scale.

---

## 53. Scaling Strategy

## FR-159

The architecture SHALL support vertical scaling of PostgreSQL.

## FR-160

The architecture SHALL support read scaling using replicas.

## FR-161

High-volume tables SHALL support partitioning.

## FR-162

Application-level sharding SHOULD be considered when a single PostgreSQL cluster becomes insufficient.

## FR-163

Tenant-based sharding MAY be introduced for extremely large enterprise tenants.

## FR-164

Sharding decisions SHALL preserve tenant isolation and operational observability.

---

## 54. Recommended Database Topology

```text
                         ┌─────────────────────┐
                         │   SalesGenie APIs   │
                         └──────────┬──────────┘
                                    │
                           Connection Pool
                                    │
                              ┌─────▼─────┐
                              │ PgBouncer │
                              └─────┬─────┘
                                    │
                        ┌───────────▼───────────┐
                        │ PostgreSQL Primary    │
                        │                       │
                        │ OLTP                  │
                        │ Transactions          │
                        │ Writes                │
                        └───────────┬───────────┘
                                    │
                  ┌─────────────────┼─────────────────┐
                  │                 │                 │
                  ▼                 ▼                 ▼
          ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
          │ Read Replica │ │ Read Replica │ │ HA Standby   │
          │ Analytics    │ │ Reporting    │ │ Failover     │
          └──────────────┘ └──────────────┘ └──────────────┘
                                    │
                                    ▼
                            Analytics Pipeline
                                    │
                 ┌──────────────────┼──────────────────┐
                 ▼                  ▼                  ▼
             Data Lake        Data Warehouse      BI Platform
```

---

## 55. Recommended Logical Data Architecture

```text
PostgreSQL
│
├── identity
│   ├── users
│   ├── roles
│   ├── permissions
│   └── sessions
│
├── organizations
│   ├── organizations
│   ├── teams
│   └── settings
│
├── crm
│   ├── customers
│   ├── contacts
│   ├── companies
│   └── accounts
│
├── sales
│   ├── leads
│   ├── opportunities
│   ├── pipelines
│   └── deals
│
├── conversations
│   ├── conversations
│   ├── participants
│   ├── messages
│   └── assignments
│
├── agents
│   ├── ai_agents
│   ├── agent_versions
│   ├── agent_runs
│   └── tool_calls
│
├── workflows
│   ├── workflows
│   ├── workflow_versions
│   ├── workflow_runs
│   └── workflow_tasks
│
├── knowledge
│   ├── knowledge_bases
│   ├── documents
│   ├── document_versions
│   └── document_chunks
│
├── analytics
│   ├── analytics_events
│   ├── metrics
│   └── kpis
│
├── billing
│   ├── plans
│   ├── subscriptions
│   ├── usage
│   └── invoices
│
├── notifications
│   ├── notifications
│   ├── preferences
│   └── deliveries
│
├── developers
│   ├── api_keys
│   ├── service_accounts
│   ├── webhooks
│   └── api_usage
│
└── security
    ├── audit_logs
    ├── security_events
    └── approvals
```

---

## 56. Example Core Table Requirements

## organizations

```text
id UUID PRIMARY KEY
name TEXT NOT NULL
slug TEXT NOT NULL
status TEXT NOT NULL
created_at TIMESTAMPTZ NOT NULL
updated_at TIMESTAMPTZ NOT NULL
deleted_at TIMESTAMPTZ NULL
```

Constraints:

```text
UNIQUE(slug)
```

---

## users

```text
id UUID PRIMARY KEY
organization_id UUID NOT NULL
email TEXT NOT NULL
name TEXT
status TEXT NOT NULL
created_at TIMESTAMPTZ NOT NULL
updated_at TIMESTAMPTZ NOT NULL
```

Indexes:

```text
(organization_id, email)
(organization_id, status)
```

---

## leads

```text
id UUID PRIMARY KEY
organization_id UUID NOT NULL
customer_id UUID
owner_id UUID
source TEXT
status TEXT
score NUMERIC
created_at TIMESTAMPTZ NOT NULL
updated_at TIMESTAMPTZ NOT NULL
deleted_at TIMESTAMPTZ
```

Indexes:

```text
(organization_id, status)
(organization_id, owner_id)
(organization_id, score)
(organization_id, created_at)
```

---

## conversations

```text
id UUID PRIMARY KEY
organization_id UUID NOT NULL
customer_id UUID
channel TEXT NOT NULL
status TEXT NOT NULL
assigned_human_id UUID
assigned_ai_agent_id UUID
created_at TIMESTAMPTZ NOT NULL
updated_at TIMESTAMPTZ NOT NULL
closed_at TIMESTAMPTZ
```

Indexes:

```text
(organization_id, status)
(organization_id, customer_id)
(organization_id, assigned_human_id)
(organization_id, assigned_ai_agent_id)
(organization_id, created_at)
```

---

## messages

```text
id UUID PRIMARY KEY
organization_id UUID NOT NULL
conversation_id UUID NOT NULL
sender_type TEXT NOT NULL
sender_id UUID
message_type TEXT NOT NULL
content TEXT
external_message_id TEXT
created_at TIMESTAMPTZ NOT NULL
```

Indexes:

```text
(conversation_id, created_at)
(organization_id, created_at)
```

---

## 57. Pagination Requirements

## FR-165

Large datasets SHALL use cursor-based pagination where appropriate.

Preferred pattern:

```text
WHERE created_at < :cursor_time
ORDER BY created_at DESC
LIMIT :limit
```

## FR-166

Unbounded queries SHALL be prohibited.

## FR-167

API endpoints SHALL enforce maximum page sizes.

---

## 58. Data Access Layer Requirements

## FR-168

Applications SHALL access PostgreSQL through a controlled data-access layer.

## FR-169

Raw SQL MAY be used for performance-critical operations.

## FR-170

ORM-generated queries SHALL be monitored for inefficiency.

## FR-171

Repositories/data-access modules SHOULD enforce tenant scoping automatically.

---

## 59. Database API Requirements

The database layer SHALL expose functionality required by:

```text
Auth Service
Organization Service
CRM Service
Sales Service
Support Service
Conversation Service
AI Gateway
Agent Service
Workflow Service
Knowledge Service
Analytics Service
Billing Service
Notification Service
Developer Platform
Integration Service
Admin Platform
Audit/Security Service
```

Each service SHALL use explicit access boundaries.

---

## 60. Failure Handling

## FR-172

Transient database failures SHALL be retried using bounded exponential backoff.

## FR-173

Non-retryable database errors SHALL fail fast.

## FR-174

Retry mechanisms SHALL not duplicate business operations.

## FR-175

Circuit breakers SHOULD protect PostgreSQL from cascading application failures.

---

## 61. Transactional Outbox

For important domain events:

```text
BEGIN TRANSACTION

UPDATE business_table

INSERT INTO outbox_events (...)

COMMIT
```

A background publisher SHALL subsequently deliver the event.

This SHALL prevent:

```text
database commit succeeded
event publication failed
```

from causing silent event loss.

---

## 62. Exactly-Once Business Semantics

PostgreSQL SHALL NOT be assumed to provide distributed exactly-once execution.

Instead, SalesGenie SHALL implement:

```text
idempotency keys
unique constraints
deduplication records
transactional outbox
consumer offsets
operation state machines
```

to achieve effectively-once business behavior where required.

---

## 63. AI Data Lifecycle

AI-generated data SHALL follow:

```text
Input
  ↓
AI Agent Run
  ↓
Model Invocation
  ↓
Tool Calls
  ↓
Generated Output
  ↓
Human Approval (if required)
  ↓
Business Action
  ↓
Audit Event
  ↓
Analytics Event
```

PostgreSQL SHALL persist the transactional metadata necessary to reconstruct this lifecycle.

---

## 64. Human Data Lifecycle

Human-driven operations SHALL follow:

```text
User Action
   ↓
Authorization
   ↓
Transaction
   ↓
Business State Change
   ↓
Audit Event
   ↓
Domain Event
   ↓
Analytics Event
```

---

## 65. AI + Human Unified Activity Model

The platform SHOULD support a unified activity model:

```text
activity_id
organization_id
actor_type
actor_id
action
resource_type
resource_id
source
timestamp
metadata
```

Where:

```text
actor_type =
human
ai_agent
service_account
system
integration
```

This enables unified auditing and analytics across AI and human operations.

---

## 66. Compliance Requirements

The architecture SHOULD support enterprise compliance requirements including:

```text
SOC 2
ISO 27001
GDPR
CCPA
HIPAA
PCI DSS
```

where applicable to the specific SalesGenie deployment and data processing scope.

Compliance controls SHALL include:

* Access control
* Audit logging
* Data retention
* Data deletion
* Encryption
* Backup protection
* Privileged access monitoring
* Data classification

---

## 67. Database Governance

## FR-176

Every production table SHALL have:

```text
owner
purpose
data classification
retention policy
tenant scope
backup requirement
criticality
```

## FR-177

Schema changes SHALL undergo code review.

## FR-178

Critical schema changes SHALL undergo architecture review.

## FR-179

Deprecated tables SHALL have a documented removal plan.

---

## 68. Production Readiness Requirements

Production PostgreSQL SHALL NOT be considered ready until:

```text
[ ] HA configured
[ ] Backups configured
[ ] PITR configured
[ ] Restore tested
[ ] Monitoring configured
[ ] Alerts configured
[ ] Connection pooling configured
[ ] TLS enabled
[ ] Encryption at rest enabled
[ ] Secrets managed securely
[ ] RLS tested where required
[ ] Tenant isolation tested
[ ] Migration process tested
[ ] Slow-query monitoring enabled
[ ] Autovacuum verified
[ ] Replication monitored
[ ] Disaster recovery documented
[ ] Capacity limits documented
[ ] Retention policies configured
[ ] Audit logging enabled
[ ] Security review completed
```

---

## 69. Non-Functional Requirements Summary

| Category         | Requirement                                    |
| ---------------- | ---------------------------------------------- |
| Availability     | Production-grade high availability             |
| Durability       | Strong transactional durability                |
| Consistency      | ACID for critical business operations          |
| Security         | TLS + encryption at rest + least privilege     |
| Multi-tenancy    | Strong tenant isolation                        |
| Scalability      | Read replicas + partitioning + future sharding |
| Performance      | P50/P95/P99 query monitoring                   |
| Recovery         | Backup + PITR + DR                             |
| Observability    | Metrics, logs, traces, query monitoring        |
| Maintainability  | Version-controlled migrations                  |
| Reliability      | Idempotency and retry-safe operations          |
| Compliance       | Auditable and retention-aware                  |
| AI Governance    | AI actor attribution and permissions           |
| Human Governance | Human actor attribution and RBAC               |
| Data Integrity   | Constraints + FK + transactional invariants    |
| Extensibility    | Domain-oriented schema architecture            |

---

## 70. Acceptance Criteria

## AC-001 — Tenant Isolation

A user belonging to Organization A SHALL NOT be able to retrieve or mutate Organization B's PostgreSQL records.

## AC-002 — RBAC

A user without a required permission SHALL be denied access to protected resources.

## AC-003 — AI Authorization

An AI agent SHALL only perform database-backed operations explicitly authorized for that agent.

## AC-004 — Human Authorization

Human users SHALL only access resources permitted by their organization role and permissions.

## AC-005 — Transaction Integrity

A failed multi-record transaction SHALL roll back atomically.

## AC-006 — Idempotency

Repeated requests with the same idempotency key SHALL not create duplicate business records.

## AC-007 — Auditability

Security-sensitive human and AI actions SHALL produce auditable records.

## AC-008 — Recovery

The production database SHALL be recoverable to an acceptable point according to the defined RPO.

## AC-009 — Failover

A PostgreSQL primary failure SHALL trigger the documented failover process.

## AC-010 — Migration Safety

Production migrations SHALL not require uncontrolled downtime.

## AC-011 — Performance

Critical database queries SHALL meet their defined latency SLOs under representative production load.

## AC-012 — Backup

Automated backup jobs SHALL be monitored and restoration SHALL be periodically validated.

## AC-013 — Data Retention

Expired records SHALL be archived or deleted according to configured retention policies.

## AC-014 — Data Lineage

AI-generated business actions SHALL be traceable to the responsible agent execution where applicable.

## AC-015 — Human-AI Collaboration

The system SHALL be able to distinguish human-generated actions from AI-generated actions.

---

## 71. Recommended PostgreSQL Technology Stack

```text
PostgreSQL
PostgreSQL HA / Managed PostgreSQL
PgBouncer
PostgreSQL WAL
Point-in-Time Recovery
PostgreSQL Replication
PostgreSQL RLS
PostgreSQL JSONB
PostgreSQL Full-Text Search
pg_stat_statements
PostgreSQL Partitioning
pgvector where appropriate
Prometheus-compatible monitoring
OpenTelemetry
Grafana
```

Supporting infrastructure:

```text
Redis
Kafka / NATS / equivalent event infrastructure
Object Storage
Search Engine
Vector Database
Data Warehouse
Data Lake
```

PostgreSQL SHALL remain the authoritative transactional source of truth for data within its defined ownership boundary.

---

## 72. Final Architecture Principle

SalesGenie's PostgreSQL architecture SHALL function as a secure, highly available, multi-tenant transactional foundation for the entire AI + human enterprise platform.

The architecture SHALL guarantee:

```text
Strong tenant isolation
        +
ACID transactions
        +
RBAC/RLS authorization
        +
AI/Human attribution
        +
Event-driven integration
        +
Idempotent processing
        +
High availability
        +
Disaster recovery
        +
Observability
        +
Controlled schema evolution
        +
Scalable read/write architecture
        +
Enterprise security
        =
Production-grade SalesGenie PostgreSQL Platform
```
