# SalesGenie — Zero Trust Security Requirements

**Document:** `zero_trust_security.md`  
**Product:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Requirement Level:** FAANG-Level / Production-Grade  
**Security Model:** Zero Trust Architecture (ZTA)  
**Scope:** Human Users, AI Agents, Multi-Agent Orchestration, MCP Tools, Workflows, APIs, Microservices, Integrations, Data, Devices, Sessions, Infrastructure, Administrative Operations, and Security Operations

---

## 1. Purpose

SalesGenie shall implement a comprehensive Zero Trust Security Architecture based on the principle:

> **Never trust, always verify.**

No user, device, service, AI agent, workflow, integration, network location, or application shall receive implicit trust based solely on its origin, network position, previous authentication, or system identity.

Every access request shall be evaluated using:

```text
Identity
+
Authentication
+
Authorization
+
Tenant
+
Resource
+
Action
+
Device / Session Context
+
Risk
+
Data Classification
+
Policy
```

The architecture shall protect both:

* Human-driven operations
* AI-driven operations

---

## 2. Zero Trust Security Objectives

SalesGenie shall:

1. Eliminate implicit trust.
2. Authenticate every protected request.
3. Authorize every protected action.
4. Enforce least privilege.
5. Continuously evaluate risk.
6. Isolate tenants.
7. Isolate AI agents.
8. Isolate workflows.
9. Secure MCP tool execution.
10. Protect sensitive data.
11. Secure service-to-service communication.
12. Enforce policy at runtime.
13. Monitor security-relevant activity.
14. Detect anomalous behavior.
15. Support rapid credential/session revocation.
16. Prevent privilege escalation.
17. Protect against AI-specific attacks.
18. Maintain complete security auditability.
19. Fail securely.
20. Assume compromise.

---

## 3. Core Zero Trust Principles

## ZT-PRINCIPLE-001 — Verify Explicitly

Every request shall be evaluated based on current security context.

---

## ZT-PRINCIPLE-002 — Least Privilege

Every identity shall receive only the minimum permissions necessary.

---

## ZT-PRINCIPLE-003 — Assume Breach

The architecture shall assume that:

```text
User Credentials
Devices
Tokens
Services
AI Agents
Integrations
Documents
External APIs
MCP Tools
Networks
```

may become compromised.

---

## ZT-PRINCIPLE-004 — Continuous Verification

Authentication shall not be considered permanent authorization.

---

## ZT-PRINCIPLE-005 — Explicit Trust Boundaries

Every trust boundary shall have explicit authentication and authorization controls.

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
AI-001 AI Sales Agent
AI-002 AI Support Agent
AI-003 AI Lead Generation Agent
AI-004 AI Research Agent
AI-005 AI Workflow Agent
AI-006 AI Customer Success Agent
AI-007 AI Security Agent
AI-008 AI Operations Agent
AI-009 AI MCP Agent
AI-010 Multi-Agent Orchestrator
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
M-010 Database Services
M-011 Event Bus
M-012 Background Workers
```

---

## 5. User Requirements

## UR-ZT-001 — Secure Access

Users shall access SalesGenie only after successful authentication.

---

## UR-ZT-002 — Explicit Authorization

Users shall only access resources and operations explicitly permitted to them.

---

## UR-ZT-003 — Tenant Isolation

Users shall only access resources belonging to authorized organizations.

---

## UR-ZT-004 — Session Visibility

Users shall be able to view active sessions where supported.

---

## UR-ZT-005 — Session Revocation

Users shall be able to revoke their active sessions.

---

## UR-ZT-006 — MFA

Users shall be able to use multi-factor authentication where enabled.

---

## UR-ZT-007 — Security Notifications

Users shall be notified of configured high-risk security events.

---

## UR-ZT-008 — Permission Transparency

Users shall be able to understand the permissions associated with their role where organizational policy permits.

---

## UR-ZT-009 — Integration Authorization

Users shall be able to authorize integrations using scoped credentials.

---

## UR-ZT-010 — AI Authorization

Users shall understand that AI agents operate under explicitly configured permissions.

---

## 6. AI User Requirements

## AI-UR-ZT-001 — AI Identity

Every AI agent shall have a unique identity.

---

## AI-UR-ZT-002 — AI Least Privilege

AI agents shall only access explicitly delegated resources.

---

## AI-UR-ZT-003 — AI Tenant Isolation

AI agents shall never access data outside their authorized tenant context.

---

## AI-UR-ZT-004 — AI Tool Authorization

AI agents shall require authorization before invoking tools.

---

## AI-UR-ZT-005 — Continuous AI Verification

AI authorization shall be evaluated at tool-execution time rather than only when an agent starts.

---

## AI-UR-ZT-006 — AI Human Approval

Configured high-risk AI operations shall require human approval.

---

## AI-UR-ZT-007 — AI Context Security

AI agents shall receive only the minimum context required to perform the requested task.

---

## AI-UR-ZT-008 — AI Data Protection

AI agents shall not expose protected data to unauthorized users, agents, tools, or integrations.

---

## 7. System Requirements

## SR-ZT-001 — Zero Trust Enforcement

SalesGenie shall implement zero-trust controls across:

```text
Frontend
API Gateway
Authentication
Authorization
Microservices
Databases
Caches
Object Storage
Vector Databases
AI Gateway
Agent Runtime
Workflow Engine
MCP Layer
Integrations
Event Bus
Background Workers
Infrastructure
```

---

## SR-ZT-002 — No Implicit Trust

Network location shall never independently determine authorization.

---

## SR-ZT-003 — Central Policy Enforcement

The platform shall provide centralized authorization policies with distributed enforcement.

---

## SR-ZT-004 — Distributed Verification

Each service shall independently validate security context before performing protected operations.

---

## SR-ZT-005 — Secure Defaults

Protected operations shall default to:

```text
DENY
```

unless explicitly authorized.

---

## 8. Zero Trust Architecture

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
                +-----------+-----------+
                |                       |
                v                       v
        Identity Provider        Risk Engine
                |                       |
                +-----------+-----------+
                            |
                            v
                    Policy Decision
                       Point
                            |
                            v
                  Policy Enforcement
                       Point
                            |
             +--------------+--------------+
             |              |              |
             v              v              v
         Human User      AI Agent       Service
             |              |              |
             +--------------+--------------+
                            |
                            v
                    Resource Service
                            |
            +---------------+---------------+
            |               |               |
            v               v               v
         Database       Vector Store     Object Store
```

---

## 9. Zero Trust Policy Model

Every protected operation shall evaluate:

```text
Subject
Action
Resource
Tenant
Environment
Identity
Authentication Strength
Role
Permissions
Device
Session
Network Context
Data Classification
Risk
Time
Location Policy
Agent Identity
Tool Identity
Workflow Identity
```

---

## 10. Authentication Requirements

## FR-ZTAUTH-001

Every protected request shall be authenticated.

---

## FR-ZTAUTH-002

The authentication system shall support configurable authentication mechanisms.

Possible mechanisms:

```text
Email + Password
OAuth/OIDC
Enterprise SSO
SAML
MFA
Passkeys
Magic Links
```

---

## FR-ZTAUTH-003

Authentication credentials shall never be stored in plaintext.

---

## FR-ZTAUTH-004

Authentication attempts shall be rate limited.

---

## FR-ZTAUTH-005

Suspicious authentication activity shall increase risk scores.

---

## 11. Authentication Strength

The system shall assign authentication strength based on:

```text
Password
MFA
Passkey
Hardware Security Key
Enterprise SSO
Device Trust
Step-Up Authentication
```

High-risk operations shall require stronger authentication where configured.

---

## 12. Step-Up Authentication

The system shall support step-up authentication for:

```text
Administrative Privilege Changes
Security Policy Changes
Credential Rotation
Sensitive Data Export
Billing Administration
Refund Operations
Bulk Customer Communication
Critical Integration Changes
Production Operations
```

---

## 13. Session Security

## FR-ZTSESSION-001

Every authenticated session shall have a unique identifier.

---

## FR-ZTSESSION-002

Sessions shall have bounded lifetimes.

---

## FR-ZTSESSION-003

Sessions shall support revocation.

---

## FR-ZTSESSION-004

Risk changes shall be capable of triggering session reauthentication.

---

## FR-ZTSESSION-005

Compromised sessions shall be immediately invalidatable.

---

## 14. Continuous Session Evaluation

A session may be re-evaluated when:

```text
Role Changes
Permission Changes
MFA Changes
Device Changes
Risk Increases
IP / Network Anomaly
Impossible Travel
Sensitive Action
Security Incident
Credential Compromise
```

---

## 15. Token Security

Tokens shall validate:

```text
Signature
Issuer
Audience
Expiration
Not-Before
Subject
Token Type
Tenant
Scopes
```

---

## FR-ZTTOKEN-001

Expired tokens shall always be rejected.

---

## FR-ZTTOKEN-002

Revoked credentials shall not authorize new protected requests.

---

## FR-ZTTOKEN-003

Refresh tokens shall be protected and revocable.

---

## 16. Identity Architecture

```text
User
 |
 +--> Authentication
 |
 +--> Identity
 |
 +--> Tenant Membership
 |
 +--> Roles
 |
 +--> Permissions
 |
 +--> Session
 |
 +--> Risk
 |
 +--> Device Context
 |
 +--> Policy
 |
 v
Authorization Decision
```

---

## 17. Human Identity

Every human identity shall have:

```text
user_id
tenant_id
roles
permissions
status
authentication_methods
session_context
risk_profile
```

---

## 18. AI Identity

Every AI agent shall have:

```text
agent_id
tenant_id
agent_type
owner_id
status
version
permissions
allowed_tools
allowed_data_sources
risk_policy
execution_policy
```

---

## 19. Machine Identity

Every service identity shall have:

```text
service_id
environment
service_role
allowed_services
allowed_operations
credential
status
```

---

## 20. Machine-to-Machine Zero Trust

Internal service calls shall require:

```text
Service Authentication
+
Service Authorization
+
Tenant Context
+
Request Context
```

Network placement alone shall not authorize internal API access.

---

## 21. Service Mesh Security

Where a service mesh is deployed, SalesGenie shall support:

```text
Mutual TLS
Service Identity
Certificate Rotation
Service Authorization
Traffic Policies
Telemetry
```

---

## 22. Microservice Authorization

Each microservice shall verify:

```text
Caller Identity
Caller Permissions
Tenant Context
Requested Resource
Requested Action
```

before executing protected operations.

---

## 23. API Gateway

The API Gateway shall enforce:

```text
Authentication
Rate Limiting
Request Validation
Threat Detection
Tenant Resolution
Token Validation
Security Headers
Request Correlation
```

The gateway shall not be the only authorization layer.

---

## 24. Policy Enforcement Points

Policy enforcement shall exist at multiple layers:

```text
API Gateway
Service Layer
Repository Layer
Database Layer
AI Gateway
Agent Runtime
Tool Runtime
Workflow Engine
Integration Layer
```

---

## 25. Policy Decision Point

The Policy Decision Point shall evaluate authorization requests.

Example:

```text
authorize(
    subject,
    tenant,
    action,
    resource,
    context
)
```

Result:

```text
ALLOW
DENY
REQUIRE_STEP_UP
REQUIRE_HUMAN_APPROVAL
```

---

## 26. RBAC

SalesGenie shall support role-based access control.

Example roles:

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

## 27. Fine-Grained Permissions

Permissions shall include:

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
conversation.export

agent.read
agent.create
agent.update
agent.execute
agent.delete

workflow.read
workflow.create
workflow.execute
workflow.update
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

## 28. ABAC

SalesGenie shall support attribute-based authorization.

Policies may evaluate:

```text
User Role
Tenant
Department
Resource Owner
Resource Classification
Action
Agent
Tool
Workflow
Risk
Device
Session
Environment
Time
```

---

## 29. Tenant Isolation

## FR-ZTTENANT-001

Every tenant-scoped request shall contain validated tenant context.

---

## FR-ZTTENANT-002

Tenant identifiers supplied by users shall never independently determine authorization.

---

## FR-ZTTENANT-003

Tenant isolation shall apply to:

```text
Database
Cache
Object Storage
Search
Vector Store
Events
Queues
AI Context
Logs
Analytics
Files
Integrations
```

---

## 30. Cross-Tenant Protection

The platform shall explicitly prevent:

```text
Cross-Tenant Reads
Cross-Tenant Writes
Cross-Tenant Searches
Cross-Tenant Vector Retrieval
Cross-Tenant Cache Access
Cross-Tenant Event Processing
Cross-Tenant AI Context
Cross-Tenant Exports
```

---

## 31. Data-Level Authorization

Authorization shall be enforced at resource level where required.

Example:

```text
Tenant
  |
  +-- Department
        |
        +-- Team
              |
              +-- User
                    |
                    +-- Resource
```

---

## 32. Database-Level Security

Database access shall use least-privileged credentials.

Where appropriate, SalesGenie shall support:

```text
Row-Level Security
Database Roles
Schema Isolation
Encrypted Columns
Connection Restrictions
Audit Logging
```

---

## 33. Cache Security

Redis/cache access shall preserve tenant and authorization boundaries.

Cache keys shall not allow accidental cross-tenant collisions.

Example:

```text
tenant:{tenant_id}:user:{user_id}:resource:{resource_id}
```

---

## 34. Object Storage Security

Object storage shall enforce:

```text
Tenant Isolation
Object Authorization
Signed URLs
Expiration
Encryption
Access Logging
```

---

## 35. Vector Database Security

Vector searches shall apply authorization filters before returning documents or chunks.

Example metadata:

```text
tenant_id
document_id
owner_id
classification
allowed_roles
allowed_users
```

---

## 36. RAG Zero Trust

RAG shall follow:

```text
User Request
      |
      v
Identity
      |
      v
Authorization
      |
      v
Tenant Filter
      |
      v
Document Permission Filter
      |
      v
Vector Retrieval
      |
      v
Content Security
      |
      v
LLM
```

---

## 37. AI Agent Zero Trust

AI agents shall not be trusted merely because they were created by an administrator.

Every execution shall validate:

```text
Agent Identity
Tenant
User
Task
Permissions
Tools
Data
Risk
Policy
```

---

## 38. AI Least Privilege

An AI agent shall only receive:

```text
Minimum Tools
Minimum Data
Minimum Scope
Minimum Duration
Minimum Execution Authority
```

required for its task.

---

## 39. AI Delegation

AI agents may act on behalf of users only within delegated authority.

```text
User Permissions
        |
        v
Delegation Policy
        |
        v
Agent Permissions
        |
        v
Tool Permissions
```

The final authority shall be the intersection of applicable permissions.

---

## 40. AI Permission Boundary

The effective AI permission shall be:

```text
Effective Permission
=
User Permission
∩
Tenant Policy
∩
Agent Permission
∩
Tool Permission
∩
Resource Permission
∩
Risk Policy
```

---

## 41. Multi-Agent Security

Agent-to-agent requests shall include:

```text
source_agent_id
destination_agent_id
tenant_id
user_id
task_id
requested_action
requested_data_scope
```

---

## 42. Agent-to-Agent Authorization

The receiving agent shall verify that the calling agent is permitted to request the operation.

---

## 43. MCP Zero Trust

MCP shall be treated as a privileged capability layer.

Every MCP call shall validate:

```text
Caller
Agent
Tenant
Tool
Action
Input
Resource
Permission
Risk
Rate Limit
Approval Policy
```

---

## 44. MCP Tool Allowlisting

Only explicitly approved tools shall be executable.

---

## 45. MCP Capability Isolation

Tools shall be categorized:

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

Higher-risk capabilities shall require stronger policies.

---

## 46. MCP Human Approval

Configured high-risk MCP operations shall require human approval.

Examples:

```text
Delete Database Record
Delete Customer Data
Export Sensitive Data
Modify User Permissions
Create Admin User
Change Billing
Issue Refund
Execute Production Command
Rotate Critical Secret
Disable Security Control
```

---

## 47. Workflow Zero Trust

Every workflow shall have:

```text
workflow_id
tenant_id
owner_id
trigger
actions
permissions
tools
integrations
risk_level
approval_policy
status
version
```

---

## 48. Workflow Permission Isolation

Workflow execution shall not automatically inherit all permissions of the workflow creator.

---

## 49. Workflow Runtime Authorization

Each sensitive workflow action shall be authorized at execution time.

---

## 50. Integration Zero Trust

Every integration shall be treated as an independent trust boundary.

Examples:

```text
Google Drive
Gmail
LinkedIn
Facebook
Instagram
WhatsApp
YouTube
TikTok
Slack
Zendesk
Salesforce
HubSpot
Jira
Notion
Microsoft Teams
```

---

## 51. Integration Credentials

Integration credentials shall be:

```text
Encrypted
Scoped
Tenant-Bound
Revocable
Rotatable
Audited
```

---

## 52. OAuth Zero Trust

OAuth shall support:

```text
PKCE
State Validation
Redirect URI Validation
Scope Minimization
Token Encryption
Token Expiration
Token Revocation
Tenant Binding
```

---

## 53. API Key Zero Trust

API keys shall support:

```text
Scopes
Expiration
Rotation
Revocation
Tenant Binding
Usage Monitoring
Audit Logging
```

---

## 54. Webhook Zero Trust

Incoming webhook requests shall validate:

```text
Signature
Timestamp
Source
Event ID
Payload Schema
Replay Protection
Rate Limit
Tenant Mapping
```

---

## 55. External Data Zero Trust

All external data shall be considered untrusted until validated.

This includes:

```text
Emails
Documents
CRM Records
Web Pages
Social Media Content
Webhook Payloads
API Responses
Knowledge Base Documents
MCP Tool Responses
```

---

## 56. Prompt Injection Defense

The system shall assume external content may contain malicious instructions.

Retrieved content shall not automatically gain instruction authority.

---

## 57. AI Context Boundary

AI context shall distinguish:

```text
System Policy
Developer Policy
User Request
Retrieved Content
Tool Result
External Data
```

---

## 58. AI Data Exfiltration Prevention

AI agents shall not:

```text
Export Unauthorized Data
Reveal Secrets
Cross Tenant Boundaries
Expose Hidden Prompts
Access Unauthorized Documents
Invoke Unauthorized Tools
```

---

## 59. AI Output Authorization

AI-generated actions shall pass through:

```text
Schema Validation
Authorization
Risk Assessment
Policy Validation
Approval
Execution
```

---

## 60. Human Approval Architecture

```text
AI Requests Action
        |
        v
Risk Engine
        |
        +---- LOW --------> Execute
        |
        +---- MEDIUM -----> Policy Check
        |
        +---- HIGH --------> Human Approval
        |
        +---- CRITICAL ----> Dual Approval
```

---

## 61. Continuous Risk Evaluation

The platform shall calculate contextual risk using signals including:

```text
Authentication
Session
Device
IP / Network
Behavior
Action
Resource
Data Sensitivity
Agent
Tool
Integration
Historical Activity
```

---

## 62. Risk Levels

```text
LOW
MEDIUM
HIGH
CRITICAL
```

---

## 63. Risk-Based Controls

## LOW

Normal access may continue.

## MEDIUM

Additional verification or monitoring may be required.

## HIGH

Step-up authentication, restricted permissions, or human approval may be required.

## CRITICAL

The operation may be blocked and security operations alerted.

---

## 64. Device Security

Where device intelligence is available, SalesGenie shall evaluate:

```text
Device Identity
Device Trust
Operating System
Browser
Security Posture
Recent Activity
Risk
```

Device trust shall not independently grant authorization.

---

## 65. Network Security

The platform shall not consider:

```text
Internal Network
VPN
Private IP
Corporate Network
Cloud VPC
```

as sufficient authorization.

---

## 66. Micro-Segmentation

Production infrastructure shall use logical segmentation between:

```text
Public Services
Application Services
AI Services
Data Services
Security Services
Management Services
```

---

## 67. API Rate Limiting

Rate limiting shall be applied based on:

```text
User
Tenant
IP
API Key
Agent
Tool
Endpoint
Risk
```

---

## 68. Resource Exhaustion Protection

The system shall limit:

```text
Request Size
File Size
AI Context Size
Tool Execution Frequency
Workflow Execution
Concurrent Sessions
Concurrent AI Tasks
API Calls
Exports
```

---

## 69. Security Headers

Protected web applications shall use appropriate:

```text
Content-Security-Policy
Strict-Transport-Security
X-Content-Type-Options
Referrer-Policy
Permissions-Policy
Frame-Ancestors
```

---

## 70. CORS

CORS shall use explicit allowlists.

Credentialed wildcard origins shall not be permitted.

---

## 71. SSRF Protection

Outbound requests shall enforce:

```text
Protocol Allowlist
Domain Allowlist
Private IP Blocking
Loopback Blocking
Cloud Metadata Blocking
DNS Rebinding Protection
Redirect Validation
Timeout
Response Size Limit
```

---

## 72. File Security

Uploaded content shall be treated as untrusted.

Security controls shall include:

```text
MIME Validation
Extension Validation
File Size Limits
Malware Scanning
Content Sanitization
Archive Protection
Path Traversal Prevention
Sandboxing
```

---

## 73. Secrets Management

Secrets shall never be embedded in:

```text
Source Code
Frontend Bundles
Logs
AI Prompts
AI Responses
Git Repositories
Client-Side Storage
```

unless explicitly designed and appropriately protected.

---

## 74. Secret Rotation

Secrets shall support:

```text
Scheduled Rotation
Manual Rotation
Emergency Rotation
Versioning
Revocation
Zero-Downtime Rotation
```

---

## 75. Encryption

SalesGenie shall protect sensitive data:

```text
In Transit
At Rest
In Backups
During Credential Storage
During Secret Storage
```

---

## 76. Cryptographic Key Management

Keys shall support:

```text
Generation
Rotation
Versioning
Revocation
Access Control
Auditing
Backup
Recovery
```

---

## 77. Data Classification

SalesGenie shall classify data as:

```text
PUBLIC
INTERNAL
CONFIDENTIAL
SENSITIVE
HIGHLY_SENSITIVE
```

Authorization and retention policies shall depend on classification.

---

## 78. Data Minimization

Services and AI agents shall receive only data necessary for the requested operation.

---

## 79. Data Loss Prevention

The system shall detect:

```text
Mass Export
Unusual Downloads
Sensitive Data Movement
Credential Leakage
Cross-Tenant Queries
Unusual AI Retrieval
Unusual Tool Calls
```

---

## 80. Audit Logging

Every security-sensitive operation shall generate an audit event containing, where applicable:

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
request_id
correlation_id
result
risk_level
policy_decision
```

---

## 81. Security Event Integrity

Security events shall be:

```text
Append-Only
Tamper-Evident
Access-Controlled
Timestamped
Searchable
Retained According to Policy
```

---

## 82. Security Monitoring

The platform shall continuously monitor:

```text
Authentication
Authorization
Sessions
API Requests
Service Calls
AI Calls
Tool Calls
MCP Calls
Workflow Executions
Data Access
Data Exports
Integrations
Administrative Actions
```

---

## 83. Threat Detection

SalesGenie shall detect:

```text
Credential Stuffing
Brute Force
Account Takeover
Session Hijacking
Token Abuse
Privilege Escalation
Cross-Tenant Access
API Abuse
Data Exfiltration
AI Abuse
Prompt Injection
Tool Hijacking
MCP Abuse
Workflow Abuse
Integration Compromise
```

---

## 84. Security Alerting

High-risk events shall trigger alerts according to configured policy.

---

## 85. Automated Containment

The platform may automatically:

```text
Revoke Session
Revoke Token
Disable API Key
Disable Agent
Disable Tool
Disconnect Integration
Restrict Account
Require MFA
Block Request
Require Human Approval
```

---

## 86. Security Incident Management

Security incidents shall follow:

```text
Detection
      |
Classification
      |
Risk Assessment
      |
Containment
      |
Investigation
      |
Eradication
      |
Recovery
      |
Post-Incident Review
```

---

## 87. Human Security Operations

Security administrators shall be able to:

```text
View Alerts
View Audit Logs
Investigate Sessions
Revoke Sessions
Disable Users
Revoke Credentials
Disable Integrations
Disable AI Agents
Disable MCP Tools
Review Policy Decisions
Review Data Exports
Investigate Incidents
```

---

## 88. AI Security Operations

AI security agents may:

```text
Analyze Events
Correlate Events
Detect Anomalies
Detect Prompt Injection
Detect Tool Abuse
Detect Data Exfiltration
Classify Incidents
Recommend Containment
Summarize Incidents
```

AI shall not independently disable critical security controls unless explicitly authorized by policy.

---

## 89. Security Policy Management

Security policies shall support:

```text
Creation
Versioning
Validation
Approval
Deployment
Rollback
Audit
```

---

## 90. Policy Versioning

Every policy change shall have:

```text
policy_id
version
author
timestamp
change_reason
previous_version
approval
status
```

---

## 91. Policy Propagation

Security policy changes shall propagate within a defined security SLO.

---

## 92. Fail-Secure Architecture

If a critical authorization dependency becomes unavailable:

```text
Protected Operation
        |
        v
Authorization Failure
        |
        v
DENY
```

The platform shall not silently bypass authorization.

---

## 93. Break-Glass Access

Emergency access shall support:

```text
Explicit Activation
Strong Authentication
Reason
Limited Duration
Restricted Scope
Full Audit
Automatic Expiration
```

---

## 94. Separation of Duties

Security-sensitive capabilities shall be separated between appropriate roles.

Examples:

```text
Security Admin
Billing Admin
Organization Admin
Developer
Auditor
Super Admin
```

---

## 95. Privileged Access Management

Privileged operations shall support:

```text
MFA
Least Privilege
Time-Bounded Access
Approval
Audit Logging
Risk Monitoring
Credential Rotation
```

---

## 96. Administrative Security

Administrative operations shall never be authorized solely because a request originates from an internal service or trusted network.

---

## 97. Security APIs

```http
GET    /api/v1/security/sessions
DELETE /api/v1/security/sessions/{session_id}

GET    /api/v1/security/events
GET    /api/v1/security/alerts

GET    /api/v1/security/policies
POST   /api/v1/security/policies
PUT    /api/v1/security/policies/{policy_id}

GET    /api/v1/security/risk
GET    /api/v1/security/incidents

POST   /api/v1/security/approvals
GET    /api/v1/security/approvals/{approval_id}

GET    /api/v1/security/api-keys
POST   /api/v1/security/api-keys
DELETE /api/v1/security/api-keys/{key_id}
```

---

## 98. Authorization API

```http
POST /api/v1/authorization/check
```

Example conceptual request:

```json
{
  "subject": "user_or_agent",
  "tenant_id": "tenant",
  "action": "lead.export",
  "resource": "lead_collection",
  "context": {
    "session_id": "session",
    "risk_level": "medium"
  }
}
```

Possible responses:

```text
ALLOW
DENY
REQUIRE_STEP_UP
REQUIRE_HUMAN_APPROVAL
```

---

## 99. AI Authorization API

```http
POST /api/v1/ai/authorization/check
```

The authorization decision shall consider:

```text
User
Agent
Tenant
Task
Tool
Resource
Action
Risk
Data Classification
```

---

## 100. MCP Authorization API

```http
POST /api/v1/mcp/authorization/check
```

The system shall evaluate:

```text
agent_id
tool_id
tenant_id
user_id
action
resource
risk_level
```

before tool execution.

---

## 101. Zero Trust Request Lifecycle

```text
REQUEST
   |
   v
Identify Subject
   |
   v
Authenticate
   |
   v
Validate Token
   |
   v
Resolve Tenant
   |
   v
Resolve Resource
   |
   v
Resolve Action
   |
   v
Load Permissions
   |
   v
Evaluate Policy
   |
   v
Evaluate Risk
   |
   +---- DENY --------------------+
   |                              |
   |                              v
   |                           REJECT
   |
   +---- STEP-UP -----------------+
   |                              |
   |                              v
   |                         Reauthenticate
   |
   +---- HUMAN APPROVAL ----------+
   |                              |
   |                              v
   |                         Approval Flow
   |
   v
ALLOW
   |
   v
Execute
   |
   v
Audit
   |
   v
Monitor
```

---

## 102. AI Zero Trust Request Lifecycle

```text
User Request
     |
     v
Authenticate User
     |
     v
Resolve Tenant
     |
     v
Create AI Execution Context
     |
     v
Resolve Agent Identity
     |
     v
Load Agent Permissions
     |
     v
Retrieve Authorized Context
     |
     v
LLM Reasoning
     |
     v
Tool Requested
     |
     v
Tool Authorization
     |
     v
Risk Evaluation
     |
     +---- DENY
     |
     +---- HUMAN APPROVAL
     |
     v
Tool Execution
     |
     v
Validate Tool Result
     |
     v
Generate Response
     |
     v
Output Security Check
     |
     v
Audit
```

---

## 103. Security Invariants

The following invariants shall always hold:

```text
1. Authentication does not imply authorization.
2. Internal network access does not imply trust.
3. AI identity does not imply permission.
4. User permission does not automatically grant unrestricted AI authority.
5. Tool availability does not imply tool authorization.
6. Workflow ownership does not imply unrestricted workflow permissions.
7. Tenant membership does not imply access to every tenant resource.
8. Retrieved data does not become trusted instructions.
9. MCP tools cannot bypass authorization.
10. RAG cannot bypass document permissions.
11. Frontend checks cannot replace backend authorization.
12. Tokens must be validated before use.
13. Revoked credentials cannot authorize protected operations.
14. Security failures default to deny.
15. High-risk operations require stronger controls.
16. Every security-sensitive action must be attributable.
17. Security policies must be auditable.
18. Tenant boundaries must be enforced at every relevant storage layer.
19. AI output must be treated as untrusted until validated.
20. External integrations are independent trust boundaries.
```

---

## 104. Zero Trust Threat Model

SalesGenie shall model:

```text
Compromised User
Compromised Admin
Compromised Device
Stolen Token
Stolen API Key
Compromised OAuth Credential
Malicious Insider
Compromised Microservice
Malicious Integration
Malicious Webhook
Malicious Document
Prompt Injection
Indirect Prompt Injection
AI Jailbreak
Agent Hijacking
Tool Hijacking
MCP Compromise
RAG Poisoning
Cross-Tenant Access
Data Exfiltration
Privilege Escalation
Supply Chain Attack
```

---

## 105. Security Testing

The implementation shall include:

```text
Authentication Testing
Authorization Testing
RBAC Testing
ABAC Testing
Tenant Isolation Testing
Session Testing
Token Testing
API Security Testing
MCP Security Testing
AI Security Testing
Prompt Injection Testing
RAG Security Testing
Workflow Security Testing
Integration Security Testing
Webhook Security Testing
SSRF Testing
XSS Testing
CSRF Testing
File Upload Testing
Secret Scanning
SAST
DAST
Dependency Scanning
Container Scanning
Penetration Testing
AI Red Teaming
```

---

## 106. Automated Authorization Tests

The test suite shall verify:

```text
User A cannot access User B's protected resources.

Tenant A cannot access Tenant B.

Agent A cannot execute Agent B's tools.

Workflow A cannot execute Workflow B's privileged actions.

MCP Tool A cannot access unauthorized resources.

AI cannot escalate its own permissions.

A revoked token cannot access protected APIs.

A revoked session cannot continue protected operations.

A deleted permission cannot authorize new operations.

RAG cannot retrieve unauthorized documents.
```

---

## 107. AI Red-Team Requirements

AI security testing shall include:

```text
System Prompt Extraction
Prompt Injection
Indirect Prompt Injection
Context Poisoning
RAG Poisoning
Tool Hijacking
Agent Hijacking
Privilege Escalation
Data Exfiltration
Credential Extraction
Unauthorized Tool Invocation
Cross-Tenant Retrieval
Malicious External Content
Malicious MCP Responses
```

---

## 108. Security Observability

Security telemetry shall correlate:

```text
user_id
agent_id
service_id
tenant_id
session_id
request_id
trace_id
workflow_id
tool_id
integration_id
event_id
```

---

## 109. Security Dashboard

Authorized security administrators shall be able to view:

```text
Active Sessions
Authentication Events
Authorization Decisions
Security Alerts
Risk Scores
Privileged Operations
AI Tool Usage
MCP Activity
Workflow Activity
Integration Activity
Data Exports
Security Incidents
```

---

## 110. Security Metrics

SalesGenie shall track:

```text
Authentication Failure Rate
MFA Adoption
Authorization Denial Rate
Privilege Escalation Attempts
Cross-Tenant Access Attempts
Session Revocation Rate
Credential Rotation Compliance
AI Tool Denial Rate
MCP Security Violations
Prompt Injection Detection Rate
Data Export Anomalies
Security Incident Rate
Mean Time To Detect
Mean Time To Respond
Mean Time To Contain
```

---

## 111. Zero Trust Security SLOs

Security operations shall define measurable SLOs for:

```text
Authentication Availability
Authorization Availability
Policy Propagation
Session Revocation
Credential Revocation
Security Event Ingestion
Security Alert Processing
Incident Detection
Incident Containment
```

---

## 112. Security Configuration

Security administrators shall be able to configure:

```text
MFA Requirements
Session Duration
Risk Thresholds
IP Policies
Device Policies
Authentication Policies
Role Policies
Data Access Policies
AI Policies
MCP Policies
Workflow Policies
Integration Policies
Export Policies
Approval Policies
```

---

## 113. Configuration Change Security

Security configuration changes shall require:

```text
Authorization
Audit
Versioning
Validation
Optional Approval
Rollback
```

---

## 114. Zero Trust for Billing

Billing operations shall be separately authorized.

AI or human actors shall not perform billing operations without the appropriate billing permission.

High-risk billing actions shall support step-up authentication and/or human approval.

---

## 115. Zero Trust for Customer Communication

Sending customer communication shall validate:

```text
User
Agent
Tenant
Channel
Recipient
Message
Campaign
Permission
Rate Limit
Risk
```

---

## 116. Zero Trust for Lead Generation

Lead-generation actions shall enforce:

```text
Tenant
Agent
User
Data Source
Lead Scope
Export Permission
Communication Permission
Rate Limits
Compliance Policies
```

---

## 117. Zero Trust for Data Export

Exports shall require:

```text
Export Permission
Data Classification Check
Tenant Validation
Resource Authorization
Risk Assessment
Rate Limit
Audit
```

High-risk exports may require human approval.

---

## 118. Zero Trust for Deletion

Deletion shall validate:

```text
Identity
Tenant
Resource Ownership
Permission
Resource Dependencies
Retention Policy
Risk
Approval
```

Critical deletion may require dual authorization.

---

## 119. Zero Trust for Administrative Actions

Administrative operations shall require:

```text
Strong Authentication
Role Authorization
Resource Authorization
Risk Evaluation
Audit
```

---

## 120. Dual-Control Operations

SalesGenie may require two authorized humans for critical actions:

```text
Production Security Policy Disablement
Critical Secret Rotation
Mass Data Deletion
Large-Scale Data Export
Platform-Level Privilege Changes
Critical Infrastructure Changes
```

---

## 121. Backup Zero Trust

Backup access shall use independent authorization controls.

Backup credentials shall not automatically provide unrestricted production access.

---

## 122. Disaster Recovery Security

Recovery procedures shall preserve:

```text
Tenant Isolation
Access Controls
Encryption
Credential Security
Auditability
Security Policies
```

---

## 123. Supply Chain Zero Trust

Third-party components shall be treated as potentially compromised.

The CI/CD pipeline shall verify:

```text
Dependencies
Container Images
Build Artifacts
Packages
Source Integrity
Secrets
Vulnerabilities
```

---

## 124. CI/CD Zero Trust

Production deployment shall require:

```text
Authenticated Identity
Authorized Repository Access
Code Review
Automated Tests
Security Scans
Artifact Verification
Deployment Authorization
Audit Logging
```

---

## 125. Environment Isolation

The following environments shall be logically separated:

```text
Development
Testing
Staging
Production
```

Production credentials shall never be reused in development.

---

## 126. Production Access

Production access shall be:

```text
Least Privileged
MFA Protected
Audited
Time-Bounded Where Possible
Risk Monitored
```

---

## 127. Security Acceptance Criteria

## AC-ZT-001

Every protected request is authenticated.

## AC-ZT-002

Every protected operation is authorized.

## AC-ZT-003

Network location cannot bypass authorization.

## AC-ZT-004

Cross-tenant access is prevented.

## AC-ZT-005

AI agents cannot exceed delegated permissions.

## AC-ZT-006

MCP tools cannot execute unauthorized actions.

## AC-ZT-007

Workflows cannot exceed configured permissions.

## AC-ZT-008

RAG retrieval respects authorization.

## AC-ZT-009

External content cannot automatically override AI security policy.

## AC-ZT-010

Revoked sessions cannot perform protected operations.

## AC-ZT-011

Revoked credentials cannot authorize protected requests.

## AC-ZT-012

High-risk actions require appropriate additional controls.

## AC-ZT-013

Security events are attributable to an actor.

## AC-ZT-014

Secrets do not appear in logs.

## AC-ZT-015

Security-sensitive configuration changes are auditable.

## AC-ZT-016

Security failures fail closed.

## AC-ZT-017

AI-generated actions pass authorization before execution.

## AC-ZT-018

Service-to-service calls require authenticated identities.

## AC-ZT-019

Tenant boundaries are enforced across databases, caches, object storage, search, vectors, events, and AI context.

## AC-ZT-020

Emergency access automatically expires.

---

## 128. FAANG-Level Zero Trust Quality Gates

```text
[ ] Zero implicit trust
[ ] Explicit authentication
[ ] Explicit authorization
[ ] Least privilege
[ ] Continuous verification
[ ] RBAC
[ ] ABAC
[ ] Tenant isolation
[ ] Resource-level authorization
[ ] Service identity
[ ] Service-to-service authentication
[ ] Mutual TLS where applicable
[ ] API gateway security
[ ] Distributed policy enforcement
[ ] Central policy decision point
[ ] Session security
[ ] Token security
[ ] MFA
[ ] Step-up authentication
[ ] Device-aware risk
[ ] Network-aware risk
[ ] Risk-based authorization
[ ] Micro-segmentation
[ ] Database security
[ ] Cache isolation
[ ] Object storage isolation
[ ] Vector database isolation
[ ] RAG authorization
[ ] AI identity
[ ] AI least privilege
[ ] Agent isolation
[ ] Agent-to-agent authorization
[ ] MCP authorization
[ ] MCP capability isolation
[ ] Workflow isolation
[ ] OAuth security
[ ] API key security
[ ] Webhook verification
[ ] External data validation
[ ] Prompt injection defense
[ ] AI data leakage prevention
[ ] Human approval
[ ] Dual control
[ ] Secrets management
[ ] Secret rotation
[ ] Encryption
[ ] Key management
[ ] Data classification
[ ] DLP
[ ] Security logging
[ ] Tamper-evident auditing
[ ] Security monitoring
[ ] Threat detection
[ ] Automated containment
[ ] Incident response
[ ] Break-glass access
[ ] Privileged access management
[ ] Supply-chain security
[ ] SAST
[ ] DAST
[ ] Dependency scanning
[ ] Container scanning
[ ] Secret scanning
[ ] Penetration testing
[ ] AI red teaming
[ ] Security SLOs
[ ] Disaster recovery
```

---

## 129. Definition of Done

`zero_trust_security.md` shall be considered fully implemented when SalesGenie enforces the following security model:

```text
                 NEVER TRUST
                      |
                      v
                IDENTIFY ACTOR
                      |
                      v
                AUTHENTICATE
                      |
                      v
              RESOLVE TENANT
                      |
                      v
             RESOLVE RESOURCE
                      |
                      v
              RESOLVE ACTION
                      |
                      v
             CHECK PERMISSIONS
                      |
                      v
               CHECK CONTEXT
                      |
                      v
                CHECK RISK
                      |
             +--------+--------+
             |        |        |
             v        v        v
           DENY    APPROVAL   ALLOW
                      |        |
                      +--------+
                           |
                           v
                       EXECUTE
                           |
                           v
                         AUDIT
                           |
                           v
                       MONITOR
```

SalesGenie shall apply this model consistently to:

```text
Human Users
AI Agents
Multi-Agent Systems
MCP Tools
Workflows
Microservices
APIs
Databases
Caches
Vector Stores
Object Storage
External Integrations
OAuth Credentials
API Keys
Webhooks
Customer Data
Lead Data
Conversations
Knowledge Bases
Billing Operations
Administrative Operations
Security Operations
```

The resulting architecture shall ensure that **no human, AI agent, service, workflow, tool, integration, device, network, credential, or application is inherently trusted**, and that every sensitive action is continuously evaluated against identity, tenant, authorization, context, data sensitivity, risk, and security policy.
