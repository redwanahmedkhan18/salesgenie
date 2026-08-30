# Developer API Keys — User, System & Functional Requirements

**Project:** SalesGenie / FlowMind AI  
**Requirement Type:** Developer API Key Management  
**File:** `developer_api_keys.md`  
**Architecture:** Enterprise SaaS + Multi-Tenant + Microservices + API-First + Event-Driven + Multi-Agent AI  
**Scope:** Human Developers + Enterprise Applications + AI Agents + Service Accounts  
**Target Scale:** 10M+ users, 500K+ concurrent conversations  
**Priority:** P0 — Core Developer Platform Security Capability

---

## 1. Purpose

The Developer API Keys subsystem provides secure lifecycle management for API credentials used by developers, applications, integrations, automation services, enterprise systems, and AI agents accessing SalesGenie APIs.

The system SHALL provide:

- API key generation
- API key rotation
- API key revocation
- API key expiration
- Scope management
- Environment isolation
- Tenant isolation
- Application association
- Key usage monitoring
- Rate limiting
- IP restrictions
- Audit logging
- Security alerts
- Secret protection
- AI-agent credential governance
- Human approval workflows
- Emergency key revocation
- Automated lifecycle management

API keys SHALL function as credentials, not as authorization policies themselves. All requests SHALL undergo server-side authentication and authorization.

---

## 2. Product Goals

The Developer API Key platform SHALL:

1. Provide secure machine-to-machine authentication.
2. Minimize credential leakage risk.
3. Enforce least-privilege access.
4. Support multi-tenant applications.
5. Support human and AI actors.
6. Provide complete credential lifecycle management.
7. Support production and sandbox environments.
8. Provide fine-grained scopes.
9. Provide configurable expiration.
10. Provide key rotation without downtime.
11. Provide real-time revocation.
12. Provide comprehensive auditability.
13. Detect anomalous API-key usage.
14. Integrate with API Gateway and API Management.
15. Integrate with Developer Portal.
16. Support enterprise security controls.
17. Support automated AI-agent credentials.
18. Provide developer-friendly APIs and UI.

---

## 3. Actors

## 3.1 Human Actors

### H-001 — External Developer

Creates and manages API keys for applications.

### H-002 — Enterprise Developer

Manages credentials for enterprise applications.

### H-003 — Application Owner

Owns an application and its associated credentials.

### H-004 — Organization Administrator

Manages organization-level API keys.

### H-005 — Security Administrator

Controls credential security policies and emergency revocation.

### H-006 — Platform Administrator

Manages platform-level credential policies.

### H-007 — Integration Engineer

Uses API keys to integrate SalesGenie with external systems.

### H-008 — DevOps Engineer

Deploys API keys through secure infrastructure.

### H-009 — Compliance Officer

Audits API credential usage and lifecycle.

---

## 4. AI Actors

### AI-001 — Autonomous Sales Agent

Uses an authorized credential to interact with SalesGenie.

### AI-002 — Customer Support Agent

Uses API credentials to access support functionality.

### AI-003 — Workflow Agent

Executes authorized workflows.

### AI-004 — Analytics Agent

Accesses analytics APIs.

### AI-005 — Developer Agent

Creates or configures integrations under explicit authorization.

### AI-006 — Agent Orchestrator

Manages credentials or delegated capabilities for multiple AI agents.

### AI-007 — Service Agent

Performs machine-to-machine background operations.

---

## 5. Core Security Principles

The API Key system SHALL follow:

```text
Least Privilege
Zero Trust
Defense in Depth
Explicit Authorization
Tenant Isolation
Credential Minimization
Secure Defaults
Short-Lived Credentials Where Possible
Continuous Monitoring
Immediate Revocation
Complete Auditability
```

---

## 6. User Requirements

## UR-001 — Create API Key

Authorized developers SHALL be able to create an API key for an application.

The creation workflow SHALL require:

* Application
* Environment
* Key name
* Permissions/scopes
* Optional expiration
* Optional IP restrictions
* Optional metadata

---

## UR-002 — Key Display

The complete API secret SHALL be displayed only once immediately after creation.

After initial display:

```text
Full secret → NEVER retrievable
```

The platform SHALL store only a secure representation sufficient for verification and lifecycle management.

---

## UR-003 — Key Identification

Every API key SHALL have a non-secret identifier.

Example:

```text
Key ID: key_01JXYZ...
Prefix: sg_live_7f3a...
```

The identifier SHALL be safe to display in dashboards and audit logs.

---

## UR-004 — Key Naming

Developers SHALL be able to assign human-readable names.

Examples:

```text
Production Backend
Marketing Automation
AI Sales Agent
Local Development
CRM Integration
Analytics Pipeline
```

---

## UR-005 — Environment Selection

Keys SHALL be associated with an environment:

```text
development
sandbox
staging
production
```

A key created for one environment SHALL NOT automatically work in another environment.

---

## UR-006 — Scope Selection

Developers SHALL be able to select API scopes.

Example:

```text
leads.read
leads.write
customers.read
customers.write
conversations.read
conversations.write
agents.execute
workflows.execute
analytics.read
webhooks.manage
billing.read
```

---

## UR-007 — Least Privilege

The UI SHALL recommend the minimum required scopes.

Developers SHALL NOT receive unrestricted permissions by default.

---

## UR-008 — Key Expiration

Developers SHALL be able to configure expiration.

Supported policies MAY include:

```text
7 days
30 days
90 days
180 days
1 year
Custom
Never
```

"Never" SHALL be disabled for organizations that prohibit non-expiring credentials.

---

## UR-009 — Key Rotation

Developers SHALL be able to rotate keys without service downtime.

The platform SHALL support:

```text
Old Key → Active
New Key → Active
Old Key → Grace Period
Old Key → Revoked
```

---

## UR-010 — Key Revocation

Authorized users SHALL be able to immediately revoke credentials.

Revocation SHALL invalidate subsequent API requests.

---

## 7. Application Association

## UR-020 — Application Binding

Every API key SHALL belong to a developer application.

```text
Organization
    ↓
Application
    ↓
Environment
    ↓
API Key
```

---

## UR-021 — Application Ownership

Only authorized users SHALL manage application credentials.

---

## UR-022 — Application Deletion

Deleting an application SHALL trigger credential handling according to organizational policy.

Production keys SHOULD be revoked before permanent application deletion.

---

## 8. Organization Requirements

## UR-030 — Organization Keys

Organizations SHALL be able to manage organization-owned API keys.

---

## UR-031 — Organization Policies

Administrators SHALL be able to enforce:

* Maximum key lifetime
* Required rotation
* Required scopes
* IP restrictions
* Production approval
* Key count limits
* Naming conventions
* Environment restrictions

---

## UR-032 — Centralized Visibility

Authorized administrators SHALL be able to view all keys within their permitted organizational scope.

The dashboard SHALL never display complete secrets.

---

## 9. Human Workflow

```text
Developer
   ↓
Developer Portal
   ↓
Select Application
   ↓
Select Environment
   ↓
Define Key Name
   ↓
Select Scopes
   ↓
Configure Expiration
   ↓
Configure Restrictions
   ↓
Security Validation
   ↓
Approval Required?
   ├── YES → Admin Approval
   └── NO
        ↓
Generate Key
        ↓
Display Secret Once
        ↓
Developer Stores Secret
        ↓
API Gateway Authentication
```

---

## 10. AI Credential Workflow

```text
AI Agent
   ↓
Agent Identity
   ↓
Requested Capability
   ↓
Policy Evaluation
   ↓
Scope Validation
   ↓
Human Approval?
   ├── YES → Human Review
   └── NO
        ↓
Credential / Delegated Token
        ↓
API Gateway
        ↓
Authorization
        ↓
Execution
        ↓
Audit Event
```

---

## 11. AI Requirements

## UR-AI-001 — AI Credential Identity

AI agents SHALL have distinguishable identities.

The system SHALL be able to associate API activity with:

```text
agent_id
agent_type
agent_version
application_id
organization_id
tenant_id
```

---

## UR-AI-002 — AI Scope Restrictions

AI credentials SHALL be limited to explicitly authorized scopes.

---

## UR-AI-003 — AI High-Risk Operations

AI agents SHALL require additional authorization for sensitive operations.

Examples:

```text
Delete customer
Export customer data
Send bulk campaign
Modify billing
Change organization settings
Delete knowledge base
Rotate production credentials
```

---

## UR-AI-004 — Human Approval

Organizations SHALL be able to require human approval before AI credentials are issued or used for high-risk operations.

---

## UR-AI-005 — AI Credential Expiration

AI credentials SHOULD have shorter lifetimes than conventional integration keys where operationally feasible.

---

## UR-AI-006 — Delegated Authorization

The platform SHOULD support delegated capabilities rather than providing AI agents with unrestricted master API keys.

---

## 12. System Requirements

## SR-001 — Credential Architecture

The API Key system SHALL consist of:

```text
Developer Portal
      ↓
API Key Management Service
      ↓
Credential Store
      ↓
Policy Engine
      ↓
API Gateway
      ↓
Authorization Service
      ↓
SalesGenie Services
```

---

## 13. Credential Storage

## SR-010 — Secret Hashing

API key secrets SHALL NOT be stored in plaintext.

The system SHOULD use a cryptographically secure one-way hashing mechanism for verification.

---

## SR-011 — Encryption

Sensitive credential metadata SHALL be encrypted at rest.

---

## SR-012 — Key Encryption Keys

Encryption keys SHALL be managed through an appropriate KMS/HSM architecture.

---

## SR-013 — Secret Isolation

API key secrets SHALL be isolated from ordinary application database records.

---

## SR-014 — Secret Access

No standard database query SHALL return the complete API key secret.

---

## 14. API Key Format

Keys SHOULD use recognizable prefixes.

Example:

```text
sg_test_xxxxxxxxxxxxxxxxx
sg_live_xxxxxxxxxxxxxxxxx
```

The secret portion SHALL contain sufficient entropy to resist brute-force attacks.

---

## 15. Functional Requirements

## FR-001 — Generate Key

The system SHALL generate cryptographically secure API key secrets using a CSPRNG.

---

## FR-002 — Key Entropy

API keys SHALL contain sufficient entropy to make brute-force discovery computationally infeasible.

---

## FR-003 — Key ID

The system SHALL generate a unique immutable key ID.

Example:

```text
key_01JABC123XYZ
```

---

## FR-004 — Key Prefix

The system SHOULD expose a non-secret prefix for identification.

---

## FR-005 — Secret Hash

The system SHALL store a secure verification representation rather than plaintext secrets.

---

## 16. API Key Metadata

Each API key SHALL maintain metadata including:

```text
key_id
key_prefix
name
organization_id
tenant_id
application_id
environment
scopes
status
created_at
created_by
last_used_at
last_used_ip
expires_at
revoked_at
revoked_by
rotation_parent_id
rotation_child_id
description
metadata
```

---

## 17. Key States

API keys SHALL support lifecycle states:

```text
CREATING
ACTIVE
EXPIRING_SOON
EXPIRED
ROTATION_PENDING
GRACE_PERIOD
REVOKED
COMPROMISED
SUSPENDED
```

---

## 18. State Transition Model

```text
CREATING
   ↓
ACTIVE
   ├───────────────┐
   ↓               ↓
EXPIRING_SOON    COMPROMISED
   ↓               ↓
EXPIRED          REVOKED
   ↑
   │
ACTIVE → ROTATION_PENDING
             ↓
         GRACE_PERIOD
             ↓
           REVOKED
```

---

## 19. Key Creation API

Conceptual API:

```http
POST /api/v1/developer/api-keys
```

Request:

```json
{
  "name": "Production Backend",
  "application_id": "app_123",
  "environment": "production",
  "scopes": [
    "leads.read",
    "leads.write"
  ],
  "expires_at": "2027-08-29T00:00:00Z"
}
```

Response SHALL contain:

```json
{
  "id": "key_123",
  "prefix": "sg_live_abc",
  "secret": "sg_live_abc...",
  "created_at": "2026-08-29T00:00:00Z"
}
```

The secret SHALL be returned only during creation/rotation.

---

## 20. List API Keys

## FR-020

The platform SHALL provide:

```http
GET /api/v1/developer/api-keys
```

The response SHALL exclude:

```text
secret
hashed_secret
encryption_key
```

---

## 21. Get API Key

## FR-021

The platform SHALL provide metadata retrieval.

```http
GET /api/v1/developer/api-keys/{key_id}
```

---

## 22. Update API Key

## FR-022

Authorized users SHALL be able to update mutable metadata.

Mutable fields MAY include:

```text
name
description
scopes
expiration
IP restrictions
metadata
```

Changing sensitive permissions SHOULD require reauthorization.

---

## 23. Revoke API Key

## FR-023

The platform SHALL provide:

```http
POST /api/v1/developer/api-keys/{key_id}/revoke
```

Revocation SHALL be idempotent.

---

## 24. Rotate API Key

## FR-024

The platform SHALL provide:

```http
POST /api/v1/developer/api-keys/{key_id}/rotate
```

The response SHALL provide a new secret.

---

## 25. Key Rotation Strategy

Rotation SHALL support zero-downtime migration.

```text
T0:
Old Key = ACTIVE

T1:
New Key = ACTIVE
Old Key = ACTIVE

T2:
Applications migrate

T3:
Old Key = GRACE_PERIOD

T4:
Old Key = REVOKED
```

---

## 26. Grace Period

Organizations SHALL be able to configure rotation grace periods.

Example:

```text
15 minutes
1 hour
6 hours
24 hours
7 days
Custom
```

---

## 27. Automatic Rotation

The system SHOULD support automatic key rotation for eligible credentials.

Automatic rotation SHALL:

1. Generate a replacement.
2. Preserve scopes.
3. Preserve environment.
4. Notify authorized owners.
5. Provide migration metadata.
6. Maintain a controlled overlap period.
7. Revoke the old key.

---

## 28. Expiration

## FR-030

The authentication layer SHALL reject expired keys.

---

## FR-031

The system SHALL notify key owners before expiration.

Notification windows SHOULD include:

```text
30 days
14 days
7 days
3 days
24 hours
```

---

## 29. Expiration Policies

Organizations SHALL be able to define maximum lifetimes.

Example:

```text
Development: 30 days
Sandbox: 90 days
Staging: 180 days
Production: 365 days
```

---

## 30. Scope System

Scopes SHALL follow a resource/action model.

Example:

```text
customers.read
customers.write
leads.read
leads.write
conversations.read
conversations.write
agents.read
agents.execute
workflows.read
workflows.execute
analytics.read
billing.read
webhooks.read
webhooks.write
```

---

## 31. Scope Validation

Every API request SHALL evaluate:

```text
API Key
    ↓
Scopes
    ↓
Requested Operation
    ↓
Authorization Policy
    ↓
Allow / Deny
```

---

## 32. Scope Escalation Prevention

A key SHALL NOT be able to request or grant scopes beyond its authorization.

---

## 33. Production Key Approval

Organizations SHALL be able to require approval for production credentials.

Workflow:

```text
Developer Request
       ↓
Security Validation
       ↓
Admin Approval
       ↓
Key Generation
```

---

## 34. Development Key Policy

Development keys MAY be automatically approved but SHALL remain restricted to non-production resources.

---

## 35. IP Restrictions

The system SHOULD support IP allowlists.

Example:

```json
{
  "ip_allowlist": [
    "203.0.113.10/32",
    "203.0.113.0/24"
  ]
}
```

---

## 36. Network Restrictions

Enterprise customers MAY configure:

* IP allowlists
* CIDR ranges
* Private network policies
* Region restrictions
* VPN requirements
* Private endpoints

---

## 37. User-Agent and Client Identification

SDK requests SHOULD identify:

```text
SDK name
SDK version
Programming language
Runtime version
Application ID
```

This metadata SHALL NOT replace authentication.

---

## 38. Authentication Flow

```text
Client
  ↓
API Request
  ↓
API Gateway
  ↓
Extract API Key
  ↓
Locate Key Metadata
  ↓
Verify Secret
  ↓
Check Status
  ↓
Check Expiration
  ↓
Check Environment
  ↓
Check Tenant
  ↓
Check IP Restrictions
  ↓
Check Rate Limit
  ↓
Check Scopes
  ↓
Policy Engine
  ↓
ALLOW / DENY
```

---

## 39. Constant-Time Verification

Credential verification SHALL use timing-safe comparison techniques where applicable.

---

## 40. Brute-Force Protection

The authentication system SHALL detect excessive invalid-key attempts.

Controls MAY include:

* Rate limiting
* Temporary source blocking
* IP reputation
* Account/application risk scoring
* Security alerts

---

## 41. Key Enumeration Protection

API responses SHALL NOT reveal whether an arbitrary credential identifier exists to unauthorized callers.

---

## 42. Authentication Error Responses

Authentication failures SHOULD return standardized responses.

Example:

```json
{
  "error": {
    "code": "invalid_api_key",
    "message": "The API credential is invalid or unavailable.",
    "request_id": "req_123"
  }
}
```

Error responses SHALL avoid revealing sensitive credential details.

---

## 43. Rate Limiting

API keys SHALL be subject to:

```text
Organization limits
Application limits
Key limits
Endpoint limits
AI-agent limits
Subscription limits
```

---

## 44. Dynamic Rate Limiting

The platform SHOULD dynamically reduce limits when anomalous activity is detected.

---

## 45. Usage Tracking

The platform SHALL track:

```text
request_count
successful_requests
failed_requests
rate_limit_events
last_used_at
last_used_ip
endpoint_usage
scope_usage
latency
error_rate
```

---

## 46. Key Usage Dashboard

Developers SHALL be able to view:

* Requests
* Errors
* Last used time
* Usage trends
* API endpoints
* Scopes used
* Rate-limit events
* Geographic information where legally appropriate

---

## 47. Unused Key Detection

The platform SHALL identify inactive credentials.

Example:

```text
No usage for 30 days
No usage for 60 days
No usage for 90 days
```

---

## 48. Stale Key Policy

Organizations SHALL be able to automatically suspend or revoke unused credentials.

---

## 49. Compromised Key Detection

The system SHALL detect suspicious usage patterns.

Potential signals:

```text
Impossible geographic movement
Unexpected IP
Sudden request spike
New ASN
Unexpected endpoint access
Scope abuse
Credential sharing
Repeated authentication failures
```

---

## 50. Risk Scoring

Each API key MAY receive a dynamic risk score.

Conceptual model:

```text
Risk Score =
IP Risk
+
Behavioral Anomaly
+
Velocity Anomaly
+
Geographic Anomaly
+
Scope Anomaly
+
Credential Age
```

---

## 51. Automated Security Response

For high-risk credentials, the system MAY:

```text
Alert
 ↓
Throttle
 ↓
Require Reauthentication
 ↓
Suspend
 ↓
Revoke
```

---

## 52. Security Alerts

The platform SHALL generate alerts for:

* New production key
* Key rotation
* Key revocation
* Expiration
* Suspicious activity
* Excessive failures
* Scope escalation attempts
* Unusual geographic activity
* Credential compromise indicators

---

## 53. Notification Channels

Security notifications MAY be delivered through:

```text
In-app
Email
Push
Slack
Webhook
SIEM
```

---

## 54. Audit Logging

Every credential lifecycle operation SHALL generate an audit event.

Events SHALL include:

```text
api_key.created
api_key.updated
api_key.rotated
api_key.revoked
api_key.expired
api_key.suspended
api_key.compromised
api_key.scope_changed
api_key.policy_changed
```

---

## 55. Audit Record

Audit events SHALL include:

```text
event_id
timestamp
organization_id
tenant_id
application_id
key_id
actor_type
actor_id
operation
old_state
new_state
scopes
ip_address
user_agent
request_id
trace_id
reason
approval_id
```

---

## 56. AI Audit Record

AI-originated credential operations SHALL additionally capture:

```text
agent_id
agent_version
model_provider
model_name
tool_name
execution_id
human_approver_id
policy_decision
```

---

## 57. Human Approval Audit

If a human approves an AI credential or high-risk key operation, the system SHALL record:

```text
approval_id
approver_id
approval_time
requested_action
requested_scopes
decision
expiration
```

---

## 58. Emergency Revocation

Security administrators SHALL have an emergency revoke mechanism.

The mechanism SHOULD support:

```text
Single Key
Application
Organization
Environment
Credential Family
AI Agent
```

---

## 59. Bulk Revocation

Authorized administrators SHALL be able to revoke multiple keys based on filters.

Examples:

```text
All production keys
All keys for application X
All keys created by user Y
All keys with scope billing.write
All keys belonging to compromised application
```

---

## 60. Kill Switch

The platform SHOULD provide an emergency credential kill switch.

```text
SECURITY INCIDENT
       ↓
GLOBAL / TENANT KILL SWITCH
       ↓
KEYS INVALIDATED
       ↓
SERVICES PROTECTED
```

This capability SHALL require privileged authorization and produce a high-severity audit event.

---

## 61. Tenant Isolation

API keys SHALL be cryptographically and logically associated with tenants.

A key from:

```text
Tenant A
```

SHALL NEVER authenticate access to:

```text
Tenant B
```

unless explicitly authorized through an approved cross-tenant service architecture.

---

## 62. Organization Isolation

Organization administrators SHALL only manage credentials within their authorized organizations.

---

## 63. Service Account Integration

The API Key platform SHALL support service accounts.

Service accounts SHALL have:

* Identity
* Owner
* Organization
* Application
* Scopes
* Lifecycle
* Audit trail

---

## 64. AI Service Account Integration

AI agents SHOULD use dedicated service identities instead of human developer credentials.

---

## 65. Credential Delegation

The platform SHOULD support temporary delegated credentials.

Example:

```text
Human
 ↓
Authorize Agent
 ↓
Temporary Credential
 ↓
Limited Scope
 ↓
Expiration
 ↓
Automatic Revocation
```

---

## 66. Secret Exposure Prevention

The system SHALL prevent API secrets from appearing in:

* Audit logs
* Application logs
* API responses
* Error messages
* Analytics
* Monitoring dashboards
* Browser telemetry
* URLs
* Query parameters

---

## 67. Browser Security

Production secret API keys SHALL NOT be intended for direct browser exposure.

Developer Portal SHALL display warnings such as:

```text
Do not embed production API keys in frontend JavaScript.
```

---

## 68. Public Client Applications

For browser/mobile clients, SalesGenie SHOULD recommend:

```text
Backend Proxy
OAuth
Short-lived Tokens
Public Client Credentials
Restricted Client Tokens
```

instead of long-lived privileged API keys.

---

## 69. Secret Scanning

The Developer Platform SHOULD detect leaked SalesGenie API keys in:

* Public repositories
* Logs
* Uploaded files
* Configuration repositories
* CI/CD output

---

## 70. Leak Response

When a leaked credential is detected, the platform SHOULD:

```text
Detect
 ↓
Verify
 ↓
Alert
 ↓
Risk Score
 ↓
Optional Automatic Revocation
 ↓
Notify Owner
 ↓
Generate Replacement
```

---

## 71. GitHub/GitLab Integration

Where supported, enterprise users MAY connect source-control systems for secret scanning.

---

## 72. CI/CD Integration

Developers SHOULD be able to inject credentials through secure secret managers.

Recommended integrations:

```text
AWS Secrets Manager
Google Secret Manager
Azure Key Vault
HashiCorp Vault
Kubernetes Secrets
GitHub Actions Secrets
GitLab CI/CD Variables
```

---

## 73. Secret Rotation Automation

The platform SHOULD provide APIs for automation systems to rotate credentials.

---

## 74. API Key Management API

The management API SHALL support:

```text
POST   /api/v1/developer/api-keys
GET    /api/v1/developer/api-keys
GET    /api/v1/developer/api-keys/{id}
PATCH  /api/v1/developer/api-keys/{id}
POST   /api/v1/developer/api-keys/{id}/rotate
POST   /api/v1/developer/api-keys/{id}/revoke
POST   /api/v1/developer/api-keys/{id}/suspend
GET    /api/v1/developer/api-keys/{id}/usage
GET    /api/v1/developer/api-keys/{id}/audit
```

---

## 75. Management API Authorization

The API Key Management API SHALL require stronger permissions than ordinary API consumption.

Example scopes:

```text
api_keys.read
api_keys.create
api_keys.update
api_keys.rotate
api_keys.revoke
api_keys.delete
```

---

## 76. Sensitive Operation Protection

Operations such as:

```text
create production key
rotate production key
revoke production key
change privileged scopes
```

SHOULD support step-up authentication.

---

## 77. Step-Up Authentication

Possible mechanisms:

```text
Password Reauthentication
MFA
WebAuthn
SSO Reauthentication
Hardware Security Key
```

---

## 78. Multi-Factor Authentication

MFA SHOULD be mandatory for high-risk credential operations.

---

## 79. Role-Based Access Control

Example roles:

```text
Developer
Senior Developer
Application Owner
Organization Admin
Security Admin
Compliance Admin
Platform Admin
```

Permissions SHALL follow least privilege.

---

## 80. Attribute-Based Access Control

The platform SHOULD evaluate:

```text
User
Role
Organization
Application
Environment
IP
Device
Risk
Time
Operation
Resource
```

---

## 81. Production Access Policy

Production API keys MAY require:

```text
Organization Admin
+
Security Policy
+
MFA
+
Approved Scopes
```

---

## 82. Key Limits

Organizations MAY configure:

```text
Maximum keys per user
Maximum keys per application
Maximum production keys
Maximum active keys
Maximum AI credentials
```

---

## 83. Duplicate Detection

The system SHOULD warn when developers create potentially redundant keys.

Example:

```text
Three active production keys
same application
same scopes
same environment
```

---

## 84. Key Naming Policy

Organizations MAY enforce naming conventions.

Example:

```text
<environment>-<application>-<purpose>
```

---

## 85. Metadata

Keys SHALL support custom metadata.

Example:

```json
{
  "team": "sales",
  "service": "lead-service",
  "owner": "platform-team"
}
```

Metadata SHALL NOT be used to bypass authorization.

---

## 86. API Key Search

Authorized users SHALL be able to search keys by:

* Name
* ID
* Prefix
* Application
* Environment
* Status
* Owner
* Scope
* Creation date

---

## 87. API Key Filtering

The dashboard SHALL support filtering by:

```text
ACTIVE
EXPIRED
REVOKED
COMPROMISED
EXPIRING_SOON
```

---

## 88. Key Inventory

The Developer Portal SHALL provide a centralized credential inventory.

Example:

```text
Application
Environment
Key
Owner
Scopes
Status
Created
Last Used
Expires
Risk
```

---

## 89. Credential Health Score

The system MAY calculate:

```text
Credential Health =
Expiration Risk
+
Rotation Risk
+
Scope Risk
+
Usage Risk
+
Network Risk
+
Security Risk
```

---

## 90. AI-Based Credential Intelligence

The platform SHOULD use AI/ML to identify:

* Unusual usage
* Scope anomalies
* Excessive privileges
* Dormant credentials
* Credential-sharing patterns
* Geographic anomalies
* Behavioral deviations
* Potential credential compromise

AI recommendations SHALL be advisory unless an explicitly configured automated policy permits enforcement.

---

## 91. Explainable Security Decisions

AI-based security recommendations SHALL provide explanations.

Example:

```text
Risk: HIGH

Reason:
The production API key normally accesses the lead APIs
from one region. It suddenly issued 14,000 requests from
a previously unseen IP range within 3 minutes.
```

---

## 92. AI False-Positive Handling

Security administrators SHALL be able to:

* Accept alert
* Dismiss alert
* Mark expected behavior
* Suppress future alerts
* Adjust policy

---

## 93. AI Automated Response

Organizations MAY configure:

```text
LOW    → Log
MEDIUM → Alert
HIGH   → Throttle
CRITICAL → Suspend / Revoke
```

Automated revocation SHALL be configurable and auditable.

---

## 94. Human Override

Authorized security administrators SHALL be able to override automated credential controls.

All overrides SHALL be audited.

---

## 95. Data Retention

Credential metadata and audit data SHALL follow configurable retention policies.

Secrets SHALL never be retained merely for audit purposes.

---

## 96. Compliance Requirements

The API Key Platform SHALL support organizational compliance requirements including:

* GDPR
* CCPA/CPRA
* SOC 2
* ISO 27001
* Enterprise security policies
* Data retention requirements

---

## 97. Compliance Audit

Auditors SHALL be able to determine:

```text
Who created a key?
Who approved it?
What scopes were granted?
When was it used?
Where was it used?
When was it rotated?
When was it revoked?
Why was it revoked?
Which application used it?
Which AI agent used it?
```

---

## 98. Security Event Integration

Credential events SHALL be publishable to:

```text
Event Bus
Webhook Platform
SIEM
Security Monitoring
Audit Platform
Analytics Platform
```

---

## 99. Webhook Events

Supported events SHOULD include:

```text
api_key.created
api_key.rotated
api_key.revoked
api_key.expired
api_key.suspended
api_key.compromised
api_key.expiring
api_key.risk_changed
```

---

## 100. Notification Requirements

Developers SHALL receive notifications for important credential events.

Examples:

```text
Production key created
Key expires in 7 days
Key rotated
Key revoked
Suspicious usage detected
Credential potentially compromised
```

---

## 101. API Key Analytics

The platform SHALL expose:

```text
Requests per key
Requests per application
Requests per endpoint
Requests by scope
Error rate
Latency
Rate-limit events
Geographic distribution
Last usage
Usage trends
```

---

## 102. Billing Integration

API usage SHALL integrate with SalesGenie usage metering where applicable.

Usage MAY contribute to:

* Subscription limits
* API quotas
* AI usage
* Workflow consumption
* Enterprise billing

---

## 103. Performance Requirements

## NFR-001

API-key authentication SHOULD add minimal latency to API requests.

---

## NFR-002

Credential lookup SHOULD use low-latency caching where safe.

---

## NFR-003

Revocation propagation SHALL occur within the defined security SLA.

Recommended target:

```text
P95 revocation propagation ≤ 30 seconds
```

Critical environments MAY target near-real-time propagation.

---

## 104. Availability Requirements

The API-key authentication subsystem SHALL be highly available.

Recommended target:

```text
≥ 99.99% authentication availability
```

---

## 105. Failure Behavior

If credential-management storage becomes unavailable:

* Existing valid credentials MAY continue through safe cached verification.
* New key creation SHALL fail safely.
* Key rotation SHALL fail safely.
* Revocation SHALL prioritize security.
* Authorization SHALL never default to allow.

---

## 106. Fail-Closed Security

Authentication and authorization failures SHALL default to denial.

```text
Unknown Credential
      ↓
DENY

Expired Credential
      ↓
DENY

Revoked Credential
      ↓
DENY

Insufficient Scope
      ↓
DENY
```

---

## 107. Cache Requirements

Credential caches SHALL have:

* Short TTL
* Secure invalidation
* Tenant-aware keys
* Revocation invalidation
* No plaintext secret storage

---

## 108. Revocation Cache Invalidation

When a key is revoked:

```text
Revocation Event
      ↓
Credential Store
      ↓
Cache Invalidation
      ↓
API Gateway
      ↓
Authentication Rejection
```

---

## 109. Distributed Architecture

```text
                  Developer Portal
                         │
                         ▼
              API Key Management API
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
       Policy Engine          Audit Service
              │                     │
              ▼                     ▼
       Credential Store       Event Platform
              │
              ▼
        Cache / Redis
              │
              ▼
         API Gateway
              │
       ┌──────┼───────┐
       ▼      ▼       ▼
      Auth    AI     Business
    Service Gateway  Services
```

---

## 110. Database Model

Conceptual `api_keys` entity:

```text
api_keys
--------
id
organization_id
tenant_id
application_id
created_by
name
prefix
secret_hash
environment
status
expires_at
created_at
updated_at
last_used_at
last_used_ip
revoked_at
revoked_by
rotation_parent_id
rotation_child_id
risk_score
description
metadata
```

---

## 111. Key Scopes Model

```text
api_key_scopes
--------------
id
api_key_id
scope
granted_at
granted_by
```

---

## 112. Key Usage Model

```text
api_key_usage
-------------
id
api_key_id
timestamp
endpoint
method
status_code
latency
ip_address
user_agent
request_id
trace_id
scope
```

Sensitive payload data SHALL NOT be stored unnecessarily.

---

## 113. Audit Model

```text
api_key_audit_events
--------------------
id
key_id
organization_id
tenant_id
actor_type
actor_id
event_type
timestamp
ip_address
request_id
trace_id
reason
approval_id
metadata
```

---

## 114. AI Credential Model

```text
ai_credentials
--------------
id
agent_id
organization_id
application_id
credential_type
scopes
issued_at
expires_at
status
created_by
approved_by
policy_id
risk_level
```

---

## 115. API Gateway Integration

Every API request authenticated with an API key SHALL be evaluated by the API Gateway.

The gateway SHALL:

1. Extract credential.
2. Validate credential.
3. Resolve application.
4. Resolve tenant.
5. Validate environment.
6. Validate scopes.
7. Apply rate limits.
8. Apply security policies.
9. Propagate identity.
10. Generate audit metadata.

---

## 116. Identity Propagation

The gateway SHOULD propagate:

```text
X-Request-ID
X-Correlation-ID
X-Application-ID
X-Tenant-ID
X-Key-ID
X-Agent-ID
X-Trace-ID
```

The actual secret SHALL never be propagated internally.

---

## 117. Microservice Authorization

Downstream services SHALL not blindly trust externally supplied identity headers.

Identity metadata SHALL be cryptographically authenticated or conveyed through trusted gateway mechanisms.

---

## 118. Secret Rotation Across Microservices

Internal services SHALL never require developers to manually distribute raw API keys across microservices.

Service-to-service credentials SHOULD use appropriate service identity mechanisms.

---

## 119. Developer Portal UI

The API Key management page SHALL contain:

```text
API Keys
────────────────────────────────

+ Create API Key

Name
Application
Environment
Scopes
Status
Created
Last Used
Expires
Risk

[View] [Rotate] [Revoke]
```

---

## 120. Create Key UI

The creation workflow SHALL contain:

```text
Step 1 — Application
Step 2 — Environment
Step 3 — Name
Step 4 — Scopes
Step 5 — Expiration
Step 6 — Network Restrictions
Step 7 — Review
Step 8 — Approval
Step 9 — Secret Display
```

---

## 121. Secret Display UI

After generation:

```text
Your API key will only be shown once.

[REDACTED SECRET]

Copy Secret

Warning:
Store this credential securely.
SalesGenie cannot display it again.
```

---

## 122. Copy Protection

The UI SHOULD minimize accidental exposure through:

* Clipboard warnings
* Auto-hide
* No persistent display
* No screenshots where platform controls permit

---

## 123. Browser Storage

The Developer Portal SHALL NOT store production API secrets in:

```text
localStorage
sessionStorage
IndexedDB
cookies
analytics payloads
```

after the credential-generation workflow completes.

---

## 124. API Key Export

The platform SHALL NOT provide downloadable files containing unrestricted production secrets by default.

---

## 125. Key Deletion

The platform MAY support logical deletion after revocation.

Historical audit records SHALL remain according to retention requirements.

---

## 126. Key Recovery

Lost API keys SHALL NOT be recoverable.

Developers SHALL create a replacement key.

---

## 127. Compromise Workflow

```text
Credential Suspected Compromised
          ↓
Revoke Immediately
          ↓
Audit Usage
          ↓
Identify Source
          ↓
Assess Impact
          ↓
Notify Owner
          ↓
Generate Replacement
          ↓
Update Application
          ↓
Verify
          ↓
Close Incident
```

---

## 128. Incident Response

Security teams SHALL be able to:

* Search credential usage
* Identify affected applications
* Revoke credentials
* Inspect audit trails
* Identify suspicious IPs
* Identify affected tenants
* Export security evidence
* Create incident records

---

## 129. Testing Requirements

The API Key subsystem SHALL have tests for:

```text
Key generation
Key uniqueness
Secret entropy
Authentication
Authorization
Scope validation
Expiration
Revocation
Rotation
Grace periods
Rate limits
Tenant isolation
Application isolation
IP restrictions
Audit logging
AI permissions
Human approvals
Compromise detection
```

---

## 130. Security Testing

Security testing SHALL include:

* Brute-force testing
* Credential enumeration testing
* Timing attack testing
* Replay testing
* Scope escalation testing
* Tenant escape testing
* Authentication bypass testing
* Authorization bypass testing
* Secret leakage testing
* Cache isolation testing
* Revocation race-condition testing

---

## 131. Contract Testing

The API Key Management API SHALL have automated contract tests.

---

## 132. Load Testing

Authentication SHALL be tested under high request volumes representing enterprise-scale workloads.

Test scenarios SHALL include:

```text
High concurrent authentication
High invalid-key traffic
High revocation volume
High rotation volume
Cache failures
Credential-store failures
Regional failures
```

---

## 133. Chaos Testing

The system SHOULD test:

* Redis failure
* Database failure
* Credential-store latency
* Network partition
* Event-bus delay
* Gateway restart
* Regional failure

Security behavior SHALL remain fail-closed.

---

## 134. Observability

The subsystem SHALL expose metrics:

```text
api_key_auth_success_total
api_key_auth_failure_total
api_key_revocation_total
api_key_rotation_total
api_key_expiration_total
api_key_suspension_total
api_key_compromise_total
api_key_auth_latency
api_key_cache_hit_ratio
api_key_cache_miss_ratio
```

---

## 135. Security Metrics

Security teams SHALL be able to monitor:

```text
Invalid authentication attempts
Credential compromise alerts
Keys without expiration
Keys past rotation policy
Unused keys
Overprivileged keys
Production keys
AI credentials
High-risk credentials
```

---

## 136. SLOs

Recommended targets:

| Metric                      |                    Target |
| --------------------------- | ------------------------: |
| Authentication availability |                  ≥ 99.99% |
| Authentication P95 latency  | ≤ 50 ms excluding network |
| Revocation propagation P95  |                  ≤ 30 sec |
| Key creation success        |                   ≥ 99.9% |
| Rotation success            |                   ≥ 99.9% |
| Audit event durability      |                  ≥ 99.99% |
| Secret exposure incidents   |                         0 |

---

## 137. Non-Functional Requirements

## NFR-010 — Security

Credentials SHALL be protected using industry-standard cryptographic mechanisms.

## NFR-011 — Reliability

Credential validation SHALL remain highly available.

## NFR-012 — Scalability

The system SHALL support millions of credentials.

## NFR-013 — Performance

Authentication SHALL add minimal latency.

## NFR-014 — Auditability

Credential lifecycle events SHALL be immutable and auditable.

## NFR-015 — Maintainability

Credential policies SHALL be centrally configurable.

## NFR-016 — Extensibility

The architecture SHALL support future authentication mechanisms.

---

## 138. Developer Experience

The platform SHALL make secure behavior the easiest behavior.

Developers SHALL be guided toward:

```text
Short-lived credentials
Least privilege
Environment separation
Automatic rotation
Secret managers
Backend-only usage
OAuth where appropriate
```

---

## 139. AI Developer Experience

AI coding agents SHALL be able to discover:

```text
Required API scopes
Authentication method
Credential configuration
Environment
Required permissions
Security restrictions
Example requests
Error conditions
```

AI assistants SHALL NOT automatically generate insecure patterns such as hard-coded production credentials.

---

## 140. AI Coding Guardrails

Documentation and SDK tooling SHOULD warn AI coding assistants when they detect patterns such as:

```python
API_KEY = "sg_live_..."
```

Recommended output:

```text
Use an environment variable or secret manager instead of
hard-coding the SalesGenie API key.
```

---

## 141. Secret Detection in AI Workflows

AI development tools SHOULD detect and redact SalesGenie secrets appearing in prompts, generated code, logs, or tool outputs where technically feasible.

---

## 142. AI Agent Credential Isolation

Each AI agent SHOULD have its own identity and credential context.

```text
Agent A → Credential A
Agent B → Credential B
Agent C → Credential C
```

Agents SHOULD NOT share privileged master keys.

---

## 143. Agent Credential Revocation

Revoking an AI agent SHALL invalidate or detach its associated credentials according to policy.

---

## 144. Human + AI Shared Workflow

```text
Human Developer
      ↓
Create Application
      ↓
Define AI Agent
      ↓
Request Scopes
      ↓
AI Security Analysis
      ↓
Policy Evaluation
      ↓
Human Approval
      ↓
Credential Issued
      ↓
AI Agent Executes
      ↓
Continuous Monitoring
      ↓
Risk Detected?
   ├── NO → Continue
   └── YES
        ↓
Throttle / Suspend / Revoke
        ↓
Human Investigation
```

---

## 145. Security Policy Engine

The policy engine SHALL evaluate rules such as:

```text
IF environment = production
AND scope contains billing.write
THEN require admin approval

IF actor = AI_AGENT
AND operation = customer.delete
THEN require human approval

IF key_age > policy.max_age
THEN require rotation

IF risk_score = critical
THEN suspend credential
```

---

## 146. Policy Precedence

Security policies SHALL follow deterministic precedence.

Recommended order:

```text
Global Security Policy
        ↓
Organization Policy
        ↓
Application Policy
        ↓
Environment Policy
        ↓
Credential Policy
        ↓
Request Policy
```

The most restrictive applicable policy SHALL win unless explicitly overridden by a higher-authority security policy.

---

## 147. Zero Trust Requirement

Every API request SHALL be evaluated independently.

A previously successful request SHALL NOT imply permanent authorization.

---

## 148. Session Independence

API keys SHALL remain stateless authentication credentials unless explicitly associated with a temporary credential session.

---

## 149. Replay Protection

Sensitive credential-management operations SHALL support replay protection through:

* Idempotency keys
* Request timestamps
* Request signatures where applicable

---

## 150. Idempotency

The following operations SHALL support idempotency:

```text
Create API Key
Rotate API Key
Revoke API Key
Suspend API Key
```

---

## 151. Concurrency Control

The platform SHALL prevent race conditions such as:

```text
Two simultaneous rotations
Two simultaneous revocations
Scope update during rotation
Deletion during rotation
```

Optimistic concurrency control SHOULD be used.

---

## 152. Versioning

The Developer API Key API SHALL support API versioning.

Example:

```text
/api/v1/developer/api-keys
/api/v2/developer/api-keys
```

Breaking changes SHALL require a new major API version.

---

## 153. Backward Compatibility

Existing active credentials SHALL remain valid during supported API migration periods unless revoked for security reasons.

---

## 154. Migration

The platform SHALL provide migration mechanisms for:

```text
Legacy API keys
Old key formats
Deprecated scopes
Legacy applications
Older SDK versions
```

---

## 155. Documentation Requirements

Documentation SHALL explain:

* API key creation
* Secure storage
* Environment management
* Scope selection
* Rotation
* Revocation
* Expiration
* Secret managers
* CI/CD usage
* AI-agent usage
* Security best practices
* Incident response

---

## 156. Example Secure Configuration

```python
import os
from salesgenie import SalesGenie

client = SalesGenie(
    api_key=os.environ["SALESGENIE_API_KEY"]
)
```

---

## 157. Example Insecure Configuration

The documentation SHALL explicitly discourage:

```python
client = SalesGenie(
    api_key="sg_live_123456789..."
)
```

---

## 158. Secret Manager Pattern

Recommended architecture:

```text
Application
    ↓
Secret Manager
    ↓
Retrieve Credential
    ↓
Initialize SDK
    ↓
SalesGenie API
```

The application SHOULD avoid persisting secrets unnecessarily.

---

## 159. CI/CD Pattern

```text
CI/CD System
     ↓
Secret Store
     ↓
Runtime Environment
     ↓
SalesGenie SDK
     ↓
API Gateway
```

Secrets SHALL not be committed to source control.

---

## 160. Acceptance Criteria

## AC-001

An authorized developer can create an API key.

## AC-002

The complete secret is shown only once.

## AC-003

The secret is never retrievable after creation.

## AC-004

API keys are stored using secure cryptographic representations.

## AC-005

Keys support scopes.

## AC-006

Keys support expiration.

## AC-007

Expired keys cannot authenticate requests.

## AC-008

Revoked keys cannot authenticate requests.

## AC-009

Keys can be rotated without mandatory downtime.

## AC-010

Rotation supports a configurable grace period.

## AC-011

Production credentials can require administrative approval.

## AC-012

AI agents cannot automatically receive unrestricted production credentials.

## AC-013

High-risk AI operations can require human approval.

## AC-014

Tenant isolation is enforced.

## AC-015

Application isolation is enforced.

## AC-016

IP restrictions can be enforced.

## AC-017

Rate limits are applied.

## AC-018

Credential usage is observable.

## AC-019

Credential lifecycle events are audited.

## AC-020

Secrets never appear in audit logs.

## AC-021

Security administrators can immediately revoke compromised keys.

## AC-022

Unused credentials can be identified.

## AC-023

Credential expiration warnings are generated.

## AC-024

Suspicious credential behavior can trigger alerts.

## AC-025

AI-based risk analysis provides explainable recommendations.

## AC-026

Automated security responses are configurable.

## AC-027

Human administrators can override automated decisions where authorized.

## AC-028

API-key management operations require appropriate authorization.

## AC-029

High-risk credential operations can require MFA.

## AC-030

Credential-management APIs are idempotent.

## AC-031

Credential operations are protected against race conditions.

## AC-032

Sandbox keys cannot access production resources.

## AC-033

Production API keys are not intended for browser exposure.

## AC-034

SDK documentation teaches secure credential handling.

## AC-035

AI coding tools are discouraged from hard-coding credentials.

---

## 161. Definition of Done

The Developer API Key subsystem SHALL be production-ready when:

* API key generation is implemented.
* Secure secret storage is implemented.
* One-time secret display is implemented.
* Key IDs and prefixes are implemented.
* Scopes are implemented.
* Expiration is implemented.
* Rotation is implemented.
* Grace periods are implemented.
* Revocation is near-real-time.
* Environment isolation is implemented.
* Tenant isolation is validated.
* Application binding is implemented.
* Rate limiting is implemented.
* IP restrictions are implemented where supported.
* Credential usage analytics are implemented.
* Audit logging is immutable.
* Security alerts are implemented.
* Compromise detection is implemented.
* Emergency revocation is implemented.
* Human approval workflows are implemented.
* AI-agent credentials are isolated.
* High-risk AI actions support human approval.
* RBAC/ABAC policies are enforced.
* MFA protection exists for high-risk operations.
* Secret scanning is supported.
* CI/CD secret-management guidance is provided.
* SDK integration is complete.
* Developer Portal integration is complete.
* API documentation is complete.
* Security testing passes.
* Penetration testing passes.
* Load testing passes.
* Chaos testing passes.
* Compliance controls are documented.
* Production monitoring is operational.

---

## 162. Strategic Architecture Outcome

The Developer API Key Platform SHALL establish a secure credential layer between developers, enterprise applications, AI agents, the SalesGenie API Gateway, and downstream microservices.

The target architecture is:

```text
                    HUMAN
                      │
                      ▼
               Developer Portal
                      │
                      ▼
              Application Identity
                      │
                      ▼
               API Key Manager
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Scopes      Policies     Approval
          │           │           │
          └───────────┼───────────┘
                      ▼
               Credential Store
                      │
                      ▼
                API Gateway
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
         Auth        AI        Services
          │           │           │
          └───────────┼───────────┘
                      ▼
               Authorization
                      │
                      ▼
               SalesGenie APIs
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Analytics    Audit       Events
          │           │           │
          └───────────┼───────────┘
                      ▼
             Security Monitoring
```

The final system SHALL provide a **zero-trust, least-privilege, tenant-isolated, auditable, AI-aware, enterprise-grade API credential platform** capable of supporting millions of developers, applications, service accounts, integrations, and autonomous AI agents without exposing long-lived privileged credentials unnecessarily.
