# SalesGenie — Upgrade & Downgrade Management Requirements

**Document:** `upgrade_downgrade.md`  
**Product:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Requirement Level:** FAANG-Level / Production-Grade SaaS  
**Scope:** Subscription Plan Upgrade, Downgrade, Plan Transition, Entitlement Reconciliation, Billing Proration, Quota Reconciliation, AI/Human Workflows  
**Actors:** End Users, Sales Agents, Support Agents, Managers, Organization Admins, Billing Admins, Super Admins, AI Agents, System Services

---

## 1. Purpose

SalesGenie shall provide a reliable, auditable, secure, and policy-driven subscription plan transition system supporting:

- Free → Paid upgrades
- Monthly → Yearly upgrades
- Lower → Higher tier upgrades
- Higher → Lower tier downgrades
- Yearly → Monthly transitions
- Paid → Free transitions
- Immediate upgrades
- End-of-billing-cycle downgrades
- Scheduled plan changes
- Proration
- Credits
- Quota reconciliation
- Feature entitlement changes
- AI-agent entitlement changes
- Human-user entitlement changes
- Integration entitlement changes
- Usage-limit reconciliation
- Payment validation
- Failed-payment handling
- Grace periods
- Cancellation/reversal
- Upgrade/downgrade previews
- Approval workflows
- Enterprise plan transitions
- Full auditability

The system shall preserve billing correctness, prevent privilege escalation, prevent quota bypasses, avoid data loss, and maintain consistent subscription state across all SalesGenie microservices.

---

## 2. Product Context

SalesGenie is a multi-tenant enterprise AI platform containing:

- Multi-agent AI orchestration
- AI customer support agents
- AI sales agents
- Human support agents
- Human sales agents
- RAG knowledge bases
- Lead generation
- Lead intelligence
- Omnichannel communication
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
- Workflow automation
- MCP tools
- External data sources
- Usage-based AI consumption
- Subscription billing
- Metered billing
- Credits
- Coupons
- Invoices
- Taxes
- Payment processing
- Billing analytics

Plan changes therefore affect multiple distributed services and must be treated as a cross-service state transition.

---

## 3. Actors

## 3.1 Human Actors

### H-01 End User

A customer using SalesGenie services under an organization's subscription.

### H-02 Sales Agent

A human sales representative using SalesGenie for lead management, prospecting, communication, and AI-assisted sales.

### H-03 Support Agent

A human customer-support representative using SalesGenie for conversations, ticket handling, and escalation.

### H-04 Manager

A supervisor responsible for team usage, performance, and operational oversight.

### H-05 Organization Admin

The primary administrator responsible for organization configuration and subscription management.

### H-06 Billing Admin

A user authorized to manage payment methods, subscriptions, invoices, credits, refunds, and plan transitions.

### H-07 Super Admin

A platform-level administrator with cross-tenant operational capabilities subject to strict authorization and audit policies.

---

## 3.2 AI Actors

### AI-01 AI Sales Agent

An autonomous or semi-autonomous agent performing sales-related operations.

### AI-02 AI Support Agent

An autonomous or semi-autonomous agent handling customer support.

### AI-03 AI Workflow Agent

An agent capable of executing configured workflows and automation tasks.

### AI-04 AI Billing Assistant

An AI assistant capable of explaining subscription changes and preparing plan-transition actions but not bypassing authorization.

### AI-05 AI Usage Optimization Agent

An AI component that analyzes consumption and recommends upgrades, downgrades, or configuration changes.

### AI-06 AI Entitlement Enforcement Agent

A policy-aware runtime component that verifies whether AI operations are permitted under the organization's active subscription.

---

## 4. Core Business Principles

1. Every organization shall have exactly one authoritative subscription state.
2. Subscription state shall be tenant-scoped.
3. Plan changes shall be authorization-controlled.
4. Billing state shall never be determined solely by frontend state.
5. Entitlements shall be derived from authoritative backend subscription state.
6. Upgrade and downgrade calculations shall be deterministic.
7. Financial calculations shall use fixed-precision monetary arithmetic.
8. Usage calculations shall be idempotent.
9. Plan transitions shall be auditable.
10. Downgrades shall not silently destroy customer data.
11. Features removed by a downgrade shall enter a controlled restricted state where necessary.
12. AI agents shall never independently modify billing state without explicit authorization.
13. Human approval shall be required where organizational policy requires it.
14. Payment-provider events shall be treated as asynchronous and potentially duplicated.
15. Webhooks shall be idempotent.
16. Failed transitions shall be recoverable.
17. Subscription state and entitlement state shall eventually converge across services.
18. Security controls shall remain active regardless of plan.
19. Regulatory and financial records shall not be deleted because of a downgrade.
20. The system shall provide users with a transparent preview before material plan changes.

---

## 5. User Requirements

## UR-001 — View Current Subscription

Users with billing permissions shall be able to view:

- Current plan
- Billing interval
- Subscription status
- Current billing period
- Renewal date
- Current usage
- Plan limits
- Feature entitlements
- AI-agent limits
- Human-user limits
- Integration limits
- Remaining quotas
- Overage information
- Scheduled plan changes
- Payment status

---

## UR-002 — Compare Plans

Authorized users shall be able to compare available plans based on:

- Price
- Billing interval
- AI usage
- Human seats
- AI agents
- Workflow limits
- RAG limits
- Knowledge-base limits
- Lead-generation limits
- Communication channels
- Integration availability
- API access
- MCP access
- Analytics
- Security capabilities
- Enterprise capabilities

---

## UR-003 — Preview Upgrade

Before confirming an upgrade, users shall receive:

- Current plan
- Target plan
- Price difference
- Proration
- Credits
- Taxes
- Discounts
- Effective date
- New limits
- New entitlements
- Removed restrictions
- Next billing amount
- Next billing date

---

## UR-004 — Preview Downgrade

Before confirming a downgrade, users shall receive:

- Current plan
- Target plan
- Effective date
- Expected billing change
- Feature removals
- Limit reductions
- User-seat impact
- AI-agent impact
- Integration impact
- Usage impact
- Data-retention implications
- Scheduled transition details

---

## UR-005 — Upgrade Subscription

Authorized billing users shall be able to upgrade their subscription.

---

## UR-006 — Downgrade Subscription

Authorized billing users shall be able to request a downgrade subject to:

- Plan policy
- Billing policy
- Usage constraints
- Organizational approval requirements
- Contract restrictions
- Enterprise rules

---

## UR-007 — Immediate Upgrade

The system shall support immediate upgrades where the billing provider and subscription policy permit.

---

## UR-008 — Scheduled Downgrade

The system shall support downgrades that become effective at the end of the current billing period.

---

## UR-009 — Cancel Scheduled Change

Authorized users shall be able to cancel a scheduled downgrade before its effective date.

---

## UR-010 — Change Billing Interval

Authorized users shall be able to transition between:

- Monthly
- Yearly

subject to pricing and billing policy.

---

## UR-011 — Understand Proration

Users shall be able to view how a plan transition affects:

- Current-period charges
- Credits
- Taxes
- Discounts
- Next invoice

---

## UR-012 — Preserve Existing Data

Users shall not lose historical:

- Conversations
- Leads
- Contacts
- Tickets
- Knowledge documents
- Workflows
- Audit logs
- Billing records
- Invoices
- Usage history

solely because of a plan downgrade.

---

## UR-013 — Understand Restricted Features

When a downgrade removes a feature, users shall be informed:

- Which feature is affected
- Why it is affected
- When restriction begins
- What data remains accessible
- What actions are disabled
- How to upgrade again

---

## UR-014 — Seat Reduction

Organization administrators shall be able to reduce human-user seats where supported.

The system shall prevent reducing seats below the number of active users when policy requires it.

---

## UR-015 — AI Agent Reduction

Organization administrators shall be able to reduce AI-agent capacity subject to active configuration and plan limits.

---

## UR-016 — Quota Reconciliation

The system shall transparently explain how existing usage is handled after a plan transition.

---

## UR-017 — Payment Validation

Users shall be notified when an upgrade cannot proceed because of:

- Missing payment method
- Invalid payment method
- Failed payment
- Payment-provider rejection
- Billing account restrictions

---

## UR-018 — Failed Transition Visibility

Users shall receive a clear status when a transition:

- Succeeds
- Fails
- Is pending
- Is scheduled
- Requires approval
- Requires payment action

---

## UR-019 — Billing History

Users with appropriate permissions shall be able to view historical plan transitions.

---

## UR-020 — Audit Visibility

Authorized administrators shall be able to view:

- Who initiated the change
- Who approved it
- Previous plan
- New plan
- Timestamp
- Effective timestamp
- Billing calculation
- Reason
- Result
- Failure information

---

## 6. AI User Requirements

## AI-UR-001 — AI Plan Recommendation

The AI usage optimization agent shall recommend plan changes based on:

- Historical usage
- Forecasted usage
- Feature utilization
- AI-token consumption
- Human-seat utilization
- Integration utilization
- Workflow utilization
- Cost efficiency

AI recommendations shall not automatically change the subscription unless explicitly authorized.

---

## AI-UR-002 — AI Upgrade Explanation

The AI billing assistant shall explain why a higher plan may be beneficial using actual tenant usage.

---

## AI-UR-003 — AI Downgrade Risk Detection

The AI system shall detect potential downgrade risks including:

- Active features exceeding target limits
- AI agents exceeding target limits
- Users exceeding seat limits
- Workflows exceeding target limits
- Knowledge bases exceeding target limits
- Integration dependencies
- Usage exceeding target quotas

---

## AI-UR-004 — AI Transition Preparation

The AI billing assistant may prepare a proposed plan transition for human approval.

It shall not:

- Bypass authorization
- Modify billing records directly
- Change payment methods
- Override pricing
- Override quotas
- Disable security controls

---

## AI-UR-005 — AI Cost Forecasting

The system shall forecast expected cost after a plan change using historical usage where sufficient data exists.

---

## AI-UR-006 — AI Entitlement Awareness

AI agents shall receive current entitlement information before executing actions requiring subscription permissions.

---

## AI-UR-007 — AI Graceful Degradation

When an AI agent loses access to a feature because of a plan change, it shall:

1. Detect entitlement denial.
2. Stop unauthorized execution.
3. Preserve conversation context where possible.
4. Explain the limitation.
5. Suggest an allowed alternative.
6. Escalate to a human when appropriate.

---

## 7. System Requirements

## SR-001 — Multi-Tenant Subscription Isolation

The system shall isolate:

- Subscription records
- Billing records
- Usage
- Entitlements
- Plan transitions
- Payment data
- Audit logs

by tenant.

---

## SR-002 — Subscription State Machine

The platform shall implement an explicit subscription state machine.

Supported states shall include:

```text
ACTIVE
UPGRADE_PENDING
UPGRADE_PROCESSING
UPGRADE_FAILED
DOWNGRADE_SCHEDULED
DOWNGRADE_PROCESSING
DOWNGRADE_FAILED
PAYMENT_REQUIRED
PAST_DUE
GRACE_PERIOD
SUSPENDED
CANCELED
EXPIRED
```

---

## SR-003 — Authoritative Subscription Service

One authoritative billing/subscription service shall own subscription state.

Other services shall consume subscription events rather than independently modifying subscription state.

---

## SR-004 — Entitlement Service

A centralized entitlement service shall derive effective permissions from:

```text
Tenant
+
Subscription
+
Plan
+
Add-ons
+
Usage
+
Policy
+
Feature flags
```

---

## SR-005 — Transactional Plan Transition

A plan transition shall execute through a durable workflow rather than relying on a single synchronous HTTP request.

---

## SR-006 — Idempotency

Every plan-transition request shall support an idempotency key.

Repeated requests with the same idempotency key shall not create duplicate:

* Charges
* Subscriptions
* Invoices
* Credits
* Plan transitions

---

## SR-007 — Distributed Consistency

The platform shall use event-driven propagation for subscription changes.

Example:

```text
Billing Service
      |
      v
Subscription Updated Event
      |
      +----> Entitlement Service
      |
      +----> Usage Service
      |
      +----> AI Gateway
      |
      +----> Agent Runtime
      |
      +----> Integration Service
      |
      +----> Analytics
      |
      +----> Notification Service
```

---

## SR-008 — Versioned Plan Definitions

Plans shall be immutable or versioned.

Historical invoices and transitions shall retain the exact plan version used for calculation.

---

## SR-009 — Monetary Precision

All monetary calculations shall use fixed-precision decimal arithmetic.

Floating-point arithmetic shall not be used for financial settlement calculations.

---

## SR-010 — Currency Support

The billing system shall maintain:

* Currency
* Amount
* Tax
* Discount
* Credit
* Net charge
* Gross charge

as explicit fields.

---

## SR-011 — Time Zone Handling

Billing periods shall be calculated using canonical timestamps and explicit timezone policies.

---

## SR-012 — Clock Safety

The system shall use server-authoritative time for:

* Billing periods
* Effective dates
* Proration
* Scheduled downgrades
* Trial expiration
* Grace periods

---

## SR-013 — Payment Provider Abstraction

The system shall support payment-provider abstraction so that subscription logic is not tightly coupled to a single payment provider.

---

## SR-014 — Webhook Reconciliation

Provider webhooks shall be:

* Authenticated
* Validated
* Deduplicated
* Persisted
* Processed asynchronously
* Reconciled against internal state

---

## SR-015 — Entitlement Cache

Entitlements may be cached for performance but shall support:

* TTL
* Versioning
* Immediate invalidation
* Event-based refresh

---

## SR-016 — Fail-Closed Authorization

When entitlement state cannot be safely determined for a privileged operation, the system shall fail closed.

---

## SR-017 — Billing Records Immutability

Finalized invoices, payment records, refunds, and financial ledger entries shall be immutable.

Corrections shall use compensating records.

---

## SR-018 — Audit Trail

Every plan transition shall generate immutable audit events.

---

## SR-019 — Observability

The system shall provide:

* Structured logs
* Metrics
* Distributed traces
* Transition latency
* Failure rates
* Payment failures
* Entitlement propagation latency
* Webhook processing metrics

---

## SR-020 — Disaster Recovery

Subscription state and financial records shall be recoverable following service failures.

---

## 8. Functional Requirements

## 8.1 Plan Upgrade

## FR-UP-001 — Upgrade Initiation

The system shall accept an upgrade request containing:

```text
tenant_id
current_subscription_id
target_plan_id
billing_interval
payment_method_id
coupon_id
idempotency_key
requested_by
```

---

## FR-UP-002 — Authorization Validation

The system shall verify that the requesting user has permission to modify the subscription.

---

## FR-UP-003 — Subscription Validation

The system shall verify:

* Subscription exists
* Tenant matches
* Subscription is active
* Target plan is available
* Billing account is valid

---

## FR-UP-004 — Payment Validation

The system shall validate payment readiness before finalizing an upgrade requiring payment.

---

## FR-UP-005 — Upgrade Calculation

The system shall calculate:

```text
Target Price
- Existing Period Credit
- Applicable Coupon
+ Taxes
+ Applicable Usage Charges
= Upgrade Charge
```

---

## FR-UP-006 — Upgrade Preview

The system shall return a deterministic preview before confirmation.

---

## FR-UP-007 — Upgrade Confirmation

After confirmation, the system shall create a durable transition record.

---

## FR-UP-008 — Payment Processing

The system shall initiate payment using the configured payment provider.

---

## FR-UP-009 — Upgrade Activation

Upon successful payment or authorized provider confirmation, the target plan shall become active according to policy.

---

## FR-UP-010 — Entitlement Expansion

The entitlement service shall activate newly available:

* Features
* AI agents
* Human seats
* Integrations
* Workflows
* API limits
* MCP tools
* RAG capacity
* Lead-generation capacity

---

## 8.2 Plan Downgrade

## FR-DOWN-001 — Downgrade Request

The system shall accept downgrade requests from authorized users.

---

## FR-DOWN-002 — Downgrade Compatibility Check

The system shall evaluate whether current usage exceeds target-plan limits.

---

## FR-DOWN-003 — Downgrade Conflict Detection

The system shall detect conflicts involving:

* User seats
* AI agents
* Active workflows
* Integrations
* Knowledge bases
* Storage
* Lead capacity
* API usage
* Messaging channels

---

## FR-DOWN-004 — Downgrade Scheduling

The system shall support scheduling the downgrade for the end of the current billing period.

---

## FR-DOWN-005 — Immediate Downgrade Policy

Immediate downgrades shall only be allowed when explicitly supported by billing policy.

---

## FR-DOWN-006 — Downgrade Effective Date

The system shall calculate and persist the effective timestamp.

---

## FR-DOWN-007 — Downgrade Notification

The system shall notify relevant users about:

* Scheduled downgrade
* Effective date
* Features affected
* Required remediation

---

## FR-DOWN-008 — Downgrade Execution

At the effective time, the system shall:

1. Validate subscription state.
2. Recalculate entitlements.
3. Reconcile quotas.
4. Apply target plan.
5. Restrict newly unavailable capabilities.
6. Preserve historical data.
7. Emit subscription events.
8. Record audit events.

---

## 8.3 Monthly ↔ Yearly Transitions

## FR-INT-001

The system shall support monthly-to-yearly transitions.

## FR-INT-002

The system shall support yearly-to-monthly transitions.

## FR-INT-003

The system shall calculate interval-specific pricing.

## FR-INT-004

The system shall calculate credits for unused subscription time according to billing policy.

## FR-INT-005

The system shall clearly display the new renewal date.

---

## 8.4 Plan Transition Preview

## FR-PREV-001

The preview API shall return:

```json
{
  "current_plan": {},
  "target_plan": {},
  "current_period": {},
  "effective_date": "",
  "proration": {},
  "credits": {},
  "discounts": {},
  "taxes": {},
  "amount_due": {},
  "next_invoice_estimate": {},
  "entitlement_changes": {},
  "usage_impact": {},
  "warnings": []
}
```

---

## 8.5 Quota Reconciliation

## FR-QUOTA-001

The system shall compare current consumption against target-plan quotas.

## FR-QUOTA-002

The system shall identify:

```text
Within Limit
At Limit
Over Limit
```

## FR-QUOTA-003

Existing historical usage shall remain immutable.

## FR-QUOTA-004

Future usage enforcement shall use the new plan.

## FR-QUOTA-005

The system shall prevent quota reset exploits through repeated upgrades/downgrades.

---

## 8.6 Feature Entitlement Reconciliation

## FR-ENT-001

Every plan transition shall generate an entitlement delta.

Example:

```text
CURRENT:
AI Agents = 10
Human Seats = 20
Integrations = 15
Workflows = 100

TARGET:
AI Agents = 5
Human Seats = 10
Integrations = 8
Workflows = 50
```

The system shall calculate:

```text
AI Agents: -5
Human Seats: -10
Integrations: -7
Workflows: -50
```

---

## FR-ENT-002

Feature removals shall not automatically delete data.

---

## FR-ENT-003

The platform shall distinguish:

```text
Feature Disabled
Feature Restricted
Data Retained
Data Deleted
```

---

## FR-ENT-004

AI agents shall verify entitlement before executing restricted capabilities.

---

## 8.7 Human Seat Management

## FR-SEAT-001

The system shall track:

```text
Purchased Seats
Assigned Seats
Active Seats
Inactive Seats
Available Seats
```

---

## FR-SEAT-002

Downgrades shall prevent active-seat count from exceeding target capacity where policy requires it.

---

## FR-SEAT-003

The system shall offer remediation options:

* Deactivate users
* Remove users
* Increase plan
* Keep scheduled downgrade pending

---

## 8.8 AI Agent Capacity

## FR-AI-001

The system shall track AI-agent capacity per tenant.

## FR-AI-002

The system shall prevent creation of AI agents beyond plan limits.

## FR-AI-003

A downgrade shall identify AI agents exceeding the new limit.

## FR-AI-004

The platform shall not silently delete AI agents.

## FR-AI-005

Excess agents shall transition to a controlled state such as:

```text
ACTIVE
RESTRICTED
DISABLED_PENDING_REVIEW
DISABLED
```

---

## 8.9 Workflow Management

## FR-WF-001

The system shall identify workflows dependent on features removed by a downgrade.

## FR-WF-002

Affected workflows shall be marked as:

```text
ACTIVE
DEGRADED
BLOCKED
```

## FR-WF-003

The platform shall preserve workflow definitions.

---

## 8.10 Integration Management

## FR-INTG-001

The system shall identify integrations unavailable under the target plan.

## FR-INTG-002

The system shall not revoke credentials merely because a feature becomes unavailable.

## FR-INTG-003

Integration execution shall be blocked when the entitlement is inactive.

## FR-INTG-004

Integration configuration shall remain recoverable after re-upgrade where policy permits.

---

## 8.11 AI Workflow Safety

## FR-AIWF-001

AI agents shall retrieve current subscription entitlements before invoking privileged tools.

## FR-AIWF-002

AI agents shall not infer entitlement from conversation text.

## FR-AIWF-003

AI agents shall not modify subscription plans without an authorized billing action.

## FR-AIWF-004

AI agents shall request human approval when organizational policy requires it.

---

## 8.12 Approval Workflow

## FR-APP-001

Organizations shall be able to configure approval requirements.

Examples:

```text
Upgrade < $500 → automatic
Upgrade >= $500 → manager approval
Downgrade → billing-admin approval
Enterprise change → finance approval
```

---

## FR-APP-002

Approval requests shall include:

* Requester
* Current plan
* Target plan
* Estimated cost
* Effective date
* Reason
* Entitlement impact

---

## FR-APP-003

Approvals shall be immutable and auditable.

---

## 8.13 Scheduled Transition Engine

## FR-SCHED-001

The system shall persist scheduled plan changes.

## FR-SCHED-002

A background worker shall process due transitions.

## FR-SCHED-003

Workers shall use distributed locking or equivalent concurrency control.

## FR-SCHED-004

Processing shall be idempotent.

## FR-SCHED-005

Failed transitions shall be retried according to policy.

---

## 8.14 Retry and Recovery

## FR-REC-001

Transient failures shall use exponential backoff.

## FR-REC-002

Permanent failures shall enter a dead-letter or recovery queue.

## FR-REC-003

Operators shall be able to replay recoverable transition events.

## FR-REC-004

Replay shall not duplicate financial transactions.

---

## 8.15 Cancellation of Scheduled Downgrade

## FR-CANCEL-001

Authorized users shall be able to cancel a scheduled downgrade.

## FR-CANCEL-002

Cancellation shall stop future downgrade execution.

## FR-CANCEL-003

The cancellation shall generate an audit event.

---

## 8.16 Upgrade After Scheduled Downgrade

## FR-CANCEL-004

If a customer upgrades while a downgrade is scheduled, the system shall reconcile both transitions.

Expected behavior:

```text
Scheduled Downgrade
        |
        v
Upgrade Requested
        |
        v
Cancel/Replace Downgrade
        |
        v
Activate New Plan
```

---

## 8.17 Payment Failure

## FR-PAY-001

If upgrade payment fails, the system shall not activate paid entitlements unless policy explicitly permits them.

## FR-PAY-002

The user shall receive payment-failure information.

## FR-PAY-003

The system shall support retry.

## FR-PAY-004

Repeated payment failures shall transition the subscription according to billing policy.

---

## 8.18 Webhook Processing

## FR-WEBHOOK-001

The system shall validate provider webhook authenticity.

## FR-WEBHOOK-002

The system shall store webhook event IDs.

## FR-WEBHOOK-003

Duplicate webhook events shall not create duplicate transitions.

## FR-WEBHOOK-004

Out-of-order webhook events shall be reconciled using provider timestamps/versioning.

---

## 8.19 Notification System

## FR-NOTIFY-001

The system shall notify users when:

* Upgrade succeeds
* Upgrade fails
* Downgrade is scheduled
* Downgrade occurs
* Downgrade fails
* Payment fails
* Plan limits change
* Features become restricted

---

## 8.20 Audit Logging

## FR-AUDIT-001

Each plan change shall create an immutable audit record containing:

```text
event_id
tenant_id
actor_id
actor_type
source
old_plan
new_plan
old_subscription_state
new_subscription_state
requested_at
effective_at
completed_at
reason
approval_id
payment_reference
idempotency_key
result
failure_code
```

---

## 9. API Requirements

## API-001 — Preview Upgrade

```http
POST /api/v1/billing/subscriptions/upgrade/preview
```

---

## API-002 — Confirm Upgrade

```http
POST /api/v1/billing/subscriptions/upgrade
```

---

## API-003 — Preview Downgrade

```http
POST /api/v1/billing/subscriptions/downgrade/preview
```

---

## API-004 — Schedule Downgrade

```http
POST /api/v1/billing/subscriptions/downgrade
```

---

## API-005 — Cancel Scheduled Change

```http
POST /api/v1/billing/subscriptions/change/cancel
```

---

## API-006 — Current Subscription

```http
GET /api/v1/billing/subscriptions/current
```

---

## API-007 — Plan Transition History

```http
GET /api/v1/billing/subscriptions/transitions
```

---

## API-008 — Transition Status

```http
GET /api/v1/billing/subscriptions/transitions/{transition_id}
```

---

## 10. AI Tool Requirements

AI agents may expose tools such as:

```text
get_current_subscription
compare_subscription_plans
preview_plan_upgrade
preview_plan_downgrade
get_usage_summary
get_entitlements
get_downgrade_impact
estimate_subscription_cost
request_plan_change
get_transition_status
cancel_scheduled_downgrade
```

AI tools shall enforce the same backend authorization as human-facing APIs.

---

## 11. AI Tool Security Requirements

AI agents shall never receive unrestricted billing capabilities.

Dangerous operations shall require:

```text
Identity Verification
+
Tenant Validation
+
Authorization
+
Policy Validation
+
Explicit Confirmation
+
Idempotency
+
Audit Logging
```

---

## 12. Non-Functional Requirements

## NFR-001 — Availability

Subscription and entitlement services shall target high availability suitable for enterprise SaaS workloads.

---

## NFR-002 — Consistency

Financial state shall be strongly consistent within the authoritative billing service.

Entitlement propagation may be eventually consistent but shall have measurable convergence guarantees.

---

## NFR-003 — Performance

Plan preview operations should normally complete within interactive API latency budgets.

Long-running payment/provider operations shall be asynchronous.

---

## NFR-004 — Scalability

The architecture shall support:

* Millions of tenants
* High-volume usage events
* High-volume subscription events
* Concurrent AI workloads
* Large numbers of scheduled transitions

---

## NFR-005 — Security

The system shall implement:

* RBAC
* Tenant isolation
* Least privilege
* Encryption in transit
* Encryption at rest
* Secure secrets management
* Audit logging
* API authentication
* Authorization checks
* Rate limiting

---

## NFR-006 — Reliability

The system shall tolerate:

* Duplicate requests
* Duplicate webhooks
* Network failures
* Worker crashes
* Payment-provider downtime
* Service restarts
* Partial event delivery

---

## NFR-007 — Observability

Metrics shall include:

```text
upgrade_requests_total
upgrade_success_total
upgrade_failure_total
downgrade_requests_total
downgrade_success_total
downgrade_failure_total
scheduled_transitions_total
transition_latency_seconds
payment_failure_total
entitlement_sync_failures_total
webhook_duplicates_total
webhook_processing_failures_total
```

---

## 13. Security Requirements

## SEC-001

Only authorized billing roles may initiate subscription changes.

## SEC-002

Every request shall be tenant-scoped.

## SEC-003

JWT claims shall not be treated as the sole source of entitlement truth.

## SEC-004

Backend authorization shall be mandatory even when the frontend hides unavailable controls.

## SEC-005

Subscription transitions shall be protected against replay attacks.

## SEC-006

Idempotency keys shall have controlled expiration and storage.

## SEC-007

Payment-provider credentials shall never be exposed to AI agents or frontend clients.

## SEC-008

Sensitive billing information shall not be written to application logs.

## SEC-009

AI agents shall not be permitted to bypass approval workflows.

---

## 14. Data Model Requirements

## Subscription

```text
subscription_id
tenant_id
plan_id
plan_version
billing_interval
status
provider
provider_subscription_id
current_period_start
current_period_end
renewal_at
scheduled_plan_id
scheduled_change_at
created_at
updated_at
version
```

## Plan Transition

```text
transition_id
tenant_id
subscription_id
transition_type
source_plan_id
target_plan_id
source_plan_version
target_plan_version
requested_by
approved_by
status
effective_at
requested_at
completed_at
idempotency_key
payment_reference
proration_amount
credit_amount
discount_amount
tax_amount
final_amount
failure_code
failure_reason
created_at
updated_at
```

## Entitlement Snapshot

```text
tenant_id
subscription_id
plan_id
plan_version
feature_entitlements
usage_limits
seat_limits
ai_agent_limits
integration_limits
workflow_limits
effective_at
version
```

---

## 15. Event Requirements

The platform shall publish events including:

```text
subscription.upgrade.requested
subscription.upgrade.approved
subscription.upgrade.completed
subscription.upgrade.failed

subscription.downgrade.requested
subscription.downgrade.scheduled
subscription.downgrade.canceled
subscription.downgrade.completed
subscription.downgrade.failed

subscription.billing_interval.changed

subscription.entitlements.changed
subscription.usage_limits.changed
subscription.payment.required
subscription.payment.failed
subscription.payment.succeeded
```

---

## 16. Event Processing Requirements

Every consumer shall support:

* Idempotent processing
* Event versioning
* Retry
* Dead-letter handling
* Observability
* Correlation IDs
* Tenant context propagation

---

## 17. Downgrade Data Safety

The system shall follow this hierarchy:

```text
Plan Limit Reduced
        |
        v
Detect Excess Resources
        |
        v
Notify Customer
        |
        v
Restrict New Creation
        |
        v
Preserve Existing Data
        |
        v
Allow Remediation
        |
        +----> Upgrade
        |
        +----> Reduce Usage
        |
        +----> Archive
```

The system shall never silently delete customer-owned data merely because of a subscription downgrade.

---

## 18. Example Upgrade Workflow

```text
Human User
    |
    v
Select Target Plan
    |
    v
Preview Upgrade
    |
    v
Calculate Price
    |
    v
Calculate Proration
    |
    v
Calculate Tax
    |
    v
Validate Payment
    |
    v
Confirm
    |
    v
Create Transition
    |
    v
Process Payment
    |
    v
Activate Subscription
    |
    v
Update Entitlements
    |
    v
Update Quotas
    |
    v
Notify Services
    |
    v
Audit Event
```

---

## 19. Example Downgrade Workflow

```text
Human User
    |
    v
Select Target Plan
    |
    v
Preview Downgrade
    |
    v
Analyze Usage
    |
    v
Detect Conflicts
    |
    v
Display Impact
    |
    v
Confirm
    |
    v
Schedule Downgrade
    |
    v
Current Period Ends
    |
    v
Execute Transition
    |
    v
Reconcile Entitlements
    |
    v
Restrict Excess Capabilities
    |
    v
Preserve Data
    |
    v
Publish Events
    |
    v
Audit
```

---

## 20. AI-Assisted Upgrade Workflow

```text
AI Usage Agent
      |
      v
Analyze Historical Usage
      |
      v
Forecast Future Usage
      |
      v
Compare Plans
      |
      v
Generate Recommendation
      |
      v
Human Review
      |
      v
Preview
      |
      v
Explicit Confirmation
      |
      v
Billing API
      |
      v
Authorization
      |
      v
Payment
      |
      v
Plan Transition
```

AI recommendation shall remain advisory until an authorized user confirms the transaction.

---

## 21. AI-Assisted Downgrade Workflow

```text
AI Usage Agent
      |
      v
Analyze Current Consumption
      |
      v
Identify Lower-Cost Plan
      |
      v
Analyze Downgrade Risks
      |
      v
Generate Impact Report
      |
      v
Human Approval
      |
      v
Schedule Downgrade
      |
      v
System Executes
      |
      v
Entitlement Reconciliation
```

---

## 22. Human + AI Collaboration Requirements

## COLLAB-001

AI may recommend a plan change.

## COLLAB-002

Human administrators may approve or reject AI recommendations.

## COLLAB-003

AI shall explain recommendation rationale.

## COLLAB-004

Humans shall remain accountable for high-impact financial actions.

## COLLAB-005

The system shall record whether a transition originated from:

```text
HUMAN
AI_RECOMMENDATION
API
AUTOMATION
ADMIN_OVERRIDE
```

---

## 23. Super Admin Requirements

Super Admins shall be able to:

* View subscription transitions
* Investigate failures
* Inspect entitlement mismatches
* Replay failed events
* View audit records
* View payment-provider synchronization state
* Resolve operational inconsistencies

Super Admins shall not bypass financial controls without explicit privileged override mechanisms.

All overrides shall be strongly audited.

---

## 24. Edge Cases

The system shall handle:

1. Upgrade request during an existing downgrade schedule.
2. Downgrade request during payment failure.
3. Duplicate upgrade request.
4. Duplicate webhook.
5. Out-of-order webhook.
6. Payment provider timeout.
7. User losing billing permission during transition.
8. Subscription canceled while transition is processing.
9. Plan becoming unavailable while transition is pending.
10. Coupon expiring during transition.
11. Tax configuration changing during transition.
12. Currency mismatch.
13. Existing usage exceeding target plan.
14. Active AI agents exceeding target plan.
15. Active users exceeding target seat count.
16. Active workflows exceeding target limits.
17. Integration becoming unavailable.
18. Worker crash during transition.
19. Database transaction failure.
20. Event delivery failure.
21. Entitlement service outage.
22. Billing provider outage.
23. Concurrent upgrades from multiple administrators.
24. Concurrent upgrade and downgrade requests.
25. Organization deletion during scheduled transition.
26. Payment reversal after upgrade.
27. Refund after plan transition.
28. Chargeback after upgrade.
29. Subscription restored after cancellation.
30. Re-upgrade after downgrade.

---

## 25. Concurrency Requirements

The system shall prevent conflicting transitions.

Example:

```text
Request A:
Plan Pro → Enterprise

Request B:
Plan Pro → Free
```

Only one transition may become authoritative.

The system shall use:

* Optimistic locking
* Version numbers
* Idempotency
* State validation
* Distributed locking where necessary

---

## 26. State Transition Rules

Valid examples:

```text
FREE
  -> MONTHLY
  -> YEARLY

MONTHLY
  -> YEARLY
  -> HIGHER_MONTHLY
  -> LOWER_MONTHLY
  -> FREE

YEARLY
  -> MONTHLY
  -> HIGHER_YEARLY
  -> LOWER_YEARLY
  -> FREE

PAID
  -> CANCELED
```

Invalid transitions shall be rejected with deterministic error codes.

---

## 27. Error Codes

The system shall provide structured errors such as:

```text
SUBSCRIPTION_NOT_FOUND
UNAUTHORIZED_PLAN_CHANGE
PLAN_NOT_AVAILABLE
INVALID_PLAN_TRANSITION
PAYMENT_METHOD_REQUIRED
PAYMENT_FAILED
INSUFFICIENT_PAYMENT_CREDIT
DOWNGRADE_CONFLICT
SEAT_LIMIT_EXCEEDED
AI_AGENT_LIMIT_EXCEEDED
WORKFLOW_LIMIT_EXCEEDED
INTEGRATION_LIMIT_EXCEEDED
APPROVAL_REQUIRED
TRANSITION_ALREADY_EXISTS
TRANSITION_IN_PROGRESS
INVALID_IDEMPOTENCY_KEY
SUBSCRIPTION_STATE_CONFLICT
BILLING_PROVIDER_UNAVAILABLE
ENTITLEMENT_SYNC_FAILED
```

---

## 28. Acceptance Criteria

## AC-001

A valid upgrade shall result in:

```text
Successful Payment
+
Updated Subscription
+
Updated Entitlements
+
Updated Quotas
+
Audit Event
+
Notifications
```

---

## AC-002

A scheduled downgrade shall not modify active entitlements before its effective date unless policy explicitly requires otherwise.

---

## AC-003

A downgrade shall not delete customer data.

---

## AC-004

Duplicate requests shall not create duplicate charges.

---

## AC-005

Duplicate webhooks shall not create duplicate transitions.

---

## AC-006

AI agents shall not independently perform unauthorized subscription changes.

---

## AC-007

All financial calculations shall be reproducible from persisted billing inputs.

---

## AC-008

Historical invoices shall remain unchanged after a plan transition.

---

## AC-009

All entitlement changes shall eventually converge across dependent services.

---

## AC-010

Every successful or failed transition shall have an immutable audit trail.

---

## 29. FAANG-Level Quality Gates

A plan-transition implementation shall not be considered production-ready unless it satisfies:

```text
[ ] Multi-tenant isolation
[ ] Strong backend authorization
[ ] Idempotent transitions
[ ] Idempotent webhook handling
[ ] Explicit subscription state machine
[ ] Immutable financial records
[ ] Versioned plans
[ ] Deterministic pricing
[ ] Fixed-precision monetary calculations
[ ] Proration correctness
[ ] Quota reconciliation
[ ] Entitlement reconciliation
[ ] AI authorization boundaries
[ ] Human approval workflows
[ ] Distributed event processing
[ ] Retry and dead-letter handling
[ ] Observability
[ ] Auditability
[ ] Disaster recovery
[ ] Concurrency protection
[ ] Data preservation during downgrade
[ ] Payment failure recovery
[ ] Scheduled transition processing
[ ] Upgrade/downgrade conflict handling
[ ] Security testing
[ ] Load testing
[ ] Chaos/failure testing
[ ] Financial reconciliation testing
```

---

## 30. Definition of Done

`upgrade_downgrade.md` is implemented when SalesGenie can reliably support the complete lifecycle:

```text
Discover Plan
      ↓
Compare Plans
      ↓
Preview Change
      ↓
Validate Authorization
      ↓
Validate Usage
      ↓
Calculate Billing
      ↓
Calculate Proration/Credits/Taxes
      ↓
Validate Payment
      ↓
Human Approval (if required)
      ↓
Confirm Transition
      ↓
Persist Transition
      ↓
Process Billing
      ↓
Update Subscription
      ↓
Reconcile Entitlements
      ↓
Reconcile Quotas
      ↓
Update AI/Human Capabilities
      ↓
Propagate Events
      ↓
Verify Distributed State
      ↓
Notify Customer
      ↓
Audit
      ↓
Monitor
      ↓
Recover Automatically on Failure
```

The final system shall provide **financial correctness, tenant isolation, authorization integrity, entitlement consistency, AI safety, data preservation, operational observability, and deterministic recovery** across every SalesGenie subscription upgrade and downgrade.
