# SalesGenie — Subscription Lifecycle Requirements

**Document:** `subscription_lifecycle.md`  
**Product:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Requirement Level:** FAANG-Level / Production-Grade SaaS  
**Scope:** Subscription Creation, Activation, Renewal, Upgrade, Downgrade, Pause, Resume, Cancellation, Reactivation, Expiration, Grace Period, Payment Failure, Dunning, Plan Changes, Entitlements, Usage, Credits, Billing, Invoices, Taxes, Coupons, Refunds, AI/Human Operations, Webhooks, Audit, Analytics, and Recovery

---

## 1. Purpose

SalesGenie shall provide a production-grade, multi-tenant subscription lifecycle management system capable of managing the complete lifecycle of customer subscriptions from initial purchase through activation, recurring billing, plan changes, payment recovery, cancellation, expiration, and reactivation.

The system shall support:

- Free subscriptions
- Trial-to-paid conversion
- Monthly subscriptions
- Yearly subscriptions
- Usage-based subscriptions
- Metered billing
- Hybrid billing
- Subscription tiers
- Plan limits
- Feature entitlements
- AI-agent limits
- Human-seat limits
- Credits
- Coupons
- Taxes
- Invoices
- Refunds
- Payment gateways
- Payment failures
- Dunning
- Grace periods
- Upgrade
- Downgrade
- Pause
- Resume
- Cancellation
- Immediate cancellation
- End-of-period cancellation
- Reactivation
- Subscription expiration
- Subscription migration
- Enterprise custom subscriptions
- AI-assisted lifecycle management
- Human-controlled lifecycle management
- Webhook-driven state synchronization
- Event-driven architecture
- Auditability
- Usage reconciliation
- Billing reconciliation
- Entitlement reconciliation

Subscription lifecycle state shall be authoritative on the backend and shall never depend on frontend state.

---

## 2. Product Context

SalesGenie is an enterprise multi-tenant AI platform supporting:

- AI Sales Agents
- AI Support Agents
- Human Sales Agents
- Human Support Agents
- Multi-Agent Orchestration
- RAG Knowledge Management
- Lead Generation
- Lead Intelligence
- Workflow Automation
- Omnichannel Communication
- MCP Tools
- External Data Sources
- Gmail
- Google Drive
- LinkedIn
- Facebook
- Instagram
- WhatsApp
- YouTube
- TikTok
- Slack
- Zendesk
- Salesforce
- HubSpot
- Jira
- Notion
- Microsoft Teams

Subscription lifecycle management shall therefore coordinate billing state with:

```text
Authentication
Authorization
Tenant Management
Entitlement Management
Usage Tracking
AI Gateway
Agent Runtime
Workflow Engine
Integration Platform
Lead Intelligence
RAG
Billing
Payment Processing
Invoice Management
Tax Management
Credit Management
Coupon Management
Analytics
Notifications
Audit
```

---

## 3. Actors

## 3.1 Human Actors

### H-01 End User

A customer using SalesGenie under an active subscription.

### H-02 Organization Admin

Responsible for managing the organization's subscription.

### H-03 Billing Admin

Authorized to manage billing and subscription operations.

### H-04 Sales Agent

Assists customers with subscription selection and upgrades.

### H-05 Customer Success Manager

Assists customers with retention, downgrade, cancellation, and reactivation.

### H-06 Finance Admin

Manages billing, invoices, refunds, credits, and financial reconciliation.

### H-07 Super Admin

Platform-level operator responsible for subscription operations and exceptional interventions.

---

## 3.2 AI Actors

### AI-01 AI Sales Agent

Recommends plans and assists customers with upgrades.

### AI-02 AI Support Agent

Explains subscription status, limits, invoices, and lifecycle events.

### AI-03 AI Billing Assistant

Provides billing information and guides authorized users through subscription operations.

### AI-04 AI Usage Advisor

Analyzes usage and recommends plan changes.

### AI-05 AI Retention Agent

Identifies cancellation risk and recommends retention actions.

### AI-06 AI Dunning Agent

Assists with payment recovery workflows.

### AI-07 AI Revenue Optimization Agent

Analyzes subscription patterns and recommends business actions.

### AI-08 AI Entitlement Agent

Validates whether requested functionality is permitted under the current subscription.

### AI-09 AI Operations Agent

Assists authorized administrators with subscription operations.

---

## 4. Core Subscription Lifecycle

The canonical lifecycle shall support:

```text
NONE
  |
  v
PENDING
  |
  v
ACTIVE
  |
  +--------------------+
  |                    |
  v                    v
PAST_DUE             PAUSED
  |                    |
  v                    v
GRACE_PERIOD         ACTIVE
  |
  +----> ACTIVE
  |
  +----> CANCELED
  |
  v
CANCELED
  |
  +----> REACTIVATED
  |
  v
EXPIRED
```

Additional transient states:

```text
UPGRADE_PENDING
DOWNGRADE_PENDING
CANCELLATION_PENDING
RENEWAL_PENDING
PAYMENT_PENDING
PAYMENT_FAILED
MIGRATION_PENDING
RECONCILIATION_REQUIRED
```

---

## 5. Subscription State Machine

## 5.1 PENDING

Subscription record exists but activation requirements are incomplete.

## 5.2 ACTIVE

Subscription is valid and entitlements are available.

## 5.3 UPGRADE_PENDING

Customer has requested an upgrade but the change is not yet finalized.

## 5.4 DOWNGRADE_PENDING

Customer has requested a downgrade that will take effect according to policy.

## 5.5 PAST_DUE

Payment is overdue.

## 5.6 GRACE_PERIOD

Subscription remains partially or fully available while payment recovery is attempted.

## 5.7 PAUSED

Subscription billing and/or service access is paused according to policy.

## 5.8 CANCELLATION_PENDING

Cancellation has been requested but has not yet reached its effective date.

## 5.9 CANCELED

Subscription is canceled.

## 5.10 EXPIRED

Subscription has ended and is no longer active.

## 5.11 REACTIVATED

Previously canceled or paused subscription has returned to an active state.

---

## 6. User Requirements

## UR-001 — Subscription Visibility

Users shall be able to view:

* Current plan
* Subscription status
* Billing interval
* Start date
* Current billing period
* Next billing date
* Renewal date
* Cancellation date
* Trial status
* Payment status
* Usage
* Quotas
* Feature entitlements
* Credits
* Outstanding invoices

---

## UR-002 — Subscription Purchase

Authorized users shall be able to subscribe to an available SalesGenie plan.

---

## UR-003 — Plan Selection

Users shall be able to select:

* Free
* Monthly
* Yearly
* Usage-based
* Metered
* Hybrid
* Enterprise/custom

according to eligibility and availability.

---

## UR-004 — Subscription Activation

Users shall receive access to entitled functionality after successful subscription activation.

---

## UR-005 — Upgrade

Authorized users shall be able to upgrade their subscription.

---

## UR-006 — Downgrade

Authorized users shall be able to request a downgrade.

The system shall clearly communicate:

* Effective date
* Feature changes
* Limit changes
* Billing impact
* Data impact
* Credit impact

---

## UR-007 — Cancellation

Authorized users shall be able to cancel their subscription.

The system shall support:

* Immediate cancellation
* End-of-period cancellation

according to policy.

---

## UR-008 — Reactivation

Users shall be able to reactivate eligible canceled or paused subscriptions.

---

## UR-009 — Pause

Authorized users shall be able to pause subscriptions when supported by the plan.

---

## UR-010 — Resume

Authorized users shall be able to resume paused subscriptions.

---

## UR-011 — Payment Recovery

Users shall be able to recover subscriptions after payment failures.

---

## UR-012 — Billing Transparency

Users shall be able to understand:

* Subscription price
* Taxes
* Discounts
* Credits
* Usage charges
* Upcoming invoice amount
* Renewal amount

---

## UR-013 — Subscription Notifications

Users shall receive notifications for important lifecycle events.

---

## UR-014 — Data Preservation

Cancellation shall not silently delete customer data.

---

## 7. AI User Requirements

## AI-UR-001 — Subscription Status Assistant

AI shall answer authorized questions about:

* Current plan
* Subscription status
* Renewal date
* Usage
* Limits
* Billing state
* Available upgrades

---

## AI-UR-002 — Plan Recommendation

AI may recommend a plan based on:

* Historical usage
* Current usage
* Feature requirements
* Number of users
* AI-agent count
* Workflow volume
* Integration usage
* Lead-generation requirements

Recommendations shall be explainable.

---

## AI-UR-003 — Upgrade Assistance

AI shall guide users through:

```text
Current Plan
      |
      v
Usage Analysis
      |
      v
Recommended Plan
      |
      v
Pricing Preview
      |
      v
User Confirmation
      |
      v
Upgrade
```

---

## AI-UR-004 — Downgrade Analysis

Before downgrade, AI may identify:

* Features that will be lost
* Quotas that will decrease
* Users exceeding limits
* AI agents exceeding limits
* Workflows exceeding limits
* Storage exceeding limits
* Integrations becoming unavailable

---

## AI-UR-005 — Cancellation Assistance

AI may identify reasons for cancellation and provide relevant retention options.

AI shall not obstruct legitimate cancellation.

---

## AI-UR-006 — Retention Recommendation

AI may recommend:

* Lower plan
* Temporary pause
* Credit
* Coupon
* Support intervention
* Configuration optimization

Financial incentives shall require explicit authorization.

---

## AI-UR-007 — Payment Recovery

AI may guide customers through:

* Payment-method update
* Invoice review
* Retry
* Billing contact update
* Human escalation

---

## AI-UR-008 — AI Subscription Actions

AI shall not independently perform high-impact subscription actions unless explicitly authorized.

Default policy:

```text
READ       = Allowed
ANALYZE    = Allowed
RECOMMEND  = Allowed
PREVIEW    = Allowed
REQUEST    = Policy-dependent
EXECUTE    = Explicit delegation required
APPROVE    = Human/admin by default
```

---

## 8. System Requirements

## SR-001 — Subscription Service

SalesGenie shall maintain a dedicated authoritative subscription-management service.

---

## SR-002 — Multi-Tenant Isolation

Every subscription shall be associated with:

```text
tenant_id
organization_id
subscription_id
```

---

## SR-003 — Subscription Uniqueness

The system shall prevent unauthorized duplicate active subscriptions for the same tenant and billing scope.

---

## SR-004 — State Machine Enforcement

Subscription transitions shall be validated against an explicit state machine.

Invalid transitions shall be rejected.

---

## SR-005 — Versioning

Subscriptions shall maintain optimistic-locking/version information.

---

## SR-006 — Idempotency

Subscription lifecycle APIs shall support idempotency keys.

---

## SR-007 — Event-Driven Architecture

Lifecycle changes shall publish domain events.

---

## SR-008 — Entitlement Integration

Subscription state shall drive feature entitlements.

---

## SR-009 — Billing Integration

Subscription state shall integrate with:

* Pricing Engine
* Payment Gateway
* Invoice Management
* Tax Management
* Coupon Management
* Credit Management
* Usage Tracking

---

## SR-010 — Usage Integration

Metered and usage-based subscriptions shall integrate with authoritative usage records.

---

## SR-011 — Webhook Processing

Payment-provider and external billing events shall be processed asynchronously.

---

## SR-012 — Webhook Idempotency

Duplicate webhook events shall not produce duplicate state transitions.

---

## SR-013 — Reconciliation

The system shall periodically reconcile:

```text
Subscription
Payment Provider
Invoice
Payment
Usage
Entitlement
```

---

## SR-014 — Auditability

Every material subscription lifecycle change shall be auditable.

---

## 9. Functional Requirements

## 9.1 Subscription Creation

## FR-CREATE-001

The system shall create a subscription only after validating:

* Tenant
* User authorization
* Plan
* Pricing
* Billing interval
* Payment requirements
* Eligibility
* Trial state
* Existing subscription state

---

## FR-CREATE-002

Subscription creation shall be idempotent.

---

## FR-CREATE-003

Subscription creation shall generate:

```text
subscription_id
tenant_id
plan_id
billing_interval
status
start_at
current_period_start
current_period_end
next_billing_at
created_at
version
```

---

## 9.2 Subscription Activation

## FR-ACT-001

The system shall activate a subscription after successful completion of required billing operations.

---

## FR-ACT-002

Activation shall trigger entitlement provisioning.

---

## FR-ACT-003

Activation shall publish:

```text
subscription.activated
```

---

## 9.3 Subscription Renewal

## FR-RENEW-001

The system shall support recurring subscription renewal.

---

## FR-RENEW-002

Renewal shall calculate:

```text
Base Price
+
Usage Charges
+
Taxes
-
Coupons
-
Credits
=
Final Amount
```

---

## FR-RENEW-003

Successful renewal shall:

* Create/update invoice
* Process payment
* Advance billing period
* Reset applicable quotas
* Update usage periods
* Preserve entitlements
* Publish renewal event

---

## 9.4 Renewal Failure

## FR-RENEW-004

If renewal payment fails:

```text
ACTIVE
   |
   v
PAST_DUE
   |
   v
GRACE_PERIOD
   |
   +----> PAYMENT_RECOVERED
   |
   v
CANCELED / EXPIRED
```

---

## 9.5 Upgrade

## FR-UPGRADE-001

The system shall support subscription upgrades.

---

## FR-UPGRADE-002

Upgrade shall calculate applicable:

* Price difference
* Proration
* Taxes
* Credits
* Discounts
* Usage charges

---

## FR-UPGRADE-003

The system shall provide a preview before applying an upgrade.

---

## FR-UPGRADE-004

Upgrade shall require explicit confirmation unless an authorized automated policy exists.

---

## FR-UPGRADE-005

Successful upgrade shall update:

* Plan
* Entitlements
* Limits
* Billing
* Usage policy
* Subscription metadata

---

## FR-UPGRADE-006

Upgrade shall publish:

```text
subscription.upgrade.requested
subscription.upgraded
```

---

## 9.6 Downgrade

## FR-DOWNGRADE-001

The system shall support subscription downgrades according to plan policy.

---

## FR-DOWNGRADE-002

The system shall preview the consequences before downgrade.

---

## FR-DOWNGRADE-003

The preview shall identify:

```text
Features Removed
Quota Reductions
Seat Reductions
AI-Agent Reductions
Workflow Reductions
Storage Reductions
Integration Restrictions
Billing Changes
```

---

## FR-DOWNGRADE-004

The system shall support effective-immediately and end-of-period downgrade policies where configured.

---

## FR-DOWNGRADE-005

Downgrade shall not silently destroy data.

---

## 9.7 Cancellation

## FR-CANCEL-001

Authorized users shall be able to request cancellation.

---

## FR-CANCEL-002

The system shall support:

```text
cancel_immediately
cancel_at_period_end
```

---

## FR-CANCEL-003

Cancellation shall require explicit confirmation.

---

## FR-CANCEL-004

The system shall record:

```text
canceled_by
cancellation_reason
cancellation_source
requested_at
effective_at
```

---

## FR-CANCEL-005

Cancellation shall publish:

```text
subscription.cancellation_requested
subscription.canceled
```

---

## 9.8 Reactivation

## FR-REACT-001

Eligible canceled subscriptions shall be reactivatable.

---

## FR-REACT-002

Reactivation shall validate:

* Account status
* Plan availability
* Payment method
* Billing status
* Eligibility
* Outstanding invoices

---

## FR-REACT-003

Reactivation shall be idempotent.

---

## 9.9 Pause

## FR-PAUSE-001

The system shall support subscription pause where plan policy permits.

---

## FR-PAUSE-002

Pause shall define:

* Billing behavior
* Service access
* Usage behavior
* Quota behavior
* Maximum pause duration
* Resume conditions

---

## 9.10 Resume

## FR-RESUME-001

Authorized users shall be able to resume paused subscriptions.

---

## FR-RESUME-002

Resume shall re-evaluate:

* Plan
* Price
* Entitlements
* Payment method
* Outstanding balance
* Usage limits

---

## 9.11 Grace Period

## FR-GRACE-001

The system shall support configurable grace periods after failed payment.

---

## FR-GRACE-002

Grace-period access shall be policy-driven.

Possible states:

```text
FULL_ACCESS
LIMITED_ACCESS
READ_ONLY
AI_DISABLED
INTEGRATIONS_DISABLED
COMPLETELY_BLOCKED
```

---

## 9.12 Dunning

## FR-DUNNING-001

The system shall support automated payment-recovery workflows.

---

## FR-DUNNING-002

Dunning shall support configurable retry schedules.

Example:

```text
Attempt 1
    |
Attempt 2
    |
Attempt 3
    |
Attempt 4
    |
Final Notice
    |
Subscription Restriction
```

---

## FR-DUNNING-003

Dunning shall avoid duplicate notifications.

---

## 9.13 Entitlement Management

## FR-ENT-001

Subscription entitlements shall be derived from:

```text
Plan
+
Subscription State
+
Add-ons
+
Usage
+
Policy
```

---

## FR-ENT-002

Entitlements shall support:

* AI agents
* Human seats
* Conversations
* Leads
* Workflows
* Storage
* RAG documents
* API calls
* Integrations
* Communication channels
* MCP tools
* Analytics
* Advanced security

---

## FR-ENT-003

Expired or canceled subscriptions shall have entitlements recalculated.

---

## FR-ENT-004

Entitlement changes shall be propagated to dependent services.

---

## 9.14 Usage-Based Subscription

## FR-USAGE-001

The system shall support usage-based billing.

---

## FR-USAGE-002

Supported meters may include:

```text
AI Tokens
AI Requests
Conversations
Leads
Workflow Executions
API Calls
Storage
RAG Processing
Voice Minutes
Messages
Integration Operations
```

---

## FR-USAGE-003

Usage events shall be immutable.

---

## FR-USAGE-004

Usage calculations shall be reproducible.

---

## FR-USAGE-005

Duplicate usage events shall not create duplicate charges.

---

## 9.15 Metered Billing

## FR-METER-001

Meters shall support configurable units.

---

## FR-METER-002

The system shall support:

* Included quantity
* Overage
* Tiered pricing
* Volume pricing
* Graduated pricing
* Flat fee + usage
* Usage-only pricing

---

## 9.16 Credits

## FR-CREDIT-001

Subscription lifecycle operations shall integrate with customer credits.

---

## FR-CREDIT-002

Credit usage shall be auditable.

---

## FR-CREDIT-003

Credit application shall be deterministic.

---

## 9.17 Coupons

## FR-COUPON-001

The system shall support subscription-specific coupons.

---

## FR-COUPON-002

Coupons shall support:

* Percentage discount
* Fixed discount
* Duration
* Plan restrictions
* Customer restrictions
* Usage limits
* Expiration

---

## 9.18 Taxes

## FR-TAX-001

Subscription billing shall calculate applicable taxes using the configured tax system.

---

## FR-TAX-002

Tax calculation shall be preserved on the resulting invoice.

---

## 9.19 Invoices

## FR-INVOICE-001

Each recurring billing event shall generate or update an invoice according to billing policy.

---

## FR-INVOICE-002

Invoices shall include:

```text
Subscription
Billing Period
Plan
Usage
Discounts
Credits
Taxes
Total
Payment Status
```

---

## 9.20 Payment Processing

## FR-PAY-001

The subscription system shall integrate with the payment gateway.

---

## FR-PAY-002

Payment state shall be synchronized asynchronously.

---

## FR-PAY-003

The subscription service shall not assume payment success solely from a client response.

---

## 10. Subscription Lifecycle Events

The platform shall publish:

```text
subscription.created
subscription.pending
subscription.activated
subscription.renewal.started
subscription.renewed
subscription.renewal.failed
subscription.payment_failed
subscription.past_due
subscription.grace_period.started
subscription.upgrade.requested
subscription.upgraded
subscription.downgrade.requested
subscription.downgraded
subscription.pause.requested
subscription.paused
subscription.resume.requested
subscription.resumed
subscription.cancellation.requested
subscription.canceled
subscription.expiring
subscription.expired
subscription.reactivation.requested
subscription.reactivated
subscription.entitlements.changed
subscription.plan.changed
subscription.reconciliation.required
```

---

## 11. Event-Driven Architecture

```text
Subscription Service
        |
        +----> Billing Service
        |
        +----> Payment Service
        |
        +----> Invoice Service
        |
        +----> Tax Service
        |
        +----> Usage Service
        |
        +----> Entitlement Service
        |
        +----> AI Gateway
        |
        +----> Agent Runtime
        |
        +----> Integration Platform
        |
        +----> Notification Service
        |
        +----> Analytics
        |
        +----> Audit Service
```

All consumers shall support:

* Idempotency
* Retry
* Dead-letter queues
* Correlation IDs
* Event versioning
* Tenant context
* Distributed tracing

---

## 12. AI Subscription Workflow

```text
Customer
   |
   v
AI Billing Assistant
   |
   v
Authenticate
   |
   v
Authorize
   |
   v
Retrieve Subscription
   |
   v
Analyze Usage
   |
   v
Generate Recommendation
   |
   v
Preview Change
   |
   v
Human Confirmation
   |
   v
Subscription Service
   |
   v
Billing + Payment
   |
   v
Entitlement Update
```

---

## 13. AI Upgrade Workflow

```text
Usage Data
    |
    v
AI Usage Advisor
    |
    v
Detect Capacity Pressure
    |
    v
Recommend Plan
    |
    v
Explain Recommendation
    |
    v
Generate Price Preview
    |
    v
Customer Confirmation
    |
    v
Upgrade
```

---

## 14. AI Downgrade Workflow

```text
Downgrade Request
       |
       v
AI Impact Analyzer
       |
       +----> Feature Impact
       +----> User Impact
       +----> AI Agent Impact
       +----> Workflow Impact
       +----> Storage Impact
       +----> Integration Impact
       |
       v
Customer Confirmation
       |
       v
Downgrade Service
```

---

## 15. AI Cancellation Workflow

```text
Cancellation Request
        |
        v
AI Cancellation Assistant
        |
        v
Collect Reason
        |
        v
Analyze Risk
        |
        v
Offer Optional Alternatives
        |
        +----> Downgrade
        +----> Pause
        +----> Support
        +----> Coupon
        |
        v
Customer Decision
        |
        v
Cancellation
```

AI shall never intentionally create friction that prevents a customer from canceling.

---

## 16. AI Dunning Workflow

```text
Payment Failed
      |
      v
AI Dunning Agent
      |
      +----> Notify Customer
      |
      +----> Explain Failure
      |
      +----> Provide Payment Recovery
      |
      +----> Recommend Human Support
      |
      v
Payment Retry
      |
      +----> Success
      |
      +----> Failure
```

AI shall not invent payment statuses or financial amounts.

---

## 17. Human Subscription Administration

Authorized administrators shall be able to:

* View subscriptions
* Search subscriptions
* Filter by status
* View billing history
* View usage
* View invoices
* View payments
* Upgrade plans
* Schedule downgrades
* Cancel subscriptions
* Pause subscriptions
* Resume subscriptions
* Reactivate subscriptions
* Initiate approved credits
* Review failed payments
* Review reconciliation failures
* View audit logs

---

## 18. Super Admin Requirements

Super Admins shall be able to:

* Search all tenant subscriptions
* Inspect subscription state
* View lifecycle history
* Review payment failures
* Review entitlement mismatches
* Review reconciliation failures
* Suspend subscriptions
* Resume subscriptions
* Apply authorized exceptions
* Review enterprise subscriptions
* Review custom pricing
* Review subscription abuse
* Trigger controlled reconciliation
* View billing events
* Review audit events

All administrative actions shall be audited.

---

## 19. Enterprise Subscription

Enterprise subscriptions shall support custom:

```text
Pricing
Billing Interval
Seats
AI Agents
Usage Limits
Features
Integrations
Support
SLA
Data Retention
Security
Contract Terms
Payment Terms
```

Enterprise overrides shall require appropriate authorization.

---

## 20. Subscription Data Model

## Subscription

```text
subscription_id
tenant_id
organization_id
customer_id
plan_id
plan_version
billing_interval
status
currency
base_price
start_at
current_period_start
current_period_end
next_billing_at
cancel_at
canceled_at
pause_at
resume_at
trial_id
payment_customer_id
payment_method_id
external_subscription_id
version
metadata
created_at
updated_at
```

---

## 21. Subscription Item

```text
subscription_item_id
subscription_id
product_id
plan_id
quantity
unit_price
billing_model
meter_id
effective_at
expires_at
metadata
```

---

## 22. Subscription Change

```text
change_id
subscription_id
change_type
previous_plan
new_plan
previous_quantity
new_quantity
effective_at
requested_at
requested_by
approved_by
reason
status
created_at
```

---

## 23. Billing Period

```text
billing_period_id
subscription_id
period_start
period_end
billing_interval
usage_snapshot_id
invoice_id
status
created_at
```

---

## 24. Lifecycle Audit Record

```text
audit_id
subscription_id
tenant_id
actor_id
actor_type
action
previous_state
new_state
reason
source
request_id
correlation_id
timestamp
result
metadata
```

---

## 25. API Requirements

## API-001 — Current Subscription

```http
GET /api/v1/subscriptions/current
```

## API-002 — Create Subscription

```http
POST /api/v1/subscriptions
```

## API-003 — Subscription Details

```http
GET /api/v1/subscriptions/{subscription_id}
```

## API-004 — Upgrade Preview

```http
POST /api/v1/subscriptions/{subscription_id}/upgrade/preview
```

## API-005 — Upgrade

```http
POST /api/v1/subscriptions/{subscription_id}/upgrade
```

## API-006 — Downgrade Preview

```http
POST /api/v1/subscriptions/{subscription_id}/downgrade/preview
```

## API-007 — Downgrade

```http
POST /api/v1/subscriptions/{subscription_id}/downgrade
```

## API-008 — Cancel

```http
POST /api/v1/subscriptions/{subscription_id}/cancel
```

## API-009 — Reactivate

```http
POST /api/v1/subscriptions/{subscription_id}/reactivate
```

## API-010 — Pause

```http
POST /api/v1/subscriptions/{subscription_id}/pause
```

## API-011 — Resume

```http
POST /api/v1/subscriptions/{subscription_id}/resume
```

## API-012 — Usage

```http
GET /api/v1/subscriptions/{subscription_id}/usage
```

## API-013 — Entitlements

```http
GET /api/v1/subscriptions/{subscription_id}/entitlements
```

## API-014 — Lifecycle History

```http
GET /api/v1/subscriptions/{subscription_id}/lifecycle
```

---

## 26. AI Tool Requirements

AI agents may access tools such as:

```text
get_subscription
get_subscription_status
get_billing_period
get_subscription_usage
get_subscription_entitlements
get_available_plans
compare_plans
preview_upgrade
preview_downgrade
preview_cancellation
get_invoice
get_payment_status
get_payment_failure
get_credit_balance
get_coupon_eligibility
request_upgrade
request_downgrade
request_cancellation
request_pause
request_reactivation
```

Every tool shall enforce backend authorization.

---

## 27. AI Financial Safety

AI shall not:

* Invent prices
* Invent invoices
* Invent payment status
* Modify financial records without authorization
* Apply unauthorized discounts
* Create unauthorized credits
* Bypass payment requirements
* Modify tax records
* Change subscription state without authorization
* Suppress billing events
* Delete financial history

---

## 28. Entitlement Enforcement

Every protected SalesGenie operation shall perform:

```text
Authenticate
    |
    v
Authorize
    |
    v
Resolve Tenant
    |
    v
Resolve Subscription
    |
    v
Resolve Entitlement
    |
    v
Check Quota
    |
    v
Check Usage
    |
    v
Allow / Deny
```

Frontend visibility shall never be considered authorization.

---

## 29. Subscription Expiration

When a subscription expires:

1. Validate state.
2. Acquire lifecycle lock.
3. Mark subscription expired.
4. Recalculate entitlements.
5. Restrict paid functionality.
6. Preserve customer data.
7. Publish expiration event.
8. Notify users.
9. Record audit event.
10. Initiate retention policy if applicable.

---

## 30. Data Preservation

Cancellation or expiration shall not automatically delete:

* Conversations
* Leads
* Contacts
* Knowledge bases
* Documents
* Workflows
* AI-agent configurations
* Integration configuration
* Audit records
* Usage records
* Invoices
* Payment records

Deletion shall follow independent data-retention policies.

---

## 31. Reconciliation

The system shall periodically reconcile:

```text
Internal Subscription
        |
        +---- Payment Provider
        |
        +---- Invoice
        |
        +---- Payment
        |
        +---- Usage
        |
        +---- Entitlement
```

Mismatches shall create:

```text
subscription.reconciliation.required
```

---

## 32. Reconciliation Examples

The system shall detect:

* Payment succeeded but subscription remains pending.
* Subscription active but payment failed.
* Payment provider canceled subscription but SalesGenie remains active.
* Internal invoice differs from provider invoice.
* Usage differs from billing usage.
* Entitlements differ from subscription plan.
* Duplicate subscription exists.
* Duplicate payment exists.
* Duplicate webhook was processed.

---

## 33. Idempotency

The following operations shall be idempotent:

```text
Create Subscription
Activate Subscription
Renew Subscription
Upgrade
Downgrade
Cancel
Pause
Resume
Reactivate
Payment Webhook
Subscription Webhook
Usage Ingestion
Invoice Creation
Entitlement Update
```

---

## 34. Concurrency Control

The system shall protect against concurrent:

```text
Upgrade
Downgrade
Cancellation
Renewal
Reactivation
Pause
Resume
Payment Processing
Entitlement Updates
```

Mechanisms may include:

* Optimistic locking
* Database transactions
* Distributed locks
* Idempotency keys
* Version numbers

---

## 35. Error Codes

The platform shall support structured errors:

```text
SUBSCRIPTION_NOT_FOUND
SUBSCRIPTION_ALREADY_ACTIVE
SUBSCRIPTION_ALREADY_CANCELED
SUBSCRIPTION_EXPIRED
SUBSCRIPTION_PAUSED
INVALID_STATE_TRANSITION
PLAN_NOT_FOUND
PLAN_NOT_AVAILABLE
PLAN_CHANGE_NOT_ALLOWED
UPGRADE_NOT_ALLOWED
DOWNGRADE_NOT_ALLOWED
CANCELLATION_NOT_ALLOWED
REACTIVATION_NOT_ALLOWED
PAYMENT_REQUIRED
PAYMENT_FAILED
PAYMENT_METHOD_INVALID
INVOICE_FAILED
TAX_CALCULATION_FAILED
COUPON_INVALID
CREDIT_INSUFFICIENT
QUOTA_EXCEEDED
USAGE_DATA_UNAVAILABLE
ENTITLEMENT_SYNC_FAILED
RECONCILIATION_REQUIRED
DUPLICATE_REQUEST
RATE_LIMITED
AUTHORIZATION_FAILED
```

---

## 36. Notification Requirements

The system shall notify users about:

```text
Subscription Created
Subscription Activated
Payment Upcoming
Renewal Upcoming
Renewal Successful
Renewal Failed
Payment Failed
Grace Period Started
Upgrade Completed
Downgrade Scheduled
Downgrade Completed
Cancellation Requested
Cancellation Completed
Subscription Expiring
Subscription Expired
Subscription Reactivated
Subscription Paused
Subscription Resumed
Quota Approaching
Quota Exhausted
```

Supported channels may include:

* Email
* In-app
* Slack
* Microsoft Teams
* SMS where supported
* AI assistant

---

## 37. Subscription Analytics

The platform shall track:

```text
New Subscriptions
Active Subscriptions
MRR
ARR
ARPU
Upgrade Rate
Downgrade Rate
Cancellation Rate
Churn Rate
Renewal Rate
Payment Failure Rate
Recovery Rate
Reactivation Rate
Pause Rate
Trial Conversion Rate
Plan Distribution
Usage Distribution
Expansion Revenue
Contraction Revenue
Net Revenue Retention
Gross Revenue Retention
```

---

## 38. AI Subscription Analytics

AI may analyze:

* Churn probability
* Upgrade probability
* Downgrade probability
* Payment failure risk
* Feature adoption
* Usage anomalies
* Expansion opportunities
* Customer health

AI predictions shall remain advisory unless an explicit automation policy authorizes an action.

---

## 39. Security Requirements

## SEC-001

All subscription APIs shall require authentication.

## SEC-002

Authorization shall be enforced server-side.

## SEC-003

Tenant isolation shall be mandatory.

## SEC-004

Subscription IDs shall not grant authorization.

## SEC-005

Sensitive billing data shall be protected.

## SEC-006

Payment credentials shall not be stored unless required and appropriately secured.

## SEC-007

AI tools shall inherit or explicitly validate authorization context.

## SEC-008

Subscription lifecycle operations shall be rate-limited.

## SEC-009

Administrative overrides shall require elevated privileges.

## SEC-010

Financial lifecycle events shall be immutable/auditable.

---

## 40. Observability

The platform shall provide:

## Metrics

```text
subscription_creation_success_rate
subscription_activation_latency
upgrade_success_rate
downgrade_success_rate
renewal_success_rate
payment_failure_rate
payment_recovery_rate
cancellation_rate
reactivation_rate
entitlement_sync_failure_rate
reconciliation_failure_rate
```

## Logs

Logs shall include:

```text
tenant_id
subscription_id
request_id
correlation_id
actor_id
operation
result
latency
error_code
```

Sensitive payment information shall not be logged.

## Tracing

Distributed traces shall cover:

```text
Frontend
API Gateway
Subscription Service
Billing Service
Payment Service
Invoice Service
Usage Service
Entitlement Service
Notification Service
```

---

## 41. Reliability Requirements

The subscription platform shall tolerate:

* Payment-provider outages
* Webhook delays
* Duplicate webhooks
* Out-of-order webhooks
* Database failures
* Queue failures
* Worker crashes
* Network failures
* Duplicate requests
* Concurrent lifecycle operations
* Delayed usage events
* Entitlement-service failures

---

## 42. Disaster Recovery

The system shall support:

* Durable subscription records
* Durable lifecycle events
* Backup and restore
* Event replay
* Entitlement reconciliation
* Billing reconciliation
* Payment reconciliation
* Recovery after worker failure

Financial and subscription records shall not depend solely on ephemeral caches.

---

## 43. Subscription Lifecycle Workflow

```text
Customer
   |
   v
Plan Selection
   |
   v
Pricing Engine
   |
   v
Coupon / Credit
   |
   v
Tax Calculation
   |
   v
Payment Gateway
   |
   v
Subscription Created
   |
   v
Subscription Activated
   |
   v
Entitlements Provisioned
   |
   v
Usage Tracking
   |
   +------------------------------+
   |                              |
   v                              v
Renewal                        Plan Change
   |                              |
   v                              v
Payment                        Upgrade/Downgrade
   |                              |
   v                              v
Renewed                       Entitlement Update
   |
   +----> Payment Failure
              |
              v
          Dunning
              |
              v
          Grace Period
              |
        +-----+-----+
        |           |
        v           v
    Recovered    Expired
        |           |
        v           v
      Active     Canceled
```

---

## 44. Subscription Lifecycle Invariants

The system shall enforce:

```text
1. A subscription cannot be ACTIVE without valid authorization.
2. A subscription cannot be ACTIVE without valid entitlement state.
3. A canceled subscription cannot silently become active.
4. A payment failure cannot be treated as payment success.
5. Duplicate webhook events cannot create duplicate state transitions.
6. Duplicate subscription requests cannot create duplicate subscriptions.
7. AI cannot bypass lifecycle authorization.
8. Subscription state must be server-authoritative.
9. Usage must be attributable to a subscription or defined billing scope.
10. Entitlements must correspond to the effective subscription state.
11. Financial records must remain auditable.
12. Lifecycle transitions must be deterministic.
```

---

## 45. Edge Cases

The system shall handle:

1. User subscribes twice simultaneously.
2. Payment succeeds but webhook is delayed.
3. Payment webhook arrives twice.
4. Payment webhook arrives out of order.
5. Subscription expires during upgrade.
6. Upgrade occurs during renewal.
7. Downgrade occurs during payment failure.
8. Cancellation occurs during upgrade.
9. Reactivation occurs while cancellation is processing.
10. Payment method expires during renewal.
11. Coupon expires before renewal.
12. Credit balance changes during invoice creation.
13. Tax service becomes unavailable.
14. Usage events arrive late.
15. Usage events arrive duplicated.
16. Entitlement service becomes unavailable.
17. Customer exceeds new downgrade limits.
18. Customer has more seats than the downgraded plan permits.
19. Customer has more AI agents than the downgraded plan permits.
20. Customer has storage exceeding downgraded limits.
21. Customer has integrations unavailable under the new plan.
22. Subscription is manually modified by Super Admin.
23. External billing provider reports an unexpected state.
24. Customer changes billing interval.
25. Subscription is paused near renewal.
26. Subscription is reactivated after a long cancellation period.
27. Customer converts from trial to paid during expiration processing.
28. Payment succeeds after subscription was marked expired.
29. Invoice creation succeeds but payment fails.
30. Payment succeeds but invoice creation fails.

---

## 46. Acceptance Criteria

## AC-001

Authorized users can create a valid subscription.

## AC-002

Unauthorized users cannot modify subscriptions.

## AC-003

Subscription state is authoritative on the backend.

## AC-004

Duplicate subscription creation requests do not create duplicate subscriptions.

## AC-005

Subscription lifecycle transitions follow the state machine.

## AC-006

Upgrades produce accurate billing previews.

## AC-007

Downgrades clearly communicate feature and quota impacts.

## AC-008

Cancellation works without artificial obstruction.

## AC-009

Pause and resume operate according to configured policy.

## AC-010

Failed payments trigger dunning and grace-period workflows.

## AC-011

Successful payment recovery restores appropriate access.

## AC-012

Expired subscriptions cannot access restricted paid features.

## AC-013

Subscription entitlements remain synchronized with subscription state.

## AC-014

Usage-based charges are calculated from authoritative usage events.

## AC-015

Duplicate usage events do not cause duplicate charges.

## AC-016

Duplicate payment-provider webhooks do not corrupt subscription state.

## AC-017

Out-of-order webhooks are handled safely.

## AC-018

Subscription conversion from trial is idempotent.

## AC-019

Cancellation does not silently delete customer data.

## AC-020

Reactivation requires appropriate authorization.

## AC-021

AI agents cannot independently bypass subscription authorization.

## AC-022

AI recommendations are explainable.

## AC-023

All financial lifecycle changes are auditable.

## AC-024

Reconciliation detects inconsistencies between SalesGenie and external billing providers.

## AC-025

Subscription state can be recovered after service failure.

---

## 47. FAANG-Level Quality Gates

The implementation shall not be considered production-ready unless:

```text
[ ] Explicit subscription state machine
[ ] Multi-tenant isolation
[ ] Server-authoritative subscription state
[ ] Idempotent subscription creation
[ ] Idempotent lifecycle operations
[ ] Optimistic locking / concurrency control
[ ] Upgrade support
[ ] Downgrade support
[ ] Pause/resume support
[ ] Cancellation support
[ ] Reactivation support
[ ] Trial conversion support
[ ] Monthly billing
[ ] Yearly billing
[ ] Usage-based billing
[ ] Metered billing
[ ] Hybrid billing
[ ] Proration
[ ] Coupons
[ ] Credits
[ ] Tax calculation
[ ] Invoice integration
[ ] Payment gateway integration
[ ] Payment failure handling
[ ] Dunning
[ ] Grace period
[ ] Webhook idempotency
[ ] Out-of-order event handling
[ ] Event replay
[ ] Entitlement synchronization
[ ] Usage reconciliation
[ ] Billing reconciliation
[ ] Subscription reconciliation
[ ] AI authorization boundaries
[ ] Human approval workflows
[ ] Abuse prevention
[ ] Audit logging
[ ] Distributed tracing
[ ] Structured metrics
[ ] Structured errors
[ ] Disaster recovery
[ ] Data preservation
[ ] Security testing
[ ] Load testing
[ ] Failure testing
[ ] Financial reconciliation testing
[ ] AI safety testing
```

---

## 48. Definition of Done

`subscription_lifecycle.md` shall be considered fully implemented when SalesGenie can reliably execute:

```text
PLAN SELECTION
      |
      v
PRICING
      |
      v
PAYMENT
      |
      v
SUBSCRIPTION CREATION
      |
      v
ACTIVATION
      |
      v
ENTITLEMENT PROVISIONING
      |
      v
USAGE TRACKING
      |
      +-------------------------------+
      |                               |
      v                               v
RENEWAL                         PLAN CHANGE
      |                               |
      v                               +----> UPGRADE
PAYMENT                            |
      |                            +----> DOWNGRADE
      v
RENEWED
      |
      +----> PAYMENT FAILURE
                  |
                  v
               DUNNING
                  |
                  v
             GRACE PERIOD
                  |
             +----+----+
             |         |
             v         v
        RECOVERED    EXPIRED
             |         |
             v         v
           ACTIVE   CANCELED
                       |
                       v
                  REACTIVATION
```

The final SalesGenie implementation shall provide **deterministic subscription state management, secure multi-tenant isolation, reliable billing integration, accurate usage metering, centralized entitlement enforcement, resilient payment recovery, AI-assisted but human-governed lifecycle operations, complete auditability, reconciliation, observability, and production-grade failure recovery across the entire subscription lifecycle**.
