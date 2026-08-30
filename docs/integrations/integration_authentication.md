# SalesGenie — Integration Authentication Requirements

**Document:** `integration_authentication.md`  
**Product:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Requirement Level:** FAANG-Level / Production-Grade  
**Scope:** Integration Authentication  
**Actors:** Human Users + AI Agents + Workflows + Platform Services + Super Admins  
**Architecture:** Enterprise Microservices + Multi-Agent AI + Event-Driven Architecture + MCP + n8n + RAG  
**Target Scale:** 10M+ users, 500K+ concurrent conversations

---

## 1. Purpose

The SalesGenie Integration Authentication subsystem shall provide a secure, centralized, multi-tenant authentication framework for connecting SalesGenie with external platforms, SaaS applications, APIs, enterprise systems, data sources, communication channels, and automation providers.

The subsystem shall support authentication for both:

- Human-initiated integrations
- AI-agent-initiated authentication requests
- Workflow-initiated integrations
- Background synchronization services
- MCP tools
- n8n workflows
- Internal microservices

The authentication system shall ensure that:

- Credentials are never exposed to unauthorized users or AI agents.
- Authentication is tenant-isolated.
- Authentication scopes are explicit.
- Tokens are securely stored.
- Token lifecycle is managed automatically.
- Authentication failures are recoverable.
- High-risk authentication changes require human authorization.
- AI agents cannot grant themselves authentication privileges.
- Authentication activity is fully auditable.

---

## 2. Scope

The subsystem shall cover:

```text
Authentication Provider Management
OAuth 2.0
OAuth 2.1
OpenID Connect
API Key Authentication
Bearer Token Authentication
JWT Authentication
Service Account Authentication
Client Credentials
Basic Authentication
HMAC Authentication
mTLS Authentication
Signed Requests
Refresh Token Management
Access Token Management
Credential Vaulting
Token Rotation
Token Revocation
Token Expiration
Authentication Scopes
Consent Management
Authentication Sessions
Authentication State
Authentication Health
Authentication Recovery
Authentication Testing
AI Authentication Requests
Human Authentication
MCP Authentication
n8n Authentication
Audit Logging
Security Monitoring
```

---

## 3. Actors

## 3.1 Super Admin

The Super Admin shall be able to:

* Configure platform-level authentication providers.
* Approve authentication methods.
* Disable insecure authentication mechanisms.
* Configure global authentication policies.
* Configure credential requirements.
* Configure OAuth security policies.
* Configure token lifetime policies.
* Review authentication audit logs.
* Monitor authentication failures.
* Revoke compromised integration credentials.
* Disable compromised providers.
* Configure enterprise authentication restrictions.

---

## 3.2 Organization Admin

The Organization Admin shall be able to:

* Connect integrations.
* Authorize OAuth applications.
* Configure API credentials.
* Manage service accounts.
* Reauthorize integrations.
* Revoke credentials.
* Rotate credentials.
* View authentication health.
* Configure integration authentication policies.
* Assign authentication access to teams.
* Assign authentication access to AI agents.
* Assign authentication access to workflows.

---

## 3.3 Team Manager

The Team Manager shall be able to:

* Use organization-approved authentication.
* Connect permitted integrations.
* Request additional authentication scopes.
* Reauthorize approved integrations.
* View authentication status.

---

## 3.4 Sales Agent

The Sales Agent shall be able to:

* Use authorized integrations.
* Initiate permitted OAuth flows.
* View connection status.
* Request authentication when required.

The Sales Agent shall never be able to view raw credentials belonging to other users.

---

## 3.5 Support Agent

The Support Agent shall be able to:

* Use approved authenticated integrations.
* Initiate permitted authentication flows.
* Reauthorize approved integrations.
* View connection health.

---

## 3.6 Developer

Developers shall be able to:

* Register authentication schemes.
* Configure OAuth metadata.
* Define authentication schemas.
* Define required scopes.
* Configure token exchange mechanisms.
* Implement authentication adapters.
* Test authentication flows.

Developers shall not automatically gain access to production credentials.

---

## 3.7 AI Agent

AI agents shall be able to:

* Detect authentication requirements.
* Request authentication.
* Redirect users to authorization flows.
* Check authentication status.
* Request reauthorization.
* Detect expired credentials.
* Request credential rotation.
* Retry operations after successful authentication.

AI agents shall never receive raw secrets.

---

## 3.8 Workflow Engine

The Workflow Engine shall:

* Check authentication status.
* Trigger authentication-required events.
* Pause workflows when authentication is unavailable.
* Resume workflows after successful authentication.
* Execute only authenticated integration actions.

---

## 4. User Requirements

## UR-001 — Authentication Dashboard

SalesGenie shall provide a centralized Integration Authentication Dashboard.

The dashboard shall display:

```text
Integration
Provider
Authentication Method
Connection Status
Authentication Status
Token Status
Token Expiration
Granted Scopes
Credential Version
Last Authentication
Last Refresh
Last Failure
```

Sensitive credential values shall never be displayed.

---

## UR-002 — Connect Integration

Authorized users shall be able to connect an external integration.

The connection flow shall support:

```text
Select Integration
        ↓
Review Authentication Requirements
        ↓
Review Requested Scopes
        ↓
Authenticate
        ↓
Consent
        ↓
Token Exchange
        ↓
Secure Storage
        ↓
Validation
        ↓
Connection Test
        ↓
Connected
```

---

## UR-003 — OAuth Authentication

Users shall be able to connect OAuth-enabled integrations through a secure authorization flow.

The platform shall support:

* Authorization Code flow.
* PKCE.
* Refresh tokens.
* Scope management.
* Consent.
* Token rotation where supported.

Implicit OAuth flows shall not be enabled for new integrations unless explicitly required by a legacy provider.

---

## UR-004 — OAuth Scope Review

Before authorization, the user shall see:

```text
Requested Scope
Reason
Data Access
Available Actions
Risk Level
```

Example:

```text
Gmail

READ_EMAIL
Reason:
Allow SalesGenie to analyze incoming sales emails.

SEND_EMAIL
Reason:
Allow approved AI agents to send sales follow-ups.

Risk:
HIGH
Approval:
Required
```

---

## UR-005 — API Key Authentication

Users shall be able to configure API-key-based integrations.

The UI shall provide:

```text
API Key
Endpoint
Environment
Optional Header Name
Optional Key ID
```

API keys shall be securely transmitted and stored.

---

## UR-006 — Service Account Authentication

Enterprise integrations shall support service accounts where supported by the provider.

The system shall allow:

* Service account registration.
* Credential upload.
* Credential validation.
* Credential rotation.
* Credential revocation.

Private keys shall never be shown after successful storage.

---

## UR-007 — Client Credentials

The system shall support OAuth client-credentials authentication for machine-to-machine integrations.

---

## UR-008 — Bearer Token Authentication

Users shall be able to configure bearer-token integrations.

Tokens shall be stored in the secure credential vault.

---

## UR-009 — JWT Authentication

The platform shall support JWT-based authentication where required by external providers.

The system shall validate:

```text
Issuer
Audience
Expiration
Not-Before
Signature
Algorithm
Key ID
```

---

## UR-010 — HMAC Authentication

The platform shall support HMAC-based request signing.

The system shall securely store signing secrets.

---

## UR-011 — mTLS Authentication

Enterprise integrations shall support mutual TLS where required.

The system shall support:

```text
Client Certificate
Private Key
CA Certificate
Certificate Expiration
Certificate Rotation
```

Private keys shall never be exposed through UI or AI interfaces.

---

## UR-012 — Authentication Status

Users shall be able to see:

```text
CONNECTED
AUTHENTICATION_REQUIRED
TOKEN_EXPIRED
TOKEN_REFRESH_REQUIRED
AUTHENTICATION_FAILED
REVOKED
DISABLED
COMPROMISED
```

---

## UR-013 — Reauthentication

Users shall be able to reauthenticate without reinstalling the integration.

---

## UR-014 — Reauthorization

Users shall be able to grant additional scopes through a controlled reauthorization process.

---

## UR-015 — Credential Rotation

Authorized users shall be able to rotate integration credentials.

The rotation process shall support zero-downtime rotation where the provider permits it.

---

## UR-016 — Credential Revocation

Authorized users shall be able to revoke credentials.

Revocation shall immediately prevent future integration access.

---

## UR-017 — Token Expiration

Users shall be notified before important credentials expire.

Notifications shall support configurable thresholds.

Example:

```text
30 days
14 days
7 days
24 hours
```

---

## UR-018 — Authentication Failure Notification

Users shall receive notifications for:

* Authentication failures.
* Token expiration.
* Token revocation.
* Provider authorization denial.
* Credential compromise.
* Repeated refresh failures.

---

## UR-019 — Authentication Testing

Users shall be able to test authentication independently from business actions.

Example:

```text
Authenticate
     ↓
Token Validation
     ↓
Scope Validation
     ↓
Provider Connectivity
     ↓
Result
```

---

## UR-020 — Authentication Troubleshooting

The system shall provide actionable diagnostics.

Example:

```text
Authentication failed.

Cause:
OAuth refresh token was revoked.

Recommended action:
Reauthorize Gmail integration.

Required permission:
Organization Admin
```

---

## UR-021 — Credential Visibility

Users shall never be shown complete:

```text
API Keys
Access Tokens
Refresh Tokens
Passwords
Private Keys
Client Secrets
Webhook Secrets
```

The UI may display masked identifiers.

Example:

```text
API Key:
••••••••••••9F3A
```

---

## UR-022 — Multiple Accounts

Users shall be able to connect multiple accounts for the same provider where supported.

Example:

```text
Google Workspace
├── sales@company.com
├── support@company.com
└── marketing@company.com
```

Each account shall have an independent authentication context.

---

## UR-023 — Authentication Ownership

The system shall identify:

```text
Who authenticated?
When?
Which tenant?
Which integration?
Which scopes?
Which account?
Which credential version?
```

---

## UR-024 — Authentication Delegation

Organization administrators shall be able to configure whether authentication may be delegated to:

* Team Managers.
* Sales Agents.
* Support Agents.
* AI Agents.

AI agents shall never receive unrestricted delegated authentication authority.

---

## UR-025 — Authentication Approval

Organizations shall be able to require approval for:

```text
New Integration
New OAuth Scope
Production Credential
Service Account
High-Risk Permission
AI Agent Authentication
Credential Rotation
Credential Replacement
```

---

## UR-026 — Authentication Session Management

Users shall be able to view active authentication sessions where supported.

---

## UR-027 — Authentication Revocation

Administrators shall be able to revoke:

* One credential.
* One account connection.
* One integration.
* All credentials for an integration.
* All credentials belonging to a compromised provider.

---

## 5. AI-Specific User Requirements

## AI-UR-001 — AI Authentication Detection

AI agents shall detect when a required integration is unauthenticated.

Example:

```text
AI Agent:
"I need Salesforce access to search the requested leads."

Authentication State:
NOT_CONNECTED
```

---

## AI-UR-002 — AI Authentication Request

The AI agent shall create a structured authentication request rather than asking for credentials directly.

```text
AuthenticationRequest
├── integration_id
├── required_scopes
├── requested_capabilities
├── business_reason
├── risk_level
├── workflow_id
├── agent_id
└── approval_required
```

---

## AI-UR-003 — AI OAuth Initiation

AI agents may initiate an OAuth authorization request.

The user shall complete authentication through the provider's authorization interface.

---

## AI-UR-004 — AI Credential Isolation

AI agents shall never receive:

```text
Access Token
Refresh Token
API Key
Client Secret
Password
Private Key
Certificate Private Key
```

---

## AI-UR-005 — AI Authentication Status

AI agents may query:

```text
is_authenticated
authentication_status
token_expiration_status
required_action
```

without receiving secret material.

---

## AI-UR-006 — AI Reauthentication

If authentication expires, the AI agent may request reauthentication.

The AI agent shall not attempt to fabricate or infer credentials.

---

## AI-UR-007 — AI Scope Minimization

AI agents shall request only scopes required to complete the current task.

Example:

```text
Task:
Find customer information.

Required:
CRM.customer.read

Not required:
CRM.customer.delete
```

---

## AI-UR-008 — AI Authentication Escalation

AI agents shall escalate to a human when:

* Authentication requires consent.
* New scopes require approval.
* Credential replacement is required.
* Security policy blocks authentication.
* Provider requires interactive login.
* Authentication appears compromised.

---

## AI-UR-009 — AI Authentication Recovery

AI agents may automatically retry authentication-dependent operations after:

```text
Token Refresh
Successful Reauthentication
Credential Rotation
Provider Recovery
```

---

## AI-UR-010 — AI Authentication Policy Awareness

AI agents shall receive only policy-derived authentication capabilities.

---

## AI-UR-011 — AI Cannot Self-Authorize

AI agents shall never be allowed to:

```text
Grant themselves OAuth scopes
Approve their own authentication
Create privileged service accounts
Retrieve user credentials
Disable MFA requirements
Bypass authentication policy
Modify tenant authentication policy
```

---

## AI-UR-012 — AI Authentication Explanation

The AI assistant shall explain:

* Why authentication is required.
* Which integration is required.
* Which scopes are required.
* What data may be accessed.
* What actions may be performed.
* Whether human approval is required.

---

## 6. System Requirements

## SR-001 — Centralized Authentication Service

SalesGenie shall provide a centralized Integration Authentication Service.

Responsibilities:

```text
Authentication
Authorization Flow
Token Exchange
Token Storage
Token Refresh
Token Revocation
Credential Rotation
Scope Management
Authentication Health
Authentication Audit
```

---

## SR-002 — Authentication Provider Registry

The system shall maintain metadata for every authentication provider.

```text
AuthenticationProvider
├── provider_id
├── integration_id
├── authentication_type
├── authorization_endpoint
├── token_endpoint
├── revocation_endpoint
├── scopes
├── PKCE_support
├── refresh_token_support
├── client_authentication_method
├── security_requirements
└── status
```

---

## SR-003 — Authentication Scheme Registry

The platform shall support pluggable authentication schemes.

```text
OAUTH2
OAUTH2_PKCE
OIDC
API_KEY
BEARER_TOKEN
JWT
CLIENT_CREDENTIALS
SERVICE_ACCOUNT
HMAC
MTLS
BASIC_AUTH
SIGNED_REQUEST
```

---

## SR-004 — Multi-Tenant Authentication Isolation

Authentication contexts shall be isolated by:

```text
tenant_id
integration_id
account_id
credential_id
environment
```

A credential belonging to one tenant shall never be accessible by another tenant.

---

## SR-005 — Secure Credential Vault

All secrets shall be stored using a dedicated secret-management mechanism.

Database records shall contain references rather than raw credentials.

---

## SR-006 — Encryption at Rest

Credential material shall be encrypted at rest using enterprise-grade cryptography.

---

## SR-007 — Encryption in Transit

All authentication traffic shall use TLS.

---

## SR-008 — Token Encryption

Access and refresh tokens shall be encrypted before persistent storage.

---

## SR-009 — Secret Access Control

Secret retrieval shall require:

```text
Authenticated Service Identity
+
Tenant Context
+
Integration Context
+
Capability Authorization
+
Policy Validation
```

---

## SR-010 — Secret Access Minimization

The platform shall retrieve secrets only at the point of execution.

Secrets shall not be unnecessarily propagated through:

```text
Frontend
Logs
Events
Queues
AI Context
MCP Responses
Workflow Payloads
Analytics
```

---

## SR-011 — OAuth PKCE

OAuth authorization-code integrations shall support PKCE wherever supported.

The system shall generate cryptographically secure:

```text
code_verifier
code_challenge
state
nonce
```

where applicable.

---

## SR-012 — OAuth State Validation

The system shall validate OAuth `state` values to prevent CSRF and authorization-response injection.

---

## SR-013 — OIDC Nonce Validation

OIDC authentication flows shall validate nonce values.

---

## SR-014 — Redirect URI Validation

Redirect URIs shall be registered and allowlisted.

Dynamic arbitrary redirect URIs shall be rejected.

---

## SR-015 — OAuth Scope Validation

The system shall validate:

```text
Requested Scopes
Granted Scopes
Required Scopes
Policy-Allowed Scopes
```

---

## SR-016 — Token Endpoint Validation

The platform shall validate configured OAuth endpoints and prevent unsafe endpoint configuration.

---

## SR-017 — SSRF Protection

Integration authentication configuration shall prevent SSRF attacks.

Outbound requests shall enforce:

```text
Allowed Schemes
Allowed Hosts
DNS Validation
Private IP Blocking
Redirect Validation
Port Restrictions
```

unless explicitly approved for enterprise private-network integrations.

---

## SR-018 — Token Refresh

The system shall automatically refresh tokens when supported.

Refresh operations shall be:

```text
Encrypted
Idempotent
Concurrency-safe
Audited
```

---

## SR-019 — Refresh Token Rotation

If a provider rotates refresh tokens, SalesGenie shall atomically replace the stored refresh token.

---

## SR-020 — Refresh Token Race Prevention

Concurrent workers shall not overwrite newer refresh tokens with stale values.

The system shall use:

```text
Distributed Lock
OR
Optimistic Versioning
OR
Atomic Compare-and-Swap
```

---

## SR-021 — Token Expiration Tracking

The system shall store token metadata:

```text
issued_at
expires_at
last_refreshed_at
credential_version
provider
scope_hash
```

Raw tokens shall not be exposed.

---

## SR-022 — Token Revocation

The system shall support provider-side token revocation where available.

---

## SR-023 — Credential Versioning

Credentials shall be versioned.

```text
Credential v1
Credential v2
Credential v3
```

Only approved versions shall be active.

---

## SR-024 — Zero-Downtime Rotation

Credential rotation shall support overlapping credential validity where supported.

```text
OLD CREDENTIAL
       +
NEW CREDENTIAL
       ↓
Validation
       ↓
Switch
       ↓
Drain
       ↓
Revoke OLD
```

---

## SR-025 — Authentication State Machine

Authentication shall use explicit states:

```text
NOT_CONNECTED
AUTHORIZATION_PENDING
AUTHENTICATING
AUTHENTICATED
TOKEN_REFRESHING
AUTHENTICATION_REQUIRED
AUTHENTICATION_FAILED
REVOKED
COMPROMISED
DISABLED
```

---

## SR-026 — Authentication State Transitions

Invalid transitions shall be rejected.

Example:

```text
REVOKED → AUTHENTICATED
```

shall require a new authentication process.

---

## SR-027 — Authentication Health

The system shall periodically validate authentication health without executing destructive actions.

---

## SR-028 — Authentication Policy Engine

Authentication requests shall pass through policy evaluation.

Policy inputs shall include:

```text
Tenant
User
Role
Agent
Workflow
Integration
Requested Scope
Environment
Risk
Provider
Action
```

---

## SR-029 — Risk Classification

Authentication operations shall be classified:

```text
LOW
MEDIUM
HIGH
CRITICAL
```

Examples:

```text
Read-only CRM → LOW
Create CRM record → MEDIUM
Send email → HIGH
Delete financial record → CRITICAL
```

---

## SR-030 — Human Approval Policy

The system shall support:

```text
AUTO_APPROVE
APPROVAL_REQUIRED
MULTI_APPROVAL
DENY
```

---

## SR-031 — Authentication Event Bus

Authentication events shall be published through the event-driven architecture.

Events shall include:

```text
integration.auth.started
integration.auth.completed
integration.auth.failed
integration.auth.expired
integration.auth.refresh.started
integration.auth.refresh.completed
integration.auth.refresh.failed
integration.auth.revoked
integration.auth.reauthorized
integration.auth.credential_rotated
integration.auth.scope_changed
```

---

## SR-032 — Authentication Idempotency

Authentication-related APIs shall support idempotency where appropriate.

---

## SR-033 — Authentication Concurrency

Concurrent authentication requests for the same account shall be coordinated.

The platform shall prevent duplicate token exchanges when unnecessary.

---

## SR-034 — Authentication Session Binding

OAuth sessions shall be bound to:

```text
tenant
user
integration
browser/session context
state
```

---

## SR-035 — Authentication Timeout

Pending authentication requests shall expire after configurable periods.

---

## SR-036 — Authentication Replay Protection

Authorization responses and sensitive authentication requests shall be protected against replay.

---

## SR-037 — MFA Awareness

The platform shall support providers that require MFA.

SalesGenie shall not attempt to bypass provider MFA.

---

## SR-038 — Enterprise SSO Awareness

The integration authentication subsystem shall support providers using:

```text
SAML
OIDC
Enterprise SSO
Identity Federation
```

where applicable.

---

## SR-039 — Authentication Policy Inheritance

Policies shall support:

```text
Platform
   ↓
Organization
   ↓
Team
   ↓
User
   ↓
AI Agent
   ↓
Workflow
```

More restrictive policies shall override less restrictive policies.

---

## SR-040 — Authentication Audit

Every sensitive authentication operation shall generate an immutable audit event.

---

## 7. Functional Requirements

## FR-001 — Register Authentication Provider

Authorized administrators shall be able to register an authentication provider.

---

## FR-002 — Configure OAuth Provider

The system shall support configuration of:

```text
Client ID
Client Secret Reference
Authorization Endpoint
Token Endpoint
Revocation Endpoint
Scopes
Redirect URI
PKCE
OIDC
```

Client secrets shall be stored only in the secure vault.

---

## FR-003 — Initiate OAuth Flow

The platform shall generate a secure authorization request.

It shall include applicable:

```text
client_id
redirect_uri
response_type
scope
state
code_challenge
code_challenge_method
nonce
```

---

## FR-004 — Validate OAuth Callback

The callback handler shall validate:

1. State.
2. Authorization code.
3. Tenant context.
4. User context.
5. Integration context.
6. Redirect URI.
7. PKCE verifier where applicable.
8. Provider response.
9. Error response.

---

## FR-005 — Exchange Authorization Code

The backend shall exchange the authorization code for tokens.

Token responses shall never be returned to the browser unless explicitly required by a secure provider architecture.

---

## FR-006 — Store Tokens

The authentication service shall:

1. Encrypt tokens.
2. Store them in the credential vault.
3. Store metadata separately.
4. Return only connection status.

---

## FR-007 — Validate Granted Scopes

The system shall compare provider-granted scopes against required scopes.

Insufficient scopes shall produce:

```text
AUTHENTICATION_INCOMPLETE
```

rather than silently granting functionality.

---

## FR-008 — API Key Registration

The platform shall allow users to securely register API keys.

---

## FR-009 — API Key Validation

The system shall perform a safe provider validation request where available.

---

## FR-010 — Service Account Registration

The platform shall support secure service-account credential registration.

---

## FR-011 — Client Credentials Flow

The platform shall implement secure client-credentials token acquisition.

---

## FR-012 — Bearer Token Configuration

The platform shall securely store and retrieve bearer tokens.

---

## FR-013 — JWT Generation

Where required, the platform shall generate signed JWT assertions using securely stored private keys.

---

## FR-014 — JWT Validation

External JWTs shall be validated for:

```text
Signature
Issuer
Audience
Expiration
Not-Before
Algorithm
Key ID
```

---

## FR-015 — HMAC Signing

The integration gateway shall sign requests using configured HMAC algorithms.

---

## FR-016 — mTLS

The integration gateway shall support client certificates and private keys stored in the secure credential system.

---

## FR-017 — Automatic Token Refresh

Before an authenticated integration operation:

```text
Check Token
      ↓
Expired/Near Expiration?
      ↓
YES
      ↓
Acquire Lock
      ↓
Refresh
      ↓
Store New Token
      ↓
Execute Request
```

---

## FR-018 — Refresh Failure Handling

If token refresh fails:

```text
Retry according to policy
        ↓
If still failed
        ↓
AUTHENTICATION_REQUIRED
        ↓
Pause dependent workflows
        ↓
Notify authorized user
```

---

## FR-019 — Credential Rotation

The system shall support automated and manual credential rotation.

---

## FR-020 — Credential Revocation

The system shall revoke credentials locally and provider-side where supported.

---

## FR-021 — Emergency Revocation

Super Admins shall be able to immediately revoke credentials associated with a security incident.

---

## FR-022 — Scope Upgrade

When an integration requires additional scopes:

```text
Detect Missing Scope
        ↓
Explain Requirement
        ↓
Policy Evaluation
        ↓
Human Approval if Required
        ↓
Reauthorization
        ↓
Validate
        ↓
Update Authentication Context
```

---

## FR-023 — Scope Downgrade

Administrators shall be able to reduce scopes where supported.

---

## FR-024 — Authentication Test

The system shall expose:

```text
POST /api/v1/integrations/{id}/authentication/test
```

The endpoint shall validate authentication without exposing secrets.

---

## FR-025 — Authentication Status API

The platform shall expose:

```text
GET /api/v1/integrations/{id}/authentication/status
```

The response shall contain safe metadata only.

---

## FR-026 — Reauthorization API

The platform shall expose:

```text
POST /api/v1/integrations/{id}/authentication/reauthorize
```

---

## FR-027 — Revocation API

The platform shall expose:

```text
POST /api/v1/integrations/{id}/authentication/revoke
```

---

## FR-028 — Credential Rotation API

The platform shall expose:

```text
POST /api/v1/integrations/{id}/authentication/rotate
```

---

## FR-029 — Authentication Requirements API

AI agents and workflows shall be able to query:

```text
GET /api/v1/integrations/{id}/authentication/requirements
```

Response:

```text
authentication_method
required_scopes
approval_required
authentication_status
required_user_action
```

---

## FR-030 — AI Authentication Request

AI agents shall submit:

```text
POST /api/v1/integrations/{id}/authentication/request
```

The request shall include:

```text
agent_id
workflow_id
reason
required_scopes
required_capabilities
risk_level
```

---

## FR-031 — Human Authentication Approval

Users shall be able to approve or reject authentication requests.

---

## FR-032 — Authentication Request Expiration

Authentication requests shall automatically expire.

---

## FR-033 — Authentication Request Audit

The platform shall audit:

```text
Requested By
Approved By
Rejected By
Scopes
Integration
Agent
Workflow
Timestamp
Decision
Reason
```

---

## FR-034 — Workflow Authentication Pause

If a workflow requires authentication:

```text
Workflow
   ↓
Authentication Missing
   ↓
Pause
   ↓
Create Authentication Request
   ↓
Notify User
   ↓
User Authenticates
   ↓
Validate
   ↓
Resume Workflow
```

---

## FR-035 — Workflow Authentication Resume

Successful authentication shall resume eligible workflows without requiring the entire workflow to restart.

---

## FR-036 — AI Authentication Resume

After successful authentication, AI agents shall retry the previously blocked operation according to policy.

---

## FR-037 — MCP Authentication

MCP tools shall expose authentication status without exposing credential material.

Example:

```text
get_integration_auth_status
get_auth_requirements
request_authentication
request_reauthorization
request_credential_rotation
```

Privileged authentication operations shall require policy validation.

---

## FR-038 — n8n Authentication

n8n workflows shall use SalesGenie's authentication abstraction rather than directly storing unrestricted platform credentials where centralized credential management is required.

---

## FR-039 — Authentication Webhooks

The system shall emit authentication lifecycle events for downstream services.

---

## FR-040 — Authentication Notifications

The notification service shall support:

```text
Email
In-App
Slack
Teams
Webhook
```

for authentication events according to tenant policy.

---

## 8. Human Authentication Workflow

```text
Organization Admin
        ↓
Integration Dashboard
        ↓
Select Salesforce
        ↓
Click "Connect"
        ↓
Authentication Requirements
        ↓
Review Requested Scopes
        ↓
Click "Authorize"
        ↓
Salesforce OAuth
        ↓
User Consent
        ↓
Authorization Code
        ↓
SalesGenie Backend
        ↓
Token Exchange
        ↓
Secure Credential Vault
        ↓
Scope Validation
        ↓
Connection Test
        ↓
Authentication = CONNECTED
        ↓
Audit Event
```

---

## 9. Human API-Key Workflow

```text
Admin
 ↓
Select Integration
 ↓
Authentication Method:
API Key
 ↓
Enter API Key
 ↓
Submit
 ↓
TLS
 ↓
Backend Authentication Service
 ↓
Credential Vault
 ↓
Validation Request
 ↓
Success
 ↓
Authentication = CONNECTED
```

---

## 10. AI Authentication Workflow

```text
User
 ↓
"Find my Salesforce leads."
 ↓
AI Sales Agent
 ↓
Capability Discovery
 ↓
Salesforce.search_leads
 ↓
Authentication Check
 ↓
NOT_AUTHENTICATED
 ↓
Policy Evaluation
 ↓
Authentication Request
 ↓
User Notification
 ↓
User Authorizes Salesforce
 ↓
OAuth Callback
 ↓
Token Exchange
 ↓
Secure Vault
 ↓
Authentication Validation
 ↓
AI Agent Receives:
"Salesforce search_leads = AVAILABLE"
 ↓
AI Executes Search
 ↓
Result Returned
```

---

## 11. AI High-Risk Authentication Workflow

```text
AI Agent
 ↓
Requires:
Salesforce.delete_lead
 ↓
Authentication Requirement
 ↓
Risk = CRITICAL
 ↓
Policy Engine
 ↓
Human Approval Required
 ↓
Approval Request
 ↓
Human Reviews
 ↓
Approve?
 ├── NO → BLOCK
 └── YES
       ↓
OAuth / Credential Authorization
       ↓
Validate
       ↓
Execute
       ↓
Audit
```

---

## 12. Token Refresh Workflow

```text
Integration Request
        ↓
Authentication Service
        ↓
Check Access Token
        ↓
Valid?
 ├── YES → Execute
 └── NO
       ↓
Check Refresh Token
       ↓
Acquire Distributed Lock
       ↓
Refresh Token
       ↓
Validate Response
       ↓
Atomically Store New Token
       ↓
Release Lock
       ↓
Execute Request
```

---

## 13. Refresh Failure Workflow

```text
API Request
 ↓
Access Token Expired
 ↓
Refresh
 ↓
Provider Rejects Refresh
 ↓
Retry Policy
 ↓
Still Failed
 ↓
Authentication = AUTHENTICATION_REQUIRED
 ↓
Dependent Workflows Paused
 ↓
AI Agent Notified
 ↓
User Notified
 ↓
Reauthorization
 ↓
Validation
 ↓
Workflow Resume
```

---

## 14. Credential Rotation Workflow

```text
Rotation Requested
        ↓
Policy Evaluation
        ↓
Approval?
        ↓
Generate / Register New Credential
        ↓
Validate New Credential
        ↓
Activate New Credential
        ↓
Switch Traffic
        ↓
Monitor
        ↓
Drain Old Credential
        ↓
Revoke Old Credential
        ↓
Audit
```

---

## 15. Authentication Security Requirements

The system shall:

1. Never store plaintext production credentials.
2. Never expose tokens to frontend JavaScript unnecessarily.
3. Never place credentials in AI prompts.
4. Never place credentials in LLM context.
5. Never include credentials in MCP responses.
6. Never include credentials in workflow payloads unless strictly required and securely isolated.
7. Never log secrets.
8. Never store secrets in analytics.
9. Never expose credentials through error messages.
10. Never send secrets through ordinary event streams.
11. Enforce TLS.
12. Enforce tenant isolation.
13. Enforce least privilege.
14. Validate OAuth state.
15. Validate PKCE.
16. Validate redirect URIs.
17. Prevent SSRF.
18. Prevent replay attacks.
19. Support credential revocation.
20. Support credential rotation.

---

## 16. Secret Redaction Requirements

The following shall always be redacted:

```text
Authorization: Bearer <TOKEN>
X-API-Key: <KEY>
client_secret=<SECRET>
refresh_token=<TOKEN>
access_token=<TOKEN>
password=<PASSWORD>
private_key=<KEY>
certificate_private_key=<KEY>
```

Example:

```text
Authorization: Bearer [REDACTED]
```

---

## 17. Authentication Threat Model

The system shall defend against:

```text
OAuth CSRF
OAuth Authorization Code Injection
Token Theft
Refresh Token Theft
Credential Leakage
Credential Replay
SSRF
Phishing
Session Hijacking
Redirect URI Manipulation
Scope Escalation
Privilege Escalation
AI Prompt Injection
AI Tool Abuse
MCP Tool Abuse
Workflow Credential Leakage
Insider Threats
Cross-Tenant Credential Access
Credential Stuffing
Brute Force
Replay Attacks
Man-in-the-Middle Attacks
Token Substitution
```

---

## 18. AI Security Model

AI authentication requests shall follow:

```text
AI Intent
    ↓
Capability Resolution
    ↓
Authentication Requirement
    ↓
Scope Minimization
    ↓
Risk Assessment
    ↓
Policy Engine
    ↓
Human Approval?
    ↓
Authentication Flow
    ↓
Credential Vault
    ↓
Authentication Result
    ↓
AI Capability Grant
```

The AI shall receive only:

```text
AVAILABLE
NOT_AVAILABLE
AUTHENTICATION_REQUIRED
APPROVAL_REQUIRED
DENIED
```

and safe diagnostic metadata.

---

## 19. Authentication Policy Examples

## Policy A — Read-Only CRM

```text
Integration:
CRM

Action:
READ

AI:
ALLOW

Human:
ALLOW

Approval:
NONE
```

## Policy B — Send Email

```text
Integration:
Gmail

Action:
SEND_EMAIL

AI:
REQUEST_ONLY

Human:
ALLOW

Approval:
REQUIRED
```

## Policy C — Financial System

```text
Integration:
Financial System

Action:
WRITE

AI:
DENY

Human:
ALLOW

Approval:
MULTI_APPROVER
```

---

## 20. Authentication API

Recommended API surface:

```text
GET    /api/v1/integrations/{id}/authentication
GET    /api/v1/integrations/{id}/authentication/status
GET    /api/v1/integrations/{id}/authentication/requirements

POST   /api/v1/integrations/{id}/authentication/start
POST   /api/v1/integrations/{id}/authentication/callback
POST   /api/v1/integrations/{id}/authentication/test
POST   /api/v1/integrations/{id}/authentication/refresh
POST   /api/v1/integrations/{id}/authentication/reauthorize
POST   /api/v1/integrations/{id}/authentication/revoke
POST   /api/v1/integrations/{id}/authentication/rotate

POST   /api/v1/integrations/{id}/authentication/request

GET    /api/v1/authentication/requests
POST   /api/v1/authentication/requests/{id}/approve
POST   /api/v1/authentication/requests/{id}/deny
```

---

## 21. Authentication Data Model

## Authentication Context

```text
AuthenticationContext
├── id
├── tenant_id
├── integration_id
├── provider_id
├── account_id
├── authentication_method
├── credential_reference
├── credential_version
├── granted_scopes
├── required_scopes
├── status
├── expires_at
├── last_authenticated_at
├── last_refreshed_at
├── last_validated_at
├── created_by
├── created_at
└── updated_at
```

---

## 22. Authentication Request Model

```text
AuthenticationRequest
├── id
├── tenant_id
├── integration_id
├── requester_type
├── requester_id
├── agent_id
├── workflow_id
├── required_scopes
├── requested_capabilities
├── reason
├── risk_level
├── approval_policy
├── status
├── approved_by
├── expires_at
├── created_at
└── resolved_at
```

---

## 23. Credential Metadata Model

```text
CredentialMetadata
├── id
├── tenant_id
├── integration_id
├── credential_reference
├── credential_type
├── version
├── status
├── issued_at
├── expires_at
├── rotated_at
├── revoked_at
├── created_by
└── created_at
```

---

## 24. Authentication Events

The platform shall emit structured events.

```text
integration.authentication.started
integration.authentication.pending
integration.authentication.completed
integration.authentication.failed
integration.authentication.expired
integration.authentication.refresh.started
integration.authentication.refresh.completed
integration.authentication.refresh.failed
integration.authentication.reauthorized
integration.authentication.revoked
integration.authentication.compromised
integration.authentication.credential_rotated
integration.authentication.scope_added
integration.authentication.scope_removed
```

---

## 25. Observability

Each authentication request shall include:

```text
request_id
trace_id
correlation_id
tenant_id
user_id
agent_id
workflow_id
integration_id
provider_id
authentication_method
operation
timestamp
```

Metrics shall include:

```text
authentication_attempts_total
authentication_success_total
authentication_failures_total
oauth_callback_failures_total
token_refresh_total
token_refresh_failures_total
credential_rotation_total
credential_revocation_total
authentication_latency
authentication_expiration_total
scope_upgrade_total
authentication_approval_total
authentication_denial_total
```

---

## 26. Performance Requirements

For internal authentication-management operations:

```text
P50 < 100 ms
P95 < 300 ms
P99 < 1 second
```

excluding external provider network latency.

OAuth flows shall be asynchronous from the perspective of long-running browser interactions.

---

## 27. Reliability Requirements

Authentication operations shall be:

```text
Idempotent
Retryable
Auditable
Observable
Recoverable
Concurrency-safe
```

Transient failures shall use exponential backoff with jitter.

---

## 28. Availability Requirements

The authentication service shall target:

```text
99.99% availability
```

Authentication failure for one provider shall not affect unrelated integrations.

Example:

```text
Salesforce outage
        ↓
Salesforce authentication unavailable

Gmail
Slack
HubSpot
Notion
        ↓
Remain operational
```

---

## 29. Disaster Recovery

The authentication subsystem shall support:

* Encrypted credential backups where permitted.
* Metadata backups.
* Credential-version recovery.
* Provider reauthorization.
* Service failover.
* Recovery from vault outages.
* Recovery from database failure.

Raw secrets shall not be copied into ordinary backup systems unless explicitly protected by the organization's secret-management architecture.

---

## 30. Authentication Dependency Architecture

```text
                    ┌─────────────────────┐
                    │   SalesGenie UI     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ API Gateway / BFF    │
                    └──────────┬──────────┘
                               │
                               ▼
                 ┌──────────────────────────┐
                 │ Integration Auth Service  │
                 └───────────┬──────────────┘
                             │
             ┌───────────────┼────────────────┐
             ▼               ▼                ▼
      Policy Engine     Credential Vault   Provider APIs
             │
             ▼
      Approval Service
             │
             ▼
        Audit Service
```

---

## 31. Integration Authentication with AI

```text
AI Agent
   ↓
Needs External Capability
   ↓
Authentication Status
   ↓
Authenticated?
 ├── YES
 │    ↓
 │  Execute
 │
 └── NO
      ↓
Authentication Requirement
      ↓
Scope Calculation
      ↓
Policy Engine
      ↓
Approval Required?
 ├── NO
 │    ↓
 │  Start Auth Flow
 │
 └── YES
      ↓
Human Approval
      ↓
Start Auth Flow
      ↓
Provider
      ↓
Token Exchange
      ↓
Credential Vault
      ↓
Validate
      ↓
Grant Capability
      ↓
AI Executes
```

---

## 32. Integration Authentication with MCP

MCP authentication tools shall follow:

```text
MCP Client
    ↓
AI Agent
    ↓
MCP Authentication Tool
    ↓
MCP Gateway
    ↓
SalesGenie Authorization
    ↓
Integration Authentication Service
    ↓
Policy Engine
    ↓
Authentication State
```

MCP responses shall contain only safe authentication metadata.

---

## 33. Integration Authentication with n8n

```text
n8n Workflow
      ↓
SalesGenie Integration
      ↓
Authentication Status
      ↓
Authenticated?
 ├── YES → Execute
 └── NO
      ↓
Pause Workflow
      ↓
Authentication Request
      ↓
Human Authorization
      ↓
Credential Vault
      ↓
Authentication Success
      ↓
Resume Workflow
```

---

## 34. Authentication Governance

Every production authentication configuration shall define:

```text
Owner
Tenant
Provider
Authentication Method
Credential Type
Scopes
Risk Level
Approval Policy
Expiration Policy
Rotation Policy
Revocation Policy
Environment
Audit Policy
```

---

## 35. Authentication Lifecycle

```text
DISCOVERED
    ↓
CONFIGURED
    ↓
AUTHORIZATION_PENDING
    ↓
AUTHENTICATING
    ↓
AUTHENTICATED
    ↓
ACTIVE
    ↓
TOKEN_REFRESH_REQUIRED
    ↓
REFRESHING
    ↓
ACTIVE
    ↓
AUTHENTICATION_REQUIRED
    ↓
REAUTHENTICATING
    ↓
ACTIVE
    ↓
REVOKED / COMPROMISED / DISABLED
```

---

## 36. Acceptance Criteria

The Integration Authentication subsystem shall be production-ready when:

* OAuth 2.x is supported.
* PKCE is supported.
* OIDC is supported where applicable.
* API keys are securely supported.
* Bearer tokens are securely supported.
* Client credentials are supported.
* Service accounts are supported.
* JWT authentication is supported.
* HMAC authentication is supported.
* mTLS is supported where required.
* Tokens are securely stored.
* Credentials are never exposed to AI agents.
* Credentials are never stored in plaintext.
* Tenant isolation is enforced.
* OAuth state validation is implemented.
* Redirect URI validation is implemented.
* PKCE validation is implemented.
* Scope validation is implemented.
* Token refresh is automated.
* Refresh-token races are prevented.
* Credential rotation is supported.
* Credential revocation is supported.
* Authentication expiration is detected.
* Authentication failures are observable.
* Authentication recovery is supported.
* High-risk authentication requests require approval.
* AI agents cannot self-authorize.
* AI agents cannot access raw credentials.
* Workflow execution can pause for authentication.
* Workflow execution can resume after authentication.
* MCP authentication is policy-controlled.
* n8n authentication is policy-controlled.
* Authentication events are auditable.
* Secrets are automatically redacted.
* SSRF protections are implemented.
* Replay protection is implemented.
* Authentication sessions expire.
* Multiple external accounts are supported.
* Authentication health is monitored.
* Provider failures are isolated.
* Authentication service is horizontally scalable.
* Authentication APIs are idempotent.
* Authentication state transitions are validated.
* Production credentials are separated from development credentials.
* Emergency credential revocation is available.

---

## 37. FAANG-Level Design Principles

## Principle 1 — Never Give the AI the Key

AI agents receive capabilities, not credentials.

```text
WRONG:

AI → Access Token → Provider

CORRECT:

AI → Capability Request
       ↓
Policy
       ↓
Integration Gateway
       ↓
Credential Vault
       ↓
Provider
```

---

## Principle 2 — Authentication Is Separate from Authorization

Authentication answers:

```text
"Who/what is connected?"
```

Authorization answers:

```text
"What may they do?"
```

SalesGenie shall keep these concerns logically separated.

---

## Principle 3 — Authentication Is a Control Plane

Authentication shall be centrally managed rather than independently implemented by every microservice.

---

## Principle 4 — Least Privilege

Only the minimum scopes required by the requested operation shall be granted.

---

## Principle 5 — Zero Trust

Every authentication-dependent request shall be validated.

---

## Principle 6 — Human-in-the-Loop for High Risk

AI agents may request privileged authentication but shall not independently authorize themselves.

---

## Principle 7 — Secrets Never Enter AI Context

Credentials shall remain outside:

```text
LLM Prompt
Conversation History
Agent Memory
RAG Documents
MCP Response
Workflow Logs
Analytics
```

---

## Principle 8 — Secure by Default

New authentication contexts shall start in:

```text
NOT_CONNECTED
```

and become active only after successful authentication and policy validation.

---

## Principle 9 — Observable Authentication

Every sensitive authentication transition shall be measurable and auditable.

---

## Principle 10 — Fail Closed

If authentication state is uncertain:

```text
DENY ACCESS
```

rather than assuming authentication succeeded.

---

## 38. Definition of Done

```text
✓ Centralized Authentication Service
✓ Authentication Provider Registry
✓ OAuth 2.x
✓ OAuth PKCE
✓ OpenID Connect
✓ API Keys
✓ Bearer Tokens
✓ Client Credentials
✓ Service Accounts
✓ JWT
✓ HMAC
✓ mTLS
✓ Secure Credential Vault
✓ Token Encryption
✓ Token Refresh
✓ Refresh Token Rotation
✓ Credential Versioning
✓ Credential Rotation
✓ Credential Revocation
✓ OAuth State Validation
✓ PKCE Validation
✓ Redirect URI Validation
✓ Scope Management
✓ Scope Minimization
✓ Authentication State Machine
✓ Authentication Health
✓ Authentication Policies
✓ RBAC
✓ ABAC
✓ Human Approval
✓ AI Authentication Requests
✓ AI Credential Isolation
✓ Workflow Authentication Pause
✓ Workflow Authentication Resume
✓ MCP Authentication
✓ n8n Authentication
✓ Authentication Audit
✓ Authentication Metrics
✓ Distributed Tracing
✓ Secret Redaction
✓ SSRF Protection
✓ Replay Protection
✓ Multi-Tenant Isolation
✓ Multiple Provider Accounts
✓ Multiple Environments
✓ Emergency Revocation
✓ Failure Recovery
✓ Horizontal Scalability
✓ High Availability
✓ Disaster Recovery
```

---

## 39. Core Architectural Principle

> **SalesGenie shall treat integration authentication as a centralized, zero-trust security boundary. Humans and AI agents may request authentication, reauthorization, or credential changes, but they shall never directly handle production secrets. The Integration Authentication Service, Policy Engine, Credential Vault, and Integration Gateway shall collectively enforce identity, scope, credential lifecycle, tenant isolation, risk controls, and auditability before any external integration is accessed.**
