# SalesGenie — Tax Management Requirements

**Document:** `tax_management.md`  
**Product:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Requirement Level:** FAANG / Enterprise Grade  
**Scope:** Tax configuration, tax determination, tax calculation, tax exemptions, VAT/GST/sales-tax handling, jurisdiction management, tax validation, tax reporting, tax-inclusive/exclusive pricing, tax IDs, AI-assisted tax operations, human approval, auditability, and integration with billing/invoice/payment systems.

---

## 1. Purpose

The Tax Management subsystem shall provide a secure, configurable, auditable, multi-tenant tax-management platform for determining and applying applicable taxes to:

- Subscriptions
- Usage-based billing
- Metered billing
- One-time charges
- Add-ons
- Credits
- Discounts
- Invoices
- Refunds
- Credit notes
- Debit notes

The subsystem shall support both automated AI-assisted tax operations and human-controlled financial governance.

The system shall be designed so that tax rules can evolve independently from the core billing engine.

---

## 2. Actors

## 2.1 Human Actors

### H-01 — End User

May:

- View applicable taxes
- View tax breakdowns
- Provide tax information
- Provide tax identification numbers
- Submit exemption information
- Request tax corrections

---

### H-02 — Organization Owner

May:

- Configure organization tax information
- Add business tax IDs
- Configure billing address
- Submit exemption documentation
- View tax calculations
- View tax history

---

### H-03 — Billing Administrator

May:

- Configure billing tax settings
- Review tax calculations
- Investigate tax discrepancies
- Approve tax-related adjustments
- Manage tax configuration within authorized scope

---

### H-04 — Finance Administrator

May:

- Manage tax policies
- Review tax reports
- Reconcile tax amounts
- Approve tax overrides
- Manage tax adjustments
- Export tax records

---

### H-05 — Tax Administrator

May:

- Configure jurisdictions
- Configure tax rules
- Configure tax rates
- Configure tax categories
- Validate tax IDs
- Manage exemption policies
- Approve tax overrides
- Review tax audit records

---

### H-06 — Support Agent

May:

- View customer tax status
- Explain tax calculations
- Submit tax correction requests

Support agents shall not directly modify tax calculations.

---

### H-07 — Sales Agent

May:

- View customer tax status when required for sales workflows
- Collect customer tax information
- Initiate tax-information collection workflows

---

### H-08 — Super Admin

May:

- Configure global tax policies
- Manage supported jurisdictions
- Manage tax providers
- Review tenant tax configuration
- Investigate tax anomalies
- Access platform-wide tax audit information

---

### H-09 — Compliance Auditor

May:

- Read tax records
- Review tax calculations
- Review tax configuration history
- Review tax overrides
- Review exemption evidence
- Export audit data

Auditors shall have read-only permissions.

---

## 3. AI Actors

## 3.1 AI Tax Assistant

The AI Tax Assistant shall:

- Explain tax calculations
- Explain tax line items
- Identify missing tax information
- Detect potential tax inconsistencies
- Assist with tax configuration
- Assist with tax-document classification
- Answer customer tax questions

The AI shall not independently make legally consequential tax determinations unless explicitly authorized by policy.

---

## 3.2 AI Tax Analyst

The AI Tax Analyst shall:

- Detect tax anomalies
- Compare tax rates
- Identify unusual jurisdiction changes
- Detect inconsistent tax treatment
- Analyze tax trends
- Identify missing tax IDs
- Identify potentially invalid exemption claims

---

## 3.3 AI Compliance Agent

The AI Compliance Agent shall:

- Monitor tax-policy compliance
- Identify configuration conflicts
- Detect potentially outdated tax rules
- Recommend human review
- Identify missing audit evidence

---

## 3.4 AI Tax Reconciliation Agent

The AI Tax Reconciliation Agent shall:

- Compare calculated tax with invoiced tax
- Compare invoices with payment records
- Identify tax discrepancies
- Recommend reconciliation actions

---

## 4. User Requirements

## UR-001 — Tax Transparency

Users shall be able to see applicable taxes on invoices.

---

## UR-002 — Tax Breakdown

Invoices shall display tax information including, where applicable:

- Tax name
- Tax type
- Tax rate
- Taxable amount
- Tax amount
- Jurisdiction

---

## UR-003 — Tax Identification

Organizations shall be able to provide:

- VAT ID
- GST ID
- Sales tax ID
- Business tax ID
- Other supported tax identifiers

---

## UR-004 — Billing Address

Users shall be able to maintain billing information required for tax determination.

---

## UR-005 — Tax Jurisdiction

The system shall determine applicable tax jurisdiction from authoritative billing/customer data.

---

## UR-006 — Tax Exemption

Eligible organizations shall be able to submit tax exemption information.

---

## UR-007 — Exemption Status

Users shall be able to view whether an exemption is:

- Pending
- Under review
- Approved
- Rejected
- Expired
- Revoked

---

## UR-008 — Tax History

Authorized users shall be able to view historical tax calculations.

---

## UR-009 — Tax Corrections

Users shall be able to request correction of potentially incorrect tax charges.

---

## UR-010 — Tax Explanation

Users shall be able to ask the AI Tax Assistant why a tax was applied.

---

## UR-011 — Tax Estimate

The billing interface may provide an estimated tax amount before invoice finalization.

Estimated tax shall be clearly distinguished from finalized tax.

---

## UR-012 — Tax-Inclusive Pricing

The system shall support tax-inclusive pricing where configured.

---

## UR-013 — Tax-Exclusive Pricing

The system shall support tax-exclusive pricing where configured.

---

## UR-014 — Tax Notifications

Users shall receive notifications when material tax-related changes affect billing.

---

## 5. AI-Based User Requirements

## AI-UR-001 — Intelligent Tax Explanation

The AI shall explain:

- Why tax was applied
- Which jurisdiction was used
- Which tax category was selected
- Which rate was applied
- How taxable amount was calculated

---

## AI-UR-002 — Missing Information Detection

The AI shall identify missing information that may prevent accurate tax determination.

Examples:

- Missing billing country
- Missing state/province
- Missing postal code
- Missing tax ID
- Missing exemption certificate

---

## AI-UR-003 — Tax Anomaly Detection

The AI shall identify:

- Unexpected tax-rate changes
- Unusual tax amounts
- Inconsistent tax treatment
- Unexpected jurisdiction changes
- Tax calculation discrepancies

---

## AI-UR-004 — Tax Configuration Recommendation

The AI may recommend configuration changes.

Recommendations shall require human approval where they affect financial outcomes.

---

## AI-UR-005 — Tax Exemption Assistance

The AI may classify submitted exemption documentation and recommend:

- Valid
- Invalid
- Expired
- Missing information
- Human review required

---

## AI-UR-006 — Tax ID Assistance

The AI may identify potentially invalid tax identifiers and recommend verification.

---

## AI-UR-007 — Tax Reconciliation

The AI shall assist finance teams in identifying tax discrepancies between:

- Billing records
- Invoice records
- Payment records
- Tax-provider results

---

## AI-UR-008 — AI Explainability

AI tax recommendations shall include:

- Reason
- Evidence
- Source data
- Confidence
- Applicable policy
- Recommended action

---

## 6. System Requirements

## SR-001 — Multi-Tenant Tax Isolation

Tax configuration and customer tax data shall be isolated by tenant.

---

## SR-002 — Tax Rule Versioning

Tax rules shall be versioned.

Historical invoices shall reference the exact tax-rule version used during calculation.

---

## SR-003 — Effective Dates

Tax rules shall support:

- Effective-from date
- Effective-to date

The system shall use the correct rule based on the applicable transaction date.

---

## SR-004 — Jurisdiction Hierarchy

The system shall support hierarchical tax jurisdictions.

Example:

```text
Country
  └── State / Province
       └── County / District
            └── City
                 └── Local Jurisdiction
```

---

## SR-005 — Tax Rate Versioning

Tax rates shall be versioned and effective-dated.

---

## SR-006 — Tax Category

Products and services shall be associated with tax categories.

Examples:

```text
SAAS
DIGITAL_SERVICE
AI_SERVICE
CONSULTING
SOFTWARE
STORAGE
VOICE_SERVICE
API_USAGE
OTHER
```

---

## SR-007 — Tax Determination Engine

The system shall determine applicable tax based on:

* Customer location
* Billing address
* Service location where applicable
* Product/service tax category
* Tax registration
* Exemption status
* Transaction date
* Tax jurisdiction
* Applicable tax policy

---

## SR-008 — Tax Calculation Engine

The calculation engine shall calculate:

```text
Taxable Amount
×
Applicable Tax Rate
=
Tax Amount
```

Complex tax rules shall be represented through configurable tax rules rather than hard-coded business logic.

---

## SR-009 — Decimal Precision

Tax calculations shall use deterministic fixed-precision decimal arithmetic.

---

## SR-010 — Rounding Policy

The system shall support configurable tax rounding policies.

Examples:

* Per-line-item rounding
* Invoice-level rounding
* Jurisdiction-level rounding

---

## SR-011 — Tax-Inclusive Calculation

For tax-inclusive prices, the system shall calculate the tax component without incorrectly increasing the customer's stated gross price.

---

## SR-012 — Tax-Exclusive Calculation

For tax-exclusive prices, the system shall add applicable taxes to the taxable amount.

---

## SR-013 — Tax Exemption

The system shall support configurable exemption rules.

---

## SR-014 — Exemption Evidence

The system shall store references to exemption documentation where required.

---

## SR-015 — Exemption Expiration

The system shall automatically identify expired exemptions.

---

## SR-016 — Tax ID Validation

The system shall support tax-ID validation through configured authoritative or approved external providers.

---

## SR-017 — Tax Provider Abstraction

The platform shall expose a provider abstraction layer.

Example:

```text
SalesGenie Tax Engine
        ↓
Tax Provider Interface
        ├── Provider A
        ├── Provider B
        ├── Provider C
        └── Internal Rules
```

The core billing system shall not depend directly on one tax provider.

---

## SR-018 — Provider Failover

Where multiple providers are configured, the system shall support controlled failover.

---

## SR-019 — Tax Calculation Snapshot

Every finalized invoice shall retain the tax calculation result used to produce the invoice.

---

## SR-020 — Tax Auditability

Every tax calculation shall be traceable to:

* Input data
* Tax rules
* Tax rates
* Jurisdiction
* Tax provider response where applicable
* Calculation timestamp
* Rule version

---

## SR-021 — Tax Override

Manual tax overrides shall be supported only through explicit authorization.

---

## SR-022 — Override Reason

Every tax override shall require a reason.

---

## SR-023 — Override Audit

Every override shall create an immutable audit event.

---

## SR-024 — No Silent Tax Mutation

Finalized tax amounts shall not be silently modified.

Corrections shall use:

* Credit notes
* Debit notes
* Adjustments
* Replacement invoices

---

## SR-025 — Tax Data Encryption

Sensitive tax information shall be encrypted at rest and in transit.

---

## SR-026 — RBAC

Tax configuration and tax operations shall be protected by role-based and policy-based access control.

---

## SR-027 — Separation of Duties

High-risk tax changes shall support separation of duties.

---

## SR-028 — Approval Workflow

Tax configuration changes may require approval based on:

* Jurisdiction
* Tax rate
* Organization
* Financial impact
* Administrative policy

---

## SR-029 — Event-Driven Architecture

Tax changes shall produce domain events.

---

## SR-030 — Tax Event Idempotency

Repeated processing of the same tax event shall not produce duplicate financial effects.

---

## 7. Supported Tax Concepts

The system should be extensible to support:

* VAT
* GST
* Sales tax
* Use tax
* Digital service tax
* Local taxes
* Regional taxes
* Federal taxes
* State taxes
* County taxes
* Municipal taxes
* Withholding tax where applicable
* Tax exemptions
* Reverse charge
* Zero-rated transactions
* Reduced rates
* Standard rates
* Tax-inclusive pricing
* Tax-exclusive pricing

Exact applicability shall depend on jurisdiction and SalesGenie's tax policy.

---

## 8. Functional Requirements

## FR-001 — Create Tax Profile

The system shall create a tax profile for an organization.

---

## FR-002 — Update Tax Profile

Authorized users shall be able to update tax information.

---

## FR-003 — Retrieve Tax Profile

Authorized services shall be able to retrieve tax information.

---

## FR-004 — Validate Billing Address

The system shall validate required billing-location fields.

---

## FR-005 — Validate Tax ID

The system shall validate supported tax identifiers.

---

## FR-006 — Store Tax ID Status

Tax IDs shall support statuses such as:

```text
UNVERIFIED
VERIFYING
VALID
INVALID
EXPIRED
SUSPENDED
```

---

## FR-007 — Determine Jurisdiction

The system shall determine the applicable tax jurisdiction.

---

## FR-008 — Determine Tax Category

The system shall determine the applicable tax category for the billed item.

---

## FR-009 — Retrieve Tax Rules

The tax engine shall retrieve applicable rules using:

* Jurisdiction
* Tax category
* Transaction date
* Customer tax status
* Exemption status

---

## FR-010 — Calculate Tax

The system shall calculate applicable tax amounts.

---

## FR-011 — Calculate Multiple Taxes

The system shall support multiple applicable taxes on a transaction.

---

## FR-012 — Tax Rate Application

The system shall apply the correct effective tax rate.

---

## FR-013 — Tax Rounding

The system shall apply configured rounding rules consistently.

---

## FR-014 — Tax Exemption Application

The system shall apply approved exemptions.

---

## FR-015 — Reverse Charge

The system shall support reverse-charge tax treatment where configured.

---

## FR-016 — Zero-Rated Transactions

The system shall support zero-rated transactions.

---

## FR-017 — Reduced Tax Rates

The system shall support reduced tax rates.

---

## FR-018 — Tax-Inclusive Pricing

The system shall extract applicable tax from tax-inclusive prices.

---

## FR-019 — Tax-Exclusive Pricing

The system shall calculate additional tax for tax-exclusive prices.

---

## FR-020 — Tax Line Items

The invoice system shall receive structured tax line items.

---

## FR-021 — Tax Summary

The system shall generate a tax summary for every finalized invoice.

---

## FR-022 — Tax Evidence

The system shall associate applicable tax evidence with the transaction.

---

## FR-023 — Tax Recalculation

The system shall support controlled tax recalculation before invoice finalization.

---

## FR-024 — Post-Finalization Correction

Post-finalization tax corrections shall use controlled financial adjustment mechanisms.

---

## FR-025 — Tax Credit

The system shall support tax credits associated with eligible credit notes.

---

## FR-026 — Tax Refund

The system shall calculate applicable tax components for refunds.

---

## FR-027 — Partial Refund Tax

Partial refunds shall correctly allocate refundable tax amounts.

---

## FR-028 — Tax Adjustment

Authorized users shall be able to create tax adjustments.

---

## FR-029 — Tax Override

Authorized tax administrators shall be able to apply manual tax overrides.

---

## FR-030 — Override Validation

The system shall validate whether an override is permitted before applying it.

---

## 9. Tax Determination Workflow

```text
Customer / Organization
        ↓
Billing Information
        ↓
Tax Profile
        ↓
Tax ID Validation
        ↓
Location Validation
        ↓
Service / Product Classification
        ↓
Jurisdiction Resolution
        ↓
Tax Rule Selection
        ↓
Tax Rate Resolution
        ↓
Exemption / Special Treatment
        ↓
Tax Calculation
        ↓
Rounding
        ↓
Tax Validation
        ↓
Invoice Tax Lines
        ↓
Finalized Tax Snapshot
```

---

## 10. AI + Human Tax Workflow

```text
Transaction
    ↓
Deterministic Tax Engine
    ↓
Tax Result
    ↓
AI Tax Analysis
    ↓
 ┌───────────────┴────────────────┐
 ↓                                ↓
Normal                         Anomaly
 ↓                                ↓
Automatic Processing             AI Recommendation
 ↓                                ↓
Invoice                         Human Review
                                   ↓
                            Approve / Reject
                                   ↓
                              Final Tax Result
```

---

## 11. Human Tax Administration Workflow

```text
Tax Administrator
       ↓
Create / Modify Tax Rule
       ↓
Validation
       ↓
Impact Analysis
       ↓
Approval Required?
   ┌───┴────┐
   ↓        ↓
  No       Yes
   ↓        ↓
Publish   Finance Approval
             ↓
           Publish
             ↓
      Effective-Date Activation
```

---

## 12. Tax Rule Management

Tax rules shall support:

```text
rule_id
tenant_id
jurisdiction_id
tax_category
tax_type
rate
calculation_method
rounding_method
inclusive_exclusive_mode
exemption_conditions
reverse_charge
effective_from
effective_to
priority
status
version
created_by
approved_by
created_at
updated_at
```

---

## 13. Tax Jurisdiction Requirements

Each jurisdiction should support:

```text
jurisdiction_id
parent_jurisdiction_id
country_code
region_code
county_code
city_code
postal_code_rules
tax_authority
status
effective_from
effective_to
```

The jurisdiction model shall support hierarchical inheritance.

---

## 14. Tax Profile Requirements

Each organization tax profile should support:

```text
tax_profile_id
organization_id
legal_name
billing_country
billing_region
billing_city
billing_postal_code
billing_address
tax_ids
tax_residency
exemption_status
exemption_reference
exemption_expiry
tax_inclusive_preference
verification_status
created_at
updated_at
```

---

## 15. Tax Calculation Request

The tax engine shall accept structured calculation requests containing:

```text
transaction_id
organization_id
customer_id
transaction_date
currency
billing_location
service_location
tax_ids
tax_exemption_status
line_items
tax_categories
prices
discounts
credits
metadata
```

---

## 16. Tax Calculation Response

The tax engine shall return:

```text
calculation_id
transaction_id
jurisdiction
taxable_amount
tax_lines
total_tax
currency
rounding_adjustment
exemption_applied
reverse_charge_applied
tax_rule_versions
provider_reference
calculated_at
```

---

## 17. Tax Line Item Requirements

Each tax line shall support:

```text
tax_line_id
invoice_id
invoice_line_item_id
tax_type
tax_name
jurisdiction
tax_rate
taxable_amount
tax_amount
currency
exemption_code
reverse_charge
tax_rule_version
```

---

## 18. Tax Provider Integration

External tax providers shall be accessed through a standardized interface.

The interface shall support:

```text
calculate_tax()
validate_tax_id()
validate_address()
retrieve_tax_rate()
retrieve_jurisdiction()
validate_exemption()
```

Provider responses shall be normalized into SalesGenie's internal tax model.

---

## 19. External Provider Failure

If an external tax provider fails, the system shall:

1. Detect the failure.
2. Record the provider error.
3. Determine whether a safe fallback exists.
4. Apply fallback according to policy.
5. Mark the calculation appropriately.
6. Notify operators where required.
7. Retry transient failures.
8. Avoid producing an invalid financial result.

The system shall never silently use stale tax data when policy prohibits it.

---

## 20. Tax Validation Requirements

Before invoice finalization, the system shall validate:

* Tax jurisdiction
* Tax category
* Tax rate
* Taxable amount
* Tax exemption
* Tax ID
* Tax calculation
* Tax rounding
* Currency
* Tax-rule version
* Effective date

---

## 21. Tax Reconciliation Requirements

The system shall reconcile:

```text
Billing Tax
     ↕
Invoice Tax
     ↕
Payment Tax
     ↕
Tax Provider Result
     ↕
Tax Reporting Records
```

Any mismatch shall be recorded and investigated according to policy.

---

## 22. Tax Reporting Requirements

Authorized finance users shall be able to generate:

* Tax collected reports
* Tax by jurisdiction
* Tax by organization
* Tax by product
* Tax by subscription
* Tax by billing period
* Tax by currency
* Exemption reports
* Reverse-charge reports
* Refund tax reports
* Credit-note tax reports
* Tax adjustment reports

---

## 23. Tax Reporting Dimensions

Reports should support:

```text
country
region
jurisdiction
tax_type
tax_category
organization
plan
product
billing_period
currency
tax_rate
exemption_status
```

---

## 24. Tax Export Requirements

Authorized users shall be able to export tax records in:

* CSV
* JSON
* PDF
* Accounting-compatible formats

Exports shall respect tenant and RBAC boundaries.

---

## 25. Invoice Integration

Tax Management shall integrate with Invoice Management.

The invoice shall contain:

```text
Subtotal
- Discounts
- Credits
= Taxable Amount
+ Tax
+ Fees
= Total
```

Tax calculations shall be linked to the invoice and individual line items where applicable.

---

## 26. Subscription Integration

Tax Management shall integrate with Subscription Management for:

* New subscriptions
* Renewals
* Upgrades
* Downgrades
* Proration
* Cancellations
* Add-ons

---

## 27. Usage-Based Billing Integration

Tax Management shall support taxation of usage-based charges such as:

* AI tokens
* API requests
* Conversations
* Messages
* Workflow executions
* Voice minutes
* Document processing
* Storage
* Lead generation
* Tool executions

---

## 28. Payment Integration

Tax Management shall integrate with Payment Processing for:

* Tax-inclusive payment totals
* Tax refunds
* Partial refunds
* Payment reconciliation
* Tax-related transaction metadata

---

## 29. Refund Requirements

When a refund occurs, the system shall:

1. Identify original tax.
2. Determine refundable tax.
3. Apply configured tax-refund policy.
4. Create refund tax records.
5. Link refund to original invoice.
6. Maintain audit history.

---

## 30. Credit Note Requirements

Credit notes shall support:

* Original invoice reference
* Original tax amount
* Credited taxable amount
* Credited tax amount
* Jurisdiction
* Tax rule version
* Reason
* Issuer
* Approval record

---

## 31. Debit Note Requirements

Debit notes shall support:

* Original invoice reference
* Additional taxable amount
* Additional tax
* Jurisdiction
* Tax rule version
* Reason
* Approval record

---

## 32. API Requirements

## POST `/api/v1/tax/calculate`

Calculate tax for a transaction.

---

## POST `/api/v1/tax/validate`

Validate a tax calculation.

---

## GET `/api/v1/tax/profile`

Retrieve the authorized organization's tax profile.

---

## PUT `/api/v1/tax/profile`

Update tax profile.

---

## POST `/api/v1/tax/ids/validate`

Validate a tax identifier.

---

## GET `/api/v1/tax/jurisdictions`

Retrieve supported jurisdictions.

---

## GET `/api/v1/tax/rules`

Retrieve authorized tax rules.

---

## POST `/api/v1/tax/rules`

Create a tax rule.

---

## PUT `/api/v1/tax/rules/{rule_id}`

Create a new version or modify a non-effective rule according to policy.

---

## POST `/api/v1/tax/rules/{rule_id}/publish`

Publish an approved tax rule.

---

## POST `/api/v1/tax/exemptions`

Submit an exemption.

---

## POST `/api/v1/tax/exemptions/{id}/approve`

Approve an exemption.

---

## POST `/api/v1/tax/exemptions/{id}/reject`

Reject an exemption.

---

## GET `/api/v1/tax/reports`

Generate tax reports.

---

## GET `/api/v1/tax/audit`

Retrieve authorized tax audit records.

---

## 33. Event Requirements

The system shall publish events such as:

```text
tax.profile.created
tax.profile.updated
tax.id.submitted
tax.id.validation_started
tax.id.validated
tax.id.invalid
tax.jurisdiction.resolved
tax.calculation.requested
tax.calculation.completed
tax.calculation.failed
tax.rule.created
tax.rule.updated
tax.rule.approved
tax.rule.published
tax.rule.expired
tax.exemption.submitted
tax.exemption.approved
tax.exemption.rejected
tax.exemption.expired
tax.override.requested
tax.override.approved
tax.override.rejected
tax.override.applied
tax.anomaly.detected
tax.reconciliation.failed
tax.reconciliation.completed
```

---

## 34. Idempotency Requirements

Tax calculations shall support idempotency.

The same transaction and calculation request shall not produce inconsistent tax results when retried under the same rule/version context.

---

## 35. Caching Requirements

The system may cache:

* Jurisdiction metadata
* Tax rates
* Tax rules
* Address validation results
* Tax-ID validation results

Cached values shall have explicit TTL and invalidation policies.

Tax calculations shall never use expired data when policy requires real-time determination.

---

## 36. Security Requirements

## SEC-001

Tax data shall be protected by server-side authorization.

## SEC-002

Tenant isolation shall be enforced for tax profiles.

## SEC-003

Tax IDs shall be protected as sensitive business information.

## SEC-004

Tax documents shall require authorized access.

## SEC-005

Tax configuration changes shall be audited.

## SEC-006

Tax overrides shall require elevated permissions.

## SEC-007

Tax-rule publication shall support approval controls.

## SEC-008

External tax-provider credentials shall be stored in secure secret management.

## SEC-009

Tax APIs shall implement rate limiting.

## SEC-010

All sensitive communication shall use encrypted transport.

---

## 37. AI Security Requirements

## AI-SEC-001

AI shall never bypass tenant authorization.

## AI-SEC-002

AI shall never expose another organization's tax information.

## AI-SEC-003

AI shall not invent tax rates.

## AI-SEC-004

AI shall not fabricate tax laws or jurisdiction rules.

## AI-SEC-005

AI-generated tax recommendations shall be clearly distinguishable from authoritative tax calculations.

## AI-SEC-006

High-impact tax changes shall require human approval.

---

## 38. AI Guardrails

The AI shall distinguish between:

```text
Authoritative Tax Result
        vs.
AI Recommendation
        vs.
AI Explanation
        vs.
Human Override
```

The authoritative tax engine shall remain the source of truth for finalized billing calculations.

---

## 39. Human Approval Requirements

Human approval shall be configurable for:

* Tax-rule publication
* Tax-rate changes
* Tax overrides
* Tax exemptions
* Large tax adjustments
* Manual jurisdiction changes
* AI tax recommendations
* AI-detected tax anomalies
* Provider failover decisions

---

## 40. Tax Override Workflow

```text
Tax Override Request
        ↓
Validate Permission
        ↓
Validate Financial Impact
        ↓
Record Reason
        ↓
AI Risk Analysis
        ↓
Approval Policy
        ↓
Human Approval
        ↓
Apply Override
        ↓
Create Audit Event
        ↓
Recalculate Tax
        ↓
Update Billing / Invoice
```

---

## 41. Tax Anomaly Detection

The system shall identify:

* Sudden tax-rate changes
* Unexpected tax jurisdiction changes
* Missing taxes
* Excess taxes
* Duplicate taxes
* Tax calculation mismatches
* Incorrect exemption application
* Expired exemption usage
* Invalid tax IDs
* Tax provider discrepancies

---

## 42. AI Tax Anomaly Workflow

```text
Tax Calculation
      ↓
Rule-Based Validation
      ↓
AI Anomaly Detection
      ↓
Risk Score
      ↓
 ┌──────────────┴──────────────┐
 ↓                             ↓
Low Risk                    High Risk
 ↓                             ↓
Continue                   Human Review
                               ↓
                         Investigate
                               ↓
                        Correct / Approve
```

---

## 43. Tax Data Retention

The system shall retain tax records according to configurable legal, financial, and organizational retention policies.

Retention shall include:

* Tax calculations
* Tax rule versions
* Tax rates
* Tax IDs
* Exemption records
* Tax documents
* Audit records
* Provider responses

---

## 44. Audit Requirements

Every material tax operation shall produce an audit record containing:

```text
audit_id
organization_id
actor_id
actor_type
action
resource_type
resource_id
timestamp
request_id
correlation_id
previous_state
new_state
reason
tax_rule_version
approval_reference
```

Audit records shall be append-only.

---

## 45. Observability Requirements

The platform shall monitor:

## Technical Metrics

* Tax calculation latency
* Tax API latency
* Provider latency
* Provider failure rate
* Tax calculation error rate
* Queue depth
* Retry count
* Cache hit rate

## Financial Metrics

* Total tax calculated
* Tax by jurisdiction
* Tax discrepancies
* Tax overrides
* Tax refunds
* Tax adjustments
* Exempt transactions

## AI Metrics

* AI anomaly detection rate
* False-positive rate
* Human override rate
* Recommendation acceptance rate
* AI tax-explanation accuracy
* AI hallucination rate

---

## 46. SLO Requirements

Recommended initial targets:

| Metric                           |    Target |
| -------------------------------- | --------: |
| Tax API availability             | >= 99.95% |
| Tax calculation p95 latency      |  < 500 ms |
| Tax profile API p95 latency      |  < 300 ms |
| Tax validation p95 latency       |  < 500 ms |
| Provider failure detection       |  < 10 sec |
| Unauthorized tax access          |         0 |
| Duplicate tax financial effects  |         0 |
| Silent tax mutations             |         0 |
| Finalized invoice tax corruption |         0 |

---

## 47. Reliability Requirements

The tax system shall tolerate:

* Service crashes
* Network failures
* External provider outages
* Duplicate events
* Delayed events
* Out-of-order events
* Database failures
* Provider timeouts
* Worker failures

The system shall preserve deterministic tax results for the same:

```text
transaction
+
tax-rule version
+
tax-rate version
+
tax-input snapshot
```

---

## 48. Disaster Recovery Requirements

The system shall support:

* Automated backups
* Point-in-time recovery
* Tax-rule recovery
* Audit-log recovery
* Tax-document recovery
* Configuration recovery
* Disaster-recovery testing

Recommended targets:

```text
RPO <= 5 minutes
RTO <= 30 minutes
```

---

## 49. Compliance Requirements

The system shall provide configurable support for applicable:

* Tax regulations
* VAT requirements
* GST requirements
* Sales-tax requirements
* Digital-service tax requirements
* Invoice requirements
* Record-retention requirements
* Tax-exemption requirements
* Audit requirements

The architecture shall avoid hard-coding jurisdiction-specific assumptions into the core billing engine.

---

## 50. Tax Policy Versioning

Tax policies shall be versioned.

Example:

```text
Tax Policy v1
    ↓
Tax Policy v2
    ↓
Tax Policy v3
```

Historical transactions shall retain references to the policy version that governed their calculation.

---

## 51. Tax Rule Conflict Resolution

If multiple rules apply, the system shall use deterministic precedence.

Example:

```text
Specific Product Rule
        ↓
Jurisdiction Rule
        ↓
Regional Rule
        ↓
Country Rule
        ↓
Default Rule
```

The exact precedence shall be configurable.

---

## 52. Tax Calculation Invariants

The system shall validate:

```text
Total Tax
=
Sum(All Applicable Tax Lines)
```

and:

```text
Invoice Total
=
Taxable Amount
+
Total Tax
+
Applicable Non-Tax Charges
-
Credits
-
Discounts
```

Exact financial treatment shall depend on the billing model.

---

## 53. Tax Exemption Lifecycle

```text
NOT_SUBMITTED
      ↓
SUBMITTED
      ↓
UNDER_REVIEW
   ┌──┴────┐
   ↓       ↓
APPROVED  REJECTED
   ↓
ACTIVE
   ↓
EXPIRING
   ↓
EXPIRED
```

Revocation shall be supported.

---

## 54. Tax ID Lifecycle

```text
UNVERIFIED
    ↓
VERIFYING
    ↓
 ┌──┴────┐
 ↓       ↓
VALID   INVALID
 ↓
ACTIVE
 ↓
EXPIRED / REVOKED
```

---

## 55. Tax Rule Lifecycle

```text
DRAFT
  ↓
VALIDATING
  ↓
REVIEW
  ↓
APPROVED
  ↓
SCHEDULED
  ↓
ACTIVE
  ↓
EXPIRED
  ↓
ARCHIVED
```

---

## 56. Tax Provider Health Management

The system shall track provider health using:

* Availability
* Latency
* Error rate
* Timeout rate
* Response validity
* Rate-limit status

Provider health shall influence controlled routing and failover.

---

## 57. Accounting Integration Requirements

Tax Management shall support exports or integration with accounting systems.

Export records should contain:

```text
invoice_number
transaction_date
customer
jurisdiction
tax_type
tax_rate
taxable_amount
tax_amount
currency
exemption_status
tax_id
credit_note_reference
refund_reference
```

---

## 58. Workflow Automation Requirements

Tax events shall be usable as SalesGenie workflow triggers.

Examples:

```text
Tax ID Invalid
    ↓
Notify Customer
    ↓
Create Support Task

Tax Exemption Expiring
    ↓
Notify Billing Admin
    ↓
Send Renewal Request

Tax Anomaly Detected
    ↓
AI Investigation
    ↓
Human Review
    ↓
Tax Correction Workflow

Tax Provider Failure
    ↓
Provider Health Check
    ↓
Failover
    ↓
Notify Operations
```

---

## 59. AI + Workflow Integration

The AI system shall be able to trigger approved workflows for:

* Tax ID verification
* Missing billing information
* Exemption renewal
* Tax anomaly investigation
* Human tax review
* Customer notification
* Finance reconciliation

AI-triggered workflows shall execute under the same RBAC and policy controls as human-triggered workflows.

---

## 60. API Authorization Requirements

Each tax API operation shall evaluate:

```text
Authenticated User
        +
Tenant
        +
Role
        +
Permission
        +
Resource Ownership
        +
Policy
        +
Risk Level
```

before execution.

---

## 61. Rate Limiting

The platform shall implement separate rate limits for:

* Tax calculation
* Tax profile APIs
* Tax-ID validation
* Tax reports
* Tax-rule management
* Administrative operations

---

## 62. Data Integrity Requirements

The system shall guarantee:

* Tax-rule version integrity
* Tax-rate version integrity
* Invoice-tax consistency
* Jurisdiction consistency
* Exemption consistency
* Tax-ID state consistency
* Financial precision
* Audit-log integrity

---

## 63. Testing Requirements

The Tax Management subsystem shall include:

## Unit Tests

* Tax calculations
* Tax rounding
* Tax-inclusive calculations
* Tax-exclusive calculations
* Exemptions
* Reverse charge
* Zero rates
* Reduced rates
* Rule precedence

## Integration Tests

* Billing integration
* Invoice integration
* Payment integration
* Tax-provider integration
* Subscription integration
* Usage-meter integration

## Security Tests

* Tenant isolation
* RBAC
* Privilege escalation
* API authorization
* Tax document access
* Tax override permissions

## AI Tests

* Tax grounding
* Hallucination detection
* Recommendation correctness
* Anomaly detection
* Authorization compliance

## Failure Tests

* Provider outage
* Provider timeout
* Duplicate events
* Network failure
* Database failure
* Worker crash
* Retry storms

---

## 64. Acceptance Criteria

## AC-001

The system shall determine tax using the correct effective tax rule.

## AC-002

Tax calculations shall use deterministic decimal arithmetic.

## AC-003

The same transaction shall not receive duplicate tax effects due to retries.

## AC-004

Finalized invoice tax shall be immutable.

## AC-005

Historical invoices shall retain their original tax-rule version.

## AC-006

Tax exemptions shall only apply when approved and active.

## AC-007

Expired exemptions shall not automatically continue to reduce tax.

## AC-008

Tax IDs shall maintain explicit verification status.

## AC-009

Tax overrides shall require authorization.

## AC-010

Tax overrides shall require an auditable reason.

## AC-011

AI shall not directly modify finalized tax records.

## AC-012

AI tax recommendations shall provide evidence and confidence.

## AC-013

Unauthorized users shall not access tax information.

## AC-014

Cross-tenant tax access shall be impossible.

## AC-015

Tax provider failures shall be detected and handled according to policy.

## AC-016

Tax calculation failures shall not silently produce incorrect invoices.

## AC-017

Tax refunds shall correctly associate with original transactions.

## AC-018

Credit notes shall correctly reverse applicable tax amounts.

## AC-019

Tax reports shall reconcile with invoice tax records.

## AC-020

Every material tax operation shall be auditable.

## AC-021

Tax rules shall support effective dates.

## AC-022

Tax rates shall support versioning.

## AC-023

Tax calculations shall preserve their input and rule snapshots.

## AC-024

AI-generated explanations shall use authoritative tax and invoice data.

## AC-025

Human approval shall be enforced for configured high-risk tax operations.

---

## 65. Definition of Done

Tax Management shall be considered production-ready only when:

* Tax determination is deterministic.
* Tax calculations are financially accurate.
* Tax rules are versioned.
* Tax rates are effective-dated.
* Jurisdictions are modeled correctly.
* Tax profiles are tenant-isolated.
* Tax IDs can be validated.
* Exemptions are governed and auditable.
* Tax overrides are authorization-controlled.
* Finalized tax data is immutable.
* Tax refunds and credits are correctly handled.
* External tax providers are abstracted.
* Provider failures are recoverable.
* AI tax operations are grounded.
* AI cannot bypass authorization.
* Human approval workflows are operational.
* Tax reporting is available.
* Tax reconciliation is available.
* Audit logging is complete.
* Monitoring and alerting are operational.
* Disaster recovery has been tested.
* Security testing has passed.
* Financial and tax invariants are continuously validated.

---

## 66. FAANG-Level Design Principles

1. **Tax correctness over convenience.**
2. **Deterministic tax calculation.**
3. **Immutable finalized financial records.**
4. **Version every tax rule and rate.**
5. **Use effective dates for regulatory changes.**
6. **Treat tax determination as a first-class domain service.**
7. **Separate tax determination from invoice rendering.**
8. **Separate tax policy from application logic.**
9. **Enforce tenant isolation at every service boundary.**
10. **Use least-privilege authorization.**
11. **Require human approval for high-impact tax overrides.**
12. **Never allow AI to silently change authoritative tax records.**
13. **Ground AI recommendations in authoritative tax data.**
14. **Make every financial tax decision auditable.**
15. **Design for jurisdictional extensibility.**
16. **Do not hard-code one country's tax model into the platform.**
17. **Use idempotency for all distributed tax operations.**
18. **Design for provider outages and degraded operation.**
19. **Preserve historical tax calculation snapshots.**
20. **Make tax reconciliation observable.**
21. **Use fixed-precision financial arithmetic.**
22. **Maintain separation of duties for sensitive tax operations.**
23. **Treat tax exemptions as governed financial credentials.**
24. **Make tax configuration changes versioned and reviewable.**
25. **Use event-driven architecture for tax lifecycle changes.**
26. **Keep the authoritative tax engine deterministic even when AI is involved.**
27. **Never silently mutate historical tax records.**
28. **Prefer explicit correction documents over destructive updates.**
29. **Design tax APIs for UI, workflows, AI agents, and integrations simultaneously.**
30. **Build compliance, security, observability, and auditability into the architecture from day one.**
