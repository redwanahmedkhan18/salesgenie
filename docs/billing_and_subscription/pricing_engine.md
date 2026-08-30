# SalesGenie — Pricing Engine Requirements

**Document:** `pricing_engine.md`  
**Product:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Requirement Level:** FAANG-Level / Enterprise Production  
**Scope:** Pricing Engine  
**Actors:** Super Admin, Organization Owner, Billing Admin, Finance Team, Admin, Sales Manager, Sales Agent, Support Agent, AI Pricing Agent, AI Sales Agent, AI Billing Agent, AI Workflow Agent, Subscription Service, Billing Service, Payment Provider, Tax Service, Usage Metering Service, Entitlement Service

---

## 1. Purpose

The SalesGenie Pricing Engine shall provide a centralized, deterministic, versioned, auditable, multi-tenant pricing infrastructure for calculating the financial price of:

- Subscription plans
- Monthly plans
- Annual plans
- Seat-based plans
- Usage-based plans
- AI model usage
- AI tokens
- Conversations
- API calls
- Workflow executions
- Automation executions
- Storage
- Knowledge-base capacity
- Voice minutes
- Messaging volume
- Omnichannel usage
- Premium integrations
- Add-ons
- Enterprise contracts
- Custom pricing
- Discounts
- Coupons
- Credits
- Promotions
- Taxes
- Proration
- Overage
- Minimum commitments
- Volume pricing
- Tiered pricing
- Graduated pricing
- Package pricing
- Hybrid pricing

The Pricing Engine shall be the authoritative source for pricing calculations and shall ensure that pricing decisions are:

- Deterministic
- Versioned
- Explainable
- Auditable
- Reproducible
- Secure
- Tenant-aware
- Currency-aware
- Tax-aware
- Idempotent
- Highly available
- Horizontally scalable

The engine shall support both **human-driven** and **AI-assisted** pricing workflows while preventing AI systems from bypassing pricing policies, authorization, financial controls, or approval requirements.

---

## 2. Product Goals

The Pricing Engine shall:

1. Provide a single authoritative pricing calculation layer.
2. Separate pricing configuration from pricing execution.
3. Support immutable pricing versions.
4. Support multiple pricing models.
5. Support subscription-specific pricing.
6. Support usage-based pricing.
7. Support hybrid pricing.
8. Support enterprise custom pricing.
9. Support discounts and promotions.
10. Support credits.
11. Support proration.
12. Support overage calculations.
13. Support taxes through a dedicated tax calculation boundary.
14. Support multiple currencies.
15. Support regional pricing.
16. Support effective-dated pricing.
17. Provide pricing previews.
18. Provide complete pricing explanations.
19. Provide deterministic quote generation.
20. Prevent unauthorized pricing overrides.
21. Support AI pricing recommendations.
22. Support AI-generated quotes subject to policy.
23. Support human approval workflows.
24. Provide complete pricing audit trails.
25. Support reconciliation against billing.
26. Scale to millions of customers and high-volume usage events.
27. Maintain financial correctness under concurrency and retries.

---

## 3. Non-Goals

The Pricing Engine shall not:

- Store raw payment-card information.
- Act as the primary payment processor.
- Replace the Billing Service.
- Replace the Subscription Service.
- Replace the Tax Service.
- Trust frontend-provided prices.
- Allow arbitrary client-side pricing.
- Allow AI agents to create unrestricted discounts.
- Allow historical prices to be silently changed.
- Modify immutable financial records.
- Grant entitlements based solely on an unverified client quote.
- Treat AI recommendations as authoritative pricing.
- Execute high-risk financial overrides without authorization.

---

## 4. Core Pricing Principles

The Pricing Engine shall follow:

```text
Price = f(
    Product,
    Plan,
    Plan Version,
    Pricing Model,
    Quantity,
    Usage,
    Currency,
    Region,
    Billing Interval,
    Customer Segment,
    Discounts,
    Credits,
    Contract Terms,
    Effective Date,
    Tax Context
)
```

Pricing shall never be determined solely by:

```text
Frontend Input
```

The authoritative calculation shall occur server-side.

---

## 5. Actors

## H-01 — Super Admin

May:

* Create pricing plans.
* Create pricing versions.
* Configure pricing rules.
* Activate pricing versions.
* Retire pricing versions.
* Configure global pricing policies.
* Configure discount policies.
* Configure pricing approval thresholds.
* View pricing analytics.
* Review pricing overrides.
* Review pricing audit logs.

---

## H-02 — Organization Owner

May:

* View applicable pricing.
* Request quotes.
* Preview subscription pricing.
* Preview upgrades.
* Preview downgrades.
* View usage pricing.
* Apply eligible coupons.
* Review discounts.
* Accept quotes.

---

## H-03 — Billing Admin

May:

* View pricing.
* Generate pricing previews.
* Generate quotes.
* Apply authorized discounts.
* Request pricing overrides.
* Review billing calculations.

---

## H-04 — Finance Team

May:

* Review pricing calculations.
* Review discounts.
* Review credits.
* Review tax calculations.
* Reconcile pricing against billing.
* Approve high-value pricing exceptions.

---

## H-05 — Sales Manager

May:

* Generate customer quotes.
* Request discounts.
* Request enterprise pricing.
* View pricing recommendations.
* Approve discounts within delegated authority.

---

## H-06 — Sales Agent

May:

* View applicable pricing.
* Generate standard quotes.
* Recommend plans.
* Request approved discounts.

---

## H-07 — Support Agent

May:

* Explain customer pricing.
* View pricing breakdowns.
* View applicable subscription pricing.
* Escalate pricing disputes.

---

## 6. AI Actors

## AI-01 — AI Pricing Agent

The AI Pricing Agent may:

* Explain prices.
* Compare plans.
* Recommend pricing plans.
* Recommend quantities.
* Recommend billing intervals.
* Forecast pricing.
* Detect pricing anomalies.
* Generate draft quotes.
* Recommend discounts within policy.
* Recommend enterprise pricing.
* Identify pricing inconsistencies.

---

## AI-02 — AI Sales Agent

The AI Sales Agent may:

* Recommend plans.
* Generate draft quotes.
* Identify expansion opportunities.
* Recommend seat quantities.
* Recommend add-ons.
* Estimate customer spend.

---

## AI-03 — AI Billing Agent

The AI Billing Agent may:

* Explain invoices.
* Explain pricing calculations.
* Detect pricing discrepancies.
* Identify unexpected charges.
* Recommend billing corrections for human review.

---

## AI-04 — AI Workflow Agent

The AI Workflow Agent may:

* Trigger pricing calculations.
* Generate pricing previews.
* Monitor pricing events.
* Route pricing approval requests.
* Trigger notifications.
* Execute approved low-risk pricing workflows.

---

## 7. Pricing Models

The Pricing Engine shall support:

```text
FLAT_RATE
PER_SEAT
PER_USER
PER_AGENT
PER_CONVERSATION
PER_MESSAGE
PER_API_CALL
PER_TOKEN
PER_MINUTE
PER_GB
PER_WORKFLOW_EXECUTION
PER_TASK
TIERED
GRADUATED
VOLUME
PACKAGE
HYBRID
CUSTOM_CONTRACT
```

---

## 8. Pricing Model Definitions

## 8.1 Flat Rate

```text
Price = Fixed Base Price
```

---

## 8.2 Per Seat

```text
Price = Seat Quantity × Unit Price
```

---

## 8.3 Usage Based

```text
Price = Billable Usage × Unit Price
```

---

## 8.4 Tiered Pricing

Example:

```text
0–1,000      → $0.010/unit
1,001–10,000 → $0.008/unit
10,001+      → $0.005/unit
```

---

## 8.5 Volume Pricing

The unit price is determined by the total quantity tier.

---

## 8.6 Graduated Pricing

Each tier is priced independently.

Example:

```text
First 1,000      × $0.010
Next 9,000       × $0.008
Remaining usage  × $0.005
```

---

## 8.7 Hybrid Pricing

Example:

```text
Base Subscription
+
Seats
+
AI Usage
+
Workflow Executions
+
Premium Add-ons
```

---

## 9. User Requirements

## UR-001 — View Price

Users shall be able to view:

* Plan price.
* Billing interval.
* Included usage.
* Seat limits.
* Usage rates.
* Add-on prices.
* Overage rates.
* Discounts.
* Applicable taxes where available.
* Estimated total.

---

## UR-002 — Compare Plans

Users shall be able to compare:

* Base price.
* Included seats.
* Included AI usage.
* Included conversations.
* Included workflows.
* Storage.
* Integrations.
* Features.
* Overage rates.
* Estimated total cost.

---

## UR-003 — Preview Price

Users shall be able to preview pricing before:

* Starting a subscription.
* Upgrading.
* Downgrading.
* Adding seats.
* Removing seats.
* Adding add-ons.
* Changing billing intervals.

---

## UR-004 — View Pricing Breakdown

The system shall expose:

```text
Base Price
+
Seat Charges
+
Usage Charges
+
Add-ons
-
Discounts
-
Credits
+
Taxes
=
Estimated Total
```

---

## UR-005 — Generate Quote

Authorized users shall be able to generate quotes.

A quote shall include:

* Customer.
* Organization.
* Products.
* Plans.
* Quantities.
* Pricing version.
* Discounts.
* Credits.
* Taxes.
* Currency.
* Effective date.
* Expiration date.
* Terms.
* Total.

---

## UR-006 — Apply Coupon

Users shall be able to apply eligible coupons.

The system shall validate:

* Eligibility.
* Expiration.
* Usage limits.
* Customer eligibility.
* Product scope.
* Plan scope.
* Region.
* Currency.
* Minimum purchase.

---

## UR-007 — View Discount

Users shall see:

* Discount type.
* Discount amount.
* Discount duration.
* Eligibility.
* Effective period.

---

## UR-008 — Request Pricing Override

Authorized users may request:

* Custom discount.
* Custom unit price.
* Contract pricing.
* Minimum commitment adjustment.
* Custom billing terms.

High-risk changes shall require approval.

---

## 10. AI User Requirements

## AI-UR-001 — Explain Pricing

AI shall explain:

* Why a price was calculated.
* Which plan was used.
* Which pricing version was used.
* Which quantities were included.
* Which discounts were applied.
* Which credits were applied.
* Which taxes were included.
* Which usage was billable.

---

## AI-UR-002 — Recommend Plan

AI shall recommend plans using:

* Historical usage.
* Current usage.
* Forecast usage.
* Number of users.
* Number of agents.
* Feature requirements.
* Budget.
* Growth projections.

---

## AI-UR-003 — Recommend Billing Interval

AI may recommend monthly versus annual pricing based on:

* Expected usage.
* Customer commitment.
* Discount impact.
* Forecast spend.

---

## AI-UR-004 — Recommend Quantity

AI may recommend:

* Number of seats.
* AI capacity.
* Workflow capacity.
* Storage capacity.
* Messaging capacity.

Recommendations shall be explicitly labeled as recommendations.

---

## AI-UR-005 — Pricing Anomaly Detection

AI shall identify:

* Unexpected price increases.
* Unexpected price decreases.
* Abnormal discounts.
* Duplicate charges.
* Incorrect quantities.
* Incorrect pricing versions.
* Suspicious overrides.
* Pricing-rule inconsistencies.

---

## 11. System Requirements

## SR-001 — Central Pricing Service

SalesGenie shall provide a dedicated Pricing Service responsible for authoritative price calculations.

---

## SR-002 — Pricing Engine

The Pricing Engine shall calculate prices using versioned rules.

```text
Pricing Request
      ↓
Context Resolution
      ↓
Product Resolution
      ↓
Plan Resolution
      ↓
Pricing Version Resolution
      ↓
Quantity / Usage Resolution
      ↓
Pricing Rule Evaluation
      ↓
Discount Evaluation
      ↓
Credit Evaluation
      ↓
Tax Boundary
      ↓
Total Calculation
      ↓
Pricing Explanation
      ↓
Price Result
```

---

## SR-003 — Server-Side Calculation

All authoritative prices shall be calculated server-side.

Frontend prices shall be informational only.

---

## SR-004 — Pricing Versioning

Every calculation shall reference:

```text
pricing_version_id
```

Pricing versions shall be immutable after activation unless explicitly versioned through a new release.

---

## SR-005 — Effective Dating

Pricing rules shall support:

```text
effective_from
effective_until
```

The engine shall select pricing based on the calculation timestamp and applicable contract terms.

---

## 12. Pricing Configuration

Pricing configuration shall support:

```text
Product
Plan
Plan Version
Pricing Model
Unit Price
Currency
Billing Interval
Included Quantity
Overage Rate
Tier Rules
Discount Rules
Eligibility Rules
Region Rules
Customer Segment
Effective Date
```

---

## 13. Currency Requirements

The engine shall support:

* USD.
* EUR.
* GBP.
* BDT.
* Other configured currencies.

Each price shall specify:

```text
currency
currency_precision
rounding_mode
```

The engine shall not perform implicit currency conversion without an explicitly configured exchange-rate source.

---

## 14. Money Representation

The system shall never use floating-point arithmetic for authoritative monetary calculations.

Use:

```text
Integer minor units
```

or:

```text
Decimal
```

with explicitly defined precision.

Example:

```text
$10.25
→
1025 cents
```

---

## 15. Rounding Requirements

The Pricing Engine shall define deterministic rounding rules.

Supported policies may include:

```text
ROUND_HALF_UP
ROUND_HALF_EVEN
ROUND_DOWN
ROUND_UP
```

Rounding rules shall be versioned.

---

## 16. Pricing Formula Requirements

Every pricing calculation shall be reproducible.

Example:

```text
Base Price
+ Seat Cost
+ Usage Cost
+ Add-On Cost
+ Overage
- Discounts
- Credits
+ Taxes
= Final Amount
```

---

## 17. Pricing Components

The engine shall support:

```text
BASE_PLAN
SEAT
USER
AGENT
AI_MODEL
TOKEN
CONVERSATION
MESSAGE
VOICE_MINUTE
API_CALL
WORKFLOW_EXECUTION
STORAGE
ADD_ON
OVERAGE
DISCOUNT
CREDIT
TAX
```

---

## 18. Included Usage

Plans may include quotas.

Example:

```json
{
  "included": {
    "ai_tokens": 1000000,
    "conversations": 5000,
    "workflow_executions": 10000,
    "storage_gb": 100
  }
}
```

Only usage exceeding configured included quantities shall become billable usage when the pricing model specifies overage billing.

---

## 19. Overage Pricing

The system shall calculate:

```text
Billable Overage
=
Actual Usage
-
Included Usage
```

If:

```text
Actual Usage <= Included Usage
```

then:

```text
Overage = 0
```

---

## 20. Usage Pricing

Usage events shall contain:

```text
usage_event_id
tenant_id
organization_id
subscription_id
meter_id
quantity
unit
timestamp
source
```

The Pricing Engine shall consume authoritative metered usage rather than trusting user-entered quantities for billing.

---

## 21. Pricing Meter Requirements

Meters may include:

```text
AI_TOKEN
AI_REQUEST
CONVERSATION
MESSAGE
VOICE_MINUTE
API_CALL
WORKFLOW_EXECUTION
STORAGE_GB
DOCUMENT_PROCESSING
RAG_QUERY
```

---

## 22. Discount Engine

The Pricing Engine shall support:

```text
PERCENTAGE
FIXED_AMOUNT
UNIT_DISCOUNT
TIER_DISCOUNT
TIME_LIMITED
RECURRING
ONE_TIME
PROMOTIONAL
CONTRACTUAL
CUSTOMER_SPECIFIC
```

---

## 23. Discount Constraints

Every discount shall define:

```text
discount_id
discount_type
value
currency
maximum_discount
minimum_purchase
eligible_products
eligible_plans
eligible_customers
eligible_regions
start_at
end_at
usage_limit
per_customer_limit
stacking_policy
approval_policy
```

---

## 24. Discount Stacking

The engine shall explicitly define whether discounts may be combined.

Supported policies:

```text
NO_STACKING
STACK_ALLOWED
BEST_DISCOUNT
PRIORITY_ORDER
EXCLUSIVE
```

---

## 25. Coupon Requirements

Coupons shall support:

* Unique codes.
* Expiration.
* Usage limits.
* Customer limits.
* Product restrictions.
* Plan restrictions.
* Region restrictions.
* Minimum spend.
* Maximum discount.
* Start date.
* End date.

---

## 26. Credits

The engine shall support:

* Account credits.
* Promotional credits.
* Service credits.
* Contract credits.
* Refund credits.

Credits shall have:

```text
credit_id
customer_id
amount
currency
remaining_amount
expiration
source
reason
```

---

## 27. Credit Application

The engine shall define:

* Which charges credits apply to.
* Credit priority.
* Expiration behavior.
* Whether credits can cover taxes.
* Whether credits can cover usage.
* Whether credits can be combined.

---

## 28. Tax Integration

The Pricing Engine shall provide a tax calculation boundary.

```text
Pricing Engine
      ↓
Tax Context
      ↓
Tax Service
      ↓
Tax Result
      ↓
Final Price
```

The Pricing Engine shall not hard-code jurisdiction-specific tax logic unless explicitly required by architecture.

---

## 29. Tax Context

Tax requests shall include:

```text
customer_location
billing_location
service_location
product_category
tax_exemption_status
currency
amount
```

---

## 30. Regional Pricing

Pricing may vary by:

* Country.
* Region.
* Currency.
* Customer segment.
* Regulatory requirements.
* Contract.

The applicable regional pricing rule shall be deterministic.

---

## 31. Customer Segmentation

The engine may support:

```text
STARTUP
SMB
MID_MARKET
ENTERPRISE
EDUCATION
NONPROFIT
CUSTOM
```

Segment-specific pricing shall be governed by explicit rules.

---

## 32. Enterprise Pricing

Enterprise customers may have:

* Custom unit prices.
* Custom plans.
* Minimum commitments.
* Custom discounts.
* Contract-specific rates.
* Custom usage rates.
* Custom seat prices.
* Custom billing intervals.

Contract pricing shall be versioned and auditable.

---

## 33. Quote Engine

The Pricing Engine shall provide a quote capability.

```text
Quote Request
 ↓
Customer Resolution
 ↓
Product Resolution
 ↓
Pricing Resolution
 ↓
Discount Resolution
 ↓
Tax Calculation
 ↓
Total
 ↓
Quote Snapshot
 ↓
Quote ID
```

---

## 34. Quote Immutability

Once issued, a quote shall preserve:

```text
pricing_version
line_items
quantities
unit_prices
discounts
credits
taxes
currency
total
terms
```

Subsequent pricing changes shall not silently alter an issued quote.

---

## 35. Quote Expiration

Quotes shall support:

```text
valid_from
expires_at
```

Expired quotes shall not automatically become executable.

---

## 36. Quote Acceptance

Acceptance shall validate:

* Quote status.
* Expiration.
* Customer.
* Authorization.
* Pricing version.
* Contract requirements.
* Payment requirements.

---

## 37. Pricing Preview

The engine shall support:

```http
POST /api/v1/pricing/preview
```

A preview shall not mutate:

* Subscription.
* Billing.
* Payment.
* Entitlements.
* Financial ledger.

---

## 38. Price Calculation API

The engine shall support:

```http
POST /api/v1/pricing/calculate
```

The response shall include:

```json
{
  "pricing_calculation_id": "calc_123",
  "pricing_version_id": "price_v42",
  "currency": "USD",
  "subtotal": 10000,
  "discount": 1000,
  "credit": 500,
  "tax": 850,
  "total": 9350,
  "rounding_mode": "ROUND_HALF_UP"
}
```

Amounts shall use minor currency units or explicit decimal values according to the API contract.

---

## 39. Price Breakdown API

The system shall support:

```http
GET /api/v1/pricing/calculations/{calculation_id}
```

---

## 40. Pricing Version API

The platform shall support:

```http
GET  /api/v1/pricing/versions
POST /api/v1/pricing/versions
GET  /api/v1/pricing/versions/{id}
POST /api/v1/pricing/versions/{id}/activate
POST /api/v1/pricing/versions/{id}/retire
```

---

## 41. Pricing Configuration API

Authorized administrators shall be able to manage:

```http
POST   /api/v1/pricing/plans
PATCH  /api/v1/pricing/plans/{id}
POST   /api/v1/pricing/rules
PATCH  /api/v1/pricing/rules/{id}
POST   /api/v1/pricing/discounts
PATCH  /api/v1/pricing/discounts/{id}
```

---

## 42. Pricing Functional Requirements

## FR-001 — Resolve Pricing Context

The engine shall resolve:

```text
tenant
organization
customer
product
plan
subscription
region
currency
billing interval
customer segment
contract
```

---

## FR-002 — Resolve Pricing Version

The engine shall select the correct pricing version based on:

* Product.
* Plan.
* Region.
* Customer.
* Contract.
* Effective date.
* Subscription context.

---

## FR-003 — Calculate Base Price

The engine shall calculate base price according to the selected pricing model.

---

## FR-004 — Calculate Seat Price

The engine shall calculate billable seats.

```text
Billable Seats
=
max(
    configured minimum seats,
    billable seat quantity
)
```

where applicable.

---

## FR-005 — Calculate Usage Charges

The engine shall:

1. Retrieve authoritative usage.
2. Resolve included quota.
3. Calculate billable usage.
4. Apply usage pricing.
5. Apply tier rules.
6. Apply rounding.

---

## 43. Tier Calculation

The engine shall support deterministic tier calculation.

Example:

```text
Usage = 15,000

Tier 1:
1,000 × $0.010

Tier 2:
9,000 × $0.008

Tier 3:
5,000 × $0.005
```

---

## 44. Volume Pricing

For volume pricing:

```text
Unit Price = Price of Applicable Tier
Total = Quantity × Unit Price
```

The engine shall distinguish volume pricing from graduated pricing.

---

## 45. Hybrid Pricing

The engine shall support:

```text
Total =
Base
+ Seats
+ Usage
+ Add-ons
+ Overage
- Discounts
- Credits
+ Taxes
```

---

## 46. Add-On Pricing

Add-ons shall support:

* Flat price.
* Per-seat price.
* Usage price.
* Recurring price.
* One-time price.

---

## 47. Billing Interval Pricing

The engine shall support:

```text
MONTHLY
QUARTERLY
SEMI_ANNUAL
ANNUAL
CUSTOM
```

Pricing rules shall explicitly define supported intervals.

---

## 48. Annual Pricing

Annual pricing shall not simply assume:

```text
Monthly × 12
```

unless explicitly configured.

Annual prices shall be independently versioned.

---

## 49. Proration

The Pricing Engine shall support proration for:

* Upgrades.
* Downgrades.
* Seat changes.
* Add-ons.
* Billing interval changes.

Proration shall use:

```text
remaining_period
billing_period
current_price
new_price
```

according to the configured proration policy.

---

## 50. Proration Policies

Supported policies may include:

```text
SECOND_BASED
DAY_BASED
PERIOD_BASED
NO_PRORATION
CUSTOM_CONTRACT
```

The selected policy shall be explicit.

---

## 51. Pricing Effective Dates

Pricing changes shall support:

```text
IMMEDIATE
NEXT_BILLING_PERIOD
SCHEDULED_DATE
CONTRACT_RENEWAL
```

---

## 52. Grandfathered Pricing

The system shall support grandfathered pricing.

Existing customers may remain on:

```text
legacy_pricing_version
```

until:

* Subscription change.
* Contract expiration.
* Migration.
* Administrative action.

The migration policy shall be explicit.

---

## 53. Pricing Migration

Pricing migration shall support:

```text
CURRENT_VERSION
     ↓
MIGRATION_RULE
     ↓
TARGET_VERSION
     ↓
CUSTOMER_VALIDATION
     ↓
PRICE_PREVIEW
     ↓
APPROVAL
     ↓
ACTIVATION
```

---

## 54. Price Increase Workflow

```text
New Pricing Proposal
 ↓
Pricing Validation
 ↓
Financial Impact Analysis
 ↓
Customer Impact Analysis
 ↓
Approval
 ↓
Version Creation
 ↓
Effective Date
 ↓
Customer Notification
 ↓
Activation
```

---

## 55. AI Pricing Recommendation Workflow

```text
Customer Usage
 ↓
Historical Usage
 ↓
Forecast
 ↓
Plan Evaluation
 ↓
Pricing Calculation
 ↓
Cost Comparison
 ↓
AI Recommendation
 ↓
Explain Recommendation
 ↓
Policy Validation
 ↓
Human/User Confirmation
```

---

## 56. AI Quote Workflow

```text
Customer Request
 ↓
AI Requirement Extraction
 ↓
Product Resolution
 ↓
Plan Recommendation
 ↓
Pricing Calculation
 ↓
Discount Policy
 ↓
Tax Calculation
 ↓
Quote Draft
 ↓
Risk Evaluation
 ↓
Approval
 ↓
Quote Issued
```

---

## 57. AI Discount Workflow

```text
Customer Context
 ↓
AI Discount Recommendation
 ↓
Discount Policy Evaluation
 ↓
Maximum Discount Check
 ↓
Approval Threshold Check
 ↓
Human Approval
 ↓
Discount Applied
```

AI shall not bypass configured discount limits.

---

## 58. AI Pricing Guardrails

AI shall never:

* Invent prices.
* Invent discounts.
* Modify pricing rules.
* Modify active pricing versions.
* Override taxes.
* Override currency rules.
* Override financial limits.
* Create unauthorized credits.
* Change contract prices without authorization.
* Execute unauthorized pricing changes.
* Modify historical calculations.

---

## 59. Human Approval Matrix

| Pricing Operation             |      Human | AI Read | AI Recommend |   AI Execute |
| ----------------------------- | ---------: | ------: | -----------: | -----------: |
| View pricing                  |        Yes |     Yes |          Yes |          N/A |
| Explain price                 |        Yes |     Yes |          Yes |          N/A |
| Plan recommendation           |        Yes |     Yes |          Yes |          Yes |
| Pricing preview               |        Yes |     Yes |          Yes |          Yes |
| Standard quote                |        Yes |     Yes |          Yes | Policy-based |
| Standard discount             |        Yes |     Yes |          Yes | Policy-based |
| Large discount                |        Yes |     Yes |          Yes |     Approval |
| Custom price                  |        Yes |     Yes |          Yes |     Approval |
| Enterprise contract price     |        Yes |     Yes |          Yes |     Approval |
| Pricing rule creation         |        Yes |      No |           No |           No |
| Pricing version activation    |        Yes |      No |           No |           No |
| Tax override                  | Restricted |      No |           No |           No |
| Historical price modification | Restricted |      No |           No |           No |
| Financial credit creation     |        Yes |     Yes |          Yes |     Approval |

---

## 60. Pricing Approval Thresholds

The system shall support configurable approval thresholds such as:

```text
Discount <= 5%
→ Auto-approved

Discount > 5% and <= 15%
→ Sales Manager approval

Discount > 15%
→ Finance approval

Custom Enterprise Pricing
→ Finance + Authorized Admin
```

Actual thresholds shall be configurable.

---

## 61. Pricing Authorization

Pricing permissions shall be RBAC and policy based.

Example:

```text
pricing.view
pricing.calculate
pricing.quote.create
pricing.discount.request
pricing.discount.approve
pricing.override.request
pricing.override.approve
pricing.rule.create
pricing.rule.update
pricing.version.activate
pricing.version.retire
pricing.audit.read
```

---

## 62. Tenant Isolation

Every pricing operation shall include:

```text
tenant_id
organization_id
```

Tenant-specific pricing shall never leak between organizations.

---

## 63. Pricing Overrides

Overrides shall include:

```text
override_id
pricing_calculation_id
requested_by
approved_by
reason
original_value
override_value
approval_status
expires_at
```

Overrides shall be explicitly scoped.

---

## 64. Override Expiration

Temporary pricing overrides shall support:

```text
valid_from
expires_at
```

Expired overrides shall not be applied.

---

## 65. Pricing Audit Log

Every material pricing action shall record:

```text
audit_id
tenant_id
actor_type
actor_id
action
pricing_version_id
calculation_id
quote_id
previous_value
new_value
reason
approval_id
request_id
correlation_id
timestamp
```

---

## 66. Pricing Explanation

Every authoritative calculation should be explainable.

Example:

```text
Base Plan:
$100.00

10 Seats:
$200.00

AI Usage:
$50.00

Add-ons:
$30.00

Subtotal:
$380.00

Discount:
-$38.00

Credit:
-$10.00

Tax:
$33.20

Total:
$365.20
```

---

## 67. Pricing Calculation Snapshot

Every finalized pricing result shall preserve:

```text
pricing_version
pricing_rules
quantities
usage
unit_prices
discounts
credits
tax_context
tax_result
rounding
currency
final_total
```

This ensures future reproducibility.

---

## 68. Deterministic Pricing

Given the same:

```text
Pricing Version
Input Context
Usage
Quantity
Currency
Effective Date
```

the engine shall return the same result.

---

## 69. Idempotency

Pricing calculations shall support idempotency for operations that create durable resources such as:

* Quotes.
* Pricing adjustments.
* Discount applications.
* Pricing migrations.

Repeated requests shall not create duplicate financial artifacts.

---

## 70. Concurrency

The system shall protect pricing configuration from concurrent conflicting updates.

Pricing version activation shall use optimistic concurrency or equivalent protection.

---

## 71. Pricing Version Activation

Only one applicable active pricing version shall be selected for a given pricing scope and effective time unless explicitly configured otherwise.

---

## 72. Pricing Configuration Validation

Before activation, the system shall validate:

* Missing prices.
* Duplicate rules.
* Overlapping tiers.
* Invalid ranges.
* Invalid currencies.
* Negative prices where prohibited.
* Invalid discount stacking.
* Invalid effective dates.
* Circular pricing dependencies.
* Unsupported billing intervals.
* Invalid minimum quantities.

---

## 73. Tier Validation

Tier definitions shall not contain ambiguous ranges.

Invalid:

```text
0–100
100–500
```

unless boundary semantics are explicitly defined.

Valid example:

```text
0–100
101–500
501+
```

or equivalent half-open interval representation.

---

## 74. Negative Price Protection

The engine shall reject negative prices unless explicitly supported as:

* Credits.
* Refunds.
* Promotional adjustments.

---

## 75. Zero Price

Zero-priced products shall be explicitly supported.

The engine shall distinguish:

```text
FREE
```

from:

```text
MISSING PRICE
```

---

## 76. Price Availability

If no valid pricing rule exists, the engine shall return a structured error.

Example:

```json
{
  "error": {
    "code": "PRICE_NOT_AVAILABLE",
    "message": "No active pricing configuration exists for the requested product and region.",
    "retryable": false
  }
}
```

---

## 77. Pricing Error Handling

The engine shall distinguish:

```text
VALIDATION_ERROR
PRICE_NOT_FOUND
INVALID_PLAN
INVALID_CURRENCY
INVALID_QUANTITY
INVALID_USAGE
DISCOUNT_NOT_ELIGIBLE
DISCOUNT_EXPIRED
DISCOUNT_LIMIT_REACHED
QUOTE_EXPIRED
PRICING_VERSION_CONFLICT
TAX_SERVICE_FAILURE
USAGE_SERVICE_FAILURE
INTERNAL_PRICING_ERROR
```

---

## 78. Retry Requirements

Retryable failures shall use:

* Exponential backoff.
* Jitter.
* Retry limits.
* Dead-letter handling.
* Replay capability.

Pricing calculation itself should remain deterministic across retries.

---

## 79. External Dependency Handling

The Pricing Engine may depend on:

```text
Usage Metering
Tax Service
Currency Exchange Service
Customer Service
Subscription Service
Billing Service
Entitlement Service
```

External failures shall not corrupt pricing configuration.

---

## 80. Caching

The system may cache:

* Active pricing versions.
* Product definitions.
* Pricing rules.
* Regional configuration.
* Static discount metadata.

The cache shall be invalidated when pricing configuration changes.

Financially authoritative results shall not rely on stale cached pricing beyond explicitly permitted consistency guarantees.

---

## 81. Cache Invalidation

Pricing updates shall publish:

```text
pricing.version.created
pricing.version.activated
pricing.version.retired
pricing.rule.updated
pricing.discount.updated
```

Consumers shall invalidate relevant caches.

---

## 82. Event Model

The Pricing Engine shall emit:

```text
pricing.calculated
pricing.preview.created
pricing.quote.created
pricing.quote.expired
pricing.quote.accepted

pricing.version.created
pricing.version.activated
pricing.version.retired

pricing.rule.created
pricing.rule.updated

pricing.discount.created
pricing.discount.applied
pricing.discount.rejected

pricing.override.requested
pricing.override.approved
pricing.override.rejected

pricing.anomaly.detected
```

---

## 83. Transactional Outbox

Critical pricing state changes shall use a transactional outbox where appropriate.

```text
Database Transaction
       |
       +── Pricing State
       |
       +── Outbox Event
              |
              ▼
         Event Broker
```

---

## 84. Reconciliation

Pricing results shall be reconcilable against:

```text
Pricing Engine
      ↕
Subscription Service
      ↕
Billing Service
      ↕
Invoice
      ↕
Payment Provider
```

The system shall detect:

* Price mismatch.
* Quantity mismatch.
* Discount mismatch.
* Currency mismatch.
* Tax mismatch.
* Pricing-version mismatch.
* Missing pricing artifact.

---

## 85. Billing Integration

The Pricing Engine shall provide authoritative pricing inputs to the Billing Service.

Billing shall not independently reinterpret pricing rules.

---

## 86. Subscription Integration

The Subscription Service shall provide:

```text
plan
quantity
billing_interval
subscription_state
effective_date
```

The Pricing Engine shall calculate applicable pricing.

---

## 87. Usage Integration

Usage data shall come from the Usage Metering Service.

The engine shall reject untrusted usage sources where authoritative billing usage is required.

---

## 88. Entitlement Integration

Pricing changes shall not directly determine authorization.

The flow shall be:

```text
Pricing
 ↓
Subscription
 ↓
Entitlements
 ↓
Feature Access
```

---

## 89. AI Pricing Analytics

AI may calculate:

```text
Price Elasticity
Customer Price Sensitivity
Expansion Probability
Discount Effectiveness
Plan Fit
Churn Risk
Revenue Opportunity
```

AI outputs shall remain analytically separate from authoritative pricing.

---

## 90. AI Revenue Optimization

AI may recommend:

* Plan structures.
* Pricing experiments.
* Discount strategies.
* Packaging.
* Add-ons.
* Usage thresholds.

Production pricing changes shall require controlled experimentation and human authorization.

---

## 91. Pricing Experiments

The platform may support controlled pricing experiments.

Experiments shall define:

```text
experiment_id
population
variant
pricing_version
start_at
end_at
eligibility
success_metrics
approval
```

Experiments shall not accidentally cross tenant boundaries.

---

## 92. Price Experiment Safety

The platform shall prevent:

* Unauthorized customers entering experiments.
* Overlapping incompatible experiments.
* Experiment leakage into enterprise contracts.
* Retroactive price changes.
* Untracked pricing variants.

---

## 93. Pricing Analytics

The platform shall expose:

```text
Average Selling Price
Average Contract Value
Average Revenue Per User
Average Revenue Per Organization
Discount Rate
Discount Cost
Revenue Expansion
Revenue Contraction
Price Change Impact
Plan Mix
Usage Revenue
Overage Revenue
Add-On Revenue
Quote Conversion Rate
```

---

## 94. Pricing Monitoring

The system shall monitor:

```text
pricing_calculation_rate
pricing_calculation_latency
pricing_error_rate
price_not_found_rate
discount_rejection_rate
quote_generation_rate
quote_conversion_rate
pricing_override_rate
pricing_anomaly_rate
pricing_version_activation_rate
reconciliation_mismatch_rate
```

---

## 95. Performance Requirements

## PERF-001

Pricing calculation API target:

```text
p95 < 200 ms
```

for calculations not requiring slow external dependencies.

---

## PERF-002

Pricing preview target:

```text
p95 < 500 ms
```

under normal operating conditions.

---

## PERF-003

Quote creation target:

```text
p95 < 1000 ms
```

excluding external provider latency.

---

## 96. Scalability Requirements

The Pricing Engine shall support:

```text
10M+ users
1M+ organizations
Millions of subscriptions
Billions of usage events
High-volume pricing calculations
High-volume quote generation
```

The service shall scale horizontally.

---

## 97. Availability

The Pricing Engine shall target:

```text
99.99% availability
```

for production pricing calculation APIs, subject to overall platform architecture.

---

## 98. Reliability

The system shall:

* Avoid silent calculation failures.
* Preserve pricing configuration.
* Support replay.
* Support reconciliation.
* Support disaster recovery.
* Maintain deterministic calculations.
* Maintain audit history.

---

## 99. Security Requirements

The Pricing Engine shall implement:

* Authentication.
* Authorization.
* RBAC.
* Tenant isolation.
* API rate limiting.
* Input validation.
* Output validation.
* Audit logging.
* Encryption in transit.
* Encryption at rest where appropriate.
* Secret management.
* Scoped service credentials.

---

## 100. Pricing Injection Protection

The engine shall reject attempts to manipulate:

```text
unit_price
discount_amount
tax_amount
currency
pricing_version
```

through unauthorized request parameters.

---

## 101. API Security

The following shall never be accepted as authoritative from untrusted clients:

```json
{
  "unit_price": 1,
  "discount": 99,
  "tax": 0,
  "total": 1
}
```

The server shall recalculate all authoritative values.

---

## 102. AI Security

AI pricing agents shall operate using:

* Scoped credentials.
* Tool-level authorization.
* Tenant-scoped context.
* Explicit policies.
* Approval gates.
* Action logging.

---

## 103. Prompt Injection Protection

Pricing agents shall not follow instructions originating from untrusted customer content that attempt to:

* Change price.
* Grant discounts.
* Change subscription.
* Override policy.
* Expose internal pricing rules.
* Access another tenant's pricing.

---

## 104. Data Model

Core entities shall include:

```text
Product
ProductVersion
PricingPlan
PricingPlanVersion
PricingRule
PricingTier
PricingComponent
PricingMeter
PricingRegion
PricingCurrency
Discount
Coupon
Credit
TaxContext
PricingCalculation
PricingLineItem
PricingSnapshot
PricingQuote
PricingQuoteItem
PricingOverride
PricingApproval
PricingExperiment
PricingEvent
PricingAuditEvent
PricingReconciliationRecord
```

---

## 105. Pricing Calculation Entity

```json
{
  "pricing_calculation_id": "calc_123",
  "tenant_id": "tenant_123",
  "organization_id": "org_123",
  "customer_id": "cust_123",
  "pricing_version_id": "price_v42",
  "currency": "USD",
  "subtotal": 38000,
  "discount": 3800,
  "credit": 1000,
  "tax": 3320,
  "total": 36520,
  "rounding_mode": "ROUND_HALF_UP",
  "created_at": "2026-08-28T00:00:00Z"
}
```

---

## 106. Pricing Line Item

```json
{
  "line_item_id": "line_123",
  "type": "SEAT",
  "description": "Professional Plan Seats",
  "quantity": 10,
  "unit_price": 2000,
  "amount": 20000,
  "currency": "USD",
  "pricing_rule_id": "rule_123"
}
```

---

## 107. Pricing Rule

```json
{
  "pricing_rule_id": "rule_123",
  "pricing_version_id": "price_v42",
  "component": "AI_TOKEN",
  "model": "PER_TOKEN",
  "unit_price": 5,
  "unit_scale": 1000000,
  "currency": "USD",
  "effective_from": "2026-08-01T00:00:00Z"
}
```

---

## 108. Quote Entity

```json
{
  "quote_id": "quote_123",
  "tenant_id": "tenant_123",
  "organization_id": "org_123",
  "customer_id": "cust_123",
  "pricing_version_id": "price_v42",
  "currency": "USD",
  "subtotal": 38000,
  "discount": 3800,
  "tax": 3320,
  "total": 37520,
  "status": "ISSUED",
  "valid_until": "2026-09-07T00:00:00Z"
}
```

---

## 109. Pricing Quote States

The quote state machine shall support:

```text
DRAFT
CALCULATING
ISSUED
ACCEPTED
REJECTED
EXPIRED
CANCELLED
SUPERSEDED
```

Invalid transitions shall be rejected.

---

## 110. Quote State Flow

```text
DRAFT
 ↓
CALCULATING
 ↓
ISSUED
 ├──→ ACCEPTED
 ├──→ REJECTED
 ├──→ EXPIRED
 └──→ CANCELLED
```

---

## 111. Pricing Version States

```text
DRAFT
VALIDATING
APPROVED
SCHEDULED
ACTIVE
RETIRED
ARCHIVED
```

Only authorized users may activate pricing versions.

---

## 112. Pricing Version Workflow

```text
Draft
 ↓
Validation
 ↓
Financial Review
 ↓
Security Review
 ↓
Approval
 ↓
Scheduled
 ↓
Activation
 ↓
Monitoring
 ↓
Retirement
```

---

## 113. Pricing Change Approval

Material pricing changes shall support:

```text
Created
 ↓
Review
 ↓
Finance Approval
 ↓
Product Approval
 ↓
Scheduled
 ↓
Activated
```

Approval requirements shall be configurable.

---

## 114. Pricing Rollback

The platform shall support rollback through version selection rather than mutating historical pricing.

Preferred approach:

```text
price_v42
   ↓
price_v43
   ↓
Problem Detected
   ↓
Activate price_v44
```

where `price_v44` restores the intended configuration.

Historical versions shall remain immutable.

---

## 115. Pricing Dispute Support

Support and finance users shall be able to inspect:

* Pricing calculation.
* Pricing version.
* Pricing rules.
* Usage.
* Discounts.
* Credits.
* Tax result.
* Quote.
* Invoice relationship.
* Audit events.

---

## 116. Pricing Calculation Reproduction

Given a historical calculation ID, authorized users shall be able to reproduce or inspect the exact calculation context.

The system shall preserve enough information to explain historical pricing without relying on mutable current configuration.

---

## 117. Historical Pricing Integrity

Historical pricing calculations shall never be recomputed using today's pricing rules and presented as historical truth.

---

## 118. Pricing Snapshot

Finalized billing-relevant pricing shall create a snapshot containing:

```text
Plan
Pricing Version
Rules
Quantities
Usage
Unit Prices
Discounts
Credits
Taxes
Currency
Rounding
Final Amount
```

---

## 119. Pricing Service Boundaries

Recommended architecture:

```text
                    ┌───────────────────────┐
                    │      API Gateway      │
                    └───────────┬───────────┘
                                │
                    ┌───────────▼───────────┐
                    │    Pricing Service    │
                    └───────────┬───────────┘
                                │
        ┌───────────────────────┼────────────────────────┐
        │                       │                        │
        ▼                       ▼                        ▼
 Pricing Rules             Usage Meter              Customer
        │                       │                        │
        └───────────────────────┼────────────────────────┘
                                │
                     ┌──────────▼──────────┐
                     │    Discount Engine  │
                     └──────────┬──────────┘
                                │
                     ┌──────────▼──────────┐
                     │     Tax Service     │
                     └──────────┬──────────┘
                                │
                     ┌──────────▼──────────┐
                     │   Pricing Result    │
                     └──────────┬──────────┘
                                │
              ┌─────────────────┼────────────────┐
              ▼                 ▼                ▼
          Billing           Subscription      Analytics
```

---

## 120. Pricing Engine Dependency Rules

The Pricing Engine shall:

* Consume authoritative usage.
* Consume subscription context.
* Resolve pricing rules.
* Calculate financial values.
* Return deterministic results.

The Pricing Engine shall not:

* Charge payment cards.
* Grant product permissions.
* Directly mutate subscription state without authorization.
* Modify financial ledger records owned by Billing.

---

## 121. Pricing-to-Billing Workflow

```text
Pricing Request
 ↓
Price Calculation
 ↓
Pricing Snapshot
 ↓
Billing Request
 ↓
Invoice Generation
 ↓
Payment
 ↓
Billing Confirmation
```

---

## 122. Pricing-to-Subscription Workflow

```text
Plan Selection
 ↓
Pricing Preview
 ↓
User Confirmation
 ↓
Subscription Change
 ↓
Pricing Snapshot
 ↓
Billing
 ↓
Entitlements
```

---

## 123. Pricing-to-AI Workflow

```text
Customer Context
 ↓
Pricing Engine
 ↓
Authoritative Calculation
 ↓
AI Explanation
 ↓
AI Recommendation
 ↓
Human/User Decision
```

AI shall consume authoritative pricing rather than independently calculating production prices.

---

## 124. AI Cost Optimization

The AI Pricing Agent may recommend:

* Lower-cost plan.
* Annual commitment.
* Seat optimization.
* Usage optimization.
* Model optimization.
* Workflow optimization.
* Add-on removal.

Recommendations shall include estimated financial impact.

---

## 125. AI Pricing Forecast

The system may generate:

```text
Current Monthly Cost
Forecast Monthly Cost
Forecast Annual Cost
Expected Usage Growth
Expected Overage
Recommended Plan
Expected Savings
```

---

## 126. Pricing Anomaly Detection

AI shall flag:

```text
Unexpected price > threshold
Discount > expected range
Price change without approved version
Unusual customer-specific price
Duplicate discount
Unexpected tax
Unexpected currency
Unexpected usage charge
```

---

## 127. Financial Safety Controls

The system shall support configurable:

```text
maximum_discount
maximum_credit
maximum_price_override
maximum_quote_value
maximum_ai_action_value
maximum_daily_pricing_adjustment
```

---

## 128. AI Financial Limits

AI execution shall be constrained by:

```text
action_type
tenant
customer
maximum_value
maximum_discount
approval_requirement
time_window
```

---

## 129. Pricing Rate Limits

The system shall rate-limit:

* Pricing calculations.
* Quote generation.
* Coupon validation.
* Pricing configuration changes.
* Pricing override requests.

Higher limits may be granted to trusted internal services.

---

## 130. Observability

Every pricing operation shall support:

```text
request_id
trace_id
correlation_id
tenant_id
organization_id
customer_id
pricing_calculation_id
pricing_version_id
quote_id
```

---

## 131. Distributed Tracing

Tracing shall propagate through:

```text
API Gateway
Pricing Service
Subscription Service
Usage Service
Discount Engine
Tax Service
Billing Service
Payment Provider
AI Gateway
Workflow Engine
```

---

## 132. Metrics

The system shall expose:

```text
pricing_calculation_count
pricing_calculation_success_rate
pricing_calculation_error_rate
pricing_calculation_latency
pricing_preview_count
quote_generation_count
quote_acceptance_rate
discount_application_rate
discount_rejection_rate
pricing_override_rate
pricing_anomaly_rate
pricing_version_activation_count
pricing_reconciliation_failure_rate
```

---

## 133. Logging

Logs shall be:

* Structured.
* Correlated.
* Tenant-aware.
* Searchable.
* Redacted.
* Immutable where required.

Sensitive financial information shall not be unnecessarily logged.

---

## 134. Disaster Recovery

The Pricing Engine shall support:

* Database backups.
* Point-in-time recovery.
* Pricing version recovery.
* Event replay.
* Pricing snapshot recovery.
* Reconciliation.
* Failover.

Target:

```text
RPO <= 5 minutes
RTO <= 30 minutes
```

for critical production infrastructure, subject to deployment architecture.

---

## 135. Testing Requirements

## Unit Tests

The system shall test:

* Flat pricing.
* Seat pricing.
* Usage pricing.
* Tier pricing.
* Volume pricing.
* Graduated pricing.
* Hybrid pricing.
* Discounts.
* Coupons.
* Credits.
* Taxes.
* Rounding.
* Proration.
* Currency.
* Effective dates.

---

## Integration Tests

The system shall test:

* Subscription Service.
* Usage Metering.
* Billing Service.
* Tax Service.
* Payment Provider.
* Entitlement Service.

---

## Security Tests

The system shall test:

* RBAC.
* Tenant isolation.
* Privilege escalation.
* Pricing manipulation.
* Discount manipulation.
* Coupon abuse.
* API authorization.
* AI tool authorization.

---

## Concurrency Tests

The system shall test:

* Concurrent pricing updates.
* Concurrent quote generation.
* Concurrent discount application.
* Concurrent pricing-version activation.
* Duplicate requests.

---

## Failure Tests

The system shall test:

* Usage service unavailable.
* Tax service unavailable.
* Billing service unavailable.
* Database failure.
* Queue failure.
* Network timeout.
* Duplicate events.
* Partial workflow failure.

---

## 136. AI Testing

AI pricing systems shall be tested for:

* Hallucinated prices.
* Hallucinated discounts.
* Prompt injection.
* Unauthorized tool use.
* Tenant boundary violations.
* Incorrect plan recommendations.
* Incorrect cost explanations.
* Incorrect pricing forecasts.
* Unauthorized financial actions.

---

## 137. Acceptance Criteria

## AC-001

Frontend-provided prices cannot override server-side pricing.

## AC-002

Every authoritative calculation references a pricing version.

## AC-003

Historical calculations remain reproducible.

## AC-004

Pricing versions are immutable after activation.

## AC-005

Pricing rules support effective dates.

## AC-006

The engine supports multiple pricing models.

## AC-007

The engine supports tiered pricing.

## AC-008

The engine supports volume pricing.

## AC-009

The engine supports graduated pricing.

## AC-010

The engine supports hybrid pricing.

## AC-011

The engine supports discounts.

## AC-012

Discount stacking is deterministic.

## AC-013

Coupon eligibility is validated server-side.

## AC-014

Credits are applied according to explicit policies.

## AC-015

Monetary calculations do not use unsafe floating-point arithmetic.

## AC-016

Rounding behavior is deterministic.

## AC-017

Currency is explicit for every monetary value.

## AC-018

Pricing previews do not mutate financial state.

## AC-019

Quotes preserve their original pricing snapshot.

## AC-020

Expired quotes cannot be accepted without revalidation.

## AC-021

Proration is deterministic.

## AC-022

Usage charges are based on authoritative usage.

## AC-023

Tax calculation is isolated behind a controlled service boundary.

## AC-024

Pricing calculations are idempotent where durable artifacts are created.

## AC-025

Concurrent pricing changes cannot corrupt active configuration.

## AC-026

Pricing configuration changes are audited.

## AC-027

Pricing overrides require authorization.

## AC-028

High-risk pricing overrides require configurable approval.

## AC-029

AI cannot modify pricing rules autonomously.

## AC-030

AI cannot bypass discount limits.

## AC-031

AI cannot fabricate authoritative prices.

## AC-032

AI pricing recommendations are clearly distinguished from authoritative calculations.

## AC-033

All material pricing operations are traceable.

## AC-034

Pricing discrepancies can be reconciled with Billing.

## AC-035

Tenant isolation is enforced.

## AC-036

Pricing service remains functional under horizontal scaling.

## AC-037

External service failures do not corrupt pricing configuration.

## AC-038

Historical pricing cannot be silently changed.

## AC-039

Pricing anomalies are observable.

## AC-040

Pricing calculations can be reconstructed for authorized users.

---

## 138. Definition of Done

The Pricing Engine shall be considered production-ready only when:

* Centralized Pricing Service is implemented.
* Pricing rules are versioned.
* Pricing versions are immutable.
* Effective dating is implemented.
* Multi-tenant isolation is implemented.
* Flat pricing is implemented.
* Seat pricing is implemented.
* User pricing is implemented.
* Usage pricing is implemented.
* Tiered pricing is implemented.
* Volume pricing is implemented.
* Graduated pricing is implemented.
* Hybrid pricing is implemented.
* Add-on pricing is implemented.
* Overage pricing is implemented.
* Discount Engine is implemented.
* Coupon Engine is implemented.
* Credit handling is implemented.
* Currency handling is implemented.
* Deterministic rounding is implemented.
* Proration is implemented.
* Pricing previews are implemented.
* Quote Engine is implemented.
* Quote snapshots are implemented.
* Quote expiration is implemented.
* Enterprise pricing is implemented.
* Pricing overrides are implemented.
* Approval workflows are implemented.
* AI pricing recommendations are implemented.
* AI guardrails are implemented.
* AI action limits are implemented.
* Usage integration is implemented.
* Subscription integration is implemented.
* Billing integration is implemented.
* Tax integration boundary is implemented.
* Reconciliation is implemented.
* Audit logging is implemented.
* Distributed tracing is implemented.
* Metrics are implemented.
* Structured logging is implemented.
* Rate limiting is implemented.
* Disaster recovery is tested.
* Security testing is completed.
* Load testing is completed.
* Concurrency testing is completed.
* Failure-mode testing is completed.
* AI safety testing is completed.
* Historical pricing reconstruction is verified.

---

## 139. FAANG-Level Engineering Principles

The SalesGenie Pricing Engine shall follow these principles:

1. **Pricing has one authoritative calculation engine.**
2. **Frontend prices are never authoritative.**
3. **Money is represented using exact arithmetic.**
4. **Every calculation is tied to an immutable pricing version.**
5. **Historical pricing remains reproducible.**
6. **Pricing rules are effective-dated.**
7. **Pricing configuration is separated from pricing execution.**
8. **Discounts are policy-controlled.**
9. **Credits are explicitly scoped and auditable.**
10. **Tax logic is isolated behind a controlled boundary.**
11. **Usage must come from authoritative metering.**
12. **Pricing previews never mutate financial state.**
13. **Quotes preserve immutable pricing snapshots.**
14. **Proration is deterministic.**
15. **Concurrent configuration changes are explicitly controlled.**
16. **Financially consequential operations are idempotent.**
17. **AI consumes authoritative pricing rather than inventing production prices.**
18. **AI recommendations are separated from authoritative financial state.**
19. **AI financial actions are constrained by explicit policies.**
20. **High-risk AI actions require human approval.**
21. **All material pricing changes are auditable.**
22. **Pricing discrepancies are automatically detectable.**
23. **External dependencies are treated as unreliable.**
24. **Pricing failures never silently produce incorrect prices.**
25. **Tenant isolation is enforced at every service boundary.**
26. **Pricing configuration changes are versioned rather than silently mutated.**
27. **Pricing calculations are observable and traceable.**
28. **Every finalized price must be explainable.**
29. **Financial correctness takes precedence over convenience.**
30. **The Pricing Engine must remain deterministic, secure, scalable, auditable, and recoverable.**
