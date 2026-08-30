# SalesGenie — Yearly Subscription

## FAANG-Level User Requirements, System Requirements & Functional Requirements

**Document:** `yearly_subscription.md`  
**Product:** SalesGenie — Enterprise AI Customer Support, Sales & Workflow Automation Platform  
**Scope:** Annual subscription lifecycle, annual billing, renewals, upgrades, downgrades, cancellation, proration, credits, refunds, usage, entitlements, invoicing, payment recovery, AI-assisted subscription management, human approvals, auditability, and enterprise administration.

---

## 1. Purpose

SalesGenie SHALL provide a production-grade yearly subscription system that enables organizations and customers to:

- Purchase annual subscription plans.
- Manage annual billing periods.
- Receive annual pricing and configured discounts.
- Upgrade annual plans.
- Downgrade annual plans.
- Cancel annual subscriptions.
- Renew subscriptions automatically.
- Manage payment methods.
- View annual invoices and receipts.
- Track annual and billing-period usage.
- Consume plan-based AI, workflow, integration, communication, storage, API, and seat entitlements.
- Support AI-assisted subscription management.
- Require human approval for high-risk financial operations.
- Handle payment failures and recovery.
- Support annual-plan-specific proration and credit calculations.
- Maintain immutable financial records.
- Provide Super Admins with complete subscription visibility.
- Maintain strict tenant isolation and authorization.

---

## 2. Product Principles

The yearly subscription system SHALL follow:

1. Financial correctness
2. Deterministic billing
3. Idempotent operations
4. Immutable financial history
5. Explicit entitlement enforcement
6. Multi-tenant isolation
7. Least-privilege authorization
8. Human-in-the-loop financial controls
9. AI safety and bounded autonomy
10. Event-driven architecture
11. High observability
12. Fault tolerance
13. Reconciliation
14. Auditability
15. Secure payment processing
16. Backward-compatible plan versioning
17. Transparent customer billing

---

## 3. Actors

| Actor | Responsibility |
|---|---|
| End User | Purchase and view eligible subscription |
| Organization Owner | Own and manage organization subscription |
| Customer Admin | Manage subscription according to permissions |
| Sales Agent | Recommend appropriate annual plans |
| Support Agent | Assist customers with subscription issues |
| Finance/Billing Admin | Handle billing operations and financial exceptions |
| Super Admin | Manage and monitor platform-wide subscriptions |
| AI Subscription Agent | Answer questions and recommend subscription actions |
| Workflow Engine | Automate approved subscription workflows |
| Subscription Service | Authoritative subscription lifecycle |
| Billing Service | Financial calculations and billing records |
| Payment Provider | Payment processing |
| Entitlement Service | Feature and quota enforcement |
| Usage Metering Service | Track resource consumption |
| Notification Service | Billing and subscription notifications |
| Audit Service | Immutable audit trail |

---

## 4. USER REQUIREMENTS

## UR-YEARLY-001 — View Annual Plans

Users SHALL be able to view available annual subscription plans.

Each plan SHALL display:

- Plan name
- Annual price
- Equivalent monthly price
- Currency
- Billing interval
- Annual discount where applicable
- Included users/seats
- AI usage
- Workflow executions
- Conversations
- Lead-generation capacity
- API usage
- Storage
- Integrations
- Voice usage
- Knowledge-base capacity
- Feature availability
- Overage pricing
- Trial eligibility
- Renewal terms
- Cancellation policy

---

## UR-YEARLY-002 — Compare Annual Plans

Users SHALL be able to compare annual plans.

Comparison SHALL clearly show:

- Annual price
- Effective monthly price
- Annual savings
- Included usage
- Feature differences
- Seat limits
- AI limits
- Workflow limits
- Integration limits
- Storage limits
- Support levels
- Overage rules

---

## UR-YEARLY-003 — Purchase Annual Subscription

Authorized users SHALL be able to purchase an annual plan.

The flow SHALL support:

1. Plan selection
2. Eligibility validation
3. Billing information
4. Tax information
5. Payment method
6. Coupon/discount
7. Price calculation
8. Annual savings calculation
9. Terms acceptance
10. Payment authorization
11. Subscription creation
12. Entitlement activation
13. Invoice generation
14. Confirmation

---

## UR-YEARLY-004 — Annual Trial Conversion

The system SHALL support trial-to-annual conversion.

Before conversion the platform SHALL:

- Notify the customer.
- Validate payment method.
- Calculate annual price.
- Apply eligible discounts.
- Calculate taxes.
- Process payment.
- Create annual invoice.
- Activate annual entitlements.

---

## UR-YEARLY-005 — View Current Annual Subscription

Authorized users SHALL be able to view:

- Current plan
- Subscription status
- Annual price
- Currency
- Subscription start date
- Current annual period
- Period end date
- Next renewal date
- Payment method
- Usage
- Entitlements
- Discounts
- Taxes
- Outstanding balance
- Cancellation status

---

## UR-YEARLY-006 — View Annual Savings

The platform SHALL show the difference between:

```text
12 × equivalent monthly price
-
annual subscription price
=
annual savings
```

The calculation SHALL be transparent and based on immutable plan pricing.

---

## UR-YEARLY-007 — Upgrade Annual Plan

Authorized users SHALL be able to upgrade to a higher annual plan.

The system SHALL provide a preview containing:

* Current annual plan
* Target annual plan
* Remaining subscription value
* New plan value
* Credit
* Proration
* Tax
* Discount
* Amount due
* Future renewal amount

---

## UR-YEARLY-008 — Downgrade Annual Plan

Authorized users SHALL be able to request a downgrade.

The system SHALL support configurable policies:

* Immediate downgrade
* End-of-period downgrade
* Next-renewal downgrade

If current usage exceeds the target plan's limits, the platform SHALL clearly identify the blocking resources.

---

## UR-YEARLY-009 — Cancel Annual Subscription

Authorized users SHALL be able to cancel an annual subscription.

Cancellation SHALL support:

* Immediate cancellation
* End-of-term cancellation
* Cancellation reason
* Retention offer
* Confirmation
* Refund policy display

---

## UR-YEARLY-010 — Resume Scheduled Cancellation

Users SHALL be able to resume an annual subscription if cancellation is scheduled for the end of the annual period and policy permits.

---

## UR-YEARLY-011 — Manage Payment Methods

Authorized users SHALL be able to:

* Add payment method
* Remove payment method
* Set default method
* Replace expired method
* Update billing details

SalesGenie SHALL NOT expose raw payment credentials.

---

## UR-YEARLY-012 — View Annual Invoice

Customers SHALL be able to view annual invoices containing:

* Invoice number
* Customer
* Organization
* Billing period
* Plan
* Line items
* Discount
* Tax
* Total
* Currency
* Payment status
* Payment date

---

## UR-YEARLY-013 — Download Invoice

Users SHALL be able to download supported invoice formats.

---

## UR-YEARLY-014 — View Billing History

Users SHALL be able to access:

* Annual invoices
* Payments
* Refunds
* Credits
* Adjustments
* Failed payment attempts
* Subscription changes

---

## UR-YEARLY-015 — Annual Usage Dashboard

Users SHALL be able to view usage for:

* Current annual period
* Current month
* Previous months
* Remaining quota
* Percentage consumed
* Projected annual usage

---

## UR-YEARLY-016 — Usage Forecasting

SalesGenie SHALL provide usage forecasts for annual subscribers.

Forecasting MAY consider:

* Historical consumption
* Current consumption
* Seasonal trends
* Workflow activity
* AI usage
* Seat growth
* Integration usage

---

## UR-YEARLY-017 — Annual Renewal Notifications

The system SHALL notify customers before renewal.

Notification timing SHALL be configurable.

Example:

```text
30 days before renewal
14 days before renewal
7 days before renewal
1 day before renewal
Renewal completed
```

---

## UR-YEARLY-018 — Payment Failure Notification

Customers SHALL receive notifications when annual renewal payment fails.

---

## UR-YEARLY-019 — AI Billing Assistant

Customers SHALL be able to ask:

* "What annual plan am I on?"
* "When does my subscription renew?"
* "How much did I save by choosing annual billing?"
* "How much have I used?"
* "Should I upgrade?"
* "What happens if I cancel?"
* "What will my next renewal cost?"

The AI SHALL retrieve authoritative subscription and billing information.

---

## UR-YEARLY-020 — AI Annual Plan Recommendation

The AI SHALL recommend annual plans using:

* Organization size
* Usage
* Feature requirements
* AI consumption
* Workflow consumption
* Seat requirements
* Integration requirements
* Historical usage
* Budget constraints

The AI SHALL clearly identify recommendations as recommendations.

---

## UR-YEARLY-021 — Human Approval for High-Risk Actions

AI SHALL NOT autonomously perform restricted financial operations without authorization.

Potentially restricted operations:

* Refund
* Large credit
* Price override
* Immediate cancellation
* Manual adjustment
* Payment-method modification
* Large plan change

---

## UR-YEARLY-022 — Refund Request

Customers SHALL be able to request refunds according to configured policy.

Refund requests SHALL support:

* Reason
* Subscription
* Invoice
* Requested amount
* Supporting information

---

## UR-YEARLY-023 — Subscription Support

Users SHALL be able to contact support for:

* Incorrect annual charge
* Payment failure
* Invoice issue
* Upgrade issue
* Downgrade issue
* Refund request
* Entitlement issue
* Renewal issue

---

## 5. SYSTEM REQUIREMENTS

## SR-YEARLY-001 — Annual Subscription Service

SalesGenie SHALL provide a dedicated Subscription Service responsible for:

* Annual subscription lifecycle
* Billing period management
* Plan association
* Renewal scheduling
* Cancellation
* Upgrade/downgrade
* Subscription status
* Subscription events

---

## SR-YEARLY-002 — Annual Billing Interval

The platform SHALL support:

```text
billing_interval = year
billing_interval_count = 1
```

The annual billing period SHALL be represented explicitly.

---

## SR-YEARLY-003 — Billing Period Model

Each annual subscription SHALL contain:

```text
subscription_id
tenant_id
organization_id
customer_id
plan_id
plan_version
billing_interval
billing_interval_count
currency
amount
billing_period_start
billing_period_end
next_billing_at
status
cancel_at
canceled_at
created_at
updated_at
version
```

---

## SR-YEARLY-004 — Plan Versioning

Annual subscriptions SHALL reference an immutable plan version.

Existing subscriptions SHALL NOT silently inherit pricing changes.

---

## SR-YEARLY-005 — Financial Precision

All annual pricing, tax, discount, credit, and proration calculations SHALL use decimal-safe arithmetic.

Binary floating-point arithmetic SHALL NOT be used for financial calculations.

---

## SR-YEARLY-006 — Currency

Every financial record SHALL explicitly contain:

```text
currency
amount
tax_amount
discount_amount
total_amount
```

---

## SR-YEARLY-007 — Tenant Isolation

Subscription and financial records SHALL be isolated by:

```text
tenant_id
organization_id
customer_id
```

Cross-tenant access SHALL be denied.

---

## SR-YEARLY-008 — Idempotency

The following operations SHALL be idempotent:

```text
create_annual_subscription
renew_annual_subscription
upgrade_annual_subscription
downgrade_annual_subscription
cancel_annual_subscription
resume_annual_subscription
generate_annual_invoice
charge_annual_subscription
refund_annual_subscription
process_payment_webhook
```

---

## SR-YEARLY-009 — Annual Renewal Engine

The renewal engine SHALL:

1. Identify subscriptions approaching renewal.
2. Validate subscription status.
3. Resolve immutable plan version.
4. Calculate renewal amount.
5. Calculate tax.
6. Apply discounts.
7. Validate payment method.
8. Process payment.
9. Generate invoice.
10. Update billing period.
11. Update entitlements.
12. Publish events.
13. Notify customer.

---

## SR-YEARLY-010 — Renewal Locking

Annual renewal workers SHALL prevent concurrent renewal processing for the same subscription using:

* Distributed locks
* Database constraints
* Idempotency keys
* Optimistic concurrency

---

## SR-YEARLY-011 — Renewal Idempotency Key

Each annual renewal SHALL have a deterministic identifier:

```text
renewal:{subscription_id}:{billing_period_start}:{billing_period_end}
```

Duplicate execution SHALL NOT result in duplicate charges.

---

## SR-YEARLY-012 — Entitlement Service

Subscription state SHALL determine access to:

* AI agents
* AI models
* Workflows
* Integrations
* Knowledge bases
* Leads
* Conversations
* Voice calls
* API access
* Storage
* Seats

---

## SR-YEARLY-013 — Annual Entitlement Accounting

The system SHALL distinguish between:

```text
monthly recurring limits
annual quotas
billing-period quotas
lifetime account limits
```

A plan SHALL explicitly declare the quota model.

---

## SR-YEARLY-014 — Usage Metering

Usage SHALL be recorded with:

```text
usage_id
tenant_id
organization_id
subscription_id
meter_type
quantity
unit
timestamp
source
request_id
idempotency_key
```

---

## SR-YEARLY-015 — Usage Aggregation

Usage SHALL be aggregatable by:

* Annual subscription
* Billing period
* Calendar month
* Tenant
* Organization
* User
* AI agent
* Workflow
* Integration
* Meter

---

## SR-YEARLY-016 — Usage Forecasting

The system SHOULD calculate projected usage using configurable forecasting models.

Forecasts SHALL NOT modify financial records.

---

## SR-YEARLY-017 — Grace Period

Annual subscriptions SHALL support configurable grace periods after failed renewal payments.

Possible access modes:

```text
FULL_ACCESS
LIMITED_ACCESS
READ_ONLY
WORKFLOW_RESTRICTED
SUSPENDED
```

---

## SR-YEARLY-018 — Failed Renewal Recovery

The system SHALL support configurable retries after annual renewal failure.

Retry policies SHALL support:

* Maximum attempts
* Retry intervals
* Exponential backoff
* Notification triggers
* Escalation
* Suspension

---

## SR-YEARLY-019 — Reconciliation

The system SHALL periodically reconcile:

```text
Subscription Service
       ↕
Billing Service
       ↕
Payment Provider
       ↕
Invoice System
```

The reconciliation engine SHALL detect:

* Missing payment
* Duplicate payment
* Incorrect invoice
* Incorrect subscription status
* Missing webhook
* Provider-side cancellation
* Amount mismatch
* Entitlement mismatch

---

## SR-YEARLY-020 — Event-Driven Architecture

The platform SHALL publish annual subscription events.

Examples:

```text
subscription.annual.created
subscription.annual.activated
subscription.annual.upgraded
subscription.annual.downgrade_scheduled
subscription.annual.downgraded
subscription.annual.renewal_started
subscription.annual.renewed
subscription.annual.payment_failed
subscription.annual.grace_period_started
subscription.annual.suspended
subscription.annual.cancellation_scheduled
subscription.annual.canceled
subscription.annual.resumed
subscription.annual.expired
```

---

## SR-YEARLY-021 — Audit Logging

All subscription changes SHALL produce immutable audit records.

Audit records SHALL include:

```text
actor_id
actor_type
tenant_id
action
resource_type
resource_id
previous_state
new_state
reason
approval_id
request_id
correlation_id
timestamp
```

---

## SR-YEARLY-022 — RBAC

Required permissions SHOULD include:

```text
subscription.read
subscription.create
subscription.upgrade
subscription.downgrade
subscription.cancel
subscription.resume
billing.read
billing.manage
invoice.read
refund.request
refund.approve
payment_method.manage
annual_plan.recommend
annual_plan.manage
```

---

## SR-YEARLY-023 — AI Permission Boundary

AI tools SHALL use least-privilege authorization.

Example:

```text
subscription.read       -> allowed
usage.read              -> allowed
invoice.read            -> allowed
plan.compare            -> allowed
plan.recommend          -> allowed

subscription.upgrade    -> confirmation/approval
subscription.cancel     -> confirmation/approval
refund.execute          -> restricted
price_override          -> restricted
payment_method.update   -> restricted
```

---

## SR-YEARLY-024 — Webhook Security

Payment webhooks SHALL support:

* Signature validation
* Timestamp validation
* Replay protection
* Event deduplication
* Rate limiting
* Event persistence
* Correlation IDs

---

## SR-YEARLY-025 — Encryption

Sensitive billing information SHALL be encrypted in transit and at rest.

Secrets SHALL be stored through secure secret management.

---

## SR-YEARLY-026 — Observability

The annual subscription platform SHALL expose:

* Metrics
* Structured logs
* Distributed traces
* Subscription events
* Payment events
* Renewal metrics
* Reconciliation metrics
* AI operation metrics

---

## 6. FUNCTIONAL REQUIREMENTS

## FR-YEARLY-001 — Create Annual Subscription

```http
POST /api/v1/subscriptions
```

Request:

```json
{
  "plan_id": "annual_plan_id",
  "billing_interval": "year",
  "billing_interval_count": 1,
  "currency": "USD",
  "payment_method_id": "pm_id",
  "coupon_code": "optional"
}
```

Response SHALL include:

```text
subscription_id
status
plan
plan_version
billing_interval
billing_period_start
billing_period_end
amount
currency
annual_savings
next_billing_at
entitlements
```

---

## FR-YEARLY-002 — Get Annual Subscription

```http
GET /api/v1/subscriptions/{subscription_id}
```

The API SHALL return the authoritative annual subscription state.

---

## FR-YEARLY-003 — List Annual Subscriptions

```http
GET /api/v1/subscriptions?billing_interval=year
```

The API SHALL support:

* Pagination
* Sorting
* Filtering
* Status
* Plan
* Tenant
* Date range

---

## FR-YEARLY-004 — Annual Price Preview

```http
POST /api/v1/subscriptions/annual/preview
```

The preview SHALL calculate:

```text
base_price
annual_discount
coupon_discount
proration
tax
credits
total
currency
```

No financial mutation SHALL occur during preview.

---

## FR-YEARLY-005 — Annual Upgrade

```http
POST /api/v1/subscriptions/{id}/upgrade
```

The system SHALL:

1. Authenticate request.
2. Authorize operation.
3. Validate target plan.
4. Load immutable plan versions.
5. Calculate remaining value.
6. Calculate target plan value.
7. Calculate credit/proration.
8. Calculate tax.
9. Display final amount.
10. Require confirmation.
11. Process payment if necessary.
12. Update subscription.
13. Update entitlements.
14. Generate invoice.
15. Publish event.
16. Write audit record.

---

## FR-YEARLY-006 — Annual Downgrade

```http
POST /api/v1/subscriptions/{id}/downgrade
```

The system SHALL validate:

* Current usage
* Target plan capacity
* Seat count
* AI usage
* Workflow usage
* Integration requirements
* Storage
* Feature dependencies

---

## FR-YEARLY-007 — Schedule Downgrade

The platform SHALL support:

```text
effective_at = annual_period_end
```

Scheduled downgrades SHALL remain visible and cancellable according to policy.

---

## FR-YEARLY-008 — Annual Cancellation

```http
POST /api/v1/subscriptions/{id}/cancel
```

Request:

```json
{
  "mode": "end_of_period",
  "reason": "optional"
}
```

---

## FR-YEARLY-009 — Resume Annual Subscription

```http
POST /api/v1/subscriptions/{id}/resume
```

The system SHALL cancel the pending cancellation when policy permits.

---

## FR-YEARLY-010 — Annual Renewal

A scheduled renewal worker SHALL identify subscriptions where:

```text
next_billing_at <= current_time
```

and process the renewal exactly once.

---

## FR-YEARLY-011 — Renewal Invoice

Every successful annual renewal SHALL generate an invoice.

The invoice SHALL reference:

```text
subscription_id
plan_id
plan_version
billing_period_start
billing_period_end
payment_id
```

---

## FR-YEARLY-012 — Renewal Failure

When annual renewal fails:

```text
ACTIVE
  ↓
PAYMENT_FAILED
  ↓
GRACE_PERIOD
  ↓
RETRY
```

Successful recovery SHALL return the subscription to:

```text
ACTIVE
```

---

## FR-YEARLY-013 — Renewal Exhaustion

When all retries fail:

```text
PAYMENT_FAILED
       ↓
SUSPENDED
```

or another configured policy state.

---

## FR-YEARLY-014 — Payment Recovery

Customers SHALL be able to update payment information and retry payment.

Successful payment SHALL:

* Clear payment failure
* Update subscription state
* Generate invoice/receipt
* Restore entitlements when permitted
* Publish recovery event

---

## FR-YEARLY-015 — Annual Refund

Refunds SHALL support:

```text
REQUESTED
UNDER_REVIEW
APPROVED
PROCESSING
COMPLETED
REJECTED
FAILED
```

---

## FR-YEARLY-016 — Refund Proration

If policy allows prorated refunds, the calculation SHALL consider:

```text
annual_amount
-
consumed_subscription_value
-
non_refundable_components
=
eligible_refund
```

The exact refund policy SHALL be configurable.

---

## FR-YEARLY-017 — Credit Management

The system SHALL support subscription credits.

Credits SHALL include:

```text
credit_id
tenant_id
subscription_id
source
amount
currency
issued_at
expires_at
status
```

Expired credits SHALL NOT be silently reused.

---

## FR-YEARLY-018 — Annual Discounts

The pricing engine SHALL support:

* Annual plan discount
* Promotional discount
* Coupon
* Contractual discount
* Customer-specific discount

All discounts SHALL be auditable.

---

## FR-YEARLY-019 — Discount Validation

The system SHALL validate:

* Eligibility
* Expiration
* Plan compatibility
* Redemption limit
* Customer eligibility
* Tenant eligibility
* Stacking rules

---

## FR-YEARLY-020 — Usage Threshold Alerts

The platform SHALL support:

```text
50%
75%
80%
90%
95%
100%
```

thresholds.

---

## FR-YEARLY-021 — Annual Quota Exhaustion

When annual quota reaches its limit, the system SHALL execute configured policy:

```text
BLOCK
THROTTLE
ALLOW_OVERAGE
REQUIRE_UPGRADE
ALLOW_WITH_WARNING
```

---

## FR-YEARLY-022 — Monthly Usage Visibility Within Annual Plan

Even if billing occurs annually, users SHALL be able to view monthly usage breakdowns.

Example:

```text
Annual AI allocation: 1,200,000 units

January:   72,000
February:  81,000
March:     95,000
...
Remaining: 952,000
```

---

## FR-YEARLY-023 — Annual Usage Forecast

The system SHALL provide:

```text
annual_allocated
annual_consumed
annual_remaining
average_monthly_usage
projected_annual_usage
projected_exhaustion_date
```

---

## FR-YEARLY-024 — AI Subscription Q&A

The AI SHALL use tools such as:

```text
get_current_subscription
get_annual_plan
get_usage
get_annual_invoice
get_payment_status
get_next_renewal
get_annual_savings
compare_annual_plans
get_entitlements
```

---

## FR-YEARLY-025 — AI Annual Plan Recommendation

The AI SHALL produce explainable recommendations such as:

```text
Current plan usage:
AI: 91%
Workflows: 84%
Seats: 96%
Storage: 63%

Recommendation:
Upgrade to Enterprise Annual.

Primary reasons:
- Seat capacity
- AI consumption
- Workflow utilization
```

---

## FR-YEARLY-026 — AI Safety

The AI SHALL NOT:

* Change subscription price arbitrarily.
* Bypass authorization.
* Modify financial records directly.
* Approve its own refund.
* Access another tenant.
* Disable entitlement enforcement.
* Circumvent payment controls.
* Invent billing information.

---

## FR-YEARLY-027 — Human-in-the-Loop Annual Upgrade

```text
AI Recommendation
       ↓
User Confirmation
       ↓
Annual Price Preview
       ↓
Risk/Authorization Check
       ↓
Payment Confirmation
       ↓
Annual Subscription Upgrade
       ↓
Entitlement Update
       ↓
Invoice
       ↓
Audit
```

---

## FR-YEARLY-028 — Human Financial Approval

High-risk operations SHALL follow:

```text
Request
  ↓
Risk Evaluation
  ↓
Approval Required
  ↓
Authorized Human
  ↓
Execution
  ↓
Audit
```

---

## FR-YEARLY-029 — Payment Method Expiration

The platform SHALL detect payment methods that may expire before annual renewal.

The system SHALL notify customers and request an updated payment method.

---

## FR-YEARLY-030 — Subscription Timeline

The customer and authorized administrators SHALL be able to view:

```text
Subscription Created
Trial Started
Annual Subscription Activated
Upgraded
Downgrade Scheduled
Downgraded
Renewal Started
Renewed
Payment Failed
Payment Recovered
Cancellation Scheduled
Cancellation Reversed
Canceled
Suspended
Reactivated
```

---

## FR-YEARLY-031 — Webhook Processing

Webhook processing SHALL:

1. Verify provider signature.
2. Validate timestamp.
3. Check event ID.
4. Check idempotency.
5. Persist webhook.
6. Process event.
7. Update subscription.
8. Publish internal event.
9. Record audit event.
10. Return acknowledgment.

---

## FR-YEARLY-032 — Duplicate Webhook Protection

A provider event SHALL produce at most one financial side effect.

---

## FR-YEARLY-033 — Out-of-Order Event Handling

The system SHALL handle delayed or out-of-order payment events using:

* Event timestamps
* State versioning
* Provider sequence IDs
* Optimistic locking
* Valid state transitions

---

## FR-YEARLY-034 — Annual Subscription Dashboard

Customer dashboard SHALL show:

```text
Current Annual Plan
Annual Price
Equivalent Monthly Price
Annual Savings
Subscription Status
Current Period
Next Renewal
Usage
Remaining Quota
Projected Usage
Payment Method
Invoices
Upgrade
Downgrade
Cancel
Resume
```

---

## FR-YEARLY-035 — Super Admin Dashboard

Super Admin SHALL be able to view:

```text
Total Annual Subscriptions
Active Annual Subscriptions
Trial Annual Subscriptions
Past-Due Annual Subscriptions
Canceled Annual Subscriptions
Annual MRR Equivalent
Annual Contract Value
Renewal Rate
Annual Churn
Upgrade Rate
Downgrade Rate
Payment Failure Rate
Refund Volume
Revenue by Annual Plan
Revenue by Tenant
Revenue by Region
```

---

## FR-YEARLY-036 — Annual Contract Value

The platform SHALL calculate annual contract value using a deterministic definition configured by the billing system.

---

## FR-YEARLY-037 — Renewal Forecast

Super Admin SHALL be able to view upcoming renewals:

```text
Next 7 days
Next 30 days
Next 60 days
Next 90 days
```

---

## FR-YEARLY-038 — Renewal Risk Detection

The AI MAY identify renewal risks using:

* Payment-method expiration
* Payment failures
* Declining engagement
* Usage reduction
* Support issues
* Cancellation intent
* Feature adoption

AI risk scores SHALL NOT directly modify subscriptions.

---

## FR-YEARLY-039 — Retention Recommendation

The AI MAY recommend:

* Plan adjustment
* Support intervention
* Training
* Feature enablement
* Promotional offer

Any financial concession SHALL require appropriate authorization.

---

## FR-YEARLY-040 — Subscription Search

Super Admin SHALL be able to search annual subscriptions using:

```text
subscription_id
tenant_id
organization_id
customer_id
email
plan
status
renewal_date
payment_status
```

---

## 7. ANNUAL SUBSCRIPTION LIFECYCLE

```text
PLAN DISCOVERY
      ↓
ANNUAL PLAN SELECTION
      ↓
ELIGIBILITY CHECK
      ↓
ANNUAL PRICE CALCULATION
      ↓
DISCOUNT CALCULATION
      ↓
TAX CALCULATION
      ↓
PAYMENT METHOD
      ↓
PAYMENT AUTHORIZATION
      ↓
SUBSCRIPTION CREATION
      ↓
ENTITLEMENT ACTIVATION
      ↓
ANNUAL ACTIVE
      ↓
USAGE MONITORING
      ↓
RENEWAL REMINDERS
      ↓
ANNUAL RENEWAL
      ↓
PAYMENT
      ↓
INVOICE
      ↓
NEW ANNUAL BILLING PERIOD
      ↓
ACTIVE
```

---

## 8. ANNUAL UPGRADE WORKFLOW

```text
CURRENT ANNUAL PLAN
        ↓
TARGET ANNUAL PLAN
        ↓
PLAN COMPATIBILITY
        ↓
REMAINING VALUE CALCULATION
        ↓
PRORATION/CREDIT
        ↓
TARGET PLAN PRICE
        ↓
TAX
        ↓
DISCOUNT
        ↓
FINAL AMOUNT
        ↓
USER CONFIRMATION
        ↓
PAYMENT
        ↓
SUBSCRIPTION UPDATE
        ↓
ENTITLEMENT UPDATE
        ↓
INVOICE
        ↓
AUDIT
```

---

## 9. ANNUAL DOWNGRADE WORKFLOW

```text
DOWNGRADE REQUEST
       ↓
TARGET PLAN VALIDATION
       ↓
USAGE CHECK
       ↓
SEAT CHECK
       ↓
FEATURE CHECK
       ↓
QUOTA CHECK
       ↓
COMPATIBLE?
   ↙          ↘
 YES           NO
 ↓              ↓
SCHEDULE        SHOW BLOCKERS
DOWNGRADE
 ↓
ANNUAL PERIOD END
 ↓
TARGET PLAN ACTIVATED
 ↓
ENTITLEMENTS UPDATED
 ↓
AUDIT EVENT
```

---

## 10. ANNUAL RENEWAL WORKFLOW

```text
RENEWAL SCHEDULER
       ↓
FIND DUE SUBSCRIPTIONS
       ↓
DISTRIBUTED LOCK
       ↓
SUBSCRIPTION VALIDATION
       ↓
PLAN VERSION RESOLUTION
       ↓
PRICE CALCULATION
       ↓
TAX/DISCOUNT
       ↓
PAYMENT
       ↓
   ┌───────────────┐
   │               │
SUCCESS          FAILURE
   │               │
   ↓               ↓
INVOICE          RETRY
   │               ↓
   ↓            GRACE PERIOD
NEW PERIOD         ↓
   │             RETRY
   ↓               ↓
ENTITLEMENTS   SUCCESS/FAILURE
   │               ↓
   ↓            SUSPENSION
NOTIFICATION
```

---

## 11. ANNUAL PAYMENT FAILURE WORKFLOW

```text
ANNUAL RENEWAL
      ↓
PAYMENT ATTEMPT
      ↓
FAILED
      ↓
PAYMENT_FAILED
      ↓
CUSTOMER NOTIFICATION
      ↓
GRACE PERIOD
      ↓
AUTOMATIC RETRY
      ↓
 ┌─────────────┐
 │             │
SUCCESS       FAILED
 │             │
 ↓             ↓
ACTIVE       NEXT RETRY
               ↓
          RETRIES EXHAUSTED
               ↓
           SUSPENSION
```

---

## 12. ANNUAL CANCELLATION WORKFLOW

```text
CANCELLATION REQUEST
        ↓
AUTHORIZATION
        ↓
CANCELLATION POLICY
        ↓
REFUND ELIGIBILITY
        ↓
RETENTION OFFER
        ↓
CUSTOMER CONFIRMATION
        ↓
IMMEDIATE / END-OF-PERIOD
        ↓
CANCELLATION SCHEDULED
        ↓
ANNUAL PERIOD ENDS
        ↓
ENTITLEMENTS UPDATED
        ↓
SUBSCRIPTION CANCELED
        ↓
AUDIT EVENT
```

---

## 13. AI-ASSISTED ANNUAL SUBSCRIPTION WORKFLOW

```text
CUSTOMER
    ↓
AI SUBSCRIPTION ASSISTANT
    ↓
AUTHENTICATION CONTEXT
    ↓
TENANT CONTEXT
    ↓
RBAC/PERMISSION CHECK
    ↓
AUTHORIZED BILLING TOOLS
    ↓
AUTHORITATIVE DATA
    ↓
AI ANALYSIS
    ↓
RECOMMENDATION
    ↓
CUSTOMER CONFIRMATION
    ↓
RISK EVALUATION
    ↓
HUMAN APPROVAL IF REQUIRED
    ↓
BILLING SERVICE
    ↓
SUBSCRIPTION SERVICE
    ↓
ENTITLEMENT SERVICE
    ↓
AUDIT SERVICE
    ↓
NOTIFICATION SERVICE
```

---

## 14. HUMAN ANNUAL SUBSCRIPTION WORKFLOW

```text
CUSTOMER ADMIN
      ↓
SELECT ANNUAL PLAN
      ↓
REVIEW ANNUAL PRICE
      ↓
REVIEW SAVINGS
      ↓
REVIEW TERMS
      ↓
PAYMENT
      ↓
SUBSCRIPTION CREATED
      ↓
ENTITLEMENTS ACTIVATED
      ↓
USAGE MONITORING
      ↓
ANNUAL RENEWAL
```

---

## 15. ANNUAL PRORATION MODEL

The system SHALL use a deterministic configurable proration model.

Conceptually:

```text
remaining_current_plan_value
=
current_plan_value × unused_period_ratio
```

Then:

```text
upgrade_amount
=
target_plan_remaining_value
-
remaining_current_plan_credit
+
tax
-
discount
+
adjustments
```

The exact accounting implementation SHALL be centrally defined by the billing engine.

---

## 16. ANNUAL REFUND MODEL

Where refunds are permitted:

```text
annual_payment
-
consumed_value
-
non_refundable_amount
-
previous_refunds
=
eligible_refund
```

The refund engine SHALL preserve all intermediate calculations for auditability.

---

## 17. AI REQUIREMENTS

## AI-YEARLY-001 — Authoritative Billing Data

AI SHALL retrieve subscription information through controlled billing tools.

AI SHALL NOT infer financial information from conversation history when authoritative data is available.

---

## AI-YEARLY-002 — Billing Tools

Minimum AI tools:

```text
get_subscription
get_annual_plan
get_plan_version
get_usage
get_usage_forecast
get_invoice
get_payment_status
get_renewal_date
get_annual_savings
compare_plans
get_entitlements
get_cancellation_policy
get_refund_policy
```

---

## AI-YEARLY-003 — Recommendation Tools

AI MAY use:

```text
recommend_annual_plan
recommend_upgrade
recommend_downgrade
recommend_retention_action
estimate_usage
estimate_renewal_risk
```

---

## AI-YEARLY-004 — No Direct Database Mutation

AI SHALL NOT directly modify subscription or financial database records.

All mutations SHALL pass through authorized domain services.

---

## AI-YEARLY-005 — Financial Guardrails

AI SHALL NOT:

* Bypass pricing rules.
* Override taxes.
* Modify invoices directly.
* Approve refunds without permission.
* Grant unauthorized credits.
* Disable quotas.
* Change another tenant's subscription.
* Circumvent payment-provider controls.

---

## 18. SECURITY REQUIREMENTS

## SEC-YEARLY-001

All subscription APIs SHALL require authentication.

## SEC-YEARLY-002

Authorization SHALL be checked on every protected operation.

## SEC-YEARLY-003

Tenant isolation SHALL be enforced at service and data layers.

## SEC-YEARLY-004

Payment credentials SHALL never be logged.

## SEC-YEARLY-005

Sensitive billing data SHALL be encrypted.

## SEC-YEARLY-006

Administrative billing actions SHALL be audited.

## SEC-YEARLY-007

Webhook signatures SHALL be verified.

## SEC-YEARLY-008

Replay attacks SHALL be prevented.

## SEC-YEARLY-009

High-risk financial actions SHALL require elevated permissions.

---

## 19. PERFORMANCE REQUIREMENTS

## PERF-YEARLY-001

Subscription reads SHOULD support low-latency responses under normal load.

## PERF-YEARLY-002

Annual renewal processing SHALL scale horizontally.

## PERF-YEARLY-003

Usage events SHALL be processed asynchronously where appropriate.

## PERF-YEARLY-004

Long-running renewal workflows SHALL NOT block API request threads.

## PERF-YEARLY-005

Payment-provider failures SHALL NOT cascade into unrelated platform services.

---

## 20. RELIABILITY REQUIREMENTS

## REL-YEARLY-001

Duplicate renewal jobs SHALL NOT cause duplicate charges.

## REL-YEARLY-002

Duplicate webhooks SHALL NOT cause duplicate financial side effects.

## REL-YEARLY-003

Service restarts SHALL NOT lose subscription state.

## REL-YEARLY-004

Partial failures SHALL be recoverable.

## REL-YEARLY-005

Payment-provider outages SHALL trigger retry/reconciliation mechanisms.

## REL-YEARLY-006

Subscription state SHALL remain internally consistent.

---

## 21. DATABASE REQUIREMENTS

Minimum entities:

```text
plans
plan_versions
subscriptions
subscription_items
subscription_events
billing_periods
payments
payment_attempts
payment_methods
invoices
invoice_items
refunds
credits
discounts
coupons
usage_meters
usage_records
entitlements
subscription_entitlements
webhook_events
billing_adjustments
approval_requests
audit_logs
renewal_jobs
reconciliation_records
```

---

## 22. SUBSCRIPTION STATE MACHINE

```text
TRIALING
    ↓
PENDING_PAYMENT
    ↓
ACTIVE
    ↓
RENEWAL_PENDING
    ↓
ACTIVE

ACTIVE
  ↓
PAYMENT_FAILED
  ↓
GRACE_PERIOD
  ↓
ACTIVE

GRACE_PERIOD
  ↓
SUSPENDED

ACTIVE
  ↓
CANCEL_SCHEDULED
  ↓
CANCELED

CANCEL_SCHEDULED
  ↓
ACTIVE
```

Invalid state transitions SHALL be rejected.

---

## 23. OBSERVABILITY REQUIREMENTS

The system SHALL expose:

```text
annual_subscriptions_created_total
annual_subscriptions_active_total
annual_subscriptions_canceled_total
annual_subscriptions_upgraded_total
annual_subscriptions_downgraded_total
annual_renewals_started_total
annual_renewals_success_total
annual_renewals_failure_total
annual_payment_success_total
annual_payment_failure_total
annual_payment_retry_total
annual_refunds_total
annual_credits_total
annual_churn_rate
annual_renewal_rate
annual_upgrade_rate
annual_downgrade_rate
annual_trial_conversion_rate
annual_revenue
annual_contract_value
annual_mrr_equivalent
annual_usage_exhaustion_total
```

---

## 24. ALERTING REQUIREMENTS

Alerts SHALL be generated for:

* Renewal failure spikes
* Payment-provider outage
* Webhook failures
* Duplicate payment attempts
* Invoice-generation failures
* Subscription-state inconsistencies
* Entitlement synchronization failures
* Reconciliation mismatches
* Abnormal refund volume
* Unusual annual churn
* Unusual renewal failures
* AI billing-tool failures
* Unauthorized financial operations

---

## 25. SUPER ADMIN REQUIREMENTS

Super Admin SHALL be able to:

* Search annual subscriptions.
* View subscription details.
* View renewal history.
* View annual invoices.
* View payment attempts.
* View failed renewals.
* View refunds.
* View credits.
* View usage.
* View entitlement state.
* View audit logs.
* View renewal forecasts.
* Investigate reconciliation failures.
* Configure annual subscription policies.
* Configure retry policies.
* Configure grace periods.
* Configure cancellation rules.
* Configure refund rules.

Super Admin financial mutations SHALL be permission-controlled and audited.

---

## 26. FINANCIAL INVARIANTS

The platform SHALL enforce:

```text
1. An annual subscription cannot have two active annual billing periods.

2. One annual renewal cannot create two successful charges.

3. Every successful annual charge must have a payment record.

4. Every successful annual charge must map to an invoice.

5. Historical annual invoices must remain immutable.

6. Annual pricing must reference an immutable plan version.

7. Subscription totals must reconcile with invoice totals.

8. Refunds cannot exceed refundable amounts.

9. Credits cannot be consumed more than once.

10. Duplicate webhooks cannot create duplicate financial effects.

11. Subscription state cannot transition through an undefined state.

12. Entitlements must correspond to the effective subscription state.

13. Tenant A cannot access tenant B's billing data.

14. AI cannot bypass authorization boundaries.

15. Every administrative financial mutation must be auditable.

16. Renewal processing must be idempotent.

17. Financial calculations must be deterministic.

18. Payment-provider state and internal state must be reconcilable.

19. A canceled subscription cannot silently renew.

20. An expired subscription cannot continue receiving paid-only
    entitlements unless explicitly authorized by policy.
```

---

## 27. ACCEPTANCE CRITERIA

The annual subscription implementation SHALL be considered production-ready when:

* [ ] Users can purchase annual plans.
* [ ] Annual pricing is deterministic.
* [ ] Annual discounts are calculated correctly.
* [ ] Annual savings are displayed transparently.
* [ ] Annual invoices are generated.
* [ ] Annual renewals execute automatically.
* [ ] Duplicate renewals cannot create duplicate charges.
* [ ] Payment failures trigger recovery.
* [ ] Grace periods are configurable.
* [ ] Annual usage is accurately metered.
* [ ] Monthly usage breakdowns are available.
* [ ] Annual usage forecasting is available.
* [ ] Upgrade proration is deterministic.
* [ ] Downgrade compatibility is validated.
* [ ] Cancellation policies are enforced.
* [ ] Refund policies are enforced.
* [ ] Credits are tracked correctly.
* [ ] Entitlements reflect subscription state.
* [ ] Payment webhooks are authenticated.
* [ ] Duplicate webhooks are safely handled.
* [ ] Out-of-order events do not corrupt state.
* [ ] Reconciliation detects financial mismatches.
* [ ] AI can answer annual billing questions accurately.
* [ ] AI recommendations are explainable.
* [ ] AI cannot bypass financial authorization.
* [ ] Human approval is available for high-risk actions.
* [ ] All financial mutations are audited.
* [ ] Tenant isolation is enforced.
* [ ] Super Admin can monitor annual subscriptions.
* [ ] Renewal risk can be surfaced.
* [ ] Customers receive renewal notifications.
* [ ] Subscription state survives service failures.
* [ ] Automated tests cover billing, renewal, proration, refunds,
  concurrency, webhooks, authorization, and recovery.

---

## 28. FAANG-LEVEL TEST REQUIREMENTS

The test suite SHALL include:

## Unit Tests

```text
plan pricing
annual discount
tax calculation
proration
credit calculation
refund calculation
renewal date calculation
state transitions
quota calculations
usage aggregation
```

## Integration Tests

```text
subscription ↔ billing
subscription ↔ payment provider
subscription ↔ entitlement service
subscription ↔ usage service
subscription ↔ notification service
subscription ↔ audit service
```

## Failure Tests

```text
payment timeout
payment provider outage
duplicate webhook
duplicate renewal job
database failure
message duplication
out-of-order event
service restart
partial transaction failure
```

## Security Tests

```text
tenant isolation
RBAC
privilege escalation
AI tool authorization
webhook forgery
replay attack
IDOR
financial endpoint abuse
```

## AI Tests

```text
billing hallucination
wrong tenant access
unauthorized mutation
incorrect plan recommendation
incorrect usage interpretation
prompt injection
tool abuse
approval bypass
```

---

## 29. FAANG-LEVEL NON-FUNCTIONAL QUALITY BAR

```text
CORRECTNESS
├── Deterministic annual billing
├── Immutable plan versions
├── Idempotent renewals
├── Accurate proration
└── Financial reconciliation

SCALABILITY
├── Horizontally scalable renewal workers
├── Partitionable usage events
├── Asynchronous billing workflows
└── High-volume webhook processing

RELIABILITY
├── Retry-safe renewal
├── Payment recovery
├── Reconciliation
├── Outbox/event delivery
└── Disaster recovery

SECURITY
├── Tenant isolation
├── RBAC
├── Least privilege
├── Secure payment integration
├── Webhook verification
└── Immutable audit logs

AI SAFETY
├── Tool-based billing access
├── Least-privilege AI permissions
├── Human approval
├── Explainable recommendations
├── No direct database mutation
└── No financial-policy bypass

OBSERVABILITY
├── Metrics
├── Structured logs
├── Distributed traces
├── Renewal dashboards
├── Billing events
└── Operational alerts

OPERABILITY
├── Reconciliation jobs
├── Dead-letter queues
├── Retry policies
├── Incident workflows
└── Administrative controls
```

---

## 30. FINAL SYSTEM REQUIREMENT

SalesGenie's yearly subscription system SHALL operate as a **secure, financially correct, multi-tenant, event-driven annual subscription platform** integrating:

```text
CUSTOMERS
    +
CUSTOMER ADMINS
    +
SALES AGENTS
    +
SUPPORT AGENTS
    +
FINANCE ADMINS
    +
SUPER ADMINS
    +
AI AGENTS
    +
WORKFLOW ENGINE
    +
SUBSCRIPTION SERVICE
    +
BILLING SERVICE
    +
PRICING ENGINE
    +
PAYMENT PROVIDERS
    +
ENTITLEMENT SERVICE
    +
USAGE METERING
    +
INVOICE SERVICE
    +
NOTIFICATION SERVICE
    +
AUDIT SERVICE
    +
RECONCILIATION ENGINE
    +
OBSERVABILITY PLATFORM
```

The architecture SHALL maintain strict separation between:

```text
RECOMMENDATION
      ↓
USER INTENT
      ↓
AUTHORIZATION
      ↓
APPROVAL
      ↓
FINANCIAL EXECUTION
      ↓
SUBSCRIPTION STATE
      ↓
ENTITLEMENT STATE
      ↓
AUDIT
      ↓
RECONCILIATION
```

No AI agent, workflow, frontend client, integration, external webhook, or internal service SHALL bypass the authoritative subscription, pricing, billing, authorization, entitlement, financial, and audit controls.
