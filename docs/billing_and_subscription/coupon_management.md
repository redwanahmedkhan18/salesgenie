# SalesGenie — Coupon Management Requirements

**Document:** `coupon_management.md`  
**Product:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Requirement Level:** FAANG / Enterprise Grade  
**Scope:** Coupon creation, distribution, validation, eligibility, application, redemption, expiration, usage limits, campaign management, AI-assisted coupon operations, human administration, fraud prevention, promotion stacking, pricing integration, subscription integration, usage-based billing integration, analytics, auditing, and lifecycle management.

---

## 1. Purpose

The Coupon Management subsystem shall provide a secure, scalable, multi-tenant, deterministic promotion engine for SalesGenie.

The subsystem shall allow authorized humans and AI agents to:

- Create coupons
- Configure promotional rules
- Publish coupons
- Distribute coupons
- Validate coupons
- Apply coupons
- Redeem coupons
- Revoke coupons
- Expire coupons
- Pause campaigns
- Configure usage limits
- Configure customer eligibility
- Configure organization eligibility
- Configure product eligibility
- Configure plan eligibility
- Configure geographic eligibility
- Configure minimum purchase requirements
- Configure maximum discount amounts
- Configure percentage and fixed discounts
- Configure subscription discounts
- Configure usage-based discounts
- Configure one-time promotions
- Configure recurring promotions
- Track coupon performance
- Detect coupon abuse
- Analyze coupon effectiveness

The system shall maintain financial correctness independently of AI recommendations.

---

## 2. Actors

## 2.1 Human Actors

### H-01 — End User

May:

- Enter a coupon code
- Apply an eligible coupon
- View discount details
- View coupon expiration
- View coupon restrictions
- Remove an applied coupon
- View redemption history where permitted

---

### H-02 — Organization Owner

May:

- Create organization-specific promotions where authorized
- Distribute coupons
- View coupon usage
- View campaign analytics
- Configure organization-level campaigns

---

### H-03 — Billing Administrator

May:

- Create coupons
- Configure discounts
- Validate coupon behavior
- Approve promotional campaigns
- Pause coupons
- Revoke coupons
- View coupon transactions

---

### H-04 — Marketing Administrator

May:

- Create campaigns
- Create coupon codes
- Configure targeting
- Distribute coupons
- Analyze campaign performance
- Generate promotional codes

---

### H-05 — Finance Administrator

May:

- Review financial impact
- Approve high-value promotions
- Configure discount limits
- Review coupon-related revenue impact
- Investigate financial anomalies

---

### H-06 — Support Agent

May:

- Validate coupons
- Apply authorized customer-service coupons
- Generate approved goodwill coupons
- View coupon eligibility
- Explain coupon rejection reasons

Support agents shall not bypass configured authorization or discount limits.

---

### H-07 — Sales Agent

May:

- Apply authorized promotional coupons
- Create approved customer-specific coupons
- View campaign eligibility
- Request promotional overrides

---

### H-08 — Super Admin

May:

- Configure global coupon policies
- Configure platform-level limits
- Disable coupon campaigns
- Suspend suspicious campaigns
- Review cross-tenant coupon metrics
- Configure emergency promotional controls

---

### H-09 — Compliance Auditor

May:

- View coupon configuration
- View coupon redemption history
- View approval history
- View audit records
- Review campaign policy versions

Auditors shall be read-only.

---

## 3. AI Actors

## 3.1 AI Coupon Assistant

The AI Coupon Assistant shall:

- Explain available coupons
- Explain eligibility
- Explain coupon restrictions
- Help users discover applicable promotions
- Explain why a coupon cannot be applied
- Assist support agents

---

## 3.2 AI Promotion Analyst

The AI Promotion Analyst shall:

- Analyze campaign performance
- Identify underperforming coupons
- Detect unusual redemption behavior
- Identify potentially abusive coupon usage
- Recommend campaign adjustments

---

## 3.3 AI Coupon Recommendation Agent

The AI may recommend:

- Applicable coupons
- Personalized promotions
- Campaign targeting
- Discount levels
- Coupon expiration strategies

AI recommendations shall not override deterministic pricing or authorization rules.

---

## 3.4 AI Fraud/Risk Agent

The AI Risk Agent shall identify:

- Excessive coupon usage
- Coupon sharing abuse
- Automated redemption
- Multiple accounts exploiting promotions
- Unusual redemption velocity
- Repeated failed coupon attempts
- Suspicious promotional activity

---

## 3.5 AI Campaign Optimization Agent

The AI Campaign Agent may analyze:

- Conversion rate
- Redemption rate
- Customer acquisition
- Customer retention
- Revenue impact
- Discount cost
- Customer lifetime value

The agent may recommend changes but shall require configured human approval for material financial changes.

---

## 4. Coupon Types

The system shall support:

```text
PERCENTAGE_DISCOUNT
FIXED_AMOUNT_DISCOUNT
FREE_TRIAL
FREE_CREDIT
USAGE_CREDIT
SUBSCRIPTION_DISCOUNT
RECURRING_DISCOUNT
ONE_TIME_DISCOUNT
WELCOME_COUPON
REFERRAL_COUPON
LOYALTY_COUPON
GOODWILL_COUPON
PROMOTIONAL_CAMPAIGN
CUSTOMER_SPECIFIC
ORGANIZATION_SPECIFIC
PARTNER_COUPON
AFFILIATE_COUPON
```

---

## 5. User Requirements

## UR-001 — Coupon Discovery

Users shall be able to discover coupons available to them.

---

## UR-002 — Coupon Entry

Users shall be able to enter coupon codes during checkout.

---

## UR-003 — Coupon Validation

Users shall receive immediate validation feedback.

---

## UR-004 — Coupon Eligibility

Users shall be informed whether the coupon applies to their purchase.

---

## UR-005 — Discount Preview

Users shall see:

* Original price
* Coupon discount
* Tax impact where applicable
* Final price

before completing the purchase.

---

## UR-006 — Coupon Removal

Users shall be able to remove an applied coupon before payment where permitted.

---

## UR-007 — Expiration Visibility

Users shall be able to see coupon expiration information where appropriate.

---

## UR-008 — Usage Limits

Users shall be informed when a coupon has reached its usage limit.

---

## UR-009 — Coupon Restrictions

Users shall be able to view applicable restrictions.

---

## UR-010 — Coupon History

Authorized users shall be able to view coupon redemption history.

---

## 6. AI-Based User Requirements

## AI-UR-001 — Coupon Discovery

AI shall identify coupons potentially applicable to a user's current purchase.

---

## AI-UR-002 — Coupon Explanation

AI shall explain:

* Discount amount
* Eligibility
* Restrictions
* Expiration
* Minimum purchase requirements

---

## AI-UR-003 — Best Coupon Recommendation

When multiple coupons are valid, AI may recommend the best eligible coupon according to configured business rules.

The final discount shall always be calculated by the deterministic pricing engine.

---

## AI-UR-004 — Coupon Conflict Resolution

AI may explain conflicts between coupons.

---

## AI-UR-005 — Personalized Promotions

AI may recommend personalized promotions based on authorized customer data.

---

## AI-UR-006 — Coupon Abuse Detection

AI shall identify suspicious coupon usage patterns.

---

## AI-UR-007 — Campaign Optimization

AI may recommend:

* Coupon values
* Target segments
* Campaign duration
* Distribution channels
* Usage limits

---

## AI-UR-008 — Human Escalation

AI shall escalate when:

* Discount exceeds configured threshold
* Customer is requesting an override
* Coupon rules are ambiguous
* Fraud risk is high
* Promotion would materially affect revenue
* Financial authorization is required

---

## 7. System Requirements

## SR-001 — Multi-Tenant Isolation

Coupon data shall be isolated by tenant.

---

## SR-002 — Deterministic Validation

Coupon validation shall be deterministic and reproducible.

---

## SR-003 — Deterministic Pricing

Coupon discounts shall be calculated by the pricing engine rather than by AI.

---

## SR-004 — Coupon Uniqueness

Coupon codes shall be unique within their applicable namespace.

---

## SR-005 — Coupon Lifecycle

Coupons shall use explicit lifecycle states.

---

## SR-006 — Coupon Versioning

Coupon configuration changes shall be versioned.

---

## SR-007 — Effective Dates

Coupons shall support:

```text
starts_at
expires_at
timezone
```

---

## SR-008 — Usage Limits

Coupons shall support:

* Global usage limit
* Per-user limit
* Per-organization limit
* Per-campaign limit
* Per-payment-method limit
* Time-window usage limit

---

## SR-009 — Discount Limits

The system shall support:

* Minimum discount
* Maximum discount
* Maximum discount amount
* Maximum percentage

---

## SR-010 — Minimum Purchase

Coupons shall support minimum purchase requirements.

---

## SR-011 — Maximum Purchase

Coupons may support maximum eligible purchase amounts.

---

## SR-012 — Product Restrictions

Coupons shall support product-level eligibility.

---

## SR-013 — Plan Restrictions

Coupons shall support plan-level eligibility.

---

## SR-014 — Subscription Restrictions

Coupons shall support:

* Monthly plans
* Yearly plans
* Trial conversion
* New subscriptions
* Renewals
* Upgrades
* Downgrades

---

## SR-015 — Usage-Based Billing

Coupons shall support usage-based discounts where configured.

---

## SR-016 — Metered Billing

Coupons shall support discounts against metered usage where permitted.

---

## SR-017 — Currency Support

Coupons shall support multiple currencies.

---

## SR-018 — Precision

Monetary calculations shall use fixed-precision arithmetic.

Floating-point arithmetic shall not be used for authoritative financial calculations.

---

## 8. Coupon Lifecycle

```text
DRAFT
  ↓
PENDING_APPROVAL
  ↓
APPROVED
  ↓
SCHEDULED
  ↓
ACTIVE
  ↓
PAUSED
  ↓
ACTIVE
  ↓
EXPIRED
  ↓
ARCHIVED
```

Alternative terminal state:

```text
ACTIVE
  ↓
REVOKED
```

---

## 9. Coupon State Requirements

## FR-001

Draft coupons shall not be redeemable.

## FR-002

Pending-approval coupons shall not be redeemable.

## FR-003

Approved coupons may be scheduled.

## FR-004

Scheduled coupons shall become active at their configured start time.

## FR-005

Expired coupons shall not be redeemable.

## FR-006

Revoked coupons shall not be redeemable.

## FR-007

Paused coupons shall not be redeemable unless policy explicitly permits continued redemption.

---

## 10. Coupon Creation

## FR-010 — Create Coupon

Authorized users shall be able to create coupons.

Coupon configuration shall include:

```text
coupon_id
tenant_id
campaign_id
code
coupon_type
discount_value
currency
minimum_purchase
maximum_discount
usage_limit
per_user_limit
per_organization_limit
starts_at
expires_at
timezone
eligibility_rules
stacking_rules
targeting_rules
status
policy_version
created_by
created_at
```

---

## 11. Coupon Code Generation

The system shall support:

```text
MANUAL_CODE
RANDOM_CODE
PREFIXED_CODE
BATCH_GENERATED_CODES
UNIQUE_CUSTOMER_CODES
UNIQUE_ORGANIZATION_CODES
```

---

## 12. Coupon Code Security

Generated codes shall:

* Use sufficient entropy
* Avoid predictable sequences
* Avoid sensitive information
* Be normalized consistently
* Support case-insensitive matching where configured

Example:

```text
WELCOME-2026-X8Q4P
```

shall not expose internal IDs.

---

## 13. Coupon Validation

The validation engine shall verify:

```text
Coupon Exists
       +
Coupon Active
       +
Start Date Valid
       +
Expiration Valid
       +
Customer Eligible
       +
Organization Eligible
       +
Product Eligible
       +
Plan Eligible
       +
Minimum Purchase
       +
Usage Limit
       +
Per-User Limit
       +
Per-Organization Limit
       +
Currency Valid
       +
Stacking Rules
       +
Risk Rules
```

---

## 14. Coupon Validation Response

The system shall return:

```text
valid
coupon_id
discount_type
discount_value
estimated_discount
currency
maximum_discount
eligibility_status
rejection_reason
expires_at
remaining_usage
```

---

## 15. Coupon Rejection Reasons

The system shall support standardized reason codes:

```text
COUPON_NOT_FOUND
COUPON_INACTIVE
COUPON_NOT_STARTED
COUPON_EXPIRED
COUPON_REVOKED
COUPON_PAUSED
USAGE_LIMIT_REACHED
USER_LIMIT_REACHED
ORGANIZATION_LIMIT_REACHED
MINIMUM_PURCHASE_NOT_MET
MAXIMUM_PURCHASE_EXCEEDED
PRODUCT_NOT_ELIGIBLE
PLAN_NOT_ELIGIBLE
CUSTOMER_NOT_ELIGIBLE
REGION_NOT_ELIGIBLE
CURRENCY_NOT_SUPPORTED
COUPON_STACKING_NOT_ALLOWED
CONFLICTING_COUPON
ACCOUNT_NOT_ELIGIBLE
PAYMENT_METHOD_NOT_ELIGIBLE
RISK_RESTRICTION
CAMPAIGN_LIMIT_REACHED
```

---

## 16. Discount Calculation

The pricing engine shall calculate the authoritative discount.

## Percentage

```text
Discount =
Eligible Amount × Percentage
```

---

## Fixed Amount

```text
Discount =
Configured Fixed Amount
```

The system shall cap the discount according to configured limits.

---

## 17. Maximum Discount

Example:

```text
Purchase = $500
Coupon = 30%
Maximum Discount = $100

Calculated Discount = $150
Applied Discount = $100
```

---

## 18. Minimum Purchase

Example:

```text
Minimum Purchase = $100
Cart = $75

Coupon = INVALID
Reason = MINIMUM_PURCHASE_NOT_MET
```

---

## 19. Coupon Application

Applying a coupon shall create a pricing calculation reference.

The system shall not permanently consume a coupon merely because it was entered.

---

## 20. Coupon Reservation

For limited-use coupons, the system may reserve a redemption during checkout.

```text
AVAILABLE
    ↓
RESERVED
    ↓
REDEEMED
```

If checkout expires:

```text
RESERVED
    ↓
RELEASED
```

---

## 21. Coupon Redemption

A coupon shall be considered redeemed only after the authoritative purchase event occurs.

Examples:

```text
Payment Successful
Subscription Activated
Invoice Finalized
```

The system shall not count abandoned checkouts as completed redemptions.

---

## 22. Redemption Idempotency

Coupon redemption shall be idempotent.

Repeated payment events shall not consume additional coupon usage.

---

## 23. Coupon Usage Accounting

The system shall track:

```text
total_usage
successful_usage
failed_usage
reserved_usage
cancelled_usage
remaining_usage
```

---

## 24. Per-User Usage

Example:

```text
Global Limit = 10,000
Per User Limit = 1

User A → Redeemed → Cannot Redeem Again
User B → Eligible
```

---

## 25. Per-Organization Usage

The system shall support organization-level redemption limits.

---

## 26. Campaign Management

A campaign shall support:

```text
campaign_id
tenant_id
name
description
objective
budget
start_date
end_date
target_segment
coupon_ids
distribution_channels
status
approval_status
created_by
```

---

## 27. Campaign Lifecycle

```text
DRAFT
 ↓
PENDING_APPROVAL
 ↓
APPROVED
 ↓
SCHEDULED
 ↓
ACTIVE
 ↓
PAUSED
 ↓
COMPLETED
 ↓
ARCHIVED
```

---

## 28. Campaign Approval

Campaigns exceeding configured financial thresholds shall require human approval.

---

## 29. AI Campaign Generation

AI may generate campaign proposals containing:

```text
campaign_name
target_audience
coupon_type
discount_value
duration
usage_limit
estimated_cost
expected_conversion
risk_score
```

The proposal shall remain non-redeemable until approved.

---

## 30. Coupon Stacking

The system shall support:

```text
STACKABLE
NON_STACKABLE
STACK_WITH_SPECIFIC_COUPONS
STACK_WITH_CREDITS
STACK_WITH_LOYALTY
```

---

## 31. Coupon Priority

When multiple eligible coupons exist, the pricing engine shall apply configured priority.

Example:

```text
Customer-Specific
      ↓
Organization-Specific
      ↓
Campaign Coupon
      ↓
General Promotional Coupon
```

---

## 32. Best Discount

If policy permits optimization, the system may evaluate:

```text
Coupon A → $20 discount
Coupon B → $35 discount
Coupon C → $25 discount
```

and recommend Coupon B.

The final result shall still be validated by the pricing engine.

---

## 33. Coupon Stacking Protection

The system shall prevent unintended discount multiplication.

Example:

```text
Original Price = $100

Coupon A = 20%
Coupon B = 30%

If stacking disabled:
Only one coupon applies.

If stacking enabled:
Configured stacking algorithm applies.
```

---

## 34. Subscription Coupons

The system shall support:

```text
FIRST_MONTH_FREE
FIRST_YEAR_DISCOUNT
N_MONTHS_DISCOUNTED
PERCENTAGE_RECURRING
FIXED_RECURRING
ONE_TIME_SUBSCRIPTION_DISCOUNT
TRIAL_EXTENSION
```

---

## 35. Subscription Renewal

Coupons shall explicitly define whether they apply to:

```text
Initial Purchase
Renewal
Upgrade
Downgrade
Proration
```

Default behavior shall be deny unless explicitly configured.

---

## 36. Usage-Based Coupons

Coupons may apply to:

```text
AI Tokens
API Calls
Messages
Conversations
Voice Minutes
Workflow Executions
Document Processing
Lead Generation
Storage
MCP Tool Calls
```

---

## 37. Usage Discount Models

Supported models may include:

```text
PERCENTAGE_USAGE_DISCOUNT
FIXED_USAGE_CREDIT
FREE_USAGE_UNITS
TIER_DISCOUNT
USAGE_CAP
```

---

## 38. Free Credits

Coupon-based credits shall have:

```text
credit_amount
currency
expiration
eligible_services
usage_limit
```

Credits shall be tracked independently from cash payments.

---

## 39. Coupon Distribution

The system shall support:

```text
EMAIL
IN_APP
WEBSITE
CHECKOUT
API
AFFILIATE
REFERRAL
SALES_AGENT
SUPPORT_AGENT
SOCIAL_CAMPAIGN
PARTNER
```

---

## 40. Customer-Specific Coupons

Customer-specific coupons shall be bound to an authorized customer identity.

The system shall prevent unauthorized sharing where restrictions apply.

---

## 41. Organization-Specific Coupons

Organization-specific coupons shall be scoped to the organization.

Cross-tenant redemption shall be prohibited.

---

## 42. Geographic Restrictions

Coupons may support:

```text
COUNTRY
REGION
CITY
TAX_JURISDICTION
MARKET
```

Location eligibility shall use authoritative account or transaction information.

---

## 43. Payment Method Restrictions

Coupons may support:

```text
CARD
BANK_TRANSFER
WALLET
PAYPAL
OTHER_PROVIDER
```

Actual supported payment methods depend on payment integrations.

---

## 44. New Customer Restrictions

Coupons may support:

```text
NEW_CUSTOMERS_ONLY
EXISTING_CUSTOMERS_ONLY
ALL_CUSTOMERS
```

---

## 45. Account Age Restrictions

Coupons may support:

```text
MIN_ACCOUNT_AGE
MAX_ACCOUNT_AGE
```

---

## 46. Referral Coupons

Referral campaigns shall support:

```text
referrer_id
referee_id
campaign_id
coupon_id
referral_status
reward_status
```

The system shall prevent self-referral abuse.

---

## 47. Affiliate Coupons

Affiliate coupons shall support:

```text
affiliate_id
campaign_id
coupon_id
redemption_count
commission_reference
```

---

## 48. Goodwill Coupons

Support agents may issue goodwill coupons within configured limits.

Example:

```text
Agent Limit = $50
Requested Coupon = $75

→ Requires Manager Approval
```

---

## 49. Human Override

Authorized humans may override coupon decisions only when policy permits.

Every override shall record:

```text
actor_id
override_reason
previous_decision
new_decision
coupon_id
transaction_id
timestamp
approval_reference
```

---

## 50. AI Decision Boundaries

AI shall never:

* Create unauthorized discounts
* Increase coupon values beyond limits
* Override coupon restrictions
* Extend expiration dates without authorization
* Modify financial records directly
* Bypass usage limits
* Bypass customer eligibility
* Bypass tenant boundaries
* Approve restricted campaigns
* Fabricate coupon availability

---

## 51. AI Coupon Recommendation

AI recommendations shall contain:

```text
coupon_id
recommendation_reason
estimated_discount
eligibility_status
confidence
policy_reference
```

The system shall validate the recommendation before application.

---

## 52. AI Confidence

AI shall provide a confidence score for recommendations.

Low-confidence recommendations shall be routed to deterministic validation or human review.

---

## 53. AI Hallucination Protection

The AI shall not invent:

* Coupon codes
* Discount values
* Expiration dates
* Usage limits
* Eligibility rules
* Campaign names

All customer-facing coupon information shall come from authoritative coupon data.

---

## 54. Coupon Fraud Prevention

The system shall detect:

```text
Coupon Brute Force
Code Enumeration
Repeated Invalid Attempts
Account Cycling
Multiple Account Abuse
Referral Abuse
Affiliate Abuse
Coupon Sharing
Automated Redemption
High Velocity Redemption
Unusual Geographic Activity
```

---

## 55. Coupon Brute-Force Protection

Coupon validation APIs shall implement:

* Rate limiting
* Progressive throttling
* Abuse detection
* Temporary blocking
* IP/device risk signals where legally permitted

---

## 56. Coupon Code Enumeration Protection

The API shall avoid revealing whether a code exists when doing so could facilitate brute-force discovery.

Customer-facing error messages may use generic messaging while internal systems retain precise reason codes.

---

## 57. Redemption Velocity

The system shall monitor:

```text
Redemptions / minute
Redemptions / hour
Redemptions / customer
Redemptions / organization
```

---

## 58. Campaign Budget

Campaigns may define:

```text
maximum_discount_budget
maximum_redemption_count
maximum_customer_count
```

The system shall prevent campaign spending beyond configured limits.

---

## 59. Campaign Budget Reservation

When required, discount budget shall be reserved atomically during transaction processing.

---

## 60. Coupon Expiration

Coupons shall expire automatically at `expires_at`.

The system shall use the configured timezone and store timestamps in UTC.

---

## 61. Expiration Race Conditions

The system shall define deterministic behavior for purchases occurring near expiration.

Example:

```text
Coupon Validation → 23:59:59
Payment Confirmation → 00:00:02
```

The authoritative transaction timestamp and policy shall determine validity.

---

## 62. Coupon Revocation

Authorized administrators may revoke coupons.

Revocation shall:

* Prevent future redemption
* Preserve historical redemption records
* Preserve financial records
* Generate audit events

---

## 63. Coupon Pause

Administrators may temporarily pause campaigns.

Pausing shall not delete existing redemption history.

---

## 64. Coupon Archiving

Archived coupons shall remain queryable for authorized reporting and audit.

---

## 65. Refund Integration

When a discounted transaction is refunded, the system shall preserve:

```text
original_price
coupon_discount
net_price
refunded_amount
coupon_id
redemption_id
```

Refund logic shall integrate with Refund Management.

---

## 66. Coupon Reversal

If a transaction is reversed or refunded, coupon usage treatment shall follow configured policy.

Possible behavior:

```text
CONSUME_PERMANENTLY
RESTORE_USAGE
RESTORE_ONLY_IF_FULL_REFUND
RESTORE_WITHIN_CAMPAIGN_WINDOW
```

---

## 67. Invoice Integration

Invoices shall preserve coupon information.

Invoice data may include:

```text
coupon_code
coupon_id
discount_amount
discount_percentage
campaign_id
```

---

## 68. Tax Integration

The coupon discount shall be applied according to tax rules before taxable amount calculation where required.

The system shall not assume that discount treatment is identical across jurisdictions.

---

## 69. Pricing Integration

Coupon Management shall integrate with:

```text
Pricing Engine
Billing Service
Subscription Service
Usage Meter
Invoice Service
Tax Service
Payment Service
Refund Service
```

---

## 70. Checkout Flow

```text
User
 ↓
Checkout
 ↓
Enter Coupon
 ↓
Coupon Validation
 ↓
Eligibility Engine
 ↓
Pricing Engine
 ↓
Tax Calculation
 ↓
Final Price
 ↓
Payment
 ↓
Invoice
 ↓
Coupon Redemption
```

---

## 71. Coupon Redemption Atomicity

The system shall ensure that successful redemption and financial transaction state remain consistent.

Where distributed transactions are impossible, the system shall use:

* Idempotent events
* Transactional outbox
* Compensation
* Reconciliation

---

## 72. Event-Driven Architecture

The system shall publish events:

```text
coupon.created
coupon.updated
coupon.approved
coupon.scheduled
coupon.activated
coupon.paused
coupon.revoked
coupon.expired
coupon.validated
coupon.validation_failed
coupon.reserved
coupon.reservation_released
coupon.redeemed
coupon.redemption_failed
coupon.limit_reached
coupon.campaign_started
coupon.campaign_paused
coupon.campaign_completed
coupon.anomaly_detected
```

---

## 73. Event Requirements

Coupon events shall support:

* Event IDs
* Idempotency
* Correlation IDs
* Causation IDs
* Schema versioning
* Retry
* Dead-letter queues
* Replay

---

## 74. Coupon API Requirements

## POST `/api/v1/coupons`

Create a coupon.

---

## GET `/api/v1/coupons/{coupon_id}`

Retrieve coupon details.

---

## GET `/api/v1/coupons`

List authorized coupons.

---

## PATCH `/api/v1/coupons/{coupon_id}`

Update eligible coupon configuration.

---

## POST `/api/v1/coupons/{coupon_id}/approve`

Approve a coupon.

---

## POST `/api/v1/coupons/{coupon_id}/activate`

Activate a coupon.

---

## POST `/api/v1/coupons/{coupon_id}/pause`

Pause a coupon.

---

## POST `/api/v1/coupons/{coupon_id}/revoke`

Revoke a coupon.

---

## POST `/api/v1/coupons/validate`

Validate a coupon code.

---

## POST `/api/v1/coupons/apply`

Apply a coupon to a pricing calculation.

---

## POST `/api/v1/coupons/redeem`

Redeem a coupon against an authoritative transaction.

---

## GET `/api/v1/coupons/{coupon_id}/redemptions`

Retrieve redemption history.

---

## GET `/api/v1/coupons/{coupon_id}/analytics`

Retrieve coupon analytics.

---

## 75. Campaign APIs

## POST `/api/v1/campaigns`

Create campaign.

## GET `/api/v1/campaigns/{campaign_id}`

Retrieve campaign.

## PATCH `/api/v1/campaigns/{campaign_id}`

Update campaign.

## POST `/api/v1/campaigns/{campaign_id}/approve`

Approve campaign.

## POST `/api/v1/campaigns/{campaign_id}/pause`

Pause campaign.

## POST `/api/v1/campaigns/{campaign_id}/resume`

Resume campaign.

## POST `/api/v1/campaigns/{campaign_id}/complete`

Complete campaign.

---

## 76. Batch Coupon Generation

The platform shall support generating large coupon batches.

Batch generation shall support:

```text
quantity
prefix
length
character_set
expiration
campaign_id
usage_limit
customer_assignment
organization_assignment
```

---

## 77. Batch Processing Requirements

Batch generation shall:

* Be asynchronous for large jobs
* Support progress tracking
* Support retries
* Avoid duplicate codes
* Provide job IDs
* Produce audit records

---

## 78. Coupon Import

Authorized users may import coupons using structured files or APIs.

Import validation shall check:

* Duplicate codes
* Invalid dates
* Invalid discounts
* Invalid campaigns
* Invalid tenants
* Invalid currencies
* Invalid usage limits

---

## 79. Coupon Export

Authorized users shall be able to export:

* Coupon configuration
* Campaign data
* Redemption data
* Analytics
* Audit information

Sensitive coupon codes shall be protected according to role.

---

## 80. Coupon Search

Authorized users shall be able to search by:

```text
coupon_id
coupon_code
campaign_id
customer_id
organization_id
status
coupon_type
created_by
date_range
```

---

## 81. Coupon Dashboard

The dashboard shall display:

```text
Active Coupons
Scheduled Coupons
Expired Coupons
Paused Coupons
Total Redemptions
Total Discount
Average Discount
Redemption Rate
Campaign Revenue
Conversion Rate
Coupon Abuse Alerts
```

---

## 82. Campaign Analytics

The system shall calculate:

```text
Issued
Delivered
Viewed
Validated
Applied
Redeemed
Revenue
Discount Cost
Conversion Rate
Redemption Rate
Average Order Value
Incremental Revenue
```

---

## 83. Financial Analytics

Finance users shall see:

```text
Gross Revenue
Discount Amount
Net Revenue
Refund Amount
Coupon Cost
Effective Discount Rate
Revenue Impact
```

---

## 84. AI Analytics

The platform shall measure:

```text
AI Coupon Recommendation Rate
AI Recommendation Acceptance Rate
AI Recommendation Conversion
AI Recommendation Error Rate
AI Escalation Rate
AI Override Rate
AI Fraud Detection Rate
```

---

## 85. AI Campaign Optimization

AI may analyze historical data and recommend:

```text
Discount Level
Campaign Duration
Target Segment
Coupon Distribution
Usage Limit
Promotion Timing
```

Recommendations shall be simulated before production deployment when feasible.

---

## 86. Promotion Simulation

The system shall support a dry-run mode.

Example:

```text
Campaign:
20% discount
Maximum discount: $50
Expected users: 10,000

Simulation:
Expected redemptions: 2,100
Estimated discount cost: $X
Estimated revenue impact: $Y
```

AI recommendations shall not modify production campaigns during simulation.

---

## 87. A/B Testing

Campaigns may support:

```text
CONTROL
VARIANT_A
VARIANT_B
```

Metrics may include:

* Conversion
* Revenue
* Redemption
* Average order value
* Retention

Assignment shall be deterministic and auditable.

---

## 88. Experiment Guardrails

Experiments shall support:

* Maximum discount budget
* Maximum customer exposure
* Minimum sample size
* Automatic stop conditions
* Revenue-loss thresholds

---

## 89. Coupon Approval Matrix

Example:

| Discount | Approval                     |
| -------- | ---------------------------- |
| ≤ 10%    | Marketing Admin              |
| 10–25%   | Billing Admin                |
| 25–50%   | Finance Admin                |
| > 50%    | Finance + Secondary Approval |

Actual thresholds shall be configurable.

---

## 90. Separation of Duties

The system shall support:

```text
Campaign Creator
        ↓
Campaign Approver
        ↓
Campaign Publisher
```

A single user shall not bypass separation-of-duty controls where required.

---

## 91. Coupon Permissions

Recommended permissions:

```text
coupon:read
coupon:create
coupon:update
coupon:validate
coupon:apply
coupon:redeem
coupon:approve
coupon:pause
coupon:resume
coupon:revoke
coupon:archive
coupon:export
coupon:analytics
coupon:override
coupon:admin
campaign:create
campaign:update
campaign:approve
campaign:publish
campaign:pause
campaign:analytics
```

---

## 92. Role Mapping

| Role            |    Read |  Create | Validate | Apply |     Redeem | Approve | Revoke | Analytics |
| --------------- | ------: | ------: | -------: | ----: | ---------: | ------: | -----: | --------: |
| End User        | Limited |      No |      Yes |   Yes |     System |      No |     No |        No |
| Sales Agent     |     Yes | Limited |      Yes |   Yes |     System | Limited |     No |   Limited |
| Support Agent   |     Yes | Limited |      Yes |   Yes |     System | Limited |     No |   Limited |
| Marketing Admin |     Yes |     Yes |      Yes |    No |     System |     Yes |    Yes |       Yes |
| Billing Admin   |     Yes |     Yes |      Yes |   Yes |     System |     Yes |    Yes |       Yes |
| Finance Admin   |     Yes |     Yes |      Yes |   Yes |     System |     Yes |    Yes |       Yes |
| Super Admin     |     Yes |     Yes |      Yes |   Yes | Controlled |     Yes |    Yes |       Yes |
| Auditor         |     Yes |      No |       No |    No |         No |      No |     No |       Yes |

---

## 93. Security Requirements

## SEC-001

All coupon APIs shall require authentication where applicable.

## SEC-002

All administrative coupon operations shall require authorization.

## SEC-003

Tenant boundaries shall be enforced server-side.

## SEC-004

Coupon codes shall not contain sensitive information.

## SEC-005

Coupon enumeration shall be rate-limited.

## SEC-006

Coupon administration shall be audited.

## SEC-007

High-value promotions shall require elevated privileges.

## SEC-008

Coupon configuration shall be protected against unauthorized modification.

## SEC-009

API requests shall be protected against replay where applicable.

## SEC-010

Coupon redemption shall be idempotent.

---

## 94. AI Security Requirements

## AI-SEC-001

AI shall not create production coupons without authorization.

## AI-SEC-002

AI shall not modify coupon financial values outside permitted bounds.

## AI-SEC-003

AI shall not bypass eligibility rules.

## AI-SEC-004

AI shall not expose private customer coupon data.

## AI-SEC-005

AI shall not expose internal fraud signals.

## AI-SEC-006

AI shall not invent coupon codes.

## AI-SEC-007

AI shall not invent discount amounts.

## AI-SEC-008

AI shall not directly modify financial ledgers.

## AI-SEC-009

AI tools shall enforce tenant isolation.

---

## 95. MCP Integration

Controlled MCP tools may include:

```text
mcp.coupon.search
mcp.coupon.validate
mcp.coupon.get_details
mcp.coupon.get_eligible
mcp.coupon.apply
mcp.coupon.get_redemption_history
mcp.campaign.get_status
mcp.campaign.get_analytics
```

Administrative tools shall require elevated permissions.

---

## 96. MCP AI Guardrails

AI agents using MCP coupon tools shall:

1. Authenticate.
2. Resolve tenant.
3. Validate permissions.
4. Validate customer context.
5. Validate coupon state.
6. Validate eligibility.
7. Calculate discount through the pricing engine.
8. Validate limits.
9. Apply configured stacking rules.
10. Record an audit event.

---

## 97. Workflow Integration

Coupon events shall be available to SalesGenie's workflow engine.

Examples:

```text
coupon.redeemed
      ↓
Update CRM
      ↓
Notify Sales Team
      ↓
Update Customer Segment
```

---

## 98. n8n Integration

Supported workflow actions may include:

```text
validate_coupon
create_coupon
activate_coupon
pause_coupon
revoke_coupon
get_coupon
get_campaign
get_coupon_analytics
notify_coupon_redemption
```

Workflow authorization shall be enforced.

---

## 99. Webhook Integration

The system may send outbound webhooks:

```text
coupon.created
coupon.activated
coupon.expired
coupon.redeemed
coupon.revoked
coupon.limit_reached
campaign.started
campaign.completed
```

Webhooks shall support:

* Signature verification
* Retry
* Idempotency
* Event IDs
* Delivery tracking

---

## 100. Observability

The coupon subsystem shall expose metrics:

```text
coupon_validation_total
coupon_validation_success_total
coupon_validation_failure_total
coupon_redemption_total
coupon_redemption_failure_total
coupon_discount_total
coupon_campaign_total
coupon_abuse_detection_total
coupon_api_latency
coupon_validation_latency
coupon_redemption_latency
```

---

## 101. Monitoring

The system shall monitor:

* Coupon validation latency
* Redemption latency
* Error rates
* Usage-limit conflicts
* Duplicate redemption attempts
* Fraud signals
* Campaign budget consumption
* Discount exposure
* API rate limits

---

## 102. Alerts

Alerts shall be generated for:

```text
Unusual Redemption Spike
Campaign Budget Near Limit
Campaign Budget Exceeded
High Coupon Failure Rate
Coupon Enumeration Attack
High Fraud Score
Duplicate Redemption
Unexpected Discount Volume
Unauthorized Coupon Modification
```

---

## 103. Distributed Tracing

Coupon operations shall propagate:

```text
request_id
correlation_id
trace_id
causation_id
```

across:

```text
API Gateway
Pricing Service
Coupon Service
Billing Service
Subscription Service
Tax Service
Invoice Service
Payment Service
Refund Service
Workflow Service
AI Gateway
Notification Service
```

---

## 104. Reliability Requirements

The system shall tolerate:

* Service crashes
* Database failures
* Queue failures
* Payment-provider failures
* Pricing-service failures
* AI-service failures
* Duplicate events
* Out-of-order events
* Network failures

---

## 105. AI Service Failure

If AI is unavailable:

```text
AI Unavailable
      ↓
Deterministic Coupon Engine
      ↓
Eligibility Validation
      ↓
Pricing Engine
      ↓
Normal Checkout
```

Coupon redemption shall remain financially correct without AI.

---

## 106. Database Requirements

Coupon persistence shall support:

* ACID transactions
* Unique constraints
* Foreign keys
* Transaction-safe counters
* Decimal monetary fields
* Versioning
* Optimistic concurrency
* Immutable redemption records

---

## 107. Concurrency Control

The system shall prevent multiple concurrent redemptions from exceeding coupon limits.

Example:

```text
Usage Limit = 1

Request A → Redeem
Request B → Redeem simultaneously
```

Only one request shall succeed.

---

## 108. Atomic Redemption

Where required:

```text
Validate
   ↓
Reserve Usage
   ↓
Commit Transaction
   ↓
Redeem
```

The system shall prevent oversubscription.

---

## 109. Distributed Transaction Strategy

Where coupon redemption spans multiple services, the platform shall use:

```text
Transactional Outbox
+
Idempotent Consumers
+
Eventual Consistency
+
Compensating Transactions
+
Reconciliation
```

rather than relying on distributed two-phase commit unless explicitly required.

---

## 110. Coupon Snapshot

At redemption time, the system shall preserve the effective coupon configuration:

```text
coupon_id
coupon_version
discount_type
discount_value
maximum_discount
eligibility_rules
stacking_rules
campaign_id
policy_version
```

Future coupon edits shall not alter historical financial calculations.

---

## 111. Audit Requirements

Every material coupon operation shall generate an audit event.

Audit fields:

```text
audit_id
tenant_id
coupon_id
campaign_id
actor_id
actor_type
action
previous_state
new_state
previous_configuration
new_configuration
reason
policy_version
request_id
correlation_id
timestamp
```

---

## 112. Redemption Audit

Every redemption shall record:

```text
redemption_id
coupon_id
customer_id
organization_id
transaction_id
invoice_id
discount_amount
currency
timestamp
status
```

---

## 113. Data Retention

Coupon records shall be retained according to:

* Financial retention requirements
* Campaign reporting requirements
* Compliance requirements
* Tenant retention policies

Completed financial records shall not be destructively altered merely because a campaign is archived.

---

## 114. Privacy

The platform shall:

* Minimize customer data exposure
* Enforce tenant isolation
* Mask sensitive information
* Apply role-based access
* Encrypt sensitive data
* Avoid exposing private coupon assignments
* Avoid exposing internal fraud scores

---

## 115. Coupon Search Security

Search results shall be scoped by:

```text
tenant
organization
role
permissions
customer ownership
```

---

## 116. Coupon API Rate Limits

Recommended rate limits shall apply separately to:

```text
Validation
Redemption
Code Generation
Campaign APIs
Administrative APIs
Analytics APIs
```

Sensitive endpoints shall use stricter limits.

---

## 117. Coupon Abuse Response

When abuse is detected, the system may:

```text
ALLOW
THROTTLE
CHALLENGE
REQUIRE_HUMAN_REVIEW
BLOCK
```

Actions shall be policy-driven.

---

## 118. Emergency Controls

Super Admin shall be able to:

* Disable coupon redemption globally
* Disable a specific campaign
* Disable a tenant's campaign
* Disable coupon generation
* Require human approval
* Pause suspicious campaigns

Emergency actions shall be audited.

---

## 119. Global Coupon Kill Switch

The platform shall support:

```text
COUPON_REDEMPTION_ENABLED = false
```

When disabled:

* Existing historical redemptions remain intact.
* New redemptions are blocked.
* Customer-facing errors remain safe.
* Administrative investigation remains available.

---

## 120. Refund Interaction

If a discounted transaction is refunded:

```text
Original Price
-
Coupon Discount
=
Net Charged Amount
```

Refund Management shall determine the refundable amount.

Coupon Management shall preserve redemption history.

---

## 121. Refund/Coupon Restoration Policy

The system shall support configurable behavior:

```text
NEVER_RESTORE
RESTORE_ON_FULL_REFUND
RESTORE_ON_ANY_REFUND
RESTORE_IF_CAMPAIGN_ACTIVE
RESTORE_IF_WITHIN_EXPIRATION
```

---

## 122. Coupon Expiration Scheduler

The scheduler shall:

* Activate scheduled coupons
* Expire expired coupons
* Release expired reservations
* Close completed campaigns
* Generate expiration events
* Update analytics

Scheduler operations shall be idempotent.

---

## 123. Scheduled Campaign Safety

A campaign scheduled for activation shall be revalidated before activation.

The system shall verify:

* Policy validity
* Financial limits
* Tenant status
* Campaign budget
* Coupon configuration
* Approval state

---

## 124. AI Campaign Scheduler

AI may recommend scheduling based on:

* Historical redemption
* Customer engagement
* Seasonality
* Campaign performance

Production schedule changes shall require authorization where configured.

---

## 125. Coupon Templates

The system shall support reusable templates:

```text
WELCOME_10
WELCOME_20
ANNUAL_30
BLACK_FRIDAY
REFERRAL
GOODWILL
TRIAL_EXTENSION
LOYALTY
PARTNER
```

Templates shall not automatically become active coupons.

---

## 126. Template Governance

Templates shall support:

```text
template_id
version
owner
status
approval_status
default_discount
default_expiration
default_limits
created_at
updated_at
```

---

## 127. AI Template Generation

AI may generate coupon templates based on approved business requirements.

AI-generated templates shall require validation before publication.

---

## 128. Localization

Coupon messaging shall support:

* Multiple languages
* Currency localization
* Date localization
* Timezone-aware expiration
* Locale-specific formatting

Financial calculations shall remain locale-independent.

---

## 129. Customer Communication

Customer-facing messages shall support:

```text
Coupon Applied
Coupon Invalid
Coupon Expired
Coupon Limit Reached
Coupon Not Eligible
Coupon Removed
Coupon Campaign Ended
```

---

## 130. AI Customer Communication

AI may explain coupon failures using authoritative reason codes.

Example:

```text
Customer:
"Why didn't my coupon work?"

AI:
"The coupon requires a minimum purchase of $100,
and your current eligible purchase is $75."
```

AI shall not invent restrictions.

---

## 131. Coupon Recommendation API

The platform may expose:

```text
POST /api/v1/coupons/recommend
```

The endpoint shall return only coupons that pass authoritative eligibility validation.

---

## 132. Coupon Eligibility API

```text
POST /api/v1/coupons/eligibility
```

The response shall contain:

```text
eligible_coupons
ineligible_coupons
reason_codes
recommended_coupon
```

---

## 133. Coupon Analytics API

```text
GET /api/v1/coupons/analytics
GET /api/v1/campaigns/{campaign_id}/analytics
```

Analytics shall enforce authorization and tenant isolation.

---

## 134. Testing Requirements

## Unit Tests

Test:

* Coupon validation
* Eligibility
* Expiration
* Usage limits
* Per-user limits
* Per-organization limits
* Minimum purchase
* Maximum discount
* Percentage discounts
* Fixed discounts
* Stacking
* Currency handling
* Subscription discounts
* Usage discounts

---

## 135. Integration Tests

Test:

* Pricing Engine
* Billing Service
* Subscription Service
* Usage Meter
* Invoice Service
* Tax Service
* Payment Service
* Refund Service
* Workflow Engine
* n8n
* MCP
* Notification Service

---

## 136. Security Tests

Test:

* Tenant isolation
* RBAC
* IDOR
* Coupon enumeration
* Brute force
* Replay attacks
* Privilege escalation
* Unauthorized campaign modification
* Unauthorized discount escalation
* API abuse

---

## 137. AI Tests

Test:

* Coupon recommendation accuracy
* Eligibility grounding
* Hallucination resistance
* Prompt injection resistance
* Fraud detection
* Campaign optimization
* Human escalation
* Authorization compliance

---

## 138. Concurrency Tests

Test:

```text
Simultaneous Redemptions
Usage Limit = 1
```

Expected:

```text
Exactly one successful redemption.
```

---

## 139. Load Tests

The system shall be tested for:

* High-volume coupon validation
* High-volume redemption
* Campaign launches
* Flash sales
* Batch generation
* Concurrent checkout
* API bursts

---

## 140. Chaos Tests

Test:

* Coupon service outage
* Pricing service outage
* Billing service outage
* Database outage
* Queue outage
* AI outage
* Duplicate events
* Delayed events
* Out-of-order events

---

## 141. Acceptance Criteria

## AC-001

Authorized users can create coupons.

## AC-002

Unauthorized users cannot create production coupons.

## AC-003

Users can validate coupon codes.

## AC-004

Invalid coupons cannot be applied.

## AC-005

Expired coupons cannot be redeemed.

## AC-006

Revoked coupons cannot be redeemed.

## AC-007

Usage limits cannot be exceeded.

## AC-008

Per-user limits cannot be exceeded.

## AC-009

Per-organization limits cannot be exceeded.

## AC-010

Minimum purchase requirements are enforced.

## AC-011

Maximum discount limits are enforced.

## AC-012

Coupon stacking rules are enforced.

## AC-013

Coupon discounts are calculated deterministically.

## AC-014

Coupon redemption is idempotent.

## AC-015

Concurrent redemption cannot exceed configured limits.

## AC-016

Historical redemption records remain immutable.

## AC-017

Coupon versions are preserved.

## AC-018

Campaign budgets cannot be exceeded.

## AC-019

Subscription coupons work according to configured rules.

## AC-020

Usage-based coupons work according to configured rules.

## AC-021

Refunds preserve coupon redemption history.

## AC-022

Tax calculation receives the correct discounted amount.

## AC-023

Invoices preserve coupon information.

## AC-024

AI cannot bypass coupon policies.

## AC-025

AI cannot invent coupon information.

## AC-026

AI recommendations are validated before application.

## AC-027

High-risk coupon activity triggers review.

## AC-028

Coupon administrative actions are audited.

## AC-029

Cross-tenant coupon access is prevented.

## AC-030

Coupon APIs are rate-limited.

## AC-031

Coupon webhooks are authenticated.

## AC-032

Coupon analytics are accurate and tenant-isolated.

## AC-033

Emergency coupon controls function correctly.

## AC-034

AI outage does not corrupt coupon processing.

## AC-035

External-service failures do not cause duplicate redemptions.

---

## 142. Definition of Done

Coupon Management shall be considered production-ready only when:

* Coupon creation is implemented.
* Coupon lifecycle management is implemented.
* Coupon validation is deterministic.
* Coupon eligibility is deterministic.
* Percentage discounts are supported.
* Fixed discounts are supported.
* Subscription coupons are supported.
* Usage-based coupons are supported.
* Customer-specific coupons are supported.
* Organization-specific coupons are supported.
* Campaign management is implemented.
* Coupon stacking rules are implemented.
* Usage limits are enforced atomically.
* Per-user limits are enforced.
* Per-organization limits are enforced.
* Coupon reservations are supported where required.
* Coupon redemption is idempotent.
* Coupon versions are preserved.
* Financial calculations use fixed precision.
* Pricing integration is complete.
* Billing integration is complete.
* Subscription integration is complete.
* Invoice integration is complete.
* Tax integration is complete.
* Refund integration is complete.
* AI recommendations are grounded.
* AI cannot bypass financial controls.
* Fraud detection is implemented.
* Rate limiting is implemented.
* Audit logging is complete.
* RBAC is implemented.
* Tenant isolation is verified.
* Campaign budgets are enforced.
* Webhooks are secured.
* Event processing is idempotent.
* Monitoring is operational.
* Alerts are configured.
* Reconciliation is implemented where required.
* Security testing is passed.
* AI safety testing is passed.
* Load testing is passed.
* Concurrency testing is passed.
* Chaos testing is passed.
* Disaster recovery is tested.

---

## 143. FAANG-Level Design Principles

1. **Coupon validation must be deterministic.**
2. **AI must never be the source of truth for financial calculations.**
3. **Every coupon redemption must be idempotent.**
4. **Usage limits must be enforced atomically.**
5. **Concurrent redemptions must not exceed configured limits.**
6. **Historical coupon configuration must be immutable through versioned snapshots.**
7. **Expired coupons must never be redeemable.**
8. **Revoked coupons must never be redeemable.**
9. **Coupon stacking must be explicitly configured.**
10. **Discount calculations must use fixed-precision arithmetic.**
11. **Campaign budgets must be enforced server-side.**
12. **Customer eligibility must be enforced server-side.**
13. **Tenant isolation must be mandatory.**
14. **Coupon codes must not expose sensitive information.**
15. **Coupon enumeration must be actively mitigated.**
16. **High-value promotions must require appropriate approval.**
17. **AI recommendations must pass deterministic validation.**
18. **AI must not invent coupon codes or discounts.**
19. **AI must not bypass authorization.**
20. **AI-generated campaigns must remain non-production until approved.**
21. **Coupon redemption must be tied to an authoritative financial transaction.**
22. **Abandoned checkout must not automatically consume permanent coupon usage.**
23. **Refunds must preserve coupon redemption history.**
24. **Coupon restoration after refund must follow explicit policy.**
25. **Subscription and usage-based promotions must have explicit applicability rules.**
26. **Tax treatment must be delegated to the tax engine.**
27. **Pricing must remain centralized in the pricing engine.**
28. **Financial records must be auditable.**
29. **Distributed workflows must use idempotency and compensation.**
30. **External webhook processing must be replay-safe.**
31. **Campaign changes must be versioned and auditable.**
32. **Fraud detection must combine deterministic controls with AI signals.**
33. **AI service failure must not compromise financial integrity.**
34. **Coupon services must degrade safely during dependency failures.**
35. **Emergency kill switches must exist for platform-wide promotional incidents.**
36. **Every material coupon state transition must be observable.**
37. **Every financial coupon effect must be traceable to a transaction.**
38. **Every AI recommendation must be attributable to a model/version and policy context.**
39. **Every human override must have an accountable actor and reason.**
40. **The system must optimize for financial correctness, security, reliability, scalability, and auditability before automation.**
