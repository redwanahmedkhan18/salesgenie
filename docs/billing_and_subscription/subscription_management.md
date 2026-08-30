# SalesGenie — Subscription Management Requirements

**Document:** `subscription_management.md`  
**Product:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Requirement Level:** FAANG-Level / Enterprise Production  
**Scope:** Subscription Management  
**Actors:** Super Admin, Organization Owner, Billing Admin, Admin, Finance Team, Sales Manager, Sales Agent, Support Agent, AI Billing Agent, AI Sales Agent, AI Support Agent, AI Workflow Agent, End User, Payment Provider

---

## 1. Purpose

The SalesGenie Subscription Management subsystem shall provide a secure, multi-tenant, auditable, highly available subscription lifecycle platform for managing:

- Free plans
- Freemium plans
- Paid plans
- Trials
- Monthly subscriptions
- Annual subscriptions
- Usage-based subscriptions
- Seat-based subscriptions
- Hybrid subscriptions
- Enterprise subscriptions
- Custom contracts
- Add-ons
- Subscription upgrades
- Subscription downgrades
- Plan changes
- Seat changes
- Billing interval changes
- Renewals
- Cancellations
- Pauses
- Resumptions
- Suspensions
- Reactivations
- Proration
- Credits
- Discounts
- Entitlements
- Usage limits
- Subscription-level budgets
- Subscription analytics
- AI-assisted subscription management
- Human approval workflows

The subsystem shall ensure that every subscription state, entitlement, financial implication, and AI-assisted action is deterministic, authorized, observable, and auditable.

---

## 2. Product Goals

The Subscription Management subsystem shall:

1. Provide a single source of truth for subscription state.
2. Support complete subscription lifecycle management.
3. Maintain strict tenant isolation.
4. Prevent unauthorized subscription modifications.
5. Prevent duplicate subscription creation.
6. Support deterministic plan changes.
7. Support deterministic proration.
8. Synchronize subscription state with the Billing Platform.
9. Synchronize subscription state with payment providers.
10. Synchronize subscription state with entitlement services.
11. Support millions of subscriptions.
12. Support high-volume subscription events.
13. Support AI-assisted subscription recommendations.
14. Support AI-assisted low-risk automation.
15. Require human approval for configurable high-risk operations.
16. Provide complete subscription audit history.
17. Provide reliable recovery from provider failures.
18. Prevent entitlement drift.
19. Provide subscription analytics.
20. Support enterprise contractual subscriptions.

---

## 3. Non-Goals

The Subscription Management subsystem shall not:

- Store raw card information unnecessarily.
- Trust subscription values supplied by the frontend.
- Allow AI agents to bypass authorization.
- Directly modify immutable billing ledger history.
- Delete historical subscription records destructively.
- Grant entitlements solely based on frontend state.
- Process provider webhooks without verification.
- Allow one tenant to access another tenant's subscription data.
- Allow AI agents to approve their own high-risk actions.

---

## 4. Actors

## 4.1 Human Actors

### H-01 — Super Admin

Platform-wide subscription administrator.

Capabilities:

- Create plans.
- Modify plan configuration.
- Activate/deactivate plans.
- View all subscriptions.
- Suspend organizations.
- Review subscription incidents.
- Configure global subscription policies.
- Review subscription analytics.
- Override selected subscription policies.
- Review audit logs.

---

### H-02 — Organization Owner

Tenant-level subscription owner.

Capabilities:

- View current subscription.
- Start eligible subscription.
- Upgrade plan.
- Downgrade plan.
- Change billing interval.
- Add seats.
- Remove seats.
- Add add-ons.
- Remove add-ons.
- Pause subscription where supported.
- Resume subscription.
- Cancel subscription.
- Reactivate eligible subscriptions.
- View subscription history.
- View usage and limits.

---

### H-03 — Billing Admin

Authorized financial administrator.

Capabilities:

- View subscriptions.
- Modify subscriptions.
- Manage billing-related subscription settings.
- Review invoices.
- Review payment status.
- Request cancellation.
- Request plan changes.
- Manage subscription budget policies.

---

### H-04 — Admin

May view subscription status and limited configuration according to RBAC.

---

### H-05 — Sales Manager

May:

- View customer subscription status.
- View plan.
- View usage.
- Identify upgrade opportunities.
- Recommend plan changes.
- View subscription lifecycle analytics.

---

### H-06 — Sales Agent

May:

- View permitted subscription information.
- Explain plan differences.
- Recommend upgrades.
- Create upgrade requests.

---

### H-07 — Support Agent

May:

- View subscription status.
- View subscription history.
- Explain subscription states.
- Initiate approved subscription support workflows.
- Escalate subscription changes.

---

### H-08 — Finance Team

May:

- Review subscription revenue.
- Review subscription changes.
- Reconcile subscriptions against billing records.
- Analyze recurring revenue.
- Review cancellations and churn.

---

### H-09 — End User

May access subscription information only where explicitly exposed by the organization.

---

## 5. AI Actors

## AI-01 — AI Subscription Agent

The AI Subscription Agent may:

- Explain subscription status.
- Explain plan differences.
- Recommend plans.
- Detect usage-limit problems.
- Recommend upgrades.
- Recommend downgrades.
- Forecast subscription costs.
- Identify unused seats.
- Detect subscription anomalies.
- Prepare subscription-change requests.
- Execute explicitly authorized low-risk actions.

---

## AI-02 — AI Sales Agent

The AI Sales Agent may:

- Recommend upgrades.
- Recommend add-ons.
- Detect expansion opportunities.
- Identify customers approaching usage limits.
- Forecast customer needs.
- Generate personalized subscription recommendations.

---

## AI-03 — AI Support Agent

The AI Support Agent may:

- Explain subscription status.
- Explain cancellation policy.
- Explain trial expiration.
- Explain renewal dates.
- Explain plan limitations.
- Create subscription support requests.

---

## AI-04 — AI Workflow Agent

The AI Workflow Agent may:

- Monitor subscription events.
- Trigger subscription workflows.
- Notify users.
- Evaluate approved policies.
- Request human approval.
- Execute authorized low-risk operations.

---

## 6. Subscription Lifecycle

The system shall support the following canonical states:

```text
DRAFT
TRIALING
ACTIVE
PAST_DUE
PAUSED
SCHEDULED_FOR_CANCELLATION
CANCELLED
EXPIRED
SUSPENDED
REACTIVATION_PENDING
```

Additional internal states may be used where required.

---

## 7. Subscription State Machine

```text
                 ┌──────────────┐
                 │     DRAFT    │
                 └──────┬───────┘
                        │
                        ▼
                 ┌──────────────┐
                 │   TRIALING   │
                 └──────┬───────┘
                        │
                Trial Conversion
                        │
                        ▼
                 ┌──────────────┐
                 │    ACTIVE    │
                 └──────┬───────┘
                        │
             ┌──────────┼──────────┐
             │          │          │
             ▼          ▼          ▼
          PAUSED     PAST_DUE   SCHEDULED_
                                CANCELLATION
             │          │          │
             │          ▼          ▼
             │       SUSPENDED  CANCELLED
             │
             ▼
          ACTIVE
```

Invalid state transitions shall be rejected.

---

## 8. User Requirements

## UR-001 — View Subscription

Authorized users shall be able to view:

* Subscription ID.
* Current plan.
* Plan version.
* Subscription status.
* Start date.
* Current billing period.
* Renewal date.
* Trial status.
* Billing interval.
* Seats.
* Add-ons.
* Usage.
* Limits.
* Discounts.
* Credits.
* Payment status.
* Cancellation status.

---

## UR-002 — Start Subscription

Authorized users shall be able to start an eligible subscription.

The system shall:

1. Authenticate the user.
2. Resolve tenant.
3. Validate organization eligibility.
4. Validate plan.
5. Validate pricing.
6. Validate payment requirements.
7. Create subscription.
8. Create billing relationship.
9. Assign entitlements.
10. Emit subscription events.
11. Record audit event.

---

## UR-003 — Start Free Subscription

The system shall support free subscriptions without requiring payment information where policy allows.

---

## UR-004 — Start Trial

Users shall be able to start eligible trials.

The system shall display:

* Trial duration.
* Trial start date.
* Trial end date.
* Included features.
* Usage limits.
* Conversion behavior.
* Cancellation policy.

---

## UR-005 — Trial Conversion

The system shall support:

```text
TRIALING
    ↓
TRIAL_EXPIRING
    ↓
PAYMENT_VALIDATION
    ↓
ACTIVE
```

where applicable.

---

## UR-006 — Upgrade Subscription

Authorized users shall be able to upgrade.

The system shall show:

* Current plan.
* New plan.
* Price difference.
* Prorated amount.
* New entitlements.
* New limits.
* Effective date.
* Next billing estimate.

---

## UR-007 — Downgrade Subscription

Authorized users shall be able to downgrade.

The system shall warn about:

* Removed features.
* Reduced limits.
* Excess usage.
* Excess seats.
* Removed integrations.
* Reduced AI capabilities.

---

## UR-008 — Change Billing Interval

Users shall be able to change between supported intervals such as:

```text
MONTHLY
ANNUAL
CUSTOM
```

The system shall calculate applicable financial adjustments.

---

## UR-009 — Seat Management

Authorized users shall be able to:

* Increase seats.
* Decrease seats.
* View used seats.
* View available seats.
* View minimum seats.
* View seat pricing.

---

## UR-010 — Add-On Management

Users shall be able to:

* Add add-ons.
* Remove add-ons.
* View add-on pricing.
* View add-on entitlements.
* View effective dates.

---

## UR-011 — Pause Subscription

Where supported, users shall be able to pause subscriptions.

The system shall enforce:

* Maximum pause duration.
* Eligibility.
* Entitlement behavior.
* Billing behavior.
* Resume requirements.

---

## UR-012 — Resume Subscription

Authorized users shall be able to resume eligible subscriptions.

---

## UR-013 — Cancel Subscription

Users shall be able to:

* Cancel immediately.
* Cancel at period end.
* Request cancellation.
* Provide cancellation reason.

---

## UR-014 — Reactivate Subscription

Eligible cancelled subscriptions shall be reactivated according to policy.

---

## UR-015 — View Subscription History

Users with appropriate permissions shall be able to view:

* Plan changes.
* Seat changes.
* Add-on changes.
* Billing interval changes.
* Cancellations.
* Renewals.
* Pauses.
* Resumptions.
* Suspensions.
* Reactivations.

---

## 9. AI User Requirements

## AI-UR-001 — Subscription Explanation

The AI system shall explain subscription state using authoritative subscription data.

The AI shall not fabricate:

* Plan.
* Price.
* Renewal date.
* Trial date.
* Usage.
* Subscription status.

---

## AI-UR-002 — Plan Recommendation

The AI system shall recommend plans using:

* Current usage.
* Historical usage.
* Feature requirements.
* Team size.
* Growth rate.
* Budget.
* Subscription history.

---

## AI-UR-003 — Upgrade Recommendation

The AI system shall identify when:

* Usage approaches limits.
* Seats approach limits.
* Users repeatedly hit feature restrictions.
* Current plan becomes economically inefficient.
* New features require a higher tier.

---

## AI-UR-004 — Downgrade Recommendation

The AI system may identify:

* Unused seats.
* Underutilized quotas.
* Unused premium features.
* Excessive plan capacity.

The recommendation shall include estimated savings and potential feature loss.

---

## AI-UR-005 — Subscription Anomaly Detection

AI shall identify:

* Unexpected upgrades.
* Unexpected downgrades.
* Rapid plan cycling.
* Repeated cancellations.
* Suspicious trial activity.
* Unusual seat changes.
* Abnormal subscription changes.

---

## AI-UR-006 — Subscription Cost Forecast

AI shall forecast:

* Next billing amount.
* Expected monthly cost.
* Expected annual cost.
* Usage-based cost.
* Overage cost.
* Expansion cost.

---

## 10. System Requirements

## SR-001 — Subscription Service

A dedicated Subscription Service shall manage:

* Subscription lifecycle.
* Subscription state.
* Plan relationships.
* Subscription items.
* Seats.
* Add-ons.
* Billing intervals.
* Trial state.
* Cancellation state.
* Renewal state.

---

## SR-002 — Single Source of Truth

The Subscription Service shall be authoritative for subscription lifecycle state.

The following systems shall consume subscription state rather than independently maintaining conflicting subscription state:

```text
Billing Service
Entitlement Service
AI Gateway
Workflow Engine
CRM Integrations
Analytics Service
Notification Service
```

---

## SR-003 — Multi-Tenant Isolation

Every subscription shall be associated with:

```text
tenant_id
organization_id
customer_account_id
```

Tenant boundaries shall be enforced server-side.

---

## SR-004 — Subscription Identity

Every subscription shall have:

```text
subscription_id
tenant_id
organization_id
customer_account_id
plan_id
plan_version_id
status
created_at
updated_at
```

---

## SR-005 — Subscription Versioning

Subscription changes shall create versioned records or immutable lifecycle events.

Historical subscription states shall remain reconstructable.

---

## SR-006 — Plan Version Binding

A subscription shall reference an explicit plan version.

Pricing changes shall not silently mutate historical subscription terms.

---

## SR-007 — Subscription Items

A subscription shall support multiple items:

```text
BASE_PLAN
SEAT
ADD_ON
USAGE_COMPONENT
CONTRACT_COMPONENT
```

---

## SR-008 — Seat Management

The system shall track:

```text
allocated_seats
active_seats
included_seats
billable_seats
minimum_seats
```

---

## SR-009 — Trial Management

Trial records shall include:

```text
trial_id
subscription_id
start_at
end_at
duration
conversion_policy
usage_limit
conversion_status
```

---

## SR-010 — Renewal Management

The system shall calculate:

* Renewal date.
* Renewal amount.
* Renewal plan.
* Renewal discounts.
* Renewal credits.
* Renewal taxes.
* Renewal payment requirements.

---

## SR-011 — Cancellation Management

Cancellation records shall include:

```text
cancellation_id
subscription_id
requested_at
effective_at
requested_by
reason
type
status
```

---

## SR-012 — Proration Engine

The system shall provide deterministic proration for:

* Plan upgrades.
* Plan downgrades.
* Seat changes.
* Add-ons.
* Billing interval changes.

---

## SR-013 — Entitlement Synchronization

Subscription changes shall update entitlements.

Example:

```text
Subscription
    ↓
Entitlement Evaluation
    ↓
Feature Access
    ↓
AI Model Access
    ↓
Channel Access
    ↓
Workflow Access
    ↓
Usage Limits
```

---

## SR-014 — Billing Synchronization

Subscription changes shall synchronize with the Billing Platform.

---

## SR-015 — Payment Provider Synchronization

Where required, subscription changes shall synchronize with the configured payment provider.

---

## SR-016 — Event-Driven Architecture

The Subscription Service shall publish lifecycle events.

---

## 11. Subscription Events

The system shall support:

```text
subscription.created
subscription.started
subscription.trial_started
subscription.trial_expiring
subscription.trial_expired
subscription.activated

subscription.upgrade_requested
subscription.upgraded

subscription.downgrade_requested
subscription.downgraded

subscription.seats_changed
subscription.addon_added
subscription.addon_removed

subscription.billing_interval_changed

subscription.renewal_upcoming
subscription.renewed
subscription.renewal_failed

subscription.pause_requested
subscription.paused
subscription.resumed

subscription.cancellation_requested
subscription.scheduled_for_cancellation
subscription.cancelled

subscription.reactivation_requested
subscription.reactivated

subscription.suspended
subscription.expired

subscription.entitlements_changed
```

---

## 12. Functional Requirements

## FR-001 — Create Subscription

The system shall support:

```http
POST /api/v1/subscriptions
```

The request shall not be allowed to define authoritative pricing.

Pricing shall be resolved server-side.

---

## FR-002 — Retrieve Subscriptions

The API shall support:

```http
GET /api/v1/subscriptions
GET /api/v1/subscriptions/{subscription_id}
```

---

## FR-003 — Update Subscription

The system shall support controlled subscription updates.

```http
PATCH /api/v1/subscriptions/{subscription_id}
```

Only supported mutable properties may be modified.

---

## FR-004 — Upgrade

The system shall support:

```http
POST /api/v1/subscriptions/{subscription_id}/upgrade
```

The operation shall:

1. Validate authorization.
2. Validate target plan.
3. Calculate price.
4. Calculate proration.
5. Evaluate entitlements.
6. Validate payment.
7. Update subscription.
8. Update entitlements.
9. Generate billing event.
10. Audit the change.

---

## FR-005 — Downgrade

The system shall support:

```http
POST /api/v1/subscriptions/{subscription_id}/downgrade
```

The system shall detect incompatible current usage.

Example:

```text
Current:
20 seats

Target:
10 seats

Result:
Downgrade blocked or requires seat reduction.
```

---

## FR-006 — Billing Interval Change

The system shall support:

```http
POST /api/v1/subscriptions/{subscription_id}/change-billing-interval
```

---

## FR-007 — Add Seats

The system shall support:

```http
POST /api/v1/subscriptions/{subscription_id}/seats
```

---

## FR-008 — Remove Seats

The system shall prevent removal below:

* Active users.
* Contractual minimum.
* Plan minimum.

unless explicitly approved.

---

## FR-009 — Add Add-On

The system shall support:

```http
POST /api/v1/subscriptions/{subscription_id}/addons
```

---

## FR-010 — Remove Add-On

The system shall support:

```http
DELETE /api/v1/subscriptions/{subscription_id}/addons/{addon_id}
```

---

## FR-011 — Start Trial

The system shall:

1. Validate trial eligibility.
2. Validate organization history.
3. Prevent trial abuse.
4. Create trial subscription.
5. Assign trial entitlements.
6. Configure expiration.
7. Schedule notifications.

---

## FR-012 — Trial Expiration

The system shall:

1. Detect expiration.
2. Notify user.
3. Attempt conversion where authorized.
4. Update subscription state.
5. Update entitlements.
6. Record audit event.

---

## FR-013 — Renew Subscription

The system shall support automatic renewal.

Renewal shall be idempotent.

---

## FR-014 — Failed Renewal

The system shall:

1. Record failure.
2. Update renewal state.
3. Start retry policy.
4. Notify customer.
5. Start dunning.
6. Suspend or restrict subscription according to policy.

---

## FR-015 — Pause Subscription

The system shall support:

```http
POST /api/v1/subscriptions/{subscription_id}/pause
```

---

## FR-016 — Resume Subscription

The system shall support:

```http
POST /api/v1/subscriptions/{subscription_id}/resume
```

---

## FR-017 — Cancel Subscription

The system shall support:

```http
POST /api/v1/subscriptions/{subscription_id}/cancel
```

Cancellation shall support:

```text
IMMEDIATE
PERIOD_END
```

---

## FR-018 — Reactivate Subscription

The system shall support:

```http
POST /api/v1/subscriptions/{subscription_id}/reactivate
```

Only eligible subscriptions may be reactivated.

---

## 13. Proration Requirements

## PR-001

Proration calculations shall be deterministic.

## PR-002

The system shall account for:

* Remaining billing period.
* Previous plan.
* New plan.
* Existing credits.
* Existing discounts.
* Tax rules.

## PR-003

The platform shall expose a preview before consequential changes.

Example:

```json
{
  "current_plan": "professional",
  "target_plan": "enterprise",
  "remaining_days": 18,
  "credit": 25.00,
  "prorated_charge": 74.50,
  "tax": 7.45,
  "total_due": 81.95
}
```

Values shall always be calculated server-side.

---

## 14. Preview Requirements

Before major subscription changes, the system shall provide:

```http
POST /api/v1/subscriptions/{id}/preview-change
```

The preview shall include:

* Current subscription.
* Target subscription.
* Financial impact.
* Entitlement impact.
* Usage impact.
* Effective date.
* Billing impact.
* Required approval.
* Policy warnings.

The preview shall not mutate state.

---

## 15. Idempotency Requirements

All subscription mutations shall support idempotency keys.

Examples:

```text
Idempotency-Key: upgrade-org-123-20260828-001
Idempotency-Key: cancel-subscription-456
Idempotency-Key: renewal-subscription-789
```

Repeated requests shall not create duplicate:

* Subscriptions.
* Upgrades.
* Downgrades.
* Renewals.
* Seat charges.
* Add-ons.
* Cancellations.

---

## 16. Concurrency Requirements

The system shall protect against concurrent subscription changes.

Example:

```text
Request A:
Upgrade → Professional → Enterprise

Request B:
Downgrade → Professional → Starter
```

The system shall prevent both operations from silently succeeding against the same subscription version.

The implementation may use:

* Optimistic concurrency.
* Version numbers.
* Compare-and-swap.
* Distributed locks where justified.

---

## 17. Entitlement Requirements

Subscription changes shall update:

```text
Feature Entitlements
AI Model Entitlements
Channel Entitlements
Integration Entitlements
Workflow Entitlements
Storage Limits
API Limits
Seat Limits
Usage Limits
```

Entitlement propagation shall be observable and retryable.

---

## 18. AI Subscription Workflows

## AI-WF-001 — AI Plan Recommendation

```text
Usage
 ↓
Historical Analysis
 ↓
Feature Analysis
 ↓
Budget Analysis
 ↓
Plan Evaluation
 ↓
AI Recommendation
 ↓
Explanation
 ↓
Human/User Confirmation
```

---

## AI-WF-002 — AI Upgrade Automation

```text
Usage Threshold
 ↓
AI Detection
 ↓
Plan Evaluation
 ↓
Cost Forecast
 ↓
Policy Evaluation
 ↓
Risk Evaluation
 ↓
Approval Check
 ↓
Execution
 ↓
Entitlement Update
 ↓
Audit
```

---

## AI-WF-003 — AI Downgrade Recommendation

```text
Usage Analysis
 ↓
Unused Capacity Detection
 ↓
Plan Evaluation
 ↓
Savings Forecast
 ↓
Feature Loss Analysis
 ↓
Recommendation
 ↓
User Confirmation
```

---

## AI-WF-004 — AI Subscription Cancellation

AI may identify cancellation intent.

AI shall not automatically cancel a subscription unless explicitly authorized by policy.

Recommended flow:

```text
Cancellation Intent
 ↓
AI Detection
 ↓
Policy Check
 ↓
Retention Explanation
 ↓
Cancellation Confirmation
 ↓
Human/User Authorization
 ↓
Cancellation
```

---

## 19. AI Guardrails

AI subscription agents shall never:

* Change subscription pricing arbitrarily.
* Change plan definitions.
* Bypass payment requirements.
* Bypass RBAC.
* Cancel another tenant's subscription.
* Modify historical subscription records.
* Create unauthorized credits.
* Increase subscription budgets autonomously.
* Approve their own high-risk actions.
* Modify entitlement policies.
* Modify tax rules.

---

## 20. Human Approval Requirements

High-risk subscription operations may require human approval.

Examples:

```text
Enterprise plan modification
Large subscription expansion
Large custom discount
Large credit
Contract change
Early termination fee waiver
Custom billing interval
Subscription transfer
Manual financial override
```

Approval workflow:

```text
PROPOSED
   ↓
PENDING_APPROVAL
   ↓
APPROVED / REJECTED
   ↓
EXECUTED
   ↓
VERIFIED
```

---

## 21. Subscription Transfer

Where supported, the platform shall allow controlled subscription transfers between:

* Customer accounts.
* Organizations.
* Billing entities.

Transfers shall require:

* Authorization.
* Validation.
* Approval where configured.
* Audit logging.
* Billing reconciliation.
* Entitlement reconciliation.

---

## 22. Subscription Ownership

The system shall maintain explicit relationships:

```text
Subscription
    ↓
Customer Account
    ↓
Organization
    ↓
Billing Profile
```

Changing ownership shall not silently alter historical billing records.

---

## 23. Subscription Security

## SEC-001

All subscription APIs shall require authentication.

## SEC-002

All subscription mutations shall require authorization.

## SEC-003

Tenant isolation shall be enforced server-side.

## SEC-004

Subscription identifiers shall not be treated as authorization credentials.

## SEC-005

Sensitive subscription data shall be encrypted in transit.

## SEC-006

Sensitive data shall be encrypted at rest where applicable.

## SEC-007

Administrative subscription actions shall be audited.

## SEC-008

AI agents shall use scoped credentials.

## SEC-009

Subscription APIs shall enforce rate limits.

## SEC-010

Webhook events shall be authenticated and deduplicated.

---

## 24. Subscription Audit Requirements

Every lifecycle mutation shall record:

```text
audit_id
tenant_id
organization_id
subscription_id
actor_type
actor_id
action
previous_state
new_state
previous_plan
new_plan
previous_seats
new_seats
reason
approval_id
request_id
correlation_id
timestamp
ip_address
user_agent
source
```

---

## 25. Subscription History

The system shall maintain a complete timeline:

```text
2026-01-01
Subscription Created

2026-01-01
Trial Started

2026-01-14
Trial Converted

2026-02-10
Seats Increased

2026-03-01
Plan Upgraded

2026-04-01
Add-On Added

2026-05-15
Cancellation Requested

2026-06-01
Subscription Cancelled
```

Historical events shall remain immutable.

---

## 26. Subscription Analytics

The platform shall calculate:

```text
Active Subscriptions
Trial Subscriptions
New Subscriptions
Upgrades
Downgrades
Cancellations
Renewals
Churn
Expansion Revenue
Contraction Revenue
MRR
ARR
ARPU
Retention
Trial Conversion
Upgrade Rate
Downgrade Rate
Cancellation Rate
Reactivation Rate
```

---

## 27. AI Subscription Analytics

AI shall analyze:

* Churn risk.
* Upgrade probability.
* Downgrade probability.
* Trial conversion probability.
* Expansion potential.
* Subscription anomalies.
* Customer lifetime value.
* Usage-to-plan fit.

AI predictions shall be treated as recommendations rather than authoritative financial state.

---

## 28. Churn Prediction

The system may calculate churn risk using:

* Usage decline.
* Login frequency.
* Feature utilization.
* Support activity.
* Payment failures.
* Subscription age.
* Plan utilization.
* Previous cancellation behavior.

The platform shall distinguish:

```text
Prediction
≠
Fact
```

---

## 29. Subscription Health Score

The platform may calculate:

```text
Subscription Health Score
=
Usage Fit
+
Feature Adoption
+
Payment Reliability
+
Engagement
+
Retention Signals
```

The score shall be explainable.

---

## 30. Subscription Notifications

The platform shall support:

```text
trial_started
trial_expiring
trial_expired
upgrade_completed
downgrade_completed
renewal_upcoming
renewal_completed
renewal_failed
payment_required
cancellation_requested
cancellation_completed
subscription_paused
subscription_resumed
subscription_suspended
usage_limit_approaching
usage_limit_reached
```

---

## 31. Notification Channels

Supported channels may include:

* Email.
* In-app.
* Slack.
* Microsoft Teams.
* Webhooks.
* Customer support channels.

---

## 32. Subscription API Requirements

## Core APIs

```http
GET    /api/v1/subscriptions
POST   /api/v1/subscriptions
GET    /api/v1/subscriptions/{id}
PATCH  /api/v1/subscriptions/{id}
```

## Lifecycle APIs

```http
POST /api/v1/subscriptions/{id}/start
POST /api/v1/subscriptions/{id}/upgrade
POST /api/v1/subscriptions/{id}/downgrade
POST /api/v1/subscriptions/{id}/pause
POST /api/v1/subscriptions/{id}/resume
POST /api/v1/subscriptions/{id}/cancel
POST /api/v1/subscriptions/{id}/reactivate
POST /api/v1/subscriptions/{id}/renew
```

## Preview APIs

```http
POST /api/v1/subscriptions/{id}/preview-change
GET  /api/v1/subscriptions/{id}/history
GET  /api/v1/subscriptions/{id}/usage
GET  /api/v1/subscriptions/{id}/entitlements
```

---

## 33. Subscription API Response Requirements

API responses shall include:

```json
{
  "subscription_id": "sub_xxx",
  "organization_id": "org_xxx",
  "plan_id": "professional",
  "plan_version": "2026-08",
  "status": "active",
  "billing_interval": "monthly",
  "current_period_start": "2026-08-01T00:00:00Z",
  "current_period_end": "2026-09-01T00:00:00Z",
  "cancel_at_period_end": false,
  "seats": {
    "included": 10,
    "active": 7,
    "billable": 10
  },
  "entitlements_version": "ent_123",
  "created_at": "2026-08-01T00:00:00Z",
  "updated_at": "2026-08-28T00:00:00Z"
}
```

---

## 34. Error Handling

Subscription APIs shall return structured errors.

Example:

```json
{
  "error": {
    "code": "SUBSCRIPTION_DOWNGRADE_BLOCKED",
    "message": "The subscription cannot be downgraded while active seats exceed the target plan limit.",
    "request_id": "req_xxx",
    "retryable": false
  }
}
```

---

## 35. Retry Requirements

Retryable subscription operations shall support:

* Exponential backoff.
* Jitter.
* Maximum retry count.
* Dead-letter queues.
* Retry visibility.
* Manual replay.

Non-retryable business validation errors shall not be automatically retried.

---

## 36. Webhook Requirements

The system shall process payment-provider subscription events such as:

```text
subscription.created
subscription.updated
subscription.deleted
subscription.paused
subscription.resumed
subscription.payment_failed
subscription.renewed
```

Processing shall include:

```text
Verify Signature
 ↓
Validate Event
 ↓
Deduplicate
 ↓
Persist Event
 ↓
Process
 ↓
Update Subscription
 ↓
Update Billing
 ↓
Update Entitlements
 ↓
Emit Internal Event
 ↓
Audit
```

---

## 37. Reconciliation Requirements

The system shall reconcile:

```text
Subscription Service
        ↕
Billing Service
        ↕
Payment Provider
        ↕
Entitlement Service
```

The system shall detect:

* Subscription exists but billing record does not.
* Billing record exists but subscription does not.
* Entitlement mismatch.
* Incorrect plan.
* Incorrect seat count.
* Incorrect renewal date.
* Provider mismatch.
* Duplicate subscription.
* Missing cancellation.

---

## 38. Subscription Integrity Rules

The system shall enforce:

```text
One active subscription per billing scope
unless explicitly supported.
```

A tenant shall not accidentally create multiple active subscriptions for the same product scope.

---

## 39. Product Scope

Subscriptions shall support explicit scopes:

```text
ORGANIZATION
WORKSPACE
PRODUCT
MODULE
ENTERPRISE_CONTRACT
```

The scope shall determine entitlement and billing behavior.

---

## 40. Enterprise Subscription Requirements

Enterprise subscriptions shall support:

* Custom plan.
* Custom pricing.
* Custom seat limits.
* Custom usage limits.
* Contract start date.
* Contract end date.
* Renewal terms.
* Minimum commitment.
* Purchase order.
* Custom discounts.
* Custom payment terms.
* Custom entitlements.
* Dedicated billing contacts.

Enterprise changes may require human approval.

---

## 41. Subscription Security Boundaries

The following hierarchy shall be enforced:

```text
Platform
   ↓
Tenant
   ↓
Organization
   ↓
Billing Account
   ↓
Subscription
   ↓
Subscription Items
```

An actor shall only access resources within its authorized scope.

---

## 42. Performance Requirements

## PERF-001

Subscription read APIs should target:

```text
p95 < 300 ms
```

under normal operating conditions.

---

## PERF-002

Subscription mutation APIs should target:

```text
p95 < 1000 ms
```

excluding external provider latency.

---

## PERF-003

Subscription state reads shall be horizontally scalable.

---

## PERF-004

High-volume lifecycle processing shall be asynchronous where appropriate.

---

## 43. Scalability Requirements

The architecture shall support:

```text
10M+ users
1M+ organizations
Millions of subscriptions
Millions of subscription events
High-volume renewal processing
High-volume usage-driven plan changes
```

The system shall support horizontal scaling.

---

## 44. Reliability Requirements

## REL-001

Subscription lifecycle processing shall be durable.

## REL-002

Subscription mutations shall be idempotent.

## REL-003

Subscription events shall be durable.

## REL-004

Provider failures shall not corrupt subscription state.

## REL-005

Failed events shall be recoverable.

## REL-006

Subscription state shall be reconstructable from authoritative records.

---

## 45. Event Processing Guarantees

The platform shall assume at-least-once delivery.

Consumers shall therefore be idempotent.

The system shall not assume:

```text
exactly-once delivery
```

from external systems.

---

## 46. Transactional Outbox

Critical subscription mutations shall use a transactional outbox pattern where appropriate.

Example:

```text
Database Transaction
    |
    +── Subscription Update
    |
    +── Outbox Event
            |
            ▼
        Event Broker
            |
            ▼
        Consumers
```

This prevents subscription state changes from being committed without corresponding events.

---

## 47. Distributed Workflow Requirements

Subscription workflows shall support:

* Correlation IDs.
* Workflow IDs.
* Idempotency keys.
* Retry policies.
* Compensation.
* Timeout handling.
* Dead-letter processing.
* Human intervention.

---

## 48. Compensation Requirements

If a multi-service subscription operation partially fails, the system shall support compensation.

Example:

```text
Upgrade Subscription
       ↓
Payment succeeds
       ↓
Subscription update succeeds
       ↓
Entitlement update fails
       ↓
Retry entitlement update
       ↓
Verify consistency
```

The system shall not blindly reverse financial transactions when a non-financial downstream service temporarily fails.

---

## 49. Subscription Budget Controls

Subscription-level controls shall support:

```text
Monthly Budget
Usage Budget
AI Budget
Workflow Budget
Integration Budget
```

Thresholds may include:

```text
50%
75%
90%
100%
```

Thresholds shall be configurable.

---

## 50. AI Subscription Cost Control

AI shall identify:

* High-cost subscriptions.
* Low-margin subscriptions.
* Excessive model usage.
* Excessive workflow usage.
* Expensive integrations.
* Unexpected usage spikes.

AI may recommend:

* Plan changes.
* Usage restrictions.
* Model optimization.
* Workflow optimization.
* Budget changes.

---

## 51. Human + AI Approval Matrix

| Operation                 |      Human | AI Read | AI Recommend |   AI Execute |
| ------------------------- | ---------: | ------: | -----------: | -----------: |
| View subscription         |        Yes |     Yes |          Yes |          N/A |
| Explain subscription      |        Yes |     Yes |          Yes |          N/A |
| Plan recommendation       |        Yes |     Yes |          Yes |          Yes |
| Usage analysis            |        Yes |     Yes |          Yes |          Yes |
| Upgrade proposal          |        Yes |     Yes |          Yes |          Yes |
| Standard upgrade          |        Yes |     Yes |          Yes | Policy-based |
| Enterprise upgrade        |        Yes |     Yes |          Yes |     Approval |
| Downgrade proposal        |        Yes |     Yes |          Yes |          Yes |
| Standard downgrade        |        Yes |     Yes |          Yes | Policy-based |
| Subscription cancellation |        Yes |     Yes |          Yes |     Approval |
| Subscription pause        |        Yes |     Yes |          Yes | Policy-based |
| Subscription resume       |        Yes |     Yes |          Yes | Policy-based |
| Large seat increase       |        Yes |     Yes |          Yes |     Approval |
| Custom discount           |        Yes |     Yes |          Yes |     Approval |
| Contract modification     |        Yes |     Yes |          Yes |     Approval |
| Historical mutation       | Restricted |      No |           No |           No |

---

## 52. AI Decision Record

Every consequential AI subscription recommendation shall record:

```text
decision_id
agent_id
model_id
model_version
prompt_version
policy_version
subscription_id
tenant_id
recommendation
confidence
risk_level
supporting_signals
approval_required
approval_status
execution_status
created_at
```

---

## 53. AI Explainability

AI subscription recommendations shall explain:

```text
Recommendation
Reason
Supporting Data
Expected Financial Impact
Expected Feature Impact
Risk
Confidence
Alternative Options
```

---

## 54. Observability Requirements

The platform shall expose metrics including:

```text
subscription_creation_rate
subscription_activation_rate
trial_start_rate
trial_conversion_rate
upgrade_rate
downgrade_rate
cancellation_rate
reactivation_rate
renewal_rate
renewal_failure_rate
subscription_api_latency
subscription_api_error_rate
entitlement_sync_failure_rate
provider_sync_failure_rate
subscription_event_lag
subscription_reconciliation_mismatch_rate
```

---

## 55. Distributed Tracing

Every subscription workflow shall propagate:

```text
trace_id
request_id
correlation_id
subscription_id
tenant_id
workflow_id
```

Across:

```text
API Gateway
Subscription Service
Billing Service
Payment Provider
Entitlement Service
Notification Service
AI Services
Workflow Engine
```

---

## 56. Data Model

Core entities shall include:

```text
Subscription
SubscriptionVersion
SubscriptionItem
SubscriptionPlan
PlanVersion
SubscriptionSeat
SubscriptionAddon
Trial
Renewal
Cancellation
SubscriptionChange
SubscriptionEvent
SubscriptionEntitlement
SubscriptionUsageLimit
SubscriptionBudget
SubscriptionDiscount
SubscriptionCredit
SubscriptionApproval
SubscriptionAuditEvent
SubscriptionReconciliationRecord
```

---

## 57. Example Subscription Entity

```json
{
  "subscription_id": "sub_123",
  "tenant_id": "tenant_123",
  "organization_id": "org_123",
  "customer_account_id": "acct_123",
  "plan_id": "professional",
  "plan_version_id": "professional_v3",
  "status": "active",
  "billing_interval": "monthly",
  "quantity": 10,
  "trial": {
    "active": false
  },
  "current_period": {
    "start": "2026-08-01T00:00:00Z",
    "end": "2026-09-01T00:00:00Z"
  },
  "cancel_at_period_end": false,
  "entitlements_version": "ent_v7",
  "version": 14,
  "created_at": "2026-08-01T00:00:00Z",
  "updated_at": "2026-08-28T00:00:00Z"
}
```

---

## 58. Subscription Change Record

Every material change shall create a change record:

```json
{
  "change_id": "chg_123",
  "subscription_id": "sub_123",
  "change_type": "UPGRADE",
  "previous_plan": "starter",
  "new_plan": "professional",
  "previous_seats": 5,
  "new_seats": 10,
  "effective_at": "2026-08-28T00:00:00Z",
  "proration_amount": 45.00,
  "actor_type": "human",
  "actor_id": "user_123",
  "status": "completed"
}
```

---

## 59. Subscription Transfer Workflow

```text
Transfer Request
 ↓
Authorization
 ↓
Eligibility Check
 ↓
Billing Validation
 ↓
Contract Validation
 ↓
Human Approval
 ↓
Subscription Ownership Update
 ↓
Entitlement Reconciliation
 ↓
Billing Reconciliation
 ↓
Notification
 ↓
Audit
```

---

## 60. Subscription Cancellation Workflow

```text
Cancellation Request
 ↓
Authenticate
 ↓
Authorize
 ↓
Eligibility Check
 ↓
Determine Cancellation Type
 ↓
Calculate Financial Impact
 ↓
Determine Effective Date
 ↓
Confirmation
 ↓
Subscription State Update
 ↓
Entitlement Update
 ↓
Billing Update
 ↓
Notification
 ↓
Audit
```

---

## 61. Upgrade Workflow

```text
User / AI Agent
      ↓
Upgrade Request
      ↓
Authorization
      ↓
Plan Validation
      ↓
Usage Validation
      ↓
Pricing Resolution
      ↓
Proration Calculation
      ↓
Tax Calculation
      ↓
Discount / Credit Calculation
      ↓
Payment Validation
      ↓
Approval Check
      ↓
Subscription Update
      ↓
Billing Update
      ↓
Entitlement Update
      ↓
Notification
      ↓
Audit
```

---

## 62. Downgrade Workflow

```text
Downgrade Request
      ↓
Plan Validation
      ↓
Usage Validation
      ↓
Seat Validation
      ↓
Feature Impact Analysis
      ↓
Financial Impact
      ↓
Confirmation
      ↓
Schedule / Execute
      ↓
Entitlement Update
      ↓
Billing Update
      ↓
Notification
      ↓
Audit
```

---

## 63. Renewal Workflow

```text
Renewal Scheduler
      ↓
Subscription Eligibility
      ↓
Plan Resolution
      ↓
Usage Settlement
      ↓
Invoice Generation
      ↓
Payment Attempt
      ↓
Payment Confirmation
      ↓
Subscription Renewal
      ↓
Entitlement Refresh
      ↓
Notification
      ↓
Audit
```

---

## 64. Failed Renewal Workflow

```text
Payment Failure
      ↓
Record Failure
      ↓
Retry Policy
      ↓
Notification
      ↓
Dunning
      ↓
Retry
      ↓
Success ───────────────► ACTIVE
      │
      ▼
Failure
      ↓
Restriction
      ↓
Suspension
```

---

## 65. Trial Workflow

```text
Trial Request
      ↓
Eligibility Validation
      ↓
Trial Creation
      ↓
Trial Entitlements
      ↓
Usage Monitoring
      ↓
Trial Expiration Warning
      ↓
Conversion Decision
      ↓
Payment Validation
      ↓
ACTIVE
```

---

## 66. Subscription Abuse Prevention

The platform shall detect:

* Multiple trial accounts.
* Rapid plan cycling.
* Repeated cancellations.
* Repeated reactivations.
* Coupon abuse.
* Suspicious seat manipulation.
* Automated account creation.
* Unusual subscription patterns.

---

## 67. Subscription Fraud Signals

Signals may include:

```text
Account Age
Payment History
Subscription History
Trial History
Usage Pattern
IP Reputation
Device Signals
Refund History
Plan Cycling
Seat Cycling
```

AI may use these signals to generate risk scores.

---

## 68. Subscription Risk Score

The system may generate:

```text
LOW
MEDIUM
HIGH
CRITICAL
```

Risk scores shall not automatically change subscription state unless explicitly configured by policy.

---

## 69. Subscription SLA Requirements

Critical subscription operations shall provide:

* Deterministic outcomes.
* Request correlation.
* Error visibility.
* Retry visibility.
* Auditability.
* Recovery mechanisms.

---

## 70. Disaster Recovery

The system shall support:

* Database backups.
* Point-in-time recovery.
* Event replay.
* Subscription reconstruction.
* Provider reconciliation.
* Entitlement reconciliation.
* Manual recovery procedures.

Target:

```text
RPO <= 5 minutes
RTO <= 30 minutes
```

for critical subscription infrastructure, subject to deployment architecture.

---

## 71. Compliance Requirements

The subsystem shall be designed to support applicable:

* Privacy requirements.
* Payment security requirements.
* Financial record requirements.
* Data-retention requirements.
* Regional data requirements.
* Enterprise contractual requirements.

---

## 72. Data Retention

Historical subscription records shall be retained according to configured policy.

Deletion of an application user shall not automatically delete required:

* Subscription history.
* Billing references.
* Financial records.
* Audit records.

---

## 73. Testing Requirements

The Subscription Management subsystem shall include:

## Unit Tests

* State transitions.
* Pricing resolution.
* Proration.
* Trial eligibility.
* Seat calculations.
* Cancellation rules.
* Renewal logic.

## Integration Tests

* Billing Service.
* Payment Provider.
* Entitlement Service.
* Notification Service.
* Workflow Engine.

## Security Tests

* RBAC.
* Tenant isolation.
* Privilege escalation.
* API authorization.
* Webhook authentication.

## Reliability Tests

* Duplicate events.
* Provider outage.
* Database failure.
* Queue failure.
* Network timeout.
* Partial workflow failure.

## AI Tests

* Hallucination resistance.
* Authorization bypass resistance.
* Prompt injection resistance.
* Tenant isolation.
* Recommendation correctness.
* High-risk action blocking.

---

## 74. Acceptance Criteria

## AC-001

A user cannot access another organization's subscription.

## AC-002

A subscription cannot be created without valid tenant context.

## AC-003

Duplicate subscription creation requests do not create duplicate active subscriptions.

## AC-004

Subscription state transitions reject invalid transitions.

## AC-005

Plan changes calculate deterministic financial impacts.

## AC-006

Downgrades detect incompatible usage.

## AC-007

Seat reductions cannot silently invalidate active users.

## AC-008

Subscription changes synchronize entitlements.

## AC-009

Subscription changes synchronize billing state.

## AC-010

Payment-provider events are verified and deduplicated.

## AC-011

Subscription renewal is idempotent.

## AC-012

Failed renewals trigger configurable recovery workflows.

## AC-013

Cancellation produces an immutable lifecycle record.

## AC-014

Subscription history remains reconstructable.

## AC-015

AI agents cannot perform unauthorized subscription operations.

## AC-016

High-risk AI subscription operations can require human approval.

## AC-017

AI recommendations are distinguishable from authoritative subscription state.

## AC-018

Every material subscription mutation is auditable.

## AC-019

Subscription state can be reconciled against billing and entitlements.

## AC-020

Subscription service remains recoverable after external provider failure.

## AC-021

Concurrent subscription changes cannot silently overwrite each other.

## AC-022

Historical plan versions remain immutable.

## AC-023

Frontend-provided prices cannot override server-side pricing.

## AC-024

Entitlement synchronization failures are detectable and recoverable.

## AC-025

Subscription analytics are generated from authoritative data.

---

## 75. Definition of Done

The Subscription Management subsystem shall be considered production-ready only when:

* Multi-tenancy is implemented.
* Subscription lifecycle is implemented.
* State-machine validation is implemented.
* Plan versioning is implemented.
* Trial management is implemented.
* Upgrade is implemented.
* Downgrade is implemented.
* Seat management is implemented.
* Add-on management is implemented.
* Billing interval changes are implemented.
* Pause/resume is implemented where supported.
* Cancellation is implemented.
* Reactivation is implemented.
* Renewal is implemented.
* Failed-renewal handling is implemented.
* Proration is deterministic.
* Subscription previews are implemented.
* Idempotency is implemented.
* Concurrency protection is implemented.
* Entitlement synchronization is implemented.
* Billing synchronization is implemented.
* Payment-provider synchronization is implemented.
* Webhook verification is implemented.
* Reconciliation is implemented.
* Audit logging is implemented.
* RBAC is implemented.
* AI guardrails are implemented.
* AI recommendation logging is implemented.
* Human approval workflows are implemented.
* Subscription analytics are implemented.
* Fraud/abuse detection is implemented.
* Observability is implemented.
* Distributed tracing is implemented.
* Disaster recovery is tested.
* Security testing is completed.
* Load testing is completed.
* Failure-mode testing is completed.
* AI safety testing is completed.
* Tenant-isolation testing is completed.

---

## 76. FAANG-Level Engineering Principles

The SalesGenie Subscription Management subsystem shall follow these principles:

1. **Subscription state has one authoritative owner.**
2. **Financial correctness takes precedence over UI convenience.**
3. **All mutations are authenticated and authorized.**
4. **Tenant isolation is enforced server-side.**
5. **Every financial-impacting operation is idempotent.**
6. **Subscription lifecycle is represented by explicit state machines.**
7. **Historical subscription state is reconstructable.**
8. **Plan versions are immutable.**
9. **Frontend values are never authoritative for pricing.**
10. **Concurrent modifications are explicitly controlled.**
11. **Critical events use durable event delivery.**
12. **Transactional outbox is used for critical state/event consistency.**
13. **External providers are treated as unreliable dependencies.**
14. **Webhook processing is authenticated and idempotent.**
15. **Entitlement propagation is observable and recoverable.**
16. **Reconciliation is a first-class capability.**
17. **AI recommendations are separated from authoritative subscription state.**
18. **AI financial actions are governed by explicit policies.**
19. **High-risk AI actions require configurable human approval.**
20. **AI cannot approve its own consequential actions.**
21. **All material subscription actions are auditable.**
22. **Distributed workflows use correlation and idempotency identifiers.**
23. **Partial failures are handled through retry and compensation.**
24. **No silent subscription mutations are permitted.**
25. **Subscription state must remain explainable, traceable, reproducible, and recoverable.**
