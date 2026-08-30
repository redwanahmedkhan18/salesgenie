# SalesGenie — Payment Gateway

## FAANG-Level User Requirements, System Requirements & Functional Requirements

**Document:** `payment_gateway.md`  
**Product:** SalesGenie — Enterprise AI Customer Support, Sales, Lead Generation & Workflow Automation Platform  
**Scope:** Payment gateway orchestration, payment methods, payment intents, authorization, capture, refunds, voids, payment status, webhooks, recurring payments, metered billing collection, invoices, credits, taxes, failed payments, retries, payment disputes, reconciliation, fraud controls, PCI scope reduction, multi-currency, multi-tenant payments, enterprise payments, AI-assisted payment operations, human payment operations, auditability, security, and observability.

---

## 1. PURPOSE

SalesGenie SHALL provide a secure, resilient, multi-tenant Payment Gateway subsystem responsible for initiating, authorizing, capturing, refunding, reconciling, and monitoring customer payments.

The Payment Gateway SHALL integrate with external payment providers through a provider-agnostic abstraction layer.

The system SHALL support:

- One-time payments
- Subscription payments
- Recurring payments
- Usage-based billing payments
- Metered billing payments
- Invoice payments
- Prepaid credits
- Partial payments
- Full payments
- Partial refunds
- Full refunds
- Payment retries
- Payment-method updates
- Payment authorization
- Payment capture
- Payment cancellation
- Payment failure recovery
- Payment disputes
- Payment reconciliation
- Multi-currency payments
- Enterprise payment workflows
- AI-assisted payment operations
- Human-operated payment operations

The system SHALL ensure that payment state, financial state, and subscription state remain consistent.

---

## 2. PAYMENT GATEWAY PRINCIPLES

The Payment Gateway SHALL follow:

1. Security by default
2. PCI scope minimization
3. Idempotency
4. Strong consistency for financial state
5. Eventual consistency for non-critical UI projections
6. Provider abstraction
7. Provider failover where supported
8. Tenant isolation
9. Least privilege
10. Immutable financial records
11. Full auditability
12. Deterministic state transitions
13. Reconciliation
14. Fraud prevention
15. Webhook authenticity verification
16. Replay protection
17. Duplicate-event protection
18. Human approval for high-risk operations
19. AI safety
20. Disaster recovery
21. Financial correctness
22. Observability

---

## 3. ACTORS

| Actor | Responsibilities |
|---|---|
| End Customer | Make payments and manage payment methods |
| Organization Owner | Manage organization billing |
| Customer Admin | Manage payment methods and invoices |
| Finance Admin | Manage payments, refunds and disputes |
| Billing Admin | Manage billing operations |
| Super Admin | Monitor platform-wide payment operations |
| AI Billing Agent | Analyze payment activity |
| AI Finance Agent | Assist with payment investigations |
| Subscription Service | Maintain subscription state |
| Billing Service | Generate financial obligations |
| Invoice Service | Generate invoices |
| Metering Service | Provide usage-based charges |
| Pricing Engine | Calculate charges |
| Payment Gateway | Orchestrate payment transactions |
| Payment Provider | Process external payment transactions |
| Fraud Service | Evaluate payment risk |
| Tax Service | Calculate applicable taxes |
| Reconciliation Service | Reconcile payment records |
| Audit Service | Record financial activity |

---

## 4. USER REQUIREMENTS

## UR-PAY-001 — Add Payment Method

Authorized customers SHALL be able to add supported payment methods.

Examples:

```text
Credit Card
Debit Card
Bank Account
Digital Wallet
Other Provider-Supported Methods
```

SalesGenie SHALL avoid storing raw payment credentials whenever possible.

---

## UR-PAY-002 — View Payment Methods

Customers SHALL be able to view:

```text
Payment Method Type
Brand
Masked Identifier
Expiration
Default Status
Verification Status
Billing Address
Created Date
```

Sensitive payment credentials SHALL never be exposed.

---

## UR-PAY-003 — Set Default Payment Method

Authorized users SHALL be able to designate a payment method as the default payment method.

---

## UR-PAY-004 — Remove Payment Method

Customers SHALL be able to remove an unused payment method.

The system SHALL prevent removal when doing so would leave an active subscription or payment obligation without a valid payment method, unless an alternative payment policy exists.

---

## UR-PAY-005 — Make One-Time Payment

Users SHALL be able to pay an invoice or other eligible charge.

---

## UR-PAY-006 — Pay Invoice

Customers SHALL be able to initiate payment against an outstanding invoice.

The UI SHALL clearly display:

```text
Invoice Number
Amount Due
Currency
Due Date
Taxes
Credits
Previous Payments
Remaining Balance
```

---

## UR-PAY-007 — View Payment Status

Users SHALL be able to see:

```text
Pending
Processing
Authorized
Succeeded
Failed
Canceled
Refunded
Partially Refunded
Disputed
```

---

## UR-PAY-008 — Payment Confirmation

Successful payments SHALL provide confirmation containing:

```text
Payment ID
Invoice ID
Amount
Currency
Payment Method
Timestamp
Status
Receipt
```

---

## UR-PAY-009 — Payment Receipt

Users SHALL be able to access payment receipts.

---

## UR-PAY-010 — Payment History

Authorized users SHALL be able to view historical payments.

Filters SHALL include:

```text
Date
Status
Amount
Currency
Invoice
Payment Method
Subscription
Transaction ID
```

---

## UR-PAY-011 — Failed Payment Explanation

Users SHALL receive understandable failure information without exposing sensitive provider internals.

Example:

```text
Payment failed.

Reason:
Your payment method was declined.

Recommended action:
Update your payment method and try again.
```

---

## UR-PAY-012 — Retry Failed Payment

Authorized users SHALL be able to retry eligible failed payments.

---

## UR-PAY-013 — Automatic Retry

SalesGenie SHALL automatically retry eligible failed recurring payments according to configured billing policies.

---

## UR-PAY-014 — Update Payment Method

Customers SHALL be able to replace an expired or failed payment method.

---

## UR-PAY-015 — Subscription Payment

Users SHALL be able to pay for:

```text
Free Tier upgrades
Monthly subscriptions
Yearly subscriptions
Usage-based subscriptions
Metered subscriptions
Enterprise subscriptions
```

---

## UR-PAY-016 — Usage-Based Payment

Customers SHALL be able to pay charges generated by:

```text
AI Tokens
Workflow Executions
Lead Generation
API Requests
Voice Minutes
Messaging
Document Processing
Storage
Integration Usage
MCP Tool Usage
```

---

## UR-PAY-017 — Partial Payment

Where supported by billing policy, customers SHALL be able to make partial payments.

---

## UR-PAY-018 — Refund Visibility

Customers SHALL be able to see refund status.

---

## UR-PAY-019 — Refund Request

Customers MAY request refunds when the billing policy permits.

Refund requests MAY require human review.

---

## UR-PAY-020 — Payment Dispute

Authorized users SHALL be able to report a payment dispute.

---

## UR-PAY-021 — Payment Security

Users SHALL be informed when additional payment verification is required.

---

## UR-PAY-022 — Currency Display

Customers SHALL see the payment currency before confirming payment.

---

## UR-PAY-023 — Payment Authorization

Before final submission, the UI SHALL display:

```text
Amount
Currency
Tax
Discount
Credits
Final Amount
Payment Method
```

---

## UR-PAY-024 — Payment Cancellation

Users SHALL be able to cancel eligible pending payments.

---

## UR-PAY-025 — Payment Notifications

Users SHALL receive notifications for:

```text
Payment succeeded
Payment failed
Payment requires action
Payment refunded
Payment disputed
Payment method expiring
Payment retry scheduled
Payment retry failed
```

---

## 5. SYSTEM REQUIREMENTS

## SR-PAY-001 — Payment Gateway Abstraction

SalesGenie SHALL implement a provider-agnostic payment abstraction.

The architecture SHALL support multiple payment providers without coupling core billing logic to a specific provider.

---

## SR-PAY-002 — Provider Adapter

Each provider SHALL implement a standardized adapter interface.

Example:

```text
create_customer()
create_payment_method()
create_payment_intent()
authorize_payment()
capture_payment()
cancel_payment()
refund_payment()
retrieve_payment()
list_payment_methods()
create_subscription_payment()
```

---

## SR-PAY-003 — Provider Configuration

The system SHALL support provider configuration per:

```text
Platform
Tenant
Organization
Region
Currency
Payment Method
Transaction Type
```

---

## SR-PAY-004 — Payment Intent

Every payment SHALL have an internal Payment Intent.

Required fields:

```text
payment_intent_id
tenant_id
organization_id
customer_id
invoice_id
subscription_id
amount
currency
status
payment_method_id
provider
provider_payment_id
idempotency_key
created_at
updated_at
```

---

## SR-PAY-005 — Payment Transaction

Every provider transaction SHALL be represented internally.

```text
payment_transaction_id
payment_intent_id
provider
provider_transaction_id
transaction_type
amount
currency
status
provider_response_code
created_at
updated_at
```

---

## SR-PAY-006 — Payment State Machine

Payment states SHALL be explicitly modeled.

```text
CREATED
  ↓
REQUIRES_PAYMENT_METHOD
  ↓
REQUIRES_CONFIRMATION
  ↓
PROCESSING
  ↓
AUTHORIZED
  ↓
CAPTURED
  ↓
SUCCEEDED
```

Failure paths:

```text
PROCESSING
    ↓
FAILED

AUTHORIZED
    ↓
CANCELED

SUCCEEDED
    ↓
PARTIALLY_REFUNDED
    ↓
REFUNDED

SUCCEEDED
    ↓
DISPUTED
```

---

## SR-PAY-007 — State Transition Enforcement

Only valid payment state transitions SHALL be permitted.

Invalid transitions SHALL be rejected.

---

## SR-PAY-008 — Idempotency

Every payment mutation SHALL support idempotency.

Examples:

```text
Create Payment
Confirm Payment
Capture Payment
Cancel Payment
Refund Payment
Retry Payment
Attach Payment Method
```

---

## SR-PAY-009 — Duplicate Prevention

Repeated requests using the same idempotency key SHALL NOT create duplicate charges.

---

## SR-PAY-010 — Payment Amount Integrity

The Payment Gateway SHALL validate the authoritative amount before processing.

The frontend SHALL never be trusted as the financial source of truth.

---

## SR-PAY-011 — Currency Integrity

The payment currency SHALL be validated against:

```text
Invoice Currency
Subscription Currency
Pricing Currency
Provider Supported Currency
Tenant Configuration
```

---

## SR-PAY-012 — Amount Integrity

The system SHALL prevent:

```text
Negative payment amount
Invalid precision
Overflow
Currency mismatch
Unauthorized amount changes
Tampered invoice amount
```

---

## SR-PAY-013 — PCI Scope Reduction

SalesGenie SHOULD use provider-hosted payment collection, tokenization, or equivalent mechanisms to minimize PCI DSS scope.

SalesGenie SHALL NOT unnecessarily store raw:

```text
PAN
CVV
Full Card Number
Magnetic Stripe Data
```

---

## SR-PAY-014 — Payment Tokenization

Payment credentials SHALL be represented internally using secure provider tokens or payment-method references.

---

## SR-PAY-015 — Encryption

Sensitive payment-related data SHALL be encrypted:

```text
At Rest
In Transit
During Sensitive Processing
```

---

## SR-PAY-016 — Secrets Management

Provider credentials SHALL be stored using secure secrets management.

They SHALL NOT be stored in:

```text
Source Code
Frontend Code
Git
Logs
Client Storage
Plaintext Database Fields
```

---

## SR-PAY-017 — Tenant Isolation

Every payment object SHALL be associated with a tenant.

Cross-tenant access SHALL be prohibited.

---

## SR-PAY-018 — Authorization

Payment operations SHALL enforce RBAC and appropriate authorization policies.

---

## SR-PAY-019 — Financial Audit

Every financially significant action SHALL produce an immutable audit record.

---

## 6. FUNCTIONAL REQUIREMENTS

## FR-PAY-001 — Create Payment Intent

```http
POST /api/v1/payments/intents
```

Request:

```json
{
  "invoice_id": "inv_123",
  "amount": 199.99,
  "currency": "USD",
  "payment_method_id": "pm_123"
}
```

The backend SHALL recalculate and validate the amount before creating the payment.

---

## FR-PAY-002 — Retrieve Payment Intent

```http
GET /api/v1/payments/intents/{payment_intent_id}
```

---

## FR-PAY-003 — Confirm Payment

```http
POST /api/v1/payments/intents/{payment_intent_id}/confirm
```

---

## FR-PAY-004 — Authorize Payment

```http
POST /api/v1/payments/intents/{payment_intent_id}/authorize
```

---

## FR-PAY-005 — Capture Payment

```http
POST /api/v1/payments/intents/{payment_intent_id}/capture
```

---

## FR-PAY-006 — Cancel Payment

```http
POST /api/v1/payments/intents/{payment_intent_id}/cancel
```

---

## FR-PAY-007 — Refund Payment

```http
POST /api/v1/payments/{payment_id}/refund
```

Request:

```json
{
  "amount": 50.00,
  "reason": "customer_request"
}
```

---

## FR-PAY-008 — Full Refund

The system SHALL support refunding the remaining refundable amount.

---

## FR-PAY-009 — Partial Refund

The system SHALL support partial refunds when allowed.

---

## FR-PAY-010 — Refund Idempotency

Repeated refund requests SHALL not create duplicate refunds.

---

## 7. PAYMENT METHOD MANAGEMENT

## FR-PAY-011 — Add Payment Method

```http
POST /api/v1/payment-methods
```

---

## FR-PAY-012 — List Payment Methods

```http
GET /api/v1/payment-methods
```

---

## FR-PAY-013 — Set Default Payment Method

```http
POST /api/v1/payment-methods/{id}/default
```

---

## FR-PAY-014 — Remove Payment Method

```http
DELETE /api/v1/payment-methods/{id}
```

---

## FR-PAY-015 — Verify Payment Method

The system SHALL support provider-specific payment-method verification flows.

---

## 8. SUBSCRIPTION PAYMENT

## FR-PAY-016

The Payment Gateway SHALL integrate with Subscription Management.

Subscription lifecycle:

```text
Subscription Created
       ↓
Payment Required
       ↓
Payment Authorized
       ↓
Payment Captured
       ↓
Subscription Active
```

---

## FR-PAY-017

A failed recurring payment SHALL transition the subscription according to configured dunning policies.

Example:

```text
PAYMENT_FAILED
      ↓
RETRY_1
      ↓
RETRY_2
      ↓
RETRY_3
      ↓
PAST_DUE
      ↓
GRACE_PERIOD
      ↓
SUSPENDED
      ↓
CANCELED
```

---

## 9. METERED BILLING PAYMENT

## FR-PAY-018

The Payment Gateway SHALL integrate with Metered Billing.

```text
Usage
 ↓
Meter
 ↓
Aggregation
 ↓
Pricing
 ↓
Rated Usage
 ↓
Invoice
 ↓
Payment Intent
 ↓
Payment Provider
 ↓
Payment
```

---

## FR-PAY-019

The system SHALL prevent payment collection for an invoice whose financial state is not finalized.

---

## 10. INVOICE PAYMENT

## FR-PAY-020

The system SHALL support:

```text
Pay Invoice
Retry Invoice
Cancel Payment
Refund Invoice Payment
View Payment Status
```

---

## FR-PAY-021

Successful invoice payment SHALL update invoice state.

Example:

```text
OPEN
 ↓
PAYMENT_PROCESSING
 ↓
PAID
```

---

## FR-PAY-022

Failed invoice payment SHALL preserve the invoice as outstanding.

---

## 11. PAYMENT RETRY ENGINE

## FR-PAY-023

The system SHALL support configurable retry schedules.

Example:

```text
Attempt 1 → Day 0
Attempt 2 → Day 2
Attempt 3 → Day 5
Attempt 4 → Day 8
```

---

## FR-PAY-024

Retry policies SHALL be configurable by:

```text
Tenant
Plan
Payment Provider
Currency
Payment Method
Failure Type
Subscription Type
```

---

## FR-PAY-025

The retry engine SHALL distinguish:

```text
Retryable
Non-Retryable
Requires Customer Action
Requires Fraud Review
```

---

## 12. PAYMENT FAILURE HANDLING

## FR-PAY-026

The system SHALL classify payment failures.

Example categories:

```text
CARD_DECLINED
INSUFFICIENT_FUNDS
EXPIRED_PAYMENT_METHOD
INVALID_PAYMENT_METHOD
AUTHENTICATION_REQUIRED
FRAUD_REVIEW
PROVIDER_ERROR
NETWORK_ERROR
RATE_LIMITED
CURRENCY_UNSUPPORTED
AMOUNT_INVALID
ACCOUNT_RESTRICTED
```

---

## FR-PAY-027

The system SHALL never retry non-retryable failures indefinitely.

---

## 13. WEBHOOK PROCESSING

## FR-PAY-028

The Payment Gateway SHALL provide a secure webhook endpoint.

```http
POST /api/v1/payments/webhooks/{provider}
```

---

## FR-PAY-029

Webhook signatures SHALL be verified before processing.

---

## FR-PAY-030

Webhook events SHALL support idempotency.

---

## FR-PAY-031

Webhook events SHALL be stored before business processing when required for reliable recovery.

---

## FR-PAY-032

Webhook processing SHALL support:

```text
Payment succeeded
Payment failed
Payment authorized
Payment captured
Payment canceled
Refund created
Refund completed
Refund failed
Dispute created
Dispute updated
Payment method updated
Subscription payment failed
```

---

## FR-PAY-033

Webhook replay SHALL be supported for authorized operators.

---

## FR-PAY-034

Webhook events SHALL have replay protection.

---

## 14. PAYMENT RECONCILIATION

## FR-PAY-035

The system SHALL reconcile:

```text
Internal Payment Intent
        ↕
Internal Transaction
        ↕
Provider Transaction
        ↕
Invoice
        ↕
Ledger
```

---

## FR-PAY-036

Reconciliation SHALL identify:

```text
Missing Transaction
Duplicate Transaction
Amount Mismatch
Currency Mismatch
Status Mismatch
Unknown Provider Transaction
Unknown Internal Transaction
Refund Mismatch
```

---

## FR-PAY-037

Reconciliation exceptions SHALL be assigned a state:

```text
OPEN
INVESTIGATING
RESOLVED
ESCALATED
```

---

## 15. REFUND MANAGEMENT

## FR-PAY-038

Refund eligibility SHALL be calculated server-side.

---

## FR-PAY-039

Refundable amount SHALL be:

```text
original_captured_amount
-
previous_refunds
```

---

## FR-PAY-040

The system SHALL prevent refunds exceeding the refundable balance.

---

## FR-PAY-041

Refunds SHALL support reason codes.

Example:

```text
CUSTOMER_REQUEST
DUPLICATE_PAYMENT
SERVICE_FAILURE
BILLING_ERROR
FRAUD
GOODWILL
OTHER
```

---

## FR-PAY-042

Large or unusual refunds SHALL require human approval.

---

## 16. DISPUTE MANAGEMENT

## FR-PAY-043

The system SHALL record payment disputes.

Fields:

```text
dispute_id
payment_id
provider_dispute_id
amount
currency
reason
status
evidence_deadline
created_at
updated_at
```

---

## FR-PAY-044

Finance administrators SHALL be able to review disputes.

---

## FR-PAY-045

The system SHALL support dispute lifecycle tracking:

```text
OPEN
EVIDENCE_REQUIRED
EVIDENCE_SUBMITTED
UNDER_REVIEW
WON
LOST
CLOSED
```

---

## 17. FRAUD DETECTION

## FR-PAY-046

Payments SHALL be evaluated against fraud policies.

Potential signals:

```text
Velocity
Payment Frequency
Amount
IP Risk
Device Risk
Geographic Anomaly
Account Age
Payment Method Risk
Failed Attempts
Behavioral Signals
```

---

## FR-PAY-047

The system SHALL support:

```text
ALLOW
REVIEW
CHALLENGE
BLOCK
```

fraud outcomes.

---

## 18. PAYMENT VELOCITY CONTROLS

## FR-PAY-048

The system SHALL detect excessive payment attempts.

Example:

```text
10 payment attempts
within 5 minutes
```

The system MAY require additional verification or temporarily block further attempts.

---

## 19. MULTI-CURRENCY

## FR-PAY-049

The system SHALL support multiple currencies where supported by the configured provider.

---

## FR-PAY-050

Currency SHALL be immutable for a finalized payment intent.

---

## FR-PAY-051

Exchange-rate information SHALL be versioned when conversion is required.

---

## 20. TAX INTEGRATION

## FR-PAY-052

The Payment Gateway SHALL consume authoritative tax calculations from the Tax Service.

The payment layer SHALL not independently invent tax amounts.

---

## 21. CREDITS

## FR-PAY-053

The system SHALL support applying authorized credits to eligible invoices.

---

## FR-PAY-054

Credit application SHALL be atomic.

---

## FR-PAY-055

Credits SHALL not be consumed more than once.

---

## 22. PAYMENT EVENTS

The system SHALL publish events including:

```text
payment.created
payment.requires_action
payment.authorized
payment.capture_started
payment.captured
payment.succeeded
payment.failed
payment.canceled
payment.expired

payment.retry_scheduled
payment.retry_started
payment.retry_failed
payment.retry_succeeded

payment.refund_requested
payment.refund_started
payment.refunded
payment.refund_failed

payment.dispute_created
payment.dispute_updated
payment.dispute_resolved

payment.method_added
payment.method_updated
payment.method_removed
payment.method_expiring

payment.webhook_received
payment.webhook_verified
payment.webhook_rejected
payment.webhook_duplicate

payment.reconciliation_started
payment.reconciliation_completed
payment.reconciliation_failed
```

---

## 23. PAYMENT API

## Payment Intents

```http
POST   /api/v1/payments/intents
GET    /api/v1/payments/intents
GET    /api/v1/payments/intents/{id}
POST   /api/v1/payments/intents/{id}/confirm
POST   /api/v1/payments/intents/{id}/authorize
POST   /api/v1/payments/intents/{id}/capture
POST   /api/v1/payments/intents/{id}/cancel
```

---

## Payments

```http
GET    /api/v1/payments
GET    /api/v1/payments/{id}
POST   /api/v1/payments/{id}/retry
POST   /api/v1/payments/{id}/refund
```

---

## Payment Methods

```http
GET    /api/v1/payment-methods
POST   /api/v1/payment-methods
GET    /api/v1/payment-methods/{id}
POST   /api/v1/payment-methods/{id}/default
DELETE /api/v1/payment-methods/{id}
```

---

## Refunds

```http
GET    /api/v1/refunds
GET    /api/v1/refunds/{id}
POST   /api/v1/refunds
```

---

## Disputes

```http
GET    /api/v1/payment-disputes
GET    /api/v1/payment-disputes/{id}
POST   /api/v1/payment-disputes/{id}/evidence
```

---

## Reconciliation

```http
GET    /api/v1/payments/reconciliation
GET    /api/v1/payments/reconciliation/{id}
POST   /api/v1/payments/reconciliation/run
```

---

## 24. DATABASE REQUIREMENTS

Minimum entities:

```text
payment_providers
payment_provider_accounts
payment_provider_configurations

payment_customers
payment_methods
payment_method_tokens

payment_intents
payment_transactions
payment_attempts

payment_authorizations
payment_captures
payment_cancellations

refunds
refund_items

payment_disputes
payment_dispute_evidence

payment_webhooks
payment_webhook_events

payment_retries
payment_retry_policies

payment_failures
payment_failure_codes

payment_reconciliation_runs
payment_reconciliation_records

payment_risk_assessments
payment_risk_events

payment_ledger_entries

payment_notifications

payment_approval_requests

payment_audit_logs
```

---

## 25. PAYMENT DATA MODEL

```text
PaymentIntent
├── payment_intent_id
├── tenant_id
├── organization_id
├── customer_id
├── invoice_id
├── subscription_id
├── amount
├── currency
├── status
├── payment_method_id
├── provider
├── provider_payment_id
├── idempotency_key
├── metadata
├── created_at
└── updated_at
```

```text
PaymentTransaction
├── transaction_id
├── payment_intent_id
├── provider
├── provider_transaction_id
├── transaction_type
├── amount
├── currency
├── status
├── provider_response_code
├── provider_response_reference
├── created_at
└── updated_at
```

```text
Refund
├── refund_id
├── payment_id
├── tenant_id
├── amount
├── currency
├── reason
├── status
├── provider_refund_id
├── requested_by
├── approved_by
├── created_at
└── completed_at
```

---

## 26. PAYMENT WORKFLOW

```text
CUSTOMER
   ↓
SELECT INVOICE
   ↓
AUTHORITATIVE BILLING VALIDATION
   ↓
CALCULATE FINAL AMOUNT
   ↓
SELECT PAYMENT METHOD
   ↓
CREATE PAYMENT INTENT
   ↓
RISK EVALUATION
   ↓
PROVIDER REQUEST
   ↓
AUTHENTICATION / 3DS IF REQUIRED
   ↓
AUTHORIZATION
   ↓
CAPTURE
   ↓
PROVIDER CONFIRMATION
   ↓
INTERNAL PAYMENT UPDATE
   ↓
INVOICE UPDATE
   ↓
SUBSCRIPTION UPDATE
   ↓
LEDGER UPDATE
   ↓
RECEIPT
   ↓
AUDIT
```

---

## 27. PAYMENT FAILURE WORKFLOW

```text
PAYMENT REQUEST
      ↓
PROVIDER
      ↓
PAYMENT FAILED
      ↓
CLASSIFY FAILURE
      ↓
┌──────────────┬──────────────────┬─────────────────┐
↓              ↓                  ↓
RETRYABLE      CUSTOMER ACTION    NON-RETRYABLE
↓              ↓                  ↓
RETRY ENGINE   NOTIFY CUSTOMER    MARK FAILED
↓              ↓
RETRY          UPDATE METHOD
↓
SUCCESS / FAILURE
```

---

## 28. REFUND WORKFLOW

```text
REFUND REQUEST
      ↓
AUTHORIZATION
      ↓
ELIGIBILITY CHECK
      ↓
REFUNDABLE BALANCE CHECK
      ↓
APPROVAL REQUIRED?
      ↓
   ┌──┴──┐
   │     │
  YES    NO
   │     │
   ↓     ↓
HUMAN   PROCESS
APPROVAL
   │
   └──────┬──────┘
          ↓
     PROVIDER REFUND
          ↓
     REFUND CONFIRMED
          ↓
     UPDATE PAYMENT
          ↓
     UPDATE INVOICE
          ↓
     UPDATE LEDGER
          ↓
        AUDIT
```

---

## 29. WEBHOOK WORKFLOW

```text
PAYMENT PROVIDER
       ↓
WEBHOOK
       ↓
TLS
       ↓
SIGNATURE VALIDATION
       ↓
EVENT VALIDATION
       ↓
EVENT ID CHECK
       ↓
DUPLICATE?
   ┌───┴────┐
  YES       NO
   ↓         ↓
IGNORE      STORE
             ↓
         PROCESS EVENT
             ↓
       STATE VALIDATION
             ↓
        DOMAIN UPDATE
             ↓
       PUBLISH EVENT
             ↓
           AUDIT
```

---

## 30. PAYMENT RECONCILIATION WORKFLOW

```text
PROVIDER TRANSACTIONS
        ↕
PROVIDER REPORT
        ↕
INTERNAL TRANSACTIONS
        ↕
PAYMENT INTENTS
        ↕
INVOICES
        ↕
LEDGER
        ↓
RECONCILIATION ENGINE
        ↓
MATCH
   ┌────┴─────┐
   ↓          ↓
MATCH       MISMATCH
   ↓          ↓
RESOLVED   EXCEPTION
              ↓
         INVESTIGATION
              ↓
        HUMAN / AI REVIEW
              ↓
           RESOLUTION
              ↓
            AUDIT
```

---

## 31. AI-BASED PAYMENT MANAGEMENT

## AI-PAY-001 — Payment Analysis

AI SHALL be able to analyze authoritative payment information.

Example queries:

```text
"What were our payment failures this month?"

"Which organizations have failed payments?"

"Which payment provider has the highest failure rate?"

"How much revenue is currently unpaid?"

"How much was refunded this month?"

"Which customers are at risk of payment failure?"
```

---

## AI-PAY-002 — Payment Failure Analysis

AI MAY classify payment failure patterns.

Example:

```text
Payment Failure Analysis

Failed Payments:
420

Primary Category:
Expired payment methods

Percentage:
41%

Recommendation:
Notify affected customers before the next billing cycle.
```

---

## AI-PAY-003 — Payment Forecasting

AI MAY estimate:

```text
Expected collection
Expected failed payments
Expected churn from payment failures
Expected retry recovery
Expected refund volume
```

---

## AI-PAY-004 — Payment Anomaly Detection

AI MAY detect:

```text
Unusual payment spikes
Unusual refund activity
High payment failure rate
Provider degradation
Suspicious payment velocity
Unusual geographic activity
Unexpected transaction amounts
```

---

## AI-PAY-005 — AI Refund Recommendation

AI MAY recommend whether a refund request appears consistent with configured policy.

AI SHALL NOT independently issue high-risk refunds.

---

## AI-PAY-006 — AI Payment Investigation

AI SHALL be able to correlate:

```text
Invoice
Payment Intent
Payment Attempt
Provider Transaction
Webhook
Refund
Subscription
Customer
Audit Event
```

---

## AI-PAY-007 — AI Payment Explanation

AI SHALL provide evidence-backed explanations.

Example:

```text
Payment failed because:

1. The provider returned CARD_DECLINED.
2. Three retry attempts were already performed.
3. The customer's payment method has not been updated.
4. The invoice remains unpaid.

Recommended action:
Request a new payment method.
```

AI SHALL distinguish observed facts from predictions.

---

## 32. AI PAYMENT TOOLS

AI payment agents MAY use controlled tools:

```text
get_payment
get_payment_intent
get_payment_attempts
get_payment_history
get_payment_method_status
get_invoice_payment_status
get_failed_payments
get_refund_status
get_dispute_status
get_payment_provider_health
get_payment_failure_analysis
get_payment_forecast
get_payment_anomalies
get_reconciliation_status
create_payment_retry_request
create_refund_request
create_payment_investigation
create_dispute_review
```

High-risk mutation tools SHALL require authorization.

---

## 33. HUMAN PAYMENT OPERATIONS

## HUMAN-PAY-001 — Customer Admin

Customer Admin SHALL be able to:

```text
View payment history
Add payment methods
Remove payment methods
Set default payment method
Pay invoices
Retry eligible payments
View receipts
View refunds
```

---

## HUMAN-PAY-002 — Finance Admin

Finance Admin SHALL be able to:

```text
Review payments
Investigate failures
Approve refunds
Review disputes
Review reconciliation
Issue authorized adjustments
Monitor payment providers
```

---

## HUMAN-PAY-003 — Super Admin

Super Admin SHALL be able to:

```text
View platform payment metrics
Monitor provider health
Review payment anomalies
Review reconciliation failures
Configure provider routing
Review high-risk transactions
Review audit logs
```

---

## 34. AI + HUMAN PAYMENT WORKFLOW

```text
PAYMENT EVENT
     ↓
PAYMENT GATEWAY
     ↓
AUTHORITATIVE DATA
     ↓
AI ANALYSIS
     ↓
RECOMMENDATION
     ↓
RISK CLASSIFICATION
     ↓
┌──────────────────────┐
│ Low Risk             │
│ → Automated Policy   │
└──────────┬───────────┘
           ↓
      Authorized Action

OR

┌──────────────────────┐
│ High Risk            │
│ → Human Approval     │
└──────────┬───────────┘
           ↓
       Human Review
           ↓
      Authorized Action
           ↓
          Audit
```

---

## 35. AI FINANCIAL SAFETY

AI SHALL NOT independently:

```text
Change payment amount
Change invoice total
Modify payment credentials
Access raw card information
Bypass payment authentication
Disable fraud controls
Issue unrestricted refunds
Modify financial ledger records
Delete payment transactions
Delete payment audit records
Override reconciliation
Change provider credentials
Disable payment security
Bypass authorization
```

---

## 36. PAYMENT SECURITY REQUIREMENTS

## SEC-PAY-001

All payment APIs SHALL require authentication.

## SEC-PAY-002

All payment operations SHALL enforce tenant isolation.

## SEC-PAY-003

Payment mutations SHALL require authorization.

## SEC-PAY-004

Sensitive payment data SHALL never be logged.

## SEC-PAY-005

Provider webhook signatures SHALL be verified.

## SEC-PAY-006

Webhook replay attacks SHALL be prevented.

## SEC-PAY-007

Payment mutations SHALL use idempotency.

## SEC-PAY-008

Payment provider credentials SHALL be encrypted and managed through secure secrets infrastructure.

## SEC-PAY-009

Administrative refunds SHALL be audited.

## SEC-PAY-010

High-value refunds SHALL require approval.

## SEC-PAY-011

Payment-method data SHALL be tokenized where possible.

## SEC-PAY-012

Access to payment operations SHALL follow least privilege.

## SEC-PAY-013

Payment identifiers SHALL not expose sensitive provider secrets.

## SEC-PAY-014

Sensitive payment information SHALL be redacted from logs and telemetry.

---

## 37. FRAUD AND RISK REQUIREMENTS

The system SHALL support risk signals:

```text
Payment velocity
Account velocity
Failed payment count
Refund velocity
Transaction amount
Historical behavior
Device information
IP reputation
Geographic anomalies
Provider risk signals
```

The risk engine SHALL support:

```text
LOW_RISK
MEDIUM_RISK
HIGH_RISK
BLOCKED
```

---

## 38. RATE LIMITING

Payment APIs SHALL support rate limits.

Example:

```text
Create Payment
→ strict rate limit

Confirm Payment
→ strict rate limit

Refund Payment
→ very strict rate limit

Payment Method Update
→ strict rate limit
```

---

## 39. OBSERVABILITY

The platform SHALL expose metrics including:

```text
payments_created_total
payments_succeeded_total
payments_failed_total
payments_canceled_total

payment_authorizations_total
payment_captures_total

refunds_requested_total
refunds_completed_total
refunds_failed_total

payment_retries_total
payment_retry_success_total
payment_retry_failure_total

payment_webhooks_received_total
payment_webhooks_verified_total
payment_webhooks_rejected_total
payment_webhooks_duplicate_total

payment_reconciliation_total
payment_reconciliation_failure_total

payment_disputes_total

payment_processing_latency
provider_response_latency
provider_error_rate
payment_failure_rate
payment_success_rate
```

---

## 40. PROVIDER HEALTH MONITORING

The system SHALL monitor:

```text
Provider Availability
Latency
Error Rate
Authorization Rate
Capture Rate
Refund Rate
Webhook Delay
Webhook Failure Rate
Rate Limits
```

---

## 41. PROVIDER FAILOVER

Where multiple providers are configured, SalesGenie MAY support controlled provider failover.

Failover SHALL consider:

```text
Currency
Payment Method
Region
Provider Health
Transaction Type
Tenant Configuration
Risk Policy
```

Failover SHALL never create duplicate payment charges.

---

## 42. PAYMENT LEDGER INTEGRATION

The Payment Gateway SHALL integrate with a financial ledger.

Example:

```text
Payment Captured
       ↓
Debit:
Payment Clearing / Cash

Credit:
Accounts Receivable
```

Refunds SHALL produce corresponding ledger entries.

---

## 43. PAYMENT-INVOICE CONSISTENCY

The system SHALL ensure:

```text
Invoice Outstanding Amount
=
Invoice Total
-
Payments Applied
-
Credits Applied
-
Refund Adjustments
```

The exact accounting model SHALL be implemented by the financial ledger service.

---

## 44. SUBSCRIPTION CONSISTENCY

Payment success SHALL be propagated to Subscription Management.

Example:

```text
Payment Succeeded
       ↓
Billing Event
       ↓
Subscription Service
       ↓
Subscription Active
```

Payment failure SHALL propagate according to subscription dunning policy.

---

## 45. METERED BILLING CONSISTENCY

Metered usage SHALL follow:

```text
Usage
 ↓
Meter
 ↓
Rated Usage
 ↓
Invoice
 ↓
Payment
```

The Payment Gateway SHALL never independently calculate metered consumption.

---

## 46. PAYMENT NOTIFICATIONS

The notification subsystem SHALL support:

```text
Payment Successful
Payment Failed
Payment Requires Authentication
Payment Retry Scheduled
Payment Retry Failed
Invoice Due
Invoice Overdue
Payment Method Expiring
Refund Completed
Refund Failed
Dispute Created
```

Notification channels MAY include:

```text
Email
In-App
Slack
Microsoft Teams
Webhook
SMS
```

---

## 47. AUDIT REQUIREMENTS

Every payment mutation SHALL generate an audit event containing:

```text
audit_id
tenant_id
actor_type
actor_id
action
resource_type
resource_id
previous_state
new_state
timestamp
request_id
correlation_id
ip_address
user_agent
reason
approval_id
```

---

## 48. PAYMENT APPROVAL WORKFLOW

High-risk operations SHALL support:

```text
REQUESTED
 ↓
RISK_CHECK
 ↓
APPROVAL_REQUIRED
 ↓
HUMAN_REVIEW
 ↓
APPROVED / REJECTED
 ↓
EXECUTION
 ↓
AUDIT
```

Potential high-risk operations:

```text
Large Refund
Manual Payment Adjustment
Manual Capture
Provider Change
High-Value Transaction
Bulk Refund
Payment Policy Change
```

---

## 49. BULK OPERATIONS

Authorized administrators MAY perform controlled bulk operations.

Examples:

```text
Retry Failed Payments
Update Payment Policies
Review Failed Transactions
Generate Payment Reports
```

Bulk refunds SHALL require strict authorization and approval.

---

## 50. PAYMENT REPORTING

The system SHALL provide:

```text
Total Payments
Successful Payments
Failed Payments
Pending Payments
Refunds
Disputes
Payment Volume
Payment Success Rate
Payment Failure Rate
Average Transaction Value
Revenue Collected
Outstanding Amount
Recovery Rate
Provider Performance
```

---

## 51. FINANCIAL REPORTING DIMENSIONS

Reports SHALL support:

```text
Tenant
Organization
Subscription
Plan
Currency
Provider
Payment Method
Country
Region
Date
Product
Invoice
Customer
```

---

## 52. PAYMENT EXPORT

Authorized users SHALL be able to export:

```text
Payments
Refunds
Disputes
Provider Transactions
Reconciliation Results
Payment Attempts
```

Formats:

```text
CSV
JSON
PDF
```

---

## 53. PAYMENT DATA RETENTION

The platform SHALL define retention policies for:

```text
Payment Intents
Transactions
Refunds
Disputes
Provider Webhooks
Audit Events
Reconciliation Records
Payment Attempts
Risk Assessments
```

Financial records SHALL be retained according to applicable legal, accounting, contractual, and compliance requirements.

---

## 54. FAILURE RECOVERY

The system SHALL recover safely from:

```text
Provider Timeout
Network Failure
Database Failure
Event Bus Failure
Webhook Failure
Application Crash
Provider Outage
Duplicate Request
Duplicate Webhook
Partial Transaction
```

---

## 55. UNKNOWN PAYMENT STATE

If the provider result is ambiguous:

```text
REQUEST SENT
    ↓
TIMEOUT
    ↓
UNKNOWN
```

SalesGenie SHALL NOT automatically assume failure.

The system SHALL retrieve provider state before retrying to prevent duplicate charges.

---

## 56. PAYMENT TIMEOUT WORKFLOW

```text
PAYMENT REQUEST
      ↓
PROVIDER
      ↓
TIMEOUT
      ↓
UNKNOWN STATE
      ↓
QUERY PROVIDER
      ↓
┌───────────────┬───────────────┐
↓               ↓               ↓
SUCCEEDED      FAILED          UNKNOWN
↓               ↓               ↓
FINALIZE       RETRY POLICY     ESCALATE
```

---

## 57. TEST REQUIREMENTS

## Unit Tests

The system SHALL test:

```text
Payment amount validation
Currency validation
Payment state transitions
Idempotency
Refund calculation
Refund limits
Retry classification
Failure classification
Authorization
Tenant isolation
Provider routing
Webhook verification
```

---

## Integration Tests

The system SHALL test:

```text
Billing → Payment Gateway
Subscription → Payment Gateway
Invoice → Payment Gateway
Metering → Billing → Payment Gateway
Payment Gateway → Provider
Provider → Webhook
Payment → Ledger
Payment → Reconciliation
Payment → Notification
```

---

## Failure Tests

The system SHALL test:

```text
Provider timeout
Provider outage
Duplicate request
Duplicate webhook
Out-of-order webhook
Webhook signature failure
Network interruption
Database failure
Event bus failure
Unknown payment state
Partial refund
Repeated refund
Payment retry failure
```

---

## Security Tests

The system SHALL test:

```text
IDOR
Tenant escape
RBAC bypass
Privilege escalation
Webhook forgery
Replay attacks
Payment tampering
Amount tampering
Currency tampering
Idempotency bypass
Refund abuse
API abuse
Credential leakage
Sensitive-data logging
```

---

## AI Tests

AI payment systems SHALL test:

```text
Payment hallucination
Incorrect payment explanation
Wrong invoice attribution
Wrong tenant access
Unauthorized refund
Unauthorized payment modification
Fraud-analysis hallucination
Incorrect forecast
Prompt injection
Tool abuse
Privilege escalation
Sensitive payment-data disclosure
```

---

## 58. FINANCIAL INVARIANTS

SalesGenie SHALL guarantee:

```text
1. A payment belongs to exactly one tenant.

2. A payment cannot be captured more than once.

3. A payment cannot be refunded beyond the refundable amount.

4. A duplicate request cannot create a duplicate payment.

5. A duplicate webhook cannot create duplicate financial effects.

6. A payment amount cannot be controlled by the frontend.

7. A finalized invoice cannot be silently changed by the payment layer.

8. A payment cannot be applied to an unauthorized invoice.

9. A payment currency cannot silently change.

10. A payment method cannot be exposed across tenants.

11. Provider credentials cannot be exposed to users.

12. Unknown provider states cannot be blindly retried.

13. Every refund has an identifiable actor.

14. Every high-risk refund has an approval trail.

15. Every payment mutation is auditable.

16. Every provider transaction is traceable internally.

17. Every internal payment is reconcilable against the provider.

18. AI cannot bypass authorization.

19. AI cannot directly modify the financial ledger.

20. AI cannot independently issue unrestricted refunds.

21. Financial state is determined by authoritative backend services.

22. Payment success and invoice state remain consistent.

23. Payment failure cannot incorrectly mark an invoice as paid.

24. Payment records cannot be silently deleted.

25. Reconciliation detects financial discrepancies.
```

---

## 59. FAANG-LEVEL PAYMENT ARCHITECTURE

```text
                         ┌───────────────────────┐
                         │      SalesGenie UI    │
                         └───────────┬───────────┘
                                     │
                                     ↓
                         ┌───────────────────────┐
                         │      API Gateway      │
                         └───────────┬───────────┘
                                     │
                                     ↓
                         ┌───────────────────────┐
                         │  Payment Orchestrator │
                         └───────────┬───────────┘
                                     │
             ┌───────────────────────┼────────────────────────┐
             ↓                       ↓                        ↓
     ┌──────────────┐       ┌────────────────┐       ┌───────────────┐
     │ Risk Engine  │       │ Billing Service│       │ Invoice Svc   │
     └──────┬───────┘       └───────┬────────┘       └───────┬───────┘
            │                       │                        │
            └───────────────────────┼────────────────────────┘
                                    ↓
                         ┌───────────────────────┐
                         │ Payment Gateway Core  │
                         └───────────┬───────────┘
                                     │
                         ┌───────────┴───────────┐
                         ↓                       ↓
                ┌─────────────────┐      ┌─────────────────┐
                │ Provider Adapter│      │ Provider Adapter│
                │       A         │      │       B         │
                └────────┬────────┘      └────────┬────────┘
                         │                        │
                         ↓                        ↓
                ┌─────────────────┐      ┌─────────────────┐
                │ Payment Provider │      │ Payment Provider │
                │       A         │      │       B         │
                └─────────────────┘      └─────────────────┘

Cross-Cutting:

┌──────────────┐
│ Event Bus    │
└──────────────┘

┌──────────────┐
│ Audit        │
└──────────────┘

┌──────────────┐
│ Ledger       │
└──────────────┘

┌──────────────┐
│ Reconciliation│
└──────────────┘

┌──────────────┐
│ Monitoring   │
└──────────────┘

┌──────────────┐
│ AI Guardrail │
└──────────────┘
```

---

## 60. END-TO-END PAYMENT WORKFLOW

```text
CUSTOMER
   ↓
INVOICE
   ↓
PAYMENT REQUEST
   ↓
AUTHENTICATION
   ↓
AUTHORIZATION
   ↓
AMOUNT VALIDATION
   ↓
CURRENCY VALIDATION
   ↓
RISK CHECK
   ↓
IDEMPOTENCY CHECK
   ↓
PAYMENT INTENT
   ↓
PROVIDER ADAPTER
   ↓
PAYMENT PROVIDER
   ↓
AUTHENTICATION / CHALLENGE
   ↓
AUTHORIZATION
   ↓
CAPTURE
   ↓
WEBHOOK
   ↓
WEBHOOK VERIFICATION
   ↓
PAYMENT STATE UPDATE
   ↓
INVOICE UPDATE
   ↓
SUBSCRIPTION UPDATE
   ↓
LEDGER UPDATE
   ↓
NOTIFICATION
   ↓
RECONCILIATION
   ↓
AUDIT
```

---

## 61. PAYMENT + SUBSCRIPTION + METERED BILLING

```text
USER
 ↓
SUBSCRIPTION
 ↓
PLAN
 ↓
RESOURCE USAGE
 ↓
METERING
 ↓
PRICING
 ↓
INVOICE
 ↓
PAYMENT INTENT
 ↓
PAYMENT GATEWAY
 ↓
PAYMENT PROVIDER
 ↓
SUCCESS / FAILURE
 ↓
┌─────────────────────────┐
│                         │
SUCCESS                 FAILURE
│                         │
↓                         ↓
Invoice Paid           Retry Engine
│                         ↓
Subscription Active   Recovery
│                         ↓
Entitlements          Paid / Past Due
│
↓
Usage Continues
```

---

## 62. AI PAYMENT OPERATIONS WORKFLOW

```text
PAYMENT EVENT
      ↓
AUTHORITATIVE PAYMENT DATA
      ↓
AI FINANCE AGENT
      ↓
ANALYSIS
      ↓
RISK CLASSIFICATION
      ↓
RECOMMENDATION
      ↓
┌─────────────────────┐
│                     │
LOW RISK            HIGH RISK
│                     │
↓                     ↓
AUTOMATED POLICY    HUMAN REVIEW
│                     │
└──────────┬──────────┘
           ↓
AUTHORIZED SERVICE
           ↓
PAYMENT OPERATION
           ↓
AUDIT
           ↓
RECONCILIATION
```

---

## 63. ENTERPRISE PAYMENT REQUIREMENTS

Enterprise customers SHALL support:

```text
Multiple Billing Entities
Multiple Payment Methods
Multiple Currencies
Custom Payment Terms
Purchase Orders
Manual Invoicing
Net Payment Terms
Payment Approval Workflows
Department Cost Allocation
Cost Centers
Spending Limits
Payment Policies
Custom Refund Policies
Custom Provider Routing
```

Where offline/manual payment methods are supported, they SHALL still be represented in the internal payment and ledger model.

---

## 64. PAYMENT APPROVAL MATRIX

Example:

```text
Refund < $100
→ Customer Admin

Refund $100–$1,000
→ Finance Admin

Refund > $1,000
→ Finance Admin + Approval

Bulk Refund
→ Finance Admin + Super Admin Approval

Provider Configuration
→ Super Admin

Financial Policy Change
→ Super Admin + Audit
```

Exact limits SHALL be tenant-configurable.

---

## 65. PRODUCTION ACCEPTANCE CRITERIA

The Payment Gateway SHALL be considered production-ready when:

* [ ] Provider abstraction exists.
* [ ] Provider adapters exist.
* [ ] Payment intents exist.
* [ ] Payment transactions exist.
* [ ] Payment state machine is enforced.
* [ ] Payment amount is server-authoritative.
* [ ] Currency validation is implemented.
* [ ] Idempotency is implemented.
* [ ] Duplicate payment prevention is implemented.
* [ ] Payment-method tokenization is implemented.
* [ ] PCI scope is minimized.
* [ ] Payment confirmation is implemented.
* [ ] Authorization is implemented.
* [ ] Capture is implemented.
* [ ] Cancellation is implemented.
* [ ] Refunds are implemented.
* [ ] Partial refunds are implemented.
* [ ] Refund limits are enforced.
* [ ] Subscription payments are supported.
* [ ] Metered billing payments are supported.
* [ ] Invoice payments are supported.
* [ ] Payment retries are implemented.
* [ ] Failed-payment classification exists.
* [ ] Dunning integration exists.
* [ ] Webhook verification exists.
* [ ] Webhook idempotency exists.
* [ ] Webhook replay protection exists.
* [ ] Payment reconciliation exists.
* [ ] Provider health monitoring exists.
* [ ] Fraud/risk controls exist.
* [ ] Payment velocity controls exist.
* [ ] Multi-currency support exists.
* [ ] Tax integration exists.
* [ ] Credit application exists.
* [ ] Payment notifications exist.
* [ ] Payment audit logging exists.
* [ ] AI payment analysis exists.
* [ ] AI payment safety controls exist.
* [ ] Human approval exists for high-risk operations.
* [ ] Tenant isolation is tested.
* [ ] Security testing is implemented.
* [ ] Failure recovery is tested.
* [ ] Unknown payment states are safely handled.
* [ ] Financial invariants are enforced.
* [ ] Provider transactions are reconcilable.
* [ ] Payment records are immutable/auditable.
* [ ] Super Admin monitoring exists.
* [ ] Enterprise payment controls exist.

---

## 66. FINAL REQUIREMENT

SalesGenie's Payment Gateway SHALL act as the authoritative orchestration layer between:

```text
Customer
   ↓
Billing
   ↓
Invoice
   ↓
Payment Gateway
   ↓
Payment Provider
   ↓
Payment
   ↓
Ledger
   ↓
Reconciliation
   ↓
Audit
```

The canonical architecture SHALL be:

```text
                    SALES GENIE
                         │
       ┌─────────────────┼──────────────────┐
       ↓                 ↓                  ↓
 Subscription        Metering           Billing
       │                 │                  │
       └─────────────────┼──────────────────┘
                         ↓
                      Invoice
                         ↓
                 Payment Intent
                         ↓
                  Risk Evaluation
                         ↓
                Payment Orchestrator
                         ↓
                Provider Abstraction
                         ↓
              ┌──────────┴──────────┐
              ↓                     ↓
        Provider A             Provider B
              │                     │
              └──────────┬──────────┘
                         ↓
                     Payment
                         ↓
                      Ledger
                         ↓
                 Reconciliation
                         ↓
                      Audit
```

AI-assisted payment operations SHALL follow:

```text
AI
 ↓
Authorized Payment Tool
 ↓
Authoritative Payment Data
 ↓
AI Analysis
 ↓
Recommendation
 ↓
Risk Evaluation
 ↓
Human Approval When Required
 ↓
Authorized Payment Service
 ↓
Payment Operation
 ↓
Audit
 ↓
Reconciliation
```

The Payment Gateway SHALL never trust frontend payment amounts, AI-generated financial values, client-side subscription state, client-side usage values, or unverified provider callbacks as authoritative financial truth.

The **Billing Service remains responsible for billing obligations**, the **Metering Service remains responsible for measured consumption**, the **Pricing Engine remains responsible for pricing**, the **Invoice Service remains responsible for invoice generation**, the **Payment Gateway remains responsible for payment orchestration**, the **Ledger remains responsible for financial accounting records**, and the **Reconciliation Service remains responsible for detecting and resolving discrepancies**.

No AI agent, frontend client, workflow, MCP server, integration, webhook, API client, or external service SHALL be permitted to bypass authentication, authorization, payment validation, idempotency, fraud controls, ledger controls, audit requirements, or reconciliation mechanisms.
