# SalesGenie — Free Plan

## FAANG-Level User Requirements, System Requirements & Functional Requirements

### File: `free_plan.md`

---

## 1. Document Overview

## 1.1 Purpose

The `Free Plan` subsystem defines the complete behavior, eligibility, entitlements, quotas, restrictions, usage controls, AI capabilities, human capabilities, billing behavior, security controls, upgrade paths, and lifecycle management for SalesGenie's zero-cost subscription tier.

The Free Plan SHALL provide a meaningful product experience while protecting SalesGenie against:

- Resource abuse
- AI runaway consumption
- Trial/free-account farming
- API abuse
- Storage abuse
- Workflow abuse
- Spam
- Credential sharing
- Automated account creation
- Cross-tenant data access
- Subscription entitlement bypass
- Excessive infrastructure consumption

The Free Plan SHALL operate using the same entitlement architecture as paid plans.

---

## 2. Product Context

SalesGenie is an enterprise AI Customer Support and Sales Agent Platform supporting:

```text
Multi-Agent AI
RAG Knowledge Management
Omnichannel Customer Support
Lead Generation
Lead Intelligence
Workflow Automation
n8n Integration
MCP Integration
CRM Integrations
Email
WhatsApp
Slack
Salesforce
HubSpot
Zendesk
Jira
Notion
Google Drive
AI Voice
Document Intelligence
Analytics
Billing
Subscription Management
Usage-Based Billing
Human-in-the-Loop Operations
```

The Free Plan SHALL provide controlled access to selected platform capabilities.

---

## 3. Free Plan Design Principles

The Free Plan SHALL follow:

```text
Zero Subscription Cost
+
Explicit Entitlements
+
Hard Resource Boundaries
+
Server-Side Enforcement
+
Fair-Use Controls
+
AI Resource Governance
+
Human User Controls
+
Tenant Isolation
+
Abuse Prevention
+
Transparent Limits
+
Upgrade Path
+
Auditability
```

---

## 4. Primary Actors

## 4.1 Free User

A user operating under the Free Plan.

---

## 4.2 Free Organization Owner

The user responsible for the Free Plan organization.

---

## 4.3 Free Organization Admin

A user authorized to manage permitted organization-level settings.

---

## 4.4 Sales User

A human user performing sales-related activities.

---

## 4.5 Support User

A human user handling customer-support activities.

---

## 4.6 AI Agent

An AI agent operating within Free Plan resource limits.

---

## 4.7 AI Workflow

An automated AI workflow executing under Free Plan limits.

---

## 4.8 Super Admin

Platform administrator responsible for global Free Plan policies.

---

## 4.9 Billing Administrator

Authorized user responsible for subscription and upgrade operations.

---

## 5. Free Plan User Requirements

## UR-FREE-001 — Free Plan Availability

Users SHALL be able to register for the Free Plan without entering a paid subscription commitment.

---

## UR-FREE-002 — Free Plan Discovery

Users SHALL be able to identify the Free Plan before account activation.

The UI SHALL clearly communicate:

```text
Price
Included Features
Usage Limits
Excluded Features
AI Limits
Storage Limits
Upgrade Options
Fair-Use Policy
```

---

## UR-FREE-003 — Free Plan Activation

Eligible users SHALL receive Free Plan entitlements after successful account creation and verification.

---

## UR-FREE-004 — Free Plan Dashboard

Free users SHALL be able to view:

```text
Current Plan
Plan Status
Usage
Remaining Quotas
AI Usage
Workflow Usage
Storage Usage
Connected Integrations
Reset Date
Available Features
Upgrade Options
```

---

## UR-FREE-005 — Usage Transparency

The platform SHALL clearly show remaining Free Plan resources.

Example:

```text
AI Messages
75 / 100 used

Workflow Executions
18 / 25 used

Storage
350 MB / 500 MB used

Knowledge Documents
7 / 10 used
```

---

## UR-FREE-006 — Limit Visibility

Users SHALL be able to understand why an operation is unavailable.

Example:

```text
This feature is unavailable on your Free Plan.

Required:
Professional Plan

Reason:
Advanced multi-agent orchestration is not included in the Free Plan.
```

---

## UR-FREE-007 — Upgrade Path

Users SHALL be able to navigate from a restricted feature directly to eligible paid plans.

---

## UR-FREE-008 — Plan Comparison

Free users SHALL be able to compare their current capabilities with paid plans.

---

## 6. Human-Based Requirements

## HUMAN-UR-FREE-001 — Free Organization Management

The Free Plan organization owner SHALL be able to:

```text
View Organization
Manage Permitted Users
Manage Basic Profile
View Usage
Manage Basic Integrations
Manage Knowledge Base
Configure Basic AI Agent
View Billing Status
Upgrade Plan
```

---

## HUMAN-UR-FREE-002 — User Limit Enforcement

The system SHALL enforce the maximum number of human users allowed by the Free Plan.

---

## HUMAN-UR-FREE-003 — User Invitations

If invitations are supported, the Free Plan SHALL enforce the configured user quota.

---

## HUMAN-UR-FREE-004 — Human Activity Tracking

The platform SHALL track Free Plan human activity for:

```text
Security
Usage Accounting
Quota Enforcement
Audit
Abuse Detection
Analytics
```

---

## HUMAN-UR-FREE-005 — Human Approval

Where an AI operation exceeds Free Plan policies, authorized human users MAY approve an alternative action only when explicitly supported by policy.

Human approval SHALL NOT bypass hard subscription restrictions.

---

## 7. AI-Based Requirements

## AI-UR-FREE-001 — AI Entitlement Awareness

Every AI agent operating under the Free Plan SHALL be aware of the effective Free Plan entitlements.

---

## AI-UR-FREE-002 — AI Quota Enforcement

AI agents SHALL respect:

```text
Token Limits
Message Limits
Agent Execution Limits
Workflow Limits
Tool Call Limits
MCP Limits
Storage Limits
Document Processing Limits
Voice Limits
API Limits
```

---

## AI-UR-FREE-003 — AI Cannot Bypass Free Plan

AI agents SHALL NOT:

```text
Modify Subscription
Increase Quota
Grant Entitlements
Bypass Rate Limits
Disable Usage Tracking
Access Paid-Only Models
Access Restricted Integrations
```

without explicit authorization.

---

## AI-UR-FREE-004 — AI Plan Explanation

Users SHALL be able to ask:

```text
"What does my Free Plan include?"

"How much AI usage do I have left?"

"Why can't I use this model?"

"Why can't I create another workflow?"

"What plan supports this feature?"
```

The AI SHALL answer using authoritative subscription data.

---

## AI-UR-FREE-005 — AI Upgrade Recommendation

AI MAY recommend a paid plan when the user's requested operation is unavailable because of Free Plan restrictions.

---

## AI-UR-FREE-006 — AI Cost Awareness

Before expensive operations, AI SHOULD estimate resource consumption.

---

## AI-UR-FREE-007 — AI Runaway Protection

AI workflows SHALL support:

```text
Maximum Iterations
Maximum Runtime
Maximum Tool Calls
Maximum Token Budget
Maximum Concurrent Runs
Maximum Cost
```

---

## 8. Free Plan System Requirements

## SR-FREE-001 — Dedicated Plan Definition

The Free Plan SHALL be represented as a configurable subscription-tier definition.

Example:

```text
tier_code = FREE
tier_type = STANDARD
price = 0
currency = configured
billing_cycle = NONE
status = ACTIVE
```

---

## SR-FREE-002 — No Hardcoded Authorization

Free Plan permissions SHALL NOT be hardcoded exclusively into frontend components.

---

## SR-FREE-003 — Server-Side Enforcement

All Free Plan restrictions SHALL be enforced server-side.

---

## SR-FREE-004 — Entitlement Engine

The entitlement engine SHALL evaluate:

```text
Organization
User
Role
Subscription
Tier
Tier Version
Feature
Usage
Quota
Policy
```

---

## 9. Free Plan Lifecycle

The Free Plan SHALL support:

```text
AVAILABLE
ACTIVE
SUSPENDED
CANCELLED
UPGRADED
```

---

## FR-FREE-001 — Activation

A verified eligible account SHALL be able to activate the Free Plan.

---

## FR-FREE-002 — Suspension

The platform MAY suspend a Free Plan account because of:

```text
Abuse
Fraud
Security Violation
Terms Violation
Resource Abuse
Automated Account Farming
```

---

## FR-FREE-003 — Upgrade

A Free Plan SHALL transition to a paid subscription through the standard subscription workflow.

---

## FR-FREE-004 — Cancellation

Users MAY close their organization/account according to SalesGenie's account-deletion policy.

---

## 10. Free Plan Feature Entitlements

The Free Plan SHOULD use explicit feature flags.

Example:

```text
feature.ai_chat = true
feature.basic_ai_agent = true
feature.rag = true
feature.lead_management = true
feature.basic_lead_generation = true
feature.basic_workflows = true
feature.basic_analytics = true
feature.api_access = limited
feature.webhooks = limited
feature.mcp = limited
feature.n8n = limited
feature.voice_ai = false
feature.advanced_rag = false
feature.sso = false
feature.scim = false
feature.enterprise_security = false
```

Actual production values SHALL be configuration-driven.

---

## 11. Free Plan Resource Categories

The Free Plan SHALL support limits for:

```text
Human Users
AI Agents
AI Messages
AI Tokens
Workflow Executions
Workflow Steps
API Requests
MCP Tool Calls
Integrations
Knowledge Documents
Storage
RAG Queries
Lead Records
Lead Generation
Email Operations
Conversation Records
Voice Usage
Document Processing
Webhooks
```

---

## 12. Human User Limits

## FR-FREE-005

The Free Plan SHALL define a maximum number of human users.

Example configuration:

```text
max_users = configurable
```

The exact production limit SHALL be managed by the subscription configuration rather than application code.

---

## 13. AI Agent Limits

## FR-FREE-006

The Free Plan SHALL define a maximum number of AI agents.

Example:

```text
max_ai_agents = configurable
```

---

## FR-FREE-007

The platform SHALL distinguish between:

```text
Created Agents
Active Agents
Executing Agents
```

---

## 14. AI Message Limits

## FR-FREE-008

The Free Plan SHALL support a configurable monthly AI-message quota.

---

## FR-FREE-009

Every billable or quota-controlled AI interaction SHALL produce a usage event.

---

## 15. AI Token Limits

The Free Plan MAY enforce:

```text
Monthly Input Tokens
Monthly Output Tokens
Monthly Total Tokens
Per-Request Token Limit
```

---

## 16. AI Model Restrictions

Free Plan users SHALL receive access only to models explicitly included in the Free Plan.

Example:

```text
Free-Compatible Models
        ↓
Entitlement Check
        ↓
AI Gateway
        ↓
Model Execution
```

Premium-only models SHALL be rejected unless the user upgrades.

---

## 17. AI Model Fallback

Where policy permits:

```text
Premium Model Request
        ↓
Not Included
        ↓
Check Free-Compatible Fallback
        ↓
Use Allowed Model
```

The user SHALL be informed when model substitution materially affects the request.

---

## 18. AI Context Limits

Free Plan SHALL define configurable limits for:

```text
Maximum Context Window
Maximum Prompt Size
Maximum Output Size
Maximum RAG Context
Maximum Tool Context
```

---

## 19. AI Agent Tool Limits

The platform SHALL control AI tool access.

Example:

```text
Tool
Allowed?
Quota
Rate
Permission
```

---

## 20. MCP Limits

Free Plan MCP access SHALL support explicit restrictions such as:

```text
Maximum MCP Servers
Maximum MCP Tools
Maximum MCP Calls
Maximum MCP Execution Time
```

---

## 21. n8n Integration Limits

If n8n is available on the Free Plan, limits MAY include:

```text
Connected n8n Instances
Workflow Executions
Webhook Executions
Execution Frequency
AI Workflow Steps
```

---

## 22. Workflow Limits

## FR-FREE-010

Free Plan SHALL define:

```text
Maximum Active Workflows
Monthly Workflow Executions
Maximum Workflow Steps
Maximum Concurrent Executions
```

---

## 23. Workflow Scheduling

Scheduled workflows SHALL be limited according to Free Plan configuration.

---

## 24. Workflow Recursion Protection

The platform SHALL prevent unlimited recursive workflows.

Controls SHOULD include:

```text
Maximum Depth
Maximum Iterations
Maximum Runtime
Maximum Execution Count
```

---

## 25. RAG Limits

The Free Plan SHALL define:

```text
Knowledge Bases
Documents
Document Size
Total Storage
Embeddings
RAG Queries
Vector Storage
```

---

## 26. Knowledge Base Limits

Example:

```text
max_knowledge_bases = configurable
max_documents = configurable
max_document_size = configurable
max_storage = configurable
```

---

## 27. Lead Management Limits

Free Plan MAY include:

```text
Lead Records
Companies
Contacts
Lead Searches
Lead Enrichment
Lead Scoring
Lead Exports
```

---

## 28. Lead Generation Limits

Free users SHALL have a configurable monthly lead-generation quota.

---

## 29. Lead Intelligence Restrictions

Advanced enrichment sources or high-volume lead intelligence MAY be restricted to paid tiers.

---

## 30. CRM Integration Limits

The Free Plan MAY support a limited number of CRM connections.

Example:

```text
max_crm_integrations = configurable
```

---

## 31. Communication Integration Limits

Free Plan SHALL explicitly define supported communication channels.

Potential capabilities:

```text
Email
WhatsApp
Slack
Messenger
Instagram
```

Each SHALL have independent entitlement and quota configuration where required.

---

## 32. Gmail Restrictions

If Gmail is available:

```text
Maximum Connected Accounts
Email Operations
Daily Email Actions
AI Email Generation
Synchronization Frequency
```

SHALL be configurable.

---

## 33. WhatsApp Restrictions

If WhatsApp is available:

```text
Connected Numbers
Messages
Conversations
Webhook Events
Automation
```

SHALL be configurable.

---

## 34. Social Integration Restrictions

Facebook, Instagram, LinkedIn, YouTube, and TikTok access SHALL be independently configurable.

---

## 35. API Access

The Free Plan MAY provide limited API access.

Possible restrictions:

```text
Requests Per Minute
Requests Per Day
Monthly Requests
Concurrent Requests
Endpoint Access
API Keys
```

---

## 36. API Key Limits

The Free Plan SHALL support configurable:

```text
Maximum API Keys
Requests Per Minute
Requests Per Day
Key Expiration
Scopes
```

---

## 37. Webhook Limits

The Free Plan MAY support:

```text
Inbound Webhooks
Outbound Webhooks
Webhook Events
Webhook Delivery Rate
Webhook Retry Count
```

---

## 38. Storage Limits

The Free Plan SHALL enforce storage limits across:

```text
Documents
Attachments
Knowledge Bases
Conversation Files
Generated Files
Vector Data
```

---

## 39. File Upload Limits

The platform SHALL enforce:

```text
Maximum File Size
Maximum Total Storage
Allowed File Types
Maximum Files
Upload Rate
```

---

## 40. Document Intelligence

If document processing is enabled, the Free Plan SHALL define:

```text
Pages Per Month
Documents Per Month
Maximum File Size
Processing Models
OCR Usage
Extraction Operations
```

---

## 41. Voice AI

Voice AI MAY be:

```text
Disabled
Limited
Metered
```

according to Free Plan configuration.

If enabled:

```text
Voice Minutes
Concurrent Calls
Calls Per Day
AI Voice Models
```

SHALL be controlled.

---

## 42. Conversation Limits

The Free Plan SHALL support configurable limits for:

```text
Active Conversations
Stored Conversations
Monthly Conversations
Concurrent Conversations
```

---

## 43. Analytics

Free Plan SHALL provide basic analytics where configured.

Potential analytics:

```text
Lead Count
Conversation Count
AI Usage
Workflow Usage
Basic Sales Metrics
Basic Support Metrics
```

Advanced analytics MAY be paid-only.

---

## 44. Dashboard Requirements

The Free Plan dashboard SHALL display:

```text
Plan
Usage
Quota
Remaining Capacity
Reset Date
Feature Availability
Upgrade CTA
```

---

## 45. Quota Warning System

The platform SHALL support configurable warning thresholds.

Recommended:

```text
50%
75%
80%
90%
95%
100%
```

---

## 46. Quota Exhaustion Policies

Each resource SHALL have an explicit exhaustion policy.

Supported policies:

```text
BLOCK
SOFT_LIMIT
QUEUE
DEGRADE
ALLOW_OVERAGE
REQUEST_UPGRADE
```

The Free Plan SHOULD default to:

```text
BLOCK
```

for resources that would otherwise create unbounded infrastructure cost.

---

## 47. AI Quota Exhaustion

When Free AI quota is exhausted:

```text
AI Request
    ↓
Quota Check
    ↓
Quota Exhausted
    ↓
Reject / Upgrade
```

The user SHALL receive a clear explanation.

---

## 48. AI Degradation

Where configured, Free Plan AI requests MAY fall back to a lower-cost model.

---

## 49. Rate Limiting

Free Plan users SHALL be subject to rate limits.

Rate limits MAY apply to:

```text
Login
API
AI Requests
Workflow Creation
Workflow Execution
File Upload
Lead Search
Lead Generation
Integration Calls
Webhooks
MCP Calls
```

---

## 50. Distributed Rate Limiting

Rate limiting SHALL operate correctly across multiple SalesGenie service instances.

Recommended technologies MAY include:

```text
Redis
Distributed Counters
Token Bucket
Leaky Bucket
Sliding Window
```

---

## 51. Fair-Use Protection

The Free Plan SHALL implement fair-use controls to prevent a small number of users from consuming disproportionate shared resources.

---

## 52. Abuse Detection

The platform SHOULD detect:

```text
Rapid Account Creation
Repeated Trial/Free Registration
High-Frequency API Calls
Automated AI Requests
Workflow Loops
Mass Lead Generation
Credential Sharing
Bot Activity
Resource Exhaustion Patterns
```

---

## 53. Free Account Farming

The system SHOULD detect suspicious patterns associated with creation of large numbers of Free Plan accounts.

---

## 54. Account Verification

SalesGenie MAY require:

```text
Email Verification
Phone Verification
Organization Verification
CAPTCHA
Risk-Based Verification
```

based on risk policy.

---

## 55. Tenant Isolation

Free Plan organizations SHALL be completely isolated from other organizations.

A Free Plan user SHALL never access another tenant's:

```text
Users
Leads
Contacts
Conversations
Documents
Knowledge Bases
AI Agents
Workflows
Integrations
Billing Information
Usage
API Keys
```

---

## 56. Authorization

Free Plan access SHALL be evaluated using:

```text
Identity
+
Tenant
+
Role
+
Subscription
+
Entitlement
+
Quota
+
Policy
```

---

## 57. Frontend Security

The frontend SHALL never be the authoritative source for Free Plan restrictions.

For example:

```text
Disabled Button
```

is insufficient protection.

The backend SHALL independently reject unauthorized operations.

---

## 58. API Security

API requests SHALL validate:

```text
Authentication
Authorization
Tenant
Subscription
Feature Entitlement
Quota
Rate Limit
Request Schema
```

---

## 59. Free Plan Upgrade Workflow

```text
Free User
    ↓
Select Paid Plan
    ↓
Eligibility Check
    ↓
Price Calculation
    ↓
Payment
    ↓
Payment Verification
    ↓
Subscription Activation
    ↓
Entitlement Update
    ↓
Quota Update
    ↓
Audit
    ↓
Notification
```

---

## 60. Upgrade Without Data Loss

Upgrading from Free to paid plans SHALL preserve compatible:

```text
Users
Leads
Contacts
Conversations
Knowledge Bases
Documents
Workflows
AI Agents
Integrations
Analytics
```

unless explicitly excluded by migration policy.

---

## 61. Free-to-Paid Migration

The system SHALL support deterministic entitlement migration.

Example:

```text
FREE v1
   ↓
PROFESSIONAL v3
   ↓
Apply New Entitlements
   ↓
Increase Limits
   ↓
Enable New Features
   ↓
Retain Existing Data
```

---

## 62. Paid-to-Free Downgrade

If a paid user downgrades to Free, the system SHALL identify incompatible resources.

Example:

```text
25 Users
      ↓
Free Limit = 3
      ↓
Downgrade Validation
      ↓
User Must Resolve Excess Resources
```

The platform SHALL NOT silently delete customer data.

---

## 63. Grace Period for Downgrade

Where supported, the system MAY provide a grace period for resolving resources that exceed Free Plan limits.

---

## 64. Data Retention

Free Plan SHALL have explicit data-retention policies.

The policy SHALL define:

```text
Conversation Retention
Document Retention
Deleted Data Retention
Audit Retention
Usage Retention
Inactive Account Retention
```

---

## 65. Inactive Account Policy

The platform MAY suspend or archive inactive Free accounts according to published policy.

---

## 66. Free Plan Billing Requirements

The Free Plan SHALL have:

```text
Base Price = 0
```

unless the plan configuration explicitly changes.

---

## 67. Payment Requirement

The Free Plan SHOULD NOT require payment unless required for:

```text
Fraud Prevention
Verification
Paid Add-On
Metered Overage
```

---

## 68. Free Plan Add-Ons

The platform MAY support paid add-ons while retaining the Free Plan.

Example:

```text
FREE PLAN
+
Additional AI Credits
+
Additional Storage
```

Any paid add-on SHALL use the standard billing architecture.

---

## 69. Overage Policy

The Free Plan SHALL explicitly define whether overages are:

```text
Disabled
Blocked
Metered
Allowed Only With Opt-In
```

The default SHOULD be:

```text
No Automatic Paid Overage
```

to prevent unexpected charges.

---

## 70. Subscription Entitlement Object

A Free Plan entitlement object SHOULD include:

```text
{
  "tier": "FREE",
  "version": "v1",
  "status": "ACTIVE",
  "features": {},
  "quotas": {},
  "limits": {},
  "credits": {},
  "expires_at": null
}
```

---

## 71. Entitlement Evaluation

The authoritative evaluation flow SHALL be:

```text
Request
    ↓
Authenticate
    ↓
Resolve Tenant
    ↓
Resolve Subscription
    ↓
Resolve Free Plan Version
    ↓
Resolve Entitlement
    ↓
Check Usage
    ↓
Check Quota
    ↓
Check Rate Limit
    ↓
Check Policy
    ↓
ALLOW / DENY / DEGRADE / QUEUE
```

---

## 72. Usage Reservation

For expensive operations:

```text
Check Quota
    ↓
Reserve Resource
    ↓
Execute
    ↓
Commit Usage
```

Failed operations SHALL release or reconcile reservations.

---

## 73. Race Condition Protection

The Free Plan SHALL prevent concurrent requests from exceeding quotas through atomic accounting.

Possible mechanisms:

```text
Atomic Redis Counters
Database Transactions
Optimistic Locking
Distributed Locks
Usage Reservations
```

---

## 74. Usage Events

The platform SHALL generate usage events such as:

```text
ai.message.used
ai.token.used
ai.agent.executed
workflow.executed
workflow.step.executed
api.request.used
mcp.tool.used
document.processed
storage.used
lead.generated
lead.enriched
voice.minute.used
```

---

## 75. Usage Event Schema

Each event SHOULD contain:

```text
Event ID
Tenant ID
User ID
Resource Type
Resource ID
Quantity
Timestamp
Subscription ID
Tier Version
Correlation ID
Source
```

---

## 76. Idempotency

Usage events SHALL support idempotent processing.

Duplicate usage events SHALL NOT double-consume quota.

---

## 77. Usage Reconciliation

The platform SHALL periodically reconcile:

```text
Recorded Usage
Quota Counters
Workflow Executions
AI Gateway Usage
Storage Usage
Billing Usage
```

---

## 78. Reset Policy

Free Plan recurring quotas SHALL support configurable reset schedules.

Typical model:

```text
Billing/Usage Period
        ↓
Quota Reset
        ↓
New Allocation
```

---

## 79. Reset Safety

Quota resets SHALL be atomic and SHALL NOT erase historical usage records.

---

## 80. AI Budget Architecture

Free AI resources SHALL follow:

```text
Organization Free AI Budget
        │
        ├── Human AI Usage
        ├── AI Agent Usage
        ├── Workflow AI Usage
        └── API AI Usage
```

---

## 81. AI Agent Budget

Each Free AI agent MAY have:

```text
Daily Token Limit
Monthly Token Limit
Maximum Runtime
Maximum Tool Calls
Maximum Cost
```

---

## 82. Human + AI Shared Resource Protection

The platform SHALL prevent AI automation from consuming the entire organization's shared Free Plan quota without appropriate controls.

---

## 83. AI Human Approval

If configured:

```text
AI Agent
   ↓
Quota Threshold
   ↓
Approval Required
   ↓
Human Review
   ↓
Approve / Reject
```

Approval SHALL not permit operations prohibited by hard platform policies.

---

## 84. Free Plan Notifications

The system SHALL support:

```text
Welcome
Plan Activated
Usage 50%
Usage 75%
Usage 90%
Usage 95%
Quota Exhausted
Feature Restricted
Upgrade Available
Security Warning
Account Suspended
```

---

## 85. Notification Channels

Notifications MAY be delivered through:

```text
In-App
Email
Slack
Microsoft Teams
Webhook
```

depending on available Free Plan integrations.

---

## 86. Free Plan Audit Logging

The system SHALL audit security-sensitive and administrative actions.

Events SHOULD include:

```text
Free Plan Activated
Free Plan Suspended
Free Plan Upgraded
Entitlement Evaluated
Quota Exhausted
Quota Reset
Admin Override
AI Budget Exceeded
API Limit Exceeded
Security Violation
```

---

## 87. AI Auditability

AI actions consuming Free Plan resources SHALL be traceable.

Each execution SHOULD provide:

```text
Agent ID
Workflow ID
Model
Usage
Tokens
Tools
MCP Calls
Duration
Result
Cost Estimate
```

---

## 88. Administrative Override

Super Admins MAY grant temporary Free Plan overrides when authorized.

Example:

```text
Organization
+
Temporary AI Credits
+
Expiration
+
Reason
+
Approver
```

---

## 89. Override Security

Overrides SHALL:

```text
Require Authorization
Be Time-Bounded
Be Audited
Be Tenant-Scoped
Be Revocable
```

---

## 90. Free Plan Analytics

Platform administrators SHALL be able to measure:

```text
Free Accounts
Active Free Accounts
Free-to-Paid Conversion
Free Plan Churn
Average AI Usage
Average Workflow Usage
Quota Exhaustion
Feature Adoption
Upgrade Triggers
Abuse Rate
Infrastructure Cost
Cost Per Free User
```

---

## 91. AI Analytics

AI MAY analyze Free Plan behavior to identify:

```text
Upgrade Opportunities
Feature Demand
Quota Bottlenecks
Potential Abuse
Resource Inefficiency
Plan Optimization Opportunities
```

AI recommendations SHALL not directly change pricing or entitlements.

---

## 92. Free-to-Paid Conversion Analytics

The platform SHOULD track:

```text
Free Activation
First Value Event
Feature Adoption
Quota Warning
Upgrade Prompt
Upgrade Attempt
Successful Upgrade
Time To Upgrade
```

---

## 93. Product-Led Growth

The Free Plan SHOULD support product-led growth through:

```text
In-Product Education
Feature Discovery
Usage Visibility
Contextual Upgrade Prompts
Plan Comparison
AI-Assisted Recommendations
```

Upgrade prompts SHALL not become abusive or block basic Free Plan usage unnecessarily.

---

## 94. Upgrade Trigger Engine

The system MAY trigger an upgrade recommendation when:

```text
Quota > 80%
Repeated Feature Restriction
Team Size Approaches Limit
AI Usage Increases
Workflow Usage Increases
Integration Limit Reached
Storage Limit Approaches
```

---

## 95. AI-Powered Upgrade Recommendation

AI MAY calculate:

```text
Current Usage
Projected Usage
Current Limit
Required Capacity
Recommended Tier
Estimated Additional Cost
Expected Feature Benefits
```

The AI SHALL clearly distinguish estimates from authoritative billing information.

---

## 96. No Unauthorized Purchase

AI SHALL NOT automatically upgrade a Free Plan unless explicit automated-purchase authorization has been configured by the customer.

---

## 97. Observability

Free Plan services SHALL expose metrics including:

```text
free_plan_active_accounts
free_plan_activation_rate
free_plan_upgrade_rate
free_plan_quota_exhaustion_rate
free_plan_ai_usage
free_plan_workflow_usage
free_plan_api_usage
free_plan_storage_usage
free_plan_abuse_events
free_plan_entitlement_latency
```

---

## 98. Service-Level Monitoring

Monitor:

```text
Entitlement Service
Subscription Service
Usage Service
AI Gateway
Workflow Engine
Billing Service
Authentication
Authorization
Redis
Database
Event Bus
```

---

## 99. Performance Requirements

Free Plan entitlement checks SHOULD target:

```text
P95 < 50 ms
P99 < 150 ms
```

under normal production conditions.

---

## 100. Scalability

The Free Plan architecture SHALL support large-scale user acquisition without requiring a separate architecture from paid plans.

The system SHALL support:

```text
Millions of Free Accounts
High Concurrent AI Requests
High Usage Event Volume
Large Multi-Tenant Data Sets
```

---

## 101. Availability

Free Plan entitlement and quota enforcement services SHOULD meet the platform's production availability objectives.

---

## 102. Failure Handling

If the usage service becomes unavailable:

```text
Security-Critical Decision
→ Fail Closed

Safe Cached Entitlement Read
→ Short TTL Cache

Usage Accounting Failure
→ Reserve / Queue / Reject
```

The system SHALL never silently allow unlimited usage because a quota service is unavailable.

---

## 103. Cache Requirements

Free Plan entitlements MAY be cached.

Cache SHALL include:

```text
Tenant ID
Subscription ID
Tier Version
Entitlements
Timestamp
TTL
```

---

## 104. Cache Invalidation

When Free Plan state changes:

```text
Subscription Changed
      ↓
Event Published
      ↓
Entitlement Cache Invalidated
      ↓
Services Refresh
```

---

## 105. Event-Driven Architecture

The Free Plan SHALL support events such as:

```text
free_plan.activated
free_plan.suspended
free_plan.upgraded
free_plan.cancelled

free_plan.quota.warning
free_plan.quota.exhausted
free_plan.quota.reset

free_plan.entitlement.updated
free_plan.usage.recorded
free_plan.abuse.detected
```

---

## 106. Event Ordering

Subscription and entitlement events SHALL include:

```text
Event ID
Sequence Number
Timestamp
Correlation ID
Tenant ID
```

to support reliable ordering and reconciliation.

---

## 107. Event Idempotency

All Free Plan lifecycle consumers SHALL process duplicate events safely.

---

## 108. Security Requirements

The Free Plan SHALL implement:

```text
Zero Trust
Least Privilege
RBAC
ABAC
MFA Where Applicable
Tenant Isolation
Rate Limiting
Audit Logging
Secure API Keys
Input Validation
Output Validation
Abuse Detection
```

---

## 109. API Key Security

Free Plan API keys SHALL:

```text
Use Scoped Permissions
Support Rotation
Support Revocation
Never Be Stored Plaintext
Never Appear in Logs
```

---

## 110. Secret Management

OAuth tokens, API keys, integration credentials, and other secrets SHALL be stored using secure secret-management mechanisms.

---

## 111. Data Privacy

Free Plan data SHALL follow the same core privacy and tenant-isolation principles as paid customers.

Free status SHALL NOT reduce fundamental data-security guarantees.

---

## 112. Free Plan API Error Contract

When a Free Plan restriction occurs, APIs SHOULD return structured errors.

Example:

```json
{
  "code": "FREE_PLAN_LIMIT_EXCEEDED",
  "resource": "ai_messages",
  "limit": 100,
  "usage": 100,
  "remaining": 0,
  "reset_at": "2026-09-01T00:00:00Z",
  "upgrade_available": true
}
```

---

## 113. Feature Restriction Error

Example:

```json
{
  "code": "FEATURE_NOT_INCLUDED",
  "feature": "advanced_voice_ai",
  "current_plan": "FREE",
  "required_plan": "PROFESSIONAL",
  "upgrade_available": true
}
```

---

## 114. Database Requirements

Core entities SHALL include:

```text
Subscription
SubscriptionTier
SubscriptionTierVersion
SubscriptionEntitlement
SubscriptionQuota
SubscriptionUsage
SubscriptionOverride
UsageEvent
Feature
Organization
User
AI Agent
Workflow
```

---

## 115. Data Integrity

The system SHALL enforce:

```text
One Active Subscription Per Billing Account
Valid Tier Reference
Valid Tier Version
Valid Organization
Valid Entitlements
Valid Usage Counters
Valid Quota Definitions
```

---

## 116. Versioning

Free Plan definitions SHALL be versioned.

Example:

```text
FREE v1
FREE v2
FREE v3
```

---

## 117. Historical Consistency

Historical usage and subscription records SHALL retain the applicable Free Plan version.

---

## 118. Free Plan Changes

When administrators modify Free Plan limits:

```text
Draft
→ Review
→ Schedule
→ Publish
→ Effective
```

where policy requires controlled deployment.

---

## 119. Backward Compatibility

Changes to the Free Plan SHALL NOT unexpectedly invalidate active user data.

---

## 120. Migration

When Free Plan limits are reduced:

```text
Detect Affected Accounts
        ↓
Notify Users
        ↓
Provide Grace Period
        ↓
Restrict New Resource Creation
        ↓
Preserve Existing Data
        ↓
Apply New Limits
```

---

## 121. Free Plan Resource State

For each quota-controlled resource, the platform SHALL maintain:

```text
Limit
Used
Remaining
Reserved
Reset At
Policy
```

---

## 122. Resource Calculation

The effective remaining capacity SHALL be calculated as:

```text
Remaining
=
Limit
-
Committed Usage
-
Reserved Usage
```

with appropriate handling for unlimited or non-metered resources.

---

## 123. Unlimited Resource Handling

The system SHALL NOT represent unlimited resources using arbitrary large integer values.

Use an explicit representation such as:

```text
unlimited = true
```

---

## 124. Zero-Quota Features

The platform SHALL support:

```text
enabled = false
limit = 0
```

for features excluded from Free Plan.

---

## 125. Entitlement Precedence

Effective entitlements SHALL follow a deterministic precedence model.

Recommended:

```text
Platform Policy
      ↓
Enterprise Contract
      ↓
Subscription Tier
      ↓
Subscription Add-On
      ↓
Approved Override
      ↓
Temporary Policy
```

Higher-level security policies SHALL always be able to restrict access.

---

## 126. AI Entitlement Precedence

AI access SHALL follow:

```text
Platform Security Policy
      ↓
Tenant Policy
      ↓
Subscription Entitlement
      ↓
AI Agent Policy
      ↓
User Permission
      ↓
Request
```

---

## 127. Human Entitlement Precedence

Human access SHALL follow:

```text
Platform Policy
      ↓
Tenant Policy
      ↓
Subscription
      ↓
Role
      ↓
Permission
      ↓
Resource
```

---

## 128. Testing Requirements

## Unit Tests

The system SHALL test:

```text
Free Plan Activation
Entitlement Evaluation
Quota Evaluation
Quota Reset
AI Limits
Workflow Limits
API Limits
Storage Limits
Feature Restrictions
Upgrade
Suspension
Overrides
```

---

## 129. Integration Tests

The system SHALL test Free Plan interaction with:

```text
Authentication
Authorization
AI Gateway
Usage Tracking
Billing
Pricing Engine
Payment Gateway
Invoice Service
Credit Management
Workflow Engine
MCP
n8n
CRM Integrations
Communication Integrations
Notification Service
Analytics
Audit Service
```

---

## 130. Security Testing

Security tests SHALL include:

```text
Free Plan Bypass
Frontend Bypass
API Parameter Tampering
Plan ID Tampering
Quota Manipulation
Tenant Isolation
Privilege Escalation
AI Authorization Bypass
API Key Abuse
Concurrent Quota Abuse
```

---

## 131. Load Testing

Load tests SHALL simulate:

```text
Large Free User Population
Mass AI Requests
Mass Workflow Execution
High-Frequency Quota Checks
High-Frequency Usage Events
Mass Account Registration
```

---

## 132. Chaos Testing

Chaos scenarios SHOULD include:

```text
Redis Failure
Database Failure
Usage Service Failure
Event Bus Failure
AI Gateway Failure
Billing Failure
Duplicate Usage Events
Out-of-Order Events
Network Partition
Service Restart
```

---

## 133. Acceptance Criteria

The Free Plan SHALL be considered production-ready when:

* [ ] Free Plan is represented as a versioned subscription tier.
* [ ] Free Plan has explicit feature entitlements.
* [ ] Free Plan has explicit usage quotas.
* [ ] Free Plan has explicit resource limits.
* [ ] Free Plan is enforced server-side.
* [ ] Frontend cannot bypass Free Plan restrictions.
* [ ] AI cannot bypass Free Plan restrictions.
* [ ] Human users are subject to configured limits.
* [ ] AI agents are subject to configured limits.
* [ ] AI model access is entitlement-controlled.
* [ ] Workflow execution is quota-controlled.
* [ ] MCP usage is quota-controlled where enabled.
* [ ] n8n usage is quota-controlled where enabled.
* [ ] API usage is rate-limited.
* [ ] Storage is quota-controlled.
* [ ] RAG usage is quota-controlled.
* [ ] Lead-generation usage is quota-controlled.
* [ ] Integration limits are enforced.
* [ ] Usage events are recorded.
* [ ] Usage events are idempotent.
* [ ] Quotas cannot be exceeded through race conditions.
* [ ] Quota resets are atomic.
* [ ] Usage reconciliation exists.
* [ ] Free-to-paid upgrade works.
* [ ] Upgrade preserves compatible data.
* [ ] Paid-to-Free downgrade handles excess resources safely.
* [ ] No unexpected paid overage occurs.
* [ ] Free Plan abuse detection exists.
* [ ] Tenant isolation is enforced.
* [ ] Security-sensitive actions are audited.
* [ ] AI actions are traceable.
* [ ] Administrative overrides are controlled.
* [ ] Entitlements are cacheable with safe invalidation.
* [ ] Subscription events are idempotent.
* [ ] Usage analytics are available.
* [ ] Free-to-paid conversion analytics are available.
* [ ] AI upgrade recommendations are safe.
* [ ] Performance targets are met.
* [ ] Load tests pass.
* [ ] Security tests pass.
* [ ] Chaos tests pass.

---

## 134. FAANG-Level Free Plan Architecture

```text
                         SALES GENIE
                              │
                              ▼
                    Subscription Service
                              │
                              ▼
                         FREE PLAN
                              │
              ┌───────────────┼────────────────┐
              │               │                │
              ▼               ▼                ▼
        Entitlements       Quotas           Limits
              │               │                │
              └───────────────┼────────────────┘
                              ▼
                       Policy Engine
                              │
                ┌─────────────┼─────────────┐
                │             │             │
                ▼             ▼             ▼
             HUMAN          AI AGENT      WORKFLOW
                │             │             │
                └─────────────┼─────────────┘
                              ▼
                       Usage Tracking
                              │
         ┌────────────────────┼────────────────────┐
         │                    │                    │
         ▼                    ▼                    ▼
      AI Usage          Workflow Usage        API Usage
         │                    │                    │
         └────────────────────┼────────────────────┘
                              ▼
                       Quota Enforcement
                              │
               ┌──────────────┼──────────────┐
               │              │              │
               ▼              ▼              ▼
             ALLOW          DEGRADE         DENY
               │              │              │
               └──────────────┼──────────────┘
                              ▼
                           Audit
                              │
                              ▼
                         Analytics
                              │
                              ▼
                         Upgrade CTA
                              │
                              ▼
                       Paid Subscription
```

---

## 135. Human + AI Free Plan Governance

```text
                      FREE PLAN GOVERNANCE
                               │
             ┌─────────────────┴─────────────────┐
             │                                   │
             ▼                                   ▼
        HUMAN CONTROL                       AI CONTROL
             │                                   │
      User Management                       AI Agents
      Configuration                         AI Workflows
      Approvals                             Tool Usage
      Upgrade                              Model Selection
      Security                              Resource Budget
             │                                   │
             └─────────────────┬─────────────────┘
                               ▼
                         POLICY ENGINE
                               │
                               ▼
                       ENTITLEMENT ENGINE
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
           FEATURE           QUOTA            RATE
           CHECK             CHECK            CHECK
              │                │                │
              └────────────────┼────────────────┘
                               ▼
                        EXECUTION DECISION
                               │
                  ┌────────────┼────────────┐
                  ▼            ▼            ▼
                ALLOW        DEGRADE       DENY
```

---

## 136. Free Plan Security Boundary

```text
                       UNTRUSTED REQUEST
                              │
                              ▼
                        Authentication
                              │
                              ▼
                        Tenant Resolution
                              │
                              ▼
                         RBAC / ABAC
                              │
                              ▼
                     Subscription Resolution
                              │
                              ▼
                     FREE PLAN ENTITLEMENTS
                              │
                              ▼
                        Quota Validation
                              │
                              ▼
                       Rate Limit Check
                              │
                              ▼
                         Risk Policy
                              │
                              ▼
                    ┌─────────┴─────────┐
                    │                   │
                    ▼                   ▼
                  ALLOW                DENY
                    │                   │
                    ▼                   ▼
               Execute              Explain
                    │
                    ▼
              Record Usage
                    │
                    ▼
                  Audit
```

---

## 137. Free Plan AI Execution Boundary

```text
AI REQUEST
    │
    ▼
User Authentication
    │
    ▼
Tenant Resolution
    │
    ▼
Free Subscription Check
    │
    ▼
AI Agent Permission
    │
    ▼
Model Entitlement
    │
    ▼
Token Budget
    │
    ▼
Tool Permission
    │
    ▼
MCP Permission
    │
    ▼
Workflow Permission
    │
    ▼
Rate Limit
    │
    ▼
Risk Policy
    │
    ▼
Reserve Usage
    │
    ▼
AI Gateway
    │
    ▼
Execute
    │
    ▼
Commit Usage
    │
    ▼
Audit
```

---

## 138. Free Plan Business Model

The Free Plan SHALL be designed around:

```text
LOW BARRIER TO ENTRY
        +
CONTROLLED RESOURCE CONSUMPTION
        +
PRODUCT VALUE
        +
PRODUCT-LED GROWTH
        +
TRANSPARENT LIMITS
        +
SAFE AI USAGE
        +
CLEAR UPGRADE PATH
```

---

## 139. Ultimate Free Plan Requirement

The SalesGenie Free Plan SHALL provide a genuinely useful entry-level AI sales and customer-support experience while maintaining strict infrastructure, AI, security, and abuse boundaries.

Every Free Plan operation SHALL ultimately be governed by:

```text
Identity
+
Tenant
+
Role
+
Subscription
+
Tier Version
+
Feature Entitlement
+
Usage
+
Quota
+
Rate Limit
+
AI Policy
+
Security Policy
=
Execution Decision
```

The final decision SHALL be one of:

```text
ALLOW
DENY
DEGRADE
QUEUE
REQUEST_APPROVAL
REQUEST_UPGRADE
```

The Free Plan SHALL never depend on frontend controls or AI instructions as its primary security boundary.

The authoritative architecture SHALL remain:

```text
Free Plan
    ↓
Versioned Entitlements
    ↓
Policy Engine
    ↓
Quota Engine
    ↓
Usage Tracking
    ↓
AI / Human / Workflow Execution
    ↓
Audit + Analytics
    ↓
Upgrade Path
```

This design SHALL allow SalesGenie to acquire large numbers of Free users while preserving:

```text
Security
+
Tenant Isolation
+
AI Governance
+
Resource Predictability
+
Billing Integrity
+
Scalability
+
Observability
+
Reliability
+
Product-Led Growth
```
