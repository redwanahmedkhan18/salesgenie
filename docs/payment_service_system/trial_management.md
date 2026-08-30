# SalesGenie — Trial Management Requirements

**Document:** `trial_management.md`  
**Product:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Requirement Level:** FAANG-Level / Production-Grade SaaS  
**Scope:** Free Trials, Trial Lifecycle, Trial Eligibility, Trial Provisioning, Trial Usage, Trial Limits, AI/Human Access, Trial Conversion, Trial Extension, Trial Expiration, Trial Cancellation, Trial Abuse Prevention, Billing Handoff, Entitlement Management, Notifications, Analytics, Auditability

---

## 1. Purpose

SalesGenie shall provide a secure, configurable, multi-tenant trial-management platform that enables prospective customers to evaluate SalesGenie before purchasing a subscription.

The trial-management system shall support:

- Trial eligibility
- Trial creation
- Trial activation
- Trial duration
- Trial configuration
- Trial-specific plans
- Trial-specific entitlements
- Trial-specific quotas
- Trial-specific AI usage
- Human-user limits
- AI-agent limits
- Workflow limits
- Integration limits
- RAG limits
- Lead-generation limits
- Omnichannel limits
- Trial usage tracking
- Trial warnings
- Trial expiration
- Trial conversion
- Trial cancellation
- Trial extension
- Trial restart policy
- Trial suspension
- Trial recovery
- Payment-method requirements
- Enterprise trial workflows
- AI-assisted trial onboarding
- Human-assisted trial onboarding
- Abuse prevention
- Fraud/risk controls
- Audit logging
- Billing integration
- Subscription conversion
- Analytics
- Notifications

The system shall prevent trial abuse, privilege escalation, quota bypasses, duplicate trials, unauthorized extensions, and inconsistent entitlement states.

---

## 2. Product Context

SalesGenie is a multi-tenant enterprise AI platform supporting:

- AI sales agents
- AI support agents
- Human sales agents
- Human support agents
- Multi-agent orchestration
- RAG knowledge management
- Lead generation
- Lead intelligence
- Omnichannel communication
- Workflow automation
- MCP tools
- External data sources
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
- Usage-based billing
- Metered billing
- Subscription plans
- Credits
- Coupons
- Invoices
- Payment processing
- Billing analytics

Trial access shall therefore be represented as a first-class entitlement and billing state rather than a frontend-only flag.

---

## 3. Actors

## 3.1 Human Actors

### H-01 Prospect

A person evaluating SalesGenie before becoming a paying customer.

### H-02 Trial User

A user operating SalesGenie under an active trial.

### H-03 Sales Agent

A SalesGenie employee assisting prospective customers during trials.

### H-04 Customer Success Manager

A human responsible for trial onboarding, adoption, and conversion.

### H-05 Organization Admin

The administrator responsible for the trial organization's configuration.

### H-06 Billing Admin

A user authorized to manage trial-to-paid conversion and billing configuration.

### H-07 Super Admin

A platform-level administrator responsible for operational trial management.

---

## 3.2 AI Actors

### AI-01 AI Sales Agent

An AI agent assisting with prospect qualification and trial conversion.

### AI-02 AI Support Agent

An AI agent assisting trial users.

### AI-03 AI Onboarding Agent

An AI agent responsible for guided trial onboarding.

### AI-04 AI Usage Advisor

An AI component that analyzes trial usage and recommends relevant features or plans.

### AI-05 AI Conversion Assistant

An AI component that identifies conversion opportunities and prepares upgrade recommendations.

### AI-06 AI Risk Agent

An AI component that detects suspicious trial behavior and potential abuse.

### AI-07 AI Entitlement Enforcement Agent

A runtime component that verifies whether AI operations are permitted under the active trial.

---

## 4. Core Business Principles

1. A trial shall belong to exactly one tenant.
2. Trial state shall be authoritative on the backend.
3. Trial entitlements shall never be controlled solely by frontend logic.
4. Trial eligibility shall be evaluated before trial creation.
5. A tenant shall not receive multiple trials unless policy explicitly permits it.
6. Trial limits shall be enforced consistently across all services.
7. Trial usage shall be tracked independently from paid subscription usage.
8. Trial usage records shall remain auditable.
9. Trial expiration shall be deterministic.
10. Trial expiration shall not silently delete customer data.
11. Trial conversion shall preserve customer configuration where supported.
12. Trial extensions shall require authorization.
13. AI agents shall not independently grant trial extensions.
14. AI agents shall not bypass trial quotas.
15. Trial abuse prevention shall operate independently from marketing logic.
16. Trial state changes shall be idempotent.
17. Payment-provider events shall be treated as asynchronous.
18. Trial entitlements shall propagate through event-driven mechanisms.
19. Security controls shall remain active during trials.
20. Trial analytics shall be tenant-aware and privacy-conscious.

---

## 5. Trial Lifecycle

The system shall support the following lifecycle:

```text
ELIGIBILITY_CHECK
       |
       v
TRIAL_CREATED
       |
       v
TRIAL_PENDING_ACTIVATION
       |
       v
TRIAL_ACTIVE
       |
       +----> TRIAL_EXTENDED
       |
       +----> TRIAL_SUSPENDED
       |
       +----> TRIAL_CANCELED
       |
       +----> TRIAL_EXPIRED
       |
       v
TRIAL_CONVERSION_PENDING
       |
       v
CONVERTED
```

---

## 6. Trial States

## 6.1 TRIAL_CREATED

Trial record exists but has not started.

## 6.2 TRIAL_PENDING_ACTIVATION

Required activation steps remain incomplete.

## 6.3 TRIAL_ACTIVE

Trial is currently available.

## 6.4 TRIAL_EXTENDED

Trial expiration has been moved forward through an authorized extension.

## 6.5 TRIAL_SUSPENDED

Trial access is temporarily restricted.

## 6.6 TRIAL_CANCELED

Trial was explicitly terminated.

## 6.7 TRIAL_EXPIRED

Trial duration has elapsed.

## 6.8 TRIAL_CONVERSION_PENDING

Customer has initiated conversion to a paid plan.

## 6.9 CONVERTED

Trial successfully transitioned to a paid subscription.

---

## 7. User Requirements

## UR-001 — Trial Discovery

Prospects shall be able to determine:

* Whether a trial is available
* Trial duration
* Included features
* Included AI capabilities
* Included quotas
* Human-user limits
* AI-agent limits
* Integration availability
* Usage restrictions
* Payment requirements
* Conversion terms

---

## UR-002 — Trial Eligibility

Prospects shall be informed whether they are eligible for a trial.

---

## UR-003 — Trial Creation

Eligible prospects shall be able to create a trial organization.

---

## UR-004 — Trial Activation

Users shall be able to activate a trial through configured verification and onboarding requirements.

---

## UR-005 — Trial Dashboard

Trial users shall be able to view:

* Trial status
* Trial start date
* Trial expiration date
* Remaining trial duration
* Current plan/trial configuration
* Current usage
* Remaining quotas
* Enabled features
* Restricted features
* AI-agent capacity
* Human-seat capacity
* Conversion options

---

## UR-006 — Trial Usage

Users shall be able to view relevant consumption including:

* AI requests
* AI tokens
* Conversations
* Leads
* Workflow executions
* API calls
* Storage
* RAG documents
* Integration operations
* Human seats

---

## UR-007 — Trial Limits

The system shall clearly display when users are:

```text
Within Limit
Approaching Limit
At Limit
Over Limit
```

---

## UR-008 — Trial Expiration Warning

Users shall receive configurable warnings before trial expiration.

Example:

```text
7 days remaining
3 days remaining
1 day remaining
Trial expires today
```

---

## UR-009 — Trial Conversion

Trial users shall be able to convert their trial into a paid subscription.

---

## UR-010 — Trial-to-Paid Plan Selection

Users shall be able to select:

* Monthly plan
* Yearly plan
* Available subscription tier
* Applicable add-ons
* Optional usage-based components

---

## UR-011 — Trial Data Preservation

Trial configuration shall remain available during conversion where the target plan supports the same capabilities.

---

## UR-012 — Trial Cancellation

Authorized users shall be able to cancel a trial before expiration.

---

## UR-013 — Trial Extension

Authorized users shall be able to request a trial extension when policy permits.

---

## UR-014 — Trial Restart

The system shall explicitly define whether an expired or canceled trial can be restarted.

Trial restart shall not be assumed to be permitted.

---

## UR-015 — Trial Expiration

Users shall be informed when their trial expires and what happens to:

* AI agents
* Human users
* Workflows
* Integrations
* Data
* Knowledge bases
* Conversations
* Leads

---

## 8. AI User Requirements

## AI-UR-001 — AI Onboarding

The AI onboarding agent shall guide users through:

* Organization setup
* User invitations
* AI-agent configuration
* Knowledge-base setup
* Integration configuration
* Lead-generation setup
* Workflow configuration

---

## AI-UR-002 — AI Feature Discovery

The AI assistant may recommend relevant SalesGenie features based on observed trial activity.

---

## AI-UR-003 — AI Usage Monitoring

The AI usage advisor shall analyze trial consumption and identify:

* High usage
* Underused features
* Approaching quotas
* Likely plan requirements
* Potential integration bottlenecks

---

## AI-UR-004 — AI Conversion Recommendation

The AI system may recommend a paid plan based on actual usage.

Recommendations shall be transparent and explainable.

---

## AI-UR-005 — AI Trial Extension Recommendation

The AI system may recommend an extension to an authorized human operator.

It shall not grant the extension independently.

---

## AI-UR-006 — AI Abuse Detection

The AI risk agent may identify suspicious patterns such as:

* Multiple accounts from the same environment
* Repeated trial creation
* Unusual API activity
* Abnormally high AI usage
* Automated account creation
* Suspicious integration behavior
* Credential sharing patterns

Risk detection shall not automatically produce irreversible account actions without policy-defined safeguards.

---

## AI-UR-007 — AI Entitlement Enforcement

AI agents shall validate current trial entitlements before executing restricted actions.

---

## AI-UR-008 — AI Trial Expiration Handling

After expiration, AI agents shall:

1. Detect expired entitlement.
2. Stop restricted operations.
3. Preserve available context.
4. Explain the restriction.
5. Offer conversion options.
6. Escalate to human support when necessary.

---

## 9. System Requirements

## SR-001 — Multi-Tenant Trial Isolation

Trial data shall be isolated by:

```text
tenant_id
organization_id
trial_id
user_id
```

---

## SR-002 — Authoritative Trial Service

A dedicated trial-management component shall own:

* Trial eligibility
* Trial state
* Trial lifecycle
* Trial duration
* Trial extensions
* Trial expiration
* Trial conversion state

---

## SR-003 — Trial Configuration

Trial policies shall be configurable without application redeployment.

Configuration shall support:

```text
trial_duration
grace_period
max_users
max_ai_agents
max_workflows
max_leads
max_storage
max_ai_usage
max_api_calls
enabled_integrations
enabled_channels
enabled_features
payment_required
verification_required
```

---

## SR-004 — Versioned Trial Policies

Trial policy versions shall be persisted.

Historical trial records shall retain the policy version used when the trial was created.

---

## SR-005 — Trial Entitlement Service

Trial entitlements shall be calculated using:

```text
Tenant
+
Trial State
+
Trial Policy
+
Feature Configuration
+
Usage
+
Risk Policy
```

---

## SR-006 — Trial Usage Isolation

Trial usage shall be tracked independently from paid subscription usage.

---

## SR-007 — Idempotent Trial Creation

Trial creation shall support idempotency keys.

Repeated requests shall not create duplicate trials.

---

## SR-008 — Eligibility Enforcement

Trial eligibility shall be determined server-side.

---

## SR-009 — Expiration Engine

The system shall provide a durable scheduled-job mechanism for trial expiration.

---

## SR-010 — Time Authority

Trial expiration shall use server-authoritative timestamps.

---

## SR-011 — Time Zone Policy

Trial periods shall use a documented timezone policy.

---

## SR-012 — Event-Driven Propagation

Trial state changes shall be published to dependent services.

Example:

```text
Trial Service
     |
     v
trial.activated
     |
     +----> Entitlement Service
     +----> Usage Service
     +----> AI Gateway
     +----> Agent Runtime
     +----> Integration Service
     +----> Notification Service
     +----> Analytics
     +----> CRM
```

---

## SR-013 — Fail-Closed Entitlement Enforcement

Restricted functionality shall fail closed when the system cannot safely determine active trial entitlement.

---

## SR-014 — Trial Abuse Controls

The system shall provide configurable abuse-prevention controls.

---

## SR-015 — Observability

The system shall provide:

* Logs
* Metrics
* Traces
* Trial lifecycle monitoring
* Conversion monitoring
* Expiration monitoring
* Abuse monitoring
* Entitlement propagation monitoring

---

## 10. Functional Requirements

## 10.1 Trial Eligibility

## FR-ELIG-001

The system shall expose a trial eligibility evaluation operation.

---

## FR-ELIG-002

Eligibility evaluation shall consider configurable factors including:

* Existing tenant
* Existing subscription
* Previous trial
* Trial history
* Account verification
* Organization identity
* Risk score
* Policy restrictions

---

## FR-ELIG-003

Eligibility responses shall provide structured reasons.

Example:

```json
{
  "eligible": false,
  "reason_code": "TRIAL_ALREADY_USED",
  "retryable": false
}
```

---

## FR-ELIG-004

The system shall avoid exposing sensitive fraud-detection details to untrusted users.

---

## 10.2 Trial Creation

## FR-TRIAL-001

The system shall create a trial only after successful eligibility validation.

---

## FR-TRIAL-002

Trial creation shall initialize:

* Trial ID
* Tenant ID
* Policy version
* Start timestamp
* End timestamp
* Status
* Entitlement snapshot
* Usage counters
* Created-by actor
* Creation source

---

## FR-TRIAL-003

Trial creation shall be atomic within the authoritative trial service.

---

## FR-TRIAL-004

Trial provisioning shall be idempotent.

---

## 10.3 Trial Activation

## FR-ACT-001

The system shall support configurable activation requirements.

Possible requirements:

* Email verification
* Organization verification
* Phone verification
* Terms acceptance
* Identity verification
* Payment method
* Human approval

---

## FR-ACT-002

Activation shall generate an audit event.

---

## FR-ACT-003

Activation shall publish:

```text
trial.activated
```

---

## 10.4 Trial Duration

## FR-DUR-001

The trial duration shall be configurable.

---

## FR-DUR-002

The system shall persist:

```text
start_at
expires_at
```

---

## FR-DUR-003

Trial duration shall not be recalculated from frontend timestamps.

---

## FR-DUR-004

Trial extensions shall modify the authoritative expiration timestamp.

---

## 10.5 Trial Entitlements

## FR-ENT-001

The system shall calculate trial entitlements at activation.

---

## FR-ENT-002

Trial entitlements shall include:

```text
Human Seats
AI Agents
AI Usage
Workflows
Leads
Storage
RAG Documents
API Calls
Integrations
Communication Channels
MCP Tools
Analytics
```

---

## FR-ENT-003

Each restricted operation shall validate current entitlement.

---

## FR-ENT-004

Frontend feature visibility shall not be considered authorization.

---

## 10.6 AI Agent Limits

## FR-AI-LIMIT-001

The system shall enforce maximum AI-agent capacity.

---

## FR-AI-LIMIT-002

Users shall not create AI agents beyond the trial quota.

---

## FR-AI-LIMIT-003

Existing AI-agent configurations shall not be silently deleted at expiration.

---

## FR-AI-LIMIT-004

Expired trials shall transition AI agents into a controlled state where required.

Example:

```text
ACTIVE
RESTRICTED
DISABLED
ARCHIVED
```

---

## 10.7 Human Seat Limits

## FR-SEAT-001

The system shall track:

```text
Purchased/Allowed Seats
Assigned Seats
Active Seats
Inactive Seats
Available Seats
```

---

## FR-SEAT-002

Trial users shall not exceed configured human-seat limits.

---

## 10.8 Usage Tracking

## FR-USAGE-001

The system shall track trial consumption for all billable or quota-controlled resources.

---

## FR-USAGE-002

Usage events shall contain:

```text
usage_event_id
tenant_id
trial_id
resource_type
resource_id
quantity
timestamp
source
idempotency_key
metadata
```

---

## FR-USAGE-003

Duplicate usage events shall not double-count consumption.

---

## FR-USAGE-004

Usage counters shall be reconciled periodically against source events.

---

## 10.9 Usage Thresholds

## FR-THRESH-001

The system shall support configurable usage thresholds.

Example:

```text
50%
75%
80%
90%
100%
```

---

## FR-THRESH-002

The system shall notify users when thresholds are reached.

---

## FR-THRESH-003

Threshold notifications shall not be repeatedly emitted for the same threshold within the configured suppression window.

---

## 10.10 Trial Expiration

## FR-EXP-001

The system shall automatically identify trials whose expiration timestamp has passed.

---

## FR-EXP-002

Expiration processing shall be idempotent.

---

## FR-EXP-003

Expiration shall:

1. Validate current trial state.
2. Mark the trial expired.
3. Recalculate entitlements.
4. Restrict trial-only capabilities.
5. Preserve customer data.
6. Publish expiration events.
7. Notify relevant users.
8. Record an audit event.

---

## FR-EXP-004

Expiration shall not delete:

* Conversations
* Leads
* Contacts
* Knowledge documents
* Workflows
* Audit records
* Billing records
* Usage history

unless an independent retention policy explicitly requires deletion.

---

## 10.11 Grace Period

## FR-GRACE-001

The system may support a configurable grace period after expiration.

---

## FR-GRACE-002

During the grace period, access shall be explicitly defined by policy.

Example:

```text
Read-only access
+
Export access
+
Upgrade access
```

---

## FR-GRACE-003

AI execution shall remain disabled when the trial entitlement has expired unless the grace policy explicitly permits it.

---

## 10.12 Trial Conversion

## FR-CONV-001

Users shall be able to convert an active trial into a paid subscription.

---

## FR-CONV-002

The conversion flow shall support:

```text
Select Plan
    ↓
Select Billing Interval
    ↓
Apply Coupon
    ↓
Calculate Taxes
    ↓
Calculate Credits
    ↓
Validate Payment
    ↓
Confirm
    ↓
Create Subscription
    ↓
Update Entitlements
```

---

## FR-CONV-003

Trial conversion shall preserve compatible configuration.

---

## FR-CONV-004

Trial usage shall be transferred into paid usage only according to explicit billing policy.

---

## FR-CONV-005

Trial-to-paid conversion shall be idempotent.

---

## 10.13 Conversion Failure

## FR-CONV-006

If payment fails:

* Trial shall not be incorrectly marked converted.
* User shall receive actionable feedback.
* Trial state shall remain recoverable.
* Payment retry shall be supported.
* No duplicate subscription shall be created.

---

## 10.14 Trial Cancellation

## FR-CANCEL-001

Authorized users shall be able to cancel a trial.

---

## FR-CANCEL-002

Cancellation shall record:

* Actor
* Reason
* Timestamp
* Trial state
* Cancellation source

---

## FR-CANCEL-003

Cancellation shall not delete customer data.

---

## 10.15 Trial Extension

## FR-EXT-001

The system shall support configurable extension policies.

---

## FR-EXT-002

Extensions shall require appropriate authorization.

---

## FR-EXT-003

Extensions shall support:

```text
extension_id
trial_id
previous_expiry
new_expiry
duration
reason
requested_by
approved_by
created_at
```

---

## FR-EXT-004

The system shall prevent unauthorized repeated extensions.

---

## FR-EXT-005

AI agents may recommend extensions but shall not grant them unless explicitly delegated the required permission by policy.

---

## 10.16 Enterprise Trial

## FR-ENT-TRIAL-001

Super Admins shall be able to create enterprise trials subject to authorization.

---

## FR-ENT-TRIAL-002

Enterprise trials may support custom:

* Duration
* Seats
* AI agents
* Usage
* Integrations
* Security features
* Support level
* Data retention
* SLA

---

## FR-ENT-TRIAL-003

Enterprise trial overrides shall be audited.

---

## 10.17 Trial Notifications

## FR-NOTIFY-001

The notification service shall support:

```text
trial.created
trial.activated
trial.usage.threshold
trial.expiring
trial.expired
trial.extended
trial.canceled
trial.conversion.started
trial.conversion.completed
trial.conversion.failed
```

---

## FR-NOTIFY-002

Notification channels may include:

* Email
* In-app
* Slack
* Microsoft Teams
* SMS where supported
* AI assistant messages

---

## 10.18 AI Onboarding Workflow

```text
Trial Activated
      |
      v
AI Onboarding Agent
      |
      +----> Organization Setup
      |
      +----> Invite Team
      |
      +----> Configure AI Agent
      |
      +----> Upload Knowledge
      |
      +----> Connect Integrations
      |
      +----> Configure Workflow
      |
      v
Activation Milestones
      |
      v
Usage Monitoring
```

---

## 10.19 AI Usage Optimization

```text
Usage Data
    |
    v
AI Usage Analysis
    |
    +----> Underutilized Features
    |
    +----> Approaching Quotas
    |
    +----> High Consumption
    |
    +----> Recommended Configuration
    |
    +----> Recommended Paid Plan
```

Recommendations shall be advisory unless explicitly authorized.

---

## 10.20 AI Trial Conversion

```text
Trial Usage
     |
     v
AI Conversion Analysis
     |
     v
Plan Recommendation
     |
     v
Human Review
     |
     v
Plan Preview
     |
     v
Explicit Confirmation
     |
     v
Billing Service
```

---

## 10.21 AI Safety

AI agents shall not:

* Create unauthorized trials
* Extend trials without permission
* Reset quotas
* Bypass eligibility
* Disable abuse controls
* Change billing plans without authorization
* Modify financial records
* Circumvent feature entitlements
* Grant enterprise privileges

---

## 11. Trial Abuse Prevention

## FR-ABUSE-001

The system shall detect repeated trial creation attempts.

---

## FR-ABUSE-002

The system shall support configurable risk signals.

Examples:

```text
Account History
Email Reputation
Organization Identity
Device Fingerprint
IP Risk
Velocity
API Behavior
Usage Pattern
Payment Signals
```

---

## FR-ABUSE-003

Risk scoring shall not be the sole basis for irreversible account actions unless explicitly configured.

---

## FR-ABUSE-004

High-risk trials may be:

```text
ALLOWED
REVIEW_REQUIRED
LIMITED
SUSPENDED
DENIED
```

---

## FR-ABUSE-005

Abuse controls shall be tenant-aware and privacy-conscious.

---

## 12. API Requirements

## API-001 — Check Eligibility

```http
GET /api/v1/trials/eligibility
```

---

## API-002 — Create Trial

```http
POST /api/v1/trials
```

---

## API-003 — Activate Trial

```http
POST /api/v1/trials/{trial_id}/activate
```

---

## API-004 — Current Trial

```http
GET /api/v1/trials/current
```

---

## API-005 — Trial Usage

```http
GET /api/v1/trials/{trial_id}/usage
```

---

## API-006 — Trial Entitlements

```http
GET /api/v1/trials/{trial_id}/entitlements
```

---

## API-007 — Trial Conversion Preview

```http
POST /api/v1/trials/{trial_id}/convert/preview
```

---

## API-008 — Convert Trial

```http
POST /api/v1/trials/{trial_id}/convert
```

---

## API-009 — Cancel Trial

```http
POST /api/v1/trials/{trial_id}/cancel
```

---

## API-010 — Request Extension

```http
POST /api/v1/trials/{trial_id}/extension-request
```

---

## API-011 — Trial History

```http
GET /api/v1/trials/history
```

---

## API-012 — Trial Status

```http
GET /api/v1/trials/{trial_id}/status
```

---

## 13. AI Tool Requirements

AI agents may use:

```text
check_trial_eligibility
get_current_trial
get_trial_usage
get_trial_entitlements
get_trial_remaining_quota
get_trial_expiration
compare_trial_plans
preview_trial_conversion
request_trial_extension
get_trial_conversion_status
get_trial_onboarding_status
```

All tools shall enforce backend authorization.

---

## 14. AI Tool Permission Model

AI tools shall be divided into:

```text
READ
RECOMMEND
REQUEST
APPROVE
EXECUTE
```

Default AI capability:

```text
READ       = Allowed
RECOMMEND  = Allowed
REQUEST    = Policy dependent
APPROVE    = Human/admin only by default
EXECUTE    = Explicitly delegated only
```

---

## 15. Trial Data Model

## Trial

```text
trial_id
tenant_id
organization_id
policy_id
policy_version
status
source
start_at
expires_at
extended_until
activated_at
canceled_at
converted_at
created_by
converted_subscription_id
risk_state
created_at
updated_at
version
```

---

## Trial Usage

```text
usage_id
trial_id
tenant_id
resource_type
quantity
unit
period_start
period_end
source
created_at
updated_at
```

---

## Trial Extension

```text
extension_id
trial_id
tenant_id
previous_expiry
new_expiry
duration
reason
requested_by
approved_by
status
created_at
approved_at
```

---

## Trial Entitlement Snapshot

```text
trial_id
policy_version
feature_entitlements
ai_agent_limit
human_seat_limit
workflow_limit
lead_limit
storage_limit
api_limit
ai_usage_limit
integration_limit
channel_entitlements
mcp_entitlements
effective_at
version
```

---

## 16. Trial Events

The system shall publish:

```text
trial.created
trial.activation.requested
trial.activated
trial.usage.updated
trial.usage.threshold_reached
trial.extension.requested
trial.extension.approved
trial.extended
trial.expiring
trial.expired
trial.suspended
trial.resumed
trial.canceled
trial.conversion.requested
trial.conversion.processing
trial.conversion.completed
trial.conversion.failed
trial.entitlements.changed
trial.abuse.detected
trial.review.required
```

---

## 17. Event Processing

Consumers shall support:

* Idempotency
* Retry
* Dead-letter handling
* Event versioning
* Correlation IDs
* Tenant context
* Distributed tracing
* Duplicate detection

---

## 18. Scheduled Trial Expiration Engine

The system shall implement:

```text
Scheduler
    |
    v
Find Due Trials
    |
    v
Acquire Lock
    |
    v
Validate State
    |
    v
Expire Trial
    |
    v
Update Entitlements
    |
    v
Publish Event
    |
    v
Notify User
    |
    v
Audit
```

Concurrent workers shall not expire the same trial multiple times.

---

## 19. Security Requirements

## SEC-001

Trial creation shall require authenticated or appropriately verified identity according to policy.

---

## SEC-002

All trial APIs shall enforce tenant isolation.

---

## SEC-003

Trial state shall never be trusted from client-side input.

---

## SEC-004

Expiration timestamps shall be server-controlled.

---

## SEC-005

Trial extensions shall require explicit authorization.

---

## SEC-006

AI agents shall not bypass trial eligibility.

---

## SEC-007

AI agents shall not manipulate trial timestamps.

---

## SEC-008

AI agents shall not modify usage counters directly.

---

## SEC-009

Trial APIs shall support rate limiting.

---

## SEC-010

Sensitive abuse-detection signals shall not be exposed to untrusted users.

---

## 20. Audit Requirements

Every material trial lifecycle action shall generate an immutable audit event.

Required fields:

```text
event_id
trial_id
tenant_id
actor_id
actor_type
action
previous_state
new_state
reason
source
timestamp
correlation_id
request_id
ip_metadata
result
```

---

## 21. Trial-to-Paid Conversion Workflow

```text
TRIAL_ACTIVE
      |
      v
Select Paid Plan
      |
      v
Preview Conversion
      |
      v
Calculate Pricing
      |
      v
Apply Coupon
      |
      v
Calculate Tax
      |
      v
Validate Payment
      |
      v
Human Confirmation
      |
      v
Create Subscription
      |
      v
Update Entitlements
      |
      v
Transfer Compatible Configuration
      |
      v
Mark Trial CONVERTED
      |
      v
Publish Events
      |
      v
Audit
```

---

## 22. Trial Expiration Workflow

```text
TRIAL_ACTIVE
      |
      v
Expiration Reached
      |
      v
Acquire Distributed Lock
      |
      v
Validate Trial State
      |
      v
Mark EXPIRED
      |
      v
Recalculate Entitlements
      |
      v
Restrict Trial Capabilities
      |
      v
Preserve Data
      |
      v
Publish trial.expired
      |
      v
Notify Users
      |
      v
Audit
```

---

## 23. Trial Extension Workflow

```text
Human/Authorized System
        |
        v
Extension Request
        |
        v
Eligibility Check
        |
        v
Policy Validation
        |
        v
Approval
        |
        v
Update Expiration
        |
        v
Update Entitlements
        |
        v
Publish trial.extended
        |
        v
Audit
```

AI may prepare or recommend this workflow but shall not bypass the approval layer.

---

## 24. Trial Entitlement Enforcement

Before every restricted operation:

```text
Request
  |
  v
Authenticate
  |
  v
Authorize
  |
  v
Resolve Tenant
  |
  v
Resolve Trial/Subscription
  |
  v
Resolve Entitlement
  |
  v
Check Usage
  |
  v
Allow / Deny
```

The frontend shall never be treated as the authoritative enforcement layer.

---

## 25. Trial Expiration Data Safety

Upon expiration:

```text
Trial Access
     |
     +----> Disabled
     |
     +----> Restricted
     |
     v
Customer Data
     |
     +----> Preserved
     |
     +----> Exportable
     |
     +----> Retained
```

Data deletion shall occur only under an independently defined retention policy.

---

## 26. Human + AI Collaboration

## COLLAB-001

AI shall assist trial users without replacing authorization controls.

## COLLAB-002

AI shall recommend relevant features based on observed usage.

## COLLAB-003

Human administrators shall approve high-impact actions.

## COLLAB-004

AI recommendations shall be explainable.

## COLLAB-005

The system shall record whether actions originated from:

```text
HUMAN
AI_RECOMMENDATION
AI_REQUEST
AUTOMATION
ADMIN
API
SYSTEM
```

---

## 27. Super Admin Requirements

Super Admins shall be able to:

* View trial organizations
* Search trials
* View trial state
* View trial usage
* View entitlement state
* Review risk state
* Approve extensions
* Suspend trials
* Resume trials
* Review conversion failures
* Investigate entitlement mismatches
* Replay recoverable events
* View audit records

Super Admin actions shall be fully audited.

---

## 28. Trial Analytics

The platform shall track:

```text
trial_starts
trial_activations
activation_rate
time_to_first_value
feature_adoption
ai_agent_creation_rate
integration_activation_rate
usage_by_resource
quota_exhaustion_rate
trial_extension_rate
trial_expiration_rate
trial_conversion_rate
conversion_time
conversion_by_plan
conversion_by_channel
conversion_by_industry
conversion_by_campaign
abuse_rate
```

---

## 29. AI Trial Analytics

AI analytics may identify:

* Trial users likely to convert
* Organizations at risk of churn
* Feature adoption gaps
* High-value prospects
* Quota bottlenecks
* Recommended onboarding actions
* Recommended plan tier

AI predictions shall be treated as probabilistic recommendations, not authoritative billing decisions.

---

## 30. Performance Requirements

## NFR-001

Trial status queries shall support interactive application latency.

## NFR-002

Trial entitlement checks shall be optimized for high-frequency AI and API workloads.

## NFR-003

Usage ingestion shall support high-volume event streams.

## NFR-004

Expiration processing shall support large batches of concurrent trial expirations.

## NFR-005

Trial creation shall remain reliable under marketing campaign traffic spikes.

---

## 31. Reliability Requirements

The system shall tolerate:

* Duplicate trial requests
* Duplicate usage events
* Duplicate webhooks
* Worker crashes
* Database failures
* Queue failures
* Payment-provider outages
* Entitlement-service outages
* Notification failures
* Network failures
* Concurrent conversion requests
* Concurrent extension requests

---

## 32. Error Codes

The system shall expose structured errors such as:

```text
TRIAL_NOT_FOUND
TRIAL_NOT_ELIGIBLE
TRIAL_ALREADY_EXISTS
TRIAL_ALREADY_USED
TRIAL_EXPIRED
TRIAL_CANCELED
TRIAL_SUSPENDED
TRIAL_LIMIT_REACHED
AI_AGENT_LIMIT_REACHED
USER_LIMIT_REACHED
WORKFLOW_LIMIT_REACHED
API_QUOTA_EXCEEDED
STORAGE_LIMIT_REACHED
INTEGRATION_NOT_AVAILABLE
EXTENSION_NOT_ALLOWED
EXTENSION_APPROVAL_REQUIRED
CONVERSION_ALREADY_STARTED
CONVERSION_ALREADY_COMPLETED
PAYMENT_METHOD_REQUIRED
PAYMENT_FAILED
ENTITLEMENT_SYNC_FAILED
TRIAL_STATE_CONFLICT
DUPLICATE_REQUEST
RATE_LIMITED
RISK_REVIEW_REQUIRED
```

---

## 33. Edge Cases

The system shall handle:

1. User creates multiple trial requests concurrently.
2. User already has an active paid subscription.
3. Organization previously used a trial.
4. Trial expires while conversion is processing.
5. Payment succeeds but conversion callback is delayed.
6. Payment provider sends duplicate webhook.
7. Payment provider sends events out of order.
8. Trial extension occurs near expiration.
9. Two administrators request extensions simultaneously.
10. AI recommends conversion after trial expiration.
11. User exceeds quota immediately before expiration.
12. Trial expires during an active AI workflow.
13. Trial expires during a human conversation.
14. Trial expires while an integration sync is running.
15. Trial is suspended for abuse.
16. Trial is resumed after review.
17. Organization upgrades during the trial.
18. User changes organization during a trial.
19. Organization is deleted during a trial.
20. Trial policy changes after trial creation.
21. Trial service becomes temporarily unavailable.
22. Entitlement service becomes unavailable.
23. Usage events arrive late.
24. Usage events arrive duplicated.
25. Notification delivery fails.
26. Trial conversion creates duplicate subscription requests.
27. Coupon expires before conversion.
28. Payment method becomes invalid during conversion.
29. Enterprise trial receives a custom extension.
30. Trial is converted after expiration during an allowed grace period.

---

## 34. Concurrency Control

The system shall protect against concurrent:

```text
Trial Creation
Trial Extension
Trial Cancellation
Trial Conversion
Trial Expiration
Entitlement Updates
Usage Updates
```

Mechanisms may include:

* Optimistic locking
* Version numbers
* Idempotency keys
* Distributed locks
* Transactional state transitions

---

## 35. Trial Policy Engine

The platform shall support policy-driven trial behavior.

Example:

```json
{
  "trial_duration_days": 14,
  "max_users": 10,
  "max_ai_agents": 3,
  "max_workflows": 25,
  "max_leads": 1000,
  "max_ai_tokens": 1000000,
  "max_storage_gb": 5,
  "payment_method_required": false,
  "extension_allowed": true,
  "max_extensions": 1,
  "grace_period_days": 3
}
```

---

## 36. Trial Policy Versioning

When a trial starts:

```text
Current Policy
      |
      v
Policy Version Snapshot
      |
      v
Trial
```

Future policy changes shall not silently rewrite historical trial terms.

---

## 37. Notification Timing

Configurable notification schedule shall support:

```text
Trial Start
|
+-- 50% elapsed
|
+-- 7 days remaining
|
+-- 3 days remaining
|
+-- 1 day remaining
|
+-- Expiration
|
+-- Grace Period
|
+-- Final Expiration
```

---

## 38. Trial Conversion Optimization

The platform may provide contextual conversion prompts based on:

* Usage thresholds
* Feature requirements
* AI-agent limits
* Human-seat limits
* Integration requirements
* Workflow requirements

Conversion prompts shall not prevent users from using legitimately available trial features.

---

## 39. Trial Quota Reset Protection

The system shall prevent users from bypassing trial quotas by:

* Creating multiple trials
* Recreating organizations
* Reconnecting identities
* Reusing expired trial accounts
* Manipulating client timestamps
* Replaying usage requests

---

## 40. Trial Security Boundary

The trial system shall enforce:

```text
Authentication
      +
Authorization
      +
Tenant Isolation
      +
Trial Eligibility
      +
Entitlement Validation
      +
Quota Validation
      +
Risk Controls
      +
Audit Logging
```

---

## 41. Acceptance Criteria

## AC-001

An eligible prospect can create exactly one valid trial according to configured policy.

## AC-002

An ineligible prospect cannot bypass eligibility through frontend manipulation.

## AC-003

Trial duration is calculated using server-authoritative timestamps.

## AC-004

Trial quotas are enforced consistently across frontend, backend, AI, API, and integration workloads.

## AC-005

Duplicate trial creation requests do not create duplicate trials.

## AC-006

Trial usage is idempotent and does not double-count duplicate events.

## AC-007

Trial expiration is idempotent.

## AC-008

Trial expiration does not silently delete customer data.

## AC-009

Expired trial users cannot continue restricted AI operations.

## AC-010

Trial conversion does not create duplicate subscriptions.

## AC-011

Successful conversion updates subscription and entitlement state consistently.

## AC-012

Failed conversion remains recoverable.

## AC-013

Trial extensions require appropriate authorization.

## AC-014

AI agents cannot independently bypass trial policy.

## AC-015

All material trial lifecycle actions are auditable.

## AC-016

Trial policy versions are preserved historically.

## AC-017

Trial abuse controls do not expose sensitive internal risk signals to end users.

## AC-018

Scheduled expiration continues to work after worker restarts.

## AC-019

Duplicate and out-of-order events do not corrupt trial state.

## AC-020

All dependent services eventually converge on the authoritative trial entitlement state.

---

## 42. FAANG-Level Quality Gates

The implementation shall not be considered production-ready unless:

```text
[ ] Multi-tenant isolation
[ ] Server-side trial eligibility
[ ] Idempotent trial creation
[ ] Idempotent usage tracking
[ ] Explicit trial state machine
[ ] Versioned trial policies
[ ] Server-authoritative expiration
[ ] Durable scheduled expiration
[ ] Distributed locking/concurrency control
[ ] Centralized entitlement enforcement
[ ] AI authorization boundaries
[ ] Human approval workflow
[ ] Trial abuse prevention
[ ] Rate limiting
[ ] Data preservation
[ ] Trial-to-paid conversion
[ ] Payment failure recovery
[ ] Webhook idempotency
[ ] Event-driven architecture
[ ] Retry mechanisms
[ ] Dead-letter handling
[ ] Audit logging
[ ] Distributed tracing
[ ] Structured metrics
[ ] Security monitoring
[ ] Usage reconciliation
[ ] Quota enforcement
[ ] Entitlement reconciliation
[ ] Disaster recovery
[ ] Load testing
[ ] Chaos/failure testing
[ ] Security testing
[ ] Financial reconciliation testing
[ ] AI safety testing
[ ] Privacy review
```

---

## 43. Definition of Done

`trial_management.md` shall be considered implemented when SalesGenie can reliably execute the complete trial lifecycle:

```text
Prospect
   |
   v
Eligibility Check
   |
   v
Trial Creation
   |
   v
Verification / Activation
   |
   v
Trial Provisioning
   |
   v
AI + Human Onboarding
   |
   v
Feature Usage
   |
   v
Usage Tracking
   |
   v
Quota Enforcement
   |
   v
Usage Notifications
   |
   +--------------------+
   |                    |
   v                    v
Extension           Conversion
   |                    |
   v                    v
Extended Trial      Paid Subscription
   |
   v
Continued Evaluation
   |
   v
Expiration
   |
   v
Grace Period
   |
   v
Restricted Access
   |
   v
Data Preservation
   |
   v
Final Expiration
```

The final SalesGenie implementation shall provide **secure trial eligibility, deterministic lifecycle management, centralized entitlement enforcement, accurate usage tracking, AI/human collaboration, abuse prevention, reliable trial-to-paid conversion, safe expiration, tenant isolation, strong auditability, and resilient distributed-system behavior**.
