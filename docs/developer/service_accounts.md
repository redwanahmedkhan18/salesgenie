# Service Accounts — User, System & Functional Requirements

**Project:** SalesGenie / FlowMind AI  
**Requirement Type:** Service Account Management Platform  
**File:** `service_accounts.md`  
**Architecture:** Enterprise SaaS + Multi-Tenant + Microservices + Event-Driven + Multi-Agent AI + API-First  
**Actors:** Human Users + AI Agents + Machine Workloads + External Integrations  
**Target Scale:** 10M+ users, 500K+ concurrent conversations  
**Priority:** P0 — Core Identity & Developer Platform Capability

---

## 1. Purpose

The Service Accounts subsystem provides non-human identities for applications, backend services, automation systems, integrations, scheduled jobs, data pipelines, AI agents, and other machine-to-machine workloads operating within SalesGenie.

The system SHALL provide:

- Service account creation
- Ownership management
- Application association
- Environment isolation
- Tenant isolation
- Credential management
- Scope management
- Role assignment
- Credential rotation
- Credential expiration
- Service account suspension
- Service account revocation
- Machine-to-machine authentication
- AI-agent identity management
- Delegated authorization
- Human approval workflows
- Policy enforcement
- Usage monitoring
- Security monitoring
- Audit logging
- Credential compromise detection
- Emergency disablement
- Lifecycle automation

Service accounts SHALL represent **workload identities**, not human identities.

---

## 2. Product Goals

The Service Account Platform SHALL:

1. Provide secure machine identity.
2. Eliminate unnecessary use of human credentials by applications.
3. Support machine-to-machine authentication.
4. Support AI-agent identities.
5. Enforce least privilege.
6. Provide tenant isolation.
7. Provide application-level identity.
8. Support multiple authentication mechanisms.
9. Support credential rotation.
10. Support short-lived credentials where possible.
11. Support production approval workflows.
12. Provide complete auditability.
13. Detect anomalous workload behavior.
14. Integrate with API Gateway.
15. Integrate with Developer Platform.
16. Integrate with API Key Management.
17. Integrate with OAuth/OIDC infrastructure.
18. Support enterprise governance.
19. Support automated lifecycle management.
20. Support millions of machine identities.

---

## 3. Core Principle

```text
Human Identity ≠ Service Account ≠ AI Agent Identity
```

A service account SHALL represent a workload or system identity.

Example:

```text
Human:
user_123

Application:
app_salesgenie_crm

Service Account:
svc_crm_sync

AI Agent:
agent_sales_qualification
```

These identities SHALL remain independently auditable.

---

## 4. Actors

## 4.1 Human Actors

### H-001 — Developer

Creates and manages service accounts for applications.

### H-002 — Application Owner

Owns service accounts associated with an application.

### H-003 — DevOps Engineer

Deploys service accounts into workloads.

### H-004 — Platform Engineer

Manages service identity infrastructure.

### H-005 — Organization Administrator

Controls organization-wide service accounts.

### H-006 — Security Administrator

Controls service account security policies.

### H-007 — Compliance Administrator

Audits machine identities.

### H-008 — Platform Administrator

Manages global identity policies.

---

## 5. AI Actors

### AI-001 — Sales Agent

Uses a service identity to execute sales operations.

### AI-002 — Support Agent

Uses a service identity to perform customer support actions.

### AI-003 — Workflow Agent

Executes automated workflows.

### AI-004 — Analytics Agent

Accesses analytics services.

### AI-005 — Data Agent

Executes authorized data processing operations.

### AI-006 — Autonomous Agent

Performs multi-step tasks within delegated permissions.

### AI-007 — Agent Orchestrator

Creates or manages identities for AI workloads under policy.

---

## 6. Identity Hierarchy

```text
Organization
      │
      ├── Human Users
      │
      ├── Applications
      │       │
      │       ├── Service Accounts
      │       │       ├── Credentials
      │       │       └── Permissions
      │       │
      │       └── AI Agents
      │               ├── Identity
      │               ├── Permissions
      │               └── Credentials
      │
      └── Policies
```

---

## 7. User Requirements

## UR-001 — Create Service Account

Authorized users SHALL be able to create a service account.

Required information:

* Name
* Description
* Organization
* Tenant
* Application
* Environment
* Purpose
* Owner
* Roles
* Scopes
* Expiration policy

---

## UR-002 — Service Account Naming

Users SHALL be able to provide human-readable service account names.

Examples:

```text
CRM Synchronization
Lead Intelligence Worker
Analytics Pipeline
Customer Support Worker
AI Sales Agent
Email Campaign Worker
```

---

## UR-003 — Unique Identity

Every service account SHALL have a globally unique identifier.

Example:

```text
svc_01JXYZABC123
```

---

## UR-004 — Service Account Ownership

Every service account SHALL have one or more responsible human owners or an owning team.

---

## UR-005 — Ownership Transfer

Authorized administrators SHALL be able to transfer ownership.

Ownership transfers SHALL be audited.

---

## 8. Environment Requirements

Service accounts SHALL support:

```text
development
sandbox
staging
production
```

A production service account SHALL NOT automatically authenticate against development or sandbox resources.

---

## 9. Tenant Isolation

Service accounts SHALL be tenant-scoped.

```text
Tenant A
   └── svc_crm_sync_A

Tenant B
   └── svc_crm_sync_B
```

A service account from Tenant A SHALL NOT access Tenant B resources unless explicitly authorized through a controlled platform-level mechanism.

---

## 10. Application Binding

Every service account SHOULD be associated with an application or workload.

Example:

```text
Application
    ↓
CRM Integration
    ↓
Service Account
    ↓
CRM Sync Worker
```

---

## 11. Purpose Declaration

Users SHALL provide the intended purpose of a service account.

Examples:

```text
CRM synchronization
Email processing
Lead enrichment
Workflow execution
Analytics ingestion
AI agent execution
Webhook processing
Background job
```

---

## 12. Permission Requirements

Service accounts SHALL use least-privilege permissions.

Users SHALL explicitly select:

* Roles
* Scopes
* Resources
* Operations
* Environment

---

## 13. Scope Examples

```text
leads.read
leads.write
customers.read
customers.write
conversations.read
conversations.write
workflows.execute
analytics.read
webhooks.read
webhooks.write
knowledge.read
knowledge.write
agents.execute
```

---

## 14. Credential Requirements

A service account SHALL support one or more authentication mechanisms.

Possible mechanisms:

```text
API Key
OAuth 2.0 Client Credentials
OIDC Workload Identity
JWT
mTLS
Signed Requests
Short-Lived Access Token
Cloud Workload Identity
```

The preferred mechanism SHALL depend on workload and deployment environment.

---

## 15. Credential Creation

Authorized users SHALL be able to create credentials for service accounts.

Credentials SHALL be independently revocable from the service account.

---

## 16. One-Time Secret Display

Long-lived secrets SHALL only be displayed once during creation.

The platform SHALL NOT provide plaintext secret recovery.

---

## 17. Credential Rotation

Users SHALL be able to rotate service account credentials without unnecessary downtime.

---

## 18. Credential Expiration

Service account credentials SHALL support expiration.

Example:

```text
30 days
90 days
180 days
365 days
Custom
```

---

## 19. Service Account Expiration

The service account itself MAY have an expiration date.

Example:

```text
Temporary Migration Worker
Expires: 2026-10-01
```

---

## 20. Temporary Service Accounts

Users SHALL be able to create temporary service accounts for:

* Migrations
* Testing
* Incident response
* Data imports
* One-time integrations
* Temporary AI experiments

Temporary identities SHOULD automatically expire.

---

## 21. Service Account Lifecycle

Service accounts SHALL support:

```text
CREATING
PENDING_APPROVAL
ACTIVE
SUSPENDED
EXPIRING_SOON
EXPIRED
COMPROMISED
DISABLED
REVOKED
DELETED
```

---

## 22. Lifecycle Transition

```text
CREATING
   ↓
PENDING_APPROVAL
   ↓
ACTIVE
   ├──→ SUSPENDED
   ├──→ EXPIRING_SOON
   ├──→ COMPROMISED
   └──→ DISABLED
             ↓
          REVOKED
             ↓
          DELETED
```

---

## 23. Service Account Suspension

Authorized administrators SHALL be able to temporarily suspend service accounts.

Suspension SHALL immediately prevent new authentication.

---

## 24. Service Account Reinstatement

Authorized administrators SHALL be able to reactivate suspended accounts after security validation.

---

## 25. Emergency Disablement

Security administrators SHALL have an emergency disable mechanism.

Supported targets:

```text
Single Service Account
Application
Environment
Tenant
Organization
AI Agent
Credential Family
```

---

## 26. Human Approval

Organizations SHALL be able to require human approval for:

* Production service accounts
* Privileged scopes
* Billing access
* Customer-data export
* Administrative access
* AI-agent service accounts
* Cross-tenant operations

---

## 27. Production Approval Workflow

```text
Developer
   ↓
Create Service Account
   ↓
Select Production
   ↓
Select Permissions
   ↓
Policy Evaluation
   ↓
Security Review
   ↓
Admin Approval
   ↓
Credential Creation
   ↓
Deployment
```

---

## 28. AI Service Accounts

AI agents SHALL be able to operate through dedicated service identities.

Example:

```text
AI Sales Agent
      ↓
svc_ai_sales_agent
      ↓
sales.leads.read
sales.leads.write
      ↓
API Gateway
```

---

## 29. AI Identity Separation

Every autonomous AI agent SHOULD have a unique identity.

```text
Agent A → svc_agent_a
Agent B → svc_agent_b
Agent C → svc_agent_c
```

Agents SHOULD NOT share unrestricted credentials.

---

## 30. AI Credential Delegation

AI agents SHOULD receive delegated permissions rather than organization-wide credentials.

```text
Human
  ↓
Authorize Agent
  ↓
Delegated Capability
  ↓
Limited Scope
  ↓
Expiration
```

---

## 31. AI High-Risk Operations

The following MAY require human approval:

```text
customer.delete
customer.export
billing.modify
campaign.bulk_send
organization.update
user.delete
service_account.create
service_account.revoke
```

---

## 32. AI Policy Enforcement

AI service account requests SHALL pass through the same authorization system as human-originated requests.

---

## 33. AI Risk Assessment

The platform SHOULD calculate AI workload risk using:

```text
Agent Identity
Scope
Requested Operation
Historical Behavior
Request Volume
Resource Sensitivity
Environment
Network Origin
Credential Age
```

---

## 34. AI Automated Response

Organizations MAY configure:

```text
LOW
→ Allow

MEDIUM
→ Monitor

HIGH
→ Require Approval

CRITICAL
→ Suspend
```

---

## 35. Human Override

Authorized security administrators SHALL be able to override automated AI identity decisions.

Every override SHALL be audited.

---

## 36. System Requirements

## SR-001 — Identity Service

SalesGenie SHALL provide a dedicated service identity subsystem.

Recommended architecture:

```text
Identity Platform
       ↓
Service Account Service
       ↓
Credential Service
       ↓
Policy Engine
       ↓
Authorization Service
       ↓
API Gateway
```

---

## 37. Service Account Service

The Service Account Service SHALL manage:

* Identity
* Ownership
* Lifecycle
* Metadata
* Applications
* Environment
* Roles
* Policies
* Credentials
* Audit events

---

## 38. Credential Service

Credential operations SHOULD be isolated from service-account metadata.

```text
Service Account Service
        ↓
Credential Service
        ↓
KMS / Secret Manager
```

---

## 39. Credential Storage

Secrets SHALL NOT be stored in plaintext.

The platform SHALL use secure cryptographic storage and/or one-way verification mechanisms appropriate to credential type.

---

## 40. KMS/HSM

Production cryptographic material SHOULD be protected by:

* KMS
* HSM
* Cloud Secret Manager
* Enterprise Vault

---

## 41. Secret Isolation

Service account credentials SHALL be logically isolated from ordinary application data.

---

## 42. Database Model

Conceptual table:

```text
service_accounts
----------------
id
organization_id
tenant_id
application_id
owner_id
name
description
purpose
environment
status
service_type
created_at
updated_at
expires_at
last_used_at
risk_score
metadata
```

---

## 43. Credential Model

```text
service_account_credentials
---------------------------
id
service_account_id
credential_type
credential_identifier
secret_hash
created_at
expires_at
last_used_at
revoked_at
status
rotation_parent_id
rotation_child_id
```

---

## 44. Permission Model

```text
service_account_permissions
---------------------------
id
service_account_id
role
scope
resource
action
granted_by
granted_at
expires_at
```

---

## 45. Ownership Model

```text
service_account_owners
----------------------
id
service_account_id
owner_type
owner_id
role
created_at
```

---

## 46. Audit Model

```text
service_account_audit_events
----------------------------
id
service_account_id
organization_id
tenant_id
actor_type
actor_id
event_type
timestamp
request_id
trace_id
ip_address
user_agent
reason
approval_id
metadata
```

---

## 47. AI Identity Model

```text
ai_service_identities
---------------------
id
service_account_id
agent_id
agent_type
agent_version
model_provider
model_name
policy_id
risk_level
created_at
expires_at
```

---

## 48. Functional Requirements

## FR-001 — Create Service Account

The platform SHALL expose:

```http
POST /api/v1/developer/service-accounts
```

---

## 49. Example Creation Request

```json
{
  "name": "CRM Synchronization",
  "application_id": "app_123",
  "environment": "production",
  "purpose": "Synchronize CRM contacts",
  "scopes": [
    "customers.read",
    "customers.write"
  ],
  "expires_at": "2027-08-29T00:00:00Z"
}
```

---

## 50. Creation Response

```json
{
  "id": "svc_01JXYZ",
  "name": "CRM Synchronization",
  "status": "ACTIVE",
  "environment": "production",
  "created_at": "2026-08-29T00:00:00Z"
}
```

Secrets SHALL be returned only through credential-generation operations.

---

## 51. List Service Accounts

The platform SHALL provide:

```http
GET /api/v1/developer/service-accounts
```

Filtering SHALL support:

```text
organization
tenant
application
environment
status
owner
purpose
service_type
```

---

## 52. Retrieve Service Account

```http
GET /api/v1/developer/service-accounts/{service_account_id}
```

The response SHALL exclude secrets.

---

## 53. Update Service Account

```http
PATCH /api/v1/developer/service-accounts/{service_account_id}
```

Mutable fields MAY include:

```text
name
description
purpose
owner
metadata
expiration
```

---

## 54. Delete Service Account

```http
DELETE /api/v1/developer/service-accounts/{service_account_id}
```

Deletion SHALL follow configured retention and audit policies.

Production service accounts SHOULD require explicit revocation before deletion.

---

## 55. Suspend Service Account

```http
POST /api/v1/developer/service-accounts/{service_account_id}/suspend
```

---

## 56. Activate Service Account

```http
POST /api/v1/developer/service-accounts/{service_account_id}/activate
```

---

## 57. Revoke Service Account

```http
POST /api/v1/developer/service-accounts/{service_account_id}/revoke
```

Revocation SHALL be idempotent.

---

## 58. Create Credential

```http
POST /api/v1/developer/service-accounts/{service_account_id}/credentials
```

---

## 59. Rotate Credential

```http
POST /api/v1/developer/service-accounts/{service_account_id}/credentials/{credential_id}/rotate
```

---

## 60. Revoke Credential

```http
POST /api/v1/developer/service-accounts/{service_account_id}/credentials/{credential_id}/revoke
```

---

## 61. List Credentials

```http
GET /api/v1/developer/service-accounts/{service_account_id}/credentials
```

The response SHALL never expose complete secrets.

---

## 62. Permission Management

The platform SHALL support:

```http
GET  /api/v1/developer/service-accounts/{id}/permissions
POST /api/v1/developer/service-accounts/{id}/permissions
PATCH /api/v1/developer/service-accounts/{id}/permissions/{permission_id}
DELETE /api/v1/developer/service-accounts/{id}/permissions/{permission_id}
```

---

## 63. Ownership Management

The platform SHALL support:

```http
GET  /api/v1/developer/service-accounts/{id}/owners
POST /api/v1/developer/service-accounts/{id}/owners
DELETE /api/v1/developer/service-accounts/{id}/owners/{owner_id}
```

---

## 64. Authentication Flow

```text
Workload
   ↓
Credential
   ↓
API Gateway
   ↓
Credential Validation
   ↓
Service Account Resolution
   ↓
Tenant Resolution
   ↓
Environment Validation
   ↓
Status Validation
   ↓
Scope Validation
   ↓
Policy Evaluation
   ↓
Rate Limit
   ↓
Authorization
   ↓
SalesGenie Service
```

---

## 65. Identity Propagation

The gateway SHOULD propagate trusted identity metadata internally:

```text
service_account_id
application_id
tenant_id
organization_id
environment
agent_id
request_id
trace_id
```

The raw credential SHALL never be propagated.

---

## 66. Authorization

Every service account request SHALL be evaluated against:

```text
Identity
Tenant
Application
Environment
Role
Scope
Resource
Action
Policy
Risk
```

---

## 67. Role-Based Access Control

Service accounts SHALL support roles.

Examples:

```text
crm.integration
analytics.worker
support.agent
sales.agent
workflow.worker
data.pipeline
```

---

## 68. Attribute-Based Access Control

ABAC MAY evaluate:

```text
Environment
Network
Tenant
Application
Service Account
Resource
Action
Time
Risk
Agent
```

---

## 69. Scope-Based Access Control

Scopes SHALL provide fine-grained permissions.

Example:

```text
customers.read
```

SHALL NOT automatically imply:

```text
customers.write
```

---

## 70. Resource-Level Restrictions

Service accounts SHOULD support resource-level restrictions.

Example:

```text
customers.read
WHERE customer_group = "enterprise"
```

---

## 71. Network Restrictions

Production service accounts SHOULD support:

* IP allowlists
* CIDR ranges
* Private networks
* VPN-only access
* Region restrictions
* mTLS

---

## 72. Rate Limiting

Service accounts SHALL be rate-limited independently.

Limits MAY exist at:

```text
Organization
Tenant
Application
Service Account
Credential
Endpoint
Agent
```

---

## 73. Usage Tracking

The platform SHALL track:

```text
request_count
success_count
failure_count
last_used_at
last_used_ip
endpoint_usage
scope_usage
latency
rate_limit_events
```

---

## 74. Service Account Dashboard

The Developer Portal SHALL provide:

```text
Service Accounts
─────────────────────────────

Name
Application
Environment
Owner
Status
Scopes
Last Used
Expires
Risk

[View] [Rotate] [Suspend] [Revoke]
```

---

## 75. Service Account Details

The detail page SHALL display:

```text
Identity
Owner
Application
Environment
Purpose
Permissions
Credentials
Usage
Security
Audit
Policies
AI Association
```

---

## 76. Credential Dashboard

The credential interface SHALL show:

```text
Credential ID
Type
Status
Created
Last Used
Expires
Rotation Status
Risk
```

The complete credential secret SHALL never be displayed after initial issuance.

---

## 77. Expiration Monitoring

The platform SHALL identify:

```text
Expired
Expiring in 30 days
Expiring in 14 days
Expiring in 7 days
Expiring in 3 days
Expiring in 24 hours
```

---

## 78. Automatic Expiration

Expired credentials SHALL automatically become invalid.

---

## 79. Automatic Service Account Deactivation

Organizations MAY configure automatic deactivation when a service account reaches its expiration date.

---

## 80. Rotation Strategy

Zero-downtime rotation SHALL follow:

```text
Old Credential
     ↓
ACTIVE

New Credential
     ↓
ACTIVE

Application Migration
     ↓
Old Credential
     ↓
GRACE_PERIOD
     ↓
REVOKED
```

---

## 81. Rotation Grace Period

Organizations SHALL be able to configure:

```text
15 minutes
1 hour
6 hours
24 hours
7 days
Custom
```

---

## 82. Automatic Rotation

The platform SHOULD support scheduled credential rotation.

Example:

```text
Every 90 days
```

The rotation engine SHALL:

1. Generate replacement.
2. Preserve required permissions.
3. Notify owners.
4. Activate replacement.
5. Maintain grace period.
6. Revoke old credential.

---

## 83. Secret Leakage Protection

Service account credentials SHALL never appear in:

* Logs
* Error messages
* URLs
* Analytics events
* Audit events
* Metrics
* Traces
* Browser telemetry

---

## 84. Secret Scanning

The platform SHOULD identify leaked credentials in:

* Git repositories
* CI/CD logs
* Uploaded source code
* Configuration files
* Developer environments

---

## 85. Compromise Detection

The platform SHOULD detect:

```text
Unexpected IP
Unexpected geography
Sudden request spike
Abnormal endpoint usage
Scope abuse
Credential sharing
Impossible travel
New ASN
Unusual user-agent
```

---

## 86. Risk Score

Each service account MAY have a dynamic risk score:

```text
Risk =
Credential Age
+
Scope Privilege
+
Behavioral Anomaly
+
Network Anomaly
+
Usage Velocity
+
Environment Sensitivity
```

---

## 87. Security Response

Based on risk:

```text
LOW
→ Monitor

MEDIUM
→ Alert

HIGH
→ Throttle

CRITICAL
→ Suspend / Revoke
```

---

## 88. Security Alerts

Alerts SHALL be generated for:

* New production service account
* Privileged permission grant
* Credential creation
* Credential rotation
* Credential revocation
* Suspicious usage
* Credential compromise
* Expiration
* Ownership transfer
* AI privilege escalation

---

## 89. Notification Channels

Supported channels MAY include:

```text
In-App
Email
Push
Slack
Webhook
SIEM
```

---

## 90. Audit Logging

The following events SHALL be audited:

```text
service_account.created
service_account.updated
service_account.activated
service_account.suspended
service_account.revoked
service_account.deleted
service_account.owner_changed
service_account.permission_added
service_account.permission_removed
service_account.credential_created
service_account.credential_rotated
service_account.credential_revoked
service_account.compromised
service_account.expired
```

---

## 91. AI Audit Events

AI service accounts SHALL additionally record:

```text
agent_id
agent_version
model_provider
model_name
execution_id
tool_name
requested_action
policy_decision
human_approval
risk_score
```

---

## 92. Audit Immutability

Credential and service identity audit records SHALL be append-only and tamper-resistant.

---

## 93. Compliance Requirements

The Service Account Platform SHALL support organizational requirements associated with:

* SOC 2
* ISO 27001
* GDPR
* CCPA/CPRA
* Enterprise security policies
* Internal access-control policies

---

## 94. Compliance Questions

Auditors SHALL be able to answer:

```text
Which service accounts exist?

Who owns them?

Why do they exist?

What applications use them?

What permissions do they have?

Which credentials are active?

When were credentials rotated?

When were they last used?

Who approved production access?

Which AI agents use them?

Which operations were executed?
```

---

## 95. Dormant Account Detection

The system SHALL identify service accounts with no recent usage.

Example:

```text
No usage for:
30 days
60 days
90 days
180 days
```

---

## 96. Dormant Account Policy

Organizations MAY automatically:

```text
Alert
Suspend
Require Review
Revoke
```

---

## 97. Overprivileged Account Detection

AI and rule-based analysis SHOULD identify service accounts with permissions significantly exceeding observed usage.

Example:

```text
Granted:
customers.read
customers.write
customers.delete
billing.write
admin.write

Observed:
customers.read
```

Recommendation:

```text
Remove unused privileged scopes.
```

---

## 98. Human Approval for Privileged Permissions

Permissions such as:

```text
admin.*
billing.write
customer.delete
data.export
organization.*
```

SHOULD require additional approval.

---

## 99. AI Privilege Escalation Protection

An AI agent SHALL NOT be able to grant itself additional service-account permissions.

```text
AI Agent
   ↓
Request Permission
   ↓
Policy Engine
   ↓
Human / Admin Approval
   ↓
Permission Granted
```

---

## 100. Service Account Creation by AI

AI agents MAY request service accounts only if explicitly permitted.

Default policy:

```text
AI → Cannot create privileged production identity
```

---

## 101. Human Approval for AI-Created Identities

Organizations SHALL be able to require human approval before an AI-generated service identity becomes active.

---

## 102. AI Agent Identity Lifecycle

```text
AI Agent Registered
       ↓
Identity Created
       ↓
Policy Assigned
       ↓
Human Approval
       ↓
Credential Issued
       ↓
Agent Executes
       ↓
Monitoring
       ↓
Risk Change
       ↓
Reauthorization / Suspension
```

---

## 103. Agent Isolation

AI agents SHALL be isolated by:

```text
Agent ID
Service Account ID
Tenant
Application
Environment
Scopes
Policy
```

---

## 104. Service-to-Service Authentication

SalesGenie microservices SHOULD use service identities for internal authentication.

Example:

```text
Lead Service
    ↓
svc_lead_service
    ↓
AI Gateway
```

---

## 105. Internal Service Identity

Internal services SHALL not depend on shared static administrator credentials.

---

## 106. Workload Identity

Where infrastructure supports it, SalesGenie SHOULD prefer workload identity over long-lived secrets.

Examples:

```text
OIDC
Cloud Workload Identity
mTLS
SPIFFE/SPIRE
Short-Lived JWT
```

---

## 107. API Key Integration

Service accounts MAY own API keys managed through the Developer API Key platform.

Relationship:

```text
Service Account
      ↓
API Credential
      ↓
API Key
```

---

## 108. OAuth Integration

Service accounts SHOULD support OAuth 2.0 Client Credentials where appropriate.

```text
Service Account
      ↓
Client ID + Secret
      ↓
Token Endpoint
      ↓
Access Token
      ↓
API Gateway
```

---

## 109. Short-Lived Tokens

Where possible:

```text
Long-Lived Identity
        ↓
Short-Lived Access Token
        ↓
API Request
```

SHALL be preferred over persistent high-privilege credentials.

---

## 110. mTLS Integration

Enterprise deployments MAY use mutual TLS for service authentication.

---

## 111. Certificate Lifecycle

If mTLS is used, the platform SHALL support:

* Certificate issuance
* Certificate expiration
* Certificate rotation
* Certificate revocation
* Certificate inventory
* Certificate audit

---

## 112. Service Account Policies

Organizations SHALL be able to configure:

```text
Maximum Lifetime
Credential Lifetime
Rotation Frequency
Allowed Credential Types
Required MFA for Management
Production Approval
Allowed Scopes
Network Restrictions
Maximum Accounts
Dormancy Threshold
AI Account Restrictions
```

---

## 113. Policy Evaluation

Every service account lifecycle operation SHALL pass through policy evaluation.

```text
Request
  ↓
Identity
  ↓
Policy
  ↓
Risk
  ↓
Approval
  ↓
Decision
```

---

## 114. Policy Precedence

Recommended order:

```text
Global Policy
    ↓
Organization Policy
    ↓
Tenant Policy
    ↓
Application Policy
    ↓
Environment Policy
    ↓
Service Account Policy
```

The most restrictive applicable policy SHALL win unless explicitly overridden by a higher-authority security policy.

---

## 115. Zero Trust

Service account authentication SHALL not imply unrestricted access.

Every request SHALL independently evaluate authorization.

---

## 116. Fail-Closed

If identity or authorization cannot be validated:

```text
DENY
```

The system SHALL never default to allowing privileged operations.

---

## 117. Revocation Propagation

Credential and service-account revocations SHALL propagate rapidly throughout the platform.

Recommended target:

```text
P95 revocation propagation ≤ 30 seconds
```

Critical security environments SHOULD target near-real-time invalidation.

---

## 118. Distributed Cache

Credential and policy caches MAY be used for performance.

Caches SHALL support:

* Tenant isolation
* Short TTL
* Revocation invalidation
* Secure keying
* No plaintext secrets

---

## 119. Concurrency Control

The system SHALL protect against:

```text
Concurrent credential rotation
Concurrent revocation
Permission update during rotation
Ownership change during deletion
Activation during suspension
```

---

## 120. Idempotency

The following operations SHALL support idempotency:

```text
Create
Activate
Suspend
Revoke
Rotate Credential
Delete
```

---

## 121. API Versioning

The service account APIs SHALL support versioning.

Example:

```text
/api/v1/developer/service-accounts
/api/v2/developer/service-accounts
```

---

## 122. Backward Compatibility

Existing service accounts SHALL remain functional during supported API migrations unless security policies require intervention.

---

## 123. Event Architecture

Service account lifecycle events SHALL be published to the SalesGenie event platform.

Example:

```text
Service Account Service
        ↓
Event Bus
        ↓
 ┌──────┼───────────┐
 ▼      ▼           ▼
Audit  Analytics  Notification
```

---

## 124. Event Examples

```json
{
  "event_type": "service_account.created",
  "service_account_id": "svc_123",
  "organization_id": "org_123",
  "tenant_id": "tenant_123",
  "environment": "production",
  "actor_type": "human",
  "actor_id": "user_123",
  "timestamp": "2026-08-29T00:00:00Z"
}
```

---

## 125. AI Event Example

```json
{
  "event_type": "service_account.requested",
  "service_account_id": "svc_ai_sales",
  "agent_id": "agent_123",
  "actor_type": "ai_agent",
  "requested_scopes": [
    "leads.read",
    "leads.write"
  ],
  "risk_level": "medium",
  "approval_required": true
}
```

---

## 126. Observability

The platform SHALL expose metrics:

```text
service_accounts_total
service_accounts_active
service_accounts_suspended
service_accounts_expired
service_account_auth_success_total
service_account_auth_failure_total
service_account_credential_rotations_total
service_account_revocations_total
service_account_compromise_events_total
service_account_policy_denials_total
service_account_auth_latency
```

---

## 127. Distributed Tracing

Service account operations SHALL support:

```text
request_id
trace_id
span_id
service_account_id
application_id
tenant_id
```

Secrets SHALL never appear in traces.

---

## 128. Performance Requirements

Service account authentication SHOULD add minimal latency.

Recommended target:

```text
Authentication P95 ≤ 50 ms
```

excluding external network latency.

---

## 129. Availability Requirements

The service identity system SHOULD target:

```text
≥ 99.99% availability
```

for production authentication and authorization.

---

## 130. Scalability

The architecture SHALL support:

```text
Millions of service accounts
Millions of credentials
Millions of applications
Hundreds of thousands of concurrent requests
Large-scale AI agent workloads
```

---

## 131. Failure Handling

If the identity database becomes temporarily unavailable:

```text
New Account Creation
→ Fail safely

Credential Rotation
→ Fail safely

Credential Revocation
→ Prioritize security

Authorization
→ Fail closed
```

---

## 132. Disaster Recovery

The platform SHALL support:

* Backup
* Replication
* Point-in-time recovery
* Regional failover
* Credential metadata recovery
* Audit-log recovery

Secrets SHALL be handled according to secure backup policies.

---

## 133. Backup Security

Credential-related backup data SHALL be encrypted and access-controlled.

---

## 134. Disaster Recovery Targets

Recommended:

```text
RPO ≤ 5 minutes
RTO ≤ 30 minutes
```

Critical identity infrastructure MAY require stronger targets.

---

## 135. Security Testing

Testing SHALL include:

```text
Authentication bypass
Authorization bypass
Tenant isolation
Scope escalation
Credential brute force
Credential enumeration
Replay attacks
Secret leakage
Race conditions
Revocation propagation
AI privilege escalation
Policy bypass
```

---

## 136. Penetration Testing

The service identity system SHALL undergo regular security testing.

---

## 137. Chaos Testing

The platform SHOULD test:

```text
Database failure
Cache failure
Event bus failure
Network partition
Credential store failure
Region failure
Policy engine failure
Gateway failure
```

---

## 138. Load Testing

The platform SHALL test:

```text
High authentication volume
Mass credential rotation
Mass account revocation
Mass AI-agent activity
Large tenant workloads
Large application fleets
```

---

## 139. Developer Experience

The Developer Portal SHALL make secure service identity creation straightforward.

Recommended flow:

```text
Create Service Account
        ↓
Select Application
        ↓
Select Environment
        ↓
Define Purpose
        ↓
Select Permissions
        ↓
Configure Credential
        ↓
Configure Expiration
        ↓
Review Security
        ↓
Approval
        ↓
Create
```

---

## 140. Service Account Security Score

The dashboard MAY show:

```text
Identity Health
Credential Health
Permission Health
Usage Health
Security Risk
Compliance Health
```

---

## 141. Security Recommendations

The platform SHOULD provide recommendations such as:

```text
Rotate credential
Remove unused scope
Enable expiration
Enable IP restriction
Replace API key with workload identity
Disable dormant account
Require production approval
```

---

## 142. AI Security Recommendations

AI SHALL be able to recommend:

```text
Least-privilege scope reduction
Credential rotation
Dormant account removal
Suspicious usage investigation
Network restriction
Shorter credential lifetime
Human approval requirement
```

AI recommendations SHALL be explainable.

---

## 143. Explainable AI Decision

Example:

```text
Recommendation: HIGH PRIORITY

The service account has:
- 9 granted scopes
- 2 scopes used in the last 90 days
- 3 administrative permissions
- Production access

Recommendation:
Remove unused privileged scopes and require approval
for future permission changes.
```

---

## 144. Human + AI Workflow

```text
Human Developer
       ↓
Create Service Account
       ↓
AI Security Analysis
       ↓
Policy Engine
       ↓
Permission Risk Analysis
       ↓
Human Approval
       ↓
Credential Issued
       ↓
AI Workload Executes
       ↓
Continuous Monitoring
       ↓
Risk Detection
       ↓
Alert / Throttle / Suspend
       ↓
Human Investigation
```

---

## 145. AI Autonomous Workflow

```text
AI Agent
   ↓
Request Capability
   ↓
Identity Resolution
   ↓
Policy Evaluation
   ↓
Risk Analysis
   ↓
Approved?
 ┌─┴─────────────┐
 │               │
YES              NO
 │               │
 ▼               ▼
Issue Token     Human Review
 │               │
 ▼               ▼
Execute         Approve/Deny
 │
 ▼
Audit
```

---

## 146. Service Account Inventory

The platform SHALL provide centralized inventory.

Example:

```text
Service Account
Application
Environment
Owner
Purpose
Credential
Permissions
Status
Last Used
Expires
Risk
```

---

## 147. Search

Administrators SHALL be able to search by:

```text
Service Account ID
Name
Application
Owner
Tenant
Environment
Status
Scope
Purpose
Agent ID
```

---

## 148. Bulk Operations

Authorized administrators SHOULD be able to:

```text
Suspend Accounts
Revoke Credentials
Rotate Credentials
Change Policies
Export Inventory
```

Bulk operations SHALL require appropriate permissions.

---

## 149. Bulk Operation Safety

Production bulk operations SHALL support:

* Confirmation
* Preview
* Impact analysis
* Approval
* Audit
* Idempotency

---

## 150. Credential Compromise Workflow

```text
Compromise Detected
       ↓
Risk Assessment
       ↓
Credential Revocation
       ↓
Service Account Suspension
       ↓
Usage Investigation
       ↓
Affected Resources Identified
       ↓
Incident Created
       ↓
Replacement Credential
       ↓
Application Migration
       ↓
Validation
       ↓
Account Reactivation
```

---

## 151. Incident Response Integration

The service account platform SHOULD integrate with the Security/Incident platform.

---

## 152. Billing Integration

Service-account API usage MAY contribute to:

```text
API Usage
AI Usage
Workflow Usage
Data Processing
Subscription Limits
Enterprise Billing
```

---

## 153. Data Minimization

Usage and audit systems SHALL collect only information necessary for:

* Security
* Compliance
* Debugging
* Billing
* Analytics

Sensitive payload data SHALL not be retained unnecessarily.

---

## 154. Privacy

Service account metadata SHALL respect organization-level data-retention and privacy policies.

---

## 155. Developer Portal Documentation

Documentation SHALL explain:

* Service account concepts
* Service account creation
* Credential management
* Scope selection
* Rotation
* Expiration
* Workload identity
* OAuth
* API keys
* AI-agent identities
* Security best practices
* Incident response

---

## 156. Secure Deployment Example

```bash
export SALESGENIE_CLIENT_ID="..."
export SALESGENIE_CLIENT_SECRET="..."
```

Applications SHOULD retrieve credentials from a secure secret manager instead of source code.

---

## 157. Insecure Pattern

The platform documentation SHALL discourage:

```python
CLIENT_SECRET = "production-secret"
```

and:

```python
API_KEY = "sg_live_..."
```

---

## 158. Secret Manager Pattern

```text
Workload
   ↓
Secret Manager / Workload Identity
   ↓
Short-Lived Credential
   ↓
SalesGenie API
```

---

## 159. Kubernetes Integration

The platform SHOULD support Kubernetes workload identity patterns.

Example:

```text
Kubernetes Service
       ↓
Service Account
       ↓
OIDC / Workload Identity
       ↓
SalesGenie Token
```

---

## 160. CI/CD Integration

CI/CD systems SHOULD use:

```text
OIDC
Secret Manager
Short-Lived Credentials
```

instead of long-lived static secrets where possible.

---

## 161. Cloud Integration

The platform SHOULD support enterprise workload identity integrations for:

```text
AWS
Google Cloud
Microsoft Azure
Kubernetes
```

---

## 162. Service Account Deletion Safety

Before deleting a service account, the system SHOULD display:

```text
Applications using account
Active credentials
Recent usage
Granted permissions
Dependent workflows
AI agents
Webhooks
Scheduled jobs
```

---

## 163. Dependency Detection

The platform SHOULD identify resources dependent on a service account.

---

## 164. Deletion Confirmation

Production service-account deletion SHOULD require:

```text
Explicit Confirmation
+
Step-Up Authentication
+
Appropriate Permission
```

---

## 165. Orphaned Service Accounts

The platform SHALL detect service accounts whose owning application or owner no longer exists.

---

## 166. Orphan Remediation

Organizations SHALL be able to:

```text
Assign Owner
Transfer Application
Suspend
Revoke
Delete
```

---

## 167. Ownership Expiration

Organizations MAY require periodic ownership recertification.

Example:

```text
Every 90 days
```

---

## 168. Access Recertification

Security administrators SHALL be able to review:

```text
Account
Owner
Permissions
Usage
Risk
Application
Environment
```

and approve or revoke access.

---

## 169. Quarterly Access Review

Enterprise organizations SHOULD support periodic service-account access reviews.

---

## 170. Compliance Evidence

The system SHOULD generate reports containing:

```text
Service Account Inventory
Permission Inventory
Credential Rotation Status
Expiration Status
Owner Information
Access Review Results
Audit History
Risk Findings
```

---

## 171. API Security

Service account management endpoints SHALL implement:

* Authentication
* Authorization
* Rate limiting
* Input validation
* CSRF protection where applicable
* Idempotency
* Audit logging
* Abuse detection

---

## 172. Input Validation

The platform SHALL validate:

```text
Service Account Name
Application ID
Tenant ID
Environment
Scopes
Expiration
Owner
Credential Type
Metadata
```

---

## 173. Enumeration Protection

Unauthorized users SHALL not be able to discover whether a service account exists.

---

## 174. Error Handling

Errors SHALL avoid leaking:

```text
Credential secrets
Internal database details
Policy implementation details
Sensitive identity information
```

---

## 175. Standard Error

Example:

```json
{
  "error": {
    "code": "service_account_access_denied",
    "message": "The requested operation is not authorized.",
    "request_id": "req_123"
  }
}
```

---

## 176. Service Account Quotas

Organizations MAY configure:

```text
Maximum Service Accounts
Maximum Production Accounts
Maximum Credentials
Maximum AI Accounts
Maximum Privileged Accounts
```

---

## 177. Rate Limits for Management APIs

Credential-management operations SHALL be rate-limited to prevent abuse.

---

## 178. Administrative Security

High-risk operations SHALL support:

```text
MFA
Step-Up Authentication
Approval
Dual Control
```

where required by organization policy.

---

## 179. Dual Control

Organizations MAY require two authorized administrators for:

```text
Global service-account revocation
Production privileged account creation
Organization-wide credential rotation
```

---

## 180. Separation of Duties

The platform SHOULD support separation between:

```text
Account Creator
Approver
Owner
Security Reviewer
Auditor
```

---

## 181. Security Boundary

Service account identities SHALL be treated as security principals.

They SHALL NOT inherit permissions from human owners automatically.

---

## 182. Human Ownership ≠ Authorization

An owner SHALL manage a service account only through explicitly granted administrative permissions.

Ownership alone SHALL NOT grant the service account access.

---

## 183. AI Ownership

AI agents SHALL not become unrestricted owners of privileged service accounts.

AI ownership SHALL be mediated through platform policies.

---

## 184. Service Account Federation

Enterprise organizations MAY federate service identities with external identity providers.

---

## 185. External Identity Mapping

Example:

```text
External Workload Identity
        ↓
Federation
        ↓
SalesGenie Service Account
        ↓
SalesGenie Permissions
```

---

## 186. Token Exchange

The platform SHOULD support secure token exchange for trusted workload identities.

---

## 187. Short-Lived Credential Architecture

Preferred architecture:

```text
Workload Identity
      ↓
Authenticate
      ↓
Token Exchange
      ↓
Short-Lived Token
      ↓
API Gateway
      ↓
Authorization
```

---

## 188. Long-Lived Credential Exception

Long-lived API keys or client secrets MAY be supported for compatibility but SHOULD be discouraged for production workloads when stronger alternatives exist.

---

## 189. Security Posture

The service identity architecture SHALL prioritize:

```text
Short-Lived Credentials
Least Privilege
Workload Identity
Strong Authentication
Continuous Authorization
Rapid Revocation
Complete Auditability
```

---

## 190. Definition of Done

The Service Account subsystem SHALL be considered production-ready when:

* Service account creation is implemented.
* Unique machine identities are implemented.
* Ownership is implemented.
* Application association is implemented.
* Tenant isolation is enforced.
* Environment isolation is enforced.
* Roles and scopes are implemented.
* Credential management is implemented.
* Credential rotation is implemented.
* Credential expiration is implemented.
* Service account expiration is implemented.
* Suspension is implemented.
* Revocation is implemented.
* Emergency disablement is implemented.
* Production approval is implemented.
* AI service identities are implemented.
* AI permissions are isolated.
* Human approval for high-risk AI operations is implemented.
* Workload identity support is available where applicable.
* API key integration is implemented.
* OAuth client-credentials integration is implemented where applicable.
* Secret storage is secure.
* Secret leakage prevention is implemented.
* Secret scanning is implemented.
* Rate limiting is implemented.
* Usage monitoring is implemented.
* Risk scoring is implemented.
* Compromise detection is implemented.
* Security alerts are implemented.
* Audit logging is immutable.
* Access recertification is supported.
* Dormant account detection is implemented.
* Overprivileged account detection is implemented.
* Ownership transfer is audited.
* Bulk operations are protected.
* Management APIs are versioned.
* APIs are idempotent.
* High-risk operations support MFA.
* Production operations support appropriate approvals.
* Observability is implemented.
* Distributed tracing is implemented.
* Load testing passes.
* Security testing passes.
* Penetration testing passes.
* Chaos testing passes.
* Disaster recovery is tested.
* Compliance evidence can be generated.
* Developer documentation is complete.

---

## 191. Acceptance Criteria

## AC-001

Authorized users can create service accounts.

## AC-002

Every service account receives a unique immutable identity.

## AC-003

Service accounts cannot authenticate after revocation.

## AC-004

Service accounts cannot access unauthorized tenants.

## AC-005

Service accounts cannot access unauthorized environments.

## AC-006

Service accounts support fine-grained scopes.

## AC-007

Service accounts support credential rotation.

## AC-008

Credential secrets cannot be retrieved after creation.

## AC-009

Credentials support expiration.

## AC-010

Expired credentials cannot authenticate.

## AC-011

Service accounts support suspension.

## AC-012

Service accounts support emergency revocation.

## AC-013

Production service accounts can require approval.

## AC-014

Privileged permissions can require approval.

## AC-015

AI agents can use dedicated service identities.

## AC-016

AI agents cannot grant themselves additional privileges.

## AC-017

AI high-risk operations can require human approval.

## AC-018

AI service-account actions are independently auditable.

## AC-019

Service-account credentials never appear in logs.

## AC-020

Service-account usage can be monitored.

## AC-021

Dormant service accounts can be detected.

## AC-022

Overprivileged service accounts can be detected.

## AC-023

Compromised credentials can be revoked rapidly.

## AC-024

Credential rotation can occur with a controlled grace period.

## AC-025

Service account ownership can be transferred.

## AC-026

Ownership changes are audited.

## AC-027

Service-account lifecycle events are auditable.

## AC-028

Management APIs enforce RBAC/ABAC.

## AC-029

High-risk operations support step-up authentication.

## AC-030

Service account operations support idempotency.

## AC-031

Concurrent lifecycle operations are safely handled.

## AC-032

Service account policies are centrally enforceable.

## AC-033

Security decisions fail closed.

## AC-034

Service account APIs integrate with the API Gateway.

## AC-035

Service account identities propagate securely to downstream services.

## AC-036

Workload identity can be used instead of long-lived secrets where supported.

## AC-037

Service account inventory is searchable.

## AC-038

Enterprise access reviews are supported.

## AC-039

Compliance evidence can be generated.

## AC-040

Service account infrastructure scales to millions of machine identities.

---

## 192. Strategic Architecture Outcome

The SalesGenie Service Account Platform SHALL provide a dedicated identity layer for all non-human workloads.

The target architecture SHALL be:

```text
                         HUMAN
                           │
                           ▼
                    Developer Portal
                           │
                           ▼
                  Identity Management
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
      Service Accounts              AI Agents
             │                           │
             ▼                           ▼
        Credentials              AI Service Identity
             │                           │
             └─────────────┬─────────────┘
                           ▼
                     Policy Engine
                           │
                     Approval Engine
                           │
                    Credential Service
                           │
                      KMS / Vault
                           │
                           ▼
                      API Gateway
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
          Auth Service   AI Gateway   Services
              │            │            │
              └────────────┼────────────┘
                           ▼
                     Authorization
                           │
                           ▼
                    SalesGenie APIs
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
     Audit             Analytics          Event Bus
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ▼
                  Security Monitoring
```

The final system SHALL establish **secure, least-privilege, tenant-isolated, auditable machine identities for SalesGenie's microservices, integrations, automation workloads, enterprise applications, and autonomous AI agents**, while minimizing dependence on long-lived static credentials and preventing AI or machine workloads from acquiring unauthorized privileges.
