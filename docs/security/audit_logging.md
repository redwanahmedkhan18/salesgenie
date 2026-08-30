# SalesGenie — FAANG-Level Audit Logging Requirements

## `audit_logging.md`

> **Scope:** Enterprise-grade audit logging and security event management for SalesGenie, covering human users, AI agents, administrators, microservices, integrations, workflows, authentication, authorization, data access, billing, subscriptions, customer support, sales operations, RAG, AI inference, configuration changes, security events, and platform administration.
>
> **Core principle:** Every security-relevant, compliance-relevant, financially relevant, privacy-relevant, administrative, AI-agent, and integration operation MUST be attributable, tamper-resistant, searchable, privacy-aware, and correlated across the distributed SalesGenie platform.

---

## 1. Audit Logging Objectives

SalesGenie MUST provide a centralized audit logging platform capable of:

- Capturing security-relevant events
- Capturing human actions
- Capturing AI-agent actions
- Capturing service-to-service actions
- Capturing administrator actions
- Capturing integration activity
- Capturing authentication events
- Capturing authorization decisions
- Capturing data-access events
- Capturing configuration changes
- Capturing billing events
- Capturing subscription events
- Capturing workflow execution events
- Capturing AI tool calls
- Capturing RAG access
- Capturing sensitive-data access
- Detecting suspicious activity
- Supporting forensic investigations
- Supporting compliance audits
- Providing immutable or tamper-evident records
- Correlating distributed events
- Providing tenant-level audit visibility
- Providing platform-level security visibility
- Preventing secret leakage through logs
- Supporting long-term retention policies
- Supporting secure log export
- Supporting automated security detection
- Supporting human and AI-assisted investigations

---

## 2. Actors

## 2.1 Human Actors

### H-001 — End User

The end user MUST be able to perform normal platform operations without receiving access to audit records they are not authorized to view.

### H-002 — Sales Agent

A sales agent MUST be able to view only audit information permitted by their organization role and scope.

### H-003 — Support Agent

A support agent MUST be able to access relevant customer-support audit information without gaining unrestricted access to security audit data.

### H-004 — Organization Administrator

An organization administrator MUST be able to review organization-level audit activity.

### H-005 — Security Administrator

A security administrator MUST be able to investigate security events, authentication events, authorization failures, suspicious behavior, and administrative actions.

### H-006 — Super Administrator

A super administrator MUST be able to investigate platform-wide audit events according to privileged-access policies.

### H-007 — Compliance Auditor

A compliance auditor MUST be able to inspect audit records, retention history, access history, and compliance-relevant events.

### H-008 — Incident Responder

An incident responder MUST be able to rapidly query, correlate, export, and preserve relevant audit evidence.

---

## 3. AI Actors

### AI-001 — AI Sales Agent

The AI sales agent MUST generate auditable events whenever it performs a consequential operation.

### AI-002 — AI Support Agent

The AI support agent MUST generate audit events for customer-data retrieval, tool usage, ticket updates, and external actions.

### AI-003 — AI Workflow Agent

The AI workflow agent MUST generate audit events for workflow decisions, tool calls, state transitions, and external side effects.

### AI-004 — AI Orchestrator

The AI orchestrator MUST provide traceable attribution for agent selection, delegation, tool invocation, and execution.

### AI-005 — AI Tool-Calling Layer

Every consequential AI tool invocation MUST be auditable.

### AI-006 — AI Security Agent

An AI security agent MAY analyze audit records but MUST operate under explicit authorization boundaries.

### AI-007 — AI Investigation Agent

An authorized AI investigation agent MAY summarize audit events but MUST NOT modify the original audit evidence.

---

## 4. User Requirements

## UR-001 — Activity Transparency

Authorized users MUST be able to understand significant activity performed within their SalesGenie organization.

## UR-002 — Security Transparency

Authorized administrators MUST be able to determine:

- Who performed an action
- What action occurred
- When it occurred
- Which resource was affected
- Which organization was affected
- Whether the operation succeeded
- Why the operation occurred when available
- Which service performed the operation
- Whether AI was involved

## UR-003 — Human Attribution

Human actions MUST be associated with a stable user identity.

## UR-004 — AI Attribution

AI-generated actions MUST clearly indicate:

- AI agent identity
- Agent version
- Model/provider where appropriate
- Parent user
- Parent session
- Tool used
- Authorization context
- Execution trace

## UR-005 — Tenant Isolation

Users MUST never be able to retrieve audit events belonging to another tenant unless explicitly authorized through platform-level privileges.

## UR-006 — Audit Search

Authorized users MUST be able to search audit records using appropriate filters.

## UR-007 — Audit Export

Authorized users MUST be able to export audit evidence according to security and compliance policy.

## UR-008 — Audit Integrity

Users MUST be able to trust that audit records cannot be silently modified or deleted.

## UR-009 — Privacy

Audit logging MUST NOT unnecessarily expose sensitive personal information, credentials, secrets, or private customer data.

## UR-010 — Incident Investigation

Security personnel MUST be able to reconstruct relevant sequences of events during an incident.

## UR-011 — Compliance Evidence

The platform MUST provide sufficient audit evidence for applicable enterprise compliance requirements.

---

## 5. System Requirements

## SR-001 — Centralized Audit Architecture

SalesGenie MUST provide a centralized audit-event architecture.

```text
Human Users
     |
AI Agents
     |
Microservices
     |
Integrations
     |
     v
Audit Event SDK
     |
     v
Audit Ingestion API
     |
     v
Event Bus / Streaming Layer
     |
     +------------------+
     |                  |
     v                  v
Hot Audit Store     Immutable Store
     |                  |
     +---------+--------+
               |
               v
       Audit Query Service
               |
       +-------+-------+
       |               |
       v               v
 Security Dashboard  Compliance
                     Reporting
```

---

## SR-002 — Central Audit Event Schema

All services MUST use a standardized audit-event schema.

Minimum fields SHOULD include:

```yaml
event_id:
event_type:
event_version:
timestamp:
tenant_id:
actor_type:
actor_id:
actor_role:
service_id:
resource_type:
resource_id:
action:
operation:
result:
severity:
source_ip:
user_agent:
session_id:
request_id:
trace_id:
parent_event_id:
ai_agent_id:
ai_model:
tool_id:
authorization_decision:
reason:
metadata:
```

---

## SR-003 — Immutable Event Identity

Every audit event MUST have a globally unique identifier.

Example:

```text
event_id = evt_01JXXXX...
```

The identifier MUST remain stable for the lifetime of the audit record.

---

## SR-004 — Event Versioning

Audit events MUST support schema versioning.

Example:

```text
audit.event.v1
audit.event.v2
audit.event.v3
```

Schema changes MUST preserve backward compatibility or provide migration/version interpretation mechanisms.

---

## SR-005 — Timestamp Integrity

Audit records MUST use trusted server-side timestamps.

Client-provided timestamps MUST NOT be treated as authoritative.

Timestamps SHOULD use UTC and a standardized representation such as ISO 8601.

---

## SR-006 — Distributed Trace Correlation

Audit events MUST support:

* request ID
* correlation ID
* trace ID
* span ID where applicable
* parent event ID

This MUST allow distributed workflows to be reconstructed.

---

## SR-007 — Tenant Context

Every tenant-scoped audit event MUST contain an authoritative tenant identifier.

Tenant identity MUST be derived from trusted authorization context rather than arbitrary client input.

---

## SR-008 — Actor Classification

The system MUST distinguish between:

```text
HUMAN
AI_AGENT
SERVICE
SYSTEM
AUTOMATION
ADMINISTRATOR
EXTERNAL_INTEGRATION
```

---

## SR-009 — Audit Storage Separation

Audit data SHOULD be stored separately from ordinary application databases to reduce the risk of attackers modifying both operational data and audit evidence.

---

## SR-010 — Tamper Resistance

Audit records MUST be protected against:

* unauthorized modification
* unauthorized deletion
* unauthorized insertion
* privilege escalation
* log forgery
* replay
* truncation
* unauthorized retention changes

---

## SR-011 — Append-Only Architecture

Audit events SHOULD be append-only.

Updates to an audit record SHOULD NOT be permitted.

Corrections MUST be represented through a new audit event.

---

## SR-012 — Cryptographic Integrity

Critical audit infrastructure SHOULD support cryptographic integrity mechanisms such as:

* digital signatures
* hash chaining
* signed batches
* authenticated event envelopes
* immutable object storage

---

## SR-013 — Log Encryption

Audit records MUST be encrypted at rest.

Audit transport MUST use secure encrypted communication.

---

## SR-014 — Access Control

Audit access MUST use:

* RBAC
* ABAC where appropriate
* tenant isolation
* least privilege
* privileged-access controls
* MFA for high-risk administrative access

---

## SR-015 — Audit-of-Audit

The system MUST audit access to audit records.

Examples:

```text
audit.view
audit.search
audit.export
audit.download
audit.retention_changed
audit.policy_changed
```

---

## SR-016 — No Secret Logging

The platform MUST prevent logging of:

* passwords
* API keys
* access tokens
* refresh tokens
* OAuth secrets
* encryption keys
* private keys
* database credentials
* session secrets
* payment credentials
* authorization headers
* cookies containing credentials

---

## 6. Functional Requirements — Core Audit Engine

## FR-001 — Create Audit Event

The platform MUST allow authorized services to create audit events.

```http
POST /api/v1/audit/events
```

The endpoint MUST validate:

* actor identity
* tenant context
* event type
* schema version
* timestamp
* resource
* action
* result

---

## FR-002 — Validate Audit Event

The ingestion service MUST reject malformed or incomplete events according to event-type requirements.

---

## FR-003 — Generate Event ID

The platform MUST generate a unique event ID when not supplied by a trusted upstream component.

---

## FR-004 — Record Event Outcome

Events MUST indicate outcome:

```text
SUCCESS
FAILURE
DENIED
PARTIAL
TIMEOUT
CANCELLED
```

---

## FR-005 — Record Severity

Events SHOULD support:

```text
DEBUG
INFO
NOTICE
WARNING
HIGH
CRITICAL
```

---

## FR-006 — Event Categorization

Events MUST be categorized.

Recommended categories:

```text
AUTHENTICATION
AUTHORIZATION
IDENTITY
SECURITY
DATA_ACCESS
DATA_MODIFICATION
AI
INTEGRATION
WORKFLOW
BILLING
SUBSCRIPTION
PAYMENT
ADMINISTRATION
CONFIGURATION
COMPLIANCE
SYSTEM
```

---

## 7. Authentication Audit Requirements

The system MUST audit:

```text
login.success
login.failure
logout
session.created
session.revoked
session.expired
password.changed
password.reset
mfa.enabled
mfa.disabled
mfa.success
mfa.failure
oauth.authorized
oauth.revoked
account.locked
account.unlocked
```

---

## 8. Authorization Audit Requirements

The system MUST audit important authorization decisions.

Examples:

```text
authorization.granted
authorization.denied
role.assigned
role.removed
permission.granted
permission.revoked
policy.created
policy.updated
policy.deleted
privileged_access.granted
privileged_access.denied
```

---

## 9. User Management Audit Requirements

The platform MUST audit:

```text
user.created
user.updated
user.deleted
user.suspended
user.unsuspended
user.invited
user.invitation_accepted
user.role_changed
user.designation_changed
user.tenant_changed
user.profile_updated
```

---

## 10. Super Admin Audit Requirements

Super-admin actions MUST receive elevated audit treatment.

The platform MUST record:

```text
admin.user_created
admin.user_banned
admin.user_unbanned
admin.role_changed
admin.tenant_created
admin.tenant_suspended
admin.tenant_deleted
admin.configuration_changed
admin.security_policy_changed
admin.audit_policy_changed
admin.data_access
admin.data_export
admin.impersonation_started
admin.impersonation_ended
```

---

## 11. Impersonation Audit Requirements

If authorized impersonation exists, the audit record MUST identify:

```text
actual_actor
impersonated_user
reason
approval
start_time
end_time
session_id
```

Every action performed during impersonation MUST remain attributable to both identities.

---

## 12. AI Audit Requirements

AI operations MUST be first-class audit events.

The system MUST capture:

```text
ai.session.created
ai.request.received
ai.agent.selected
ai.agent.delegated
ai.prompt.processed
ai.tool.invoked
ai.tool.completed
ai.tool.failed
ai.data.retrieved
ai.data.filtered
ai.workflow.executed
ai.action.approved
ai.action.denied
ai.output.generated
ai.output.blocked
ai.guardrail.triggered
ai.policy_violation.detected
```

---

## 13. AI Agent Attribution

Every consequential AI action MUST contain:

```yaml
ai:
  agent_id:
  agent_version:
  model_provider:
  model:
  execution_id:
  parent_user_id:
  parent_session_id:
  tool_id:
  tool_call_id:
  policy_id:
```

---

## 14. AI Tool-Call Auditing

Every tool call MUST record:

```text
Tool Name
Tool Version
Calling Agent
Calling User
Tenant
Requested Operation
Authorization Decision
Execution Result
Execution Duration
External Resource
Trace ID
```

Sensitive tool parameters MUST be redacted or hashed according to policy.

---

## 15. AI Human-in-the-Loop Audit

When an AI action requires human approval, the system MUST record:

```text
AI action proposed
Human reviewer
Approval/rejection
Approval timestamp
Reason
Final action
Result
```

---

## 16. AI Autonomous Action Audit

If an AI agent is authorized to act autonomously, the audit record MUST identify:

```text
automation policy
agent
policy version
trigger
action
resource
authorization context
result
```

---

## 17. RAG Audit Requirements

The platform MUST audit:

```text
rag.collection.created
rag.document.uploaded
rag.document.updated
rag.document.deleted
rag.document.retrieved
rag.document.shared
rag.embedding.created
rag.embedding.deleted
rag.search.executed
rag.access.denied
rag.permission.changed
```

---

## 18. Data Access Audit Requirements

Sensitive data access SHOULD be audited.

Examples:

```text
customer.profile.viewed
customer.profile.updated
customer.data.exported
conversation.viewed
conversation.exported
document.viewed
document.downloaded
pii.accessed
sensitive_record.accessed
```

The system MUST avoid storing the full sensitive payload in the audit record.

---

## 19. Data Modification Audit Requirements

The system MUST audit high-value mutations.

Examples:

```text
record.created
record.updated
record.deleted
record.restored
record.bulk_updated
record.bulk_deleted
```

Where appropriate, audit events SHOULD contain before/after metadata rather than full sensitive records.

---

## 20. Integration Audit Requirements

SalesGenie MUST audit integration lifecycle and operational events.

Examples:

```text
integration.created
integration.connected
integration.updated
integration.disconnected
integration.deleted
integration.authenticated
integration.authentication_failed
integration.sync_started
integration.sync_completed
integration.sync_failed
integration.webhook_received
integration.rate_limited
```

Applicable integrations include:

```text
Google
Google Drive
Gmail
LinkedIn
Facebook
Instagram
WhatsApp
YouTube
TikTok
Slack
Zendesk
Salesforce
HubSpot
Jira
Notion
Microsoft Teams
```

---

## 21. OAuth Audit Requirements

The system MUST audit:

```text
oauth.authorization_started
oauth.authorization_completed
oauth.authorization_failed
oauth.token_issued
oauth.token_refreshed
oauth.token_revoked
oauth.scope_changed
```

Tokens MUST NOT appear in audit records.

---

## 22. Workflow Audit Requirements

The workflow engine MUST audit:

```text
workflow.created
workflow.updated
workflow.enabled
workflow.disabled
workflow.started
workflow.completed
workflow.failed
workflow.cancelled
workflow.paused
workflow.resumed
workflow.step_started
workflow.step_completed
workflow.step_failed
workflow.approval_requested
workflow.approval_granted
workflow.approval_denied
```

---

## 23. Billing Audit Requirements

Billing operations MUST be auditable.

Examples:

```text
billing.plan_created
billing.plan_updated
billing.plan_deleted
billing.subscription_created
billing.subscription_updated
billing.subscription_cancelled
billing.payment_started
billing.payment_succeeded
billing.payment_failed
billing.refund_requested
billing.refund_completed
billing.invoice_created
billing.invoice_paid
billing.invoice_failed
billing.coupon_applied
billing.credit_added
billing.credit_removed
```

Payment credentials MUST never be logged.

---

## 24. Subscription Audit Requirements

The platform MUST audit:

```text
subscription.started
subscription.trial_started
subscription.trial_ended
subscription.upgraded
subscription.downgraded
subscription.paused
subscription.resumed
subscription.renewed
subscription.cancelled
subscription.expired
subscription.reactivated
```

---

## 25. Configuration Audit Requirements

The system MUST audit changes to:

```text
security configuration
AI configuration
model configuration
integration configuration
workflow configuration
billing configuration
subscription configuration
tenant configuration
feature flags
rate limits
quotas
permissions
retention policies
audit policies
```

---

## 26. Key Management Audit Requirements

Cryptographic lifecycle operations MUST be audited.

Examples:

```text
key.created
key.enabled
key.disabled
key.rotated
key.revoked
key.destroy_requested
key.destroyed
key.policy_changed
key.encrypt
key.decrypt
key.wrap
key.unwrap
key.access_denied
```

Plaintext key material MUST never be logged.

---

## 27. Security Event Audit Requirements

The system MUST capture:

```text
security.alert_created
security.alert_acknowledged
security.alert_resolved
security.policy_violation
security.anomaly_detected
security.suspicious_login
security.brute_force_detected
security.credential_exposure
security.cross_tenant_attempt
security.privilege_escalation_attempt
security.rate_limit_violation
security.secret_detected
```

---

## 28. API Audit Requirements

Important API operations MUST be auditable.

The platform SHOULD record:

```text
HTTP method
endpoint category
authenticated principal
tenant
authorization result
status code
latency
request ID
trace ID
resource ID
```

Raw request bodies MUST NOT automatically be logged.

---

## 29. Bulk Operation Audit Requirements

Bulk operations MUST produce audit records.

Examples:

```text
bulk_user_update
bulk_user_delete
bulk_data_export
bulk_record_update
bulk_record_delete
bulk_permission_change
bulk_key_rotation
```

The event MUST indicate:

```text
operation_id
initiator
scope
affected_count
success_count
failure_count
```

---

## 30. Search Requirements

Authorized users MUST be able to search by:

```text
event_id
event_type
tenant_id
actor_id
actor_type
service_id
resource_type
resource_id
action
result
severity
timestamp
IP
trace_id
request_id
AI agent
integration
```

---

## 31. Advanced Audit Filtering

The system SHOULD support combinations such as:

```text
tenant = tenant_123
AND actor_type = AI_AGENT
AND action = data_access
AND severity >= HIGH
AND timestamp >= last_24_hours
```

---

## 32. Audit Timeline

The UI MUST provide a chronological timeline.

Example:

```text
10:01:02  User login
10:01:04  AI session created
10:01:05  RAG search executed
10:01:06  Salesforce contact retrieved
10:01:08  AI generated recommendation
10:01:11  Human approval requested
10:01:25  Human approved
10:01:27  Salesforce update completed
```

---

## 33. Distributed Trace Reconstruction

The system MUST support reconstructing:

```text
User Request
     |
     v
API Gateway
     |
     v
AI Gateway
     |
     v
Agent Orchestrator
     |
     v
RAG Service
     |
     v
Salesforce Integration
     |
     v
External Salesforce API
```

using shared trace and correlation identifiers.

---

## 34. Audit Export

Authorized users MUST be able to export audit records.

Supported formats SHOULD include:

```text
JSON
CSV
NDJSON
PDF
```

Export MUST be:

* authorization-controlled
* logged
* integrity-protected
* optionally encrypted
* rate-limited

---

## 35. Audit Export Security

Every export MUST generate an audit event:

```text
audit.export.started
audit.export.completed
audit.export.failed
```

The system MUST record:

```text
exporter
scope
filters
record_count
timestamp
destination
reason
```

---

## 36. Retention Requirements

Retention MUST be configurable by:

```text
tenant
event category
severity
compliance policy
environment
data classification
```

Example:

```yaml
retention:
  security_events: 3650d
  authentication: 730d
  billing: 2555d
  ai_activity: 730d
  standard_activity: 365d
```

Actual periods MUST be configurable according to applicable legal, contractual, and business requirements.

---

## 37. Legal Hold

The platform SHOULD support legal holds.

When a legal hold applies:

```text
Retention policy
      |
      v
Legal Hold
      |
      v
Deletion blocked
```

Audit evidence under legal hold MUST not be automatically deleted.

---

## 38. Audit Deletion

Normal users MUST never be able to delete audit events.

Privileged deletion, where legally required, MUST require:

* strong authorization
* documented reason
* approval
* immutable audit trail
* retention-policy validation

---

## 39. Log Integrity

The system SHOULD support hash chaining.

Example:

```text
Event A
   |
   v
Hash A
   |
   v
Event B + Hash A
   |
   v
Hash B
   |
   v
Event C + Hash B
```

Tampering with historical events SHOULD be detectable.

---

## 40. Log Ingestion Reliability

The audit pipeline MUST tolerate temporary downstream failures.

It SHOULD support:

* durable queues
* retries
* dead-letter queues
* backpressure
* replay
* deduplication
* idempotent ingestion

---

## 41. Audit Event Delivery Semantics

The system SHOULD support:

```text
At-least-once delivery
```

with deduplication based on:

```text
event_id
```

Critical events SHOULD have stronger delivery guarantees where technically feasible.

---

## 42. Dead-Letter Queue

Failed audit events MUST be routed to a controlled dead-letter mechanism rather than silently discarded.

The system MUST alert when the dead-letter queue exceeds configured thresholds.

---

## 43. Audit Loss Prevention

The platform MUST NOT silently drop security-critical events.

If audit infrastructure is unavailable, the platform MUST follow a predefined policy:

```text
FAIL-CLOSED
FAIL-OPEN
LOCAL-BUFFER
DEFERRED-AUDIT
```

Critical security operations SHOULD prefer fail-closed or durable local buffering.

---

## 44. Privacy Requirements

Audit logs MUST follow data minimization principles.

The platform SHOULD store:

```text
resource_id
operation
classification
result
metadata
```

instead of entire sensitive payloads.

---

## 45. PII Redaction

Sensitive values MUST be automatically redacted where necessary.

Examples:

```text
email -> r***@example.com
phone -> ********1234
token -> [REDACTED]
password -> [REDACTED]
api_key -> [REDACTED]
```

---

## 46. Secret Detection

The audit pipeline SHOULD detect accidental secret leakage using:

* pattern matching
* entropy analysis
* credential detectors
* token signatures
* provider-specific secret patterns

Detected secrets MUST be removed or quarantined according to security policy.

---

## 47. AI Log Redaction

AI prompts and responses MUST NOT automatically be stored in full audit logs.

The platform SHOULD store:

```text
prompt_hash
response_hash
prompt classification
response classification
token counts
model
agent
tool calls
policy decisions
```

Full prompts/responses MAY be stored separately only where permitted by tenant policy, privacy requirements, and data-retention rules.

---

## 48. Human Access to Audit Logs

Audit access MUST follow:

```text
Identity
   +
Role
   +
Tenant
   +
Resource Scope
   +
Purpose
   +
Policy
```

---

## 49. AI Access to Audit Logs

AI systems MUST access audit data through a controlled audit-query interface.

AI agents MUST NOT receive unrestricted database access.

---

## 50. AI Investigation Requirements

Authorized AI investigation agents MAY:

* summarize events
* identify anomalies
* correlate traces
* classify incidents
* identify suspicious sequences
* generate investigation timelines
* recommend remediation

AI agents MUST NOT:

* modify audit records
* delete evidence
* disable audit logging
* alter retention policies
* suppress security events
* rewrite event history

unless explicitly authorized by a separately governed automation policy.

---

## 51. AI Audit Analytics

The platform SHOULD support AI-assisted detection of:

```text
Impossible travel
Unusual login patterns
Mass data access
Abnormal API usage
Cross-tenant access attempts
Unusual AI tool calls
Agent privilege escalation
Credential misuse
Unexpected integration activity
Mass export behavior
Unusual billing activity
```

AI-generated detections MUST reference the underlying audit evidence.

---

## 52. Human Approval for AI Security Actions

AI-generated security recommendations SHOULD use:

```text
Detection
   |
   v
Evidence
   |
   v
AI Recommendation
   |
   v
Human Approval
   |
   v
Security Action
   |
   v
Audit Event
```

---

## 53. Alerting Requirements

The system MUST support alerts based on:

* event type
* severity
* frequency
* actor
* tenant
* resource
* geographic context
* AI agent
* service
* integration
* correlated events

---

## 54. Correlation Rules

The detection engine SHOULD support rules such as:

```text
IF
  user.login.failure >= 10
  WITHIN 5 minutes
THEN
  create security alert
```

Another example:

```text
IF
  AI_AGENT performs > N sensitive_data_access operations
  WITHIN 10 minutes
  AND
  access pattern deviates from baseline
THEN
  create high-risk alert
```

---

## 55. Audit Dashboard

The Super Admin Control Center SHOULD contain:

```text
Total Events
Critical Events
High-Risk Events
Failed Logins
Authorization Denials
AI Actions
Integration Events
Data Access Events
Admin Actions
Billing Events
Security Alerts
Audit Pipeline Health
Storage Health
Retention Status
```

---

## 56. Tenant Audit Dashboard

Organization administrators SHOULD see:

```text
User Activity
AI Activity
Integration Activity
Workflow Activity
Data Access
Security Events
Authentication Events
Administrative Events
Export Activity
```

Only authorized event categories MUST be displayed.

---

## 57. Real-Time Audit Stream

Security administrators SHOULD be able to view near-real-time events.

Example:

```text
[10:32:01] HIGH  AI_AGENT data_access
[10:32:03] INFO  OAuth token refreshed
[10:32:04] WARN  Authorization denied
[10:32:06] CRITICAL Cross-tenant access attempt
```

---

## 58. Audit API

Recommended API surface:

```http
POST   /api/v1/audit/events
GET    /api/v1/audit/events
GET    /api/v1/audit/events/{event_id}
POST   /api/v1/audit/search
GET    /api/v1/audit/timeline
GET    /api/v1/audit/actors/{actor_id}
GET    /api/v1/audit/resources/{resource_id}
GET    /api/v1/audit/trace/{trace_id}
POST   /api/v1/audit/export
GET    /api/v1/audit/exports/{export_id}
GET    /api/v1/audit/statistics
GET    /api/v1/audit/health
GET    /api/v1/audit/retention
```

---

## 59. Audit Event Example

```json
{
  "event_id": "evt_01JXYZ",
  "event_type": "ai.tool.invoked",
  "event_version": "1.0",
  "timestamp": "2026-08-28T10:30:25Z",
  "tenant_id": "tenant_123",
  "actor_type": "AI_AGENT",
  "actor_id": "agent_sales_001",
  "parent_user_id": "user_456",
  "service_id": "ai_gateway",
  "resource_type": "salesforce_contact",
  "resource_id": "contact_789",
  "action": "read",
  "result": "SUCCESS",
  "severity": "INFO",
  "request_id": "req_123",
  "trace_id": "trace_456",
  "ai_agent_id": "agent_sales_001",
  "ai_model": "configured_model",
  "tool_id": "salesforce.get_contact",
  "authorization_decision": "ALLOW",
  "metadata": {
    "purpose": "sales_assistance"
  }
}
```

---

## 60. Audit Event Privacy Rule

The event above MUST NOT contain:

```text
Salesforce OAuth token
API secret
Customer password
Encryption key
Full credit-card number
Session secret
Private cryptographic material
```

---

## 61. Audit Storage Architecture

Recommended:

```text
                   +----------------+
                   | API Gateway    |
                   +-------+--------+
                           |
                           v
                   +---------------+
                   | Audit SDK     |
                   +-------+-------+
                           |
                           v
                   +---------------+
                   | Audit Ingest  |
                   +-------+-------+
                           |
                           v
                    +-------------+
                    | Event Bus    |
                    +------+------+
                           |
              +------------+-------------+
              |                          |
              v                          v
       +-------------+            +-------------+
       | Hot Store   |            | Immutable   |
       | Search      |            | Archive     |
       +------+------+            +------+------+
              |                          |
              +------------+-------------+
                           |
                           v
                  +----------------+
                  | Audit Query API |
                  +--------+-------+
                           |
              +------------+-------------+
              |                          |
              v                          v
       Security Dashboard        Compliance UI
```

---

## 62. Performance Requirements

The audit system MUST support high-volume distributed workloads.

It SHOULD support:

* asynchronous ingestion
* batching
* partitioning
* streaming
* backpressure
* horizontal scaling
* indexed search
* time-based partitioning
* archival tiers

Audit logging MUST NOT introduce unacceptable latency to user-facing operations.

---

## 63. Scalability Requirements

The architecture MUST support:

```text
10M+ users
500K+ concurrent conversations
Millions of daily audit events
Large-scale AI tool activity
Large-scale integration events
Large-scale workflow execution
```

The exact capacity MUST be validated through load testing.

---

## 64. Availability Requirements

Critical audit ingestion SHOULD target:

```text
>= 99.99% availability
```

The audit platform SHOULD support:

* multi-instance deployment
* multi-zone deployment
* durable event queues
* automated recovery
* health checks

---

## 65. Security Requirements

The audit platform MUST:

* use encrypted transport
* use encrypted storage
* enforce least privilege
* enforce tenant isolation
* protect audit APIs
* protect audit exports
* prevent secret logging
* detect tampering
* protect administrative operations
* audit audit-access operations

---

## 66. Network Security

Audit services SHOULD be isolated in a protected service network.

External clients MUST NOT directly access audit storage.

```text
Internet
   |
   v
API Gateway
   |
   v
Audit API
   |
   v
Private Audit Network
   |
   +--> Event Bus
   +--> Audit Store
   +--> Immutable Archive
```

---

## 67. Database Security

Audit databases MUST use:

* encryption at rest
* restricted service accounts
* network segmentation
* database-level access controls
* backup encryption
* audit trails
* controlled administrative access

---

## 68. Backup Requirements

Audit records MUST be backed up according to retention and compliance requirements.

Backups MUST:

* be encrypted
* have restricted access
* be integrity protected
* be tested for restoration

---

## 69. Disaster Recovery

The audit platform MUST define:

```text
RPO
RTO
Backup frequency
Replication strategy
Failover strategy
Recovery procedure
Audit continuity procedure
```

---

## 70. Clock Synchronization

Production services generating audit events MUST use reliable time synchronization.

The platform SHOULD use centralized or trusted time sources to reduce timestamp inconsistencies across microservices.

---

## 71. Event Ordering

The system MUST NOT assume that distributed events always arrive in chronological order.

Audit reconstruction SHOULD use:

```text
timestamp
sequence number
trace ID
span ID
parent event ID
service timestamp
ingestion timestamp
```

---

## 72. Duplicate Event Handling

Duplicate events MUST be detectable.

The system SHOULD use:

```text
event_id
idempotency_key
source_event_id
```

to prevent duplicate audit records from corrupting analytics.

---

## 73. Replay Protection

Replayed audit events MUST be detected where event authenticity and ordering require it.

---

## 74. Service Identity

Every microservice MUST have a unique service identity.

Example:

```text
auth-service
ai-gateway
rag-service
workflow-service
billing-service
integration-service
whatsapp-service
lead-intelligence-service
audit-service
```

Service identities MUST be included in relevant audit events.

---

## 75. Integration Identity

External integrations MUST be represented as distinct actor or source identities.

Example:

```text
salesforce-prod
hubspot-prod
gmail-prod
slack-prod
zendesk-prod
```

---

## 76. Sensitive Operation Classification

SalesGenie SHOULD classify operations into:

```text
LOW
MEDIUM
HIGH
CRITICAL
```

Examples:

```text
LOW:
Profile viewed

MEDIUM:
Record updated

HIGH:
Bulk data export

CRITICAL:
Production security policy changed
```

---

## 77. Critical Event Handling

Critical events SHOULD:

* bypass ordinary buffering limits where possible
* receive immediate persistence priority
* generate alerts
* receive extended retention
* be replicated
* be protected from automated deletion

---

## 78. Audit Policy Engine

The platform SHOULD provide configurable audit policies.

Example:

```yaml
audit_policy:
  customer_data_access:
    enabled: true

  ai_tool_calls:
    enabled: true

  prompt_logging:
    enabled: false

  billing_events:
    enabled: true

  admin_actions:
    enabled: true

  retention:
    default_days: 365
```

---

## 79. Tenant Audit Policy

Organizations SHOULD be able to configure permitted audit behaviors within platform limits.

Example:

```text
AI logging
Integration logging
Data-access logging
Export logging
Retention configuration
```

Platform security policies MUST take precedence over tenant preferences.

---

## 80. Data Residency

Where required, audit records SHOULD support region-specific storage.

Example:

```text
EU Tenant
   |
   v
EU Audit Region

US Tenant
   |
   v
US Audit Region
```

---

## 81. Compliance Reporting

The system SHOULD generate reports for:

```text
User access
Administrative activity
Security events
Data access
AI activity
Integration activity
Billing activity
Configuration changes
Authentication
Authorization
```

---

## 82. Compliance Evidence Integrity

Exported compliance evidence SHOULD include:

```text
export_id
generation_timestamp
query_scope
event_count
hash/checksum
generated_by
retention_policy
```

---

## 83. Audit Investigation Workflow

```text
Security Alert
      |
      v
Investigator Opens Event
      |
      v
Trace Correlation
      |
      v
Actor Analysis
      |
      v
Resource Analysis
      |
      v
Related Events
      |
      v
Timeline Reconstruction
      |
      v
Evidence Export
      |
      v
Incident Record
      |
      v
Resolution
```

---

## 84. AI-Assisted Investigation Workflow

```text
Security Alert
      |
      v
Audit Evidence
      |
      v
AI Investigation Agent
      |
      +--> Timeline
      +--> Anomaly Detection
      +--> Related Actors
      +--> Related Resources
      +--> Risk Assessment
      |
      v
Human Security Analyst
      |
      v
Final Decision
```

AI conclusions MUST remain distinguishable from original audit evidence.

---

## 85. Audit Integrity Invariants

### AI-INV-001

AI agents MUST NOT modify original audit records.

### AI-INV-002

AI-generated summaries MUST reference underlying evidence.

### AI-INV-003

AI agents MUST NOT suppress audit events.

### AI-INV-004

AI agents MUST NOT disable audit logging without explicit authorization.

### AI-INV-005

AI agents MUST NOT receive unrestricted access to audit storage.

---

## 86. Human Security Invariants

### HI-001

Normal users cannot access unauthorized audit records.

### HI-002

Tenant administrators cannot access other tenants' audit data.

### HI-003

Auditors cannot modify audit records.

### HI-004

Audit administrators cannot silently erase evidence.

### HI-005

Privileged audit access is itself audited.

---

## 87. Platform Security Invariants

### SI-001

Every critical administrative operation MUST generate an audit event.

### SI-002

Every security-sensitive AI operation MUST be attributable.

### SI-003

Every important integration operation MUST be traceable.

### SI-004

Audit records MUST be protected against unauthorized modification.

### SI-005

Secrets MUST never be intentionally stored in audit logs.

### SI-006

Cross-tenant audit access MUST be denied unless explicitly authorized.

### SI-007

Audit access MUST itself be auditable.

### SI-008

Audit events MUST support distributed trace correlation.

### SI-009

Critical audit evidence MUST survive ordinary application failures.

### SI-010

Audit retention MUST follow applicable legal and contractual requirements.

---

## 88. Testing Requirements

## Unit Tests

The system MUST test:

* event creation
* event validation
* schema validation
* actor attribution
* tenant attribution
* severity classification
* redaction
* event IDs
* timestamps
* correlation IDs
* authorization

## Integration Tests

The system MUST test:

* API gateway
* authentication service
* AI gateway
* RAG service
* workflow engine
* billing service
* integration services
* database
* event bus
* immutable storage

## Security Tests

The system MUST test:

* tenant isolation
* privilege escalation
* audit tampering
* event forgery
* log injection
* secret leakage
* unauthorized export
* unauthorized deletion
* AI audit bypass

## Failure Tests

The system MUST test:

* event-bus outage
* database outage
* storage outage
* network partition
* high event volume
* duplicate events
* delayed events
* malformed events
* service crashes

---

## 89. Red-Team Requirements

Security testing MUST attempt to:

```text
Delete audit evidence
Modify historical events
Forge event identities
Inject fake events
Hide AI tool calls
Bypass tenant filters
Export another tenant's logs
Leak secrets through metadata
Suppress security events
Disable audit logging
Manipulate timestamps
Replay events
Exploit privileged audit APIs
```

All critical bypass attempts MUST fail.

---

## 90. Observability Requirements

The audit service itself MUST expose:

```text
audit_events_ingested_total
audit_events_failed_total
audit_events_dropped_total
audit_events_duplicate_total
audit_events_redacted_total
audit_queue_depth
audit_processing_latency
audit_storage_latency
audit_query_latency
audit_export_total
audit_export_failures
audit_dead_letter_count
audit_integrity_failures
audit_security_alerts
```

---

## 91. SLO Requirements

Recommended production SLOs:

| Metric                       |       Target |
| ---------------------------- | -----------: |
| Audit ingestion availability |    >= 99.99% |
| Critical event durability    |   >= 99.999% |
| Standard event durability    |    >= 99.99% |
| Audit query availability     |     >= 99.9% |
| Critical alert processing    | < 60 seconds |
| Standard event visibility    | < 10 seconds |
| Audit API p95 latency        |     < 300 ms |
| Audit API p99 latency        |   < 1 second |

Targets MUST be validated against production architecture and workload.

---

## 92. Recommended Event Taxonomy

```text
auth.*
identity.*
authorization.*
admin.*
security.*
user.*
tenant.*
ai.*
rag.*
workflow.*
integration.*
oauth.*
data.*
document.*
conversation.*
billing.*
subscription.*
payment.*
invoice.*
key.*
configuration.*
compliance.*
audit.*
system.*
```

---

## 93. Recommended Severity Mapping

```text
INFO
  Normal successful operations

NOTICE
  Important administrative operations

WARNING
  Suspicious or unusual behavior

HIGH
  Significant security or compliance event

CRITICAL
  Potential compromise, destructive security action,
  cross-tenant access attempt, or major control failure
```

---

## 94. End-to-End Audit Example

```text
Human User
    |
    | Login
    v
Auth Service
    |
    | auth.success
    v
AI Gateway
    |
    | ai.session.created
    v
AI Sales Agent
    |
    | rag.search
    v
RAG Service
    |
    | rag.document.retrieved
    v
Salesforce Integration
    |
    | integration.api.request
    v
Salesforce
    |
    | response
    v
AI Agent
    |
    | ai.action.proposed
    v
Human Approval
    |
    | approval.granted
    v
Salesforce Integration
    |
    | contact.updated
    v
Audit Service
    |
    +--> Hot Search Store
    |
    +--> Immutable Archive
    |
    +--> Security Analytics
```

---

## 95. Final Acceptance Criteria

## AC-001 — Human Activity

* Human actions are attributable.
* Tenant isolation is enforced.
* Sensitive operations are logged.
* Unauthorized audit access is denied.

## AC-002 — AI Activity

* AI actions are attributable.
* Agent identity is recorded.
* Parent user/session is recorded.
* Tool calls are auditable.
* AI cannot modify audit evidence.

## AC-003 — Security

* Authentication events are recorded.
* Authorization failures are recorded.
* Privileged actions are recorded.
* Security alerts are generated according to policy.

## AC-004 — Integration

* Integration lifecycle events are recorded.
* OAuth events are recorded.
* Synchronization activity is recorded.
* External side effects are traceable.

## AC-005 — Data Protection

* Secrets are redacted.
* Sensitive payloads are minimized.
* Logs are encrypted.
* Unauthorized users cannot retrieve protected audit data.

## AC-006 — Integrity

* Audit records cannot be silently modified.
* Audit records cannot be silently deleted.
* Tampering is detectable.
* Audit access is itself audited.

## AC-007 — Reliability

* Events survive temporary downstream failures.
* Failed events enter a durable retry/dead-letter mechanism.
* Duplicate events are handled safely.
* Critical events receive priority treatment.

## AC-008 — Investigation

* Investigators can search by actor.
* Investigators can search by resource.
* Investigators can search by trace ID.
* Investigators can reconstruct distributed timelines.
* Evidence can be securely exported.

---

## 96. FAANG-Level Non-Functional Requirements

| Category            | Requirement                                             |
| ------------------- | ------------------------------------------------------- |
| Security            | Tamper-resistant, least-privilege audit architecture    |
| Privacy             | Data minimization and automatic secret redaction        |
| Integrity           | Append-only and integrity-verifiable events             |
| Attribution         | Human, AI, service, system, and integration attribution |
| Isolation           | Strong tenant-level audit boundaries                    |
| Scalability         | Millions of events across distributed microservices     |
| Reliability         | Durable asynchronous event ingestion                    |
| Availability        | High-availability audit control plane                   |
| Performance         | Low-latency event ingestion                             |
| Observability       | Metrics, traces, health checks, and alerting            |
| Compliance          | Configurable retention and evidence export              |
| AI Governance       | Complete traceability of AI actions                     |
| Security Operations | Real-time suspicious-event detection                    |
| Disaster Recovery   | Replicated audit storage and tested recovery            |
| Extensibility       | Versioned event schema and event taxonomy               |
| Forensics           | Correlated, searchable, immutable evidence              |
| Governance          | Separation of duties and privileged audit access        |

---

## 97. SalesGenie Audit Logging Golden Path

```text
                 +-------------------+
                 | Human User        |
                 +---------+---------+
                           |
                           v
                 +-------------------+
                 | AI Agent / UI     |
                 +---------+---------+
                           |
                           v
                 +-------------------+
                 | API Gateway       |
                 +---------+---------+
                           |
                           v
                 +-------------------+
                 | Auth + Policy     |
                 +---------+---------+
                           |
                           v
                 +-------------------+
                 | Business Service  |
                 +---------+---------+
                           |
                           +--------------------+
                           |                    |
                           v                    v
                    External Action       AI Tool Call
                           |                    |
                           +---------+----------+
                                     |
                                     v
                            +----------------+
                            | Audit SDK      |
                            +-------+--------+
                                    |
                                    v
                            +----------------+
                            | Audit Ingest   |
                            +-------+--------+
                                    |
                                    v
                            +----------------+
                            | Event Bus      |
                            +-------+--------+
                                    |
                    +---------------+---------------+
                    |                               |
                    v                               v
             +-------------+                +-------------+
             | Search Store|                | Immutable   |
             |             |                | Archive     |
             +------+------+                +------+------+
                    |                              |
                    +---------------+--------------+
                                    |
                                    v
                           +------------------+
                           | Audit Query API  |
                           +--------+---------+
                                    |
                       +------------+-------------+
                       |                          |
                       v                          v
                Security Dashboard       Compliance Dashboard
```

---

## 98. Final Requirement

SalesGenie MUST treat audit logging as a **security control plane and forensic evidence system**, not as ordinary application logging.

The platform MUST provide complete, trustworthy attribution across:

```text
HUMANS
   +
AI AGENTS
   +
MICROSERVICES
   +
AUTOMATIONS
   +
INTEGRATIONS
   +
ADMINISTRATORS
   +
SECURITY OPERATIONS
```

Every consequential action MUST be traceable through:

```text
WHO
  +
WHAT
  +
WHEN
  +
WHERE
  +
WHICH TENANT
  +
WHICH RESOURCE
  +
WHICH SERVICE
  +
WHICH AI AGENT
  +
WHICH POLICY
  +
WHICH REQUEST
  +
WHICH TRACE
  +
WHAT RESULT
```

The resulting audit architecture MUST allow SalesGenie to answer, with high confidence and without exposing unnecessary sensitive data:

> **"Who or what performed this action, under whose authority, against which resource, through which service or AI agent, according to which policy, what happened afterward, and can we prove that the record itself has not been tampered with?"**

That capability is the foundation for enterprise security operations, compliance, incident response, AI governance, tenant isolation, and trustworthy operation of the SalesGenie platform.
