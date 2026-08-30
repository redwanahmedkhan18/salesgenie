# SalesGenie Database Architecture — FAANG-Level Requirements

## 1. Document Overview

### Project

SalesGenie — Enterprise AI Customer Support & Sales Agent Platform

### Document

Database Architecture Requirements

### File

`database_architecture.md`

### Architecture Objective

SalesGenie shall implement a production-grade, multi-tenant, highly available, horizontally scalable database architecture capable of supporting:

- Enterprise customer data
- Users and organizations
- RBAC and permissions
- CRM data
- Leads and opportunities
- Conversations and messages
- AI agents
- AI-generated outputs
- RAG knowledge bases
- Documents and document metadata
- Workflows
- Workflow executions
- Omnichannel communication
- Notifications
- Billing and subscriptions
- Analytics
- Audit logs
- Integrations
- API consumers
- Webhooks
- Developer platform data
- Search metadata
- Human-agent operations
- AI-agent operations
- Real-time workloads
- Compliance requirements
- Disaster recovery
- AI-assisted database operations

The architecture shall support both:

1. Human-operated database workflows
2. AI-assisted database workflows

AI shall never bypass database security, tenant isolation, authorization, transaction guarantees, or governance controls.

---

## 2. System Context

```text
                           Internet
                              |
                              v
                       CDN / WAF / Gateway
                              |
                              v
                     API Gateway / BFF
                              |
          +-------------------+-------------------+
          |                   |                   |
          v                   v                   v
      Auth Service       Platform Services     AI Gateway
          |                   |                   |
          +-------------------+-------------------+
                              |
                              v
                     Database Abstraction
                              |
        +---------------------+----------------------+
        |                     |                      |
        v                     v                      v
   PostgreSQL             Redis              Object Storage
   Primary DB             Cache              Documents/Files
        |
        +-----------------------+
        |                       |
        v                       v
   Read Replicas          Analytics Store
```

---

## 3. Database Strategy

## 3.1 Primary Database

PostgreSQL shall be the primary transactional database for core SalesGenie business data.

The primary database shall support:

* ACID transactions
* Referential integrity
* Constraints
* Indexing
* JSON/JSONB where appropriate
* Full-text search where appropriate
* Row-level security where appropriate
* Partitioning
* Replication
* Point-in-time recovery
* Auditing integration

---

## 3.2 Polyglot Persistence

SalesGenie shall not force every workload into a single database.

Recommended storage responsibilities:

| Workload            | Storage                                        |
| ------------------- | ---------------------------------------------- |
| Transactional data  | PostgreSQL                                     |
| Cache               | Redis                                          |
| Sessions            | Redis                                          |
| Distributed locks   | Redis                                          |
| Event streams       | Event broker / Redis Streams where appropriate |
| Documents           | Object storage                                 |
| Vector embeddings   | Vector database / PostgreSQL vector extension  |
| Search indexes      | Search engine                                  |
| Long-term analytics | Analytical database / warehouse                |
| Logs                | Log platform                                   |
| Metrics             | Time-series/metrics platform                   |

---

## 4. Database Actors

## 4.1 Human Actors

### DBA

The DBA shall be able to:

* Monitor database health.
* Manage schemas.
* Manage indexes.
* Manage replicas.
* Manage backups.
* Manage migrations.
* Inspect query performance.
* Manage database users.
* Manage permissions.
* Configure maintenance.
* Perform controlled recovery.
* Review audit logs.

---

### Platform Administrator

The platform administrator shall be able to:

* View database health.
* View tenant database usage.
* Configure retention policies.
* Configure approved database policies.
* Review database alerts.
* Approve high-risk database operations.

---

### SRE

The SRE shall be able to:

* Monitor database SLOs.
* Monitor replication.
* Monitor connections.
* Monitor storage.
* Monitor query latency.
* Monitor lock contention.
* Execute failover.
* Execute disaster recovery procedures.

---

### Backend Engineer

The backend engineer shall be able to:

* Access authorized schemas.
* Execute transactional queries.
* Create migrations.
* Define indexes.
* Implement repositories.
* Use transactions.
* Perform bulk operations safely.

---

### Data Engineer

The data engineer shall be able to:

* Build data pipelines.
* Extract operational data.
* Transform analytics data.
* Maintain analytical models.
* Manage ETL/ELT jobs.

---

### AI Engineer

The AI engineer shall be able to:

* Access approved AI datasets.
* Store model metadata.
* Store AI execution metadata.
* Store embeddings metadata.
* Query AI evaluation data.
* Manage AI-related schemas.

---

## 5. AI Actors

## 5.1 AI Database Operations Agent

The AI database operations agent may analyze:

* Query performance
* Index usage
* Table growth
* Storage consumption
* Connection utilization
* Replication lag
* Lock contention
* Deadlocks
* Query plans
* Slow queries
* Cache effectiveness
* Partition utilization
* Tenant database usage
* Data retention
* Backup health
* Migration risk

AI recommendations shall be policy-controlled.

---

## 5.2 AI Database Optimization Agent

The AI optimization agent may recommend:

* Index creation
* Index removal
* Query optimization
* Partitioning
* Archival
* Vacuum configuration
* Connection-pool changes
* Replica scaling
* Storage scaling
* Schema optimization

High-risk changes require human approval.

---

## 6. User Requirements

## UR-DB-001 — Reliable Data Storage

Users shall be able to store and retrieve SalesGenie business data reliably.

---

## UR-DB-002 — Data Consistency

Users shall not observe invalid transactional states caused by partial database writes.

---

## UR-DB-003 — Multi-Tenant Isolation

Users belonging to one organization shall never access another organization's database records without explicit authorization.

---

## UR-DB-004 — Fast Access

Frequently accessed transactional data shall be available within defined latency SLOs.

---

## UR-DB-005 — Data Durability

Critical customer and business data shall survive application crashes and database node failures according to defined RPO/RTO targets.

---

## UR-DB-006 — Searchable Data

Authorized users shall be able to search:

* Customers
* Leads
* Conversations
* Messages
* Tickets
* Knowledge metadata
* Workflows
* Documents
* Organizations

---

## UR-DB-007 — Historical Data

Users shall be able to retrieve historical business information according to retention and authorization policies.

---

## 7. Multi-Tenant Requirements

## UR-DB-008

Every tenant-owned entity shall contain an authoritative tenant/organization identifier.

Example:

```text
tenant_id
organization_id
```

---

## UR-DB-009

Tenant identity shall be derived from trusted authentication context.

Clients shall not be trusted to define arbitrary tenant scope.

---

## UR-DB-010

Cross-tenant queries shall be denied unless explicitly authorized for platform-level administrative operations.

---

## UR-DB-011

Tenant-specific database usage shall be measurable.

---

## UR-DB-012

Large tenants shall be capable of future isolation strategies including:

* Dedicated schemas
* Dedicated database
* Dedicated cluster
* Dedicated region

---

## 8. Core Domain Requirements

## UR-DB-013 — Organizations

The database shall support:

* Organizations
* Workspaces
* Teams
* Departments
* Tenant settings
* Subscription associations

---

## UR-DB-014 — Users

The database shall support:

* Users
* Profiles
* Roles
* Permissions
* User status
* Organization membership
* Team membership

---

## UR-DB-015 — Customers

The database shall support:

* Customer profiles
* Contacts
* Customer attributes
* Customer lifecycle
* Customer segments
* Customer activity

---

## UR-DB-016 — Leads

The database shall support:

* Lead profiles
* Lead sources
* Lead scores
* Lead status
* Lead ownership
* Lead activities
* Lead enrichment
* Lead qualification

---

## UR-DB-017 — Sales Opportunities

The database shall support:

* Opportunities
* Pipeline stages
* Deal value
* Probability
* Sales owner
* Forecast
* Activities
* Conversion history

---

## UR-DB-018 — Conversations

The database shall support:

* Conversations
* Participants
* Channels
* Messages
* Attachments
* Agent involvement
* Human involvement
* Conversation state
* Conversation metadata

---

## UR-DB-019 — Support Tickets

The database shall support:

* Tickets
* Ticket status
* Priority
* Assignment
* SLA
* Resolution
* Escalation
* Customer relationship

---

## 9. AI Requirements

## UR-DB-AI-001 — AI Agents

The database shall support:

* AI agents
* Agent versions
* Agent configurations
* Agent capabilities
* Agent permissions
* Agent execution records

---

## UR-DB-AI-002 — AI Runs

Every production AI execution shall be traceable.

Example metadata:

```text
run_id
tenant_id
conversation_id
agent_id
model
provider
model_version
prompt_version
workflow_id
started_at
completed_at
status
latency
token_usage
cost
```

---

## UR-DB-AI-003 — AI Decisions

AI-generated decisions shall be attributable to:

* Agent
* Model
* Version
* Prompt
* Input context
* Timestamp
* Tenant
* Human approval where applicable

---

## UR-DB-AI-004 — Human-in-the-Loop

The database shall support workflows where AI output requires human approval.

---

## UR-DB-AI-005 — AI Auditability

AI actions affecting business data shall be auditable.

---

## 10. Functional Requirements

## 10.1 Database Access Layer

### FR-DB-001

All application services shall access databases through approved data-access abstractions.

Examples:

```text
Repository
DAO
Service Layer
ORM
Query Builder
```

---

### FR-DB-002

Business logic shall not directly depend on database connection details.

---

### FR-DB-003

Database credentials shall not be embedded in application source code.

---

## 10.2 Connection Management

### FR-DB-004

The platform shall use bounded database connection pools.

---

### FR-DB-005

Connection pools shall support:

* Maximum connections
* Minimum connections
* Idle timeout
* Connection timeout
* Query timeout
* Health checks

---

### FR-DB-006

Individual application instances shall not be allowed to exhaust the database connection capacity.

---

## 11. Transactions

### FR-DB-007

Operations requiring atomicity shall execute inside database transactions.

Examples:

```text
Create customer + activity
Create lead + ownership
Create opportunity + pipeline event
Create subscription + billing state
Create ticket + assignment
Create workflow execution + execution state
```

---

### FR-DB-008

Transactions shall be kept as short as practical.

---

### FR-DB-009

External API calls shall not remain inside long-running database transactions.

---

## 12. Isolation Levels

The database layer shall support appropriate PostgreSQL transaction isolation levels.

Default workloads should use:

```text
READ COMMITTED
```

Higher isolation may be used when business correctness requires it.

---

## 13. Optimistic Concurrency

### FR-DB-010

Entities susceptible to concurrent updates shall support optimistic concurrency.

Example:

```text
version
updated_at
row_version
```

---

## 14. Pessimistic Locking

### FR-DB-011

Pessimistic locks shall be used only for workflows where optimistic concurrency is insufficient.

---

## 15. Deadlock Handling

### FR-DB-012

The application shall detect database deadlocks and safely retry eligible transactions.

---

## 16. Schema Architecture

Recommended logical domains:

```text
auth
organizations
users
rbac
customers
crm
sales
support
conversations
messaging
ai
agents
rag
documents
workflows
integrations
notifications
billing
analytics
developer
webhooks
audit
platform
```

---

## 17. Schema Ownership

Each service shall have clearly defined ownership over its database entities.

Example:

```text
Auth Service
    └── users / authentication metadata

CRM Service
    └── customers / leads / opportunities

Conversation Service
    └── conversations / messages

Billing Service
    └── subscriptions / invoices

Workflow Service
    └── workflows / executions

AI Service
    └── agent executions / model metadata
```

---

## 18. Database Ownership

### FR-DB-013

Services shall not directly modify another service's database tables unless explicitly approved.

---

## 19. Microservice Database Strategy

SalesGenie shall support a controlled database-per-service architecture.

```text
                    Platform
                       |
        +--------------+--------------+
        |              |              |
        v              v              v
      Auth DB       CRM DB       Billing DB
        |              |              |
        v              v              v
    Auth Service    CRM Service   Billing Service
```

Shared database usage shall be minimized.

---

## 20. Referential Integrity

### FR-DB-014

Foreign keys shall be used where strong relational integrity is required.

---

### FR-DB-015

Application-level references may be used across independently owned microservice databases.

---

## 21. Primary Keys

The platform shall use globally unique identifiers for distributed entities.

Recommended:

```text
UUID
UUIDv7
```

UUIDv7 or equivalent time-sortable identifiers should be preferred for high-write distributed tables where supported.

---

## 22. ID Requirements

### FR-DB-016

Identifiers shall not expose sensitive sequential business information.

---

## 23. Audit Fields

Business entities should include:

```text
id
tenant_id
created_at
updated_at
created_by
updated_by
version
```

where applicable.

---

## 24. Soft Deletion

### FR-DB-017

Soft deletion shall be used when business or compliance requirements require recovery or historical traceability.

Example:

```text
deleted_at
deleted_by
```

---

## 25. Hard Deletion

### FR-DB-018

Hard deletion shall require explicit authorization and shall respect:

* Legal retention
* Audit requirements
* Referential integrity
* Compliance policy
* Backup lifecycle

---

## 26. Data Retention

Each domain shall define:

```text
Retention period
Archival policy
Deletion policy
Legal hold behavior
Tenant-specific overrides
```

---

## 27. Partitioning

Large tables shall support partitioning where required.

Candidates include:

```text
messages
conversation_events
audit_logs
analytics_events
ai_runs
workflow_executions
notifications
webhook_events
```

---

## 28. Time-Based Partitioning

Large append-heavy datasets should support time-based partitioning.

Example:

```text
analytics_events_2026_08
analytics_events_2026_09
```

---

## 29. Tenant-Based Partitioning

Tenant partitioning may be used when:

* Tenant cardinality is manageable.
* Tenant isolation requires it.
* Query patterns justify it.

---

## 30. Indexing

### FR-DB-019

Indexes shall be created based on real query patterns.

---

### FR-DB-020

Common indexes shall include:

```text
tenant_id
created_at
updated_at
status
owner_id
customer_id
conversation_id
workflow_id
organization_id
```

where applicable.

---

## 31. Composite Indexes

Composite indexes shall be used for common multi-column queries.

Example:

```text
(tenant_id, status, created_at)
```

---

## 32. Partial Indexes

Partial indexes may be used for highly selective conditions.

Example:

```text
WHERE deleted_at IS NULL
```

---

## 33. JSONB

JSONB may be used for flexible metadata.

JSONB shall not replace relational modeling for highly queried core attributes.

---

## 34. Database Constraints

The database shall enforce:

```text
NOT NULL
UNIQUE
CHECK
FOREIGN KEY
PRIMARY KEY
```

where applicable.

---

## 35. Business Invariants

Critical invariants shall be enforced at the database layer when practical.

Examples:

```text
Subscription cannot have invalid status
Invoice cannot reference nonexistent tenant
Message cannot reference nonexistent conversation
Lead cannot belong to nonexistent tenant
```

---

## 36. Search Data

Transactional databases shall not be overloaded with large-scale search workloads.

Search-heavy workloads should use:

```text
Search Index
```

while PostgreSQL remains the source of truth.

---

## 37. Vector Data

The platform shall support vector metadata for:

* Documents
* Chunks
* Knowledge bases
* Embeddings
* Semantic search

---

## 38. Embedding Metadata

Embedding records shall include:

```text
embedding_id
tenant_id
document_id
chunk_id
model
model_version
dimensions
content_hash
created_at
```

---

## 39. AI Knowledge Versioning

RAG-related database records shall track:

```text
knowledge_base_id
knowledge_base_version
document_version
embedding_version
chunk_version
```

---

## 40. AI Cache Consistency

Database changes affecting AI cache validity shall emit invalidation events.

Example:

```text
Database Change
      |
      v
Domain Event
      |
      v
Cache Invalidation
      |
      v
Redis / AI Cache
```

---

## 41. AI Output Storage

The database may store:

* AI response metadata
* AI decisions
* Classification results
* Lead scores
* Summaries
* Recommendations
* Generated content metadata

Large generated artifacts should be stored in object storage.

---

## 42. AI Output Versioning

AI-generated business outputs shall be versioned when they can change over time.

---

## 43. AI Human Approval

Example:

```text
AI Recommendation
       |
       v
Pending Approval
       |
   +---+---+
   |       |
Approve   Reject
   |       |
   v       v
Applied  Archived
```

The database shall preserve the decision history.

---

## 44. Eventual Consistency

The platform shall explicitly define eventual consistency boundaries.

Examples:

```text
Analytics
Search index
Recommendations
Aggregations
Notifications
AI insights
```

---

## 45. Strong Consistency

Strong transactional consistency shall be used for:

```text
Billing
Subscription state
Authorization
Critical customer updates
Financial records
Transactional workflow state
```

---

## 46. Read Replicas

### FR-DB-021

Read replicas may be used for read-heavy workloads.

---

### FR-DB-022

The application shall distinguish between:

```text
Read-after-write requirements
Eventually consistent reads
Strongly consistent reads
```

---

## 47. Replication

Production PostgreSQL shall support replication.

The architecture shall support:

```text
Primary
   |
   +--> Replica 1
   |
   +--> Replica 2
```

---

## 48. Failover

### FR-DB-023

Production database failover shall be automated where supported.

---

### FR-DB-024

Failover procedures shall be tested regularly.

---

## 49. Database Availability

Critical transactional database workloads shall target:

```text
99.99%+
```

availability where infrastructure supports the target.

---

## 50. Backup Requirements

### FR-DB-025

Production databases shall have automated backups.

Backups shall include:

* Full backups
* Incremental/WAL-based recovery where applicable
* Point-in-time recovery
* Backup verification

---

## 51. Backup Encryption

### SEC-DB-001

Database backups shall be encrypted at rest.

---

## 52. Point-in-Time Recovery

### FR-DB-026

Critical databases shall support point-in-time recovery.

---

## 53. Recovery Objectives

Recommended initial targets:

```text
Critical transactional RPO: ≤ 5 minutes
Critical transactional RTO: ≤ 15 minutes
```

Targets shall be validated against actual infrastructure capabilities.

---

## 54. Disaster Recovery

The database architecture shall support recovery from:

```text
Database node failure
Storage failure
Availability-zone failure
Region failure
Data corruption
Accidental deletion
Bad migration
Application bug
Security incident
Credential compromise
```

---

## 55. Database Migrations

### FR-DB-027

All schema changes shall use version-controlled migrations.

---

### FR-DB-028

Migrations shall be:

* Deterministic
* Reviewable
* Reproducible
* Testable
* Auditable

---

## 56. Zero-Downtime Migrations

Production migrations should use expand-and-contract strategies.

```text
Old Schema
    |
    v
Expand
    |
    v
Dual Compatibility
    |
    v
Backfill
    |
    v
Application Switch
    |
    v
Contract
```

---

## 57. Migration Safety

Production migrations shall not perform uncontrolled:

```text
DROP TABLE
DROP COLUMN
Mass UPDATE
Mass DELETE
Long blocking ALTER
```

without risk assessment and migration strategy.

---

## 58. Migration Rollback

Every migration shall define:

```text
Forward migration
Rollback strategy
Data migration strategy
Compatibility window
Failure recovery
```

---

## 59. Database Security

## SEC-DB-002

All production database connections shall use encryption in transit.

---

## SEC-DB-003

Database credentials shall be stored in the secrets-management system.

---

## SEC-DB-004

Database users shall follow least privilege.

---

## SEC-DB-005

Application services shall not use superuser credentials.

---

## SEC-DB-006

Administrative database access shall require elevated authorization.

---

## 60. Database Roles

Recommended roles:

```text
db_admin
migration_runner
service_runtime
readonly
analytics_reader
backup_operator
security_auditor
```

---

## 61. Row-Level Security

PostgreSQL Row-Level Security may be used for tenant isolation.

Example conceptual policy:

```text
tenant_id = current_tenant_id()
```

---

## 62. RLS Safety

RLS policies shall be tested against:

```text
Normal user
Tenant admin
Platform admin
Service account
Background worker
AI agent
Migration user
```

---

## 63. SQL Injection Protection

### SEC-DB-007

All dynamic SQL shall use parameterized queries or safe query builders.

---

## 64. Secret Protection

Database records shall not store raw:

```text
API keys
Passwords
Access tokens
Private keys
Encryption keys
```

unless specifically designed with appropriate encryption and key management.

---

## 65. Encryption at Rest

Production database storage shall use encryption at rest.

---

## 66. Sensitive Data

Sensitive customer information shall have:

* Data classification
* Access controls
* Retention rules
* Encryption where required
* Auditability

---

## 67. Audit Logging

Database-related security events shall be auditable.

Examples:

```text
Login
Permission changes
Schema changes
Sensitive reads
Sensitive writes
Deletion
Administrative operations
AI database actions
```

---

## 68. AI Database Access

AI agents shall use dedicated service identities.

Example:

```text
AI Agent
   |
   v
AI Service Identity
   |
   v
Policy Engine
   |
   v
Database Access Layer
   |
   v
Authorized Database
```

---

## 69. AI Database Query Restrictions

AI agents shall not have unrestricted SQL access in production.

Allowed operations shall be policy-defined.

---

## 70. AI Read Access

AI may query approved read-only datasets for:

* Analytics
* Recommendations
* Customer intelligence
* Sales intelligence
* Support intelligence
* Operational insights

---

## 71. AI Write Access

AI write operations shall be:

* Explicitly scoped
* Authenticated
* Authorized
* Validated
* Audited
* Idempotent where applicable

---

## 72. AI Destructive Operations

AI shall never automatically execute unrestricted:

```text
DROP
TRUNCATE
DELETE *
ALTER
CREATE USER
GRANT
REVOKE
```

operations.

---

## 73. AI SQL Generation

If AI generates SQL, the system shall validate:

```text
Syntax
Schema
Permissions
Tenant scope
Query cost
Mutation type
Affected rows
Transaction safety
```

before execution.

---

## 74. AI Query Cost Guard

AI-generated queries shall have resource limits.

Controls shall include:

```text
Statement timeout
Row limit
Result-size limit
Memory/resource controls
Tenant scope
Read/write policy
```

---

## 75. AI Query Approval

High-risk AI-generated mutations shall require human approval.

---

## 76. AI Database Optimization

AI shall analyze:

```text
pg_stat_statements
Query plans
Index usage
Table size
Dead tuples
Vacuum behavior
Connection utilization
Lock contention
Replication lag
```

where permitted.

---

## 77. AI Index Recommendations

AI may recommend:

```text
CREATE INDEX
CREATE INDEX CONCURRENTLY
DROP UNUSED INDEX
Composite index
Partial index
Covering index
```

Recommendations shall be validated before execution.

---

## 78. AI Query Optimization

AI may identify:

* Sequential scans
* Poor joins
* Missing indexes
* N+1 queries
* Inefficient pagination
* Excessive sorting
* Large aggregation costs
* Bad query predicates

---

## 79. AI Anomaly Detection

The AI system shall detect:

```text
Latency spikes
Connection spikes
Deadlocks
Replication lag
Storage anomalies
Query anomalies
Tenant traffic anomalies
Unexpected data growth
Failed migrations
```

---

## 80. AI Auto-Remediation

AI may automatically perform low-risk operations only when enabled.

Examples:

```text
Scale read replicas
Trigger cache warming
Adjust safe operational thresholds
Generate optimization recommendations
Trigger approved maintenance workflows
```

---

## 81. Human Approval

Human approval shall be required for:

```text
Schema changes
Data deletion
Permission changes
RLS changes
Database failover
Migration execution
Large-scale updates
Index removal on critical tables
Data retention changes
```

---

## 82. Human Override

Authorized operators shall be able to:

* Disable AI database automation.
* Reject recommendations.
* Roll back AI changes.
* Freeze AI mutations.
* Restrict AI to read-only mode.

---

## 83. Database Observability

The platform shall monitor:

```text
CPU
Memory
Storage
IOPS
Connections
Transactions
Queries
Locks
Deadlocks
Replication
Cache hit ratio
Vacuum
Autovacuum
Table growth
Index growth
```

---

## 84. Query Performance Monitoring

The platform shall track:

```text
p50 latency
p95 latency
p99 latency
QPS
slow queries
error rate
rows returned
rows scanned
execution time
```

---

## 85. Database SLOs

Each critical database shall define:

```text
Availability SLO
Latency SLO
Error-rate SLO
Replication SLO
Recovery SLO
Backup SLO
```

---

## 86. Connection Management

The system shall detect:

* Connection exhaustion
* Idle connection accumulation
* Connection leaks
* Pool saturation
* Long-running transactions

---

## 87. Lock Monitoring

The system shall monitor:

```text
Lock waits
Deadlocks
Long transactions
Blocking queries
```

---

## 88. Long Transaction Detection

Transactions exceeding configured thresholds shall generate alerts.

---

## 89. Storage Monitoring

The system shall monitor:

```text
Database size
Table size
Index size
WAL growth
Temporary files
Storage utilization
```

---

## 90. Data Growth Forecasting

AI shall estimate future database growth using:

```text
Historical growth
Tenant growth
Traffic growth
Message volume
AI execution volume
Analytics events
Retention policies
```

---

## 91. Capacity Planning

The system shall calculate:

```text
Current capacity
Peak utilization
Projected utilization
Storage runway
Connection runway
IO runway
Replica capacity
```

---

## 92. Database Scaling

The architecture shall support:

```text
Vertical scaling
Read replicas
Partitioning
Sharding
Tenant isolation
Database-per-service
Database-per-tenant for exceptional workloads
```

---

## 93. Sharding

Sharding shall be introduced only when a single PostgreSQL cluster cannot satisfy:

* Storage
* Throughput
* Connection
* Isolation
* Availability

requirements.

---

## 94. Shard Key

Potential shard keys include:

```text
tenant_id
organization_id
region_id
```

Tenant-based sharding should be preferred when workload characteristics justify it.

---

## 95. Shard Routing

The platform shall provide deterministic routing:

```text
Tenant ID
    |
    v
Shard Router
    |
    +----> Shard A
    |
    +----> Shard B
    |
    +----> Shard C
```

---

## 96. Cross-Shard Queries

Cross-shard transactions shall be minimized.

Analytics and asynchronous aggregation should be preferred over distributed transactional joins.

---

## 97. Database Cache Integration

The architecture shall integrate PostgreSQL with Redis.

```text
Application
    |
    +------> Redis
    |          |
    |          +--> Cache Hit
    |
    +------> PostgreSQL
               |
               +--> Source of Truth
```

---

## 98. Cache Invalidation

Database changes shall trigger cache invalidation events where stale data would violate application correctness.

---

## 99. Outbox Pattern

The platform shall support the transactional outbox pattern.

```text
Database Transaction
      |
      +--> Business Data
      |
      +--> Outbox Event
               |
               v
          Event Publisher
               |
               v
         Event Infrastructure
```

---

## 100. Outbox Requirements

Outbox events shall contain:

```text
event_id
tenant_id
aggregate_id
aggregate_type
event_type
payload
created_at
published_at
retry_count
status
```

---

## 101. Idempotent Event Publishing

Consumers shall process database-originated events idempotently.

---

## 102. CDC

Change Data Capture may be used for:

* Analytics
* Search indexing
* Data synchronization
* AI pipelines
* Data warehouse ingestion

---

## 103. Analytics Isolation

Transactional database queries shall not be used for unrestricted analytical workloads.

---

## 104. Analytics Pipeline

```text
PostgreSQL
    |
    v
CDC / Event Stream
    |
    v
Data Pipeline
    |
    v
Analytics Warehouse
    |
    v
BI / AI Analytics
```

---

## 105. Search Synchronization

Database changes shall synchronize with search indexes asynchronously.

---

## 106. Search Consistency

The database remains the authoritative source of truth.

Search indexes shall be considered derived state.

---

## 107. Document Architecture

Large documents shall not be stored directly in PostgreSQL unless specifically required.

Preferred:

```text
Object Storage
      |
      v
Document Metadata in PostgreSQL
      |
      v
Embedding / Search Pipeline
```

---

## 108. File Metadata

Database records shall include:

```text
file_id
tenant_id
object_key
content_type
size
checksum
version
created_at
created_by
```

---

## 109. Billing Data

Billing-related database records shall use stronger consistency requirements.

Critical records include:

```text
subscriptions
plans
invoices
payments
usage
credits
entitlements
```

---

## 110. Financial Integrity

Financial operations shall be:

* Transactional
* Idempotent
* Auditable
* Immutable where appropriate

---

## 111. Notification Data

The database shall store notification metadata such as:

```text
notification_id
tenant_id
user_id
type
status
channel
created_at
sent_at
read_at
```

---

## 112. Webhook Data

The database shall support:

```text
webhook_id
tenant_id
endpoint
event_type
delivery_status
attempt_count
last_attempt_at
next_retry_at
response_code
```

---

## 113. Webhook Idempotency

Incoming and outgoing webhook processing shall support idempotency.

---

## 114. Developer Platform Data

The database shall support:

```text
API keys
Service accounts
OAuth applications
Webhooks
SDK applications
API usage
Developer projects
Sandbox environments
```

Secrets shall not be stored as plaintext.

---

## 115. RBAC Database Requirements

The database shall support:

```text
Users
Roles
Permissions
Role assignments
Resource scopes
Tenant scopes
Team scopes
```

---

## 116. Authorization Model

The platform shall support combinations of:

```text
RBAC
ABAC
Tenant isolation
Resource ownership
Team permissions
Service permissions
AI permissions
```

---

## 117. Audit Database

Audit records shall contain:

```text
audit_id
tenant_id
actor_id
actor_type
action
resource_type
resource_id
timestamp
ip_address
request_id
metadata
result
```

Sensitive data shall be minimized.

---

## 118. Immutable Audit Records

Audit records shall be protected against unauthorized modification.

---

## 119. Request Correlation

Database-related operations should include:

```text
request_id
trace_id
tenant_id
user_id
service_name
```

where appropriate.

---

## 120. Data Quality

The database platform shall detect:

```text
Duplicate records
Orphaned records
Invalid foreign references
Missing required fields
Invalid state transitions
Unexpected null values
Abnormal cardinality
```

---

## 121. AI Data Quality Monitoring

AI shall detect:

* Distribution shifts
* Missing fields
* Duplicate entities
* Inconsistent labels
* Invalid AI outputs
* Abnormal lead scores
* Unexpected customer attributes

---

## 122. Data Validation

Application and database validation shall work together.

```text
Client Validation
       |
       v
API Validation
       |
       v
Domain Validation
       |
       v
Database Constraints
```

---

## 123. Data Integrity Checks

Scheduled integrity jobs shall validate critical relationships.

---

## 124. N+1 Query Prevention

Application services shall detect and prevent N+1 query patterns.

---

## 125. Pagination

Large datasets shall use cursor/keyset pagination where appropriate.

Offset pagination shall not be used for extremely large tables without performance justification.

---

## 126. Bulk Operations

Bulk inserts and updates shall use controlled batch sizes.

---

## 127. Batch Processing

Long-running data processing shall run asynchronously rather than blocking API requests.

---

## 128. Query Limits

User-facing database queries shall have:

```text
Statement timeout
Result limits
Pagination
Tenant scope
Resource limits
```

---

## 129. Database API Safety

Database queries originating from API requests shall never allow clients to arbitrarily specify:

```text
SQL
table names
column expressions
database commands
```

---

## 130. Database Testing

The system shall test:

```text
Schema
Constraints
Transactions
Concurrency
Deadlocks
Migrations
Indexes
RLS
Tenant isolation
Replication
Failover
Backups
Recovery
Performance
AI database access
```

---

## 131. Migration Testing

Every production migration shall be tested against:

```text
Production-like dataset
Current schema
Previous schema
Expected traffic
Rollback procedure
```

---

## 132. Performance Testing

Database load testing shall simulate:

* Normal traffic
* Peak traffic
* Burst traffic
* Large tenants
* Many tenants
* AI workloads
* Message-heavy workloads
* Analytics workloads

---

## 133. Chaos Testing

Chaos testing shall include:

```text
Primary failure
Replica failure
Network failure
Storage failure
Connection exhaustion
High CPU
High IO
Replication lag
Bad migration
Database restart
```

---

## 134. AI Security Testing

AI database access shall be tested against:

```text
Prompt injection
SQL injection
Tenant escape
Privilege escalation
Unauthorized mutation
Sensitive-data extraction
Cross-tenant inference
Malicious query generation
Resource exhaustion
```

---

## 135. AI Database Guardrails

AI database requests shall pass:

```text
Authentication
Authorization
Tenant validation
Schema validation
Query validation
Cost validation
Risk classification
Execution policy
Audit logging
```

---

## 136. AI Database Risk Model

```text
AI Request
    |
    v
Authentication
    |
    v
Authorization
    |
    v
Tenant Validation
    |
    v
SQL Validation
    |
    v
Risk Classification
    |
    +---- Low Risk ----> Execute
    |
    +---- Medium Risk -> Policy / Approval
    |
    +---- High Risk ---> Human Approval
```

---

## 137. Database AI Governance

AI database operations shall operate in:

```text
OBSERVE
RECOMMEND
CONTROLLED_AUTOMATION
```

modes.

---

## 138. AI Change Audit

Every AI database action shall record:

```text
ai_action_id
agent_id
model
model_version
prompt_version
request_id
tenant_id
operation
target
risk_level
approval_status
executed_at
result
rollback_reference
```

---

## 139. AI Rollback

Every reversible AI database modification shall have a rollback mechanism.

---

## 140. Human Override

Administrators shall be able to immediately disable AI database mutations.

---

## 141. Environment Separation

Separate database environments shall exist:

```text
Development
Testing
Staging
Production
```

---

## 142. Production Isolation

Production credentials and production databases shall never be exposed to ordinary development environments.

---

## 143. Test Data

Production customer data shall not be copied into development environments without approved anonymization.

---

## 144. Data Masking

The platform shall support masking/anonymization for:

```text
Customer information
Contact information
Messages
Authentication data
Financial information
Sensitive metadata
```

---

## 145. Database Resource Governance

Each tenant shall have configurable limits for:

```text
Storage
Records
Messages
AI executions
API operations
Search records
Documents
```

---

## 146. Tenant Quotas

The system shall enforce tenant quotas before resource exhaustion occurs.

---

## 147. Noisy Neighbor Protection

The database architecture shall prevent a single tenant from monopolizing database resources.

Controls may include:

```text
Rate limiting
Connection limits
Query limits
Workload prioritization
Tenant quotas
Queue isolation
Dedicated infrastructure
```

---

## 148. Priority Classes

Database workloads may be classified:

```text
Critical
High
Normal
Low
Background
```

---

## 149. Database Maintenance

Scheduled maintenance shall include:

```text
Vacuum
Analyze
Index maintenance
Partition maintenance
Statistics refresh
Backup verification
Integrity checks
```

---

## 150. Autovacuum

PostgreSQL autovacuum shall be monitored and tuned based on workload.

---

## 151. Bloat Management

The system shall detect:

```text
Table bloat
Index bloat
Dead tuples
```

and generate remediation recommendations.

---

## 152. Query Plan Analysis

AI and human operators shall be able to inspect:

```text
EXPLAIN
EXPLAIN ANALYZE
```

for approved diagnostic workloads.

Production query-plan analysis shall avoid unsafe diagnostic operations on highly sensitive workloads.

---

## 153. Query Performance Regression

The platform shall detect query performance regressions after:

```text
Deployment
Migration
Index changes
Schema changes
Traffic changes
```

---

## 154. Database Deployment

Database infrastructure shall be provisioned using infrastructure-as-code where practical.

---

## 155. Infrastructure Requirements

Production database infrastructure shall support:

```text
High availability
Private networking
Encryption
Backups
Monitoring
Failover
Scaling
Disaster recovery
```

---

## 156. Kubernetes Integration

If PostgreSQL is Kubernetes-managed, the platform shall support:

```text
StatefulSets
PersistentVolumes
StorageClasses
PodDisruptionBudgets
Anti-Affinity
Topology Spread
Readiness Probes
Liveness Probes
Secrets
Network Policies
```

For critical production databases, managed database services may be preferred when they provide stronger operational guarantees.

---

## 157. Network Security

Database servers shall not be publicly exposed.

Access shall occur through:

```text
Private Network
VPC
VPN
Private Endpoint
Service Mesh
Controlled Bastion
```

where applicable.

---

## 158. Database Firewall

Network-level rules shall restrict access to approved services.

---

## 159. Monitoring Architecture

```text
                    Database
                       |
       +---------------+---------------+
       |               |               |
       v               v               v
    Metrics          Logs           Traces
       |               |               |
       +---------------+---------------+
                       |
                       v
                Observability
                       |
              +--------+--------+
              |                 |
              v                 v
          Dashboards          Alerts
```

---

## 160. Database Alerts

Critical alerts shall include:

```text
Database unavailable
Primary failure
Replication failure
Replication lag
High connection usage
High CPU
High storage
High latency
Deadlocks
Long transactions
Backup failure
WAL growth
Disk exhaustion
Failed migration
```

---

## 161. AI Database Monitoring

AI shall monitor:

```text
Query anomaly
Storage growth
Index effectiveness
Tenant growth
Replication trends
Latency trends
Migration risk
Capacity risk
```

---

## 162. AI Capacity Forecast

AI shall forecast when infrastructure is likely to exceed configured thresholds.

Example:

```text
Current storage: 62%
Growth: 4.5% / week
Projected threshold breach: 7 weeks
Recommendation: expand storage
```

---

## 163. Database Cost Optimization

AI may analyze:

```text
Storage cost
Replica cost
IO cost
Backup cost
Query cost
Tenant resource usage
Unused indexes
Unused replicas
```

---

## 164. AI Cost Recommendations

AI may recommend:

* Removing unused indexes
* Archiving cold data
* Adjusting replica count
* Partitioning large tables
* Moving analytics workloads
* Adjusting retention

Human approval shall be required for destructive changes.

---

## 165. Database Resource Ownership

Every production database shall have:

```text
Owner
Service owner
SRE owner
Security owner
Data classification
Recovery tier
```

---

## 166. Database Documentation

Every database shall document:

```text
Schema
Owner
Dependencies
SLOs
RPO
RTO
Backup
Recovery
Security
Migration strategy
Scaling strategy
```

---

## 167. Dependency Mapping

The platform shall maintain database dependency maps.

Example:

```text
Auth Service
   |
   +--> Auth DB
   |
   +--> Redis

CRM Service
   |
   +--> CRM DB
   |
   +--> Search

AI Service
   |
   +--> AI DB
   +--> Vector Store
   +--> Redis
```

---

## 168. Service Dependency Failure

Database failure in one non-critical service shall not automatically cascade into unrelated services.

---

## 169. Circuit Breaking

Database-dependent services shall use circuit breakers where appropriate.

---

## 170. Graceful Degradation

Where possible:

```text
Database Failure
      |
      v
Cached / Derived Data
      |
      v
Reduced Functionality
```

Critical transactional operations shall fail safely rather than silently corrupting state.

---

## 171. Data Corruption Protection

The platform shall detect and respond to:

```text
Checksum mismatch
Unexpected schema state
Invalid foreign references
Unexpected value distributions
Malformed records
```

---

## 172. Database Security Incident

The platform shall support incident response for:

```text
Credential compromise
Unauthorized query
Data exfiltration
Tenant isolation failure
Privilege escalation
Malicious migration
Data deletion
```

---

## 173. Security Incident Response

The platform shall support:

```text
Credential rotation
Connection revocation
User disablement
Tenant isolation
Audit extraction
Backup recovery
Forensic investigation
```

---

## 174. Compliance

The database architecture shall support applicable requirements for:

```text
Data retention
Data deletion
Auditability
Access control
Encryption
Data export
Data isolation
```

Specific regulatory requirements shall be configured according to deployment jurisdiction and customer contract.

---

## 175. Data Export

Authorized tenants shall be able to export their permitted data.

Exports shall be:

* Authenticated
* Authorized
* Audited
* Rate-limited
* Generated asynchronously

---

## 176. Data Import

Imports shall support:

```text
Validation
Schema checking
Duplicate detection
Idempotency
Error reporting
Rollback where practical
Audit logging
```

---

## 177. Import Isolation

Large imports shall not block normal transactional workloads.

---

## 178. Database API Contracts

Database-facing services shall expose stable domain-level APIs rather than exposing raw database structures to clients.

---

## 179. Versioning

Database schema versions shall be tracked.

Example:

```text
schema_version
migration_version
application_compatibility_version
```

---

## 180. Compatibility

Application releases shall remain compatible with the database during rolling deployments.

---

## 181. Blue-Green Compatibility

Database changes shall support:

```text
Old Application
       +
New Application
       |
       v
Compatible Database Schema
```

---

## 182. Canary Releases

Database-impacting application releases should support canary deployment.

---

## 183. Feature Flags

Database-dependent feature rollouts should use feature flags for controlled activation.

---

## 184. Database Rollback

Application rollback shall not automatically imply unsafe database rollback.

Backward-compatible migrations shall be preferred.

---

## 185. Data Lineage

The platform shall be able to determine:

```text
Data source
Data owner
Transformation
Derived datasets
AI usage
Analytics usage
```

---

## 186. AI Data Lineage

AI-generated outputs shall reference source data where appropriate.

Example:

```text
AI Insight
   |
   +--> Customer
   +--> Conversation
   +--> Documents
   +--> Model
   +--> Knowledge Version
```

---

## 187. AI Explainability Metadata

Where applicable, database records shall preserve:

```text
model
model_version
input_reference
knowledge_version
prompt_version
decision_timestamp
confidence
human_review
```

---

## 188. Data Quality SLO

Critical data domains shall define quality targets for:

```text
Completeness
Accuracy
Consistency
Timeliness
Uniqueness
Validity
```

---

## 189. Database Acceptance Criteria

## AC-DB-001

PostgreSQL is the authoritative transactional database for core SalesGenie business data.

## AC-DB-002

Redis is not treated as the authoritative store for durable transactional records.

## AC-DB-003

Every tenant-owned record has enforceable tenant scope.

## AC-DB-004

Cross-tenant access is blocked.

## AC-DB-005

Database credentials are stored securely.

## AC-DB-006

Application services do not use database superuser credentials.

## AC-DB-007

Production connections use encryption.

## AC-DB-008

Database backups are automated.

## AC-DB-009

Point-in-time recovery is available for critical databases.

## AC-DB-010

Recovery procedures are tested.

## AC-DB-011

Database migrations are version-controlled.

## AC-DB-012

Production migrations support backward compatibility.

## AC-DB-013

Critical operations use ACID transactions.

## AC-DB-014

Deadlocks are detected and handled safely.

## AC-DB-015

Connection pools are bounded.

## AC-DB-016

Slow queries are observable.

## AC-DB-017

Database replication is observable.

## AC-DB-018

Database failover is tested.

## AC-DB-019

Large tables have an appropriate partitioning strategy.

## AC-DB-020

Indexes are monitored for effectiveness.

## AC-DB-021

Unused indexes are identified.

## AC-DB-022

Table and index bloat is monitored.

## AC-DB-023

Long-running transactions are detected.

## AC-DB-024

Database storage growth is monitored.

## AC-DB-025

Database connections are monitored.

## AC-DB-026

Database workloads are isolated from analytical workloads.

## AC-DB-027

Search indexes are treated as derived data.

## AC-DB-028

Object storage is used for large files.

## AC-DB-029

AI executions are auditable.

## AC-DB-030

AI-generated database queries cannot bypass authorization.

## AC-DB-031

AI-generated SQL is validated before execution.

## AC-DB-032

AI database mutations are policy-controlled.

## AC-DB-033

High-risk AI database mutations require human approval.

## AC-DB-034

AI database operations are auditable.

## AC-DB-035

AI database mutations can be disabled.

## AC-DB-036

AI database mutations can be rolled back where technically possible.

## AC-DB-037

AI cannot arbitrarily access another tenant's data.

## AC-DB-038

RLS or equivalent tenant isolation is tested.

## AC-DB-039

Production data is not exposed to development environments without approved masking.

## AC-DB-040

Database security incidents can trigger credential revocation and investigation.

---

## 190. Non-Functional Requirements

## NFR-DB-001 — Availability

Critical transactional databases shall target:

```text
99.99%+
```

where infrastructure permits.

---

## NFR-DB-002 — Performance

Initial target for typical same-region transactional queries:

```text
p50 < 20 ms
p95 < 100 ms
p99 < 250 ms
```

Targets shall be measured at the service boundary and refined according to workload.

---

## NFR-DB-003 — Scalability

The architecture shall support:

```text
10M+ users
Large multi-tenant deployments
High-volume conversations
High-volume messages
High-volume AI executions
High-volume analytics events
```

without requiring a single monolithic database instance.

---

## NFR-DB-004 — Reliability

No single database node shall represent an unacceptable single point of failure for critical workloads.

---

## NFR-DB-005 — Durability

Critical transactional data shall use durable storage and tested recovery mechanisms.

---

## NFR-DB-006 — Security

The system shall enforce:

```text
Least privilege
Tenant isolation
Encryption in transit
Encryption at rest
Authentication
Authorization
Auditing
Secret management
```

---

## NFR-DB-007 — Observability

Every production database shall provide sufficient telemetry for:

```text
Performance diagnosis
Capacity planning
Security investigation
Failure recovery
AI optimization
```

---

## NFR-DB-008 — Maintainability

Database schemas, migrations, indexes, and infrastructure definitions shall be version-controlled.

---

## NFR-DB-009 — Disaster Recovery

Critical databases shall support defined and tested RPO/RTO targets.

---

## NFR-DB-010 — Cost Efficiency

Database resources shall scale according to actual workload requirements.

---

## 191. Recommended Core Entity Model

```text
Organization
    |
    +---- Users
    |
    +---- Teams
    |
    +---- Roles
    |
    +---- Permissions
    |
    +---- Customers
    |       |
    |       +---- Contacts
    |       +---- Conversations
    |       +---- Tickets
    |       +---- Leads
    |
    +---- Leads
    |       |
    |       +---- Activities
    |       +---- Scores
    |
    +---- Opportunities
    |       |
    |       +---- Activities
    |       +---- Pipeline
    |
    +---- Conversations
    |       |
    |       +---- Messages
    |       +---- Participants
    |       +---- Attachments
    |
    +---- Knowledge Bases
    |       |
    |       +---- Documents
    |       +---- Chunks
    |       +---- Embeddings
    |
    +---- AI Agents
    |       |
    |       +---- Agent Versions
    |       +---- AI Runs
    |       +---- AI Decisions
    |
    +---- Workflows
    |       |
    |       +---- Executions
    |
    +---- Integrations
    |
    +---- Notifications
    |
    +---- Billing
    |
    +---- API Applications
    |
    +---- Webhooks
    |
    +---- Audit Logs
```

---

## 192. Recommended Database Topology

```text
                         Global Traffic
                              |
                              v
                         API Gateway
                              |
                 +------------+------------+
                 |                         |
                 v                         v
            Application               AI Gateway
                 |                         |
                 +------------+------------+
                              |
                              v
                       Database Router
                              |
          +-------------------+-------------------+
          |                   |                   |
          v                   v                   v
       Primary            Read Replica        Read Replica
          |
          v
     WAL / Replication
          |
     +----+----+
     |         |
     v         v
  Backup    DR Region
```

---

## 193. Recommended Data Flow

```text
User Request
     |
     v
API Gateway
     |
     v
Service
     |
     +------> Redis Cache
     |             |
     |             +---- Hit ----> Response
     |
     v
PostgreSQL
     |
     +------> Transaction
     |
     +------> Outbox Event
                    |
                    v
              Event Broker
                    |
        +-----------+-----------+
        |           |           |
        v           v           v
      Search     Analytics      AI
```

---

## 194. AI Database Architecture

```text
                         AI Gateway
                              |
                              v
                     AI Policy Engine
                              |
                    +---------+---------+
                    |                   |
                    v                   v
                Read Path           Write Path
                    |                   |
                    v                   v
              Query Validator     Mutation Validator
                    |                   |
                    v                   v
               PostgreSQL        Human Approval
                    |                   |
                    |                   v
                    |               Execute
                    |                   |
                    +---------+---------+
                              |
                              v
                         Audit System
```

---

## 195. Database Operational Lifecycle

```text
Design
  |
  v
Schema
  |
  v
Migration
  |
  v
Deploy
  |
  v
Monitor
  |
  v
Optimize
  |
  v
Scale
  |
  v
Archive
  |
  v
Retain/Delete
```

---

## 196. Definition of Done

* [ ] PostgreSQL primary architecture implemented.
* [ ] Database-per-service boundaries defined.
* [ ] Tenant isolation implemented.
* [ ] Tenant-aware schema design implemented.
* [ ] RBAC persistence implemented.
* [ ] Core customer schema implemented.
* [ ] Lead schema implemented.
* [ ] Sales opportunity schema implemented.
* [ ] Conversation schema implemented.
* [ ] Message schema implemented.
* [ ] Support-ticket schema implemented.
* [ ] AI-agent schema implemented.
* [ ] AI-run schema implemented.
* [ ] AI-decision schema implemented.
* [ ] Workflow schema implemented.
* [ ] Workflow-execution schema implemented.
* [ ] RAG metadata schema implemented.
* [ ] Document metadata schema implemented.
* [ ] Embedding metadata implemented.
* [ ] Integration schema implemented.
* [ ] Notification schema implemented.
* [ ] Billing schema implemented.
* [ ] Developer-platform schema implemented.
* [ ] Webhook schema implemented.
* [ ] Audit schema implemented.
* [ ] Primary keys standardized.
* [ ] UUID/UUIDv7 strategy implemented.
* [ ] Audit fields standardized.
* [ ] Database constraints implemented.
* [ ] Foreign-key strategy implemented.
* [ ] Indexing strategy implemented.
* [ ] Composite indexes implemented where required.
* [ ] Partial indexes implemented where required.
* [ ] Partitioning implemented for high-volume tables.
* [ ] Connection pooling implemented.
* [ ] Query timeout implemented.
* [ ] Transaction management implemented.
* [ ] Deadlock handling implemented.
* [ ] Optimistic concurrency implemented.
* [ ] Read replicas implemented where required.
* [ ] Replication implemented.
* [ ] Automated failover implemented.
* [ ] Backups implemented.
* [ ] Point-in-time recovery implemented.
* [ ] Disaster recovery implemented.
* [ ] Recovery testing completed.
* [ ] Migration framework implemented.
* [ ] Zero-downtime migration strategy implemented.
* [ ] Schema compatibility strategy implemented.
* [ ] Database encryption at rest enabled.
* [ ] TLS enabled.
* [ ] Database credentials moved to secrets management.
* [ ] Least-privilege database roles implemented.
* [ ] Application superuser access eliminated.
* [ ] RLS or equivalent tenant isolation implemented.
* [ ] SQL injection protection implemented.
* [ ] Database audit logging implemented.
* [ ] Query monitoring implemented.
* [ ] Slow-query monitoring implemented.
* [ ] Lock monitoring implemented.
* [ ] Deadlock monitoring implemented.
* [ ] Storage monitoring implemented.
* [ ] Replication monitoring implemented.
* [ ] Backup monitoring implemented.
* [ ] Database SLOs defined.
* [ ] Database capacity monitoring implemented.
* [ ] Tenant quota monitoring implemented.
* [ ] Noisy-neighbor protection implemented.
* [ ] Outbox pattern implemented where required.
* [ ] CDC implemented where required.
* [ ] Search synchronization implemented.
* [ ] Analytics synchronization implemented.
* [ ] Object storage integration implemented.
* [ ] Data retention policies implemented.
* [ ] Data export implemented.
* [ ] Data deletion implemented.
* [ ] Data masking implemented.
* [ ] Data quality checks implemented.
* [ ] AI database service identity implemented.
* [ ] AI database authorization implemented.
* [ ] AI SQL validation implemented.
* [ ] AI query resource limits implemented.
* [ ] AI database audit logging implemented.
* [ ] AI index recommendations implemented.
* [ ] AI query optimization implemented.
* [ ] AI capacity forecasting implemented.
* [ ] AI anomaly detection implemented.
* [ ] AI cost optimization implemented.
* [ ] AI database risk classification implemented.
* [ ] Human approval workflow implemented.
* [ ] AI mutation kill switch implemented.
* [ ] AI rollback mechanism implemented.
* [ ] AI tenant isolation tested.
* [ ] AI prompt-injection defenses tested.
* [ ] AI SQL-injection defenses tested.
* [ ] Performance tests completed.
* [ ] Load tests completed.
* [ ] Stress tests completed.
* [ ] Concurrency tests completed.
* [ ] Migration tests completed.
* [ ] Security tests completed.
* [ ] Tenant-isolation tests completed.
* [ ] Chaos tests completed.
* [ ] Backup/restore tests completed.
* [ ] Failover tests completed.
* [ ] Operational runbooks completed.
* [ ] Database dependency maps documented.
* [ ] Database ownership documented.
* [ ] Production readiness review completed.
