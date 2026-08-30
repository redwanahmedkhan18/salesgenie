# SalesGenie — MCP Workflow Requirements Specification

> **Document:** `mcp_workflows.md`  
> **System:** SalesGenie Enterprise AI Customer Support & Sales Agent Platform  
> **Scope:** MCP-powered AI and human workflows  
> **Requirement Level:** FAANG-grade / Production / Enterprise  
> **Actors:** Super Admin, Organization Admin, Manager, Sales Agent, Support Agent, Human Approver, AI Agent, MCP Orchestrator, Workflow Engine, External MCP Server, External Integration

---

## 1. Purpose

SalesGenie SHALL provide a secure, multi-tenant, observable, policy-controlled MCP workflow platform that allows AI agents and human users to discover, authorize, execute, monitor, compose, and govern MCP tools and resources.

MCP workflows SHALL support:

- AI-driven tool execution
- Human-driven tool execution
- AI-to-human handoff
- Human approval of AI actions
- Human-to-AI delegation
- Multi-step MCP workflows
- MCP tool chaining
- MCP resource retrieval
- MCP prompt usage
- Conditional MCP execution
- Scheduled MCP execution
- Event-triggered MCP execution
- External SaaS integrations
- CRM operations
- Lead intelligence
- Customer support
- Sales automation
- RAG operations
- Data enrichment
- Reporting
- Administrative operations
- Enterprise governance
- Auditability
- Tenant isolation
- Cost and execution limits
- Failure recovery
- MCP server health management

---

## 2. Core Design Principles

SalesGenie MCP workflows SHALL follow these principles:

1. **Zero Trust**
2. **Least Privilege**
3. **Explicit Authorization**
4. **Tenant Isolation**
5. **Human Control for High-Risk Actions**
6. **Deterministic Execution Boundaries**
7. **Idempotent Operations**
8. **Schema-Validated Tool Calls**
9. **Observable Execution**
10. **Auditable Decisions**
11. **Fail-Safe Behavior**
12. **Provider Independence**
13. **Backward Compatibility**
14. **Cost-Aware Execution**
15. **AI-Human Collaboration**
16. **No Silent Side Effects**
17. **Policy Before Execution**
18. **Data Minimization**
19. **Reproducibility**
20. **Production-Grade Reliability**

---

## 3. Actors

## 3.1 Super Admin

The Super Admin SHALL be able to:

- Manage global MCP infrastructure.
- Register MCP servers.
- Disable MCP servers.
- Inspect MCP server health.
- Manage platform-level MCP policies.
- Configure global execution limits.
- Configure global security policies.
- Inspect MCP audit logs.
- Inspect MCP failures.
- Inspect MCP usage and costs.
- Manage trusted MCP providers.
- Configure platform-wide approval requirements.
- Define prohibited tools.
- Define prohibited MCP servers.
- Configure global rate limits.
- Inspect tenant MCP consumption.
- Investigate security incidents.
- Perform emergency MCP shutdown.
- Replay or terminate authorized executions.

---

## 3.2 Organization Admin

The Organization Admin SHALL be able to:

- Enable approved MCP servers for the organization.
- Configure organization MCP policies.
- Assign MCP permissions to roles.
- Configure workflow-level MCP permissions.
- Configure agent-level MCP permissions.
- Configure user-level MCP permissions.
- Require human approval for selected tools.
- Configure execution budgets.
- Configure rate limits.
- Inspect organization MCP activity.
- Review MCP audit logs.
- Disable MCP access for users.
- Disable MCP access for AI agents.
- Configure integration credentials.
- Configure data-access boundaries.

---

## 3.3 Manager

Managers SHALL be able to:

- Create MCP workflows.
- Edit MCP workflows.
- Approve workflows.
- Publish workflows.
- Assign workflows to agents.
- Configure approval rules.
- Review execution history.
- Retry failed executions where authorized.
- Cancel running workflows where authorized.
- Inspect MCP usage.
- Review AI-generated tool actions.
- Approve or reject pending actions.

---

## 3.4 Sales Agent

Sales Agents SHALL be able to:

- Execute authorized MCP workflows.
- Invoke approved MCP tools.
- Request AI assistance.
- Approve AI actions when authorized.
- Review proposed MCP actions.
- Reject AI-proposed actions.
- Cancel authorized executions.
- View execution results.
- Retry recoverable failures.
- View relevant execution history.

---

## 3.5 Support Agent

Support Agents SHALL be able to:

- Execute customer-support MCP workflows.
- Retrieve authorized customer information.
- Search approved knowledge resources.
- Update approved support systems.
- Escalate AI actions.
- Approve high-impact support actions.
- Inspect MCP execution results.

---

## 3.6 Human Approver

A Human Approver SHALL be able to:

- Review pending AI MCP actions.
- Inspect the reason for an action.
- Inspect tool parameters.
- Inspect relevant evidence.
- Approve actions.
- Reject actions.
- Modify permitted parameters.
- Request additional information.
- Delegate approval.
- Record an approval reason.
- Record a rejection reason.

---

## 3.7 AI Agent

AI Agents SHALL be able to:

- Discover authorized MCP tools.
- Inspect tool schemas.
- Select tools based on task requirements.
- Generate structured tool parameters.
- Execute authorized low-risk tools.
- Chain multiple MCP tools.
- Retrieve MCP resources.
- Request human approval.
- Receive tool results.
- Continue workflows after successful tool execution.
- Recover from recoverable failures.
- Escalate when confidence or authorization is insufficient.

AI Agents SHALL NOT:

- Bypass authorization.
- Modify permissions.
- Access unauthorized tenants.
- Access unauthorized MCP servers.
- Access secrets directly.
- Execute prohibited tools.
- Circumvent approval requirements.
- Modify audit records.
- Disable safety controls.
- Continue execution after mandatory approval rejection.

---

## 4. User Requirements

## UR-MCP-001 — MCP Discovery

Users SHALL be able to discover MCP servers, tools, resources, and prompts available to them.

### Acceptance Criteria

- Only authorized MCP capabilities SHALL be displayed.
- Unauthorized tools SHALL NOT be exposed as executable capabilities.
- Tool metadata SHALL include:
  - Tool name
  - Description
  - Server
  - Version
  - Required permissions
  - Input schema
  - Risk classification
  - Availability
  - Approval requirement

---

## UR-MCP-002 — MCP Tool Execution

Authorized users SHALL be able to execute MCP tools.

### Acceptance Criteria

- Authorization SHALL occur server-side.
- Input SHALL be schema validated.
- Execution SHALL generate an audit event.
- Execution SHALL produce a traceable execution ID.
- Results SHALL be associated with the initiating actor.

---

## UR-MCP-003 — AI Tool Execution

AI Agents SHALL be able to invoke authorized MCP tools.

### Acceptance Criteria

The platform SHALL verify:

1. Agent identity.
2. Tenant identity.
3. Workflow identity.
4. Tool authorization.
5. User authorization.
6. Input schema.
7. Execution policy.
8. Approval requirement.
9. Execution budget.
10. Rate limits.

---

## UR-MCP-004 — Human Approval

The system SHALL support mandatory human approval before high-risk MCP operations.

Examples:

- Bulk outreach.
- Data export.
- Customer deletion.
- Lead deletion.
- Financial changes.
- Refunds.
- Permission changes.
- Security-policy changes.
- Bulk CRM modification.
- Mass messaging.
- Irreversible external actions.

---

## UR-MCP-005 — AI-to-Human Handoff

AI Agents SHALL be able to pause execution and request human intervention.

The request SHALL contain:

- Workflow ID.
- Execution ID.
- Agent ID.
- MCP server.
- Tool.
- Intended action.
- Parameters.
- Reason.
- Evidence.
- Risk classification.
- Required decision.
- Expiration time.

---

## UR-MCP-006 — Human-to-AI Delegation

Users SHALL be able to delegate authorized tasks to AI Agents.

Example:

> "Find high-value leads, enrich them, score them, and prepare outreach drafts."

The AI SHALL execute only within the delegated permissions and workflow policy.

---

## UR-MCP-007 — MCP Workflow Composition

Users SHALL be able to compose multiple MCP operations into a single workflow.

Example:

```text
Lead Trigger
    ↓
MCP Company Search
    ↓
MCP Lead Enrichment
    ↓
AI Lead Scoring
    ↓
MCP CRM Update
    ↓
Human Approval
    ↓
MCP Email Send
    ↓
MCP CRM Activity Log
```

---

## UR-MCP-008 — Execution Visibility

Users SHALL be able to view:

* Current execution status.
* Current workflow node.
* MCP server.
* Tool invocation.
* Execution duration.
* Tool result status.
* Errors.
* Retry attempts.
* Approval status.
* AI reasoning summary.
* Human decisions.
* Final outcome.

Sensitive internal reasoning SHALL NOT be exposed merely for observability.

---

## UR-MCP-009 — Failure Recovery

Users SHALL be able to:

* Retry recoverable failures.
* Cancel running workflows.
* Resume paused workflows.
* Inspect failed tool calls.
* View failure causes.
* Escalate failures.
* Replay authorized executions.

---

## UR-MCP-010 — MCP Server Management

Authorized administrators SHALL be able to:

* Register MCP servers.
* Update server metadata.
* Enable servers.
* Disable servers.
* Test connectivity.
* Inspect health.
* Inspect available tools.
* Inspect available resources.
* Configure authentication.
* Configure access policies.

---

## 5. System Requirements

## SR-MCP-001 — Multi-Tenant Isolation

The MCP subsystem SHALL enforce strict tenant isolation.

Every tenant-scoped MCP operation SHALL carry:

```text
organization_id
workspace_id
user_id
agent_id
workflow_id
execution_id
```

The system SHALL prevent:

* Cross-tenant tool execution.
* Cross-tenant resource retrieval.
* Cross-tenant credential access.
* Cross-tenant MCP server configuration.
* Cross-tenant workflow execution.

---

## SR-MCP-002 — Identity Propagation

The system SHALL propagate authenticated identity across:

```text
Frontend
    ↓
API Gateway
    ↓
Workflow Engine
    ↓
AI Agent
    ↓
MCP Gateway
    ↓
MCP Server
    ↓
External Service
```

Identity SHALL NOT be inferred solely from client-provided parameters.

---

## SR-MCP-003 — MCP Gateway

SalesGenie SHALL provide an MCP Gateway responsible for:

* Authentication.
* Authorization.
* Tool discovery.
* Schema validation.
* Policy enforcement.
* Rate limiting.
* Execution budgets.
* Credential isolation.
* Audit logging.
* Request tracing.
* Result validation.
* Failure handling.

---

## SR-MCP-004 — Tool Registry

The platform SHALL maintain a centralized MCP Tool Registry.

Each tool SHALL contain:

```yaml
tool_id:
server_id:
name:
version:
description:
input_schema:
output_schema:
risk_level:
required_permissions:
approval_required:
enabled:
tenant_scope:
rate_limit:
timeout:
retry_policy:
idempotency_policy:
```

---

## SR-MCP-005 — MCP Server Registry

Each MCP server SHALL have:

```yaml
server_id:
name:
provider:
version:
endpoint:
authentication_type:
health_status:
trust_level:
enabled:
allowed_tenants:
allowed_roles:
available_tools:
available_resources:
available_prompts:
created_at:
updated_at:
```

---

## SR-MCP-006 — Strict Schema Validation

Every MCP tool request SHALL be validated against its declared schema.

The system SHALL reject:

* Missing required fields.
* Invalid types.
* Unknown restricted parameters.
* Invalid enum values.
* Oversized inputs.
* Malformed structured data.
* Unauthorized resource identifiers.

---

## SR-MCP-007 — Tool Result Validation

MCP tool results SHALL be validated before being consumed by AI Agents.

The system SHALL detect:

* Invalid response schemas.
* Unexpected payloads.
* Oversized results.
* Malicious instructions.
* Prompt injection indicators.
* Unauthorized data.
* Sensitive information leakage.

---

## SR-MCP-008 — Credential Isolation

MCP credentials SHALL NOT be exposed to:

* End users.
* AI prompts.
* AI model context.
* Browser clients.
* Workflow definitions.
* Logs.

Credentials SHALL be retrieved through secure server-side credential management.

---

## SR-MCP-009 — Least Privilege

Every MCP execution SHALL evaluate permissions at:

```text
Tenant
  ↓
Workspace
  ↓
User
  ↓
Role
  ↓
Agent
  ↓
Workflow
  ↓
MCP Server
  ↓
MCP Tool
  ↓
Resource
```

The effective permission SHALL be the intersection of applicable policies.

---

## SR-MCP-010 — Execution Budgets

The system SHALL enforce configurable limits for:

* Maximum workflow steps.
* Maximum MCP calls.
* Maximum execution time.
* Maximum retries.
* Maximum token usage.
* Maximum payload size.
* Maximum external API calls.
* Maximum cost.
* Maximum recursion depth.

---

## SR-MCP-011 — Idempotency

MCP workflows SHALL support idempotency keys.

Example:

```text
organization_id
+
workflow_id
+
execution_id
+
node_id
+
idempotency_key
```

Repeated requests SHALL NOT unintentionally create duplicate side effects.

---

## SR-MCP-012 — Distributed Tracing

Every MCP execution SHALL support distributed tracing.

Required identifiers:

```text
request_id
trace_id
span_id
organization_id
workflow_id
execution_id
node_id
agent_id
tool_call_id
```

---

## SR-MCP-013 — Auditability

The system SHALL record every security-sensitive MCP operation.

Audit records SHALL include:

```yaml
timestamp:
actor_type:
actor_id:
organization_id:
workflow_id:
execution_id:
mcp_server:
tool:
action:
parameters_redacted:
authorization_decision:
approval_state:
result_status:
latency:
error_code:
ip_or_source:
trace_id:
```

---

## SR-MCP-014 — Sensitive Data Redaction

The logging subsystem SHALL redact:

* API keys.
* OAuth tokens.
* Passwords.
* Session tokens.
* Payment credentials.
* Authentication headers.
* Sensitive customer data where configured.

---

## SR-MCP-015 — Asynchronous Execution

Long-running MCP workflows SHALL execute asynchronously.

The system SHALL support:

* Job queues.
* Worker pools.
* Retry queues.
* Dead-letter queues.
* Job prioritization.
* Backpressure.
* Execution cancellation.

---

## SR-MCP-016 — MCP Health Monitoring

The system SHALL continuously monitor MCP servers.

Health checks SHALL measure:

* Availability.
* Latency.
* Error rate.
* Timeout rate.
* Authentication failures.
* Tool failure rate.
* Rate-limit responses.
* Circuit-breaker state.

---

## SR-MCP-017 — Circuit Breaker

The platform SHALL temporarily stop calls to unhealthy MCP servers when configurable failure thresholds are exceeded.

Circuit states:

```text
CLOSED
   ↓
OPEN
   ↓
HALF_OPEN
   ↓
CLOSED
```

---

## SR-MCP-018 — Rate Limiting

Rate limits SHALL be enforceable by:

* Tenant.
* User.
* Agent.
* Workflow.
* MCP server.
* MCP tool.
* External integration.

---

## SR-MCP-019 — MCP Version Compatibility

The platform SHALL support MCP capability/version compatibility checks.

Unsupported capabilities SHALL be rejected gracefully.

---

## SR-MCP-020 — Provider Independence

The MCP architecture SHALL prevent application business logic from being tightly coupled to a specific MCP provider.

---

## 6. Functional Requirements

## 6.1 MCP Server Registration

## FR-MCP-001

The system SHALL allow authorized administrators to register an MCP server.

## FR-MCP-002

The system SHALL validate MCP server connectivity during registration.

## FR-MCP-003

The system SHALL discover available:

* Tools.
* Resources.
* Prompts.
* Capabilities.

## FR-MCP-004

The system SHALL persist discovered MCP metadata.

## FR-MCP-005

The system SHALL support manual server disablement.

---

## 6.2 MCP Tool Discovery

## FR-MCP-006

The system SHALL expose only tools permitted by policy.

## FR-MCP-007

The system SHALL allow filtering tools by:

* Category.
* MCP server.
* Risk.
* Permission.
* Availability.
* Tenant.
* Agent.

## FR-MCP-008

AI Agents SHALL receive only authorized tool definitions.

---

## 6.3 AI MCP Execution

## FR-MCP-009

AI Agents SHALL select MCP tools based on task requirements.

## FR-MCP-010

The MCP Gateway SHALL independently authorize every AI-generated tool call.

## FR-MCP-011

AI-generated parameters SHALL undergo schema validation.

## FR-MCP-012

The system SHALL reject unauthorized tool calls.

## FR-MCP-013

The system SHALL record the complete execution lifecycle.

---

## 6.4 Human MCP Execution

## FR-MCP-014

Human users SHALL be able to execute authorized MCP tools.

## FR-MCP-015

Human execution SHALL use the same authorization boundary as AI execution.

## FR-MCP-016

Human users SHALL receive structured execution results.

---

## 6.5 AI-Human Approval

## FR-MCP-017

The system SHALL classify MCP tools by risk.

Example:

```text
LOW
MEDIUM
HIGH
CRITICAL
```

## FR-MCP-018

Administrators SHALL configure approval requirements by risk level.

## FR-MCP-019

The system SHALL pause workflows requiring approval.

## FR-MCP-020

The system SHALL notify authorized approvers.

## FR-MCP-021

Approvers SHALL be able to:

```text
APPROVE
REJECT
EDIT
REQUEST_INFORMATION
DELEGATE
```

## FR-MCP-022

Approval decisions SHALL be immutable audit events.

---

## 6.6 AI-to-Human Escalation

## FR-MCP-023

AI Agents SHALL escalate when:

* Required authorization is unavailable.
* Tool confidence is insufficient.
* The action is high-risk.
* The tool returns ambiguous results.
* The external system reports a conflict.
* The action is irreversible.
* Policy explicitly requires approval.

---

## 6.7 Human-to-AI Delegation

## FR-MCP-024

Users SHALL be able to delegate tasks to AI Agents.

Delegation SHALL define:

```yaml
objective:
allowed_tools:
allowed_servers:
data_scope:
max_steps:
max_cost:
deadline:
approval_policy:
success_criteria:
```

## FR-MCP-025

AI Agents SHALL NOT exceed delegated authority.

---

## 6.8 MCP Workflow Chaining

## FR-MCP-026

The workflow engine SHALL support sequential MCP execution.

```text
MCP A
 ↓
MCP B
 ↓
MCP C
```

## FR-MCP-027

The workflow engine SHALL support parallel execution.

```text
             ┌── MCP A ──┐
Trigger ─────┼── MCP B ──┼── Aggregator
             └── MCP C ──┘
```

## FR-MCP-028

The workflow engine SHALL support conditional MCP execution.

```text
IF lead_score >= 80
    → CRM Update
ELSE
    → Nurture Workflow
```

## FR-MCP-029

The workflow engine SHALL support loops with explicit iteration limits.

---

## 6.9 MCP Resources

## FR-MCP-030

AI Agents SHALL be able to retrieve authorized MCP resources.

## FR-MCP-031

Resource access SHALL enforce tenant and user permissions.

## FR-MCP-032

Retrieved resources SHALL be marked with provenance metadata.

---

## 6.10 MCP Prompts

## FR-MCP-033

The platform SHALL support authorized MCP prompts.

## FR-MCP-034

MCP prompts SHALL be treated as untrusted input.

## FR-MCP-035

MCP prompts SHALL NOT override SalesGenie system policies.

---

## 6.11 Prompt Injection Defense

## FR-MCP-036

The system SHALL treat external MCP content as untrusted.

## FR-MCP-037

The system SHALL detect potential indirect prompt injection.

## FR-MCP-038

Retrieved instructions SHALL NOT modify:

* System policies.
* Permissions.
* Security configuration.
* Tool authorization.
* Approval requirements.

---

## 6.12 MCP + RAG

## FR-MCP-039

MCP workflows SHALL be able to retrieve RAG knowledge.

## FR-MCP-040

RAG retrieval SHALL enforce:

```text
organization_id
workspace_id
document_permissions
user_permissions
```

## FR-MCP-041

AI-generated external actions based on RAG information SHALL preserve provenance.

---

## 6.13 MCP + CRM

## FR-MCP-042

MCP workflows SHALL support authorized CRM operations.

Examples:

* Search contacts.
* Create leads.
* Update leads.
* Retrieve opportunities.
* Update opportunities.
* Add activities.
* Create tasks.
* Retrieve customer history.

## FR-MCP-043

CRM mutations SHALL be subject to authorization and idempotency.

---

## 6.14 MCP + Lead Intelligence

## FR-MCP-044

MCP workflows SHALL support:

```text
Company Search
Lead Discovery
Lead Enrichment
Contact Verification
Lead Scoring
Market Research
Competitor Research
CRM Synchronization
```

## FR-MCP-045

External lead information SHALL preserve provenance.

---

## 6.15 MCP + Sales Automation

## FR-MCP-046

AI Agents SHALL be able to prepare sales actions through MCP.

Examples:

```text
Find Lead
→ Enrich Lead
→ Score Lead
→ Generate Message
→ Human Approval
→ Send Message
→ Update CRM
```

## FR-MCP-047

Bulk outreach SHALL require configurable approval.

---

## 6.16 MCP + Customer Support

## FR-MCP-048

Support workflows SHALL support:

* Customer lookup.
* Ticket lookup.
* Ticket creation.
* Ticket update.
* Knowledge retrieval.
* Customer communication.
* Escalation.
* CRM synchronization.

---

## 6.17 MCP + Omnichannel

MCP workflows SHALL integrate with SalesGenie's supported channels.

Examples:

```text
Website
WhatsApp
Telegram
Slack
Discord
Email
Voice
```

Channel-specific operations SHALL inherit tenant, user, and workflow permissions.

---

## 6.18 MCP + n8n

## FR-MCP-049

SalesGenie SHALL support interoperability between MCP workflows and n8n workflows.

## FR-MCP-050

n8n-triggered MCP operations SHALL be authenticated and authorized.

## FR-MCP-051

MCP-triggered n8n workflows SHALL use signed or authenticated requests.

## FR-MCP-052

n8n workflow execution SHALL preserve:

```text
tenant
workflow
actor
execution
trace
```

context.

---

## 6.19 MCP + Scheduler

## FR-MCP-053

MCP workflows SHALL support scheduled execution.

Examples:

```text
Every day at 09:00
Every Monday
Every 6 hours
Monthly
Cron expression
```

## FR-MCP-054

Scheduled execution SHALL execute under a predefined service identity and policy.

## FR-MCP-055

Scheduled AI execution SHALL NOT bypass approval requirements.

---

## 6.20 MCP Event Triggers

## FR-MCP-056

MCP workflows SHALL support event-driven triggers.

Examples:

```text
New Lead
New Customer
New Ticket
New Email
CRM Update
Payment Event
Webhook
MCP Resource Event
```

## FR-MCP-057

Duplicate events SHALL be safely handled.

---

## 6.21 Error Handling

## FR-MCP-058

The system SHALL classify MCP failures.

Example:

```text
AUTHENTICATION_ERROR
AUTHORIZATION_ERROR
VALIDATION_ERROR
TIMEOUT
RATE_LIMIT
SERVER_ERROR
NETWORK_ERROR
SCHEMA_ERROR
POLICY_VIOLATION
PROVIDER_UNAVAILABLE
UNKNOWN_ERROR
```

## FR-MCP-059

Recoverable failures SHALL use bounded retries.

## FR-MCP-060

Retries SHALL use exponential backoff with jitter.

## FR-MCP-061

Non-recoverable failures SHALL stop or route execution according to workflow policy.

---

## 6.22 Dead-Letter Queue

## FR-MCP-062

Failed MCP jobs exceeding retry limits SHALL enter a dead-letter queue.

## FR-MCP-063

Authorized operators SHALL be able to:

* Inspect.
* Retry.
* Replay.
* Cancel.
* Archive.

dead-lettered jobs.

---

## 6.23 MCP Execution State Machine

Every MCP workflow execution SHALL support states:

```text
CREATED
   ↓
QUEUED
   ↓
RUNNING
   ↓
WAITING_APPROVAL
   ↓
APPROVED
   ↓
RUNNING
   ↓
COMPLETED
```

Alternative terminal states:

```text
FAILED
CANCELLED
REJECTED
TIMED_OUT
EXPIRED
```

Invalid state transitions SHALL be rejected.

---

## 6.24 Monitoring

## FR-MCP-064

The platform SHALL expose MCP metrics including:

* Total tool calls.
* Successful calls.
* Failed calls.
* Timeout rate.
* Retry rate.
* Average latency.
* P95 latency.
* P99 latency.
* Approval latency.
* Tool usage.
* Agent usage.
* Tenant usage.
* Cost.
* Token consumption.
* Server availability.

---

## 6.25 Alerts

The system SHALL generate alerts for:

* MCP server outage.
* Abnormal error rate.
* Repeated tool failures.
* Excessive retries.
* Execution timeout spikes.
* Unauthorized access attempts.
* Cross-tenant access attempts.
* Cost anomalies.
* Runaway agents.
* Infinite workflow loops.
* Excessive tool calls.
* Approval backlog.

---

## 6.26 MCP Cost Management

## FR-MCP-065

The platform SHALL meter MCP usage.

Usage SHALL be attributable to:

```text
Tenant
User
Agent
Workflow
MCP Server
Tool
Execution
```

## FR-MCP-066

The system SHALL enforce configurable MCP budgets.

## FR-MCP-067

The system SHALL stop or degrade execution when configured budgets are exceeded.

---

## 6.27 Workflow Versioning

## FR-MCP-068

MCP workflows SHALL be version controlled.

Each version SHALL contain:

```yaml
workflow_id:
version:
definition:
mcp_servers:
tools:
permissions:
approval_policy:
execution_policy:
created_by:
created_at:
published_at:
status:
```

## FR-MCP-069

Running executions SHALL remain associated with the exact workflow version from which they originated.

## FR-MCP-070

Published workflows SHALL support rollback.

---

## 6.28 MCP Workflow Templates

## FR-MCP-071

The platform SHALL provide reusable MCP workflow templates.

Examples:

### Lead Enrichment

```text
Lead Trigger
→ Company Lookup
→ Contact Enrichment
→ AI Qualification
→ CRM Update
```

### Sales Outreach

```text
Lead Selection
→ AI Research
→ Message Generation
→ Human Approval
→ Email/WhatsApp
→ CRM Update
```

### Support Resolution

```text
Ticket Trigger
→ Customer Lookup
→ RAG Retrieval
→ AI Response
→ Policy Check
→ Human Approval if Required
→ Customer Response
→ Ticket Update
```

---

## 6.29 Security Requirements

## FR-MCP-072

The platform SHALL enforce RBAC and policy-based authorization.

## FR-MCP-073

Every tool call SHALL be authorized independently.

## FR-MCP-074

AI Agents SHALL never inherit unrestricted human permissions automatically.

## FR-MCP-075

Tool permissions SHALL be explicitly granted.

## FR-MCP-076

Security-sensitive MCP operations SHALL require elevated authorization.

---

## 6.30 High-Risk Operations

The following SHALL be configurable as mandatory-approval operations:

```text
DELETE_CUSTOMER
DELETE_LEAD
DELETE_DOCUMENT
EXPORT_DATA
SEND_BULK_EMAIL
SEND_BULK_WHATSAPP
CHANGE_BILLING
REFUND_PAYMENT
CHANGE_USER_ROLE
CHANGE_SECURITY_POLICY
CREATE_ADMIN
DISABLE_SECURITY_CONTROL
MODIFY_PRODUCTION_CONFIGURATION
MASS_CRM_UPDATE
```

---

## 6.31 AI Safety Boundaries

## FR-MCP-077

AI Agents SHALL NOT:

```text
Change their own permissions
Create unrestricted credentials
Disable audit logging
Disable approval policies
Access another tenant
Modify system prompts
Modify security policies
Delete audit evidence
Bypass rate limits
Bypass execution budgets
```

---

## 6.32 Human Safety Boundaries

## FR-MCP-078

Human users SHALL NOT bypass server-side MCP authorization through UI manipulation.

All permissions SHALL be enforced server-side.

---

## 7. AI Workflow Requirements

## AI-MCP-001 — Autonomous Low-Risk Actions

AI Agents MAY autonomously execute low-risk operations when explicitly authorized.

Examples:

* Read-only CRM search.
* Knowledge retrieval.
* Lead research.
* Analytics retrieval.
* Non-destructive enrichment.

---

## AI-MCP-002 — Controlled Medium-Risk Actions

Medium-risk actions SHALL require configurable policy evaluation.

Examples:

* CRM modification.
* Creating tasks.
* Updating customer metadata.
* Creating support tickets.

---

## AI-MCP-003 — Human-Gated High-Risk Actions

High-risk operations SHALL require human approval.

---

## AI-MCP-004 — AI Confidence

AI workflows MAY use confidence thresholds.

Example:

```text
confidence >= 0.90
    → execute

0.70 <= confidence < 0.90
    → additional validation

confidence < 0.70
    → human review
```

Confidence SHALL NOT replace authorization.

---

## AI-MCP-005 — Tool Selection

AI Agents SHALL select tools only from the authorized tool set provided by the MCP policy engine.

---

## AI-MCP-006 — Tool Planning

AI Agents MAY create execution plans.

Example:

```text
Objective:
Identify qualified enterprise leads.

Plan:
1. Search companies.
2. Enrich companies.
3. Retrieve decision makers.
4. Score leads.
5. Store qualified leads.
6. Request approval for outreach.
```

The plan SHALL remain subject to runtime authorization.

---

## 8. Human Workflow Requirements

## HUMAN-MCP-001

Humans SHALL be able to manually initiate MCP workflows.

## HUMAN-MCP-002

Humans SHALL be able to inspect AI-generated MCP plans.

## HUMAN-MCP-003

Humans SHALL be able to approve or reject high-risk actions.

## HUMAN-MCP-004

Humans SHALL be able to override AI recommendations only within their own authorization scope.

## HUMAN-MCP-005

Human overrides SHALL be audited.

---

## 9. MCP Policy Engine

The policy engine SHALL evaluate:

```text
WHO
WHAT
WHERE
WHEN
WHY
HOW
RISK
DATA_SCOPE
COST
APPROVAL
```

Example policy:

```yaml
policy:
  role: sales_agent
  tool: send_email
  risk: high
  max_recipients: 10
  approval_required: true
  allowed_channels:
    - email
  allowed_hours:
    start: "08:00"
    end: "18:00"
```

---

## 10. MCP Authorization Decision

Every MCP operation SHALL result in a deterministic authorization decision:

```text
ALLOW
DENY
REQUIRE_APPROVAL
RATE_LIMIT
BUDGET_EXCEEDED
POLICY_VIOLATION
```

The decision SHALL be logged.

---

## 11. MCP Execution Context

Every execution SHALL maintain:

```yaml
ExecutionContext:
  request_id:
  trace_id:
  organization_id:
  workspace_id:
  user_id:
  actor_type:
  agent_id:
  workflow_id:
  workflow_version:
  execution_id:
  node_id:
  mcp_server_id:
  tool_id:
  permissions:
  approval_state:
  budget:
  deadline:
```

---

## 12. MCP Workflow API Requirements

The backend SHALL expose APIs conceptually equivalent to:

```text
POST   /api/v1/mcp/servers
GET    /api/v1/mcp/servers
GET    /api/v1/mcp/servers/{server_id}
PATCH  /api/v1/mcp/servers/{server_id}
DELETE /api/v1/mcp/servers/{server_id}

GET    /api/v1/mcp/tools
GET    /api/v1/mcp/tools/{tool_id}

POST   /api/v1/mcp/tools/{tool_id}/execute

POST   /api/v1/mcp/workflows
GET    /api/v1/mcp/workflows
GET    /api/v1/mcp/workflows/{workflow_id}
PATCH  /api/v1/mcp/workflows/{workflow_id}

POST   /api/v1/mcp/workflows/{workflow_id}/execute
POST   /api/v1/mcp/executions/{execution_id}/cancel
POST   /api/v1/mcp/executions/{execution_id}/retry
GET    /api/v1/mcp/executions/{execution_id}

GET    /api/v1/mcp/approvals
POST   /api/v1/mcp/approvals/{approval_id}/approve
POST   /api/v1/mcp/approvals/{approval_id}/reject

GET    /api/v1/mcp/audit
GET    /api/v1/mcp/metrics
GET    /api/v1/mcp/health
```

Actual endpoint naming SHALL remain consistent with SalesGenie's existing API conventions.

---

## 13. Event Model

The MCP subsystem SHALL emit events such as:

```text
MCP_SERVER_REGISTERED
MCP_SERVER_ENABLED
MCP_SERVER_DISABLED
MCP_SERVER_UNHEALTHY

MCP_TOOL_DISCOVERED
MCP_TOOL_EXECUTION_STARTED
MCP_TOOL_EXECUTION_COMPLETED
MCP_TOOL_EXECUTION_FAILED

MCP_WORKFLOW_CREATED
MCP_WORKFLOW_STARTED
MCP_WORKFLOW_PAUSED
MCP_WORKFLOW_RESUMED
MCP_WORKFLOW_COMPLETED
MCP_WORKFLOW_FAILED
MCP_WORKFLOW_CANCELLED

MCP_APPROVAL_REQUESTED
MCP_APPROVAL_APPROVED
MCP_APPROVAL_REJECTED
MCP_APPROVAL_EXPIRED

MCP_POLICY_ALLOWED
MCP_POLICY_DENIED
MCP_POLICY_VIOLATED

MCP_BUDGET_EXCEEDED
MCP_RATE_LIMITED
MCP_CIRCUIT_OPENED
MCP_CIRCUIT_CLOSED
```

---

## 14. Data Model Requirements

Core entities SHALL include:

```text
MCPServer
MCPTool
MCPResource
MCPPrompt
MCPPermission
MCPPolicy
MCPWorkflow
MCPWorkflowVersion
MCPWorkflowExecution
MCPToolExecution
MCPApproval
MCPExecutionEvent
MCPAuditEvent
MCPCredentialReference
MCPUsageRecord
MCPServerHealth
MCPDeadLetterJob
```

Every tenant-scoped entity SHALL include appropriate tenant ownership metadata.

---

## 15. Reliability Requirements

The MCP subsystem SHALL:

* Use bounded retries.
* Use exponential backoff.
* Support circuit breakers.
* Support dead-letter queues.
* Support graceful degradation.
* Support execution cancellation.
* Support recovery after worker restart.
* Support idempotent execution.
* Prevent duplicate side effects.
* Preserve workflow state after recoverable failures.
* Prevent infinite execution loops.

---

## 16. Performance Requirements

The MCP subsystem SHALL:

* Execute independent tool calls in parallel when safe.
* Avoid unnecessary tool calls.
* Cache safe read-only results where appropriate.
* Use asynchronous workers for long-running operations.
* Enforce connection pooling.
* Avoid unbounded payloads.
* Enforce execution timeouts.
* Provide queue backpressure.

Performance SHALL be measured using:

```text
P50
P95
P99
Error Rate
Throughput
Queue Latency
Tool Latency
Workflow Completion Time
```

---

## 17. Observability Requirements

The platform SHALL provide dashboards for:

## MCP Infrastructure

```text
Server Availability
Server Errors
Server Latency
Tool Failures
```

## AI Operations

```text
Agent Tool Calls
AI Tool Success Rate
AI Tool Failure Rate
Approval Rate
Escalation Rate
```

## Business Operations

```text
Leads Processed
CRM Actions
Support Actions
Messages Sent
Workflow Success Rate
```

## Cost

```text
MCP Calls
External API Usage
AI Tokens
Workflow Cost
Tenant Cost
```

---

## 18. Compliance and Governance

The platform SHALL support:

* Data retention policies.
* Data deletion policies.
* Audit retention.
* Data export controls.
* Consent-aware communication workflows.
* Data provenance.
* Third-party data tracking.
* Subprocessor awareness.
* Tenant-specific governance policies.

---

## 19. Testing Requirements

The MCP subsystem SHALL have:

## Unit Tests

* Authorization.
* Schema validation.
* Policy evaluation.
* Risk classification.
* Budget enforcement.
* Retry logic.
* Idempotency.

## Integration Tests

* MCP server connectivity.
* Tool discovery.
* Tool execution.
* Credential handling.
* Workflow execution.
* Approval workflows.

## Security Tests

* Cross-tenant access.
* Privilege escalation.
* Prompt injection.
* Tool injection.
* Unauthorized tool calls.
* Credential leakage.
* Policy bypass.

## Reliability Tests

* MCP server outage.
* Network timeout.
* Rate limiting.
* Worker crash.
* Queue failure.
* Duplicate events.
* Duplicate tool calls.

## AI Evaluation Tests

* Tool selection accuracy.
* Parameter correctness.
* Tool-result interpretation.
* Policy compliance.
* Approval routing.
* Hallucinated tool prevention.

---

## 20. Acceptance Criteria

The MCP workflow subsystem SHALL NOT be considered production-ready until:

* [ ] Every MCP tool call is authenticated.
* [ ] Every MCP tool call is authorized.
* [ ] Tenant isolation is enforced.
* [ ] AI agents cannot bypass permissions.
* [ ] Tool inputs are schema validated.
* [ ] Tool outputs are validated.
* [ ] Credentials are isolated.
* [ ] High-risk actions require approval.
* [ ] Approval decisions are auditable.
* [ ] Every execution has a trace ID.
* [ ] Every execution has an execution ID.
* [ ] Idempotency is implemented.
* [ ] Retry policies are bounded.
* [ ] Dead-letter handling exists.
* [ ] Circuit breakers exist.
* [ ] Execution budgets exist.
* [ ] Rate limits exist.
* [ ] MCP health monitoring exists.
* [ ] MCP failures are observable.
* [ ] Sensitive information is redacted.
* [ ] Cross-tenant security tests pass.
* [ ] Prompt-injection tests pass.
* [ ] Workflow state recovery works.
* [ ] Human cancellation works.
* [ ] AI-to-human escalation works.
* [ ] Human-to-AI delegation works.
* [ ] MCP workflow versioning works.
* [ ] MCP audit logs are immutable.
* [ ] Cost attribution works.
* [ ] Production alerts are configured.
* [ ] MCP workflows can be safely disabled.
* [ ] Emergency MCP shutdown is available to authorized administrators.

---

## 21. FAANG-Level Non-Functional Requirements

## Security

```text
NFR-MCP-SEC-001
Zero-trust MCP authorization.

NFR-MCP-SEC-002
Strict tenant isolation.

NFR-MCP-SEC-003
Least-privilege tool permissions.

NFR-MCP-SEC-004
Server-side authorization enforcement.

NFR-MCP-SEC-005
Credential isolation.

NFR-MCP-SEC-006
Prompt-injection resistance.

NFR-MCP-SEC-007
Immutable security audit trail.
```

## Reliability

```text
NFR-MCP-REL-001
Bounded retries.

NFR-MCP-REL-002
Circuit breakers.

NFR-MCP-REL-003
Dead-letter queues.

NFR-MCP-REL-004
Idempotent side effects.

NFR-MCP-REL-005
Crash-safe workflow state.

NFR-MCP-REL-006
Graceful provider degradation.
```

## Scalability

```text
NFR-MCP-SCALE-001
Horizontal MCP worker scaling.

NFR-MCP-SCALE-002
Queue-based workload distribution.

NFR-MCP-SCALE-003
Tenant-aware workload isolation.

NFR-MCP-SCALE-004
Backpressure under overload.

NFR-MCP-SCALE-005
Parallel execution for independent operations.
```

## Observability

```text
NFR-MCP-OBS-001
Distributed tracing.

NFR-MCP-OBS-002
Structured logs.

NFR-MCP-OBS-003
Execution metrics.

NFR-MCP-OBS-004
Security audit events.

NFR-MCP-OBS-005
Tenant-level operational visibility.
```

---

## 22. Reference AI + Human MCP Workflow

```text
                         ┌──────────────────────┐
                         │ Human User / Event   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Workflow Trigger     │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ AI Workflow Planner  │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Policy Engine        │
                         └──────────┬───────────┘
                                    │
                    ┌───────────────┼────────────────┐
                    │               │                │
                    ▼               ▼                ▼
                 ALLOW        REQUIRE APPROVAL      DENY
                    │               │
                    │               ▼
                    │      ┌─────────────────┐
                    │      │ Human Approver  │
                    │      └────────┬────────┘
                    │               │
                    │        ┌──────┴──────┐
                    │        │             │
                    │        ▼             ▼
                    │     APPROVE        REJECT
                    │        │
                    └────────┤
                             ▼
                  ┌──────────────────────┐
                  │ MCP Gateway          │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ MCP Tool / Resource │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ External System      │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ Result Validation     │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ AI / Workflow Engine │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ Audit + Observability│
                  └──────────────────────┘
```

---

## 23. Golden Rules

1. **AI autonomy SHALL never imply authorization.**
2. **Every MCP tool call SHALL be independently authorized.**
3. **Every external side effect SHALL be policy controlled.**
4. **High-risk actions SHALL support mandatory human approval.**
5. **No MCP credential SHALL enter model context.**
6. **No MCP server SHALL be trusted merely because it is registered.**
7. **External MCP content SHALL be treated as untrusted data.**
8. **MCP tool schemas SHALL be validated before execution.**
9. **MCP results SHALL be validated before agent consumption.**
10. **Every execution SHALL be traceable.**
11. **Every security-sensitive action SHALL be auditable.**
12. **Every retryable operation SHALL be idempotent or protected against duplicate side effects.**
13. **Every AI workflow SHALL have bounded execution limits.**
14. **Every tenant SHALL remain cryptographically/logically isolated according to the platform's security architecture.**
15. **Human intervention SHALL be available for configured high-impact decisions.**
16. **Workflow failures SHALL never silently become successful executions.**
17. **MCP outages SHALL not compromise core SalesGenie functionality.**
18. **Authorization SHALL always be enforced server-side.**
19. **Audit logs SHALL never be controlled by the AI agent being audited.**
20. **The MCP layer SHALL remain independently observable, governable, and disableable.**
