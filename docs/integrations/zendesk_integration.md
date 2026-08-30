# SalesGenie — Zendesk Integration Requirements

**Document:** `zendesk_integration.md`  
**Product:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Requirement Level:** FAANG-Level / Production Enterprise  
**Integration Type:** Zendesk Support, Ticketing, Customer Service, Knowledge, Events & Agent Collaboration  
**Actors:** Human Users + AI Agents + System Services  
**Primary Principle:** Every AI capability must remain permission-aware, auditable, reversible, observable, and compliant with Zendesk and tenant-level policies.

---

## 1. Scope

The Zendesk Integration enables SalesGenie tenants to connect Zendesk as an enterprise customer-support and service-management system.

The integration SHALL support:

- Zendesk account/tenant connection
- OAuth authentication
- API authentication where supported
- Ticket synchronization
- Ticket creation
- Ticket updates
- Ticket assignment
- Ticket status management
- Ticket comments
- Internal notes
- Customer/user synchronization
- Organizations synchronization
- Groups and agents synchronization
- Ticket fields
- Tags
- Custom fields
- Views
- Knowledge-base synchronization where supported
- AI-assisted ticket classification
- AI-assisted ticket summarization
- AI-assisted response generation
- AI-assisted routing
- AI-assisted prioritization
- AI-assisted sentiment detection
- AI-assisted intent detection
- AI-assisted escalation
- Human-in-the-loop approval
- Zendesk event/webhook ingestion
- Bidirectional synchronization
- Conflict resolution
- Retry and failure handling
- Rate-limit management
- Integration monitoring
- Audit logging
- Data governance
- Tenant isolation
- RBAC/ABAC enforcement
- Integration health monitoring
- Workflow automation
- MCP-based AI tool access
- Cross-channel customer context
- SalesGenie CRM/customer-profile enrichment

---

## 2. Actors

## 2.1 Human Actors

### HR-01 — Super Admin

The Super Admin manages platform-wide governance and may:

- Enable or disable Zendesk integration capabilities.
- Configure global integration policies.
- Monitor integration health.
- Review security events.
- Review audit logs.
- Configure platform-wide limits.
- Manage approved Zendesk capabilities.
- Investigate integration failures.
- Suspend compromised integrations.

The Super Admin SHALL NOT automatically gain access to tenant Zendesk customer data unless explicitly authorized by tenant governance and platform policy.

---

### HR-02 — Organization Admin

The Organization Admin manages Zendesk integration for their organization.

Capabilities include:

- Connect Zendesk.
- Disconnect Zendesk.
- Configure synchronization.
- Configure mappings.
- Configure AI automation.
- Configure ticket-routing policies.
- Configure escalation rules.
- Manage integration users.
- Configure webhooks.
- Configure synchronization frequency.
- Review integration logs.
- Test connectivity.
- Configure approval requirements.

---

### HR-03 — Sales Manager

The Sales Manager may:

- View customer support context relevant to sales.
- Search Zendesk tickets.
- Review customer history.
- Use AI-generated summaries.
- Create or update support-related workflows.
- Trigger approved actions.
- Assign tickets according to permissions.

---

### HR-04 — Support Manager

The Support Manager may:

- View Zendesk tickets.
- Assign tickets.
- Reassign tickets.
- Change priorities.
- Change statuses.
- Review AI recommendations.
- Approve AI-generated responses.
- Configure escalation policies.
- Configure SLA-aware routing.

---

### HR-05 — Support Agent

A Support Agent may:

- View authorized tickets.
- Search customer history.
- Generate AI summaries.
- Generate response suggestions.
- Add comments.
- Add internal notes.
- Update ticket status.
- Apply approved tags.
- Request AI assistance.

The agent SHALL NOT perform Zendesk actions outside their effective permissions.

---

### HR-06 — Sales Agent

A Sales Agent may:

- View permitted customer support context.
- Search customer tickets.
- Generate customer summaries.
- Identify sales opportunities from support interactions.
- Create leads or tasks based on authorized workflows.

---

### HR-07 — AI Support Agent

The AI Support Agent may:

- Read authorized ticket information.
- Classify tickets.
- Summarize conversations.
- Detect intent.
- Detect sentiment.
- Recommend priority.
- Recommend assignment.
- Generate response drafts.
- Execute approved low-risk actions.
- Escalate high-risk interactions.
- Trigger workflows.

AI agents SHALL operate under explicit authorization policies.

---

### HR-08 — AI Sales Agent

The AI Sales Agent may:

- Analyze authorized support interactions.
- Detect potential buying signals.
- Enrich customer profiles.
- Recommend follow-up actions.
- Create authorized CRM activities.
- Trigger sales workflows.

---

### HR-09 — Workflow Automation Engine

The workflow engine may:

- Receive Zendesk events.
- Evaluate conditions.
- Execute actions.
- Trigger AI agents.
- Trigger MCP tools.
- Synchronize records.
- Create tickets.
- Update tickets.
- Route tickets.
- Escalate tickets.

---

### HR-10 — Integration Service

The Integration Service manages:

- Authentication.
- Authorization.
- API communication.
- Webhooks.
- Synchronization.
- Rate limits.
- Retries.
- Error handling.
- Mapping.
- Data normalization.
- Observability.

---

## 3. User Requirements

## UR-ZD-001 — Connect Zendesk

Users SHALL be able to connect their organization's Zendesk account to SalesGenie.

### Human Flow

1. User opens Integrations.
2. User selects Zendesk.
3. User selects Connect.
4. SalesGenie initiates authentication.
5. User authorizes requested permissions.
6. Zendesk redirects to SalesGenie.
7. SalesGenie validates the authorization response.
8. Credentials are securely stored.
9. SalesGenie validates connectivity.
10. Integration becomes Active.

### AI Flow

The AI Agent MAY recommend connecting Zendesk when:

- A workflow requires Zendesk.
- Customer-support automation is configured.
- A ticket-related action is requested.
- Customer history is unavailable from current channels.

AI SHALL NOT connect an account without explicit authorization.

---

## UR-ZD-002 — Disconnect Zendesk

Authorized users SHALL be able to disconnect Zendesk.

The system SHALL:

- Revoke credentials where supported.
- Disable active webhooks.
- Stop synchronization.
- Cancel pending integration jobs.
- Preserve required audit records.
- Mark the integration as disconnected.
- Prevent further API operations.

---

## UR-ZD-003 — Test Zendesk Connection

Users SHALL be able to test:

- Authentication.
- API connectivity.
- Permissions.
- Webhook connectivity.
- Read access.
- Write access.
- Rate-limit availability.

The system SHALL provide actionable diagnostics.

---

## UR-ZD-004 — Synchronize Tickets

Users SHALL be able to synchronize Zendesk tickets with SalesGenie.

Supported synchronization modes SHALL include:

- Initial full synchronization.
- Incremental synchronization.
- Event-driven synchronization.
- Scheduled synchronization.
- Manual synchronization.

---

## UR-ZD-005 — Create Zendesk Tickets

Authorized users and AI agents SHALL be able to create Zendesk tickets.

Ticket creation SHALL support:

- Subject.
- Description.
- Requester.
- Organization.
- Assignee.
- Group.
- Priority.
- Status.
- Tags.
- Custom fields.
- Channel metadata.
- Attachments where supported.

---

## UR-ZD-006 — Update Zendesk Tickets

Authorized users and AI agents SHALL be able to update tickets.

Supported fields SHOULD include:

- Status.
- Priority.
- Assignee.
- Group.
- Tags.
- Custom fields.
- Subject.
- Description.
- Comments.
- Internal notes.

---

## UR-ZD-007 — Ticket Comments

SalesGenie SHALL distinguish between:

- Public comments.
- Internal notes.
- AI-generated drafts.
- Human-authored responses.

AI SHALL NOT publish a customer-visible response unless explicitly authorized by policy.

---

## UR-ZD-008 — AI Ticket Classification

AI SHALL classify tickets using configurable taxonomies.

Possible classifications:

- Billing.
- Technical support.
- Product inquiry.
- Sales inquiry.
- Refund.
- Complaint.
- Feature request.
- Account issue.
- Security issue.
- General inquiry.

Users SHALL be able to define custom categories.

---

## UR-ZD-009 — AI Ticket Summarization

SalesGenie SHALL generate concise ticket summaries containing:

- Customer intent.
- Problem statement.
- Relevant history.
- Previous actions.
- Current status.
- Required next action.
- Risk indicators.
- Sentiment.
- Suggested resolution.

---

## UR-ZD-010 — AI Response Generation

SalesGenie SHALL generate response suggestions using:

- Ticket history.
- Customer context.
- Zendesk metadata.
- Approved knowledge sources.
- Organization policies.
- Product documentation.
- RAG context.

Generated responses SHALL include confidence and source/context metadata where applicable.

---

## UR-ZD-011 — AI Ticket Routing

AI SHALL recommend or execute ticket routing according to policy.

Routing factors MAY include:

- Intent.
- Language.
- Customer tier.
- Priority.
- Product.
- Agent expertise.
- Workload.
- SLA.
- Sentiment.
- Business hours.

---

## UR-ZD-012 — Human Approval

Organizations SHALL be able to require human approval for:

- Public responses.
- Refund-related actions.
- Account changes.
- Sensitive customer requests.
- High-risk communications.
- Ticket closure.
- Priority escalation.
- Customer-data modifications.

---

## UR-ZD-013 — AI Escalation

AI SHALL escalate tickets when:

- Confidence is below threshold.
- Customer sentiment is highly negative.
- Security concerns are detected.
- Legal/compliance concerns are detected.
- Repeated resolution attempts fail.
- VIP customer policy applies.
- SLA breach risk is detected.
- Human intervention is required.

---

## UR-ZD-014 — Customer Context

Authorized users SHALL be able to view Zendesk context from SalesGenie's unified customer profile.

The profile MAY include:

- Zendesk user ID.
- Customer identity.
- Organization.
- Ticket history.
- Recent interactions.
- Open tickets.
- Resolved tickets.
- Ticket categories.
- Customer sentiment.
- Support history.
- AI-generated summaries.

---

## UR-ZD-015 — Cross-Channel Context

SalesGenie SHALL correlate authorized Zendesk information with:

- Gmail.
- WhatsApp.
- Instagram.
- Facebook.
- LinkedIn.
- Slack.
- CRM systems.
- SalesGenie conversations.

The system SHALL prevent unauthorized cross-tenant or cross-user data correlation.

---

## 4. System Requirements

## SR-ZD-001 — Multi-Tenant Isolation

The system SHALL enforce strict tenant isolation.

Every Zendesk object SHALL be associated with:

```text
tenant_id
organization_id
integration_id
zendesk_account_id
external_object_id
```

Cross-tenant data access SHALL be prohibited.

---

## SR-ZD-002 — Integration Architecture

The integration SHALL use a dedicated Integration Service.

Recommended architecture:

```text
Frontend
   |
API Gateway
   |
Integration Service
   |
+-------------------------+
| Zendesk Connector       |
| OAuth Manager           |
| Webhook Processor       |
| Sync Engine             |
| Mapping Engine          |
| Rate Limit Manager      |
| Retry Manager           |
| Audit Logger            |
+-------------------------+
   |
Zendesk APIs
```

---

## SR-ZD-003 — API Abstraction

Zendesk API calls SHALL NOT be directly implemented throughout business services.

All Zendesk operations SHALL pass through a connector abstraction:

```text
ZendeskConnector
```

Example capabilities:

```text
authenticate()
test_connection()
get_ticket()
list_tickets()
create_ticket()
update_ticket()
add_comment()
add_internal_note()
get_user()
list_users()
get_organization()
list_organizations()
list_groups()
list_agents()
search_tickets()
```

---

## SR-ZD-004 — OAuth Security

OAuth credentials SHALL:

* Be encrypted at rest.
* Never be logged.
* Never be returned to frontend clients.
* Support secure token refresh.
* Support revocation.
* Be scoped to the minimum required permissions.

---

## SR-ZD-005 — Secret Management

Secrets SHALL be stored in:

* KMS-backed secret storage.
* Vault.
* Cloud secret manager.
* Equivalent enterprise secret-management infrastructure.

Secrets SHALL NOT be stored in:

* Source code.
* Git repositories.
* Frontend bundles.
* Browser local storage.
* Plain-text database columns.
* Application logs.

---

## SR-ZD-006 — Rate-Limit Management

The system SHALL detect Zendesk API rate limits.

The rate-limit subsystem SHALL support:

* Request throttling.
* Retry-after handling.
* Exponential backoff.
* Jitter.
* Per-tenant quotas.
* Global quotas.
* Priority queues.

---

## SR-ZD-007 — Idempotency

Write operations SHALL support idempotency.

The system SHALL prevent duplicate:

* Tickets.
* Comments.
* Updates.
* Webhook processing.
* Synchronization jobs.

---

## SR-ZD-008 — Event Processing

Zendesk events SHALL be processed asynchronously.

Recommended pipeline:

```text
Zendesk Webhook
      |
Webhook Gateway
      |
Signature Validation
      |
Event Deduplication
      |
Event Queue
      |
Event Processor
      |
Normalization
      |
Workflow Engine
      |
AI Agent / Human
```

---

## SR-ZD-009 — Queue-Based Architecture

Long-running operations SHALL use asynchronous queues.

Candidate technologies:

* Redis Streams.
* Kafka.
* RabbitMQ.
* AWS SQS.
* Google Pub/Sub.
* Azure Service Bus.

---

## SR-ZD-010 — Data Normalization

Zendesk records SHALL be normalized into SalesGenie canonical schemas.

Example:

```json
{
  "tenant_id": "tenant-id",
  "integration_id": "integration-id",
  "source": "zendesk",
  "external_id": "ticket-id",
  "object_type": "ticket",
  "customer_id": "customer-id",
  "status": "open",
  "priority": "high",
  "tags": [],
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

---

## SR-ZD-011 — Eventual Consistency

SalesGenie SHALL support eventual consistency between:

```text
SalesGenie
    ↕
Zendesk
```

The system SHALL expose synchronization state to authorized users.

---

## SR-ZD-012 — Conflict Resolution

Conflicts SHALL be detected when both systems modify the same record.

Resolution policies SHALL support:

* Zendesk wins.
* SalesGenie wins.
* Latest update wins.
* Field-level merge.
* Human resolution.
* Custom tenant policy.

---

## SR-ZD-013 — Observability

The system SHALL expose:

* Request latency.
* API error rate.
* API throughput.
* Rate-limit usage.
* Synchronization lag.
* Failed jobs.
* Retry count.
* Webhook failures.
* Token failures.
* AI action failures.
* Ticket processing latency.

---

## SR-ZD-014 — Auditability

Every privileged action SHALL produce an audit event.

Example:

```json
{
  "event": "zendesk.ticket.updated",
  "tenant_id": "tenant-id",
  "actor_type": "ai_agent",
  "actor_id": "agent-id",
  "ticket_id": "ticket-id",
  "action": "change_status",
  "old_value": "open",
  "new_value": "pending",
  "authorization_policy": "support_auto_resolution",
  "timestamp": "timestamp"
}
```

---

## SR-ZD-015 — Availability

The integration SHALL be designed for high availability.

Target:

```text
Service Availability: >= 99.9%
```

Critical operations SHALL support:

* Retries.
* Queue persistence.
* Failover.
* Circuit breakers.
* Dead-letter queues.

---

## SR-ZD-016 — Disaster Recovery

The system SHALL support:

* Credential recovery procedures.
* Queue recovery.
* Failed synchronization recovery.
* Replayable events.
* Database backup.
* Audit-log preservation.

---

## 5. Functional Requirements

## FR-ZD-001 — Integration Registration

The system SHALL allow an authorized Organization Admin to register a Zendesk integration.

Required metadata:

```text
integration_id
tenant_id
provider
account_id
status
created_by
created_at
updated_at
```

---

## FR-ZD-002 — Integration Lifecycle

Supported states:

```text
PENDING
CONNECTING
ACTIVE
DEGRADED
AUTH_REQUIRED
RATE_LIMITED
ERROR
SUSPENDED
DISCONNECTED
```

---

## FR-ZD-003 — Connection Validation

The system SHALL validate:

1. Credentials.
2. Zendesk account.
3. Required scopes.
4. API connectivity.
5. Read permissions.
6. Write permissions.
7. Webhook capability.

---

## FR-ZD-004 — Ticket Search

Users SHALL be able to search authorized Zendesk tickets by:

* Ticket ID.
* Customer.
* Email.
* Organization.
* Subject.
* Status.
* Priority.
* Assignee.
* Group.
* Tags.
* Custom fields.
* Date range.

---

## FR-ZD-005 — Ticket Retrieval

The system SHALL retrieve:

* Ticket metadata.
* Requester.
* Assignee.
* Organization.
* Comments.
* Attachments metadata.
* Tags.
* Custom fields.
* Status history where available.

---

## FR-ZD-006 — Ticket Creation

The system SHALL support:

```text
Create Ticket
Assign Ticket
Set Priority
Set Status
Add Tags
Set Custom Fields
Add Public Comment
Add Internal Note
```

---

## FR-ZD-007 — Ticket Update

The system SHALL validate permissions before every update.

Authorization SHALL be evaluated at:

```text
tenant
organization
user
role
resource
action
field
```

---

## FR-ZD-008 — Bulk Operations

Authorized users SHALL be able to perform bulk operations where supported.

Examples:

```text
Bulk Assign
Bulk Tag
Bulk Update Status
Bulk Change Priority
Bulk Escalate
```

Bulk AI actions SHALL support approval policies.

---

## FR-ZD-009 — AI Classification Pipeline

For each eligible ticket:

```text
Ticket
 ↓
Preprocessing
 ↓
PII/Sensitive Data Detection
 ↓
Context Retrieval
 ↓
LLM Classification
 ↓
Confidence Evaluation
 ↓
Policy Evaluation
 ↓
Human Approval OR Action
 ↓
Audit
```

---

## FR-ZD-010 — AI Confidence Thresholds

Organizations SHALL configure confidence thresholds.

Example:

```text
>= 0.95 → Auto-action
0.80–0.94 → Human review
< 0.80 → Escalate
```

Thresholds SHALL be configurable by workflow and action.

---

## FR-ZD-011 — AI Ticket Summarization

The system SHALL generate summaries without modifying Zendesk unless explicitly requested.

Summaries SHALL be stored separately from source data where appropriate.

---

## FR-ZD-012 — AI Response Drafting

AI SHALL generate:

* Suggested response.
* Tone.
* Intent.
* Confidence.
* Supporting context.
* Suggested next action.

---

## FR-ZD-013 — AI Auto-Response

Auto-response SHALL require explicit tenant policy.

Policy SHALL specify:

```text
allowed_channels
allowed_ticket_types
confidence_threshold
business_hours
excluded_topics
maximum_actions
approval_required
```

---

## FR-ZD-014 — AI Ticket Routing

The routing engine SHALL evaluate:

```text
intent
priority
customer_tier
language
product
agent_skill
agent_availability
workload
SLA
sentiment
```

---

## FR-ZD-015 — SLA-Aware Processing

The system SHALL identify tickets approaching SLA thresholds.

Possible states:

```text
NORMAL
AT_RISK
BREACHED
```

The workflow engine MAY escalate AT_RISK tickets.

---

## FR-ZD-016 — Sentiment Analysis

AI SHALL optionally classify:

```text
positive
neutral
negative
highly_negative
```

Sentiment SHALL be used only where authorized by tenant policy.

---

## FR-ZD-017 — Intent Detection

AI SHALL identify customer intent and map it to configured workflow actions.

Example:

```text
"Refund my subscription"
        ↓
Intent: Refund Request
        ↓
Risk Check
        ↓
Policy Evaluation
        ↓
Human Approval
        ↓
Zendesk Update
```

---

## FR-ZD-018 — Knowledge Integration

Zendesk knowledge content SHALL be eligible for RAG ingestion where technically and contractually supported.

The ingestion pipeline SHALL support:

```text
Fetch
 ↓
Normalize
 ↓
Chunk
 ↓
Embed
 ↓
Index
 ↓
Metadata
 ↓
Tenant Isolation
```

---

## FR-ZD-019 — Knowledge Freshness

The system SHALL track:

```text
source_updated_at
indexed_at
embedding_version
content_hash
sync_status
```

Changed documents SHALL be re-indexed.

Deleted documents SHALL be removed or invalidated from retrieval.

---

## FR-ZD-020 — Webhook Processing

The system SHALL support Zendesk webhook/event ingestion where available.

Webhook processing SHALL include:

1. Authentication.
2. Signature validation.
3. Payload validation.
4. Tenant identification.
5. Event deduplication.
6. Event persistence.
7. Queue publishing.
8. Workflow execution.

---

## FR-ZD-021 — Webhook Replay Protection

The system SHALL prevent duplicate event execution using:

```text
event_id
provider_event_id
timestamp
payload_hash
integration_id
```

---

## FR-ZD-022 — Synchronization

The Sync Engine SHALL support:

```text
Initial Sync
Incremental Sync
Scheduled Sync
Event-Driven Sync
Manual Sync
```

---

## FR-ZD-023 — Sync Cursor

Incremental synchronization SHALL maintain durable cursors.

Example:

```text
last_cursor
last_successful_sync
last_attempted_sync
records_processed
records_failed
```

---

## FR-ZD-024 — Sync Recovery

If synchronization fails, the system SHALL resume from the last safe checkpoint.

The system SHALL avoid restarting a full synchronization unnecessarily.

---

## FR-ZD-025 — Mapping Engine

Users SHALL map Zendesk fields to SalesGenie fields.

Example:

```text
Zendesk priority → SalesGenie priority
Zendesk organization → SalesGenie account
Zendesk requester → SalesGenie customer
Zendesk tags → SalesGenie tags
Zendesk custom_field_123 → SalesGenie customer_segment
```

---

## FR-ZD-026 — Custom Field Mapping

The mapping system SHALL support:

* Text.
* Number.
* Boolean.
* Date.
* Enum.
* Multi-select.
* Reference fields.

---

## FR-ZD-027 — Data Transformation

Mappings SHALL support transformations such as:

```text
String normalization
Date conversion
Enum mapping
Boolean conversion
Default values
Conditional mapping
Regex extraction
Field concatenation
```

---

## FR-ZD-028 — Integration Health

The dashboard SHALL display:

```text
Connection Status
Authentication Status
Last Successful Sync
Sync Lag
API Errors
Rate Limits
Webhook Health
Failed Jobs
Retry Queue
```

---

## FR-ZD-029 — Error Handling

Errors SHALL be categorized:

```text
AUTHENTICATION_ERROR
AUTHORIZATION_ERROR
RATE_LIMIT_ERROR
VALIDATION_ERROR
NOT_FOUND
CONFLICT
NETWORK_ERROR
TIMEOUT
PROVIDER_ERROR
INTERNAL_ERROR
```

---

## FR-ZD-030 — Retry Policy

Retryable failures SHALL use exponential backoff.

Example:

```text
Attempt 1 → 1s
Attempt 2 → 2s
Attempt 3 → 4s
Attempt 4 → 8s
Attempt 5 → 16s
```

Random jitter SHALL be applied.

Non-retryable errors SHALL NOT be retried indefinitely.

---

## FR-ZD-031 — Dead Letter Queue

Failed events and jobs SHALL be moved to a DLQ after configured retry limits.

Authorized users SHALL be able to:

* Inspect.
* Retry.
* Replay.
* Discard.
* Export diagnostic information.

---

## FR-ZD-032 — Circuit Breaker

The Zendesk connector SHALL implement circuit breaking.

States:

```text
CLOSED
OPEN
HALF_OPEN
```

The circuit SHALL open when provider failures exceed configured thresholds.

---

## FR-ZD-033 — AI Tool Authorization

Every AI-initiated Zendesk action SHALL pass through an authorization layer.

Example:

```text
AI Agent
   ↓
Tool Request
   ↓
Policy Engine
   ↓
RBAC/ABAC
   ↓
Risk Engine
   ↓
Approval Check
   ↓
Zendesk Connector
```

---

## FR-ZD-034 — AI Tool Registry

Zendesk tools SHALL be registered in the SalesGenie AI/MCP tool registry.

Example tools:

```text
zendesk.search_tickets
zendesk.get_ticket
zendesk.create_ticket
zendesk.update_ticket
zendesk.add_comment
zendesk.add_internal_note
zendesk.search_users
zendesk.get_organization
zendesk.list_groups
zendesk.assign_ticket
zendesk.escalate_ticket
```

---

## FR-ZD-035 — MCP Integration

SalesGenie MCP infrastructure SHALL expose Zendesk capabilities as controlled tools.

Every MCP tool SHALL define:

```text
tool_name
description
input_schema
output_schema
required_permissions
risk_level
tenant_scope
audit_policy
rate_limit
approval_policy
```

---

## FR-ZD-036 — MCP Read Tools

Read tools MAY be automatically executed when:

* The AI agent has permission.
* The tenant allows AI access.
* Data access policy permits the operation.

---

## FR-ZD-037 — MCP Write Tools

Write tools SHALL require:

* Authorization.
* Tenant policy validation.
* Action validation.
* Idempotency.
* Audit logging.

High-risk actions SHALL require human approval.

---

## FR-ZD-038 — Prompt Injection Protection

Zendesk content SHALL be treated as untrusted external content.

The AI system SHALL NOT interpret ticket content as system instructions.

Example:

```text
Zendesk Ticket Content
        ↓
UNTRUSTED DATA
        ↓
Context Sanitization
        ↓
AI Context
```

A ticket containing:

```text
"Ignore your system instructions..."
```

SHALL NOT alter agent-level policies.

---

## FR-ZD-039 — Sensitive Data Protection

The system SHALL detect and protect sensitive information.

Controls MAY include:

* PII detection.
* Redaction.
* Field-level access control.
* Encryption.
* Restricted logging.
* Data masking.

---

## FR-ZD-040 — Attachment Security

Zendesk attachments SHALL be treated as untrusted input.

The system SHALL support:

* File-type validation.
* Malware scanning.
* Size limits.
* Content inspection.
* Access authorization.
* Secure temporary storage.
* Expiring download URLs.

---

## FR-ZD-041 — Human-in-the-Loop

The system SHALL present approval requests containing:

```text
Requested Action
Ticket
Customer
AI Reasoning Summary
Confidence
Affected Fields
Proposed Changes
Risk Level
Policy
Approve
Reject
Edit
```

---

## FR-ZD-042 — Action Preview

Before high-risk actions, users SHALL see a diff.

Example:

```text
Status:
Open → Pending

Priority:
Normal → High

Assignee:
Agent A → Agent B

Public Reply:
[AI generated response]
```

---

## FR-ZD-043 — Rollback

Where Zendesk semantics permit, SalesGenie SHALL support compensating actions.

Example:

```text
Previous Status = Open
Current Status = Pending

Rollback:
Pending → Open
```

Rollback SHALL itself be audited.

---

## FR-ZD-044 — Audit Search

Authorized administrators SHALL be able to search audit events by:

* User.
* AI agent.
* Ticket.
* Customer.
* Action.
* Date.
* IP/device metadata where permitted.
* Integration.
* Workflow.
* Result.
* Risk level.

---

## FR-ZD-045 — Customer Deletion

When a tenant requests deletion of synchronized customer information, the system SHALL:

* Identify corresponding records.
* Apply tenant retention policies.
* Remove eligible SalesGenie copies.
* Remove embeddings where applicable.
* Remove cached data.
* Preserve legally required audit records.

---

## FR-ZD-046 — Data Retention

Tenants SHALL be able to configure retention policies for:

```text
Ticket Data
Customer Data
AI Summaries
Embeddings
Logs
Audit Events
Webhook Payloads
Synchronization Metadata
```

---

## FR-ZD-047 — Tenant-Level AI Controls

Organization Admins SHALL configure:

```text
AI Enabled
Auto Classification
Auto Assignment
Auto Tagging
Auto Response
Auto Escalation
Auto Closure
Human Approval
Knowledge Retrieval
Customer Data Access
```

---

## FR-ZD-048 — Business Hours

Workflows SHALL support business-hour policies.

Example:

```text
Business Hours:
09:00–18:00

Outside Business Hours:
Escalate urgent tickets
Queue normal tickets
Disable autonomous public responses
```

---

## FR-ZD-049 — Multi-Language Support

AI processing SHALL support multilingual Zendesk tickets where configured.

The system SHALL preserve:

* Original language.
* Original ticket content.
* Detected language.
* Translated content if generated.

---

## FR-ZD-050 — Translation

SalesGenie MAY translate tickets for authorized agents.

Translation SHALL NOT overwrite the original Zendesk content unless explicitly requested.

---

## FR-ZD-051 — Sales Opportunity Detection

AI SHALL optionally detect sales opportunities from support tickets.

Signals MAY include:

```text
Product inquiry
Upgrade request
Feature interest
Pricing question
Expansion signal
Repeated usage issue
Enterprise requirement
```

AI-generated opportunities SHALL be treated as recommendations unless automation is explicitly enabled.

---

## FR-ZD-052 — CRM Synchronization

Zendesk customer and support context MAY be synchronized with:

* SalesGenie CRM.
* HubSpot.
* Salesforce.
* Other authorized CRM integrations.

The system SHALL maintain source attribution.

---

## FR-ZD-053 — Workflow Triggers

Zendesk events SHALL be available as workflow triggers.

Examples:

```text
Ticket Created
Ticket Updated
Ticket Assigned
Ticket Reopened
Ticket Solved
Ticket Closed
Priority Changed
Customer Updated
Organization Updated
Tag Added
SLA At Risk
Negative Sentiment Detected
```

---

## FR-ZD-054 — Workflow Conditions

Workflows SHALL support conditions such as:

```text
IF ticket.priority == "urgent"
IF ticket.sentiment == "highly_negative"
IF customer.tier == "enterprise"
IF ticket.intent == "refund"
IF SLA < threshold
IF AI.confidence >= threshold
IF business_hours == false
```

---

## FR-ZD-055 — Workflow Actions

Supported workflow actions SHALL include:

```text
Create Ticket
Update Ticket
Assign Ticket
Add Tag
Remove Tag
Add Comment
Add Internal Note
Escalate Ticket
Trigger AI Agent
Request Human Approval
Send Notification
Create CRM Task
Update Customer Profile
Start Workflow
Stop Workflow
```

---

## FR-ZD-056 — Scheduler Integration

Scheduled Zendesk workflows SHALL support:

```text
Hourly
Daily
Weekly
Custom Cron
Business Hours
SLA-Based Scheduling
Delayed Execution
```

---

## FR-ZD-057 — Rate-Aware Workflow Execution

Workflow execution SHALL respect:

```text
Zendesk API limits
Tenant quotas
Global platform quotas
Workflow priority
Retry policy
```

---

## FR-ZD-058 — Pagination

All Zendesk collection operations SHALL correctly support pagination.

The connector SHALL prevent:

* Missing records.
* Duplicate records.
* Infinite pagination loops.

---

## FR-ZD-059 — Caching

The system MAY cache low-volatility Zendesk metadata such as:

* Groups.
* Ticket fields.
* Users.
* Organizations.
* Configuration.

Cache entries SHALL have TTL and tenant isolation.

---

## FR-ZD-060 — Search Optimization

SalesGenie SHALL avoid unnecessary Zendesk API calls by using:

* Local indexes.
* Search indexes.
* Cached metadata.
* Incremental synchronization.
* Query batching where supported.

---

## 6. AI-Specific Requirements

## AI-ZD-001 — AI Permission Boundary

AI SHALL never possess implicit administrative privileges.

The effective permission set SHALL be:

```text
AI Permissions
∩
Tenant Policy
∩
User Permissions
∩
Resource Permissions
∩
Action Policy
```

---

## AI-ZD-002 — AI Action Risk Classification

Actions SHALL be classified:

### LOW

```text
Read Ticket
Summarize Ticket
Classify Ticket
Analyze Sentiment
Recommend Tags
```

### MEDIUM

```text
Add Internal Note
Add Tag
Assign Ticket
Change Priority
```

### HIGH

```text
Public Customer Reply
Close Ticket
Refund
Account Modification
Delete Data
Security Action
```

High-risk actions SHALL normally require human approval.

---

## AI-ZD-003 — AI Explainability

For consequential actions, AI SHALL provide:

```text
Decision
Confidence
Evidence
Policy
Recommended Action
Risk
```

---

## AI-ZD-004 — AI Hallucination Protection

AI-generated responses SHALL use approved context.

The system SHALL support:

* RAG grounding.
* Citation/source tracking.
* Confidence thresholds.
* Unsupported-claim detection.
* Human approval.

---

## AI-ZD-005 — AI Feedback

Agents SHALL be able to provide:

```text
Accept
Reject
Edit
Regenerate
Incorrect Classification
Incorrect Summary
Incorrect Routing
```

Feedback SHOULD be stored for model evaluation.

---

## AI-ZD-006 — AI Evaluation

The platform SHALL measure:

```text
Classification Accuracy
Routing Accuracy
Summary Quality
Response Acceptance Rate
Human Edit Rate
Escalation Rate
Hallucination Rate
False Positive Rate
False Negative Rate
```

---

## 7. Human-Based Requirements

## HUMAN-ZD-001

Humans SHALL retain ultimate control over high-impact customer-service actions.

## HUMAN-ZD-002

Humans SHALL be able to override AI recommendations.

## HUMAN-ZD-003

Humans SHALL be able to edit AI-generated responses before publication.

## HUMAN-ZD-004

Humans SHALL be able to disable autonomous Zendesk workflows.

## HUMAN-ZD-005

Humans SHALL be able to inspect the source context used by AI.

## HUMAN-ZD-006

Humans SHALL be able to retry failed integration operations.

## HUMAN-ZD-007

Humans SHALL be able to manually resolve synchronization conflicts.

## HUMAN-ZD-008

Humans SHALL be able to revoke Zendesk integration access.

## HUMAN-ZD-009

Humans SHALL be able to inspect complete integration audit trails.

---

## 8. Security Requirements

## SEC-ZD-001

All communication SHALL use TLS.

## SEC-ZD-002

OAuth tokens SHALL be encrypted at rest.

## SEC-ZD-003

Tokens SHALL never be exposed to browser JavaScript unless technically unavoidable and explicitly secured.

## SEC-ZD-004

Tokens SHALL never appear in logs.

## SEC-ZD-005

Webhook authenticity SHALL be validated.

## SEC-ZD-006

Tenant authorization SHALL be evaluated for every Zendesk operation.

## SEC-ZD-007

AI tool calls SHALL pass through policy enforcement.

## SEC-ZD-008

Zendesk content SHALL be treated as untrusted external data.

## SEC-ZD-009

Attachments SHALL be scanned before AI processing.

## SEC-ZD-010

Sensitive data SHALL be excluded from telemetry where possible.

## SEC-ZD-011

Administrative actions SHALL require strong authentication.

## SEC-ZD-012

Integration credentials SHALL support revocation.

## SEC-ZD-013

Audit logs SHALL be tamper-resistant.

## SEC-ZD-014

The system SHALL implement least-privilege access.

---

## 9. Performance Requirements

## PERF-ZD-001

Normal read operations SHOULD target:

```text
p50 < 500 ms
p95 < 2 s
p99 < 5 s
```

excluding external-provider latency.

## PERF-ZD-002

Webhook ingestion SHOULD acknowledge valid events rapidly and process business logic asynchronously.

## PERF-ZD-003

Synchronization SHALL scale horizontally.

## PERF-ZD-004

AI processing SHALL use asynchronous execution for long-running workloads.

## PERF-ZD-005

Large ticket histories SHALL use pagination and incremental retrieval.

---

## 10. Reliability Requirements

## REL-ZD-001

Transient Zendesk failures SHALL automatically retry.

## REL-ZD-002

Persistent failures SHALL enter the DLQ.

## REL-ZD-003

Duplicate events SHALL be safely ignored.

## REL-ZD-004

Integration failures SHALL NOT corrupt canonical SalesGenie records.

## REL-ZD-005

Synchronization SHALL be restartable.

## REL-ZD-006

Provider outages SHALL trigger circuit-breaker behavior.

## REL-ZD-007

Users SHALL receive clear degradation status.

---

## 11. Monitoring Requirements

The dashboard SHALL expose:

```text
Integration Status
API Request Count
API Error Count
Rate-Limit Usage
Webhook Events
Webhook Failures
Sync Progress
Sync Lag
Failed Jobs
Retry Count
DLQ Count
AI Actions
Human Approvals
AI Rejections
Average Ticket Processing Time
```

---

## 12. SLO / SLA Requirements

Recommended targets:

```text
Integration Availability       >= 99.9%
Webhook Processing Success     >= 99.95%
Successful Sync Rate           >= 99.9%
Duplicate Event Rate           < 0.01%
Unauthorized Action Rate       = 0
Credential Leakage             = 0
Cross-Tenant Data Leakage      = 0
Critical Security Incidents    = 0
```

---

## 13. Data Model Requirements

Recommended entities:

```text
ZendeskIntegration
ZendeskCredential
ZendeskWebhook
ZendeskTicket
ZendeskTicketComment
ZendeskUser
ZendeskOrganization
ZendeskGroup
ZendeskAgent
ZendeskTicketField
ZendeskMapping
ZendeskSyncJob
ZendeskSyncCursor
ZendeskEvent
ZendeskRateLimit
ZendeskError
ZendeskAuditEvent
ZendeskAITask
ZendeskApproval
```

---

## 14. Recommended ZendeskIntegration Schema

```json
{
  "id": "uuid",
  "tenant_id": "uuid",
  "organization_id": "uuid",
  "provider": "zendesk",
  "account_id": "string",
  "subdomain": "string",
  "status": "active",
  "auth_type": "oauth",
  "scopes": [],
  "last_sync_at": "timestamp",
  "last_successful_sync_at": "timestamp",
  "sync_cursor": "string",
  "webhook_enabled": true,
  "ai_enabled": true,
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

---

## 15. Recommended ZendeskTicket Schema

```json
{
  "id": "uuid",
  "tenant_id": "uuid",
  "integration_id": "uuid",
  "external_id": "string",
  "requester_id": "string",
  "organization_id": "string",
  "assignee_id": "string",
  "group_id": "string",
  "subject": "string",
  "status": "open",
  "priority": "high",
  "tags": [],
  "custom_fields": {},
  "ai_intent": "string",
  "ai_sentiment": "negative",
  "ai_confidence": 0.94,
  "last_synced_at": "timestamp",
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

---

## 16. API Requirements

SalesGenie SHALL expose internal APIs similar to:

```text
GET    /api/v1/integrations/zendesk
POST   /api/v1/integrations/zendesk/connect
POST   /api/v1/integrations/zendesk/test
POST   /api/v1/integrations/zendesk/disconnect

GET    /api/v1/integrations/zendesk/tickets
GET    /api/v1/integrations/zendesk/tickets/{id}
POST   /api/v1/integrations/zendesk/tickets
PATCH  /api/v1/integrations/zendesk/tickets/{id}

POST   /api/v1/integrations/zendesk/tickets/{id}/comments
POST   /api/v1/integrations/zendesk/tickets/{id}/internal-notes
POST   /api/v1/integrations/zendesk/tickets/{id}/assign
POST   /api/v1/integrations/zendesk/tickets/{id}/escalate

POST   /api/v1/integrations/zendesk/sync
GET    /api/v1/integrations/zendesk/sync/status

GET    /api/v1/integrations/zendesk/health
GET    /api/v1/integrations/zendesk/logs
GET    /api/v1/integrations/zendesk/audit

POST   /api/v1/integrations/zendesk/webhooks
```

---

## 17. Workflow Examples

## Workflow A — AI Ticket Triage

```text
Trigger:
Zendesk Ticket Created

        ↓

Retrieve Ticket

        ↓

AI Intent Detection

        ↓

AI Sentiment Detection

        ↓

AI Priority Recommendation

        ↓

Check SLA

        ↓

Policy Evaluation

        ↓

IF confidence >= threshold
        |
        +── Assign Ticket
        +── Add Tags
        +── Update Priority

ELSE
        |
        +── Human Review

        ↓

Audit Event
```

---

## Workflow B — AI Customer Response

```text
Trigger:
New Zendesk Ticket

        ↓

Retrieve Conversation

        ↓

Retrieve Customer Profile

        ↓

Retrieve Knowledge Base

        ↓

RAG

        ↓

Generate Response

        ↓

Safety Validation

        ↓

Confidence Check

        ↓

Human Approval?

YES → Human Review → Publish
NO  → Policy-Based Auto Response

        ↓

Audit
```

---

## Workflow C — Negative Sentiment Escalation

```text
Ticket Updated
      ↓
Sentiment Analysis
      ↓
Highly Negative?
      ↓
YES
      ↓
Check Customer Tier
      ↓
Enterprise Customer?
      ↓
YES
      ↓
Escalate
      ↓
Assign Senior Agent
      ↓
Notify Support Manager
      ↓
Create Audit Event
```

---

## Workflow D — Sales Opportunity Detection

```text
Zendesk Ticket
      ↓
AI Analysis
      ↓
Detect Buying Signal
      ↓
Confidence Check
      ↓
Policy Check
      ↓
Create Sales Opportunity
      ↓
Update CRM
      ↓
Notify Sales Agent
      ↓
Audit
```

---

## 18. AI + Human Decision Matrix

| Action                  | AI Read | AI Recommend |   AI Execute | Human Approval |
| ----------------------- | ------: | -----------: | -----------: | -------------: |
| Read Ticket             |     Yes |          Yes |          Yes |             No |
| Summarize Ticket        |     Yes |          Yes |          Yes |             No |
| Classify Ticket         |     Yes |          Yes |          Yes |       Optional |
| Sentiment Analysis      |     Yes |          Yes |          Yes |             No |
| Recommend Tags          |     Yes |          Yes |     Optional |       Optional |
| Add Internal Note       |     Yes |          Yes |     Optional |   Configurable |
| Assign Ticket           |     Yes |          Yes |     Optional |   Configurable |
| Change Priority         |     Yes |          Yes |     Optional |   Configurable |
| Public Response         |     Yes |          Yes | Configurable |        Usually |
| Close Ticket            |     Yes |          Yes |   Restricted |            Yes |
| Delete Data             |      No |           No |           No |       Required |
| Security Action         |     Yes |          Yes |   Restricted |       Required |
| Customer Account Change |     Yes |          Yes |   Restricted |       Required |
| Refund                  |     Yes |          Yes |   Restricted |       Required |

---

## 19. RBAC Requirements

Recommended roles:

```text
SUPER_ADMIN
ORGANIZATION_ADMIN
SUPPORT_MANAGER
SUPPORT_AGENT
SALES_MANAGER
SALES_AGENT
AI_SUPPORT_AGENT
AI_SALES_AGENT
AUDITOR
READ_ONLY
```

Example permission model:

```text
zendesk.ticket.read
zendesk.ticket.create
zendesk.ticket.update
zendesk.ticket.assign
zendesk.ticket.comment
zendesk.ticket.internal_note
zendesk.ticket.close
zendesk.customer.read
zendesk.customer.update
zendesk.integration.manage
zendesk.webhook.manage
zendesk.sync.manage
zendesk.ai.execute
zendesk.ai.approve
zendesk.audit.read
```

---

## 20. Acceptance Criteria

## AC-ZD-001

A properly authorized user can connect Zendesk successfully.

## AC-ZD-002

Unauthorized users cannot access Zendesk credentials.

## AC-ZD-003

Unauthorized AI agents cannot execute Zendesk write operations.

## AC-ZD-004

Zendesk ticket creation creates exactly one corresponding ticket.

## AC-ZD-005

Repeated webhook delivery does not duplicate business actions.

## AC-ZD-006

Rate limits trigger controlled backoff rather than uncontrolled failures.

## AC-ZD-007

Synchronization resumes after temporary failure.

## AC-ZD-008

AI-generated public responses respect approval policies.

## AC-ZD-009

Ticket content cannot override system or agent instructions.

## AC-ZD-010

Every privileged AI action generates an audit event.

## AC-ZD-011

Cross-tenant Zendesk data access is impossible through APIs, workflows, AI agents, MCP tools, or background workers.

## AC-ZD-012

Disconnected integrations cannot execute new Zendesk operations.

## AC-ZD-013

Failed jobs are observable and recoverable.

## AC-ZD-014

Human users can override AI recommendations.

## AC-ZD-015

Zendesk synchronization exposes current health and synchronization state.

---

## 21. Non-Functional Requirements

## NFR-ZD-001 — Scalability

The integration SHALL support horizontal scaling for:

* API workers.
* Webhook workers.
* Sync workers.
* AI workers.
* Queue consumers.

---

## NFR-ZD-002 — Security

The integration SHALL follow:

```text
Zero Trust
Least Privilege
Defense in Depth
Secure by Default
Fail Closed
Tenant Isolation
```

---

## NFR-ZD-003 — Reliability

No single Zendesk API failure SHALL bring down the SalesGenie platform.

---

## NFR-ZD-004 — Maintainability

Zendesk-specific logic SHALL remain isolated from generic workflow and AI orchestration logic.

---

## NFR-ZD-005 — Extensibility

The connector architecture SHALL permit future support for:

```text
Zendesk API versions
Additional Zendesk capabilities
Additional support platforms
Custom enterprise connectors
MCP tools
Workflow nodes
```

---

## 22. Definition of Done

The Zendesk Integration SHALL be considered production-ready only when:

* OAuth authentication is implemented.
* Credential encryption is implemented.
* RBAC/ABAC is enforced.
* Tenant isolation is tested.
* Ticket CRUD is implemented where supported.
* Ticket comments and internal notes are supported.
* User and organization synchronization works.
* Incremental synchronization works.
* Webhook ingestion works.
* Webhook deduplication works.
* Rate-limit handling works.
* Retry policies work.
* DLQ is implemented.
* Circuit breakers are implemented.
* AI classification works.
* AI summarization works.
* AI response generation works.
* Human approval works.
* AI action authorization works.
* MCP tool authorization works.
* Prompt-injection defenses are implemented.
* Sensitive-data controls are implemented.
* Audit logging works.
* Integration monitoring works.
* Integration health dashboard works.
* Synchronization recovery works.
* Conflict resolution works.
* Automated tests cover critical paths.
* Security tests pass.
* Load tests pass.
* Failure-injection tests pass.
* Cross-tenant isolation tests pass.
* AI safety evaluations pass.
* Documentation is complete.
* Production observability is enabled.

---

## 23. FAANG-Level Engineering Principles

The Zendesk Integration SHALL follow these principles:

1. **API-first architecture**
2. **Contract-driven development**
3. **Zero-trust authorization**
4. **Strict tenant isolation**
5. **Least-privilege access**
6. **Idempotent writes**
7. **Event-driven architecture**
8. **Asynchronous processing**
9. **Durable queues**
10. **Replayable events**
11. **Circuit breakers**
12. **Exponential backoff**
13. **Dead-letter queues**
14. **Strong observability**
15. **Immutable audit trails**
16. **Human-in-the-loop controls**
17. **AI risk-based authorization**
18. **Prompt-injection resistance**
19. **Data minimization**
20. **Defense in depth**
21. **Graceful degradation**
22. **Backward-compatible API contracts**
23. **Automated security testing**
24. **Automated integration testing**
25. **Continuous AI evaluation**
26. **Policy-driven autonomy**
27. **Explicit failure semantics**
28. **Operational transparency**
29. **Reversible automation where possible**
30. **No implicit AI authority**

---

## 24. Final Architecture

```text
                         SALESGenie
                             |
                      API Gateway / BFF
                             |
              +--------------+--------------+
              |                             |
       Integration Service             AI Platform
              |                             |
       +------+-------+             +-------+-------+
       |              |             |               |
 OAuth Manager   Zendesk Connector  Agent Runtime   RAG
       |              |             |               |
       |        +-----+-----+       |          Knowledge
       |        |           |       |
       |     REST API    Webhooks    |
       |        |           |        |
       +--------+-----------+--------+
                |
             Zendesk
                |
       +--------+---------+
       |        |         |
     Tickets Users   Organizations
       |
       v
 Event Bus / Queue
       |
       +-----------------------------+
       |                             |
 Workflow Engine                Sync Engine
       |                             |
       +-------------+---------------+
                     |
              Policy Engine
                     |
          +----------+----------+
          |                     |
      AI Action             Human Approval
          |                     |
          +----------+----------+
                     |
               Audit Service
                     |
             Monitoring / SIEM
```

## 25. Requirement Traceability

```text
User Requirements
       ↓
System Requirements
       ↓
Functional Requirements
       ↓
Security Requirements
       ↓
AI/MCP Authorization
       ↓
Workflow Automation
       ↓
Observability
       ↓
Auditability
       ↓
Acceptance Criteria
       ↓
Production Readiness
```

**Core principle:**

> SalesGenie SHALL treat Zendesk as an external enterprise system and untrusted data source while providing controlled, policy-governed, auditable AI and human automation over authorized Zendesk resources.
