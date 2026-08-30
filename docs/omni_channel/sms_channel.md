# SalesGenie — SMS Channel Requirements

## 1. Document Overview

### 1.1 Purpose

The SalesGenie SMS Channel shall provide an enterprise-grade AI-powered and human-assisted communication channel for customer support, sales engagement, lead qualification, notifications, ticket management, workflow automation, and customer relationship management through SMS.

The SMS channel shall operate as a first-class component of SalesGenie's omnichannel platform while reusing the platform's shared:

* Customer identity system
* Conversation management
* AI orchestration
* RAG knowledge base
* Human support workspace
* Ticket management
* SLA management
* Intelligent routing
* Workflow automation
* CRM integrations
* Analytics
* Audit logging
* RBAC
* Multi-tenant security

The design shall follow SalesGenie's broader enterprise architecture principles, including tenant isolation, strict AI/tool permissions, asynchronous processing, failure recovery, observability, cost controls, and human approval for high-impact actions.

---

## 2. Scope

The SMS Channel shall support:

* SMS number provisioning and configuration
* SMS provider integration
* Inbound SMS
* Outbound SMS
* Two-way conversations
* AI support agents
* Human support agents
* Hybrid AI-human support
* AI-to-human escalation
* Human-to-AI handoff
* Customer identity resolution
* Conversation history
* RAG-powered support
* Intent detection
* Entity extraction
* Sentiment analysis
* Lead qualification
* Sales engagement
* Ticket creation
* Ticket updates
* SLA management
* Intelligent routing
* Workflow automation
* CRM synchronization
* Customer notifications
* AI-generated summaries
* AI-assisted agent responses
* Customer feedback
* Customer satisfaction measurement
* SMS analytics
* AI analytics
* Human-agent analytics
* Delivery tracking
* Failure handling
* Opt-in/opt-out management
* Consent management
* Compliance controls
* Audit logging
* Multi-tenant isolation

---

## 3. Actors and User Roles

## 3.1 End Customer

The customer shall be able to:

* Send SMS messages to the organization's configured business number.
* Receive automated AI responses.
* Request human support.
* Continue an existing conversation.
* Receive support updates.
* Receive authorized transactional notifications.
* Receive sales communication where consent and policy permit.
* Respond to notifications.
* Opt out of applicable messaging.
* Provide feedback.
* Rate support interactions where enabled.

## 3.2 AI Support Agent

The AI agent shall be able to:

* Understand incoming SMS.
* Detect intent.
* Extract entities.
* Analyze sentiment.
* Retrieve approved knowledge.
* Generate context-aware responses.
* Maintain conversation state.
* Answer supported questions.
* Execute authorized tools.
* Trigger workflows.
* Create or update tickets.
* Qualify leads.
* Detect purchase intent.
* Recommend next actions.
* Escalate to humans.
* Summarize conversations.

## 3.3 Human Support Agent

Human agents shall be able to:

* View SMS conversations.
* Accept assigned conversations.
* Send SMS responses.
* Take over AI conversations.
* Return conversations to AI.
* View customer profiles.
* View conversation history.
* View AI summaries.
* View AI recommendations.
* Search knowledge.
* Create tickets.
* Update tickets.
* Add internal notes.
* Apply tags.
* Transfer conversations.
* Escalate conversations.
* Resolve conversations.

## 3.4 Sales Agent

Sales agents shall be able to:

* Receive qualified SMS leads.
* View customer intelligence.
* View AI lead scores.
* View conversation history.
* Continue sales conversations.
* Create opportunities.
* Update CRM records.
* Schedule follow-ups.
* Receive AI sales recommendations.

## 3.5 Supervisor

Supervisors shall be able to:

* Monitor active SMS conversations.
* Monitor agent workload.
* Reassign conversations.
* Override routing.
* Monitor AI escalations.
* Monitor SLA performance.
* Review customer sentiment.
* Review AI performance.
* Audit conversations.

## 3.6 Organization Administrator

Organization administrators shall be able to:

* Configure SMS providers.
* Configure SMS numbers.
* Configure AI agents.
* Configure human teams.
* Configure routing.
* Configure SLAs.
* Configure workflows.
* Configure knowledge bases.
* Configure messaging policies.
* Configure consent rules.
* View SMS analytics.

## 3.7 Super Administrator

SalesGenie super administrators shall be able to:

* Monitor SMS integrations.
* Monitor provider health.
* Manage organizations.
* Monitor platform-wide SMS usage.
* Monitor messaging costs.
* Investigate abuse.
* Audit administrative actions.
* Suspend problematic integrations.
* Manage global messaging policies.

---

## 4. User Requirements

## UR-001 — SMS Conversation Initiation

Customers shall be able to initiate a conversation by sending an SMS to an organization's configured business number.

## UR-002 — Natural Language Communication

Customers shall be able to communicate using ordinary natural-language SMS messages without predefined commands.

## UR-003 — AI First Response

The system shall provide an AI response when:

* AI support is enabled.
* The request is supported.
* Sufficient confidence exists.
* Required knowledge is available.
* Customer consent/messaging status permits the response.
* Safety and policy checks pass.

## UR-004 — Human Support

Customers shall be able to request human assistance through SMS.

Examples:

```text
Talk to a human
Agent please
Connect me to support
I need a real person
```

## UR-005 — Automatic Human Escalation

The system shall automatically escalate when configured conditions occur, including:

* Low AI confidence.
* Unsupported request.
* Critical negative sentiment.
* Security-sensitive request.
* Repeated AI failure.
* High-value customer.
* High purchase intent.
* SLA risk.
* Explicit human request.

## UR-006 — Context Preservation

AI-to-human handoff shall preserve relevant conversation context so the customer does not need to repeat information unnecessarily.

## UR-007 — Customer Identity

The system shall identify customers using available phone-number identifiers and SalesGenie customer identity records.

## UR-008 — Unified Customer Profile

The system shall maintain a unified customer profile containing authorized:

* Customer ID
* Phone number
* Name
* Organization
* Customer tier
* SMS identity
* Conversation history
* Tickets
* Leads
* Opportunities
* Purchases
* Tags
* Preferences
* Consent state
* Engagement history

## UR-009 — Personalized Support

The system shall provide personalized responses using authorized customer context.

## UR-010 — Knowledge-Based Support

Customers shall receive answers grounded in approved organizational knowledge.

## UR-011 — No Unsupported Claims

The AI shall not fabricate business information when reliable evidence is unavailable.

## UR-012 — Clarification

The AI shall ask for clarification when the customer's request is ambiguous.

## UR-013 — Multilingual SMS

The system shall support multilingual SMS conversations where configured.

## UR-014 — Ticket Creation

Customers shall be able to initiate support requests that result in ticket creation where configured.

## UR-015 — Ticket Updates

Customers shall be able to receive authorized ticket status updates through SMS.

## UR-016 — Lead Detection

The system shall identify potential sales opportunities from SMS conversations.

## UR-017 — Lead Qualification

The AI shall qualify leads using configurable attributes such as:

* Need
* Product interest
* Budget
* Timeline
* Company
* Industry
* Purchase intent
* Decision authority

## UR-018 — Sales Handoff

Qualified leads shall be routed to the appropriate sales team.

## UR-019 — Notifications

The system shall support authorized transactional and operational SMS notifications.

## UR-020 — Consent

The system shall maintain messaging consent and customer communication preferences.

## UR-021 — Opt-Out

Customers shall be able to opt out of applicable messaging.

## UR-022 — Opt-In

Where required, the system shall support configurable customer opt-in workflows.

## UR-023 — Transparency

The system shall support appropriate disclosure of AI-assisted communication according to organizational policy.

## UR-024 — Feedback

Customers shall be able to provide support feedback where enabled.

## UR-025 — Customer Satisfaction

Customers shall be able to rate completed support interactions where configured.

## UR-026 — Privacy

Customer phone numbers, SMS content, and related communication data shall be protected according to SalesGenie's privacy and data-governance policies.

---

## 5. System Requirements

## 5.1 Architecture

## SR-001 — Omnichannel Architecture

SMS shall operate as an independent channel adapter connected to SalesGenie's common omnichannel conversation platform.

## SR-002 — Canonical Channel Interface

The channel abstraction shall support:

* SMS
* WhatsApp
* Messenger
* Instagram
* Telegram
* Email
* Web chat
* Future communication channels

## SR-003 — Multi-Tenancy

SMS data shall be isolated by:

* Tenant
* Organization
* Workspace
* User
* Phone number
* Conversation

## SR-004 — Event-Driven Processing

SMS events shall be processed using an event-driven architecture.

## SR-005 — Asynchronous Processing

Long-running operations shall execute asynchronously, including:

* AI inference
* RAG retrieval
* Document processing
* Lead enrichment
* CRM synchronization
* Workflow execution
* Analytics processing

---

## 5.2 SMS Provider Integration

## SR-006 — Provider Abstraction

The SMS subsystem shall isolate provider-specific functionality behind a provider adapter.

The architecture shall support providers such as:

* Twilio
* Vonage
* Plivo
* MessageBird
* Telnyx
* Other compliant SMS providers

Provider-specific capabilities shall not leak into the canonical SalesGenie conversation model.

## SR-007 — Number Configuration

Organizations shall be able to configure supported business phone numbers.

## SR-008 — Sender Identity

The system shall maintain:

* Provider ID
* Phone number
* Country
* Messaging capability
* Tenant
* Organization
* Status

## SR-009 — Provider Credentials

Provider API credentials shall be stored in a secure secret-management system.

## SR-010 — Credential Isolation

Provider credentials shall never be exposed to frontend clients, AI models, agents, or unauthorized services.

## SR-011 — Webhook Support

The system shall expose secure HTTPS webhook endpoints for supported SMS providers.

## SR-012 — Webhook Authentication

Incoming webhook requests shall be authenticated using the provider's supported verification mechanism.

## SR-013 — Event Validation

Incoming SMS events shall undergo:

* Authentication
* Schema validation
* Tenant resolution
* Provider validation
* Duplicate detection

## SR-014 — Event Deduplication

Repeated provider webhook events shall not create duplicate:

* Messages
* Conversations
* Tickets
* Leads
* Workflow executions

## SR-015 — Event Persistence

Important inbound SMS events shall be persisted before asynchronous downstream processing.

## SR-016 — Retry Processing

Transient provider failures shall use bounded retries with exponential backoff.

## SR-017 — Dead-Letter Queue

Events that repeatedly fail processing shall be placed in a dead-letter queue.

---

## 5.3 Messaging Requirements

## SR-018 — Canonical Message Model

Every SMS shall be normalized into a common SalesGenie message representation.

## SR-019 — Inbound SMS

The system shall support inbound text messages.

## SR-020 — Outbound SMS

The system shall support outbound text messages.

## SR-021 — Delivery Tracking

The system shall capture provider delivery status where supported.

## SR-022 — Failure Tracking

The system shall capture:

* Rejected messages
* Failed messages
* Undelivered messages
* Provider errors
* Invalid numbers
* Rate-limit errors

## SR-023 — Message Ordering

The system shall use provider timestamps and message IDs to preserve chronological conversation state.

## SR-024 — Idempotency

Outbound operations shall use idempotency controls to prevent duplicate messages.

## SR-025 — Phone Number Normalization

Phone numbers shall be normalized into a canonical international format.

## SR-026 — Invalid Number Detection

The system shall identify invalid or malformed destination numbers before attempting delivery where possible.

---

## 5.4 AI Requirements

## SR-027 — AI Orchestration

The AI layer shall coordinate:

* Intent detection
* Entity extraction
* Sentiment analysis
* RAG retrieval
* Response generation
* Lead scoring
* Escalation
* Tool execution
* Workflow execution

## SR-028 — Model Abstraction

The SMS channel shall not be coupled to one LLM provider.

## SR-029 — RAG

The AI shall support Retrieval-Augmented Generation using authorized organizational knowledge.

## SR-030 — Tenant-Aware Retrieval

RAG retrieval shall enforce:

* Tenant boundaries
* Workspace permissions
* Document permissions
* Knowledge-base permissions
* User permissions

SalesGenie's broader architecture requires vector/document metadata and retrieval filters to prevent cross-tenant or unauthorized retrieval.

## SR-031 — Confidence Evaluation

AI responses shall include configurable confidence signals.

## SR-032 — Grounding

The system shall distinguish:

* Retrieved facts
* Customer-provided information
* Model inference
* Predictions
* Assumptions

## SR-033 — Hallucination Protection

The system shall apply grounding and validation mechanisms before sending AI-generated business responses.

## SR-034 — AI Guardrails

The AI shall enforce:

* System instructions
* Organization policies
* Agent policies
* Safety rules
* Tool authorization
* Data-access policies

## SR-035 — AI Fallback

Every critical AI workflow shall have a deterministic fallback when:

* The model is unavailable.
* The model times out.
* Retrieval fails.
* Confidence is insufficient.
* Tool execution fails.

SalesGenie's AI audit requirements explicitly call for deterministic fallbacks for important AI capabilities.

---

## 5.5 Human Support Requirements

## SR-036 — Agent Workspace

Human agents shall have a unified workspace for SMS conversations.

## SR-037 — Conversation Assignment

SMS conversations shall be assignable to:

* Agents
* Teams
* Queues
* Departments

## SR-038 — Agent Presence

The system shall maintain configurable agent availability states.

## SR-039 — Concurrent Conversations

Agents shall be able to manage multiple SMS conversations simultaneously.

## SR-040 — AI Assistance

Agents shall receive:

* Suggested replies
* Conversation summaries
* Customer intelligence
* Knowledge recommendations
* Next-best actions
* Sentiment alerts
* Sales recommendations

## SR-041 — Internal Notes

Internal notes shall never be transmitted to customers.

---

## 5.6 Consent and Messaging Governance

## SR-042 — Consent State

The system shall maintain a customer messaging-consent state.

Example:

```text
UNKNOWN
OPTED_IN
OPTED_OUT
PENDING_CONFIRMATION
REVOKED
BLOCKED
```

## SR-043 — Consent History

Consent changes shall be timestamped and auditable.

## SR-044 — Opt-Out Enforcement

The outbound messaging service shall prevent prohibited outbound messages to opted-out recipients.

## SR-045 — Consent-Aware AI

The AI shall not initiate or recommend unauthorized SMS communication.

## SR-046 — Campaign Restrictions

Bulk or campaign messaging shall require configured authorization and approval policies.

## SR-047 — High-Risk Approval

High-impact communication actions shall support human approval.

SalesGenie's broader agent-safety architecture requires human approval for configured high-risk actions such as bulk outreach, data export, deletion, financial changes, and security-policy changes.

---

## 5.7 Security Requirements

## SR-048 — Authentication

Administrative and agent operations shall require authenticated identities.

## SR-049 — RBAC

SMS functionality shall enforce role-based access control.

## SR-050 — Least Privilege

Every agent, service, workflow, and tool shall receive only required permissions.

## SR-051 — Secret Management

Provider credentials, API keys, signing secrets, and webhook credentials shall be securely managed.

## SR-052 — Encryption

Sensitive data shall be encrypted:

* In transit
* At rest

## SR-053 — Phone Number Protection

Phone numbers shall be treated as protected customer information.

## SR-054 — Audit Logging

Security-sensitive SMS actions shall generate audit events.

## SR-055 — Tenant Isolation

One organization shall never access another organization's SMS data.

## SR-056 — Prompt Injection Protection

Customer SMS content shall be considered untrusted input.

The system shall prevent SMS content from overriding:

* System instructions
* Organization policies
* Tool permissions
* Security controls
* Tenant boundaries

## SR-057 — Tool Safety

AI tool inputs and outputs shall be schema-validated and permission-checked.

SalesGenie's agent safety requirements specifically require strict tool schemas, prevention of unauthorized tools or privilege escalation, execution budgets, and protection against loops and duplicate actions.

---

## 5.8 Performance Requirements

## SR-058 — Message Ingestion Latency

Inbound SMS events shall be acknowledged rapidly and processed asynchronously.

## SR-059 — AI Response Latency

The system shall maintain configurable response-latency SLOs.

## SR-060 — Horizontal Scaling

SMS ingestion workers shall support horizontal scaling.

## SR-061 — Queue Scaling

Message processing queues shall scale independently from AI inference workloads.

## SR-062 — Rate Limiting

The system shall implement rate limits for:

* Customers
* Tenants
* Phone numbers
* Agents
* API consumers
* AI workloads

## SR-063 — Backpressure

The system shall implement queue backpressure during traffic spikes.

---

## 5.9 Reliability Requirements

## SR-064 — Fault Isolation

SMS failures shall not affect other SalesGenie channels.

## SR-065 — Provider Failure Recovery

Provider outages shall trigger:

* Detection
* Retry
* Queueing
* Alerting
* Failover where supported

## SR-066 — Circuit Breaker

External provider failures shall activate circuit breakers where appropriate.

## SR-067 — Duplicate Protection

Provider retries shall not result in duplicate business actions.

## SR-068 — Disaster Recovery

Critical SMS conversation data shall be recoverable according to SalesGenie's disaster-recovery objectives.

## SR-069 — Observability

The system shall monitor:

* Inbound volume
* Outbound volume
* Delivery success
* Delivery failure
* Provider latency
* Webhook failures
* Queue depth
* AI latency
* AI failures
* Human escalations
* SLA breaches

SalesGenie's performance and reliability architecture requires monitoring of API latency, queue behavior, worker concurrency, retry storms, dead-letter queues, external-provider failures, and service degradation.

---

## 6. Functional Requirements

## FR-001 — SMS Provider Connection

Authorized administrators shall be able to connect an SMS provider.

The system shall:

1. Authenticate the administrator.
2. Validate provider configuration.
3. Store credentials securely.
4. Validate provider connectivity.
5. Register required webhooks.
6. Validate inbound messaging.
7. Validate outbound messaging.
8. Mark the integration active.

---

## FR-002 — SMS Number Registration

Administrators shall be able to associate a phone number with:

* Tenant
* Organization
* Workspace
* Support team
* Sales team
* AI agent
* Routing policy

---

## FR-003 — Integration Health

The system shall expose integration states:

```text
CONNECTED
CONFIGURATION_REQUIRED
CREDENTIAL_ERROR
WEBHOOK_ERROR
PROVIDER_ERROR
RATE_LIMITED
NUMBER_UNAVAILABLE
SUSPENDED
DISCONNECTED
```

---

## FR-004 — Inbound SMS Processing

The system shall:

1. Receive provider webhook.
2. Authenticate webhook.
3. Validate payload.
4. Resolve provider.
5. Resolve SMS number.
6. Resolve tenant.
7. Normalize phone number.
8. Deduplicate event.
9. Persist event.
10. Resolve customer.
11. Resolve conversation.
12. Publish message event.
13. Trigger routing.
14. Trigger AI or human processing.

---

## FR-005 — Message Normalization

The canonical message object shall contain:

```text
message_id
provider_message_id
tenant_id
organization_id
channel = sms
phone_number_id
conversation_id
customer_id
sender_phone
recipient_phone
sender_type
message_type
content
timestamp
delivery_status
metadata
source_event_id
```

---

## FR-006 — Customer Resolution

The system shall:

1. Normalize sender phone number.
2. Search customer identity records.
3. Match existing customer.
4. Create a customer profile when appropriate.
5. Associate the phone number with the customer.
6. Update authorized metadata.

---

## FR-007 — Conversation Creation

The system shall automatically create a conversation when an unknown SMS customer sends a new message.

---

## FR-008 — Conversation Context

The system shall maintain:

* Current messages
* Historical messages
* Customer profile
* Tickets
* AI state
* Human state
* Workflow state
* Lead state
* Sales context
* Relevant knowledge
* Consent state

---

## FR-009 — Intent Detection

The AI shall classify intents including:

```text
GENERAL_SUPPORT
TECHNICAL_SUPPORT
BILLING
ORDER_STATUS
PRODUCT_INQUIRY
PRICING
SALES
LEAD_GENERATION
COMPLAINT
REFUND
ACCOUNT_SUPPORT
HUMAN_AGENT_REQUEST
APPOINTMENT
FOLLOW_UP
```

Organizations shall be able to customize intent taxonomies.

---

## FR-010 — Entity Extraction

The AI shall extract relevant entities including:

* Customer name
* Product
* Order ID
* Invoice ID
* Account ID
* Company
* Location
* Date
* Amount
* Budget
* Timeline
* Requirement

---

## FR-011 — Sentiment Detection

The system shall classify sentiment:

```text
POSITIVE
NEUTRAL
NEGATIVE
FRUSTRATED
ANGRY
URGENT
SATISFIED
```

---

## FR-012 — Urgency Detection

The AI shall identify urgent requests.

Urgency shall influence:

* Priority
* Routing
* SLA
* Escalation
* Notifications

---

## FR-013 — Knowledge Retrieval

The system shall:

1. Convert customer SMS into retrieval query.
2. Search authorized knowledge.
3. Apply tenant filtering.
4. Rank retrieved content.
5. Validate knowledge freshness.
6. Provide evidence to the AI.

---

## FR-014 — AI Response Generation

The AI shall generate responses using:

* Current conversation
* Customer context
* Retrieved knowledge
* Organization instructions
* Agent configuration
* Workflow state
* Messaging policies

---

## FR-015 — AI Response Validation

Before sending an AI response, the system shall validate:

* Relevance
* Grounding
* Confidence
* Safety
* Policy compliance
* Customer authorization
* Tool authorization
* Messaging eligibility

---

## FR-016 — AI Response Delivery

Validated AI responses shall be sent through the configured SMS provider.

---

## FR-017 — Human Request Detection

The AI shall recognize requests such as:

```text
Talk to an agent
Human please
I want customer support
Connect me to someone
Can I speak with a real person?
```

The conversation shall then be routed to human support.

---

## FR-018 — AI-to-Human Handoff

The system shall transfer conversations while preserving:

* Customer profile
* Conversation history
* AI summary
* Intent
* Sentiment
* Priority
* Lead score
* SLA state
* Escalation reason
* Relevant knowledge
* Recommended next action

---

## FR-019 — Human-to-AI Handoff

Authorized agents shall be able to return a conversation to AI.

---

## FR-020 — Hybrid Conversation State

The system shall support:

```text
AI_ACTIVE
AI_ASSISTED_HUMAN
HUMAN_ACTIVE
WAITING_FOR_CUSTOMER
WAITING_FOR_AGENT
ESCALATED
RESOLVED
CLOSED
```

---

## FR-021 — Confidence-Based Escalation

The system shall support configurable rules:

```text
IF ai_confidence < configured_threshold
THEN
    escalate_to_human = true
```

---

## FR-022 — Sentiment-Based Escalation

The system shall support:

```text
IF sentiment = CRITICAL_NEGATIVE
THEN
    priority = HIGH
    route = HUMAN_SUPPORT
```

---

## FR-023 — SLA-Based Escalation

The system shall escalate conversations approaching SLA breach.

---

## FR-024 — Intelligent Routing

The routing engine shall consider:

* Intent
* Skill
* Team
* Agent availability
* Language
* Customer tier
* Sentiment
* Priority
* SLA status
* Sales stage

---

## FR-025 — Agent Assignment

Authorized supervisors shall be able to:

* Assign
* Reassign
* Transfer
* Escalate
* Unassign

SMS conversations.

---

## FR-026 — Ticket Creation

Tickets shall be creatable by:

* AI
* Human agents
* Workflows
* Escalation rules
* Customers where configured

---

## FR-027 — Ticket Synchronization

SMS conversations and tickets shall share a common customer and conversation identity.

---

## FR-028 — SLA Management

The system shall:

* Start SLA timers.
* Track first response.
* Track resolution deadlines.
* Detect risk.
* Notify agents.
* Escalate breaches.
* Record SLA metrics.

---

## FR-029 — Workflow Triggers

SMS events shall trigger SalesGenie workflows.

Example:

```text
SMS RECEIVED
      |
      v
Intent Detection
      |
      v
Customer Support Request
      |
      v
Ticket Creation
      |
      v
Priority Calculation
      |
      v
Agent Routing
      |
      v
Agent Notification
```

---

## FR-030 — Sales Workflow

Example:

```text
SMS RECEIVED
      |
      v
Purchase Intent Detection
      |
      v
Lead Qualification
      |
      v
Lead Score
      |
      v
CRM Lead Creation
      |
      v
Sales Assignment
      |
      v
Human Sales Follow-up
```

---

## FR-031 — AI Tool Calling

The AI shall be able to call authorized tools such as:

* Customer lookup
* CRM lookup
* Ticket lookup
* Order lookup
* Product lookup
* Knowledge search
* Calendar lookup
* Workflow execution

---

## FR-032 — Tool Authorization

The AI shall not execute privileged actions solely because the customer requested them.

The system shall validate:

* Tenant permission
* User authorization
* Agent authorization
* Tool permission
* Customer ownership
* Required confirmation

---

## FR-033 — Tool Execution Budget

The system shall enforce configurable limits for:

* Maximum tool calls
* Maximum workflow steps
* Maximum retries
* Maximum execution time
* Maximum AI tokens
* Maximum outbound messages

SalesGenie's agent architecture explicitly requires execution budgets and protection against infinite loops, recursive workflows, repeated messages, duplicate actions, and runaway costs.

---

## FR-034 — Lead Scoring

The system shall calculate lead scores based on configurable signals:

* Intent
* Engagement
* Product interest
* Budget
* Timeline
* Company
* Industry
* Customer value
* Purchase intent

---

## FR-035 — Lead Qualification

The AI shall classify leads:

```text
UNQUALIFIED
MARKETING_QUALIFIED
SALES_QUALIFIED
HIGH_INTENT
HOT
CUSTOMER
```

---

## FR-036 — CRM Synchronization

Authorized SMS customer and lead information shall synchronize with supported CRM platforms.

---

## FR-037 — AI Conversation Summary

The AI shall generate:

* Customer objective
* Main issue
* Important details
* Sentiment
* Actions taken
* Pending actions
* Recommended next action
* Escalation reason

---

## FR-038 — AI Suggested Replies

Human agents shall receive AI-generated response suggestions.

Agents shall be able to:

* Accept
* Edit
* Regenerate
* Reject

suggestions.

---

## FR-039 — Next-Best Action

The system shall recommend actions based on:

* Customer intent
* Sentiment
* Customer value
* Conversation history
* Business rules
* Sales stage
* Support stage

---

## FR-040 — Conversation Search

Authorized users shall search conversations by:

* Customer
* Phone number
* Conversation ID
* Message content
* Ticket
* Intent
* Sentiment
* Agent
* Date
* Tags
* Status

---

## FR-041 — Conversation Tags

Agents shall apply tags including:

```text
VIP
HIGH_PRIORITY
SALES_LEAD
COMPLAINT
BILLING
TECHNICAL
ESCALATED
FOLLOW_UP
CHURN_RISK
UPSELL
```

---

## FR-042 — Internal Notes

Human agents shall create private internal notes associated with conversations.

---

## FR-043 — Opt-Out Processing

The system shall recognize configured opt-out messages.

Examples:

```text
STOP
UNSUBSCRIBE
CANCEL
END
QUIT
```

The exact keywords and handling shall be configurable according to provider, jurisdiction, and messaging policy.

Upon valid opt-out:

1. Update consent state.
2. Record timestamp.
3. Record source.
4. Stop prohibited outbound messaging.
5. Notify relevant systems.
6. Audit the action.

---

## FR-044 — Opt-In Processing

The system shall support configured opt-in workflows.

The system shall record:

* Consent source
* Timestamp
* Channel
* Phone number
* Consent type
* Policy/version
* Confirmation status

---

## FR-045 — Consent Enforcement

Every outbound SMS operation shall evaluate consent and messaging-policy state before delivery.

---

## FR-046 — Customer Notifications

The system shall support configurable notifications for:

* Ticket creation
* Ticket update
* Agent assignment
* Appointment
* SLA warning
* SLA breach
* Order update
* Payment notification
* Lead follow-up
* Support escalation

---

## FR-047 — Delivery Status

The system shall process provider delivery events such as:

```text
QUEUED
SENT
DELIVERED
FAILED
UNDELIVERED
REJECTED
UNKNOWN
```

---

## FR-048 — Delivery Failure Handling

When an SMS fails:

1. Store provider error.
2. Update message state.
3. Retry only when safe.
4. Avoid duplicate delivery.
5. Notify appropriate internal systems.
6. Escalate persistent failures.

---

## FR-049 — Conversation Analytics

The system shall provide:

* Total SMS conversations
* Active conversations
* Resolved conversations
* Messages sent
* Messages received
* New customers
* Returning customers
* AI conversations
* Human conversations
* Hybrid conversations
* Escalations
* Tickets
* Leads
* Conversion rate
* First response time
* Resolution time
* CSAT
* SLA compliance

---

## FR-050 — AI Analytics

The system shall measure:

* AI containment rate
* AI resolution rate
* AI escalation rate
* AI confidence
* AI latency
* AI failure rate
* Retrieval quality
* Groundedness
* Tool success
* Human takeover rate

---

## FR-051 — Human Agent Analytics

The system shall measure:

* Conversations handled
* First response time
* Average response time
* Resolution time
* SLA compliance
* CSAT
* Escalation rate
* Active workload
* AI assistance usage

---

## FR-052 — SMS Provider Analytics

The system shall provide:

* Message volume
* Delivery rate
* Failure rate
* Provider latency
* Provider error rate
* Number utilization
* Cost
* Retry rate
* Rate-limit events

---

## FR-053 — Cost Analytics

The system shall track SMS communication costs by:

* Tenant
* Organization
* Phone number
* Provider
* Country
* Conversation
* Campaign
* Workflow
* User

---

## FR-054 — AI Cost Analytics

The system shall separately track:

* LLM cost
* Embedding cost
* RAG cost
* Tool cost
* Workflow cost
* Total AI cost

SalesGenie's platform architecture requires tenant-level usage metering, cost-per-conversation analysis, cost controls, model-routing policies, and safeguards against runaway agents and unexpected provider bills.

---

## FR-055 — Customer Feedback

The system shall collect available customer feedback.

---

## FR-056 — Customer Satisfaction

The system shall calculate:

* CSAT
* First-contact resolution
* Resolution time
* Repeat-contact rate
* AI containment
* Human takeover
* Escalation rate

---

## FR-057 — Audit Logs

The system shall record:

* Provider connection
* Provider disconnection
* Number configuration
* Credential changes
* Consent changes
* Agent assignment
* AI-to-human handoff
* Human-to-AI handoff
* Tool execution
* Workflow execution
* Ticket changes
* Data exports
* Administrative actions

---

## FR-058 — Data Export

Authorized users shall be able to export SMS conversation information according to permissions.

---

## FR-059 — Data Deletion

Authorized users shall be able to delete or anonymize customer communication data according to retention and compliance policies.

---

## FR-060 — Failure Recovery

The system shall recover safely from:

* Provider outage
* Webhook outage
* AI provider outage
* Database outage
* Redis outage
* Queue failure
* CRM failure
* Workflow failure
* Network timeout

---

## 7. Advanced AI Functional Requirements

## FR-061 — Customer Intelligence

The system shall continuously derive customer intelligence from authorized SMS conversations.

## FR-062 — Conversation Intelligence

The AI shall extract:

* Intent
* Topics
* Sentiment
* Entities
* Pain points
* Objections
* Purchase signals
* Churn signals
* Upsell signals
* Escalation signals

## FR-063 — Churn Detection

The AI shall identify configurable churn-risk indicators.

## FR-064 — Upsell Detection

The AI shall identify relevant cross-sell and upsell opportunities.

## FR-065 — Complaint Detection

The AI shall identify complaints and increase priority when appropriate.

## FR-066 — Knowledge Gap Detection

The system shall identify recurring SMS questions that cannot be answered from the existing knowledge base.

## FR-067 — AI Feedback

Agents shall be able to rate AI responses:

```text
CORRECT
INCORRECT
HELPFUL
UNHELPFUL
UNSAFE
MISSING_KNOWLEDGE
REQUIRES_ESCALATION
```

## FR-068 — AI Improvement Pipeline

Feedback shall support improvement of:

* Prompts
* RAG retrieval
* Knowledge base
* Routing
* AI agents
* Evaluation datasets
* Escalation policies

---

## 8. Data Requirements

## 8.1 SMS Provider

```text
provider_id
tenant_id
organization_id
provider_name
account_reference
credential_reference
status
created_at
updated_at
```

## 8.2 SMS Phone Number

```text
phone_number_id
tenant_id
organization_id
provider_id
phone_number
country
capabilities
status
support_team_id
sales_team_id
ai_agent_id
created_at
updated_at
```

## 8.3 Customer

```text
customer_id
tenant_id
phone_number
display_name
language
customer_type
customer_tier
consent_state
tags
created_at
updated_at
```

## 8.4 Conversation

```text
conversation_id
tenant_id
customer_id
channel = sms
phone_number_id
status
priority
assigned_agent_id
assigned_team_id
ai_agent_id
intent
sentiment
lead_score
sla_status
consent_state
created_at
updated_at
resolved_at
```

## 8.5 Message

```text
message_id
conversation_id
provider_message_id
sender_type
sender_phone
recipient_phone
message_type
content
timestamp
delivery_status
provider_status
error_code
ai_generated
human_generated
workflow_generated
```

## 8.6 AI Analysis

```text
analysis_id
conversation_id
intent
sentiment
entities
confidence
lead_score
purchase_intent
churn_score
upsell_score
escalation_score
risk_score
retrieval_quality
created_at
```

## 8.7 Consent Record

```text
consent_id
customer_id
phone_number
consent_type
consent_state
source
timestamp
policy_version
evidence_reference
created_at
updated_at
```

## 8.8 Escalation

```text
escalation_id
conversation_id
reason
priority
source
ai_confidence
sentiment
assigned_team
assigned_agent
created_at
resolved_at
```

---

## 9. AI-Human Decision Architecture

```text
                         SMS
                          |
                          v
                 Provider Webhook
                          |
                          v
                 Authentication
                          |
                          v
                  Schema Validation
                          |
                          v
                   Deduplication
                          |
                          v
                 Message Normalizer
                          |
                          v
                 Customer Resolution
                          |
                          v
                Conversation Context
                          |
                          v
             Intent / Entity / Sentiment
                          |
                          v
                  Consent Check
                          |
                          v
                  AI Decision Engine
                          |
              +-----------+-----------+
              |                       |
       AI Confidence HIGH       Confidence LOW
              |                       |
              v                       v
       Knowledge Retrieval       Human Routing
              |                       |
              v                       v
       Response Generation       Agent Workspace
              |                       |
              v                       v
        Safety Validation        Human Response
              |                       |
              +-----------+-----------+
                          |
                          v
                  Consent Validation
                          |
                          v
                    SMS Provider
                          |
                          v
                     Customer
                          |
                          v
             Analytics / Audit / Learning
```

---

## 10. AI Containment Policy

The system shall permit autonomous AI resolution only when all configured conditions pass.

```text
IF
    intent_supported = true
    AND knowledge_confidence >= threshold
    AND safety_check = PASS
    AND policy_check = PASS
    AND consent_check = PASS
    AND customer_did_not_request_human = true
    AND tool_authorization = valid
THEN
    AI may respond
ELSE
    escalate_to_human
```

---

## 11. Human Escalation Policy

```text
IF
    customer_requests_human
    OR ai_confidence < threshold
    OR sentiment = critical_negative
    OR security_risk = true
    OR policy_risk = true
    OR repeated_ai_failure >= configured_limit
    OR high_value_customer = true
    OR sla_breach_risk = true
THEN
    create_escalation
    preserve_context
    generate_ai_summary
    calculate_priority
    assign_human_team
    notify_agent
```

---

## 12. SMS Event Processing

The system shall support applicable SMS provider events through the canonical event layer.

```text
INBOUND_MESSAGE
OUTBOUND_MESSAGE
MESSAGE_STATUS
DELIVERY_SUCCESS
DELIVERY_FAILURE
UNDELIVERED
PROVIDER_ERROR
OPT_IN
OPT_OUT
CONSENT_CHANGE
NUMBER_CHANGE
```

---

## 13. Security and Trust Model

## 13.1 Incoming SMS Trust

All customer-generated SMS content shall be treated as untrusted external input.

```text
External SMS
     |
     v
Webhook Authentication
     |
     v
Schema Validation
     |
     v
Tenant Resolution
     |
     v
Prompt Injection Detection
     |
     v
AI Policy Enforcement
     |
     v
Authorized Processing
```

## 13.2 Tool Execution

```text
Customer SMS
      |
      v
Intent Detection
      |
      v
Tool Candidate
      |
      v
Authorization Check
      |
      +---- DENY ----> Safe Response
      |
      v
Confirmation Requirement
      |
      +---- REQUIRED --> Customer Confirmation
      |
      v
Tool Execution
      |
      v
Audit Log
```

---

## 14. Outbound Messaging Decision Engine

Every outbound SMS shall pass through a centralized policy engine.

```text
Outbound Message
       |
       v
Recipient Validation
       |
       v
Consent Check
       |
       +---- DENY ----> Block
       |
       v
Tenant Policy Check
       |
       v
Rate Limit Check
       |
       v
Messaging Policy Check
       |
       v
Risk Classification
       |
       +---- HIGH RISK ----> Human Approval
       |
       v
Provider Selection
       |
       v
Idempotency Check
       |
       v
Send SMS
       |
       v
Delivery Tracking
```

---

## 15. Non-Functional Requirements

## NFR-001 — Availability

The SMS service shall target enterprise-grade availability consistent with SalesGenie's production SLA.

## NFR-002 — Scalability

The system shall horizontally scale:

* Webhook ingestion
* Message processing
* AI orchestration
* Workflow execution
* Agent workloads

## NFR-003 — Security

The system shall implement:

* Zero-trust principles
* Least privilege
* RBAC
* Encryption
* Secret management
* Audit logging
* Tenant isolation

## NFR-004 — Observability

The system shall provide:

* Structured logs
* Metrics
* Distributed tracing
* Health checks
* Error tracking
* Alerting

## NFR-005 — Maintainability

Provider-specific SMS logic shall remain isolated behind adapters.

## NFR-006 — Extensibility

The SMS module shall reuse SalesGenie's shared:

* Conversation model
* Customer model
* AI orchestration
* Knowledge retrieval
* Routing
* Ticketing
* SLA
* Analytics
* Workflow engine

## NFR-007 — Internationalization

The system shall support multilingual SMS where technically and operationally supported.

## NFR-008 — Data Consistency

Distributed conversation, ticket, customer, workflow, and consent states shall remain consistent.

## NFR-009 — API Resilience

Provider API changes, outages, rate limits, and errors shall be isolated within the provider integration layer.

## NFR-010 — Cost Efficiency

The system shall minimize:

* Duplicate SMS
* Unnecessary AI calls
* Repeated retrieval
* Excessive workflow execution
* Runaway agent behavior

---

## 16. Enterprise Acceptance Criteria

The SMS Channel shall be considered production-ready when:

* An SMS provider can be securely connected.
* A business phone number can be configured.
* Provider credentials are securely stored.
* Webhooks are authenticated.
* Incoming SMS events are validated.
* Duplicate events are prevented.
* Phone numbers are normalized.
* Customers are correctly resolved.
* Conversations are created correctly.
* AI responses are context-aware.
* RAG responses are grounded.
* AI hallucinations are mitigated.
* Unsupported requests are handled safely.
* AI confidence controls work.
* Human requests are detected.
* AI-to-human handoff preserves context.
* Human agents can send SMS responses.
* Human-to-AI handoff works.
* Hybrid conversations work.
* Intelligent routing works.
* Ticket creation works.
* SLA tracking works.
* Lead qualification works.
* CRM synchronization works.
* Consent is enforced.
* Opt-out is enforced.
* Unauthorized outbound communication is blocked.
* Delivery statuses are tracked.
* Provider failures are handled.
* Retry mechanisms work.
* Dead-letter processing works.
* Duplicate outbound messages are prevented.
* AI tool authorization is enforced.
* Prompt injection protections are active.
* AI execution budgets are enforced.
* Customer data is tenant-isolated.
* Audit logs are generated.
* SMS costs are measured.
* AI costs are measured.
* Messenger/other channel failures do not affect SMS.
* SMS failures do not affect other SalesGenie channels.
* Load testing is completed.
* Security testing is completed.
* AI evaluation is completed.
* Consent and messaging-policy tests are completed.
* Production monitoring is operational.

---

## 17. Success Metrics

## Customer Experience

* CSAT
* Customer effort score
* First-contact resolution
* Resolution time
* Repeat-contact rate
* Complaint rate
* Customer retention

## AI Performance

* AI containment rate
* AI resolution rate
* AI escalation rate
* AI confidence
* Grounded-response rate
* Hallucination rate
* AI response latency
* AI failure rate
* Tool execution success

## Human Support

* First response time
* Average response time
* Resolution time
* SLA compliance
* Agent utilization
* Agent workload
* CSAT
* Escalation rate

## Sales

* SMS leads
* Qualified leads
* Lead conversion
* Opportunities created
* Sales conversion
* Revenue attributed to SMS
* Average deal value

## Messaging

* Inbound messages
* Outbound messages
* Delivery rate
* Failure rate
* Undelivered rate
* Provider latency
* Webhook success rate
* Webhook failure rate
* Retry rate
* Duplicate rate
* Opt-out rate
* Opt-in rate

## Cost

* Cost per SMS
* Cost per conversation
* Cost per resolved ticket
* AI cost per conversation
* Provider cost per tenant
* Total communication cost
* Total AI communication cost

---

## 18. Definition of Done

The SalesGenie SMS Channel shall be considered complete only when:

1. Customers can communicate with SalesGenie organizations through SMS.
2. AI agents can autonomously resolve supported requests.
3. AI responses are grounded in authorized organizational knowledge.
4. AI can detect intent, entities, sentiment, urgency, and business signals.
5. Human agents can seamlessly take over AI conversations.
6. AI can assist human agents.
7. Customer context remains available throughout the lifecycle.
8. SMS events are reliably normalized into SalesGenie's canonical conversation model.
9. Inbound and outbound messages are idempotent.
10. Delivery states are tracked.
11. Provider failures are recoverable.
12. Tickets can be created from SMS conversations.
13. SLA policies are enforceable.
14. Intelligent routing works.
15. Leads can be qualified.
16. CRM integrations can synchronize authorized information.
17. AI summaries are generated.
18. AI suggested replies work.
19. Customer consent is enforced.
20. Opt-out is reliably processed.
21. Unauthorized outbound messaging is blocked.
22. Customer satisfaction can be measured.
23. AI performance can be measured.
24. Human-agent performance can be measured.
25. Provider performance can be measured.
26. SMS and AI costs can be measured.
27. Audit logs cover critical operations.
28. Tenant isolation is guaranteed.
29. Prompt injection protection is active.
30. Unauthorized tool execution is blocked.
31. AI execution budgets are enforced.
32. High-risk actions support human approval.
33. Webhook failures can be recovered.
34. Duplicate events cannot create duplicate business actions.
35. The SMS service supports horizontal scaling.
36. Provider-specific functionality is isolated behind adapters.
37. Security, load, reliability, consent, and AI-quality testing are complete.
38. Monitoring and alerting are operational.
39. Disaster recovery procedures have been tested.
40. The module is suitable for enterprise production deployment.
