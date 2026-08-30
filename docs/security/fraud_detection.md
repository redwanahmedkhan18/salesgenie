# SalesGenie — FAANG-Level Fraud Detection Requirements

## `fraud_detection.md`

> **Scope:** Enterprise-grade fraud detection for SalesGenie covering human users, AI agents, organizations, subscriptions, billing, payments, credits, coupons, invoices, usage-based billing, integrations, APIs, workflows, and platform operations.
>
> **Objective:** Detect, score, investigate, prevent, contain, and continuously learn from fraudulent behavior using deterministic rules, statistical analysis, machine learning, graph analytics, AI-assisted investigation, and controlled human decision-making.

---

## 1. Fraud Detection Objectives

SalesGenie MUST provide a unified fraud detection platform capable of:

- Detecting account fraud.
- Detecting payment fraud.
- Detecting subscription fraud.
- Detecting promotional abuse.
- Detecting coupon abuse.
- Detecting free-tier abuse.
- Detecting trial abuse.
- Detecting credit abuse.
- Detecting usage-meter manipulation.
- Detecting invoice manipulation.
- Detecting refund abuse.
- Detecting chargeback-related fraud.
- Detecting identity fraud.
- Detecting account takeover.
- Detecting synthetic identities.
- Detecting bot-driven abuse.
- Detecting API-driven fraud.
- Detecting AI-agent-driven fraud.
- Detecting workflow automation abuse.
- Detecting multi-account abuse.
- Detecting referral abuse.
- Detecting integration abuse.
- Detecting insider fraud indicators.
- Detecting coordinated fraud rings.
- Detecting anomalous financial behavior.
- Detecting fraud across multiple tenants where platform-level visibility is authorized.
- Supporting human fraud investigation.
- Supporting AI-assisted fraud investigation.
- Supporting controlled automated prevention.
- Maintaining evidence and auditability.
- Minimizing false positives.
- Continuously improving detection accuracy.

---

## 2. Fraud Detection Actors

## 2.1 Human Actors

### FD-H-001 — End User

The system MUST detect fraudulent behavior associated with end-user accounts.

### FD-H-002 — Sales Agent

The system MUST detect suspicious sales activity, lead manipulation, promotional abuse, and unauthorized account actions.

### FD-H-003 — Support Agent

The system MUST monitor suspicious refunds, credits, account modifications, and customer-data access.

### FD-H-004 — Organization Administrator

The system MUST detect suspicious organization-level billing, subscription, user, and usage behavior.

### FD-H-005 — Billing Administrator

Billing administrators MUST be monitored for unusual financial operations.

### FD-H-006 — Security Administrator

Security administrators MUST be able to investigate fraud signals according to RBAC permissions.

### FD-H-007 — Fraud Analyst

Fraud analysts MUST be able to investigate, classify, escalate, and resolve fraud cases.

### FD-H-008 — Super Administrator

Super-admin financial and account-management activity MUST receive enhanced fraud monitoring.

### FD-H-009 — Finance Operator

Finance users MUST be monitored for unusual refund, invoice, credit, and payment activity.

---

## 3. AI Fraud Actors

## FD-AI-001 — AI Sales Agent

The system MUST detect suspicious AI-generated sales activity.

## FD-AI-002 — AI Support Agent

The system MUST monitor AI-driven refunds, credits, account changes, and customer-data access.

## FD-AI-003 — AI Billing Agent

AI billing agents MUST operate under explicit financial-action policies.

## FD-AI-004 — AI Workflow Agent

The system MUST detect automated workflows used to generate fraudulent financial activity.

## FD-AI-005 — AI Orchestrator

The platform MUST monitor agent delegation and action chains.

## FD-AI-006 — AI Fraud Analyst

AI MAY analyze fraud signals and recommend decisions.

## FD-AI-007 — Autonomous Fraud Prevention Agent

Autonomous fraud-prevention actions MUST be constrained by explicit policy and authorization.

---

## 4. Fraud Taxonomy

SalesGenie MUST support detection of at least:

```text
ACCOUNT_FRAUD
ACCOUNT_TAKEOVER
IDENTITY_FRAUD
SYNTHETIC_IDENTITY
MULTI_ACCOUNT_ABUSE
PAYMENT_FRAUD
CARD_TESTING
CARDING
PAYMENT_METHOD_ABUSE
CHARGEBACK_FRAUD
REFUND_FRAUD
REFUND_ABUSE
SUBSCRIPTION_FRAUD
TRIAL_ABUSE
FREE_TIER_ABUSE
COUPON_ABUSE
PROMOTIONAL_ABUSE
CREDIT_ABUSE
REFERRAL_ABUSE
USAGE_MANIPULATION
METERING_FRAUD
INVOICE_FRAUD
BILLING_MANIPULATION
PRICING_ABUSE
API_FRAUD
BOT_FRAUD
AUTOMATION_ABUSE
AI_AGENT_FRAUD
WORKFLOW_FRAUD
INTEGRATION_FRAUD
OAUTH_ABUSE
INSIDER_FRAUD
COLLUSION
FRAUD_RING
DATA_MANIPULATION
IDENTITY_VERIFICATION_FRAUD
```

---

## 5. Fraud Risk Levels

The system MUST support:

```text
NONE
LOW
MEDIUM
HIGH
CRITICAL
```

Example:

```text
0–19    NONE
20–39   LOW
40–59   MEDIUM
60–79   HIGH
80–100  CRITICAL
```

Thresholds MUST be configurable.

---

## 6. User Requirements

## UR-001 — Fraud Visibility

Authorized users MUST be able to view fraud alerts within their permitted scope.

## UR-002 — Real-Time Fraud Detection

High-risk financial fraud signals SHOULD be evaluated in near real time.

## UR-003 — Fraud Risk Score

Every actionable fraud case MUST have a normalized risk score.

## UR-004 — Explainable Fraud Decision

The system MUST explain why a transaction, account, or behavior was considered suspicious.

## UR-005 — Evidence

Every material fraud decision MUST reference supporting evidence.

## UR-006 — Fraud Timeline

Investigators MUST be able to reconstruct relevant activity chronologically.

## UR-007 — Fraud Case Management

Fraud analysts MUST be able to create and manage investigation cases.

## UR-008 — Case Assignment

Fraud cases MUST be assignable to authorized investigators.

## UR-009 — Case Status

Cases MUST support:

```text
NEW
TRIAGED
INVESTIGATING
ACTION_REQUIRED
CONFIRMED_FRAUD
SUSPECTED_FRAUD
FALSE_POSITIVE
RESOLVED
CLOSED
```

## UR-010 — Human Review

High-impact fraud decisions MUST support human review.

## UR-011 — AI Assistance

Authorized users MAY request AI-generated fraud analysis.

## UR-012 — AI Recommendations

AI MAY recommend:

* risk classification
* investigation steps
* evidence to inspect
* containment actions
* account actions
* payment actions

## UR-013 — Tenant Isolation

Organization administrators MUST only access fraud information belonging to their tenant.

## UR-014 — Fraud Appeals

Legitimate users SHOULD be able to appeal fraud-related restrictions.

## UR-015 — Decision Transparency

The platform SHOULD communicate appropriate fraud-related restrictions without exposing detection logic that would materially enable evasion.

---

## 7. System Requirements

## SR-001 — Distributed Fraud Detection Architecture

SalesGenie MUST implement a centralized fraud-detection control plane.

```text
                    +----------------------+
                    | Human Activity       |
                    +----------+-----------+
                               |
                    +----------v-----------+
                    | AI Activity          |
                    +----------+-----------+
                               |
                    +----------v-----------+
                    | Billing / Payments   |
                    +----------+-----------+
                               |
                    +----------v-----------+
                    | Subscriptions        |
                    +----------+-----------+
                               |
                    +----------v-----------+
                    | Usage / Credits      |
                    +----------+-----------+
                               |
                    +----------v-----------+
                    | Integrations / APIs  |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Event Collection     |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Event Normalization  |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Feature Engineering  |
                    +----------+-----------+
                               |
                +--------------+--------------+
                |                             |
                v                             v
        +------------------+         +-------------------+
        | Rule Engine      |         | ML/AI Detection   |
        +--------+---------+         +---------+---------+
                 |                             |
                 +-------------+---------------+
                               |
                               v
                    +----------------------+
                    | Fraud Correlation     |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Risk Scoring          |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Fraud Decision Engine |
                    +----------+-----------+
                               |
                 +-------------+-------------+
                 |                           |
                 v                           v
          Automated Controls          Human Investigation
                 |                           |
                 +-------------+-------------+
                               |
                               v
                    +----------------------+
                    | Case / Evidence Store |
                    +----------------------+
```

---

## 8. Fraud Telemetry Sources

The system MUST ingest fraud-relevant signals from:

```text
Authentication Service
Identity Service
Authorization Service
API Gateway
AI Gateway
Agent Orchestrator
Workflow Engine
Billing Service
Payment Service
Subscription Service
Pricing Engine
Coupon Service
Credit Service
Usage Tracking
Metered Billing
Invoice Service
Refund Service
Tax Service
CRM Integrations
Google Integrations
Gmail
Google Drive
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
Database Services
Object Storage
Audit Logs
Security Monitoring
Network Monitoring
```

---

## 9. Fraud Event Schema

Each fraud-relevant event SHOULD contain:

```yaml
event_id:
event_type:
event_version:

timestamp:
ingestion_timestamp:

tenant_id:

actor_type:
actor_id:
actor_role:

account_id:
organization_id:

session_id:
device_id:

source_ip:
source_country:
user_agent:

request_id:
trace_id:
correlation_id:

resource_type:
resource_id:

action:
result:

payment_id:
payment_method_id:
transaction_id:

subscription_id:
invoice_id:
refund_id:
coupon_id:
credit_id:

amount:
currency:

usage_metric:
usage_value:

ai_agent_id:
ai_model:
ai_agent_version:

integration_id:
workflow_id:

risk_score:
risk_level:

detection_rule_id:
fraud_case_id:

data_classification:

metadata:
```

Sensitive payment credentials MUST NOT be stored in raw form.

---

## 10. Fraud Detection Layers

SalesGenie MUST support multiple detection mechanisms:

```text
Layer 1 — Deterministic Rules
Layer 2 — Threshold Detection
Layer 3 — Velocity Detection
Layer 4 — Behavioral Baselines
Layer 5 — Statistical Anomaly Detection
Layer 6 — Machine Learning Classification
Layer 7 — Graph-Based Fraud Detection
Layer 8 — Device / Identity Correlation
Layer 9 — Cross-Event Correlation
Layer 10 — AI-Assisted Investigation
Layer 11 — Human Investigation
```

---

## 11. Rule-Based Fraud Detection

Fraud analysts MUST be able to define controlled rules.

Example:

```yaml
rule_id: PAYMENT_VELOCITY_001

name: Excessive Payment Attempts

conditions:
  payment_attempts:
    operator: ">="
    value: 10

  time_window:
    value: 10m

severity: HIGH

actions:
  - increase_risk
  - create_fraud_signal
```

---

## 12. Velocity Detection

The system MUST support velocity analysis across:

```text
Account
User
Organization
IP
Device
Payment Method
Card Fingerprint
Email
Phone
Coupon
Referral
API Key
AI Agent
Workflow
Integration
```

---

## 13. Payment Fraud Detection

The platform MUST detect suspicious payment behavior including:

```text
Repeated payment failures
Rapid payment attempts
Multiple payment methods
Multiple cards per account
Same payment method across unrelated accounts
Unusual transaction amount
Unusual transaction frequency
Unusual geographic behavior
Payment-method switching
Suspicious billing profile
```

---

## 14. Card Testing Detection

The platform SHOULD detect payment-method testing patterns.

Example:

```text
Account
 |
 +--> Card A → declined
 +--> Card B → declined
 +--> Card C → declined
 +--> Card D → declined
 +--> Card E → success
```

Combined with high velocity, this SHOULD increase fraud risk.

---

## 15. Payment Method Correlation

The system SHOULD identify relationships between:

```text
Payment Method
      |
      +--> Account A
      +--> Account B
      +--> Account C
      +--> Organization D
```

Repeated use across suspiciously related accounts SHOULD increase risk.

---

## 16. Chargeback Fraud Detection

The system SHOULD track:

```text
Chargeback history
Chargeback frequency
Transaction history
Refund history
Customer tenure
Subscription history
Payment history
```

and calculate chargeback-related risk.

---

## 17. Refund Fraud Detection

The platform MUST detect:

```text
Repeated refunds
Refund immediately after payment
Refund abuse across accounts
Refunds outside normal policy
Unusual refund amounts
High-value refund patterns
Employee refund anomalies
AI-generated refund anomalies
```

---

## 18. Refund Velocity

Example:

```text
User
 |
 +--> Refund #1
 +--> Refund #2
 +--> Refund #3
 +--> Refund #4
 +--> Refund #5
```

within a short period SHOULD trigger additional review.

---

## 19. Subscription Fraud

The platform MUST detect:

```text
Rapid subscription creation
Rapid cancellation
Repeated subscription cycling
Plan manipulation
Billing-period manipulation
Upgrade/downgrade abuse
Payment-method rotation
Subscription sharing abuse
```

---

## 20. Free-Tier Abuse

The system MUST detect attempts to create multiple free accounts to bypass limits.

Signals MAY include:

```text
Email similarity
Phone similarity
Device fingerprint
IP relationship
Payment relationship
Organization relationship
Behavioral similarity
Browser characteristics
API behavior
```

---

## 21. Trial Abuse

The platform MUST detect repeated trial usage intended to bypass commercial limits.

Example:

```text
Trial #1
   |
Expired
   |
Trial #2
   |
Expired
   |
Trial #3
```

Repeated patterns SHOULD increase fraud risk.

---

## 22. Multi-Account Fraud

The system SHOULD identify account clusters based on shared signals.

Potential relationship signals:

```text
Device
IP
Payment Method
Email Domain
Phone
Organization
API Key
Referral
Behavior
```

---

## 23. Synthetic Identity Detection

Where sufficient identity information exists, the system SHOULD detect inconsistent identity patterns.

Examples:

```text
Identity information
+
Payment information
+
Device information
+
Behavior
```

with significant contradictions SHOULD increase risk.

---

## 24. Account Takeover Fraud

The platform SHOULD detect:

```text
Credential anomaly
+
New device
+
New location
+
Password reset
+
Payment method change
+
Subscription change
```

as a potential account takeover.

---

## 25. Account Recovery Fraud

The system MUST monitor:

```text
Password reset
Email change
Phone change
MFA change
Recovery method change
Payment method change
```

and detect suspicious sequences.

---

## 26. Coupon Fraud

The platform MUST detect:

```text
Repeated coupon use
Coupon stacking
Coupon sharing
Coupon cycling
Expired coupon exploitation
Coupon enumeration
Coupon brute force
Coupon redemption across suspicious accounts
```

---

## 27. Coupon Enumeration

The system SHOULD detect repeated attempts to discover valid coupon codes.

Example:

```text
CODE001
CODE002
CODE003
...
CODE999
```

with abnormal frequency SHOULD trigger abuse detection.

---

## 28. Promotional Abuse

The system SHOULD detect coordinated exploitation of:

```text
Discounts
Promotions
Referral rewards
Free credits
Trial credits
Free-tier allowances
Campaign incentives
```

---

## 29. Credit Fraud

The system MUST detect:

```text
Unusual credit grants
Repeated credit consumption
Credit transfers
Credit refund manipulation
Credit balance manipulation
Negative balance exploitation
Credit generation anomalies
```

---

## 30. Usage-Based Billing Fraud

The system MUST detect suspicious usage patterns.

Examples:

```text
Artificial usage generation
Usage spikes
Usage replay
Usage deletion
Usage modification
Meter manipulation
Synthetic API traffic
AI-generated traffic intended to manipulate billing
```

---

## 31. Metering Integrity

Usage records SHOULD be immutable or tamper-evident after billing finalization.

The platform MUST detect unexpected modifications.

---

## 32. Billing Manipulation

The system SHOULD monitor:

```text
Plan changes
Price changes
Usage changes
Invoice changes
Credit changes
Tax changes
Refund changes
Payment changes
```

for suspicious patterns.

---

## 33. Invoice Fraud Detection

The system SHOULD detect:

```text
Unexpected invoice amount
Repeated invoice generation
Invoice modification
Invoice deletion
Invoice status manipulation
Unusual invoice credits
```

---

## 34. Pricing Abuse

The platform MUST monitor unusual use of:

```text
Coupons
Promotions
Plan limits
Feature entitlements
Credits
Usage overrides
Custom pricing
Enterprise discounts
```

---

## 35. Referral Fraud

The system SHOULD detect:

```text
Self-referrals
Circular referrals
Referral farming
Multiple accounts
Device sharing
Payment sharing
Suspicious referral clusters
```

---

## 36. Bot-Driven Fraud

The platform MUST detect automated abuse involving:

```text
Registration
Login
Trial activation
Coupon redemption
Payment attempts
API usage
Refund requests
Referral generation
```

---

## 37. API Fraud Detection

The system SHOULD identify:

```text
API key sharing
API key rotation anomalies
Automated account creation
High request velocity
Resource enumeration
Usage manipulation
Billing manipulation
```

---

## 38. AI-Driven Fraud

AI activity MUST be treated as a fraud-relevant actor.

The system MUST monitor:

```text
AI Agent
 |
 +--> User
 +--> Organization
 +--> Payment
 +--> Subscription
 +--> Coupon
 +--> Credit
 +--> Usage
 +--> Refund
 +--> External API
```

---

## 39. AI Agent Financial Permissions

AI agents MUST have explicit financial permissions.

Example:

```yaml
agent_id:
financial_permissions:
  view_billing: true
  create_subscription: true
  upgrade_plan: false
  issue_refund: false
  grant_credit: false
  modify_coupon: false
```

---

## 40. AI Refund Fraud Detection

The system MUST monitor AI-issued or AI-recommended refunds.

High-risk refunds SHOULD require human approval.

---

## 41. AI Credit Abuse Detection

AI agents MUST NOT be allowed to issue unlimited credits.

Credit operations MUST enforce:

```text
Per-action limit
Per-user limit
Per-agent limit
Per-organization limit
Time-window limit
Approval requirement
```

---

## 42. AI Coupon Abuse

The system SHOULD detect AI agents repeatedly generating or applying promotional benefits outside their authorized policy.

---

## 43. AI Usage Manipulation

The platform SHOULD detect AI agents generating artificial usage to:

```text
consume credits
trigger billing
inflate usage
trigger commissions
bypass limits
```

---

## 44. AI Agent Collusion

The system SHOULD identify suspicious multi-agent behavior.

Example:

```text
Agent A
  |
  v
Creates account

Agent B
  |
  v
Generates trial

Agent C
  |
  v
Consumes credits

Agent D
  |
  v
Requests refund
```

Such correlated behavior SHOULD increase fraud risk.

---

## 45. Workflow Fraud

The workflow engine MUST detect workflows that:

```text
Create accounts
+
Apply promotions
+
Consume credits
+
Generate usage
+
Trigger refunds
```

at abnormal velocity.

---

## 46. Recursive Workflow Fraud

The system MUST detect recursive or chained workflows capable of generating artificial financial activity.

---

## 47. Integration Fraud

Fraud detection SHOULD monitor external integrations for:

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

Signals SHOULD include:

```text
Unexpected API activity
Token changes
OAuth scope expansion
Abnormal request rates
Account switching
Unusual geographic origin
Data synchronization anomalies
```

---

## 48. Employee Fraud Detection

Where legally and organizationally appropriate, the system SHOULD detect:

```text
Unusual refunds
Unusual credits
Unusual coupon application
Unusual plan changes
Unusual invoice modification
Unusual customer-account manipulation
```

---

## 49. Privileged Financial Activity

Privileged operations MUST be risk-scored.

Examples:

```text
Manual refund
Credit adjustment
Plan override
Price override
Invoice adjustment
Tax override
Subscription modification
```

---

## 50. Four-Eyes Principle

High-value or high-risk financial operations SHOULD support dual approval.

Example:

```text
Operator
   |
   v
Refund Request
   |
   v
Risk Evaluation
   |
   v
Second Approver
   |
   v
Execution
```

---

## 51. Fraud Correlation Engine

The system MUST correlate fraud signals using:

```text
tenant_id
account_id
user_id
organization_id
session_id
device_id
source_ip
payment_method_id
transaction_id
subscription_id
invoice_id
refund_id
coupon_id
credit_id
api_key_id
ai_agent_id
workflow_id
integration_id
```

---

## 52. Fraud Graph

SalesGenie SHOULD maintain a relationship graph:

```text
                 +-------------+
                 |    User     |
                 +------+------+
                        |
          +-------------+-------------+
          |             |             |
          v             v             v
       Device           IP       Payment Method
          |             |             |
          +-------------+-------------+
                        |
                        v
                     Account
                        |
          +-------------+-------------+
          |             |             |
          v             v             v
     Subscription     Coupon       Credit
          |
          v
       Usage
          |
          v
       Invoice
          |
          v
       Payment
```

Graph analysis MAY identify coordinated fraud.

---

## 53. Fraud Ring Detection

The system SHOULD detect clusters containing:

```text
Multiple accounts
+
Shared devices
+
Shared payment methods
+
Shared IP ranges
+
Shared behavioral patterns
+
Shared promotional activity
```

---

## 54. Cross-Account Correlation

The platform MUST correlate activity across accounts where platform-level authorization permits it.

Tenant administrators MUST NOT receive cross-tenant data.

---

## 55. Behavioral Baselines

The system SHOULD establish baselines for:

```text
Users
Organizations
Payment behavior
Subscription behavior
Usage
AI agents
Workflows
Integrations
Employees
```

---

## 56. Behavioral Anomaly

Example:

```text
Normal monthly usage:
10,000 API calls

Observed:
2,000,000 API calls

AND

new payment method

AND

new device

Result:
HIGH FRAUD RISK
```

---

## 57. Transaction Risk Scoring

Every eligible transaction SHOULD receive a risk evaluation based on:

```text
Transaction Amount
Payment History
Account Age
Customer History
Velocity
Device
IP
Location
Payment Method
Chargeback History
Refund History
Coupon Usage
Trial History
Subscription History
Behavioral Anomaly
Graph Relationships
AI Activity
Threat Intelligence
```

---

## 58. Account Risk Scoring

Account risk SHOULD incorporate:

```text
Account age
Authentication history
Device relationships
Payment history
Subscription behavior
Refund behavior
Coupon behavior
Usage behavior
API behavior
AI activity
Fraud history
Related accounts
```

---

## 59. Organization Risk Scoring

Organization risk SHOULD incorporate:

```text
User count
Payment history
Usage behavior
Refund patterns
Credit usage
Subscription behavior
API activity
Administrative behavior
Related accounts
Fraud history
```

---

## 60. Dynamic Risk

Risk MUST be recalculated when material new evidence arrives.

Example:

```text
Initial Risk = 32

New payment anomaly
       |
       v
Risk = 51

New account relationship
       |
       v
Risk = 73

Confirmed suspicious transaction
       |
       v
Risk = 91
```

---

## 61. Fraud Decision Engine

The decision engine SHOULD produce:

```yaml
decision:
risk_score:
risk_level:
confidence:
decision_reason:
signals:
recommended_action:
required_approval:
expires_at:
policy_version:
```

---

## 62. Fraud Decision Outcomes

Supported outcomes SHOULD include:

```text
ALLOW
ALLOW_WITH_MONITORING
STEP_UP_VERIFICATION
REVIEW
DELAY
LIMIT
BLOCK
REJECT
SUSPEND
```

---

## 63. Step-Up Verification

For suspicious but inconclusive behavior, the system SHOULD request additional verification rather than immediately blocking the user.

Possible controls:

```text
MFA
Email verification
Phone verification
Identity verification
Payment re-authentication
Human review
```

---

## 64. Adaptive Fraud Controls

Controls SHOULD be proportional to risk.

```text
LOW
  |
  v
Monitor

MEDIUM
  |
  v
Additional Verification

HIGH
  |
  v
Review / Limit

CRITICAL
  |
  v
Block / Suspend / Investigate
```

---

## 65. Automated Fraud Prevention

The system MAY automatically:

```text
Reject transaction
Pause subscription
Require MFA
Restrict coupon
Limit credits
Pause workflow
Restrict AI agent
Revoke session
Require human review
Temporarily restrict account
```

Only approved policies MAY trigger automatic actions.

---

## 66. Human Approval

The following SHOULD require human approval:

```text
Permanent account suspension
Large refund
Large credit grant
Organization suspension
Permanent billing restriction
Large-scale subscription cancellation
High-value financial adjustment
```

---

## 67. AI Fraud Investigation

AI MAY:

```text
Summarize evidence
Correlate transactions
Identify suspicious patterns
Analyze account relationships
Identify fraud rings
Estimate fraud probability
Recommend investigation steps
Recommend controls
Draft case summaries
```

---

## 68. AI Evidence Grounding

AI fraud analysis MUST reference underlying evidence.

Example:

```yaml
finding:
  type: PAYMENT_FRAUD

confidence:
  0.94

evidence:
  - transaction_id: TXN-001
  - account_id: ACC-001
  - device_id: DEV-009
  - event_id: EVT-882
```

---

## 69. AI Hallucination Controls

AI output MUST distinguish:

```text
OBSERVED
INFERRED
SUSPECTED
RECOMMENDED
CONFIRMED
```

AI MUST NOT present an inference as confirmed fraud without sufficient evidence.

---

## 70. AI Fraud Decision Restrictions

AI MUST NOT independently:

* Confirm criminal activity.
* Permanently ban users without policy authorization.
* Issue unrestricted refunds.
* Grant unrestricted credits.
* Modify financial records.
* Delete fraud evidence.
* Suppress fraud alerts.
* Modify fraud rules without authorization.
* Bypass payment controls.
* Bypass RBAC.
* Access unrelated tenants.

---

## 71. Fraud Case Management

Each case SHOULD contain:

```yaml
case_id:
tenant_id:
status:
priority:
fraud_type:
risk_score:
confidence:
subject_type:
subject_id:
assigned_to:
created_at:
updated_at:
evidence:
related_events:
related_transactions:
related_accounts:
actions:
resolution:
resolution_reason:
```

---

## 72. Fraud Case Evidence

Evidence MAY include:

```text
Authentication events
Payment events
Subscription events
Usage events
Refund events
Coupon events
Credit events
Invoice events
API events
AI actions
Workflow executions
Integration activity
Device signals
IP signals
Relationship graph
```

---

## 73. Evidence Integrity

Fraud evidence SHOULD support:

```text
Immutable storage
Hashing
Timestamping
Tamper detection
Versioning
Access auditing
Retention policy
```

---

## 74. Fraud Case Timeline

Example:

```text
09:01 Account Created
09:02 Trial Activated
09:03 Coupon Applied
09:05 Credit Granted
09:06 Usage Spike
09:07 Subscription Created
09:08 Payment Failed
09:09 Payment Method Changed
09:10 Payment Succeeded
09:11 Refund Requested
09:12 Fraud Detected
09:13 Transaction Restricted
09:14 Analyst Assigned
```

---

## 75. Fraud Alert Deduplication

Multiple related signals SHOULD be grouped into one fraud case where appropriate.

Example:

```text
1,000 payment failures
        |
        v
1 correlated CARD_TESTING case
```

---

## 76. Alert Fatigue Prevention

The system MUST minimize unnecessary alerts through:

```text
Deduplication
Correlation
Risk thresholds
Suppression
Behavioral baselines
Case grouping
Adaptive thresholds
```

---

## 77. False Positive Management

Fraud analysts MUST be able to classify:

```text
TRUE_FRAUD
SUSPECTED_FRAUD
FALSE_POSITIVE
BENIGN
DUPLICATE
INCONCLUSIVE
```

---

## 78. Fraud Model Feedback

Approved investigation outcomes SHOULD feed model/rule improvement pipelines.

```text
Detection
   |
   v
Investigation
   |
   v
Classification
   |
   v
Analyst Feedback
   |
   v
Model / Rule Evaluation
   |
   v
Validation
   |
   v
Production
```

---

## 79. Machine Learning Fraud Models

The platform SHOULD support models for:

```text
Transaction Risk
Account Risk
Payment Risk
Subscription Risk
Coupon Abuse
Trial Abuse
Refund Abuse
Credit Abuse
Usage Abuse
Account Takeover
Fraud Ring Detection
Bot Detection
```

---

## 80. ML Feature Store

Fraud features SHOULD include:

```text
transaction_velocity
payment_failure_rate
refund_rate
coupon_redemption_rate
trial_count
account_age
device_count
ip_count
payment_method_count
shared_payment_accounts
usage_velocity
subscription_change_rate
login_anomaly_score
api_velocity
ai_action_velocity
related_account_count
```

---

## 81. Feature Freshness

Time-sensitive fraud features SHOULD support near-real-time updates.

---

## 82. Model Versioning

Every production fraud model MUST have:

```text
model_id
version
training_data_version
feature_schema_version
evaluation_metrics
approval_status
deployment_status
rollback_version
```

---

## 83. Model Drift

The system SHOULD monitor:

```text
Feature Drift
Prediction Drift
Fraud Rate Drift
False Positive Drift
False Negative Indicators
Data Quality Drift
```

---

## 84. Model Explainability

Fraud models SHOULD expose interpretable risk factors.

Example:

```text
+30  High payment velocity
+20  New device
+15  Multiple failed payments
+12  Shared payment method
+10  Abnormal refund pattern
--------------------------------
 87  CRITICAL
```

---

## 85. Graph-Based Fraud Detection

Graph analysis SHOULD identify:

```text
Account clusters
Payment-method clusters
Device clusters
IP clusters
Referral networks
Coupon networks
Transaction networks
AI-agent relationships
Workflow relationships
```

---

## 86. Ring Detection Example

```text
Account A
   |
Device X
   |
Account B
   |
Payment P
   |
Account C
   |
Coupon Z
   |
Account D
```

A dense suspicious cluster SHOULD receive elevated fraud risk.

---

## 87. Temporal Fraud Detection

The platform MUST support time-window analysis.

Examples:

```text
5 minutes
1 hour
24 hours
7 days
30 days
Billing period
Subscription lifetime
```

---

## 88. Fraud Sequence Detection

The platform SHOULD detect suspicious sequences.

Example:

```text
Account Creation
      ↓
Trial Activation
      ↓
Coupon Redemption
      ↓
Credit Consumption
      ↓
Usage Spike
      ↓
Refund
```

---

## 89. Fraud Pattern Replay

Fraud rules and models SHOULD be testable against historical events.

The platform SHOULD support:

```text
Historical replay
Simulation
Backtesting
What-if analysis
Threshold testing
Model comparison
```

---

## 90. Fraud Rule Governance

Every fraud rule MUST support:

```text
rule_id
version
owner
status
severity
conditions
actions
created_at
updated_at
approved_by
```

---

## 91. Fraud Rule Lifecycle

```text
DRAFT
TESTING
APPROVED
ACTIVE
DISABLED
DEPRECATED
ROLLED_BACK
```

---

## 92. Fraud Rule Safety

Rules MUST prevent:

```text
Infinite action loops
Unbounded blocking
Cross-tenant effects
Unauthorized financial changes
Alert storms
```

---

## 93. Fraud Control Policies

Policies SHOULD define:

```yaml
policy_id:
scope:
risk_threshold:
required_action:
approval_required:
maximum_amount:
time_window:
tenant_scope:
actor_scope:
exceptions:
```

---

## 94. Tenant-Specific Fraud Policies

Enterprise organizations MAY configure fraud thresholds within platform limits.

Platform-level security controls MUST remain authoritative.

---

## 95. Cross-Tenant Fraud Detection

Platform security MAY correlate signals across tenants only where:

```text
Legal basis exists
Platform authorization exists
Privacy controls permit it
Data minimization is enforced
```

Tenant administrators MUST never receive another tenant's fraud evidence.

---

## 96. Payment Data Protection

The fraud system MUST NOT store:

```text
Full card number
CVV
Raw payment credentials
Payment authentication secrets
```

where unnecessary.

Tokenized payment identifiers SHOULD be used.

---

## 97. PII Protection

Fraud telemetry SHOULD minimize:

```text
Name
Address
Phone
Email
Identity documents
```

and apply masking where possible.

---

## 98. Fraud Data Encryption

Fraud evidence MUST be encrypted:

```text
In Transit
At Rest
During sensitive processing where applicable
```

---

## 99. Fraud Data Retention

Fraud data MUST follow configurable retention policies.

Retention SHOULD distinguish:

```text
Active cases
Closed cases
Fraud evidence
False positives
Aggregated features
Model-training data
Audit records
```

---

## 100. Fraud Investigation Access

Fraud case access MUST use least privilege.

Permissions SHOULD include:

```text
fraud.case.read
fraud.case.create
fraud.case.assign
fraud.case.investigate
fraud.case.resolve
fraud.case.export
fraud.rule.manage
fraud.model.manage
fraud.response.execute
```

---

## 101. Privileged Fraud Actions

High-impact actions MUST require elevated permissions.

---

## 102. Fraud Action Audit

Every fraud-related action MUST generate an audit event.

Examples:

```text
Fraud Case Created
Risk Changed
Account Restricted
Transaction Blocked
Refund Held
Credit Frozen
Coupon Disabled
Rule Changed
Model Changed
Case Resolved
Evidence Exported
```

---

## 103. Fraud Notifications

The system MAY notify through:

```text
In-App
Email
Slack
Microsoft Teams
Webhook
Incident Management System
```

---

## 104. Critical Fraud Notification

Critical fraud SHOULD trigger redundant notifications.

```text
CRITICAL FRAUD
      |
      +--> Security
      +--> Fraud Team
      +--> Finance
      +--> Incident System
```

---

## 105. Fraud Dashboard

SalesGenie SHOULD provide a Fraud Command Center containing:

```text
Fraud Risk Overview
Critical Cases
High-Risk Transactions
Account Fraud
Payment Fraud
Subscription Fraud
Coupon Abuse
Trial Abuse
Credit Abuse
Refund Abuse
Usage Fraud
AI Fraud
Workflow Fraud
Integration Fraud
Fraud Rings
Case Queue
Detection Health
Model Health
```

---

## 106. Transaction Risk Dashboard

The dashboard SHOULD display:

```text
Transaction
Amount
Risk Score
Risk Level
Confidence
Payment Method
Account
Device
Location
Related Transactions
Fraud Signals
Decision
Action
```

---

## 107. Account Risk Dashboard

The dashboard SHOULD display:

```text
Account Risk
Account Age
Authentication History
Payment History
Subscription History
Refund History
Coupon History
Credit History
Usage History
Related Accounts
Devices
IPs
Fraud Cases
```

---

## 108. Fraud Ring Dashboard

Investigators SHOULD be able to visualize:

```text
Accounts
Devices
IPs
Payment Methods
Coupons
Referrals
Transactions
Subscriptions
AI Agents
Workflows
```

as related entities.

---

## 109. AI Fraud Dashboard

The platform SHOULD provide:

```text
AI Fraud Cases
Agent Risk
Financial Actions
Refunds
Credits
Coupons
Subscriptions
Usage
Tool Calls
Workflow Actions
Human Approvals
Policy Violations
```

---

## 110. Fraud Analytics

The platform SHOULD provide:

```text
Fraud Rate
Fraud Loss
Prevented Loss
False Positive Rate
Fraud Detection Rate
Chargeback Rate
Refund Abuse Rate
Coupon Abuse Rate
Trial Abuse Rate
Credit Abuse Rate
Account Takeover Rate
AI Fraud Rate
Fraud Ring Count
```

---

## 111. Fraud KPIs

The platform MUST measure:

```text
Fraud Detection Rate
False Positive Rate
False Negative Indicators
Fraud Loss
Prevented Fraud Loss
Average Fraud Score
Detection Latency
Decision Latency
Investigation Time
Containment Time
Resolution Time
```

---

## 112. Fraud Operations Metrics

The system SHOULD expose:

```text
MTTD — Mean Time to Detect
MTTA — Mean Time to Acknowledge
MTTC — Mean Time to Contain
MTTR — Mean Time to Resolve
```

---

## 113. Fraud Detection Health

The fraud detection system MUST monitor:

```text
Events Received
Events Processed
Events Dropped
Events Delayed
Rule Latency
ML Latency
AI Latency
Correlation Latency
Decision Latency
Queue Depth
Model Availability
Feature Availability
```

---

## 114. Fraud Detection Blind Spots

The system MUST detect when expected telemetry disappears.

Example:

```text
Payment Service
      |
      v
Expected events
      |
      X
No telemetry
      |
      v
FRAUD DETECTION BLIND SPOT
```

---

## 115. Event Reliability

Critical financial events MUST NOT be silently lost.

The system SHOULD support:

```text
Durable Queues
Retries
Dead-Letter Queues
Idempotency
Replay
Backpressure
```

---

## 116. Duplicate Event Handling

Duplicate payment, refund, subscription, and usage events MUST NOT cause duplicate financial actions.

---

## 117. Idempotent Fraud Decisions

Fraud decisions MUST be idempotent.

Repeated processing of the same event MUST NOT create uncontrolled restrictions.

---

## 118. Fraud Detection Availability

Recommended target:

```text
Fraud Detection Control Plane >= 99.99%
```

Critical transaction-risk evaluation SHOULD remain available during partial infrastructure failures.

---

## 119. Degraded Mode

If ML/AI detection is unavailable:

```text
ML/AI
  |
  X
  |
  v
Deterministic Rules
  |
  v
Velocity Controls
  |
  v
Policy Enforcement
```

Core fraud-prevention controls MUST continue operating.

---

## 120. Fraud Detection Scalability

SalesGenie MUST support fraud detection across:

```text
10M+ users
500K+ concurrent conversations
Large-scale transactions
Large-scale API traffic
Millions of usage events
Large-scale AI agent activity
Large-scale workflow execution
Large-scale integration traffic
```

Fraud services MUST scale horizontally.

---

## 121. Fraud Detection Performance

Recommended targets:

| Operation                  |       Target |
| -------------------------- | -----------: |
| Real-time transaction risk | < 300 ms p95 |
| Critical fraud signal      |     < 60 sec |
| High-risk signal           |      < 2 min |
| Risk API                   | < 300 ms p95 |
| Fraud investigation query  | < 500 ms p95 |
| Case search                |  < 1 sec p95 |
| Alert delivery             |     < 60 sec |

Targets MUST be validated using production-like workloads.

---

## 122. Fraud Detection Security

The fraud platform itself MUST be protected against:

```text
Rule Tampering
Model Tampering
Feature Manipulation
Evidence Deletion
Alert Suppression
Risk Score Manipulation
Decision Bypass
Tenant Isolation Bypass
Privilege Escalation
Insider Abuse
```

---

## 123. Adversarial Fraud Detection

The system SHOULD be tested against:

```text
Velocity Evasion
Device Rotation
IP Rotation
Account Rotation
Payment Method Rotation
Coupon Rotation
Referral Rotation
Behavioral Mimicry
API Rate Evasion
Distributed Automation
AI Agent Evasion
Workflow Evasion
```

---

## 124. Fraud Model Adversarial Testing

Models SHOULD be evaluated against:

```text
Feature manipulation
Data poisoning
Adversarial examples
Concept drift
Fraud-pattern evolution
Synthetic fraud behavior
```

---

## 125. AI Fraud Adversarial Testing

AI systems MUST be tested against:

```text
Prompt manipulation
Tool manipulation
Policy bypass
Financial action escalation
Refund manipulation
Credit manipulation
Coupon manipulation
Usage generation
Multi-agent collusion
Workflow abuse
```

---

## 126. AI + Human Fraud Operating Model

```text
                    FRAUD TELEMETRY
                           |
                           v
                  +-------------------+
                  | Deterministic     |
                  | Rules             |
                  +---------+---------+
                            |
                            v
                  +-------------------+
                  | Velocity /        |
                  | Behavioral        |
                  +---------+---------+
                            |
                            v
                  +-------------------+
                  | ML Fraud Models   |
                  +---------+---------+
                            |
                            v
                  +-------------------+
                  | AI Investigation  |
                  +---------+---------+
                            |
                            v
                  +-------------------+
                  | Correlation       |
                  +---------+---------+
                            |
                            v
                  +-------------------+
                  | Risk Engine       |
                  +---------+---------+
                            |
                +-----------+-----------+
                |                       |
                v                       v
        Automated Policy         Human Analyst
                |                       |
                +-----------+-----------+
                            |
                            v
                    Fraud Decision
                            |
                            v
                       Response
                            |
                            v
                    Evidence Store
                            |
                            v
                     Feedback Loop
```

---

## 127. Fraud Prevention Workflow

```text
Transaction / Activity
        |
        v
Telemetry Collection
        |
        v
Normalization
        |
        v
Feature Extraction
        |
        v
Rule Evaluation
        |
        v
Behavioral Analysis
        |
        v
ML Evaluation
        |
        v
AI Investigation
        |
        v
Risk Correlation
        |
        v
Fraud Score
        |
        v
Decision Engine
        |
   +----+----+
   |         |
   v         v
Allow     Restrict
             |
             v
       Human Review
             |
             v
       Final Decision
             |
             v
          Evidence
             |
             v
          Feedback
```

---

## 128. Example — Payment Fraud Workflow

```text
Payment Attempt
      |
      v
Velocity Check
      |
      v
Payment History
      |
      v
Device Correlation
      |
      v
IP Correlation
      |
      v
Account Risk
      |
      v
Payment Risk
      |
      v
Fraud Graph
      |
      v
Risk Score
      |
      +---- < 40 ----> ALLOW
      |
      +---- 40–69 ---> MONITOR / VERIFY
      |
      +---- 70–89 ---> REVIEW / LIMIT
      |
      +---- 90+ -----> BLOCK / INVESTIGATE
```

---

## 129. Example — Free-Tier Abuse Workflow

```text
New Account
    |
    v
Identity Signals
    |
    v
Device Signals
    |
    v
IP Signals
    |
    v
Existing Account Correlation
    |
    v
Trial / Free Usage History
    |
    v
Risk Score
    |
    +---- Low ------> Grant Free Tier
    |
    +---- Medium ---> Verify
    |
    +---- High -----> Restrict
```

---

## 130. Example — Coupon Abuse Workflow

```text
Coupon Redemption
        |
        v
Coupon Validity
        |
        v
Account History
        |
        v
Redemption Velocity
        |
        v
Device / IP Correlation
        |
        v
Related Accounts
        |
        v
Promotion Abuse Model
        |
        v
Risk Score
        |
        +---- Allow
        |
        +---- Review
        |
        +---- Reject
```

---

## 131. Example — Refund Fraud Workflow

```text
Refund Request
      |
      v
Customer History
      |
      v
Refund Frequency
      |
      v
Payment History
      |
      v
Subscription History
      |
      v
AI / Human Initiator
      |
      v
Refund Risk
      |
      +---- Low ------> Auto Process
      |
      +---- Medium ---> Review
      |
      +---- High -----> Hold + Investigate
```

---

## 132. Example — AI Financial Fraud Workflow

```text
AI Agent
   |
   v
Financial Action
   |
   v
Agent Identity
   |
   v
Permission Check
   |
   v
Behavioral Baseline
   |
   v
Action Velocity
   |
   v
Customer Risk
   |
   v
Financial Risk
   |
   v
Fraud Decision
   |
   +---- Approved
   |
   +---- Human Review
   |
   +---- Blocked
```

---

## 133. Fraud Investigation Workflow

```text
Fraud Signal
    |
    v
Case Created
    |
    v
AI Triage
    |
    v
Risk Classification
    |
    v
Evidence Collection
    |
    v
Relationship Analysis
    |
    v
Human Investigation
    |
    +---- False Positive
    |
    +---- Suspected Fraud
    |
    +---- Confirmed Fraud
             |
             v
        Containment
             |
             v
        Remediation
             |
             v
        Case Closure
             |
             v
        Model Feedback
```

---

## 134. Fraud Case Lifecycle

```text
DETECTED
   ↓
TRIAGED
   ↓
INVESTIGATING
   ↓
ACTION_REQUIRED
   ↓
CONFIRMED_FRAUD
   ↓
CONTAINED
   ↓
RESOLVED
   ↓
CLOSED
```

Alternative terminal state:

```text
FALSE_POSITIVE
```

---

## 135. Fraud Response Actions

Supported controls SHOULD include:

```text
Transaction Block
Payment Hold
Step-Up Verification
Account Restriction
Account Suspension
Session Revocation
Coupon Restriction
Credit Freeze
Credit Limit Reduction
Usage Limit Reduction
Subscription Hold
Workflow Pause
AI Agent Restriction
Integration Restriction
API Rate Limiting
Manual Review
```

---

## 136. Response Authorization

Every automated response MUST verify:

```text
Actor Authorization
Tenant Scope
Resource Scope
Fraud Policy
Risk Threshold
Action Limits
Approval Requirements
```

---

## 137. Response Rollback

Where technically possible, fraud controls SHOULD support rollback.

Example:

```text
False Positive
      |
      v
Restriction
      |
      v
Analyst Review
      |
      v
Rollback
      |
      v
Account Restored
```

---

## 138. Fraud Appeals

The platform SHOULD provide an appeal workflow:

```text
Restriction
    |
    v
User Appeal
    |
    v
Evidence Collection
    |
    v
Human Review
    |
    +---- Uphold
    |
    +---- Reverse
    |
    +---- Request Verification
```

---

## 139. Fraud Intelligence

The platform SHOULD maintain historical fraud intelligence including:

```text
Known Fraud Patterns
Known Fraud Accounts
Known Fraud Relationships
Fraud Ring Indicators
Previous Fraud Cases
Chargeback Patterns
Coupon Abuse Patterns
Trial Abuse Patterns
AI Fraud Patterns
```

---

## 140. Fraud Detection Feedback Loop

```text
Fraud Detection
      |
      v
Human Investigation
      |
      v
Confirmed Outcome
      |
      v
Feature / Rule Feedback
      |
      v
Model Evaluation
      |
      v
Backtesting
      |
      v
Approval
      |
      v
Production
```

---

## 141. Fraud Detection Quality

The system SHOULD optimize for:

```text
High Recall
+
High Precision
+
Low False Positives
+
Low Detection Latency
+
Low Decision Latency
+
Explainability
+
Operational Reliability
```

---

## 142. Fraud Detection Coverage Matrix

| Fraud Type         | Signals           | Detection          | Decision | Human Review      | Evidence |
| ------------------ | ----------------- | ------------------ | -------- | ----------------- | -------- |
| Payment Fraud      | Payment/Account   | Rules + ML         | Yes      | Optional          | Yes      |
| Card Testing       | Payment Velocity  | Rules + ML         | Yes      | Optional          | Yes      |
| Refund Abuse       | Refund History    | Rules + Behavioral | Yes      | Yes for high risk | Yes      |
| Trial Abuse        | Identity/Device   | Behavioral + Graph | Yes      | Optional          | Yes      |
| Free-Tier Abuse    | Account/Device/IP | Graph + Behavioral | Yes      | Optional          | Yes      |
| Coupon Abuse       | Redemption        | Rules + Graph      | Yes      | Optional          | Yes      |
| Credit Abuse       | Credit Events     | Rules + Behavioral | Yes      | Yes for high risk | Yes      |
| Usage Fraud        | Metering/API      | Behavioral + ML    | Yes      | Optional          | Yes      |
| Subscription Fraud | Subscription      | Rules + ML         | Yes      | Optional          | Yes      |
| Account Takeover   | Auth/Device       | Behavioral         | Yes      | Yes               | Yes      |
| Fraud Ring         | Graph             | Graph ML           | Yes      | Yes               | Yes      |
| AI Fraud           | Agent/Tool        | AI + Rules         | Yes      | Yes               | Yes      |
| Workflow Fraud     | Workflow          | Behavioral         | Yes      | Optional          | Yes      |
| Integration Fraud  | OAuth/API         | Behavioral         | Yes      | Optional          | Yes      |
| Insider Fraud      | Audit/Finance     | Behavioral         | Review   | Yes               | Yes      |

---

## 143. Non-Functional Requirements

| Category         | Requirement                       |
| ---------------- | --------------------------------- |
| Availability     | >= 99.99% target                  |
| Scalability      | Millions of events                |
| Latency          | Near-real-time risk decisions     |
| Accuracy         | High precision and recall         |
| Reliability      | Durable event processing          |
| Security         | Defense in depth                  |
| Privacy          | Data minimization                 |
| Explainability   | Evidence-backed decisions         |
| Tenant Isolation | Mandatory                         |
| AI Governance    | Policy-controlled AI              |
| Human Oversight  | Required for high-impact actions  |
| Auditability     | Complete decision history         |
| Resilience       | Degraded-mode operation           |
| Extensibility    | Versioned rules/models            |
| Observability    | End-to-end fraud telemetry        |
| Integrity        | Tamper-evident evidence           |
| Performance      | Horizontally scalable             |
| Compliance       | Configurable retention and access |

---

## 144. Security Invariants

## SI-001

Fraud scores MUST NOT be directly modifiable by ordinary users.

## SI-002

Fraud evidence MUST be tenant-isolated.

## SI-003

AI MUST NOT fabricate fraud evidence.

## SI-004

AI MUST NOT modify source fraud telemetry.

## SI-005

Financial actions MUST pass authorization.

## SI-006

High-impact automated restrictions MUST be policy-controlled.

## SI-007

Fraud rules MUST be versioned.

## SI-008

Fraud models MUST be versioned.

## SI-009

Fraud cases MUST be auditable.

## SI-010

Fraud evidence MUST be protected from unauthorized deletion.

## SI-011

Payment credentials MUST never appear in raw fraud telemetry.

## SI-012

Cross-tenant fraud intelligence MUST respect privacy and authorization boundaries.

## SI-013

Fraud detection MUST continue operating in degraded mode.

## SI-014

Duplicate events MUST NOT cause duplicate financial actions.

## SI-015

AI agents MUST operate under least privilege.

---

## 145. Testing Requirements

## Unit Tests

MUST cover:

```text
Rule Evaluation
Risk Scoring
Velocity Detection
Feature Calculation
Graph Relationships
Decision Policies
Tenant Filtering
PII Masking
Payment Token Handling
Alert Deduplication
Case Creation
```

## Integration Tests

MUST cover:

```text
Authentication
Billing
Payments
Subscriptions
Pricing
Coupons
Credits
Usage
Metering
Invoices
Refunds
API Gateway
AI Gateway
Workflow Engine
Integrations
Audit Logging
Notification Services
```

---

## 146. Fraud Simulation Tests

The system MUST simulate:

```text
Card Testing
Payment Velocity Attack
Refund Abuse
Coupon Abuse
Trial Abuse
Free-Tier Abuse
Multi-Account Abuse
Referral Abuse
Credit Abuse
Usage Manipulation
Account Takeover
Fraud Ring
API Automation
Bot Abuse
AI Financial Abuse
Workflow Fraud
Integration Fraud
Insider Fraud
```

---

## 147. Load Testing

The platform MUST validate fraud detection under:

```text
Normal Traffic
Peak Traffic
Traffic Spike
Fraud Burst
Mass Account Creation
Mass Payment Attempts
Mass API Requests
Mass AI Agent Actions
Mass Workflow Execution
```

---

## 148. Chaos Testing

The fraud platform SHOULD test:

```text
Event Bus Failure
Database Failure
Feature Store Failure
ML Service Failure
AI Service Failure
Payment Service Failure
Network Partition
Queue Saturation
Notification Failure
Telemetry Loss
```

---

## 149. Red-Team Requirements

Red-team exercises SHOULD attempt to:

```text
Evade velocity detection
Rotate devices
Rotate IPs
Rotate accounts
Rotate payment methods
Distribute fraudulent activity
Manipulate usage
Exploit coupon systems
Exploit trial systems
Exploit credits
Exploit refunds
Exploit subscriptions
Manipulate AI agents
Manipulate workflows
Bypass human approval
Poison fraud features
Manipulate telemetry
Suppress alerts
```

---

## 150. Fraud Detection SLOs

Recommended targets:

| Metric                         |       Target |
| ------------------------------ | -----------: |
| Fraud detection availability   |    >= 99.99% |
| Critical fraud detection       |     < 60 sec |
| High-risk fraud detection      |      < 2 min |
| Transaction risk evaluation    | < 300 ms p95 |
| Fraud query                    | < 500 ms p95 |
| Critical alert delivery        |     < 60 sec |
| Critical event loss            |    Near-zero |
| Telemetry blind-spot detection |      < 5 min |

---

## 151. Ultimate SalesGenie Fraud Detection Model

SalesGenie MUST operate fraud detection as a continuous intelligence system:

```text
OBSERVE
   |
   v
COLLECT
   |
   v
NORMALIZE
   |
   v
ENRICH
   |
   v
CORRELATE
   |
   v
DETECT
   |
   v
SCORE
   |
   v
CLASSIFY
   |
   v
DECIDE
   |
   v
PREVENT
   |
   v
INVESTIGATE
   |
   v
CONTAIN
   |
   v
REMEDIATE
   |
   v
VERIFY
   |
   v
PRESERVE
   |
   v
LEARN
   |
   v
IMPROVE
```

---

## 152. Final FAANG-Level Acceptance Criteria

## AC-001 — Payment Fraud

The system MUST detect suspicious payment velocity, payment-method abuse, card testing, and anomalous transactions.

## AC-002 — Subscription Fraud

The system MUST detect subscription cycling, plan manipulation, and suspicious subscription activity.

## AC-003 — Promotional Fraud

The system MUST detect coupon, trial, free-tier, referral, and promotional abuse.

## AC-004 — Credit Fraud

The system MUST detect abnormal credit grants, consumption, manipulation, and exploitation.

## AC-005 — Usage Fraud

The system MUST detect artificial usage, meter manipulation, and billing-related usage anomalies.

## AC-006 — Refund Fraud

The system MUST detect abnormal refund behavior and support controlled refund review.

## AC-007 — Account Fraud

The system MUST detect account takeover, multi-account abuse, and suspicious identity behavior.

## AC-008 — AI Fraud

The system MUST monitor AI agents performing financially relevant actions.

## AC-009 — Workflow Fraud

The system MUST detect automated workflows that generate suspicious financial activity.

## AC-010 — Fraud Rings

The system SHOULD correlate accounts, devices, IPs, payment methods, coupons, referrals, and transactions to identify coordinated fraud.

## AC-011 — Risk Scoring

The system MUST provide explainable risk scores and confidence levels.

## AC-012 — Human + AI

The system MUST support deterministic controls, ML detection, AI investigation, and human decision-making.

## AC-013 — Automated Prevention

The system MUST support policy-controlled automated fraud prevention.

## AC-014 — Human Oversight

High-impact financial restrictions MUST support appropriate human approval.

## AC-015 — Evidence

Fraud decisions MUST be traceable to immutable or tamper-evident evidence.

## AC-016 — Privacy

Fraud detection MUST enforce tenant isolation, least privilege, data minimization, and payment-data protection.

## AC-017 — Reliability

The platform MUST prevent silent loss of critical fraud events.

## AC-018 — Resilience

Core fraud controls MUST remain functional when ML or AI services are unavailable.

## AC-019 — Scalability

The fraud platform MUST scale with SalesGenie's enterprise architecture and projected high-volume workloads.

## AC-020 — Continuous Learning

Fraud outcomes SHOULD continuously improve detection rules, features, models, and investigation workflows.

---

## 153. Core Requirement

The SalesGenie fraud-detection platform MUST provide a **multi-layer, real-time, explainable, tenant-safe, AI-aware fraud intelligence and prevention system** that understands relationships between:

```text
USERS
+
ORGANIZATIONS
+
ACCOUNTS
+
DEVICES
+
IP ADDRESSES
+
PAYMENT METHODS
+
TRANSACTIONS
+
SUBSCRIPTIONS
+
PLANS
+
COUPONS
+
PROMOTIONS
+
TRIALS
+
FREE TIERS
+
CREDITS
+
USAGE
+
METERS
+
INVOICES
+
REFUNDS
+
API KEYS
+
AI AGENTS
+
WORKFLOWS
+
INTEGRATIONS
```

and continuously determines:

```text
WHO is acting?
        |
        v
WHAT are they doing?
        |
        v
WHAT financial resource is affected?
        |
        v
IS the behavior normal?
        |
        v
IS there a relationship to known abuse?
        |
        v
WHAT is the probability of fraud?
        |
        v
WHAT is the potential financial impact?
        |
        v
WHAT evidence supports the decision?
        |
        v
WHAT control should be applied?
        |
        v
DOES a human need to approve it?
        |
        v
WHAT happened after the decision?
        |
        v
WHAT can the system learn?
```

The final fraud lifecycle MUST therefore be:

```text
SIGNAL
  ↓
TELEMETRY
  ↓
FEATURES
  ↓
RULES
  ↓
BEHAVIOR
  ↓
ML
  ↓
AI ANALYSIS
  ↓
GRAPH CORRELATION
  ↓
RISK SCORE
  ↓
FRAUD DECISION
  ↓
AUTOMATED CONTROL / HUMAN REVIEW
  ↓
CONTAINMENT
  ↓
INVESTIGATION
  ↓
RESOLUTION
  ↓
AUDIT
  ↓
FEEDBACK
  ↓
MODEL + RULE IMPROVEMENT
```

> **Core principle:** SalesGenie MUST detect fraud before it becomes material financial loss whenever feasible, while minimizing false positives and ensuring that every significant fraud decision is explainable, evidence-backed, authorized, auditable, privacy-preserving, tenant-safe, and resilient to adversarial human, automated, and AI-driven behavior.
