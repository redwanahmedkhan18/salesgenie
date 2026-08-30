# SALESGENIE — RBAC REQUIREMENTS

**File:** `rbac.md`  
**Project:** SalesGenie  
**Document Type:** Role-Based Access Control (RBAC) — User Requirements, System Requirements & Functional Requirements  
**Version:** 1.0.0  
**Status:** Production Architecture Baseline  
**Security Classification:** Confidential  
**Target:** Enterprise / FAANG-Level Multi-Tenant SaaS

---

## 1. PURPOSE

This document defines the complete Role-Based Access Control (RBAC) architecture for SalesGenie.

RBAC is responsible for determining:

- Who can access a module
- Which resources a user can access
- Which actions a user can perform
- At which organizational scope the user can act
- Which permissions can be delegated
- Which permissions require approval
- Which AI agents can perform which actions
- Which human operators can override or approve AI actions

SalesGenie MUST combine RBAC with:

```text
RBAC
+
ABAC
+
ReBAC
+
Policy-Based Authorization
+
Tenant Isolation
+
Subscription Entitlements
+
Risk-Based Controls
+
Human Approval
```

RBAC MUST NOT be treated as the only authorization mechanism for high-risk operations.

---

## 2. RBAC VISION

SalesGenie MUST implement a centralized, hierarchical, scope-aware RBAC system.

Core model:

```text
USER
  |
  ↓
USER ROLE
  |
  ↓
ROLE
  |
  ↓
PERMISSIONS
  |
  ↓
RESOURCE
  |
  ↓
ACTION
  |
  ↓
SCOPE
  |
  ↓
POLICY
  |
  ↓
AUTHORIZATION DECISION
```

Example:

```text
Sales Agent
    |
    +-- lead:read
    +-- lead:create
    +-- lead:update
    +-- conversation:read
    +-- conversation:create
```

The role alone does not determine final authorization.

The system MUST also evaluate:

```text
Tenant
Workplace
Team
Resource Ownership
Subscription
Risk
Context
Approval
```

---

## 3. CORE RBAC PRINCIPLES

## RBAC-PRINCIPLE-001 — Default Deny

If a user does not possess the required permission:

```text
DENY
```

---

## RBAC-PRINCIPLE-002 — Least Privilege

Every role MUST contain only the minimum permissions required to perform its responsibilities.

---

## RBAC-PRINCIPLE-003 — Separation of Duties

Critical responsibilities SHOULD be distributed across multiple roles.

Example:

```text
Refund Request
      ↓
Billing Admin
      ↓
Refund Approval
      ↓
Authorized Approver
```

---

## RBAC-PRINCIPLE-004 — No Implicit Privilege

A role MUST NOT receive additional privileges simply because it belongs to a higher organizational level unless explicitly configured.

---

## RBAC-PRINCIPLE-005 — Scope Isolation

A role MAY be:

```text
Platform-scoped
Organization-scoped
Workplace-scoped
Team-scoped
Project-scoped
Resource-scoped
```

---

## RBAC-PRINCIPLE-006 — Server-Side Enforcement

RBAC MUST be enforced on the backend.

Frontend role checks are only UX controls.

---

## RBAC-PRINCIPLE-007 — AI Independence

AI agents MUST have their own roles and permissions.

An AI agent MUST NOT automatically inherit all permissions of the human who created it.

---

## 4. USER REQUIREMENTS

## UR-RBAC-001 — Role Assignment

Authorized administrators MUST be able to assign roles to users.

---

## UR-RBAC-002 — Role Removal

Authorized administrators MUST be able to revoke roles.

Role revocation MUST immediately or rapidly invalidate associated authorization caches.

---

## UR-RBAC-003 — Multiple Roles

SalesGenie MUST support multiple roles for a single user where organizational policy permits.

Example:

```text
User
 |
 +-- Sales Manager
 +-- Business Analyst
 +-- Marketing Manager
```

---

## UR-RBAC-004 — Scoped Roles

Users MUST be able to have roles limited to specific:

```text
Organization
Workplace
Team
Project
```

---

## UR-RBAC-005 — Role-Based Dashboard

After authentication, users MUST receive a dashboard based on their effective roles and permissions.

Example:

```text
Sales Agent
    ↓
Sales Dashboard

Marketing Manager
    ↓
Marketing Dashboard

Finance Manager
    ↓
Finance Dashboard
```

---

## UR-RBAC-006 — Permission-Based UI

Users MUST only see modules for which they have appropriate permissions.

---

## UR-RBAC-007 — Backend Protection

A hidden frontend module MUST NOT be considered security protection.

Unauthorized API calls MUST be rejected.

---

## UR-RBAC-008 — Resource-Level Permissions

Users MUST be able to access resources according to their role and scope.

---

## UR-RBAC-009 — Action-Level Permissions

RBAC MUST distinguish between:

```text
Read
Create
Update
Delete
Export
Approve
Publish
Execute
Assign
Manage
```

---

## UR-RBAC-010 — Read/Write Separation

A role with:

```text
resource:read
```

MUST NOT automatically receive:

```text
resource:update
```

---

## UR-RBAC-011 — Delete Protection

Delete permissions MUST be explicitly granted.

Critical deletion MAY require additional approval.

---

## UR-RBAC-012 — Export Protection

Export permissions MUST be separate from read permissions.

---

## UR-RBAC-013 — Role Management

Authorized administrators MUST be able to:

* Create roles
* Modify roles
* Deactivate roles
* Assign permissions
* Remove permissions
* Assign users
* Review role membership

---

## UR-RBAC-014 — Custom Roles

Enterprise organizations MUST be able to create custom roles.

---

## UR-RBAC-015 — Role Templates

SalesGenie SHOULD provide predefined role templates.

---

## UR-RBAC-016 — Temporary Roles

The system SHOULD support temporary role assignments.

Example:

```text
Sales Manager
Effective:
2026-08-22 09:00

Expires:
2026-08-30 18:00
```

---

## UR-RBAC-017 — Delegated Roles

Authorized users MAY delegate selected permissions to another user.

Delegation MUST be:

```text
Scoped
Time-limited
Audited
Revocable
```

---

## UR-RBAC-018 — Role Approval

Sensitive role assignments SHOULD require approval.

Example:

```text
Organization Admin
Security Admin
Billing Admin
```

---

## UR-RBAC-019 — Role History

Users with appropriate permission MUST be able to view:

```text
Role assigned
Role removed
Who performed action
When
Reason
Previous state
New state
```

---

## UR-RBAC-020 — Role Conflict Detection

The system SHOULD detect incompatible roles.

Example:

```text
Refund Requester
+
Refund Approver
```

may be prohibited by organizational policy.

---

## UR-RBAC-021 — AI Roles

AI agents MUST support role assignment.

Example:

```text
AI Sales Agent
AI Marketing Agent
AI SEO Agent
AI Support Agent
AI Business Analyst
```

---

## UR-RBAC-022 — AI Role Restrictions

AI roles MUST have restricted permissions.

AI agents MUST NOT automatically receive:

```text
super_admin
security_admin
billing_root
```

---

## UR-RBAC-023 — Human Approval

RBAC MUST integrate with human approval for sensitive AI actions.

---

## UR-RBAC-024 — Subscription-Based Role Capabilities

A role's available functionality MUST also respect subscription entitlements.

---

## UR-RBAC-025 — Auditability

All privileged RBAC operations MUST be auditable.

---

## 5. SYSTEM REQUIREMENTS

## SR-RBAC-001 — Central RBAC Service

SalesGenie SHOULD provide a centralized authorization/RBAC capability.

Conceptually:

```text
                +----------------------+
                |  RBAC / Policy       |
                |  Authorization       |
                |  Service             |
                +----------+-----------+
                           |
       +-------------------+-------------------+
       |                   |                   |
     Users               AI Agents          Services
       |                   |                   |
       +-------------------+-------------------+
                           |
                     Permissions
```

---

## SR-RBAC-002 — Role Registry

The system MUST maintain a centralized registry of roles.

---

## SR-RBAC-003 — Permission Registry

The system MUST maintain a centralized permission catalog.

---

## SR-RBAC-004 — Role-Permission Mapping

The system MUST maintain:

```text
Role
    ↓
Permissions
```

---

## SR-RBAC-005 — User-Role Mapping

The system MUST maintain:

```text
User
    ↓
Role
```

---

## SR-RBAC-006 — Scope Mapping

The system MUST maintain role scopes.

Example:

```text
User A
 |
 +-- Sales Manager
       |
       +-- Workplace A
```

---

## SR-RBAC-007 — Tenant Isolation

RBAC MUST enforce tenant isolation.

Example:

```text
Tenant A
   |
   +-- User A
       +-- Role
       +-- Permissions
```

User A MUST NOT automatically access:

```text
Tenant B
```

---

## SR-RBAC-008 — Workplace Isolation

Workplace-scoped roles MUST be restricted to authorized workplaces.

---

## SR-RBAC-009 — Team Isolation

Team-scoped roles MUST be restricted to authorized teams.

---

## SR-RBAC-010 — Resource Ownership

RBAC MUST integrate with resource ownership.

Example:

```text
Sales Agent
 |
 +-- Own Lead → Allowed
 +-- Other Agent Lead → Restricted
```

---

## SR-RBAC-011 — Permission Namespacing

Permissions SHOULD use:

```text
<resource>:<action>
```

Example:

```text
lead:read
lead:create
lead:update
lead:delete
lead:export
```

---

## SR-RBAC-012 — Permission Metadata

Every permission SHOULD contain:

```text
permission_id
name
resource
action
description
risk_level
scope
status
```

---

## SR-RBAC-013 — Role Metadata

Every role SHOULD contain:

```text
role_id
name
description
role_type
scope_type
status
system_role
created_by
created_at
updated_at
```

---

## SR-RBAC-014 — System Roles

Core system roles MUST be protected from unauthorized modification.

---

## SR-RBAC-015 — Custom Roles

Custom roles MUST be tenant-specific unless explicitly designed as platform-wide roles.

---

## SR-RBAC-016 — Role Versioning

Role definitions SHOULD be versioned.

---

## SR-RBAC-017 — Permission Versioning

Permission changes SHOULD be versioned.

---

## SR-RBAC-018 — Policy Evaluation

The authorization engine MUST evaluate:

```text
User
+
Role
+
Permission
+
Scope
+
Resource
+
Action
+
Policy
```

---

## SR-RBAC-019 — Authorization Decision

The system MUST support:

```text
ALLOW
DENY
REQUIRE_APPROVAL
REQUIRE_MFA
REQUIRE_REAUTHENTICATION
```

---

## SR-RBAC-020 — Fail Closed

If RBAC infrastructure fails during a critical authorization request:

```text
DENY
```

---

## SR-RBAC-021 — High Availability

RBAC infrastructure MUST support:

```text
Horizontal Scaling
Replication
Caching
Failover
Health Checks
Monitoring
```

---

## SR-RBAC-022 — Low Latency

RBAC evaluation SHOULD target:

```text
Cached:
< 10 ms

Central:
< 50 ms

Complex:
< 100 ms
```

---

## SR-RBAC-023 — Cache Invalidation

Role and permission changes MUST invalidate relevant cached authorization decisions.

---

## SR-RBAC-024 — Audit Logging

RBAC changes MUST generate audit events.

---

## SR-RBAC-025 — Security Monitoring

The system MUST monitor suspicious RBAC activity.

---

## SR-RBAC-026 — Privilege Escalation Prevention

The system MUST prevent users from granting themselves permissions they do not possess.

---

## SR-RBAC-027 — Role Delegation Control

Users MUST only delegate permissions that they are explicitly allowed to delegate.

---

## SR-RBAC-028 — Separation of Duties

The system MUST support role conflict policies.

---

## SR-RBAC-029 — API Authorization

All protected APIs MUST enforce RBAC or equivalent authorization.

---

## SR-RBAC-030 — Service Authorization

Service-to-service calls MUST use service identities and permissions.

---

## SR-RBAC-031 — AI Authorization

AI agents MUST be represented as authorization principals.

---

## SR-RBAC-032 — Tool Authorization

AI agent tool calls MUST be checked against permissions.

---

## SR-RBAC-033 — MCP Authorization

MCP tools MUST have explicit scopes.

---

## SR-RBAC-034 — RAG Authorization

AI retrieval MUST respect document-level permissions.

---

## SR-RBAC-035 — Subscription Authorization

Feature availability MUST be evaluated against subscription entitlements.

---

## SR-RBAC-036 — API Key Authorization

API keys MUST support granular scopes.

---

## SR-RBAC-037 — OAuth Authorization

OAuth scopes MUST be enforced.

---

## SR-RBAC-038 — Integration Authorization

Third-party integrations MUST respect both SalesGenie RBAC and external provider scopes.

---

## 6. FUNCTIONAL REQUIREMENTS

## FR-RBAC-001 — Create Role

Authorized administrators MUST be able to create custom roles.

Required fields:

```text
Role Name
Description
Scope
Permissions
Status
```

---

## FR-RBAC-002 — Update Role

Authorized administrators MUST be able to modify custom roles.

---

## FR-RBAC-003 — Delete Role

Authorized administrators MAY delete custom roles only when:

```text
No critical dependency exists
```

---

## FR-RBAC-004 — Deactivate Role

Roles SHOULD support:

```text
ACTIVE
INACTIVE
ARCHIVED
```

---

## FR-RBAC-005 — Assign Role

Authorized administrators MUST be able to assign a role to a user.

---

## FR-RBAC-006 — Remove Role

Authorized administrators MUST be able to remove a role.

---

## FR-RBAC-007 — Role Scope

Role assignment MUST support:

```text
Platform
Organization
Workplace
Team
Project
Resource
```

---

## FR-RBAC-008 — Role Expiration

Temporary roles MUST automatically expire.

---

## FR-RBAC-009 — Permission Assignment

Authorized administrators MUST be able to assign permissions to roles.

---

## FR-RBAC-010 — Permission Removal

Authorized administrators MUST be able to remove permissions from custom roles.

---

## FR-RBAC-011 — Permission Search

Administrators MUST be able to search permissions by:

```text
Resource
Action
Module
Risk
Scope
```

---

## FR-RBAC-012 — Role Search

Administrators MUST be able to search roles by:

```text
Role Name
Scope
Status
Organization
User
```

---

## FR-RBAC-013 — Role Details

Role details MUST show:

```text
Role Name
Description
Scope
Permissions
Users
Created By
Created At
Updated At
Status
```

---

## FR-RBAC-014 — User Permission View

Authorized administrators MUST be able to view a user's effective permissions.

---

## FR-RBAC-015 — Effective Permission Calculation

The system MUST calculate:

```text
Direct Permissions
+
Role Permissions
+
Scoped Permissions
+
Temporary Permissions
-
Explicit Restrictions
```

---

## FR-RBAC-016 — Permission Conflict

Explicit deny policies MUST override normal allow rules unless a higher-priority security policy explicitly permits otherwise.

---

## FR-RBAC-017 — Multiple Roles

The system MUST calculate effective permissions across multiple roles.

Example:

```text
User
 |
 +-- Sales Agent
 +-- Business Analyst
```

Effective permissions:

```text
Sales permissions
+
Business analysis permissions
```

---

## FR-RBAC-018 — Scope Conflict

If a permission exists globally but the user lacks authorization for the specific scope:

```text
DENY
```

---

## FR-RBAC-019 — Resource Authorization

The system MUST check whether the resource belongs to the user's authorized scope.

---

## FR-RBAC-020 — Action Authorization

The system MUST check whether the role contains the required action permission.

---

## FR-RBAC-021 — Read Authorization

Example:

```text
lead:read
```

must permit authorized reading only.

---

## FR-RBAC-022 — Create Authorization

Example:

```text
lead:create
```

must permit authorized lead creation.

---

## FR-RBAC-023 — Update Authorization

Example:

```text
lead:update
```

must permit authorized lead updates.

---

## FR-RBAC-024 — Delete Authorization

Example:

```text
lead:delete
```

must permit deletion only when explicitly authorized.

---

## FR-RBAC-025 — Export Authorization

Example:

```text
lead:export
```

must be independent from:

```text
lead:read
```

---

## FR-RBAC-026 — Approval Authorization

Example:

```text
campaign:approve
refund:approve
security:approve
```

must be independently controlled.

---

## FR-RBAC-027 — Publish Authorization

Publishing production content MUST require:

```text
content:publish
```

or equivalent.

---

## FR-RBAC-028 — Execute Authorization

Automation workflows MUST require:

```text
workflow:execute
```

---

## 7. ROLE HIERARCHY

SalesGenie SHOULD use logical organizational levels rather than unrestricted privilege inheritance.

Recommended hierarchy:

```text
PLATFORM
 |
 +-- Super Admin
 +-- Platform Admin
 +-- Security Admin
 +-- Billing Admin
 |
 ORGANIZATION
 |
 +-- Organization Owner
 +-- Organization Admin
 |
 WORKPLACE
 |
 +-- Workplace Admin
 |
 TEAM
 |
 +-- Team Manager
 |
 BUSINESS
 |
 +-- Sales Manager
 +-- Sales Agent
 +-- Marketing Manager
 +-- Marketing Specialist
 +-- SEO Manager
 +-- SEO Specialist
 +-- Product Manager
 +-- Finance Manager
 +-- Business Analyst
 +-- Support Manager
 +-- Support Agent
 |
 AI
 |
 +-- AI Agent Builder
 +-- AI Sales Agent
 +-- AI Marketing Agent
 +-- AI SEO Agent
 +-- AI Support Agent
 |
 CUSTOMER
 |
 +-- End User
 +-- External Client
```

Important:

> Organizational hierarchy MUST NOT automatically mean unrestricted permission inheritance.

---

## 8. CORE ROLE DEFINITIONS

## 8.1 SUPER ADMIN

Scope:

```text
PLATFORM
```

Capabilities:

```text
platform:manage
organization:manage
user:manage
role:manage
security:manage
system:manage
audit:read
```

Critical operations MUST require additional controls.

---

## 8.2 PLATFORM ADMIN

Scope:

```text
PLATFORM
```

Typical permissions:

```text
platform:read
platform:manage
organization:read
organization:manage
user:read
system:monitor
```

---

## 8.3 SECURITY ADMIN

Scope:

```text
PLATFORM / SECURITY
```

Typical permissions:

```text
security:read
security:investigate
security:manage
security:revoke_sessions
security:manage_policies
audit:read
```

---

## 8.4 BILLING ADMIN

Scope:

```text
PLATFORM / BILLING
```

Typical permissions:

```text
billing:read
billing:manage
invoice:read
invoice:create
refund:request
refund:approve
subscription:manage
```

---

## 8.5 ORGANIZATION OWNER

Scope:

```text
ORGANIZATION
```

Typical permissions:

```text
organization:read
organization:update
user:manage
team:manage
workplace:manage
billing:manage
integration:manage
analytics:read
```

---

## 8.6 ORGANIZATION ADMIN

Scope:

```text
ORGANIZATION
```

Typical permissions:

```text
organization:read
organization:update
user:manage
team:manage
workplace:manage
analytics:read
integration:manage
```

---

## 8.7 WORKPLACE ADMIN

Scope:

```text
WORKPLACE
```

Typical permissions:

```text
workplace:read
workplace:update
user:read
team:manage
analytics:read
workflow:manage
```

---

## 8.8 TEAM MANAGER

Scope:

```text
TEAM
```

Typical permissions:

```text
team:read
team:update
member:read
lead:read
lead:assign
analytics:read
```

---

## 8.9 SALES MANAGER

Typical permissions:

```text
lead:read
lead:create
lead:update
lead:assign
campaign:read
campaign:create
analytics:read
report:create
```

---

## 8.10 SALES AGENT

Typical permissions:

```text
lead:read
lead:create
lead:update
conversation:read
conversation:create
task:create
```

---

## 8.11 MARKETING MANAGER

Typical permissions:

```text
campaign:read
campaign:create
campaign:update
campaign:approve
campaign:publish
marketing_analytics:read
automation:manage
```

---

## 8.12 MARKETING SPECIALIST

Typical permissions:

```text
campaign:read
campaign:create
campaign:update
content:create
marketing_analytics:read
```

---

## 8.13 SEO MANAGER

Typical permissions:

```text
seo:read
seo:manage
seo:approve
seo:publish
seo_analytics:read
```

---

## 8.14 SEO SPECIALIST

Typical permissions:

```text
seo:read
seo:analyze
keyword:research
content:optimize
seo_analytics:read
```

---

## 8.15 PRODUCT MANAGER

Typical permissions:

```text
product:read
product:create
product:update
product:analyze
market_intelligence:read
product_strategy:create
```

---

## 8.16 FINANCE MANAGER

Typical permissions:

```text
finance:read
finance:analyze
profit_loss:read
revenue:read
expense:read
financial_report:create
financial_report:export
```

---

## 8.17 BUSINESS ANALYST

Typical permissions:

```text
analytics:read
analytics:create
report:create
market_intelligence:read
business_analysis:read
```

---

## 8.18 SUPPORT MANAGER

Typical permissions:

```text
ticket:read
ticket:manage
ticket:assign
support_analytics:read
support_agent:manage
escalation:manage
```

---

## 8.19 SUPPORT AGENT

Typical permissions:

```text
ticket:read
ticket:update
ticket:reply
ticket:escalate
conversation:read
```

---

## 8.20 AI AGENT BUILDER

Typical permissions:

```text
ai_agent:create
ai_agent:read
ai_agent:update
ai_agent:test
ai_agent:publish
tool:manage
```

Publishing highly privileged agents SHOULD require approval.

---

## 8.21 AI SALES AGENT

Typical permissions:

```text
lead:read
lead:score
lead:update
conversation:read
conversation:create
sales_analysis:read
```

---

## 8.22 AI MARKETING AGENT

Typical permissions:

```text
market:read
campaign:read
campaign:draft
marketing_analysis:read
content:create
```

Campaign publication SHOULD require policy authorization.

---

## 8.23 AI SEO AGENT

Typical permissions:

```text
seo:read
seo:analyze
keyword:research
content:optimize
```

---

## 8.24 AI SUPPORT AGENT

Typical permissions:

```text
ticket:read
conversation:read
response:draft
ticket:classify
ticket:route
```

---

## 8.25 END USER

Typical permissions:

```text
profile:read
profile:update
subscription:read
conversation:create
support:create
own_data:read
```

---

## 8.26 EXTERNAL CLIENT

Permissions MUST be explicitly granted.

Example:

```text
api:read
lead:read
analytics:read
report:read
```

---

## 9. PERMISSION CATALOG

## LEADS

```text
lead:read
lead:create
lead:update
lead:delete
lead:assign
lead:score
lead:enrich
lead:export
```

---

## CONTACTS

```text
contact:read
contact:create
contact:update
contact:delete
contact:export
```

---

## CAMPAIGNS

```text
campaign:read
campaign:create
campaign:update
campaign:delete
campaign:approve
campaign:publish
campaign:pause
campaign:export
```

---

## PRODUCTS

```text
product:read
product:create
product:update
product:delete
product:analyze
product:publish
```

---

## ANALYTICS

```text
analytics:read
analytics:create
analytics:update
analytics:export
analytics:share
```

---

## FINANCE

```text
finance:read
finance:analyze
finance:export
finance:manage
```

---

## BILLING

```text
billing:read
billing:manage
subscription:read
subscription:manage
invoice:read
invoice:create
refund:request
refund:approve
```

---

## USERS

```text
user:read
user:create
user:update
user:suspend
user:delete
user:assign_role
user:revoke_role
```

---

## ROLES

```text
role:read
role:create
role:update
role:delete
role:assign
role:revoke
role:delegate
```

---

## SECURITY

```text
security:read
security:investigate
security:manage
security:revoke_sessions
security:manage_policies
security:manage_devices
```

---

## AI

```text
ai_agent:read
ai_agent:create
ai_agent:update
ai_agent:delete
ai_agent:test
ai_agent:publish
ai_agent:execute
ai_tool:read
ai_tool:execute
ai_tool:manage
```

---

## WORKFLOWS

```text
workflow:read
workflow:create
workflow:update
workflow:delete
workflow:execute
workflow:publish
```

---

## KNOWLEDGE BASE

```text
kb:read
kb:create
kb:update
kb:delete
kb:publish
kb:share
```

---

## REPORTS

```text
report:read
report:create
report:update
report:delete
report:share
report:export
```

---

## 10. ROLE-PERMISSION MATRIX

| Role                 | Leads        | Marketing  | SEO        | Finance    | Billing     | Support      | Security     | Users     |
| -------------------- | ------------ | ---------- | ---------- | ---------- | ----------- | ------------ | ------------ | --------- |
| Super Admin          | Full         | Full       | Full       | Controlled | Full        | Full         | Full         | Full      |
| Platform Admin       | Admin        | Admin      | Admin      | Limited    | Limited     | Admin        | Limited      | Admin     |
| Security Admin       | Audit        | Audit      | Audit      | Audit      | Audit       | Audit        | Full         | Security  |
| Billing Admin        | None/Minimal | None       | None       | Billing    | Full        | None         | Audit        | Limited   |
| Organization Owner   | Full Org     | Full Org   | Full Org   | Read       | Org Billing | Full Org     | Policy       | Full Org  |
| Organization Admin   | Org          | Org        | Org        | Limited    | Limited     | Org          | Limited      | Org       |
| Workplace Admin      | Workplace    | Workplace  | Workplace  | Limited    | None        | Workplace    | Limited      | Workplace |
| Team Manager         | Team         | Team       | Team       | None       | None        | Team         | None         | Team      |
| Sales Manager        | Team         | Limited    | None       | Limited    | None        | Limited      | None         | Team      |
| Sales Agent          | Assigned     | Limited    | None       | None       | None        | Limited      | None         | None      |
| Marketing Manager    | Limited      | Full       | Limited    | Limited    | None        | None         | None         | None      |
| Marketing Specialist | Limited      | Specialist | Limited    | None       | None        | None         | None         | None      |
| SEO Manager          | Limited      | Limited    | Full       | None       | None        | None         | None         | None      |
| SEO Specialist       | Limited      | Limited    | Specialist | None       | None        | None         | None         | None      |
| Product Manager      | Product      | Product    | Product    | Limited    | None        | None         | None         | None      |
| Finance Manager      | Analytics    | Analytics  | Analytics  | Full       | Limited     | None         | None         | None      |
| Business Analyst     | Analytics    | Analytics  | Analytics  | Controlled | None        | None         | None         | None      |
| Support Manager      | Limited      | None       | None       | Limited    | Limited     | Full         | Limited      | Support   |
| Support Agent        | Assigned     | None       | None       | None       | None        | Assigned     | None         | None      |
| AI Agent Builder     | Controlled   | Controlled | Controlled | None       | None        | Controlled   | None         | None      |
| AI Sales Agent       | Leads        | None       | None       | None       | None        | Conversation | None         | None      |
| AI Marketing Agent   | Limited      | Marketing  | Limited    | None       | None        | None         | None         | None      |
| AI SEO Agent         | Limited      | Limited    | SEO        | None       | None        | None         | None         | None      |
| AI Support Agent     | Limited      | None       | None       | None       | None        | Support      | None         | None      |
| End User             | Own          | Own        | Own        | Own        | Own Billing | Own Support  | Own Security | Own       |
| External Client      | Scoped       | Scoped     | Scoped     | Scoped     | Scoped      | Scoped       | None         | Scoped    |

> The matrix is a conceptual baseline. Actual permissions MUST be evaluated at resource, action, tenant and policy level.

---

## 11. ROLE ASSIGNMENT FLOW

```text
Administrator
      |
      ↓
Select User
      |
      ↓
Select Role
      |
      ↓
Select Scope
      |
      ↓
Select Organization / Workplace / Team
      |
      ↓
Check Role Conflicts
      |
      ↓
Check Delegation Authority
      |
      ↓
Approval Required?
      |
    YES
      ↓
Approval Workflow
      |
      ↓
Assign Role
      |
      ↓
Invalidate Authorization Cache
      |
      ↓
Audit Event
```

---

## 12. ROLE REVOCATION FLOW

```text
Administrator
      |
      ↓
Select User
      |
      ↓
Select Role
      |
      ↓
Verify Authority
      |
      ↓
Revoke
      |
      ↓
Invalidate Sessions / Permissions
      |
      ↓
Invalidate Cache
      |
      ↓
Audit
```

---

## 13. EFFECTIVE PERMISSION CALCULATION

Example:

```text
User
 |
 +-- Sales Agent
 |      |
 |      +-- lead:read
 |      +-- lead:create
 |
 +-- Business Analyst
        |
        +-- analytics:read
        +-- report:create
```

Effective permissions:

```text
lead:read
lead:create
analytics:read
report:create
```

Then scope and policy constraints MUST be applied.

---

## 14. ROLE CONFLICT MODEL

Potential conflicts:

```text
Billing Requester
+
Billing Approver
```

```text
Security Investigator
+
Security Incident Subject
```

```text
Refund Requester
+
Refund Approver
```

```text
Campaign Creator
+
Campaign Approver
```

Organizations SHOULD be able to configure role conflict policies.

---

## 15. TEMPORARY ROLE MODEL

```yaml
temporary_role:
  user_id: "user-123"
  role_id: "sales_manager"
  scope_type: "workplace"
  scope_id: "workplace-456"
  start_at: "2026-08-22T09:00:00Z"
  expires_at: "2026-08-29T18:00:00Z"
  reason: "Manager vacation coverage"
  approved_by: "user-789"
```

The system MUST automatically remove effective access after expiration.

---

## 16. AI ROLE MODEL

AI identity:

```text
AI Agent
   |
   ↓
AI Role
   |
   ↓
Allowed Tools
   |
   ↓
Permissions
   |
   ↓
Tenant Scope
   |
   ↓
Resource Scope
```

Example:

```yaml
ai_agent:
  name: "SalesGenie Sales Agent"
  role: "ai_sales_agent"
  permissions:
    - lead:read
    - lead:score
    - lead:update
    - conversation:read
  scope:
    type: "organization"
    id: "org-123"
```

---

## 17. AI HUMAN APPROVAL

Example:

```text
AI Sales Agent
      |
      ↓
Generate outreach
      |
      ↓
campaign:publish?
      |
      ↓
High Risk
      |
      ↓
Human Approval
      |
      ↓
Marketing Manager
      |
      ↓
APPROVE
      |
      ↓
Publish
```

---

## 18. API AUTHORIZATION

Every protected API endpoint MUST declare required permission(s).

Example:

```text
GET /api/v1/leads
Required:
lead:read
```

```text
POST /api/v1/leads
Required:
lead:create
```

```text
DELETE /api/v1/leads/{id}
Required:
lead:delete
```

---

## 19. RESOURCE-LEVEL RBAC

Example:

```text
GET /api/v1/leads/LEAD-123
```

Authorization:

```text
1. User authenticated
2. User belongs to tenant
3. User has lead:read
4. Lead belongs to authorized scope
5. Ownership/relationship permits access
```

Only then:

```text
ALLOW
```

---

## 20. TENANT-SCOPED RBAC

```text
Tenant A
 |
 +-- Organization A
      |
      +-- Workplace A
           |
           +-- Team A
                |
                +-- Sales Agent
```

The Sales Agent MUST NOT access:

```text
Tenant B
```

even if the resource ID is known.

---

## 21. WORKPLACE-SCOPED RBAC

```text
Organization
 |
 +-- Workplace A
 |     |
 |     +-- Admin A
 |
 +-- Workplace B
       |
       +-- Admin B
```

Admin A MUST NOT automatically access Workplace B.

---

## 22. TEAM-SCOPED RBAC

```text
Sales Manager
 |
 +-- Team A
      |
      +-- Agent 1
      +-- Agent 2
```

The Sales Manager MAY manage Team A but not necessarily Team B.

---

## 23. PROJECT-SCOPED RBAC

Optional project-level roles:

```text
Project Owner
Project Manager
Project Editor
Project Viewer
```

---

## 24. RESOURCE-SCOPED RBAC

For highly sensitive operations:

```text
User
 ↓
Specific Resource
 ↓
Specific Permission
```

Example:

```text
Finance Report #123
```

may only be accessible to specifically authorized users.

---

## 25. CUSTOM ROLE BUILDER

The UI SHOULD provide:

```text
Create Role
     ↓
Role Information
     ↓
Select Scope
     ↓
Select Modules
     ↓
Select Permissions
     ↓
Review
     ↓
Conflict Detection
     ↓
Save
```

---

## 26. PERMISSION SELECTION UI

Permissions SHOULD be grouped:

```text
Sales
Marketing
SEO
Product
Finance
Billing
Support
Analytics
Security
AI
Automation
Integrations
Users
Organizations
```

Each category SHOULD expose:

```text
Read
Create
Update
Delete
Export
Approve
Publish
Execute
Manage
```

---

## 27. ROLE PREVIEW

Before saving a role, administrators SHOULD see:

```text
Role:
Regional Sales Manager

Scope:
Workplace: Dhaka Sales

Permissions:
lead:read
lead:create
lead:update
lead:assign
analytics:read

Risk:
Medium

Conflicts:
None
```

---

## 28. ROLE SIMULATION

Administrators SHOULD be able to test:

```text
Can this role:
- Read Lead?
- Delete Lead?
- Export Analytics?
- Publish Campaign?
- Access Financial Data?
```

---

## 29. PRIVILEGE ESCALATION DETECTION

The system MUST detect attempts such as:

```text
Sales Agent
   ↓
Assigns self
   ↓
Super Admin
```

Expected:

```text
DENY
+
AUDIT
+
SECURITY EVENT
```

---

## 30. ROLE DELEGATION

Delegation example:

```text
Organization Owner
       |
       ↓
Delegate
       |
       ↓
Organization Admin
       |
       ↓
Workplace A only
       |
       ↓
7-day expiration
```

---

## 31. ROLE CHANGE AUDIT

Audit event:

```json
{
  "event_type": "ROLE_ASSIGNED",
  "actor_id": "admin-123",
  "target_user_id": "user-456",
  "role": "sales_manager",
  "scope_type": "workplace",
  "scope_id": "workplace-789",
  "reason": "Promotion",
  "timestamp": "2026-08-22T10:00:00Z"
}
```

---

## 32. RBAC AUDIT EVENTS

The system SHOULD support:

```text
ROLE_CREATED
ROLE_UPDATED
ROLE_DELETED
ROLE_ACTIVATED
ROLE_DEACTIVATED
ROLE_ASSIGNED
ROLE_REVOKED
ROLE_DELEGATED
ROLE_EXPIRED

PERMISSION_ADDED
PERMISSION_REMOVED

ROLE_CONFLICT_DETECTED
PRIVILEGE_ESCALATION_ATTEMPT
UNAUTHORIZED_ROLE_ASSIGNMENT
```

---

## 33. RBAC MONITORING

Metrics:

```text
Active Roles
Active Assignments
Role Changes
Permission Changes
Denied Requests
Privilege Escalation Attempts
Temporary Roles
Expired Roles
Delegated Roles
Approval Requests
AI Authorization Requests
```

---

## 34. RBAC ALERTS

Security alerts SHOULD trigger for:

```text
Mass role assignments
Mass permission changes
Super Admin assignment
Security Admin assignment
Billing Admin assignment
Cross-tenant role changes
Privilege escalation
Unexpected AI role escalation
```

---

## 35. ROLE ASSIGNMENT SECURITY

Assignment of privileged roles SHOULD require:

```text
MFA
+
Reauthentication
+
Approval
+
Audit
```

depending on policy.

---

## 36. SUPER ADMIN RBAC PROTECTION

Super Admin MUST NOT be treated as a normal role.

Controls SHOULD include:

```text
Strong MFA
Step-up authentication
Privileged session monitoring
Just-in-time access
Approval
Break-glass controls
Immutable audit
```

---

## 37. BILLING RBAC PROTECTION

Billing roles MUST be isolated from:

```text
Security administration
Platform root operations
Unrestricted customer data
```

unless explicitly authorized.

---

## 38. SECURITY RBAC PROTECTION

Security Admin permissions SHOULD be isolated from:

```text
Billing
Sales
Marketing
Product
```

unless required for an incident.

---

## 39. CUSTOMER RBAC

End Users SHOULD have:

```text
Own Account
Own Subscription
Own Conversations
Own Support Requests
Own Data
```

They MUST NOT access internal organization roles.

---

## 40. EXTERNAL CLIENT RBAC

External Clients MUST receive explicit API scopes.

Example:

```text
External Client
 |
 +-- leads:read
 +-- analytics:read
```

They MUST NOT receive:

```text
user:manage
security:manage
billing:manage
```

unless explicitly required and authorized.

---

## 41. SUBSCRIPTION + RBAC

Effective access:

```text
Role Permissions
        +
Subscription Entitlements
        +
Policy
```

Example:

```text
Marketing Manager
        |
        ↓
campaign:publish
        |
        ↓
Enterprise Plan?
        |
       YES
        |
        ↓
ALLOW
```

If the plan does not contain the feature:

```text
DENY / UPGRADE REQUIRED
```

---

## 42. RBAC + FEATURE FLAGS

Feature flags MAY control availability.

However:

```text
Feature Flag
≠
Authorization
```

Both SHOULD be evaluated.

---

## 43. RBAC + ABAC

Example:

```text
Role:
Sales Agent

Permission:
lead:update

Condition:
resource.owner_id == user.id
```

Effective decision:

```text
ALLOW
```

for own leads.

---

## 44. RBAC + ReBAC

Example:

```text
Role:
Team Manager

Permission:
lead:update

Relationship:
lead.team_id == manager.team_id
```

Effective decision:

```text
ALLOW
```

---

## 45. RBAC + RAG

Before AI retrieves a document:

```text
User
 ↓
Role
 ↓
Document Permission
 ↓
Tenant
 ↓
RAG Retrieval
```

Unauthorized documents MUST NOT enter model context.

---

## 46. RBAC + MCP

Every MCP tool MUST declare required permissions.

Example:

```yaml
tool:
  name: send_email
  required_permissions:
    - communication:send
```

---

## 47. RBAC + AI AGENT BUILDER

AI Agent Builder MAY create agents.

However, it MUST NOT automatically grant privileged permissions.

Example:

```text
AI Agent Builder
     |
     ↓
Create AI Agent
     |
     ↓
Select Tools
     |
     ↓
Permission Validation
     |
     ↓
Risk Evaluation
     |
     ↓
Approval if required
```

---

## 48. RBAC + DIGITAL MARKETING

Campaign permissions:

```text
campaign:read
campaign:create
campaign:update
campaign:approve
campaign:publish
campaign:pause
campaign:delete
```

---

## 49. RBAC + SEO AUTOMATION

SEO permissions:

```text
seo:read
seo:analyze
seo:create
seo:update
seo:publish
```

---

## 50. RBAC + LEAD GENERATION

Lead generation permissions:

```text
lead:search
lead:read
lead:create
lead:enrich
lead:score
lead:assign
lead:update
lead:export
```

AI lead-generation agents MUST only execute authorized actions.

---

## 51. RBAC + MARKET INTELLIGENCE

Permissions:

```text
market:read
market:analyze
competitor:read
competitor:analyze
trend:read
```

External data access MUST also respect integration policies.

---

## 52. RBAC + BUSINESS ANALYTICS

Permissions:

```text
analytics:read
analytics:create
analytics:export
profitability:read
revenue:read
expense:read
```

---

## 53. RBAC + AD ANALYTICS

Permissions:

```text
ads:read
ads:analyze
ads:export
ads:manage
```

---

## 54. RBAC + EXCEL EXPORT

Excel/report generation MUST require:

```text
report:export
```

or appropriate resource-specific export permission.

---

## 55. RBAC + SUPPORT

Support authorization MUST ensure:

```text
Support Agent
   ↓
Assigned Ticket
   ↓
Read / Reply
```

while:

```text
Support Agent
   ↓
Organization Billing
```

is denied unless explicitly authorized.

---

## 56. RBAC + FINANCE

Finance permissions MUST support:

```text
finance:read
finance:analyze
finance:export
finance:manage
```

Financial exports SHOULD receive higher risk classification.

---

## 57. RBAC + PAYMENT

Payment permissions:

```text
payment:read
payment:create
payment:refund_request
payment:refund_approve
payment:cancel
```

Requester and approver SHOULD be separated.

---

## 58. RBAC + SECURITY

Security permissions:

```text
security:read
security:investigate
security:manage
security:revoke_sessions
security:manage_policies
```

---

## 59. RBAC API MODEL

Conceptual endpoints:

```text
GET    /api/v1/rbac/roles
POST   /api/v1/rbac/roles
GET    /api/v1/rbac/roles/{id}
PATCH  /api/v1/rbac/roles/{id}
DELETE /api/v1/rbac/roles/{id}

GET    /api/v1/rbac/permissions
GET    /api/v1/rbac/users/{id}/roles
POST   /api/v1/rbac/users/{id}/roles
DELETE /api/v1/rbac/users/{id}/roles/{role_id}

POST   /api/v1/rbac/check
POST   /api/v1/rbac/simulate
```

---

## 60. RBAC CHECK REQUEST

```json
{
  "subject_id": "user-123",
  "action": "lead:update",
  "resource_type": "lead",
  "resource_id": "lead-456",
  "tenant_id": "tenant-789"
}
```

---

## 61. RBAC CHECK RESPONSE

```json
{
  "decision": "ALLOW",
  "role": "sales_agent",
  "permission": "lead:update",
  "scope": "team",
  "reason": "RESOURCE_ASSIGNED_TO_USER"
}
```

---

## 62. DENIED RESPONSE

```json
{
  "decision": "DENY",
  "reason_code": "INSUFFICIENT_PERMISSION"
}
```

The API SHOULD avoid revealing unnecessary authorization details to unauthorized users.

---

## 63. APPROVAL RESPONSE

```json
{
  "decision": "REQUIRE_APPROVAL",
  "approval_type": "MANAGER_APPROVAL",
  "approval_request_id": "approval-123"
}
```

---

## 64. RBAC DATABASE MODEL

Conceptual schema:

```text
users
roles
permissions
role_permissions
user_roles
role_scopes
organizations
workplaces
teams
resource_permissions
delegations
role_conflicts
approval_requests
audit_events
```

---

## 65. USER_ROLES

```text
user_role_id
user_id
role_id
scope_type
scope_id
assigned_by
assigned_at
expires_at
status
```

---

## 66. ROLES

```text
role_id
name
slug
description
role_type
scope_type
tenant_id
is_system_role
status
version
created_by
created_at
updated_at
```

---

## 67. PERMISSIONS

```text
permission_id
name
resource
action
risk_level
description
status
```

---

## 68. ROLE_PERMISSIONS

```text
role_id
permission_id
granted_by
created_at
```

---

## 69. ROLE SCOPES

```text
role_scope_id
role_id
scope_type
scope_id
```

---

## 70. ROLE CONFLICTS

```text
conflict_id
role_a
role_b
severity
policy
created_at
```

---

## 71. ROLE VERSIONING

Example:

```text
sales_manager
v1
v2
v3
```

Existing users MUST NOT unexpectedly receive new privileges because of uncontrolled role changes.

Changes SHOULD be explicitly versioned and deployed.

---

## 72. RBAC CACHE

Potential cache keys:

```text
rbac:user:{user_id}
rbac:role:{role_id}
rbac:permissions:{role_id}
rbac:effective:{user_id}:{scope}
```

Cache invalidation MUST occur after:

```text
Role change
Permission change
User suspension
Scope change
Subscription change
```

---

## 73. DISTRIBUTED RBAC

For microservices:

```text
                    RBAC SERVICE
                         |
        +----------------+----------------+
        |                |                |
   Sales Service   Marketing Service  Support
        |                |                |
        +----------------+----------------+
                         |
                   Policy Engine
```

---

## 74. SERVICE-TO-SERVICE RBAC

Services MUST authenticate using service identities.

Example:

```text
Lead Intelligence Service
        |
        ↓
Sales Service
        |
        ↓
Service Role:
lead:enrich
```

---

## 75. SERVICE ROLE

Example:

```yaml
service_role:
  name: lead_intelligence_service
  permissions:
    - company:read
    - lead:enrich
  scopes:
    - tenant
```

---

## 76. API KEY ROLE

API keys SHOULD be mapped to scopes rather than unrestricted roles.

Example:

```text
API Key
 |
 +-- role: external_readonly
 |
 +-- lead:read
 +-- analytics:read
```

---

## 77. OAUTH ROLE MAPPING

External identity providers MAY map identities to internal roles.

Example:

```text
Google Workspace Group
        ↓
SalesGenie Role
        ↓
Marketing Specialist
```

Mapping MUST be controlled by authorized administrators.

---

## 78. SCIM ROLE PROVISIONING

Enterprise SCIM MAY support:

```text
Create User
Deactivate User
Group Assignment
Role Mapping
```

SCIM-provisioned roles MUST respect tenant policy.

---

## 79. RBAC SECURITY TESTING

Mandatory tests:

```text
Role assignment
Role removal
Permission inheritance
Multiple roles
Scope restrictions
Tenant isolation
Workplace isolation
Team isolation
BOLA
IDOR
Privilege escalation
Mass assignment
Role conflict
AI escalation
API scope bypass
Cache invalidation
Expired roles
Delegated roles
```

---

## 80. PERFORMANCE TESTING

RBAC MUST be tested under:

```text
10,000 users
100,000 users
1M users
10M+ users
```

where applicable.

The architecture SHOULD support horizontal scaling without redesigning authorization semantics.

---

## 81. AVAILABILITY

Target:

```text
99.99%+
```

for critical authorization infrastructure, subject to overall SalesGenie SLO design.

---

## 82. OBSERVABILITY

The RBAC system MUST expose:

```text
Metrics
Logs
Traces
Audit events
Policy decisions
Latency
Error rates
Cache hit ratio
```

Sensitive information MUST be appropriately redacted.

---

## 83. SECURITY EVENTS

RBAC SHOULD integrate with the security platform for:

```text
Privilege escalation
Unauthorized role assignment
Mass permission modification
Cross-tenant attempts
Unexpected privileged access
Suspicious AI behavior
```

---

## 84. ADMIN RBAC DASHBOARD

The RBAC administration dashboard SHOULD contain:

```text
Role Overview
Permission Overview
User Role Assignments
Role Conflicts
Temporary Access
Delegations
Approval Requests
Audit History
Risk Events
Permission Simulator
```

---

## 85. ROLE ANALYTICS

Administrators SHOULD see:

```text
Most used roles
Unused roles
Overprivileged roles
Users with excessive permissions
Recently changed roles
Temporary roles
Expired roles
```

---

## 86. OVERPRIVILEGE DETECTION

SalesGenie SHOULD detect users with permissions significantly exceeding their normal role requirements.

Example:

```text
Sales Agent
+
billing:manage
+
security:manage
+
user:delete
```

The system SHOULD flag this for review.

---

## 87. ACCESS REVIEW

Enterprise organizations SHOULD support periodic access reviews.

Example:

```text
Quarterly Access Review
        ↓
Managers review users
        ↓
Confirm / Revoke roles
        ↓
Audit
```

---

## 88. CERTIFICATION WORKFLOW

```text
Manager
   ↓
Review Role
   ↓
Confirm Access
   ↓
Revoke unnecessary permission
   ↓
Submit
```

---

## 89. JUST-IN-TIME ACCESS

High-privilege roles SHOULD support JIT access.

Example:

```text
User
 ↓
Request Security Admin
 ↓
Reason
 ↓
Approval
 ↓
15-minute access
 ↓
Automatic expiration
```

---

## 90. BREAK-GLASS ROLE

Example:

```text
Emergency Security Administrator
```

Requirements:

```text
Strong authentication
Reason
Short duration
Automatic alert
Immutable audit
Post-event review
```

---

## 91. RBAC AND HUMANIZED SECURITY

SalesGenie MUST support human intervention.

```text
RBAC Engine
      |
      ↓
Risk Engine
      |
      ↓
High Risk
      |
      ↓
Human Security Admin
      |
      ↓
Approve / Reject
```

AI may recommend a decision, but the human policy boundary remains authoritative for critical actions.

---

## 92. RBAC AND AI SECURITY

AI MAY:

```text
Analyze role assignments
Detect anomalies
Recommend least privilege
Detect privilege escalation
Recommend role cleanup
Identify unused permissions
```

AI MUST NOT silently modify privileged roles without authorization.

---

## 93. AI ROLE RECOMMENDATION

Example:

```text
User behavior
      ↓
AI analysis
      ↓
Recommended Role:
Sales Manager
      ↓
Human/Admin Review
      ↓
Approve
      ↓
Role Assignment
```

---

## 94. AI LEAST-PRIVILEGE OPTIMIZATION

AI SHOULD identify:

```text
Unused permissions
Excess permissions
Duplicate roles
Overlapping roles
Risky role combinations
```

Recommendations MUST require authorized human/system approval before applying critical changes.

---

## 95. RBAC GOVERNANCE

Governance SHOULD include:

```text
Role lifecycle
Permission lifecycle
Role ownership
Access reviews
Role certification
Change management
Audit
Risk assessment
```

---

## 96. ROLE LIFECYCLE

```text
DRAFT
 ↓
REVIEW
 ↓
APPROVED
 ↓
ACTIVE
 ↓
DEPRECATED
 ↓
ARCHIVED
```

---

## 97. PERMISSION LIFECYCLE

```text
PROPOSED
 ↓
REVIEWED
 ↓
ACTIVE
 ↓
DEPRECATED
 ↓
REMOVED
```

---

## 98. ROLE CHANGE MANAGEMENT

Critical role changes SHOULD use:

```text
Change Request
 ↓
Review
 ↓
Security Validation
 ↓
Approval
 ↓
Deployment
 ↓
Monitoring
```

---

## 99. RBAC ACCEPTANCE CRITERIA

The RBAC system is acceptable only when:

```text
[ ] Default deny works
[ ] Least privilege is enforced
[ ] Multiple roles work
[ ] Scoped roles work
[ ] Platform roles work
[ ] Organization roles work
[ ] Workplace roles work
[ ] Team roles work
[ ] Project roles work
[ ] Resource permissions work
[ ] Action permissions work
[ ] Read/write separation works
[ ] Delete permissions are explicit
[ ] Export permissions are explicit
[ ] Custom roles work
[ ] System roles are protected
[ ] Role assignment works
[ ] Role revocation works
[ ] Temporary roles work
[ ] Role expiration works
[ ] Delegation works
[ ] Role conflicts work
[ ] Privilege escalation is prevented
[ ] Tenant isolation works
[ ] Workplace isolation works
[ ] Team isolation works
[ ] Resource ownership works
[ ] API authorization works
[ ] Service authorization works
[ ] API key scopes work
[ ] OAuth scopes work
[ ] SCIM role mapping works where enabled
[ ] Subscription entitlements work
[ ] AI roles work
[ ] AI tools are permission-controlled
[ ] MCP tools are permission-controlled
[ ] RAG respects permissions
[ ] Human approval works
[ ] JIT access works
[ ] Break-glass access works
[ ] Access review works
[ ] Role simulation works
[ ] Permission simulation works
[ ] Audit logging works
[ ] Security alerts work
[ ] Cache invalidation works
[ ] Fail-closed behavior works
[ ] BOLA protection works
[ ] IDOR protection works
[ ] Mass-assignment protection works
[ ] Performance targets are met
[ ] High availability is implemented
```

---

## 100. REFERENCE RBAC ARCHITECTURE

```text
                         SALESGENIE
                             |
                       AUTHENTICATION
                             |
                             ↓
                       IDENTITY SERVICE
                             |
                             ↓
                      TENANT RESOLUTION
                             |
                             ↓
                     +---------------+
                     | RBAC ENGINE   |
                     +-------+-------+
                             |
             +---------------+---------------+
             |               |               |
            USER            ROLE         PERMISSION
             |               |               |
             +---------------+---------------+
                             |
                           SCOPE
                             |
             +---------------+---------------+
             |               |               |
       ORGANIZATION       WORKPLACE         TEAM
             |               |               |
             +---------------+---------------+
                             |
                          RESOURCE
                             |
                           ACTION
                             |
                      POLICY ENGINE
                             |
                    +--------+--------+
                    |                 |
                  ALLOW             DENY
                    |
                    ↓
                RISK ENGINE
                    |
          +---------+---------+
          |                   |
        LOW/MED              HIGH
          |                   |
        Execute           Approval
                              |
                              ↓
                           HUMAN
                              |
                        APPROVE / DENY
                              |
                              ↓
                           EXECUTE
                              |
                              ↓
                         AUDIT LOG
```

---

## 101. FINAL RBAC RULES

SalesGenie MUST enforce the following rules:

1. Every protected resource MUST have an authorization boundary.
2. Every protected action MUST require an explicit permission.
3. Every role MUST have a defined scope.
4. Every user MUST receive only necessary roles.
5. Multiple roles MUST be evaluated safely.
6. Default access MUST be denied.
7. Tenant isolation MUST always be enforced.
8. Workplace and team boundaries MUST be enforced.
9. Resource ownership MUST be evaluated where applicable.
10. Frontend role checks MUST never replace backend authorization.
11. System roles MUST be protected.
12. Custom roles MUST be constrained.
13. Users MUST NOT grant themselves privileges.
14. Users MUST NOT delegate privileges they do not possess.
15. Role conflicts MUST be detectable.
16. Critical operations SHOULD use separation of duties.
17. Temporary roles MUST expire.
18. Delegated roles MUST be auditable.
19. Subscription entitlements MUST restrict unavailable features.
20. AI agents MUST have independent roles.
21. AI agents MUST have explicit tool permissions.
22. AI agents MUST NOT bypass human approval policies.
23. MCP tools MUST have explicit authorization scopes.
24. RAG retrieval MUST respect RBAC.
25. Financial permissions MUST be isolated.
26. Billing permissions MUST be isolated.
27. Security permissions MUST be isolated.
28. Export permissions MUST be explicit.
29. Delete permissions MUST be explicit.
30. API keys MUST be scoped.
31. OAuth scopes MUST be enforced.
32. Service identities MUST have least privilege.
33. Authorization failures MUST fail closed.
34. Authorization changes MUST invalidate relevant caches.
35. Privileged changes MUST be audited.
36. Suspicious RBAC activity MUST generate security events.
37. Access reviews SHOULD be supported.
38. JIT access SHOULD be supported for privileged roles.
39. Break-glass access MUST be tightly controlled.
40. RBAC MUST integrate with ABAC and ReBAC for contextual authorization.
41. RBAC MUST integrate with risk-based authorization.
42. RBAC MUST integrate with human approval.
43. RBAC MUST support both human and machine identities.
44. RBAC MUST be horizontally scalable.
45. RBAC MUST remain highly available.
46. RBAC MUST protect against horizontal privilege escalation.
47. RBAC MUST protect against vertical privilege escalation.
48. RBAC MUST protect against cross-tenant privilege escalation.
49. RBAC MUST protect against BOLA/IDOR.
50. RBAC MUST protect against mass assignment.
51. RBAC policies MUST be versioned.
52. Role changes MUST be traceable.
53. Permission changes MUST be traceable.
54. AI may recommend RBAC changes but MUST NOT silently grant privileged access.
55. Human security intervention MUST remain available for critical authorization decisions.

---

## 102. DEFINITION OF DONE

The SalesGenie RBAC subsystem is production-ready when the platform can reliably answer:

```text
WHO IS REQUESTING?
        ↓
WHAT ROLE(S) DO THEY HAVE?
        ↓
WHERE IS THE ROLE VALID?
        ↓
WHAT PERMISSIONS DOES THE ROLE PROVIDE?
        ↓
WHAT RESOURCE IS BEING ACCESSED?
        ↓
WHAT ACTION IS BEING REQUESTED?
        ↓
DOES THE RESOURCE BELONG TO THE AUTHORIZED SCOPE?
        ↓
DO OWNERSHIP / RELATIONSHIP RULES ALLOW ACCESS?
        ↓
DO SUBSCRIPTION ENTITLEMENTS ALLOW THE FEATURE?
        ↓
IS THE ACTION HIGH RISK?
        ↓
IS ADDITIONAL APPROVAL REQUIRED?
        ↓
ALLOW / DENY / REQUIRE APPROVAL
```

The fundamental SalesGenie RBAC principle is:

> **A role grants potential capabilities; it does not automatically grant unrestricted access. Effective authorization is the intersection of role, permission, scope, resource, action, tenant, policy, entitlement, context, and risk.**
