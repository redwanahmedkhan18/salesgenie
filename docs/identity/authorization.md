# SALESGENIE — AUTHORIZATION REQUIREMENTS

**File:** `authorization.md`  
**Project:** SalesGenie  
**Document Type:** Authorization Architecture — User Requirements, System Requirements & Functional Requirements  
**Version:** 1.0.0  
**Status:** Architecture Baseline  
**Security Classification:** Confidential  
**Target:** Enterprise / FAANG-Level Multi-Tenant SaaS

---

## 1. DOCUMENT PURPOSE

This document defines the complete authorization architecture for SalesGenie.

Authentication answers:

> "Who are you?"

Authorization answers:

> "What are you allowed to do, where are you allowed to do it, under which conditions, and what actions require approval?"

SalesGenie MUST implement authorization independently from authentication.

The authorization platform MUST control access for:

- Super Admin
- Platform Admin
- Security Admin
- Billing Admin
- Organization Owner
- Organization Admin
- Workplace Admin
- Team Manager
- Sales Manager
- Sales Agent
- Marketing Manager
- Marketing Specialist
- SEO Manager
- SEO Specialist
- Product Manager
- Finance Manager
- Business Analyst
- Support Manager
- Support Agent
- AI Agent
- Developer
- End User
- External Client
- API Client
- Service Account
- Other future roles

Authorization MUST support:

```text
RBAC
+
ABAC
+
ReBAC
+
Tenant Isolation
+
Resource-Level Permissions
+
Action-Level Permissions
+
AI-Agent Authorization
+
Human Approval
+
Policy-Based Access Control
+
Temporary Access
+
Delegated Access
+
Emergency Access
```

---

## 2. AUTHORIZATION VISION

SalesGenie MUST use a centralized, policy-driven authorization architecture capable of making decisions consistently across all microservices.

Conceptually:

```text
Request
   |
   ↓
Identity
   |
   ↓
Tenant Context
   |
   ↓
Role / Permission
   |
   ↓
Resource
   |
   ↓
Action
   |
   ↓
Policy Evaluation
   |
   ↓
Risk Evaluation
   |
   ↓
Approval Requirement
   |
   ↓
ALLOW / DENY / REQUIRE_APPROVAL
```

The system MUST NOT rely on frontend role checks as a security boundary.

---

## 3. CORE AUTHORIZATION PRINCIPLES

## AUTHZ-PRINCIPLE-001 — Deny by Default

If no explicit policy grants access:

```text
DENY
```

---

## AUTHZ-PRINCIPLE-002 — Least Privilege

Users, services and AI agents MUST receive only the permissions necessary to perform their responsibilities.

---

## AUTHZ-PRINCIPLE-003 — Separation of Duties

Critical operations SHOULD require multiple roles or approval stages.

Example:

```text
Sales Agent
    ↓
Creates discount
    ↓
Sales Manager approval
```

---

## AUTHZ-PRINCIPLE-004 — Tenant Isolation

A user MUST NOT access another tenant's resources unless explicit cross-tenant authorization exists.

---

## AUTHZ-PRINCIPLE-005 — Server-Side Enforcement

Every protected operation MUST be authorized on the server.

---

## AUTHZ-PRINCIPLE-006 — Resource Ownership

Authorization MUST consider resource ownership where applicable.

Example:

```text
Sales Agent
    ↓
Can modify own leads

Sales Manager
    ↓
Can modify team leads

Organization Admin
    ↓
Can modify organization leads
```

---

## AUTHZ-PRINCIPLE-007 — Context-Aware Authorization

Authorization MAY depend on:

* User
* Role
* Tenant
* Workplace
* Team
* Resource
* Resource owner
* Action
* Time
* Device trust
* Authentication strength
* Risk level
* Approval status
* Data sensitivity
* Subscription plan

---

## 4. USER REQUIREMENTS

## UR-AUTHZ-001 — Role-Based Access

Users MUST receive permissions based on their assigned roles.

---

## UR-AUTHZ-002 — Multiple Roles

A user MAY have multiple roles where organizational policy permits.

Example:

```text
User
 ├── Marketing Manager
 ├── SEO Manager
 └── Business Analyst
```

Effective permissions MUST be calculated safely.

---

## UR-AUTHZ-003 — Scoped Roles

Roles MUST support scopes such as:

```text
Platform
Organization
Workplace
Team
Project
Campaign
Resource
```

---

## UR-AUTHZ-004 — Resource-Level Access

Users MUST be able to access individual resources only when authorized.

Examples:

```text
Lead A → accessible
Lead B → denied
Campaign X → accessible
Campaign Y → denied
```

---

## UR-AUTHZ-005 — Action-Level Permissions

Authorization MUST distinguish between actions.

Example:

```text
lead:read
lead:create
lead:update
lead:delete
lead:export
lead:assign
lead:enrich
```

---

## UR-AUTHZ-006 — Read vs Write

A user with read permission MUST NOT automatically receive write permission.

---

## UR-AUTHZ-007 — Delete Protection

Delete operations MUST require explicit delete permission.

Critical deletion SHOULD require additional approval.

---

## UR-AUTHZ-008 — Export Protection

Exporting sensitive business data MUST be separately permissioned.

---

## UR-AUTHZ-009 — Billing Authorization

Billing operations MUST be isolated from general administrative permissions.

---

## UR-AUTHZ-010 — Security Authorization

Security-sensitive actions MUST require dedicated permissions.

Examples:

```text
security:manage
security:investigate
security:revoke_sessions
security:manage_mfa
security:manage_policies
```

---

## UR-AUTHZ-011 — AI Agent Authorization

AI agents MUST have explicitly defined permissions.

An AI agent MUST NOT inherit unlimited permissions from its human owner.

---

## UR-AUTHZ-012 — Human Approval

The platform MUST support human approval for high-risk AI or user operations.

---

## UR-AUTHZ-013 — Temporary Permissions

Authorized administrators SHOULD be able to grant time-limited permissions.

---

## UR-AUTHZ-014 — Delegated Access

Users MAY delegate specific permissions to another authorized identity.

Delegation MUST have:

* Scope
* Expiration
* Audit trail
* Revocation

---

## UR-AUTHZ-015 — Subscription-Based Authorization

Some functionality MUST depend on the customer's subscription plan.

Example:

```text
Free
Monthly
Yearly
Enterprise
Custom
```

Plan-based restrictions MUST be enforced server-side.

---

## UR-AUTHZ-016 — Feature Entitlements

The system MUST support feature entitlements.

Example:

```text
AI Lead Generation
Advanced Analytics
SEO Automation
AI Support
Human Support
Advanced Market Intelligence
API Access
Enterprise SSO
```

---

## UR-AUTHZ-017 — Role Visibility

Users SHOULD only see modules they are authorized to use.

Frontend visibility is for usability; backend authorization remains mandatory.

---

## UR-AUTHZ-018 — Unauthorized Access Handling

Unauthorized requests MUST return appropriate errors without revealing protected resource information.

---

## UR-AUTHZ-019 — Auditability

Authorization decisions and privileged changes MUST be auditable.

---

## UR-AUTHZ-020 — Policy Transparency

Authorized administrators SHOULD be able to understand why an access request was:

```text
ALLOWED
DENIED
REQUIRES_APPROVAL
```

without exposing sensitive internal security information.

---

## 5. AUTHORIZATION MODEL

SalesGenie SHOULD implement a hybrid authorization model:

```text
RBAC
+
ABAC
+
ReBAC
+
PBAC
+
Entitlement-Based Access
```

---

## 6. RBAC — ROLE-BASED ACCESS CONTROL

RBAC maps:

```text
User
 ↓
Role
 ↓
Permissions
```

Example:

```text
Sales Agent
   |
   +-- lead:read
   +-- lead:create
   +-- lead:update
   +-- lead:assign_self
   +-- campaign:read
```

---

## 7. ABAC — ATTRIBUTE-BASED ACCESS CONTROL

ABAC evaluates attributes.

Example:

```text
IF
user.role = "Sales Agent"
AND
resource.owner_id = user.id
AND
resource.tenant_id = user.tenant_id
THEN
ALLOW
```

---

## 8. ReBAC — RELATIONSHIP-BASED ACCESS CONTROL

ReBAC evaluates relationships.

Example:

```text
User
 ↓ member_of
Team
 ↓ owns
Campaign
```

The user may access the campaign because of the relationship.

---

## 9. PBAC — POLICY-BASED ACCESS CONTROL

Central policies SHOULD define authorization decisions.

Example:

```yaml
policy:
  name: sales_agent_lead_update
  subject:
    role: sales_agent
  resource:
    type: lead
  action:
    - update
  condition:
    owner_matches_subject: true
  effect: allow
```

---

## 10. AUTHORIZATION SUBJECTS

Subjects may include:

```text
Human User
AI Agent
Service Account
API Client
System Process
Integration
```

---

## 11. RESOURCES

SalesGenie resources SHOULD include:

```text
User
Organization
Workplace
Team
Lead
Contact
Company
Campaign
Ad
Product
Customer
Conversation
Ticket
Knowledge Base
Document
Workflow
AI Agent
Prompt
Model
Integration
Subscription
Invoice
Payment
Analytics
Report
API Key
Security Policy
Audit Log
```

---

## 12. ACTIONS

Common actions:

```text
create
read
update
delete
list
search
export
import
assign
approve
reject
execute
publish
archive
restore
share
invite
manage
configure
rotate
revoke
impersonate
```

---

## 13. PERMISSION NAMING STANDARD

Permissions SHOULD follow:

```text
<resource>:<action>
```

Examples:

```text
lead:read
lead:create
lead:update
lead:delete
lead:export

campaign:read
campaign:create
campaign:update
campaign:publish

analytics:read
analytics:export

billing:read
billing:manage

user:read
user:create
user:update
user:suspend

security:read
security:manage
security:investigate
```

---

## 14. PLATFORM ROLE AUTHORIZATION

## 14.1 SUPER ADMIN

Super Admin has the highest platform-level authority.

Capabilities MAY include:

```text
Platform configuration
User management
Organization management
Role management
Security administration
System monitoring
Service configuration
Global audit access
Emergency controls
```

Super Admin MUST still be subject to:

* MFA
* Audit logging
* Step-up authentication
* Break-glass policies
* Separation of duties for selected operations

---

## 14.2 PLATFORM ADMIN

Platform Admin manages platform operations.

Example permissions:

```text
platform:read
platform:manage
organization:read
organization:manage
user:read
system:monitor
```

Platform Admin SHOULD NOT automatically receive:

```text
security:root
billing:root
```

---

## 14.3 SECURITY ADMIN

Security Admin manages security controls.

Permissions:

```text
security:read
security:investigate
security:manage
security:revoke_sessions
security:manage_policies
security:view_audit
```

Security Admin MUST NOT automatically control billing or business data.

---

## 14.4 BILLING ADMIN

Billing Admin manages:

```text
plans
subscriptions
invoices
payments
credits
refund workflows
usage
billing configuration
```

Billing Admin MUST NOT automatically receive unrestricted access to customer business data.

---

## 15. ORGANIZATION ROLE AUTHORIZATION

## 15.1 ORGANIZATION OWNER

Organization Owner manages organization-wide resources.

Capabilities:

```text
organization settings
users
roles
workplaces
billing
integrations
security policies
subscription
analytics
```

Critical billing/security actions SHOULD require reauthentication and MFA.

---

## 15.2 ORGANIZATION ADMIN

Organization Admin manages operational resources within the organization.

Permissions MAY include:

```text
organization:read
organization:update
user:read
user:create
user:update
team:manage
workplace:manage
analytics:read
integration:manage
```

---

## 15.3 WORKPLACE ADMIN

Workplace Admin manages a specific workplace.

Scope:

```text
Organization
    ↓
Workplace
```

The administrator MUST NOT automatically access unrelated workplaces.

---

## 15.4 TEAM MANAGER

Team Manager manages:

* Team members
* Team leads
* Team campaigns
* Team performance
* Team workflows

---

## 16. SALES AUTHORIZATION

## 16.1 SALES MANAGER

Sales Manager MAY:

```text
View team leads
Assign leads
Create campaigns
Monitor performance
Approve sales actions
View sales analytics
```

---

## 16.2 SALES AGENT

Sales Agent MAY:

```text
View assigned leads
Create leads
Update assigned leads
Add notes
Communicate with prospects
Use AI sales tools
Generate sales recommendations
```

Sales Agent MUST NOT automatically:

```text
Delete organization data
View all financial information
Change billing
Change security settings
Modify organization roles
```

---

## 17. MARKETING AUTHORIZATION

## 17.1 MARKETING MANAGER

Marketing Manager MAY:

```text
Manage campaigns
Manage marketing strategy
Access marketing analytics
Manage marketing automation
Review market intelligence
Manage advertising integrations
Approve campaign publication
```

---

## 17.2 MARKETING SPECIALIST

Marketing Specialist MAY:

```text
Create campaign content
Analyze trends
Generate marketing assets
Execute approved campaigns
Review campaign performance
```

---

## 18. SEO AUTHORIZATION

## 18.1 SEO MANAGER

SEO Manager MAY:

```text
Manage SEO strategy
Manage SEO projects
View SEO analytics
Approve SEO changes
Manage SEO automation
```

---

## 18.2 SEO SPECIALIST

SEO Specialist MAY:

```text
Keyword research
Content optimization
Technical SEO analysis
Competitor analysis
Backlink analysis
SEO recommendations
```

Publishing production changes SHOULD require appropriate permissions.

---

## 19. PRODUCT AUTHORIZATION

## PRODUCT MANAGER

Product Manager MAY:

```text
Create products
Update product information
Analyze product performance
Analyze competitors
Analyze market conditions
Review profitability
Create product strategies
```

High-impact pricing or financial changes SHOULD require additional authorization.

---

## 20. FINANCE AUTHORIZATION

## FINANCE MANAGER

Finance Manager MAY:

```text
View financial analytics
Analyze revenue
Analyze expenses
Analyze profit/loss
Analyze product profitability
Generate reports
Export financial reports
```

Financial exports SHOULD be separately permissioned.

---

## 21. BUSINESS ANALYST AUTHORIZATION

Business Analyst MAY:

```text
Access approved business data
Build analytics
Create reports
Analyze trends
Analyze customer behavior
Analyze product performance
Generate business recommendations
```

Sensitive financial data SHOULD require explicit permission.

---

## 22. SUPPORT AUTHORIZATION

## SUPPORT MANAGER

Support Manager MAY:

```text
Manage support agents
View support analytics
Manage queues
Configure escalation
Review conversations
Manage support workflows
```

---

## SUPPORT AGENT

Support Agent MAY:

```text
View assigned tickets
Respond to customers
Use AI support assistant
Escalate tickets
Update ticket status
```

Support Agents MUST NOT automatically access:

```text
billing administration
security administration
private organizational analytics
```

---

## 23. END USER AUTHORIZATION

End Users MUST have the most restrictive customer-level permissions.

They MAY:

```text
View own account
Manage own profile
Use subscribed features
Create support requests
View own conversations
View own data
Manage allowed integrations
```

They MUST NOT access:

```text
other customers
organization administration
internal employee tools
platform administration
```

---

## 24. EXTERNAL CLIENT AUTHORIZATION

External Clients MAY receive controlled API/integration access.

Access MUST be:

```text
Scoped
Tenant-bound
Time-bound where appropriate
Audited
Revocable
```

---

## 25. AI AGENT AUTHORIZATION

AI agents require a separate authorization model.

Example:

```text
AI Sales Agent
    |
    +-- lead:read
    +-- lead:update
    +-- conversation:read
    +-- conversation:create
    +-- analytics:read
```

It SHOULD NOT automatically receive:

```text
billing:manage
security:manage
user:delete
organization:delete
```

---

## 26. AI AGENT TOOL AUTHORIZATION

Every AI tool invocation MUST be authorized.

Flow:

```text
AI Agent
   ↓
Tool Request
   ↓
Identity Verification
   ↓
Permission Check
   ↓
Tenant Check
   ↓
Risk Check
   ↓
Approval Check
   ↓
ALLOW / DENY
   ↓
Tool Execution
```

---

## 27. HIGH-RISK AI ACTIONS

AI actions SHOULD be classified:

```text
LOW
MEDIUM
HIGH
CRITICAL
```

Example:

| Risk     | Example         | Policy                   |
| -------- | --------------- | ------------------------ |
| Low      | Generate report | AI allowed               |
| Medium   | Update lead     | Permission check         |
| High     | Send campaign   | Approval may be required |
| Critical | Refund money    | Human approval required  |

---

## 28. HUMAN-IN-THE-LOOP AUTHORIZATION

SalesGenie MUST support human approval workflows.

```text
AI proposes action
       ↓
Risk Engine
       ↓
Policy Engine
       ↓
Human Approval
       ↓
Action Execution
```

---

## 29. APPROVAL OBJECT

Approval requests SHOULD contain:

```text
approval_id
requester
request_type
resource
action
tenant
reason
risk_level
created_at
expires_at
approver
status
decision
decision_reason
```

---

## 30. APPROVAL STATES

```text
PENDING
APPROVED
REJECTED
EXPIRED
CANCELLED
```

---

## 31. FOUR-EYES PRINCIPLE

Critical actions SHOULD support:

```text
Requester ≠ Approver
```

Examples:

```text
Large refund
Sensitive data export
Security policy change
Organization deletion
Bulk customer deletion
High-value campaign execution
```

---

## 32. TEMPORARY ACCESS

Temporary permissions MUST support:

```text
Permission
Scope
Start Time
Expiration
Reason
Approver
```

Example:

```yaml
temporary_access:
  user: analyst-123
  permission: finance:export
  scope: organization:456
  expires_at: "2026-08-22T18:00:00Z"
  reason: "Quarterly reporting"
```

Access MUST automatically expire.

---

## 33. BREAK-GLASS AUTHORIZATION

Emergency access MUST:

* Require strong authentication
* Require explicit reason
* Trigger immediate security alerts
* Have short expiration
* Be fully audited
* Be reviewed afterward

---

## 34. IMPERSONATION

Administrative impersonation MAY be supported only under strict controls.

Requirements:

```text
Explicit permission
+
Reason
+
Audit event
+
Time limit
+
Visible impersonation indicator
+
Restricted sensitive operations
```

Admins MUST NOT be able to silently impersonate users.

---

## 35. CROSS-TENANT ACCESS

Cross-tenant access MUST be denied by default.

If legitimate platform operations require it:

```text
Platform identity
      ↓
Explicit cross-tenant permission
      ↓
Reason
      ↓
Audit
      ↓
Time-limited access
```

---

## 36. TENANT ISOLATION

Every resource authorization decision MUST validate tenant ownership.

Conceptually:

```text
resource.tenant_id
        ==
request.tenant_id
```

unless an explicit privileged cross-tenant policy exists.

---

## 37. WORKPLACE ISOLATION

For workplace-scoped roles:

```text
request.workplace_id
        ==
user.allowed_workplace_id
```

---

## 38. TEAM ISOLATION

For team-scoped roles:

```text
resource.team_id
        IN
user.authorized_team_ids
```

---

## 39. RESOURCE OWNERSHIP

Authorization SHOULD support:

```text
owner
creator
assignee
manager
member
viewer
editor
```

Example:

```text
Sales Agent
    |
    +-- Own Leads → Full allowed actions
    |
    +-- Team Leads → Limited actions
    |
    +-- Other Team Leads → Denied
```

---

## 40. SUBSCRIPTION AUTHORIZATION

Authorization MUST support plan entitlements.

Example:

```text
Free
 |
 +-- Limited AI usage
 +-- Basic analytics
 +-- Basic support

Monthly
 |
 +-- Advanced AI
 +-- Advanced analytics
 +-- Automation

Yearly
 |
 +-- Same/expanded features
 +-- Higher limits

Enterprise
 |
 +-- SSO
 +-- SCIM
 +-- Advanced security
 +-- Custom limits
 +-- Premium support
```

---

## 41. ENTITLEMENT MODEL

An entitlement SHOULD contain:

```text
tenant_id
feature
plan
limit
current_usage
status
effective_from
effective_until
```

---

## 42. USAGE-BASED AUTHORIZATION

Some actions MUST be denied or limited when usage exceeds plan limits.

Example:

```text
AI credits = 0
      ↓
AI generation request
      ↓
Entitlement check
      ↓
DENY / Upgrade / Purchase credits
```

---

## 43. FEATURE FLAG AUTHORIZATION

Feature flags MUST NOT be treated as the only security boundary.

Correct:

```text
Feature Flag
+
Authorization Policy
```

Incorrect:

```text
Feature Flag only
```

---

## 44. DATA CLASSIFICATION

Resources SHOULD be classified:

```text
PUBLIC
INTERNAL
CONFIDENTIAL
SENSITIVE
RESTRICTED
```

Authorization MUST consider data sensitivity.

---

## 45. SENSITIVE DATA

Examples:

```text
Financial records
Payment information
Security logs
Personal data
Authentication data
API credentials
Customer communications
Business strategy
```

Sensitive resources MUST require stronger permissions.

---

## 46. DATA EXPORT AUTHORIZATION

Export operations SHOULD require separate permissions.

Example:

```text
analytics:read
```

does NOT automatically imply:

```text
analytics:export
```

---

## 47. BULK OPERATION AUTHORIZATION

Bulk actions MUST be separately evaluated.

Examples:

```text
Bulk delete
Bulk export
Bulk update
Bulk message
Bulk campaign execution
```

Risk scoring SHOULD consider the number of affected resources.

---

## 48. ADMINISTRATIVE ACTION AUTHORIZATION

Administrative operations MUST use stricter policy.

Examples:

```text
Role modification
Permission modification
User suspension
Organization deletion
Security policy modification
Billing configuration
```

---

## 49. AUTHORIZATION POLICY ENGINE

SalesGenie SHOULD have a centralized policy decision layer.

Conceptually:

```text
                 +------------------+
Request -------->| Policy Engine    |
                 +--------+---------+
                          |
             +------------+------------+
             |            |            |
           RBAC         ABAC         ReBAC
             |            |            |
             +------------+------------+
                          |
                    Risk Evaluation
                          |
                    Entitlements
                          |
                    Approval Rules
                          |
                          ↓
               ALLOW / DENY / APPROVAL
```

---

## 50. POLICY DECISION RESPONSE

Example:

```json
{
  "decision": "ALLOW",
  "policy_id": "sales-agent-own-lead-update",
  "reason_code": "RESOURCE_OWNER_MATCH",
  "ttl_seconds": 60
}
```

For denial:

```json
{
  "decision": "DENY",
  "policy_id": "organization-billing-access",
  "reason_code": "INSUFFICIENT_PERMISSION"
}
```

---

## 51. AUTHORIZATION DECISION TYPES

The engine SHOULD support:

```text
ALLOW
DENY
REQUIRE_MFA
REQUIRE_REAUTHENTICATION
REQUIRE_APPROVAL
RATE_LIMIT
READ_ONLY
```

---

## 52. POLICY EVALUATION ORDER

Recommended:

```text
1. Identity validity
2. Session validity
3. Tenant validation
4. Account status
5. Role evaluation
6. Permission evaluation
7. Resource ownership
8. Relationship evaluation
9. Data sensitivity
10. Subscription entitlement
11. Risk evaluation
12. Approval requirement
13. Final decision
```

---

## 53. POLICY PRIORITY

Explicit deny MUST override allow unless an emergency policy explicitly supersedes it.

Conceptually:

```text
Explicit DENY
      ↓
Highest priority

Explicit ALLOW
      ↓
Conditional allow

Default
      ↓
DENY
```

---

## 54. AUTHORIZATION CACHING

Authorization decisions MAY be cached.

However:

```text
Role changes
Permission changes
Session revocation
Account suspension
Security policy changes
```

MUST invalidate relevant authorization caches.

---

## 55. AUTHORIZATION CONSISTENCY

Critical authorization decisions SHOULD favor strongly consistent data.

Eventually consistent caches MUST NOT create security bypasses.

---

## 56. MICROSERVICE AUTHORIZATION

Each microservice MUST enforce authorization for protected operations.

Example:

```text
Frontend
   ↓
API Gateway
   ↓
Sales Service
   ↓
Authorization Check
   ↓
Database
```

The frontend MUST NOT be trusted.

---

## 57. API GATEWAY AUTHORIZATION

API Gateway MAY perform:

* Token validation
* Basic identity validation
* Rate limiting
* Tenant context validation

Business/resource authorization MUST still be enforced by the target service.

---

## 58. SERVICE-TO-SERVICE AUTHORIZATION

Service A calling Service B MUST be authorized as:

```text
Service Identity
+
Action
+
Resource
+
Tenant
```

Example:

```text
lead-intelligence-service
      ↓
sales-service
      ↓
lead:enrich
```

---

## 59. WEBHOOK AUTHORIZATION

Incoming webhooks MUST validate:

```text
Signature
Timestamp
Replay protection
Source
Tenant
Event type
```

---

## 60. API KEY AUTHORIZATION

API keys MUST support:

```text
Scopes
Tenant
Expiration
Rate limit
Status
Owner
```

---

## 61. OAUTH SCOPE AUTHORIZATION

OAuth scopes MUST be granular.

Example:

```text
leads:read
leads:write
campaigns:read
campaigns:execute
analytics:read
```

---

## 62. AUTHORIZATION FOR INTEGRATIONS

Integrations such as:

```text
Google
Gmail
Slack
HubSpot
Salesforce
Notion
Google Drive
Microsoft Teams
Zendesk
Jira
WhatsApp
Facebook
Instagram
YouTube
TikTok
```

MUST have explicit scopes.

The integration MUST NOT receive permissions beyond those granted by the user/organization.

---

## 63. AI-GENERATED MARKETING AUTHORIZATION

For AI marketing automation:

```text
User
 ↓
Marketing Permission
 ↓
Campaign Permission
 ↓
AI Agent Permission
 ↓
Ad Platform Permission
 ↓
Approval Policy
 ↓
Publish
```

---

## 64. AI-GENERATED SEO AUTHORIZATION

AI SEO agents MAY:

```text
Analyze
Recommend
Draft
Optimize
```

Production publishing SHOULD require:

```text
seo:publish
```

or explicit human approval.

---

## 65. AI SALES AUTHORIZATION

AI Sales Agent MAY:

```text
Analyze leads
Score leads
Generate outreach
Draft responses
Update permitted CRM fields
```

Sending external messages SHOULD be controlled by policy.

---

## 66. AI SUPPORT AUTHORIZATION

AI Support Agent MAY:

```text
Read customer conversation
Generate responses
Classify tickets
Recommend solutions
```

Actions such as:

```text
Refund
Account deletion
Security change
```

SHOULD require human authorization.

---

## 67. FINANCIAL AUTHORIZATION

Financial actions MUST be tightly controlled.

Examples:

```text
Refund
Payment modification
Invoice adjustment
Credit allocation
Billing plan change
```

SHOULD require:

```text
Dedicated permission
+
Risk evaluation
+
MFA
+
Approval where appropriate
```

---

## 68. BILLING AUTHORIZATION

Billing Admin MUST have billing permissions without automatically obtaining organization-wide data access.

Example:

```text
billing:read
billing:manage
invoice:read
invoice:create
refund:request
refund:approve
```

Refund approval SHOULD be separated from refund request.

---

## 69. SECURITY AUTHORIZATION

Security Admin MAY:

```text
Investigate
Review audit logs
Revoke sessions
Manage security policies
Respond to incidents
```

Security-sensitive changes MUST be audited.

---

## 70. USER MANAGEMENT AUTHORIZATION

Administrative user operations SHOULD be separated:

```text
user:read
user:create
user:update
user:suspend
user:delete
user:assign_role
user:reset_mfa
```

Role assignment MUST NOT automatically imply unrestricted data access.

---

## 71. ROLE MANAGEMENT

Only authorized roles may create or modify roles.

Custom roles MUST support:

```text
Name
Description
Permissions
Scope
Status
Created By
Updated By
```

---

## 72. CUSTOM ROLES

Enterprise organizations SHOULD be able to create custom roles.

Example:

```text
Regional Sales Analyst

Permissions:
    lead:read
    analytics:read
    report:create

Scope:
    workplace
```

---

## 73. CUSTOM ROLE SAFETY

Custom roles MUST NOT allow unauthorized privilege escalation.

A user MUST NOT grant themselves permissions they do not possess.

---

## 74. PRIVILEGE ESCALATION PROTECTION

The authorization engine MUST detect:

```text
User grants self admin
User grants broader permission than own scope
AI agent grants permission
Tenant admin creates platform-level permission
```

These MUST be denied.

---

## 75. PERMISSION GRANTING MODEL

A principal may grant only permissions that:

```text
principal itself possesses
AND
principal is allowed to delegate
```

---

## 76. DELEGATION

Delegation MUST include:

```text
Delegator
Delegate
Permission
Resource
Scope
Start
Expiration
Reason
```

---

## 77. AUTHORIZATION AUDIT LOG

Every sensitive authorization change MUST generate an audit event.

Example:

```json
{
  "event_type": "ROLE_PERMISSION_CHANGED",
  "actor_id": "uuid",
  "target_id": "uuid",
  "tenant_id": "uuid",
  "permission": "lead:export",
  "scope": "organization",
  "result": "SUCCESS",
  "timestamp": "2026-08-22T00:00:00Z"
}
```

---

## 78. DENIED ACCESS LOGGING

Security-relevant denied access attempts SHOULD be logged.

The system MUST avoid logging sensitive payloads.

---

## 79. AUTHORIZATION MONITORING

Metrics SHOULD include:

```text
Authorization requests
Allow rate
Deny rate
Approval rate
Policy evaluation latency
Policy failures
Privilege escalation attempts
Cross-tenant access attempts
Sensitive export attempts
AI authorization denials
```

---

## 80. AUTHORIZATION ALERTS

Alerts SHOULD be generated for:

```text
Repeated denied access
Cross-tenant attempts
Privilege escalation
Mass permission changes
Unexpected admin access
Suspicious AI tool usage
Mass data exports
```

---

## 81. AI AUTHORIZATION MONITORING

AI agent activity MUST be observable.

Example:

```text
AI Agent
   ↓
Tool Request
   ↓
Authorization
   ↓
Execution
   ↓
Result
   ↓
Audit
```

---

## 82. AI AGENT GUARDRAILS

AI agents MUST NOT:

```text
Grant themselves permissions
Modify their own authorization
Bypass approval
Access another tenant
Disable security controls
Create unrestricted credentials
```

---

## 83. HUMAN + AI SECURITY MODEL

SalesGenie MUST implement:

```text
AI Detection
+
Policy Engine
+
Security Rules
+
Human Review
```

rather than:

```text
AI alone
```

for critical authorization decisions.

---

## 84. RISK-BASED AUTHORIZATION

Authorization SHOULD incorporate risk.

Example:

```text
Normal request
+
Normal device
+
Normal location
+
Low-value operation
=
ALLOW
```

Whereas:

```text
New device
+
High-value financial operation
+
Unusual location
=
REAUTH / MFA / HUMAN APPROVAL
```

---

## 85. CONTEXTUAL AUTHORIZATION

Policies MAY evaluate:

```text
Time
Location
Device
Network
Authentication strength
Risk
Subscription
Usage
Resource sensitivity
Business state
```

---

## 86. TIME-BASED AUTHORIZATION

Organizations MAY restrict access by time.

Example:

```text
Finance export
Allowed:
09:00–18:00
```

Emergency access MAY override normal schedules under strict controls.

---

## 87. LOCATION-BASED AUTHORIZATION

Location-based policies MAY be supported.

However, they SHOULD use approximate location and SHOULD account for:

* VPN
* Mobile IPs
* Corporate networks
* Geolocation errors

Location MUST NOT be treated as perfect proof of identity.

---

## 88. DEVICE-BASED AUTHORIZATION

Organizations MAY require:

```text
Managed Device
+
MFA
```

for sensitive operations.

---

## 89. NETWORK-BASED AUTHORIZATION

Enterprise customers MAY restrict administrative access to:

```text
Corporate IP ranges
VPN
Private network
Zero-trust network
```

---

## 90. DATA ACCESS POLICIES

Sensitive resources SHOULD support field-level restrictions.

Example:

```text
Support Agent:
customer.name       → ALLOW
customer.email      → ALLOW
customer.revenue    → DENY
payment.details     → DENY
```

---

## 91. FIELD-LEVEL AUTHORIZATION

For highly sensitive resources, authorization SHOULD support:

```text
Object-level access
+
Field-level access
```

---

## 92. MASKING

Unauthorized sensitive fields MAY be masked.

Example:

```text
Full:
user@example.com

Masked:
u***@example.com
```

---

## 93. EXPORT WATERMARKING

Sensitive exports SHOULD include:

```text
Exported By
Organization
Timestamp
Report ID
```

where legally and operationally appropriate.

---

## 94. BULK EXPORT CONTROLS

Large exports SHOULD require:

```text
Export Permission
+
Risk Evaluation
+
Optional Approval
+
Audit
```

---

## 95. AUTHORIZATION API

Conceptual authorization endpoint:

```text
POST /api/v1/authorization/check
```

Request:

```json
{
  "subject": "user-123",
  "action": "lead:update",
  "resource": {
    "type": "lead",
    "id": "lead-456"
  },
  "tenant_id": "tenant-789"
}
```

Response:

```json
{
  "decision": "ALLOW",
  "reason": "TEAM_MEMBER_WITH_EDIT_PERMISSION"
}
```

---

## 96. BATCH AUTHORIZATION

The authorization engine SHOULD support batch checks for UI/data loading.

Example:

```text
Can user:
    read lead A?
    read lead B?
    update lead C?
    export report D?
```

Batch authorization MUST not weaken tenant isolation.

---

## 97. AUTHORIZATION PERFORMANCE

Target authorization latency:

```text
Local cached decision:
< 10 ms target

Central policy decision:
< 50 ms target

Complex resource authorization:
< 100 ms target
```

Authorization MUST NOT become an uncontrolled bottleneck.

---

## 98. HIGH AVAILABILITY

Authorization infrastructure SHOULD provide:

```text
Horizontal scaling
Redundant policy services
Distributed cache
Policy replication
Health checks
Circuit breakers
Observability
```

---

## 99. FAIL-SAFE AUTHORIZATION

For critical security decisions:

```text
Authorization service unavailable
        ↓
DENY
```

The system MUST NOT automatically convert authorization failures into allow decisions.

---

## 100. POLICY VERSIONING

Authorization policies MUST be versioned.

Example:

```text
Policy v1
Policy v2
Policy v3
```

Changes MUST be auditable.

---

## 101. POLICY TESTING

Before deployment, policies SHOULD be tested against:

```text
Allow cases
Deny cases
Tenant isolation
Privilege escalation
Role conflicts
AI agent access
Expired permissions
Temporary permissions
Cross-tenant requests
```

---

## 102. POLICY SIMULATION

Administrators SHOULD be able to simulate:

```text
"Can Sales Agent X update Lead Y?"
```

without actually executing the operation.

Response:

```text
Decision
Policy
Reason
Required approval
```

---

## 103. POLICY CHANGE APPROVAL

Critical authorization policy changes SHOULD require:

```text
Policy administrator
+
Security approval
```

depending on organizational policy.

---

## 104. AUTHORIZATION CACHE INVALIDATION

When any of the following changes:

```text
Role
Permission
Tenant membership
User suspension
Security policy
Subscription
Resource ownership
```

relevant cached decisions MUST be invalidated or expire rapidly.

---

## 105. SUBSCRIPTION + AUTHORIZATION FLOW

```text
User Request
    ↓
Authentication
    ↓
Tenant
    ↓
Role
    ↓
Permission
    ↓
Subscription
    ↓
Usage Limit
    ↓
Risk
    ↓
Approval
    ↓
Decision
```

---

## 106. AI + SUBSCRIPTION AUTHORIZATION

Example:

```text
User requests AI market analysis
        ↓
Authenticated?
        ↓
Tenant valid?
        ↓
Permission?
        ↓
Feature entitlement?
        ↓
Usage available?
        ↓
AI agent authorized?
        ↓
Risk acceptable?
        ↓
ALLOW
```

---

## 107. MARKET INTELLIGENCE AUTHORIZATION

SalesGenie market intelligence features may access:

```text
Market data
Competitor analysis
Industry trends
Customer analytics
Advertising data
```

Access MUST be limited by role and subscription.

---

## 108. DIGITAL MARKETING AUTHORIZATION

Marketing automation MUST support permissions for:

```text
campaign:create
campaign:update
campaign:approve
campaign:publish
campaign:pause
campaign:delete
campaign:export
```

---

## 109. AD PLATFORM AUTHORIZATION

Connected advertising accounts MUST have explicit scopes.

Potential platforms:

```text
Facebook
Instagram
WhatsApp
YouTube
TikTok
```

The system MUST enforce both:

```text
SalesGenie authorization
+
External platform authorization
```

---

## 110. ANALYTICS AUTHORIZATION

Analytics MUST support:

```text
analytics:view
analytics:create
analytics:export
analytics:share
analytics:admin
```

---

## 111. FINANCIAL ANALYTICS AUTHORIZATION

Financial dashboards MUST distinguish:

```text
Revenue
Expenses
Profit
Loss
Product profitability
Ad spend
ROI
```

and enforce role-based access.

---

## 112. REPORT AUTHORIZATION

Reports SHOULD support:

```text
report:view
report:create
report:update
report:share
report:export
report:delete
```

---

## 113. REPORT SHARING

Shared reports MUST support:

```text
Viewer
Commenter
Editor
Owner
```

with expiration where appropriate.

---

## 114. KNOWLEDGE BASE AUTHORIZATION

Knowledge-base resources SHOULD support:

```text
kb:read
kb:create
kb:update
kb:publish
kb:delete
kb:share
```

---

## 115. RAG AUTHORIZATION

AI retrieval MUST enforce authorization before retrieving documents.

Critical rule:

```text
AI cannot retrieve a document
unless the requesting identity is authorized
to access that document.
```

---

## 116. RAG SECURITY

Authorization MUST be applied:

```text
Before Retrieval
+
During Retrieval
+
Before Generation where necessary
```

The model MUST NOT receive unauthorized documents.

---

## 117. CONVERSATION AUTHORIZATION

Customer conversations MUST be scoped by:

```text
Tenant
Workspace
Team
Assignment
Customer
Role
```

---

## 118. SUPPORT ESCALATION AUTHORIZATION

Support agents MAY escalate tickets.

Only authorized roles SHOULD:

```text
Close critical ticket
Access restricted ticket
Approve refund
Modify customer account
```

---

## 119. WORKFLOW AUTHORIZATION

Automation workflows MUST have:

```text
workflow:read
workflow:create
workflow:update
workflow:execute
workflow:publish
workflow:delete
```

---

## 120. HIGH-RISK WORKFLOW ACTIONS

Workflows performing:

```text
Payments
Refunds
Mass messaging
Bulk deletion
Credential changes
Security changes
```

MUST require stricter authorization.

---

## 121. MCP TOOL AUTHORIZATION

If SalesGenie uses MCP servers, every tool invocation MUST be authorized.

```text
User / AI Agent
       ↓
MCP Tool Request
       ↓
Identity
       ↓
Tenant
       ↓
Permission
       ↓
Tool Scope
       ↓
Risk
       ↓
Approval
       ↓
Execution
```

---

## 122. MCP SECURITY

MCP tools MUST NOT receive unrestricted access merely because an AI agent can call them.

---

## 123. TOOL-LEVEL PERMISSIONS

Example:

```text
mcp:google_search
mcp:crm_read
mcp:crm_write
mcp:send_email
mcp:create_campaign
```

Each tool SHOULD have its own permission scope.

---

## 124. WEB SEARCH AUTHORIZATION

AI market-analysis agents MAY access public web information.

Private customer information MUST NOT be sent to external search services without authorization and applicable privacy controls.

---

## 125. EXTERNAL DATA AUTHORIZATION

Data retrieved from:

```text
Google
Fiverr
Upwork
LinkedIn
Advertising platforms
CRM platforms
```

MUST respect the source platform's authorization, terms, scopes and applicable legal constraints.

---

## 126. AUTHORIZATION FOR CONNECTED ACCOUNTS

Every OAuth integration MUST maintain:

```text
integration_id
tenant_id
owner_id
provider
scopes
status
created_at
expires_at
```

---

## 127. TOKEN ACCESS FOR INTEGRATIONS

External access tokens MUST be protected using secure secret storage.

They MUST NOT be exposed to frontend JavaScript unless strictly required by the provider's architecture.

---

## 128. AUTHORIZATION FOR PAYMENT OPERATIONS

Payment operations MUST use dedicated permissions.

Example:

```text
payment:read
payment:create
payment:refund_request
payment:refund_approve
payment:cancel
```

---

## 129. AUTHORIZATION FOR ACCOUNT DELETION

Account deletion MUST require:

```text
Explicit permission
+
Reauthentication
+
Confirmation
+
Audit
```

Organization deletion SHOULD require owner/admin approval and potentially cooling-off mechanisms.

---

## 130. AUTHORIZATION FOR ORGANIZATION DELETION

Organization deletion SHOULD require:

```text
Organization Owner
+
MFA
+
Reauthentication
+
Explicit confirmation
+
Optional security/billing approval
```

---

## 131. AUTHORIZATION FOR ROLE DELETION

Deleting a role MUST verify that:

```text
No critical users depend on it
```

or safely migrate affected users.

---

## 132. AUTHORIZATION FOR PERMISSION CHANGES

Permission changes MUST be audited.

Critical permission escalation SHOULD require dual approval.

---

## 133. SECURITY EVENT RESPONSE

Authorization MUST integrate with the security system.

Example:

```text
Suspicious authorization
        ↓
Risk Engine
        ↓
Security Event
        ↓
AI Analysis
        ↓
Security Admin
        ↓
Session Revocation
        ↓
Incident Management
```

---

## 134. INCIDENT RESPONSE AUTHORIZATION

Security personnel MAY receive emergency permissions through controlled break-glass mechanisms.

Every use MUST be audited.

---

## 135. AUTHORIZATION DATA MODEL

Conceptual entities:

```text
User
Role
Permission
RolePermission
UserRole
Organization
OrganizationMembership
Workplace
WorkplaceMembership
Team
TeamMembership
Resource
ResourceOwnership
Policy
PolicyRule
Entitlement
Approval
Delegation
Session
AuditEvent
ServiceIdentity
AgentIdentity
APIKey
```

---

## 136. ROLE-PERMISSION RELATIONSHIP

```text
User
 |
 +---- UserRole
          |
          ↓
        Role
          |
          ↓
    RolePermission
          |
          ↓
      Permission
```

---

## 137. RESOURCE RELATIONSHIP

```text
Resource
 |
 +-- tenant_id
 +-- organization_id
 +-- workplace_id
 +-- team_id
 +-- owner_id
 +-- classification
```

---

## 138. POLICY ENTITY

A policy SHOULD contain:

```text
policy_id
name
version
subject
action
resource
conditions
effect
priority
status
created_by
updated_by
created_at
updated_at
```

---

## 139. AUTHORIZATION DECISION LOG

The platform SHOULD record:

```text
subject
action
resource
tenant
decision
policy
reason
risk
timestamp
```

Highly sensitive decision logs MUST be protected.

---

## 140. FRONTEND AUTHORIZATION

The frontend MAY use authorization information to:

```text
Hide navigation
Disable buttons
Show permitted modules
Display role-specific dashboards
```

But:

> Frontend authorization MUST NEVER be considered a security boundary.

---

## 141. BACKEND AUTHORIZATION

Every protected backend endpoint MUST perform authorization.

Example:

```text
GET /leads/{id}
        ↓
Authenticate
        ↓
Authorize
        ↓
Tenant check
        ↓
Resource check
        ↓
Return data
```

---

## 142. DATABASE AUTHORIZATION

Where appropriate, SalesGenie SHOULD use database-level controls such as:

```text
Row-Level Security
Database roles
Views
Stored procedures
```

for defense in depth.

---

## 143. ROW-LEVEL SECURITY

Tenant-sensitive tables SHOULD enforce:

```text
tenant_id = current_tenant
```

where technically appropriate.

---

## 144. OBJECT-LEVEL AUTHORIZATION

APIs MUST protect against IDOR/BOLA vulnerabilities.

Example:

```text
GET /leads/123
```

MUST NOT return Lead 123 merely because the user knows the ID.

---

## 145. BOLA PROTECTION

Authorization MUST validate:

```text
User
+
Tenant
+
Resource
+
Relationship
+
Action
```

before returning an object.

---

## 146. MASS ASSIGNMENT PROTECTION

APIs MUST validate writable fields.

Users MUST NOT be able to submit:

```json
{
  "role": "super_admin",
  "tenant_id": "another-tenant"
}
```

and modify protected authorization attributes.

---

## 147. PRIVILEGE ESCALATION TESTING

Automated security tests MUST attempt:

```text
Horizontal privilege escalation
Vertical privilege escalation
Cross-tenant escalation
AI privilege escalation
API privilege escalation
```

---

## 148. HORIZONTAL PRIVILEGE ESCALATION

Example:

```text
Sales Agent A
attempts
Lead belonging to Sales Agent B
```

Expected:

```text
DENY
```

unless policy explicitly allows it.

---

## 149. VERTICAL PRIVILEGE ESCALATION

Example:

```text
Sales Agent
attempts
Organization Admin operation
```

Expected:

```text
DENY
```

---

## 150. CROSS-TENANT ESCALATION

Example:

```text
Tenant A user
attempts
Tenant B resource
```

Expected:

```text
DENY
+
Security event where appropriate
```

---

## 151. AUTHORIZATION TEST MATRIX

| Identity             | Resource          | Action  | Expected |
| -------------------- | ----------------- | ------- | -------- |
| Sales Agent          | Own Lead          | Read    | ALLOW    |
| Sales Agent          | Own Lead          | Update  | ALLOW    |
| Sales Agent          | Other Team Lead   | Delete  | DENY     |
| Sales Manager        | Team Lead         | Update  | ALLOW    |
| Marketing Specialist | Sales Lead        | Delete  | DENY     |
| Finance Manager      | Financial Report  | Read    | ALLOW    |
| Support Agent        | Assigned Ticket   | Update  | ALLOW    |
| Support Agent        | Billing Admin     | Manage  | DENY     |
| Organization Admin   | Organization User | Update  | ALLOW    |
| Workplace Admin      | Other Workplace   | Read    | DENY     |
| AI Sales Agent       | Lead              | Score   | ALLOW    |
| AI Sales Agent       | Billing           | Refund  | DENY     |
| AI Support Agent     | Ticket            | Respond | ALLOW    |
| AI Agent             | Security Policy   | Modify  | DENY     |
| External Client      | Authorized API    | Read    | ALLOW    |
| Tenant A             | Tenant B Resource | Read    | DENY     |

---

## 152. ACCEPTANCE CRITERIA

Authorization is complete when:

```text
[ ] RBAC works
[ ] ABAC works
[ ] ReBAC is supported
[ ] Policy-based authorization works
[ ] Default deny works
[ ] Tenant isolation works
[ ] Workplace isolation works
[ ] Team isolation works
[ ] Resource-level authorization works
[ ] Action-level authorization works
[ ] Read/write separation works
[ ] Delete permissions are explicit
[ ] Export permissions are explicit
[ ] Custom roles work
[ ] Role delegation is protected
[ ] Privilege escalation is prevented
[ ] Temporary permissions work
[ ] Delegated permissions work
[ ] Subscription entitlements work
[ ] Usage limits affect authorization
[ ] AI agents have independent identities
[ ] AI tools require authorization
[ ] Human approval workflows work
[ ] High-risk actions require additional controls
[ ] Billing authorization is isolated
[ ] Security authorization is isolated
[ ] API scopes work
[ ] API keys are scoped
[ ] OAuth scopes are enforced
[ ] MCP tools are authorized
[ ] RAG respects document authorization
[ ] Integrations respect scopes
[ ] Financial data is protected
[ ] Sensitive exports are controlled
[ ] Bulk operations are protected
[ ] Admin impersonation is controlled
[ ] Break-glass access is controlled
[ ] Authorization events are audited
[ ] Authorization denials are monitored
[ ] Policy changes are versioned
[ ] Policy simulation works
[ ] Authorization caching is secure
[ ] Cache invalidation works
[ ] Fail-closed behavior works
[ ] BOLA protection works
[ ] Mass-assignment protection works
[ ] Horizontal escalation tests pass
[ ] Vertical escalation tests pass
[ ] Cross-tenant tests pass
[ ] AI-agent escalation tests pass
[ ] Authorization performance targets are met
[ ] High availability is implemented
```

---

## 153. REFERENCE AUTHORIZATION ARCHITECTURE

```text
                         REQUEST
                            |
                            ↓
                    API GATEWAY / WAF
                            |
                            ↓
                     IDENTITY CHECK
                            |
                            ↓
                    TENANT RESOLUTION
                            |
                            ↓
                  AUTHORIZATION ENGINE
                            |
        +-------------------+-------------------+
        |                   |                   |
       RBAC                ABAC                ReBAC
        |                   |                   |
        +-------------------+-------------------+
                            |
                    RESOURCE POLICY
                            |
                    ACTION PERMISSION
                            |
                    DATA CLASSIFICATION
                            |
                    SUBSCRIPTION ENTITLEMENT
                            |
                       RISK ENGINE
                            |
                    APPROVAL ENGINE
                            |
              +-------------+-------------+
              |             |             |
            ALLOW         DENY        APPROVAL
              |             |             |
              ↓             ↓             ↓
          SERVICE       SECURITY       HUMAN
          EXECUTION       EVENT       REVIEW
              |
              ↓
          AUDIT LOG
```

---

## 154. END-TO-END AUTHORIZATION FLOW

```text
User / AI Agent
       |
       ↓
Authentication
       |
       ↓
Identity Established
       |
       ↓
Tenant Context
       |
       ↓
Role Resolution
       |
       ↓
Permission Resolution
       |
       ↓
Resource Resolution
       |
       ↓
Ownership / Relationship
       |
       ↓
Subscription Entitlement
       |
       ↓
Data Classification
       |
       ↓
Risk Evaluation
       |
       ↓
Approval Requirement
       |
       +----------------------+
       |                      |
     ALLOW                  DENY
       |                      |
       ↓                      ↓
Execute                 Audit / Alert
       |
       ↓
Audit
       |
       ↓
Response
```

---

## 155. FINAL ARCHITECTURAL RULES

SalesGenie authorization MUST enforce:

1. Authentication does not imply authorization.
2. Authorization MUST be enforced server-side.
3. Default behavior MUST be deny.
4. Tenant isolation MUST be mandatory.
5. Roles MUST be scoped.
6. Permissions MUST be granular.
7. Resource ownership MUST be evaluated where appropriate.
8. RBAC MUST be combined with contextual policies.
9. AI agents MUST have independent identities.
10. AI agents MUST never inherit unrestricted human permissions.
11. High-risk AI operations MUST support human approval.
12. Billing permissions MUST be separated from general administration.
13. Security permissions MUST be separated from normal operations.
14. Export permissions MUST be explicit.
15. Delete permissions MUST be explicit.
16. Sensitive data MUST require stronger authorization.
17. API keys MUST be scoped.
18. OAuth scopes MUST be enforced.
19. MCP tools MUST be individually authorized.
20. RAG retrieval MUST respect document-level authorization.
21. Subscription plans MUST control feature entitlements.
22. Usage limits MUST be enforced server-side.
23. Temporary access MUST expire automatically.
24. Delegated access MUST be auditable.
25. Privilege escalation MUST be prevented.
26. Cross-tenant access MUST be denied by default.
27. Administrative impersonation MUST be controlled and audited.
28. Break-glass access MUST be restricted and monitored.
29. Critical operations SHOULD use separation of duties.
30. Authorization policies MUST be versioned.
31. Authorization decisions MUST be observable.
32. Authorization failures MUST fail closed.
33. Authorization caches MUST never create security bypasses.
34. Authorization policy changes MUST be auditable.
35. Authorization MUST remain independent from frontend visibility.
36. Authorization MUST protect against BOLA/IDOR vulnerabilities.
37. Authorization MUST protect against mass assignment.
38. Authorization MUST support both human and machine identities.
39. AI security analysis MAY assist authorization decisions but MUST NOT independently bypass security policy.
40. Human security intervention MUST remain available for critical authorization decisions.

---

## 156. DEFINITION OF DONE

The SalesGenie authorization platform is production-ready when every protected operation can answer:

```text
WHO
 ↓
WHAT IDENTITY?
 ↓
WHICH TENANT?
 ↓
WHICH WORKPLACE?
 ↓
WHICH TEAM?
 ↓
WHICH ROLE?
 ↓
WHICH PERMISSION?
 ↓
WHICH RESOURCE?
 ↓
WHICH ACTION?
 ↓
WHO OWNS IT?
 ↓
WHICH RELATIONSHIP?
 ↓
WHICH DATA CLASSIFICATION?
 ↓
WHICH SUBSCRIPTION?
 ↓
WHAT USAGE LIMIT?
 ↓
WHAT RISK?
 ↓
IS APPROVAL REQUIRED?
 ↓
FINAL DECISION
```

with one of:

```text
ALLOW
DENY
REQUIRE_MFA
REQUIRE_REAUTHENTICATION
REQUIRE_APPROVAL
```

The fundamental SalesGenie authorization rule is:

> **No identity, human or AI, may access a resource merely because it is authenticated. Access MUST be explicitly authorized according to identity, tenant, role, permission, resource, action, context, policy, entitlement, and risk.**
