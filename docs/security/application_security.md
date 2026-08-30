# SalesGenie — Application Security Requirements

**Document:** `application_security.md`  
**Product:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Requirement Level:** FAANG-Level / Production-Grade  
**Security Scope:** Human Users + AI Agents + Multi-Agent Orchestration + MCP + APIs + Microservices + Web Application + Integrations + Workflows + Data + Billing + Administration

---

## 1. Purpose

SalesGenie shall implement defense-in-depth application security covering the complete application lifecycle:

```text
Browser
   |
   v
Frontend
   |
   v
API Gateway / WAF
   |
   v
Authentication
   |
   v
Authorization
   |
   v
Application Services
   |
   +---- AI Gateway
   |       |
   |       +---- Agents
   |       +---- LLM Providers
   |       +---- MCP Tools
   |
   +---- Workflow Engine
   |
   +---- Integration Platform
   |
   +---- Business Services
   |
   v
Data Layer
```

Security shall apply equally to:

* Human-generated actions
* AI-generated actions
* AI-assisted human actions
* Background jobs
* Scheduled workflows
* Webhooks
* Service-to-service requests
* MCP tool calls
* External integrations

---

## 2. Application Security Objectives

SalesGenie shall:

1. Prevent unauthorized access.
2. Prevent privilege escalation.
3. Protect tenant boundaries.
4. Protect authentication credentials.
5. Protect sessions and tokens.
6. Prevent injection attacks.
7. Prevent cross-site attacks.
8. Protect APIs.
9. Protect sensitive customer data.
10. Protect AI agents from abuse.
11. Prevent AI-driven data leakage.
12. Secure MCP tool execution.
13. Secure workflow execution.
14. Secure integrations.
15. Protect administrative functionality.
16. Prevent malicious file uploads.
17. Protect against SSRF.
18. Protect against automated abuse.
19. Provide comprehensive auditability.
20. Detect and contain application security incidents.
21. Fail securely.
22. Maintain security throughout the SDLC.

---

## 3. Security Principles

## APPSEC-PRINCIPLE-001 — Defense in Depth

No single security control shall be considered sufficient.

---

## APPSEC-PRINCIPLE-002 — Secure by Default

New features, endpoints, resources, agents, workflows, and integrations shall default to the most restrictive secure configuration.

---

## APPSEC-PRINCIPLE-003 — Least Privilege

Every human, AI agent, service, workflow, and integration shall receive only the permissions required.

---

## APPSEC-PRINCIPLE-004 — Fail Securely

Security validation failures shall result in denial rather than permissive fallback behavior.

---

## APPSEC-PRINCIPLE-005 — Complete Mediation

Protected operations shall be authorized every time they are executed.

---

## APPSEC-PRINCIPLE-006 — Assume Untrusted Input

All external input shall be treated as untrusted.

This includes:

```text
HTTP Requests
Form Data
Query Parameters
JSON
Headers
Cookies
Files
URLs
Emails
CRM Records
Webhooks
AI Prompts
AI Outputs
RAG Documents
MCP Results
Third-Party API Responses
```

---

## 4. Actors

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
AI-007 Security Agent
AI-008 MCP Agent
AI-009 Multi-Agent Orchestrator
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

## UR-APPSEC-001 — Secure Authentication

Users shall authenticate through approved authentication mechanisms before accessing protected functionality.

---

## UR-APPSEC-002 — Secure Sessions

Users shall have secure, revocable sessions with controlled expiration.

---

## UR-APPSEC-003 — MFA

Users shall be able to use multi-factor authentication where enabled by policy.

---

## UR-APPSEC-004 — Permission Enforcement

Users shall only access functionality permitted by their assigned roles and policies.

---

## UR-APPSEC-005 — Tenant Isolation

Users shall only access data belonging to authorized organizations.

---

## UR-APPSEC-006 — Secure Integrations

Users shall be able to connect external integrations through secure authorization flows.

---

## UR-APPSEC-007 — Security Visibility

Authorized users shall be able to view relevant security events, sessions, and account activity.

---

## UR-APPSEC-008 — Credential Revocation

Users and authorized administrators shall be able to revoke applicable credentials and sessions.

---

## UR-APPSEC-009 — Secure File Handling

Users shall receive secure validation and feedback when uploading files.

---

## UR-APPSEC-010 — Security Notifications

Users shall receive notifications for configured security-sensitive events.

---

## 6. AI User Requirements

## AI-UR-APPSEC-001 — AI Identity

Every AI agent shall have a unique and auditable identity.

---

## AI-UR-APPSEC-002 — AI Authorization

AI agents shall execute operations only when explicitly authorized.

---

## AI-UR-APPSEC-003 — AI Least Privilege

AI agents shall have restricted:

```text
Tools
Data Sources
Resources
Actions
Scopes
Execution Duration
```

---

## AI-UR-APPSEC-004 — AI Tenant Isolation

AI agents shall never retrieve, infer, expose, or manipulate data belonging to an unauthorized tenant.

---

## AI-UR-APPSEC-005 — AI Tool Security

AI tool calls shall pass authorization and security validation before execution.

---

## AI-UR-APPSEC-006 — AI Output Validation

AI-generated structured actions shall be validated before being executed.

---

## AI-UR-APPSEC-007 — Human Approval

High-risk AI actions shall require human approval according to policy.

---

## AI-UR-APPSEC-008 — Prompt Injection Resistance

External content shall not automatically obtain instruction authority over AI agents.

---

## AI-UR-APPSEC-009 — AI Auditability

AI actions shall be attributable to:

```text
User
Agent
Workflow
Tool
Tenant
Execution
```

---

## 7. System Requirements

## SR-APPSEC-001 — Central Security Architecture

SalesGenie shall maintain a centralized application security architecture with distributed enforcement.

---

## SR-APPSEC-002 — Secure API Architecture

All protected APIs shall implement:

```text
Authentication
Authorization
Input Validation
Output Validation
Rate Limiting
Logging
Error Handling
```

---

## SR-APPSEC-003 — Security Boundary Enforcement

Security boundaries shall exist at:

```text
Frontend
API Gateway
Service
Repository
Database
AI Gateway
Agent Runtime
Tool Runtime
Workflow Runtime
Integration Runtime
```

---

## SR-APPSEC-004 — Tenant-Aware Architecture

All tenant-scoped operations shall maintain validated tenant context.

---

## SR-APPSEC-005 — Security Context Propagation

Security context shall be propagated across asynchronous and synchronous operations.

---

## 8. Secure SDLC

SalesGenie shall implement security throughout:

```text
Requirements
    |
    v
Threat Modeling
    |
    v
Secure Design
    |
    v
Secure Development
    |
    v
Code Review
    |
    v
SAST
    |
    v
Dependency Scanning
    |
    v
DAST
    |
    v
Security Testing
    |
    v
Deployment
    |
    v
Runtime Monitoring
    |
    v
Incident Response
```

---

## 9. Threat Modeling

Every critical feature shall undergo threat modeling.

Threat modeling shall consider:

```text
Assets
Actors
Trust Boundaries
Attack Surface
Threat Actors
Attack Paths
Security Controls
Residual Risk
```

---

## 10. OWASP Application Security Coverage

SalesGenie shall explicitly defend against major web and API attack classes including:

```text
Broken Access Control
Cryptographic Failures
Injection
Insecure Design
Security Misconfiguration
Vulnerable Components
Authentication Failures
Software/Data Integrity Failures
Logging/Monitoring Failures
SSRF
```

---

## 11. Authentication Security

## FR-APPSEC-AUTH-001

Authentication endpoints shall use secure transport.

---

## FR-APPSEC-AUTH-002

Password credentials shall never be stored in plaintext.

---

## FR-APPSEC-AUTH-003

Passwords shall use a modern adaptive password hashing algorithm.

---

## FR-APPSEC-AUTH-004

Authentication attempts shall be rate limited.

---

## FR-APPSEC-AUTH-005

Credential stuffing protections shall be implemented.

---

## FR-APPSEC-AUTH-006

Brute-force attempts shall trigger throttling or blocking.

---

## FR-APPSEC-AUTH-007

Authentication errors shall not reveal sensitive account information.

---

## 12. Password Security

The system shall support:

```text
Minimum Length
Password Strength Validation
Secure Hashing
Password Reset
Password Rotation Policy
Compromised Password Detection
Rate Limiting
```

---

## 13. Password Reset

Password-reset tokens shall be:

```text
Random
Single-Use
Time-Limited
Non-Guessable
Revocable
```

---

## 14. MFA

MFA shall support configurable methods such as:

```text
TOTP
Passkeys
Security Keys
Enterprise Identity Provider
```

---

## 15. Session Management

Every authenticated session shall include:

```text
session_id
user_id
tenant_id
created_at
expires_at
last_activity
authentication_strength
device_context
risk_context
status
```

---

## 16. Session Protection

Sessions shall support:

```text
Expiration
Revocation
Rotation
Idle Timeout
Absolute Timeout
Risk Reauthentication
Concurrent Session Controls
```

---

## 17. Cookie Security

Authentication cookies, where used, shall use appropriate:

```text
Secure
HttpOnly
SameSite
```

attributes.

---

## 18. CSRF Protection

State-changing browser operations shall implement appropriate CSRF protections when cookie-based authentication is used.

---

## 19. JWT Security

JWT validation shall verify:

```text
Signature
Issuer
Audience
Expiration
Not-Before
Subject
Token Type
Tenant Context
Scopes
```

---

## 20. Token Lifetime

Access tokens shall use bounded lifetimes.

Refresh tokens shall support:

```text
Rotation
Revocation
Reuse Detection
Expiration
```

---

## 21. Authorization

Authorization shall be enforced server-side.

Frontend visibility controls shall never be considered sufficient authorization.

---

## 22. RBAC

SalesGenie shall support:

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

## 23. Fine-Grained Permissions

Permissions shall support:

```text
user.read
user.create
user.update
user.delete

lead.read
lead.create
lead.update
lead.delete
lead.export

conversation.read
conversation.create
conversation.update
conversation.export

agent.read
agent.create
agent.update
agent.execute
agent.delete

workflow.read
workflow.create
workflow.update
workflow.execute
workflow.delete

integration.read
integration.connect
integration.update
integration.disconnect

mcp.read
mcp.execute
mcp.admin

billing.read
billing.manage
refund.create

security.read
security.manage

audit.read
```

---

## 24. Object-Level Authorization

Every resource access shall validate:

```text
Actor
Tenant
Resource
Action
Ownership
Policy
```

---

## 25. Broken Access Control Prevention

The system shall prevent:

```text
IDOR
Horizontal Privilege Escalation
Vertical Privilege Escalation
Cross-Tenant Access
Unauthorized Resource Enumeration
Unauthorized Administrative Operations
```

---

## 26. Tenant Isolation

Tenant context shall be derived from authenticated identity and validated authorization context.

Client-provided tenant IDs shall never independently establish authorization.

---

## 27. Database Security

Database access shall use:

```text
Least-Privilege Accounts
Parameterized Queries
Connection Restrictions
Encryption
Audit Logging
```

---

## 28. Row-Level Security

Where appropriate, tenant and resource-level access shall be enforced using database-level controls such as row-level security.

---

## 29. SQL Injection Prevention

All SQL operations shall use:

```text
Parameterized Queries
Prepared Statements
Safe ORM APIs
Strict Input Validation
```

Dynamic SQL shall be prohibited unless explicitly reviewed and safely parameterized.

---

## 30. NoSQL Injection Prevention

Structured query builders and strict input schemas shall be used.

User-controlled query operators shall not be passed directly into database queries.

---

## 31. Command Injection

User-controlled values shall never be directly executed by operating-system shells.

---

## 32. Template Injection

User-controlled data shall not be evaluated as executable template expressions.

---

## 33. LDAP Injection

Where directory integrations are used, LDAP queries shall use safe parameterization and escaping.

---

## 34. XSS Protection

SalesGenie shall protect against:

```text
Stored XSS
Reflected XSS
DOM XSS
```

using:

```text
Output Encoding
Content Sanitization
Content Security Policy
Safe Rendering APIs
```

---

## 35. HTML Sanitization

Rich user-generated content shall be sanitized before rendering.

---

## 36. Content Security Policy

The application shall maintain a restrictive Content Security Policy appropriate to the frontend architecture.

The policy shall minimize:

```text
script-src
connect-src
frame-src
img-src
style-src
font-src
worker-src
```

origins.

---

## 37. Clickjacking Protection

The application shall prevent unauthorized framing using appropriate:

```text
frame-ancestors
X-Frame-Options
```

controls where applicable.

---

## 38. CORS

CORS shall use explicit trusted origins.

Wildcard credentialed origins shall not be permitted.

---

## 39. Security Headers

The application shall implement appropriate security headers including:

```text
Content-Security-Policy
Strict-Transport-Security
X-Content-Type-Options
Referrer-Policy
Permissions-Policy
```

---

## 40. HTTP Request Security

Requests shall be validated for:

```text
Method
Content-Type
Content-Length
Headers
Encoding
Schema
Authentication
Authorization
```

---

## 41. Input Validation

All application inputs shall be validated against explicit schemas.

Validation shall include:

```text
Type
Format
Length
Range
Allowed Values
Encoding
Structure
```

---

## 42. Mass Assignment Protection

API endpoints shall explicitly define writable fields.

Clients shall not be able to modify protected fields through arbitrary JSON properties.

---

## 43. Parameter Pollution

The system shall handle duplicate query parameters and conflicting input representations deterministically.

---

## 44. HTTP Parameter Validation

Endpoints shall reject unexpected parameters where strict schemas are required.

---

## 45. File Upload Security

Uploaded files shall undergo:

```text
Extension Validation
MIME Validation
Magic-Byte Validation
Size Validation
Malware Scanning
Content Sanitization
Filename Sanitization
Storage Isolation
```

---

## 46. Path Traversal Protection

User-controlled filenames and paths shall never directly determine filesystem locations.

---

## 47. Archive Security

Archives shall be protected against:

```text
Zip Bombs
Path Traversal
Recursive Archives
Oversized Extraction
Malicious Files
```

---

## 48. SSRF Protection

Outbound requests shall enforce:

```text
Protocol Allowlist
Domain Allowlist
Private IP Blocking
Loopback Blocking
Metadata Endpoint Blocking
DNS Rebinding Protection
Redirect Validation
Response Size Limits
Timeouts
```

---

## 49. URL Validation

URLs supplied by users or AI agents shall be parsed and validated before network access.

---

## 50. API Security

Every protected API endpoint shall enforce:

```text
Authentication
Authorization
Input Validation
Rate Limiting
Output Filtering
Audit Logging
Error Handling
```

---

## 51. API Rate Limiting

Rate limits shall be configurable per:

```text
User
Tenant
IP
API Key
Agent
Workflow
Endpoint
Integration
```

---

## 52. Abuse Prevention

The system shall detect:

```text
Credential Stuffing
API Enumeration
Mass Scraping
Automated Abuse
Request Flooding
Resource Exhaustion
```

---

## 53. API Enumeration Protection

Sensitive resources shall avoid exposing predictable identifiers where security-sensitive.

Resource enumeration shall require authorization.

---

## 54. GraphQL Security

If GraphQL is used, SalesGenie shall enforce:

```text
Query Depth Limits
Query Complexity Limits
Authorization
Introspection Policy
Rate Limiting
Payload Limits
```

---

## 55. API Response Security

Responses shall not expose:

```text
Passwords
Secrets
Access Tokens
Refresh Tokens
Internal Credentials
Database Credentials
Stack Traces
Internal Security Configuration
```

---

## 56. Error Handling

Production error responses shall be:

```text
Consistent
Minimal
Non-Descriptive Regarding Internals
Traceable Using Correlation IDs
```

---

## 57. Exception Handling

Unhandled exceptions shall not expose:

```text
Stack Traces
Source Code
SQL
Environment Variables
File Paths
Credentials
Internal Network Details
```

---

## 58. Logging Security

Logs shall never contain:

```text
Passwords
Access Tokens
Refresh Tokens
API Keys
OAuth Secrets
Encryption Keys
Payment Credentials
Sensitive Customer Data
```

unless explicitly required and securely protected.

---

## 59. Audit Logging

Security-sensitive operations shall generate immutable audit events.

Events shall include where applicable:

```text
event_id
timestamp
tenant_id
actor_id
actor_type
agent_id
service_id
action
resource_type
resource_id
result
request_id
trace_id
risk_level
```

---

## 60. Log Integrity

Security logs shall be:

```text
Tamper-Evident
Access-Controlled
Timestamped
Append-Oriented
Retained According to Policy
```

---

## 61. Secrets Management

Application secrets shall be stored using a dedicated secrets-management mechanism.

Secrets shall not be committed to source control.

---

## 62. Secret Detection

CI/CD shall scan for:

```text
API Keys
Private Keys
Tokens
Passwords
Database Credentials
Cloud Credentials
OAuth Secrets
```

---

## 63. Secret Rotation

Secrets shall support:

```text
Automatic Rotation
Manual Rotation
Emergency Rotation
Versioning
Revocation
```

---

## 64. Cryptography

Sensitive information shall be encrypted:

```text
In Transit
At Rest
In Backups
During Credential Storage
```

---

## 65. TLS

External and internal sensitive communication shall use modern TLS configurations.

---

## 66. Key Management

Cryptographic keys shall support:

```text
Access Control
Rotation
Versioning
Revocation
Auditing
Secure Storage
```

---

## 67. Sensitive Data Protection

Sensitive data shall be classified.

Example:

```text
PUBLIC
INTERNAL
CONFIDENTIAL
SENSITIVE
HIGHLY_SENSITIVE
```

---

## 68. Data Minimization

Applications shall collect, process, store, and expose only the data necessary for the requested business operation.

---

## 69. Data Masking

Sensitive information shall be masked in administrative interfaces, logs, and diagnostics where full visibility is unnecessary.

---

## 70. Data Export Security

Exports shall require explicit authorization.

High-risk exports shall support:

```text
Risk Evaluation
Approval
Audit Logging
Rate Limiting
Expiration
```

---

## 71. Background Job Security

Background workers shall authenticate and authorize privileged tasks.

Jobs shall not implicitly trust queue messages.

---

## 72. Queue Security

Queue messages shall validate:

```text
Producer Identity
Tenant
Message Type
Schema
Authorization Context
```

---

## 73. Event Security

Event consumers shall validate event authenticity and tenant context.

---

## 74. Webhook Security

Incoming webhooks shall validate:

```text
Signature
Timestamp
Event ID
Source
Payload Schema
Replay Protection
Tenant Mapping
```

---

## 75. Integration Security

Every integration shall have:

```text
Credential Isolation
Scope Restrictions
Tenant Binding
Authorization
Audit Logging
Revocation
Rotation
```

---

## 76. OAuth Security

OAuth implementations shall support:

```text
Authorization Code Flow
PKCE
State Validation
Redirect URI Validation
Scope Minimization
Secure Token Storage
Token Revocation
Tenant Binding
```

---

## 77. API Key Security

API keys shall support:

```text
Scope
Expiration
Rotation
Revocation
Tenant Binding
Usage Monitoring
Audit Logging
```

---

## 78. AI Application Security

AI-specific security controls shall be implemented as an additional application-security layer.

---

## 79. Prompt Security

System instructions shall be isolated from:

```text
User Content
Retrieved Documents
Emails
Web Pages
CRM Data
MCP Results
Third-Party Responses
```

---

## 80. Prompt Injection Defense

The application shall detect and mitigate:

```text
Direct Prompt Injection
Indirect Prompt Injection
Instruction Override
System Prompt Extraction
Context Manipulation
Tool Instruction Injection
```

---

## 81. Trusted Instruction Hierarchy

SalesGenie shall maintain an explicit instruction hierarchy:

```text
Platform Security Policy
        >
Application Policy
        >
Agent Policy
        >
User Request
        >
External Content
```

External content shall never override higher-priority security policy.

---

## 82. AI Input Validation

AI requests shall validate:

```text
Prompt Size
Context Size
Allowed Model
Allowed Tools
Tenant
User
Agent
Task
```

---

## 83. AI Output Validation

AI-generated output shall be validated before:

```text
Database Write
API Call
Email Send
CRM Update
Workflow Trigger
File Operation
MCP Execution
Administrative Operation
```

---

## 84. Structured AI Actions

AI agents shall use structured action schemas for executable operations.

Example:

```json
{
  "action": "crm.update_lead",
  "resource_id": "lead_123",
  "parameters": {
    "status": "qualified"
  }
}
```

The application shall independently authorize the action before execution.

---

## 85. AI Hallucination Safety

AI-generated identifiers, URLs, commands, recipients, financial values, and permissions shall not be trusted without application validation.

---

## 86. AI Data Leakage Prevention

AI systems shall prevent exposure of:

```text
Secrets
System Prompts
Internal Policies
Unauthorized Customer Data
Cross-Tenant Data
Credentials
Private Documents
Internal Infrastructure Information
```

---

## 87. RAG Security

RAG retrieval shall enforce authorization before returning documents to an AI agent.

---

## 88. RAG Metadata Filtering

Vector retrieval shall support security metadata such as:

```text
tenant_id
document_id
owner_id
classification
allowed_roles
allowed_users
```

---

## 89. RAG Poisoning Defense

Documents containing malicious instructions shall be treated as untrusted content.

---

## 90. AI Agent Identity

Each AI agent shall have:

```text
agent_id
tenant_id
owner_id
agent_type
version
status
permissions
allowed_tools
allowed_data_sources
```

---

## 91. Agent Authorization

Agent execution shall validate:

```text
User
Tenant
Agent
Task
Action
Resource
Tool
Risk
Policy
```

---

## 92. Agent Isolation

Agents shall not automatically inherit unrestricted permissions from their creators.

---

## 93. Agent-to-Agent Security

Agent-to-agent communication shall validate:

```text
Source Agent
Destination Agent
Tenant
Task
Requested Action
Requested Data Scope
```

---

## 94. MCP Security

MCP shall be considered a privileged application capability layer.

Every tool execution shall validate:

```text
User
Agent
Tenant
Tool
Action
Resource
Input
Permission
Risk
```

---

## 95. MCP Tool Allowlisting

Only approved MCP tools shall be executable.

---

## 96. MCP Capability Classification

Tools shall be classified:

```text
READ
WRITE
DELETE
NETWORK
FILESYSTEM
DATABASE
EXECUTION
CREDENTIAL
ADMIN
```

---

## 97. MCP Input Validation

Tool arguments shall be validated against explicit schemas before execution.

---

## 98. MCP Output Validation

MCP responses shall be treated as untrusted external data.

---

## 99. MCP Human Approval

High-risk MCP operations shall require human approval.

Examples:

```text
Delete Data
Modify Permissions
Export Sensitive Data
Execute Production Command
Modify Billing
Create Administrative Accounts
Rotate Critical Secrets
```

---

## 100. Workflow Security

Every workflow shall have explicit:

```text
Owner
Tenant
Permissions
Triggers
Actions
Tools
Integrations
Risk Policy
Approval Policy
Version
Status
```

---

## 101. Workflow Authorization

Each privileged workflow action shall be authorized at execution time.

---

## 102. Workflow Isolation

A workflow shall not automatically inherit unrestricted privileges from its creator.

---

## 103. Scheduled Task Security

Scheduled workflows shall use dedicated execution identities.

---

## 104. Browser Security

The frontend shall protect against:

```text
XSS
CSRF
Clickjacking
Token Leakage
Insecure Storage
Malicious Redirects
```

---

## 105. Client-Side Security

The frontend shall never be trusted to enforce:

```text
Authorization
Tenant Isolation
Role Restrictions
Billing Permissions
Administrative Permissions
```

These shall be enforced server-side.

---

## 106. Local Storage Security

Sensitive authentication credentials shall not be unnecessarily stored in browser-accessible persistent storage.

---

## 107. Third-Party JavaScript

Third-party scripts shall be minimized and explicitly reviewed.

---

## 108. Dependency Security

Dependencies shall be continuously evaluated for:

```text
Known Vulnerabilities
Malicious Packages
License Issues
Supply Chain Risk
Abandoned Dependencies
```

---

## 109. Dependency Pinning

Production dependencies shall use controlled versions and integrity verification where supported.

---

## 110. Software Supply Chain

CI/CD shall verify:

```text
Source Integrity
Dependency Integrity
Build Artifacts
Container Images
Secrets
Security Scans
```

---

## 111. Container Security

Containers shall use:

```text
Minimal Base Images
Non-Root Users
Read-Only Filesystems Where Possible
Capability Restrictions
Resource Limits
Image Scanning
Secret Isolation
```

---

## 112. Infrastructure Security

Production infrastructure shall implement:

```text
Network Segmentation
Least-Privilege IAM
Secret Management
Encryption
Logging
Monitoring
Patch Management
```

---

## 113. Service-to-Service Security

Microservices shall authenticate service identities before protected requests.

---

## 114. Service Authorization

Each service shall verify whether the calling service is authorized for the requested operation.

---

## 115. Internal API Security

Internal APIs shall not assume that requests are trusted because they originate from an internal network.

---

## 116. Database Connection Security

Application services shall use dedicated least-privileged database identities.

---

## 117. Cache Security

Cache keys shall preserve tenant and authorization boundaries.

Example:

```text
tenant:{tenant_id}:resource:{resource_id}
```

---

## 118. Object Storage Security

Object storage shall enforce:

```text
Tenant Isolation
Object Authorization
Encryption
Signed URL Expiration
Access Logging
```

---

## 119. Search Security

Search operations shall apply authorization filters before returning results.

---

## 120. Billing Security

Billing operations shall require explicit billing permissions.

High-risk operations shall support:

```text
Step-Up Authentication
Human Approval
Audit Logging
```

---

## 121. Payment Security

Payment information shall be handled through appropriate payment-provider security architecture.

SalesGenie shall avoid storing sensitive payment credentials unless explicitly required and securely designed.

---

## 122. Administrative Security

Administrative functionality shall require:

```text
Strong Authentication
Explicit Authorization
Least Privilege
Audit Logging
Risk Monitoring
```

---

## 123. Super Admin Security

Super-admin operations shall have additional protections:

```text
MFA
Step-Up Authentication
Detailed Audit
Risk Evaluation
Session Monitoring
```

---

## 124. Privileged Operations

Privileged actions shall include:

```text
Create Admin
Delete User
Modify Permissions
Disable Security Control
Export Sensitive Data
Modify Billing
Issue Refund
Delete Tenant Data
Modify Integration Credentials
```

---

## 125. Separation of Duties

Security-sensitive operations shall support separation between:

```text
Organization Admin
Security Admin
Billing Admin
Developer
Auditor
Super Admin
```

---

## 126. Human Approval

The platform shall support configurable approval workflows for high-risk actions.

```text
AI / Human Request
       |
       v
Risk Assessment
       |
       +---- LOW ------> Execute
       |
       +---- HIGH -----> Human Approval
       |
       +---- CRITICAL -> Dual Approval
```

---

## 127. Risk-Based Security

Risk evaluation may consider:

```text
Identity
Authentication Strength
Session
Device
IP
Location
Behavior
Resource
Action
Data Classification
Agent
Tool
Workflow
Integration
Historical Activity
```

---

## 128. Security Monitoring

Security monitoring shall detect:

```text
Authentication Abuse
Authorization Failures
Privilege Escalation
API Abuse
Cross-Tenant Attempts
Token Abuse
Data Exfiltration
AI Abuse
MCP Abuse
Workflow Abuse
Integration Abuse
```

---

## 129. Automated Security Response

Where policy permits, the platform may:

```text
Revoke Session
Revoke Token
Disable API Key
Disable Agent
Disable Tool
Disconnect Integration
Require MFA
Block Request
Restrict Account
Require Human Approval
```

---

## 130. Security Incident Management

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

## 131. Security Audit Dashboard

Authorized security administrators shall be able to inspect:

```text
Authentication Events
Authorization Events
Active Sessions
Security Alerts
API Activity
AI Activity
MCP Activity
Workflow Activity
Integration Activity
Data Exports
Administrative Actions
Security Incidents
```

---

## 132. Security Metrics

SalesGenie shall track:

```text
Authentication Failure Rate
Authorization Denial Rate
MFA Adoption
Session Revocations
Credential Rotations
Security Alerts
Privilege Escalation Attempts
Cross-Tenant Access Attempts
API Abuse
AI Tool Denials
MCP Violations
Prompt Injection Attempts
Data Export Anomalies
Mean Time To Detect
Mean Time To Respond
Mean Time To Contain
```

---

## 133. Security Testing

The application shall implement:

```text
Unit Security Tests
Integration Security Tests
API Security Tests
Authorization Tests
Tenant Isolation Tests
Session Tests
Token Tests
Fuzz Testing
SAST
DAST
Dependency Scanning
Container Scanning
Secret Scanning
Penetration Testing
Threat Modeling
AI Red Teaming
MCP Security Testing
```

---

## 134. Authorization Test Matrix

Tests shall verify:

```text
User A cannot access User B's resources.

Tenant A cannot access Tenant B's resources.

Sales Agent cannot perform Security Admin operations.

Billing Admin cannot modify security policies unless explicitly authorized.

AI Agent cannot execute unauthorized tools.

Agent A cannot invoke Agent B's privileged capabilities.

Workflow cannot exceed configured permissions.

MCP cannot bypass authorization.

RAG cannot retrieve unauthorized documents.

Revoked tokens cannot access protected endpoints.
```

---

## 135. Security Fuzzing

Security-critical APIs shall be fuzz tested for:

```text
Malformed JSON
Unexpected Types
Oversized Payloads
Unicode Abuse
Boundary Values
Nested Objects
Duplicate Parameters
Malformed Headers
Invalid Encodings
```

---

## 136. API Contract Security

API contracts shall explicitly define:

```text
Authentication
Authorization
Request Schema
Response Schema
Error Schema
Rate Limits
Sensitive Fields
```

---

## 137. Security Regression Testing

Security tests shall run automatically before production deployment.

A failed critical security test shall block deployment.

---

## 138. CI/CD Security Gates

Production deployment shall require successful:

```text
Unit Tests
Integration Tests
SAST
Dependency Scan
Secret Scan
Container Scan
Security Regression Tests
```

---

## 139. Critical Vulnerability Policy

Critical security vulnerabilities shall block production deployment until resolved or formally risk-accepted.

---

## 140. Security Configuration Management

Security configuration shall be:

```text
Version Controlled
Validated
Audited
Tested
Reviewable
Rollback Capable
```

---

## 141. Feature Flag Security

Security-sensitive features shall not be enabled merely through client-side feature flags.

Server-side authorization shall remain authoritative.

---

## 142. Security Documentation

Every security-sensitive subsystem shall document:

```text
Threat Model
Trust Boundaries
Authentication
Authorization
Data Classification
Secrets
Attack Surface
Failure Modes
Monitoring
Incident Response
```

---

## 143. Secure Coding Standards

Developers shall follow secure coding practices covering:

```text
Input Validation
Output Encoding
Authentication
Authorization
Cryptography
Error Handling
Logging
Secrets
Database Access
File Handling
Network Requests
Concurrency
```

---

## 144. Code Review Security

Security-sensitive changes shall receive additional review.

Examples:

```text
Authentication
Authorization
Payments
Billing
Tenant Isolation
AI Tools
MCP
File Handling
Secrets
Data Export
Administrative Functions
```

---

## 145. Race Condition Protection

Security-critical operations shall prevent TOCTOU vulnerabilities.

Authorization and state validation shall occur as close as possible to the protected operation.

---

## 146. Idempotency

Sensitive operations shall support idempotency where repeated requests could cause:

```text
Duplicate Payment
Duplicate Refund
Duplicate Email
Duplicate CRM Update
Duplicate Workflow
Duplicate Data Mutation
```

---

## 147. Replay Protection

Security-sensitive requests shall support replay protection where applicable.

---

## 148. Concurrency Controls

Critical operations shall implement appropriate:

```text
Locks
Optimistic Concurrency
Version Checks
Idempotency Keys
Atomic Transactions
```

---

## 149. Transaction Security

Security-sensitive mutations shall use atomic transactions where required to prevent inconsistent security state.

---

## 150. Resource Exhaustion

The application shall protect against:

```text
CPU Exhaustion
Memory Exhaustion
Database Exhaustion
Queue Exhaustion
AI Token Exhaustion
File Storage Exhaustion
Connection Exhaustion
```

---

## 151. AI Resource Abuse

AI usage shall enforce:

```text
Token Limits
Context Limits
Request Limits
Concurrent Execution Limits
Tool Call Limits
Workflow Limits
Tenant Quotas
```

---

## 152. AI Cost Security

AI agents shall not be able to generate unbounded provider costs.

High-cost operations shall be subject to:

```text
Budget
Quota
Rate Limit
Approval
```

---

## 153. Model Provider Security

AI provider credentials shall remain server-side.

Client applications shall not receive unrestricted provider API keys.

---

## 154. Multi-Provider Security

When using multiple LLM providers, each provider credential shall be isolated.

Provider-specific permissions shall be configurable.

---

## 155. AI Provider Failover Security

Automatic failover shall preserve:

```text
Tenant
Authorization
Data Policy
Model Policy
Tool Permissions
Security Policy
```

---

## 156. AI Memory Security

Persistent AI memory shall enforce:

```text
Tenant Isolation
User Authorization
Retention Policy
Deletion Policy
Data Classification
```

---

## 157. Conversation Security

Conversation access shall validate:

```text
Tenant
User
Role
Conversation Ownership
Channel
Permission
```

---

## 158. Customer Support Security

AI and human support agents shall only access customer information necessary for their assigned tasks.

---

## 159. Sales Security

Sales agents shall only access authorized:

```text
Leads
Contacts
Accounts
Opportunities
Campaigns
Conversation Data
```

---

## 160. Lead Generation Security

Lead generation shall enforce:

```text
Data Source Authorization
Tenant Scope
Lead Access
Export Permissions
Communication Permissions
Rate Limits
Compliance Policies
```

---

## 161. Communication Security

Before sending customer communication, the platform shall validate:

```text
Sender
Recipient
Tenant
Channel
Permission
Campaign
Message
Rate Limit
Risk
```

---

## 162. Notification Security

Security-sensitive notifications shall avoid exposing secrets or unnecessary sensitive information.

---

## 163. Email Security

Email integration shall enforce:

```text
OAuth Scope Restrictions
Tenant Binding
Credential Encryption
Sender Authorization
Recipient Validation
Audit Logging
```

---

## 164. Social Integration Security

Social integrations shall enforce:

```text
Account Ownership
OAuth Scope
Tenant Binding
Action Authorization
Rate Limits
Audit Logging
```

---

## 165. CRM Security

CRM integrations shall enforce:

```text
Read Scope
Write Scope
Object-Level Authorization
Field-Level Restrictions
Tenant Binding
Credential Isolation
```

---

## 166. Security for External Data

External data shall be treated as untrusted.

The application shall validate:

```text
Source
Schema
Encoding
Size
Content
Authorization Context
```

---

## 167. Data Poisoning Defense

External records shall not automatically become trusted application configuration or AI instructions.

---

## 168. Security for Documents

Documents shall be scanned and validated before:

```text
Storage
Indexing
RAG Retrieval
AI Processing
Workflow Processing
```

---

## 169. Security for OCR

OCR output shall be treated as untrusted extracted content.

---

## 170. Security for Generated Documents

AI-generated documents shall pass application validation before being:

```text
Stored
Shared
Emailed
Published
Uploaded to External Systems
```

---

## 171. Security for Exports

Bulk exports shall implement:

```text
Authorization
Data Classification
Rate Limits
Audit
Optional Approval
```

---

## 172. Security for Deletion

Deletion shall validate:

```text
Actor
Tenant
Resource
Permission
Retention Policy
Dependencies
Approval Policy
```

---

## 173. Secure Defaults

Default configurations shall:

```text
Deny Unauthorized Access
Disable Unnecessary Features
Use Minimal Permissions
Require Secure Transport
Enable Logging
Use Safe Headers
Restrict External Connections
```

---

## 174. Configuration Validation

The platform shall detect insecure configurations such as:

```text
Debug Mode in Production
Wildcard CORS
Weak Authentication
Disabled TLS
Excessive Permissions
Public Storage
Unrestricted MCP Tools
Unrestricted SSRF
Missing Rate Limits
Missing Authorization
```

---

## 175. Production Security Checklist

```text
[ ] HTTPS enforced
[ ] Secure headers enabled
[ ] CSP configured
[ ] CORS restricted
[ ] Authentication enforced
[ ] MFA supported
[ ] Sessions protected
[ ] Tokens validated
[ ] Authorization enforced
[ ] RBAC implemented
[ ] Object-level authorization implemented
[ ] Tenant isolation enforced
[ ] SQL injection protected
[ ] XSS protected
[ ] CSRF protected
[ ] SSRF protected
[ ] File uploads secured
[ ] Path traversal protected
[ ] Secrets managed securely
[ ] Secrets scanned
[ ] Encryption enabled
[ ] API rate limits enabled
[ ] Abuse detection enabled
[ ] Audit logs enabled
[ ] Security monitoring enabled
[ ] Dependency scanning enabled
[ ] SAST enabled
[ ] DAST enabled
[ ] Container scanning enabled
[ ] AI security controls enabled
[ ] Prompt injection protection enabled
[ ] RAG authorization enabled
[ ] MCP authorization enabled
[ ] Workflow authorization enabled
[ ] Integration authorization enabled
[ ] Human approval configured
[ ] Billing security enabled
[ ] Administrative security enabled
[ ] Incident response configured
[ ] Backup security verified
[ ] Disaster recovery tested
```

---

## 176. AI Security Checklist

```text
[ ] Every AI agent has an identity
[ ] Every AI agent has a tenant
[ ] AI permissions are explicit
[ ] AI tools are allowlisted
[ ] Tool arguments are validated
[ ] Tool responses are treated as untrusted
[ ] AI output is validated
[ ] AI cannot bypass authorization
[ ] AI cannot cross tenants
[ ] RAG respects authorization
[ ] External content cannot override system policy
[ ] Prompt injection defenses enabled
[ ] AI data leakage controls enabled
[ ] AI cost limits enabled
[ ] AI rate limits enabled
[ ] High-risk actions require approval
[ ] AI activity is audited
[ ] AI red-team testing is performed
```

---

## 177. MCP Security Checklist

```text
[ ] MCP servers are explicitly registered
[ ] MCP tools are allowlisted
[ ] Tool permissions are scoped
[ ] Tool arguments are validated
[ ] Tool outputs are sanitized
[ ] MCP calls are authenticated
[ ] MCP calls are authorized
[ ] MCP calls are tenant-scoped
[ ] High-risk tools require approval
[ ] Tool execution is rate limited
[ ] Tool execution is audited
[ ] MCP credentials are protected
[ ] MCP servers are monitored
```

---

## 178. Security Architecture

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
             |                             |
             v                             v
      Authentication                 Risk Engine
             |                             |
             +--------------+--------------+
                            |
                            v
                     Authorization
                            |
                            v
                   Application Services
                            |
       +--------------------+--------------------+
       |                    |                    |
       v                    v                    v
    AI Gateway         Workflow Engine      Integrations
       |                    |                    |
       v                    v                    v
    Agents               Actions             External APIs
       |
       v
   MCP Layer
       |
       v
  Authorized Tools
       |
       +--------------------+
                            |
                            v
                       Data Layer
                            |
       +------------+-------+--------+------------+
       |            |                |            |
       v            v                v            v
   PostgreSQL     Redis        Object Store    Vector DB
```

---

## 179. Secure Request Lifecycle

```text
REQUEST
   |
   v
TLS
   |
   v
WAF
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
Input Validation
   |
   v
Authorization
   |
   v
Risk Evaluation
   |
   +------ DENY ------> REJECT
   |
   +------ APPROVAL --> HUMAN REVIEW
   |
   v
Business Logic
   |
   v
Data Authorization
   |
   v
Database / Tool / Integration
   |
   v
Output Validation
   |
   v
Audit Log
   |
   v
Response
```

---

## 180. AI Request Lifecycle

```text
USER REQUEST
      |
      v
AUTHENTICATE USER
      |
      v
RESOLVE TENANT
      |
      v
AUTHORIZE AI TASK
      |
      v
CREATE AI EXECUTION CONTEXT
      |
      v
AGENT AUTHORIZATION
      |
      v
RAG AUTHORIZATION
      |
      v
LLM PROCESSING
      |
      v
AI ACTION PROPOSED
      |
      v
SCHEMA VALIDATION
      |
      v
TOOL AUTHORIZATION
      |
      v
RISK EVALUATION
      |
      +------ DENY
      |
      +------ APPROVAL
      |
      v
TOOL EXECUTION
      |
      v
RESULT VALIDATION
      |
      v
OUTPUT SECURITY CHECK
      |
      v
AUDIT
      |
      v
USER RESPONSE
```

---

## 181. Security Decision Model

The effective authorization decision shall be based on:

```text
Effective Access
=
Identity
∩
Tenant
∩
Role
∩
Resource Permission
∩
Action Permission
∩
Agent Permission
∩
Tool Permission
∩
Data Policy
∩
Risk Policy
∩
Approval Policy
```

---

## 182. Security Invariants

The following shall always remain true:

```text
1. Authentication never implies authorization.

2. Frontend authorization is never authoritative.

3. Internal network access never implies trust.

4. Tenant IDs supplied by clients never independently establish tenant access.

5. AI agents never receive unrestricted user permissions.

6. Tool availability never implies tool authorization.

7. Workflow ownership never implies unrestricted workflow authority.

8. Retrieved documents never become trusted instructions.

9. MCP tools cannot bypass application authorization.

10. RAG cannot bypass document permissions.

11. External API responses are untrusted.

12. Webhook payloads are untrusted until verified.

13. AI output is untrusted until validated.

14. Security failures default to deny.

15. Sensitive actions are auditable.

16. Secrets never appear in normal logs.

17. Revoked credentials cannot perform protected operations.

18. Cross-tenant access is always prohibited unless explicitly designed and authorized.

19. Critical vulnerabilities block production deployment.

20. Security controls cannot be disabled through client-side code.
```

---

## 183. Security Acceptance Criteria

## AC-APPSEC-001

All protected APIs require authentication.

## AC-APPSEC-002

All protected resources enforce server-side authorization.

## AC-APPSEC-003

Cross-tenant access attempts are rejected.

## AC-APPSEC-004

Horizontal privilege escalation is prevented.

## AC-APPSEC-005

Vertical privilege escalation is prevented.

## AC-APPSEC-006

Authentication credentials are securely stored.

## AC-APPSEC-007

Sessions are revocable and expire.

## AC-APPSEC-008

Sensitive tokens are not exposed to unauthorized clients.

## AC-APPSEC-009

SQL injection defenses are verified.

## AC-APPSEC-010

XSS defenses are verified.

## AC-APPSEC-011

CSRF defenses are verified where applicable.

## AC-APPSEC-012

SSRF defenses are verified.

## AC-APPSEC-013

Malicious file uploads are blocked.

## AC-APPSEC-014

Secrets are absent from source control and logs.

## AC-APPSEC-015

Security-sensitive operations generate audit events.

## AC-APPSEC-016

AI actions are authorized before execution.

## AC-APPSEC-017

MCP tools are allowlisted and authorized.

## AC-APPSEC-018

RAG retrieval respects resource permissions.

## AC-APPSEC-019

AI-generated output cannot directly bypass application security controls.

## AC-APPSEC-020

High-risk AI operations can require human approval.

## AC-APPSEC-021

Workflow actions are independently authorized.

## AC-APPSEC-022

External integrations are isolated and scoped.

## AC-APPSEC-023

Rate limits prevent application abuse.

## AC-APPSEC-024

Critical security vulnerabilities block deployment.

## AC-APPSEC-025

Security incidents can be detected, investigated, and contained.

---

## 184. FAANG-Level Application Security Quality Gates

```text
[ ] Secure architecture
[ ] Threat modeling
[ ] Defense in depth
[ ] Secure defaults
[ ] Least privilege
[ ] Complete mediation
[ ] Authentication
[ ] MFA
[ ] Session security
[ ] Token security
[ ] RBAC
[ ] ABAC
[ ] Object-level authorization
[ ] Tenant isolation
[ ] Input validation
[ ] Output encoding
[ ] SQL injection prevention
[ ] NoSQL injection prevention
[ ] Command injection prevention
[ ] XSS prevention
[ ] CSRF protection
[ ] SSRF protection
[ ] File upload security
[ ] Path traversal protection
[ ] Secure CORS
[ ] CSP
[ ] Security headers
[ ] API rate limiting
[ ] Abuse prevention
[ ] Secure error handling
[ ] Secure logging
[ ] Audit logging
[ ] Secrets management
[ ] Encryption
[ ] Key management
[ ] Dependency security
[ ] Supply-chain security
[ ] Container security
[ ] CI/CD security
[ ] SAST
[ ] DAST
[ ] Dependency scanning
[ ] Secret scanning
[ ] Penetration testing
[ ] AI security
[ ] Prompt injection protection
[ ] RAG security
[ ] AI output validation
[ ] AI authorization
[ ] AI cost controls
[ ] MCP security
[ ] Workflow security
[ ] Integration security
[ ] Webhook security
[ ] Human approval
[ ] Administrative security
[ ] Billing security
[ ] Data export security
[ ] Incident response
[ ] Security monitoring
[ ] Security SLOs
```

---

## 185. Definition of Done

`application_security.md` shall be considered fully implemented when SalesGenie provides defense-in-depth application security across:

```text
Human Users
AI Agents
Multi-Agent Orchestration
MCP Tools
Workflows
Frontend
Backend
APIs
Microservices
Authentication
Authorization
Sessions
Tokens
Databases
Caches
Object Storage
Vector Databases
RAG
External Integrations
OAuth
API Keys
Webhooks
Billing
Payments
Files
Customer Data
Lead Data
Conversations
Administrative Functions
Background Workers
CI/CD
Infrastructure
```

The final application-security model shall be:

```text
               UNTRUSTED INPUT
                      |
                      v
                 VALIDATION
                      |
                      v
               AUTHENTICATION
                      |
                      v
                AUTHORIZATION
                      |
                      v
                TENANT CHECK
                      |
                      v
                 RISK CHECK
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
        DENY       APPROVAL     ALLOW
                                  |
                                  v
                           BUSINESS LOGIC
                                  |
                                  v
                         RESOURCE CHECK
                                  |
                                  v
                    DATABASE / AI / MCP /
                    WORKFLOW / INTEGRATION
                                  |
                                  v
                         OUTPUT VALIDATION
                                  |
                                  v
                              AUDIT
                                  |
                                  v
                            MONITORING
```

SalesGenie shall therefore ensure that **no human, AI agent, service, workflow, integration, API, tool, document, external response, or client-controlled input is inherently trusted**, and that application security controls remain authoritative at the server, service, resource, AI, and execution layers.
