# SalesGenie — Integration OAuth Requirements

**Document:** `integration_oauth.md`  
**Product:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Requirement Level:** FAANG-Level / Production-Grade  
**Scope:** OAuth 2.0 / OAuth 2.1 / OpenID Connect Integration Framework  
**Actors:** Human Users, AI Agents, Workflows, MCP Clients, n8n, Microservices, Organization Admins, Super Admins  
**Architecture:** Multi-Tenant Microservices + Multi-Agent AI + Event-Driven + MCP + n8n + RAG  
**Target Scale:** 10M+ Users / 500K Concurrent Conversations

---

## 1. Purpose

The SalesGenie OAuth subsystem shall provide a secure, scalable, provider-agnostic OAuth authorization framework for connecting SalesGenie with external applications and enterprise services.

The subsystem shall support:

- Human-initiated OAuth.
- AI-initiated authentication requests.
- Workflow-initiated OAuth requirements.
- OAuth 2.0.
- OAuth 2.1-compatible security practices.
- OpenID Connect where applicable.
- Authorization Code Flow.
- PKCE.
- Refresh Tokens.
- Token Rotation.
- Token Revocation.
- Incremental Authorization.
- Scope Management.
- Consent Management.
- Multi-account connections.
- Multi-tenant isolation.
- Provider-specific OAuth adapters.
- OAuth authentication for MCP tools.
- OAuth authentication for n8n workflows.
- OAuth-aware AI agents.
- OAuth security monitoring.
- OAuth auditability.

---

## 2. OAuth Design Goals

SalesGenie OAuth shall follow:

```text
Least Privilege
Zero Trust
Defense in Depth
Secure by Default
Tenant Isolation
Credential Isolation
Explicit Consent
Human Oversight
AI Capability Isolation
Strong Cryptography
Provider Independence
Idempotency
Observability
Auditability
High Availability
Horizontal Scalability
```

---

## 3. Supported OAuth Capabilities

The platform shall support:

```text
OAuth 2.0 Authorization Code
OAuth 2.0 Authorization Code + PKCE
OAuth 2.1 Security Model
OpenID Connect
Refresh Tokens
Refresh Token Rotation
Token Revocation
Incremental Authorization
Dynamic Scope Requests
Multiple OAuth Accounts
Multiple Providers
Provider-Specific Parameters
Provider-Specific Scopes
Client Credentials
Device Authorization where supported
Token Introspection where supported
JWT Client Authentication where supported
Private Key JWT where supported
```

Implicit Grant shall not be used for newly implemented integrations.

Resource Owner Password Credentials shall not be implemented for new integrations.

---

## 4. OAuth Actors

## 4.1 Resource Owner

The human user who owns or controls the external account.

---

## 4.2 OAuth Client

SalesGenie or an approved SalesGenie integration component acting on behalf of a tenant.

---

## 4.3 Authorization Server

The external identity/provider authorization service.

Examples:

```text
Google
Microsoft
Salesforce
HubSpot
Slack
Notion
Zendesk
Atlassian
```

---

## 4.4 Resource Server

The external API that receives OAuth access tokens.

---

## 4.5 SalesGenie OAuth Service

Central service responsible for:

```text
OAuth Discovery
Authorization URL Generation
State Management
PKCE
Callback Processing
Code Exchange
Token Storage
Token Refresh
Token Revocation
Scope Validation
OAuth Session Management
OAuth Health
OAuth Audit
```

---

## 4.6 AI Agent

An AI worker that requests an OAuth-backed capability.

The AI agent shall never directly receive OAuth secrets.

---

## 4.7 Workflow Engine

The workflow execution system that may require OAuth-authenticated actions.

---

## 5. User Requirements

## UR-OAUTH-001 — Connect OAuth Integration

Authorized users shall be able to connect an OAuth-supported integration.

The experience shall be:

```text
Integration Catalog
        ↓
Select Provider
        ↓
Connect
        ↓
Review Permissions
        ↓
Authorize
        ↓
Provider Login
        ↓
Provider Consent
        ↓
Callback
        ↓
Token Exchange
        ↓
Validation
        ↓
Connected
```

---

## UR-OAUTH-002 — OAuth Provider Selection

Users shall be able to select from organization-approved OAuth providers.

---

## UR-OAUTH-003 — Permission Review

Before authorization, SalesGenie shall display:

```text
Provider
Requested Permissions
Reason for Each Permission
Data Access
Actions Enabled
Risk Level
Organization Policy
```

---

## UR-OAUTH-004 — Human Consent

Users shall explicitly consent to requested OAuth permissions through the provider's authorization interface.

SalesGenie shall never simulate provider consent.

---

## UR-OAUTH-005 — OAuth Account Selection

Users shall be able to select which external account should be connected when the provider supports multiple accounts.

Example:

```text
Google Workspace

sales@company.com
support@company.com
marketing@company.com
```

---

## UR-OAUTH-006 — Multiple Connections

Users shall be able to connect multiple accounts from the same OAuth provider.

---

## UR-OAUTH-007 — Connection Naming

Users shall be able to assign a friendly name to an OAuth connection.

Example:

```text
Salesforce — Production
Salesforce — Sandbox
Gmail — Sales Team
Google Drive — Marketing
```

---

## UR-OAUTH-008 — OAuth Status

Users shall see:

```text
NOT_CONNECTED
AUTHORIZATION_PENDING
CONNECTED
TOKEN_EXPIRING
REFRESHING
REAUTHENTICATION_REQUIRED
REVOKED
FAILED
DISABLED
COMPROMISED
```

---

## UR-OAUTH-009 — Token Expiration

Users shall be informed when OAuth credentials are approaching expiration.

---

## UR-OAUTH-010 — Automatic Refresh

Users shall not normally need to manually refresh OAuth access tokens.

SalesGenie shall refresh tokens automatically when supported.

---

## UR-OAUTH-011 — Reauthorization

Users shall be able to reauthorize a connection without recreating the integration.

---

## UR-OAUTH-012 — Incremental Authorization

Users shall be able to grant additional permissions only when a new feature requires them.

Example:

```text
Initial:

crm.contacts.read

Later:

crm.contacts.write
```

SalesGenie shall not request all possible scopes during initial authorization.

---

## UR-OAUTH-013 — Scope Visibility

Users shall be able to view currently granted scopes.

---

## UR-OAUTH-014 — Scope Changes

Users shall be informed whenever an OAuth operation requests permissions beyond the current authorization.

---

## UR-OAUTH-015 — Disconnect Integration

Users with sufficient permissions shall be able to disconnect an OAuth connection.

---

## UR-OAUTH-016 — Revoke Access

Users shall be able to initiate provider-side OAuth revocation where supported.

---

## UR-OAUTH-017 — OAuth Troubleshooting

The UI shall explain failures using safe, actionable messages.

Example:

```text
OAuth authorization failed.

Reason:
The provider denied the requested permission.

Action:
Review the requested permissions and try again.
```

Raw provider secrets shall never be displayed.

---

## UR-OAUTH-018 — OAuth Connection Test

Users shall be able to test whether an OAuth connection is still valid.

---

## UR-OAUTH-019 — OAuth Audit Visibility

Authorized administrators shall be able to view:

```text
Connected By
Connected At
Provider
Account
Granted Scopes
Last Refresh
Last Validation
Last Failure
Current Status
```

---

## UR-OAUTH-020 — OAuth Approval

Organizations shall be able to require administrator approval before an OAuth integration is connected.

---

## UR-OAUTH-021 — High-Risk OAuth Scope Approval

Organizations shall be able to require human approval for high-risk permissions.

Example:

```text
Email Read
→ LOW/MEDIUM

Email Send
→ HIGH

Email Delete
→ CRITICAL
```

---

## 6. AI User Requirements

## AI-UR-OAUTH-001 — AI Detects Missing OAuth

An AI agent shall detect when an OAuth-backed capability is unavailable because authentication has not been completed.

Example:

```text
User:
"Send this proposal to the customer."

AI:
Gmail.send_email required.

OAuth:
NOT_CONNECTED
```

---

## AI-UR-OAUTH-002 — AI Requests OAuth

The AI agent shall be able to create an OAuth authorization request.

```text
OAuthRequest
├── agent_id
├── tenant_id
├── workflow_id
├── integration_id
├── required_scopes
├── capability
├── business_reason
├── risk_level
└── approval_policy
```

---

## AI-UR-OAUTH-003 — AI Scope Minimization

The AI shall request only scopes required for the current operation.

Example:

```text
Task:
Read a customer's calendar.

Required:
calendar.read

Not required:
calendar.write
calendar.delete
```

---

## AI-UR-OAUTH-004 — AI OAuth Explanation

The AI shall explain:

```text
Why OAuth is required
Which provider is required
Which permissions are required
What data may be accessed
What action will be performed
Whether approval is required
```

---

## AI-UR-OAUTH-005 — AI Cannot Approve OAuth

AI agents shall never approve their own OAuth authorization request.

---

## AI-UR-OAUTH-006 — AI Cannot Generate Consent

AI agents shall never:

* Fake user consent.
* Simulate provider consent.
* Bypass provider login.
* Bypass MFA.
* Bypass administrator approval.
* Forge OAuth authorization codes.
* Modify OAuth scopes after approval.

---

## AI-UR-OAUTH-007 — AI OAuth Status

AI agents may query:

```text
oauth_status
required_scopes
granted_scopes
expires_at_status
reauthorization_required
```

without receiving raw OAuth tokens.

---

## AI-UR-OAUTH-008 — AI OAuth Recovery

If an access token expires:

```text
AI Agent
    ↓
OAuth Status
    ↓
Refresh Available?
 ├── YES → Refresh → Retry
 └── NO
       ↓
Reauthorization Required
       ↓
Human Notification
```

---

## AI-UR-OAUTH-009 — AI Credential Isolation

AI agents shall never receive:

```text
authorization_code
access_token
refresh_token
client_secret
private_key
client_assertion
```

unless a provider architecture explicitly requires a narrowly scoped non-secret identifier; secret material shall remain inside the OAuth infrastructure.

---

## AI-UR-OAUTH-010 — AI OAuth Escalation

The AI shall escalate to a human when:

```text
New Scope Required
High-Risk Permission
Provider Requires Interactive Login
Consent Required
OAuth Revoked
Refresh Token Invalid
Organization Policy Blocks Request
Security Risk Detected
```

---

## AI-UR-OAUTH-011 — AI OAuth Capability Model

The AI shall interact with OAuth through capabilities.

```text
AI
 ↓
Capability
 ↓
OAuth Policy
 ↓
OAuth Service
 ↓
Credential Vault
 ↓
Resource Server
```

The AI shall not interact directly with provider tokens.

---

## 7. System Requirements

## SR-OAUTH-001 — Central OAuth Service

SalesGenie shall implement a centralized OAuth Service.

Responsibilities:

```text
Provider Configuration
OAuth Discovery
Authorization Requests
OAuth Sessions
State Management
PKCE
Callback Validation
Token Exchange
Token Storage
Token Refresh
Token Revocation
Scope Management
Connection Health
Audit
```

---

## SR-OAUTH-002 — Multi-Tenant OAuth Isolation

Every OAuth connection shall be scoped to:

```text
tenant_id
integration_id
provider_id
account_id
credential_id
environment
```

Cross-tenant access shall be impossible through application-level authorization and data-layer isolation.

---

## SR-OAUTH-003 — OAuth Client Registration

The platform shall maintain provider client configuration:

```text
client_id
client_secret_reference
authorization_endpoint
token_endpoint
revocation_endpoint
introspection_endpoint
redirect_uri
allowed_scopes
pkce_required
client_auth_method
```

Secrets shall be stored in the credential vault.

---

## SR-OAUTH-004 — Provider Registry

Each OAuth provider shall have a registered configuration.

```text
OAuthProvider
├── provider_id
├── name
├── authorization_endpoint
├── token_endpoint
├── revocation_endpoint
├── introspection_endpoint
├── issuer
├── jwks_uri
├── scopes
├── pkce_support
├── refresh_token_support
├── token_rotation_support
├── client_auth_method
└── status
```

---

## SR-OAUTH-005 — Authorization Code Flow

The platform shall implement Authorization Code Flow.

---

## SR-OAUTH-006 — PKCE

PKCE shall be enabled for applicable OAuth authorization-code flows.

The platform shall generate a cryptographically secure:

```text
code_verifier
```

and derive:

```text
code_challenge
```

using an approved challenge method supported by the provider.

---

## SR-OAUTH-007 — OAuth State

Every browser-based OAuth authorization request shall include a cryptographically random state value.

The state shall be:

```text
Unpredictable
Single-use
Short-lived
Tenant-bound
User-bound
Integration-bound
```

---

## SR-OAUTH-008 — OAuth Callback Validation

The callback handler shall validate:

```text
state
authorization_code
tenant_context
user_context
integration_context
redirect_uri
PKCE_verifier
provider
```

---

## SR-OAUTH-009 — OAuth State Replay Prevention

A consumed OAuth state value shall never be accepted again.

---

## SR-OAUTH-010 — OAuth State Expiration

OAuth state values shall expire automatically.

---

## SR-OAUTH-011 — Redirect URI Allowlist

Only registered redirect URIs shall be accepted.

Arbitrary redirect URIs shall be rejected.

---

## SR-OAUTH-012 — Open Redirect Protection

The OAuth service shall prevent attacker-controlled redirect destinations.

---

## SR-OAUTH-013 — Authorization Endpoint Validation

The authorization endpoint shall be sourced from trusted provider configuration or validated discovery metadata.

---

## SR-OAUTH-014 — Token Endpoint Validation

Token requests shall be sent only to trusted provider endpoints.

---

## SR-OAUTH-015 — TLS

All OAuth communication shall use secure TLS connections.

---

## SR-OAUTH-016 — Token Encryption

Access tokens and refresh tokens shall be encrypted before persistent storage.

---

## SR-OAUTH-017 — Secret Vault

OAuth secrets shall be stored in a dedicated secret-management layer.

Database records shall contain:

```text
credential_reference
```

rather than plaintext secrets.

---

## SR-OAUTH-018 — Access Token Isolation

OAuth access tokens shall remain inside the integration execution boundary.

They shall not be passed into:

```text
LLM Context
AI Memory
RAG
MCP Output
Frontend State
Browser Local Storage
Analytics
Application Logs
```

---

## SR-OAUTH-019 — Refresh Token Protection

Refresh tokens shall receive stronger protection than ordinary OAuth metadata because they may enable long-lived access.

---

## SR-OAUTH-020 — Refresh Token Rotation

Where the provider rotates refresh tokens, SalesGenie shall atomically persist the newly issued token.

---

## SR-OAUTH-021 — Refresh Concurrency

Multiple concurrent requests for the same OAuth account shall not create token-refresh races.

The system shall use one of:

```text
Distributed Lock
Optimistic Concurrency
Atomic Compare-and-Swap
```

---

## SR-OAUTH-022 — Token Expiration

The system shall track:

```text
issued_at
expires_at
last_refresh_at
last_validation_at
credential_version
```

---

## SR-OAUTH-023 — Clock Skew

Token validation shall account for configurable clock skew.

---

## SR-OAUTH-024 — Token Refresh Threshold

The platform shall support proactive refresh before expiration.

Example:

```text
Token expires in:
< configurable threshold

Action:
Refresh
```

---

## SR-OAUTH-025 — Refresh Failure Classification

Refresh failures shall be classified:

```text
TRANSIENT
INVALID_REFRESH_TOKEN
REVOKED
INVALID_CLIENT
INSUFFICIENT_SCOPE
PROVIDER_ERROR
RATE_LIMITED
NETWORK_ERROR
UNKNOWN
```

---

## SR-OAUTH-026 — Automatic Retry

Transient OAuth failures shall use exponential backoff with jitter.

Permanent authorization failures shall not be retried indefinitely.

---

## SR-OAUTH-027 — Token Revocation

The system shall support RFC-compliant provider token revocation where supported.

---

## SR-OAUTH-028 — Token Introspection

The system shall support token introspection where the provider exposes it.

---

## SR-OAUTH-029 — OIDC Discovery

For OIDC providers, the system shall support trusted discovery metadata.

Relevant metadata may include:

```text
issuer
authorization_endpoint
token_endpoint
jwks_uri
userinfo_endpoint
revocation_endpoint
scopes_supported
response_types_supported
code_challenge_methods_supported
```

---

## SR-OAUTH-030 — OIDC Issuer Validation

OIDC ID tokens shall be validated against the configured issuer.

---

## SR-OAUTH-031 — OIDC Audience Validation

ID tokens shall validate:

```text
aud
```

against the expected OAuth client identifier.

---

## SR-OAUTH-032 — OIDC Nonce

OIDC authorization requests shall use nonce protection where required.

---

## SR-OAUTH-033 — OIDC Signature Validation

ID-token signatures shall be validated using trusted provider keys.

---

## SR-OAUTH-034 — Algorithm Restrictions

The platform shall maintain an allowlist of accepted signing algorithms.

Algorithm confusion shall be prevented.

---

## SR-OAUTH-035 — JWKS Key Rotation

The platform shall support provider JWKS key rotation.

Unknown key IDs may trigger safe metadata refresh subject to rate limits and validation.

---

## SR-OAUTH-036 — Scope Registry

The platform shall maintain:

```text
scope
description
risk_level
capabilities
provider
allowed_roles
approval_requirement
```

---

## SR-OAUTH-037 — Scope-to-Capability Mapping

OAuth scopes shall map to explicit SalesGenie capabilities.

Example:

```text
gmail.read
    ↓
gmail.search_messages

gmail.send
    ↓
gmail.send_message
```

---

## SR-OAUTH-038 — Scope Escalation Prevention

An AI agent or workflow shall not be able to silently convert:

```text
READ
```

into:

```text
WRITE
```

or:

```text
WRITE
```

into:

```text
DELETE
```

---

## SR-OAUTH-039 — Incremental Authorization

The OAuth service shall support incremental scope acquisition.

---

## SR-OAUTH-040 — Scope Downgrade

Administrators shall be able to reduce permitted scopes where the provider supports reauthorization.

---

## SR-OAUTH-041 — Tenant OAuth Policy

Organizations shall be able to configure:

```text
Allowed Providers
Blocked Providers
Allowed Scopes
Blocked Scopes
AI OAuth Policy
Human OAuth Policy
Approval Requirements
Token Lifetime Policy
Reauthorization Policy
```

---

## SR-OAUTH-042 — Environment Isolation

OAuth credentials shall be separated between:

```text
development
staging
production
sandbox
```

Production OAuth credentials shall never be used by development environments.

---

## SR-OAUTH-043 — Account Isolation

Each external account connection shall maintain an independent OAuth context.

---

## SR-OAUTH-044 — Credential Versioning

OAuth credentials shall support versioning.

```text
credential_v1
credential_v2
credential_v3
```

---

## SR-OAUTH-045 — Emergency Revocation

Administrators shall be able to immediately revoke a compromised OAuth connection.

---

## SR-OAUTH-046 — OAuth Security Events

The system shall publish:

```text
oauth.authorization.started
oauth.authorization.completed
oauth.authorization.failed
oauth.callback.rejected
oauth.token.issued
oauth.token.refreshed
oauth.token.refresh_failed
oauth.token.revoked
oauth.scope.changed
oauth.connection.created
oauth.connection.disabled
oauth.connection.compromised
oauth.reauthorization.required
```

---

## SR-OAUTH-047 — Auditability

Every privileged OAuth operation shall generate an immutable audit record.

---

## SR-OAUTH-048 — Observability

OAuth operations shall expose:

```text
metrics
logs
traces
audit_events
security_events
```

without exposing secrets.

---

## SR-OAUTH-049 — Correlation

Every OAuth transaction shall include:

```text
request_id
trace_id
correlation_id
oauth_transaction_id
tenant_id
integration_id
provider_id
```

---

## SR-OAUTH-050 — Secret Redaction

The following shall automatically be redacted:

```text
access_token
refresh_token
authorization_code
client_secret
client_assertion
private_key
Authorization headers
Cookie headers
```

---

## SR-OAUTH-051 — SSRF Protection

OAuth discovery and provider configuration shall prevent SSRF.

The platform shall validate:

```text
scheme
hostname
DNS resolution
IP address
redirect chain
port
certificate
```

---

## SR-OAUTH-052 — Private Network Protection

Requests to private or link-local addresses shall be blocked unless explicitly permitted by an enterprise private-integration policy.

---

## SR-OAUTH-053 — Rate Limiting

OAuth endpoints shall enforce rate limits for:

```text
authorization initiation
callback processing
token refresh
revocation
provider discovery
```

---

## SR-OAUTH-054 — Abuse Prevention

The system shall detect:

```text
OAuth authorization flooding
Callback replay
State guessing
Token refresh abuse
Scope escalation attempts
Provider abuse
```

---

## SR-OAUTH-055 — Idempotency

OAuth connection creation and related backend operations shall be idempotent where appropriate.

---

## SR-OAUTH-056 — Horizontal Scaling

The OAuth service shall support horizontal scaling.

OAuth state and transaction data shall not depend on process-local memory.

---

## 8. Functional Requirements

## FR-OAUTH-001 — Start OAuth Authorization

The platform shall provide:

```http
POST /api/v1/integrations/{integration_id}/oauth/authorize
```

The service shall return a short-lived authorization transaction and authorization URL.

---

## FR-OAUTH-002 — Generate Authorization URL

The service shall generate a provider-specific URL containing applicable parameters:

```text
client_id
redirect_uri
response_type=code
scope
state
code_challenge
code_challenge_method
nonce
```

---

## FR-OAUTH-003 — Create OAuth Transaction

Each authorization attempt shall create:

```text
OAuthTransaction
├── transaction_id
├── tenant_id
├── user_id
├── integration_id
├── provider_id
├── state_hash
├── pkce_verifier_reference
├── requested_scopes
├── redirect_uri
├── status
├── expires_at
├── created_at
└── consumed_at
```

Sensitive values shall be protected.

---

## FR-OAUTH-004 — Redirect User

SalesGenie shall redirect the user to the configured provider authorization endpoint.

---

## FR-OAUTH-005 — Receive Callback

The callback endpoint shall support:

```http
GET /api/v1/integrations/oauth/callback
```

---

## FR-OAUTH-006 — Validate Callback State

The system shall reject callbacks where:

```text
state missing
state invalid
state expired
state already consumed
tenant mismatch
user mismatch
integration mismatch
```

---

## FR-OAUTH-007 — Handle OAuth Error

The system shall correctly handle:

```text
access_denied
invalid_request
unauthorized_client
unsupported_response_type
invalid_scope
server_error
temporarily_unavailable
```

and provider-specific errors.

---

## FR-OAUTH-008 — Exchange Authorization Code

The backend shall exchange the authorization code for tokens using the configured token endpoint.

---

## FR-OAUTH-009 — Validate Token Response

The platform shall validate:

```text
token_type
access_token
expires_in
refresh_token
scope
id_token
```

where applicable.

---

## FR-OAUTH-010 — Validate Granted Scope

The system shall compare provider-granted scopes against requested and policy-approved scopes.

---

## FR-OAUTH-011 — Reject Insufficient Scope

If mandatory scopes are missing:

```text
OAuth Status:
INCOMPLETE
```

The system shall not falsely mark the integration as fully connected.

---

## FR-OAUTH-012 — Persist OAuth Connection

A successful connection shall create:

```text
OAuthConnection
```

containing safe metadata and a secure credential reference.

---

## FR-OAUTH-013 — Store Token Metadata

The system shall persist:

```text
token_type
expires_at
scope_hash
issued_at
credential_version
provider_account_id
```

without exposing the token.

---

## FR-OAUTH-014 — Identify External Account

Where provider APIs support it, SalesGenie shall identify the external account associated with the OAuth connection.

---

## FR-OAUTH-015 — Fetch User Identity

For OIDC or provider APIs that expose identity endpoints, SalesGenie may retrieve the minimum required identity attributes.

---

## FR-OAUTH-016 — Link OAuth Account

The system shall associate the external account with the correct:

```text
tenant
user
organization
integration
```

according to policy.

---

## FR-OAUTH-017 — Prevent Account Confusion

The system shall not automatically associate an OAuth account with another user or tenant based solely on an external email address.

---

## FR-OAUTH-018 — Token Refresh

The platform shall expose an internal token acquisition interface:

```text
get_valid_access_token(
    tenant_id,
    integration_id,
    account_id,
    capability
)
```

The returned access token shall remain within the trusted execution boundary.

---

## FR-OAUTH-019 — Proactive Refresh

The system shall refresh tokens before expiration when supported.

---

## FR-OAUTH-020 — Lazy Refresh

If a token expires unexpectedly, the integration gateway shall attempt refresh before returning an authentication failure.

---

## FR-OAUTH-021 — Concurrent Refresh Coordination

Only one refresh operation shall become authoritative for a credential version.

---

## FR-OAUTH-022 — Refresh Token Rotation

When a provider returns a new refresh token:

```text
Validate
 ↓
Encrypt
 ↓
Atomic Replace
 ↓
Invalidate Old Version
```

---

## FR-OAUTH-023 — Refresh Failure

If refresh fails permanently:

```text
OAuthConnection.status =
REAUTHENTICATION_REQUIRED
```

---

## FR-OAUTH-024 — Reauthorization

The platform shall allow:

```http
POST /api/v1/integrations/{integration_id}/oauth/reauthorize
```

---

## FR-OAUTH-025 — Disconnect

The platform shall allow:

```http
POST /api/v1/integrations/{integration_id}/oauth/disconnect
```

---

## FR-OAUTH-026 — Revoke

The platform shall allow:

```http
POST /api/v1/integrations/{integration_id}/oauth/revoke
```

where provider revocation is available.

---

## FR-OAUTH-027 — Incremental Scope Request

The platform shall allow:

```http
POST /api/v1/integrations/{integration_id}/oauth/scopes/request
```

---

## FR-OAUTH-028 — Scope Approval

A scope request shall pass through:

```text
Scope Request
    ↓
Risk Classification
    ↓
Tenant Policy
    ↓
Role Policy
    ↓
AI Policy
    ↓
Human Approval if Required
    ↓
OAuth Reauthorization
```

---

## FR-OAUTH-029 — OAuth Approval

Authorized administrators shall be able to approve or deny OAuth scope requests.

---

## FR-OAUTH-030 — OAuth Request Expiration

Pending OAuth approval requests shall expire automatically.

---

## FR-OAUTH-031 — OAuth Connection Health

The system shall expose:

```http
GET /api/v1/integrations/{integration_id}/oauth/health
```

---

## FR-OAUTH-032 — OAuth Health Check

Health checks shall determine:

```text
Connection Exists
Token Available
Token Expiration
Refresh Available
Granted Scopes
Provider Reachability
Last Successful Authentication
Last Refresh
```

---

## FR-OAUTH-033 — OAuth Provider Discovery

Where supported, the system shall discover provider OAuth metadata using trusted mechanisms.

---

## FR-OAUTH-034 — OIDC Discovery

The system shall retrieve and validate OIDC discovery metadata.

---

## FR-OAUTH-035 — JWKS Retrieval

The system shall retrieve provider public keys for OIDC token validation.

---

## FR-OAUTH-036 — JWKS Cache

JWKS metadata shall be cached with controlled expiration and refresh behavior.

---

## FR-OAUTH-037 — OIDC ID Token Validation

The platform shall validate:

```text
signature
issuer
audience
expiration
issued_at
nonce
```

as applicable.

---

## FR-OAUTH-038 — Token Type Validation

The platform shall ensure expected token types are used according to provider configuration.

---

## FR-OAUTH-039 — OAuth Client Authentication

The system shall support provider-specific client authentication methods:

```text
client_secret_basic
client_secret_post
private_key_jwt
none
```

only where explicitly supported and permitted by provider security policy.

---

## FR-OAUTH-040 — Private Key JWT

Where supported, SalesGenie shall generate client assertions using securely stored signing keys.

---

## FR-OAUTH-041 — OAuth Provider Rate Limits

Provider rate-limit responses shall be translated into safe internal error categories.

---

## FR-OAUTH-042 — OAuth Circuit Breaker

Repeated provider failures shall trigger circuit-breaking to prevent cascading failures.

---

## FR-OAUTH-043 — OAuth Retry

Retryable provider failures shall use:

```text
Exponential Backoff
+
Jitter
+
Maximum Attempts
+
Circuit Breaking
```

---

## FR-OAUTH-044 — OAuth Audit Event

Every OAuth lifecycle event shall generate an audit event containing:

```text
event_id
tenant_id
user_id
agent_id
workflow_id
integration_id
provider_id
operation
result
risk_level
timestamp
correlation_id
```

No secrets shall be included.

---

## 9. Human OAuth Workflow

```text
Human User
    ↓
SalesGenie Integration Catalog
    ↓
Select Google
    ↓
Click "Connect"
    ↓
SalesGenie OAuth Service
    ↓
Generate OAuth Transaction
    ↓
Generate State
    ↓
Generate PKCE
    ↓
Generate Authorization URL
    ↓
Google Authorization Server
    ↓
User Login
    ↓
User Consent
    ↓
Authorization Code
    ↓
SalesGenie Callback
    ↓
Validate State
    ↓
Validate PKCE
    ↓
Exchange Code
    ↓
Receive Tokens
    ↓
Encrypt Credentials
    ↓
Credential Vault
    ↓
Validate Scopes
    ↓
Validate Account
    ↓
Connection Test
    ↓
CONNECTED
    ↓
Audit Event
```

---

## 10. AI OAuth Workflow

```text
User
 ↓
"Send the proposal to John."
 ↓
AI Sales Agent
 ↓
Determine Required Capability
 ↓
gmail.send_email
 ↓
OAuth Capability Mapping
 ↓
Required Scope:
gmail.send
 ↓
Check OAuth State
 ↓
NOT_CONNECTED
 ↓
Risk Assessment
 ↓
Policy Engine
 ↓
Approval Required?
 ↓
YES
 ↓
Human Approval
 ↓
OAuth Authorization
 ↓
Provider Consent
 ↓
Callback
 ↓
Token Exchange
 ↓
Credential Vault
 ↓
OAuth Validation
 ↓
Capability Granted
 ↓
AI Executes gmail.send_email
 ↓
Audit
```

---

## 11. AI OAuth Reauthentication Workflow

```text
AI Agent
    ↓
Integration Request
    ↓
OAuth Access Token
    ↓
Provider Returns 401
    ↓
OAuth Service
    ↓
Refresh Token Available?
    ├── YES
    │    ↓
    │  Refresh
    │    ↓
    │  Store New Token
    │    ↓
    │  Retry Once
    │
    └── NO
         ↓
      Reauthorization Required
         ↓
      Create Human Request
         ↓
      Notify User
         ↓
      User Reauthorizes
         ↓
      Validate
         ↓
      Retry Operation
```

---

## 12. Incremental Authorization Workflow

```text
Existing Connection
        ↓
Current Scopes
        ↓
crm.contacts.read
        ↓
AI Requires:
crm.contacts.write
        ↓
Missing Scope Detected
        ↓
Risk Assessment
        ↓
Policy Evaluation
        ↓
Human Approval?
        ↓
OAuth Reauthorization
        ↓
New Scope Granted
        ↓
Validate
        ↓
Update OAuth Connection
        ↓
Capability Enabled
```

---

## 13. OAuth Revocation Workflow

```text
Admin
 ↓
Disconnect Integration
 ↓
Policy Check
 ↓
Mark Connection:
REVOCATION_PENDING
 ↓
Provider Revocation Endpoint
 ↓
Success?
 ├── YES → REVOKED
 └── NO
      ↓
Local Revocation
      ↓
Provider Revocation Retry
      ↓
Audit
```

---

## 14. OAuth Failure State Machine

```text
NOT_CONNECTED
      ↓
AUTHORIZATION_PENDING
      ↓
AUTHENTICATING
      ↓
AUTHENTICATED
      ↓
ACTIVE
      │
      ├── TOKEN_EXPIRING
      │       ↓
      │   REFRESHING
      │       ↓
      │     ACTIVE
      │
      ├── REFRESH_FAILED
      │       ↓
      │ REAUTHENTICATION_REQUIRED
      │
      ├── REVOKED
      │
      ├── COMPROMISED
      │
      └── DISABLED
```

Invalid state transitions shall be rejected.

---

## 15. OAuth Data Model

## OAuth Provider

```text
OAuthProvider
├── id
├── provider_key
├── name
├── issuer
├── authorization_endpoint
├── token_endpoint
├── revocation_endpoint
├── introspection_endpoint
├── userinfo_endpoint
├── jwks_uri
├── supported_scopes
├── supported_response_types
├── supported_grant_types
├── supported_client_auth_methods
├── pkce_required
├── refresh_token_supported
├── status
├── created_at
└── updated_at
```

---

## OAuth Client

```text
OAuthClient
├── id
├── provider_id
├── client_id
├── client_secret_reference
├── environment
├── redirect_uris
├── allowed_scopes
├── client_auth_method
├── status
├── created_at
└── updated_at
```

---

## OAuth Connection

```text
OAuthConnection
├── id
├── tenant_id
├── user_id
├── integration_id
├── provider_id
├── external_account_id
├── external_account_name
├── credential_reference
├── credential_version
├── granted_scopes
├── status
├── token_type
├── issued_at
├── expires_at
├── last_refresh_at
├── last_validation_at
├── last_error_code
├── created_at
└── updated_at
```

---

## OAuth Transaction

```text
OAuthTransaction
├── id
├── tenant_id
├── user_id
├── integration_id
├── provider_id
├── state_hash
├── pkce_verifier_reference
├── requested_scopes
├── redirect_uri
├── status
├── expires_at
├── created_at
└── consumed_at
```

---

## 16. OAuth API Requirements

```text
GET    /api/v1/oauth/providers

GET    /api/v1/integrations/{id}/oauth
GET    /api/v1/integrations/{id}/oauth/status
GET    /api/v1/integrations/{id}/oauth/health
GET    /api/v1/integrations/{id}/oauth/scopes

POST   /api/v1/integrations/{id}/oauth/authorize
GET    /api/v1/integrations/oauth/callback

POST   /api/v1/integrations/{id}/oauth/refresh
POST   /api/v1/integrations/{id}/oauth/reauthorize
POST   /api/v1/integrations/{id}/oauth/revoke
POST   /api/v1/integrations/{id}/oauth/disconnect

POST   /api/v1/integrations/{id}/oauth/scopes/request
POST   /api/v1/integrations/{id}/oauth/test

GET    /api/v1/oauth/requests
POST   /api/v1/oauth/requests/{id}/approve
POST   /api/v1/oauth/requests/{id}/deny
```

---

## 17. MCP OAuth Requirements

MCP clients and tools shall never receive raw OAuth credentials.

Supported MCP capabilities may include:

```text
oauth.get_status
oauth.get_requirements
oauth.request_authorization
oauth.request_reauthorization
oauth.request_scope
oauth.test_connection
```

Example:

```text
MCP Tool Request
      ↓
oauth.get_status
      ↓
SalesGenie OAuth Service
      ↓
Safe Response

{
  "status": "AUTHENTICATION_REQUIRED",
  "provider": "salesforce",
  "required_scopes": [
    "contacts.read"
  ],
  "approval_required": true
}
```

The response shall never contain an access token or refresh token.

---

## 18. n8n OAuth Requirements

n8n workflows shall be able to consume OAuth-authenticated SalesGenie integrations through a controlled credential boundary.

```text
n8n
 ↓
SalesGenie Integration Gateway
 ↓
OAuth Capability
 ↓
OAuth Service
 ↓
Credential Vault
 ↓
External Provider
```

n8n workflow payloads shall not contain long-lived refresh tokens.

---

## 19. Workflow OAuth Requirements

A workflow shall support:

```text
OAuth Precondition
OAuth Authentication Check
OAuth Scope Check
OAuth Reauthorization
OAuth Token Refresh
OAuth Failure Branch
OAuth Recovery
OAuth Human Approval
```

Example:

```text
Trigger
 ↓
OAuth Check
 ↓
Authenticated?
 ├── YES → Continue
 └── NO
      ↓
Request Authentication
      ↓
Pause Workflow
      ↓
Human Authorization
      ↓
Resume Workflow
```

---

## 20. AI + Human Shared OAuth Control Model

```text
                     ┌─────────────────┐
                     │   Human User    │
                     └────────┬────────┘
                              │
                         Consent /
                         Approval
                              │
                              ▼
┌──────────────┐       ┌───────────────┐
│   AI Agent   │──────►│ Policy Engine  │
└──────┬───────┘       └───────┬───────┘
       │                       │
       │ Capability Request    │
       └──────────────────────►│
                               ▼
                       ┌───────────────┐
                       │ OAuth Service │
                       └───────┬───────┘
                               │
                               ▼
                       ┌───────────────┐
                       │ Credential    │
                       │ Vault         │
                       └───────┬───────┘
                               │
                               ▼
                       External Provider
```

---

## 21. OAuth Security Requirements

The platform shall:

1. Use Authorization Code Flow for browser-based OAuth integrations.
2. Use PKCE where applicable.
3. Generate cryptographically secure state values.
4. Bind state to tenant and user context.
5. Make authorization state single-use.
6. Expire authorization transactions.
7. Validate redirect URIs.
8. Validate OAuth callbacks.
9. Encrypt OAuth tokens.
10. Protect refresh tokens.
11. Redact tokens from logs.
12. Prevent tokens from entering LLM context.
13. Prevent tokens from entering RAG storage.
14. Prevent tokens from entering MCP responses.
15. Prevent tokens from entering analytics.
16. Prevent tokens from entering ordinary event payloads.
17. Prevent cross-tenant token access.
18. Prevent scope escalation.
19. Prevent OAuth callback replay.
20. Prevent SSRF.
21. Validate TLS certificates.
22. Enforce rate limits.
23. Detect abuse.
24. Support revocation.
25. Support rotation.
26. Support emergency revocation.
27. Fail closed when OAuth state is uncertain.

---

## 22. OAuth Threat Model

SalesGenie shall defend against:

```text
Authorization Code Theft
OAuth CSRF
State Fixation
State Replay
PKCE Downgrade
Redirect URI Manipulation
Open Redirect
Token Leakage
Refresh Token Theft
Token Replay
Scope Escalation
Confused Deputy
Account Linking Attack
Cross-Tenant Access
Session Hijacking
SSRF
Provider Impersonation
JWKS Manipulation
JWT Algorithm Confusion
OIDC Nonce Replay
Credential Stuffing
OAuth Phishing
AI OAuth Abuse
MCP OAuth Abuse
Workflow Credential Leakage
Insider Credential Access
```

---

## 23. OAuth Risk Classification

## LOW

```text
Read-only public profile
Basic identity information
Read-only non-sensitive data
```

---

## MEDIUM

```text
Read private business data
Create records
Access customer metadata
```

---

## HIGH

```text
Send email
Modify CRM records
Access sensitive business information
Write customer data
```

---

## CRITICAL

```text
Delete records
Financial operations
Administrative operations
Security configuration
Credential management
Organization-wide access
```

---

## 24. OAuth Approval Matrix

| Operation                           |      Human |             AI |         Approval |
| ----------------------------------- | ---------: | -------------: | ---------------: |
| Read public profile                 |    Allowed |        Allowed |             None |
| Read CRM contacts                   |    Allowed |        Allowed |           Policy |
| Write CRM contacts                  |    Allowed |        Allowed |     Configurable |
| Send email                          |    Allowed |        Request | Usually required |
| Delete CRM records                  |    Allowed | Denied/Request |         Required |
| Modify security settings            |    Allowed |         Denied |   Multi-approval |
| Grant organization-wide OAuth scope |    Allowed |         Denied |   Multi-approval |
| Revoke critical integration         |    Allowed |        Request |         Required |
| Retrieve raw OAuth token            | Restricted |         Denied | Never through AI |

---

## 25. Performance Requirements

OAuth control-plane operations shall target:

```text
P50 < 100 ms
P95 < 300 ms
P99 < 1 second
```

excluding external provider latency.

Token refresh shall target:

```text
P95 < 500 ms
```

excluding provider latency.

---

## 26. Reliability Requirements

The OAuth subsystem shall provide:

```text
Retryable Operations
Idempotent Operations
Distributed Coordination
Circuit Breaking
Graceful Degradation
Provider Isolation
Credential Recovery
Auditability
```

A failure from one provider shall not cascade to other providers.

---

## 27. Availability Requirements

The OAuth control plane shall target:

```text
99.99% availability
```

Provider-specific outages shall be isolated.

Example:

```text
Google OAuth unavailable

Salesforce OAuth → Operational
HubSpot OAuth → Operational
Slack OAuth → Operational
Microsoft OAuth → Operational
```

---

## 28. Monitoring Requirements

OAuth metrics shall include:

```text
oauth_authorization_attempts_total
oauth_authorization_success_total
oauth_authorization_failures_total

oauth_callback_total
oauth_callback_rejected_total

oauth_token_exchange_total
oauth_token_exchange_failures_total

oauth_refresh_total
oauth_refresh_success_total
oauth_refresh_failures_total

oauth_revocation_total

oauth_reauthorization_total

oauth_scope_upgrade_total
oauth_scope_denial_total

oauth_connection_active_total
oauth_connection_expired_total

oauth_provider_latency
oauth_provider_error_rate
oauth_provider_rate_limit_total
```

---

## 29. Security Monitoring

Security analytics shall detect:

```text
Unusual OAuth Authorization Volume
Repeated Authorization Failures
Repeated Callback Failures
State Validation Failures
Multiple Scope Escalations
Abnormal Token Refresh Patterns
Unexpected Geographic Changes
Unexpected Account Linking
Repeated Revocation
Suspicious AI OAuth Requests
Suspicious MCP OAuth Requests
```

---

## 30. Audit Requirements

Audit records shall include:

```text
Event ID
Tenant ID
Actor Type
Actor ID
AI Agent ID
Workflow ID
Provider
Integration
OAuth Connection
Requested Scopes
Granted Scopes
Operation
Risk Level
Approval Status
Result
Timestamp
IP Metadata where policy permits
Correlation ID
```

Secrets shall never be included.

---

## 31. OAuth Error Taxonomy

SalesGenie shall normalize provider errors.

```text
OAUTH_INVALID_REQUEST
OAUTH_ACCESS_DENIED
OAUTH_INVALID_CLIENT
OAUTH_INVALID_GRANT
OAUTH_INVALID_SCOPE
OAUTH_UNAUTHORIZED_CLIENT
OAUTH_UNSUPPORTED_GRANT
OAUTH_TOKEN_EXPIRED
OAUTH_REFRESH_REVOKED
OAUTH_INSUFFICIENT_SCOPE
OAUTH_PROVIDER_UNAVAILABLE
OAUTH_PROVIDER_RATE_LIMITED
OAUTH_STATE_INVALID
OAUTH_STATE_EXPIRED
OAUTH_STATE_REPLAYED
OAUTH_PKCE_FAILED
OAUTH_REDIRECT_URI_INVALID
OAUTH_ACCOUNT_LINK_FAILED
OAUTH_POLICY_DENIED
OAUTH_APPROVAL_REQUIRED
OAUTH_CONNECTION_DISABLED
OAUTH_SECURITY_BLOCKED
```

---

## 32. OAuth Error Recovery

```text
OAuth Failure
      ↓
Classify Error
      ↓
Transient?
 ├── YES
 │    ↓
 │  Retry with Backoff
 │
 └── NO
      ↓
Permanent Authentication Error?
 ├── YES
 │    ↓
 │  Reauthorization Required
 │
 └── NO
      ↓
Security Failure?
      ↓
Block + Alert + Audit
```

---

## 33. OAuth Provider Adapter Architecture

Each provider shall use an adapter abstraction.

```text
OAuthProviderAdapter
├── build_authorization_url()
├── validate_callback()
├── exchange_code()
├── refresh_token()
├── revoke_token()
├── introspect_token()
├── get_account_identity()
├── validate_scopes()
└── normalize_error()
```

Provider-specific behavior shall remain isolated from the core OAuth engine.

---

## 34. Provider Adapter Examples

```text
GoogleOAuthAdapter
MicrosoftOAuthAdapter
SalesforceOAuthAdapter
HubSpotOAuthAdapter
SlackOAuthAdapter
NotionOAuthAdapter
ZendeskOAuthAdapter
JiraOAuthAdapter
```

The architecture shall allow additional adapters without modifying the core OAuth state machine.

---

## 35. OAuth Connection Lifecycle

```text
DISCOVERED
    ↓
CONFIGURED
    ↓
AUTHORIZATION_PENDING
    ↓
AUTHORIZING
    ↓
TOKEN_EXCHANGED
    ↓
VALIDATING
    ↓
ACTIVE
    ↓
TOKEN_EXPIRING
    ↓
REFRESHING
    ↓
ACTIVE

Possible terminal states:

REVOKED
DISABLED
COMPROMISED
DELETED
```

---

## 36. OAuth Transaction Lifecycle

```text
CREATED
   ↓
AUTHORIZATION_URL_GENERATED
   ↓
USER_REDIRECTED
   ↓
CALLBACK_RECEIVED
   ↓
STATE_VALIDATED
   ↓
CODE_EXCHANGED
   ↓
TOKEN_VALIDATED
   ↓
COMPLETED
```

Failure states:

```text
EXPIRED
CANCELLED
REJECTED
FAILED
REPLAYED
SECURITY_BLOCKED
```

---

## 37. Enterprise OAuth Governance

Every production OAuth integration shall define:

```text
Provider Owner
Integration Owner
OAuth Client
Allowed Redirect URIs
Allowed Scopes
Risk Classification
Approval Policy
Token Lifetime
Refresh Policy
Revocation Policy
Rotation Policy
Environment
Tenant Availability
AI Availability
Workflow Availability
Audit Policy
```

---

## 38. Acceptance Criteria

The OAuth subsystem shall be considered production-ready when:

* Authorization Code Flow works end-to-end.
* PKCE is implemented.
* OAuth state is cryptographically secure.
* OAuth state is single-use.
* OAuth state expires.
* State is tenant-bound.
* State is user-bound.
* Redirect URIs are allowlisted.
* OAuth callbacks are validated.
* Authorization codes are exchanged server-side.
* Tokens are encrypted.
* Refresh tokens are protected.
* Tokens never enter LLM context.
* Tokens never enter RAG.
* Tokens never enter MCP responses.
* Tokens never enter analytics.
* Tokens never appear in logs.
* Refresh-token rotation is concurrency-safe.
* Token expiration is tracked.
* Proactive refresh is supported.
* Lazy refresh is supported.
* Refresh failures are classified.
* Permanent failures trigger reauthorization.
* Incremental authorization is supported.
* Scope minimization is enforced.
* Scope escalation is blocked.
* OAuth revocation is supported.
* OIDC validation is supported where applicable.
* Issuer validation is enforced.
* Audience validation is enforced.
* Nonce validation is enforced where applicable.
* JWKS validation is secure.
* JWKS rotation is supported.
* OAuth provider failures are isolated.
* OAuth requests are rate-limited.
* SSRF protection is implemented.
* AI agents cannot self-authorize.
* AI agents cannot access OAuth credentials.
* AI agents can request OAuth capabilities.
* Human approval is supported.
* High-risk OAuth scopes require approval.
* Workflows can pause for OAuth.
* Workflows can resume after OAuth.
* MCP can safely query OAuth status.
* n8n can use OAuth-backed capabilities.
* OAuth events are auditable.
* OAuth metrics are available.
* Distributed tracing is available.
* Emergency revocation is supported.
* Multi-tenant isolation is enforced.
* Production and development credentials are isolated.
* OAuth service supports horizontal scaling.
* OAuth operations are idempotent where applicable.
* The system fails closed on ambiguous authentication state.

---

## 39. FAANG-Level OAuth Design Principles

## Principle 1 — OAuth Is a Security Boundary

OAuth shall not be treated as merely an integration configuration feature.

It is a security control plane between SalesGenie and external systems.

---

## Principle 2 — Tokens Are Never AI Data

```text
AI ≠ Token Holder
AI = Capability Consumer
```

The AI receives a capability result rather than OAuth credentials.

---

## Principle 3 — Consent Is Human-Owned

AI may request authorization.

Only an authorized human or explicitly configured non-human policy may approve it.

---

## Principle 4 — Least Privilege

Every OAuth authorization shall request the smallest practical permission set.

---

## Principle 5 — Incremental Authorization

Do not request permissions before they are needed.

```text
Need
 ↓
Detect
 ↓
Request Minimum Scope
 ↓
Approve
 ↓
Authorize
```

---

## Principle 6 — Provider Isolation

A provider-specific OAuth failure shall not compromise the OAuth subsystem or unrelated integrations.

---

## Principle 7 — Fail Closed

If:

```text
State Invalid
Scope Uncertain
Token Uncertain
Tenant Uncertain
Identity Uncertain
Provider Identity Uncertain
```

then the operation shall be denied.

---

## Principle 8 — Credential Vault Boundary

```text
AI / UI / Workflow
        ↓
Capability Request
        ↓
Policy Engine
        ↓
OAuth Service
        ↓
Credential Vault
        ↓
Integration Gateway
        ↓
External Provider
```

Credentials shall remain behind the trusted boundary.

---

## Principle 9 — Every OAuth Action Is Auditable

The system shall be able to answer:

```text
Who authorized this?
Which tenant?
Which provider?
Which external account?
Which scopes?
Why were the scopes requested?
Which AI agent requested them?
Which workflow requested them?
Who approved them?
When?
What happened afterward?
```

---

## Principle 10 — OAuth Must Be Operationally Recoverable

An expired or revoked token shall not permanently break a workflow.

The system shall provide:

```text
Detect
 ↓
Refresh
 ↓
Retry
 ↓
Reauthorize
 ↓
Resume
```

---

## 40. Definition of Done

```text
✓ OAuth 2.0
✓ OAuth 2.1-Compatible Security Practices
✓ Authorization Code Flow
✓ PKCE
✓ OAuth State
✓ State Replay Protection
✓ Redirect URI Validation
✓ OAuth Callback Validation
✓ Token Exchange
✓ Access Token Management
✓ Refresh Token Management
✓ Refresh Token Rotation
✓ Token Expiration
✓ Proactive Refresh
✓ Lazy Refresh
✓ Token Revocation
✓ Token Introspection
✓ OIDC
✓ OIDC Discovery
✓ ID Token Validation
✓ Issuer Validation
✓ Audience Validation
✓ Nonce Validation
✓ JWKS
✓ JWKS Rotation
✓ Scope Registry
✓ Scope Minimization
✓ Incremental Authorization
✓ Scope Escalation Protection
✓ Human Consent
✓ Human Approval
✓ AI OAuth Requests
✓ AI OAuth Credential Isolation
✓ AI Capability-Based OAuth
✓ Workflow OAuth Preconditions
✓ Workflow OAuth Pause/Resume
✓ MCP OAuth Integration
✓ n8n OAuth Integration
✓ Provider Adapter Architecture
✓ Multi-Account OAuth
✓ Multi-Tenant Isolation
✓ Environment Isolation
✓ Credential Vault
✓ Token Encryption
✓ Secret Redaction
✓ SSRF Protection
✓ OAuth Rate Limiting
✓ OAuth Abuse Detection
✓ Circuit Breaking
✓ Retry with Jitter
✓ OAuth Health Checks
✓ OAuth Metrics
✓ Distributed Tracing
✓ Immutable Audit
✓ Emergency Revocation
✓ Credential Versioning
✓ High Availability
✓ Horizontal Scalability
✓ Disaster Recovery
✓ Fail-Closed Security
```

---

## 41. Core OAuth Architecture Principle

> **SalesGenie shall implement OAuth as a centralized, zero-trust authorization boundary. Humans and AI agents may initiate OAuth requests, determine required capabilities, and request additional scopes, but OAuth credentials and tokens shall remain exclusively within the trusted OAuth and integration execution boundary. Every authorization shall enforce tenant isolation, PKCE/state protection, least-privilege scopes, explicit consent, policy-based approval, secure token lifecycle management, continuous observability, and immutable auditability.**
