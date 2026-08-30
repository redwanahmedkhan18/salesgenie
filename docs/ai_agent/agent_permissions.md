# SalesGenie — FAANG-Level Agent Permissions Requirements Specification

**Document:** `agent_permissions.md`
**Project:** SalesGenie
**Capability:** AI Agent Permissions, Human Agent Permissions, Authorization, RBAC, ABAC, Delegation, Approval, and Policy Enforcement
**Version:** 1.0
**Status:** Production-Grade Requirements Specification

---

## 1. Purpose

The Agent Permissions subsystem defines how SalesGenie controls what AI agents and human users are allowed to **see, access, modify, execute, delegate, approve, and automate**.

The subsystem must provide fine-grained, tenant-isolated, policy-driven authorization across:

* AI agents
* human support agents
* sales agents
* administrators
* workflows
* tools
* integrations
* knowledge bases
* conversations
* customers
* leads
* CRM records
* reports
* files
* analytics
* billing
* communications
* MCP tools
* APIs
* background jobs
* automation workflows

SalesGenie's authorization model must enforce least privilege at the **organization, user, role, agent, workflow, tool, operation, resource, and data level**. This is consistent with the platform's production audit requirements, which explicitly require least-privilege permissions per agent, organization, user, workflow, and tool.

---

## 2. Authorization Principle

The core security invariant shall be:

```text
Authentication
    ↓
Tenant Resolution
    ↓
Identity Resolution
    ↓
Role Resolution
    ↓
Permission Resolution
    ↓
Resource Ownership Check
    ↓
Policy Evaluation
    ↓
Risk Evaluation
    ↓
Approval Evaluation
    ↓
Allow / Deny
```

The system shall never treat:

```text
AI intent
```

as equivalent to:

```text
authorization
```

The AI model must not be capable of granting itself permissions, selecting unauthorized capabilities, crossing tenants, or accessing secrets.

---

## 3. Scope

The Agent Permissions subsystem shall govern:

```text
User Permissions
Role Permissions
Agent Permissions
Tool Permissions
Workflow Permissions
Resource Permissions
Data Permissions
Integration Permissions
API Permissions
MCP Permissions
Approval Permissions
Delegation Permissions
Administrative Permissions
Security Permissions
Audit Permissions
```

---

## 4. Target Users

The authorization subsystem shall support at minimum:

| Actor               | Description                              |
| ------------------- | ---------------------------------------- |
| Super Admin         | Platform-wide administrator              |
| Organization Admin  | Organization administrator               |
| Security Admin      | Security and authorization administrator |
| AI Architect        | AI/agent architecture administrator      |
| Agent Manager       | Manages AI agents                        |
| Sales Manager       | Manages sales operations                 |
| Sales Agent         | Performs sales operations                |
| Support Manager     | Manages support teams                    |
| Human Support Agent | Handles customer support                 |
| Marketing Manager   | Manages marketing                        |
| Analyst             | Reads analytics and reports              |
| Knowledge Manager   | Manages organizational knowledge         |
| Finance/Admin       | Handles financial workflows              |
| Auditor             | Read-only governance                     |
| Developer           | Builds integrations and tools            |
| End User            | Interacts with permitted AI agents       |
| AI Agent            | Autonomous/semi-autonomous system actor  |

---

## 5. User Requirements

## UR-001 — Permission Visibility

Authorized users shall be able to view permissions assigned to:

* themselves
* their role
* their organization
* assigned AI agents
* assigned workflows
* assigned tools

Users shall not be able to inspect sensitive authorization information they are not permitted to view.

---

## UR-002 — Permission Management

Authorized administrators shall be able to:

* grant permissions
* revoke permissions
* assign roles
* remove roles
* configure agent permissions
* configure workflow permissions
* configure tool permissions
* define permission policies
* configure approval requirements
* configure delegation policies

---

## UR-003 — AI Agent Permission Management

Authorized users shall be able to define exactly what each AI agent can do.

For every agent, administrators shall be able to configure:

* readable resources
* writable resources
* executable tools
* allowed workflows
* accessible knowledge bases
* communication channels
* external integrations
* allowed operations
* approval requirements
* execution limits
* data scopes

The platform's agent model already treats permissions and tools as explicit agent configuration concepts; this subsystem shall formalize those controls as enforceable authorization policies.

---

## UR-004 — Human Agent Permission Management

Support and sales managers shall be able to configure permissions for human agents based on:

* role
* team
* organization
* department
* location where applicable
* assigned queues
* customer segments
* channels
* resource ownership

---

## UR-005 — Permission Search

Administrators shall be able to search permissions by:

* permission ID
* permission name
* category
* role
* user
* agent
* workflow
* tool
* resource
* organization

---

## UR-006 — Permission Groups

Administrators shall be able to create reusable permission groups.

Examples:

```text
Support Agent
Support Manager
Sales Agent
Sales Manager
Marketing Analyst
Knowledge Manager
Finance Operator
AI Support Agent
AI Sales Agent
AI Research Agent
Executive Agent
Auditor
```

---

## UR-007 — Permission Preview

Before granting permissions, administrators shall be able to preview the effective authorization.

Example:

```text
Agent:
AI Support Agent

Can:
✓ Read customer profiles
✓ Read conversations
✓ Search knowledge
✓ Create tickets
✓ Update tickets

Cannot:
✗ Delete customers
✗ Export customer database
✗ Modify billing
✗ Change permissions
✗ Access another organization
```

---

## UR-008 — Effective Permissions

Users shall be able to inspect effective permissions resulting from:

```text
Direct Permissions
+
Role Permissions
+
Organization Policies
+
Agent Policies
+
Workflow Policies
+
Resource Policies
-
Explicit Denials
```

---

## UR-009 — Permission Explanation

Authorized administrators shall be able to determine why an action was allowed or denied.

Example:

```text
Decision:
DENY

Actor:
support_ai_agent

Action:
customer.delete

Reason:
Agent policy does not contain customer:delete.
```

---

## UR-010 — Temporary Permissions

Authorized administrators shall be able to grant temporary permissions.

Temporary permissions shall support:

* start time
* expiration time
* scope
* reason
* approver
* target resource

---

## UR-011 — Emergency Revocation

Administrators shall be able to immediately revoke permissions from:

* users
* AI agents
* workflows
* tools
* integrations
* organizations

---

## UR-012 — Permission Audit

Authorized users shall be able to view:

* who granted permission
* who revoked permission
* previous value
* new value
* reason
* timestamp
* affected user/agent
* affected organization
* approval information

---

## 6. System Requirements

## SR-001 — Central Authorization Service

SalesGenie shall provide a centralized authorization service responsible for permission decisions.

All sensitive backend services shall use the authorization service rather than independently implementing inconsistent permission logic.

---

## SR-002 — Server-Side Enforcement

Authorization shall always be enforced server-side.

Frontend permission checks shall only improve UX.

They shall never be considered security controls.

This requirement aligns with the platform audit requirement that protected endpoints must enforce authorization and must not rely on frontend restrictions.

---

## SR-003 — Multi-Tenant Isolation

Every permission decision shall include tenant context.

Minimum authorization context:

```text
tenant_id
organization_id
user_id
agent_id
role_ids
team_id
workflow_id
tool_id
resource_type
resource_id
operation
```

The system shall reject requests where tenant context is missing or inconsistent.

---

## SR-004 — Deny by Default

Unknown or undefined permissions shall result in:

```text
DENY
```

The platform shall never interpret missing permission configuration as permission to execute.

---

## SR-005 — Least Privilege

Every actor shall receive only the minimum permissions required to perform its assigned function.

Least privilege shall apply independently to:

```text
Organization
User
Role
Agent
Workflow
Tool
Integration
Resource
Operation
```

---

## SR-006 — Explicit Permission Model

Permissions shall be represented as structured identifiers.

Recommended format:

```text
<domain>:<resource>:<action>
```

Examples:

```text
customer:read
customer:update
customer:delete

conversation:read
conversation:write
conversation:assign

ticket:read
ticket:create
ticket:update
ticket:assign
ticket:delete

lead:read
lead:update
lead:delete

knowledge:read
knowledge:write
knowledge:delete

agent:read
agent:create
agent:update
agent:execute
agent:delete

tool:read
tool:execute
tool:approve

workflow:read
workflow:create
workflow:execute
workflow:delete

analytics:read
billing:read
billing:manage

audit:read
organization:manage
user:manage
permission:manage
```

---

## 7. Permission Domains

SalesGenie shall support permission domains including:

```text
identity
organization
user
role
permission
agent
agent_memory
agent_tool
workflow
conversation
customer
contact
lead
company
ticket
support
knowledge
document
file
analytics
sales
marketing
advertising
seo
finance
billing
communication
email
whatsapp
telegram
messenger
sms
voice
webchat
crm
integration
mcp
report
dashboard
audit
security
system
```

---

## 8. Permission Actions

The platform shall support standardized actions:

```text
read
list
search
create
write
update
edit
delete
execute
approve
reject
assign
unassign
export
import
share
publish
unpublish
configure
manage
admin
audit
impersonate
delegate
revoke
```

Not every resource must support every action.

---

## 9. RBAC Requirements

## SR-007 — Role-Based Access Control

SalesGenie shall support RBAC.

Roles shall map to reusable permission sets.

Example:

```text
support_agent
    ↓
ticket:read
ticket:create
ticket:update
conversation:read
conversation:write
knowledge:read
agent:execute
```

---

## SR-008 — Role Hierarchy

The platform may support hierarchical roles.

Example:

```text
Support Agent
      ↓
Support Senior Agent
      ↓
Support Manager
      ↓
Organization Admin
      ↓
Super Admin
```

Higher-level roles shall not automatically receive unrestricted access to every resource unless explicitly configured.

---

## SR-009 — Custom Roles

Organization administrators shall be able to create custom roles.

---

## SR-010 — Role Versioning

Role changes shall be versioned and auditable.

---

## 10. ABAC Requirements

RBAC alone shall not be sufficient for enterprise authorization.

SalesGenie shall support attribute-based access control.

Authorization may depend on:

```text
user attributes
role
department
team
organization
tenant
agent type
resource owner
resource sensitivity
customer segment
workflow
channel
environment
time
IP/risk context
approval status
data classification
```

---

## Example

```text
support_agent
+
customer.organization_id == agent.organization_id
+
ticket.assigned_team == agent.team
=
ALLOW
```

Otherwise:

```text
DENY
```

---

## 11. Resource-Level Permissions

## SR-011

Permissions shall be evaluated at the resource level.

Example:

```text
customer:read
```

does not automatically mean:

```text
all_customers:read
```

The system shall additionally validate ownership and resource scope.

---

## SR-012 — Ownership Enforcement

The platform shall verify:

```text
resource.tenant_id
resource.organization_id
resource.owner_id
resource.team_id
```

where applicable.

The database layer must consistently enforce organization/workspace ownership on tenant-scoped data.

---

## 12. AI Agent Permissions

## SR-013 — Explicit AI Permission Set

Every AI agent shall have an explicit permission profile.

Example:

```json
{
  "agent_id": "support-agent-001",
  "permissions": [
    "customer:read",
    "conversation:read",
    "conversation:write",
    "ticket:read",
    "ticket:create",
    "ticket:update",
    "knowledge:read",
    "agent:execute"
  ]
}
```

---

## SR-014 — AI Permission Allowlist

AI agents shall operate from an allowlist of permitted capabilities.

The model shall only receive tools and capabilities that have passed authorization filtering.

---

## SR-015 — AI Cannot Self-Elevate

AI agents shall not be able to:

* grant themselves permissions
* modify their own roles
* modify their own policies
* approve their own high-risk actions
* access administrator credentials
* bypass approval
* change tenant identity

---

## SR-016 — AI Permission Boundaries

An AI agent may only act within:

```text
Agent Permissions
∩
User Permissions
∩
Organization Permissions
∩
Workflow Permissions
∩
Tool Permissions
∩
Resource Permissions
```

The effective permission shall be the intersection of applicable authorization boundaries.

---

## 13. Human Agent Permissions

Human agents shall receive permissions based on:

```text
Role
+
Team
+
Organization
+
Resource Assignment
+
Policy
```

Example:

```text
Human Support Agent

ALLOW:
customer:read
conversation:read
conversation:write
ticket:read
ticket:create
ticket:update
knowledge:read

DENY:
customer:delete
billing:manage
permission:manage
security:manage
organization:delete
```

---

## 14. Hybrid AI + Human Authorization

## SR-017

When AI operates on behalf of a human user, the platform shall evaluate both:

```text
AI Agent Permissions
```

and:

```text
Human User Permissions
```

The AI shall never inherit privileges that the initiating human does not possess.

---

## SR-018 — Delegated Authorization

A human may explicitly delegate selected permissions to an AI agent.

Delegation shall define:

```text
delegator
delegate
permissions
resources
purpose
start_time
expiration_time
approval
constraints
```

---

## SR-019 — Delegation Restrictions

Delegated permissions shall not exceed the delegator's effective permissions.

---

## 15. Tool Permissions

Every tool shall have explicit permissions.

Example:

```text
tool:
crm.create_customer

required_permission:
customer:create
```

An agent may call the tool only when:

```text
agent permission
AND
user permission
AND
organization policy
AND
tool permission
```

all permit execution.

---

## 16. Workflow Permissions

Workflows shall have explicit permission boundaries.

A workflow shall declare:

```text
allowed_agents
allowed_users
allowed_tools
allowed_operations
allowed_resources
```

AI agents shall not use workflows outside their authorization scope.

---

## 17. MCP Permissions

MCP servers and MCP tools shall require explicit authorization.

The system shall map:

```text
MCP Server
    ↓
MCP Tool
    ↓
SalesGenie Permission
    ↓
Agent Permission
    ↓
User Permission
```

MCP documentation shall explicitly describe tools, permissions, schemas, and approval policies.

---

## 18. Functional Requirements

## FR-001 — Create Permission

Authorized administrators shall be able to create a permission definition.

Required fields:

```text
permission_id
name
description
domain
resource
action
risk_level
scope
```

---

## FR-002 — Assign Permission to Role

The system shall allow authorized administrators to assign permissions to roles.

---

## FR-003 — Assign Permission to User

The system shall support direct user permissions where organizational policy permits.

---

## FR-004 — Assign Permission to AI Agent

The system shall support direct agent permission assignments.

---

## FR-005 — Revoke Permission

Authorized administrators shall be able to revoke permissions immediately.

---

## FR-006 — Permission Check API

The system shall expose a centralized authorization decision interface.

Example:

```http
POST /api/v1/authorization/check
```

Request:

```json
{
  "actor_type": "ai_agent",
  "actor_id": "support-agent-001",
  "action": "ticket:update",
  "resource_type": "ticket",
  "resource_id": "ticket-123"
}
```

Response:

```json
{
  "decision": "allow",
  "reason_code": "ROLE_AND_RESOURCE_SCOPE_MATCH"
}
```

---

## 19. Effective Permission Calculation

## FR-007

The system shall calculate effective permissions from all applicable authorization sources.

Example:

```text
User Permissions
+
Role Permissions
+
Organization Policies
+
Agent Permissions
+
Workflow Permissions
+
Tool Permissions
+
Resource Scope
+
Temporary Delegation
-
Explicit Denials
```

---

## FR-008 — Permission Precedence

Recommended precedence:

```text
Explicit DENY
    >
Security Policy
    >
Organization Policy
    >
Resource Policy
    >
Agent Policy
    >
Workflow Policy
    >
Role Permission
    >
Direct Permission
```

A restrictive policy shall override a permissive lower-level configuration.

---

## 20. Permission Evaluation

## FR-009

Every protected operation shall evaluate:

```text
WHO?
WHAT?
WHERE?
ON WHICH RESOURCE?
FOR WHICH ORGANIZATION?
UNDER WHICH AGENT?
THROUGH WHICH WORKFLOW?
USING WHICH TOOL?
UNDER WHICH POLICY?
```

---

## 21. Permission Decision Codes

The system shall provide deterministic decision codes.

Examples:

```text
ALLOW
DENY_NO_PERMISSION
DENY_TENANT_MISMATCH
DENY_RESOURCE_SCOPE
DENY_AGENT_POLICY
DENY_WORKFLOW_POLICY
DENY_TOOL_POLICY
DENY_ROLE_POLICY
DENY_EXPLICIT_POLICY
DENY_APPROVAL_REQUIRED
DENY_APPROVAL_REJECTED
DENY_PERMISSION_EXPIRED
DENY_AGENT_DISABLED
DENY_USER_DISABLED
DENY_TOOL_DISABLED
DENY_SECURITY_POLICY
DENY_RATE_LIMIT
DENY_EXECUTION_BUDGET
```

---

## 22. Human Approval

## FR-010

Certain permissions shall require human approval before execution.

Examples:

```text
customer:delete
lead:bulk_delete
customer:export
billing:refund
billing:manage
campaign:bulk_send
security:manage
permission:manage
organization:delete
```

The production audit specifically requires explicit human approval for high-risk actions including bulk outreach, data export, deletion, financial changes, and security-policy changes.

---

## 23. Permission Risk Classification

Permissions shall be classified as:

```text
LOW
MEDIUM
HIGH
CRITICAL
```

Example:

| Permission          | Risk     |
| ------------------- | -------- |
| customer:read       | LOW      |
| analytics:read      | LOW      |
| ticket:update       | MEDIUM   |
| customer:update     | MEDIUM   |
| message:send        | MEDIUM   |
| campaign:bulk_send  | HIGH     |
| customer:export     | HIGH     |
| customer:delete     | HIGH     |
| billing:refund      | CRITICAL |
| permission:manage   | CRITICAL |
| security:manage     | CRITICAL |
| organization:delete | CRITICAL |

---

## 24. Temporary Permissions

## FR-011

The system shall support temporary permissions.

Example:

```json
{
  "permission": "crm:export",
  "scope": "organization",
  "granted_by": "admin-001",
  "expires_at": "2026-09-01T00:00:00Z",
  "reason": "Quarterly audit"
}
```

---

## 25. Permission Expiration

Expired permissions shall automatically become invalid.

The system shall not depend on frontend state to detect expiration.

---

## 26. Permission Delegation

## FR-012

Authorized users shall be able to delegate selected permissions.

Delegation shall support:

* specific permission
* resource scope
* agent
* user
* workflow
* duration
* reason
* approval
* revocation

---

## 27. Permission Revocation

## FR-013

Revocation shall invalidate active authorization as quickly as operationally possible.

Cached permission decisions shall have bounded TTLs.

Critical revocations may invalidate sessions or authorization caches immediately.

---

## 28. Permission Simulation

## FR-014

Administrators shall be able to simulate an authorization request before changing production permissions.

Example:

```text
Actor:
AI Sales Agent

Action:
lead:update

Resource:
Lead #8128

Result:
ALLOW

Reason:
Agent has lead:update
AND
lead belongs to organization
AND
workflow permits update
```

---

## 29. Permission Diff

## FR-015

The system shall show authorization differences before and after a configuration change.

Example:

```text
Before:
customer:read
conversation:read

After:
customer:read
customer:update
conversation:read
conversation:write
```

---

## 30. Permission Change Approval

High-impact permission changes shall optionally require approval.

Examples:

```text
grant permission:manage
grant billing:manage
grant customer:export
grant security:manage
grant organization:delete
```

---

## 31. Permission Audit Logs

## FR-016

Every permission modification shall create an immutable audit event.

Required fields:

```text
audit_id
actor_id
actor_type
target_type
target_id
permission
old_value
new_value
tenant_id
organization_id
reason
approval_id
timestamp
ip_metadata
request_id
```

---

## 32. Authorization Audit Logs

## FR-017

The system shall log authorization decisions for security-sensitive operations.

Example:

```json
{
  "decision": "DENY",
  "actor": "ai_support_agent",
  "action": "customer:delete",
  "resource": "customer-123",
  "reason": "AGENT_PERMISSION_MISSING",
  "timestamp": "..."
}
```

---

## 33. Permission Analytics

Authorized administrators shall be able to analyze:

* most-used permissions
* denied operations
* permission violations
* excessive permissions
* unused permissions
* temporary permissions
* expired permissions
* permission escalations
* high-risk permission usage
* agent permission usage

---

## 34. Excessive Permission Detection

The system should identify agents or users with permissions significantly beyond their observed operational requirements.

Example:

```text
Agent:
AI Support Agent

Granted:
47 permissions

Observed:
12 permissions

Potential excessive permissions:
35
```

The system shall provide recommendations for least-privilege reduction.

---

## 35. Unused Permission Detection

The system shall identify permissions that have not been used during a configurable period.

Example:

```text
Permission:
billing:manage

Assigned:
AI Sales Agent

Used:
0 times in 90 days

Recommendation:
Review and revoke
```

---

## 36. Permission Conflict Detection

The system shall detect contradictory authorization policies.

Example:

```text
Organization Policy:
DENY customer:export

Agent Policy:
ALLOW customer:export
```

The system shall apply the defined precedence model and report the conflict.

---

## 37. Privilege Escalation Detection

The platform shall detect attempts to:

* modify own permissions
* modify another agent's permissions
* modify role definitions
* access admin resources
* bypass approval
* use another user's credentials
* access another tenant
* manipulate tenant IDs
* invoke restricted tools

Such attempts shall be logged and optionally trigger security alerts.

---

## 38. Cross-Tenant Protection

## FR-018

Every resource access shall verify tenant ownership.

Example:

```text
Request:
GET customer/999

Authenticated Tenant:
tenant-A

Customer Tenant:
tenant-B

Decision:
DENY_TENANT_MISMATCH
```

The system shall never rely solely on a client-provided `tenant_id`.

---

## 39. Permission-Aware Agent Tool Discovery

## FR-019

When an AI agent requests available tools, the platform shall return only tools that are authorized for the effective execution context.

```text
All Tools
    ↓
Organization Filter
    ↓
User Filter
    ↓
Agent Filter
    ↓
Workflow Filter
    ↓
Risk Filter
    ↓
Tool Permission Filter
    ↓
Authorized Tools
```

---

## 40. Permission-Aware Workflow Execution

## FR-020

Before each workflow node executes, the platform shall re-evaluate authorization.

This prevents an agent from retaining stale permissions after authorization changes.

---

## 41. Permission-Aware Multi-Agent Collaboration

When one AI agent delegates work to another agent:

```text
Agent A
    ↓
Agent B
```

Agent B shall not inherit Agent A's complete permission set automatically.

Instead:

```text
Delegated Capability
=
Agent A allowed capability
∩
Agent B allowed capability
∩
Workflow policy
```

---

## 42. Permission Propagation

Permission context shall propagate through:

```text
Frontend
→ API Gateway
→ Authentication
→ Agent Service
→ Orchestrator
→ Workflow
→ Tool Engine
→ MCP/API
→ External Provider
```

Each service shall preserve authorization context securely.

---

## 43. API Requirements

## API-001 — List Permissions

```http
GET /api/v1/permissions
```

## API-002 — Permission Details

```http
GET /api/v1/permissions/{permission_id}
```

## API-003 — User Permissions

```http
GET /api/v1/users/{user_id}/permissions
```

## API-004 — Agent Permissions

```http
GET /api/v1/agents/{agent_id}/permissions
```

## API-005 — Grant Agent Permission

```http
POST /api/v1/agents/{agent_id}/permissions
```

## API-006 — Revoke Agent Permission

```http
DELETE /api/v1/agents/{agent_id}/permissions/{permission_id}
```

## API-007 — Authorization Check

```http
POST /api/v1/authorization/check
```

## API-008 — Effective Permissions

```http
GET /api/v1/agents/{agent_id}/effective-permissions
```

## API-009 — Permission Simulation

```http
POST /api/v1/authorization/simulate
```

## API-010 — Permission Audit

```http
GET /api/v1/authorization/audit
```

---

## 44. Example Authorization Request

```json
{
  "actor": {
    "type": "ai_agent",
    "id": "support-agent-001"
  },
  "principal": {
    "user_id": "user-123",
    "organization_id": "org-456",
    "tenant_id": "tenant-456"
  },
  "action": "ticket:update",
  "resource": {
    "type": "ticket",
    "id": "ticket-789",
    "tenant_id": "tenant-456",
    "organization_id": "org-456"
  },
  "workflow_id": "support-workflow-001",
  "tool_id": "ticket.update"
}
```

---

## 45. Example Authorization Response

```json
{
  "decision": "ALLOW",
  "permission": "ticket:update",
  "risk_level": "MEDIUM",
  "reason_code": "AUTHORIZED",
  "requires_approval": false,
  "policy_version": "2026.08.26"
}
```

---

## 46. Example Denial Response

```json
{
  "decision": "DENY",
  "reason_code": "DENY_AGENT_PERMISSION",
  "message": "The AI agent is not authorized to perform customer deletion.",
  "requires_human_approval": false
}
```

---

## 47. Database Requirements

The system should maintain entities including:

```text
permissions
roles
role_permissions
users
user_roles
user_permissions
agents
agent_permissions
agent_roles
agent_tool_permissions
workflow_permissions
resource_permissions
permission_policies
permission_delegations
permission_approvals
permission_audit_events
authorization_decisions
permission_cache
```

---

## 48. Suggested Permission Schema

## permissions

```text
id
permission_id
name
description
domain
resource
action
risk_level
scope_type
status
created_at
updated_at
```

## agent_permissions

```text
id
agent_id
permission_id
tenant_id
organization_id
scope
resource_filter
granted_by
expires_at
status
created_at
updated_at
```

## permission_delegations

```text
id
delegator_id
delegate_type
delegate_id
permission_id
resource_scope
reason
approval_id
starts_at
expires_at
status
created_at
```

## authorization_decisions

```text
id
request_id
tenant_id
organization_id
actor_type
actor_id
user_id
agent_id
workflow_id
tool_id
action
resource_type
resource_id
decision
reason_code
policy_version
timestamp
```

---

## 49. Security Requirements

## SEC-001

Authorization must be enforced server-side.

## SEC-002

Tenant identity must be derived from trusted authentication context.

## SEC-003

AI-generated tenant IDs must never be trusted.

## SEC-004

AI agents must not be able to grant themselves permissions.

## SEC-005

AI agents must not be able to modify their own authorization policy.

## SEC-006

Human users must not be able to grant permissions exceeding their own delegation authority.

## SEC-007

Sensitive permissions must require additional approval.

## SEC-008

Authorization decisions must be auditable.

## SEC-009

Permission caches must have bounded lifetime.

## SEC-010

Permission revocation must invalidate relevant caches.

## SEC-011

Cross-tenant resource access must always be denied.

## SEC-012

Authorization must not depend on frontend state.

## SEC-013

MCP tools must have explicit permissions.

## SEC-014

External tool results must never modify authorization policies.

## SEC-015

Permission changes must be protected against CSRF, replay, and unauthorized API invocation.

---

## 50. AI Safety Requirements

AI agents shall not be able to:

```text
grant themselves permissions
change role hierarchy
modify authorization policy
disable security controls
bypass approval
forge authorization context
change tenant identity
access unauthorized tools
access unauthorized knowledge
access unauthorized customer data
export restricted data
execute prohibited operations
```

The platform's agent/tool safety audit explicitly requires prevention of unauthorized tool calls, privilege escalation, tenant crossing, secret access, and uncontrolled autonomous actions.

---

## 51. Human-AI Permission Model

For hybrid execution:

```text
Human User
    |
    v
User Effective Permissions
    |
    v
AI Agent Permissions
    |
    v
Workflow Permissions
    |
    v
Tool Permissions
    |
    v
Resource Permissions
    |
    v
Organization Policy
    |
    v
Authorization Decision
```

The effective permission shall never exceed the narrowest applicable boundary.

---

## 52. Permission Matrix

| Capability        | End User | AI Support | Human Support |   AI Sales | Human Sales |    Manager | Admin |
| ----------------- | -------: | ---------: | ------------: | ---------: | ----------: | ---------: | ----: |
| Customer Read     |        ✓ |          ✓ |             ✓ |    Limited |           ✓ |          ✓ |     ✓ |
| Customer Update   |        — |    Limited |             ✓ |    Limited |           ✓ |          ✓ |     ✓ |
| Customer Delete   |        — |          ✗ |             ✗ |          ✗ |  Restricted | Restricted |     ✓ |
| Conversation Read |        ✓ |          ✓ |             ✓ |    Limited |           ✓ |          ✓ |     ✓ |
| Ticket Create     |        ✓ |          ✓ |             ✓ |    Limited |           ✓ |          ✓ |     ✓ |
| Ticket Assign     |        — |    Limited |             ✓ |          ✗ |     Limited |          ✓ |     ✓ |
| Knowledge Read    |        ✓ |          ✓ |             ✓ |          ✓ |           ✓ |          ✓ |     ✓ |
| Knowledge Write   |        — |          ✗ |       Limited |          ✗ |     Limited |          ✓ |     ✓ |
| Lead Read         |        — |    Limited |       Limited |          ✓ |           ✓ |          ✓ |     ✓ |
| Lead Update       |        — |    Limited |       Limited |          ✓ |           ✓ |          ✓ |     ✓ |
| Bulk Outreach     |        ✗ | Restricted |    Restricted | Restricted |           ✓ |          ✓ |     ✓ |
| Data Export       |        ✗ |          ✗ |    Restricted |          ✗ |  Restricted |          ✓ |     ✓ |
| Billing Read      |        ✗ |          ✗ |             ✗ |          ✗ |           ✗ |    Limited |     ✓ |
| Billing Manage    |        ✗ |          ✗ |             ✗ |          ✗ |           ✗ | Restricted |     ✓ |
| Permission Manage |        ✗ |          ✗ |             ✗ |          ✗ |           ✗ | Restricted |     ✓ |
| Audit Read        |        ✗ |          ✗ |       Limited |          ✗ |     Limited |          ✓ |     ✓ |
| Security Manage   |        ✗ |          ✗ |             ✗ |          ✗ |           ✗ | Restricted |     ✓ |

---

## 53. Permission Lifecycle

```text
DEFINE
  ↓
REVIEW
  ↓
APPROVE
  ↓
ASSIGN
  ↓
ACTIVATE
  ↓
MONITOR
  ↓
REVIEW
  ↓
RESTRICT / MODIFY
  ↓
REVOKE
  ↓
AUDIT
  ↓
ARCHIVE
```

---

## 54. Permission Change Workflow

```text
Administrator
    ↓
Select Actor
    ↓
Select Permission
    ↓
Select Resource Scope
    ↓
Select Duration
    ↓
Risk Evaluation
    ↓
Approval Required?
    ├── NO → Apply
    |
    └── YES
          ↓
       Approval
          ↓
      Approved?
       /      \
     YES       NO
      |         |
    Apply      Reject
      |
      v
Audit Event
      |
      v
Permission Active
```

---

## 55. AI Permission Evaluation Workflow

```text
AI Agent
    ↓
Requests Action
    ↓
Resolve Tool
    ↓
Resolve User Context
    ↓
Resolve Agent Permissions
    ↓
Resolve Workflow Permissions
    ↓
Resolve Resource Scope
    ↓
Evaluate Organization Policy
    ↓
Evaluate Risk
    ↓
Approval Required?
    ├── YES → Human Approval
    |
    └── NO
          ↓
    Authorization Decision
          ↓
       ALLOW / DENY
          ↓
        Execute
          ↓
        Audit
```

---

## 56. Performance Requirements

## PERF-001

Authorization decisions should target:

```text
P95 < 100 ms
```

for cached/simple authorization decisions.

---

## PERF-002

Complex policy evaluation should target:

```text
P95 < 200 ms
```

excluding external dependency latency.

---

## PERF-003

Permission checks shall support caching where safe.

---

## PERF-004

Critical permission revocation shall bypass stale authorization caches.

---

## 57. Reliability Requirements

## REL-001

Authorization failures shall fail closed.

## REL-002

An unavailable authorization service shall not silently grant access.

## REL-003

Permission changes shall be transactional.

## REL-004

Concurrent permission updates shall not create inconsistent authorization states.

## REL-005

Authorization decisions shall remain traceable after service failures.

## REL-006

Permission configuration shall survive service restarts.

---

## 58. Testing Requirements

The authorization subsystem shall include:

```text
Unit Tests
Integration Tests
API Tests
RBAC Tests
ABAC Tests
Tenant Isolation Tests
Agent Permission Tests
Tool Permission Tests
Workflow Permission Tests
MCP Permission Tests
Delegation Tests
Approval Tests
Revocation Tests
Concurrency Tests
Cache Invalidation Tests
Privilege Escalation Tests
Negative Tests
Security Tests
End-to-End Tests
```

Critical SalesGenie business paths should include RBAC and cross-tenant isolation tests, along with negative tests for permission failures.

---

## 59. Mandatory Negative Tests

The system must verify that:

* [ ] User cannot access another tenant.
* [ ] Agent cannot access another tenant.
* [ ] Agent cannot use unauthorized tool.
* [ ] Agent cannot modify its own permissions.
* [ ] Agent cannot modify another agent's permissions.
* [ ] User cannot grant unauthorized permissions.
* [ ] Expired permission is denied.
* [ ] Revoked permission is denied.
* [ ] Disabled agent is denied.
* [ ] Disabled user is denied.
* [ ] Disabled tool is denied.
* [ ] Workflow cannot exceed its permission scope.
* [ ] MCP tool cannot exceed its permission mapping.
* [ ] Resource ownership is validated.
* [ ] Explicit deny overrides allow.
* [ ] High-risk operations require approval.
* [ ] Approval rejection prevents execution.
* [ ] Approval expiration prevents execution.
* [ ] Stale authorization cache cannot bypass revocation.

---

## 60. Observability Requirements

The platform shall expose:

```text
authorization_allow_count
authorization_deny_count
authorization_denial_rate
permission_change_count
permission_escalation_attempts
cross_tenant_denials
approval_requests
approval_rejections
expired_permission_count
revoked_permission_usage
agent_permission_usage
unused_permissions
high_risk_permission_usage
```

---

## 61. Security Alerts

The system should generate alerts for:

```text
Repeated authorization failures
Cross-tenant access attempts
Privilege escalation attempts
Self-permission modification attempts
Unauthorized tool execution
Unauthorized data exports
Repeated approval bypass attempts
Suspicious permission changes
Mass permission grants
Mass permission revocations
Unexpected AI behavior
```

---

## 62. Permission Governance Dashboard

Administrators shall have access to dashboards showing:

### Identity

* users
* roles
* agents
* organizations

### Authorization

* permissions
* grants
* revocations
* effective permissions

### Security

* denied operations
* privilege escalation
* cross-tenant attempts

### AI Governance

* AI agents with excessive permissions
* AI agent tool access
* autonomous high-risk attempts
* human approvals

### Compliance

* permission changes
* audit history
* temporary access
* expired access

---

## 63. Compliance and Data Governance

The permission subsystem shall support governance controls around:

* customer data
* lead data
* conversation data
* documents
* AI prompts
* AI responses
* analytics
* billing
* integrations
* external data

SalesGenie's broader audit requirements call for classification of data sensitivity, ownership, data-flow tracing, retention/deletion controls, export/deletion workflows, consent controls, and minimized third-party data sharing.

---

## 64. Administrative Controls

Super Admins shall be able to:

* create platform permissions
* modify permission definitions
* manage global roles
* manage organization authorization policies
* revoke emergency access
* inspect authorization decisions
* inspect permission changes
* manage security policies
* configure approval policies
* audit AI agent permissions

Organization Admins shall be restricted to their organization.

---

## 65. Separation of Duties

The platform shall support separation-of-duties policies.

Examples:

```text
User who creates a refund
    !=
User who approves the refund
```

```text
User who grants permission:manage
    !=
User who approves critical permission escalation
```

where organizational policy requires it.

---

## 66. Four-Eyes Approval

Critical authorization changes may require two independent approvers.

Example:

```text
Permission:
security:manage

Requested By:
Organization Admin

Approval 1:
Security Admin

Approval 2:
Super Admin

Result:
ACTIVE
```

---

## 67. Break-Glass Access

The system may support emergency break-glass access for critical incidents.

Break-glass access must require:

* explicit reason
* authorized actor
* limited duration
* limited scope
* mandatory audit
* post-incident review

Break-glass access shall not silently become permanent authorization.

---

## 68. Permission Policy Versioning

Every authorization decision shall reference the policy version used.

Example:

```json
{
  "policy_version": "2026.08.26.14",
  "decision": "DENY"
}
```

This ensures historical decisions remain explainable after policies change.

---

## 69. Permission Cache

The system may cache authorization decisions.

Cache keys should include sufficient authorization context, such as:

```text
tenant
organization
actor
agent
workflow
permission
resource
policy_version
```

A cache must never allow one tenant's decision to be reused for another tenant.

---

## 70. API Security

All permission-management APIs shall require:

* authentication
* authorization
* request validation
* tenant validation
* CSRF protection where applicable
* rate limiting
* audit logging
* idempotency where appropriate

---

## 71. No Frontend-Only Authorization

The following is explicitly prohibited:

```text
if (user.role === "admin") {
    showDeleteButton();
}
```

being treated as sufficient authorization.

The backend must independently evaluate:

```text
Can Actor X
perform Operation Y
on Resource Z?
```

---

## 72. Agent Permission Configuration Example

```json
{
  "agent_id": "sales-agent-001",
  "permissions": [
    "lead:read",
    "lead:update",
    "company:read",
    "contact:read",
    "crm:read",
    "crm:update",
    "opportunity:create",
    "knowledge:read",
    "analytics:read",
    "email:draft"
  ],
  "denied_permissions": [
    "billing:manage",
    "permission:manage",
    "security:manage",
    "customer:delete",
    "data:export"
  ]
}
```

---

## 73. Support AI Agent Example

```json
{
  "agent_id": "support-ai-001",
  "permissions": [
    "customer:read",
    "conversation:read",
    "conversation:write",
    "ticket:read",
    "ticket:create",
    "ticket:update",
    "ticket:assign",
    "knowledge:read",
    "sentiment:read",
    "sla:read"
  ],
  "requires_approval_for": [
    "customer:update",
    "bulk:message",
    "customer:export"
  ]
}
```

---

## 74. Human Support Agent Example

```json
{
  "role": "support_agent",
  "permissions": [
    "customer:read",
    "conversation:read",
    "conversation:write",
    "ticket:read",
    "ticket:create",
    "ticket:update",
    "knowledge:read"
  ]
}
```

---

## 75. Sales Manager Example

```json
{
  "role": "sales_manager",
  "permissions": [
    "lead:read",
    "lead:create",
    "lead:update",
    "lead:assign",
    "company:read",
    "contact:read",
    "opportunity:read",
    "opportunity:create",
    "opportunity:update",
    "analytics:read",
    "report:read",
    "agent:execute"
  ]
}
```

---

## 76. Permission Inheritance

Permission inheritance shall be explicit.

Example:

```text
Organization
    ↓
Team
    ↓
Role
    ↓
User
```

AI agents may inherit selected organizational policies but shall not automatically inherit all human permissions.

---

## 77. Agent Permission Boundary

An AI agent acting on behalf of a user shall satisfy:

```text
Effective AI Permission
=
User Permission
∩
Agent Permission
∩
Workflow Permission
∩
Tool Permission
∩
Resource Permission
∩
Organization Policy
```

If any required boundary denies the action:

```text
FINAL DECISION = DENY
```

---

## 78. Functional Requirement — Explainability

## FR-021

Every authorization decision shall be explainable using structured reason codes.

The platform shall provide:

```text
Decision
Policy
Permission
Resource Scope
Actor
Approval State
Policy Version
```

It shall not expose confidential model chain-of-thought.

---

## 79. Functional Requirement — Permission Recommendations

The platform should provide AI-assisted permission recommendations based on observed usage.

Example:

```text
AI Recommendation

Agent:
Support Agent

Unused:
billing:read
analytics:admin
customer:export

Recommendation:
Review and remove these permissions.
```

Recommendations shall never automatically modify permissions.

---

## 80. Functional Requirement — Permission Anomaly Detection

The system should detect abnormal authorization behavior.

Examples:

```text
AI support agent suddenly accessing billing
Sales agent accessing security settings
Human support agent exporting thousands of records
Agent repeatedly attempting denied actions
```

Such events shall be available for security investigation.

---

## 81. Functional Requirement — Policy Testing

Administrators shall be able to test authorization policies against predefined scenarios.

Example:

```text
Scenario:
AI Support Agent attempts customer deletion.

Expected:
DENY

Actual:
DENY

Status:
PASS
```

---

## 82. Functional Requirement — Policy Regression Testing

Changes to authorization policies shall be testable against existing authorization scenarios before production activation.

---

## 83. Functional Requirement — Safe Policy Deployment

Authorization policy changes shall support:

```text
Draft
    ↓
Validate
    ↓
Test
    ↓
Review
    ↓
Approve
    ↓
Publish
    ↓
Monitor
    ↓
Rollback
```

---

## 84. Functional Requirement — Rollback

Authorized administrators shall be able to roll back a faulty permission-policy deployment.

---

## 85. Functional Requirement — Authorization Metrics

The platform shall expose authorization metrics through the existing observability architecture.

Metrics shall include:

```text
allowed requests
denied requests
denial reasons
authorization latency
permission changes
high-risk decisions
approval latency
cross-tenant attempts
privilege escalation attempts
```

SalesGenie's broader architecture is intended to use Prometheus/Grafana for real-time operational and AI metrics, so authorization telemetry should integrate into that observability model.

---

## 86. Non-Functional Requirements

## NFR-001 — Security

Authorization must fail closed.

## NFR-002 — Scalability

The authorization service must scale independently from application services.

## NFR-003 — Availability

Authorization must support highly available deployment.

## NFR-004 — Performance

Common authorization checks should be low-latency.

## NFR-005 — Consistency

Critical permission changes must propagate reliably.

## NFR-006 — Auditability

Every sensitive permission decision must be traceable.

## NFR-007 — Extensibility

New permission domains must be addable without redesigning the authorization engine.

## NFR-008 — Multi-Tenancy

No permission path may allow cross-tenant access.

## NFR-009 — Maintainability

Authorization logic shall be centralized and consistently implemented.

## NFR-010 — Backward Compatibility

Permission-policy version changes shall not silently break existing production workflows.

---

## 87. Acceptance Criteria

The Agent Permissions subsystem shall not be considered production-ready until:

* [ ] Every protected resource has explicit authorization.
* [ ] Every AI agent has an explicit permission profile.
* [ ] Every human agent has an explicit role/permission profile.
* [ ] Permissions are enforced server-side.
* [ ] Authorization defaults to deny.
* [ ] Least privilege is enforced.
* [ ] Tenant isolation is enforced.
* [ ] Resource ownership is validated.
* [ ] RBAC is implemented.
* [ ] ABAC/resource-level policies are supported.
* [ ] Agent permissions cannot self-escalate.
* [ ] Human users cannot grant unauthorized privileges.
* [ ] Workflow permissions are enforced.
* [ ] Tool permissions are enforced.
* [ ] MCP permissions are enforced.
* [ ] User and AI permissions are intersected for delegated AI actions.
* [ ] High-risk operations require approval where configured.
* [ ] Temporary permissions expire automatically.
* [ ] Permission revocation propagates correctly.
* [ ] Authorization caches cannot bypass revocation.
* [ ] Permission changes are audited.
* [ ] Authorization decisions are auditable.
* [ ] Cross-tenant access tests pass.
* [ ] Privilege-escalation tests pass.
* [ ] Negative authorization tests pass.
* [ ] Policy regression tests pass.
* [ ] Permission simulation works.
* [ ] Effective-permission calculation works.
* [ ] Permission conflicts are detectable.
* [ ] Excessive permissions can be identified.
* [ ] Unused permissions can be identified.
* [ ] Break-glass access is audited if enabled.
* [ ] Four-eyes approval is supported for critical operations where required.
* [ ] Authorization metrics are observable.
* [ ] Security alerts exist for abnormal authorization behavior.
* [ ] Authorization service failure fails closed.
* [ ] Authorization policy versions are traceable.
* [ ] Production authorization changes support rollback.

---

## 88. FAANG-Level Authorization Principles

SalesGenie's Agent Permissions architecture shall follow:

1. **Deny by default**
2. **Least privilege**
3. **Zero implicit trust**
4. **Server-side enforcement**
5. **Tenant isolation**
6. **Resource-level authorization**
7. **RBAC + ABAC**
8. **Explicit AI permissions**
9. **No AI self-escalation**
10. **Human approval for high-risk actions**
11. **Separation of duties**
12. **Four-eyes approval for critical operations**
13. **Short-lived delegated permissions**
14. **Immediate critical revocation**
15. **Immutable auditability**
16. **Policy versioning**
17. **Authorization decision explainability**
18. **Continuous permission monitoring**
19. **Permission anomaly detection**
20. **Safe policy deployment**
21. **Policy regression testing**
22. **Fail-closed authorization**
23. **No frontend-only security**
24. **No cross-tenant authorization**
25. **Bounded AI autonomy**

---

## 89. Final Authorization Architecture

```text
                         ┌─────────────────────┐
                         │    SalesGenie UI    │
                         └──────────┬──────────┘
                                    │
                                    v
                         ┌─────────────────────┐
                         │ Authentication      │
                         │ Identity / Session  │
                         └──────────┬──────────┘
                                    │
                                    v
                         ┌─────────────────────┐
                         │ Authorization       │
                         │ Policy Engine       │
                         └──────────┬──────────┘
                                    │
                 ┌──────────────────┼──────────────────┐
                 │                  │                  │
                 v                  v                  v
          User Permissions   Agent Permissions   Organization Policy
                 │                  │                  │
                 └──────────────────┼──────────────────┘
                                    │
                                    v
                         ┌─────────────────────┐
                         │ Workflow Policy     │
                         └──────────┬──────────┘
                                    │
                                    v
                         ┌─────────────────────┐
                         │ Tool / MCP Policy   │
                         └──────────┬──────────┘
                                    │
                                    v
                         ┌─────────────────────┐
                         │ Resource Ownership  │
                         │ + Data Scope        │
                         └──────────┬──────────┘
                                    │
                                    v
                         ┌─────────────────────┐
                         │ Risk Evaluation     │
                         └──────────┬──────────┘
                                    │
                         ┌──────────┴──────────┐
                         │                     │
                         v                     v
                    LOW/MEDIUM            HIGH/CRITICAL
                         │                     │
                         │              Human Approval
                         │                     │
                         └──────────┬──────────┘
                                    │
                                    v
                         ┌─────────────────────┐
                         │ ALLOW / DENY        │
                         └──────────┬──────────┘
                                    │
                         ┌──────────┴──────────┐
                         │                     │
                         v                     v
                     EXECUTE                 DENY
                         │                     │
                         v                     v
                 ┌──────────────┐      ┌──────────────┐
                 │ Audit / Logs │      │ Security     │
                 │ Metrics      │      │ Alert        │
                 │ Traces       │      └──────────────┘
                 └──────────────┘
```

---

## 90. Final Product Requirement

The SalesGenie Agent Permissions subsystem shall operate as a **centralized enterprise authorization plane for both human and AI actors**.

The system must ensure that:

```text
AI Agent
    ≠
Human User
    ≠
Role
    ≠
Tool
    ≠
Workflow
    ≠
Resource
```

Each must have an independently enforceable authorization boundary.

The final authorization decision shall be:

```text
ALLOW
only when

Authentication
AND
Tenant Isolation
AND
User Authorization
AND
Agent Authorization
AND
Workflow Authorization
AND
Tool Authorization
AND
Resource Authorization
AND
Organization Policy
AND
Risk Policy
AND
Approval Policy
```

all permit the requested operation.

Otherwise:

```text
DENY
```

This design ensures that SalesGenie's AI agents can operate autonomously where safe, collaborate with human agents where appropriate, and execute enterprise actions at scale without allowing model behavior to bypass security, authorization, tenant isolation, governance, or human-control boundaries.
