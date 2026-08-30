# SalesGenie — Yearly Plan Requirements

**Document:** `yearly_plan.md`  
**Product:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Requirement Level:** FAANG-Level / Production-Grade  
**Scope:** Annual subscription plan definition, lifecycle, entitlements, billing, usage, AI/human workflows, governance, and operational controls  
**Actors:** End Users, Sales Agents, Support Agents, Managers, Organization Admins, Billing Admins, Super Admins, AI Agents, Workflow Engine, Billing Service, Integration Services, Notification Services

---

## 1. Purpose

The Yearly Plan module defines the complete annual subscription experience for SalesGenie customers.

The module MUST support:

- Annual recurring subscriptions
- Annual pricing and plan entitlements
- Monthly-equivalent usage visibility
- Annual billing and invoicing
- AI and human-agent capacity controls
- Feature entitlements
- Usage-based overages where enabled
- Credits and quota management
- Subscription upgrades and downgrades
- Proration and billing adjustments
- Renewal management
- Cancellation
- Payment failures
- Grace periods
- Plan changes
- Coupons and promotional pricing
- Tax calculation
- Refunds
- Enterprise governance
- Auditability
- Customer notifications
- AI-assisted subscription management
- Human-administered subscription management

The system MUST treat the yearly plan as a first-class billing product rather than simply multiplying monthly pricing by twelve.

---

## 2. Product Context

SalesGenie is a multi-tenant enterprise AI platform providing:

- AI customer support
- AI sales agents
- Human support agents
- Human sales agents
- Multi-agent orchestration
- RAG knowledge bases
- Lead generation
- Lead intelligence
- Omnichannel communication
- Workflow automation
- MCP-based tools and workflows
- Third-party integrations
- AI voice capabilities
- Analytics
- CRM automation
- Campaign automation
- Document intelligence

The yearly plan MUST provide controlled access to these capabilities according to the organization's purchased entitlements.

---

## 3. Actors

## 3.1 End User

An end user MAY:

- View available plans
- View yearly-plan benefits
- Subscribe to an eligible yearly plan
- View subscription status
- View remaining entitlements
- View usage
- View billing history
- Download invoices
- Update permitted billing information
- Cancel renewal where permitted

---

## 3.2 Sales Agent

A sales agent MAY:

- View customer subscription status when authorized
- View plan entitlements
- View usage indicators
- Recommend upgrades
- Initiate upgrade workflows subject to authorization
- Escalate billing issues

A sales agent MUST NOT directly modify billing records without appropriate permission.

---

## 3.3 Support Agent

A support agent MAY:

- View subscription status
- View billing state
- View entitlement state
- Investigate subscription-related issues
- Assist with cancellation or renewal workflows
- Create billing-support tickets

Sensitive payment information MUST remain protected.

---

## 3.4 Organization Admin

An organization admin MAY:

- Purchase yearly plans
- Change plans
- Manage subscription settings
- Manage organization users
- Assign seats
- Configure AI agents
- Configure usage limits
- View organization usage
- View invoices
- Manage authorized billing contacts
- Configure renewal preferences

---

## 3.5 Billing Admin

A billing admin MAY:

- Manage payment methods
- View invoices
- Manage coupons
- Request refunds
- Review billing events
- Manage tax information
- View billing analytics
- Configure billing contacts

---

## 3.6 Super Admin

A Super Admin MAY:

- Create yearly plans
- Modify plan configuration
- Enable/disable plans
- Configure entitlements
- Configure annual pricing
- Configure quotas
- Configure usage policies
- Configure discounts
- Configure grace periods
- Configure renewal policies
- Configure refund policies
- Override eligible subscription states
- Audit billing operations

All privileged actions MUST be audited.

---

## 3.7 AI Agent

AI agents MAY:

- Explain yearly-plan benefits
- Recommend yearly plans
- Calculate estimated savings
- Explain entitlements
- Monitor quota consumption
- Warn about approaching limits
- Recommend upgrades
- Trigger approved subscription workflows
- Generate billing explanations
- Assist with renewal decisions

AI agents MUST NOT bypass authorization or execute financial actions outside their granted tool permissions.

---

## 3.8 Human Billing Operator

A human billing operator MAY:

- Review subscription events
- Resolve billing exceptions
- Approve eligible refunds
- Correct configuration errors
- Investigate payment failures
- Resolve entitlement inconsistencies
- Handle escalated subscription cases

---

## 4. User Requirements

## UR-YEARLY-001 — Annual Plan Discovery

The system SHALL allow customers to discover yearly subscription plans.

Users SHALL be able to view:

- Plan name
- Annual price
- Monthly-equivalent price
- Annual savings
- Included features
- Included AI usage
- Included human-agent capacity
- Included seats
- Included integrations
- Included credits
- Usage limits
- Overage policies
- Renewal terms
- Cancellation terms

---

## UR-YEARLY-002 — Annual Value Transparency

The system SHALL clearly communicate the financial benefit of annual billing.

The UI SHOULD display:

```text
Monthly equivalent: $X/month
Annual price: $Y/year
Monthly billing equivalent: $Z/year
Annual savings: $N
Savings percentage: P%
```

Savings calculations MUST be deterministic and server-authoritative.

---

## UR-YEARLY-003 — Annual Subscription Purchase

Authorized users SHALL be able to purchase an annual subscription.

The purchase flow SHALL include:

1. Plan selection
2. Organization selection
3. Seat configuration
4. Entitlement preview
5. Pricing calculation
6. Coupon validation
7. Tax calculation
8. Payment-method selection
9. Billing information
10. Order confirmation
11. Payment authorization
12. Subscription creation
13. Entitlement provisioning
14. Invoice generation
15. Confirmation notification

---

## UR-YEARLY-004 — Annual Plan Comparison

Users SHALL be able to compare yearly plans.

Comparison SHOULD include:

* Price
* Savings
* Seats
* AI agents
* AI messages
* AI tokens
* Voice minutes
* Workflow executions
* MCP tool executions
* Lead-generation credits
* RAG storage
* Knowledge-base capacity
* Integrations
* API access
* Automation limits
* Analytics
* Support level

---

## UR-YEARLY-005 — Subscription Visibility

Users SHALL be able to view:

* Current plan
* Subscription ID
* Subscription status
* Start date
* Renewal date
* Billing interval
* Annual price
* Payment status
* Next invoice date
* Cancellation state
* Grace-period state
* Entitlement state

---

## UR-YEARLY-006 — Usage Visibility

Users SHALL be able to view yearly-plan usage.

Usage MAY include:

* AI requests
* AI tokens
* Conversations
* Messages
* Voice minutes
* Workflow executions
* MCP executions
* API requests
* Leads generated
* Enrichment operations
* Storage
* Human-agent seats
* AI-agent seats
* Integration operations

Usage SHOULD be presented as:

```text
Used
Included
Remaining
Projected usage
Projected exhaustion date
Overage
```

---

## UR-YEARLY-007 — Renewal Management

Authorized users SHALL be able to:

* Enable automatic renewal
* Disable automatic renewal
* View renewal date
* Update payment method
* Review renewal price
* Review upcoming plan changes
* Receive renewal reminders

---

## UR-YEARLY-008 — Cancellation

Authorized users SHALL be able to cancel future renewal.

The system SHALL clearly distinguish:

```text
Cancel immediately
Cancel at period end
Disable auto-renewal
```

Cancellation behavior MUST follow the organization's subscription policy.

---

## UR-YEARLY-009 — Upgrade

Users with appropriate permissions SHALL be able to upgrade their annual plan.

The system MUST calculate:

* Existing subscription value
* Remaining subscription value
* New plan price
* Applicable credit
* Taxes
* Discounts
* Proration
* Amount due

---

## UR-YEARLY-010 — Downgrade

Users SHALL be able to request eligible downgrades.

Downgrades SHOULD generally take effect at the end of the current billing period unless policy explicitly supports immediate changes.

---

## UR-YEARLY-011 — Billing History

Authorized users SHALL be able to view:

* Invoices
* Payments
* Refunds
* Credits
* Adjustments
* Failed payments
* Subscription changes
* Renewal events

---

## UR-YEARLY-012 — Invoice Access

Users SHALL be able to:

* View invoices
* Download invoices
* Retrieve invoice metadata
* View tax information
* View payment status

---

## UR-YEARLY-013 — Notifications

The system SHALL notify customers about:

* Subscription activation
* Payment success
* Payment failure
* Upcoming renewal
* Renewal success
* Renewal failure
* Usage thresholds
* Plan expiration
* Cancellation
* Refund completion
* Entitlement changes

---

## UR-YEARLY-014 — AI Plan Advisor

SalesGenie SHOULD provide an AI plan advisor capable of analyzing:

* Historical usage
* Current usage
* Growth rate
* Number of users
* AI-agent usage
* Workflow usage
* Integration usage
* Projected consumption

The AI MAY recommend the most appropriate yearly plan.

---

## UR-YEARLY-015 — Human-Assisted Billing

Customers SHALL be able to escalate billing issues to authorized human operators.

The escalation workflow SHALL preserve:

* Customer context
* Subscription state
* Billing events
* Payment state
* AI conversation history
* Relevant audit events

---

## 5. System Requirements

## SR-YEARLY-001 — Multi-Tenant Isolation

The yearly-plan subsystem MUST enforce strict tenant isolation.

Every subscription SHALL be associated with:

```text
tenant_id
organization_id
subscription_id
plan_id
billing_customer_id
```

Cross-tenant subscription access MUST be denied.

---

## SR-YEARLY-002 — Authoritative Billing State

The Billing Service SHALL be the authoritative source for:

* Subscription state
* Pricing
* Billing interval
* Payment state
* Invoice state
* Refund state

Frontend applications MUST NOT be authoritative for billing state.

---

## SR-YEARLY-003 — Entitlement Service

The platform SHALL provide an entitlement service responsible for determining whether an organization can access:

* Features
* AI models
* AI agents
* Integrations
* APIs
* Workflows
* MCP tools
* Storage
* Usage quotas

---

## SR-YEARLY-004 — Immutable Billing Events

Financially significant events MUST be recorded as immutable events.

Examples:

```text
subscription.created
subscription.activated
subscription.upgraded
subscription.downgraded
subscription.renewal.started
subscription.renewed
subscription.cancelled
payment.authorized
payment.captured
payment.failed
invoice.created
invoice.paid
invoice.failed
refund.created
refund.completed
credit.issued
credit.consumed
```

---

## SR-YEARLY-005 — Idempotency

All financial operations MUST support idempotency.

Examples:

```text
create_subscription
process_payment
create_invoice
apply_coupon
issue_refund
renew_subscription
change_plan
provision_entitlements
```

Duplicate requests MUST NOT create duplicate financial transactions.

---

## SR-YEARLY-006 — Pricing Versioning

Yearly pricing MUST be versioned.

A subscription MUST retain the pricing version used during purchase.

Historical invoices MUST NOT change when future pricing changes.

---

## SR-YEARLY-007 — Plan Versioning

Plan configurations MUST be versioned.

Existing customers MUST retain their purchased entitlement contract unless an explicit migration policy applies.

---

## SR-YEARLY-008 — Currency Support

The billing engine SHOULD support multiple currencies.

The system MUST store:

* Currency
* Amount
* Decimal precision
* Exchange-rate metadata when applicable
* Pricing version

Currency conversion MUST NOT be performed by the frontend.

---

## SR-YEARLY-009 — Tax Support

The system SHALL support:

* Tax jurisdiction
* Tax rate
* Tax amount
* Tax exemptions
* Tax IDs
* Tax-inclusive pricing
* Tax-exclusive pricing

---

## SR-YEARLY-010 — Payment Security

The system MUST NOT store raw payment-card data unless the platform explicitly meets the applicable compliance requirements.

Payment credentials SHOULD be tokenized through the payment provider.

---

## SR-YEARLY-011 — RBAC

Subscription operations MUST be permission-controlled.

Example permissions:

```text
billing.subscription.read
billing.subscription.create
billing.subscription.update
billing.subscription.cancel
billing.plan.read
billing.invoice.read
billing.payment.manage
billing.refund.request
billing.refund.approve
billing.usage.read
billing.analytics.read
```

---

## SR-YEARLY-012 — Audit Logging

The system MUST audit:

* Plan changes
* Price changes
* Subscription creation
* Subscription cancellation
* Renewal changes
* Refunds
* Credits
* Coupon application
* Manual overrides
* Entitlement changes
* Billing configuration changes

Audit records SHALL include:

```text
actor_id
actor_type
tenant_id
action
resource_type
resource_id
timestamp
request_id
correlation_id
before_state
after_state
reason
```

---

## 6. Functional Requirements

## 6.1 Annual Plan Configuration

## FR-YEARLY-001

Super Admins SHALL be able to create yearly plans.

Required attributes:

```text
plan_id
plan_name
description
billing_interval = yearly
currency
annual_price
monthly_equivalent_price
status
version
effective_from
effective_until
```

---

## FR-YEARLY-002

The system SHALL support yearly-plan lifecycle states:

```text
DRAFT
ACTIVE
PAUSED
DEPRECATED
ARCHIVED
```

---

## FR-YEARLY-003

Only ACTIVE yearly plans SHALL be purchasable.

---

## FR-YEARLY-004

Deprecated plans SHALL remain available for existing subscribers where required for backward compatibility.

---

## 6.2 Pricing Engine

## FR-YEARLY-005

The pricing engine SHALL calculate annual subscription prices server-side.

Formula:

```text
annual_subtotal =
    base_annual_price
    + seat_charges
    + enabled_add_ons
    + usage_commitments
    - applicable_discounts
```

---

## FR-YEARLY-006

The pricing engine SHALL calculate:

```text
list_price
discount
coupon_discount
credit_applied
tax
final_amount
```

---

## FR-YEARLY-007

The system SHALL expose an immutable pricing quote before payment.

Quote SHALL contain:

```text
quote_id
tenant_id
plan_id
plan_version
currency
subtotal
discount
tax
total
expires_at
```

---

## FR-YEARLY-008

Expired quotes MUST NOT be used for payment.

---

## 6.3 Annual Subscription Creation

## FR-YEARLY-009

The system SHALL create an annual subscription only after successful validation of:

* Tenant
* User authorization
* Plan
* Pricing
* Payment method
* Tax information
* Coupon
* Eligibility

---

## FR-YEARLY-010

Subscription creation SHALL be transactional.

The system MUST prevent states where:

```text
payment succeeded
BUT
subscription was not created
```

or:

```text
subscription created
BUT
payment was not authorized
```

without an explicit recoverable state.

---

## 6.4 Entitlement Provisioning

## FR-YEARLY-011

Upon successful activation, the system SHALL provision plan entitlements.

Entitlements MAY include:

```text
users
seats
ai_agents
human_agents
ai_messages
ai_tokens
voice_minutes
workflow_executions
mcp_tool_calls
api_requests
lead_generation_credits
lead_enrichment_credits
storage
knowledge_base_size
integrations
```

---

## FR-YEARLY-012

Entitlement provisioning SHALL be idempotent.

---

## FR-YEARLY-013

If entitlement provisioning fails after successful payment, the system SHALL:

1. Record the failure
2. Retry automatically
3. Alert operations when retry thresholds are exceeded
4. Preserve the financial transaction
5. Prevent duplicate provisioning

---

## 6.5 Annual Usage

## FR-YEARLY-014

The usage engine SHALL track consumption against yearly-plan entitlements.

Each usage event SHOULD contain:

```text
usage_event_id
tenant_id
subscription_id
meter_id
quantity
unit
timestamp
source
agent_id
workflow_id
integration_id
request_id
```

---

## FR-YEARLY-015

The system SHALL support configurable annual quota models:

### Annual Pool

The customer receives a total annual quota.

Example:

```text
120,000 AI messages/year
```

### Monthly Reset

The customer receives a monthly allowance during an annual commitment.

Example:

```text
10,000 AI messages/month
```

### Hybrid

The customer receives monthly limits plus annual committed resources.

---

## FR-YEARLY-016

The system SHALL prevent unauthorized usage beyond entitlement limits.

---

## FR-YEARLY-017

Where overages are enabled, the system SHALL:

1. Detect quota exhaustion
2. Validate overage eligibility
3. Record metered usage
4. Calculate overage cost
5. Notify the customer
6. Add charges to the billing ledger

---

## 6.6 Usage Forecasting

## FR-YEARLY-018

The system SHOULD calculate projected annual usage.

Example:

```text
current_usage
average_daily_usage
average_monthly_usage
remaining_quota
projected_annual_usage
projected_overage
```

---

## FR-YEARLY-019

AI agents MAY generate recommendations such as:

* Upgrade plan
* Purchase additional credits
* Reduce high-cost workflows
* Optimize model usage
* Increase seat capacity

AI recommendations MUST be explainable.

---

## 6.7 Renewal

## FR-YEARLY-020

The system SHALL automatically initiate renewal workflows before the annual expiration date.

Configurable renewal windows SHOULD include:

```text
30 days
14 days
7 days
3 days
1 day
```

---

## FR-YEARLY-021

The renewal engine SHALL validate:

* Subscription status
* Payment method
* Pricing
* Tax
* Coupon eligibility
* Entitlements
* Account status

---

## FR-YEARLY-022

Successful renewal SHALL:

1. Capture payment
2. Generate invoice
3. Extend subscription period
4. Refresh applicable quotas
5. Maintain eligible entitlements
6. Record renewal event
7. Notify customer

---

## FR-YEARLY-023

Failed renewal SHALL enter a recoverable payment-failure state.

---

## 6.8 Payment Failure

## FR-YEARLY-024

The system SHALL retry eligible failed renewal payments according to configurable retry policies.

Example:

```text
Attempt 1: Day 0
Attempt 2: Day 2
Attempt 3: Day 5
Attempt 4: Day 10
```

---

## FR-YEARLY-025

During a grace period, the platform SHALL support configurable behavior:

```text
FULL_ACCESS
LIMITED_ACCESS
READ_ONLY
SUSPENDED
```

---

## FR-YEARLY-026

The customer SHALL receive notifications for each significant payment-failure state.

---

## 6.9 Upgrade

## FR-YEARLY-027

The system SHALL support annual-to-annual upgrades.

---

## FR-YEARLY-028

Upgrade calculations SHALL support:

```text
remaining_term_credit
new_plan_cost
tax_adjustment
discount_adjustment
amount_due
```

---

## FR-YEARLY-029

The system SHALL immediately provision newly acquired entitlements when the upgrade is successfully completed.

---

## 6.10 Downgrade

## FR-YEARLY-030

Downgrades SHALL be validated against:

* Current usage
* Future entitlements
* Active seats
* AI agents
* Integrations
* Storage
* Workflows
* MCP tools
* Feature dependencies

---

## FR-YEARLY-031

The system SHALL warn customers when current resource usage exceeds the target plan.

---

## 6.11 Cancellation

## FR-YEARLY-032

The system SHALL support cancellation at the end of the annual billing period.

---

## FR-YEARLY-033

The system SHALL preserve access until the effective cancellation date unless immediate cancellation is explicitly authorized.

---

## FR-YEARLY-034

Cancellation SHALL trigger:

* Subscription state update
* Renewal suppression
* Audit event
* Notification
* Future entitlement expiration scheduling

---

## 6.12 Refunds

## FR-YEARLY-035

The system SHALL support policy-controlled annual subscription refunds.

Refund eligibility SHALL consider:

```text
purchase_date
usage
refund_policy
payment_state
coupon
credits
previous_refunds
```

---

## FR-YEARLY-036

Refunds MUST be processed through an idempotent workflow.

---

## FR-YEARLY-037

Refund events SHALL be permanently auditable.

---

## 6.13 Coupons and Discounts

## FR-YEARLY-038

The yearly plan SHALL support coupon eligibility rules.

Examples:

```text
percentage_discount
fixed_discount
first_year_discount
new_customer_discount
enterprise_discount
campaign_discount
```

---

## FR-YEARLY-039

Coupons SHALL support:

* Start date
* End date
* Maximum redemptions
* Per-customer redemption limits
* Applicable plans
* Applicable currencies
* Minimum spend
* Eligibility conditions

---

## FR-YEARLY-040

Expired or invalid coupons MUST be rejected server-side.

---

## 6.14 Credits

## FR-YEARLY-041

The system SHALL support account credits.

Credits MAY originate from:

* Promotions
* Refund adjustments
* Customer service compensation
* Prepaid balances
* Enterprise contracts

---

## FR-YEARLY-042

Credit consumption SHALL be recorded using an immutable ledger.

---

## 6.15 AI Billing Assistant

## FR-YEARLY-043

The AI billing assistant SHALL answer questions about:

* Current yearly plan
* Annual cost
* Renewal date
* Usage
* Remaining quota
* Invoices
* Savings
* Plan differences
* Upgrade options
* Cancellation policy

---

## FR-YEARLY-044

The AI SHALL retrieve billing information from authoritative services rather than relying on conversational memory.

---

## FR-YEARLY-045

The AI SHALL require explicit authorization before executing:

* Plan changes
* Cancellation
* Payment-method changes
* Refund requests
* Credit operations

---

## 6.16 Human Billing Operations

## FR-YEARLY-046

Authorized billing operators SHALL be able to search subscriptions using:

```text
subscription_id
tenant_id
organization_id
customer_id
invoice_id
email
payment_reference
```

---

## FR-YEARLY-047

Operators SHALL be able to inspect a subscription timeline.

Timeline SHOULD include:

```text
subscription_created
payment_authorized
payment_captured
invoice_created
entitlements_provisioned
usage_events
plan_changes
renewal_events
refunds
cancellations
```

---

## FR-YEARLY-048

Manual overrides SHALL require:

* Authorized role
* Reason
* Operator identity
* Timestamp
* Approval where required
* Audit record

---

## 6.17 Human + AI Workflow

## FR-YEARLY-049

SalesGenie SHALL support hybrid subscription workflows.

Example:

```text
Customer
   ↓
AI Billing Assistant
   ↓
Subscription Analysis
   ↓
AI Recommendation
   ↓
Customer Approval
   ↓
Authorization Check
   ↓
Billing Service
   ↓
Payment Gateway
   ↓
Entitlement Service
   ↓
Notification Service
```

---

## FR-YEARLY-050

For high-risk operations, the workflow SHALL support:

```text
AI detects request
      ↓
AI prepares action
      ↓
Human approval required
      ↓
Human reviews
      ↓
Action executed
      ↓
Audit recorded
```

---

## 7. API Requirements

## FR-YEARLY-051

The platform SHALL provide APIs for:

```http
GET    /api/v1/billing/plans
GET    /api/v1/billing/plans/{plan_id}
POST   /api/v1/billing/quotes
POST   /api/v1/billing/subscriptions
GET    /api/v1/billing/subscriptions/{subscription_id}
PATCH  /api/v1/billing/subscriptions/{subscription_id}
POST   /api/v1/billing/subscriptions/{subscription_id}/upgrade
POST   /api/v1/billing/subscriptions/{subscription_id}/downgrade
POST   /api/v1/billing/subscriptions/{subscription_id}/cancel
POST   /api/v1/billing/subscriptions/{subscription_id}/renew
GET    /api/v1/billing/subscriptions/{subscription_id}/usage
GET    /api/v1/billing/invoices
GET    /api/v1/billing/invoices/{invoice_id}
POST   /api/v1/billing/coupons/validate
POST   /api/v1/billing/refunds
GET    /api/v1/billing/credits
```

---

## 8. Data Model Requirements

## FR-YEARLY-052 — YearlyPlan

```text
YearlyPlan
---------
id
name
description
billing_interval
annual_price
currency
monthly_equivalent_price
discount_percentage
entitlements
status
version
effective_from
effective_until
created_at
updated_at
```

---

## FR-YEARLY-053 — Subscription

```text
Subscription
------------
id
tenant_id
organization_id
customer_id
plan_id
plan_version
billing_interval
status
start_date
current_period_start
current_period_end
renewal_date
auto_renew
cancel_at_period_end
currency
subtotal
discount
tax
total
payment_method_id
created_at
updated_at
```

---

## FR-YEARLY-054 — Entitlement

```text
Entitlement
-----------
id
tenant_id
subscription_id
feature_key
quota
used
remaining
reset_policy
effective_from
effective_until
status
```

---

## FR-YEARLY-055 — UsageEvent

```text
UsageEvent
----------
id
tenant_id
subscription_id
meter_id
quantity
unit
source
agent_id
workflow_id
integration_id
request_id
timestamp
```

---

## FR-YEARLY-056 — Renewal

```text
Renewal
-------
id
subscription_id
attempt_number
scheduled_at
processed_at
payment_status
invoice_id
amount
currency
status
failure_reason
```

---

## 9. AI Agent Requirements

## AI-YEARLY-001 — Plan Recommendation

AI SHALL recommend yearly plans based on:

* Customer requirements
* Usage history
* Team size
* Growth trajectory
* Feature requirements
* Budget constraints

---

## AI-YEARLY-002 — Usage Optimization

AI SHOULD identify:

* Unused entitlements
* Expensive workflows
* Excessive model usage
* High-cost integrations
* Underutilized seats

---

## AI-YEARLY-003 — Renewal Prediction

AI SHOULD predict:

* Renewal likelihood
* Usage exhaustion
* Upgrade probability
* Payment-risk signals

Predictions MUST NOT independently change billing state.

---

## AI-YEARLY-004 — Billing Explanation

AI SHALL explain invoices in human-readable language.

---

## AI-YEARLY-005 — Guardrails

AI MUST NOT:

* Bypass authorization
* Modify billing ledgers directly
* Invent prices
* Invent invoices
* Invent payment status
* Reveal another tenant's information
* Execute unauthorized refunds
* Modify subscription state without permission

---

## 10. Human Workflow Requirements

## HUMAN-YEARLY-001

Billing administrators SHALL have a dedicated annual subscription dashboard.

---

## HUMAN-YEARLY-002

The dashboard SHALL provide:

* Active annual subscriptions
* Upcoming renewals
* Failed renewals
* Cancellations
* Refunds
* Revenue
* Annual recurring revenue
* Usage
* Overages
* Customer health indicators

---

## HUMAN-YEARLY-003

Billing operators SHALL be able to investigate subscription incidents without accessing raw payment credentials.

---

## 11. Security Requirements

## SEC-YEARLY-001

All subscription APIs MUST enforce authentication.

---

## SEC-YEARLY-002

All subscription operations MUST enforce authorization.

---

## SEC-YEARLY-003

Sensitive billing data MUST be encrypted in transit and at rest.

---

## SEC-YEARLY-004

Secrets MUST NOT be stored in:

* Source code
* Frontend bundles
* Logs
* AI prompts
* Browser local storage

---

## SEC-YEARLY-005

Payment-provider webhooks MUST be signature-validated.

---

## SEC-YEARLY-006

Webhook events MUST be idempotently processed.

---

## SEC-YEARLY-007

Billing operations MUST use correlation IDs for distributed tracing.

---

## 12. Reliability Requirements

## REL-YEARLY-001

The annual billing subsystem SHOULD target:

```text
99.99% billing API availability
```

for production workloads.

---

## REL-YEARLY-002

Financial operations MUST be recoverable after:

* Service crash
* Network failure
* Database timeout
* Payment-provider timeout
* Duplicate webhook
* Message-delivery failure

---

## REL-YEARLY-003

The system SHALL use durable event processing for critical billing events.

---

## REL-YEARLY-004

Failed entitlement provisioning SHALL use retry policies with exponential backoff.

---

## 13. Performance Requirements

## PERF-YEARLY-001

Plan retrieval SHOULD complete within:

```text
P95 < 300 ms
```

under normal production load.

---

## PERF-YEARLY-002

Subscription status retrieval SHOULD target:

```text
P95 < 500 ms
```

excluding third-party payment-provider latency.

---

## PERF-YEARLY-003

Usage dashboards SHOULD use pre-aggregated metrics where required for high-volume tenants.

---

## 14. Scalability Requirements

The system SHALL support:

* Millions of tenants
* Millions of annual subscriptions
* High-volume usage events
* High-frequency AI usage
* Large numbers of billing events
* Concurrent renewal operations

Usage ingestion SHOULD be horizontally scalable.

---

## 15. Observability Requirements

The system SHALL expose metrics including:

```text
yearly_plan_purchases_total
yearly_subscription_active_total
yearly_subscription_cancelled_total
yearly_subscription_upgrades_total
yearly_subscription_downgrades_total
yearly_renewals_total
yearly_renewal_failures_total
yearly_payment_failures_total
yearly_refunds_total
yearly_usage_events_total
yearly_overage_events_total
yearly_entitlement_failures_total
```

---

## 16. Alerting Requirements

Alerts SHALL be configurable for:

* Renewal failure spikes
* Payment-provider errors
* Entitlement provisioning failures
* Usage-metering failures
* Duplicate financial events
* Billing reconciliation mismatches
* Unexpected revenue changes
* High refund rates
* Failed webhook processing

---

## 17. Reconciliation Requirements

## REC-YEARLY-001

The system SHALL periodically reconcile:

```text
Payment Provider
        ↕
Billing Ledger
        ↕
Subscription Database
        ↕
Invoice System
        ↕
Entitlement System
```

---

## REC-YEARLY-002

The reconciliation engine SHALL detect:

* Missing payments
* Duplicate payments
* Missing invoices
* Incorrect subscription states
* Incorrect entitlement states
* Incorrect refunds

---

## 18. Compliance Requirements

The system SHOULD support applicable:

* PCI DSS controls
* SOC 2 controls
* GDPR requirements where applicable
* Data-retention policies
* Financial audit requirements
* Tax compliance requirements

Payment-card data SHOULD remain within the payment provider's PCI-compliant environment whenever possible.

---

## 19. Acceptance Criteria

## AC-YEARLY-001

A customer can purchase an annual plan successfully.

## AC-YEARLY-002

The system calculates annual pricing correctly.

## AC-YEARLY-003

The customer receives the correct entitlements after payment.

## AC-YEARLY-004

Duplicate purchase requests do not create duplicate subscriptions.

## AC-YEARLY-005

Annual usage is accurately metered.

## AC-YEARLY-006

The customer can see remaining yearly quota.

## AC-YEARLY-007

The system correctly processes annual renewal.

## AC-YEARLY-008

Failed renewal payments enter the configured retry/grace workflow.

## AC-YEARLY-009

Cancellation prevents future automatic renewal.

## AC-YEARLY-010

Upgrades correctly calculate applicable credits and charges.

## AC-YEARLY-011

Downgrades respect entitlement constraints.

## AC-YEARLY-012

Coupons are validated server-side.

## AC-YEARLY-013

Invoices contain correct annual pricing, tax, discount, and payment information.

## AC-YEARLY-014

Refunds are idempotent and auditable.

## AC-YEARLY-015

AI agents cannot perform unauthorized billing operations.

## AC-YEARLY-016

Human billing operators can investigate annual subscriptions.

## AC-YEARLY-017

All financially significant actions are auditable.

## AC-YEARLY-018

Cross-tenant subscription access is impossible through authorized APIs.

---

## 20. End-to-End Annual Subscription Workflow

```text
Customer
   |
   v
SalesGenie Frontend
   |
   v
Authentication
   |
   v
Authorization / RBAC
   |
   v
Yearly Plan Catalog
   |
   v
Plan Comparison
   |
   v
AI Plan Advisor
   |
   v
Pricing Engine
   |
   +--> Coupon Service
   |
   +--> Tax Service
   |
   +--> Credit Service
   |
   v
Quote Generation
   |
   v
Customer Confirmation
   |
   v
Payment Gateway
   |
   v
Payment Authorization
   |
   v
Billing Ledger
   |
   v
Subscription Service
   |
   v
Entitlement Service
   |
   +--> AI Agents
   +--> Human Agents
   +--> Workflows
   +--> MCP Tools
   +--> Integrations
   +--> Lead Generation
   +--> RAG
   |
   v
Usage Metering
   |
   v
Billing Analytics
   |
   v
Notifications
```

---

## 21. Annual Renewal Workflow

```text
Renewal Scheduler
      |
      v
Upcoming Renewal Detection
      |
      v
Subscription Validation
      |
      v
Pricing Validation
      |
      v
Tax Calculation
      |
      v
Payment Method Validation
      |
      v
Payment Gateway
      |
      +---- SUCCESS ----+
      |                 |
      v                 v
Invoice Generation   Renewal Event
      |                 |
      +--------+--------+
               |
               v
       Entitlement Refresh
               |
               v
       Usage Period Reset
               |
               v
        Customer Notification
```

---

## 22. Failed Renewal Workflow

```text
Renewal Attempt
      |
      v
Payment Failed
      |
      v
Record Failure
      |
      v
Notify Customer
      |
      v
Retry Scheduler
      |
      +---- SUCCESS --> Renew Subscription
      |
      +---- FAILURE
              |
              v
         Grace Period
              |
              v
       Limited Access
              |
              v
      Final Payment Retry
              |
              +---- SUCCESS --> Restore Access
              |
              +---- FAILURE
                         |
                         v
                  Subscription Suspended
```

---

## 23. AI + Human Escalation Workflow

```text
Customer
   |
   v
AI Billing Assistant
   |
   v
Intent Detection
   |
   +--> Informational Request
   |          |
   |          v
   |      AI Response
   |
   +--> Low-Risk Action
   |          |
   |          v
   |      Authorization
   |          |
   |          v
   |      Execute
   |
   +--> High-Risk Financial Action
              |
              v
       Human Approval Queue
              |
              v
       Billing Administrator
              |
              v
        Approve / Reject
              |
              v
        Billing Service
              |
              v
          Audit Log
```

---

## 24. Non-Functional Quality Requirements

The yearly-plan implementation MUST prioritize:

* Correctness over convenience
* Financial consistency
* Strong tenant isolation
* Idempotency
* Auditability
* Deterministic pricing
* Secure authorization
* High availability
* Horizontal scalability
* Event-driven architecture
* Backward compatibility
* Observability
* Disaster recovery
* Operational transparency

---

## 25. Definition of Done

The `yearly_plan.md` implementation SHALL be considered complete only when:

* [ ] Annual plans can be configured
* [ ] Annual prices are versioned
* [ ] Annual subscriptions can be purchased
* [ ] Pricing quotes are generated
* [ ] Coupons work correctly
* [ ] Taxes are calculated correctly
* [ ] Payments are processed securely
* [ ] Invoices are generated
* [ ] Entitlements are provisioned
* [ ] AI usage is metered
* [ ] Human-agent capacity is enforced
* [ ] MCP usage is metered
* [ ] Workflow usage is metered
* [ ] Integration usage is metered
* [ ] Annual quotas are enforced
* [ ] Overage handling works where enabled
* [ ] Usage forecasting works
* [ ] AI billing assistant works
* [ ] Human billing escalation works
* [ ] Upgrades work
* [ ] Downgrades work
* [ ] Cancellation works
* [ ] Renewal works
* [ ] Failed payments are recoverable
* [ ] Grace periods work
* [ ] Refunds work
* [ ] Credits work
* [ ] Billing events are immutable
* [ ] Webhooks are idempotent
* [ ] Reconciliation works
* [ ] RBAC is enforced
* [ ] Audit logging is complete
* [ ] Cross-tenant isolation is verified
* [ ] Metrics and alerts are implemented
* [ ] Security controls are validated
* [ ] Disaster-recovery procedures are tested
* [ ] End-to-end automated tests pass
* [ ] Production observability is enabled

---

## 26. Core Design Principle

SalesGenie's yearly plan MUST be implemented as an **enterprise-grade annual subscription contract with independently managed pricing, entitlements, usage metering, billing, payment, renewal, and access-control systems**.

The architecture MUST ensure:

```text
Pricing ≠ Subscription State
Subscription State ≠ Entitlement State
Entitlement State ≠ Usage State
Usage State ≠ Payment State
Payment State ≠ Invoice State
```

These domains SHALL communicate through well-defined APIs and durable events while maintaining a consistent, auditable financial state.

AI agents MAY assist, recommend, explain, monitor, and orchestrate.

Humans SHALL retain control over explicitly designated high-risk financial and administrative operations.

No AI agent, frontend component, or integration SHALL bypass the authoritative Billing, Authorization, Security, or Audit layers.
