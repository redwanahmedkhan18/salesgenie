# SalesGenie — WhatsApp Integration

## FAANG-Level User Requirements, System Requirements & Functional Requirements

**Document:** `whatsapp_integration.md`  
**Platform:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Integration Domain:** WhatsApp Business Platform  
**Architecture:** Enterprise Microservices + Multi-Agent AI + Event-Driven Architecture + RAG + Workflow Automation + MCP + Omnichannel Messaging

---

## 1. Purpose

The WhatsApp Integration SHALL enable SalesGenie organizations to connect supported WhatsApp Business accounts and provide enterprise-grade customer support, sales engagement, lead generation, conversational AI, human-agent operations, workflow automation, CRM synchronization, analytics, security, and governance.

The integration SHALL support, subject to the capabilities, permissions, policies, and limitations of the applicable WhatsApp Business/Meta APIs:

- WhatsApp Business account connection
- Business phone number management
- Customer identity resolution
- Two-way messaging
- Text messages
- Supported media messages
- Documents
- Images
- Videos
- Audio
- Location
- Contacts
- Interactive messages
- Message templates
- Template management
- Template validation/status tracking
- Delivery receipts
- Read receipts
- Conversation synchronization
- AI customer support
- AI sales agents
- Human support agents
- AI-to-human escalation
- Human-to-AI handoff
- Lead generation
- Lead qualification
- Lead scoring
- Customer segmentation
- Intent detection
- Sentiment analysis
- Language detection
- RAG-powered responses
- Workflow triggers
- Workflow actions
- CRM synchronization
- Notifications
- SLA management
- Analytics
- Audit logging
- Integration monitoring
- Rate-limit management
- Retry handling
- Dead-letter processing
- Reconciliation
- MCP tool access
- Multi-tenant isolation
- Enterprise RBAC

---

## 2. Product Scope

## 2.1 In Scope

The WhatsApp integration SHALL provide:

1. Secure WhatsApp Business authorization
2. Business account discovery
3. Phone-number discovery
4. Multiple WhatsApp account support
5. Multiple business phone-number support
6. Account-level configuration
7. Message ingestion
8. Message normalization
9. Message delivery tracking
10. Outbound messaging
11. Template messaging
12. Media handling
13. Interactive messaging where supported
14. Conversation management
15. Customer identity resolution
16. AI intent classification
17. AI sentiment analysis
18. AI language detection
19. AI entity extraction
20. AI lead scoring
21. AI lead qualification
22. AI response generation
23. RAG knowledge retrieval
24. Human-agent responses
25. Human takeover
26. AI resume
27. Human escalation
28. Lead creation
29. CRM synchronization
30. Workflow automation
31. Team routing
32. Agent assignment
33. SLA management
34. Integration health monitoring
35. Rate-limit protection
36. Error handling
37. Retry processing
38. Dead-letter queues
39. Reconciliation
40. Analytics
41. Security
42. Auditability
43. MCP integration
44. Super-admin monitoring

---

## 3. Actors

## 3.1 WhatsApp Customer

An external customer communicating with an organization's WhatsApp Business number.

## 3.2 Sales Agent

A human responsible for converting WhatsApp prospects into qualified leads, opportunities, and customers.

## 3.3 Support Agent

A human responsible for resolving customer-support conversations.

## 3.4 Manager

A user responsible for team performance, routing, SLA management, and analytics.

## 3.5 Organization Administrator

A tenant administrator responsible for WhatsApp integrations, users, agents, workflows, policies, and configuration.

## 3.6 Super Administrator

A platform-level administrator responsible for governance, security, reliability, compliance, and tenant-wide integration oversight.

## 3.7 AI Sales Agent

An autonomous or semi-autonomous SalesGenie agent responsible for approved WhatsApp sales interactions.

## 3.8 AI Support Agent

An AI agent responsible for resolving eligible WhatsApp support requests.

## 3.9 Workflow Engine

The automation engine responsible for executing workflows triggered by WhatsApp events.

## 3.10 Integration Service

The microservice responsible for WhatsApp API communication, authentication, webhooks, synchronization, rate limiting, retries, and provider-specific operations.

---

## 4. User Requirements

## UR-WA-001 — WhatsApp Business Connection

Authorized administrators SHALL be able to connect supported WhatsApp Business accounts to SalesGenie.

## UR-WA-002 — Secure Authorization

Administrators SHALL be able to authorize WhatsApp Business access using a secure provider authorization process.

## UR-WA-003 — Business Account Discovery

SalesGenie SHALL discover supported WhatsApp Business accounts associated with the authorized context.

## UR-WA-004 — Phone Number Discovery

SalesGenie SHALL discover eligible business phone numbers.

## UR-WA-005 — Phone Number Selection

Administrators SHALL be able to select which WhatsApp business phone numbers are managed by SalesGenie.

## UR-WA-006 — Multiple Accounts

Organizations SHALL be able to connect multiple WhatsApp Business accounts.

## UR-WA-007 — Multiple Numbers

Organizations SHALL be able to manage multiple business phone numbers.

## UR-WA-008 — Account Isolation

Each WhatsApp account and phone number SHALL remain isolated by organization and integration context.

## UR-WA-009 — Integration Dashboard

Administrators SHALL be able to view:

- WhatsApp Business account
- Business phone number
- Display name
- Connection status
- Authorization status
- Webhook status
- Messaging status
- AI status
- Assigned teams
- Assigned agents
- Last synchronization
- Last successful API request
- Integration health

## UR-WA-010 — Unified Inbox

Users SHALL be able to manage WhatsApp conversations through the SalesGenie unified inbox.

## UR-WA-011 — Conversation History

Authorized users SHALL be able to view available WhatsApp conversation history.

## UR-WA-012 — Real-Time Messages

Incoming WhatsApp messages SHALL appear in near real time.

## UR-WA-013 — Human Response

Authorized human agents SHALL be able to respond to WhatsApp customers.

## UR-WA-014 — AI Response

Organizations SHALL be able to enable AI handling for eligible WhatsApp conversations.

## UR-WA-015 — Human Takeover

Human agents SHALL be able to take over AI-managed conversations.

## UR-WA-016 — AI Resume

Authorized agents SHALL be able to return eligible conversations to AI handling.

## UR-WA-017 — Human Escalation

AI SHALL escalate conversations according to configured policies.

## UR-WA-018 — Lead Detection

SalesGenie SHALL detect potential leads from WhatsApp interactions.

## UR-WA-019 — Lead Qualification

AI SHALL qualify WhatsApp leads according to configurable criteria.

## UR-WA-020 — Lead Scoring

SalesGenie SHALL calculate configurable lead scores.

## UR-WA-021 — CRM Synchronization

Organizations SHALL be able to synchronize WhatsApp contacts, leads, and opportunities with supported CRM systems.

## UR-WA-022 — Customer Profile

Agents SHALL be able to view relevant customer context.

## UR-WA-023 — Intent Detection

SalesGenie SHALL detect customer intent.

## UR-WA-024 — Sentiment Detection

SalesGenie SHALL detect customer sentiment.

## UR-WA-025 — Language Detection

SalesGenie SHALL detect supported conversation languages.

## UR-WA-026 — Personalized Responses

AI SHALL generate context-aware responses using authorized customer and organizational context.

## UR-WA-027 — RAG Grounding

AI SHALL use configured knowledge bases when knowledge-grounded responses are required.

## UR-WA-028 — Routing

Administrators SHALL be able to route WhatsApp conversations to AI agents, human agents, or teams.

## UR-WA-029 — Assignment

Managers SHALL be able to assign and reassign conversations.

## UR-WA-030 — Tags

Authorized users SHALL be able to tag WhatsApp conversations.

## UR-WA-031 — Priority

Authorized users SHALL be able to change conversation priority.

## UR-WA-032 — Search

Users SHALL be able to search WhatsApp conversations.

## UR-WA-033 — Filtering

Users SHALL be able to filter conversations by:

- WhatsApp account
- Phone number
- Agent
- Team
- AI agent
- Status
- Priority
- Intent
- Sentiment
- Lead status
- Language
- Tags
- Date
- Customer

## UR-WA-034 — Notifications

Agents SHALL receive notifications for assigned and escalated conversations.

## UR-WA-035 — SLA

Managers SHALL be able to configure WhatsApp response and resolution SLAs.

## UR-WA-036 — Analytics

Managers SHALL be able to analyze WhatsApp support, sales, AI, and operational performance.

## UR-WA-037 — Integration Health

Administrators SHALL be able to determine whether the WhatsApp integration is operational.

## UR-WA-038 — Failure Visibility

Administrators SHALL be able to inspect:

- Authentication failures
- Authorization failures
- Webhook failures
- Provider API failures
- Rate-limit events
- Message failures
- Template failures
- CRM synchronization failures
- Workflow failures

## UR-WA-039 — Reauthorization

Administrators SHALL be able to reauthorize disconnected or invalid integrations.

## UR-WA-040 — Disconnect

Authorized administrators SHALL be able to disconnect WhatsApp integrations.

---

## 5. AI User Requirements

## UR-AI-WA-001 — Conversation Understanding

AI SHALL understand WhatsApp conversations using authorized conversation context.

## UR-AI-WA-002 — Intent Classification

AI SHALL classify intents such as:

```text
product_inquiry
pricing_inquiry
purchase_intent
product_availability
order_status
order_issue
technical_support
refund_request
complaint
appointment_request
human_agent_request
general_inquiry
spam
other
```

## UR-AI-WA-003 — Entity Extraction

AI SHALL extract:

```text
customer_name
product
service
quantity
budget
location
order_id
company
job_role
date
purchase_timeline
```

## UR-AI-WA-004 — Lead Qualification

AI SHALL determine lead qualification using configured business rules.

## UR-AI-WA-005 — Lead Scoring

AI SHALL calculate lead scores using configurable signals.

## UR-AI-WA-006 — Buying Intent

AI SHALL estimate purchase intent.

## UR-AI-WA-007 — Customer Segmentation

AI SHALL classify customers into configurable segments.

Example:

```text
prospect
high_intent_prospect
existing_customer
vip_customer
enterprise_prospect
support_customer
spam
unknown
```

## UR-AI-WA-008 — Sentiment

AI SHALL classify:

```text
positive
neutral
negative
angry
frustrated
urgent
```

## UR-AI-WA-009 — Language

AI SHALL identify the conversation language.

## UR-AI-WA-010 — Response Recommendation

AI SHALL recommend responses to human agents.

## UR-AI-WA-011 — Autonomous Response

AI SHALL respond autonomously only when permitted by organization policy.

## UR-AI-WA-012 — Confidence

The platform SHALL calculate AI confidence before configured autonomous actions.

## UR-AI-WA-013 — Escalation

AI SHALL escalate when:

* Confidence is below threshold
* Customer requests a human
* Sentiment becomes highly negative
* Sensitive actions are requested
* Required knowledge is unavailable
* Policy restrictions apply
* Repeated AI failures occur
* High-value leads require human intervention
* Organization rules require approval

## UR-AI-WA-014 — Guardrails

AI SHALL obey:

* System policies
* Organization policies
* Brand policies
* Channel policies
* RBAC
* Tool permissions
* Workflow policies
* Approval requirements
* Data-access policies

## UR-AI-WA-015 — Tool Authorization

AI SHALL never directly execute privileged WhatsApp operations without authorization.

---

## 6. Human-Agent Requirements

## UR-HUMAN-WA-001 — Unified Inbox

Human agents SHALL manage WhatsApp conversations from the SalesGenie unified inbox.

## UR-HUMAN-WA-002 — Customer Context

Agents SHALL see:

* Customer profile
* Conversation history
* Intent
* Sentiment
* Lead score
* Qualification status
* AI summary
* Recommended response
* Relevant knowledge

## UR-HUMAN-WA-003 — Human Reply

Agents SHALL be able to send supported WhatsApp messages.

## UR-HUMAN-WA-004 — AI Assistance

Agents SHALL be able to request AI-generated response suggestions.

## UR-HUMAN-WA-005 — AI Editing

Agents SHALL be able to edit AI-generated responses.

## UR-HUMAN-WA-006 — AI Rejection

Agents SHALL be able to reject AI recommendations.

## UR-HUMAN-WA-007 — Internal Notes

Agents SHALL be able to create internal notes.

## UR-HUMAN-WA-008 — Takeover

Agents SHALL be able to take over conversations from AI.

## UR-HUMAN-WA-009 — Escalation

Agents SHALL be able to escalate conversations to:

* Senior agent
* Manager
* Specialized team
* Support team
* Sales team

## UR-HUMAN-WA-010 — Lead Conversion

Sales agents SHALL be able to convert qualified WhatsApp leads into opportunities and customers.

---

## 7. System Requirements

## SR-WA-001 — Microservice Architecture

The WhatsApp integration SHALL operate as an independently deployable service/component.

## SR-WA-002 — Provider Adapter

WhatsApp-specific functionality SHALL be isolated behind a provider adapter.

## SR-WA-003 — API Gateway

External integration APIs SHALL pass through controlled API gateway boundaries.

## SR-WA-004 — Tenant Isolation

Every WhatsApp resource SHALL contain organization context.

```text
organization_id
    ↓
integration_id
    ↓
whatsapp_business_account_id
    ↓
phone_number_id
    ↓
conversation_id
    ↓
message_id
```

## SR-WA-005 — Credential Encryption

Credentials and access tokens SHALL:

* Be encrypted at rest
* Be transmitted securely
* Never be exposed to frontend clients
* Never be logged
* Be stored in secure secret storage
* Be access-controlled

## SR-WA-006 — Webhook Verification

Incoming webhook requests SHALL be verified according to applicable WhatsApp/Meta requirements.

## SR-WA-007 — Webhook Authenticity

Webhook payload authenticity SHALL be validated before processing.

## SR-WA-008 — Idempotency

The system SHALL process provider events idempotently.

Duplicate events SHALL NOT create duplicate:

* Messages
* Conversations
* Leads
* Tickets
* CRM records
* Workflow executions

## SR-WA-009 — Event-Driven Architecture

The integration SHALL use asynchronous event processing.

```text
WhatsApp / Meta
       ↓
Webhook Gateway
       ↓
Webhook Verification
       ↓
Event Normalizer
       ↓
Event Bus
       ↓
WhatsApp Integration Processor
       ↓
AI / Human / Workflow / CRM
```

## SR-WA-010 — Queue Processing

Queues SHALL support:

* Webhook events
* Message processing
* AI inference
* Lead scoring
* CRM synchronization
* Workflow execution
* Retry processing

## SR-WA-011 — Dead-Letter Queue

Events exceeding retry limits SHALL enter a dead-letter queue.

## SR-WA-012 — Rate Limiting

The system SHALL enforce provider-aware rate limiting.

## SR-WA-013 — Backpressure

The system SHALL support backpressure during high-volume events.

## SR-WA-014 — Circuit Breaker

Repeated provider failures SHALL activate circuit-breaker behavior.

## SR-WA-015 — Retry

Transient failures SHALL use exponential backoff with jitter.

## SR-WA-016 — API Versioning

The provider API version SHALL be explicitly managed.

## SR-WA-017 — Capability Detection

The platform SHALL determine whether a requested WhatsApp operation is supported by:

* Account
* Phone number
* Provider API version
* Permissions
* Message type
* Provider policies

## SR-WA-018 — Canonical Data Model

Provider-specific payloads SHALL be converted into SalesGenie's canonical data models.

## SR-WA-019 — Message Model

```text
CanonicalMessage
├── message_id
├── external_message_id
├── organization_id
├── integration_id
├── channel
├── business_account_id
├── phone_number_id
├── conversation_id
├── sender
├── recipient
├── message_type
├── content
├── attachments
├── direction
├── delivery_status
├── timestamp
├── metadata
└── correlation_id
```

## SR-WA-020 — Conversation Model

WhatsApp conversations SHALL map to the platform's canonical conversation model.

## SR-WA-021 — Event Ordering

The system SHALL preserve event ordering where business correctness requires it.

## SR-WA-022 — Reconciliation

The platform SHALL support reconciliation for missing or inconsistent data.

## SR-WA-023 — Auditability

Security-sensitive and administrative operations SHALL generate immutable audit events.

## SR-WA-024 — Observability

The integration SHALL expose:

* Metrics
* Structured logs
* Distributed traces
* Health checks
* Queue metrics
* Provider API metrics
* Error metrics
* Webhook metrics

---

## 8. WhatsApp Account Management

## FR-WA-001 — Create Integration

Authorized administrators SHALL be able to create a WhatsApp integration.

## FR-WA-002 — Start Authorization

The system SHALL initiate the supported Meta/WhatsApp authorization flow.

## FR-WA-003 — Callback Processing

The system SHALL securely process authorization callbacks.

## FR-WA-004 — Validate Authorization

The system SHALL validate authorization before activation.

## FR-WA-005 — Discover Business Accounts

The system SHALL retrieve supported WhatsApp Business accounts.

## FR-WA-006 — Discover Phone Numbers

The system SHALL retrieve eligible business phone numbers.

## FR-WA-007 — Select Phone Numbers

Administrators SHALL select which phone numbers SalesGenie manages.

## FR-WA-008 — Configure Webhooks

The system SHALL configure required webhook subscriptions.

## FR-WA-009 — Health Check

The integration SHALL perform post-connection health checks.

## FR-WA-010 — Activation

The integration SHALL only enter ACTIVE state after required validation succeeds.

---

## 9. Phone Number Management

## FR-WA-011 — Phone Number Inventory

SalesGenie SHALL maintain an inventory of connected business phone numbers.

## FR-WA-012 — Number Metadata

The system SHALL store supported:

* Phone number identifier
* Display name
* Business account
* Status
* Messaging capability
* Webhook state
* AI configuration

## FR-WA-013 — Enable/Disable

Administrators SHALL be able to enable or disable a phone number.

## FR-WA-014 — Agent Mapping

Administrators SHALL be able to map numbers to:

* AI agents
* Sales teams
* Support teams
* Human agents
* Workflows

## FR-WA-015 — Number-Level Policy

Organizations SHALL be able to configure AI and routing policies per number.

---

## 10. Messaging Requirements

## FR-WA-016 — Incoming Message Ingestion

The system SHALL ingest supported incoming WhatsApp messages.

## FR-WA-017 — Message Validation

Incoming messages SHALL be validated before processing.

## FR-WA-018 — Message Normalization

Provider messages SHALL be converted to canonical SalesGenie messages.

## FR-WA-019 — Customer Resolution

The system SHALL resolve the sender against an existing customer identity where possible.

## FR-WA-020 — Conversation Resolution

The system SHALL resolve the appropriate conversation.

## FR-WA-021 — Conversation Creation

If no matching conversation exists, SalesGenie SHALL create one.

## FR-WA-022 — Message Persistence

Messages SHALL be persisted according to retention policies.

## FR-WA-023 — Conversation Update

The system SHALL update:

* Last message
* Customer
* Intent
* Sentiment
* Assignment
* Priority
* Tags
* Lead state
* AI state

## FR-WA-024 — Outbound Message

Authorized humans and AI agents SHALL be able to send supported outbound messages.

## FR-WA-025 — Delivery Tracking

The system SHALL track supported message lifecycle states.

Example:

```text
queued
submitted
sent
delivered
read
failed
```

## FR-WA-026 — Message Failure

Failed outbound messages SHALL expose actionable failure information to authorized users.

---

## 11. WhatsApp Message Types

Where supported by the provider and account configuration, SalesGenie SHALL support:

```text
text
image
video
audio
document
sticker
location
contact
interactive
template
reaction
system_event
```

Unsupported message types SHALL be gracefully represented without corrupting the conversation.

---

## 12. Media Handling

## FR-WA-027 — Media Detection

The system SHALL detect supported media attachments.

## FR-WA-028 — Secure Media Retrieval

Media SHALL be retrieved through authorized provider mechanisms.

## FR-WA-029 — Malware Protection

Uploaded or retrieved files SHALL be evaluated according to the platform's file-security policy.

## FR-WA-030 — Media Storage

Media SHALL be stored only when required and permitted.

## FR-WA-031 — Media Access Control

Media SHALL inherit conversation and tenant authorization.

## FR-WA-032 — Media Expiration

Temporary media URLs and cached assets SHALL expire according to configured security policies.

## FR-WA-033 — AI Media Processing

Eligible media SHALL be processed by AI services where enabled.

Examples:

```text
OCR
image understanding
document extraction
audio transcription
video analysis
```

---

## 13. WhatsApp Template Management

## FR-WA-034 — Template Inventory

SalesGenie SHALL maintain an inventory of available WhatsApp message templates where accessible.

## FR-WA-035 — Template Status

The platform SHALL track supported template statuses.

## FR-WA-036 — Template Categories

The platform SHALL represent provider-supported template categories.

## FR-WA-037 — Template Variables

Users SHALL be able to map dynamic variables to template parameters.

Example:

```text
{{customer_name}}
{{order_id}}
{{appointment_date}}
{{product_name}}
```

## FR-WA-038 — Template Validation

SalesGenie SHALL validate required template parameters before sending.

## FR-WA-039 — Template Selection

AI and human agents SHALL only use templates permitted by organization and provider policy.

## FR-WA-040 — Template Analytics

The platform SHALL track supported template usage and outcomes.

---

## 14. AI Processing

## FR-WA-041 — Intent Detection

The AI layer SHALL classify WhatsApp customer intent.

## FR-WA-042 — Sentiment Detection

The AI layer SHALL classify customer sentiment.

## FR-WA-043 — Language Detection

The AI layer SHALL detect the conversation language.

## FR-WA-044 — Entity Extraction

AI SHALL extract structured business entities.

## FR-WA-045 — Conversation Summary

AI SHALL generate structured summaries.

## FR-WA-046 — RAG Retrieval

The AI agent SHALL retrieve relevant authorized knowledge.

## FR-WA-047 — Response Generation

AI SHALL generate context-aware WhatsApp responses.

## FR-WA-048 — Response Validation

Generated responses SHALL pass validation before transmission.

## FR-WA-049 — Policy Validation

AI responses SHALL pass organizational policy checks.

## FR-WA-050 — Confidence Evaluation

The system SHALL calculate response confidence.

## FR-WA-051 — Escalation

Low-confidence or restricted interactions SHALL be escalated.

---

## 15. AI Sales Automation

## FR-WA-052 — Lead Identification

AI SHALL identify potential sales leads.

## FR-WA-053 — Qualification

AI SHALL qualify leads.

## FR-WA-054 — Lead Scoring

AI SHALL score leads.

Conceptual model:

```text
Lead Score =
    Intent Score
  + Engagement Score
  + Qualification Score
  + Business Fit Score
  + Behavioral Score
  - Spam/Risk Score
```

## FR-WA-055 — Product Interest

AI SHALL identify products or services of interest.

## FR-WA-056 — Buying Timeline

AI SHALL estimate purchasing timeline when sufficient evidence exists.

## FR-WA-057 — Budget Extraction

AI SHALL extract budget information when explicitly provided.

## FR-WA-058 — Sales Routing

High-value or high-intent leads SHALL be routed to appropriate sales teams.

## FR-WA-059 — Follow-Up

AI SHALL initiate configured follow-up workflows subject to provider and organization policies.

---

## 16. Customer Support Automation

## FR-WA-060 — Support Intent

AI SHALL identify customer-support requests.

## FR-WA-061 — FAQ Resolution

AI SHALL resolve supported FAQs using approved knowledge sources.

## FR-WA-062 — Order Support

Where connected systems provide authorized information, AI SHALL retrieve order information.

## FR-WA-063 — Ticket Creation

AI or workflows SHALL create support tickets when required.

## FR-WA-064 — Escalation

Complex support requests SHALL be routed to human agents.

## FR-WA-065 — Complaint Handling

High-severity complaints SHALL receive configurable priority.

---

## 17. Human-in-the-Loop

## FR-WA-066 — Approval Queue

The platform SHALL provide human approval queues for restricted AI actions.

## FR-WA-067 — Approval Context

Approval requests SHALL include:

```text
customer_context
conversation_summary
proposed_message
intent
sentiment
lead_score
ai_confidence
reason
risk_level
knowledge_context
```

## FR-WA-068 — Approve

Authorized users SHALL approve proposed AI actions.

## FR-WA-069 — Reject

Authorized users SHALL reject proposed AI actions.

## FR-WA-070 — Edit

Authorized users SHALL edit AI-generated responses before sending.

## FR-WA-071 — Audit

Approval decisions SHALL be auditable.

---

## 18. Workflow Integration

WhatsApp SHALL function as both a workflow event source and an action destination where provider capabilities permit.

## FR-WA-072 — Message Trigger

```text
whatsapp.message.received
```

## FR-WA-073 — Conversation Triggers

```text
whatsapp.conversation.created
whatsapp.conversation.updated
whatsapp.conversation.escalated
whatsapp.conversation.resolved
```

## FR-WA-074 — Delivery Triggers

```text
whatsapp.message.sent
whatsapp.message.delivered
whatsapp.message.read
whatsapp.message.failed
```

## FR-WA-075 — Lead Triggers

```text
whatsapp.lead.detected
whatsapp.lead.qualified
whatsapp.lead.high_intent
whatsapp.lead.converted
```

## FR-WA-076 — AI Triggers

```text
whatsapp.intent.detected
whatsapp.sentiment.detected
whatsapp.ai.escalated
whatsapp.ai.completed
```

## FR-WA-077 — Integration Triggers

```text
whatsapp.integration.error
whatsapp.integration.reconnected
whatsapp.integration.disconnected
whatsapp.rate_limit.detected
```

## FR-WA-078 — Workflow Conditions

Example:

```text
intent == "purchase"
AND lead_score >= 80
```

```text
sentiment == "negative"
```

```text
customer_segment == "enterprise"
```

```text
message_type == "document"
```

## FR-WA-079 — Workflow Actions

Where supported:

```text
send_whatsapp_message
send_whatsapp_template
assign_agent
assign_team
add_tag
create_lead
update_lead
create_ticket
notify_agent
trigger_ai_agent
request_human_approval
sync_crm
start_follow_up
```

## FR-WA-080 — Workflow Idempotency

WhatsApp-triggered workflows SHALL be idempotent.

---

## 19. Lead Generation

## FR-WA-081 — Lead Detection

Leads SHALL be detected from:

* Incoming messages
* Customer replies
* Product inquiries
* Pricing inquiries
* Purchase intent
* Workflow events
* AI classifications

## FR-WA-082 — Lead Creation

SalesGenie SHALL create leads based on configurable rules.

## FR-WA-083 — Deduplication

Duplicate leads SHALL be prevented.

## FR-WA-084 — Lead Enrichment

Authorized enrichment sources SHALL be usable.

## FR-WA-085 — Lead Score

The platform SHALL maintain an explainable lead score.

## FR-WA-086 — Qualification Status

Supported states may include:

```text
new
contacted
qualified
sales_qualified
disqualified
converted
lost
```

## FR-WA-087 — Lead Assignment

Qualified leads SHALL be assigned to sales representatives.

## FR-WA-088 — Source Attribution

The lead source SHALL identify WhatsApp.

---

## 20. CRM Synchronization

## FR-WA-089 — Contact Sync

Supported customer information SHALL synchronize with connected CRM systems.

## FR-WA-090 — Lead Sync

WhatsApp leads SHALL synchronize with supported CRM systems.

## FR-WA-091 — Opportunity Sync

Qualified leads SHALL be eligible for opportunity creation.

## FR-WA-092 — Field Mapping

Administrators SHALL configure CRM field mappings.

## FR-WA-093 — Deduplication

CRM synchronization SHALL prevent duplicate records.

## FR-WA-094 — Conflict Resolution

The platform SHALL support configurable conflict resolution.

## FR-WA-095 — Sync Status

Users SHALL be able to inspect synchronization status.

## FR-WA-096 — Sync Retry

Transient CRM synchronization failures SHALL be retried.

---

## 21. Customer Identity Resolution

## FR-WA-097 — Identity Resolution

The platform SHALL associate WhatsApp identifiers with SalesGenie customer profiles.

## FR-WA-098 — Phone Number Matching

Where authorized, phone number identifiers SHALL be used for identity resolution.

## FR-WA-099 — Duplicate Detection

Potential duplicate customer profiles SHALL be detected.

## FR-WA-100 — Identity Merge

Authorized administrators SHALL be able to merge duplicate customer records according to data-governance policies.

## FR-WA-101 — Cross-Channel Identity

Where permitted, WhatsApp identities MAY be associated with customer identities from other channels.

---

## 22. Conversation Routing

## FR-WA-102 — Rule-Based Routing

Administrators SHALL be able to configure routing rules.

Example:

```text
IF intent == "sales"
THEN route_to = SalesTeam
```

## FR-WA-103 — Sentiment Routing

Negative sentiment SHALL be routable to support teams.

## FR-WA-104 — Language Routing

Conversations SHALL be routable based on language.

## FR-WA-105 — Customer Tier Routing

VIP and enterprise customers SHALL be routable to specialized teams.

## FR-WA-106 — AI Routing

The AI orchestrator SHALL select an appropriate AI agent.

## FR-WA-107 — Load-Based Routing

The system MAY route conversations based on human-agent workload.

---

## 23. Security Requirements

## FR-WA-108 — RBAC

WhatsApp operations SHALL enforce SalesGenie RBAC.

Example permissions:

```text
whatsapp.integration.view
whatsapp.integration.create
whatsapp.integration.update
whatsapp.integration.delete

whatsapp.account.view
whatsapp.account.manage

whatsapp.phone_number.view
whatsapp.phone_number.manage

whatsapp.conversation.view
whatsapp.conversation.reply
whatsapp.conversation.assign
whatsapp.conversation.takeover

whatsapp.message.send
whatsapp.template.view
whatsapp.template.manage

whatsapp.ai.enable
whatsapp.ai.configure

whatsapp.workflow.execute

whatsapp.webhook.manage

whatsapp.analytics.view
whatsapp.audit.view
```

## FR-WA-109 — Least Privilege

All WhatsApp operations SHALL follow least-privilege access.

## FR-WA-110 — Tenant Isolation

Users SHALL only access authorized organizational data.

## FR-WA-111 — Credential Redaction

Credentials SHALL never appear in:

* Logs
* Error messages
* Browser storage
* Analytics
* Audit records

## FR-WA-112 — Audit Logging

The system SHALL audit:

* Authorization
* Reauthorization
* Connection
* Disconnection
* Configuration changes
* AI activation
* AI deactivation
* Human takeover
* AI resume
* Template configuration
* Webhook configuration
* Security events

---

## 24. Webhook Requirements

## FR-WA-113 — Webhook Endpoint

SalesGenie SHALL expose secure webhook endpoints.

## FR-WA-114 — Verification

Webhook verification SHALL comply with applicable WhatsApp/Meta requirements.

## FR-WA-115 — Authenticity

Webhook authenticity SHALL be validated.

## FR-WA-116 — Deduplication

Duplicate events SHALL be detected.

## FR-WA-117 — Persistence

Webhook metadata SHALL be persisted according to retention policies.

## FR-WA-118 — Event Publication

Validated events SHALL be published to the internal event bus.

## FR-WA-119 — Retry

Failed event processing SHALL be retried.

## FR-WA-120 — Dead Letter

Permanently failed events SHALL enter a dead-letter queue.

---

## 25. Error Handling

## FR-WA-121 — Authentication Error

The platform SHALL identify invalid credentials.

## FR-WA-122 — Authorization Error

Permission failures SHALL be distinguished from authentication failures.

## FR-WA-123 — Rate Limit

Provider rate-limit responses SHALL be detected.

## FR-WA-124 — Template Error

Invalid or unavailable templates SHALL produce actionable errors.

## FR-WA-125 — Message Error

Failed outbound messages SHALL be classified.

## FR-WA-126 — Network Error

Network failures SHALL use retry mechanisms.

## FR-WA-127 — Timeout

Provider timeouts SHALL be handled safely.

## FR-WA-128 — Validation Error

Invalid payloads SHALL be rejected without corrupting canonical data.

## FR-WA-129 — AI Error

AI failures SHALL trigger configured fallback behavior.

## FR-WA-130 — Workflow Error

Workflow failures SHALL be isolated from message ingestion.

Error taxonomy:

```text
AUTHENTICATION_ERROR
AUTHORIZATION_ERROR
RATE_LIMIT_ERROR
TEMPLATE_ERROR
MESSAGE_ERROR
VALIDATION_ERROR
NOT_FOUND
CONFLICT
NETWORK_ERROR
TIMEOUT
PROVIDER_ERROR
INTERNAL_ERROR
POLICY_ERROR
AI_ERROR
WORKFLOW_ERROR
```

---

## 26. Retry Strategy

The integration SHALL support:

```text
Immediate Retry
      ↓
Exponential Backoff
      ↓
Jitter
      ↓
Maximum Retry Count
      ↓
Dead Letter Queue
      ↓
Manual Replay
```

Retries SHALL NOT be used for permanent failures such as:

```text
invalid_credentials
invalid_template
invalid_recipient
permission_denied
invalid_payload
policy_violation
```

---

## 27. Integration Monitoring

## FR-WA-131 — Health Status

The system SHALL expose:

```text
HEALTHY
DEGRADED
AUTH_REQUIRED
RATE_LIMITED
WEBHOOK_FAILURE
API_FAILURE
DISCONNECTED
DISABLED
```

## FR-WA-132 — Metrics

The platform SHALL collect:

```text
messages_received
messages_sent
messages_failed

messages_delivered
messages_read

conversations_created
conversations_updated
conversations_resolved

ai_responses
ai_escalations
human_takeovers
human_responses

leads_created
leads_qualified
leads_converted

template_messages_sent
template_failures

crm_sync_success
crm_sync_failure

webhook_events
webhook_failures

api_requests
api_errors
rate_limit_events

retry_count
dead_letter_count
```

## FR-WA-133 — Latency

The platform SHALL measure:

* Webhook ingestion latency
* Event processing latency
* AI inference latency
* Human inbox propagation latency
* Outbound message latency
* CRM synchronization latency

## FR-WA-134 — Alerts

Critical integration failures SHALL trigger alerts.

## FR-WA-135 — Distributed Tracing

Requests SHALL propagate:

```text
correlation_id
trace_id
request_id
organization_id
integration_id
phone_number_id
conversation_id
```

---

## 28. Analytics

## FR-WA-136 — Conversation Analytics

The system SHALL report:

* Conversation volume
* Active conversations
* Resolved conversations
* Average response time
* Average resolution time
* Conversation growth

## FR-WA-137 — Messaging Analytics

The system SHALL report:

* Messages received
* Messages sent
* Messages delivered
* Messages read
* Message failures
* Delivery latency

## FR-WA-138 — AI Analytics

The system SHALL report:

* AI response count
* AI resolution rate
* AI escalation rate
* AI confidence
* AI failure rate
* Human takeover rate

## FR-WA-139 — Sales Analytics

The system SHALL report:

* Leads generated
* Qualified leads
* Sales-qualified leads
* Conversion rate
* Opportunities created
* Revenue attribution where available

## FR-WA-140 — Human-Agent Analytics

The platform SHALL report:

* Conversations handled
* Response time
* Resolution rate
* Escalation rate
* Conversion rate
* Workload

---

## 29. MCP Integration

WhatsApp capabilities SHALL be exposed through the SalesGenie MCP layer where appropriate.

## MCP Tools

```text
whatsapp.list_accounts
whatsapp.list_phone_numbers
whatsapp.get_account
whatsapp.get_phone_number
whatsapp.get_conversation
whatsapp.search_conversations
whatsapp.get_customer
whatsapp.send_message
whatsapp.send_template
whatsapp.send_media
whatsapp.assign_conversation
whatsapp.add_tag
whatsapp.create_lead
whatsapp.update_lead
whatsapp.get_templates
whatsapp.get_message_status
whatsapp.integration_health
whatsapp.request_human_handoff
```

## MCP Authorization

Every MCP operation SHALL enforce:

```text
organization_authorization
user_authorization
agent_authorization
tool_permission
resource_permission
action_policy
audit_logging
rate_limiting
```

AI agents SHALL never receive unrestricted WhatsApp access.

---

## 30. Prompt Injection Protection

WhatsApp customer content SHALL always be treated as untrusted input.

Customer messages SHALL NOT override:

```text
system instructions
developer policies
organization policies
RBAC
tool permissions
workflow restrictions
security policies
data-access controls
```

Architecture:

```text
WhatsApp Customer Message
            ↓
      Untrusted Input
            ↓
       Sanitization
            ↓
      Context Builder
            ↓
 Policy / Authorization Engine
            ↓
            LLM
            ↓
      Tool Authorization
            ↓
 WhatsApp / CRM / Workflow
```

---

## 31. AI Decision Pipeline

```text
WhatsApp Message
       ↓
Webhook Validation
       ↓
Message Normalization
       ↓
Customer Resolution
       ↓
Conversation Resolution
       ↓
AI Enabled?
       │
   ┌───┴────┐
   │        │
  NO       YES
   │        │
 Human      ▼
 Queue   Context Retrieval
            │
            ▼
      Intent Detection
            │
            ▼
     Sentiment Detection
            │
            ▼
        Lead Scoring
            │
            ▼
      Policy Evaluation
            │
       ┌────┴─────┐
       │          │
 Human Required  AI Allowed
       │          │
       ▼          ▼
 Human Queue   RAG Retrieval
                    │
                    ▼
              Generate Reply
                    │
                    ▼
              Validate Reply
                    │
             ┌──────┴──────┐
             │             │
          Reject          Accept
             │             │
             ▼             ▼
        Human Review   WhatsApp API
```

---

## 32. AI-to-Human Handoff

## Handoff Triggers

```text
explicit_human_request
low_ai_confidence
negative_sentiment
angry_customer
high_value_lead
complex_support_case
policy_restricted_action
refund_request
payment_request
legal_request
security_request
repeated_ai_failure
customer_frustration
organization_rule
workflow_rule
```

## Handoff Context

The AI SHALL provide:

```text
customer_summary
conversation_summary
intent
sentiment
lead_score
qualification_status
conversation_history
relevant_knowledge
recommended_action
reason_for_escalation
ai_confidence
```

---

## 33. Human-to-AI Handoff

When a human agent returns a conversation to AI:

1. The system SHALL verify agent authorization.
2. The system SHALL record the handoff.
3. The system SHALL preserve conversation state.
4. The system SHALL provide relevant context to the AI.
5. The system SHALL re-evaluate applicable policies.
6. The AI SHALL resume only if the conversation is eligible.
7. The system SHALL audit the transition.

---

## 34. End-to-End Sales Workflow

```text
WhatsApp Customer
       ↓
Product Inquiry
       ↓
AI Intent Detection
       ↓
Product Knowledge Retrieval
       ↓
AI Response
       ↓
Customer Engagement
       ↓
Purchase Intent Detection
       ↓
Lead Score >= Threshold
       ↓
Lead Creation
       ↓
Lead Qualification
       ↓
Sales Team Assignment
       ↓
CRM Synchronization
       ↓
Human Sales Agent
       ↓
Opportunity Creation
       ↓
Conversion
```

---

## 35. End-to-End Support Workflow

```text
Customer Message
       ↓
Intent Detection
       ↓
Support Classification
       ↓
RAG Retrieval
       ↓
AI Resolution
       │
       ├── Resolved
       │      ↓
       │   Close Conversation
       │
       └── Not Resolved
              ↓
        Human Escalation
              ↓
        Support Agent
              ↓
        Ticket / CRM
              ↓
        Resolution
              ↓
        Customer Notification
```

---

## 36. High-Intent Lead Workflow

```text
TRIGGER:
whatsapp.message.received

CONDITIONS:
intent == "purchase"
AND lead_score >= 80

ACTIONS:
1. Create lead
2. Mark sales-qualified
3. Assign sales team
4. Notify sales manager
5. Synchronize CRM
6. Start sales workflow
7. Record attribution
```

---

## 37. Negative Sentiment Workflow

```text
TRIGGER:
whatsapp.message.received

CONDITION:
sentiment == "negative"

ACTIONS:
1. Increase priority
2. Disable autonomous AI handling
3. Assign support agent
4. Notify manager
5. Create support ticket
6. Record escalation
```

---

## 38. Template Follow-Up Workflow

```text
TRIGGER:
lead.follow_up_required

CONDITIONS:
lead.status == "qualified"
AND follow_up_allowed == true
AND required_template_available == true

ACTIONS:
1. Select approved template
2. Resolve template variables
3. Validate parameters
4. Apply policy
5. Send WhatsApp template
6. Track delivery
7. Update CRM
8. Schedule next follow-up
```

---

## 39. Customer Identity Data Model

```text
WhatsAppIdentity
├── id
├── organization_id
├── phone_number
├── external_user_identifier
├── customer_id
├── first_seen_at
├── last_seen_at
├── verification_status
└── metadata
```

The platform SHALL avoid exposing provider-specific identifiers to unauthorized users.

---

## 40. WhatsApp Integration Data Model

## WhatsAppIntegration

```text
WhatsAppIntegration
├── id
├── organization_id
├── provider
├── name
├── status
├── authorization_status
├── credential_reference
├── api_version
├── created_at
├── updated_at
└── last_health_check_at
```

## WhatsAppBusinessAccount

```text
WhatsAppBusinessAccount
├── id
├── integration_id
├── organization_id
├── external_account_id
├── display_name
├── status
├── created_at
└── updated_at
```

## WhatsAppPhoneNumber

```text
WhatsAppPhoneNumber
├── id
├── business_account_id
├── organization_id
├── external_phone_number_id
├── phone_number
├── display_name
├── status
├── webhook_status
├── ai_enabled
├── assigned_agent_id
├── assigned_team_id
├── created_at
└── updated_at
```

## WhatsAppConversation

```text
WhatsAppConversation
├── id
├── organization_id
├── integration_id
├── business_account_id
├── phone_number_id
├── external_conversation_id
├── customer_id
├── assigned_agent_id
├── assigned_team_id
├── state
├── intent
├── sentiment
├── lead_score
├── ai_mode
├── priority
├── created_at
├── updated_at
└── last_message_at
```

## WhatsAppMessage

```text
WhatsAppMessage
├── id
├── organization_id
├── conversation_id
├── external_message_id
├── sender_id
├── recipient_id
├── direction
├── message_type
├── content
├── media_reference
├── template_id
├── delivery_status
├── ai_generated
├── human_generated
├── created_at
├── sent_at
├── delivered_at
├── read_at
└── failed_at
```

## WhatsAppLead

```text
WhatsAppLead
├── id
├── organization_id
├── conversation_id
├── customer_id
├── source
├── phone_number_id
├── lead_score
├── qualification_status
├── intent
├── product_interest
├── assigned_agent_id
├── crm_record_id
├── created_at
└── updated_at
```

---

## 41. API Requirements

## Integration APIs

```text
POST   /api/v1/integrations/whatsapp
GET    /api/v1/integrations/whatsapp
GET    /api/v1/integrations/whatsapp/{id}
PATCH  /api/v1/integrations/whatsapp/{id}
DELETE /api/v1/integrations/whatsapp/{id}
```

## OAuth APIs

```text
GET  /api/v1/integrations/whatsapp/oauth/authorize
GET  /api/v1/integrations/whatsapp/oauth/callback
POST /api/v1/integrations/whatsapp/{id}/reauthorize
```

## Business Account APIs

```text
GET /api/v1/integrations/whatsapp/{id}/business-accounts
```

## Phone Number APIs

```text
GET    /api/v1/integrations/whatsapp/{id}/phone-numbers
POST   /api/v1/integrations/whatsapp/{id}/phone-numbers
PATCH  /api/v1/integrations/whatsapp/phone-numbers/{phone_number_id}
DELETE /api/v1/integrations/whatsapp/phone-numbers/{phone_number_id}
```

## Conversation APIs

```text
GET   /api/v1/whatsapp/conversations
GET   /api/v1/whatsapp/conversations/{conversation_id}
POST  /api/v1/whatsapp/conversations/{conversation_id}/messages
PATCH /api/v1/whatsapp/conversations/{conversation_id}
POST  /api/v1/whatsapp/conversations/{conversation_id}/assign
POST  /api/v1/whatsapp/conversations/{conversation_id}/takeover
POST  /api/v1/whatsapp/conversations/{conversation_id}/resume-ai
```

## Template APIs

```text
GET  /api/v1/whatsapp/templates
GET  /api/v1/whatsapp/templates/{template_id}
POST /api/v1/whatsapp/templates/{template_id}/send
```

## Webhook APIs

```text
GET  /api/v1/webhooks/whatsapp
POST /api/v1/webhooks/whatsapp
```

## Analytics APIs

```text
GET /api/v1/whatsapp/analytics/conversations
GET /api/v1/whatsapp/analytics/messages
GET /api/v1/whatsapp/analytics/leads
GET /api/v1/whatsapp/analytics/ai
GET /api/v1/whatsapp/analytics/agents
GET /api/v1/whatsapp/analytics/templates
GET /api/v1/whatsapp/analytics/health
```

---

## 42. Event Schema

```json
{
  "event_id": "uuid",
  "event_type": "whatsapp.message.received",
  "provider": "whatsapp",
  "organization_id": "uuid",
  "integration_id": "uuid",
  "business_account_id": "external-business-account-id",
  "phone_number_id": "external-phone-number-id",
  "conversation_id": "uuid",
  "external_event_id": "provider-event-id",
  "timestamp": "2026-08-28T05:00:00Z",
  "payload": {},
  "correlation_id": "uuid",
  "trace_id": "trace-id",
  "schema_version": "1.0"
}
```

---

## 43. Webhook Event Types

The internal event model SHOULD support:

```text
whatsapp.message.received
whatsapp.message.sent
whatsapp.message.delivered
whatsapp.message.read
whatsapp.message.failed

whatsapp.conversation.created
whatsapp.conversation.updated
whatsapp.conversation.resolved

whatsapp.customer.created
whatsapp.customer.updated

whatsapp.lead.detected
whatsapp.lead.qualified
whatsapp.lead.converted

whatsapp.ai.started
whatsapp.ai.completed
whatsapp.ai.escalated

whatsapp.integration.connected
whatsapp.integration.disconnected
whatsapp.integration.error
whatsapp.rate_limit.detected
```

---

## 44. Security Threat Model

The integration SHALL defend against:

```text
stolen_access_tokens
credential_leakage
webhook_spoofing
replay_attacks
duplicate_events
cross_tenant_access
privilege_escalation
prompt_injection
AI_tool_abuse
data_exfiltration
PII_leakage
unauthorized_messages
API_abuse
rate_limit_exhaustion
workflow_abuse
CRM_poisoning
malicious_attachments
malicious_links
account_takeover
```

AI-generated actions SHALL pass through independent authorization and policy enforcement.

---

## 45. Privacy and Data Governance

The system SHALL implement:

```text
data_minimization
purpose_limitation
tenant_isolation
access_control
retention_policy
deletion_policy
auditability
encryption
secret_management
PII_protection
```

Sensitive customer information SHALL only be exposed to authorized users and AI agents.

---

## 46. Super Admin Requirements

## FR-WA-141 — Global Monitoring

Super administrators SHALL be able to monitor WhatsApp integration health across organizations according to platform governance policies.

## FR-WA-142 — Tenant Inventory

Authorized super administrators SHALL be able to inspect:

* Organizations with WhatsApp integrations
* Connected business accounts
* Connected phone numbers
* Integration status
* Webhook failures
* API failures
* Authentication failures
* Rate-limit events

## FR-WA-143 — Emergency Disablement

Super administrators SHALL be able to disable an integration during security or operational incidents.

## FR-WA-144 — Security Auditing

Super administrators SHALL be able to inspect relevant security events.

## FR-WA-145 — Incident Detection

The platform SHALL detect widespread WhatsApp integration failures.

---

## 47. Non-Functional Requirements

## NFR-WA-001 — Availability

The WhatsApp integration SHALL target enterprise-grade availability consistent with the SalesGenie platform SLA.

## NFR-WA-002 — Scalability

The service SHALL horizontally scale to support high-volume messaging.

## NFR-WA-003 — Reliability

Accepted events SHALL not be silently lost because of transient infrastructure or provider failures.

## NFR-WA-004 — Performance

Webhook requests SHALL be acknowledged rapidly while expensive processing occurs asynchronously.

## NFR-WA-005 — Durability

Critical events SHALL be durably persisted before irreversible processing where required.

## NFR-WA-006 — Security

The integration SHALL support:

* Encryption in transit
* Encryption at rest
* RBAC
* Least privilege
* Secret management
* Audit logging
* Tenant isolation
* Data minimization

## NFR-WA-007 — Observability

Critical operations SHALL be observable through:

* Metrics
* Logs
* Traces
* Health checks
* Alerts

## NFR-WA-008 — Maintainability

WhatsApp-specific provider logic SHALL remain isolated from channel-independent business logic.

## NFR-WA-009 — Extensibility

The architecture SHALL support future WhatsApp capabilities without redesigning the core SalesGenie conversation architecture.

---

## 48. Provider Abstraction

SalesGenie SHALL implement a channel/provider abstraction.

```text
ChannelIntegrationInterface
        │
        ├── WhatsAppAdapter
        ├── InstagramAdapter
        ├── FacebookAdapter
        ├── GmailAdapter
        ├── LinkedInAdapter
        └── FutureChannelAdapters
```

Conceptual interface:

```text
connect()
authorize()
disconnect()
health_check()
subscribe_webhooks()
unsubscribe_webhooks()
send_message()
send_template()
send_media()
receive_event()
sync_conversations()
sync_messages()
sync_templates()
normalize_event()
handle_rate_limit()
handle_error()
```

---

## 49. Cross-Channel Omnichannel Requirements

WhatsApp SHALL participate in SalesGenie's unified omnichannel architecture.

```text
                    ┌──────────────┐
                    │    Gmail     │
                    └──────┬───────┘
                           │
┌──────────────┐           │          ┌──────────────┐
│ Instagram    │───────────┼──────────│ Facebook     │
└──────────────┘           │          └──────────────┘
                           ▼
                    ┌──────────────┐
                    │  SalesGenie  │
                    │ Conversation │
                    │    Layer     │
                    └──────┬───────┘
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
          AI Agent     Human Agent     CRM
```

The platform SHALL maintain a canonical conversation model so AI and human agents can operate across channels consistently.

---

## 50. Cross-Channel Customer Journey

Example:

```text
Instagram
   ↓
Customer expresses interest
   ↓
Lead created
   ↓
WhatsApp
   ↓
Sales conversation
   ↓
AI qualification
   ↓
Human sales agent
   ↓
CRM opportunity
   ↓
Email
   ↓
Follow-up
   ↓
WhatsApp
   ↓
Conversion
```

The system SHALL preserve appropriate customer and consent context across channel transitions.

---

## 51. Recommended Enterprise SLO Targets

```text
Webhook ingestion availability:       >= 99.99%
Integration service availability:     >= 99.95%
Webhook acknowledgement latency:     p95 < 500 ms
Internal event publication:           p95 < 1 second
AI routing decision:                  p95 < 2 seconds
Human inbox propagation:              p95 < 1 second
Outbound request initiation:          p95 < 2 seconds
Duplicate event rate:                 < 0.01%
Unrecoverable event loss:             0
Unauthorized actions:                0
Cross-tenant data leakage:            0
```

Actual SLOs SHALL be aligned with infrastructure capacity and contractual SLA requirements.

---

## 52. Acceptance Criteria

## AC-WA-001

An authorized administrator can connect a supported WhatsApp Business account.

## AC-WA-002

Eligible business phone numbers can be discovered and connected.

## AC-WA-003

The integration becomes ACTIVE only after authorization and health validation succeed.

## AC-WA-004

Valid webhook events are authenticated, normalized, persisted, and published.

## AC-WA-005

Incoming WhatsApp messages create or update the correct SalesGenie conversation.

## AC-WA-006

Duplicate webhook events do not create duplicate messages or conversations.

## AC-WA-007

Human agents can view and respond to WhatsApp conversations.

## AC-WA-008

AI agents can process eligible conversations.

## AC-WA-009

AI uses authorized RAG knowledge when required.

## AC-WA-010

Low-confidence conversations are escalated to humans.

## AC-WA-011

Human agents can take over AI conversations.

## AC-WA-012

Human agents can return eligible conversations to AI.

## AC-WA-013

Supported WhatsApp message types are normalized correctly.

## AC-WA-014

Supported media can be processed securely.

## AC-WA-015

Supported templates can be selected, validated, and sent.

## AC-WA-016

Message delivery states are recorded.

## AC-WA-017

High-intent WhatsApp interactions can create leads.

## AC-WA-018

Lead scoring and qualification are applied according to configured policies.

## AC-WA-019

Qualified leads can synchronize with supported CRM systems.

## AC-WA-020

WhatsApp events can trigger workflows.

## AC-WA-021

Workflow actions can send supported WhatsApp messages.

## AC-WA-022

Rate-limit events trigger controlled backoff.

## AC-WA-023

Transient provider failures trigger retries.

## AC-WA-024

Permanent failures enter the dead-letter queue when appropriate.

## AC-WA-025

Administrators can inspect integration health.

## AC-WA-026

Security-sensitive operations are auditable.

## AC-WA-027

RBAC prevents unauthorized WhatsApp operations.

## AC-WA-028

Cross-tenant access is prevented.

## AC-WA-029

MCP tools cannot bypass authorization.

## AC-WA-030

Customer prompt injection cannot override system or organization policies.

## AC-WA-031

High-risk AI actions can require human approval.

## AC-WA-032

CRM synchronization failures can be retried or manually recovered.

## AC-WA-033

Integration failures are visible through monitoring and alerting.

## AC-WA-034

Webhook and message processing remain reliable during temporary provider outages.

## AC-WA-035

Reconciliation can identify missing or inconsistent records.

---

## 53. Implementation Priority

## P0 — Critical

```text
WhatsApp authorization
Business account connection
Phone number connection
Webhook verification
Webhook ingestion
Message normalization
Conversation management
Inbound messaging
Outbound messaging
Delivery tracking
AI response processing
Human response processing
Human takeover
AI escalation
RBAC
Tenant isolation
Credential security
Rate limiting
Retry handling
Audit logging
Integration health
```

## P1 — High

```text
WhatsApp templates
Media handling
Interactive messages
Lead generation
Lead scoring
Lead qualification
CRM synchronization
Workflow triggers
Workflow actions
Conversation routing
Human approval
AI confidence routing
Analytics
MCP tools
```

## P2 — Advanced

```text
Advanced customer journey intelligence
Predictive lead scoring
Revenue attribution
AI sales recommendations
Cross-channel identity resolution
Predictive customer intent
AI-driven routing optimization
Anomaly detection
Predictive integration failure detection
Advanced conversation analytics
Automated customer segmentation
```

---

## 54. Definition of Done

The WhatsApp integration SHALL be considered production-ready only when:

* [ ] Secure WhatsApp Business authorization is implemented.
* [ ] Business accounts can be connected.
* [ ] Business phone numbers can be connected.
* [ ] Multiple accounts are supported.
* [ ] Multiple phone numbers are supported.
* [ ] Tenant isolation is enforced.
* [ ] Webhook verification is implemented.
* [ ] Webhook authenticity validation is implemented.
* [ ] Duplicate event detection is implemented.
* [ ] Incoming messages are normalized.
* [ ] Outbound messages are supported.
* [ ] Delivery status is tracked.
* [ ] Conversation history is persisted according to policy.
* [ ] Supported media types are handled securely.
* [ ] Templates are supported.
* [ ] Template variables are validated.
* [ ] AI intent detection works.
* [ ] AI sentiment detection works.
* [ ] AI language detection works.
* [ ] AI entity extraction works.
* [ ] AI lead scoring works.
* [ ] AI qualification works.
* [ ] RAG grounding works.
* [ ] AI responses work.
* [ ] Human responses work.
* [ ] AI-to-human handoff works.
* [ ] Human-to-AI resume works.
* [ ] Human approval works.
* [ ] Lead creation works.
* [ ] Lead deduplication works.
* [ ] CRM synchronization works.
* [ ] Workflow triggers work.
* [ ] Workflow actions work where supported.
* [ ] MCP tools are permission-controlled.
* [ ] Rate limiting works.
* [ ] Retry and exponential backoff work.
* [ ] Dead-letter handling works.
* [ ] Reconciliation works.
* [ ] Integration health monitoring works.
* [ ] Analytics are available.
* [ ] Audit logging works.
* [ ] RBAC is enforced.
* [ ] Tenant isolation tests pass.
* [ ] Security tests pass.
* [ ] Prompt-injection tests pass.
* [ ] AI authorization tests pass.
* [ ] Load tests pass.
* [ ] Failure-recovery tests pass.
* [ ] Provider capability restrictions are enforced.
* [ ] Production monitoring and alerting are configured.

---

## 55. Final Enterprise Architecture

```text
                           ┌─────────────────────────┐
                           │ WhatsApp Customer       │
                           └────────────┬────────────┘
                                        │
                                        ▼
                           ┌─────────────────────────┐
                           │ WhatsApp Business       │
                           │ Platform                │
                           └────────────┬────────────┘
                                        │
                                        ▼
                           ┌─────────────────────────┐
                           │ Webhook Gateway          │
                           ├─────────────────────────┤
                           │ Verification             │
                           │ Authentication           │
                           │ Rate Limiting            │
                           │ Idempotency               │
                           └────────────┬────────────┘
                                        │
                                        ▼
                           ┌─────────────────────────┐
                           │ Event Normalizer         │
                           └────────────┬────────────┘
                                        │
                                        ▼
                           ┌─────────────────────────┐
                           │ Event Bus / Queue        │
                           └────────────┬────────────┘
                                        │
                  ┌─────────────────────┼─────────────────────┐
                  │                     │                     │
                  ▼                     ▼                     ▼
          ┌───────────────┐     ┌───────────────┐     ┌──────────────┐
          │ Conversation  │     │ Lead          │     │ Workflow     │
          │ Service       │     │ Intelligence  │     │ Engine       │
          └───────┬───────┘     └───────┬───────┘     └──────┬───────┘
                  │                     │                     │
                  └─────────────────────┼─────────────────────┘
                                        │
                                        ▼
                           ┌─────────────────────────┐
                           │ AI Orchestrator          │
                           ├─────────────────────────┤
                           │ Intent Detection         │
                           │ Sentiment Analysis       │
                           │ Language Detection       │
                           │ Entity Extraction        │
                           │ Lead Scoring              │
                           │ RAG Retrieval             │
                           │ Agent Selection           │
                           │ Guardrails                │
                           │ Tool Authorization        │
                           └────────────┬────────────┘
                                        │
                         ┌──────────────┴──────────────┐
                         │                             │
                         ▼                             ▼
                 ┌────────────────┐           ┌──────────────────┐
                 │ AI Sales /     │           │ Human Agent      │
                 │ Support Agent  │           │ Workspace        │
                 └───────┬────────┘           └────────┬─────────┘
                         │                             │
                         └──────────────┬──────────────┘
                                        │
                                        ▼
                           ┌─────────────────────────┐
                           │ Policy / RBAC /          │
                           │ Approval Engine           │
                           └────────────┬────────────┘
                                        │
                    ┌───────────────────┼───────────────────┐
                    │                   │                   │
                    ▼                   ▼                   ▼
             ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
             │ WhatsApp API │    │ CRM Systems  │    │ Workflow     │
             │              │    │              │    │ Actions      │
             └──────────────┘    └──────────────┘    └──────────────┘
                    │                   │                   │
                    └───────────────────┼───────────────────┘
                                        │
                                        ▼
                           ┌─────────────────────────┐
                           │ Analytics / Monitoring   │
                           │ Audit / Observability    │
                           └─────────────────────────┘
```

---

## 56. Final Requirement Principle

SalesGenie SHALL treat WhatsApp as a first-class enterprise omnichannel channel rather than a basic messaging connector.

The complete lifecycle SHALL be:

```text
CONNECT
   ↓
AUTHORIZE
   ↓
DISCOVER BUSINESS ACCOUNT
   ↓
DISCOVER PHONE NUMBER
   ↓
CONFIGURE
   ↓
REGISTER WEBHOOK
   ↓
RECEIVE EVENT
   ↓
VALIDATE
   ↓
NORMALIZE
   ↓
RESOLVE CUSTOMER
   ↓
RESOLVE CONVERSATION
   ↓
UNDERSTAND
   ↓
CLASSIFY
   ↓
DETECT INTENT
   ↓
ANALYZE SENTIMENT
   ↓
QUALIFY
   ↓
SCORE
   ↓
ROUTE
   ↓
AI OR HUMAN
   ↓
RAG / CONTEXT RETRIEVAL
   ↓
GENERATE / WRITE RESPONSE
   ↓
POLICY VALIDATION
   ↓
HUMAN APPROVAL WHEN REQUIRED
   ↓
SEND THROUGH WHATSAPP
   ↓
TRACK DELIVERY
   ↓
CREATE / UPDATE LEAD
   ↓
SYNC CRM
   ↓
TRIGGER WORKFLOWS
   ↓
MONITOR
   ↓
AUDIT
   ↓
ANALYZE
   ↓
OPTIMIZE
```

The architecture SHALL ensure that **AI autonomy never bypasses authentication, authorization, tenant isolation, policy enforcement, human approval requirements, auditability, provider capabilities, rate limits, messaging restrictions, or organizational governance controls**.
