# SalesGenie — Feature Entitlements Requirements

**Document:** `feature_entitlements.md`  
**Product:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Requirement Level:** FAANG-Level / Production-Grade  
**Scope:** Feature entitlement management, plan-based access control, tenant entitlements, AI/human access, feature lifecycle, trials, add-ons, overrides, usage integration, RBAC integration, entitlement evaluation, auditability, and enforcement.

---

## 1. Purpose

The Feature Entitlements subsystem SHALL determine which SalesGenie capabilities a tenant, user, human agent, AI agent, workflow, API client, or integration is permitted to access.

Feature entitlements SHALL operate independently from usage limits while integrating with the Plan Limits subsystem.

The architecture SHALL distinguish:

```text
Subscription
    ↓
Plan
    ↓
Feature Entitlements
    ↓
Role / Permission
    ↓
Context Policy
    ↓
Entitlement Evaluation
    ↓
Feature Access
```

A user MUST NOT receive access to a feature merely because the feature exists in the application.

---

## 2. Product Context

SalesGenie supports:

* AI customer support
* AI sales agents
* Human support agents
* Human sales agents
* Multi-agent orchestration
* RAG knowledge management
* Lead generation
* Lead intelligence
* Omnichannel communication
* Workflow automation
* MCP tools
* External integrations
* Voice AI
* Analytics
* CRM automation
* Document intelligence
* Billing and subscriptions
* Enterprise administration
* API access

Feature entitlements SHALL provide the commercial and technical control plane for these capabilities.

---

## 3. Core Entitlement Model

SalesGenie SHALL evaluate access using:

```text
Identity
    +
Tenant
    +
Subscription
    +
Plan
    +
Feature Entitlement
    +
RBAC Permission
    +
Context
    +
Policy
    =
Access Decision
```

The system MUST NOT treat:

```text
UI visibility
Frontend flags
Local storage
Client-side configuration
```

as authoritative entitlement mechanisms.

---

## 4. Actors

The entitlement system SHALL support:

```text
End User
Sales Agent
Support Agent
Team Lead
Manager
Organization Admin
Billing Admin
Developer
Analyst
Human Supervisor
Super Admin
AI Agent
AI Supervisor Agent
Workflow Engine
MCP Agent
API Client
Integration Service
Background Worker
System Service
```

---

## 5. User Requirements

## UR-FE-001 — Feature Visibility

Users SHALL only see features they are entitled to use.

---

## UR-FE-002 — Feature Access

Users SHALL be prevented from executing unauthorized features even if they manually construct API requests.

---

## UR-FE-003 — Plan Transparency

Authorized users SHALL be able to view which features are included in their current plan.

---

## UR-FE-004 — Feature Status

The UI SHALL distinguish:

```text
AVAILABLE
LOCKED
TRIAL
ADD-ON
COMING_SOON
ADMIN_ONLY
REQUIRES_UPGRADE
SUSPENDED
```

---

## UR-FE-005 — Upgrade Guidance

When a feature is unavailable because of the current plan, the system SHOULD provide:

* Required plan
* Upgrade option
* Add-on option
* Trial option where applicable
* Reason for restriction

---

## UR-FE-006 — Entitlement-Aware Navigation

The platform SHALL dynamically configure navigation based on:

* Plan
* Entitlements
* User role
* Organization policy
* Feature status

---

## UR-FE-007 — AI Feature Awareness

AI agents SHALL know which capabilities they are permitted to invoke.

---

## UR-FE-008 — Human Feature Awareness

Human operators SHALL receive accurate feature availability based on their organization and role.

---

## UR-FE-009 — Feature Trial

Where enabled, users SHALL be able to access eligible features during a defined trial period.

---

## UR-FE-010 — Feature Expiration

Users SHALL lose access automatically when an entitlement expires unless another entitlement grants access.

---

## 6. System Requirements

## SR-FE-001 — Centralized Entitlement Service

SalesGenie SHALL provide a centralized Feature Entitlement Service.

The service SHALL be authoritative for feature-access decisions.

---

## SR-FE-002 — Tenant Isolation

Every entitlement SHALL be scoped to a tenant or organization.

Cross-tenant entitlement access MUST be impossible.

---

## SR-FE-003 — Server-Side Enforcement

All commercially controlled features MUST be enforced server-side.

---

## SR-FE-004 — RBAC Integration

Feature entitlements MUST integrate with authorization.

The following condition SHALL apply:

```text
Feature Entitled
        AND
Role Authorized
        AND
Context Authorized
        =
Feature Accessible
```

---

## SR-FE-005 — Subscription Integration

Entitlements SHALL be derived from the active subscription and associated plan.

---

## SR-FE-006 — Plan Versioning

Entitlement configurations SHALL be versioned.

Historical subscriptions MUST retain the appropriate entitlement policy.

---

## SR-FE-007 — Add-On Support

The architecture SHALL support feature add-ons independently from base plans.

---

## SR-FE-008 — Temporary Entitlements

The system SHALL support temporary feature access.

Examples:

```text
Trial
Promotion
Beta access
Enterprise exception
Support grant
Temporary override
```

---

## 7. Entitlement Types

## FR-FE-001

The platform SHALL support the following entitlement types:

```text
BOOLEAN
QUANTITY
USAGE
TIER
CAPABILITY
ROLE
MODEL
CHANNEL
INTEGRATION
API
TEMPORARY
ADD_ON
TRIAL
```

---

## 8. Boolean Entitlements

## FR-FE-002

Boolean entitlements SHALL represent simple feature availability.

Example:

```yaml
ai_customer_support:
  enabled: true

voice_ai:
  enabled: false

advanced_analytics:
  enabled: true
```

---

## 9. Quantity Entitlements

## FR-FE-003

Quantity entitlements SHALL define maximum resources.

Examples:

```text
AI agents
Human agents
Knowledge bases
Integrations
Workflows
Campaigns
API clients
```

---

## 10. Usage Entitlements

## FR-FE-004

Usage entitlements SHALL integrate with Plan Limits.

Examples:

```text
AI messages
Voice minutes
Lead generation credits
Workflow executions
MCP calls
API requests
```

---

## 11. Tiered Entitlements

## FR-FE-005

Features MAY have capability tiers.

Example:

```text
RAG_BASIC
RAG_ADVANCED
RAG_ENTERPRISE
```

Another example:

```text
ANALYTICS_BASIC
ANALYTICS_ADVANCED
ANALYTICS_ENTERPRISE
```

---

## 12. Feature Catalog

SalesGenie SHOULD maintain a centralized feature catalog.

Example categories:

```text
AI
SALES
SUPPORT
LEADS
WORKFLOWS
RAG
VOICE
CHANNELS
INTEGRATIONS
MCP
ANALYTICS
SECURITY
ADMIN
API
BILLING
ENTERPRISE
```

---

## 13. AI Feature Entitlements

## FR-FE-006

The system SHALL support entitlements for:

```text
AI customer support
AI sales agents
AI lead qualification
AI lead generation
AI lead enrichment
AI email generation
AI response generation
AI conversation summarization
AI sentiment analysis
AI intent classification
AI forecasting
AI workflow generation
AI agent builder
Multi-agent orchestration
AI memory
AI RAG
AI voice
AI document intelligence
AI analytics
AI autonomous actions
```

---

## 14. Human Feature Entitlements

## FR-FE-007

Human users SHALL receive entitlements for:

```text
Human inbox
Conversation management
Lead management
CRM access
Workflow management
Knowledge-base management
Analytics
Campaign management
Integration management
Team management
AI-agent supervision
Conversation takeover
Approval workflows
Audit access
Billing access
```

---

## 15. AI + Human Hybrid Entitlements

## FR-FE-008

SalesGenie SHALL support hybrid features where AI and humans collaborate.

Examples:

```text
AI drafts response
        ↓
Human reviews
        ↓
Human approves
        ↓
System sends
```

and:

```text
AI handles conversation
        ↓
Confidence falls below threshold
        ↓
Human handoff
        ↓
Human takes control
```

---

## 16. Channel Entitlements

## FR-FE-009

The platform SHALL support channel-level entitlements.

Example:

```text
WEB_CHAT
EMAIL
GMAIL
WHATSAPP
FACEBOOK
INSTAGRAM
LINKEDIN
TIKTOK
YOUTUBE
SLACK
MICROSOFT_TEAMS
VOICE
SMS
```

Each channel MAY be independently entitled.

---

## 17. Integration Entitlements

## FR-FE-010

The system SHALL support integration-specific entitlements.

Examples:

```text
Google
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

## 18. MCP Entitlements

## FR-FE-011

The platform SHALL support MCP-specific entitlements.

Examples:

```text
MCP access
MCP server connections
MCP tool execution
Custom MCP servers
Marketplace MCP servers
Enterprise MCP policies
```

---

## 19. Workflow Entitlements

## FR-FE-012

The system SHALL support:

```text
Workflow builder
Workflow execution
Scheduled workflows
Event-driven workflows
AI-generated workflows
Human approval steps
Conditional branches
Parallel execution
External API actions
MCP actions
Custom workflow nodes
```

---

## 20. RAG Entitlements

## FR-FE-013

The platform SHALL support:

```text
Basic RAG
Advanced RAG
Hybrid search
Vector search
Semantic search
Knowledge graphs
Document ingestion
Custom embeddings
Advanced retrieval
Reranking
Enterprise knowledge isolation
```

---

## 21. Lead Generation Entitlements

## FR-FE-014

The platform SHALL support:

```text
Company search
Contact search
Lead generation
Lead enrichment
Intent detection
Lead scoring
ICP analysis
Lead qualification
Automated outreach
Lead intelligence
```

---

## 22. Voice Entitlements

## FR-FE-015

The system SHALL support:

```text
Voice AI
Inbound calls
Outbound calls
Call transcription
Call summarization
Call recording
Voice analytics
AI voice agents
Human handoff
```

---

## 23. Analytics Entitlements

## FR-FE-016

The system SHALL support:

```text
Basic analytics
Advanced analytics
AI analytics
Sales analytics
Support analytics
Agent analytics
Conversation analytics
Revenue analytics
Usage analytics
Custom reports
Export
Scheduled reports
```

---

## 24. Security Entitlements

## FR-FE-017

Enterprise security capabilities MAY include:

```text
SSO
SAML
SCIM
MFA policies
IP allowlists
Advanced audit logs
Security analytics
Data retention policies
Custom roles
Advanced RBAC
Enterprise compliance controls
```

---

## 25. API Entitlements

## FR-FE-018

The platform SHALL support:

```text
REST API
Webhooks
API keys
OAuth applications
Service accounts
Custom integrations
Bulk APIs
Enterprise APIs
```

---

## 26. Admin Entitlements

## FR-FE-019

Administrative features SHALL include:

```text
Organization management
User management
Role management
Feature management
Integration management
Billing management
Usage management
Audit logs
Security settings
Policy management
```

---

## 27. Entitlement Evaluation

## FR-FE-020

The entitlement engine SHALL expose a deterministic evaluation function.

Conceptually:

```text
evaluate(
    tenant,
    subject,
    feature,
    context
)
→
EntitlementDecision
```

---

## FR-FE-021

The decision SHALL include:

```json
{
  "allowed": true,
  "feature": "ai_voice",
  "source": "enterprise_plan",
  "status": "ACTIVE",
  "expires_at": null,
  "reason": "Feature included in subscription"
}
```

---

## 28. Entitlement Precedence

## FR-FE-022

The system SHALL define deterministic precedence.

Recommended precedence:

```text
Emergency Deny
      ↓
Tenant Suspension
      ↓
Explicit Security Deny
      ↓
Role Authorization
      ↓
Temporary Override
      ↓
Add-On Entitlement
      ↓
Plan Entitlement
      ↓
Trial Entitlement
      ↓
Default Deny
```

The exact precedence SHALL be centrally configured and versioned.

---

## 29. Default Deny

## FR-FE-023

Unknown features MUST default to denied.

Example:

```text
Unknown feature
      ↓
No entitlement
      ↓
DENY
```

---

## 30. Entitlement Expiration

## FR-FE-024

Entitlements SHALL support:

```text
starts_at
expires_at
renewal_behavior
status
```

---

## FR-FE-025

Expired entitlements MUST NOT grant access.

---

## 31. Subscription Changes

## FR-FE-026

When a subscription changes:

```text
Subscription Change
       ↓
Plan Resolution
       ↓
Entitlement Recalculation
       ↓
Entitlement Cache Invalidation
       ↓
New Access State
```

---

## 32. Upgrade Workflow

```text
Customer
   ↓
Select Higher Plan
   ↓
Payment
   ↓
Subscription Update
   ↓
Entitlement Calculation
   ↓
Entitlement Activation
   ↓
Cache Invalidation
   ↓
Feature Available
```

---

## 33. Downgrade Workflow

```text
Customer
   ↓
Select Lower Plan
   ↓
Downgrade Validation
   ↓
Identify Lost Features
   ↓
Identify Active Dependencies
   ↓
Customer Confirmation
   ↓
Subscription Update
   ↓
Entitlement Revocation
   ↓
Grace Period / Immediate Enforcement
```

The system MUST prevent silent destructive behavior.

---

## 34. Add-On Workflow

```text
Customer
   ↓
Select Feature Add-On
   ↓
Eligibility Check
   ↓
Payment
   ↓
Add-On Activation
   ↓
Entitlement Grant
   ↓
Audit Event
```

---

## 35. Trial Workflow

```text
Eligible Customer
      ↓
Start Trial
      ↓
Create Temporary Entitlement
      ↓
Trial Active
      ↓
Warning Notifications
      ↓
Trial Expiration
      ↓
Convert / Renew / Revoke
```

---

## 36. AI-Based Entitlement Requirements

## AI-FE-001

AI agents SHALL query the entitlement engine before invoking restricted capabilities.

---

## AI-FE-002

AI agents SHALL NOT infer entitlement from:

```text
Conversation history
User claims
Prompt instructions
Frontend state
Cached UI state
```

---

## AI-FE-003

AI agents SHALL use authoritative entitlement APIs.

---

## AI-FE-004

If an AI agent lacks entitlement, it SHALL provide a controlled explanation rather than attempting a bypass.

---

## AI-FE-005

AI agents MAY recommend:

* Upgrade
* Add-on
* Trial
* Human escalation

when a feature is unavailable.

---

## AI-FE-006

AI agents SHALL NOT:

```text
Grant themselves features
Modify entitlements
Modify subscriptions
Bypass RBAC
Bypass tenant policies
Disable security restrictions
Invoke restricted MCP tools
```

---

## 37. Human-Based Entitlement Requirements

## HUMAN-FE-001

Organization Admins SHALL be able to view feature entitlements.

---

## HUMAN-FE-002

Billing Admins SHALL be able to view commercially relevant entitlements.

---

## HUMAN-FE-003

Super Admins SHALL be able to configure global entitlement policies.

---

## HUMAN-FE-004

Support personnel MAY receive temporary feature grants when authorized.

---

## HUMAN-FE-005

Temporary grants SHALL require:

```text
Reason
Actor
Approver where required
Start time
Expiration time
Affected tenant
Affected feature
Audit record
```

---

## 38. Entitlement Override

## FR-FE-027

Authorized administrators SHALL be able to create feature overrides.

Example:

```yaml
override:
  tenant_id: tenant_123
  feature: advanced_analytics
  action: GRANT
  starts_at: "2026-08-28T00:00:00Z"
  expires_at: "2026-09-28T00:00:00Z"
  reason: "Enterprise pilot"
```

---

## 39. Override Security

## FR-FE-028

High-risk overrides SHOULD require dual authorization.

---

## FR-FE-029

Overrides MUST be audited.

---

## FR-FE-030

Overrides MUST automatically expire.

---

## 40. Entitlement Dependencies

## FR-FE-031

Features SHALL support dependencies.

Example:

```text
AI Voice
   ↓
AI Agent
   ↓
Voice Provider
   ↓
Voice Minutes Entitlement
```

Another example:

```text
Advanced RAG
   ↓
Basic RAG
   ↓
Knowledge Base
   ↓
Document Storage
```

---

## FR-FE-032

The system SHALL validate dependencies before activation.

---

## 41. Feature Bundles

## FR-FE-033

The system SHALL support feature bundles.

Example:

```yaml
enterprise_ai_bundle:
  features:
    - multi_agent
    - advanced_rag
    - ai_voice
    - advanced_analytics
    - custom_workflows
    - enterprise_api
```

---

## 42. Feature Conflicts

## FR-FE-034

The entitlement engine SHALL support conflicting policies.

Example:

```text
Feature Grant
      +
Security Deny
      =
DENY
```

---

## 43. Organization-Level Entitlements

## FR-FE-035

Organization-level entitlements SHALL define capabilities available to the tenant.

---

## 44. User-Level Entitlements

## FR-FE-036

The system MAY support user-specific entitlements.

Example:

```text
Organization:
AI Voice = ENABLED

User:
AI Voice = DENIED
```

The effective decision MUST respect security and authorization policy.

---

## 45. AI-Agent-Level Entitlements

## FR-FE-037

Each AI agent MAY have capability restrictions.

Example:

```yaml
ai_sales_agent:
  capabilities:
    - read_leads
    - score_leads
    - draft_email

  denied:
    - delete_customer
    - refund_payment
```

---

## 46. Workflow-Level Entitlements

## FR-FE-038

Workflows SHALL execute only entitled actions.

A workflow MUST NOT bypass feature restrictions merely because it was previously configured.

---

## 47. MCP Tool Entitlements

## FR-FE-039

MCP tool execution SHALL validate:

```text
Tenant entitlement
+
Agent capability
+
Tool permission
+
Integration entitlement
+
Usage limit
```

before execution.

---

## 48. API Enforcement

## FR-FE-040

All feature-controlled APIs SHALL enforce entitlements.

Example:

```http
POST /api/v1/voice/calls
```

MUST verify:

```text
voice_ai entitlement
+
voice_call capability
+
voice usage limit
```

---

## 49. Frontend Enforcement

## FR-FE-041

The frontend MAY hide unavailable features.

---

## FR-FE-042

The frontend SHALL NOT be considered authoritative.

---

## FR-FE-043

Frontend entitlement state SHALL be refreshable after:

```text
Plan upgrade
Plan downgrade
Add-on purchase
Trial expiration
Admin override
Subscription suspension
```

---

## 50. Entitlement Cache

## FR-FE-044

Entitlement decisions MAY be cached.

Cache entries SHALL include:

```text
tenant_id
subject_id
feature
policy_version
decision
expires_at
```

---

## FR-FE-045

Critical entitlement changes SHALL invalidate relevant caches immediately or within a defined SLA.

---

## 51. Entitlement APIs

## FR-FE-046

SalesGenie SHALL provide APIs such as:

```http
GET    /api/v1/entitlements
GET    /api/v1/entitlements/{feature}
POST   /api/v1/entitlements/check
GET    /api/v1/entitlements/catalog
GET    /api/v1/entitlements/features
GET    /api/v1/entitlements/dependencies
GET    /api/v1/admin/entitlements
POST   /api/v1/admin/entitlements/overrides
PATCH  /api/v1/admin/entitlements/overrides/{id}
DELETE /api/v1/admin/entitlements/overrides/{id}
```

---

## 52. Bulk Entitlement Evaluation

## FR-FE-047

The system SHOULD support batch evaluation.

Example:

```json
{
  "features": [
    "ai_voice",
    "advanced_rag",
    "mcp",
    "advanced_analytics",
    "salesforce"
  ]
}
```

---

## 53. Entitlement Error Codes

The platform SHALL return deterministic errors.

```text
FEATURE_NOT_ENTITLED
FEATURE_DISABLED
FEATURE_EXPIRED
FEATURE_SUSPENDED
PLAN_FEATURE_UNAVAILABLE
ADDON_REQUIRED
TRIAL_EXPIRED
ENTITLEMENT_OVERRIDE_EXPIRED
ENTITLEMENT_DEPENDENCY_MISSING
ROLE_NOT_AUTHORIZED
TENANT_SUSPENDED
FEATURE_POLICY_DENIED
UNKNOWN_FEATURE
```

---

## 54. Data Model

## FR-FE-048 — Feature

```text
Feature
-------
id
feature_key
name
description
category
type
status
risk_level
version
created_at
updated_at
```

---

## FR-FE-049 — PlanFeatureEntitlement

```text
PlanFeatureEntitlement
----------------------
id
plan_id
plan_version
feature_id
enabled
value
tier
configuration
effective_from
effective_until
created_at
updated_at
```

---

## FR-FE-050 — TenantEntitlement

```text
TenantEntitlement
-----------------
id
tenant_id
feature_id
source_type
source_id
status
value
tier
starts_at
expires_at
policy_version
created_at
updated_at
```

---

## FR-FE-051 — UserEntitlement

```text
UserEntitlement
---------------
id
tenant_id
user_id
feature_id
action
value
status
starts_at
expires_at
created_by
created_at
updated_at
```

---

## FR-FE-052 — AI Agent Entitlement

```text
AIAgentEntitlement
------------------
id
tenant_id
agent_id
feature_id
capability
allowed
policy_version
starts_at
expires_at
created_at
updated_at
```

---

## FR-FE-053 — EntitlementOverride

```text
EntitlementOverride
-------------------
id
tenant_id
feature_id
action
previous_state
new_state
reason
requested_by
approved_by
starts_at
expires_at
status
created_at
updated_at
```

---

## 55. Entitlement Audit

## FR-FE-054

Every entitlement modification SHALL create an audit event.

The event SHALL contain:

```text
event_id
tenant_id
feature_id
actor_id
actor_type
action
previous_state
new_state
reason
timestamp
request_id
correlation_id
approval_id
```

---

## 56. Observability

The system SHALL expose metrics including:

```text
entitlement_checks_total
entitlement_denials_total
entitlement_grants_total
entitlement_overrides_total
entitlement_expirations_total
entitlement_cache_hits_total
entitlement_cache_misses_total
entitlement_evaluation_errors_total
feature_dependency_failures_total
feature_upgrade_prompts_total
```

---

## 57. Security Requirements

## SEC-FE-001

Entitlement APIs MUST require authentication.

---

## SEC-FE-002

Entitlement modifications MUST require explicit authorization.

---

## SEC-FE-003

Tenant identifiers MUST be validated against the authenticated principal.

---

## SEC-FE-004

Client-provided entitlement values MUST NEVER be trusted.

---

## SEC-FE-005

The system MUST prevent privilege escalation through entitlement manipulation.

---

## SEC-FE-006

AI agents MUST operate under least-privilege capability policies.

---

## SEC-FE-007

Support overrides MUST be restricted and audited.

---

## 58. Reliability Requirements

## REL-FE-001

The entitlement service SHALL be highly available.

---

## REL-FE-002

Temporary entitlement-service failures SHALL NOT silently grant unauthorized access.

---

## REL-FE-003

Critical feature checks SHOULD fail closed.

---

## REL-FE-004

Cached entitlement decisions SHALL have bounded TTLs.

---

## 59. Performance Requirements

## PERF-FE-001

Simple entitlement checks SHOULD target:

```text
P95 < 50 ms
```

under normal production conditions.

---

## PERF-FE-002

Batch entitlement checks SHOULD avoid repeated database lookups.

---

## PERF-FE-003

Entitlement evaluation SHALL NOT materially degrade AI response latency.

---

## 60. Scalability Requirements

The entitlement architecture SHALL support:

```text
Millions of tenants
Millions of users
Millions of AI agents
Thousands of feature definitions
Billions of entitlement checks
High-volume API traffic
High-volume AI inference
```

The service SHALL support horizontal scaling.

---

## 61. Feature Lifecycle

Features SHALL support:

```text
DRAFT
BETA
ACTIVE
DEPRECATED
SUNSET
DISABLED
```

---

## 62. Feature Launch Workflow

```text
Feature Definition
      ↓
Security Review
      ↓
Entitlement Configuration
      ↓
Internal Testing
      ↓
Beta
      ↓
Limited Tenant Rollout
      ↓
General Availability
```

---

## 63. Feature Sunset Workflow

```text
Feature Deprecation
      ↓
Customer Notification
      ↓
Migration Recommendation
      ↓
Grace Period
      ↓
Feature Disabled
      ↓
Legacy Data Retention / Migration
```

---

## 64. AI Feature Rollout

The system SHOULD support AI-assisted rollout decisions.

Example:

```text
Feature Performance
        +
Tenant Adoption
        +
Error Rate
        +
Cost
        +
Security Signals
        ↓
AI Rollout Recommendation
        ↓
Human Approval
        ↓
Feature Expansion
```

AI MUST NOT autonomously bypass production governance controls.

---

## 65. Plan and Feature Matrix

SalesGenie SHALL support a centralized matrix such as:

| Feature             |    Free | Starter | Professional | Business | Enterprise |
| ------------------- | ------: | ------: | -----------: | -------: | ---------: |
| Basic AI Support    |       ✓ |       ✓ |            ✓ |        ✓ |          ✓ |
| AI Sales Agent      | Limited |       ✓ |            ✓ |        ✓ |          ✓ |
| Multi-Agent         |       — | Limited |            ✓ |        ✓ |          ✓ |
| RAG                 | Limited |       ✓ |            ✓ |        ✓ |          ✓ |
| Advanced RAG        |       — |       — |            ✓ |        ✓ |          ✓ |
| Lead Generation     | Limited |       ✓ |            ✓ |        ✓ |          ✓ |
| Workflow Automation | Limited |       ✓ |            ✓ |        ✓ |          ✓ |
| MCP                 |       — | Limited |            ✓ |        ✓ |          ✓ |
| Voice AI            |       — |       — |            ✓ |        ✓ |          ✓ |
| Advanced Analytics  |       — |       — |            ✓ |        ✓ |          ✓ |
| SSO                 |       — |       — |            — |        ✓ |          ✓ |
| SCIM                |       — |       — |            — |        — |          ✓ |
| Custom Roles        |       — |       — |            ✓ |        ✓ |          ✓ |
| Enterprise API      |       — |       — |            — |        ✓ |          ✓ |

The actual commercial matrix SHALL remain configuration-driven rather than hard-coded.

---

## 66. Feature Dependency Example

```text
Advanced AI Sales Agent
        ↓
AI Agent Builder
        ↓
AI Agent Entitlement
        ↓
LLM Access
        ↓
AI Token Limit
        ↓
Required Integration
```

All dependencies SHALL be validated before execution.

---

## 67. AI + Human Collaboration Workflow

```text
Customer
   ↓
AI Agent
   ↓
Check AI Entitlement
   ↓
Execute AI Capability
   ↓
Confidence Evaluation
   ↓
Human Handoff Required?
      |
      +---- NO ----> AI Completes Task
      |
      +---- YES
              ↓
       Check Human Entitlement
              ↓
       Assign Human Agent
              ↓
       Human Intervention
              ↓
       Complete Task
              ↓
       Record Usage
```

---

## 68. Entitlement + Limit Integration

Feature entitlements SHALL determine **whether a capability exists**.

Plan limits SHALL determine **how much it can be used**.

Example:

```text
AI Voice Entitlement
        ↓
YES
        ↓
Voice Minutes Limit
        ↓
1000 minutes
        ↓
Current Usage
        ↓
850 minutes
        ↓
Remaining
        ↓
150 minutes
```

Therefore:

```text
Entitlement = Capability Access
Limit = Resource Capacity
Authorization = Actor Permission
```

All three SHALL be enforced independently.

---

## 69. Example Entitlement Configuration

```yaml
plan:
  id: professional
  version: 3

features:

  ai_customer_support:
    enabled: true

  ai_sales_agent:
    enabled: true
    tier: advanced

  multi_agent:
    enabled: true

  advanced_rag:
    enabled: true

  voice_ai:
    enabled: true

  mcp:
    enabled: true

  workflow_automation:
    enabled: true

  advanced_analytics:
    enabled: true

  sso:
    enabled: false

  scim:
    enabled: false

  enterprise_api:
    enabled: false

integrations:

  gmail:
    enabled: true

  google_drive:
    enabled: true

  salesforce:
    enabled: true

  hubspot:
    enabled: true

  zendesk:
    enabled: true
```

---

## 70. End-to-End Feature Access Workflow

```text
User / AI Agent
       ↓
Authentication
       ↓
Tenant Resolution
       ↓
RBAC Authorization
       ↓
Feature Request
       ↓
Entitlement Evaluation
       ↓
Dependency Evaluation
       ↓
Plan Limit Evaluation
       ↓
Context Policy
       ↓
Allowed?
   /         \
 NO           YES
 |             |
Deny          Execute
 |             |
Reason         Meter Usage
 |             |
Upgrade /      Audit
Support        Analytics
```

---

## 71. AI Tool Invocation Workflow

```text
AI Agent
   ↓
Select Tool
   ↓
Tool Entitlement Check
   ↓
Agent Capability Check
   ↓
Tenant Policy Check
   ↓
MCP / Integration Entitlement
   ↓
Plan Limit Check
   ↓
Allowed?
   /      \
 NO        YES
 |          |
Reject      Execute
            ↓
         Record Usage
```

---

## 72. Human Feature Access Workflow

```text
Human User
    ↓
Authentication
    ↓
Tenant
    ↓
Role
    ↓
Permission
    ↓
Feature Entitlement
    ↓
Feature Dependency
    ↓
Plan Limit
    ↓
Access
```

---

## 73. Feature Lock UX

When a feature is unavailable, the UI SHOULD communicate:

```text
Feature
Status
Reason
Required Plan
Current Plan
Upgrade Option
Trial Option
Contact Sales
```

Example:

```text
Advanced RAG

Not included in your current plan.

Available in Professional and Enterprise.

[Upgrade Plan]
[Start Trial]
```

---

## 74. Entitlement Revocation

When an entitlement is revoked:

```text
Entitlement Revoked
       ↓
Cache Invalidation
       ↓
Active Session Update
       ↓
Future Requests Denied
       ↓
Running Operations Policy
       ↓
Audit Event
```

Long-running operations SHALL follow a predefined revocation policy.

---

## 75. Grace Periods

The system MAY support grace periods for:

```text
Subscription expiration
Payment failure
Plan downgrade
Feature retirement
Temporary entitlement expiration
```

Grace periods MUST be explicitly configured.

---

## 76. Billing Integration

Feature entitlements SHALL integrate with billing events:

```text
Payment Success
       ↓
Subscription Active
       ↓
Entitlements Activated
```

and:

```text
Payment Failure
       ↓
Subscription State Change
       ↓
Entitlement Policy
       ↓
Grace / Restrict / Suspend
```

---

## 77. Subscription Cancellation

Cancellation SHALL follow a configured policy:

```text
Cancel Immediately
OR
Cancel At Period End
```

The entitlement engine MUST calculate access accordingly.

---

## 78. Enterprise Custom Entitlements

Enterprise customers MAY receive custom entitlements.

Examples:

```text
Custom AI models
Custom MCP servers
Private integrations
Higher API access
Custom security features
Dedicated voice capacity
Advanced analytics
Custom workflow capabilities
```

Custom entitlements SHALL be tenant-specific and auditable.

---

## 79. Entitlement Reconciliation

The platform SHALL periodically reconcile:

```text
Subscription
      ↕
Plan
      ↕
Plan Features
      ↕
Tenant Entitlements
      ↕
Overrides
      ↕
RBAC
      ↕
Effective Access
```

The system SHALL identify:

* Missing entitlements
* Unexpected entitlements
* Expired grants
* Invalid overrides
* Plan mismatches
* Subscription mismatches
* Unauthorized grants

---

## 80. Acceptance Criteria

## AC-FE-001

Only entitled tenants can access commercial features.

## AC-FE-002

Unauthorized users cannot access features through direct API calls.

## AC-FE-003

Frontend manipulation cannot bypass entitlements.

## AC-FE-004

Unknown features default to denied.

## AC-FE-005

Plan upgrades activate the correct entitlements.

## AC-FE-006

Plan downgrades remove or restrict features according to policy.

## AC-FE-007

Add-ons activate their associated entitlements.

## AC-FE-008

Expired trials revoke temporary entitlements.

## AC-FE-009

Temporary overrides expire automatically.

## AC-FE-010

Entitlement changes invalidate stale caches.

## AC-FE-011

AI agents cannot grant themselves entitlements.

## AC-FE-012

AI agents cannot bypass feature restrictions.

## AC-FE-013

Human administrators require authorization to modify entitlements.

## AC-FE-014

High-risk entitlement changes can require approval.

## AC-FE-015

MCP tools respect feature entitlements.

## AC-FE-016

Workflows respect feature entitlements.

## AC-FE-017

Integrations respect feature entitlements.

## AC-FE-018

Feature dependencies are validated.

## AC-FE-019

Feature conflicts resolve deterministically.

## AC-FE-020

Feature entitlements integrate with Plan Limits.

## AC-FE-021

Feature entitlements integrate with RBAC.

## AC-FE-022

All entitlement modifications are audited.

## AC-FE-023

Cross-tenant entitlement access is impossible.

## AC-FE-024

Subscription suspension applies the correct entitlement policy.

## AC-FE-025

Enterprise custom entitlements are supported.

---

## 81. Definition of Done

The `feature_entitlements.md` implementation SHALL be considered complete when:

* [ ] Centralized feature catalog exists
* [ ] Feature keys are immutable and unique
* [ ] Feature categories are supported
* [ ] Boolean entitlements work
* [ ] Quantity entitlements work
* [ ] Usage entitlements work
* [ ] Tiered entitlements work
* [ ] Plan-based entitlements work
* [ ] Tenant entitlements work
* [ ] User entitlements work
* [ ] AI-agent entitlements work
* [ ] Workflow entitlements work
* [ ] MCP entitlements work
* [ ] Integration entitlements work
* [ ] Channel entitlements work
* [ ] API entitlements work
* [ ] Add-ons work
* [ ] Trials work
* [ ] Temporary overrides work
* [ ] Expiration works
* [ ] Feature dependencies work
* [ ] Feature conflicts work
* [ ] RBAC integration works
* [ ] Plan Limits integration works
* [ ] Billing integration works
* [ ] Frontend feature gating works
* [ ] Backend feature enforcement works
* [ ] AI feature enforcement works
* [ ] Human feature enforcement works
* [ ] MCP enforcement works
* [ ] Workflow enforcement works
* [ ] Cache invalidation works
* [ ] Audit logging works
* [ ] Reconciliation works
* [ ] Observability works
* [ ] Security controls pass testing
* [ ] Tenant isolation passes testing
* [ ] Load testing passes
* [ ] Failure-mode testing passes
* [ ] Upgrade testing passes
* [ ] Downgrade testing passes
* [ ] Trial expiration testing passes
* [ ] Enterprise override testing passes
* [ ] End-to-end tests pass
* [ ] Production monitoring is enabled

---

## 82. Architectural Invariant

SalesGenie SHALL enforce the following invariant:

```text
A feature MAY be executed only when:

Authenticated
    AND
Tenant Valid
    AND
Subscription Eligible
    AND
Feature Entitled
    AND
Role Authorized
    AND
Actor Capability Authorized
    AND
Feature Dependencies Satisfied
    AND
Plan Limits Satisfied
    AND
Security Policy Allows
```

The platform MUST guarantee:

```text
AI cannot bypass feature entitlements.
Human users cannot bypass feature entitlements.
Frontend clients cannot bypass feature entitlements.
API clients cannot bypass feature entitlements.
Workflows cannot bypass feature entitlements.
MCP tools cannot bypass feature entitlements.
Integrations cannot bypass feature entitlements.
```

The Feature Entitlement Service SHALL remain the authoritative capability-access layer for the SalesGenie platform.
