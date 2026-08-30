# SalesGenie — MCP Platform Requirements Specification

> **Document:** `mcp_platform.md`
> **Platform:** SalesGenie Enterprise AI Customer Support & Sales Agent Platform
> **Scope:** Enterprise Model Context Protocol (MCP) Platform
> **Actors:** Super Admin, Organization Admin, Manager, Sales Agent, Support Agent, Human Approver, AI Agent, MCP Platform, MCP Gateway, MCP Server, MCP Tool, MCP Resource, Workflow Engine, External Service
> **Requirement Standard:** FAANG-level / Enterprise Production
> **Architecture:** Multi-tenant, microservices, event-driven, AI-native, policy-driven

---

## 1. Platform Objective

SalesGenie SHALL provide an enterprise-grade MCP platform that enables AI agents and human users to securely discover, govern, execute, compose, monitor, and manage MCP servers, tools, resources, and prompts.

The MCP platform SHALL operate as a controlled execution layer between SalesGenie AI agents/workflows and external systems.

```text
Users
  │
  ├── Human Users
  │
  └── AI Agents
          │
          ▼
┌─────────────────────────────┐
│ SalesGenie AI / Workflow    │
│ Orchestration Layer         │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ MCP Policy & Authorization  │
│ Layer                       │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ MCP Gateway                 │
│                             │
│ Discovery                   │
│ Authentication              │
│ Authorization               │
│ Validation                  │
│ Rate Limiting               │
│ Credential Isolation        │
│ Observability               │
└──────────────┬──────────────┘
               │
       ┌───────┼────────┐
       ▼       ▼        ▼
    MCP      MCP      MCP
   Server   Server   Server
       │       │        │
       ▼       ▼        ▼
   External Systems / APIs
```

---

## 2. Platform Goals

The MCP platform SHALL provide:

* Secure MCP server management.
* MCP server discovery.
* MCP tool discovery.
* MCP resource discovery.
* MCP prompt discovery.
* MCP server lifecycle management.
* MCP capability negotiation.
* AI tool execution.
* Human tool execution.
* AI-human approval workflows.
* MCP workflow orchestration.
* MCP server health monitoring.
* MCP usage monitoring.
* MCP cost attribution.
* MCP security governance.
* Credential isolation.
* Tenant isolation.
* Policy enforcement.
* Auditability.
* Version compatibility.
* Failure recovery.
* Rate limiting.
* Execution budgets.
* Tool-level permissions.
* Data-level permissions.
* Enterprise observability.
* Emergency MCP shutdown.
* Platform-level governance.

---

## 3. Design Principles

The platform SHALL follow:

1. Zero Trust.
2. Least Privilege.
3. Defense in Depth.
4. Tenant Isolation.
5. Explicit Authorization.
6. Policy Before Execution.
7. Human Oversight.
8. AI Bounded Autonomy.
9. Secure-by-Default Configuration.
10. Fail-Safe Execution.
11. Deterministic Authorization.
12. Immutable Auditability.
13. Provider Independence.
14. Schema-First Tool Execution.
15. Idempotent External Side Effects.
16. Observable Distributed Execution.
17. Graceful Degradation.
18. Backward Compatibility.
19. Cost-Aware Execution.
20. No Silent Side Effects.

---

## 4. Actors

## 4.1 Super Admin

The Super Admin SHALL be able to:

* Register MCP servers.
* Approve MCP servers.
* Reject MCP servers.
* Disable MCP servers globally.
* Configure platform MCP policies.
* Configure global MCP security policies.
* Configure platform-wide rate limits.
* Configure execution budgets.
* Configure risk policies.
* Manage trusted MCP providers.
* View all MCP servers.
* View all MCP tools.
* View global MCP usage.
* View tenant MCP usage.
* View MCP security events.
* View MCP audit logs.
* View platform health.
* Investigate incidents.
* Perform emergency shutdown.
* Restore disabled MCP services.
* Configure MCP maintenance mode.

The Super Admin SHALL NOT be able to access tenant business data unless separately authorized through the platform's administrative access-control mechanism.

---

## 4.2 Organization Admin

The Organization Admin SHALL be able to:

* Enable approved MCP servers for their organization.
* Disable MCP servers.
* Assign MCP permissions.
* Configure organization MCP policies.
* Configure agent permissions.
* Configure workflow permissions.
* Configure user permissions.
* Configure approval requirements.
* Configure execution limits.
* Configure MCP credentials.
* Monitor MCP usage.
* Review MCP audit events.
* Review MCP failures.
* Configure approved external systems.

---

## 4.3 Manager

Managers SHALL be able to:

* Create MCP-enabled workflows.
* Configure MCP tools.
* Assign tools to AI agents.
* Assign workflows to teams.
* Configure approval policies.
* Review executions.
* Review failures.
* Retry authorized executions.
* Cancel authorized executions.
* Review AI-generated actions.

---

## 4.4 Sales Agent

Sales Agents SHALL be able to:

* Use authorized MCP capabilities.
* Execute approved workflows.
* Trigger AI workflows.
* Review AI actions.
* Approve configured actions.
* Reject configured actions.
* View execution status.
* View execution results.

---

## 4.5 Support Agent

Support Agents SHALL be able to:

* Execute approved support workflows.
* Search customer data through authorized MCP tools.
* Retrieve knowledge resources.
* Update support systems.
* Escalate AI actions.
* Approve configured customer-impacting operations.

---

## 4.6 Human Approver

Human Approvers SHALL be able to:

* Review AI-generated MCP actions.
* Inspect proposed parameters.
* Inspect relevant evidence.
* Approve actions.
* Reject actions.
* Request clarification.
* Modify parameters where permitted.
* Delegate approval.
* Provide approval/rejection reasons.

---

## 4.7 AI Agent

AI Agents SHALL be able to:

* Discover authorized tools.
* Discover authorized resources.
* Select appropriate tools.
* Construct structured tool calls.
* Execute authorized low-risk operations.
* Chain tools.
* Consume validated tool results.
* Request human approval.
* Escalate ambiguous operations.
* Recover from recoverable failures.

AI Agents SHALL NOT be able to:

* Modify their own permissions.
* Grant permissions.
* Access secrets.
* Disable security policies.
* Disable auditing.
* Bypass human approval.
* Access another tenant.
* Execute prohibited tools.
* Modify platform governance.

---

## 5. User Requirements

## UR-MCP-001 — MCP Marketplace

Users SHALL have access to an MCP marketplace/catalog showing approved MCP servers and capabilities.

The catalog SHALL provide:

* Server name.
* Provider.
* Description.
* Version.
* Capabilities.
* Tools.
* Resources.
* Prompts.
* Security status.
* Availability.
* Required permissions.
* Risk classification.
* Organization availability.

---

## UR-MCP-002 — MCP Server Installation

Authorized administrators SHALL be able to enable an approved MCP server.

Installation SHALL support:

```text
Discover
→ Review
→ Authorize
→ Configure
→ Validate
→ Enable
```

---

## UR-MCP-003 — MCP Server Configuration

Administrators SHALL be able to configure:

* Authentication.
* Allowed users.
* Allowed roles.
* Allowed agents.
* Allowed workflows.
* Allowed tools.
* Allowed resources.
* Rate limits.
* Execution timeout.
* Retry policy.
* Approval requirements.
* Data-access scope.

---

## UR-MCP-004 — MCP Tool Catalog

Users SHALL be able to browse authorized MCP tools.

Each tool SHALL expose:

```yaml
tool:
  name:
  description:
  server:
  version:
  input_schema:
  output_schema:
  risk_level:
  required_permissions:
  approval_required:
  enabled:
```

---

## UR-MCP-005 — AI Tool Usage

Users SHALL be able to configure which MCP tools an AI Agent can use.

Example:

```yaml
agent:
  name: Sales Research Agent

  allowed_tools:
    - company_search
    - lead_enrichment
    - contact_lookup

  prohibited_tools:
    - bulk_delete
    - payment_refund

  approval_required:
    - send_email
```

---

## UR-MCP-006 — Human Tool Usage

Humans SHALL be able to execute authorized MCP tools through SalesGenie interfaces.

The same server-side authorization engine SHALL be used for human and AI execution.

---

## UR-MCP-007 — AI-Human Collaboration

Users SHALL be able to configure:

```text
AI → Human Approval → MCP
```

and:

```text
Human → AI Delegation → MCP
```

---

## UR-MCP-008 — MCP Workflow Builder

Authorized users SHALL be able to create MCP workflows using a visual workflow builder.

Supported nodes SHALL include:

```text
Trigger
AI Agent
MCP Tool
MCP Resource
MCP Prompt
Condition
Loop
Parallel
Human Approval
Delay
Webhook
HTTP
Transform
Database
Notification
End
```

---

## UR-MCP-009 — MCP Workflow Execution

Users SHALL be able to:

* Start workflows.
* Pause workflows.
* Resume workflows.
* Cancel workflows.
* Retry workflows.
* Inspect executions.
* View results.

---

## UR-MCP-010 — MCP Server Health

Users SHALL be able to see:

* Server status.
* Availability.
* Latency.
* Error rate.
* Tool health.
* Authentication status.
* Rate-limit status.
* Circuit-breaker status.

---

## 6. System Requirements

## SR-MCP-001 — Multi-Tenancy

The MCP platform SHALL be multi-tenant by design.

Every tenant-scoped operation SHALL carry:

```text
organization_id
workspace_id
user_id
agent_id
workflow_id
execution_id
```

Tenant boundaries SHALL be enforced at:

* API layer.
* Service layer.
* Authorization layer.
* Data layer.
* Credential layer.
* MCP gateway.
* Audit layer.

---

## SR-MCP-002 — MCP Gateway

SalesGenie SHALL provide a dedicated MCP Gateway.

The MCP Gateway SHALL provide:

```text
Authentication
Authorization
Tool Discovery
Resource Discovery
Schema Validation
Policy Enforcement
Rate Limiting
Credential Isolation
Request Routing
Response Validation
Tracing
Metrics
Auditing
Circuit Breaking
```

---

## SR-MCP-003 — MCP Registry

The platform SHALL maintain an MCP Server Registry.

Example:

```yaml
MCPServer:
  server_id:
  organization_id:
  provider:
  name:
  description:
  version:
  protocol_version:
  endpoint:
  authentication_type:
  trust_level:
  status:
  health_status:
  capabilities:
  enabled:
  created_at:
  updated_at:
```

---

## SR-MCP-004 — MCP Tool Registry

The platform SHALL maintain a normalized tool registry.

```yaml
MCPTool:
  tool_id:
  server_id:
  name:
  description:
  version:
  input_schema:
  output_schema:
  risk_level:
  permissions:
  approval_policy:
  enabled:
  created_at:
  updated_at:
```

---

## SR-MCP-005 — Resource Registry

The platform SHALL maintain MCP resource metadata.

```yaml
MCPResource:
  resource_id:
  server_id:
  uri:
  name:
  description:
  mime_type:
  permissions:
  tenant_scope:
  enabled:
```

---

## SR-MCP-006 — Prompt Registry

The platform SHALL maintain MCP prompt metadata.

```yaml
MCPPrompt:
  prompt_id:
  server_id:
  name:
  description:
  arguments_schema:
  permissions:
  enabled:
```

---

## SR-MCP-007 — Capability Negotiation

The platform SHALL negotiate supported MCP capabilities between:

```text
SalesGenie MCP Gateway
        ↕
MCP Server
```

Unsupported capabilities SHALL be rejected gracefully.

---

## SR-MCP-008 — Authentication

The MCP platform SHALL support secure authentication mechanisms appropriate to the MCP server.

Credential handling SHALL remain server-side.

Credentials SHALL never be included in:

* AI prompts.
* AI context.
* Browser responses.
* Standard logs.
* Workflow definitions.

---

## SR-MCP-009 — Authorization

Every MCP request SHALL be authorized independently.

Authorization SHALL evaluate:

```text
Identity
Tenant
Role
Agent
Workflow
Server
Tool
Resource
Risk
Policy
Approval
Budget
Rate Limit
```

---

## SR-MCP-010 — Policy Engine

The platform SHALL provide a centralized MCP policy engine.

The policy engine SHALL support:

* Allow rules.
* Deny rules.
* Approval rules.
* Rate limits.
* Time restrictions.
* Data restrictions.
* Tool restrictions.
* Server restrictions.
* Agent restrictions.
* Tenant restrictions.
* Cost restrictions.

---

## SR-MCP-011 — Risk Classification

Every MCP capability SHALL have a configurable risk classification.

```text
READ_ONLY
LOW
MEDIUM
HIGH
CRITICAL
```

---

## SR-MCP-012 — Human Approval Policy

The platform SHALL support:

```text
No Approval
Conditional Approval
Mandatory Approval
Multi-Party Approval
```

Approval policies SHALL be configurable by:

* Server.
* Tool.
* Workflow.
* Agent.
* Role.
* Organization.
* Risk level.

---

## SR-MCP-013 — Execution Budget

The system SHALL support:

```text
Maximum MCP Calls
Maximum Workflow Steps
Maximum Execution Time
Maximum Payload Size
Maximum Result Size
Maximum Retry Count
Maximum AI Tokens
Maximum Cost
Maximum Concurrent Executions
```

---

## SR-MCP-014 — Rate Limiting

Rate limiting SHALL be configurable at:

```text
Platform
Tenant
User
Agent
Workflow
MCP Server
MCP Tool
External Integration
```

---

## SR-MCP-015 — Idempotency

All side-effecting operations SHALL support idempotency wherever technically possible.

The platform SHALL prevent accidental duplicate operations.

---

## SR-MCP-016 — Distributed Tracing

The platform SHALL provide distributed tracing across:

```text
Frontend
→ API Gateway
→ Workflow Engine
→ AI Agent
→ MCP Gateway
→ MCP Server
→ External Service
```

Required identifiers:

```text
request_id
trace_id
span_id
execution_id
tool_call_id
workflow_id
workflow_version
agent_id
organization_id
```

---

## SR-MCP-017 — Audit Logging

The platform SHALL create audit records for:

* Server registration.
* Server enablement.
* Server disablement.
* Tool discovery.
* Tool execution.
* Resource access.
* Permission changes.
* Policy changes.
* Approval requests.
* Approval decisions.
* Security failures.
* Configuration changes.

---

## SR-MCP-018 — Data Redaction

Sensitive data SHALL be automatically redacted from logs.

Examples:

```text
API Keys
OAuth Tokens
Passwords
Session Tokens
Authorization Headers
Payment Credentials
Sensitive Customer Data
```

---

## SR-MCP-019 — MCP Server Isolation

A compromised MCP server SHALL NOT be able to:

* Access another MCP server's credentials.
* Modify SalesGenie permissions.
* Access unrelated tenants.
* Modify audit records.
* Modify platform policies.
* Access unrestricted internal services.

---

## SR-MCP-020 — Sandboxing

Where technically appropriate, untrusted MCP integrations SHALL execute within isolated runtime boundaries.

Isolation SHALL minimize:

* Network exposure.
* Filesystem access.
* Credential access.
* Process privileges.
* Internal service access.

---

## 7. Functional Requirements

## 7.1 MCP Server Lifecycle

## FR-MCP-001 — Register Server

Authorized administrators SHALL be able to register MCP servers.

## FR-MCP-002 — Validate Server

The platform SHALL validate:

* Connectivity.
* Protocol compatibility.
* Authentication.
* Server metadata.
* Capabilities.

## FR-MCP-003 — Enable Server

Only approved servers SHALL be enabled for production use.

## FR-MCP-004 — Disable Server

Authorized administrators SHALL be able to disable servers immediately.

## FR-MCP-005 — Remove Server

The platform SHALL support controlled removal of MCP servers while preserving historical execution/audit records.

---

## 7.2 Discovery

## FR-MCP-006

The system SHALL discover MCP tools.

## FR-MCP-007

The system SHALL discover MCP resources.

## FR-MCP-008

The system SHALL discover MCP prompts.

## FR-MCP-009

The system SHALL synchronize MCP metadata when server capabilities change.

## FR-MCP-010

Removed tools SHALL no longer be executable.

---

## 7.3 MCP Tool Execution

## FR-MCP-011

The platform SHALL accept structured MCP tool requests.

## FR-MCP-012

The platform SHALL validate input schemas.

## FR-MCP-013

The platform SHALL authorize the request.

## FR-MCP-014

The platform SHALL execute the tool only after policy approval.

## FR-MCP-015

The platform SHALL validate tool results.

## FR-MCP-016

The platform SHALL record execution telemetry.

---

## 7.4 Human Execution

## FR-MCP-017

Humans SHALL be able to execute permitted MCP tools.

## FR-MCP-018

The UI SHALL display required permissions.

## FR-MCP-019

The UI SHALL display approval requirements.

## FR-MCP-020

The UI SHALL display expected external side effects where available.

---

## 7.5 AI Execution

## FR-MCP-021

AI Agents SHALL receive only authorized tools.

## FR-MCP-022

AI Agents SHALL generate structured tool calls.

## FR-MCP-023

The MCP Gateway SHALL independently validate AI-generated calls.

## FR-MCP-024

AI tool execution SHALL be bounded by workflow policy.

## FR-MCP-025

AI Agents SHALL receive structured tool results.

---

## 7.6 AI Tool Planning

The platform SHALL support AI planning:

```text
User Objective
      ↓
AI Planning
      ↓
Tool Selection
      ↓
Policy Evaluation
      ↓
Approval if Required
      ↓
Execution
      ↓
Validation
      ↓
Next Step
```

AI plans SHALL never constitute authorization.

---

## 7.7 Human Approval

## FR-MCP-026

The platform SHALL create approval requests for configured operations.

## FR-MCP-027

Approval requests SHALL include:

```text
Workflow
Agent
MCP Server
Tool
Action
Parameters
Risk
Expected Impact
Evidence
Requested By
Expiration
```

## FR-MCP-028

Approvers SHALL be able to:

```text
Approve
Reject
Modify
Request Information
Delegate
```

## FR-MCP-029

Approval decisions SHALL be immutable.

---

## 7.8 MCP Resource Access

## FR-MCP-030

The platform SHALL authorize every resource request.

## FR-MCP-031

Resources SHALL preserve provenance.

## FR-MCP-032

Resource content SHALL be treated as untrusted external data.

## FR-MCP-033

Sensitive resources SHALL support additional authorization requirements.

---

## 7.9 MCP Prompt Handling

## FR-MCP-034

The platform SHALL support authorized MCP prompts.

## FR-MCP-035

MCP prompt content SHALL NOT override SalesGenie system instructions.

## FR-MCP-036

MCP prompt injection SHALL be detected and mitigated where possible.

---

## 7.10 Prompt Injection Defense

The platform SHALL assume that:

```text
MCP Tool Description
MCP Resource
MCP Prompt
External API Response
External Document
CRM Record
Customer Message
```

may contain malicious or untrusted instructions.

The platform SHALL prevent such content from:

* Granting permissions.
* Changing policies.
* Executing unauthorized tools.
* Modifying system configuration.
* Disabling security controls.

---

## 7.11 Workflow Integration

The MCP platform SHALL integrate with the SalesGenie workflow engine.

Supported workflow patterns SHALL include:

```text
Sequential
Parallel
Conditional
Loop
Human Approval
AI Decision
Event Driven
Scheduled
Webhook Driven
Retry
Compensation
```

---

## 7.12 MCP Workflow Example — Lead Generation

```text
Trigger
  ↓
MCP Company Search
  ↓
MCP Contact Discovery
  ↓
MCP Lead Enrichment
  ↓
AI Lead Qualification
  ↓
AI Lead Scoring
  ↓
MCP CRM Create Lead
  ↓
Human Approval
  ↓
MCP Email/WhatsApp
  ↓
MCP CRM Activity Update
```

---

## 7.13 MCP Workflow Example — Customer Support

```text
New Ticket
  ↓
MCP Customer Lookup
  ↓
MCP Ticket History
  ↓
MCP Knowledge Retrieval
  ↓
AI Resolution
  ↓
Policy Evaluation
  ↓
┌─────────────────────┐
│ Low Risk            │
│ → Automatic Reply   │
└─────────────────────┘

OR

┌─────────────────────┐
│ High Risk           │
│ → Human Approval    │
└─────────────────────┘
  ↓
MCP Ticket Update
```

---

## 7.14 MCP + CRM

The platform SHALL support authorized operations such as:

```text
Search Contact
Create Contact
Update Contact
Search Lead
Create Lead
Update Lead
Search Opportunity
Create Task
Update Task
Add Activity
Retrieve Customer History
```

CRM mutations SHALL be:

* Authorized.
* Audited.
* Idempotent where possible.
* Tenant-scoped.

---

## 7.15 MCP + Lead Intelligence

The platform SHALL support:

```text
Company Search
Lead Discovery
Company Enrichment
Contact Enrichment
Decision Maker Discovery
Lead Qualification
Lead Scoring
Competitor Research
Market Research
CRM Synchronization
```

External information SHALL preserve source/provenance metadata.

---

## 7.16 MCP + RAG

MCP SHALL integrate with SalesGenie's RAG layer.

The system SHALL support:

```text
MCP Resource
     ↓
Document Retrieval
     ↓
Permission Filtering
     ↓
Chunk Retrieval
     ↓
AI Context
     ↓
Decision
```

RAG data SHALL remain tenant-isolated.

---

## 7.17 MCP + Omnichannel

The MCP platform SHALL support integrations with SalesGenie's supported communication channels.

Examples:

```text
Email
WhatsApp
Slack
Telegram
Discord
Website Chat
Voice
```

Channel-specific actions SHALL inherit MCP authorization policies.

---

## 7.18 MCP + n8n

The MCP platform SHALL interoperate with n8n workflows.

Supported patterns:

```text
n8n
 ↓
SalesGenie MCP Gateway
 ↓
MCP Tool
```

and:

```text
MCP Tool
 ↓
SalesGenie
 ↓
n8n Workflow
```

Authentication, authorization, tenant context, and tracing SHALL be preserved.

---

## 7.19 MCP + Scheduler

The platform SHALL support:

```text
Cron
Daily
Weekly
Monthly
Interval
One-Time
```

Scheduled executions SHALL run using explicit service identities.

Scheduled workflows SHALL NOT bypass approval policies.

---

## 7.20 Event-Driven MCP

The platform SHALL support triggers including:

```text
New Lead
New Customer
New Ticket
New Email
CRM Event
Webhook
Payment Event
MCP Event
System Event
```

Events SHALL support deduplication.

---

## 7.21 Error Handling

The platform SHALL classify MCP failures:

```text
AUTHENTICATION_ERROR
AUTHORIZATION_ERROR
VALIDATION_ERROR
SCHEMA_ERROR
TIMEOUT
RATE_LIMIT
NETWORK_ERROR
SERVER_ERROR
PROVIDER_UNAVAILABLE
POLICY_VIOLATION
BUDGET_EXCEEDED
UNKNOWN_ERROR
```

---

## 7.22 Retry System

Retry behavior SHALL support:

```text
Maximum Attempts
Exponential Backoff
Jitter
Retryable Error Classification
Non-Retryable Error Classification
Dead-Letter Routing
```

The system SHALL NOT retry irreversible operations blindly.

---

## 7.23 Circuit Breaker

The platform SHALL implement:

```text
CLOSED
  ↓
OPEN
  ↓
HALF_OPEN
  ↓
CLOSED
```

Circuit breakers SHALL be configurable per MCP server and optionally per tool.

---

## 7.24 Dead-Letter Queue

Failed executions exceeding retry limits SHALL be moved to a dead-letter queue.

Authorized operators SHALL be able to:

```text
Inspect
Retry
Replay
Cancel
Archive
```

---

## 7.25 Execution State Management

MCP executions SHALL support:

```text
CREATED
QUEUED
RUNNING
WAITING_APPROVAL
APPROVED
REJECTED
PAUSED
RESUMED
COMPLETED
FAILED
CANCELLED
TIMED_OUT
EXPIRED
```

Invalid state transitions SHALL be rejected.

---

## 8. MCP Platform Administration

## FR-MCP-ADMIN-001

Super Admin SHALL have a global MCP dashboard.

Dashboard SHALL display:

```text
Total MCP Servers
Active MCP Servers
Unhealthy Servers
Total Tools
Active Tools
Tool Calls
Success Rate
Failure Rate
Average Latency
P95 Latency
P99 Latency
Active Executions
Pending Approvals
Security Events
Estimated Cost
```

---

## FR-MCP-ADMIN-002

Organization Admin SHALL have organization-level MCP dashboards.

---

## FR-MCP-ADMIN-003

Administrators SHALL be able to inspect MCP configuration history.

---

## FR-MCP-ADMIN-004

Configuration changes SHALL be auditable.

---

## 9. MCP Security Requirements

## SEC-MCP-001

Every request SHALL be authenticated.

## SEC-MCP-002

Every request SHALL be authorized.

## SEC-MCP-003

Every sensitive operation SHALL be audited.

## SEC-MCP-004

Secrets SHALL never enter AI context.

## SEC-MCP-005

AI Agents SHALL never receive unrestricted credentials.

## SEC-MCP-006

MCP servers SHALL be treated as external trust boundaries.

## SEC-MCP-007

External MCP content SHALL be considered untrusted.

## SEC-MCP-008

Tenant boundaries SHALL be enforced server-side.

## SEC-MCP-009

Client-side authorization SHALL never be considered sufficient.

## SEC-MCP-010

Audit logs SHALL be protected from modification by AI Agents and normal users.

---

## 10. High-Risk MCP Operations

The following operations SHALL support mandatory human approval:

```text
DELETE_CUSTOMER
DELETE_LEAD
DELETE_DOCUMENT
EXPORT_CUSTOMER_DATA
EXPORT_ORGANIZATION_DATA
SEND_BULK_EMAIL
SEND_BULK_WHATSAPP
SEND_BULK_MESSAGES
REFUND_PAYMENT
MODIFY_BILLING
CREATE_ADMIN
CHANGE_USER_ROLE
CHANGE_SECURITY_POLICY
DISABLE_SECURITY_CONTROL
MODIFY_PRODUCTION_CONFIGURATION
MASS_CRM_UPDATE
MASS_DATA_DELETE
```

Organizations SHALL be able to extend this list.

---

## 11. AI Governance

## AI-MCP-001

AI autonomy SHALL be explicitly configured.

Supported autonomy modes:

```text
READ_ONLY
ASSISTED
SUPERVISED
CONTROLLED_AUTONOMOUS
```

---

## AI-MCP-002

AI Agents SHALL operate only within delegated authority.

---

## AI-MCP-003

AI Agents SHALL stop execution when authority is exceeded.

---

## AI-MCP-004

AI Agents SHALL request approval when required.

---

## AI-MCP-005

AI Agents SHALL escalate ambiguous operations.

---

## AI-MCP-006

AI Agents SHALL not infer authorization from:

* User intent alone.
* Tool availability.
* Previous approvals.
* Previous successful executions.
* Prompt instructions.

---

## 12. Human Governance

## HUMAN-MCP-001

Humans SHALL retain control over configured high-impact operations.

## HUMAN-MCP-002

Human approvals SHALL have configurable expiration.

## HUMAN-MCP-003

Expired approvals SHALL not authorize execution.

## HUMAN-MCP-004

Human overrides SHALL be audited.

## HUMAN-MCP-005

Approval policies SHALL be evaluated at execution time.

---

## 13. MCP Permissions

The platform SHALL support granular permissions.

Example:

```text
mcp.server.read
mcp.server.manage
mcp.tool.discover
mcp.tool.execute
mcp.resource.read
mcp.prompt.execute
mcp.workflow.create
mcp.workflow.execute
mcp.workflow.cancel
mcp.approval.review
mcp.policy.manage
mcp.audit.read
mcp.metrics.read
mcp.credentials.manage
```

Permissions SHALL be assignable through RBAC and policy controls.

---

## 14. Data Model

Core entities SHALL include:

```text
MCPServer
MCPServerVersion
MCPServerHealth
MCPTool
MCPToolVersion
MCPResource
MCPPrompt
MCPCapability
MCPPermission
MCPPolicy
MCPCredentialReference
MCPWorkflow
MCPWorkflowVersion
MCPWorkflowExecution
MCPToolExecution
MCPApproval
MCPAuditEvent
MCPUsageRecord
MCPRateLimit
MCPBudget
MCPDeadLetterJob
MCPCircuitBreaker
MCPEvent
```

---

## 15. MCP Server State Machine

```text
REGISTERED
    ↓
VALIDATING
    ↓
APPROVED
    ↓
ENABLED
    ↓
HEALTHY
```

Alternative states:

```text
REJECTED
DISABLED
UNHEALTHY
MAINTENANCE
DECOMMISSIONED
```

---

## 16. MCP Tool State Machine

```text
DISCOVERED
    ↓
VALIDATED
    ↓
AUTHORIZED
    ↓
ENABLED
```

Alternative states:

```text
DISABLED
BLOCKED
DEPRECATED
REMOVED
```

---

## 17. Observability

The platform SHALL expose:

## Infrastructure Metrics

```text
MCP Server Availability
Server Latency
Server Error Rate
Connection Failures
Authentication Failures
```

## Tool Metrics

```text
Tool Calls
Successful Calls
Failed Calls
Timeouts
Retries
Average Latency
P95 Latency
P99 Latency
```

## AI Metrics

```text
AI Tool Calls
AI Tool Selection
Approval Requests
Approval Rate
Rejection Rate
Escalation Rate
```

## Business Metrics

```text
Leads Processed
Customers Processed
Tickets Processed
CRM Actions
Messages Sent
Workflow Completion
```

---

## 18. MCP Cost Management

The platform SHALL track:

```text
MCP Calls
External API Calls
AI Tokens
Workflow Executions
Tool Usage
Tenant Usage
Agent Usage
```

Cost SHALL be attributable to:

```text
organization_id
user_id
agent_id
workflow_id
execution_id
mcp_server_id
tool_id
```

---

## 19. MCP Usage Quotas

Organizations SHALL be able to define:

```yaml
quota:
  max_daily_calls:
  max_monthly_calls:
  max_concurrent_executions:
  max_execution_cost:
  max_tool_calls_per_workflow:
  max_external_api_calls:
```

Quota exhaustion SHALL trigger configurable behavior:

```text
STOP
QUEUE
DEGRADE
REQUIRE_ADMIN_APPROVAL
```

---

## 20. MCP Marketplace Governance

Before an MCP server becomes organization-available:

```text
Submission
   ↓
Metadata Validation
   ↓
Security Review
   ↓
Capability Review
   ↓
Permission Review
   ↓
Risk Classification
   ↓
Approval
   ↓
Publication
```

The marketplace SHALL distinguish:

```text
Trusted
Verified
Organization Approved
Unverified
Blocked
Deprecated
```

---

## 21. MCP Versioning

The platform SHALL support:

* MCP protocol compatibility.
* Server versions.
* Tool versions.
* Workflow versions.
* Backward compatibility.
* Deprecation policies.

A workflow execution SHALL reference the exact workflow and MCP tool/server version used at execution time.

---

## 22. MCP Configuration Management

Configuration changes SHALL support:

```text
Draft
Review
Approval
Publish
Rollback
```

Production configuration SHALL not be modified silently.

---

## 23. Emergency Controls

Super Admin SHALL have emergency controls for:

```text
Disable All MCP
Disable Tenant MCP
Disable MCP Server
Disable MCP Tool
Disable AI MCP Execution
Disable Human MCP Execution
Cancel Active Executions
Block External Side Effects
```

Emergency actions SHALL generate critical audit events.

---

## 24. Reliability Requirements

The MCP platform SHALL provide:

* Horizontal scaling.
* Worker recovery.
* Queue persistence.
* Retry handling.
* Circuit breakers.
* Dead-letter queues.
* Idempotency.
* Execution recovery.
* Graceful degradation.
* Provider failure isolation.

---

## 25. Scalability Requirements

The architecture SHALL support:

```text
Multiple MCP Servers
Thousands of MCP Tools
Large Tool Catalogs
Large Tenant Counts
High Workflow Throughput
High Concurrent AI Agents
High Concurrent MCP Executions
```

The platform SHALL scale horizontally without requiring changes to workflow definitions.

---

## 26. Performance Requirements

The platform SHALL measure:

```text
API Latency
MCP Gateway Latency
Tool Discovery Latency
Tool Execution Latency
Queue Latency
Workflow Latency
Approval Latency
```

Performance targets SHALL be configurable by deployment tier.

---

## 27. Availability Requirements

MCP platform availability SHALL be independently monitored from external MCP provider availability.

A provider outage SHALL not be interpreted as a SalesGenie platform outage.

The platform SHALL provide graceful failure behavior.

---

## 28. API Requirements

The MCP subsystem SHALL expose APIs conceptually equivalent to:

```text
POST   /api/v1/mcp/servers
GET    /api/v1/mcp/servers
GET    /api/v1/mcp/servers/{server_id}
PATCH  /api/v1/mcp/servers/{server_id}
DELETE /api/v1/mcp/servers/{server_id}

POST   /api/v1/mcp/servers/{server_id}/validate
POST   /api/v1/mcp/servers/{server_id}/enable
POST   /api/v1/mcp/servers/{server_id}/disable

GET    /api/v1/mcp/tools
GET    /api/v1/mcp/tools/{tool_id}
POST   /api/v1/mcp/tools/{tool_id}/execute

GET    /api/v1/mcp/resources
GET    /api/v1/mcp/resources/{resource_id}

GET    /api/v1/mcp/prompts
POST   /api/v1/mcp/prompts/{prompt_id}/execute

POST   /api/v1/mcp/workflows
GET    /api/v1/mcp/workflows
GET    /api/v1/mcp/workflows/{workflow_id}
PATCH  /api/v1/mcp/workflows/{workflow_id}

POST   /api/v1/mcp/workflows/{workflow_id}/execute

GET    /api/v1/mcp/executions
GET    /api/v1/mcp/executions/{execution_id}
POST   /api/v1/mcp/executions/{execution_id}/cancel
POST   /api/v1/mcp/executions/{execution_id}/retry

GET    /api/v1/mcp/approvals
POST   /api/v1/mcp/approvals/{approval_id}/approve
POST   /api/v1/mcp/approvals/{approval_id}/reject

GET    /api/v1/mcp/metrics
GET    /api/v1/mcp/health
GET    /api/v1/mcp/audit
```

Actual API paths SHALL remain consistent with SalesGenie's established API architecture.

---

## 29. Event Architecture

The MCP platform SHALL emit events including:

```text
MCP_SERVER_REGISTERED
MCP_SERVER_APPROVED
MCP_SERVER_ENABLED
MCP_SERVER_DISABLED
MCP_SERVER_UNHEALTHY
MCP_SERVER_RECOVERED

MCP_TOOL_DISCOVERED
MCP_TOOL_UPDATED
MCP_TOOL_DISABLED
MCP_TOOL_DEPRECATED

MCP_RESOURCE_DISCOVERED
MCP_PROMPT_DISCOVERED

MCP_EXECUTION_CREATED
MCP_EXECUTION_STARTED
MCP_EXECUTION_COMPLETED
MCP_EXECUTION_FAILED
MCP_EXECUTION_CANCELLED
MCP_EXECUTION_TIMED_OUT

MCP_APPROVAL_REQUESTED
MCP_APPROVAL_APPROVED
MCP_APPROVAL_REJECTED
MCP_APPROVAL_EXPIRED

MCP_POLICY_ALLOWED
MCP_POLICY_DENIED
MCP_POLICY_VIOLATED

MCP_RATE_LIMITED
MCP_BUDGET_EXCEEDED

MCP_CIRCUIT_OPENED
MCP_CIRCUIT_CLOSED

MCP_SECURITY_EVENT
MCP_EMERGENCY_DISABLED
```

---

## 30. Reference AI + Human Architecture

```text
                         ┌──────────────────┐
                         │ Human User       │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ SalesGenie UI    │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ API Gateway      │
                         └────────┬─────────┘
                                  │
                ┌─────────────────┴─────────────────┐
                │                                   │
                ▼                                   ▼
      ┌──────────────────┐                ┌──────────────────┐
      │ Workflow Engine  │                │ AI Agent Runtime │
      └────────┬─────────┘                └────────┬─────────┘
               │                                   │
               └─────────────────┬─────────────────┘
                                 ▼
                    ┌────────────────────────┐
                    │ MCP Policy Engine      │
                    └────────────┬───────────┘
                                 │
                    ┌────────────┼─────────────┐
                    │            │             │
                    ▼            ▼             ▼
                 ALLOW       APPROVAL        DENY
                    │            │
                    │            ▼
                    │     ┌───────────────┐
                    │     │ Human Review  │
                    │     └───────┬───────┘
                    │             │
                    │        APPROVE
                    │             │
                    └─────────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │ MCP Gateway             │
                    └────────────┬───────────┘
                                 │
               ┌─────────────────┼─────────────────┐
               │                 │                 │
               ▼                 ▼                 ▼
        ┌────────────┐    ┌────────────┐    ┌────────────┐
        │ MCP Server │    │ MCP Server │    │ MCP Server │
        │ CRM        │    │ Research   │    │ Support    │
        └─────┬──────┘    └─────┬──────┘    └─────┬──────┘
              │                 │                 │
              ▼                 ▼                 ▼
          Salesforce        Web/Data          Zendesk
```

---

## 31. Example Enterprise AI Workflow

```text
USER:
"Find enterprise SaaS companies with high buying intent and prepare
personalized outreach."

        ↓

AI SALES AGENT
        ↓
Create Execution Plan
        ↓
Policy Engine
        ↓
MCP Company Search
        ↓
MCP Lead Intelligence
        ↓
MCP Contact Enrichment
        ↓
AI Qualification
        ↓
AI Lead Scoring
        ↓
MCP CRM Create/Update
        ↓
AI Message Generation
        ↓
Risk Evaluation
        ↓
HIGH RISK
        ↓
Human Approval
        ↓
APPROVED
        ↓
MCP Email/WhatsApp
        ↓
MCP CRM Activity Update
        ↓
Execution Completed
        ↓
Audit + Metrics + Cost
```

---

## 32. Example Human-Controlled Workflow

```text
Sales Agent
    ↓
Select MCP Tool
    ↓
Enter Parameters
    ↓
Client Validation
    ↓
Server Authorization
    ↓
Policy Evaluation
    ↓
Risk Check
    ↓
MCP Execution
    ↓
Result Validation
    ↓
Audit
    ↓
Result Display
```

---

## 33. Example Autonomous AI Workflow

```text
Event
  ↓
AI Agent
  ↓
Authorized Tool Discovery
  ↓
AI Tool Selection
  ↓
Policy Engine
  ↓
LOW RISK
  ↓
MCP Gateway
  ↓
MCP Tool
  ↓
Result Validation
  ↓
AI Interpretation
  ↓
Next Tool
  ↓
Completion
```

The AI SHALL NOT execute a tool merely because it selected the tool.

Authorization SHALL always occur after tool selection and before execution.

---

## 34. Security Threat Model

The MCP platform SHALL defend against:

```text
Prompt Injection
Indirect Prompt Injection
Tool Injection
Malicious Tool Descriptions
Malicious MCP Servers
Credential Theft
Privilege Escalation
Cross-Tenant Access
Data Exfiltration
Replay Attacks
Duplicate Side Effects
Unauthorized Tool Calls
Rate-Limit Abuse
Runaway AI Agents
Infinite Workflow Loops
Malicious External Responses
Supply-Chain Risk
Configuration Tampering
Audit Log Tampering
```

---

## 35. Security Response

When a serious MCP security event occurs, the platform SHALL support:

```text
Detect
 ↓
Classify
 ↓
Alert
 ↓
Block
 ↓
Isolate
 ↓
Audit
 ↓
Investigate
 ↓
Recover
```

---

## 36. Testing Requirements

## Unit Testing

The platform SHALL test:

* Authorization.
* Policy evaluation.
* Schema validation.
* Risk classification.
* Rate limiting.
* Budget enforcement.
* Idempotency.
* Retry logic.
* State transitions.

## Integration Testing

The platform SHALL test:

* MCP server registration.
* Capability discovery.
* Tool execution.
* Resource access.
* Prompt execution.
* Workflow execution.
* Human approval.
* Credential management.

## Security Testing

The platform SHALL test:

* Tenant isolation.
* Privilege escalation.
* Prompt injection.
* Tool injection.
* Credential leakage.
* Unauthorized access.
* Policy bypass.
* Replay attacks.
* Malicious MCP servers.

## Reliability Testing

The platform SHALL test:

* Server outages.
* Network failures.
* Worker crashes.
* Queue failures.
* Rate limiting.
* Timeouts.
* Duplicate events.
* Duplicate requests.
* Provider degradation.

---

## 37. Non-Functional Requirements

## NFR-MCP-SEC-001

All MCP communication SHALL use secure transport.

## NFR-MCP-SEC-002

Secrets SHALL be encrypted at rest and protected in transit.

## NFR-MCP-SEC-003

MCP credentials SHALL be isolated from AI model context.

## NFR-MCP-SEC-004

Security-sensitive events SHALL be auditable.

---

## NFR-MCP-REL-001

The platform SHALL support failure recovery without losing valid workflow state.

## NFR-MCP-REL-002

External provider failures SHALL be isolated.

## NFR-MCP-REL-003

Side-effecting operations SHALL avoid duplicate execution.

---

## NFR-MCP-SCALE-001

MCP workers SHALL scale horizontally.

## NFR-MCP-SCALE-002

The platform SHALL support queue-based workload distribution.

## NFR-MCP-SCALE-003

The platform SHALL enforce tenant-aware workload controls.

---

## NFR-MCP-OBS-001

All MCP executions SHALL be traceable.

## NFR-MCP-OBS-002

All major MCP metrics SHALL be measurable.

## NFR-MCP-OBS-003

All security decisions SHALL be observable.

---

## 38. Production Readiness Checklist

## Platform

* [ ] MCP Gateway implemented.
* [ ] MCP Server Registry implemented.
* [ ] MCP Tool Registry implemented.
* [ ] MCP Resource Registry implemented.
* [ ] MCP Prompt Registry implemented.
* [ ] MCP Policy Engine implemented.
* [ ] MCP Authorization Engine implemented.
* [ ] MCP Credential Isolation implemented.
* [ ] MCP Health Monitoring implemented.
* [ ] MCP Audit System implemented.

## AI

* [ ] AI tool discovery implemented.
* [ ] AI tool authorization implemented.
* [ ] AI tool execution implemented.
* [ ] AI-human approval implemented.
* [ ] AI escalation implemented.
* [ ] AI execution budgets implemented.
* [ ] AI tool-call validation implemented.
* [ ] Prompt-injection defenses implemented.

## Human

* [ ] Human tool execution implemented.
* [ ] Human approval UI implemented.
* [ ] Human rejection implemented.
* [ ] Human override auditing implemented.
* [ ] Human cancellation implemented.

## Reliability

* [ ] Retry system implemented.
* [ ] Circuit breakers implemented.
* [ ] Dead-letter queues implemented.
* [ ] Idempotency implemented.
* [ ] Execution recovery implemented.
* [ ] Timeout handling implemented.

## Security

* [ ] RBAC implemented.
* [ ] Tenant isolation tested.
* [ ] Credential isolation tested.
* [ ] Cross-tenant access tests passed.
* [ ] Privilege escalation tests passed.
* [ ] Prompt injection tests passed.
* [ ] Tool injection tests passed.
* [ ] Audit integrity verified.

## Operations

* [ ] MCP dashboards implemented.
* [ ] MCP alerts implemented.
* [ ] Cost tracking implemented.
* [ ] Usage quotas implemented.
* [ ] Emergency shutdown implemented.
* [ ] Configuration rollback implemented.
* [ ] Server health monitoring implemented.

---

## 39. Golden Rules

1. **MCP availability SHALL never imply authorization.**
2. **AI tool selection SHALL never imply permission.**
3. **Every tool call SHALL be independently authorized.**
4. **Every external side effect SHALL be policy controlled.**
5. **High-risk actions SHALL support human approval.**
6. **No credentials SHALL enter AI model context.**
7. **External MCP content SHALL be treated as untrusted.**
8. **Every tool request SHALL be schema validated.**
9. **Every tool response SHALL be validated before AI consumption.**
10. **Every execution SHALL have a unique execution ID.**
11. **Every execution SHALL be traceable.**
12. **Every security-sensitive action SHALL be auditable.**
13. **AI Agents SHALL never grant themselves permissions.**
14. **AI Agents SHALL never modify security policies.**
15. **Human users SHALL not bypass server-side authorization.**
16. **Tenant isolation SHALL be enforced independently of UI controls.**
17. **Retries SHALL never blindly repeat irreversible side effects.**
18. **Workflow executions SHALL remain bounded.**
19. **MCP failures SHALL not silently become successful operations.**
20. **Emergency MCP shutdown SHALL always be available to authorized administrators.**
21. **The MCP platform SHALL be independently observable from external MCP providers.**
22. **The platform SHALL preserve complete execution provenance.**
23. **Policy evaluation SHALL occur at runtime, not only during workflow creation.**
24. **Approval decisions SHALL not be inferred from historical approvals.**
25. **MCP governance SHALL apply equally to AI-initiated and human-initiated operations.**
