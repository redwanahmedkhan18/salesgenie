# SalesGenie — API Security Requirements

**Document:** `api_security.md`  
**Product:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Requirement Level:** FAANG-Level / Production-Grade  
**Scope:** Human APIs + AI APIs + Internal Service APIs + MCP APIs + Integration APIs + Webhooks + Admin APIs + Billing APIs + Lead Intelligence APIs

---

## 1. Purpose

SalesGenie shall provide a defense-in-depth API security architecture protecting every API request, response, resource, service, AI action, integration, workflow, and administrative operation.

The API security model shall apply to:

```text
Human Users
AI Agents
Multi-Agent Orchestrator
MCP Tools
Workflows
Frontend Applications
Mobile Applications
Internal Microservices
External Integrations
Webhooks
Background Workers
Scheduled Jobs
Administrative Services
Billing Services
```

The API security architecture shall prevent:

```text
Unauthorized Access
Broken Access Control
Privilege Escalation
Cross-Tenant Access
Authentication Abuse
Token Abuse
Injection
API Enumeration
Data Exfiltration
SSRF
Replay Attacks
Request Forgery
Resource Exhaustion
AI Tool Abuse
MCP Abuse
Webhook Abuse
Sensitive Data Leakage
```

---

## 2. API Security Objectives

SalesGenie APIs shall:

1. Authenticate every protected request.
2. Authorize every protected operation.
3. Enforce tenant isolation.
4. Validate all request inputs.
5. Validate all API outputs.
6. Protect authentication tokens.
7. Enforce API rate limits.
8. Prevent API abuse.
9. Prevent injection attacks.
10. Prevent resource enumeration.
11. Prevent sensitive data exposure.
12. Protect internal service APIs.
13. Protect AI APIs.
14. Protect MCP execution APIs.
15. Protect webhook APIs.
16. Protect administrative APIs.
17. Protect billing and payment APIs.
18. Provide complete API auditability.
19. Provide security monitoring.
20. Support rapid credential revocation.
21. Fail securely.
22. Maintain backward-compatible API security controls.

---

## 3. API Security Principles

## API-PRINCIPLE-001 — Zero Trust

Every API request shall be treated as untrusted until authentication, authorization, validation, and policy checks succeed.

---

## API-PRINCIPLE-002 — Least Privilege

Users, services, agents, API keys, workflows, and integrations shall receive only the minimum API permissions required.

---

## API-PRINCIPLE-003 — Server-Side Enforcement

Security decisions shall always be enforced by the server.

Frontend restrictions shall never constitute authorization.

---

## API-PRINCIPLE-004 — Complete Mediation

Every protected resource operation shall independently verify authorization.

---

## API-PRINCIPLE-005 — Secure by Default

New API endpoints shall default to authenticated, authorized, validated, rate-limited behavior.

---

## API-PRINCIPLE-006 — Fail Closed

Security validation failures shall deny access.

---

## API-PRINCIPLE-007 — Tenant Isolation

Every tenant-scoped API operation shall explicitly validate tenant context.

---

## API-PRINCIPLE-008 — Untrusted External Data

All external API responses, webhook payloads, AI outputs, MCP results, and integration data shall be treated as untrusted.

---

## 4. API Actors

## Human Actors

```text
H-001 End User
H-002 Sales Agent
H-003 Support Agent
H-004 Organization Admin
H-005 Security Admin
H-006 Billing Admin
H-007 Developer
H-008 Auditor
H-009 Super Admin
```

## AI Actors

```text
AI-001 Sales Agent
AI-002 Support Agent
AI-003 Lead Generation Agent
AI-004 Research Agent
AI-005 Customer Success Agent
AI-006 Workflow Agent
AI-007 MCP Agent
AI-008 Multi-Agent Orchestrator
```

## Machine Actors

```text
M-001 API Gateway
M-002 Authentication Service
M-003 Authorization Service
M-004 AI Gateway
M-005 Workflow Engine
M-006 Integration Service
M-007 Billing Service
M-008 Lead Intelligence Service
M-009 Notification Service
M-010 Background Worker
```

---

## 5. User Requirements

## UR-APISEC-001 — Secure API Access

Users shall access protected APIs only after successful authentication.

---

## UR-APISEC-002 — Role-Based API Access

Users shall only invoke APIs permitted by their assigned roles and permissions.

---

## UR-APISEC-003 — Resource-Level Authorization

Users shall only access resources for which they have explicit authorization.

---

## UR-APISEC-004 — Tenant Isolation

Users shall never access another organization's resources through API manipulation.

---

## UR-APISEC-005 — Secure API Sessions

Authenticated API sessions shall expire, rotate, and support revocation according to policy.

---

## UR-APISEC-006 — API Error Safety

Users shall receive safe API errors that do not expose internal implementation details.

---

## UR-APISEC-007 — API Security Visibility

Authorized administrators shall be able to inspect API security activity.

---

## UR-APISEC-008 — Credential Revocation

Users and authorized administrators shall be able to revoke applicable API credentials.

---

## UR-APISEC-009 — API Key Management

Authorized developers shall be able to create, rotate, restrict, monitor, and revoke API keys.

---

## UR-APISEC-010 — Secure Data Access

Users shall only receive API fields permitted by authorization and data-classification policies.

---

## 6. AI User Requirements

## AI-UR-APISEC-001 — AI API Identity

Every AI-generated API request shall be attributable to an authenticated AI execution identity.

---

## AI-UR-APISEC-002 — AI API Authorization

AI agents shall only invoke APIs explicitly permitted by their capabilities.

---

## AI-UR-APISEC-003 — AI Tenant Isolation

AI agents shall never invoke APIs against unauthorized tenant resources.

---

## AI-UR-APISEC-004 — AI Tool Authorization

API calls initiated through AI tools shall undergo independent authorization before execution.

---

## AI-UR-APISEC-005 — AI Input Validation

AI-generated API parameters shall be validated using the same security controls as human-generated requests.

---

## AI-UR-APISEC-006 — AI Output Validation

Responses returned to AI agents shall be filtered according to tenant, permission, and data-classification policies.

---

## AI-UR-APISEC-007 — AI Rate Limits

AI agents shall have separate request and execution limits.

---

## AI-UR-APISEC-008 — AI Cost Protection

AI-generated API activity shall be bounded to prevent uncontrolled external API costs.

---

## AI-UR-APISEC-009 — High-Risk AI API Actions

High-risk API operations shall support human approval.

---

## AI-UR-APISEC-010 — AI Auditability

Every security-sensitive AI API call shall be attributable to:

```text
User
Tenant
Agent
Workflow
Tool
API
Resource
Execution
```

---

## 7. System Requirements

## SR-APISEC-001 — API Gateway

SalesGenie shall provide a centralized API gateway or equivalent enforcement layer.

The gateway shall support:

```text
TLS
Authentication
Rate Limiting
Request Validation
Routing
Threat Detection
CORS
Security Headers
Request Size Limits
Correlation IDs
Logging
```

---

## SR-APISEC-002 — API Security Middleware

All protected services shall implement security middleware.

---

## SR-APISEC-003 — Distributed Authorization

Authorization shall be enforced both at gateway/service boundaries and at resource-operation boundaries.

---

## SR-APISEC-004 — Security Context Propagation

API security context shall propagate across microservices.

Example:

```text
User
   |
   v
API Gateway
   |
   v
Auth Context
   |
   v
Service A
   |
   v
Service B
   |
   v
Database
```

---

## SR-APISEC-005 — Correlation IDs

Every API request shall receive a unique correlation/request identifier.

---

## SR-APISEC-006 — Trace Context

Distributed API calls shall support trace propagation for security investigation and observability.

---

## 8. API Authentication

## FR-APISEC-AUTH-001

Protected APIs shall require authentication.

---

## FR-APISEC-AUTH-002

Supported authentication mechanisms may include:

```text
OAuth 2.0
OpenID Connect
JWT
API Keys
Service Credentials
Mutual TLS
Signed Requests
Webhook Signatures
```

---

## FR-APISEC-AUTH-003

Authentication mechanisms shall be selected based on actor type and API risk.

---

## FR-APISEC-AUTH-004

Authentication failures shall not disclose whether a particular credential, user, or account exists.

---

## 9. JWT Security

JWT validation shall verify:

```text
Signature
Algorithm
Issuer
Audience
Subject
Expiration
Not-Before
Token Type
Scopes
Tenant
Authentication Strength
```

---

## FR-APISEC-JWT-001

The server shall reject expired tokens.

---

## FR-APISEC-JWT-002

The server shall reject tokens with invalid signatures.

---

## FR-APISEC-JWT-003

The server shall reject unexpected signing algorithms.

---

## FR-APISEC-JWT-004

The server shall validate issuer and audience.

---

## FR-APISEC-JWT-005

JWT claims shall not independently establish authorization.

---

## 10. Token Security

Access tokens shall:

```text
Have Limited Lifetime
Be Validated Server-Side
Be Revocable Where Applicable
Be Scoped
Be Tenant-Bound Where Required
```

Refresh tokens shall support:

```text
Rotation
Reuse Detection
Revocation
Expiration
```

---

## 11. API Key Security

API keys shall support:

```text
Creation
Naming
Scopes
Expiration
Rotation
Revocation
Usage Tracking
IP Restrictions Where Appropriate
Tenant Binding
Audit Logging
```

---

## FR-APISEC-KEY-001

API keys shall never be stored in plaintext where recoverability is unnecessary.

---

## FR-APISEC-KEY-002

API keys shall never appear in normal logs.

---

## FR-APISEC-KEY-003

Revoked API keys shall immediately lose access according to the platform's consistency guarantees.

---

## 12. Service-to-Service Authentication

Internal APIs shall require authenticated service identities for protected operations.

Possible mechanisms:

```text
mTLS
Signed JWT
Short-Lived Service Tokens
Workload Identity
```

---

## 13. Service-to-Service Authorization

Each internal API shall validate:

```text
Calling Service
Requested Operation
Target Service
Tenant Context
Resource
Scope
```

---

## 14. mTLS

High-security internal services shall support mutual TLS where appropriate.

---

## 15. API Authorization

Authorization shall occur after authentication and before business operations.

---

## 16. RBAC

API permissions shall support roles including:

```text
END_USER
SALES_AGENT
SUPPORT_AGENT
ORG_ADMIN
SECURITY_ADMIN
BILLING_ADMIN
DEVELOPER
AUDITOR
SUPER_ADMIN
```

---

## 17. Permission Model

Permissions shall follow a structure such as:

```text
resource.action
```

Examples:

```text
users.read
users.create
users.update
users.delete

leads.read
leads.create
leads.update
leads.delete
leads.export

conversations.read
conversations.create
conversations.update
conversations.export

agents.read
agents.create
agents.update
agents.execute
agents.delete

workflows.read
workflows.create
workflows.update
workflows.execute
workflows.delete

integrations.read
integrations.connect
integrations.update
integrations.disconnect

mcp.read
mcp.execute
mcp.admin

billing.read
billing.manage
billing.refund

audit.read
security.manage
```

---

## 18. Object-Level Authorization

Every resource request shall evaluate:

```text
Actor
Tenant
Resource
Action
Ownership
Permission
Policy
```

---

## 19. Attribute-Based Authorization

Where required, authorization may also consider:

```text
Role
Department
Resource Classification
Region
Customer
Agent
Workflow
Time
Network
Risk
Authentication Strength
```

---

## 20. Broken Object-Level Authorization

SalesGenie shall prevent IDOR and BOLA vulnerabilities.

Example:

```text
GET /api/v1/leads/{lead_id}
```

shall verify that the authenticated actor can access the specified `lead_id`.

---

## 21. Broken Function-Level Authorization

Every privileged endpoint shall enforce explicit permission checks.

---

## 22. Tenant Context

Tenant context shall be derived from trusted authentication and authorization information.

Client-supplied tenant IDs shall never independently grant tenant access.

---

## 23. Cross-Tenant Protection

The API layer shall reject:

```text
Tenant A -> Tenant B Resource
Tenant A -> Tenant B Conversation
Tenant A -> Tenant B Lead
Tenant A -> Tenant B Integration
Tenant A -> Tenant B Workflow
Tenant A -> Tenant B AI Agent
Tenant A -> Tenant B Billing Data
```

---

## 24. Request Validation

All requests shall be validated against explicit schemas.

Validation shall include:

```text
Data Type
Required Fields
Allowed Fields
String Length
Numeric Range
Enum Values
Format
Encoding
Nested Structure
```

---

## 25. Content-Type Validation

Endpoints shall accept only supported content types.

Unexpected content types shall be rejected.

---

## 26. HTTP Method Security

Endpoints shall explicitly define supported HTTP methods.

Unsupported methods shall be rejected.

---

## 27. Request Size Limits

API requests shall enforce maximum sizes for:

```text
Headers
URL
Query Parameters
JSON Body
Multipart Requests
Files
AI Prompts
Webhook Payloads
```

---

## 28. JSON Security

JSON parsing shall defend against:

```text
Deep Nesting
Oversized Payloads
Unexpected Types
Duplicate Fields
Malformed JSON
Parser Differential Attacks
```

---

## 29. Mass Assignment Protection

Only explicitly allowed fields shall be writable.

Protected fields shall include where applicable:

```text
user_id
tenant_id
role
permissions
is_super_admin
billing_status
security_status
created_at
```

---

## 30. Query Parameter Security

Query parameters shall be:

```text
Typed
Validated
Bounded
Authorized
```

---

## 31. Pagination Security

Pagination shall enforce:

```text
Maximum Page Size
Maximum Offset
Cursor Validation
Tenant Scope
Authorization
```

---

## 32. Sorting Security

Sort fields shall use explicit allowlists.

Clients shall not inject arbitrary database expressions.

---

## 33. Filtering Security

Filter fields and operators shall be explicitly controlled.

---

## 34. SQL Injection Prevention

All database access shall use:

```text
Parameterized Queries
Prepared Statements
Safe ORM APIs
Validated Query Builders
```

---

## 35. NoSQL Injection Prevention

Untrusted operators shall not be directly inserted into NoSQL queries.

---

## 36. Command Injection Prevention

API input shall never be directly executed by operating-system shells.

---

## 37. SSRF Protection

APIs that accept URLs shall implement:

```text
Protocol Allowlist
Domain Allowlist
Private IP Blocking
Loopback Blocking
Cloud Metadata Blocking
DNS Rebinding Protection
Redirect Validation
Connection Timeout
Response Size Limits
```

---

## 38. URL Validation

URLs shall be parsed using a trusted URL parser.

String-prefix validation shall not be considered sufficient.

---

## 39. Redirect Security

API-generated redirects shall prevent open redirect vulnerabilities.

---

## 40. File Upload API Security

File APIs shall enforce:

```text
Maximum File Size
MIME Validation
Magic-Byte Validation
Extension Validation
Filename Sanitization
Malware Scanning
Storage Isolation
Authorization
```

---

## 41. Path Traversal

User-controlled paths shall never directly access filesystem resources.

---

## 42. API Response Security

Responses shall exclude unauthorized fields.

---

## 43. Field-Level Authorization

Sensitive fields shall be conditionally returned based on:

```text
Role
Permission
Tenant
Resource
Data Classification
```

---

## 44. Sensitive Data Exposure Prevention

API responses shall not expose:

```text
Passwords
Password Hashes
Private Keys
OAuth Client Secrets
API Keys
Access Tokens
Refresh Tokens
Encryption Keys
Database Credentials
Internal Secrets
```

---

## 45. Data Masking

Sensitive fields may be returned only in masked form where operationally necessary.

Example:

```text
sk_live_************9a8f
```

---

## 46. API Error Model

Errors shall use a consistent schema.

Example:

```json
{
  "error": {
    "code": "FORBIDDEN",
    "message": "You do not have permission to perform this operation.",
    "request_id": "req_123456"
  }
}
```

---

## 47. Error Information Disclosure

Production APIs shall not expose:

```text
Stack Traces
SQL Statements
Filesystem Paths
Internal IP Addresses
Environment Variables
Secret Values
Service Credentials
Framework Debug Information
```

---

## 48. HTTP Status Codes

APIs shall use consistent status codes:

```text
200 OK
201 Created
202 Accepted
204 No Content

400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
405 Method Not Allowed
409 Conflict
413 Payload Too Large
415 Unsupported Media Type
422 Unprocessable Entity
429 Too Many Requests

500 Internal Server Error
502 Bad Gateway
503 Service Unavailable
```

---

## 49. Enumeration Protection

APIs shall prevent unauthorized enumeration of:

```text
Users
Tenants
Leads
Contacts
Conversations
Files
Integrations
API Keys
Invoices
Agents
Workflows
```

---

## 50. Resource Identifiers

Security-sensitive resources shall use non-predictable identifiers where appropriate.

---

## 51. API Rate Limiting

Rate limits shall support multiple dimensions:

```text
IP
User
Tenant
API Key
Service
Agent
Workflow
Endpoint
Integration
```

---

## 52. Rate-Limit Tiers

Different limits shall be configurable for:

```text
Anonymous
Authenticated
Free Plan
Paid Plan
Enterprise
AI Agent
Internal Service
Administrative API
```

---

## 53. Burst Protection

The API gateway shall support burst controls to protect backend services.

---

## 54. Distributed Rate Limiting

Rate limiting shall remain effective across multiple API gateway instances.

---

## 55. Adaptive Rate Limiting

The system may dynamically reduce limits based on:

```text
Risk
Abuse Signals
Authentication Failures
Traffic Spikes
Resource Exhaustion
Security Incidents
```

---

## 56. Brute-Force Protection

Authentication-related endpoints shall implement:

```text
Rate Limits
Progressive Delays
Account Protection
IP Controls
Credential Abuse Detection
```

---

## 57. API Abuse Detection

The system shall detect:

```text
High-Frequency Requests
Enumeration
Credential Stuffing
Token Abuse
Scraping
Anomalous API Patterns
Bulk Export Attempts
```

---

## 58. API Quotas

API quotas shall support:

```text
Requests
Tokens
Data Transfer
Exports
AI Calls
Tool Calls
Workflow Executions
Integration Calls
```

---

## 59. API Cost Protection

Expensive APIs shall enforce:

```text
Quota
Rate Limit
Budget
Concurrency Limit
Timeout
Maximum Payload
Maximum Result Size
```

---

## 60. Timeout Protection

Every outbound API operation shall have explicit timeout limits.

---

## 61. Concurrency Protection

Expensive operations shall enforce maximum concurrent executions.

---

## 62. Circuit Breakers

External dependency failures shall trigger circuit breakers where appropriate.

---

## 63. Retry Security

Retries shall use:

```text
Bounded Attempts
Exponential Backoff
Jitter
Idempotency
Retryable-Error Classification
```

---

## 64. Idempotency

Sensitive state-changing APIs shall support idempotency keys where duplicate requests could cause harm.

Examples:

```text
Payment
Refund
Invoice
Subscription
Email
CRM Update
Lead Creation
Workflow Trigger
```

---

## 65. Replay Protection

Security-sensitive APIs shall detect and reject replayed requests where applicable.

---

## 66. Request Signing

High-risk external APIs may use signed requests.

Signature validation shall include:

```text
Payload
Timestamp
Nonce
Key ID
Algorithm
```

---

## 67. Timestamp Validation

Signed requests shall reject timestamps outside an allowed clock-skew window.

---

## 68. Nonce Validation

Security-sensitive signed APIs shall prevent nonce reuse.

---

## 69. CORS

CORS policies shall use explicit trusted origins.

The API shall not use unrestricted credentialed wildcard origins.

---

## 70. CSRF

Cookie-authenticated APIs shall implement appropriate CSRF protection.

Bearer-token APIs shall still prevent token leakage and unsafe cross-origin behavior.

---

## 71. Security Headers

API responses shall include appropriate headers such as:

```text
Strict-Transport-Security
X-Content-Type-Options
Content-Security-Policy
Referrer-Policy
Permissions-Policy
```

where applicable.

---

## 72. TLS

All production API traffic containing protected data shall use HTTPS/TLS.

---

## 73. TLS Enforcement

HTTP requests shall be redirected or rejected according to deployment architecture.

---

## 74. Internal TLS

Sensitive service-to-service traffic shall use encryption.

---

## 75. Webhook Security

Incoming webhooks shall validate:

```text
Signature
Timestamp
Event ID
Source
Tenant
Payload Schema
Replay Status
```

---

## 76. Webhook Replay Protection

Webhook event identifiers shall be stored for sufficient time to detect duplicate delivery.

---

## 77. Webhook Payload Validation

Webhook payloads shall never be trusted merely because they originate from a configured provider.

---

## 78. Webhook Tenant Binding

Webhook events shall map to the correct tenant using trusted integration metadata.

---

## 79. OAuth API Security

OAuth APIs shall validate:

```text
State
PKCE
Redirect URI
Issuer
Audience
Scopes
Token Expiration
Tenant Binding
```

---

## 80. Integration API Security

Every integration API shall enforce:

```text
Credential Isolation
Scope Restrictions
Tenant Binding
Authorization
Rate Limits
Audit Logging
Credential Revocation
```

---

## 81. API Key Rotation

Integration API keys shall support controlled rotation without unnecessary service interruption.

---

## 82. AI API Gateway

All external LLM calls shall pass through a controlled AI gateway where appropriate.

The gateway shall enforce:

```text
Tenant
Agent
Model
Quota
Budget
Tool Permissions
Prompt Limits
Security Policy
Logging
```

---

## 83. AI API Request Validation

AI-generated requests shall be validated exactly like human requests.

---

## 84. AI Tool API Authorization

Before an AI agent calls an API:

```text
Agent Identity
      |
      v
Tenant Validation
      |
      v
Permission Check
      |
      v
Resource Check
      |
      v
Risk Evaluation
      |
      +---- DENY
      |
      +---- APPROVAL
      |
      v
API Execution
```

---

## 85. AI Prompt Injection Defense

API responses containing external content shall not be treated as trusted instructions by AI agents.

---

## 86. AI Response Sanitization

External API content returned to AI agents shall be tagged or structured as untrusted data where required.

---

## 87. AI Output Validation

AI-generated API arguments shall pass:

```text
Schema Validation
Permission Validation
Resource Validation
Business Validation
Security Validation
```

---

## 88. MCP API Security

MCP-related APIs shall require:

```text
Authenticated Actor
Authorized Agent
Authorized Tool
Authorized Resource
Validated Parameters
Risk Evaluation
Audit Logging
```

---

## 89. MCP Tool Allowlisting

Only approved MCP tools shall be callable.

---

## 90. MCP High-Risk Operations

The following shall support additional controls:

```text
DELETE
EXPORT
ADMIN
DATABASE_WRITE
FILESYSTEM_WRITE
PRODUCTION_EXECUTION
SECRET_ACCESS
BILLING
```

---

## 91. Workflow API Security

Workflow APIs shall validate:

```text
Workflow Owner
Tenant
Trigger
Action
Tool
Integration
Permissions
Execution Identity
```

---

## 92. Workflow Trigger Security

External requests shall not trigger privileged workflows without authorization.

---

## 93. Scheduled Workflow Security

Scheduled workflows shall execute under dedicated identities with limited permissions.

---

## 94. Background API Security

Background workers shall authenticate when invoking protected APIs.

---

## 95. Queue Message Security

Queue messages shall validate:

```text
Producer
Schema
Tenant
Event Type
Authorization Context
Timestamp
```

---

## 96. Administrative API Security

Administrative APIs shall require:

```text
Strong Authentication
Explicit Role
Permission
Tenant Scope
Audit Logging
```

---

## 97. Super Admin API Security

Super-admin APIs shall support:

```text
MFA
Step-Up Authentication
Session Risk Checks
Detailed Audit
Approval for Critical Actions
```

---

## 98. Billing API Security

Billing APIs shall require explicit billing permissions.

Protected operations include:

```text
Create Subscription
Change Plan
Cancel Subscription
Refund
Modify Payment Method
View Invoice
Export Billing Data
Apply Coupon
Modify Credits
```

---

## 99. Payment API Security

Payment APIs shall:

```text
Avoid unnecessary storage of sensitive payment credentials
Use trusted payment-provider integrations
Validate transaction state
Prevent duplicate processing
Audit payment mutations
```

---

## 100. Lead Intelligence API Security

Lead APIs shall protect:

```text
Lead Data
Contact Data
Company Data
Research Data
Exports
Scoring Results
Enrichment Data
```

---

## 101. Bulk API Security

Bulk APIs shall enforce:

```text
Maximum Records
Maximum Payload
Authorization
Quota
Rate Limits
Async Processing
Audit Logging
```

---

## 102. Bulk Export Security

Bulk exports shall support:

```text
Permission Check
Data Classification
Risk Evaluation
Approval
Audit
Expiring Download Links
```

---

## 103. Signed Download URLs

Generated download URLs shall:

```text
Expire
Be Scoped
Be Non-Guessable
Be Revocable Where Supported
```

---

## 104. API Versioning

APIs shall use explicit versioning.

Example:

```text
/api/v1/
/api/v2/
```

---

## 105. Security Across Versions

Deprecated API versions shall not bypass newer security controls.

---

## 106. Backward Compatibility

Security patches shall be applied consistently across supported API versions.

---

## 107. API Deprecation

Deprecated APIs shall have:

```text
Deprecation Date
Migration Path
Usage Monitoring
Security Review
Retirement Date
```

---

## 108. OpenAPI Security

Every API shall maintain an explicit OpenAPI contract defining:

```text
Endpoints
Methods
Request Schemas
Response Schemas
Authentication
Scopes
Errors
Rate Limits
```

---

## 109. API Contract Validation

CI/CD shall validate that implementation matches the declared API security contract.

---

## 110. API Documentation Security

Documentation shall not expose:

```text
Production Secrets
Private Endpoints
Internal Credentials
Sensitive Infrastructure
```

---

## 111. API Logging

API security logs shall record:

```text
Request ID
Timestamp
Actor
Actor Type
Tenant
Endpoint
Method
Resource
Action
Result
Status Code
Source
Risk
```

---

## 112. API Log Sanitization

API logs shall redact:

```text
Authorization Headers
Cookies
API Keys
Passwords
OAuth Tokens
Payment Credentials
Secrets
Sensitive Payload Fields
```

---

## 113. Audit Logging

The following API operations shall generate audit events:

```text
Login
Logout
Token Refresh
API Key Creation
API Key Rotation
API Key Revocation
Permission Change
Role Change
Data Export
Administrative Action
Billing Mutation
Refund
Integration Connection
Integration Disconnection
AI Tool Execution
MCP Execution
Workflow Execution
Sensitive Data Access
```

---

## 114. Audit Event Integrity

Security audit events shall be:

```text
Immutable
Timestamped
Access-Controlled
Tamper-Evident
Tenant-Aware
Traceable
```

---

## 115. Security Monitoring

API monitoring shall detect:

```text
401 Spikes
403 Spikes
429 Spikes
5xx Spikes
Enumeration
Credential Abuse
Token Abuse
Unusual Data Access
Cross-Tenant Attempts
Bulk Exports
AI Tool Abuse
MCP Abuse
Webhook Abuse
```

---

## 116. API Security Alerts

Alerts shall support severity levels:

```text
LOW
MEDIUM
HIGH
CRITICAL
```

---

## 117. Security Alert Examples

```text
Repeated Failed Authentication
Unusual Admin API Access
Cross-Tenant Access Attempt
Large Data Export
Credential Abuse
API Key Misuse
Unexpected Service Identity
MCP Tool Abuse
AI Agent Permission Violation
```

---

## 118. Automated Response

The platform may automatically:

```text
Block IP
Throttle User
Revoke Token
Revoke API Key
Disable Integration
Disable Agent
Suspend Workflow
Require MFA
Require Human Approval
```

according to policy.

---

## 119. API Security Incident Response

Incidents shall follow:

```text
Detection
    |
Classification
    |
Investigation
    |
Containment
    |
Eradication
    |
Recovery
    |
Post-Incident Review
```

---

## 120. API Security Testing

SalesGenie shall implement:

```text
Unit Tests
Integration Tests
Contract Tests
Authorization Tests
Tenant Isolation Tests
Authentication Tests
Fuzz Tests
SAST
DAST
Dependency Scanning
Penetration Testing
Load Testing
Abuse Testing
AI Red Teaming
MCP Security Testing
```

---

## 121. API Authorization Test Matrix

Security tests shall verify:

```text
User A cannot access User B resources.

Tenant A cannot access Tenant B resources.

End User cannot access Admin APIs.

Sales Agent cannot access Security Admin APIs.

Billing Admin cannot modify security policies.

AI Agent cannot call unauthorized APIs.

AI Agent cannot access another tenant.

Workflow cannot exceed its permissions.

MCP cannot bypass API authorization.

Revoked credentials cannot access protected endpoints.

Expired tokens cannot access protected endpoints.
```

---

## 122. API Fuzz Testing

APIs shall be tested using:

```text
Malformed JSON
Oversized JSON
Invalid Types
Unexpected Fields
Null Values
Empty Values
Unicode
Deeply Nested Objects
Duplicate Parameters
Malformed Headers
Invalid Encodings
Boundary Values
```

---

## 123. Security Regression Tests

Security regression tests shall execute automatically in CI/CD.

---

## 124. CI/CD API Security Gates

Production deployment shall require:

```text
Unit Tests
Integration Tests
API Contract Tests
Authorization Tests
Tenant Isolation Tests
SAST
Dependency Scan
Secret Scan
DAST
Security Regression Tests
```

---

## 125. Critical Vulnerability Gate

Critical API security vulnerabilities shall block production deployment unless formally risk-accepted through an authorized process.

---

## 126. Dependency Security

API dependencies shall be continuously scanned for known vulnerabilities.

---

## 127. Supply Chain Security

API services shall validate:

```text
Dependency Integrity
Build Integrity
Container Integrity
Source Integrity
Artifact Integrity
```

---

## 128. Container Security

API containers shall use:

```text
Minimal Base Images
Non-Root Execution
Read-Only Filesystem Where Possible
Dropped Linux Capabilities
Resource Limits
Image Scanning
Secret Isolation
```

---

## 129. Resource Exhaustion Protection

APIs shall protect:

```text
CPU
Memory
Database Connections
Redis Connections
Queue Capacity
File Storage
Network Connections
AI Tokens
External API Quotas
```

---

## 130. Database API Protection

API services shall use:

```text
Parameterized Queries
Least-Privilege DB Users
Connection Pool Limits
Query Timeouts
Transaction Limits
Tenant-Aware Queries
```

---

## 131. Cache API Security

Cache keys shall include tenant/resource boundaries where required.

Example:

```text
tenant:{tenant_id}:lead:{lead_id}
```

---

## 132. Search API Security

Search APIs shall apply authorization filters before returning records.

---

## 133. Vector Search Security

Vector search APIs shall enforce:

```text
Tenant Filter
Document Permission
User Permission
Role
Classification
```

before returning results.

---

## 134. RAG API Security

RAG APIs shall never retrieve documents solely because they are semantically similar.

Authorization shall be evaluated before retrieval results are exposed.

---

## 135. Conversation API Security

Conversation APIs shall validate:

```text
Tenant
Conversation Owner
Participant
Role
Channel
Permission
```

---

## 136. Customer Data API Security

Customer data APIs shall minimize fields returned to each actor.

---

## 137. Communication API Security

Before sending a message through an API, the platform shall validate:

```text
Sender
Recipient
Tenant
Channel
Permission
Message
Campaign
Rate Limit
Risk
```

---

## 138. Email API Security

Email APIs shall protect:

```text
Sender Identity
Recipient Data
OAuth Credentials
Message Content
Attachments
Tenant Context
```

---

## 139. Social API Security

Social APIs shall enforce:

```text
Account Ownership
Tenant Binding
OAuth Scope
Action Authorization
Rate Limits
Audit
```

---

## 140. CRM API Security

CRM APIs shall enforce:

```text
Tenant
Object Permission
Field Permission
Integration Scope
User Role
```

---

## 141. External API Security

External API calls shall enforce:

```text
Credential Isolation
Allowlisted Destinations
TLS
Timeout
Rate Limit
Response Size Limit
Schema Validation
Audit
```

---

## 142. External API Response Security

External responses shall not automatically be trusted as:

```text
Instructions
Commands
Application Configuration
Security Policy
Permissions
```

---

## 143. AI API Data Leakage Prevention

The API layer shall prevent AI agents from receiving data beyond their authorized scope.

---

## 144. Prompt Injection via API Responses

API responses containing attacker-controlled content shall be marked as untrusted before entering AI contexts.

---

## 145. AI API Cost Controls

Each tenant and agent shall have configurable:

```text
Requests Per Minute
Requests Per Hour
Token Budget
Concurrent Calls
Tool Calls
Workflow Calls
External API Calls
```

---

## 146. API Security Risk Engine

High-risk API operations may be evaluated using:

```text
Actor
Tenant
Resource
Action
Authentication Strength
Device
IP
Behavior
Agent
Workflow
Tool
Data Classification
Historical Activity
```

---

## 147. Human Approval

The API layer shall support approval gates for high-risk operations.

Example:

```text
AI Request
    |
    v
API Authorization
    |
    v
Risk Engine
    |
    +---- LOW ------> Execute
    |
    +---- HIGH -----> Human Approval
    |
    +---- CRITICAL -> Dual Approval
```

---

## 148. Security Invariants

The following shall always remain true:

```text
1. Authentication never implies authorization.

2. Frontend controls never establish authorization.

3. Internal network origin never implies trust.

4. Tenant ID supplied by a client never independently establishes access.

5. AI identity never implies unrestricted API access.

6. Tool availability never implies tool authorization.

7. Workflow ownership never implies unrestricted API access.

8. External API responses are untrusted.

9. Webhook payloads are untrusted until verified.

10. API errors never expose secrets.

11. Security failures default to deny.

12. Revoked credentials cannot access protected APIs.

13. Expired tokens cannot access protected APIs.

14. Cross-tenant access is prohibited unless explicitly authorized by design.

15. Sensitive API operations are auditable.

16. Critical vulnerabilities block production deployment.

17. API rate limits cannot be bypassed through alternate API gateways.

18. AI-generated requests are subject to the same server-side authorization as human requests.

19. MCP calls cannot bypass API authorization.

20. Workflow calls cannot bypass API authorization.
```

---

## 149. API Security Architecture

```text
                         INTERNET
                            |
                            v
                    +---------------+
                    | WAF / DDoS    |
                    +---------------+
                            |
                            v
                    +---------------+
                    | API Gateway   |
                    +---------------+
                            |
             +--------------+--------------+
             |              |              |
             v              v              v
       Rate Limiter     AuthN/AuthZ     Threat Engine
             |              |              |
             +--------------+--------------+
                            |
                            v
                    Request Validation
                            |
                            v
                    Tenant Resolution
                            |
                            v
                    Resource Authorization
                            |
             +--------------+--------------+
             |              |              |
             v              v              v
         AI Gateway    Business APIs    Admin APIs
             |              |              |
             v              v              v
          Agents        Services       Billing
             |
             v
         MCP Layer
             |
             v
       Authorized Tools
             |
             +-----------------------------+
                                           |
                                           v
                                    Data / External APIs
                                           |
                                           v
                                    Output Validation
                                           |
                                           v
                                      Audit Log
                                           |
                                           v
                                      Monitoring
```

---

## 150. Secure API Request Lifecycle

```text
REQUEST
   |
   v
TLS Validation
   |
   v
WAF
   |
   v
Request Size Validation
   |
   v
Rate Limit
   |
   v
Authentication
   |
   v
Token Validation
   |
   v
Tenant Resolution
   |
   v
Schema Validation
   |
   v
Authorization
   |
   v
Object-Level Authorization
   |
   v
Risk Evaluation
   |
   +------ DENY
   |
   +------ APPROVAL
   |
   v
Business Logic
   |
   v
Database / AI / MCP / Integration
   |
   v
Output Authorization
   |
   v
Response Validation
   |
   v
Audit
   |
   v
Monitoring
   |
   v
RESPONSE
```

---

## 151. AI API Request Lifecycle

```text
USER
 |
 v
AUTHENTICATION
 |
 v
AI REQUEST
 |
 v
AI GATEWAY
 |
 v
TENANT VALIDATION
 |
 v
AGENT AUTHORIZATION
 |
 v
PROMPT / INPUT VALIDATION
 |
 v
LLM
 |
 v
AI ACTION
 |
 v
STRUCTURED SCHEMA VALIDATION
 |
 v
API AUTHORIZATION
 |
 v
RESOURCE AUTHORIZATION
 |
 v
RISK ENGINE
 |
 +---- DENY
 |
 +---- HUMAN APPROVAL
 |
 v
API EXECUTION
 |
 v
RESPONSE VALIDATION
 |
 v
DATA FILTERING
 |
 v
AUDIT
 |
 v
USER
```

---

## 152. Security Decision Model

Effective API authorization shall be conceptually modeled as:

```text
Access =
Identity
∩ Tenant
∩ Role
∩ Permission
∩ Resource
∩ Action
∩ Agent Policy
∩ Workflow Policy
∩ Tool Policy
∩ Data Policy
∩ Risk Policy
∩ Approval Policy
```

---

## 153. API Security SLOs

The platform shall define measurable security objectives including:

```text
Authentication Failure Detection
Authorization Failure Detection
Credential Revocation Latency
Security Alert Latency
Security Event Processing Latency
Rate-Limit Enforcement Accuracy
Audit Event Delivery Reliability
Critical Vulnerability Remediation Time
```

---

## 154. Security Metrics

SalesGenie shall monitor:

```text
Authentication Failure Rate
401 Rate
403 Rate
429 Rate
5xx Rate
Authorization Denial Rate
API Key Usage
Token Revocations
Credential Rotations
Cross-Tenant Attempts
Enumeration Attempts
Bulk Export Events
SSRF Attempts
Injection Attempts
Webhook Verification Failures
AI Tool Denials
MCP Denials
Workflow Security Violations
API Abuse Incidents
Mean Time To Detect
Mean Time To Respond
Mean Time To Contain
```

---

## 155. API Security Dashboard

Authorized security administrators shall be able to view:

```text
API Traffic
Authentication Events
Authorization Events
Rate-Limit Events
Blocked Requests
API Key Activity
Token Activity
Security Alerts
Cross-Tenant Attempts
AI API Activity
MCP API Activity
Webhook Activity
Admin API Activity
Bulk Exports
Security Incidents
```

---

## 156. API Security Acceptance Criteria

## AC-APISEC-001

Every protected API endpoint requires authentication.

## AC-APISEC-002

Every protected API operation enforces server-side authorization.

## AC-APISEC-003

Object-level authorization prevents unauthorized resource access.

## AC-APISEC-004

Tenant isolation prevents cross-tenant access.

## AC-APISEC-005

JWT signatures, issuer, audience, and expiration are validated.

## AC-APISEC-006

Revoked credentials cannot access protected APIs.

## AC-APISEC-007

Expired credentials cannot access protected APIs.

## AC-APISEC-008

API keys support scopes, rotation, expiration, and revocation.

## AC-APISEC-009

Sensitive credentials are not exposed through API responses.

## AC-APISEC-010

Mass assignment is prevented.

## AC-APISEC-011

SQL injection protections are verified.

## AC-APISEC-012

SSRF protections are verified.

## AC-APISEC-013

Request size limits are enforced.

## AC-APISEC-014

Rate limiting is enforced.

## AC-APISEC-015

Abuse detection is operational.

## AC-APISEC-016

Webhook signatures are validated.

## AC-APISEC-017

Replay protection exists for applicable security-sensitive APIs.

## AC-APISEC-018

CORS policies are restricted.

## AC-APISEC-019

Production errors do not expose internal implementation details.

## AC-APISEC-020

Security-sensitive API activity is audited.

## AC-APISEC-021

AI API requests receive explicit authorization.

## AC-APISEC-022

AI-generated API arguments are independently validated.

## AC-APISEC-023

AI agents cannot cross tenant boundaries.

## AC-APISEC-024

MCP operations cannot bypass API authorization.

## AC-APISEC-025

Workflow operations cannot bypass API authorization.

## AC-APISEC-026

High-risk API actions can require human approval.

## AC-APISEC-027

Bulk exports are authorization-controlled and audited.

## AC-APISEC-028

Critical API vulnerabilities block production deployment.

## AC-APISEC-029

API security regression tests run automatically.

## AC-APISEC-030

Security incidents can be detected and investigated through API telemetry.

---

## 157. FAANG-Level API Security Quality Gates

```text
[ ] Zero-trust API architecture
[ ] API gateway
[ ] WAF
[ ] DDoS protection
[ ] Authentication
[ ] JWT validation
[ ] OAuth/OIDC
[ ] API key security
[ ] Service identity
[ ] mTLS where appropriate
[ ] RBAC
[ ] ABAC
[ ] Object-level authorization
[ ] Function-level authorization
[ ] Tenant isolation
[ ] Input validation
[ ] Output validation
[ ] Mass assignment protection
[ ] SQL injection protection
[ ] NoSQL injection protection
[ ] Command injection protection
[ ] SSRF protection
[ ] Path traversal protection
[ ] File upload protection
[ ] Request size limits
[ ] Pagination limits
[ ] Query validation
[ ] CORS
[ ] CSRF
[ ] TLS
[ ] Security headers
[ ] Rate limiting
[ ] Adaptive throttling
[ ] Abuse detection
[ ] API quotas
[ ] Cost controls
[ ] Timeout controls
[ ] Circuit breakers
[ ] Retry controls
[ ] Idempotency
[ ] Replay protection
[ ] Webhook signatures
[ ] OAuth security
[ ] Integration security
[ ] AI API security
[ ] Prompt injection defense
[ ] AI output validation
[ ] AI authorization
[ ] AI cost controls
[ ] MCP authorization
[ ] MCP allowlisting
[ ] Workflow authorization
[ ] Admin API protection
[ ] Billing API protection
[ ] Payment API protection
[ ] Bulk export protection
[ ] Sensitive-field filtering
[ ] Secure errors
[ ] Audit logging
[ ] API monitoring
[ ] Security alerts
[ ] Incident response
[ ] SAST
[ ] DAST
[ ] Dependency scanning
[ ] Secret scanning
[ ] Fuzz testing
[ ] Penetration testing
[ ] API contract testing
[ ] Tenant isolation testing
[ ] Authorization regression testing
[ ] AI red-team testing
[ ] MCP security testing
[ ] CI/CD security gates
```

---

## 158. Definition of Done

`api_security.md` shall be considered fully implemented when SalesGenie provides end-to-end API security for:

```text
Human APIs
AI APIs
Agent APIs
MCP APIs
Workflow APIs
Integration APIs
Webhook APIs
Authentication APIs
Authorization APIs
Lead APIs
Conversation APIs
Customer APIs
CRM APIs
Email APIs
Social APIs
Billing APIs
Payment APIs
Subscription APIs
Invoice APIs
Admin APIs
Super Admin APIs
Search APIs
RAG APIs
File APIs
Export APIs
Internal Microservice APIs
Background Worker APIs
```

The final security model shall ensure:

```text
UNTRUSTED REQUEST
        |
        v
       TLS
        |
        v
       WAF
        |
        v
   RATE LIMIT
        |
        v
 AUTHENTICATION
        |
        v
 TOKEN VALIDATION
        |
        v
 TENANT RESOLUTION
        |
        v
 INPUT VALIDATION
        |
        v
 AUTHORIZATION
        |
        v
 OBJECT AUTHORIZATION
        |
        v
 RISK EVALUATION
        |
   +----+----+
   |         |
  DENY    APPROVAL
   |         |
   |         v
   |      HUMAN
   |      APPROVAL
   |         |
   +---------+
        |
        v
 BUSINESS LOGIC
        |
        v
 DATABASE / AI / MCP / WORKFLOW / INTEGRATION
        |
        v
 OUTPUT AUTHORIZATION
        |
        v
 RESPONSE VALIDATION
        |
        v
 AUDIT LOG
        |
        v
 MONITORING
        |
        v
 SECURE RESPONSE
```

SalesGenie shall ensure that **every API request is authenticated, every protected operation is authorized, every resource is tenant-scoped, every input is validated, every sensitive response is filtered, every high-risk AI/MCP/workflow action is controlled, and every security-sensitive operation is auditable.**
