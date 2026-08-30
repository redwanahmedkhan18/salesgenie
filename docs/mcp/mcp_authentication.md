# SalesGenie — MCP Authentication Requirements Specification

> **Document:** `mcp_authentication.md`  
> **Product:** SalesGenie Enterprise AI Customer Support & Sales Agent Platform  
> **Subsystem:** MCP Authentication  
> **Requirement Level:** FAANG / Enterprise Production  
> **Actors:** Super Admin, Organization Admin, Manager, Human User, AI Agent, MCP Gateway, MCP Server, MCP Tool, Identity Service, Authorization Service, Policy Engine, Secrets Manager, Audit Service, Security Service, Monitoring Service  
> **Scope:** Authentication, credential lifecycle, identity binding, token management, credential isolation, authorization handoff, AI authentication, human authentication, MCP server authentication, MCP tool execution authentication, rotation, revocation, auditing, security monitoring, and enterprise identity governance.

---

## 1. Purpose

The MCP Authentication subsystem SHALL provide secure, centralized, tenant-aware authentication for all MCP-related interactions within SalesGenie.

The subsystem SHALL authenticate:

- Human users accessing MCP tools.
- AI agents requesting MCP tools.
- Workflows invoking MCP tools.
- SalesGenie services connecting to MCP servers.
- MCP servers connecting to external providers.
- MCP tool execution requests.
- Administrative operations.
- Credential-management operations.

Authentication SHALL establish **who or what is making a request**.

Authorization SHALL separately determine **whether that identity is allowed to perform the requested operation**.

Authentication SHALL NOT imply authorization.

---

## 2. Objectives

The subsystem SHALL:

1. Provide centralized MCP authentication.
2. Support human and AI identities.
3. Support service-to-service authentication.
4. Support MCP server authentication.
5. Support external provider authentication.
6. Support OAuth 2.0 where applicable.
7. Support OpenID Connect where applicable.
8. Support API-key-based integrations where required.
9. Support signed-token authentication where appropriate.
10. Support short-lived access tokens.
11. Support refresh-token rotation.
12. Support credential rotation.
13. Support credential revocation.
14. Support credential expiration.
15. Support tenant isolation.
16. Prevent credential leakage.
17. Prevent token replay.
18. Prevent token substitution.
19. Prevent identity spoofing.
20. Support authentication step-up for sensitive operations.
21. Support machine-to-machine authentication.
22. Support workload identity.
23. Support authentication audit trails.
24. Support authentication anomaly detection.
25. Support emergency credential revocation.
26. Support credential health monitoring.
27. Support authentication failure protection.
28. Prevent AI agents from accessing raw credentials.
29. Prevent AI agents from modifying authentication configuration.
30. Provide enterprise-grade authentication boundaries.

---

## 3. Core Security Principles

The subsystem SHALL follow:

- Zero Trust.
- Least Privilege.
- Defense in Depth.
- Explicit Identity.
- Strong Authentication.
- Short-Lived Credentials.
- Credential Isolation.
- Secret Minimization.
- Tenant Isolation.
- Server-Side Enforcement.
- Fail-Closed Security.
- Continuous Verification.
- Explicit Trust Boundaries.
- Immutable Auditing.
- Credential Rotation.
- Revocation.
- Replay Protection.
- Separation of Authentication and Authorization.

---

## 4. Authentication Architecture

```text
                         SALES GENIE
                              |
              +---------------+----------------+
              |                                |
         Human User                         AI Agent
              |                                |
              +---------------+----------------+
                              |
                       Identity Service
                              |
                       Authentication
                              |
                       Access Token
                              |
                         API Gateway
                              |
                     MCP Authentication
                              |
                     Authorization Layer
                              |
                       Policy Engine
                              |
                         MCP Gateway
                              |
                        MCP Server
                              |
                     External Provider
```

No MCP tool SHALL receive an unauthenticated request from a SalesGenie actor.

---

## 5. Trust Boundaries

The following SHALL be treated as separate trust domains:

```text
Browser
    ↓
Frontend
    ↓
API Gateway
    ↓
Identity Service
    ↓
AI Gateway
    ↓
Workflow Engine
    ↓
MCP Gateway
    ↓
MCP Server
    ↓
External Provider
```

Authentication credentials SHALL NOT be implicitly trusted across these boundaries.

---

## 6. Identity Types

SalesGenie SHALL support at minimum:

```text
HUMAN_USER
AI_AGENT
WORKFLOW
SERVICE
MCP_SERVER
SYSTEM
ADMIN
```

---

## 7. Human Identity

Human identities SHALL be represented using immutable internal identity IDs.

Example:

```yaml
human_identity:
  user_id: "usr_01JXXXXXXXX"
  organization_id: "org_01JXXXXXXXX"
  tenant_id: "tenant_01JXXXXXXXX"
  role_ids:
    - "sales_agent"
  status: "ACTIVE"
```

---

## 8. AI Identity

Every AI Agent SHALL have an independent identity.

Example:

```yaml
ai_identity:
  agent_id: "agent_01JXXXXXXXX"
  organization_id: "org_01JXXXXXXXX"
  tenant_id: "tenant_01JXXXXXXXX"
  owner_user_id: "usr_01JXXXXXXXX"
  status: "ACTIVE"
```

An AI Agent SHALL NOT authenticate as its owner user.

---

## 9. Workflow Identity

Workflows SHOULD have independent identities where appropriate.

```yaml
workflow_identity:
  workflow_id: "wf_01JXXXXXXXX"
  organization_id: "org_01JXXXXXXXX"
  service_identity: "svc_workflow_engine"
```

A workflow SHALL NOT automatically inherit the full identity of the human who created it.

---

## 10. Service Identity

Internal services SHALL authenticate using service identities.

Examples:

```text
AI Gateway
Workflow Engine
MCP Gateway
Authorization Service
Audit Service
```

---

## 11. MCP Server Identity

Every registered MCP server SHALL have an identity.

```yaml
mcp_server_identity:
  server_id: "mcp_srv_01JXXXXXXXX"
  organization_id:
  provider_id:
  authentication_mode:
  status:
```

---

## 12. Authentication Methods

SalesGenie SHALL support authentication methods appropriate to the MCP server and external provider.

Supported methods MAY include:

```text
OAuth 2.0
OpenID Connect
API Key
Bearer Token
JWT
mTLS
Client Certificate
HMAC Signature
Service Account
Workload Identity
Signed Requests
```

The platform SHALL use the strongest supported authentication mechanism appropriate for the integration.

---

## 13. Human Authentication

Human users SHALL authenticate through SalesGenie's Identity Service.

Supported mechanisms MAY include:

```text
Email + Password
OAuth
OpenID Connect
SSO
SAML
MFA
Passkeys
Security Keys
```

MCP services SHALL rely on the authenticated SalesGenie identity rather than independently collecting user passwords.

---

## 14. Human Authentication Flow

```text
Human User
    ↓
SalesGenie Login
    ↓
Identity Provider
    ↓
MFA / Step-Up if Required
    ↓
Identity Verification
    ↓
Access Token
    ↓
SalesGenie API Gateway
    ↓
MCP Gateway
    ↓
Authorization
    ↓
MCP Tool
```

---

## 15. AI Authentication Flow

```text
AI Agent
    ↓
Agent Identity
    ↓
Signed Internal Request
    ↓
AI Gateway
    ↓
Agent Authentication
    ↓
User/Workflow Context Validation
    ↓
Authorization
    ↓
MCP Gateway
    ↓
MCP Server Authentication
    ↓
Tool Execution
```

---

## 16. AI Authentication Requirements

## FR-MCP-AUTH-001

Every AI Agent SHALL have an immutable identity.

## FR-MCP-AUTH-002

Every AI tool request SHALL contain an authenticated agent identity.

## FR-MCP-AUTH-003

AI Agents SHALL NOT directly authenticate to external MCP providers using raw credentials.

## FR-MCP-AUTH-004

AI Agents SHALL NOT access OAuth client secrets.

## FR-MCP-AUTH-005

AI Agents SHALL NOT access API keys.

## FR-MCP-AUTH-006

AI Agents SHALL NOT access refresh tokens.

## FR-MCP-AUTH-007

AI Agents SHALL NOT access private signing keys.

---

## 17. User-to-Agent Identity Binding

When an AI Agent acts on behalf of a human, SalesGenie SHALL maintain both identities.

```yaml
request_context:
  human_user_id:
  ai_agent_id:
  organization_id:
  tenant_id:
  workflow_id:
  session_id:
  request_id:
```

The system SHALL preserve the distinction between:

```text
WHO REQUESTED THE ACTION
```

and

```text
WHO EXECUTED THE ACTION
```

---

## 18. Delegated Authentication

SalesGenie MAY support delegated authentication.

Example:

```text
Human User
    ↓
Authorizes AI Agent
    ↓
AI Agent
    ↓
MCP Gateway
    ↓
External Provider
```

Delegation SHALL be:

* Explicit.
* Scoped.
* Time-limited where appropriate.
* Revocable.
* Auditable.

---

## 19. Delegation Token

Delegated credentials SHOULD contain context such as:

```yaml
delegation:
  subject: "agent_123"
  actor: "user_123"
  organization_id: "org_123"
  tenant_id: "tenant_123"
  scopes:
    - "crm.read"
  issued_at:
  expires_at:
  delegation_id:
```

---

## 20. Token Requirements

Access tokens SHOULD be:

* Short-lived.
* Scoped.
* Audience-restricted.
* Issuer-validated.
* Integrity-protected.
* Non-sensitive in AI context.
* Revocable where required.

---

## 21. JWT Validation

Where JWTs are used, SalesGenie SHALL validate:

```text
Signature
Issuer
Audience
Expiration
Not-Before
Issued-At
Subject
Key ID
Token Type
Required Claims
```

---

## 22. JWT Security

The platform SHALL reject:

```text
Expired Tokens
Malformed Tokens
Wrong Issuer
Wrong Audience
Invalid Signature
Unsupported Algorithm
Missing Required Claims
Future-dated Invalid Tokens
Revoked Tokens
Wrong Tenant
Wrong Subject
```

---

## 23. JWT Algorithm Restrictions

The system SHALL use an explicit allowlist of cryptographic algorithms.

The system SHALL NOT dynamically trust an algorithm declared by an untrusted token.

---

## 24. Token Audience

MCP tokens SHOULD be audience-restricted.

Example:

```yaml
aud:
  - "salesgenie-mcp-gateway"
```

A token intended for another service SHALL NOT automatically be accepted by the MCP Gateway.

---

## 25. Token Issuer

The MCP Gateway SHALL validate the expected issuer.

Example:

```text
iss = SalesGenie Identity Service
```

---

## 26. Token Subject

The `sub` claim SHALL identify the authenticated principal.

Examples:

```text
usr_123
agent_123
svc_mcp_gateway
```

---

## 27. Token Expiration

Access tokens SHALL expire automatically.

The system SHALL reject expired tokens before MCP execution.

---

## 28. Token Refresh

Refresh tokens SHALL:

* Never be exposed to AI models.
* Never be placed in tool arguments.
* Never be logged.
* Be stored securely.
* Support rotation where possible.
* Support revocation.
* Be bound to appropriate clients.

---

## 29. Refresh Token Rotation

The system SHOULD rotate refresh tokens after successful use.

Reuse of an invalidated refresh token SHALL trigger security handling.

---

## 30. Token Replay Protection

The platform SHOULD support:

```text
Token Expiration
Nonce
Request ID
Timestamp Validation
Audience Restriction
Token Rotation
mTLS
DPoP or equivalent sender-constrained mechanisms where appropriate
```

---

## 31. Request Authentication

Each MCP execution request SHOULD include:

```yaml
request:
  request_id:
  trace_id:
  timestamp:
  principal_id:
  principal_type:
  token:
  audience:
  tenant_id:
  organization_id:
```

---

## 32. Request Freshness

High-risk operations SHOULD require request freshness validation.

The platform MAY reject requests outside an allowed clock-skew window.

---

## 33. API Key Authentication

Where external MCP providers require API keys:

* API keys SHALL be stored in the Secrets Manager.
* API keys SHALL never be exposed to AI agents.
* API keys SHALL never be stored in workflow definitions.
* API keys SHALL never be stored in browser storage.
* API keys SHALL never appear in logs.
* API keys SHALL support rotation where possible.
* API keys SHALL be revocable.

---

## 34. OAuth 2.0 Authentication

The platform SHOULD support:

```text
Authorization Code
PKCE
Client Credentials
Refresh Token
Token Revocation
```

The appropriate OAuth flow SHALL be selected based on actor and provider requirements.

---

## 35. OAuth Authorization Code + PKCE

Human-facing integrations SHOULD use:

```text
Authorization Code + PKCE
```

where supported.

The authorization code SHALL be exchanged server-side or through an approved secure OAuth flow.

---

## 36. OAuth Client Credentials

Service-to-service integrations MAY use:

```text
Client Credentials
```

when the external provider supports machine authentication.

Client secrets SHALL remain in secure server-side storage.

---

## 37. OAuth Scope Management

OAuth scopes SHALL be minimized.

Example:

```text
crm.read
crm.write
```

shall be preferred over:

```text
crm.full_access
```

when the provider supports granular scopes.

---

## 38. MCP Server Authentication

Every MCP server connection SHALL use an explicitly configured authentication mode.

Example:

```yaml
mcp_server:
  authentication:
    type: "OAUTH2"
    token_endpoint:
    scopes:
      - "crm.read"
```

---

## 39. MCP Server Authentication Validation

Before executing tools, SalesGenie SHALL verify:

```text
Server Identity
Authentication Status
Credential Validity
Credential Expiration
Server Trust State
Organization Binding
Environment
```

---

## 40. MCP Server Trust

Authentication SHALL NOT automatically imply trust.

The system SHALL maintain separate states:

```text
AUTHENTICATED
TRUSTED
AUTHORIZED
ENABLED
```

---

## 41. MCP Tool Authentication

Tool execution SHALL inherit the authenticated MCP server connection only after:

```text
Actor Authentication
Server Authentication
Authorization
Policy Evaluation
```

have succeeded.

---

## 42. Tool-Level Identity

The MCP Gateway SHALL maintain execution context:

```yaml
execution_identity:
  actor_type:
  actor_id:
  user_id:
  agent_id:
  workflow_id:
  organization_id:
  tenant_id:
  server_id:
  tool_id:
  request_id:
```

---

## 43. Authentication Context Propagation

Identity context SHALL propagate safely across:

```text
Frontend
API Gateway
AI Gateway
Workflow Engine
MCP Gateway
MCP Server
```

Sensitive credentials SHALL NOT be propagated unnecessarily.

---

## 44. Credential Isolation

Credentials SHALL be isolated from:

```text
AI Models
Human UI
Workflow Definitions
Prompt Templates
Logs
Traces
Analytics
Audit Payloads
Error Messages
Browser Storage
Client-Side JavaScript
```

---

## 45. Secrets Manager

All MCP credentials SHALL be stored in a dedicated Secrets Manager or equivalent secure infrastructure.

Examples:

```text
OAuth Client Secret
Refresh Token
API Key
Private Key
Certificate
Provider Credential
MCP Server Credential
```

---

## 46. Secret Retrieval

Services SHALL retrieve secrets only when necessary for execution.

Secret access SHALL be:

* Authenticated.
* Authorized.
* Audited.
* Time-bounded.
* Scope-limited.

---

## 47. Secret Injection

Secrets SHOULD be injected into runtime execution environments rather than application-level AI contexts.

Example:

```text
MCP Gateway
    ↓
Secrets Manager
    ↓
Credential
    ↓
Secure Runtime Connection
    ↓
MCP Server
```

---

## 48. Secret Exposure Prevention

The system SHALL prevent secrets from appearing in:

```text
Prompt
Tool Schema
Tool Arguments
Tool Results
Logs
Exception Messages
Trace Attributes
Metrics Labels
Database Records
Browser Responses
```

---

## 49. Credential Encryption

Credentials SHALL be encrypted:

```text
At Rest
In Transit
```

Encryption keys SHALL be managed separately from encrypted credential data.

---

## 50. Key Management

The platform SHOULD use a dedicated KMS/HSM-backed key-management architecture where available.

Key rotation SHALL be supported.

---

## 51. Credential Rotation

Credentials SHALL support:

```text
Manual Rotation
Scheduled Rotation
Automatic Rotation
Emergency Rotation
Provider-Initiated Rotation
```

---

## 52. Credential Expiration

Credentials SHALL support explicit expiration metadata.

Example:

```yaml
credential:
  expires_at:
  rotation_due_at:
  status: "ACTIVE"
```

---

## 53. Expired Credential Handling

When a credential expires:

```text
New Executions → BLOCKED
Existing Safe Sessions → Policy Dependent
AI Discovery → Tool Marked Unavailable
Administrator → ALERTED
Audit → RECORDED
```

---

## 54. Credential Revocation

Authorized administrators SHALL be able to revoke credentials immediately.

Revocation SHALL prevent new authenticated MCP requests using the revoked credential.

---

## 55. Emergency Credential Revocation

Emergency revocation SHALL support:

```text
Credential
MCP Server
Provider
Organization
Agent
User
```

scope.

---

## 56. Human Authentication Requirements

Human users SHALL:

* Authenticate before accessing protected MCP functionality.
* Use valid SalesGenie credentials.
* Pass MFA when required.
* Receive only valid session tokens.
* Be subject to session expiration.
* Be subject to account status checks.
* Be subject to organization restrictions.

---

## 57. Human Session Management

Human sessions SHALL support:

```text
Login
Refresh
Expiration
Logout
Global Logout
Session Revocation
Concurrent Session Control
Device Tracking
Risk-Based Reauthentication
```

---

## 58. Step-Up Authentication

Sensitive MCP actions SHOULD trigger step-up authentication.

Examples:

```text
Delete CRM Data
Export Customer Data
Send Bulk Messages
Issue Refund
Modify Billing
Change MCP Credentials
Modify MCP Policies
```

---

## 59. MFA

MFA SHALL be configurable for:

```text
Super Admin
Organization Admin
High-Privilege Users
Sensitive MCP Operations
Credential Management
```

---

## 60. AI Authentication Boundaries

AI Agents SHALL NOT:

```text
Authenticate as Super Admin
Obtain Human Passwords
Read MFA Secrets
Read OAuth Client Secrets
Read Refresh Tokens
Read API Keys
Disable MFA
Modify Identity Policies
Create Unauthorized Credentials
Impersonate Another Agent
```

---

## 61. AI Authentication Delegation

When an AI Agent acts on behalf of a human:

```text
Human Identity
+
Agent Identity
+
Delegation Context
+
Tenant Context
```

SHALL remain available to the authorization layer.

---

## 62. Agent Authentication Lifecycle

```text
Agent Created
    ↓
Identity Provisioned
    ↓
Credential / Workload Identity Assigned
    ↓
Agent Enabled
    ↓
Authentication
    ↓
Tool Execution
    ↓
Credential Rotation
    ↓
Agent Disabled / Retired
    ↓
Credentials Revoked
```

---

## 63. Agent Disablement

When an AI Agent is disabled:

```text
New Authentication → DENY
New Tool Execution → DENY
New Workflow Execution → DENY
Active Sessions → Policy Dependent
Credentials → Revoke or Quarantine
```

---

## 64. Workflow Authentication

Workflows SHALL authenticate through a service or workload identity.

A workflow SHALL NOT store long-lived provider secrets directly inside workflow configuration.

---

## 65. Scheduled Workflow Authentication

Scheduled workflows SHALL use non-human service identities.

Human credentials SHALL NOT be required for routine scheduled execution unless explicitly supported and securely delegated.

---

## 66. Human-Created Workflow

A workflow created by a human SHALL not automatically remain authenticated as that human indefinitely.

Example:

```text
User A creates workflow
        ↓
Workflow runs tomorrow
        ↓
Workflow Service Identity
        ↓
Authorized MCP Credential
```

---

## 67. Service-to-Service Authentication

Internal SalesGenie services SHALL authenticate using strong service identity mechanisms.

Examples:

```text
mTLS
Signed JWT
Workload Identity
Service Tokens
```

---

## 68. Internal Service Token

Internal tokens SHOULD include:

```yaml
service_token:
  sub:
  iss:
  aud:
  iat:
  exp:
  service:
  environment:
```

---

## 69. Service Token Validation

Services SHALL validate:

```text
Signature
Issuer
Audience
Expiration
Service Identity
Environment
Required Claims
```

---

## 70. MCP Gateway Authentication

The MCP Gateway SHALL authenticate:

```text
Human Requests
AI Requests
Workflow Requests
Service Requests
Administrative Requests
```

before routing MCP operations.

---

## 71. MCP Gateway Responsibilities

The MCP Gateway SHALL:

1. Validate identity.
2. Validate token.
3. Validate tenant.
4. Validate organization.
5. Validate actor.
6. Validate request freshness where required.
7. Resolve credential.
8. Invoke authorization.
9. Invoke policy evaluation.
10. Retrieve provider credentials securely.
11. Execute MCP request.
12. Record audit events.
13. Remove sensitive credential material from the execution response.

---

## 72. Authentication Failure States

The subsystem SHALL support:

```text
AUTHENTICATION_FAILED
TOKEN_EXPIRED
TOKEN_REVOKED
INVALID_SIGNATURE
INVALID_AUDIENCE
INVALID_ISSUER
INVALID_SUBJECT
INVALID_CLIENT
INVALID_CREDENTIAL
CREDENTIAL_EXPIRED
CREDENTIAL_REVOKED
MFA_REQUIRED
STEP_UP_REQUIRED
TENANT_MISMATCH
SERVER_NOT_TRUSTED
SERVER_DISABLED
AGENT_DISABLED
USER_DISABLED
SESSION_REVOKED
```

---

## 73. Authentication Error Handling

Authentication errors SHALL NOT disclose sensitive details.

Bad:

```text
"The API key for Salesforce account X is invalid."
```

Preferred:

```text
"Authentication failed for the requested MCP integration."
```

Detailed information SHALL be available only to authorized administrators through secure audit/diagnostic interfaces.

---

## 74. Authentication Failure Rate Limiting

Repeated authentication failures SHALL trigger configurable controls:

```text
Rate Limit
Temporary Lock
Credential Quarantine
IP Restriction
Account Lock
Security Alert
MCP Server Isolation
```

---

## 75. Brute Force Protection

The system SHALL protect:

```text
Human Login
OAuth Token Exchange
API Authentication
MCP Authentication
Service Authentication
```

from brute-force attacks.

---

## 76. Credential Stuffing Protection

Human authentication SHALL support controls against credential stuffing.

Possible mechanisms:

```text
Rate Limiting
IP Reputation
Device Signals
MFA
Risk-Based Authentication
Temporary Lockout
```

---

## 77. Replay Attack Protection

The platform SHOULD use:

```text
Short-Lived Tokens
Nonce
Request IDs
Timestamp Validation
Token Rotation
Sender-Constrained Tokens
```

for replay-sensitive operations.

---

## 78. Session Binding

High-risk MCP sessions MAY be bound to:

```text
User
Device
Session
Organization
Tenant
Agent
Workflow
```

---

## 79. Tenant Authentication Isolation

An authenticated identity SHALL be bound to exactly the permitted tenant context.

Example:

```text
User A
Tenant A
    ↓
MCP Tool
    ↓
Tenant B
    ↓
DENY
```

---

## 80. Organization Isolation

The system SHALL prevent an organization-level identity from authenticating into another organization without explicit cross-organization authorization.

---

## 81. Environment Isolation

Credentials SHALL be environment-specific.

```text
Development Credentials
≠
Staging Credentials
≠
Production Credentials
```

Production credentials SHALL NOT be available to development or staging workloads.

---

## 82. Credential Scope

Credentials SHOULD be scoped to:

```text
Tenant
Organization
MCP Server
Provider
Tool
Environment
Capability
```

where technically supported.

---

## 83. OAuth Account Linking

Human users SHALL be able to connect supported third-party accounts through secure OAuth flows.

Example:

```text
User
 ↓
Connect Salesforce
 ↓
OAuth Authorization
 ↓
Provider Consent
 ↓
Authorization Code
 ↓
SalesGenie Token Exchange
 ↓
Secure Credential Storage
```

---

## 84. OAuth Consent

The UI SHALL clearly communicate requested scopes.

Example:

```text
SalesGenie requests:

✓ Read CRM leads
✓ Read contact information

✗ Delete CRM records
✗ Modify billing
```

---

## 85. Credential Ownership

The system SHALL track credential ownership.

Example:

```yaml
credential:
  credential_id:
  owner_type: "USER"
  owner_id:
  organization_id:
  tenant_id:
  provider:
  environment:
```

---

## 86. Credential Types

The system SHALL support:

```text
USER_OAUTH
ORGANIZATION_OAUTH
SERVICE_CREDENTIAL
MCP_SERVER_CREDENTIAL
API_KEY
ACCESS_TOKEN
REFRESH_TOKEN
CERTIFICATE
PRIVATE_KEY
WORKLOAD_IDENTITY
```

---

## 87. Credential Selection

When multiple credentials exist, the system SHALL select credentials according to deterministic policy.

Example:

```text
Workflow Credential
    >
Organization Credential
    >
User Delegated Credential
```

The precedence SHALL be explicitly configured.

---

## 88. Credential Fallback

Credential fallback SHALL NOT silently cross security boundaries.

Example:

```text
User Credential Failed
      ↓
Organization Credential
      ↓
```

shall only occur if explicitly authorized by policy.

---

## 89. Credential Health

The system SHALL monitor:

```text
Valid
Expired
Expiring Soon
Revoked
Invalid
Unauthorized
Provider Error
Unknown
```

---

## 90. Credential Health Checks

The system MAY periodically validate credentials using safe provider endpoints.

Health checks SHALL avoid destructive operations.

---

## 91. Credential Expiration Alerts

Administrators SHOULD receive alerts:

```text
30 days before expiration
14 days before expiration
7 days before expiration
1 day before expiration
At expiration
```

Intervals SHALL be configurable.

---

## 92. Authentication Audit

Every authentication event SHALL be auditable.

Events SHALL include:

```text
MCP_AUTH_ATTEMPT
MCP_AUTH_SUCCESS
MCP_AUTH_FAILURE
MCP_TOKEN_ISSUED
MCP_TOKEN_REFRESHED
MCP_TOKEN_REVOKED
MCP_CREDENTIAL_CREATED
MCP_CREDENTIAL_UPDATED
MCP_CREDENTIAL_ROTATED
MCP_CREDENTIAL_REVOKED
MCP_CREDENTIAL_EXPIRED
MCP_OAUTH_CONNECTED
MCP_OAUTH_DISCONNECTED
MCP_STEP_UP_REQUIRED
MCP_MFA_REQUIRED
MCP_SESSION_CREATED
MCP_SESSION_REVOKED
MCP_AGENT_AUTHENTICATED
MCP_SERVER_AUTHENTICATED
MCP_AUTH_SECURITY_EVENT
```

---

## 93. Authentication Audit Record

```yaml
audit_event:
  event_id:
  event_type:
  timestamp:
  organization_id:
  tenant_id:
  actor_type:
  actor_id:
  user_id:
  agent_id:
  workflow_id:
  server_id:
  credential_id:
  request_id:
  trace_id:
  source:
  authentication_method:
  result:
  failure_reason:
  risk_score:
```

Secrets SHALL never be included.

---

## 94. Security Monitoring

The system SHALL detect:

```text
Repeated Authentication Failures
Impossible Travel Signals
Unexpected Provider Changes
Credential Reuse
Credential Rotation Failure
Token Replay
Token Audience Mismatch
Tenant Mismatch
Agent Identity Anomaly
Unusual Authentication Frequency
Unusual MCP Server Authentication
Unexpected Geographic Signals
```

---

## 95. Authentication Anomaly Detection

AI-assisted security monitoring MAY detect anomalous authentication patterns.

Example:

```text
Agent normally:
20 tool authentications/hour

Observed:
4,000 authentications/hour

Action:
Security alert
+
Rate limit
+
Optional temporary isolation
```

Automated isolation SHALL be policy-controlled.

---

## 96. Authentication Risk Scoring

The platform MAY calculate:

```text
Identity Risk
Credential Risk
Device Risk
Session Risk
Server Risk
Tool Risk
Behavior Risk
```

The resulting risk MAY influence authentication requirements.

---

## 97. Risk-Based Authentication

High-risk authentication MAY require:

```text
MFA
Step-Up Authentication
Reauthentication
Human Approval
Credential Revalidation
Session Termination
```

---

## 98. High-Risk MCP Authentication

The system SHOULD require stronger authentication for:

```text
Financial MCP Servers
Administrative MCP Servers
Production Infrastructure Tools
Destructive Tools
Bulk Export Tools
Identity Management Tools
Credential Management Tools
```

---

## 99. Authentication and Authorization Separation

Authentication SHALL answer:

```text
Who are you?
```

Authorization SHALL answer:

```text
What are you allowed to do?
```

Example:

```text
Authenticated Agent
        ↓
Authorization
        ↓
crm.search_leads → ALLOW
crm.delete_leads → DENY
```

---

## 100. Authentication and Policy

Authentication context SHALL be supplied to the policy engine.

Example:

```yaml
policy_context:
  actor:
    type: "AI_AGENT"
    id: "agent_123"

  user:
    id: "user_123"

  tenant:
    id: "tenant_123"

  organization:
    id: "org_123"

  tool:
    id: "crm.delete_lead"

  authentication:
    method: "WORKLOAD_IDENTITY"
    assurance_level: "HIGH"
```

---

## 101. Authentication Assurance Levels

The platform SHOULD support:

```text
LOW
MEDIUM
HIGH
VERY_HIGH
```

Authentication assurance SHALL be considered by policies for sensitive actions.

---

## 102. Step-Up Example

```text
AI Agent
   ↓
Authenticated
   ↓
Requests:
crm.delete_leads
   ↓
Risk = HIGH
   ↓
Step-Up Required
   ↓
Human Authentication
   ↓
Human Approval
   ↓
Authorization
   ↓
Execution
```

---

## 103. Authentication for Bulk Operations

Bulk operations MAY require stronger authentication based on:

```text
Record Count
Data Classification
Operation Type
Risk Level
Actor Type
Tenant Policy
```

---

## 104. Authentication for External Communication

External communication tools MAY require:

```text
Authenticated User
+
Agent Identity
+
Delegation
+
Step-Up
+
Approval
```

depending on policy.

---

## 105. Authentication for Financial Operations

Financial MCP tools SHALL support stronger authentication.

Examples:

```text
Create Payment
Refund
Transfer
Modify Billing
Issue Credit
```

Recommended control:

```text
Strong Authentication
+
Authorization
+
Human Approval
+
Audit
```

---

## 106. Authentication for Administrative Tools

Administrative MCP tools SHALL require elevated authentication assurance.

Examples:

```text
Create User
Delete User
Modify RBAC
Modify MCP Policy
Change Credentials
Disable Security Controls
```

---

## 107. Super Admin Authentication

Super Admin accounts SHOULD support:

```text
MFA
Strong Session Controls
Step-Up Authentication
Device Controls
Session Monitoring
Security Alerts
```

High-risk MCP operations SHOULD require reauthentication.

---

## 108. Organization Admin Authentication

Organization Admins SHALL be subject to:

```text
RBAC
MFA where configured
Session Expiration
Risk-Based Authentication
Audit Logging
```

---

## 109. AI Agent Credential Provisioning

When an AI Agent is created:

```text
Agent Created
    ↓
Identity Created
    ↓
Credential Strategy Selected
    ↓
Credential Provisioned
    ↓
Scope Applied
    ↓
Credential Stored Securely
    ↓
Agent Activated
```

---

## 110. AI Agent Credential Rotation

AI Agent credentials SHALL support rotation without requiring model changes.

The AI model SHALL never know the credential value.

---

## 111. Agent Credential Revocation

When an agent is:

```text
Disabled
Deleted
Compromised
Suspended
```

its credentials SHALL be revoked or quarantined according to policy.

---

## 112. MCP Server Credential Rotation

MCP server credentials SHALL support zero/minimal-downtime rotation where provider capabilities permit.

Preferred model:

```text
Old Credential
+
New Credential
        ↓
Validation
        ↓
Switch
        ↓
Revoke Old Credential
```

---

## 113. Credential Rotation Failure

If rotation fails:

```text
Current Valid Credential
        ↓
Remain Active
        ↓
Retry Rotation
        ↓
Alert Administrator
```

The system SHALL avoid replacing a valid credential with an invalid credential.

---

## 114. Credential Revocation Propagation

Credential revocation SHALL propagate to:

```text
Credential Store
MCP Gateway
Authentication Cache
Authorization Cache
Active Sessions where applicable
Workflow Runtime
AI Runtime
```

---

## 115. Cache Invalidation

Authentication and credential caches SHALL support immediate or bounded-time invalidation.

High-risk revocations SHALL prioritize immediate invalidation.

---

## 116. Fail-Closed Behavior

When authentication state is uncertain:

```text
DENY
```

shall be the default for sensitive MCP operations.

---

## 117. Fail-Open Prohibition

The platform SHALL NOT fail open because:

```text
Identity Service unavailable
Credential status unknown
Token validation unavailable
Authorization unavailable
Tenant context unavailable
Revocation status unavailable
```

for high-risk MCP operations.

---

## 118. Availability Strategy

The authentication subsystem SHOULD support highly available identity infrastructure.

However:

```text
Availability
<
Security
```

for high-risk authentication decisions.

---

## 119. Authentication API Requirements

The subsystem SHALL conceptually support APIs such as:

```text
POST /api/v1/mcp/auth/token
POST /api/v1/mcp/auth/refresh
POST /api/v1/mcp/auth/revoke

GET  /api/v1/mcp/auth/status
GET  /api/v1/mcp/auth/sessions

POST /api/v1/mcp/credentials
GET  /api/v1/mcp/credentials
GET  /api/v1/mcp/credentials/{credential_id}
PATCH /api/v1/mcp/credentials/{credential_id}
POST /api/v1/mcp/credentials/{credential_id}/rotate
POST /api/v1/mcp/credentials/{credential_id}/revoke
POST /api/v1/mcp/credentials/{credential_id}/validate

POST /api/v1/mcp/oauth/connect
GET  /api/v1/mcp/oauth/callback
POST /api/v1/mcp/oauth/disconnect

POST /api/v1/mcp/servers/{server_id}/authenticate
POST /api/v1/mcp/servers/{server_id}/reauthenticate
POST /api/v1/mcp/servers/{server_id}/revoke-authentication

GET /api/v1/mcp/auth/audit
GET /api/v1/mcp/auth/security-events
```

Actual endpoint naming SHALL remain consistent with SalesGenie's existing API architecture.

---

## 120. Authentication Events

The system SHOULD publish events:

```text
MCP_AUTH_REQUESTED
MCP_AUTH_SUCCESS
MCP_AUTH_FAILURE

MCP_TOKEN_ISSUED
MCP_TOKEN_REFRESHED
MCP_TOKEN_REVOKED
MCP_TOKEN_EXPIRED

MCP_CREDENTIAL_CREATED
MCP_CREDENTIAL_UPDATED
MCP_CREDENTIAL_ROTATION_STARTED
MCP_CREDENTIAL_ROTATED
MCP_CREDENTIAL_ROTATION_FAILED
MCP_CREDENTIAL_REVOKED
MCP_CREDENTIAL_EXPIRED

MCP_SERVER_AUTH_STARTED
MCP_SERVER_AUTHENTICATED
MCP_SERVER_AUTH_FAILED
MCP_SERVER_AUTH_REVOKED

MCP_AGENT_AUTHENTICATED
MCP_AGENT_AUTH_FAILED
MCP_AGENT_CREDENTIAL_ROTATED
MCP_AGENT_CREDENTIAL_REVOKED

MCP_USER_AUTHENTICATED
MCP_USER_AUTH_FAILED
MCP_USER_SESSION_REVOKED

MCP_STEP_UP_REQUIRED
MCP_STEP_UP_COMPLETED
MCP_STEP_UP_FAILED

MCP_AUTH_SECURITY_ALERT
MCP_AUTH_ANOMALY_DETECTED
MCP_AUTH_EMERGENCY_REVOCATION
```

---

## 121. Authentication State Machine

```text
UNAUTHENTICATED
       ↓
AUTHENTICATING
       ↓
AUTHENTICATED
       ↓
AUTHORIZED
       ↓
EXECUTING
       ↓
COMPLETED
```

Failure states:

```text
AUTHENTICATION_FAILED
TOKEN_EXPIRED
TOKEN_REVOKED
CREDENTIAL_EXPIRED
CREDENTIAL_REVOKED
MFA_REQUIRED
STEP_UP_REQUIRED
TENANT_MISMATCH
IDENTITY_DISABLED
SERVER_UNTRUSTED
```

---

## 122. Credential State Machine

```text
PENDING
   ↓
ACTIVE
   ↓
EXPIRING
   ↓
EXPIRED
   ↓
REVOKED
```

Alternative:

```text
ACTIVE
   ↓
ROTATING
   ↓
ROTATED
```

Security state:

```text
ACTIVE
   ↓
QUARANTINED
   ↓
REVOKED
```

---

## 123. Human Authentication Workflow

```text
User
 ↓
Login
 ↓
Identity Provider
 ↓
Credential Validation
 ↓
MFA
 ↓
Identity Created
 ↓
Session Created
 ↓
Access Token
 ↓
MCP Request
 ↓
Authentication Validation
 ↓
Authorization
 ↓
Policy
 ↓
MCP Execution
```

---

## 124. AI Authentication Workflow

```text
AI Agent
 ↓
Agent Identity
 ↓
Signed Request
 ↓
AI Gateway
 ↓
Token / Workload Identity Validation
 ↓
Human Delegation Validation
 ↓
Tenant Validation
 ↓
Authorization
 ↓
Policy
 ↓
MCP Gateway
 ↓
Provider Credential Retrieval
 ↓
MCP Server Authentication
 ↓
Tool Execution
```

---

## 125. Scheduled AI Workflow Authentication

```text
Scheduler
 ↓
Workflow Identity
 ↓
Service Authentication
 ↓
Workflow Authorization
 ↓
Tool Authorization
 ↓
Credential Retrieval
 ↓
MCP Authentication
 ↓
Tool Execution
```

No human login session SHALL be required unless explicitly configured.

---

## 126. Authentication Security Headers

API-facing authentication endpoints SHOULD enforce appropriate security headers and transport security.

All authentication traffic SHALL use secure transport.

---

## 127. TLS

Production MCP authentication traffic SHALL use TLS.

Internal service communication SHOULD use mTLS where appropriate.

---

## 128. Certificate Authentication

For supported enterprise MCP integrations, the platform MAY use client certificates.

Certificate lifecycle SHALL support:

```text
Provision
Validate
Rotate
Expire
Revoke
```

---

## 129. Certificate Validation

The platform SHALL validate:

```text
Certificate Chain
Expiration
Issuer
Subject
Key Usage
Extended Key Usage
Revocation Status where supported
```

---

## 130. Authentication Logging

Authentication logs SHALL contain enough information for investigation without exposing secrets.

Allowed:

```text
user_id
agent_id
server_id
credential_id
request_id
timestamp
result
authentication_method
```

Forbidden:

```text
password
API key
refresh token
private key
client secret
raw access token
```

---

## 131. PII Protection

Authentication telemetry SHALL minimize unnecessary personal data.

Where possible, logs SHOULD use immutable internal IDs instead of raw personal information.

---

## 132. Authentication Metrics

The subsystem SHALL expose metrics such as:

```text
mcp_auth_attempt_total
mcp_auth_success_total
mcp_auth_failure_total
mcp_token_issued_total
mcp_token_refresh_total
mcp_token_revocation_total
mcp_credential_rotation_total
mcp_credential_rotation_failure_total
mcp_credential_expiration_total
mcp_server_auth_failure_total
mcp_agent_auth_failure_total
mcp_user_auth_failure_total
mcp_step_up_total
mcp_mfa_required_total
mcp_auth_latency
mcp_auth_anomaly_total
```

---

## 133. Authentication Alerts

Alerts SHOULD trigger for:

```text
Authentication Failure Spike
Credential Rotation Failure
Expired Production Credential
Repeated Token Replay
Unexpected Server Authentication
Mass Credential Revocation
Agent Authentication Anomaly
Admin Authentication Anomaly
Suspicious Cross-Tenant Authentication
```

---

## 134. Authentication Incident Response

Security incidents SHALL support:

```text
Detect
 ↓
Classify
 ↓
Contain
 ↓
Revoke
 ↓
Rotate
 ↓
Investigate
 ↓
Remediate
 ↓
Restore
 ↓
Audit
```

---

## 135. Emergency Response

Authorized administrators SHALL be able to:

```text
Revoke Credential
Disable MCP Server
Disable Agent
Disable User
Disable Tool
Invalidate Sessions
Force Credential Rotation
Block Provider
```

---

## 136. Mass Revocation

The platform SHOULD support controlled mass revocation for:

```text
Provider
MCP Server
Organization
Tenant
Agent Group
Credential Type
```

---

## 137. Credential Compromise Workflow

```text
Compromise Detected
       ↓
Credential Quarantine
       ↓
Revoke Credential
       ↓
Invalidate Related Sessions
       ↓
Rotate Credential
       ↓
Investigate Usage
       ↓
Review Audit Logs
       ↓
Reauthorize
       ↓
Restore
```

---

## 138. Authentication Dependency Failure

If an external identity provider is unavailable:

```text
Existing Valid Short-Lived Sessions
    → Policy Dependent

New High-Risk Authentication
    → DENY

Credential Rotation
    → QUEUE / ALERT

High-Risk MCP Execution
    → DENY if authentication state cannot be verified
```

---

## 139. Authentication Testing

## Unit Tests

The system SHALL test:

```text
Token Validation
Expiration
Issuer
Audience
Signature
Subject
Tenant Binding
Credential Selection
Credential Expiration
Credential Revocation
Scope Validation
Delegation
```

---

## 140. Integration Tests

The system SHALL test:

```text
Human Login
AI Authentication
Workflow Authentication
MCP Server Authentication
OAuth
API Keys
Service Authentication
Credential Rotation
Credential Revocation
Token Refresh
MCP Gateway
External Provider
```

---

## 141. Security Tests

The subsystem SHALL test:

```text
Token Replay
Token Substitution
JWT Algorithm Confusion
Expired Token
Invalid Signature
Wrong Audience
Wrong Issuer
Cross-Tenant Authentication
Credential Leakage
Secret Exposure
Session Hijacking
Privilege Escalation
Credential Theft
OAuth CSRF
OAuth Redirect Manipulation
Refresh Token Reuse
Brute Force
Credential Stuffing
```

---

## 142. AI Security Tests

The system SHALL test whether AI Agents can:

```text
Access Raw Credentials
Generate Valid Authentication Tokens
Impersonate Users
Impersonate Admins
Reuse Expired Tokens
Bypass Token Validation
Modify Authentication Policy
Read Refresh Tokens
Read API Keys
Invoke MCP Without Authentication
Cross Tenant Boundaries
```

All unauthorized attempts SHALL fail.

---

## 143. Human Security Tests

The system SHALL test:

```text
MFA Bypass
Session Fixation
Session Replay
Session Revocation
Logout Invalidation
Password Abuse
OAuth Account Takeover
Credential Stuffing
Brute Force
Privilege Escalation
```

---

## 144. Chaos Testing

The platform SHOULD test:

```text
Identity Service Failure
Secrets Manager Failure
MCP Gateway Failure
Token Validation Failure
Credential Store Failure
Network Partition
Clock Skew
Provider Authentication Failure
Credential Rotation Failure
```

The system SHALL fail safely.

---

## 145. Performance Requirements

Authentication SHALL be optimized for:

```text
High Concurrent AI Agents
High Concurrent Human Users
High Workflow Execution
High MCP Tool Invocation
Multi-Tenant SaaS
Distributed Microservices
```

Authentication infrastructure SHALL not become a single bottleneck for MCP execution.

---

## 146. Availability Requirements

Identity and authentication services SHOULD be highly available.

Critical authentication data SHOULD support:

```text
Replication
Failover
Backup
Recovery
Monitoring
```

---

## 147. Consistency Requirements

Security-critical authentication state SHALL prioritize consistency.

Examples:

```text
Credential Revocation
Agent Disablement
User Disablement
MCP Server Disablement
Token Revocation
```

shall propagate within defined security SLAs.

---

## 148. Caching Requirements

The system MAY cache:

```text
Public Keys
Provider Metadata
Non-Sensitive Identity Metadata
```

The system SHALL use controlled TTLs for security-sensitive authentication state.

---

## 149. Public Key Rotation

For JWT/OIDC integrations, the platform SHALL support provider key rotation.

The system SHALL retrieve and validate updated public keys using trusted metadata.

---

## 150. Clock Synchronization

Authentication infrastructure SHALL use synchronized system clocks.

Clock skew SHALL be explicitly handled for:

```text
iat
exp
nbf
Request Timestamp
OAuth Token Validity
Certificate Validity
```

---

## 151. Authentication Configuration

Administrators SHALL be able to configure:

```text
Authentication Method
Token Lifetime
Refresh Policy
MFA Requirement
Step-Up Requirement
Credential Expiration
Rotation Schedule
Session Lifetime
Authentication Rate Limits
Provider Scopes
Allowed Algorithms
Trust Policies
```

---

## 152. Configuration Governance

Authentication configuration changes SHALL:

* Require authorization.
* Be audited.
* Support versioning where appropriate.
* Support rollback where feasible.
* Trigger security events for high-risk changes.

---

## 153. AI Configuration Restrictions

AI Agents SHALL NOT modify:

```text
Authentication Policy
MFA Policy
Credential Policy
Token Lifetime
OAuth Scopes
Identity Provider
MCP Server Trust
Credential Rotation Policy
```

---

## 154. Human Configuration Restrictions

Only authorized administrative roles SHALL manage authentication configuration.

---

## 155. Multi-Tenant Authentication

Every authentication request SHALL contain or derive:

```text
Tenant
Organization
Principal
Environment
```

The platform SHALL reject ambiguous tenant contexts.

---

## 156. Cross-Tenant Access

Cross-tenant authentication SHALL be denied by default.

If explicitly supported, it SHALL require:

```text
Explicit Identity Relationship
Explicit Policy
Explicit Scope
Audit
Strong Authentication
```

---

## 157. Multi-Organization Users

If a user belongs to multiple organizations, the active organization context SHALL be explicit.

Example:

```text
User
 ↓
Organization Selection
 ↓
Tenant Context
 ↓
MCP Authentication
```

---

## 158. Account Status

Authentication SHALL check account status.

Supported states:

```text
ACTIVE
PENDING
SUSPENDED
DISABLED
LOCKED
DELETED
```

Only eligible states SHALL authenticate.

---

## 159. Agent Status

AI Agents SHALL support:

```text
ACTIVE
PAUSED
SUSPENDED
DISABLED
RETIRED
```

Only authorized active agents SHALL authenticate.

---

## 160. MCP Server Status

MCP Servers SHALL support:

```text
REGISTERED
AUTHENTICATING
AUTHENTICATED
ENABLED
DEGRADED
DISABLED
BLOCKED
RETIRED
```

Authentication SHALL fail for disabled or blocked servers.

---

## 161. Provider Account Status

External provider credentials SHALL support:

```text
CONNECTED
AUTHENTICATED
EXPIRED
REVOKED
DISCONNECTED
ERROR
```

---

## 162. Authentication Health Dashboard

Administrators SHOULD be able to view:

```text
Connected MCP Servers
Authentication Success Rate
Authentication Failure Rate
Expiring Credentials
Expired Credentials
Revoked Credentials
Failed Rotations
OAuth Connections
Agent Authentication
Human Authentication
Security Alerts
```

---

## 163. Human Dashboard

Authorized users SHOULD see:

```text
Connected Accounts
Authentication Status
Connected MCP Servers
Credential Expiration
Recent Authentication Activity
Security Notifications
Reauthentication Requests
```

Raw credentials SHALL never be displayed.

---

## 164. AI Dashboard

AI Agents SHALL NOT have access to credential management UI.

AI-facing systems MAY expose:

```text
Authentication Available
Tool Available
Credential Valid
Authentication Required
Authentication Failed
Human Action Required
```

but SHALL NOT expose credential secrets.

---

## 165. User Requirements

## UR-MCP-AUTH-001

Users SHALL be able to securely connect supported MCP integrations.

## UR-MCP-AUTH-002

Users SHALL understand which permissions/scopes an integration requests.

## UR-MCP-AUTH-003

Users SHALL be able to disconnect integrations.

## UR-MCP-AUTH-004

Users SHALL be notified when authentication expires.

## UR-MCP-AUTH-005

Users SHALL be able to reauthenticate integrations.

## UR-MCP-AUTH-006

Users SHALL be able to revoke connected integrations where authorized.

## UR-MCP-AUTH-007

Users SHALL receive clear authentication errors without sensitive information.

---

## 166. AI User Requirements

## UR-MCP-AUTH-008

AI Agents SHALL authenticate automatically using managed identity mechanisms.

## UR-MCP-AUTH-009

AI Agents SHALL not require humans to manually provide secrets during every execution unless policy explicitly requires human interaction.

## UR-MCP-AUTH-010

AI Agents SHALL receive only the authentication context required to execute authorized MCP tools.

## UR-MCP-AUTH-011

AI Agents SHALL escalate to humans when authentication requires human interaction.

Example:

```text
AI:
"Salesforce authorization has expired.
Please reconnect Salesforce to continue."
```

---

## 167. Human + AI Combined Authentication

For delegated AI execution:

```text
Human Identity
      +
AI Agent Identity
      +
Workflow Identity
      +
Tenant Identity
      +
MCP Server Identity
      +
Credential Identity
```

SHALL form the complete authentication context.

---

## 168. Combined Execution Example

```text
User:
"Update these 20 leads."

      ↓

Authenticated User
user_123

      ↓

Authorized AI Agent
agent_sales_01

      ↓

Workflow
wf_lead_update

      ↓

MCP Server
mcp_srv_salesforce

      ↓

Credential
cred_salesforce_org_01

      ↓

MCP Tool
salesforce.update_lead

      ↓

Authorization
ALLOW / REQUIRE_APPROVAL / DENY

      ↓

Execution
```

---

## 169. Authentication Decision

The final authentication context SHALL be represented conceptually as:

```yaml
authentication_context:
  principal:
    type: "AI_AGENT"
    id: "agent_123"

  delegated_by:
    type: "HUMAN_USER"
    id: "user_123"

  workflow:
    id: "wf_123"

  organization:
    id: "org_123"

  tenant:
    id: "tenant_123"

  mcp_server:
    id: "mcp_srv_123"

  credential:
    id: "cred_123"

  authentication:
    method: "OAUTH2"
    assurance_level: "HIGH"

  validity:
    authenticated: true
    expires_at:
```

---

## 170. Acceptance Criteria

The MCP Authentication subsystem SHALL be considered production-ready only when:

* [ ] Human authentication is implemented.
* [ ] AI Agent authentication is implemented.
* [ ] Workflow authentication is implemented.
* [ ] Service authentication is implemented.
* [ ] MCP Server authentication is implemented.
* [ ] Authentication and authorization are separated.
* [ ] Tenant identity is enforced.
* [ ] Organization identity is enforced.
* [ ] Agent identity is independent.
* [ ] Human-to-agent delegation is supported.
* [ ] OAuth 2.0 is supported where applicable.
* [ ] OIDC is supported where applicable.
* [ ] API-key authentication is supported where required.
* [ ] JWT validation is implemented securely.
* [ ] Token expiration is enforced.
* [ ] Token issuer validation is enforced.
* [ ] Token audience validation is enforced.
* [ ] Token signature validation is enforced.
* [ ] Token replay protection is implemented.
* [ ] Refresh-token rotation is implemented where supported.
* [ ] Credential encryption is implemented.
* [ ] Secrets Manager integration is implemented.
* [ ] Credentials are isolated from AI models.
* [ ] Credentials are isolated from workflow definitions.
* [ ] Credentials are isolated from browser storage.
* [ ] Secrets are redacted from logs.
* [ ] Credential rotation is implemented.
* [ ] Credential revocation is implemented.
* [ ] Credential expiration is implemented.
* [ ] Emergency credential revocation is implemented.
* [ ] MFA is supported.
* [ ] Step-up authentication is supported.
* [ ] Risk-based authentication is supported.
* [ ] Cross-tenant authentication is blocked by default.
* [ ] Environment credential isolation is implemented.
* [ ] Authentication rate limiting is implemented.
* [ ] Brute-force protection is implemented.
* [ ] Credential-stuffing protection is implemented.
* [ ] Authentication anomaly detection is implemented.
* [ ] Authentication events are audited.
* [ ] Security events are monitored.
* [ ] Authentication metrics are available.
* [ ] Authentication alerts are available.
* [ ] Authentication state is observable.
* [ ] Authentication failure is fail-closed for sensitive operations.
* [ ] AI Agents cannot access raw credentials.
* [ ] AI Agents cannot impersonate humans.
* [ ] AI Agents cannot modify authentication policies.
* [ ] AI Agents cannot bypass MCP Gateway authentication.
* [ ] Human administrators can revoke compromised credentials.
* [ ] MCP server credentials can be rotated.
* [ ] Provider credentials can be disconnected.
* [ ] Public key rotation is supported for JWT/OIDC.
* [ ] Clock skew is handled.
* [ ] Production authentication traffic is encrypted.
* [ ] Security testing is implemented.
* [ ] AI-specific authentication security testing is implemented.
* [ ] Disaster recovery is tested.

---

## 171. Golden Rules

1. **Authentication SHALL establish identity; authorization SHALL establish permission.**
2. **Authentication SHALL never imply authorization.**
3. **Every MCP request SHALL have an authenticated principal.**
4. **Every AI Agent SHALL have its own identity.**
5. **AI Agents SHALL never authenticate as their human owners.**
6. **Human and AI identities SHALL remain separately auditable.**
7. **Delegated AI actions SHALL preserve both human and agent identity.**
8. **Workflow identities SHALL be independent from the human creator where appropriate.**
9. **MCP servers SHALL have explicit identities.**
10. **External provider credentials SHALL never be exposed to AI models.**
11. **AI Agents SHALL never receive passwords, API keys, refresh tokens, client secrets, or private keys.**
12. **Credentials SHALL be stored in secure secret-management infrastructure.**
13. **Secrets SHALL never appear in prompts, tool arguments, logs, traces, or analytics.**
14. **Access tokens SHALL be short-lived whenever practical.**
15. **Tokens SHALL be validated for signature, issuer, audience, subject, and expiration.**
16. **Expired tokens SHALL always be rejected.**
17. **Revoked credentials SHALL not authenticate new MCP operations.**
18. **Credential rotation SHALL be supported wherever provider capabilities permit.**
19. **Credential revocation SHALL propagate rapidly across authentication infrastructure.**
20. **Authentication state SHALL be tenant-aware.**
21. **Cross-tenant authentication SHALL be denied by default.**
22. **Production credentials SHALL never be reused in development environments.**
23. **Authentication failures SHALL not disclose secrets or sensitive implementation details.**
24. **High-risk MCP operations SHALL support stronger authentication assurance.**
25. **Sensitive operations SHALL support step-up authentication.**
26. **MFA SHALL be enforceable for privileged users.**
27. **AI Agents SHALL never disable MFA.**
28. **AI Agents SHALL never modify authentication policies.**
29. **AI Agents SHALL never create credentials without explicit server-side authorization.**
30. **AI-generated content SHALL never be treated as authentication authority.**
31. **Tool descriptions SHALL never authenticate an AI Agent.**
32. **MCP tool responses SHALL never establish identity.**
33. **MCP server authentication SHALL be independent from tool authorization.**
34. **A trusted MCP server SHALL not automatically authorize every tool.**
35. **A valid credential SHALL not automatically authorize every MCP operation.**
36. **Authentication caches SHALL have bounded lifetimes.**
37. **High-risk revocations SHALL invalidate relevant cached authentication state immediately or within a defined security SLA.**
38. **Authentication uncertainty SHALL result in denial for sensitive operations.**
39. **The platform SHALL fail closed when security-critical authentication state cannot be verified.**
40. **Every authentication event SHALL be auditable.**
41. **Every credential lifecycle event SHALL be auditable.**
42. **Authentication telemetry SHALL never contain raw secrets.**
43. **Credential compromise SHALL trigger revocation and rotation procedures.**
44. **MCP authentication SHALL be observable through metrics, logs, traces, and security alerts.**
45. **Authentication SHALL be enforced server-side and SHALL never rely on frontend controls.**
46. **No browser-controlled value SHALL be trusted as proof of MCP authorization.**
47. **No AI model SHALL be trusted to enforce authentication.**
48. **No workflow definition SHALL be trusted to enforce authentication.**
49. **No MCP server SHALL be trusted to enforce SalesGenie's tenant isolation.**
50. **SalesGenie's MCP Gateway SHALL remain the authoritative authentication enforcement boundary.**
51. **Authentication credentials SHALL be scoped to the smallest practical identity, tenant, server, environment, and capability boundary.**
52. **Human approval SHALL never substitute for missing authentication.**
53. **A human approval SHALL occur only after the requesting actor has been authenticated.**
54. **Authentication SHALL precede authorization, and authorization SHALL precede MCP execution.**
55. **No MCP tool SHALL execute solely because a credential exists.**
