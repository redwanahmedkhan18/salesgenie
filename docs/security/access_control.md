# SalesGenie — Access Control Requirements

**Document:** `access_control.md`  
**Product:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Requirement Level:** FAANG-Level / Production-Grade  
**Scope:** Human Access + AI Access + API Access + Service Access + Workflow Access + Integration Access + Tenant Access + Administrative Access

---

## 1. Purpose

SalesGenie shall implement a centralized, policy-driven, zero-trust access-control architecture that determines whether a human, AI agent, service, workflow, integration, API client, or other machine actor is permitted to perform a specific action on a specific resource within a specific tenant and security context.

The access-control system shall protect:

- Organizations
- Tenants
- Users
- Teams
- Roles
- Permissions
- Leads
- Contacts
- Companies
- Conversations
- Tickets
- Customers
- Knowledge bases
- Documents
- AI agents
- AI tools
- AI workflows
- Workflow executions
- Integrations
- API keys
- API clients
- Webhooks
- Billing resources
- Subscriptions
- Invoices
- Usage data
- Analytics
- Security configurations
- Audit logs
- Administrative resources
- Platform-level resources

The system shall prevent:

```text
Unauthorized Access
Privilege Escalation
Horizontal Privilege Abuse
Vertical Privilege Abuse
Cross-Tenant Access
Role Abuse
Permission Creep
AI Privilege Escalation
AI Tool Abuse
Workflow Privilege Escalation
Service-to-Service Abuse
API Abuse
Integration Abuse
Resource Ownership Bypass
Administrative Abuse
Policy Bypass
```

---

## 2. Access Control Objectives

SalesGenie shall:

1. Enforce least privilege.
2. Enforce deny-by-default authorization.
3. Enforce tenant isolation.
4. Authenticate actors before protected operations.
5. Authorize every protected operation.
6. Support RBAC.
7. Support ABAC.
8. Support resource-based authorization.
9. Support policy-based authorization.
10. Support delegated authorization.
11. Support human-to-AI authorization.
12. Support AI-to-tool authorization.
13. Support AI-to-AI authorization.
14. Support service-to-service authorization.
15. Support workflow authorization.
16. Support integration authorization.
17. Support API authorization.
18. Support privileged access controls.
19. Prevent self-privilege escalation.
20. Provide complete authorization auditability.
21. Support rapid permission revocation.
22. Support temporary permissions.
23. Support permission expiration.
24. Support enterprise access policies.
25. Make authorization decisions deterministic, explainable, and testable.

---

## 3. Access Control Principles

## ACP-001 — Deny by Default

Any request without an explicit applicable allow policy shall be denied.

```text
No Explicit Allow
        |
        v
      DENY
```

---

## ACP-002 — Least Privilege

Every actor shall receive only the minimum permissions required.

---

## ACP-003 — Explicit Authorization

Authentication alone shall never imply authorization.

```text
Authenticated != Authorized
```

---

## ACP-004 — Tenant Isolation

All tenant-scoped resources shall be protected by tenant-aware authorization.

---

## ACP-005 — Server-Side Enforcement

Authorization shall be enforced server-side.

Client-side controls shall never be considered a security boundary.

---

## ACP-006 — Every Request Is Evaluated

Protected requests shall be evaluated against current identity, permissions, resource, and policy context.

---

## ACP-007 — Human and AI Separation

Human permissions and AI permissions shall remain logically distinct.

---

## ACP-008 — Delegation Must Be Explicit

An AI agent shall receive permissions through explicit delegation.

---

## ACP-009 — No Privilege Inheritance by Default

AI agents, workflows, services, and integrations shall not automatically inherit the full privileges of their initiating human.

---

## ACP-010 — Fail Closed

Authorization infrastructure failures shall result in denial for protected operations.

---

## 4. Access Control Actors

SalesGenie shall support authorization for:

```text
Human User
End User
Sales Agent
Support Agent
Team Lead
Manager
Organization Admin
Security Admin
Billing Admin
Developer
Auditor
Super Admin

AI Agent
AI Orchestrator
AI Worker
AI Tool
AI Workflow
Workflow Execution

Microservice
Background Worker
Service Account
API Client
API Key
Integration
Webhook Producer
MCP Client
MCP Server
```

---

## 5. User Requirements

## UR-ACCESS-001 — Role-Based Access

Users shall receive permissions based on assigned roles.

---

## UR-ACCESS-002 — Permission Visibility

Authorized administrators shall be able to view effective permissions for users.

---

## UR-ACCESS-003 — Access Restrictions

Users shall be prevented from accessing resources outside their authorized scope.

---

## UR-ACCESS-004 — Team-Based Access

Organizations shall be able to restrict resources to specific teams where supported.

---

## UR-ACCESS-005 — Resource Ownership

Users shall be able to access resources they own when their role permits ownership-based access.

---

## UR-ACCESS-006 — Shared Resources

Authorized users shall be able to access resources explicitly shared with them.

---

## UR-ACCESS-007 — Access Revocation

Administrators shall be able to revoke user permissions.

---

## UR-ACCESS-008 — Temporary Access

Authorized administrators shall be able to grant temporary access where supported.

---

## UR-ACCESS-009 — Permission Expiration

Temporary permissions shall automatically expire.

---

## UR-ACCESS-010 — Access Requests

Users may request access to restricted resources where an approval workflow is configured.

---

## 6. System Requirements

## SR-ACCESS-001 — Central Authorization Layer

SalesGenie shall provide a centralized authorization layer or consistently enforced distributed authorization architecture.

---

## SR-ACCESS-002 — Policy Decision Point

The platform shall provide a trusted policy decision mechanism.

---

## SR-ACCESS-003 — Policy Enforcement Point

Protected services shall enforce authorization decisions before executing protected operations.

---

## SR-ACCESS-004 — Policy Administration Point

Authorized administrators shall be able to manage access policies.

---

## 7. Authorization Architecture

```text
                         REQUEST
                            |
                            v
                     Authentication
                            |
                            v
                      Identity Context
                            |
              +-------------+-------------+
              |             |             |
              v             v             v
            Tenant         Role        Attributes
              |             |             |
              +-------------+-------------+
                            |
                            v
                     Resource Context
                            |
                            v
                     Action Context
                            |
                            v
                     Policy Engine
                            |
                    +-------+-------+
                    |               |
                    v               v
                  ALLOW            DENY
                    |
                    v
              Policy Enforcement
                    |
                    v
                  Resource
```

---

## 8. Authorization Decision Model

Every protected operation should conceptually evaluate:

```text
Decision =
    Identity
    +
    Authentication Context
    +
    Tenant
    +
    Role
    +
    Permissions
    +
    Resource
    +
    Action
    +
    Ownership
    +
    Attributes
    +
    Policy
    +
    Risk
    +
    Delegation Context
```

---

## 9. RBAC Requirements

SalesGenie shall support granular role-based access control.

Example roles:

```text
END_USER
SALES_AGENT
SUPPORT_AGENT
TEAM_LEAD
MANAGER
ORG_ADMIN
SECURITY_ADMIN
BILLING_ADMIN
DEVELOPER
AUDITOR
SUPER_ADMIN
```

---

## 10. Role Hierarchy

Where required, roles may use controlled hierarchy.

Example:

```text
SUPER_ADMIN
    |
    +── ORG_ADMIN
          |
          +── MANAGER
                |
                +── TEAM_LEAD
                      |
                      +── SALES_AGENT
                      +── SUPPORT_AGENT
```

Role hierarchy shall never unintentionally grant platform-wide privileges.

---

## 11. Permission Model

Permissions shall use granular resource-action semantics.

Examples:

```text
lead:read
lead:create
lead:update
lead:delete
lead:export

contact:read
contact:create
contact:update
contact:delete

conversation:read
conversation:create
conversation:update
conversation:delete

ticket:read
ticket:create
ticket:update
ticket:delete

agent:read
agent:create
agent:update
agent:execute
agent:delete

workflow:read
workflow:create
workflow:update
workflow:execute
workflow:delete

integration:read
integration:connect
integration:update
integration:execute
integration:disconnect

knowledge_base:read
knowledge_base:create
knowledge_base:update
knowledge_base:delete

billing:read
billing:manage

subscription:read
subscription:manage

user:read
user:create
user:update
user:suspend
user:delete

role:read
role:assign
role:modify

audit:read
security:manage
```

---

## 12. Permission Granularity

Permissions shall distinguish between:

```text
READ
CREATE
UPDATE
DELETE
EXECUTE
APPROVE
EXPORT
SHARE
ADMINISTER
```

---

## 13. Wildcard Permissions

Wildcard permissions shall be restricted to privileged administrative contexts.

Example:

```text
lead:*
workflow:*
admin:*
```

Ordinary users shall not receive broad wildcards unless explicitly required.

---

## 14. ABAC Requirements

SalesGenie shall support attribute-based authorization where RBAC alone is insufficient.

Supported attributes may include:

```text
tenant_id
organization_id
department_id
team_id
user_id
resource_owner_id
resource_tenant_id
resource_classification
environment
risk_level
device_trust
authentication_strength
subscription_plan
data_region
time_window
agent_id
workflow_id
integration_id
```

---

## 15. Resource-Based Access Control

Resources may define:

```text
Owner
Tenant
Team
Visibility
Classification
Allowed Users
Allowed Roles
Allowed Agents
```

---

## 16. Ownership Authorization

Example:

```text
IF
    user.id == resource.owner_id
AND
    user.permission == "lead:update"
THEN
    ALLOW
```

---

## 17. Team Authorization

Example:

```text
IF
    user.team_id == resource.team_id
AND
    user.permission == "conversation:read"
THEN
    ALLOW
```

---

## 18. Organization Authorization

Organization administrators shall only manage resources belonging to their organization unless explicitly granted platform-level permissions.

---

## 19. Tenant Authorization

Every tenant-scoped request shall validate:

```text
request.tenant_id
resource.tenant_id
identity.tenant_id
```

---

## 20. Cross-Tenant Access Prevention

The authorization layer shall reject:

```text
identity.tenant_id != resource.tenant_id
```

unless a dedicated platform-level policy explicitly permits the operation.

---

## 21. Client Tenant ID Protection

Client-provided tenant IDs shall never independently determine authorization.

---

## 22. Tenant Context Injection

Tenant context shall be established from trusted authentication or server-side identity context.

---

## 23. Cross-Tenant Query Protection

Database queries shall enforce tenant boundaries.

Example conceptual requirement:

```text
SELECT *
FROM leads
WHERE tenant_id = authenticated_tenant_id;
```

---

## 24. Horizontal Privilege Escalation Protection

A user shall not access another user's resources merely by changing an object identifier.

Example attack:

```text
GET /leads/user-owned-lead-123
```

Changing the ID to another user's lead shall result in denial when authorization does not permit access.

---

## 25. Vertical Privilege Escalation Protection

A lower-privileged actor shall not invoke administrator operations by manipulating:

```text
Role
Permission
Request Payload
Headers
JWT Claims
Resource IDs
API Parameters
```

---

## 26. Self-Privilege Modification

Users shall not modify their own:

```text
Role
Permissions
Tenant
Administrative Status
Security Privileges
```

unless a specifically authorized workflow permits it.

---

## 27. Role Assignment

Only authorized administrators shall assign roles.

---

## 28. Role Modification

Modification of privileged roles shall require elevated authorization.

---

## 29. Role Deletion

A role shall not be deleted if doing so would unintentionally orphan or escalate privileged access.

---

## 30. Permission Revocation

Permission revocation shall propagate to active authorization decisions within a defined security SLO.

---

## 31. Authorization Cache Invalidation

Critical role or permission changes shall invalidate relevant authorization caches.

---

## 32. Temporary Permissions

Temporary permissions shall contain:

```text
permission
grantee
grantor
reason
created_at
expires_at
scope
```

---

## 33. Time-Bound Access

Policies may restrict access by time.

Example:

```text
08:00 - 18:00
Monday - Friday
```

---

## 34. Location-Aware Access

Organizations may optionally restrict access based on configured location or network policies.

Such controls shall not replace identity authentication.

---

## 35. Device-Aware Authorization

High-risk operations may require trusted device context.

---

## 36. Risk-Based Authorization

Authorization may incorporate risk signals.

Example:

```text
LOW RISK
    → Normal Access

MEDIUM RISK
    → Additional Verification

HIGH RISK
    → Step-Up Authentication

CRITICAL RISK
    → DENY
```

---

## 37. Step-Up Authorization

High-risk operations shall support stronger authentication.

Examples:

```text
Delete Organization
Create Super Admin
Export Customer Database
Generate Privileged API Key
Modify Security Policy
Change Billing Ownership
```

---

## 38. Privileged Access

Privileged access shall be subject to:

```text
MFA
Least Privilege
Short Session
Audit Logging
Approval
Risk Evaluation
```

where configured.

---

## 39. Just-In-Time Access

SalesGenie should support temporary privileged access for sensitive administrative operations.

---

## 40. Approval-Based Access

High-risk permissions may require approval by an authorized administrator.

---

## 41. Separation of Duties

Sensitive administrative operations may require multiple independent roles.

Example:

```text
Requester
    ≠
Approver
```

---

## 42. Break-Glass Access

Emergency access may be supported under strict controls.

Break-glass authorization shall be:

```text
Explicit
Time-Limited
Audited
Alerted
Revocable
```

---

## 43. API Access Control

Every protected API endpoint shall define:

```text
Authentication Requirement
Required Permission
Tenant Scope
Resource Scope
Action
Rate Limit
Risk Level
```

---

## 44. API Scope

API clients shall use granular scopes.

Example:

```text
leads:read
leads:write
contacts:read
conversations:read
workflows:execute
billing:read
```

---

## 45. API Key Authorization

API keys shall be associated with:

```text
Tenant
Owner
Application
Scopes
Expiration
Status
```

---

## 46. API Key Least Privilege

API keys shall not automatically inherit the owner's complete privileges.

---

## 47. Service-to-Service Authorization

Internal service calls shall be authorized based on service identity and service permissions.

Example:

```text
AI Gateway
    |
    +── lead-intelligence:read
    +── rag-service:query
    +── workflow-service:execute
```

---

## 48. Service Identity Isolation

A service shall not automatically access every internal database or service.

---

## 49. Microservice Authorization Matrix

Example:

| Caller           | Resource            | Action     | Expected |
| ---------------- | ------------------- | ---------- | -------- |
| AI Gateway       | RAG Service         | Query      | ALLOW    |
| AI Gateway       | Billing DB          | Write      | DENY     |
| Billing Service  | Billing DB          | Read/Write | ALLOW    |
| Lead Service     | Billing DB          | Read       | DENY     |
| Workflow Service | Integration Service | Execute    | ALLOW    |
| Unknown Service  | Any Service         | Any        | DENY     |

---

## 50. Background Worker Access

Workers shall receive only the permissions necessary for their job.

---

## 51. Job-Specific Authorization

A background worker executing:

```text
lead_enrichment
```

shall not automatically gain:

```text
billing:write
user:delete
security:manage
```

---

## 52. AI Access Control

Every AI agent shall have an independent authorization profile.

Example:

```text
agent_id
tenant_id
roles
permissions
tools
integrations
data_scopes
risk_level
```

---

## 53. AI Agent Permission Boundary

AI agents shall operate within an explicit permission boundary.

---

## 54. AI Human Permission Separation

The following shall not be assumed:

```text
Human Permission
        =
AI Permission
```

Instead:

```text
Human Permission
        |
        v
Delegation Policy
        |
        v
AI Permission
```

---

## 55. AI Delegation

Delegated AI access shall specify:

```text
initiating_user
agent
tenant
task
resource
action
tool
expiration
risk_level
```

---

## 56. AI Privilege Ceiling

An AI agent's effective privileges shall be bounded by:

```text
Agent Policy
∩
Delegated User Scope
∩
Tenant Policy
∩
Resource Policy
```

---

## 57. AI Tool Authorization

The AI model shall not directly authorize its own tool execution.

Tool calls shall pass through the platform authorization layer.

---

## 58. AI Tool Permission Matrix

Example:

| AI Agent       | Tool         | Permission       | Expected |
| -------------- | ------------ | ---------------- | -------- |
| Sales Agent    | Lead Search  | lead:read        | ALLOW    |
| Sales Agent    | Lead Update  | lead:update      | ALLOW    |
| Sales Agent    | Billing Tool | billing:write    | DENY     |
| Support Agent  | Ticket Tool  | ticket:update    | ALLOW    |
| Research Agent | Web Search   | research:execute | ALLOW    |
| Research Agent | User Admin   | user:delete      | DENY     |

---

## 59. AI Prompt Injection Protection

Prompt content shall never grant authorization.

```text
User Prompt
     |
     v
AI Model
     |
     v
Tool Request
     |
     v
Authorization Engine
     |
     v
ALLOW / DENY
```

---

## 60. AI Agent Impersonation Prevention

An AI agent shall not claim to be:

```text
Another User
Another Admin
Another Agent
Another Service
```

without an explicitly authorized identity transition.

---

## 61. AI-to-AI Authorization

Agent-to-agent communication shall be authorized.

Example:

```text
Orchestrator
    |
    v
Research Agent
```

must be explicitly permitted.

---

## 62. Multi-Agent Isolation

One AI agent shall not automatically access another agent's:

```text
Memory
Credentials
Tools
Permissions
Integrations
Private Data
```

---

## 63. Agent Memory Authorization

AI memory access shall be subject to:

```text
Tenant
Agent
User
Resource
Data Classification
Permission
```

---

## 64. AI Data Access

AI agents shall only retrieve data that their authorization context permits.

---

## 65. AI Export Restrictions

AI agents shall not export protected data unless explicitly authorized.

---

## 66. Human Approval for High-Risk AI Operations

AI agents shall support human approval for configured high-risk actions.

Examples:

```text
Delete Lead Database
Delete User
Create Admin
Change Permissions
Export Customer Data
Change Billing
Connect Privileged Integration
```

---

## 67. Workflow Access Control

Every workflow shall have:

```text
workflow_id
tenant_id
owner_id
permissions
allowed_tools
allowed_integrations
execution_policy
```

---

## 68. Workflow Execution Authorization

Every workflow execution shall verify that the initiating actor is authorized to execute the workflow.

---

## 69. Workflow Tool Authorization

A workflow shall only invoke explicitly permitted tools.

---

## 70. Workflow Service Authorization

A workflow shall only invoke authorized services.

---

## 71. Workflow Privilege Escalation Protection

A workflow shall not dynamically grant itself additional permissions.

---

## 72. Workflow Delegation

Workflow delegation shall preserve:

```text
Human Identity
Agent Identity
Workflow Identity
Tenant Identity
Execution Identity
```

---

## 73. Workflow Execution Chain

Example:

```text
Human
  |
  v
AI Orchestrator
  |
  v
Workflow
  |
  v
Agent
  |
  v
Tool
  |
  v
Integration
  |
  v
External API
```

Every transition shall be authorized.

---

## 74. Integration Access Control

Every integration shall have a tenant-bound access policy.

---

## 75. Integration Permissions

Example:

```text
gmail:read
gmail:send
drive:read
slack:send
salesforce:read
salesforce:write
hubspot:read
hubspot:write
zendesk:read
zendesk:write
jira:read
jira:create
```

---

## 76. Integration Scope Minimization

Only required third-party scopes shall be requested.

---

## 77. Integration User Authorization

Users shall only connect integrations if they have the appropriate integration permission.

---

## 78. Integration Execution Authorization

AI agents and workflows shall not use integrations unless authorized.

---

## 79. Integration Disconnect Authorization

Disconnect operations shall require appropriate authorization.

---

## 80. Webhook Access Control

Webhook processing shall validate:

```text
Provider
Integration
Signature
Tenant
Event Type
Resource
```

---

## 81. MCP Access Control

MCP clients shall authenticate and authorize tool access.

---

## 82. MCP Tool Authorization

An MCP tool invocation shall evaluate:

```text
client_identity
tenant
user
agent
tool
resource
action
scope
```

---

## 83. MCP Resource Authorization

MCP resources shall enforce the same tenant and authorization boundaries as native SalesGenie resources.

---

## 84. Database Access Control

Application services shall not bypass authorization by directly exposing database access.

---

## 85. Data Layer Tenant Enforcement

Where feasible, tenant isolation should be reinforced at the data layer.

Possible mechanisms:

```text
Tenant-Aware Repository
Row-Level Security
Database Policies
Schema Isolation
```

---

## 86. Resource-Level Authorization

Authorization shall be evaluated at resource level when necessary.

Example:

```text
lead:read
```

does not necessarily mean:

```text
every lead in the tenant
```

if the organization uses owner/team restrictions.

---

## 87. Data Classification

Sensitive resources may have classifications:

```text
PUBLIC
INTERNAL
CONFIDENTIAL
RESTRICTED
HIGHLY_RESTRICTED
```

---

## 88. Classification-Based Access

Restricted data shall require appropriate permissions.

---

## 89. Export Authorization

Export operations shall require explicit permission.

Example:

```text
lead:export
customer_data:export
analytics:export
audit:export
```

---

## 90. Bulk Operation Authorization

Bulk operations shall use stronger authorization than individual low-risk operations where appropriate.

Examples:

```text
Bulk Delete
Bulk Export
Bulk Role Assignment
Bulk User Suspension
Bulk Credential Revocation
```

---

## 91. Delete Authorization

Deletion shall require explicit delete permission.

---

## 92. Soft Delete

Sensitive resources should support soft deletion where operationally appropriate.

---

## 93. Destructive Action Confirmation

High-impact destructive operations shall require explicit confirmation.

---

## 94. Audit Log Access

Audit logs shall be accessible only to authorized users.

---

## 95. Audit Log Tamper Protection

Users who can read audit logs shall not automatically be able to modify or delete them.

---

## 96. Security Policy Access

Security configuration shall require privileged permissions.

---

## 97. Billing Access

Billing permissions shall be separated from ordinary sales and support permissions.

Example:

```text
billing:read
billing:manage
subscription:manage
invoice:read
payment:manage
```

---

## 98. Administrative Access

Administrative permissions shall be granular.

Example:

```text
user:read
user:create
user:update
user:suspend
role:assign
security:manage
audit:read
integration:manage
billing:manage
```

---

## 99. Super Admin Access

Super Admin permissions shall be restricted to platform-level operations.

---

## 100. Super Admin Tenant Boundary

Super Admin operations shall require explicit platform-level authorization and shall be heavily audited.

---

## 101. Administrative Impersonation

If administrative impersonation is supported, it shall:

```text
Require Explicit Permission
Display Impersonation State
Preserve Original Admin Identity
Preserve Target Identity
Be Time-Limited
Be Audited
```

---

## 102. Access Request Workflow

Where enabled:

```text
User
  |
  v
Access Request
  |
  v
Manager/Admin
  |
  v
Approval
  |
  v
Temporary Permission
  |
  v
Expiration
```

---

## 103. Access Review

Organizations should periodically review:

```text
Users
Roles
Permissions
AI Agents
Workflows
Service Accounts
API Keys
Integrations
```

---

## 104. Permission Creep Detection

SalesGenie should identify identities whose privileges exceed their operational requirements.

---

## 105. Dormant Access Detection

The system should identify unused permissions.

---

## 106. Orphaned Permission Detection

The system shall identify permissions associated with:

```text
Deleted Users
Deleted Agents
Deleted Workflows
Deleted Services
Deleted Integrations
```

---

## 107. Access Revocation

Access revocation shall support:

```text
User
Role
Permission
Session
Token
API Key
AI Agent
Workflow
Service
Integration
```

---

## 108. Emergency Access Revocation

Security administrators shall be able to revoke access rapidly during incidents.

---

## 109. Global User Revocation

Authorized security administrators shall be able to revoke all active access for a compromised user.

---

## 110. Global Agent Revocation

Authorized security administrators shall be able to disable an AI agent and terminate active authorized executions.

---

## 111. Global Integration Revocation

Authorized administrators shall be able to disable an integration and invalidate local authorization.

---

## 112. Authorization Audit Logging

Every sensitive authorization decision should be auditable.

---

## 113. Authorization Event Schema

Events should include:

```text
event_id
timestamp
request_id
actor_id
actor_type
tenant_id
resource_id
resource_type
action
decision
policy_id
role
permissions
delegation_context
source_ip
device_id
risk_level
reason
```

---

## 114. Denied Access Logging

Security-relevant denied requests shall be logged.

---

## 115. Authorization Decision Reason

Where appropriate, authorization systems should expose machine-readable denial reasons without revealing sensitive policy information.

Example:

```text
TENANT_MISMATCH
INSUFFICIENT_PERMISSION
RESOURCE_NOT_VISIBLE
ROLE_REQUIRED
MFA_REQUIRED
TOKEN_EXPIRED
AGENT_SCOPE_EXCEEDED
WORKFLOW_NOT_AUTHORIZED
```

---

## 116. Access Monitoring

SalesGenie shall monitor:

```text
Authorization Failures
Privilege Escalation Attempts
Cross-Tenant Attempts
Admin Access
Bulk Exports
Bulk Deletes
AI Tool Denials
Workflow Authorization Failures
Service Authorization Failures
API Scope Violations
```

---

## 117. Authorization Anomaly Detection

The platform should detect unusual access patterns.

Examples:

```text
Sudden Permission Expansion
Mass Resource Access
Unusual Tenant Access
Unusual Admin Activity
Abnormal AI Tool Usage
Repeated Authorization Failures
```

---

## 118. Automated Access Response

Security automation may:

```text
Deny Request
Require MFA
Revoke Session
Suspend User
Disable API Key
Suspend AI Agent
Suspend Workflow
Disable Integration
```

based on configured policies.

---

## 119. Policy Versioning

Authorization policies shall support versioning.

---

## 120. Policy Rollback

Administrators shall be able to safely roll back policy changes where supported.

---

## 121. Policy Change Audit

All privileged policy changes shall be audited.

---

## 122. Policy Testing

Authorization policies shall be tested before production activation where practical.

---

## 123. Policy Simulation

The platform should support policy simulation.

Example:

```text
"What would SALES_AGENT be allowed to access?"
```

without actually modifying permissions.

---

## 124. Effective Permission Calculation

The platform shall calculate effective permissions from:

```text
Direct Permissions
+
Role Permissions
+
Team Permissions
+
Resource Permissions
+
Temporary Grants
+
Policy Constraints
-
Explicit Denials
```

subject to the platform's policy precedence model.

---

## 125. Explicit Deny

The authorization engine should support explicit deny policies for high-risk controls.

---

## 126. Policy Precedence

SalesGenie shall define deterministic precedence rules for:

```text
Allow
Deny
Role
Resource Policy
Tenant Policy
Platform Policy
Delegation Policy
```

---

## 127. Permission Conflict Resolution

Conflicting policies shall resolve deterministically and fail securely.

---

## 128. Access Control API

The authorization service should expose internal APIs for:

```text
Check Permission
Check Resource Access
Evaluate Policy
List Effective Permissions
List Roles
Grant Permission
Revoke Permission
Create Policy
Update Policy
Delete Policy
Simulate Policy
```

---

## 129. Authorization API Example

Conceptual request:

```json
{
  "actor": {
    "id": "user-123",
    "type": "HUMAN"
  },
  "tenant_id": "tenant-456",
  "resource": {
    "type": "lead",
    "id": "lead-789"
  },
  "action": "update",
  "context": {
    "agent_id": null,
    "workflow_id": null
  }
}
```

Expected response:

```json
{
  "decision": "ALLOW",
  "reason": "PERMISSION_GRANTED"
}
```

---

## 130. Authorization Performance

Authorization checks shall be optimized to avoid materially degrading API latency.

---

## 131. Authorization Availability

Authorization infrastructure shall be highly available because protected services depend on it.

---

## 132. Authorization Failure Handling

If authorization infrastructure becomes unavailable:

```text
Sensitive Operations
        |
        v
      DENY
```

No insecure bypass shall be introduced.

---

## 133. Authorization Cache Security

Cached authorization decisions shall:

```text
Have TTL
Be Tenant-Aware
Be Identity-Aware
Be Policy-Aware
Be Invalidated on Critical Changes
```

---

## 134. Access Control Consistency

All microservices shall follow the same authorization model.

---

## 135. Central Policy Contracts

Authorization semantics shall be defined centrally to prevent inconsistent service behavior.

---

## 136. Frontend Access Control

The frontend may hide unauthorized UI elements.

Examples:

```text
Admin Menu
Delete Button
Billing Controls
API Key Management
Integration Management
```

However:

```text
Frontend Restriction != Security Boundary
```

---

## 137. Backend Enforcement

Every protected frontend action shall also be enforced by the backend.

---

## 138. GraphQL Access Control

If GraphQL is used, authorization shall occur at field/resource/action boundaries as appropriate.

---

## 139. WebSocket Access Control

WebSocket connections shall validate identity and permissions.

---

## 140. Real-Time Subscription Authorization

Users shall only subscribe to events belonging to authorized tenants and resources.

---

## 141. File Access Control

Documents and files shall enforce:

```text
Tenant
Owner
Team
Role
Permission
Classification
```

---

## 142. Knowledge Base Access Control

RAG retrieval shall enforce document-level authorization.

An AI agent shall not retrieve documents unavailable to its authorization context.

---

## 143. RAG Authorization Flow

```text
User
  |
  v
AI Agent
  |
  v
Authorization Context
  |
  v
Retriever
  |
  v
Permission Filter
  |
  v
Authorized Documents
  |
  v
LLM
```

---

## 144. Vector Database Authorization

Vector search shall apply tenant and permission filters before returning protected documents.

---

## 145. Conversation Access Control

Conversations shall support appropriate visibility:

```text
PRIVATE
TEAM
ORGANIZATION
CUSTOMER
ADMIN
```

according to product policy.

---

## 146. Customer Data Access

Customer records shall only be accessible to authorized actors.

---

## 147. Lead Access Control

Lead visibility may be constrained by:

```text
Owner
Team
Organization
Role
Tenant
```

---

## 148. Sales Pipeline Access

Pipeline operations shall require appropriate permissions.

---

## 149. Support Ticket Access

Support tickets shall enforce tenant and role-based access.

---

## 150. Analytics Access Control

Analytics visibility shall follow tenant and role boundaries.

---

## 151. Billing Analytics Access

Billing analytics shall require billing or authorized administrative permissions.

---

## 152. Usage Data Access

Usage information shall be tenant-isolated and role-restricted.

---

## 153. Subscription Access

Subscription management shall require explicit billing permissions.

---

## 154. Security Dashboard Access

Security dashboards shall be limited to authorized security and administrative roles.

---

## 155. Audit Dashboard Access

Audit dashboards shall be limited to authorized roles.

---

## 156. Access Control for Human + AI Collaboration

SalesGenie shall preserve authorization context across:

```text
Human
  ↓
AI Agent
  ↓
Workflow
  ↓
Tool
  ↓
Integration
  ↓
External System
```

The system shall prevent authorization context from being silently broadened at any step.

---

## 157. Delegation Token

Delegated AI execution may use a signed delegation context containing:

```text
initiator_id
tenant_id
agent_id
workflow_id
allowed_actions
allowed_resources
allowed_tools
issued_at
expires_at
delegation_id
```

---

## 158. Delegation Token Restrictions

Delegation credentials shall:

```text
Be Short-Lived
Be Scoped
Be Non-Transferable
Be Auditable
Be Revocable
```

where applicable.

---

## 159. AI Authorization Invariant

The following must always hold:

```text
Effective AI Permissions
    <=
Explicit Delegated Permissions
```

---

## 160. Workflow Authorization Invariant

The following must always hold:

```text
Effective Workflow Permissions
    <=
Configured Workflow Permissions
```

---

## 161. Service Authorization Invariant

The following must always hold:

```text
Service Action
    <=
Service Identity Permissions
```

---

## 162. Integration Authorization Invariant

The following must always hold:

```text
Integration Action
    <=
Integration Scope
```

---

## 163. User Authorization Invariant

The following must always hold:

```text
User Action
    <=
Effective User Permissions
```

---

## 164. Tenant Authorization Invariant

The following must always hold:

```text
Actor Tenant
    ==
Resource Tenant
```

unless explicitly authorized platform-level access exists.

---

## 165. Access Control Test Matrix

SalesGenie shall test at minimum:

| Scenario                              | Expected Result |
| ------------------------------------- | --------------- |
| User reads authorized lead            | ALLOW           |
| User reads unauthorized lead          | DENY            |
| User accesses another tenant          | DENY            |
| Sales Agent updates lead              | ALLOW           |
| Sales Agent manages billing           | DENY            |
| Billing Admin manages billing         | ALLOW           |
| Org Admin manages own tenant          | ALLOW           |
| Org Admin manages another tenant      | DENY            |
| User assigns self Admin role          | DENY            |
| AI reads delegated leads              | ALLOW           |
| AI accesses undelegated billing       | DENY            |
| AI executes unauthorized tool         | DENY            |
| Workflow executes authorized tool     | ALLOW           |
| Workflow executes unauthorized tool   | DENY            |
| Service calls authorized service      | ALLOW           |
| Service accesses unauthorized service | DENY            |
| API key uses permitted scope          | ALLOW           |
| API key exceeds scope                 | DENY            |
| Revoked API key                       | DENY            |
| Expired delegation                    | DENY            |
| Disabled user                         | DENY            |
| Revoked session                       | DENY            |
| MCP client uses authorized tool       | ALLOW           |
| MCP client uses unauthorized tool     | DENY            |
| Unauthorized export                   | DENY            |
| Unauthorized bulk delete              | DENY            |

---

## 166. Security Testing Requirements

Access control testing shall include:

```text
RBAC Testing
ABAC Testing
Tenant Isolation Testing
Horizontal Privilege Escalation
Vertical Privilege Escalation
IDOR Testing
Object-Level Authorization
Function-Level Authorization
API Authorization
JWT Claim Manipulation
Role Manipulation
Permission Manipulation
AI Authorization Bypass
Prompt Injection
Tool Abuse
Workflow Privilege Escalation
MCP Authorization Bypass
Integration Scope Abuse
Service Identity Abuse
Bulk Operation Abuse
```

---

## 167. Property-Based Authorization Testing

The platform should test security invariants across generated combinations of:

```text
Users
Roles
Tenants
Resources
Actions
Agents
Workflows
Services
Integrations
```

---

## 168. Fuzzing

Authorization APIs shall be tested against malformed:

```text
Tenant IDs
User IDs
Resource IDs
Role IDs
Permission IDs
JWT Claims
API Parameters
Delegation Contexts
```

---

## 169. Access Control Threat Model

Threat actors include:

```text
Unauthenticated Attacker
Compromised User
Malicious User
Malicious Admin
Compromised API Client
Compromised AI Agent
Prompt Injection Attacker
Malicious Workflow
Compromised Integration
Compromised Service
Malicious Insider
Cross-Tenant Attacker
```

---

## 170. Threat Scenarios

SalesGenie shall defend against:

```text
Changing resource IDs
Changing tenant IDs
Forging roles
Forging permissions
Forging AI identities
Replaying delegation tokens
Calling hidden APIs
Calling admin endpoints
Bypassing frontend restrictions
Using stale permissions
Abusing integrations
Abusing service accounts
Using AI prompts to bypass policy
Using workflows to escalate privileges
```

---

## 171. Access Control Monitoring Metrics

SalesGenie shall track:

```text
Authorization Requests
Authorization Allows
Authorization Denials
Authorization Latency
Cross-Tenant Denials
Privilege Escalation Attempts
Policy Violations
AI Tool Denials
Workflow Denials
Service Authorization Failures
API Scope Violations
Temporary Access Grants
Temporary Access Expirations
Role Changes
Permission Changes
Access Revocations
```

---

## 172. Security Alerts

Alerts shall be generated for high-risk events.

Examples:

```text
Repeated Cross-Tenant Attempts
Repeated Privilege Escalation
Mass Permission Changes
Mass Role Changes
Unexpected Admin Access
AI Scope Violation
Workflow Scope Violation
Service Authorization Anomaly
Large Data Export
Unauthorized Billing Access
```

---

## 173. Access Control Incident Response

The platform shall support rapid:

```text
User Suspension
Session Revocation
Token Revocation
API Key Revocation
Agent Suspension
Workflow Suspension
Service Credential Revocation
Integration Disablement
Permission Revocation
Role Revocation
```

---

## 174. Access Review Requirements

Periodic reviews shall evaluate:

```text
Excessive Permissions
Unused Permissions
Privileged Accounts
Temporary Grants
AI Agent Permissions
Workflow Permissions
Service Permissions
API Key Scopes
Integration Scopes
```

---

## 175. Compliance and Governance

Access control shall support enterprise security requirements for:

```text
Least Privilege
Separation of Duties
Access Reviews
Privileged Access
Auditability
Identity Lifecycle
Data Isolation
Security Monitoring
```

---

## 176. Access Control CI/CD Gates

Production deployments shall validate:

```text
[ ] Authentication Tests
[ ] RBAC Tests
[ ] ABAC Tests
[ ] Tenant Isolation Tests
[ ] IDOR Tests
[ ] Privilege Escalation Tests
[ ] API Authorization Tests
[ ] AI Authorization Tests
[ ] Workflow Authorization Tests
[ ] Service Authorization Tests
[ ] Integration Authorization Tests
[ ] MCP Authorization Tests
[ ] RAG Authorization Tests
[ ] Billing Authorization Tests
[ ] Audit Logging Tests
[ ] Revocation Tests
[ ] Policy Regression Tests
```

---

## 177. Access Control Acceptance Criteria

## AC-ACCESS-001

Every protected API operation requires authorization.

## AC-ACCESS-002

Every tenant-scoped resource validates tenant ownership.

## AC-ACCESS-003

Cross-tenant access is denied by default.

## AC-ACCESS-004

Users cannot grant themselves privileges.

## AC-ACCESS-005

Users cannot modify their own administrative roles.

## AC-ACCESS-006

RBAC permissions are enforced server-side.

## AC-ACCESS-007

ABAC policies are evaluated where configured.

## AC-ACCESS-008

Resource ownership restrictions are enforced.

## AC-ACCESS-009

Team restrictions are enforced.

## AC-ACCESS-010

Temporary permissions expire automatically.

## AC-ACCESS-011

Permission revocation propagates within the defined security SLO.

## AC-ACCESS-012

API keys are scope-limited.

## AC-ACCESS-013

Service identities are independently authorized.

## AC-ACCESS-014

AI agents have explicit permission boundaries.

## AC-ACCESS-015

AI agents cannot automatically inherit unrestricted human permissions.

## AC-ACCESS-016

AI tool calls are authorization-controlled.

## AC-ACCESS-017

AI agents cannot obtain privileges through prompt instructions.

## AC-ACCESS-018

AI-to-AI operations are authorized.

## AC-ACCESS-019

Workflow execution is authorization-controlled.

## AC-ACCESS-020

Workflow tools are explicitly authorized.

## AC-ACCESS-021

Integration access is tenant-bound.

## AC-ACCESS-022

MCP tools enforce authorization.

## AC-ACCESS-023

RAG retrieval enforces document authorization.

## AC-ACCESS-024

Unauthorized exports are denied.

## AC-ACCESS-025

Unauthorized destructive operations are denied.

## AC-ACCESS-026

Privileged operations support step-up authentication where configured.

## AC-ACCESS-027

Access decisions are auditable.

## AC-ACCESS-028

Denied security-sensitive requests are logged.

## AC-ACCESS-029

Policy changes are audited.

## AC-ACCESS-030

Emergency access revocation is supported.

## AC-ACCESS-031

Authorization failures fail closed.

## AC-ACCESS-032

Authorization policies are regression-tested.

## AC-ACCESS-033

Frontend authorization controls never replace backend enforcement.

## AC-ACCESS-034

Disabled identities cannot access protected resources.

## AC-ACCESS-035

Revoked credentials cannot authorize protected operations.

---

## 178. FAANG-Level Access Control Quality Gates

```text
[ ] Zero-trust authorization
[ ] Deny-by-default
[ ] Least privilege
[ ] Central authorization model
[ ] Policy decision point
[ ] Policy enforcement point
[ ] RBAC
[ ] ABAC
[ ] Resource-based authorization
[ ] Tenant-aware authorization
[ ] Ownership-based authorization
[ ] Team-based authorization
[ ] Explicit permissions
[ ] Granular CRUD permissions
[ ] Execute permissions
[ ] Export permissions
[ ] Approval permissions
[ ] Administrative permissions
[ ] Explicit deny
[ ] Deterministic policy precedence
[ ] Permission versioning
[ ] Policy versioning
[ ] Policy simulation
[ ] Policy testing
[ ] Policy rollback
[ ] Permission expiration
[ ] Temporary access
[ ] Just-in-time access
[ ] Separation of duties
[ ] Break-glass access
[ ] Privileged access controls
[ ] API authorization
[ ] API scopes
[ ] API key authorization
[ ] Service-to-service authorization
[ ] Service identity isolation
[ ] Worker authorization
[ ] AI identity authorization
[ ] AI delegation
[ ] AI privilege ceiling
[ ] AI tool authorization
[ ] AI-to-AI authorization
[ ] Prompt-injection-resistant authorization
[ ] Workflow authorization
[ ] Workflow identity isolation
[ ] Integration authorization
[ ] OAuth scope enforcement
[ ] Webhook authorization
[ ] MCP authorization
[ ] RAG authorization
[ ] Vector-level authorization
[ ] File authorization
[ ] Conversation authorization
[ ] Lead authorization
[ ] Ticket authorization
[ ] Billing authorization
[ ] Subscription authorization
[ ] Analytics authorization
[ ] Audit authorization
[ ] Security-dashboard authorization
[ ] Frontend permission controls
[ ] Backend authorization enforcement
[ ] Cross-tenant isolation
[ ] IDOR protection
[ ] Horizontal privilege protection
[ ] Vertical privilege protection
[ ] Self-privilege escalation protection
[ ] Bulk-operation protection
[ ] Authorization caching controls
[ ] Cache invalidation
[ ] Authorization audit logs
[ ] Authorization monitoring
[ ] Anomaly detection
[ ] Automated access response
[ ] Emergency revocation
[ ] Access reviews
[ ] Permission creep detection
[ ] Orphaned permission detection
[ ] Security testing
[ ] Fuzz testing
[ ] Property-based authorization testing
[ ] CI/CD authorization gates
[ ] Security invariants
```

---

## 179. Core Access-Control Security Invariants

The following invariants shall always hold:

```text
1. Authentication does not imply authorization.

2. No explicit authorization means DENY.

3. Every protected resource has an authorization boundary.

4. Every tenant-scoped resource is tenant-isolated.

5. Client-supplied tenant IDs never independently determine authorization.

6. A user cannot grant themselves additional privileges.

7. A lower-privileged user cannot invoke privileged functions.

8. A user cannot access another user's resource without authorization.

9. A tenant administrator cannot access another tenant by manipulating IDs.

10. An AI agent cannot automatically inherit unrestricted human permissions.

11. AI permissions cannot exceed explicit delegation.

12. AI model output cannot grant authorization.

13. AI tool execution requires authorization.

14. AI-to-AI communication requires authorization.

15. Workflow execution requires authorization.

16. Workflow permissions cannot expand dynamically without policy approval.

17. Service identities are independently authorized.

18. Integrations are tenant-bound.

19. API keys are scope-limited.

20. Expired permissions cannot authorize operations.

21. Revoked permissions cannot authorize operations.

22. Disabled identities cannot access protected resources.

23. Sensitive exports require explicit authorization.

24. Destructive operations require explicit authorization.

25. Privileged operations require stronger controls where configured.

26. Authorization decisions are auditable.

27. Security-sensitive denials are observable.

28. Authorization failures fail closed.

29. Frontend restrictions never replace backend authorization.

30. RAG retrieval cannot return documents outside the caller's authorization scope.

31. Vector search cannot bypass document permissions.

32. MCP tools cannot bypass SalesGenie authorization.

33. Delegation cannot broaden the initiating identity's allowed scope.

34. Authorization cache cannot preserve revoked privileges beyond its security SLO.

35. Policy changes are auditable and attributable.

36. Cross-tenant authorization is denied by default.

37. Every machine identity has a bounded permission set.

38. Every privileged operation has an attributable actor.

39. Human and AI identities remain distinguishable.

40. Authorization policy remains independently enforceable from AI-generated instructions.
```

---

## 180. Reference Authorization Flow

```text
                              REQUEST
                                 |
                                 v
                         +---------------+
                         | Authentication|
                         +-------+-------+
                                 |
                                 v
                         +---------------+
                         | Identity      |
                         | Resolution    |
                         +-------+-------+
                                 |
                                 v
                         +---------------+
                         | Tenant        |
                         | Resolution    |
                         +-------+-------+
                                 |
                                 v
                    +------------+-------------+
                    |                          |
                    v                          v
                  HUMAN                     MACHINE
                    |                          |
                    |                 +--------+--------+
                    |                 |                 |
                    v                 v                 v
                  User              AI Agent          Service
                    |                 |                 |
                    +--------+--------+-----------------+
                             |
                             v
                    +-------------------+
                    | Delegation Context|
                    +---------+---------+
                              |
                              v
                    +-------------------+
                    | Role / Permissions|
                    +---------+---------+
                              |
                              v
                    +-------------------+
                    | Resource Context  |
                    +---------+---------+
                              |
                              v
                    +-------------------+
                    | Policy Evaluation |
                    +---------+---------+
                              |
                     +--------+--------+
                     |                 |
                     v                 v
                   DENY              ALLOW
                     |                 |
                     |                 v
                     |        +----------------+
                     |        | Policy         |
                     |        | Enforcement    |
                     |        +-------+--------+
                     |                |
                     |                v
                     |            RESOURCE
                     |
                     v
                  AUDIT
                     ^
                     |
                   ALLOW
                     |
                     v
                  AUDIT
```

---

## 181. Definition of Done

`access_control.md` shall be considered fully implemented when SalesGenie can consistently enforce authorization across:

```text
Human Users
End Users
Sales Agents
Support Agents
Managers
Organization Admins
Security Admins
Billing Admins
Developers
Auditors
Super Admins

AI Agents
AI Orchestrators
AI Workers
AI Tools
AI Workflows
Workflow Executions

Microservices
Background Workers
Service Accounts
API Clients
API Keys
Integrations
Webhooks
MCP Clients
MCP Servers
```

and across:

```text
Organizations
Tenants
Teams
Users
Leads
Contacts
Companies
Conversations
Tickets
Customers
Knowledge Bases
Documents
Vector Stores
AI Agents
AI Tools
Workflows
Workflow Executions
Integrations
API Keys
Billing
Subscriptions
Invoices
Usage
Analytics
Security Configuration
Audit Logs
Administrative Resources
```

The final architecture shall guarantee:

```text
                    IDENTITY
                       |
                       v
                 AUTHENTICATION
                       |
                       v
                    TENANT
                       |
                       v
             ROLE + PERMISSIONS
                       |
                       v
              DELEGATION CONTEXT
                       |
                       v
             RESOURCE + OWNERSHIP
                       |
                       v
              ATTRIBUTE + RISK
                       |
                       v
                POLICY ENGINE
                       |
                +------+------+
                |             |
                v             v
              DENY          ALLOW
                              |
                              v
                     POLICY ENFORCEMENT
                              |
                              v
                    RESOURCE / TOOL / API
                              |
                              v
                           AUDIT
```

SalesGenie shall enforce **identity-aware, tenant-aware, least-privilege, policy-driven authorization for every human and machine action**, while ensuring that AI agents, workflows, integrations, services, and APIs cannot use delegation, model output, resource identifiers, inherited privileges, or frontend behavior to bypass the platform's authorization boundaries.
