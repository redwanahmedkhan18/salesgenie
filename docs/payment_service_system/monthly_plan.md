# SalesGenie — Monthly Plan

## FAANG-Level User Requirements, System Requirements & Functional Requirements

### File: `monthly_plan.md`

---

## 1. Document Overview

## 1.1 Purpose

The `Monthly Plan` subsystem defines the complete product, subscription, entitlement, quota, billing, usage, AI, human-user, lifecycle, security, and operational requirements for SalesGenie's monthly subscription offering.

The Monthly Plan SHALL support a production-grade SaaS subscription model where customers are billed on a recurring monthly basis while maintaining:

- Deterministic subscription state
- Versioned pricing
- Versioned entitlements
- Accurate usage tracking
- AI resource governance
- Human-user governance
- Multi-tenant isolation
- Payment reliability
- Invoice generation
- Tax handling
- Discounts and coupons
- Credits
- Refunds
- Subscription lifecycle management
- Upgrade/downgrade handling
- Grace periods
- Dunning
- Proration
- Auditability
- Observability
- High-scale operation

---

## 2. Product Context

SalesGenie is an enterprise AI Customer Support and Sales Agent Platform supporting:

```text
Multi-Agent AI
RAG Knowledge Management
AI Customer Support
AI Sales Agents
Lead Generation
Lead Intelligence
Workflow Automation
n8n Integration
MCP Integration
Omnichannel Communication
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

The Monthly Plan SHALL integrate with the broader SalesGenie billing architecture.

---

## 3. Core Design Principles

The Monthly Plan SHALL follow:

```text
Subscription
    +
Pricing
    +
Entitlements
    +
Usage
    +
Payment
    +
Invoice
    +
Tax
    +
Credits
    +
Discounts
    +
Renewal
    +
Dunning
    +
Audit
```

The system SHALL maintain a strict separation between:

```text
Pricing
Entitlement
Usage
Billing
Payment
Accounting
```

---

## 4. Primary Actors

## 4.1 Monthly Subscriber

A customer organization subscribed to a monthly SalesGenie plan.

---

## 4.2 Organization Owner

The owner responsible for the organization's subscription.

---

## 4.3 Billing Administrator

The authorized human responsible for:

```text
Subscription
Payment Method
Invoices
Coupons
Credits
Billing Contacts
Plan Changes
```

---

## 4.4 Organization Admin

A human administrator managing users, agents, workflows, and organization settings.

---

## 4.5 Sales User

A human sales representative using SalesGenie.

---

## 4.6 Support User

A human customer-support representative.

---

## 4.7 AI Agent

An autonomous or semi-autonomous SalesGenie AI agent operating within the Monthly Plan.

---

## 4.8 AI Workflow

An AI-driven workflow consuming Monthly Plan resources.

---

## 4.9 Super Admin

A SalesGenie platform administrator.

---

## 4.10 Billing Service

The service responsible for subscription, invoice, usage, and billing-state operations.

---

## 4.11 Payment Gateway

The external payment provider responsible for payment authorization, capture, refund, and payment-method operations.

---

## 5. Monthly Plan User Requirements

## UR-MONTHLY-001 — Plan Discovery

Users SHALL be able to view the Monthly Plan before subscribing.

The plan page SHALL clearly communicate:

```text
Monthly Price
Currency
Included Features
AI Capabilities
Human User Limits
Usage Limits
Included Credits
Integration Limits
Storage Limits
Workflow Limits
Overage Policy
Renewal Policy
Cancellation Policy
Refund Policy
Upgrade Options
Downgrade Options
```

---

## UR-MONTHLY-002 — Monthly Pricing Transparency

The user SHALL see the effective recurring monthly price before checkout.

---

## UR-MONTHLY-003 — Subscription Creation

Eligible users SHALL be able to subscribe to the Monthly Plan through SalesGenie's standard checkout flow.

---

## UR-MONTHLY-004 — Payment Confirmation

Users SHALL receive confirmation when monthly subscription payment succeeds.

---

## UR-MONTHLY-005 — Subscription Status

Users SHALL be able to view:

```text
Active
Pending
Past Due
Grace Period
Suspended
Cancelled
Expired
```

---

## UR-MONTHLY-006 — Renewal Visibility

Users SHALL be able to see:

```text
Next Billing Date
Next Invoice Date
Current Monthly Price
Expected Recurring Amount
Applicable Discounts
Applicable Taxes
```

---

## UR-MONTHLY-007 — Billing History

Billing administrators SHALL be able to access:

```text
Invoices
Payments
Refunds
Credits
Discounts
Subscription Changes
```

---

## UR-MONTHLY-008 — Payment Method Management

Authorized users SHALL be able to:

```text
Add Payment Method
Replace Payment Method
Remove Payment Method
Set Default Payment Method
```

subject to payment-provider and billing-policy constraints.

---

## 6. Human-Based Requirements

## HUMAN-UR-MONTHLY-001 — Human User Provisioning

The Monthly Plan SHALL support organization-level human-user provisioning.

The system SHALL enforce the configured maximum:

```text
max_human_users
```

---

## HUMAN-UR-MONTHLY-002 — User Invitations

Authorized administrators SHALL be able to invite users until the plan's user limit is reached.

---

## HUMAN-UR-MONTHLY-003 — Role Assignment

Authorized administrators SHALL be able to assign supported roles such as:

```text
Organization Owner
Admin
Sales Manager
Sales Agent
Support Manager
Support Agent
Analyst
Viewer
```

subject to plan and RBAC policy.

---

## HUMAN-UR-MONTHLY-004 — User Removal

Administrators SHALL be able to deactivate or remove users according to organizational policy.

---

## HUMAN-UR-MONTHLY-005 — User Limit Protection

The system SHALL reject creation or invitation of users beyond the Monthly Plan entitlement.

---

## HUMAN-UR-MONTHLY-006 — Human Usage Visibility

Human users SHALL be able to view usage relevant to their permissions.

---

## HUMAN-UR-MONTHLY-007 — Human Approval

The Monthly Plan MAY require human approval for high-risk or high-cost AI operations.

---

## 7. AI-Based Requirements

## AI-UR-MONTHLY-001 — AI Plan Awareness

AI agents SHALL operate using authoritative Monthly Plan entitlements.

---

## AI-UR-MONTHLY-002 — AI Resource Governance

AI execution SHALL respect:

```text
Token Limits
Message Limits
Model Limits
Agent Limits
Tool Limits
Workflow Limits
MCP Limits
RAG Limits
Voice Limits
Document Processing Limits
API Limits
```

---

## AI-UR-MONTHLY-003 — AI Cannot Modify Subscription

AI agents SHALL NOT independently:

```text
Upgrade Subscription
Downgrade Subscription
Change Pricing
Modify Quotas
Grant Credits
Change Payment Method
Disable Billing
```

unless explicitly authorized through a controlled automation.

---

## AI-UR-MONTHLY-004 — AI Usage Forecasting

AI MAY estimate future Monthly Plan usage based on:

```text
Historical Usage
Current Consumption
Projected Workload
Remaining Quota
Days Remaining
```

---

## AI-UR-MONTHLY-005 — AI Budget Protection

AI agents SHALL support:

```text
Maximum Token Budget
Maximum Runtime
Maximum Tool Calls
Maximum Workflow Depth
Maximum Concurrent Runs
Maximum Estimated Cost
```

---

## AI-UR-MONTHLY-006 — AI Upgrade Recommendation

AI MAY recommend another plan when:

```text
Usage Is Increasing
Quota Is Nearly Exhausted
Required Feature Is Unavailable
Required Capacity Exceeds Plan
```

Recommendations SHALL use authoritative pricing data.

---

## AI-UR-MONTHLY-007 — Human + AI Shared Quota

AI and human-generated operations SHALL be accounted for according to the Monthly Plan's defined quota model.

---

## 8. Monthly Subscription System Requirements

## SR-MONTHLY-001 — Subscription Object

Each Monthly Plan subscription SHALL include:

```text
subscription_id
organization_id
customer_id
plan_id
plan_version
status
billing_interval
currency
base_price
started_at
current_period_start
current_period_end
next_billing_at
cancel_at
cancelled_at
created_at
updated_at
```

---

## SR-MONTHLY-002 — Billing Interval

The Monthly Plan SHALL use:

```text
billing_interval = MONTH
```

unless explicitly configured otherwise.

---

## SR-MONTHLY-003 — Versioned Pricing

Pricing SHALL be versioned.

Example:

```text
MONTHLY_PRO v1
MONTHLY_PRO v2
MONTHLY_PRO v3
```

Existing subscriptions SHALL retain their applicable pricing version unless a controlled price-change migration occurs.

---

## 9. Monthly Plan Entitlements

The Monthly Plan SHALL support explicit entitlements for:

```text
Human Users
AI Agents
AI Messages
AI Tokens
AI Models
Workflows
Workflow Executions
MCP Servers
MCP Tool Calls
n8n Executions
API Requests
API Keys
Webhooks
Knowledge Bases
Documents
Storage
RAG Queries
Lead Records
Lead Generation
Lead Enrichment
CRM Integrations
Communication Integrations
Voice Minutes
Document Processing
Analytics
```

---

## 10. Entitlement Architecture

The effective entitlement SHALL be calculated as:

```text
Platform Policy
        ↓
Tenant Policy
        ↓
Subscription Tier
        ↓
Subscription Version
        ↓
Add-ons
        ↓
Approved Overrides
        ↓
Effective Entitlement
```

---

## 11. Monthly Plan Human User Limits

## FR-MONTHLY-001

The platform SHALL support:

```text
max_human_users
```

as a configurable entitlement.

---

## FR-MONTHLY-002

User provisioning SHALL perform an atomic quota check before creating a new active user.

---

## 12. AI Agent Limits

## FR-MONTHLY-003

The Monthly Plan SHALL define:

```text
max_ai_agents
max_active_ai_agents
max_concurrent_ai_agents
```

where applicable.

---

## 13. AI Message Quota

## FR-MONTHLY-004

The Monthly Plan MAY provide a monthly AI-message quota.

The quota SHALL reset at the beginning of each subscription period unless configured otherwise.

---

## 14. AI Token Quota

The system SHALL support:

```text
Monthly Input Tokens
Monthly Output Tokens
Monthly Total Tokens
Per-Request Token Limit
Per-Agent Token Budget
```

---

## 15. AI Model Entitlements

The platform SHALL maintain a model entitlement registry.

Example:

```text
Model
Provider
Tier Availability
Input Price
Output Price
Context Limit
Enabled
```

---

## 16. AI Model Selection

AI requests SHALL pass through an entitlement-aware AI gateway:

```text
AI Request
    ↓
Authentication
    ↓
Authorization
    ↓
Monthly Plan Check
    ↓
Model Entitlement
    ↓
Quota Check
    ↓
Rate Limit
    ↓
AI Gateway
```

---

## 17. AI Model Fallback

Where configured, the system MAY automatically select an allowed lower-cost model if the requested model is unavailable.

---

## 18. RAG Requirements

The Monthly Plan SHALL define:

```text
Knowledge Bases
Documents
Storage
Embedding Usage
RAG Queries
Vector Storage
Document Size
```

---

## 19. Workflow Requirements

The Monthly Plan SHALL support configurable:

```text
Active Workflows
Workflow Executions
Workflow Steps
Concurrent Executions
Execution Runtime
Scheduled Executions
```

---

## 20. Workflow AI Governance

AI workflows SHALL be subject to:

```text
Plan Entitlement
Quota
Token Budget
Tool Permissions
MCP Permissions
Runtime Limit
Concurrency Limit
```

---

## 21. n8n Integration

If enabled, the Monthly Plan SHALL define:

```text
Connected n8n Instances
Workflow Executions
Webhook Executions
Execution Frequency
AI Workflow Usage
```

---

## 22. MCP Requirements

The Monthly Plan SHALL support configurable:

```text
MCP Servers
MCP Tools
MCP Tool Calls
MCP Execution Runtime
Concurrent MCP Requests
```

---

## 23. API Access

Monthly Plan API access SHALL support configurable:

```text
Requests Per Minute
Requests Per Hour
Requests Per Day
Monthly Requests
Concurrent Requests
Endpoint Permissions
```

---

## 24. API Key Management

The plan SHALL define:

```text
Maximum API Keys
Key Scopes
Key Rotation
Key Expiration
Rate Limits
```

---

## 25. Webhook Requirements

The Monthly Plan SHALL support:

```text
Inbound Webhooks
Outbound Webhooks
Webhook Events
Webhook Delivery
Webhook Retry
Webhook Rate Limits
```

---

## 26. Lead Generation

The Monthly Plan SHALL support configurable:

```text
Lead Records
Lead Searches
Lead Generation
Lead Enrichment
Lead Scoring
Lead Exports
Company Records
Contact Records
```

---

## 27. CRM Integration

The Monthly Plan MAY support:

```text
Salesforce
HubSpot
Zendesk
Jira
Notion
Google Drive
Slack
Microsoft Teams
```

Each integration SHALL have explicit entitlement and quota definitions.

---

## 28. Communication Channels

The Monthly Plan SHALL support configurable access to:

```text
Email
WhatsApp
Facebook
Instagram
LinkedIn
YouTube
TikTok
Slack
Microsoft Teams
```

---

## 29. Gmail Requirements

If Gmail is included, the Monthly Plan SHALL support configurable:

```text
Connected Accounts
Email Synchronization
AI Email Generation
Email Operations
Daily Email Actions
```

---

## 30. WhatsApp Requirements

If WhatsApp is included, the Monthly Plan SHALL define:

```text
Connected Numbers
Messages
Conversations
Webhook Events
Automation
AI Replies
```

---

## 31. Voice AI Requirements

If Voice AI is included:

```text
Voice Minutes
Concurrent Calls
Calls Per Period
AI Voice Models
Transcription
Text-to-Speech
```

SHALL be explicitly controlled.

---

## 32. Document Intelligence

The Monthly Plan SHALL define:

```text
Documents Per Month
Pages Per Month
OCR Operations
Extraction Operations
Maximum File Size
Processing Models
```

---

## 33. Storage

Storage SHALL include:

```text
Documents
Attachments
Knowledge Base Files
Conversation Files
Generated Files
Vector Data
```

---

## 34. Storage Quota

The system SHALL enforce:

```text
storage_limit
storage_used
storage_reserved
storage_remaining
```

---

## 35. Analytics

Monthly Plan customers SHALL receive analytics according to plan entitlement.

Potential metrics:

```text
Sales
Leads
Conversions
Conversations
AI Usage
Workflow Usage
Support Performance
Agent Performance
Integration Activity
```

---

## 36. Usage Tracking

Every quota-controlled operation SHALL produce a usage event.

Example:

```text
ai.message.used
ai.token.used
ai.agent.executed
workflow.executed
workflow.step.executed
mcp.tool.used
api.request.used
lead.generated
lead.enriched
document.processed
storage.used
voice.minute.used
integration.request.used
```

---

## 37. Usage Event Schema

Each usage event SHOULD include:

```text
event_id
organization_id
user_id
subscription_id
plan_id
plan_version
resource_type
resource_id
quantity
timestamp
correlation_id
source
metadata
```

---

## 38. Usage Idempotency

Usage processing SHALL be idempotent.

Duplicate events SHALL NOT double-consume quota or generate duplicate billable usage.

---

## 39. Usage Reservation

Expensive operations SHALL use:

```text
Check
→ Reserve
→ Execute
→ Commit
```

Failed executions SHALL release or reconcile reservations.

---

## 40. Concurrency Protection

The Monthly Plan SHALL prevent quota bypass caused by concurrent requests.

The system MAY use:

```text
Redis Atomic Operations
Database Transactions
Optimistic Locking
Distributed Locks
Usage Reservations
```

---

## 41. Quota Reset

Monthly recurring quotas SHALL reset according to the subscription billing period.

```text
Current Period Ends
        ↓
New Period Starts
        ↓
New Quota Allocation
```

---

## 42. Quota Reset Safety

Quota reset SHALL NOT delete historical usage.

Historical usage SHALL remain queryable for:

```text
Billing
Analytics
Audit
Support
Reconciliation
```

---

## 43. Billing Period Requirements

Each Monthly Plan SHALL maintain:

```text
period_start
period_end
billing_date
usage_period_start
usage_period_end
```

---

## 44. Billing Anchor

The system SHALL maintain a deterministic billing anchor.

Example:

```text
Subscription Started:
August 15

Monthly Renewal:
15th of each month
```

If the selected billing day does not exist in a month, the billing engine SHALL apply a deterministic calendar policy.

---

## 45. Subscription Creation Flow

```text
User
 ↓
Select Monthly Plan
 ↓
Authentication
 ↓
Eligibility
 ↓
Pricing Calculation
 ↓
Coupon Validation
 ↓
Tax Calculation
 ↓
Payment Method
 ↓
Payment Authorization
 ↓
Payment Capture
 ↓
Subscription Creation
 ↓
Entitlement Activation
 ↓
Invoice Generation
 ↓
Usage Period Creation
 ↓
Notifications
 ↓
Audit
```

---

## 46. Payment Requirements

The Monthly Plan SHALL support:

```text
Payment Authorization
Payment Capture
Payment Verification
Payment Failure
Payment Retry
Payment Refund
Payment Reversal
```

---

## 47. Payment Provider Abstraction

The system SHALL abstract payment providers behind a common interface.

```text
PaymentGateway
    ├── Provider A
    ├── Provider B
    └── Provider C
```

---

## 48. Payment Idempotency

Subscription creation and payment operations SHALL use idempotency keys.

Duplicate checkout requests SHALL NOT create duplicate subscriptions or charges.

---

## 49. Invoice Requirements

Every successful recurring Monthly Plan billing cycle SHALL generate or associate an invoice according to billing policy.

Invoice SHALL contain:

```text
Invoice ID
Customer
Organization
Subscription
Billing Period
Line Items
Subtotal
Discount
Credits
Tax
Total
Currency
Payment Status
Due Date
Paid Date
```

---

## 50. Invoice Numbering

Invoice numbers SHALL be:

```text
Unique
Immutable
Sequential or Policy-Compliant
Auditable
Tenant-Aware Where Required
```

---

## 51. Tax Calculation

The billing engine SHALL support:

```text
Tax Jurisdiction
Tax Rate
Tax Exemption
Tax ID
Taxable Amount
Tax Amount
```

---

## 52. Coupon Support

The Monthly Plan MAY support coupons.

Coupon validation SHALL check:

```text
Coupon Status
Expiration
Usage Limit
Customer Eligibility
Plan Eligibility
Minimum Amount
Currency
Billing Interval
```

---

## 53. Coupon Application

Discount calculation SHALL be deterministic and auditable.

---

## 54. Credit Support

The Monthly Plan MAY support account credits.

Credits SHALL maintain:

```text
Credit ID
Amount
Currency
Source
Expiration
Remaining Balance
Applied Amount
```

---

## 55. Credit Application

Credit application SHALL follow a deterministic order.

Example:

```text
Subtotal
 ↓
Discount
 ↓
Credits
 ↓
Tax
 ↓
Final Amount
```

The exact tax/credit ordering SHALL be defined by the billing policy and applicable jurisdiction.

---

## 56. Proration

The Monthly Plan SHALL support proration when plan changes occur during an active billing period, where enabled.

---

## 57. Upgrade Proration

Example:

```text
Current Plan
      ↓
Upgrade Mid-Cycle
      ↓
Unused Existing Value
      ↓
Remaining Higher-Tier Value
      ↓
Proration Calculation
      ↓
Charge / Credit
```

---

## 58. Downgrade Proration

Downgrade behavior SHALL be explicitly configured.

Possible policies:

```text
Immediate
Next Renewal
Credit-Based
No Refund
```

---

## 59. Plan Upgrade

Users SHALL be able to upgrade from the Monthly Plan when eligible.

---

## 60. Upgrade Requirements

The upgrade engine SHALL:

```text
Validate Target Plan
Calculate Price
Calculate Proration
Apply Coupon
Apply Credit
Calculate Tax
Process Payment
Update Subscription
Update Entitlements
Generate Invoice
Record Audit Event
```

---

## 61. Plan Downgrade

Users SHALL be able to schedule eligible downgrades.

---

## 62. Downgrade Safety

If the target plan cannot support existing resources:

```text
Detect Excess Resources
        ↓
Notify User
        ↓
Provide Resolution Options
        ↓
Schedule Downgrade
```

The system SHALL NOT silently delete resources.

---

## 63. Cancellation

The Monthly Plan SHALL support:

```text
Cancel Immediately
Cancel At Period End
```

according to product policy.

---

## 64. Cancellation Flow

```text
User Requests Cancellation
        ↓
Authorization
        ↓
Cancellation Policy
        ↓
Refund Evaluation
        ↓
Subscription State Update
        ↓
Entitlement Policy
        ↓
Notification
        ↓
Audit
```

---

## 65. Cancellation at Period End

If cancellation occurs at period end:

```text
Current Entitlements
        ↓
Remain Active
        ↓
Until Period End
        ↓
Subscription Ends
```

---

## 66. Payment Failure

When recurring payment fails:

```text
Payment Failed
        ↓
Record Failure
        ↓
Retry Policy
        ↓
Notify Customer
        ↓
Grace Period
        ↓
Dunning
        ↓
Suspend / Cancel
```

---

## 67. Retry Policy

The payment retry engine SHALL support configurable:

```text
Retry Count
Retry Interval
Retry Schedule
Failure Classification
Final Failure Action
```

---

## 68. Grace Period

The Monthly Plan MAY provide a grace period after failed payment.

During grace period:

```text
Existing Access
Restricted Access
Read-Only Access
Suspension
```

SHALL be configurable.

---

## 69. Dunning

Dunning SHALL support:

```text
Email Notification
In-App Notification
Payment Update Request
Retry
Final Warning
Suspension
Cancellation
```

---

## 70. Subscription States

The Monthly Plan SHALL support:

```text
INCOMPLETE
TRIALING
ACTIVE
PAST_DUE
GRACE_PERIOD
SUSPENDED
CANCEL_AT_PERIOD_END
CANCELLED
EXPIRED
```

Only states applicable to the configured SalesGenie billing policy SHALL be exposed.

---

## 71. State Machine

```text
INCOMPLETE
    ↓
ACTIVE
    │
    ├──→ PAST_DUE
    │       ↓
    │   GRACE_PERIOD
    │       │
    │       ├──→ ACTIVE
    │       │
    │       └──→ SUSPENDED
    │                 ↓
    │              CANCELLED
    │
    ├──→ CANCEL_AT_PERIOD_END
    │          ↓
    │      CANCELLED
    │
    └──→ UPGRADED / DOWNGRADED
```

---

## 72. Subscription State Integrity

Invalid state transitions SHALL be rejected.

---

## 73. Webhook Processing

Payment-provider webhooks SHALL be:

```text
Authenticated
Validated
Idempotent
Audited
Replay-Protected
Order-Aware
```

---

## 74. Webhook Events

The system SHOULD support events such as:

```text
payment.succeeded
payment.failed
invoice.created
invoice.paid
invoice.payment_failed
subscription.created
subscription.updated
subscription.cancelled
refund.created
refund.completed
```

---

## 75. Event-Driven Billing

SalesGenie SHALL support event-driven subscription processing.

Example:

```text
Payment Success
      ↓
Event Bus
      ↓
Subscription Service
      ↓
Entitlement Service
      ↓
Usage Service
      ↓
Invoice Service
      ↓
Notification Service
      ↓
Analytics
```

---

## 76. Event Idempotency

Every billing event SHALL have:

```text
event_id
event_type
event_version
timestamp
correlation_id
aggregate_id
```

Duplicate events SHALL be safely ignored or reconciled.

---

## 77. Out-of-Order Events

The billing architecture SHALL tolerate delayed or out-of-order provider events.

---

## 78. Reconciliation

The system SHALL periodically reconcile:

```text
Payment Provider
Subscription Database
Invoice Database
Usage Database
Entitlement Database
```

---

## 79. Billing Reconciliation

Differences SHALL produce:

```text
Reconciliation Event
Alert
Audit Entry
Correction Workflow
```

---

## 80. Monthly Usage Accounting

Each Monthly billing period SHALL maintain:

```text
Opening Usage
Usage Events
Reserved Usage
Committed Usage
Adjustments
Credits
Closing Usage
```

---

## 81. Metered Billing Compatibility

If the Monthly Plan includes usage-based components, the system SHALL support:

```text
Meter
Usage Event
Aggregation
Rate
Unit Price
Threshold
Subtotal
```

---

## 82. Hybrid Billing

The Monthly Plan MAY combine:

```text
Fixed Monthly Subscription
+
Included Usage
+
Metered Overage
+
Add-Ons
```

Automatic overage SHALL require explicit product policy and customer authorization.

---

## 83. Overage Safety

The system SHALL never unexpectedly charge a customer solely because a quota was exceeded.

Where overage is disabled:

```text
Quota Exhausted
      ↓
Block / Degrade
      ↓
Notify
      ↓
Upgrade CTA
```

---

## 84. Included Credits

The Monthly Plan MAY include monthly AI or platform credits.

Example:

```text
Monthly Credits
        ↓
Usage
        ↓
Remaining Credits
```

---

## 85. Credit Reset

Included recurring credits SHALL reset according to the billing period unless explicitly configured otherwise.

---

## 86. Credit Expiration

Unused recurring credits MAY expire at period end according to plan policy.

The expiration policy SHALL be clearly communicated.

---

## 87. Credit Ledger

Credits SHALL be tracked through an immutable ledger.

Example:

```text
Credit Granted
Credit Reserved
Credit Consumed
Credit Released
Credit Expired
Credit Adjusted
```

---

## 88. Billing Ledger

Financially relevant billing operations SHOULD use an append-only ledger.

---

## 89. Money Precision

Monetary values SHALL NOT rely on floating-point arithmetic.

Use:

```text
Decimal
Integer Minor Units
```

according to currency requirements.

---

## 90. Currency

Each Monthly Plan subscription SHALL have an explicit currency.

---

## 91. Currency Consistency

A subscription SHALL NOT silently change currency during renewal.

---

## 92. Price Calculation

The pricing engine SHALL calculate:

```text
Base Price
+
Add-Ons
-
Discounts
-
Credits
+
Tax
=
Final Amount
```

according to configured billing policy.

---

## 93. Price Calculation Determinism

Given the same:

```text
Plan Version
Usage
Currency
Coupon
Credits
Tax Context
Billing Date
```

the pricing engine SHALL produce the same result.

---

## 94. Price Preview

Before subscription or plan change, users SHALL be able to preview:

```text
Base Price
Discount
Credit
Tax
Total
Next Billing Date
```

---

## 95. Billing Transparency

Users SHALL be informed about:

```text
Recurring Amount
Billing Frequency
Renewal Date
Usage Charges
Potential Overage
Tax
Discount Duration
```

---

## 96. Payment Security

Payment card information SHALL NOT be stored directly in SalesGenie unless the platform is explicitly designed and certified for such storage.

Prefer payment-provider tokenization.

---

## 97. Secret Protection

Payment provider secrets SHALL be stored in secure secret-management infrastructure.

---

## 98. Payment Audit

The platform SHALL audit:

```text
Payment Attempt
Payment Success
Payment Failure
Refund
Payment Method Change
Subscription Change
Admin Override
```

---

## 99. Authorization

Billing operations SHALL require appropriate permissions.

Example:

```text
View Billing
Manage Payment Method
Change Plan
Cancel Subscription
Issue Refund
Apply Credit
Modify Coupon
```

shall be independently permission-controlled.

---

## 100. Tenant Isolation

Monthly Plan billing data SHALL be isolated by organization.

A tenant SHALL never access another tenant's:

```text
Invoices
Payments
Subscriptions
Usage
Credits
Coupons
Tax Information
Payment Methods
```

---

## 101. AI Billing Security

AI agents SHALL NOT be able to access raw payment credentials.

---

## 102. AI Financial Actions

AI MAY explain billing information but SHALL NOT perform high-impact financial actions without explicit authorization.

Examples:

```text
Refund
Upgrade
Downgrade
Cancel
Change Payment Method
```

---

## 103. AI Billing Assistant

The platform MAY provide an AI billing assistant capable of answering:

```text
What is my monthly price?
When is my next renewal?
How much AI usage have I consumed?
Why was my invoice higher?
What features are included?
What happens if I downgrade?
```

Answers SHALL be generated from authoritative billing data.

---

## 104. Human Approval for Financial Actions

Where AI-initiated billing workflows exist:

```text
AI Recommendation
      ↓
Human Confirmation
      ↓
Authorization
      ↓
Billing Execution
```

---

## 105. Refund Requirements

The Monthly Plan SHALL integrate with the refund subsystem.

Refund eligibility SHALL consider:

```text
Payment Status
Refund Policy
Subscription State
Refund Window
Previous Refunds
Invoice
```

---

## 106. Partial Refunds

The billing system SHALL support partial refunds where permitted.

---

## 107. Refund Idempotency

A refund operation SHALL be idempotent.

---

## 108. Invoice Corrections

If an invoice requires correction, the platform SHALL use appropriate credit-note, adjustment, or replacement mechanisms instead of mutating historical financial records.

---

## 109. Audit Logging

The system SHALL audit:

```text
Subscription Created
Subscription Renewed
Subscription Upgraded
Subscription Downgraded
Subscription Cancelled
Payment Succeeded
Payment Failed
Invoice Created
Invoice Paid
Refund Created
Refund Completed
Coupon Applied
Credit Applied
Tax Calculated
Quota Reset
Entitlement Changed
Administrative Override
```

---

## 110. Audit Record

Each audit event SHOULD contain:

```text
event_id
organization_id
actor_id
actor_type
action
resource_type
resource_id
before
after
timestamp
ip_address
correlation_id
reason
```

---

## 111. Administrative Override

Super Admins MAY perform controlled overrides.

Examples:

```text
Temporary Credit
Temporary Quota Increase
Grace Period Extension
Manual Subscription Correction
Refund Approval
Billing Adjustment
```

---

## 112. Override Requirements

Overrides SHALL:

```text
Require Authorization
Be Time-Bounded Where Possible
Be Tenant-Scoped
Have A Reason
Be Audited
Be Reversible
```

---

## 113. Monthly Plan Notifications

The platform SHALL support notifications for:

```text
Subscription Created
Payment Successful
Invoice Generated
Upcoming Renewal
Payment Failed
Payment Retry
Grace Period
Subscription Suspended
Subscription Cancelled
Plan Changed
Quota Warning
Quota Exhausted
Refund
Credit Applied
```

---

## 114. Notification Timing

Renewal notifications SHOULD support configurable schedules.

Example:

```text
7 Days Before Renewal
3 Days Before Renewal
1 Day Before Renewal
Payment Success
Payment Failure
```

---

## 115. Monthly Billing Dashboard

Billing administrators SHALL be able to view:

```text
Current Plan
Monthly Price
Billing Period
Next Billing Date
Payment Method
Usage
Credits
Discounts
Invoices
Payments
Subscription Status
```

---

## 116. Usage Dashboard

The usage dashboard SHALL display:

```text
AI Messages
AI Tokens
AI Agents
Workflow Executions
MCP Calls
API Requests
Storage
Leads
Voice Minutes
Document Processing
```

according to plan entitlements.

---

## 117. Usage Forecast

The system MAY calculate:

```text
Current Consumption Rate
Projected Period Usage
Projected Quota Exhaustion
Estimated Overage
Recommended Action
```

---

## 118. Billing Analytics

Platform administrators SHALL be able to analyze:

```text
Monthly Recurring Revenue
New Monthly Subscriptions
Renewals
Cancellations
Upgrade Rate
Downgrade Rate
Payment Failure Rate
Refund Rate
Average Revenue Per Account
Customer Lifetime Value
Plan Utilization
AI Cost
Gross Margin
```

---

## 119. AI Cost Analytics

SalesGenie SHALL track AI infrastructure cost associated with Monthly Plan customers where technically and contractually appropriate.

Potential dimensions:

```text
Organization
AI Agent
Model
Provider
Workflow
User
Feature
Token Type
```

---

## 120. Unit Economics

The system SHOULD calculate:

```text
Revenue Per Account
AI Cost Per Account
Infrastructure Cost
Gross Margin
Contribution Margin
```

---

## 121. Observability

Monthly Plan services SHALL expose metrics such as:

```text
monthly_subscription_count
monthly_active_subscriptions
monthly_renewal_success_rate
monthly_payment_failure_rate
monthly_churn_rate
monthly_upgrade_rate
monthly_downgrade_rate
monthly_refund_rate
monthly_mrr
monthly_usage
monthly_ai_cost
monthly_quota_exhaustion
```

---

## 122. Distributed Tracing

Billing operations SHALL propagate:

```text
Correlation ID
Trace ID
Request ID
Subscription ID
Organization ID
```

across services.

---

## 123. Performance Requirements

Subscription entitlement checks SHOULD target:

```text
P95 < 50 ms
P99 < 150 ms
```

under normal production load.

---

## 124. Billing API Performance

Billing APIs SHOULD meet platform-defined SLA targets while protecting downstream payment providers from excessive traffic.

---

## 125. Reliability

Subscription state SHALL remain correct despite:

```text
Network Failure
Service Restart
Payment Provider Timeout
Duplicate Webhooks
Delayed Webhooks
Database Failover
Event Replay
```

---

## 126. Failure Semantics

For billing-critical operations:

```text
Unknown Payment State
        ↓
Do Not Assume Failure
        ↓
Reconcile With Provider
```

The platform SHALL avoid charging or provisioning twice because of ambiguous network failures.

---

## 127. Payment Timeout Handling

A payment timeout SHALL produce an intermediate state where necessary rather than immediately assuming the payment failed.

---

## 128. Subscription Provisioning Safety

Entitlements SHALL only become active when the subscription state satisfies activation policy.

---

## 129. Entitlement Cache

Monthly Plan entitlements MAY be cached for performance.

Cache SHALL include:

```text
Organization
Subscription ID
Plan ID
Plan Version
Entitlements
Timestamp
TTL
```

---

## 130. Cache Invalidation

Subscription changes SHALL invalidate entitlement caches.

```text
Subscription Changed
        ↓
Event
        ↓
Cache Invalidation
        ↓
Entitlement Refresh
```

---

## 131. Eventual Consistency

The architecture SHALL define which operations permit eventual consistency.

Billing-critical operations SHALL use stronger consistency where required.

---

## 132. Database Requirements

Core entities SHALL include:

```text
Customer
Organization
Subscription
SubscriptionPlan
SubscriptionPlanVersion
SubscriptionItem
Entitlement
Quota
UsagePeriod
UsageEvent
UsageReservation
Invoice
InvoiceItem
Payment
PaymentMethodReference
Refund
Credit
CreditLedger
Coupon
Discount
TaxRecord
BillingEvent
AuditEvent
```

---

## 133. Database Constraints

The system SHALL enforce:

```text
Valid Organization
Valid Customer
Valid Subscription
Valid Plan
Valid Plan Version
Valid Billing Period
Unique Invoice Number
Unique Payment Reference
Unique Usage Event ID
Unique External Event ID
```

---

## 134. Historical Financial Integrity

Financial records SHALL be immutable after finalization except through explicit correction mechanisms.

---

## 135. Plan Versioning

Monthly Plan versions SHALL preserve historical billing behavior.

Example:

```text
MONTHLY_STANDARD v1
MONTHLY_STANDARD v2
MONTHLY_STANDARD v3
```

---

## 136. Price Change Management

Price changes SHALL support:

```text
Draft
Review
Approval
Scheduled
Effective
Archived
```

---

## 137. Existing Customer Price Policy

The system SHALL support configurable price-change policies:

```text
Grandfather Existing Customers
Immediate Change
Next Renewal
Customer Consent Required
```

---

## 138. Price Change Notification

Customers SHALL be notified of material recurring-price changes according to applicable policy and law.

---

## 139. Monthly Renewal Flow

```text
Billing Scheduler
        ↓
Identify Renewals
        ↓
Resolve Subscription
        ↓
Resolve Plan Version
        ↓
Calculate Recurring Price
        ↓
Apply Credits / Discounts
        ↓
Calculate Usage Charges
        ↓
Calculate Tax
        ↓
Create Invoice
        ↓
Charge Payment Method
        ↓
Confirm Payment
        ↓
Mark Invoice Paid
        ↓
Start New Usage Period
        ↓
Reset Recurring Quotas
        ↓
Publish Events
        ↓
Notify Customer
        ↓
Audit
```

---

## 140. Renewal Idempotency

A renewal SHALL have a deterministic idempotency key.

Example:

```text
subscription_id + billing_period_start
```

Duplicate renewal jobs SHALL NOT create duplicate charges.

---

## 141. Scheduler Reliability

The billing scheduler SHALL support:

```text
Distributed Execution
Leader Election or Claiming
Retries
Dead-Letter Handling
Idempotency
Monitoring
```

---

## 142. Renewal Recovery

If a renewal job fails:

```text
Detect Failure
        ↓
Retry
        ↓
Reconcile
        ↓
Continue / Escalate
```

---

## 143. Monthly Plan Usage Period

Every subscription period SHALL have a unique usage period.

Example:

```text
subscription_id
period_start
period_end
```

---

## 144. Usage Period Isolation

Usage from one billing period SHALL NOT accidentally consume another period's quota.

---

## 145. Usage Adjustment

Authorized administrators SHALL be able to create usage adjustments.

Adjustments SHALL require:

```text
Reason
Actor
Amount
Timestamp
Reference
Audit Event
```

---

## 146. Usage Reconciliation

The system SHALL reconcile:

```text
AI Gateway Usage
Workflow Engine Usage
MCP Usage
API Gateway Usage
Storage Usage
Integration Usage
Billing Usage
```

---

## 147. Free vs Monthly Boundary

The platform SHALL explicitly distinguish:

```text
FREE
MONTHLY
YEARLY
USAGE_BASED
METERED
```

subscriptions.

No Free Plan entitlement SHALL accidentally apply to a Monthly Plan.

---

## 148. Monthly Plan and Add-Ons

The Monthly Plan MAY support add-ons such as:

```text
Additional AI Credits
Additional Storage
Additional Users
Additional Voice Minutes
Additional Workflow Executions
Additional Integrations
```

---

## 149. Add-On Lifecycle

Add-ons SHALL support:

```text
Added
Active
Paused
Cancelled
Expired
```

---

## 150. Add-On Billing

Add-ons MAY be:

```text
Recurring Monthly
One-Time
Usage-Based
```

according to configuration.

---

## 151. Subscription Items

A subscription SHALL support multiple line items:

```text
Base Plan
Add-On
Metered Component
Discount
Credit
```

---

## 152. Customer Self-Service

Billing administrators SHOULD be able to self-service:

```text
View Invoice
Download Invoice
Update Payment Method
Change Plan
Cancel Plan
View Usage
View Payment History
```

subject to permissions.

---

## 153. Invoice Download

Invoices SHOULD be available in supported formats such as:

```text
PDF
```

---

## 154. Invoice Email

Invoices MAY be delivered through email after successful billing.

---

## 155. Billing Portal

SalesGenie MAY provide a dedicated billing portal.

The billing portal SHALL enforce authentication and tenant authorization.

---

## 156. Billing API

The API SHALL expose secure endpoints for:

```text
GET Subscription
POST Subscription
PATCH Subscription
POST Upgrade
POST Downgrade
POST Cancel
GET Invoices
GET Payments
GET Usage
POST Payment Method
GET Credits
```

Exact endpoint naming SHALL follow SalesGenie's API conventions.

---

## 157. API Error Contract

Billing APIs SHALL return structured errors.

Example:

```json
{
  "code": "SUBSCRIPTION_PAYMENT_REQUIRED",
  "message": "A valid payment method is required.",
  "subscription_id": "sub_xxx",
  "retryable": false
}
```

---

## 158. Quota Error Contract

Example:

```json
{
  "code": "MONTHLY_QUOTA_EXCEEDED",
  "resource": "ai_messages",
  "limit": 10000,
  "used": 10000,
  "remaining": 0,
  "reset_at": "2026-09-28T00:00:00Z"
}
```

---

## 159. Security Requirements

The Monthly Plan SHALL implement:

```text
Zero Trust
Least Privilege
RBAC
ABAC Where Required
Tenant Isolation
Encryption
Secure Secret Management
Audit Logging
Rate Limiting
Fraud Detection
Webhook Verification
Idempotency
Replay Protection
```

---

## 160. Fraud Detection

The platform SHOULD detect:

```text
Repeated Payment Failures
Suspicious Account Creation
Payment Method Abuse
Coupon Abuse
Credit Abuse
Refund Abuse
Credential Sharing
Automated Subscription Creation
```

---

## 161. Coupon Abuse Prevention

The platform SHALL prevent users from repeatedly applying restricted coupons.

---

## 162. Credit Abuse Prevention

Credits SHALL be scoped to:

```text
Organization
Subscription
Currency
Expiration
```

according to policy.

---

## 163. Refund Abuse Detection

Repeated refunds MAY trigger:

```text
Risk Review
Manual Approval
Account Restriction
```

according to policy.

---

## 164. AI Abuse Detection

AI systems SHALL monitor unusual:

```text
Token Consumption
Workflow Recursion
Tool Calls
MCP Calls
API Requests
Lead Generation
```

---

## 165. AI Runaway Protection

The platform SHALL terminate AI executions that exceed configured:

```text
Token Budget
Time Budget
Tool Budget
Cost Budget
Recursion Depth
```

---

## 166. Human + AI Resource Governance

The Monthly Plan SHALL use a unified resource governance model:

```text
                 MONTHLY PLAN
                       │
          ┌────────────┴────────────┐
          │                         │
       HUMAN                      AI
          │                         │
     User Actions              Agent Actions
     API Actions               Workflow Actions
     Manual Work               Tool Actions
          │                         │
          └────────────┬────────────┘
                       ▼
                 USAGE ENGINE
                       │
                       ▼
                QUOTA ENGINE
                       │
                       ▼
                 POLICY ENGINE
                       │
             ┌─────────┼─────────┐
             ▼         ▼         ▼
           ALLOW     DEGRADE     DENY
```

---

## 167. AI + Human Auditability

Every high-impact action SHALL identify whether it originated from:

```text
HUMAN
AI
AUTOMATION
SYSTEM
ADMIN
```

---

## 168. Human Approval Boundary

Where approval is required:

```text
AI
 ↓
Proposed Action
 ↓
Human Approval
 ↓
Authorized Execution
 ↓
Usage Recording
 ↓
Audit
```

---

## 169. AI Cannot Become Billing Authority

The AI layer SHALL consume billing decisions from authoritative billing services.

The AI SHALL NOT independently calculate final financial charges.

---

## 170. Pricing Authority

The Pricing Engine SHALL be the authoritative source for:

```text
Plan Price
Discount
Coupon
Proration
Add-On Price
Metered Price
```

---

## 171. Billing Authority

The Billing Service SHALL be authoritative for:

```text
Subscription State
Billing Period
Invoice State
Payment State
Credit Ledger
Refund State
```

---

## 172. Entitlement Authority

The Entitlement Service SHALL be authoritative for:

```text
Feature Access
Resource Limits
AI Capabilities
Integration Access
Quota
```

---

## 173. Usage Authority

The Usage Service SHALL be authoritative for:

```text
Usage Events
Aggregations
Reservations
Quota Consumption
Usage Periods
```

---

## 174. Separation of Concerns

The architecture SHALL avoid placing all billing logic in a single service.

Recommended:

```text
Pricing Service
Subscription Service
Billing Service
Payment Service
Invoice Service
Tax Service
Credit Service
Usage Service
Entitlement Service
Notification Service
Analytics Service
```

---

## 175. Monthly Plan Architecture

```text
                         SALES GENIE
                              │
                              ▼
                     Subscription Service
                              │
                              ▼
                       MONTHLY PLAN
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
          ▼                   ▼                   ▼
       Pricing           Entitlements          Usage
          │                   │                   │
          ▼                   ▼                   ▼
      Discounts            Quotas              Meters
      Coupons              Features           Reservations
      Credits              Limits             Events
          │                   │                   │
          └───────────────────┼───────────────────┘
                              ▼
                         Billing Engine
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
           Invoice         Tax Engine     Payment
              │               │               │
              └───────────────┼───────────────┘
                              ▼
                        Event Bus
                              │
       ┌──────────────┬───────┼────────┬──────────────┐
       ▼              ▼       ▼        ▼              ▼
     Audit         Analytics  AI     Notifications  Reconciliation
```

---

## 176. Monthly Plan AI Execution Architecture

```text
AI Request
    ↓
Authentication
    ↓
Tenant Resolution
    ↓
RBAC / ABAC
    ↓
Monthly Subscription Check
    ↓
Feature Entitlement
    ↓
Model Entitlement
    ↓
Quota Check
    ↓
Rate Limit
    ↓
Risk Policy
    ↓
Reserve Usage
    ↓
AI Gateway
    ↓
Model
    ↓
Tool / MCP / RAG
    ↓
Execution
    ↓
Commit Usage
    ↓
Audit
    ↓
Analytics
```

---

## 177. Monthly Renewal Architecture

```text
              BILLING SCHEDULER
                      │
                      ▼
              Renewal Candidates
                      │
                      ▼
             Subscription Validation
                      │
                      ▼
                Price Calculation
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
     Discounts      Credits        Tax
        │             │             │
        └─────────────┼─────────────┘
                      ▼
                 Invoice
                      │
                      ▼
               Payment Gateway
                      │
              ┌───────┴────────┐
              ▼                ▼
            Success           Failure
              │                │
              ▼                ▼
       Renew Subscription    Retry/Dunning
              │                │
              ▼                ▼
        Reset Quotas       Grace Period
              │                │
              ▼                ▼
        New Usage Period    Suspend
              │
              ▼
          Notification
              │
              ▼
            Audit
```

---

## 178. Monthly Plan Security Boundary

```text
UNTRUSTED REQUEST
       ↓
Authentication
       ↓
Tenant Resolution
       ↓
Authorization
       ↓
Subscription Resolution
       ↓
Monthly Plan Entitlement
       ↓
Quota Validation
       ↓
Rate Limit
       ↓
Fraud / Risk Check
       ↓
Execution
       ↓
Usage Recording
       ↓
Audit
```

---

## 179. Failure Recovery

The Monthly Plan SHALL recover safely from:

```text
Payment Provider Timeout
Duplicate Payment
Duplicate Webhook
Database Failure
Redis Failure
Event Bus Failure
Invoice Failure
Tax Service Failure
Notification Failure
AI Gateway Failure
Usage Service Failure
```

---

## 180. Dead-Letter Handling

Failed billing events SHALL be moved to a dead-letter mechanism after configurable retry attempts.

---

## 181. Manual Recovery

Authorized billing administrators SHALL have tools to:

```text
Replay Event
Reconcile Subscription
Reconcile Payment
Regenerate Invoice
Apply Adjustment
Restore Entitlement
```

All manual actions SHALL be audited.

---

## 182. Disaster Recovery

Billing data SHALL be included in SalesGenie's disaster-recovery strategy.

Critical records include:

```text
Subscriptions
Invoices
Payments
Refunds
Credits
Usage
Entitlements
Audit Logs
```

---

## 183. Backup Requirements

Critical billing databases SHALL support:

```text
Automated Backups
Point-in-Time Recovery
Encryption
Retention Policy
Recovery Testing
```

---

## 184. Data Retention

The system SHALL define retention policies for:

```text
Invoices
Payments
Usage
Audit Logs
Subscription History
Refunds
Credits
Tax Records
```

Retention SHALL comply with applicable legal and financial requirements.

---

## 185. Privacy

Monthly Plan customers SHALL retain the same fundamental data-protection guarantees as other SalesGenie customers.

---

## 186. Testing Requirements

## Unit Tests

The platform SHALL test:

```text
Plan Resolution
Price Calculation
Tax Calculation
Coupon Calculation
Credit Calculation
Proration
Quota Calculation
Usage Aggregation
Subscription State Machine
Renewal
Cancellation
Upgrade
Downgrade
Payment Retry
Refund
```

---

## 187. Integration Tests

The system SHALL test integration with:

```text
Payment Gateway
Subscription Service
Pricing Engine
Usage Service
Entitlement Service
Invoice Service
Tax Service
Credit Service
Notification Service
AI Gateway
Workflow Engine
MCP
n8n
CRM Integrations
```

---

## 188. Security Tests

Security testing SHALL include:

```text
Tenant Isolation
Billing Data Access
Privilege Escalation
Payment Replay
Webhook Forgery
Coupon Abuse
Credit Abuse
Refund Abuse
Quota Bypass
Plan ID Tampering
Price Tampering
Subscription ID Tampering
AI Billing Authorization
```

---

## 189. Concurrency Tests

The platform SHALL test:

```text
Concurrent Checkout
Concurrent Renewal
Concurrent Upgrade
Concurrent Downgrade
Concurrent Quota Consumption
Concurrent Payment Webhooks
Concurrent Usage Events
```

---

## 190. Chaos Tests

The platform SHOULD simulate:

```text
Payment Gateway Timeout
Duplicate Webhooks
Out-of-Order Events
Redis Failure
Database Failover
Event Bus Failure
Invoice Failure
Tax Service Failure
Notification Failure
```

---

## 191. Load Testing

The Monthly Plan SHALL be tested under:

```text
High Subscription Volume
Mass Renewal
Mass Invoice Generation
High AI Usage
High Usage Event Throughput
High Concurrent Entitlement Checks
```

---

## 192. Acceptance Criteria

The Monthly Plan SHALL be considered production-ready when:

* [ ] Monthly Plan is versioned.
* [ ] Monthly pricing is configurable.
* [ ] Billing interval is explicitly monthly.
* [ ] Subscription lifecycle is implemented.
* [ ] Subscription state transitions are validated.
* [ ] Human-user limits are enforced.
* [ ] AI-agent limits are enforced.
* [ ] AI model entitlements are enforced.
* [ ] AI token usage is tracked.
* [ ] AI message usage is tracked.
* [ ] Workflow quotas are enforced.
* [ ] MCP quotas are enforced.
* [ ] n8n quotas are enforced where enabled.
* [ ] API limits are enforced.
* [ ] Storage limits are enforced.
* [ ] RAG limits are enforced.
* [ ] Lead-generation limits are enforced.
* [ ] Integration limits are enforced.
* [ ] Usage periods are created per billing cycle.
* [ ] Usage events are idempotent.
* [ ] Usage reservations prevent race-condition bypass.
* [ ] Monthly quota resets are atomic.
* [ ] Subscription renewal is automated.
* [ ] Renewal is idempotent.
* [ ] Payment failures trigger retry logic.
* [ ] Grace periods are supported.
* [ ] Dunning is supported.
* [ ] Invoice generation is implemented.
* [ ] Tax calculation is integrated.
* [ ] Coupons are supported where enabled.
* [ ] Credits are supported where enabled.
* [ ] Proration is deterministic.
* [ ] Upgrades are supported.
* [ ] Downgrades are supported.
* [ ] Cancellation is supported.
* [ ] Refunds are integrated.
* [ ] Payment-provider webhooks are authenticated.
* [ ] Webhooks are idempotent.
* [ ] Billing records are auditable.
* [ ] Financial records are immutable after finalization.
* [ ] Tenant isolation is enforced.
* [ ] AI cannot independently alter billing.
* [ ] Human approval exists for high-impact AI financial actions where required.
* [ ] Billing reconciliation exists.
* [ ] Usage reconciliation exists.
* [ ] Billing analytics exist.
* [ ] AI cost analytics exist.
* [ ] Subscription events are observable.
* [ ] Distributed tracing exists.
* [ ] Disaster recovery covers billing data.
* [ ] Security testing passes.
* [ ] Concurrency testing passes.
* [ ] Load testing passes.
* [ ] Chaos testing passes.

---

## 193. FAANG-Level Monthly Plan Requirement Matrix

| Domain       | Human Requirement         | AI Requirement          | System Requirement           | Functional Requirement        |
| ------------ | ------------------------- | ----------------------- | ---------------------------- | ----------------------------- |
| Subscription | View/manage subscription  | Explain subscription    | Versioned subscription state | Create/update/cancel          |
| Pricing      | View price                | Explain pricing         | Pricing engine               | Calculate deterministic price |
| Payment      | Manage payment method     | Explain payment status  | Payment abstraction          | Charge/retry/refund           |
| Invoice      | View/download invoice     | Explain invoice         | Invoice service              | Generate/finalize invoice     |
| Tax          | View tax                  | Explain tax             | Tax engine                   | Calculate tax                 |
| Usage        | View usage                | Forecast usage          | Usage service                | Track/aggregate usage         |
| AI           | Use AI                    | Execute agents          | AI gateway                   | Enforce AI quotas             |
| Workflow     | Create workflows          | Execute workflows       | Workflow engine              | Enforce workflow limits       |
| MCP          | Configure allowed tools   | Invoke allowed tools    | MCP gateway                  | Enforce MCP quotas            |
| n8n          | Connect n8n               | Execute automation      | Integration service          | Enforce execution limits      |
| Leads        | Manage leads              | Generate/enrich leads   | Lead service                 | Enforce lead quotas           |
| Storage      | Upload files              | Process files           | Storage service              | Enforce storage limits        |
| Credits      | View credits              | Explain credits         | Credit ledger                | Apply/expire credits          |
| Coupons      | Apply eligible coupons    | Explain discount        | Coupon service               | Validate/apply coupon         |
| Refund       | Request refund            | Explain eligibility     | Refund service               | Process refund                |
| Security     | Secure billing access     | Respect authorization   | Zero-trust architecture      | Enforce RBAC/ABAC             |
| Analytics    | View account analytics    | Analyze usage           | Analytics pipeline           | Generate billing metrics      |
| Audit        | View permitted audit data | Explain audited actions | Audit service                | Immutable audit logging       |

---

## 194. Ultimate Monthly Plan Requirement

The SalesGenie Monthly Plan SHALL provide a production-grade recurring subscription system in which:

```text
Human Users
      +
AI Agents
      +
AI Workflows
      +
Integrations
      +
MCP Tools
      +
n8n Automation
      +
API Usage
      +
Storage
      +
Lead Generation
      +
RAG
      +
Voice
```

are governed by:

```text
Subscription
      ↓
Plan Version
      ↓
Entitlements
      ↓
Quota
      ↓
Usage
      ↓
Policy
      ↓
Authorization
      ↓
Execution
      ↓
Billing
      ↓
Audit
```

Financial operations SHALL be governed by:

```text
Pricing Engine
      ↓
Discounts
      ↓
Credits
      ↓
Tax
      ↓
Invoice
      ↓
Payment
      ↓
Reconciliation
```

Subscription lifecycle SHALL be governed by:

```text
CREATE
  ↓
ACTIVATE
  ↓
RENEW
  ↓
UPGRADE / DOWNGRADE
  ↓
PAST_DUE
  ↓
GRACE_PERIOD
  ↓
SUSPEND
  ↓
CANCEL
```

The final Monthly Plan architecture SHALL preserve:

```text
Security
+
Tenant Isolation
+
Billing Integrity
+
AI Governance
+
Usage Accuracy
+
Payment Reliability
+
Financial Auditability
+
Scalability
+
Observability
+
Disaster Recovery
+
Product Transparency
+
Human Control
+
AI Safety
```

No frontend component, AI agent, workflow, API client, integration, or external event SHALL be trusted as the authoritative source of subscription status, pricing, quota, payment state, or financial truth.

The authoritative SalesGenie architecture SHALL remain:

```text
                  MONTHLY SUBSCRIPTION
                          │
          ┌───────────────┼────────────────┐
          ▼               ▼                ▼
       PRICING       ENTITLEMENTS         USAGE
          │               │                │
          └───────────────┼────────────────┘
                          ▼
                    POLICY ENGINE
                          │
              ┌───────────┼───────────┐
              ▼           ▼           ▼
            HUMAN        AI        AUTOMATION
              │           │           │
              └───────────┼───────────┘
                          ▼
                    BILLING ENGINE
                          │
          ┌───────────────┼────────────────┐
          ▼               ▼                ▼
       INVOICE           TAX             PAYMENT
          │               │                │
          └───────────────┼────────────────┘
                          ▼
                    EVENT / LEDGER
                          │
          ┌───────────────┼────────────────┐
          ▼               ▼                ▼
        AUDIT          ANALYTICS      RECONCILIATION
```

The Monthly Plan SHALL therefore function as a first-class subscription tier within SalesGenie's enterprise billing architecture rather than as a collection of frontend feature flags or isolated payment logic.
