# SalesGenie — SMS Notifications Requirements

**Document:** `sms_notifications.md`  
**Product:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Requirement Type:** User Requirements, System Requirements, Functional Requirements  
**Scope:** AI + Human SMS Notification Platform  
**Architecture:** Enterprise Microservices + Event-Driven + Multi-Agent AI + Omnichannel  
**Scale Target:** 10M+ users, 500K+ concurrent conversations, millions of notification events  
**Requirement Level:** Enterprise / FAANG-level

---

## 1. Purpose

The SMS Notification subsystem shall provide a secure, reliable, scalable, tenant-isolated, AI-assisted and human-controlled SMS notification infrastructure for SalesGenie.

The subsystem shall support:

- Transactional SMS
- Authentication SMS
- Security SMS
- Sales SMS
- Support SMS
- Billing SMS
- Workflow SMS
- Operational SMS
- Alert SMS
- Reminder SMS
- Escalation SMS
- AI-generated SMS
- Human-authored SMS
- Scheduled SMS
- Recurring SMS
- Bulk SMS
- SMS campaigns
- SMS delivery tracking
- SMS provider failover
- SMS suppression
- SMS deduplication
- SMS throttling
- SMS rate limiting
- SMS personalization
- SMS localization
- SMS analytics
- SMS compliance
- SMS auditing
- Two-way SMS where enabled
- Human-to-customer SMS communication
- AI-to-customer SMS communication with governance

---

## 2. Scope

## 2.1 In Scope

- SMS notification generation
- SMS templates
- Template versioning
- Template approval
- Recipient resolution
- Phone-number validation
- Country-code handling
- Sender identity
- SMS routing
- SMS scheduling
- Recurring SMS
- SMS batching
- SMS deduplication
- SMS throttling
- SMS rate limiting
- SMS queueing
- SMS retries
- Dead-letter queues
- SMS provider abstraction
- Provider failover
- Delivery tracking
- Failure tracking
- Carrier-related status processing where supported
- Opt-in/opt-out management
- Consent management integration
- Suppression lists
- AI-generated SMS
- AI personalization
- AI prioritization
- AI send-time optimization
- AI frequency optimization
- AI response generation
- Human approval
- Human-authored SMS
- Two-way SMS
- SMS conversation management
- SMS security
- SMS privacy
- SMS compliance
- SMS analytics
- SMS observability
- SMS audit logging
- Cost monitoring
- Country-specific routing and policy controls

---

## 3. Actors

## 3.1 Human Actors

### End User

Receives SalesGenie SMS notifications.

### Customer

Receives sales, support, transactional, security, or workflow SMS messages.

### Sales Agent

Uses SMS notifications for:

- Leads
- Prospects
- Opportunities
- Follow-ups
- Customer interactions
- Deal alerts
- AI recommendations

### Sales Manager

Receives:

- High-value opportunity alerts
- Pipeline alerts
- Revenue alerts
- Team notifications
- Escalation alerts

### Support Agent

Receives:

- Ticket alerts
- Customer replies
- SLA warnings
- Escalations
- Assignment notifications

### Support Manager

Receives:

- Queue alerts
- SLA breach alerts
- Escalation notifications
- Critical customer issues

### Customer Success Manager

Receives:

- Customer health alerts
- Renewal alerts
- Churn-risk alerts
- Expansion opportunities

### Organization Admin

Manages organization-level SMS policies.

### Super Admin

Manages platform-wide SMS infrastructure.

### Security Officer

Receives security-related SMS alerts where configured.

### Compliance Officer

Reviews SMS compliance and audit events.

### Developer / Engineer

Receives critical operational alerts.

---

## 4. AI Actors

## 4.1 SMS Intelligence Agent

Determines whether SMS is an appropriate notification channel.

## 4.2 SMS Classification Agent

Classifies notifications by:

- Category
- Priority
- Severity
- Urgency
- Audience

## 4.3 SMS Personalization Agent

Personalizes SMS content using authorized context.

## 4.4 SMS Summarization Agent

Converts complex events into concise SMS notifications.

## 4.5 SMS Optimization Agent

Optimizes:

- Send time
- Frequency
- Content
- Recipient selection
- Channel selection

## 4.6 SMS Routing Agent

Determines:

- Provider
- Sender
- Route
- Country-specific configuration

## 4.7 SMS Suppression Agent

Detects redundant or low-value notifications.

## 4.8 SMS Compliance Agent

Validates SMS against applicable policies.

## 4.9 SMS Safety Agent

Detects:

- Sensitive data exposure
- Unauthorized content
- Malicious URLs
- Prompt injection
- Social engineering patterns
- Unsafe instructions
- Policy violations

## 4.10 AI SMS Response Agent

For two-way SMS, the AI may:

- Understand incoming messages
- Classify intent
- Retrieve authorized context
- Generate responses
- Execute permitted actions
- Escalate to humans

---

## 5. User Requirements

## UR-001 — SMS Notifications

Users shall receive SMS notifications for events relevant to their role, permissions, preferences, and configured policies.

## UR-002 — SMS Preferences

Users shall be able to configure eligible SMS notification preferences.

Preferences shall support:

- Notification category
- Frequency
- Priority
- Quiet hours
- Language
- Time zone
- Phone number
- SMS enablement

## UR-003 — Category Preferences

Users shall be able to configure categories including:

- Sales
- Support
- Security
- Billing
- Workflow
- System
- AI
- Operational
- Reminder
- Alert

## UR-004 — Transactional SMS

Users shall receive mandatory transactional SMS where configured.

Examples:

- Verification code
- MFA code
- Password recovery
- Account security notification
- Critical billing notification

## UR-005 — Security SMS

Users shall receive security notifications for relevant account events.

Examples:

- New login
- Suspicious login
- Password change
- MFA change
- Account lock
- Account recovery
- API credential change

## UR-006 — Sales SMS

Sales users shall receive configurable notifications for:

- New lead
- Qualified lead
- High-intent lead
- Lead score change
- Lead assignment
- Deal creation
- Deal stage change
- Deal risk
- Deal won
- Deal lost
- Follow-up reminders

## UR-007 — Support SMS

Support users shall receive:

- New ticket
- Ticket assignment
- Customer reply
- SLA warning
- SLA breach
- Escalation
- Resolution notification

## UR-008 — Billing SMS

Users shall receive:

- Payment confirmation
- Payment failure
- Subscription change
- Trial expiration
- Usage threshold
- Budget alert

## UR-009 — Workflow SMS

Users shall receive:

- Workflow completion
- Workflow failure
- Workflow approval
- Workflow rejection
- Workflow timeout
- Workflow escalation

## UR-010 — Critical Alerts

Authorized users shall be able to receive urgent SMS alerts for critical events.

## UR-011 — SMS Scheduling

Authorized users shall be able to schedule eligible SMS notifications.

## UR-012 — SMS Cancellation

Authorized users shall be able to cancel eligible scheduled SMS messages.

## UR-013 — SMS History

Authorized users shall be able to view SMS notification history.

## UR-014 — SMS Search

Authorized users shall be able to search eligible SMS notification records.

## UR-015 — SMS Localization

SMS content shall support the user's configured language where available.

## UR-016 — Timezone Awareness

Scheduled SMS shall respect the recipient's configured timezone where applicable.

## UR-017 — SMS Opt-Out

Recipients shall be able to opt out of eligible SMS communications.

## UR-018 — Mandatory SMS Protection

Users shall not be able to disable legally or operationally mandatory messages where policy requires delivery.

## UR-019 — SMS Actions

SMS messages may contain secure links to:

- View lead
- View deal
- View ticket
- Approve
- Reject
- Assign
- Escalate
- Resolve
- View invoice
- Authenticate

## UR-020 — Secure Actions

SMS actions shall require server-side authorization.

---

## 6. AI User Requirements

## AI-UR-001 — AI SMS Generation

Authorized AI agents shall be able to generate SMS content for approved notification types.

## AI-UR-002 — AI Personalization

AI shall personalize SMS using authorized data.

## AI-UR-003 — AI Summarization

AI shall convert complex events into concise SMS messages.

Example:

```text
3 high-intent leads were detected.
2 require follow-up within 1 hour.
Open SalesGenie to review.
```

## AI-UR-004 — AI Priority Detection

AI shall identify potentially high-value or urgent notifications.

## AI-UR-005 — AI Send-Time Optimization

AI may recommend optimal delivery times for eligible notifications.

## AI-UR-006 — AI Frequency Optimization

AI may recommend reducing excessive SMS frequency.

## AI-UR-007 — AI Suppression

AI may suppress redundant eligible notifications.

## AI-UR-008 — AI Personalization

AI may personalize:

* Greeting
* Summary
* CTA
* Recommended action
* Customer context

## AI-UR-009 — AI SMS Response

For enabled two-way SMS, AI may generate customer responses.

## AI-UR-010 — AI Escalation

AI shall escalate conversations to humans when:

* Confidence is low
* Customer requests a human
* Sensitive actions are requested
* High-risk content is detected
* Business policy requires human approval
* Customer sentiment indicates escalation
* The requested action exceeds AI authority

## AI-UR-011 — AI Compliance

AI-generated SMS shall be validated against applicable communication policies.

## AI-UR-012 — No Fabrication

AI shall not fabricate:

* Deals
* Customer actions
* Financial values
* Security events
* Delivery status
* Appointments
* Tickets
* Business metrics

---

## 7. System Requirements

## SR-001 — Dedicated SMS Notification Service

SalesGenie shall provide a dedicated SMS notification service or bounded subsystem.

```text
SalesGenie Services
        ↓
Event Bus
        ↓
SMS Notification Processor
        ↓
Policy Engine
        ↓
AI SMS Intelligence
        ↓
Recipient Resolver
        ↓
Template Engine
        ↓
SMS Queue
        ↓
Provider Router
        ↓
SMS Provider
        ↓
Carrier
        ↓
Delivery Events
        ↓
Analytics + Audit
```

## SR-002 — Event-Driven Architecture

SMS notifications shall primarily be triggered through events.

## SR-003 — Asynchronous Delivery

SMS delivery shall be asynchronous.

## SR-004 — Durable Queue

SMS requests shall be persisted in durable queues before delivery.

## SR-005 — Idempotency

SMS processing shall be idempotent.

## SR-006 — Deduplication

The platform shall prevent accidental duplicate SMS delivery.

## SR-007 — Tenant Isolation

SMS data and processing shall be isolated by tenant.

## SR-008 — Organization Isolation

Organization-level SMS policies shall be isolated.

## SR-009 — RBAC

SMS operations shall enforce role-based authorization.

## SR-010 — ABAC

Fine-grained authorization shall be supported where required.

---

## 8. SMS Notification Object

Every SMS notification shall support:

```text
sms_notification_id
tenant_id
organization_id
recipient_id
recipient_phone
sender_id
notification_type
category
priority
severity
message
template_id
template_version
source_service
source_event_id
entity_type
entity_id
channel
status
provider
provider_message_id
country_code
carrier
scheduled_at
queued_at
sent_at
delivered_at
failed_at
opt_out_status
expires_at
locale
timezone
idempotency_key
correlation_id
created_at
updated_at
```

---

## 9. Functional Requirements

## 9.1 SMS Creation

## FR-001

The system shall accept SMS notification requests from authorized SalesGenie services.

## FR-002

The system shall validate SMS requests.

## FR-003

The system shall validate recipients.

## FR-004

The system shall validate tenant context.

## FR-005

The system shall generate a unique SMS notification ID.

## FR-006

The system shall classify the notification.

## FR-007

The system shall assign priority and severity.

---

## 10. SMS Categories

The platform shall support:

```text
TRANSACTIONAL
AUTHENTICATION
SECURITY
COMPLIANCE
BILLING
SALES
SUPPORT
CUSTOMER_SUCCESS
WORKFLOW
AI
SYSTEM
OPERATIONAL
ADMINISTRATIVE
REMINDER
ALERT
ESCALATION
```

---

## 11. SMS Priority

Supported levels:

```text
LOW
NORMAL
HIGH
URGENT
CRITICAL
```

Priority shall influence:

* Queue selection
* Delivery latency
* Retry policy
* Suppression
* Escalation
* Routing

---

## 12. SMS Severity

Supported levels:

```text
INFO
NOTICE
WARNING
ERROR
CRITICAL
```

---

## 13. SMS Templates

## FR-008

The system shall support reusable SMS templates.

## FR-009

Templates shall support:

* Variables
* Conditional content
* Localization
* Dynamic links
* CTA text
* Versioning

## FR-010

Templates shall be version controlled.

## FR-011

Published templates shall be immutable.

## FR-012

Template modifications shall create new versions.

## FR-013

Templates shall support approval workflows.

---

## 14. Dynamic Variables

Example:

```json
{
  "customer_name": "John",
  "deal_name": "Enterprise Renewal",
  "deal_value": 50000,
  "risk_score": 0.87
}
```

## FR-014

The template engine shall safely render dynamic values.

## FR-015

Missing variables shall not cause uncontrolled failures.

## FR-016

Untrusted data shall be safely encoded.

---

## 15. Phone Number Management

## FR-017

The system shall support international phone numbers.

## FR-018

Phone numbers shall be normalized into a canonical representation.

Example:

```text
+8801XXXXXXXXX
```

## FR-019

The platform shall validate phone-number syntax.

## FR-020

The platform shall store country information.

## FR-021

The system shall prevent unauthorized phone-number modification.

## FR-022

Phone-number changes shall be auditable.

---

## 16. Recipient Resolution

## FR-023

The platform shall resolve recipients using authorized user/customer records.

## FR-024

The system shall verify that the recipient is eligible for SMS.

## FR-025

The system shall verify applicable consent/opt-in status.

## FR-026

The system shall verify suppression status.

## FR-027

The system shall prevent unauthorized recipient targeting.

---

## 17. Sender Identity

The platform shall support:

```text
Long code
Short code
Toll-free number
Alphanumeric sender ID
Provider-specific sender identity
```

where supported by the destination country and provider.

## FR-028

Sender identities shall be verified and policy-controlled.

## FR-029

Unauthorized sender identities shall not be usable.

---

## 18. SMS Routing

## FR-030

The platform shall select an SMS provider based on:

* Tenant configuration
* Destination country
* Provider health
* Cost policy
* Rate limits
* Deliverability
* Sender availability
* Regulatory restrictions

## FR-031

Provider routing shall be configurable.

---

## 19. Provider Abstraction

The platform shall implement a provider abstraction layer.

```text
SMS Notification Service
          ↓
Provider Interface
       ↙      ↓      ↘
Provider A  Provider B  Provider C
```

## FR-032

Core SalesGenie services shall not depend directly on a specific SMS provider.

---

## 20. Provider Failover

## FR-033

The platform shall support provider failover where technically and legally permitted.

```text
Primary Provider
      ↓ failure
Secondary Provider
      ↓ failure
Tertiary Provider
```

## FR-034

Failover events shall be observable.

## FR-035

Failover shall be auditable.

## FR-036

The system shall prevent duplicate delivery caused by unsafe failover behavior.

---

## 21. SMS Queue

## FR-037

SMS requests shall enter durable queues.

## FR-038

Queues shall support priority.

Example:

```text
CRITICAL_QUEUE
HIGH_QUEUE
NORMAL_QUEUE
LOW_QUEUE
BULK_QUEUE
```

## FR-039

Bulk SMS shall not starve authentication or critical transactional SMS.

---

## 22. Retry System

## FR-040

Transient provider failures shall trigger controlled retries.

## FR-041

Retries shall use exponential backoff where appropriate.

Example:

```text
Attempt 1 → Immediate
Attempt 2 → 30 seconds
Attempt 3 → 2 minutes
Attempt 4 → 10 minutes
Attempt 5 → 30 minutes
```

## FR-042

Retry policies shall be configurable.

## FR-043

Permanent failures shall not be retried indefinitely.

---

## 23. Dead-Letter Queue

## FR-044

Messages exceeding retry limits shall enter a dead-letter queue.

## FR-045

Authorized operators shall be able to inspect failed SMS.

## FR-046

Authorized operators shall be able to retry eligible messages.

## FR-047

Dead-letter operations shall be audited.

---

## 24. SMS Deduplication

## FR-048

The platform shall detect duplicate SMS requests.

Deduplication may use:

```text
tenant_id
recipient_id
notification_type
entity_id
event_id
idempotency_key
time_window
```

## FR-049

Duplicate messages shall be suppressed according to policy.

---

## 25. SMS Aggregation

## FR-050

The system shall support aggregation of related events.

Example:

```text
20 individual lead events
          ↓
1 summarized SMS
```

## FR-051

Aggregation shall preserve relevant entity references.

---

## 26. SMS Scheduling

## FR-052

Authorized users and services shall be able to schedule SMS.

## FR-053

Scheduling shall support:

* One-time messages
* Delayed messages
* Recurring messages

## FR-054

Scheduled SMS shall respect timezone.

## FR-055

Scheduled SMS shall respect quiet hours where applicable.

## FR-056

Authorized users shall be able to cancel eligible scheduled SMS.

---

## 27. Quiet Hours

## FR-057

The platform shall support configurable quiet hours.

## FR-058

Non-critical SMS shall be deferred during quiet hours where policy permits.

## FR-059

Critical security notifications may bypass quiet hours according to policy.

---

## 28. Consent and Opt-In

## FR-060

The system shall track SMS consent/opt-in state.

Supported states may include:

```text
OPTED_IN
OPTED_OUT
PENDING
UNKNOWN
EXPIRED
REVOKED
```

## FR-061

Eligible SMS shall only be sent when applicable consent requirements are satisfied.

## FR-062

Consent changes shall be auditable.

## FR-063

Consent status shall be checked before eligible SMS delivery.

---

## 29. Opt-Out

## FR-064

The system shall support recipient opt-out.

Examples:

```text
STOP
UNSUBSCRIBE
CANCEL
END
QUIT
```

where supported by the configured provider and applicable messaging program.

## FR-065

Opt-out requests shall be processed promptly.

## FR-066

Opt-out status shall update the recipient's suppression state.

## FR-067

The system shall prevent eligible future SMS from being sent after opt-out.

## FR-068

Mandatory communications shall follow applicable legal and operational exceptions.

---

## 30. Suppression

SMS may be suppressed because of:

```text
Recipient opt-out
Consent withdrawal
Duplicate event
User preference
Notification fatigue
Invalid phone number
Carrier restriction
Provider restriction
Tenant policy
Compliance policy
Security policy
Rate limit
AI recommendation
```

---

## 31. Delivery Tracking

The system shall support:

```text
CREATED
VALIDATED
APPROVED
QUEUED
PROCESSING
SENT
DELIVERED
FAILED
RETRYING
SUPPRESSED
CANCELLED
EXPIRED
DEAD_LETTERED
```

## FR-069

Provider message IDs shall be correlated with internal SMS IDs.

## FR-070

Delivery status updates shall be idempotently processed.

---

## 32. Delivery Receipts

## FR-071

The system shall process provider delivery callbacks/webhooks where supported.

## FR-072

Webhook authenticity shall be validated.

## FR-073

Duplicate delivery callbacks shall not corrupt message state.

## FR-074

Out-of-order delivery events shall be handled safely.

---

## 33. Two-Way SMS

Where enabled, SalesGenie shall support inbound SMS.

```text
Customer SMS
     ↓
SMS Provider
     ↓
Webhook
     ↓
Inbound SMS Service
     ↓
Conversation Service
     ↓
AI / Human Agent
     ↓
Response
     ↓
SMS Provider
     ↓
Customer
```

## FR-075

Inbound SMS shall be associated with the correct tenant.

## FR-076

Inbound SMS shall be associated with the correct customer/contact where possible.

## FR-077

Inbound messages shall be persisted according to retention policies.

## FR-078

Inbound messages shall support conversation threading.

---

## 34. AI Two-Way SMS

## FR-079

AI shall classify inbound SMS intent.

Possible intents:

```text
QUESTION
REQUEST
COMPLAINT
PURCHASE_INTENT
SUPPORT_REQUEST
APPOINTMENT
OPT_OUT
SECURITY
BILLING
ESCALATION
UNKNOWN
```

## FR-080

AI shall retrieve only authorized customer context.

## FR-081

AI shall generate responses within configured policies.

## FR-082

AI shall not perform unauthorized actions.

## FR-083

AI shall escalate low-confidence interactions.

---

## 35. Human Handoff

AI shall hand conversations to humans when:

```text
Customer explicitly requests human
Low AI confidence
Sensitive request
Financial action
Account-security issue
High-value sales opportunity
Customer complaint
Legal/compliance issue
Negative sentiment
Repeated AI failure
Policy restriction
```

## FR-084

Human handoff shall preserve conversation context.

## FR-085

Human agents shall see the relevant inbound and outbound SMS history.

## FR-086

Handoff events shall be audited.

---

## 36. AI SMS Generation

## FR-087

AI shall generate SMS only for authorized notification types.

## FR-088

AI-generated messages shall pass validation before delivery.

## FR-089

AI shall reference the triggering event.

## FR-090

AI shall not invent information.

## FR-091

AI shall not disclose unauthorized information.

## FR-092

AI-generated SMS shall respect configured character limits.

---

## 37. SMS Character Optimization

## FR-093

The system shall calculate SMS length before sending.

## FR-094

The platform shall account for message segmentation where applicable.

## FR-095

The system shall warn or optimize content when a message exceeds configured limits.

## FR-096

AI may shorten messages to minimize unnecessary message segments.

---

## 38. AI Personalization

AI may personalize:

```text
Greeting
Customer name
Event summary
Recommended action
CTA
Deal context
Support context
```

## FR-097

AI personalization shall use only authorized data.

## FR-098

AI shall not expose sensitive inferred attributes.

---

## 39. AI Send-Time Optimization

## FR-099

AI may recommend optimal SMS send times.

Signals may include:

```text
Recipient timezone
Historical engagement
Historical response behavior
Notification urgency
Business hours
User preferences
Quiet hours
```

## FR-100

AI shall not delay mandatory critical notifications beyond configured limits.

---

## 40. AI Notification Fatigue

## FR-101

The system shall measure SMS frequency.

Metrics shall include:

```text
SMS per user
SMS per customer
SMS per hour
SMS per day
SMS per week
Opt-out rate
Response rate
```

## FR-102

AI may recommend:

* Aggregation
* Frequency reduction
* Suppression
* Channel change
* Digest-like summaries

## FR-103

AI shall not suppress mandatory security notifications.

---

## 41. AI SMS Safety

The safety pipeline shall detect:

```text
Prompt injection
Sensitive data exposure
Unauthorized disclosure
Malicious URLs
Social engineering
Fraud patterns
Unsafe instructions
Policy violations
Fabricated claims
```

## FR-104

High-risk AI-generated SMS shall not be automatically delivered.

## FR-105

High-risk messages shall support human review.

---

## 42. Human-Generated SMS

## FR-106

Authorized human agents shall be able to send SMS.

## FR-107

Human-authored SMS shall support:

* Recipient
* Message
* Template
* Attachments/media where supported
* Schedule
* Priority

## FR-108

Human users shall only contact recipients they are authorized to contact.

## FR-109

Mass SMS operations shall require elevated permissions.

---

## 43. Human Approval

Approval may be required based on:

```text
Recipient count
Message category
AI generation
Sensitive information
External recipients
Campaign type
Financial content
Security content
Compliance policy
Tenant policy
```

## FR-110

Approval records shall include:

```text
notification_id
approver_id
decision
reason
timestamp
```

---

## 44. AI + Human SMS Workflow

```text
Business Event
      ↓
Event Bus
      ↓
SMS Notification Processor
      ↓
Tenant Validation
      ↓
Policy Evaluation
      ↓
AI Classification
      ↓
Priority Detection
      ↓
Recipient Resolution
      ↓
Consent / Opt-In Check
      ↓
Suppression Check
      ↓
Deduplication
      ↓
Notification Fatigue Check
      ↓
Template Selection
      ↓
AI Content Generation
      ↓
Character / Segment Validation
      ↓
Security Validation
      ↓
Compliance Validation
      ↓
Human Approval?
   ↙           ↘
 YES            NO
 ↓              ↓
Human Review   Queue
 ↓
Approve/Reject
 ↓
SMS Queue
 ↓
Provider Routing
 ↓
SMS Delivery
 ↓
Delivery Receipt
 ↓
Analytics
 ↓
Audit
```

---

## 45. SMS State Machine

```text
CREATED
   ↓
VALIDATED
   ↓
APPROVED
   ↓
QUEUED
   ↓
PROCESSING
   ↓
SENT
   ↓
DELIVERED
```

Alternative states:

```text
FAILED
RETRYING
SUPPRESSED
CANCELLED
EXPIRED
DEAD_LETTERED
```

---

## 46. Secure SMS Actions

## FR-111

SMS links shall use HTTPS where applicable.

## FR-112

SMS links shall not contain permanent secrets.

## FR-113

Sensitive actions shall use short-lived authorization mechanisms.

## FR-114

Server-side authorization shall be performed for every action.

## FR-115

Sensitive actions may require re-authentication.

## FR-116

SMS action execution shall be audited.

---

## 47. Authentication SMS

The platform shall support:

```text
OTP
MFA
Login verification
Password recovery
Account verification
Security confirmation
```

## FR-117

Authentication SMS shall have strict expiration.

## FR-118

Authentication codes shall be single-use.

## FR-119

Authentication codes shall not be stored in plaintext where avoidable.

## FR-120

Authentication attempts shall be rate-limited.

---

## 48. Security SMS

Supported security events:

```text
New login
Suspicious login
Password changed
MFA enabled
MFA disabled
API key created
API key revoked
Permission changed
Role changed
Account locked
Account recovered
Potential account takeover
Security incident
```

---

## 49. Sales SMS

Supported events:

```text
New lead
Lead qualified
Lead assigned
High-intent lead
Lead score changed
Deal created
Deal stage changed
Deal at risk
Deal won
Deal lost
Follow-up due
Follow-up overdue
High-value opportunity
Pipeline threshold
Revenue milestone
```

---

## 50. Support SMS

Supported events:

```text
Ticket created
Ticket assigned
Customer replied
Priority changed
SLA warning
SLA breach
Escalation
Ticket resolved
Customer complaint
AI escalation
```

---

## 51. Billing SMS

Supported events:

```text
Payment successful
Payment failed
Invoice available
Subscription created
Subscription upgraded
Subscription downgraded
Subscription cancelled
Trial ending
Usage threshold
Budget threshold
Credit exhaustion
```

---

## 52. Workflow SMS

Supported events:

```text
Workflow started
Workflow completed
Workflow failed
Workflow paused
Workflow resumed
Workflow timeout
Workflow retry
Approval required
Approval granted
Approval rejected
```

---

## 53. SMS Attachments / Rich Messaging

Where supported by the provider and destination:

```text
MMS
Rich SMS
Media
Images
Documents
Buttons
Deep links
```

## FR-121

Unsupported rich content shall gracefully fall back to standard SMS.

## FR-122

Sensitive attachments shall require appropriate authorization.

---

## 54. Bulk SMS

Bulk SMS shall support:

```text
Batching
Queueing
Rate limiting
Throttling
Progress tracking
Failure tracking
Provider limits
Tenant limits
Campaign limits
```

## FR-123

Bulk SMS shall not block transactional SMS.

## FR-124

Bulk campaigns shall have independent resource quotas.

---

## 55. SMS Rate Limiting

Rate limits shall support:

```text
Per user
Per recipient
Per tenant
Per organization
Per provider
Per destination country
Per sender
Per notification type
Per campaign
Per API key
```

## FR-125

Rate limits shall be configurable.

---

## 56. Carrier and Country Controls

The system shall support country-aware policy evaluation.

Controls may include:

```text
Destination country
Sender availability
Provider availability
Messaging restrictions
Opt-in requirements
Content restrictions
Rate limits
Routing rules
Cost controls
```

## FR-126

The system shall reject unsupported destinations before attempting delivery.

---

## 57. SMS Cost Management

The platform shall track:

```text
Messages sent
Message segments
Provider cost
Tenant cost
Campaign cost
Country cost
Provider cost
Retry cost
Failed-message cost
```

## FR-127

The platform shall enforce configurable SMS budgets.

## FR-128

The platform shall alert authorized administrators when budgets approach thresholds.

---

## 58. SMS Analytics

The system shall calculate:

```text
SMS generated
SMS queued
SMS sent
SMS delivered
SMS failed
Delivery rate
Failure rate
Opt-out rate
Response rate
Average delivery latency
Provider latency
Retry rate
Suppression rate
AI-generated volume
Human-generated volume
AI approval rate
Human override rate
Messages per recipient
Messages per tenant
Cost per tenant
Cost per campaign
```

---

## 59. AI SMS Analytics

AI shall analyze:

```text
Response behavior
Delivery trends
Opt-out trends
Content performance
Send-time performance
Notification fatigue
Recipient engagement
Provider performance
Cost efficiency
```

AI may recommend:

```text
Change send time
Shorten content
Reduce frequency
Change provider
Change recipient targeting
Use another notification channel
```

---

## 60. Observability

The platform shall expose:

```text
SMS throughput
Queue depth
Queue latency
Processing latency
Provider latency
Delivery latency
Retry count
Dead-letter count
Failure rate
Opt-out rate
Provider health
Provider quota
AI latency
AI failure rate
Template rendering failures
Webhook processing failures
```

---

## 61. Distributed Tracing

Every SMS workflow shall support:

```text
request_id
notification_id
event_id
correlation_id
trace_id
tenant_id
provider_message_id
```

## FR-129

End-to-end SMS processing shall be traceable across microservices.

---

## 62. Multi-Tenant Requirements

## FR-130

Every SMS request shall contain tenant context.

## FR-131

Tenant authorization shall be enforced at every trust boundary.

## FR-132

Tenant SMS policies shall be isolated.

## FR-133

One tenant shall not access another tenant's SMS data.

## FR-134

Tenant-specific providers shall be supported where configured.

## FR-135

Tenant-specific sender identities shall be supported where configured.

---

## 63. Localization

## FR-136

SMS templates shall support multiple locales.

## FR-137

The platform shall select the recipient's configured language.

## FR-138

Fallback language shall be configurable.

## FR-139

AI translation shall preserve the intended meaning.

---

## 64. Privacy

## FR-140

SMS content shall follow SalesGenie's data-minimization policies.

## FR-141

Sensitive personal data shall not be unnecessarily included in SMS.

## FR-142

The platform shall support configurable retention of SMS content and metadata.

## FR-143

SMS history shall be accessible only to authorized users.

---

## 65. Sensitive Data Protection

The platform shall detect inappropriate SMS inclusion of:

```text
Passwords
Authentication tokens
API keys
Session tokens
Private credentials
Payment secrets
Highly sensitive personal information
Internal security information
```

## FR-144

Sensitive data shall be blocked or redacted according to policy.

---

## 66. AI Governance

## AI-001

AI shall not bypass SMS authorization.

## AI-002

AI shall not bypass consent requirements.

## AI-003

AI shall not bypass tenant isolation.

## AI-004

AI shall not bypass opt-out status.

## AI-005

AI shall not fabricate events.

## AI-006

AI shall not expose unauthorized data.

## AI-007

AI shall not disable mandatory security messages.

## AI-008

AI decisions shall be auditable.

## AI-009

AI-generated SMS shall be traceable to the triggering event.

## AI-010

High-risk AI SMS shall support human approval.

## AI-011

AI shall operate within deterministic platform policies.

---

## 67. Human Governance

## HUMAN-001

Authorized humans shall be able to approve AI-generated SMS.

## HUMAN-002

Authorized humans shall be able to reject AI-generated SMS.

## HUMAN-003

Authorized humans shall be able to override AI recommendations where policy permits.

## HUMAN-004

Human overrides shall be audited.

## HUMAN-005

Administrators shall be able to disable AI SMS optimization.

## HUMAN-006

Administrators shall be able to configure SMS policies.

---

## 68. SMS Audit Logging

The platform shall audit:

```text
SMS creation
SMS modification
SMS scheduling
SMS cancellation
SMS approval
SMS rejection
SMS suppression
SMS sending
SMS delivery
SMS failure
SMS retry
SMS provider failover
SMS opt-in
SMS opt-out
Consent changes
Template creation
Template modification
Template publication
AI generation
AI recommendation
AI suppression
Human approval
Human rejection
Human override
Inbound SMS
AI response
Human handoff
Administrative operations
```

---

## 69. API Requirements

Example API surface:

```text
POST   /api/v1/sms/notifications
GET    /api/v1/sms/notifications
GET    /api/v1/sms/notifications/{id}
PATCH  /api/v1/sms/notifications/{id}
DELETE /api/v1/sms/notifications/{id}

POST   /api/v1/sms/notifications/{id}/send
POST   /api/v1/sms/notifications/{id}/cancel
POST   /api/v1/sms/notifications/{id}/retry

POST   /api/v1/sms/bulk
POST   /api/v1/sms/schedule

GET    /api/v1/sms/templates
POST   /api/v1/sms/templates
GET    /api/v1/sms/templates/{id}
PATCH  /api/v1/sms/templates/{id}

GET    /api/v1/sms/preferences
PATCH  /api/v1/sms/preferences

GET    /api/v1/sms/consent
POST   /api/v1/sms/consent
DELETE /api/v1/sms/consent

POST   /api/v1/sms/opt-out

GET    /api/v1/sms/delivery/{id}
GET    /api/v1/sms/analytics

GET    /api/v1/sms/providers
GET    /api/v1/sms/health

POST   /api/v1/sms/webhooks/provider
POST   /api/v1/sms/inbound
```

---

## 70. API Security

All SMS APIs shall support:

```text
JWT authentication
RBAC
ABAC where required
Tenant authorization
Rate limiting
Input validation
Idempotency
Audit logging
Correlation IDs
Distributed tracing
Structured errors
Webhook signature validation
```

---

## 71. SMS Event Schema

Example:

```json
{
  "event_id": "evt_123",
  "event_type": "lead.high_intent",
  "tenant_id": "tenant_123",
  "organization_id": "org_123",
  "entity_type": "lead",
  "entity_id": "lead_456",
  "actor_id": "user_789",
  "timestamp": "2026-08-29T03:30:00Z",
  "payload": {
    "lead_score": 0.94,
    "conversion_probability": 0.87
  },
  "correlation_id": "corr_123"
}
```

---

## 72. SMS Request Schema

Example:

```json
{
  "recipient_id": "customer_123",
  "notification_type": "lead_high_intent",
  "category": "sales",
  "priority": "high",
  "severity": "notice",
  "template_id": "lead-high-intent-v2",
  "variables": {
    "customer_name": "John",
    "lead_score": 94
  },
  "scheduled_at": null,
  "expires_at": "2026-08-30T00:00:00Z",
  "idempotency_key": "lead_456-high-intent"
}
```

---

## 73. Inbound SMS Schema

Example:

```json
{
  "message_id": "inbound_123",
  "tenant_id": "tenant_123",
  "phone_number": "+8801XXXXXXXXX",
  "provider_message_id": "provider_456",
  "direction": "inbound",
  "message": "I want to know the price",
  "received_at": "2026-08-29T03:40:00Z",
  "correlation_id": "corr_789"
}
```

---

## 74. AI SMS Decision Pipeline

```text
Business Event
      ↓
Event Validation
      ↓
Tenant Validation
      ↓
Authorization
      ↓
SMS Relevance Detection
      ↓
Priority Prediction
      ↓
Severity Detection
      ↓
Recipient Resolution
      ↓
Consent / Opt-In Check
      ↓
Opt-Out Check
      ↓
Suppression Check
      ↓
Deduplication
      ↓
Notification Fatigue Check
      ↓
Template Selection
      ↓
AI Content Generation
      ↓
Character / Segment Optimization
      ↓
Sensitive Data Detection
      ↓
URL Validation
      ↓
Compliance Validation
      ↓
Human Approval?
      ↓
SMS Queue
      ↓
Provider Routing
      ↓
Delivery
      ↓
Delivery Receipt
      ↓
Analytics
      ↓
Audit
```

---

## 75. Two-Way AI SMS Pipeline

```text
Inbound SMS
     ↓
Webhook Validation
     ↓
Tenant Resolution
     ↓
Customer Resolution
     ↓
Opt-Out Detection
     ↓
Intent Classification
     ↓
Authentication / Authorization
     ↓
Context Retrieval
     ↓
RAG / Knowledge Retrieval
     ↓
AI Reasoning
     ↓
Safety Validation
     ↓
Policy Validation
     ↓
Confidence Evaluation
     ↓
Human Handoff?
   ↙          ↘
 YES           NO
 ↓             ↓
Human Agent   AI Response
 ↓             ↓
     SMS Provider
           ↓
        Customer
```

---

## 76. SMS Security Validation Pipeline

```text
Content Validation
      ↓
Phone Validation
      ↓
Recipient Authorization
      ↓
Sensitive Data Detection
      ↓
URL Validation
      ↓
AI Safety Validation
      ↓
Consent Validation
      ↓
Opt-Out Validation
      ↓
Compliance Validation
      ↓
Rate Limit Validation
      ↓
Final Delivery
```

---

## 77. Critical SMS Escalation

```text
CRITICAL SECURITY EVENT
        ↓
Immediate SMS
        ↓
Delivery Monitoring
        ↓
No Delivery Confirmation
        ↓
Retry
        ↓
Secondary Provider
        ↓
Alternative Notification Channel
        ↓
Human Escalation
```

---

## 78. Notification Fatigue Prevention

The system shall monitor:

```text
SMS frequency
Recipient response rate
Opt-out rate
Notification category frequency
Repeated identical notifications
AI suppression recommendations
```

AI may recommend:

```text
Aggregate
Suppress
Delay
Reduce frequency
Change channel
Escalate
```

---

## 79. Provider Health Monitoring

The system shall continuously monitor:

```text
Provider availability
API latency
Delivery latency
Error rate
Provider rejection rate
Carrier failures
Rate-limit status
Provider quota
Authentication status
```

## FR-145

Provider degradation shall trigger operational alerts.

## FR-146

Provider failures shall trigger configured failover.

---

## 80. Campaign Isolation

Bulk SMS campaigns shall be isolated from:

```text
Authentication SMS
Security SMS
Critical alerts
Billing SMS
Transactional SMS
Operational alerts
```

## FR-147

Bulk workloads shall not consume all shared SMS capacity.

---

## 81. Performance Requirements

## PERF-001

SMS notification creation shall target:

```text
P95 ≤ 200 ms
P99 ≤ 500 ms
```

excluding external provider delivery latency.

## PERF-002

Queue ingestion shall scale horizontally.

## PERF-003

SMS processing shall not block core SalesGenie transactions.

## PERF-004

Critical queues shall receive higher processing priority.

## PERF-005

Bulk SMS processing shall run independently from critical transactional SMS.

---

## 82. Scalability Requirements

The platform shall support:

```text
10M+ users
500K+ concurrent conversations
Millions of SMS notifications/hour
Large enterprise tenants
Large SMS campaigns
Billions of historical notification events
Multiple SMS providers
Global destinations
```

## SCALE-001

SMS workers shall scale horizontally.

## SCALE-002

Provider workers shall scale independently.

## SCALE-003

Tenant workloads shall be isolated.

## SCALE-004

No single tenant shall exhaust shared SMS resources.

---

## 83. Reliability Requirements

## REL-001

The platform shall provide durable SMS queues.

## REL-002

The platform shall support controlled retries.

## REL-003

The platform shall support dead-letter queues.

## REL-004

The platform shall support provider failover.

## REL-005

SMS processing shall be idempotent.

## REL-006

Duplicate transactional SMS shall be prevented.

## REL-007

Critical SMS shall have stronger delivery guarantees than informational SMS.

## REL-008

SMS subsystem failure shall not block core SalesGenie operations.

---

## 84. Disaster Recovery

The platform shall support:

```text
Queue recovery
Database recovery
Provider failover
Configuration recovery
Template recovery
Audit recovery
Cross-zone recovery
Cross-region recovery where required
```

---

## 85. Acceptance Criteria

## AC-001

Authorized services can create SMS notification requests.

## AC-002

Unauthorized services cannot send SMS.

## AC-003

Users can configure SMS preferences.

## AC-004

Recipients receive eligible transactional SMS.

## AC-005

Security SMS follows mandatory policy.

## AC-006

Eligible SMS respects applicable consent.

## AC-007

Opt-out requests are processed correctly.

## AC-008

Opted-out recipients are suppressed from eligible SMS.

## AC-009

Duplicate SMS requests are detected.

## AC-010

SMS traffic is rate-limited.

## AC-011

Bulk SMS cannot starve critical SMS.

## AC-012

SMS requests enter durable queues.

## AC-013

Transient provider failures trigger retries.

## AC-014

Permanent failures are not retried indefinitely.

## AC-015

Failed SMS enters the dead-letter queue.

## AC-016

Provider failures trigger configured failover.

## AC-017

Delivery receipts are processed correctly.

## AC-018

Duplicate provider webhooks do not corrupt message state.

## AC-019

Out-of-order provider events are handled safely.

## AC-020

Provider message IDs are correlated with internal SMS IDs.

## AC-021

Phone numbers are validated and normalized.

## AC-022

Unauthorized recipients cannot be targeted.

## AC-023

Templates support versioning.

## AC-024

Dynamic variables are safely rendered.

## AC-025

SMS character/segment limits are enforced.

## AC-026

Secure SMS links do not expose permanent secrets.

## AC-027

Sensitive actions require server-side authorization.

## AC-028

AI can generate approved SMS notifications.

## AC-029

AI-generated SMS passes safety validation.

## AC-030

AI cannot bypass tenant authorization.

## AC-031

AI cannot bypass opt-out status.

## AC-032

AI cannot bypass consent policies.

## AC-033

AI cannot fabricate business events.

## AC-034

AI cannot expose unauthorized customer data.

## AC-035

High-risk AI SMS supports human approval.

## AC-036

Human users can approve or reject AI-generated SMS.

## AC-037

Human overrides are audited.

## AC-038

AI cannot disable mandatory security SMS.

## AC-039

Scheduled SMS respects timezone.

## AC-040

Scheduled SMS respects quiet hours.

## AC-041

Critical SMS can bypass quiet hours according to policy.

## AC-042

Two-way SMS conversations can be associated with the correct customer.

## AC-043

Inbound SMS is validated.

## AC-044

Inbound SMS supports conversation threading.

## AC-045

AI can classify inbound SMS intent.

## AC-046

AI can generate authorized responses.

## AC-047

Low-confidence AI conversations are escalated to humans.

## AC-048

Human agents can take over AI conversations.

## AC-049

Conversation context is preserved during handoff.

## AC-050

Inbound and outbound SMS events are auditable.

## AC-051

SMS analytics accurately report delivery performance.

## AC-052

SMS costs are measurable.

## AC-053

Tenant-level SMS budgets can be enforced.

## AC-054

Provider health is observable.

## AC-055

Provider failures generate alerts.

## AC-056

Tenant isolation is enforced.

## AC-057

SMS history is accessible only to authorized users.

## AC-058

Sensitive information is detected and restricted.

## AC-059

End-to-end SMS workflows are traceable.

## AC-060

The SMS subsystem can recover from provider and infrastructure failures.

---

## 86. Definition of Done

The `sms_notifications` subsystem shall be considered production-ready only when:

* [ ] Dedicated SMS notification service is implemented.
* [ ] Event-driven processing is implemented.
* [ ] Durable queues are implemented.
* [ ] SMS APIs are implemented.
* [ ] Transactional SMS is implemented.
* [ ] Authentication SMS is implemented.
* [ ] Security SMS is implemented.
* [ ] Sales SMS is implemented.
* [ ] Support SMS is implemented.
* [ ] Billing SMS is implemented.
* [ ] Workflow SMS is implemented.
* [ ] Operational SMS is implemented.
* [ ] SMS templates are implemented.
* [ ] Template versioning is implemented.
* [ ] Template approval is implemented.
* [ ] Dynamic variables are implemented.
* [ ] Phone validation is implemented.
* [ ] Phone normalization is implemented.
* [ ] Recipient authorization is implemented.
* [ ] Consent validation is implemented.
* [ ] Opt-out management is implemented.
* [ ] Suppression lists are implemented.
* [ ] Deduplication is implemented.
* [ ] Rate limiting is implemented.
* [ ] Throttling is implemented.
* [ ] Priority queues are implemented.
* [ ] Retry policies are implemented.
* [ ] Dead-letter queues are implemented.
* [ ] Provider abstraction is implemented.
* [ ] Multiple provider support is implemented.
* [ ] Provider failover is implemented.
* [ ] Provider health monitoring is implemented.
* [ ] Delivery tracking is implemented.
* [ ] Delivery receipt processing is implemented.
* [ ] Webhook validation is implemented.
* [ ] Bulk SMS isolation is implemented.
* [ ] SMS scheduling is implemented.
* [ ] Recurring SMS is implemented.
* [ ] Quiet hours are implemented.
* [ ] SMS character/segment handling is implemented.
* [ ] Cost tracking is implemented.
* [ ] Country-aware routing is implemented.
* [ ] AI SMS generation is implemented.
* [ ] AI personalization is implemented.
* [ ] AI summarization is implemented.
* [ ] AI prioritization is implemented.
* [ ] AI send-time optimization is implemented.
* [ ] AI frequency optimization is implemented.
* [ ] AI suppression is implemented.
* [ ] AI safety validation is implemented.
* [ ] AI compliance validation is implemented.
* [ ] AI governance is implemented.
* [ ] Human approval is implemented.
* [ ] Human override is implemented.
* [ ] Two-way SMS is implemented where enabled.
* [ ] Inbound SMS processing is implemented.
* [ ] AI intent classification is implemented.
* [ ] AI response generation is implemented.
* [ ] Human handoff is implemented.
* [ ] Conversation context preservation is implemented.
* [ ] SMS analytics are implemented.
* [ ] Cost analytics are implemented.
* [ ] Deliverability monitoring is implemented.
* [ ] Observability is implemented.
* [ ] Distributed tracing is implemented.
* [ ] Correlation IDs are implemented.
* [ ] Audit logging is implemented.
* [ ] Multi-tenant isolation is implemented.
* [ ] Localization is implemented.
* [ ] Privacy controls are implemented.
* [ ] Sensitive-data detection is implemented.
* [ ] Secure SMS action handling is implemented.
* [ ] Disaster recovery is tested.
* [ ] Provider failover is tested.
* [ ] Duplicate delivery scenarios are tested.
* [ ] Webhook replay scenarios are tested.
* [ ] Out-of-order delivery events are tested.
* [ ] AI hallucination/fabrication defenses are tested.
* [ ] Prompt-injection defenses are tested.
* [ ] Sensitive-data leakage tests are completed.
* [ ] Consent and opt-out tests are completed.
* [ ] Tenant-isolation tests are completed.
* [ ] Load testing is completed.
* [ ] Security testing is completed.
* [ ] End-to-end SMS delivery is validated.

---

## 87. FAANG-Level Design Principles

The SalesGenie SMS Notification subsystem shall follow:

1. **Event-driven architecture**
2. **API-first design**
3. **Asynchronous processing**
4. **Durable messaging**
5. **Idempotent processing**
6. **At-least-once processing with idempotent effects**
7. **Exactly-once business effect where technically achievable**
8. **Provider abstraction**
9. **Provider failover**
10. **Tenant isolation**
11. **Zero-trust authorization**
12. **Policy-driven delivery**
13. **Consent-aware delivery**
14. **Opt-out enforcement**
15. **Notification deduplication**
16. **Notification aggregation**
17. **Notification fatigue prevention**
18. **Priority-aware queues**
19. **Critical notification escalation**
20. **Human-in-the-loop governance**
21. **AI-assisted personalization**
22. **AI-assisted prioritization**
23. **AI-assisted optimization**
24. **AI-assisted two-way communication**
25. **No AI fabrication**
26. **Sensitive-data minimization**
27. **Secure SMS actions**
28. **Country-aware routing**
29. **Cost-aware routing**
30. **Comprehensive auditability**
31. **End-to-end observability**
32. **Horizontal scalability**
33. **Fault isolation**
34. **Graceful degradation**
35. **Disaster recovery**
36. **Bulk/transactional workload isolation**
37. **Privacy by design**
38. **Security by design**
39. **Compliance by design**
40. **Deterministic controls around probabilistic AI**
41. **Human override for high-impact decisions**
42. **Continuous deliverability monitoring**
43. **Enterprise-grade governance**
44. **Secure webhook processing**
45. **Conversation-aware AI orchestration**
