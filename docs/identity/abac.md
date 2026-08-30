# SalesGenie — Attribute-Based Access Control (ABAC) Requirements

## `abac.md`

**Document Type:** User Requirements + System Requirements + Functional Requirements  
**Product:** SalesGenie Enterprise AI SaaS Platform  
**Version:** 1.0  
**Status:** Architecture / Requirements Baseline  
**Security Classification:** Confidential  
**Architecture Pattern:** Zero-Trust + RBAC + ABAC + Policy-Based Access Control  
**Primary Objective:** Fine-grained, context-aware authorization across the entire SalesGenie platform

---

## 1. Document Purpose

This document defines the complete Attribute-Based Access Control (ABAC) requirements for SalesGenie.

ABAC will operate together with:

- Authentication
- RBAC
- Organization hierarchy
- Tenant isolation
- Workspace isolation
- Resource-level permissions
- Policy-Based Access Control (PBAC)
- AI-assisted authorization
- Human security review
- Zero-Trust security
- Audit logging
- Risk-based access control
- Session management
- API authorization
- Service-to-service authorization

ABAC will determine whether a user, AI agent, service, or external integration can perform a specific action against a specific resource under a specific context.

The authorization decision will not depend solely on the user's role.

The platform must evaluate:

```text
Subject
   +
Subject Attributes
   +
Resource
   +
Resource Attributes
   +
Action
   +
Environment Attributes
   +
Organization Policies
   +
Security Policies
   +
Risk Signals
   +
Subscription Constraints
   +
Data Classification
   +
ABAC Policy
   ↓
Authorization Decision
   ↓
ALLOW / DENY / STEP-UP / HUMAN_REVIEW / LIMITED_ACCESS
```

---

## 2. ABAC Vision

SalesGenie must provide enterprise-grade authorization capable of answering questions such as:

> "Can this Sales Agent export customer data?"

not merely:

> "Is this person a Sales Agent?"

The authorization engine must evaluate:

```text
Who is requesting?
What role do they have?
Which organization do they belong to?
Which workplace do they belong to?
Which team do they belong to?
What resource are they accessing?
Who owns that resource?
What action are they attempting?
Where are they connecting from?
What device are they using?
What is their security risk?
What time is it?
What subscription does the organization have?
What data classification applies?
What policies apply?
Is approval required?
Is the action AI-generated?
Is the action performed by a human?
Is the action sensitive?
```

---

## 3. Core ABAC Principles

SalesGenie ABAC must follow these principles.

## 3.1 Default Deny

Every request must be denied unless an applicable policy explicitly permits it.

```text
No matching policy
       ↓
DENY
```

---

## 3.2 Least Privilege

Users and agents receive only the minimum access required to perform their responsibilities.

---

## 3.3 Need-to-Know

Sensitive information must only be accessible when the subject has a legitimate business need.

---

## 3.4 Context-Aware Authorization

Authorization must consider environmental context.

Examples:

```text
IP address
Country
Location
Device
Browser
Session
Time
Network
Risk score
Authentication strength
MFA status
```

---

## 3.5 Resource-Level Authorization

Access must be enforceable at:

```text
Platform
Organization
Workplace
Team
Project
Campaign
Lead
Contact
Customer
Conversation
Product
Document
Knowledge Base
Workflow
Agent
Report
Invoice
Payment
API
Integration
```

---

## 3.6 Continuous Authorization

Authorization must not be evaluated only at login.

Sensitive requests must be continuously evaluated.

---

## 4. ABAC Actors

The ABAC engine must support the following subjects.

## 4.1 Human Users

Examples:

* Super Admin
* Platform Admin
* Security Admin
* Billing Admin
* Organization Owner
* Organization Admin
* Workplace Admin
* Team Manager
* Sales Manager
* Sales Agent
* Marketing Manager
* Marketing Specialist
* SEO Manager
* SEO Specialist
* Product Manager
* Finance Manager
* Business Analyst
* Support Manager
* Support Agent
* Developer
* AI Agent Builder
* End User
* External Client

---

## 4.2 AI Agents

AI subjects include:

```text
Lead Generation Agent
Market Research Agent
Competitor Analysis Agent
Marketing Agent
SEO Agent
Sales Agent
Customer Support Agent
Financial Analysis Agent
Business Analyst Agent
Product Strategy Agent
Data Analysis Agent
Reporting Agent
Security Agent
Billing Agent
Workflow Agent
```

AI agents must not inherit unlimited human permissions.

Each AI agent requires explicit policies.

---

## 4.3 Service Accounts

Examples:

```text
analytics-service
billing-service
lead-service
auth-service
notification-service
ai-gateway
reporting-service
integration-service
```

---

## 4.4 External Integrations

Examples:

```text
Google
Google Ads
Meta
Facebook
Instagram
WhatsApp
YouTube
TikTok
LinkedIn
Salesforce
HubSpot
Slack
Microsoft Teams
Zendesk
Jira
Notion
Google Drive
Gmail
```

---

## 5. ABAC Attribute Model

SalesGenie must implement a standardized attribute taxonomy.

```text
Subject Attributes
Resource Attributes
Action Attributes
Environment Attributes
Organization Attributes
Security Attributes
Business Attributes
Subscription Attributes
Compliance Attributes
AI Attributes
```

---

## 6. Subject Attributes

Each authenticated subject may contain:

```text
subject.id
subject.type
subject.role
subject.roles[]
subject.status
subject.email_verified
subject.organization_id
subject.workplace_id
subject.team_id
subject.department_id
subject.designation
subject.permissions[]
subject.clearance_level
subject.security_level
subject.account_age
subject.mfa_enabled
subject.authentication_method
subject.device_trust
subject.risk_score
subject.country
subject.region
subject.ip_address
subject.session_id
subject.subscription_role
subject.approval_level
subject.manager_id
```

---

## 7. Subject Type

Supported values:

```text
human
ai_agent
service_account
integration
system
external_client
```

Example:

```json
{
  "subject": {
    "type": "human",
    "role": "sales_agent"
  }
}
```

---

## 8. Resource Attributes

Resources must expose authorization metadata.

Example:

```json
{
  "resource": {
    "type": "lead",
    "id": "lead_123",
    "organization_id": "org_001",
    "workplace_id": "wp_001",
    "team_id": "team_001",
    "owner_id": "user_123",
    "classification": "confidential",
    "created_by": "user_123",
    "status": "active"
  }
}
```

---

## 9. Resource Classification

SalesGenie must support:

```text
PUBLIC
INTERNAL
CONFIDENTIAL
RESTRICTED
HIGHLY_RESTRICTED
```

Example:

```text
Public marketing content
        ↓
PUBLIC

Sales reports
        ↓
INTERNAL

Customer records
        ↓
CONFIDENTIAL

Payment information
        ↓
RESTRICTED

Security credentials
        ↓
HIGHLY_RESTRICTED
```

---

## 10. Action Attributes

Every authorization request must identify the action.

Supported actions include:

```text
create
read
list
search
update
delete
archive
restore
export
download
upload
share
publish
approve
reject
assign
reassign
execute
run
generate
analyze
train
configure
configure_policy
manage
impersonate
invite
ban
unban
reset
billing
refund
cancel
deploy
integrate
connect
disconnect
```

---

## 11. Environment Attributes

The authorization engine must evaluate:

```text
environment.timestamp
environment.timezone
environment.ip
environment.country
environment.region
environment.city
environment.network_type
environment.device_id
environment.device_type
environment.browser
environment.os
environment.vpn_detected
environment.proxy_detected
environment.tor_detected
environment.device_trusted
environment.session_age
environment.authentication_age
environment.mfa_verified
environment.risk_score
environment.anomaly_score
```

---

## 12. Organization Attributes

Policies may depend on:

```text
organization.id
organization.status
organization.plan
organization.subscription_status
organization.industry
organization.region
organization.data_residency
organization.security_policy
organization.compliance_profile
organization.max_users
organization.max_agents
organization.export_policy
organization.ai_policy
```

---

## 13. Subscription Attributes

Authorization must integrate with SalesGenie's subscription system.

Example plans:

```text
FREE
STARTER
PRO
BUSINESS
ENTERPRISE
CUSTOM
```

Example:

```text
FREE
 ↓
basic analytics

PRO
 ↓
advanced analytics

BUSINESS
 ↓
team automation

ENTERPRISE
 ↓
advanced governance
ABAC policies
SSO
audit controls
advanced security
```

Subscription status:

```text
active
trial
past_due
suspended
cancelled
expired
```

---

## 14. Business Attributes

ABAC may evaluate business context.

Examples:

```text
customer_value
lead_score
deal_value
campaign_budget
product_value
financial_risk
profitability
business_unit
market_region
sales_region
customer_segment
```

---

## 15. AI Attributes

AI agents require additional attributes.

```text
ai.agent_id
ai.agent_type
ai.version
ai.trust_level
ai.authorization_scope
ai.model_provider
ai.model_name
ai.execution_mode
ai.human_approval_required
ai.data_access_scope
ai.action_risk
ai.confidence_score
ai.tool_permissions
```

---

## 16. User Requirements

## UR-ABAC-001 — Fine-Grained Access

Users must receive access according to their attributes and applicable policies.

---

## UR-ABAC-002 — Organization Isolation

Users must never access another organization's resources unless explicitly authorized.

---

## UR-ABAC-003 — Workplace Isolation

Users must only access workplaces permitted by policy.

---

## UR-ABAC-004 — Team-Level Access

Managers must be able to access team resources according to team policies.

---

## UR-ABAC-005 — Resource Ownership

Users may access resources they own when policy permits.

---

## UR-ABAC-006 — Delegated Access

Users may receive temporary delegated permissions.

---

## UR-ABAC-007 — Temporary Access

Administrators must be able to create time-limited permissions.

---

## UR-ABAC-008 — Context-Based Restrictions

Access may depend on:

```text
location
device
time
risk
network
MFA
session
```

---

## UR-ABAC-009 — Sensitive Data Protection

Highly sensitive resources require stronger authorization.

---

## UR-ABAC-010 — Export Protection

Data export must have independent ABAC policies.

---

## UR-ABAC-011 — AI Authorization

AI agents must operate under explicit authorization policies.

---

## UR-ABAC-012 — Human Escalation

High-risk operations must support human approval.

---

## UR-ABAC-013 — Policy Transparency

Authorized administrators must be able to understand why an action was allowed or denied.

---

## UR-ABAC-014 — Auditability

Every authorization decision must be auditable.

---

## UR-ABAC-015 — Continuous Security

Authorization must be reevaluated when risk or context changes.

---

## 17. System Requirements

## SR-ABAC-001 — Policy Decision Point

SalesGenie must implement a centralized Policy Decision Point (PDP).

```text
API Request
    ↓
Authorization Middleware
    ↓
Policy Enforcement Point
    ↓
Policy Decision Point
    ↓
Policy Evaluation
    ↓
Decision
```

---

## 18. Policy Enforcement Point

Every protected API must contain a Policy Enforcement Point.

Example:

```text
GET /api/v1/leads
        ↓
PEP
        ↓
ABAC Engine
        ↓
ALLOW / DENY
```

---

## 19. Policy Administration Point

Authorized administrators must manage policies through a Policy Administration Point.

Capabilities:

```text
Create policy
Edit policy
Disable policy
Delete policy
Test policy
Simulate policy
Version policy
Rollback policy
Approve policy
Publish policy
```

---

## 20. Policy Information Point

The system must retrieve attributes from trusted sources.

Sources include:

```text
Identity Service
Organization Service
User Service
Device Service
Session Service
Risk Engine
Billing Service
Resource Service
Security Service
Audit Service
Subscription Service
AI Gateway
```

---

## 21. Policy Information Architecture

```text
                   ┌───────────────────┐
                   │   ABAC Request    │
                   └─────────┬─────────┘
                             ↓
                   ┌───────────────────┐
                   │ Policy Enforcement│
                   │      Point        │
                   └─────────┬─────────┘
                             ↓
                   ┌───────────────────┐
                   │ Policy Decision    │
                   │      Point        │
                   └─────────┬─────────┘
                             ↓
          ┌──────────────────┼───────────────────┐
          ↓                  ↓                   ↓
   Subject Attributes   Resource Attributes   Environment
          ↓                  ↓                   ↓
          └──────────────────┼───────────────────┘
                             ↓
                   ┌───────────────────┐
                   │ Policy Evaluation │
                   │      Engine       │
                   └─────────┬─────────┘
                             ↓
                ┌────────────┼────────────┐
                ↓            ↓            ↓
              ALLOW        DENY       STEP-UP
```

---

## 22. Authorization Decision Types

SalesGenie must support more than binary authorization.

```text
ALLOW
DENY
STEP_UP_AUTH
HUMAN_REVIEW
LIMITED_ACCESS
MASK_DATA
READ_ONLY
TEMPORARY_ACCESS
```

---

## 23. ABAC Policy Model

Policies should contain:

```text
policy_id
name
description
version
effect
subjects
actions
resources
conditions
priority
environment_constraints
risk_constraints
approval_requirements
obligations
status
created_by
approved_by
created_at
updated_at
```

Example:

```yaml
policy:
  id: sales-agent-read-leads
  effect: allow

  subject:
    role: sales_agent

  action:
    - read
    - search

  resource:
    type: lead

  condition:
    organization_match: true
    workplace_match: true
    team_match: true

  environment:
    max_risk_score: 50
```

---

## 24. Policy Evaluation Logic

The authorization engine must evaluate:

```text
Subject
AND
Resource
AND
Action
AND
Environment
AND
Organization
AND
Subscription
AND
Security
AND
Compliance
```

Example:

```text
IF

subject.role == sales_agent

AND

subject.organization_id == resource.organization_id

AND

subject.workplace_id == resource.workplace_id

AND

action == read

AND

resource.type == lead

AND

subject.risk_score < 70

THEN

ALLOW
```

---

## 25. Organization-Level ABAC

Organization owners must be able to define policies such as:

```text
Sales agents can access leads
only within their organization.
```

---

## 26. Workplace-Level ABAC

Workplace administrators may define:

```text
Marketing team
can access marketing campaigns.

Sales team
can access sales leads.

Finance team
can access financial reports.
```

---

## 27. Team-Level ABAC

Team managers may define:

```text
Team member
→ own resources

Team manager
→ team resources

Department manager
→ department resources
```

---

## 28. Resource Ownership Policy

Example:

```text
IF
subject.id == resource.owner_id
AND
action == read
THEN
ALLOW
```

---

## 29. Managerial Hierarchy

ABAC must understand organizational hierarchy.

Example:

```text
Organization Owner
       ↓
Organization Admin
       ↓
Workplace Admin
       ↓
Department Manager
       ↓
Team Manager
       ↓
Team Member
```

Authorization may depend on hierarchical relationships.

---

## 30. Geographic ABAC

The platform may restrict access based on location.

Example:

```text
IF
user.country == organization.allowed_country
THEN
ALLOW
```

Unauthorized geographic access:

```text
ALLOW
   ↓
Risk Engine
   ↓
Suspicious location
   ↓
STEP_UP_AUTH
```

---

## 31. Time-Based ABAC

Policies may define access windows.

Example:

```text
Sales agents:
08:00–22:00

Finance:
08:00–20:00

Security administration:
business hours + emergency override
```

Outside the permitted period:

```text
DENY
```

or:

```text
STEP_UP_AUTH
```

---

## 32. Device-Based ABAC

Policies may require trusted devices.

Example:

```text
IF
resource.classification == HIGHLY_RESTRICTED

AND

device.trusted == false

THEN

DENY
```

---

## 33. Risk-Based ABAC

The ABAC engine must integrate with a risk engine.

Risk signals may include:

```text
Impossible travel
Unusual IP
New device
Multiple failed logins
Suspicious API activity
Abnormal download volume
Unusual export behavior
Credential anomalies
```

Risk levels:

```text
0–20   LOW
21–50  MEDIUM
51–75  HIGH
76–100 CRITICAL
```

---

## 34. Risk-Based Authorization

Example:

```text
risk < 50
→ normal access

risk 50–75
→ restricted access / MFA

risk 76–90
→ human review

risk > 90
→ deny
```

---

## 35. Data Masking

ABAC must support field-level protection.

Example:

```text
Sales Agent:

name       → visible
company    → visible
email      → visible
phone      → visible
revenue    → restricted
payment    → masked
financial  → denied
```

---

## 36. Field-Level ABAC

Policies may specify:

```text
field
action
subject
condition
effect
```

Example:

```yaml
resource: customer

field: payment_information

condition:
  role:
    not_in:
      - finance_manager
      - billing_admin

effect: mask
```

---

## 37. Export ABAC

Export operations must be treated as high-risk.

Before export:

```text
User
 ↓
ABAC
 ↓
Resource classification
 ↓
Record count
 ↓
Risk score
 ↓
Destination
 ↓
Policy
 ↓
Decision
```

Possible decisions:

```text
ALLOW
LIMIT
MASK
STEP_UP
HUMAN_REVIEW
DENY
```

---

## 38. Bulk Operation Protection

Bulk operations require additional policy evaluation.

Examples:

```text
Export 10 records
Export 1,000 records
Delete 5,000 leads
Download entire customer database
```

The larger the operation, the higher the risk.

---

## 39. AI Agent ABAC

AI agents must have separate identities.

Example:

```text
agent_id = market-research-agent-001
```

The agent must have:

```text
allowed tools
allowed APIs
allowed resources
allowed actions
data scope
organization scope
maximum risk
human approval requirement
```

---

## 40. AI Agent Least Privilege

An AI Marketing Agent must not automatically access:

```text
payment data
security credentials
private customer data
billing records
```

unless explicitly authorized.

---

## 41. AI Action Risk Classification

AI actions should be classified:

```text
LOW
MEDIUM
HIGH
CRITICAL
```

Example:

```text
Generate marketing copy
→ LOW

Create campaign draft
→ MEDIUM

Publish campaign
→ HIGH

Modify payment configuration
→ CRITICAL
```

---

## 42. AI Human-in-the-Loop

High-risk AI actions must support human approval.

```text
AI Agent
   ↓
Action Request
   ↓
ABAC
   ↓
Risk Assessment
   ↓
Human Approval
   ↓
Execution
```

---

## 43. Humanized Security

The system must support human security intervention.

Examples:

```text
Security Admin review
Billing Admin review
Organization Owner approval
Manual account recovery
Manual suspicious activity investigation
Manual export approval
```

---

## 44. Human Approval Workflow

```text
High-Risk Request
       ↓
ABAC
       ↓
HUMAN_REVIEW
       ↓
Security/Admin Queue
       ↓
Approve / Reject
       ↓
Decision Recorded
       ↓
Action Executed
```

---

## 45. Subscription-Based ABAC

ABAC must enforce feature availability according to subscription.

Example:

```text
FREE
→ basic analytics

PRO
→ advanced analytics

BUSINESS
→ automation

ENTERPRISE
→ advanced ABAC
→ custom policies
→ SSO
→ advanced audit
```

---

## 46. Billing Security

Billing resources must have strict ABAC.

Example:

```text
Billing Admin
→ full billing access

Organization Owner
→ organization billing

Finance Manager
→ financial reports

Sales Agent
→ no payment information
```

---

## 47. API ABAC

Every protected API endpoint must be evaluated.

Example:

```text
POST /api/v1/leads
GET /api/v1/leads
DELETE /api/v1/leads/{id}
POST /api/v1/leads/export
```

Each endpoint must have:

```text
subject requirements
resource requirements
action requirements
context requirements
risk requirements
```

---

## 48. Service-to-Service ABAC

Microservices must authenticate and authorize service calls.

Example:

```text
Lead Service
     ↓
AI Gateway
     ↓
Authorization
     ↓
AI Service
```

A compromised service must not automatically gain access to all platform resources.

---

## 49. API Gateway Enforcement

The API Gateway should perform an initial authorization check.

Sensitive services must perform independent authorization.

```text
Client
 ↓
API Gateway
 ↓
Authentication
 ↓
Initial ABAC
 ↓
Microservice
 ↓
Resource-level ABAC
 ↓
Database
```

---

## 50. Database-Level Protection

ABAC must integrate with database security where appropriate.

Possible mechanisms:

```text
Row-Level Security
Column-Level Security
Tenant filters
Database roles
Encryption
Data masking
```

---

## 51. Tenant Isolation

Every tenant-scoped resource must include:

```text
tenant_id
organization_id
```

Authorization must validate tenant ownership before returning data.

---

## 52. Cross-Tenant Access

Cross-tenant access must be denied by default.

Only explicitly authorized platform-level operations may cross tenant boundaries.

---

## 53. Super Admin ABAC

Even Super Admin access should be policy-controlled.

Sensitive operations may require:

```text
MFA
trusted device
reason
ticket/reference
step-up authentication
audit logging
```

---

## 54. Break-Glass Access

SalesGenie may implement emergency access.

Break-glass access must require:

```text
strong authentication
reason
time limitation
scope limitation
enhanced logging
post-event review
```

Example:

```text
Duration:
30 minutes

Scope:
organization_123

Reason:
Production security incident
```

---

## 55. Delegated Administration

Administrators may delegate permissions.

Example:

```text
Organization Owner
 ↓
Organization Admin
 ↓
Temporary billing permission
 ↓
Expires in 24 hours
```

---

## 56. Permission Expiration

Temporary permissions must automatically expire.

```text
permission.created_at
permission.expires_at
```

Expired permissions must immediately become invalid.

---

## 57. Policy Priority

When policies conflict, SalesGenie must apply deterministic precedence.

Recommended:

```text
Explicit DENY
      ↓
Security policy
      ↓
Compliance policy
      ↓
Resource policy
      ↓
Organization policy
      ↓
Role policy
      ↓
Default
```

Default:

```text
DENY
```

---

## 58. Policy Conflict Resolution

Example:

```text
Role:
ALLOW export

Organization:
ALLOW export

Security:
DENY export from untrusted devices
```

Result:

```text
DENY
```

---

## 59. Policy Versioning

Every policy must support versions.

```text
v1
v2
v3
```

The system must support:

```text
draft
review
approved
published
deprecated
rollback
```

---

## 60. Policy Testing

Administrators must be able to simulate requests.

Example:

```text
User:
sales_agent_123

Action:
export

Resource:
lead_database

Device:
untrusted

Risk:
72
```

Expected:

```text
DENY
```

---

## 61. Policy Simulator

The platform must provide:

```text
Policy Simulator
```

It should show:

```text
Input attributes
Matched policies
Policy conditions
Decision
Obligations
Reason
Risk factors
```

---

## 62. Explainable Authorization

Every decision should generate an explanation.

Example:

```text
DENIED

Reason:
The requested resource is classified as RESTRICTED
and the requesting user's role does not have export
permission.

Additional factor:
Device is untrusted.
```

Sensitive internal policy details must not be exposed to unauthorized users.

---

## 63. Authorization Logging

Every decision must log:

```text
request_id
subject_id
subject_type
organization_id
workplace_id
resource_type
resource_id
action
decision
policy_id
policy_version
risk_score
device_id
ip
timestamp
reason
```

---

## 64. Security Audit

Security administrators must be able to investigate:

```text
Denied requests
Allowed requests
Repeated denials
Policy violations
Suspicious access
Bulk exports
Privilege escalation
AI actions
Administrative actions
```

---

## 65. ABAC Analytics

Dashboard metrics should include:

```text
Authorization requests
Allowed requests
Denied requests
Step-up requests
Human reviews
Policy violations
High-risk requests
Top denied resources
Top denied users
Top risky IPs
AI authorization activity
```

---

## 66. Anomaly Detection

The system should detect:

```text
Sudden increase in exports
Repeated authorization failures
Unusual resource access
Unusual administrative actions
AI agents accessing unusual resources
Cross-region activity
```

---

## 67. AI Security Monitoring

AI agents must be monitored for:

```text
permission escalation attempts
unauthorized tool calls
unexpected data access
prompt injection
data exfiltration attempts
policy bypass attempts
abnormal action frequency
```

---

## 68. Prompt Injection Protection

If an AI agent receives instructions attempting to bypass authorization:

```text
User Input
 ↓
AI Agent
 ↓
Tool Request
 ↓
ABAC
 ↓
Policy Evaluation
 ↓
DENY
```

Authorization must never depend solely on AI reasoning.

---

## 69. AI Must Not Self-Authorize

AI agents cannot:

```text
grant themselves permission
modify their own authorization
disable security policies
approve their own high-risk actions
```

---

## 70. External Integration ABAC

External integrations must receive scoped access.

Example:

```text
Google Ads Integration
→ marketing campaigns
→ advertising metrics

NOT:

billing
security
user management
```

---

## 71. OAuth Scope Mapping

OAuth scopes must be mapped into ABAC attributes.

Example:

```text
google.ads.read
google.ads.campaign.manage
```

The system must not assume OAuth authorization automatically means SalesGenie authorization.

---

## 72. Webhook ABAC

Incoming webhooks must be validated using:

```text
signature
source
integration identity
tenant
resource
event type
policy
```

---

## 73. Data Residency

ABAC may enforce regional restrictions.

Example:

```text
EU customer data
→ EU-approved processing location

Restricted data
→ approved infrastructure only
```

---

## 74. Compliance-Aware Authorization

The ABAC engine should support policies aligned with applicable requirements such as:

```text
GDPR
SOC 2
ISO 27001
HIPAA
PCI DSS
```

Actual compliance applicability must be determined by the organization's use case and legal requirements.

---

## 75. Encryption Requirements

Sensitive authorization data must be encrypted:

```text
At rest
In transit
During service communication
```

---

## 76. Secret Protection

ABAC policies must never contain plaintext:

```text
API keys
passwords
OAuth client secrets
private keys
database credentials
```

---

## 77. Caching Requirements

Authorization decisions may be cached only when safe.

Cache keys must include relevant attributes.

Example:

```text
subject
resource
action
organization
policy_version
risk_state
```

High-risk decisions should not use long-lived caches.

---

## 78. Cache Invalidation

Permission changes must invalidate relevant authorization caches.

Examples:

```text
Role changed
Organization changed
User banned
Policy changed
Device revoked
Session revoked
Subscription downgraded
```

---

## 79. Fail-Safe Behavior

If the ABAC engine becomes unavailable:

```text
Sensitive action
→ DENY

Non-sensitive cached action
→ only allowed if explicitly configured
```

The system must never fail open for sensitive resources.

---

## 80. High Availability

The ABAC engine must support:

```text
Horizontal scaling
Replication
Health checks
Failover
Load balancing
Circuit breakers
Timeout handling
```

---

## 81. Performance Requirements

Target authorization latency:

```text
p50 < 20 ms
p95 < 50 ms
p99 < 100 ms
```

for normal cached/local policy evaluations where infrastructure permits.

Complex distributed evaluations may have higher latency but must remain bounded.

---

## 82. Scalability Requirements

The architecture must support:

```text
Millions of users
Millions of organizations
Large policy sets
High API request volumes
Large numbers of AI agents
High-frequency authorization requests
```

---

## 83. Policy Distribution

Policies should be distributable to regional/service-level policy engines.

```text
Central Policy Store
        ↓
Policy Distribution
        ↓
Regional PDP
        ↓
Service PEP
```

---

## 84. Event-Driven ABAC

Authorization-related events should be published.

Examples:

```text
UserRoleChanged
UserBanned
PolicyCreated
PolicyUpdated
PolicyPublished
PolicyRevoked
RiskScoreChanged
DeviceRevoked
SubscriptionChanged
OrganizationSuspended
```

---

## 85. Example Event

```json
{
  "event": "UserRoleChanged",
  "user_id": "user_123",
  "organization_id": "org_123",
  "old_role": "sales_agent",
  "new_role": "sales_manager",
  "timestamp": "2026-08-22T00:00:00Z"
}
```

---

## 86. Database Requirements

Core ABAC entities should include:

```text
subjects
subject_attributes
resources
resource_attributes
actions
policies
policy_versions
policy_bindings
policy_conditions
policy_obligations
authorization_decisions
authorization_requests
delegations
approvals
risk_signals
security_contexts
```

---

## 87. Policy Database Model

Example:

```text
Policy
 ├── PolicyVersion
 │      ├── Conditions
 │      ├── Subjects
 │      ├── Resources
 │      ├── Actions
 │      └── Obligations
 │
 ├── Scope
 ├── Priority
 ├── Status
 └── AuditMetadata
```

---

## 88. API Requirements

Required APIs include:

```text
POST /api/v1/authorization/check
POST /api/v1/authorization/batch-check

GET /api/v1/policies
POST /api/v1/policies
GET /api/v1/policies/{id}
PUT /api/v1/policies/{id}
DELETE /api/v1/policies/{id}

POST /api/v1/policies/{id}/test
POST /api/v1/policies/{id}/publish
POST /api/v1/policies/{id}/rollback

GET /api/v1/authorization/audit
GET /api/v1/authorization/analytics
```

---

## 89. Authorization Request Schema

```json
{
  "subject": {
    "id": "user_123",
    "type": "human",
    "role": "sales_agent"
  },
  "action": "read",
  "resource": {
    "type": "lead",
    "id": "lead_123"
  },
  "environment": {
    "device_trusted": true,
    "risk_score": 20,
    "mfa_verified": true
  }
}
```

---

## 90. Authorization Response

```json
{
  "decision": "ALLOW",
  "request_id": "req_123",
  "policy_id": "lead-read-policy",
  "policy_version": "4",
  "obligations": [],
  "expires_at": null
}
```

---

## 91. Limited Access

ABAC may return:

```json
{
  "decision": "LIMITED_ACCESS",
  "restrictions": [
    "no_export",
    "no_delete",
    "mask_financial_fields"
  ]
}
```

---

## 92. Human Review Response

```json
{
  "decision": "HUMAN_REVIEW",
  "approval_required": true,
  "approval_type": "security_admin",
  "expires_in": 900
}
```

---

## 93. Functional Requirements

## FR-ABAC-001 — Evaluate Authorization

The system shall evaluate authorization requests using subject, resource, action, environment, organization, security, and policy attributes.

---

## FR-ABAC-002 — Default Deny

The system shall deny requests when no applicable allow policy exists.

---

## FR-ABAC-003 — Organization Matching

The system shall validate organization ownership before granting tenant-scoped access.

---

## FR-ABAC-004 — Workplace Matching

The system shall validate workplace scope.

---

## FR-ABAC-005 — Team Matching

The system shall evaluate team membership where applicable.

---

## FR-ABAC-006 — Ownership Evaluation

The system shall evaluate resource ownership.

---

## FR-ABAC-007 — Role Evaluation

The system shall consume RBAC role attributes.

---

## FR-ABAC-008 — Attribute Evaluation

The system shall evaluate arbitrary approved attributes.

---

## FR-ABAC-009 — Time Conditions

The system shall support time-based policies.

---

## FR-ABAC-010 — Location Conditions

The system shall support location-based policies.

---

## FR-ABAC-011 — Device Conditions

The system shall support trusted/untrusted device policies.

---

## FR-ABAC-012 — Risk Conditions

The system shall evaluate security risk scores.

---

## FR-ABAC-013 — MFA Conditions

The system shall enforce MFA requirements for sensitive actions.

---

## FR-ABAC-014 — Subscription Conditions

The system shall evaluate subscription state and plan.

---

## FR-ABAC-015 — Data Classification

The system shall evaluate resource classification.

---

## FR-ABAC-016 — Field-Level Authorization

The system shall support field-level access control.

---

## FR-ABAC-017 — Export Authorization

The system shall apply separate policies to exports.

---

## FR-ABAC-018 — Bulk Authorization

The system shall evaluate bulk operations based on volume and risk.

---

## FR-ABAC-019 — AI Authorization

The system shall authorize AI agents independently from human users.

---

## FR-ABAC-020 — AI Tool Authorization

The system shall validate every sensitive AI tool call.

---

## FR-ABAC-021 — AI Human Approval

The system shall route high-risk AI actions to humans.

---

## FR-ABAC-022 — Delegated Access

The system shall support temporary delegated permissions.

---

## FR-ABAC-023 — Permission Expiration

The system shall automatically revoke expired permissions.

---

## FR-ABAC-024 — Break-Glass

The system shall support controlled emergency access.

---

## FR-ABAC-025 — Policy Versioning

The system shall maintain immutable policy versions.

---

## FR-ABAC-026 — Policy Testing

The system shall provide policy simulation.

---

## FR-ABAC-027 — Policy Rollback

The system shall support safe policy rollback.

---

## FR-ABAC-028 — Policy Approval

Sensitive policy changes shall require approval.

---

## FR-ABAC-029 — Audit Logging

The system shall log every authorization decision.

---

## FR-ABAC-030 — Explainability

The system shall provide an authorization reason.

---

## FR-ABAC-031 — Analytics

The system shall provide authorization analytics.

---

## FR-ABAC-032 — Anomaly Detection

The system shall identify unusual authorization patterns.

---

## FR-ABAC-033 — Cross-Service Authorization

The system shall authorize service-to-service requests.

---

## FR-ABAC-034 — Integration Authorization

The system shall authorize external integrations.

---

## FR-ABAC-035 — Webhook Authorization

The system shall validate incoming webhook authorization context.

---

## FR-ABAC-036 — Cache Invalidation

The system shall invalidate authorization caches after security changes.

---

## FR-ABAC-037 — Fail Secure

The system shall fail closed for sensitive operations when authorization infrastructure is unavailable.

---

## 94. Role + ABAC Hybrid Model

SalesGenie should not replace RBAC with ABAC.

The recommended model is:

```text
RBAC
+
ABAC
+
PBAC
+
Risk-Based Access Control
+
Resource-Level Authorization
```

Example:

```text
RBAC:
Sales Agent

ABAC:
organization_id matches

ABAC:
team_id matches

ABAC:
risk_score < 50

ABAC:
trusted_device = true

Resource:
classification = CONFIDENTIAL

Action:
read

        ↓

ALLOW
```

---

## 95. Example — Sales Agent Reading Lead

```text
Sales Agent
     ↓
GET Lead
     ↓
ABAC
     ↓
Organization matches?
     ↓ YES
Workplace matches?
     ↓ YES
Team permitted?
     ↓ YES
Lead classification allowed?
     ↓ YES
Risk acceptable?
     ↓ YES
     ↓
ALLOW
```

---

## 96. Example — Sales Agent Exporting Leads

```text
Export Request
      ↓
ABAC
      ↓
Role permits export?
      ↓
Resource classification?
      ↓
Number of records?
      ↓
Device trusted?
      ↓
MFA?
      ↓
Risk score?
      ↓
Organization export policy?
      ↓
Decision
```

Possible:

```text
ALLOW
LIMIT
STEP_UP
HUMAN_REVIEW
DENY
```

---

## 97. Example — AI Marketing Agent

```text
AI Marketing Agent
       ↓
Create Campaign
       ↓
ABAC
       ↓
Agent identity verified
       ↓
Organization verified
       ↓
Campaign scope verified
       ↓
Tool permitted
       ↓
Action risk = MEDIUM
       ↓
ALLOW
```

Publishing:

```text
AI Marketing Agent
       ↓
Publish Campaign
       ↓
Action risk = HIGH
       ↓
Human approval required
       ↓
Marketing Manager
       ↓
APPROVE
       ↓
Publish
```

---

## 98. Example — Finance Data

```text
Sales Agent
 ↓
Request financial report
 ↓
ABAC
 ↓
Role insufficient
 ↓
DENY
```

Finance Manager:

```text
Finance Manager
 ↓
Financial report
 ↓
Organization match
 ↓
Trusted device
 ↓
MFA
 ↓
ALLOW
```

---

## 99. Example — Suspicious Location

```text
User
 ↓
Request customer database
 ↓
Unknown country
 ↓
Risk Engine
 ↓
Risk = 82
 ↓
ABAC
 ↓
HUMAN_REVIEW
```

---

## 100. Example — Subscription Restriction

```text
Organization
 ↓
FREE PLAN
 ↓
Request advanced analytics
 ↓
ABAC
 ↓
Feature unavailable
 ↓
DENY / UPGRADE_REQUIRED
```

---

## 101. Security Requirements

ABAC must integrate with:

```text
JWT
OAuth 2.0
OpenID Connect
MFA
Device Trust
Session Security
Risk Engine
Audit Logs
Encryption
Secrets Management
API Gateway
Service Mesh
```

---

## 102. Zero-Trust Model

Every request must be evaluated as potentially untrusted.

```text
Never Trust
Always Verify
```

Even:

```text
authenticated user
administrator
AI agent
internal service
trusted integration
```

must be authorized for each protected operation.

---

## 103. Privilege Escalation Protection

ABAC must prevent:

```text
sales_agent
   ↓
sales_manager
```

without an authorized administrative action.

A user cannot modify attributes used to grant themselves greater privileges.

---

## 104. Attribute Integrity

Security-sensitive attributes must originate from trusted systems.

Examples:

```text
role
organization_id
security_level
risk_score
subscription_status
device_trust
```

Users must not directly control these values.

---

## 105. Attribute Tampering Detection

The system should detect suspicious attribute changes.

Examples:

```text
organization_id changed unexpectedly
role changed without approval
security clearance increased
device trust changed
risk score manipulation
```

---

## 106. Audit Immutability

Authorization audit logs should be tamper-resistant.

Recommended architecture:

```text
Application
 ↓
Audit Event
 ↓
Immutable Event Store
 ↓
Security Monitoring
```

---

## 107. Observability

ABAC must expose:

```text
Metrics
Logs
Traces
Decision latency
Policy evaluation latency
Decision counts
Error rates
Policy failures
```

---

## 108. Monitoring Alerts

Alerts should include:

```text
High authorization denial rate
Mass export attempts
Repeated policy bypass attempts
Privilege escalation
Unexpected AI tool access
Cross-tenant attempts
High-risk administrative actions
ABAC engine failure
Policy deployment failure
```

---

## 109. Disaster Recovery

ABAC configuration must be backed up.

Recovery must preserve:

```text
Policies
Policy versions
Policy bindings
Security configurations
Audit records
Delegations
Approval records
```

---

## 110. Availability

ABAC must not become a single point of failure.

Recommended:

```text
Multiple PDP instances
Replicated policy store
Distributed cache
Regional failover
Health checks
Circuit breakers
```

---

## 111. Development Requirements

All authorization-sensitive code must use centralized authorization libraries/middleware.

Developers must not implement arbitrary authorization logic independently in every endpoint.

Recommended:

```text
authorize(
    subject,
    action,
    resource,
    context
)
```

---

## 112. Testing Requirements

ABAC must have:

```text
Unit Tests
Integration Tests
Policy Tests
Security Tests
Penetration Tests
Load Tests
Failure Tests
Regression Tests
AI Authorization Tests
Cross-Tenant Tests
```

---

## 113. Mandatory Authorization Test Cases

The system must test:

```text
Correct user + correct organization
Correct user + wrong organization
Correct user + wrong workplace
Wrong role
Expired permission
Untrusted device
High-risk session
Missing MFA
Restricted resource
Bulk export
AI agent unauthorized action
Cross-tenant request
Suspended organization
Expired subscription
Policy conflict
Policy unavailable
```

---

## 114. Security Test

Example:

```text
User A:
organization = org_001

Resource:
organization = org_002

Action:
read

Expected:
DENY
```

This test must exist for every tenant-scoped resource class.

---

## 115. Performance Test

The authorization service must be load-tested under:

```text
1K RPS
10K RPS
50K RPS
100K+ RPS
```

Actual production capacity must be established through benchmarking and infrastructure sizing.

---

## 116. Functional ABAC Dashboard

Authorized administrators should see:

```text
Authorization Overview
Policies
Policy Simulator
Policy Versions
Access Requests
Denied Requests
High-Risk Requests
Human Review Queue
AI Access
Delegations
Resource Policies
Attribute Sources
Audit Logs
```

---

## 117. Policy Dashboard

Example:

```text
Policy Name
Status
Version
Priority
Scope
Created By
Approved By
Last Updated
Last Used
```

---

## 118. Human Review Dashboard

Security and authorized administrators should see:

```text
Request ID
Requester
Organization
Resource
Action
Risk
Reason
Requested At
Expiration
Reviewer
Status
```

---

## 119. Policy Governance

Policy lifecycle:

```text
Draft
 ↓
Testing
 ↓
Security Review
 ↓
Approval
 ↓
Published
 ↓
Monitoring
 ↓
Revision
 ↓
Deprecated
```

---

## 120. Separation of Duties

Critical policies must require multiple parties.

Example:

```text
Policy Creator
      ≠
Policy Approver
```

For highly sensitive policies:

```text
Security Admin
+
Organization Owner
```

may be required.

---

## 121. Administrative ABAC

Administrative permissions must also be attribute-controlled.

Examples:

```text
Super Admin
Platform Admin
Security Admin
Billing Admin
Organization Admin
Workplace Admin
```

must not automatically have unrestricted access to unrelated resources.

---

## 122. Business Growth Data Protection

SalesGenie's business intelligence data must be protected.

Sensitive resources include:

```text
profit
loss
revenue
ad spend
ROI
customer acquisition cost
conversion rate
product profitability
competitor analysis
business strategy
```

Access should depend on:

```text
role
organization
workplace
business unit
data classification
```

---

## 123. Marketing Data Protection

Marketing data may include:

```text
campaign performance
Facebook Ads
Instagram Ads
YouTube Ads
TikTok Ads
WhatsApp campaigns
LinkedIn campaigns
audience demographics
conversion data
ad spending
```

ABAC must protect these resources from unauthorized departments.

---

## 124. Lead Generation Data Protection

Lead-generation resources include:

```text
lead profiles
contact information
lead scores
company intelligence
prospecting data
enrichment data
sales signals
competitor data
```

These resources must have appropriate classification and authorization policies.

---

## 125. Customer Support Data Protection

Support resources include:

```text
customer conversations
tickets
customer identity
attachments
support history
internal notes
AI-generated responses
```

Internal notes must not automatically be visible to end users.

---

## 126. Product Intelligence Protection

Product analysis may contain:

```text
competitor strategy
market analysis
pricing analysis
product roadmap
profitability projections
business recommendations
```

These must be treated as confidential business intelligence.

---

## 127. AI-Generated Recommendation Protection

AI-generated strategic recommendations must support:

```text
organization ownership
role restrictions
versioning
auditability
human approval
```

---

## 128. External Client Access

External clients must only access explicitly shared resources.

Example:

```text
External Client
 ↓
Shared Report
 ↓
ABAC
 ↓
share.expiry > now
 ↓
share.organization == client.organization
 ↓
ALLOW
```

---

## 129. Shared Resource Expiration

Shared resources must support:

```text
expiration time
allowed users
allowed organization
allowed actions
download restriction
export restriction
```

---

## 130. Notification Requirements

Users should receive security notifications for sensitive authorization events.

Examples:

```text
New device
Password change
High-risk login
New permission
Permission revoked
Large export
Security review
Account recovery
```

---

## 131. Security Event Correlation

ABAC events should be correlated with:

```text
Authentication
Authorization
Billing
AI activity
API activity
Device activity
Session activity
Data export
Administrative actions
```

---

## 132. Advanced Risk-Based ABAC

The system may calculate:

```text
risk_score =
authentication_risk
+
device_risk
+
location_risk
+
behavioral_risk
+
resource_sensitivity
+
action_risk
```

The score must be generated by a trusted security/risk service rather than by the client.

---

## 133. Continuous Access Evaluation

If risk changes during a session:

```text
Normal
 ↓
Suspicious behavior detected
 ↓
Risk increases
 ↓
ABAC reevaluation
 ↓
Access restricted
```

---

## 134. Session Revocation

If a critical security event occurs:

```text
Session
 ↓
Risk Engine
 ↓
Critical risk
 ↓
ABAC
 ↓
Session revoked
```

---

## 135. Security Policy Examples

## Policy A — Sales Lead Access

```yaml
effect: allow

subject:
  role: sales_agent

resource:
  type: lead

conditions:
  same_organization: true
  same_workplace: true
  same_team: true
  risk_score:
    lt: 70
```

---

## 136. Security Policy B — Export

```yaml
effect: allow

subject:
  role:
    in:
      - sales_manager
      - organization_admin

action:
  - export

conditions:
  mfa_verified: true
  device_trusted: true
  risk_score:
    lt: 50
```

---

## 137. Security Policy C — AI Publishing

```yaml
subject:
  type: ai_agent

action:
  - publish

conditions:
  human_approval: true

effect: allow
```

---

## 138. Security Policy D — Finance

```yaml
subject:
  role:
    in:
      - finance_manager
      - billing_admin

resource:
  classification:
    in:
      - restricted
      - highly_restricted

conditions:
  mfa_verified: true

effect: allow
```

---

## 139. Security Policy E — External Client

```yaml
subject:
  type: external_client

resource:
  shared_with_subject: true

conditions:
  share_not_expired: true

actions:
  - read

effect: allow
```

---

## 140. Recommended Technology Architecture

The ABAC implementation should remain technology-agnostic at the requirements layer.

A production implementation may use:

```text
Policy Engine
+
Policy Store
+
Authorization Middleware
+
Risk Engine
+
Identity Service
+
Audit Service
```

Potential policy engines may include standards-compatible solutions such as:

```text
Open Policy Agent
Cedar
Casbin
custom policy engine
```

The final selection should be based on benchmarked requirements, operational complexity, ecosystem compatibility, and security review.

---

## 141. Service Architecture

```text
                    CLIENT
                       │
                       ↓
                API GATEWAY
                       │
                       ↓
             AUTHENTICATION LAYER
                       │
                       ↓
               POLICY ENFORCER
                       │
                       ↓
              ┌─────────────────┐
              │   ABAC / PDP    │
              └────────┬────────┘
                       │
       ┌───────────────┼────────────────┐
       ↓               ↓                ↓
 Identity          Risk Engine      Policy Store
       ↓               ↓                ↓
 Organization      Device Trust      Policy Cache
       │
       ↓
 Resource Service
       │
       ↓
 Business Service
       │
       ↓
 Database
```

---

## 142. Complete Authorization Flow

```text
1. User/AI sends request
          ↓
2. Authentication validates identity
          ↓
3. API Gateway receives request
          ↓
4. Policy Enforcement Point intercepts
          ↓
5. Subject attributes retrieved
          ↓
6. Resource attributes retrieved
          ↓
7. Environment attributes retrieved
          ↓
8. Risk engine evaluated
          ↓
9. Subscription evaluated
          ↓
10. Applicable policies retrieved
          ↓
11. ABAC engine evaluates policies
          ↓
12. Policy conflicts resolved
          ↓
13. Decision generated
          ↓
14. Obligations generated
          ↓
15. Human approval if required
          ↓
16. Resource access granted/restricted/denied
          ↓
17. Authorization event logged
          ↓
18. Analytics updated
```

---

## 143. ABAC + RBAC Architecture

```text
                  USER
                    ↓
              AUTHENTICATION
                    ↓
                   RBAC
                    ↓
             "WHAT ROLE?"
                    ↓
                   ABAC
                    ↓
             "UNDER WHAT
              CONDITIONS?"
                    ↓
            RESOURCE POLICY
                    ↓
             RISK ENGINE
                    ↓
          HUMAN APPROVAL?
              /          \
            YES           NO
             ↓             ↓
       HUMAN REVIEW      DECISION
             ↓
        APPROVE/DENY
             ↓
           ACCESS
```

---

## 144. ABAC + AI Architecture

```text
              AI AGENT
                  ↓
          AI Identity Token
                  ↓
           Tool Request
                  ↓
             ABAC/PDP
                  ↓
         Agent Permissions
                  ↓
          Resource Policy
                  ↓
            Risk Engine
                  ↓
        Action Risk Assessment
                  ↓
       ┌──────────┴───────────┐
       ↓                      ↓
    LOW/MEDIUM             HIGH
       ↓                      ↓
    EXECUTE             HUMAN REVIEW
                              ↓
                         APPROVE/DENY
```

---

## 145. Non-Functional Requirements

## NFR-ABAC-001 — Security

Authorization must follow defense-in-depth principles.

## NFR-ABAC-002 — Availability

ABAC must be highly available.

## NFR-ABAC-003 — Performance

Authorization latency must remain low and predictable.

## NFR-ABAC-004 — Scalability

ABAC must scale horizontally.

## NFR-ABAC-005 — Auditability

All sensitive decisions must be auditable.

## NFR-ABAC-006 — Explainability

Authorization decisions must be explainable to authorized administrators.

## NFR-ABAC-007 — Reliability

Authorization failures must fail securely.

## NFR-ABAC-008 — Maintainability

Policies must be independently manageable from application code.

## NFR-ABAC-009 — Testability

Policies must be automatically testable.

## NFR-ABAC-010 — Observability

ABAC must provide comprehensive metrics, logs, and traces.

---

## 146. Acceptance Criteria

The ABAC implementation will be considered production-ready when:

```text
✓ Every protected API supports authorization
✓ Tenant isolation is enforced
✓ Organization isolation is enforced
✓ Resource-level policies work
✓ Role + attribute policies work
✓ Risk-based policies work
✓ Device-based policies work
✓ Location-based policies work
✓ Time-based policies work
✓ Subscription policies work
✓ Field-level masking works
✓ Export controls work
✓ AI agents have separate identities
✓ AI tools are authorization-controlled
✓ High-risk AI actions support human approval
✓ Temporary permissions expire
✓ Break-glass access is audited
✓ Policy versioning works
✓ Policy rollback works
✓ Policy simulation works
✓ Authorization decisions are logged
✓ Security administrators can investigate events
✓ Cross-tenant attacks are blocked
✓ Privilege escalation is blocked
✓ Fail-closed behavior works
✓ Performance targets are benchmarked
✓ Load testing is completed
✓ Security testing is completed
✓ Audit integrity is validated
```

---

## 147. Final SalesGenie ABAC Security Model

SalesGenie's final authorization architecture should be:

```text
                    ┌───────────────────────┐
                    │       USER / AI       │
                    └───────────┬───────────┘
                                ↓
                    ┌───────────────────────┐
                    │    AUTHENTICATION     │
                    └───────────┬───────────┘
                                ↓
                    ┌───────────────────────┐
                    │        RBAC           │
                    │   Role / Permission   │
                    └───────────┬───────────┘
                                ↓
                    ┌───────────────────────┐
                    │        ABAC           │
                    │ Subject + Resource +  │
                    │ Action + Environment  │
                    └───────────┬───────────┘
                                ↓
                    ┌───────────────────────┐
                    │    RISK ENGINE        │
                    └───────────┬───────────┘
                                ↓
                    ┌───────────────────────┐
                    │ SECURITY / COMPLIANCE │
                    └───────────┬───────────┘
                                ↓
                    ┌───────────────────────┐
                    │ HUMAN APPROVAL        │
                    │    IF REQUIRED        │
                    └───────────┬───────────┘
                                ↓
                    ┌───────────────────────┐
                    │ AUTHORIZATION RESULT  │
                    └───────────┬───────────┘
                                ↓
             ┌──────────────────┼──────────────────┐
             ↓                  ↓                  ↓
           ALLOW              LIMIT              DENY
             ↓                  ↓
        RESOURCE ACCESS   MASK / RESTRICT
             │
             ↓
        ┌─────────────────┐
        │ AUDIT + MONITOR │
        └─────────────────┘
```

---

## 148. Final Principle

SalesGenie must implement ABAC as a **centralized, policy-driven, zero-trust authorization layer** rather than scattering permission checks throughout individual services.

The final authorization model is:

```text
Authentication
      +
RBAC
      +
ABAC
      +
Resource-Level Authorization
      +
Risk-Based Authorization
      +
Subscription Authorization
      +
AI Agent Authorization
      +
Human-in-the-Loop Security
      +
Tenant Isolation
      +
Continuous Evaluation
      +
Immutable Audit
      =
Enterprise-Grade SalesGenie Authorization
```

The most important security rule is:

```text
IDENTITY ALONE IS NEVER SUFFICIENT FOR ACCESS.
```

SalesGenie must determine access based on:

```text
WHO
+
WHAT ROLE
+
WHICH ORGANIZATION
+
WHICH WORKPLACE
+
WHICH TEAM
+
WHAT RESOURCE
+
WHAT ACTION
+
WHAT DATA CLASSIFICATION
+
WHAT DEVICE
+
WHAT LOCATION
+
WHAT TIME
+
WHAT RISK
+
WHAT SUBSCRIPTION
+
WHAT AI AUTHORITY
+
WHAT POLICY
+
WHETHER HUMAN APPROVAL IS REQUIRED
```

and only then produce:

```text
ALLOW
DENY
STEP_UP_AUTH
HUMAN_REVIEW
LIMITED_ACCESS
MASK_DATA
READ_ONLY
```

This ABAC layer is therefore the **context-aware authorization foundation** of the SalesGenie security architecture and must operate across human users, AI agents, APIs, microservices, external integrations, business data, financial data, marketing data, lead-generation data, support data, and administrative operations.
