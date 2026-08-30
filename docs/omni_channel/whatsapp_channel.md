# SalesGenie — WhatsApp Channel

## FAANG-Level User Requirements, System Requirements & Functional Requirements

**Project:** SalesGenie Enterprise AI Customer Support & Sales Platform
**Module:** WhatsApp Channel
**Scope:** AI + Human + Hybrid Customer Support and Sales
**Architecture:** Enterprise Multi-Tenant Microservices + Multi-Agent AI + Event-Driven
**Primary Integration:** WhatsApp Business Platform / Cloud API
**Status:** Production-Grade Requirements Specification
**Version:** 1.0

---

## 1. Purpose

The WhatsApp Channel shall provide SalesGenie with an enterprise-grade conversational communication layer for customer support, sales, lead generation, customer engagement, notifications, transactional communication, and AI-powered automation.

WhatsApp shall operate as a first-class omnichannel channel and shall integrate with:

* AI Support Agents
* AI Sales Agents
* Human Support Agents
* Human Sales Agents
* Hybrid AI + Human Support
* Conversation Management
* Ticket Management
* Customer 360
* CRM
* Knowledge Base
* RAG
* Workflow Automation
* SLA Management
* Customer Satisfaction
* Sentiment Analysis
* Conversation Intelligence
* Analytics
* Business Reports
* Sales Reports
* Marketing Reports
* Advertising Intelligence
* Revenue Analytics
* Audit and Compliance
* Notification Services

The system shall provide a unified customer journey:

```text
WhatsApp Message
        ↓
Customer Identity Resolution
        ↓
Conversation Resolution
        ↓
AI Understanding
        ↓
Intent / Sentiment / Priority
        ↓
Routing
        ↓
AI / Human / Hybrid Decision
        ↓
Knowledge Retrieval
        ↓
Response / Action
        ↓
Workflow Execution
        ↓
Resolution
        ↓
Analytics
        ↓
Business Outcome
```

---

## 2. Product Vision

SalesGenie's WhatsApp Channel shall transform WhatsApp from a basic messaging channel into an intelligent enterprise customer interaction platform.

The objective is not merely:

```text
Customer → WhatsApp → Agent
```

but:

```text
Customer
   ↓
WhatsApp
   ↓
SalesGenie Intelligence Layer
   ├── Identity
   ├── Memory
   ├── Intent
   ├── Sentiment
   ├── Context
   ├── Customer Value
   ├── AI Reasoning
   ├── Knowledge
   ├── CRM
   ├── Ticketing
   ├── Workflow
   └── Business Rules
   ↓
AI / Human / Hybrid
   ↓
Action
   ↓
Resolution / Conversion / Retention
```

---

## 3. Primary Actors

## 3.1 End Customer

The end customer shall be able to:

* Start a WhatsApp conversation.
* Reply to an existing conversation.
* Send text messages.
* Send supported media.
* Send documents.
* Send voice messages where supported.
* Send images.
* Send videos.
* Share relevant information.
* Request customer support.
* Request a human agent.
* Ask product questions.
* Request pricing.
* Request a demo.
* Track support requests.
* Receive notifications.
* Receive transactional updates.
* Interact with interactive messages.
* Select predefined options.
* Continue conversations without losing context.
* Receive multilingual responses.
* Receive personalized responses.
* Receive AI responses.
* Receive human responses.
* Move from AI to human support without restarting the conversation.

---

## 4. Human Support Agent Requirements

Human support agents shall be able to:

* View WhatsApp conversations.
* Reply to customers.
* Send media.
* Send documents.
* Use templates where applicable.
* View customer history.
* View customer profile.
* View organization information.
* View tickets.
* View previous conversations.
* View AI-generated summaries.
* View AI intent.
* View sentiment.
* View priority.
* View customer value.
* View SLA state.
* View recommended responses.
* Edit AI-generated responses.
* Accept AI escalations.
* Take over AI conversations.
* Return conversations to AI.
* Assign conversations.
* Reassign conversations.
* Add internal notes.
* Create tickets.
* Update tickets.
* Trigger approved workflows.
* Search conversations.
* Search knowledge-base content.

---

## 5. Human Sales Agent Requirements

Sales agents shall be able to:

* Receive WhatsApp sales inquiries.
* View lead profiles.
* View lead scores.
* View company information.
* View previous conversations.
* View buying intent.
* View product interests.
* View AI recommendations.
* Respond to prospects.
* Approve AI-generated responses.
* Send personalized messages.
* Schedule eligible follow-ups.
* Create CRM activities.
* Create opportunities.
* Update pipeline stages.
* Trigger sales workflows.
* Track conversion.
* Track revenue attribution.

---

## 6. Support Manager Requirements

Support managers shall be able to:

* Monitor WhatsApp queues.
* Monitor active conversations.
* Monitor unresolved conversations.
* Monitor SLA performance.
* Monitor agent workload.
* Monitor AI resolution rate.
* Monitor human resolution rate.
* Monitor escalations.
* Configure routing.
* Configure escalation policies.
* Configure SLA policies.
* Review customer satisfaction.
* Review sentiment trends.
* Review AI performance.
* Audit agent actions.

---

## 7. Sales Manager Requirements

Sales managers shall be able to:

* Monitor WhatsApp leads.
* Monitor response time.
* Monitor sales conversations.
* Monitor qualified leads.
* Monitor opportunities.
* Monitor conversion.
* Monitor revenue generated through WhatsApp.
* Review AI sales recommendations.
* Review agent performance.
* Configure sales routing.
* Configure follow-up workflows.

---

## 8. Organization Administrator Requirements

Administrators shall be able to:

* Connect WhatsApp Business Accounts.
* Configure business phone numbers.
* Configure WhatsApp channels.
* Configure teams.
* Configure AI agents.
* Configure routing.
* Configure escalation.
* Configure SLA.
* Configure templates.
* Configure business hours.
* Configure automation.
* Configure permissions.
* Configure retention.
* Configure security policies.
* Configure analytics.
* Configure notifications.
* Configure customer communication policies.

---

## 9. Super Admin Requirements

Super Admins shall be able to:

* Monitor WhatsApp channel health across tenants.
* Monitor provider health.
* Monitor webhook health.
* Monitor message processing.
* Monitor message failures.
* Monitor platform-wide usage.
* Monitor tenant quotas.
* Monitor abuse.
* Monitor suspicious activity.
* Disable compromised integrations.
* Review global audit logs.
* Configure platform-level limits.
* Manage feature flags.
* Investigate provider incidents.

---

## 10. User Requirements

## UR-001 — WhatsApp Communication

The system shall allow customers to communicate with SalesGenie through WhatsApp.

## UR-002 — Persistent Conversations

Customers shall be able to continue conversations without losing previous context.

## UR-003 — Unified Customer Identity

WhatsApp conversations shall be associated with the appropriate SalesGenie customer identity.

## UR-004 — AI Support

Customers shall be able to receive AI-generated support responses.

## UR-005 — Human Support

Customers shall be able to communicate with human agents.

## UR-006 — Hybrid Support

Customers shall be able to transition between AI and human support without restarting the conversation.

## UR-007 — Human Request

Customers shall be able to explicitly request a human agent.

## UR-008 — Context Preservation

Human agents shall receive the complete relevant context when a conversation is escalated.

---

## 11. Customer Identity Requirements

## UR-009 — WhatsApp Identity

The system shall identify a customer using the WhatsApp identity available from the channel.

## UR-010 — Identity Resolution

The system shall attempt to associate the WhatsApp identity with:

* Customer
* Contact
* Lead
* Account
* Organization
* Opportunity
* Ticket
* Existing conversation

## UR-011 — Cross-Channel Identity

Where identity confidence is sufficient, the system shall associate WhatsApp activity with the customer's existing omnichannel identity.

## UR-012 — Duplicate Prevention

The system shall minimize duplicate customer profiles.

## UR-013 — Identity Conflict

Ambiguous identity matches shall be flagged rather than silently merging unrelated customers.

---

## 12. AI Understanding Requirements

## UR-014 — Intent Detection

AI shall detect:

* Support requests
* Product questions
* Pricing requests
* Sales inquiries
* Demo requests
* Complaints
* Billing issues
* Refund requests
* Technical problems
* Order inquiries
* Account issues
* Feature requests
* Partnership requests
* General questions
* Spam
* Urgent requests

Organizations shall be able to configure custom intents.

## UR-015 — Sentiment Detection

AI shall detect customer sentiment.

Possible classifications:

* Positive
* Neutral
* Negative
* Frustrated
* Angry
* Satisfied
* Urgent

## UR-016 — Language Detection

The system shall detect the language of incoming WhatsApp messages.

## UR-017 — Multilingual Response

AI shall be capable of responding in the customer's language when enabled.

## UR-018 — Entity Extraction

AI shall extract relevant entities such as:

* Customer name
* Company
* Product
* Order number
* Ticket number
* Invoice number
* Date
* Location
* Requested service
* Budget indicators
* Buying timeline

---

## 13. AI Response Requirements

## UR-019 — AI Drafting

AI shall generate responses using authorized:

* Conversation history
* Customer profile
* CRM information
* Ticket information
* Knowledge base
* Business policies
* Product information
* Previous actions

## UR-020 — Personalization

AI responses shall be personalized using authorized customer context.

## UR-021 — Tone

The platform shall support configurable AI tones:

* Professional
* Friendly
* Concise
* Empathetic
* Technical
* Sales-oriented
* Formal

## UR-022 — AI Confidence

AI responses shall have an internal confidence/quality signal where supported by the AI pipeline.

## UR-023 — Low Confidence Escalation

Low-confidence conversations shall be eligible for human escalation.

---

## 14. AI Safety Requirements

## UR-024 — Restricted Actions

AI shall not execute unauthorized actions.

## UR-025 — High-Risk Approval

Configurable high-risk actions shall require human approval.

Examples:

* Refunds
* Financial commitments
* Account deletion
* Sensitive information disclosure
* Contract modifications
* High-value sales actions
* Security changes

## UR-026 — Prompt Injection Protection

Customer messages shall be treated as untrusted input.

## UR-027 — Knowledge Grounding

AI shall use authorized knowledge sources for configured workflows.

## UR-028 — Human Override

Humans shall always be able to override AI decisions.

---

## 15. Human Handoff Requirements

## UR-029 — AI-to-Human Handoff

AI shall escalate conversations to human agents based on configurable rules.

## UR-030 — Human-to-AI Handoff

Authorized agents shall be able to return eligible conversations to AI.

## UR-031 — AI Pause

When a human takes control, autonomous AI messaging shall be paused.

## UR-032 — Context Transfer

Handoff shall preserve:

* Conversation history
* Customer identity
* Intent
* Sentiment
* Summary
* Entities
* Ticket
* SLA
* AI actions
* Previous recommendations

---

## 16. WhatsApp Message Requirements

The system shall support applicable WhatsApp message types, including:

* Text
* Image
* Video
* Audio
* Document
* Location
* Contact
* Interactive messages
* Template messages
* Reply interactions
* Product/catalog interactions where enabled

---

## 17. Interactive Messaging Requirements

The platform shall support interactive customer experiences where available.

Examples:

```text
Customer
   ↓
"How can we help?"
   ├── Support
   ├── Sales
   ├── Billing
   └── Human Agent
```

Interactive actions shall map to deterministic backend operations.

---

## 18. Sales Requirements

## UR-033 — Lead Detection

AI shall detect potential leads from WhatsApp conversations.

## UR-034 — Lead Qualification

AI shall extract qualification information.

## UR-035 — Lead Scoring

The system shall calculate configurable lead scores.

## UR-036 — Sales Routing

Qualified leads shall be routed to appropriate sales agents.

## UR-037 — Product Recommendations

AI may recommend relevant products based on authorized product information.

## UR-038 — Demo Requests

The system shall detect and process demo requests.

## UR-039 — Opportunity Detection

AI shall identify potential sales opportunities.

## UR-040 — Sales Conversion

The system shall associate WhatsApp interactions with sales outcomes where possible.

---

## 19. Support Requirements

## UR-041 — Support Request

Customers shall be able to initiate support cases through WhatsApp.

## UR-042 — Ticket Creation

Support conversations shall be convertible into tickets.

## UR-043 — Ticket Tracking

Customers shall be able to receive permitted ticket updates through WhatsApp.

## UR-044 — Ticket Context

Agents shall see ticket context directly within the WhatsApp conversation.

---

## 20. SLA Requirements

## UR-045 — First Response SLA

The platform shall measure time from incoming WhatsApp message to first meaningful response.

## UR-046 — Resolution SLA

The platform shall measure resolution duration.

## UR-047 — SLA Warning

The system shall notify agents before configurable SLA thresholds are breached.

## UR-048 — SLA Escalation

SLA violations shall trigger configured escalation workflows.

---

## 21. Notification Requirements

The system shall support WhatsApp notifications for eligible use cases.

Examples:

* Ticket created
* Ticket updated
* Appointment reminder
* Order status
* Payment status
* Shipping status
* Account notification
* Support resolution
* Sales follow-up
* Service notification

Applicable provider policies and message-template requirements shall be enforced by the channel policy layer.

---

## 22. System Requirements

## 22.1 Architecture

The WhatsApp Channel shall be implemented as a dedicated bounded domain integrated with SalesGenie's microservice architecture.

Recommended logical architecture:

```text
WhatsApp Provider
        ↓
WhatsApp Gateway
        ↓
Webhook Service
        ↓
WhatsApp Channel Service
        ↓
Message Normalizer
        ↓
Identity Resolver
        ↓
Conversation Service
        ↓
Event Bus
        ├── AI Gateway
        ├── Routing Service
        ├── Ticket Service
        ├── CRM Service
        ├── Knowledge Base
        ├── Workflow Engine
        ├── SLA Service
        └── Analytics Service
```

---

## 23. Provider Integration Requirements

## SR-001 — Provider Abstraction

WhatsApp provider logic shall be isolated behind a provider abstraction.

Example:

```text
WhatsAppProvider
├── MetaCloudProvider
└── FutureProviderAdapters
```

## SR-002 — Provider Credentials

Provider credentials shall never be stored in frontend code.

## SR-003 — Secret Management

Access tokens and secrets shall be stored using secure server-side secret management.

## SR-004 — Token Rotation

The platform shall support credential rotation.

## SR-005 — Connection Validation

Administrators shall be able to validate WhatsApp integrations.

---

## 24. WhatsApp Business Account Requirements

The platform shall maintain configuration for:

```text
WhatsAppBusinessAccount
PhoneNumber
PhoneNumberId
BusinessDisplayName
BusinessProfile
ProviderConnection
Tenant
WebhookConfiguration
MessagingPolicy
```

Each WhatsApp phone number shall be associated with exactly the appropriate tenant and business configuration.

---

## 25. Webhook Requirements

## SR-006 — HTTPS Webhook

Production webhook endpoints shall use HTTPS.

## SR-007 — Webhook Verification

The system shall support provider webhook verification.

## SR-008 — Signature Verification

Incoming webhook payloads shall be authenticated using provider-supported signature validation.

## SR-009 — Replay Protection

The system shall detect and reject replayed webhook events.

## SR-010 — Idempotency

Webhook processing shall be idempotent.

## SR-011 — Fast Acknowledgement

Webhook endpoints shall acknowledge valid events quickly and process expensive workloads asynchronously.

---

## 26. Inbound Message Pipeline

```text
Webhook
   ↓
Authentication
   ↓
Schema Validation
   ↓
Replay Detection
   ↓
Idempotency
   ↓
Message Persistence
   ↓
Normalization
   ↓
Identity Resolution
   ↓
Conversation Resolution
   ↓
Event Publication
   ↓
AI / Human Processing
```

---

## 27. Message Data Model

The system shall maintain a canonical message entity.

```text
WhatsAppMessage
├── id
├── tenant_id
├── business_account_id
├── phone_number_id
├── conversation_id
├── customer_id
├── provider_message_id
├── sender_id
├── recipient_id
├── message_type
├── text
├── media
├── location
├── interactive_payload
├── template_metadata
├── reply_context
├── status
├── direction
├── created_at
├── received_at
└── processed_at
```

---

## 28. Conversation Data Model

```text
WhatsAppConversation
├── id
├── tenant_id
├── customer_id
├── phone_number_id
├── assigned_agent_id
├── assigned_team_id
├── ai_agent_id
├── state
├── intent
├── sentiment
├── priority
├── language
├── sla_policy_id
├── ticket_id
├── lead_id
├── opportunity_id
├── last_message_at
├── last_customer_message_at
├── last_agent_message_at
├── ai_enabled
├── human_controlled
├── created_at
└── updated_at
```

---

## 29. Message State Requirements

The platform shall maintain message state such as:

```text
RECEIVED
PROCESSING
QUEUED
SENT
DELIVERED
READ
FAILED
RETRYING
```

The system shall not assume that a send operation means successful delivery.

---

## 30. Conversation State Machine

```text
NEW
 ↓
RECEIVED
 ↓
CLASSIFIED
 ↓
ROUTED
 ↓
AI_PROCESSING
 ├── AI_RESPONDED
 │      ↓
 │   WAITING_FOR_CUSTOMER
 │
 └── HUMAN_REQUIRED
        ↓
     ASSIGNED
        ↓
     HUMAN_RESPONDED
        ↓
     WAITING_FOR_CUSTOMER
        ↓
     RESOLVED
        ↓
     CLOSED
```

Additional states:

```text
ESCALATED
SLA_WARNING
SLA_BREACHED
FAILED
BLOCKED
SPAM
```

---

## 31. Identity Resolution Architecture

```text
WhatsApp Identity
       ↓
Exact Customer Match
       ↓
Existing Contact
       ↓
Lead Match
       ↓
Phone / Email Correlation
       ↓
CRM Match
       ↓
Existing Conversation
       ↓
Create Customer Identity
```

Identity resolution shall use deterministic rules before probabilistic matching.

---

## 32. Multi-Tenant Isolation

## SR-012 — Tenant Isolation

Every WhatsApp entity shall contain tenant ownership.

## SR-013 — Query Isolation

Every query shall enforce tenant boundaries.

## SR-014 — Event Isolation

Events shall contain tenant context.

## SR-015 — AI Isolation

AI context shall never mix information from different tenants.

## SR-016 — Knowledge Isolation

RAG retrieval shall be tenant- and permission-aware.

## SR-017 — Attachment Isolation

WhatsApp media shall be isolated by tenant.

---

## 33. AI Gateway Integration

The WhatsApp Channel shall use SalesGenie's centralized AI Gateway.

```text
WhatsApp
   ↓
Conversation Service
   ↓
AI Gateway
   ├── Intent Agent
   ├── Support Agent
   ├── Sales Agent
   ├── Memory Agent
   ├── Search/RAG Agent
   ├── Sentiment Agent
   └── Orchestrator
```

---

## 34. AI Context Construction

The AI context shall include only authorized information.

```text
System Policy
      +
Tenant Policy
      +
Agent Instructions
      +
Conversation History
      +
Customer Context
      +
CRM Context
      +
Ticket Context
      +
Knowledge Retrieval
      +
Current Message
      ↓
AI Model
```

The system shall distinguish:

* System instructions
* Trusted business data
* Retrieved knowledge
* Customer-provided content
* AI-generated content

---

## 35. RAG Requirements

## SR-018 — Knowledge Retrieval

The AI shall be able to retrieve authorized knowledge.

## SR-019 — Permission Filtering

Retrieval shall enforce document permissions.

## SR-020 — Tenant Filtering

Retrieval shall enforce tenant isolation.

## SR-021 — Freshness

The system shall support knowledge freshness and versioning.

## SR-022 — Provenance

AI responses should retain provenance metadata internally.

---

## 36. Prompt Injection Defense

Incoming WhatsApp content shall be considered untrusted.

The platform shall prevent customer messages from:

* Changing system instructions.
* Granting permissions.
* Calling unauthorized tools.
* Bypassing approval policies.
* Accessing other customers.
* Accessing restricted documents.
* Changing tenant configuration.
* Executing administrative operations.

---

## 37. Agent Tool Security

AI agents shall only receive tools they are authorized to use.

Example:

```text
Customer Message
      ↓
AI Agent
      ↓
Authorized Tool Filter
      ↓
Allowed Tools Only
      ↓
LLM
      ↓
Tool Request
      ↓
Permission Check
      ↓
Approval Check
      ↓
Execution
      ↓
Audit
```

---

## 38. Human Approval Requirements

The following may require human approval depending on tenant policy:

* Refund
* Cancellation
* Account modification
* High-value purchase
* Discount
* Contractual commitment
* Sensitive data disclosure
* High-impact CRM changes
* Bulk messaging
* High-risk workflow execution

---

## 39. Human Takeover Architecture

```text
AI Conversation
      ↓
Human Takeover
      ↓
AI Auto-Send Disabled
      ↓
Agent Assigned
      ↓
Agent Workspace
      ↓
Human Response
      ↓
Conversation Continues
```

---

## 40. AI Resume Architecture

```text
Human Resolution
      ↓
Agent Marks AI-Eligible
      ↓
Policy Validation
      ↓
AI Re-enabled
      ↓
Future Messages
      ↓
AI Processing
```

---

## 41. Routing Engine

Routing shall consider:

* Intent
* Customer tier
* Language
* Priority
* Sentiment
* Agent skills
* Agent availability
* Current workload
* SLA
* Department
* Sales/support classification
* Business hours
* Geographic rules

---

## 42. Routing Examples

```text
IF intent = billing
THEN billing_team

IF intent = sales
THEN sales_team

IF intent = technical_support
THEN technical_support

IF customer.tier = enterprise
THEN enterprise_support

IF sentiment = highly_negative
THEN priority_support

IF language = Bengali
THEN Bengali_support

IF AI_confidence < threshold
THEN human_support

IF lead_score > threshold
THEN senior_sales_agent
```

---

## 43. Queue Requirements

The system shall support:

* Support queue
* Sales queue
* Billing queue
* Technical queue
* VIP queue
* Enterprise queue
* Escalation queue
* AI-review queue
* Human-approval queue

---

## 44. Agent Assignment

The system shall support:

* Manual assignment
* Round-robin
* Least-loaded
* Skill-based
* Priority-based
* AI-based
* Team-based
* SLA-based assignment

---

## 45. WhatsApp Media Requirements

The platform shall support applicable WhatsApp media workflows.

Supported categories shall include:

```text
Text
Image
Audio
Video
Document
Location
Contact
Interactive
Template
```

Media processing shall be asynchronous.

---

## 46. Media Processing Pipeline

```text
Incoming Media
      ↓
Metadata Validation
      ↓
Provider Retrieval
      ↓
Secure Storage
      ↓
Malware / Security Scan
      ↓
Optional OCR / Transcription
      ↓
AI Processing
      ↓
Conversation Context
```

---

## 47. Voice Message Requirements

Where supported, voice messages shall be processed using:

```text
Voice Message
      ↓
Secure Media Retrieval
      ↓
Audio Validation
      ↓
Speech-to-Text
      ↓
Intent / Sentiment
      ↓
AI Processing
      ↓
Text or Voice Response
```

The original media shall remain associated with the conversation.

---

## 48. Image Understanding Requirements

Where enabled, AI shall be able to analyze supported images for legitimate customer-support use cases.

Examples:

* Product issue
* Screenshot
* Invoice
* Receipt
* Damaged product
* Identification document
* Error message

Sensitive image processing shall be controlled by tenant policy.

---

## 49. Document Understanding Requirements

Supported documents may be processed for:

* Invoice extraction
* Order information
* Support evidence
* Product documentation
* Business forms
* Customer-submitted documents

Document processing shall respect security, retention, and permission policies.

---

## 50. Template Management

The system shall provide a centralized template management subsystem.

Templates shall support:

* Template name
* Language
* Category
* Variables
* Header
* Body
* Footer
* Buttons
* Media
* Approval status
* Provider status
* Version
* Tenant ownership

---

## 51. Template Personalization

AI may personalize approved template variables.

Example:

```text
Hello {{customer.first_name}},

Your support request {{ticket.id}}
has been updated to {{ticket.status}}.
```

AI shall not modify protected policy, compliance, or legal text unless explicitly authorized.

---

## 52. Interactive Message Requirements

The platform shall support configurable interactive experiences where supported.

Examples:

```text
Choose an option:

[Track Order]
[Contact Support]
[Talk to Sales]
```

and:

```text
What do you need?

[Billing]
[Technical]
[Sales]
[Human Agent]
```

Button/list identifiers shall map to deterministic backend operations.

---

## 53. Product Messaging

For businesses using product catalogs, WhatsApp conversations may integrate with SalesGenie's product system.

The system shall support:

* Product lookup
* Product recommendation
* Product inquiry
* Product selection
* Product interest tracking
* Product-to-lead association
* Product-to-opportunity association

---

## 54. CRM Integration

WhatsApp shall integrate with SalesGenie's CRM.

The system shall support authorized access to:

* Customer
* Contact
* Organization
* Lead
* Opportunity
* Account
* Activities
* Previous interactions
* Purchase history

---

## 55. Ticket Integration

The WhatsApp Channel shall integrate with ticket management.

## FR-001 — Create Ticket

A conversation may create a ticket automatically or manually.

## FR-002 — Link Ticket

Existing WhatsApp conversations may be linked to existing tickets.

## FR-003 — Update Ticket

Authorized AI or human agents may update tickets.

## FR-004 — Ticket Notifications

Eligible ticket events may trigger WhatsApp notifications.

---

## 56. Workflow Integration

The WhatsApp Channel shall integrate with SalesGenie's workflow engine.

Example:

```text
WhatsApp Message
      ↓
Intent = Order Status
      ↓
Identify Customer
      ↓
Find Order
      ↓
Retrieve Status
      ↓
Generate Response
      ↓
Send WhatsApp Message
      ↓
Log Action
```

---

## 57. Advanced Workflow Example

```text
Customer sends:
"I want to cancel my order."

        ↓

Intent Detection
        ↓

Cancellation Intent
        ↓

Customer Lookup
        ↓

Order Lookup
        ↓

Policy Evaluation
        ↓
      ┌───────────────┐
      │ Eligible?     │
      └───────┬───────┘
              │
        ┌─────┴─────┐
        ▼           ▼
       YES          NO
        ↓           ↓
   Human/AI       Explain
   Policy         Policy
   Action         Limitation
        ↓
    Approval
        ↓
     Execute
        ↓
    Update CRM
        ↓
    Update Ticket
        ↓
 WhatsApp Response
```

---

## 58. Event-Driven Architecture

The system shall publish events such as:

```text
whatsapp.message.received
whatsapp.message.processed
whatsapp.message.sent
whatsapp.message.delivered
whatsapp.message.read
whatsapp.message.failed
whatsapp.media.received
whatsapp.conversation.created
whatsapp.conversation.updated
whatsapp.conversation.assigned
whatsapp.conversation.escalated
whatsapp.conversation.resolved
whatsapp.ai.started
whatsapp.ai.completed
whatsapp.ai.escalated
whatsapp.human.takeover
whatsapp.human.response
whatsapp.ticket.created
whatsapp.ticket.updated
whatsapp.lead.created
whatsapp.opportunity.created
whatsapp.workflow.triggered
```

---

## 59. Queue Architecture

Asynchronous workloads shall use durable queues/event streams.

Workloads shall include:

* Webhook processing
* Message normalization
* Media retrieval
* Media scanning
* Speech-to-text
* OCR
* AI inference
* RAG retrieval
* CRM enrichment
* Ticket creation
* Workflow execution
* Outbound sending
* Analytics processing

---

## 60. Reliability Requirements

## SR-023 — Durable Ingestion

Successfully received webhook events shall be persisted before expensive downstream processing.

## SR-024 — Idempotent Processing

Repeated events shall not produce duplicate business actions.

## SR-025 — Retry

Transient failures shall use exponential backoff.

## SR-026 — Dead Letter Queue

Repeated failures shall enter a dead-letter queue.

## SR-027 — Replay

Authorized operators shall be able to replay failed events.

## SR-028 — Provider Outage

Provider outages shall not cause permanent loss of accepted messages.

---

## 61. AI Failure Handling

If AI is unavailable:

```text
AI Failure
   ↓
Retry
   ↓
Fallback Model
   ↓
Rule-Based Response
   ↓
Human Queue
```

The fallback path shall be configurable.

---

## 62. Message Loop Prevention

The system shall prevent:

```text
AI
 ↓
WhatsApp
 ↓
Automated Reply
 ↓
AI
 ↓
WhatsApp
 ↓
Automated Reply
```

Controls shall include:

* Sender classification
* Automation detection
* Conversation state
* Message counters
* Rate limits
* Loop detection
* Workflow limits
* AI response suppression

---

## 63. Rate Limiting

Rate limits shall exist at:

* Tenant
* Business account
* Phone number
* Customer
* API
* AI agent
* Workflow
* Outbound messaging

The platform shall prevent runaway automation.

---

## 64. Abuse Detection

The system shall detect:

* Spam
* Message flooding
* Suspicious behavior
* Automated loops
* Compromised credentials
* Excessive outbound messaging
* Abnormal AI activity
* Malicious media
* Prompt injection
* Unauthorized automation

---

## 65. Security Requirements

## SR-029 — Encryption

Sensitive data shall be encrypted at rest.

## SR-030 — TLS

External communications shall use secure transport.

## SR-031 — Secret Isolation

Provider credentials shall never be exposed to frontend clients.

## SR-032 — Least Privilege

Provider and internal service permissions shall follow least privilege.

## SR-033 — Credential Revocation

Administrators shall be able to disconnect/revoke WhatsApp integrations.

## SR-034 — Audit

Security-sensitive operations shall be logged.

---

## 66. RBAC Requirements

The system shall enforce permissions such as:

```text
whatsapp.read
whatsapp.send
whatsapp.reply
whatsapp.assign
whatsapp.escalate
whatsapp.takeover
whatsapp.ai.manage
whatsapp.templates.manage
whatsapp.integration.manage
whatsapp.analytics.read
whatsapp.audit.read
whatsapp.media.read
whatsapp.media.send
whatsapp.workflow.execute
whatsapp.export
```

---

## 67. AI Agent Permissions

AI agents shall have explicit permissions.

Example:

```text
Support AI
├── read_customer
├── read_ticket
├── search_knowledge
├── create_ticket
└── send_message

Sales AI
├── read_customer
├── read_lead
├── search_products
├── create_lead
└── send_message
```

High-impact tools shall require approval according to policy.

---

## 68. Audit Requirements

The system shall record:

```text
WHATSAPP_MESSAGE_RECEIVED
WHATSAPP_MESSAGE_SENT
WHATSAPP_MESSAGE_FAILED
WHATSAPP_MESSAGE_DELIVERED
WHATSAPP_MESSAGE_READ
WHATSAPP_CONVERSATION_CREATED
WHATSAPP_CONVERSATION_ASSIGNED
WHATSAPP_AI_RESPONSE
WHATSAPP_AI_ESCALATION
WHATSAPP_HUMAN_TAKEOVER
WHATSAPP_HUMAN_RESPONSE
WHATSAPP_TEMPLATE_SENT
WHATSAPP_MEDIA_ACCESSED
WHATSAPP_TICKET_CREATED
WHATSAPP_WORKFLOW_EXECUTED
WHATSAPP_INTEGRATION_CONNECTED
WHATSAPP_INTEGRATION_DISCONNECTED
```

Audit records shall contain:

```text
event_id
tenant_id
actor_id
actor_type
action
resource_type
resource_id
timestamp
ip_address
user_agent
trace_id
metadata
```

---

## 69. Customer 360 Requirements

The WhatsApp workspace shall provide a customer context panel.

It shall include:

* Customer profile
* Phone identity
* Email identity
* Organization
* Lead score
* Customer tier
* Lifetime value
* Tickets
* Orders
* Previous conversations
* Email history
* Website chat history
* Sales activities
* AI insights
* Notes
* Recent activities

---

## 70. Omnichannel Requirements

WhatsApp conversations shall be linked to SalesGenie's omnichannel conversation model.

Example:

```text
Customer
   │
   ├── WhatsApp
   ├── Email
   ├── Website Chat
   ├── Telegram
   ├── Slack
   ├── Discord
   └── Voice
          ↓
   Unified Customer Identity
          ↓
   Unified Conversation Timeline
```

The platform shall avoid creating duplicate customer records when reliable identity matching is available.

---

## 71. Conversation Search

Authorized users shall be able to search WhatsApp conversations using:

* Customer
* Phone number
* Name
* Organization
* Agent
* Team
* Intent
* Sentiment
* Priority
* Ticket ID
* Lead ID
* Opportunity ID
* Date
* Conversation status
* AI status
* Human status

---

## 72. Analytics Requirements

The WhatsApp analytics subsystem shall provide:

## Operational Metrics

* Incoming messages
* Outgoing messages
* Active conversations
* New conversations
* Resolved conversations
* Escalations
* Failed messages
* Delivery rate
* Read rate
* Response time
* Resolution time

## AI Metrics

* AI response rate
* AI resolution rate
* AI escalation rate
* AI confidence
* Human override rate
* AI acceptance rate
* AI edit rate
* AI latency
* Token usage
* AI cost
* Hallucination incidents

## Human Metrics

* Conversations handled
* First response time
* Resolution time
* SLA compliance
* Escalations
* Customer satisfaction
* Agent workload
* Reopen rate

## Sales Metrics

* Leads generated
* Qualified leads
* Opportunities
* Conversion rate
* Revenue
* Average deal value
* Sales response time
* Follow-up completion
* Revenue attribution

---

## 73. Customer Satisfaction

The platform shall support customer satisfaction measurement after eligible conversations.

Possible mechanisms:

```text
Conversation Resolved
       ↓
Customer Satisfaction Request
       ↓
Rating
       ↓
Feedback
       ↓
Sentiment Analysis
       ↓
Analytics
```

---

## 74. Conversation Intelligence

The AI shall analyze WhatsApp conversations for:

* Customer intent
* Buying signals
* Objections
* Complaints
* Competitor mentions
* Product requests
* Sentiment
* Urgency
* Churn risk
* Upsell opportunities
* Cross-sell opportunities
* Support quality
* Agent quality

---

## 75. Lead Intelligence

The WhatsApp channel shall contribute data to SalesGenie's lead intelligence system.

Example:

```text
WhatsApp Conversation
       ↓
Intent
       ↓
Buying Signal
       ↓
Lead Score
       ↓
Qualification
       ↓
CRM Lead
       ↓
Opportunity
       ↓
Revenue
```

---

## 76. AI Follow-Up

The system shall support configurable AI follow-up workflows.

Example:

```text
Customer shows buying intent
        ↓
Lead Created
        ↓
Sales Agent Assigned
        ↓
No Response
        ↓
Follow-Up Recommendation
        ↓
Human Approval
        ↓
WhatsApp Message
```

The system shall respect applicable channel policies and messaging constraints.

---

## 77. Business Hours

Each tenant shall be able to configure:

* Time zone
* Business hours
* Holidays
* Weekend behavior
* After-hours routing
* Emergency escalation

Example:

```text
Business Hours
     ↓
Human Available
     ↓
Human Queue

After Hours
     ↓
AI Support
     ↓
Emergency Detection
     ↓
On-Call Escalation
```

---

## 78. Notification Engine

Notifications shall support:

```text
Immediate
Scheduled
Event-triggered
Workflow-triggered
SLA-triggered
AI-triggered
Human-triggered
```

---

## 79. API Requirements

Representative endpoints:

```text
/api/v1/whatsapp/accounts
/api/v1/whatsapp/business-accounts
/api/v1/whatsapp/phone-numbers
/api/v1/whatsapp/conversations
/api/v1/whatsapp/messages
/api/v1/whatsapp/media
/api/v1/whatsapp/templates
/api/v1/whatsapp/webhooks
/api/v1/whatsapp/routing
/api/v1/whatsapp/escalations
/api/v1/whatsapp/sla
/api/v1/whatsapp/analytics
/api/v1/whatsapp/integrations
```

---

## 80. Webhook API

Representative endpoint:

```http
POST /api/v1/whatsapp/webhooks
```

Processing:

```text
POST
 ↓
Signature Verification
 ↓
Payload Validation
 ↓
Replay Detection
 ↓
Idempotency
 ↓
Persist Event
 ↓
Return Success
 ↓
Async Processing
```

---

## 81. Send Message API

Representative endpoint:

```http
POST /api/v1/whatsapp/messages/send
```

Conceptual request:

```json
{
  "phone_number_id": "phone_123",
  "conversation_id": "conv_123",
  "recipient": "customer_whatsapp_id",
  "message_type": "text",
  "text": "Your support request has been updated.",
  "idempotency_key": "msg_123"
}
```

---

## 82. Template Send API

Representative endpoint:

```http
POST /api/v1/whatsapp/messages/template
```

Conceptual request:

```json
{
  "phone_number_id": "phone_123",
  "conversation_id": "conv_123",
  "recipient": "customer_whatsapp_id",
  "template_id": "template_123",
  "language": "en",
  "variables": {
    "customer_name": "John",
    "ticket_id": "TKT-123"
  }
}
```

---

## 83. Media API

Representative endpoints:

```text
POST /api/v1/whatsapp/media/upload
GET  /api/v1/whatsapp/media/{id}
POST /api/v1/whatsapp/media/send
```

Media access shall be authorization-controlled.

---

## 84. Conversation API

Representative endpoints:

```text
GET /api/v1/whatsapp/conversations
GET /api/v1/whatsapp/conversations/{id}
POST /api/v1/whatsapp/conversations/{id}/assign
POST /api/v1/whatsapp/conversations/{id}/takeover
POST /api/v1/whatsapp/conversations/{id}/resume-ai
POST /api/v1/whatsapp/conversations/{id}/resolve
POST /api/v1/whatsapp/conversations/{id}/escalate
```

---

## 85. Outbound Message State Machine

```text
CREATED
   ↓
QUEUED
   ↓
SENDING
   ↓
SENT
   ↓
DELIVERED
   ↓
READ
```

Failure branch:

```text
SENDING
   ↓
FAILED
   ↓
RETRY
   ↓
SENDING
```

Permanent failure:

```text
FAILED
   ↓
DEAD_LETTER
   ↓
OPERATOR_REVIEW
```

---

## 86. Idempotency Requirements

Every externally triggered business action shall have an idempotency strategy.

Examples:

```text
Webhook Event ID
Provider Message ID
Workflow Execution ID
Outbound Message ID
Idempotency Key
```

Repeated provider events shall not:

* Create duplicate tickets.
* Create duplicate leads.
* Send duplicate responses.
* Create duplicate workflow executions.
* Duplicate CRM activities.

---

## 87. Performance Requirements

## SR-035 — Webhook Response

Webhook handlers shall acknowledge valid events without waiting for:

* LLM inference
* RAG retrieval
* CRM calls
* Ticket creation
* Workflow completion
* Media analysis

## SR-036 — AI Latency

AI responses should target SalesGenie's platform response objectives.

## SR-037 — Inbox Performance

The agent inbox shall remain responsive under high conversation volume.

## SR-038 — Large Conversations

Large conversation histories shall use:

* Pagination
* Summaries
* Context windows
* Incremental retrieval
* Memory compression

---

## 88. Scalability Requirements

The system shall horizontally scale:

```text
Webhook Workers
Message Workers
AI Workers
Media Workers
OCR Workers
Transcription Workers
Outbound Workers
Analytics Workers
Workflow Workers
```

Each workload shall scale independently.

---

## 89. Availability Requirements

The WhatsApp Channel shall be designed for enterprise availability.

The architecture shall support:

* Multiple application instances
* Durable queues
* Database replication
* Redis where appropriate
* Health checks
* Circuit breakers
* Retries
* Provider failure handling
* Graceful degradation
* Disaster recovery

---

## 90. Observability

The system shall expose:

```text
whatsapp_webhook_rate
whatsapp_message_ingestion_rate
whatsapp_message_processing_latency
whatsapp_outbound_latency
whatsapp_delivery_rate
whatsapp_read_rate
whatsapp_failure_rate
whatsapp_retry_rate
whatsapp_queue_depth
whatsapp_ai_latency
whatsapp_ai_resolution_rate
whatsapp_human_resolution_rate
whatsapp_escalation_rate
whatsapp_sla_breach_rate
whatsapp_media_processing_latency
```

---

## 91. Distributed Tracing

Every message lifecycle shall support:

```text
trace_id
span_id
tenant_id
conversation_id
message_id
provider_message_id
workflow_id
ai_run_id
agent_id
```

Trace flow:

```text
WhatsApp
 ↓
Webhook
 ↓
Channel Service
 ↓
Conversation Service
 ↓
AI Gateway
 ↓
RAG
 ↓
CRM
 ↓
Workflow
 ↓
Outbound Service
 ↓
WhatsApp
```

---

## 92. Structured Logging

Logs shall include:

```text
timestamp
service
tenant_id
trace_id
conversation_id
message_id
operation
provider
status
latency
error_code
```

Raw customer message contents shall not be unnecessarily written to logs.

---

## 93. Error Handling

The system shall handle:

* Invalid webhook payload
* Invalid signature
* Duplicate webhook
* Expired credentials
* Provider outage
* Rate limits
* Invalid recipient
* Unsupported message type
* Media retrieval failure
* AI failure
* RAG failure
* CRM failure
* Ticket failure
* Workflow failure
* Database failure
* Queue failure

---

## 94. Graceful Degradation

If AI fails:

```text
AI Failure
    ↓
Retry
    ↓
Fallback Model
    ↓
Rule-Based Processing
    ↓
Human Queue
```

If CRM fails:

```text
CRM Failure
    ↓
Continue Conversation
    ↓
Queue CRM Sync
    ↓
Retry Later
```

If ticket service fails:

```text
Ticket Failure
    ↓
Persist Conversation
    ↓
Retry Ticket Creation
```

---

## 95. Data Retention

The platform shall support configurable retention for:

* Messages
* Conversation metadata
* Media
* AI metadata
* AI summaries
* Customer profiles
* Audit records
* Delivery events
* Analytics events

---

## 96. Data Deletion

Authorized deletion workflows shall support:

* Customer deletion
* Conversation deletion
* Media deletion
* Ticket unlinking
* AI-context deletion
* Search-index deletion
* Analytics deletion where legally required

Deletion shall propagate to derived stores where applicable.

---

## 97. Export

Authorized users shall be able to export permitted:

* Conversations
* Messages
* Media metadata
* Tickets
* Customer history
* Analytics

Exports shall be audited.

---

## 98. Accessibility Requirements

The WhatsApp agent workspace shall support:

* Keyboard navigation
* Screen readers
* Focus management
* Semantic controls
* Accessible labels
* High contrast
* Responsive layouts
* Mobile-friendly agent workspace

---

## 99. Functional Requirements

## FR-001 — Connect WhatsApp Business Account

The system shall allow administrators to connect a WhatsApp Business Account.

Flow:

```text
Select WhatsApp
      ↓
Authenticate
      ↓
Authorize
      ↓
Discover Business Account
      ↓
Discover Phone Numbers
      ↓
Configure Number
      ↓
Configure Webhook
      ↓
Validate Connection
      ↓
Activate Channel
```

---

## FR-002 — Configure Phone Number

Administrators shall configure:

* Display name
* Phone number
* Business account
* Support team
* Sales team
* AI agent
* Business hours
* SLA
* Routing
* Escalation
* Templates
* Automation

---

## FR-003 — Receive Message

The system shall:

1. Receive webhook.
2. Validate signature.
3. Validate schema.
4. Check duplicate.
5. Persist event.
6. Normalize message.
7. Resolve customer.
8. Resolve conversation.
9. Publish event.
10. Trigger AI/routing.
11. Notify human agents where applicable.

---

## FR-004 — Parse Message

The system shall parse applicable:

* Text
* Media
* Location
* Contact
* Interactive payload
* Template interaction
* Reply context
* Provider metadata

---

## FR-005 — Store Message

Every valid message shall be persisted with:

```text
tenant_id
conversation_id
customer_id
provider_message_id
direction
message_type
content_metadata
timestamp
status
```

---

## FR-006 — Detect Intent

AI shall classify incoming messages.

Example:

```text
"I want to know the price."

→ sales_inquiry
```

```text
"My order has not arrived."

→ order_status
```

```text
"I want to speak to a human."

→ human_request
```

---

## FR-007 — Detect Sentiment

AI shall analyze sentiment and use the result as an input to routing and escalation.

---

## FR-008 — Detect Language

The system shall detect the customer's language.

---

## FR-009 — Generate Summary

For long conversations, AI shall generate an internal summary.

---

## FR-010 — Retrieve Knowledge

The AI shall search authorized knowledge sources before answering configured knowledge-dependent questions.

---

## FR-011 — Generate AI Response

The AI shall generate a response using:

```text
Current Message
+
Conversation Context
+
Customer Context
+
CRM Context
+
Ticket Context
+
Knowledge
+
Business Policies
```

---

## FR-012 — Validate AI Response

The system shall validate:

* Response schema
* Policy compliance
* Tool authorization
* Sensitive data rules
* Required approval
* Tenant policy
* Message constraints

---

## FR-013 — Send AI Response

If autonomous AI sending is permitted:

```text
AI Response
 ↓
Policy Validation
 ↓
Send
 ↓
Persist
 ↓
Track Status
 ↓
Audit
```

---

## FR-014 — Human Approval

If approval is required:

```text
AI Draft
 ↓
Human Approval Queue
 ├── Approve
 ├── Edit
 ├── Reject
 └── Escalate
```

---

## FR-015 — Human Takeover

When a human agent takes over:

```text
Conversation
 ↓
Lock AI Auto-Send
 ↓
Assign Agent
 ↓
Display Context
 ↓
Agent Response
```

---

## FR-016 — Agent Reply

The agent shall be able to:

* Send text
* Send supported media
* Use templates
* Reply to messages
* Add internal notes
* Trigger workflows

---

## FR-017 — Create Ticket

The system shall create tickets automatically based on:

* Intent
* Business rules
* AI recommendation
* Human action
* Customer request

---

## FR-018 — Assign Ticket

Tickets shall be assigned using:

* Team
* Skill
* Priority
* SLA
* Customer tier
* Workload

---

## FR-019 — Lead Creation

Qualified WhatsApp conversations shall be convertible into CRM leads.

---

## FR-020 — Opportunity Creation

Qualified leads shall be convertible into sales opportunities.

---

## FR-021 — CRM Activity

WhatsApp activities shall be recorded as CRM activities where configured.

---

## FR-022 — Follow-Up

The platform shall support configurable follow-up workflows.

---

## FR-023 — Template Selection

The AI/workflow engine shall select eligible templates based on:

* Intent
* Language
* Workflow
* Customer status
* Business policy

---

## FR-024 — Interactive Message

The system shall send supported interactive messages.

Example:

```text
How can we help?

[Support]
[Sales]
[Billing]
```

The selected action shall be mapped to a deterministic backend operation.

---

## FR-025 — Media Receive

The system shall:

```text
Receive Media
 ↓
Validate
 ↓
Retrieve
 ↓
Scan
 ↓
Store
 ↓
Process
 ↓
Associate With Conversation
```

---

## FR-026 — Voice Processing

Where enabled:

```text
Voice
 ↓
Transcription
 ↓
Intent
 ↓
Sentiment
 ↓
AI
 ↓
Response
```

---

## FR-027 — Image Processing

Where enabled:

```text
Image
 ↓
Security Scan
 ↓
Vision Model
 ↓
Entity Extraction
 ↓
Support/Sales Context
```

---

## FR-028 — Document Processing

Where enabled:

```text
Document
 ↓
Security Scan
 ↓
OCR / Parser
 ↓
Structured Extraction
 ↓
AI
 ↓
Conversation Context
```

---

## FR-029 — SLA Tracking

The system shall start SLA timers when eligible customer messages are received.

---

## FR-030 — SLA Escalation

The system shall automatically escalate conversations approaching or exceeding SLA thresholds.

---

## FR-031 — Customer Satisfaction

After resolution, eligible conversations may trigger customer satisfaction collection.

---

## FR-032 — Conversation Resolution

Agents and AI shall be able to mark conversations as resolved.

Resolution shall record:

* Resolver
* Resolution reason
* Resolution timestamp
* Resolution type
* AI/human involvement

---

## FR-033 — Conversation Reopen

A new customer message after resolution shall reopen the conversation according to tenant policy.

---

## FR-034 — AI Reopen Handling

If a resolved conversation is reopened, the system shall restore relevant historical context.

---

## FR-035 — Search

Authorized users shall search WhatsApp conversations using full-text and structured filters.

---

## FR-036 — Customer Timeline

The agent shall see the WhatsApp conversation alongside the customer's broader SalesGenie activity timeline.

---

## FR-037 — Analytics

The system shall calculate WhatsApp operational, AI, human, sales, and customer metrics.

---

## FR-038 — Audit

Every significant message, assignment, AI action, human action, workflow action, and integration change shall produce an audit record.

---

## FR-039 — Notification

The system shall notify appropriate users for:

* New conversation
* Assignment
* Escalation
* SLA warning
* SLA breach
* AI approval
* Failed message
* Provider outage

---

## FR-040 — Retry

Transient outbound failures shall be retried using controlled backoff.

---

## FR-041 — Dead Letter

Repeatedly failed events shall enter a dead-letter queue.

---

## FR-042 — Replay

Authorized operators shall be able to replay failed events.

---

## FR-043 — Duplicate Prevention

Duplicate provider events shall not create duplicate business actions.

---

## FR-044 — AI Loop Prevention

The system shall detect and suppress automated AI-to-AI or AI-to-automation messaging loops.

---

## FR-045 — Permission Enforcement

Every protected operation shall be authorized server-side.

The frontend shall never be treated as the security boundary.

---

## FR-046 — Tenant Enforcement

Every protected WhatsApp operation shall enforce tenant ownership.

---

## FR-047 — AI Tool Authorization

Before any AI tool call:

```text
AI Request
 ↓
User/Tenant Permissions
 ↓
Tool Permission
 ↓
Risk Policy
 ↓
Approval
 ↓
Execution
 ↓
Audit
```

---

## FR-048 — Business Rule Engine

Organizations shall be able to configure rules without changing application code.

Example:

```text
IF customer.tier = enterprise
AND intent = technical_support
THEN route enterprise_technical_team
```

---

## FR-049 — Automation Control

Administrators shall be able to enable or disable:

* AI auto-response
* AI escalation
* Human approval
* Automated follow-up
* Automated ticket creation
* Automated lead creation
* Automated CRM updates

---

## FR-050 — Channel Health

Administrators shall be able to view:

* Connection status
* Webhook status
* Last successful event
* Last failed event
* Message failures
* Provider errors
* Queue depth
* Processing latency

---

## 100. Example End-to-End AI Support Flow

```text
Customer:
"My order has not arrived yet."

             ↓

WhatsApp Webhook

             ↓

Message Persistence

             ↓

Customer Identity

             ↓

Conversation Resolution

             ↓

AI Intent

order_status

             ↓

CRM / Order Lookup

             ↓

Order Found

             ↓

Knowledge / Policy

             ↓

AI Response

"Your order is currently in transit
and is expected to arrive tomorrow."

             ↓

Policy Validation

             ↓

WhatsApp Send

             ↓

Delivery Tracking

             ↓

Conversation Update

             ↓

Analytics

             ↓

Audit
```

---

## 101. Example Human Escalation Flow

```text
Customer:
"I've contacted you three times and
nobody has solved this."

             ↓

Sentiment Detection

             ↓

High Frustration

             ↓

Priority Increase

             ↓

Escalation Rule

             ↓

Human Support Queue

             ↓

Agent Assignment

             ↓

AI Summary

             ↓

Customer 360

             ↓

Human Response

             ↓

Resolution

             ↓

Customer Satisfaction

             ↓

Analytics
```

---

## 102. Example Sales Flow

```text
Customer:
"How much does the enterprise plan cost?
Can I schedule a demo?"

             ↓

AI Intent

sales_inquiry
demo_request

             ↓

Lead Detection

             ↓

Lead Score

             ↓

CRM Lead

             ↓

Sales Routing

             ↓

Senior Sales Agent

             ↓

AI Sales Recommendation

             ↓

Human Approval

             ↓

WhatsApp Response

             ↓

Demo Scheduled

             ↓

CRM Opportunity

             ↓

Revenue Attribution
```

---

## 103. Example Hybrid Flow

```text
Customer
   ↓
WhatsApp
   ↓
AI Support
   ↓
Knowledge Retrieval
   ↓
AI Draft
   ↓
Human Approval
   ↓
Human Edits
   ↓
WhatsApp Send
   ↓
Customer
   ↓
Follow-Up
   ↓
AI Resumes
```

---

## 104. Example Emergency Flow

```text
Customer Message
       ↓
AI Classification
       ↓
High Risk
       ↓
Security / Legal / Financial
       ↓
Autonomous AI Disabled
       ↓
Priority Escalation
       ↓
Specialist Team
       ↓
Human Approval
       ↓
Customer Response
       ↓
Audit
```

---

## 105. Acceptance Criteria

## AC-001 — New WhatsApp Conversation

Given a new customer sends a WhatsApp message:

```text
Message received
→ Customer identified
→ Conversation created
→ Intent detected
→ Priority calculated
→ Routing completed
```

---

## AC-002 — Existing Conversation

Given a known customer sends another message:

```text
Message
→ Existing Customer
→ Existing Conversation
→ Existing Context
```

No duplicate customer or unnecessary conversation shall be created.

---

## AC-003 — AI Support

Given a low-risk supported question:

```text
Message
→ Intent
→ RAG
→ AI Response
→ Policy Validation
→ Send
→ Audit
```

---

## AC-004 — Human Request

Given a customer requests a human:

```text
Message
→ Human Intent
→ AI Auto-Send Disabled
→ Human Queue
→ Agent Assignment
→ Agent Response
```

---

## AC-005 — Low Confidence

Given AI confidence is below the configured threshold:

```text
Message
→ AI Analysis
→ Low Confidence
→ Human Escalation
```

---

## AC-006 — Human Takeover

Given an agent takes control:

```text
AI Conversation
→ Human Takeover
→ AI Auto-Send Disabled
→ Agent Receives Context
→ Agent Replies
```

---

## AC-007 — AI Resume

Given the human agent returns the conversation to AI:

```text
Human Mode
→ Policy Check
→ AI Enabled
→ Future Message
→ AI Processing
```

---

## AC-008 — Duplicate Webhook

Given the same webhook event arrives twice:

```text
Webhook #1 → Process
Webhook #2 → Detect Duplicate
```

Expected:

```text
No duplicate message
No duplicate ticket
No duplicate lead
No duplicate AI response
No duplicate workflow
```

---

## AC-009 — Provider Failure

Given outbound sending fails transiently:

```text
Send
→ Failure
→ Retry
→ Send
→ Status Updated
```

If retries are exhausted:

```text
Dead Letter
→ Alert
→ Operator Review
```

---

## AC-010 — Media

Given a customer sends an image:

```text
Image
→ Validate
→ Secure Storage
→ Scan
→ AI Vision if enabled
→ Conversation Context
```

---

## AC-011 — SLA Breach

Given a conversation approaches SLA breach:

```text
SLA Warning
→ Agent Notification
→ Priority Increase
→ Escalation if required
```

---

## AC-012 — Cross-Channel Identity

Given the same customer previously interacted through email and then WhatsApp:

```text
Email Identity
        +
WhatsApp Identity
        ↓
Customer Identity Resolver
        ↓
Same Customer Profile
```

provided identity confidence satisfies the configured threshold.

---

## 106. Non-Functional Quality Targets

| Category        | Requirement                            |
| --------------- | -------------------------------------- |
| Availability    | Enterprise-grade high availability     |
| Scalability     | Horizontal scaling                     |
| Reliability     | Durable event processing               |
| Security        | Encryption + least privilege           |
| Isolation       | Strict tenant isolation                |
| AI Safety       | Policy + approval + tool authorization |
| Performance     | Asynchronous processing                |
| Observability   | Metrics + logs + tracing               |
| Recovery        | Replay + retry + DLQ                   |
| Auditability    | Immutable audit records                |
| Accessibility   | WCAG-aligned UI                        |
| Maintainability | Provider abstraction                   |
| Extensibility   | Event-driven architecture              |
| Cost Control    | Usage metering and AI budgets          |

---

## 107. FAANG-Level Engineering Principles

The WhatsApp Channel shall follow these principles:

1. WhatsApp is a first-class SalesGenie channel.
2. Provider-specific implementation shall remain isolated behind an abstraction layer.
3. Every inbound event shall be idempotent.
4. Every outbound action shall have an idempotency strategy.
5. Webhook ingestion shall never wait for LLM processing.
6. AI shall never receive unrestricted permissions.
7. Customer messages shall always be treated as untrusted input.
8. Human takeover shall override autonomous AI behavior.
9. High-risk actions shall support human approval.
10. Tenant isolation shall be enforced server-side.
11. Customer identity shall be separated from channel identity.
12. Conversation state shall be independent of provider implementation.
13. AI context shall be permission-aware.
14. RAG retrieval shall be tenant- and ACL-aware.
15. Media shall be treated as untrusted input.
16. Provider outages shall not silently lose accepted events.
17. All important actions shall be auditable.
18. All asynchronous operations shall be observable.
19. AI failure shall have deterministic fallback behavior.
20. Automated messaging shall have loop prevention.
21. Outbound automation shall have rate and quota controls.
22. Business rules shall be configurable.
23. Human agents shall have complete AI-generated context during escalation.
24. AI shall not silently modify authoritative business records.
25. Analytics shall use source-of-truth business events.
26. Security controls shall exist independently of prompts.
27. Frontend permissions shall never replace backend authorization.
28. The architecture shall support future messaging providers.
29. The system shall degrade gracefully when dependent services fail.
30. WhatsApp interactions shall contribute to SalesGenie's unified customer and business intelligence layer.

---

## 108. Reference Architecture

```text
                         CUSTOMER
                            │
                            ▼
                   ┌─────────────────┐
                   │    WHATSAPP     │
                   │ BUSINESS PLATFORM│
                   └────────┬────────┘
                            │
                            ▼
                   ┌─────────────────┐
                   │ WHATSAPP GATEWAY│
                   └────────┬────────┘
                            │
                            ▼
                   ┌─────────────────┐
                   │ WEBHOOK SERVICE │
                   │ Verify/Validate │
                   └────────┬────────┘
                            │
                            ▼
                   ┌─────────────────┐
                   │ WHATSAPP SERVICE│
                   │ Parse/Normalize │
                   └────────┬────────┘
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
      ┌────────────┐ ┌────────────┐ ┌────────────┐
      │  IDENTITY  │ │ CONVERSATION│ │   MEDIA    │
      │  RESOLVER  │ │   SERVICE   │ │   SERVICE  │
      └──────┬─────┘ └──────┬─────┘ └──────┬─────┘
             │              │              │
             └──────────────┼──────────────┘
                            ▼
                     ┌─────────────┐
                     │  EVENT BUS  │
                     └──────┬──────┘
                            │
       ┌────────────────────┼────────────────────┐
       ▼                    ▼                    ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  AI GATEWAY  │     │   ROUTING    │     │   TICKETING  │
└──────┬───────┘     └──────┬───────┘     └──────┬───────┘
       │                    │                    │
       ▼                    ▼                    ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ RAG / MEMORY │     │ HUMAN AGENTS │     │     SLA      │
└──────┬───────┘     └──────┬───────┘     └──────┬───────┘
       │                    │                    │
       └────────────────────┼────────────────────┘
                            ▼
                   ┌─────────────────┐
                   │ AI/HUMAN POLICY │
                   │     ENGINE      │
                   └────────┬────────┘
                            │
                    ┌───────┴────────┐
                    ▼                ▼
             ┌─────────────┐  ┌─────────────┐
             │ AI RESPONSE │  │ HUMAN AGENT │
             └──────┬──────┘  └──────┬──────┘
                    │                │
                    └───────┬────────┘
                            ▼
                    ┌─────────────┐
                    │   POLICY    │
                    │   ENGINE    │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │ OUTBOUND    │
                    │ WHATSAPP    │
                    │ SERVICE     │
                    └──────┬──────┘
                           │
                           ▼
                       WHATSAPP
                           │
                           ▼
                        CUSTOMER
```

---

## 109. End-to-End Business Architecture

```text
                     WHATSAPP
                         │
                         ▼
                 CUSTOMER MESSAGE
                         │
                         ▼
                 IDENTITY RESOLUTION
                         │
                         ▼
                 CONVERSATION MEMORY
                         │
                         ▼
                  AI UNDERSTANDING
             ┌───────────┼───────────┐
             ▼           ▼           ▼
          Intent      Sentiment    Priority
             │           │           │
             └───────────┼───────────┘
                         ▼
                   ROUTING ENGINE
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
       AI ONLY        HYBRID          HUMAN
          │              │              │
          ▼              ▼              ▼
        RAG          AI DRAFT       AGENT
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                  POLICY ENGINE
                         │
                         ▼
                     RESPONSE
                         │
                         ▼
                    WHATSAPP
                         │
                         ▼
                    CUSTOMER
                         │
                         ▼
                 BUSINESS OUTCOME
                  ┌──────┼───────┐
                  ▼      ▼       ▼
               Support  Sales  Retention
                  │      │       │
                  └──────┼───────┘
                         ▼
                      ANALYTICS
                         │
                         ▼
                 BUSINESS INTELLIGENCE
```

---

## 110. Final Product Outcome

The completed SalesGenie WhatsApp Channel shall provide an enterprise-grade AI + human conversational system capable of transforming WhatsApp interactions into:

* Customer support resolutions
* Tickets
* Leads
* Opportunities
* Sales conversations
* Customer insights
* Workflow executions
* Automated notifications
* Human escalations
* Customer satisfaction signals
* Revenue opportunities
* Retention signals
* Business intelligence

The final product shall therefore operate as:

```text
WHATSAPP
    ↓
CUSTOMER IDENTITY
    ↓
CONVERSATION MEMORY
    ↓
AI INTELLIGENCE
    ↓
BUSINESS CONTEXT
    ↓
ROUTING
    ↓
AI / HUMAN / HYBRID
    ↓
KNOWLEDGE + CRM + TICKETING
    ↓
WORKFLOW
    ↓
ACTION
    ↓
RESOLUTION / CONVERSION
    ↓
ANALYTICS
    ↓
BUSINESS OUTCOME
```

The WhatsApp Channel shall be a core component of SalesGenie's broader omnichannel architecture rather than an independent messaging feature.
