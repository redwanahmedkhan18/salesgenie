# SalesGenie — Human Support Agent

<!-- Source basis: SalesGenie support-agent role, ticket model, RBAC, analytics, AI/RAG, human-in-the-loop, security, observability, and production-readiness requirements from the project's stored materials. -->

## FAANG-Level User Requirements, System Requirements & Functional Requirements

**Project:** SalesGenie  
**Module:** Human Support Agent  
**Architecture:** Enterprise Multi-Tenant SaaS + AI/Human Hybrid Support  
**Primary Users:** Support Agents, Support Managers, Organization Admins, Workplace Admins, Super Admins  
**Supporting Systems:** AI Gateway, Multi-Agent Orchestration, RAG, CRM, Ticketing, Omnichannel Messaging, Workflow Engine, Analytics, Audit, Billing, Notification and Integration Services  
**Requirement Standard:** Production-grade / FAANG-level

---

## 1. Module Vision

The Human Support Agent module shall provide a unified enterprise workspace through which human support agents can:

- Receive customer support requests.
- Handle conversations across multiple communication channels.
- Manage support tickets.
- Take over conversations from AI agents.
- Collaborate with AI copilots.
- Search enterprise knowledge.
- Access authorized customer context.
- Diagnose and resolve customer problems.
- Escalate complex issues.
- Transfer tickets to specialized teams.
- Manage SLA commitments.
- Execute approved support workflows.
- Record internal notes.
- Track resolution history.
- Collaborate with other agents.
- Monitor personal workload.
- Receive AI-generated recommendations.
- Review AI-generated summaries.
- Maintain full accountability for human actions.
- Provide feedback to improve AI support quality.

The Human Support Agent shall remain the authoritative decision-maker for actions assigned to human responsibility.

AI assistance shall augment the human agent rather than silently replacing human judgment for governed or high-impact operations.

---

## 2. Design Principles

The module shall follow these principles:

1. **Human ownership**
2. **AI-assisted productivity**
3. **Customer-context continuity**
4. **Omnichannel operation**
5. **Single source of truth**
6. **Least-privilege access**
7. **Strict tenant isolation**
8. **Auditable actions**
9. **SLA-driven operations**
10. **Deterministic state transitions**
11. **Observable workflows**
12. **Fault tolerance**
13. **Secure-by-default design**
14. **Evidence-grounded AI**
15. **Explicit human approval for high-impact actions**
16. **No ownerless tickets**
17. **No silent AI actions**
18. **Continuous quality improvement**

---

## 3. Human Support Agent Role

The platform shall define:

```text
support_agent
```

as a first-class RBAC role.

The Support Agent shall operate within the permissions granted by:

```text
Tenant
    ↓
Organization
    ↓
Workplace
    ↓
Team
    ↓
Role
    ↓
Permission
    ↓
Resource
```

The Support Agent shall never receive access merely because a frontend component exposes an action.

All authorization shall be enforced server-side.

---

## 4. Support Agent Permission Domains

The Support Agent permission model shall support granular permissions such as:

```text
support:read
support:write

ticket:read
ticket:create
ticket:update
ticket:assign
ticket:transfer
ticket:escalate
ticket:resolve
ticket:reopen
ticket:close

conversation:read
conversation:write
conversation:takeover
conversation:release
conversation:transfer
conversation:escalate

customer:read
customer:write

knowledge:read

ai:use
ai:suggest
ai:summarize
ai:translate
ai:classify
ai:recommend

attachment:read
attachment:write

workflow:execute

notification:read

analytics:read

internal_note:read
internal_note:write

audit:read
```

High-impact permissions shall be independently controllable.

---

## 5. User Requirements

## UR-001 — Agent Authentication

The Support Agent shall be able to securely authenticate into SalesGenie.

The system shall support configured authentication mechanisms including:

* Email/password
* MFA
* SSO
* OAuth/OIDC
* Enterprise identity providers

---

## UR-002 — Agent Session Management

The agent shall be able to:

* View active sessions where permitted.
* Sign out.
* Refresh an authenticated session.
* Re-authenticate when required.
* Complete MFA challenges.
* Terminate compromised sessions where authorized.

---

## UR-003 — Agent Dashboard

The Support Agent shall have a personalized dashboard containing:

* Assigned tickets
* Unassigned queue
* Active conversations
* Pending responses
* SLA-at-risk tickets
* Escalated tickets
* High-priority tickets
* Recently resolved tickets
* Customer follow-ups
* AI recommendations
* Notifications
* Performance metrics

---

## 6. Agent Work Queue

## UR-004 — Unified Work Queue

The agent shall have a unified work queue for support work.

The queue shall support:

* Assigned tickets
* Assigned conversations
* Pending tickets
* Escalations
* Transfers
* Follow-ups
* SLA-risk cases

---

## UR-005 — Queue Filtering

The agent shall be able to filter work by:

```text
status
priority
customer
category
product
channel
team
SLA
assignment
created_at
updated_at
language
sentiment
AI confidence
```

---

## UR-006 — Queue Sorting

The agent shall be able to sort tickets by:

* Priority
* SLA urgency
* Creation time
* Last customer response
* Customer tier
* AI confidence
* Sentiment
* Assignment
* Updated time

---

## UR-007 — Queue Search

The agent shall be able to search tickets and conversations using:

* Ticket ID
* Customer name
* Email
* Phone
* Subject
* Message content
* Product
* Category
* Tags

---

## 7. Ticket Management Requirements

The Support Agent shall be able to manage the complete ticket lifecycle.

Supported states shall include:

```text
NEW
OPEN
IN_PROGRESS
WAITING_FOR_CUSTOMER
WAITING_FOR_INTERNAL_TEAM
ESCALATED
TRANSFERRED
PENDING
RESOLVED
CLOSED
REOPENED
```

---

## UR-008 — Ticket Creation

The agent shall be able to manually create a support ticket.

Required information may include:

```text
customer
title
description
category
priority
product
channel
assignment
```

---

## UR-009 — Ticket Editing

Authorized agents shall be able to modify permitted ticket fields.

---

## UR-010 — Ticket Priority

The agent shall be able to set priority according to permission.

Supported priority levels:

```text
LOW
MEDIUM
HIGH
URGENT
CRITICAL
```

---

## UR-011 — Ticket Assignment

The agent shall be able to:

* Assign tickets to self.
* Assign tickets to authorized agents.
* Assign tickets to authorized teams.
* Request reassignment.

---

## UR-012 — Ticket Transfer

The agent shall be able to transfer a ticket to another authorized team or agent.

Every transfer shall preserve:

* Ticket history
* Conversation history
* Internal notes
* Attachments
* SLA state
* Customer context
* AI context

---

## UR-013 — Ticket Escalation

The agent shall be able to escalate tickets to:

* Support Manager
* Technical Specialist
* Billing Team
* Security Team
* Sales Team
* Product Team
* Other configured teams

---

## UR-014 — Ticket Resolution

The agent shall be able to resolve tickets when the customer issue has been addressed.

The agent shall provide a resolution classification where required.

---

## UR-015 — Ticket Reopening

The agent shall be able to reopen eligible tickets.

---

## UR-016 — Internal Notes

Agents shall be able to create private notes.

Internal notes shall never be exposed to customers.

---

## 8. Customer 360 Requirements

## UR-017 — Customer Profile

The agent shall be able to view authorized customer information.

The customer profile may include:

```text
customer_id
name
email
phone
company
job_title
customer_tier
lead_status
lead_score
lifetime_value
total_orders
last_interaction
segments
tags
```

---

## UR-018 — Customer Interaction History

The agent shall be able to view:

* Previous tickets
* Previous conversations
* Previous resolutions
* Previous escalations
* Customer feedback
* Relevant CRM interactions

---

## UR-019 — Customer Timeline

The system shall provide a chronological customer timeline.

The timeline shall unify authorized events across channels.

---

## 9. Omnichannel Requirements

The agent shall be able to manage supported communication channels through a unified workspace.

Potential channels include:

```text
Website Chat
Email
WhatsApp
Telegram
Slack
Microsoft Teams
SMS
Voice
Social Messaging
```

The actual channel availability shall depend on tenant configuration.

---

## UR-020 — Unified Conversation

The agent shall not need separate support interfaces for each supported channel.

---

## UR-021 — Channel Context

The agent shall be able to identify:

* Channel
* Customer identity
* Conversation origin
* Message timestamps
* Delivery status
* Previous interactions

---

## UR-022 — Cross-Channel Context

When the same customer moves between channels, authorized context shall remain available.

---

## 10. Human Takeover Requirements

## UR-023 — AI-to-Human Handoff

The Support Agent shall be able to take over conversations from AI.

The handoff package shall contain:

```text
customer
conversation
intent
summary
priority
sentiment
AI confidence
AI actions
knowledge used
attempted resolutions
unresolved questions
recommended next action
```

---

## UR-024 — Immediate Human Takeover

The agent shall be able to take over an active AI conversation when permitted.

---

## UR-025 — Human Authority

Once the human agent takes over:

* AI shall not independently send customer-facing messages.
* AI may continue operating as a copilot.
* Human messages shall be explicitly identified as human-generated.
* Human decisions shall remain authoritative.

---

## UR-026 — AI Assistance During Human Support

The agent shall be able to request AI assistance without surrendering conversation control.

---

## 11. AI Copilot Requirements

## UR-027 — AI Suggested Reply

The agent shall be able to generate response suggestions.

---

## UR-028 — AI Summary

The agent shall be able to request:

* Conversation summary
* Customer summary
* Case summary
* Previous-resolution summary

---

## UR-029 — AI Knowledge Recommendation

The AI copilot shall recommend relevant knowledge articles.

---

## UR-030 — AI Next Best Action

The AI shall recommend appropriate next steps.

---

## UR-031 — AI Translation

The agent shall be able to translate customer messages or responses where configured.

---

## UR-032 — AI Tone Transformation

The agent shall be able to request controlled response styles such as:

```text
professional
concise
empathetic
technical
friendly
formal
```

---

## UR-033 — AI Similar Case Search

The agent shall be able to retrieve similar previously resolved cases.

---

## UR-034 — AI Customer Sentiment

The agent shall be able to view AI-generated sentiment indicators.

---

## UR-035 — AI Confidence

The agent shall be able to see AI confidence where the platform exposes it.

---

## 12. Knowledge Requirements

## UR-036 — Knowledge Search

The Support Agent shall be able to search authorized knowledge.

Search shall support:

* Keyword search
* Semantic search
* Hybrid search
* Filters
* Product filtering
* Category filtering
* Version filtering

---

## UR-037 — Knowledge Evidence

Where configured, AI recommendations shall identify the supporting knowledge source.

---

## UR-038 — Knowledge Feedback

The agent shall be able to indicate:

```text
useful
not useful
incorrect
outdated
missing_information
```

---

## 13. SLA Requirements

## UR-039 — SLA Visibility

The agent shall see:

* First response SLA
* Resolution SLA
* Remaining time
* SLA status
* Escalation deadline

---

## UR-040 — SLA Warning

The platform shall notify agents when tickets approach SLA thresholds.

---

## UR-041 — SLA Breach

The system shall identify breached tickets and execute configured escalation policies.

---

## 14. Collaboration Requirements

## UR-042 — Agent Collaboration

Agents shall be able to collaborate on authorized cases.

---

## UR-043 — Mentions

Agents shall be able to mention authorized colleagues in internal notes.

---

## UR-044 — Specialist Assistance

Agents shall be able to request specialist assistance.

---

## UR-045 — Supervisor Assistance

Agents shall be able to request supervisor intervention.

---

## 15. Attachment Requirements

Agents shall be able to:

* Upload attachments.
* Download authorized attachments.
* Preview supported files.
* Attach files to tickets.
* Attach files to conversations.

The system shall validate file type and size.

---

## 16. Notification Requirements

Agents shall receive notifications for:

* New assignments
* Transfers
* Escalations
* Customer replies
* Mentions
* SLA warnings
* SLA breaches
* Supervisor requests
* Approval requests
* Workflow failures
* System incidents

---

## 17. Human Support Agent System Requirements

## 17.1 Agent Workspace Architecture

The frontend shall provide a unified Support Agent Workspace containing:

```text
┌─────────────────────────────────────────────────────┐
│                 Support Agent Workspace             │
├───────────────┬─────────────────────┬───────────────┤
│ Work Queue    │ Conversation /      │ Customer 360  │
│               │ Ticket Workspace    │               │
│ - Assigned    │                     │ - Profile     │
│ - Priority    │ - Messages         │ - History     │
│ - SLA Risk    │ - Internal Notes   │ - Tickets     │
│ - Escalated   │ - AI Copilot       │ - CRM         │
│               │ - Attachments      │ - Timeline    │
├───────────────┴─────────────────────┴───────────────┤
│                 AI Copilot / Knowledge              │
└─────────────────────────────────────────────────────┘
```

---

## 17.2 Ticket Data Model

A support ticket shall contain at minimum:

```text
id
number
tenant_id
organization_id
workplace_id
customer_id

title
description

status
priority
category
subcategory
product

channel
source

assigned_team_id
assigned_agent_id

ai_confidence
ai_classification
ai_summary

sla_policy_id
sla_status
sla_due_at

created_at
updated_at
first_response_at
resolved_at
closed_at

tags
metadata
```

The existing SalesGenie support model already represents ticket identity, title, customer, status, priority, category, AI confidence and timestamps as core ticket attributes.

---

## 18. Conversation System Requirements

Each conversation shall support:

```text
conversation_id
tenant_id
customer_id
channel
status
participants
messages
assigned_agent
assigned_team
ai_participation
human_takeover
created_at
updated_at
closed_at
```

Messages shall support:

```text
message_id
conversation_id
sender_type
sender_id
content
attachments
timestamp
delivery_status
read_status
metadata
```

---

## 19. Human Agent State Machine

The Support Agent shall have an operational state.

Supported states:

```text
OFFLINE
AVAILABLE
BUSY
AWAY
BREAK
IN_TRAINING
DISABLED
```

The routing engine shall consider agent availability before assignment.

---

## 20. Capacity Management

The system shall support configurable agent capacity.

Example:

```text
max_active_chats
max_active_tickets
max_voice_calls
max_concurrent_tasks
```

The routing engine shall avoid overloading agents beyond configured capacity unless an authorized supervisor overrides the policy.

---

## 21. Skill Management

Agents shall have configurable skills.

Example:

```text
technical_support
billing
payments
product_support
enterprise_support
sales_support
security
api_support
integration_support
english
spanish
bengali
```

Each skill may have:

```text
skill_id
name
level
verified
certification
last_verified_at
```

---

## 22. Intelligent Routing Requirements

The routing engine shall support:

### Deterministic Routing

* Skill
* Priority
* Customer tier
* Language
* Channel
* Team
* Availability
* Capacity
* SLA
* Product

### AI-Assisted Routing

AI may recommend:

* Best team
* Best agent
* Required skill
* Complexity
* Priority
* Escalation level

The final assignment shall remain subject to deterministic authorization and routing policies.

---

## 23. One Ticket, One Owner

Every active ticket shall have:

```text
owner_team
owner_agent
```

unless the ticket is explicitly in an unassigned queue.

Multiple collaborators may participate, but accountability shall remain explicit.

---

## 24. Escalation System Requirements

Escalation triggers shall include:

```text
customer_requested_human
low_ai_confidence
negative_sentiment
high_priority
critical_customer
security_issue
privacy_issue
billing_issue
legal_issue
repeated_failure
sla_at_risk
sla_breach
technical_complexity
agent_requested
supervisor_requested
```

Hard escalation policies shall override normal AI confidence decisions for configured high-risk categories.

---

## 25. Human Agent Workflow

```text
Customer Request
       ↓
Omnichannel Gateway
       ↓
Identity Resolution
       ↓
Ticket / Conversation
       ↓
AI Triage
       ↓
Human Routing
       ↓
Support Agent Queue
       ↓
Agent Accepts Case
       ↓
Customer 360 Loaded
       ↓
Conversation History Loaded
       ↓
Knowledge Retrieved
       ↓
AI Copilot Available
       ↓
Agent Diagnoses Issue
       ↓
Agent Responds
       ↓
Customer Response
       ↓
Resolution Verification
       ↓
Resolve
       ↓
Customer Feedback
       ↓
Analytics / QA
```

---

## 26. Functional Requirements

## FR-001 — Login

**Input:**

```json
{
  "email": "agent@example.com",
  "password": "********",
  "tenant_id": "tenant-id",
  "mfa_code": "123456"
}
```

**System shall:**

1. Authenticate the agent.
2. Validate tenant.
3. Validate role.
4. Validate permissions.
5. Validate MFA if required.
6. Create session.
7. Return authorized agent context.

---

## 27. FR-002 — Load Agent Workspace

When the Support Agent opens the workspace, the backend shall return:

```text
agent profile
permissions
active assignments
queue metrics
SLA-risk tickets
notifications
active conversations
AI recommendations
performance summary
```

---

## 28. FR-003 — Fetch Assigned Tickets

The API shall return tickets assigned to the authenticated agent.

The backend shall enforce:

```text
tenant isolation
organization authorization
workplace authorization
team authorization
agent authorization
```

---

## 29. FR-004 — Ticket Assignment

The system shall:

1. Validate agent permission.
2. Validate ticket ownership.
3. Validate target agent.
4. Validate target agent availability.
5. Validate capacity.
6. Update assignment.
7. Generate audit event.
8. Publish assignment event.
9. Notify the target agent.

---

## 30. FR-005 — Accept Ticket

When an agent accepts a ticket:

```text
ticket.status = IN_PROGRESS
ticket.assigned_agent_id = authenticated_agent
```

The transition shall be validated server-side.

---

## 31. FR-006 — Send Customer Message

The system shall:

1. Authenticate agent.
2. Validate conversation access.
3. Validate message.
4. Validate channel.
5. Persist message.
6. Publish event.
7. Deliver message.
8. Record delivery state.
9. Update conversation timestamp.
10. Update SLA state.
11. Generate audit information.

---

## 32. FR-007 — Internal Note

The system shall allow:

```text
POST /support/tickets/{ticket_id}/internal-notes
```

Internal notes shall:

* Be stored securely.
* Be visible only to authorized support personnel.
* Never be sent through customer-facing channels.
* Be included in audit history.

---

## 33. FR-008 — Human Takeover

When the agent takes over an AI conversation:

1. Validate permission.
2. Acquire conversation lock.
3. Set human ownership.
4. Pause autonomous AI customer messaging.
5. Generate/retain AI handoff context.
6. Load customer context.
7. Load conversation history.
8. Load relevant knowledge.
9. Notify relevant services.
10. Record audit event.

---

## 34. FR-009 — AI Copilot Suggestion

The agent shall be able to request:

```text
POST /support/ai/suggest
```

The request shall contain:

```text
conversation_id
ticket_id
customer_context
current_message
requested_style
```

The AI service shall return:

```text
suggested_response
confidence
knowledge_sources
warnings
recommended_action
```

The agent shall remain responsible for approving the response.

---

## 35. FR-010 — AI Summary

The AI copilot shall summarize:

```text
customer_problem
conversation_history
previous_attempts
current_status
important_entities
customer_sentiment
recommended_next_step
```

---

## 36. FR-011 — Knowledge Retrieval

The agent shall be able to request authorized knowledge.

The system shall enforce:

```text
tenant_id
organization_id
workplace_id
knowledge_permissions
document_permissions
```

before retrieval results are returned.

---

## 37. FR-012 — AI Knowledge Citation

AI-generated suggestions shall optionally include:

```text
source_document
source_version
source_section
relevance_score
citation
```

---

## 38. FR-013 — Ticket Escalation

When an agent escalates a ticket:

```text
POST /support/tickets/{ticket_id}/escalate
```

the system shall:

1. Validate permission.
2. Validate target team.
3. Record escalation reason.
4. Update priority if policy requires.
5. Update ownership.
6. Start escalation SLA.
7. Notify receiving team.
8. Record audit event.
9. Publish escalation event.

---

## 39. FR-014 — Ticket Transfer

Transfer shall require:

```text
target_team
target_agent
reason
```

where required by policy.

The system shall preserve the complete ticket history.

---

## 40. FR-015 — Ticket Resolution

Before resolving a ticket, the system may require:

```text
resolution_code
resolution_summary
root_cause
customer_confirmation
```

depending on configuration.

---

## 41. FR-016 — Ticket Reopening

When a customer replies after resolution:

```text
resolved → reopened
```

shall occur automatically where configured.

The system shall preserve the previous resolution state.

---

## 42. FR-017 — SLA Calculation

The SLA engine shall calculate:

```text
first_response_deadline
resolution_deadline
remaining_time
business_time
pause_time
breach_time
```

---

## 43. FR-018 — SLA Escalation

At configurable thresholds:

```text
50% → warning
75% → manager notification
90% → escalation
100% → SLA breach
```

The exact thresholds shall be tenant-configurable.

---

## 44. FR-019 — Customer Search

The agent shall be able to search customers by:

```text
customer_id
email
phone
name
company
ticket_id
```

---

## 45. FR-020 — Customer Timeline

The system shall return a chronological timeline containing authorized:

```text
support tickets
messages
calls
emails
CRM interactions
orders
subscriptions
feedback
escalations
```

---

## 46. FR-021 — Similar Ticket Search

The AI system shall retrieve semantically similar historical tickets.

Results shall include:

```text
ticket_id
similarity
problem
resolution
resolution_quality
knowledge_used
```

---

## 47. FR-022 — Agent Performance Dashboard

The agent shall be able to view permitted personal metrics:

```text
tickets_handled
tickets_resolved
avg_first_response
avg_resolution_time
sla_compliance
reopen_rate
escalation_rate
customer_satisfaction
active_workload
ai_assisted_resolutions
```

---

## 48. FR-023 — Agent Notifications

The notification system shall generate notifications for:

```text
new_ticket
new_message
assignment
transfer
escalation
mention
sla_warning
sla_breach
approval_request
supervisor_message
system_alert
```

---

## 49. FR-024 — Real-Time Updates

The agent workspace shall receive real-time updates for:

* New tickets
* New messages
* Ticket assignments
* Customer replies
* SLA state changes
* Escalations
* AI recommendations
* Agent mentions

WebSocket or equivalent real-time infrastructure shall be used where appropriate.

---

## 50. FR-025 — Concurrency Control

The system shall prevent conflicting updates when multiple agents interact with the same ticket.

Possible mechanisms:

```text
optimistic locking
version numbers
distributed locks
transactional updates
```

---

## 51. FR-026 — Duplicate Message Protection

The platform shall use idempotency keys for channel events and message delivery where required.

Repeated external events shall not produce duplicate customer messages.

---

## 52. FR-027 — Attachment Processing

Uploaded files shall pass through:

```text
authentication
authorization
size validation
content-type validation
malware/security scanning
storage
metadata extraction
access-control validation
```

---

## 53. FR-028 — Support Workflow Execution

Authorized agents shall be able to trigger predefined support workflows.

Examples:

```text
Refund Request
Account Verification
Password Reset
Subscription Issue
Technical Diagnostic
Customer Callback
Escalate to Engineering
Create CRM Task
Create Follow-Up
```

High-risk workflows shall require explicit approval.

---

## 54. FR-029 — Workflow Authorization

The system shall validate:

```text
agent permission
tenant policy
workflow permission
customer authorization
resource authorization
approval requirement
```

before execution.

---

## 55. FR-030 — AI Tool Execution

When an agent uses an AI-supported workflow:

1. Validate agent permission.
2. Validate AI tool permission.
3. Validate input schema.
4. Execute tool.
5. Validate output.
6. Record execution.
7. Apply approval policy.
8. Record outcome.

The platform shall never blindly trust model-generated tool parameters.

---

## 56. FR-031 — Human Approval

Configured high-risk actions shall generate an approval request.

Examples:

```text
refund
financial modification
data export
customer deletion
security modification
bulk communication
account ownership change
```

---

## 57. FR-032 — Audit Logging

Every business-critical agent action shall generate an audit event.

Audit information shall include:

```text
event_id
tenant_id
organization_id
actor_id
actor_role
action
resource_type
resource_id
timestamp
request_id
correlation_id
old_state
new_state
result
reason
metadata
```

---

## 58. FR-033 — Agent Action History

The ticket timeline shall identify:

```text
HUMAN_ACTION
AI_ACTION
SYSTEM_ACTION
CUSTOMER_ACTION
```

where appropriate.

---

## 59. FR-034 — AI/Human Attribution

Customer-facing messages shall retain authoritative attribution.

The platform shall distinguish:

```text
human_generated
ai_generated
ai_suggested_human_approved
system_generated
```

---

## 60. FR-035 — Customer Feedback

After resolution, the system shall optionally request:

```text
CSAT score
rating
comment
resolution feedback
```

---

## 61. FR-036 — Agent Feedback on AI

The agent shall be able to rate AI suggestions:

```text
accepted
edited
rejected
incorrect
unsafe
irrelevant
helpful
```

This feedback shall feed the AI evaluation pipeline.

---

## 62. FR-037 — Knowledge Gap Detection

The system shall identify cases where:

```text
no knowledge found
knowledge outdated
knowledge incorrect
knowledge insufficient
agent manually solved issue
```

and generate knowledge-improvement signals.

---

## 63. FR-038 — Agent Quality Assurance

Support managers shall be able to sample agent conversations according to configured QA policies.

QA criteria may include:

```text
accuracy
professionalism
policy adherence
resolution quality
empathy
response completeness
security compliance
SLA compliance
```

---

## 64. FR-039 — Agent Coaching

The system may generate private coaching recommendations based on:

* QA results
* CSAT
* SLA performance
* Reopen rate
* Escalation patterns
* Customer feedback
* AI-assistance usage

---

## 65. FR-040 — Agent Workload Analytics

Managers shall be able to analyze:

```text
active tickets
tickets per agent
queue backlog
utilization
capacity
response time
resolution time
SLA risk
```

---

## 66. FR-041 — Support Manager Override

Authorized managers shall be able to:

* Reassign tickets.
* Override priority.
* Override routing.
* Override SLA state where policy permits.
* Force escalation.
* Take over conversations.
* Disable an agent.
* Rebalance queues.

Every override shall be audited.

---

## 67. FR-042 — Agent Availability

Agents shall be able to change availability where permitted.

The routing engine shall consume the availability state.

---

## 68. FR-043 — Agent Capacity

The system shall prevent automatic assignment when:

```text
agent.status != AVAILABLE
```

or:

```text
active_workload >= configured_capacity
```

unless an override policy applies.

---

## 69. FR-044 — Language Support

The workspace shall display customer language information.

AI-assisted translation shall be available where configured.

---

## 70. FR-045 — Customer Sentiment Escalation

If customer sentiment deteriorates beyond configured thresholds, the system shall recommend escalation or notify the agent.

---

## 71. FR-046 — High-Value Customer Handling

Customers identified as high-value or enterprise customers may receive:

* Priority routing
* Dedicated support queues
* Senior-agent escalation
* Enhanced SLA
* Additional customer context

---

## 72. FR-047 — Security Incident Support

Tickets classified as security-related shall be routed according to security escalation policy.

Support agents shall not receive access to sensitive security information unless explicitly authorized.

---

## 73. FR-048 — Billing Support

Billing-related tickets shall integrate with the billing service where authorized.

The agent may view:

```text
subscription
plan
billing status
invoice status
usage
payment status
```

according to permissions.

Sensitive payment credentials shall never be exposed to agents.

---

## 74. FR-049 — CRM Integration

Where configured, the agent shall be able to view authorized CRM information.

Potential integrations include:

```text
HubSpot
Salesforce
Zoho
```

CRM information shall be treated as external system data and shall not silently overwrite SalesGenie source-of-truth data.

---

## 75. FR-050 — Integration Failure Handling

If an external integration fails:

* The ticket shall remain available.
* The failure shall be visible to the agent where relevant.
* The system shall retry according to policy.
* Duplicate actions shall be prevented.
* A fallback path shall be available.
* The failure shall be logged.

SalesGenie's production-readiness requirements explicitly call for timeout, retry, backoff, circuit-breaker, fallback, idempotency and graceful degradation for critical dependencies.

---

## 76. System Security Requirements

## SSR-001 — Tenant Isolation

Every Support Agent API request shall be evaluated against tenant context.

---

## SSR-002 — RBAC

The system shall enforce the Support Agent role and granular permissions.

SalesGenie's stored role model explicitly includes `support_agent` alongside `support_manager`, `knowledge_manager`, `auditor`, and other platform roles.

---

## SSR-003 — Least Privilege

Agents shall receive only the minimum permissions necessary to perform assigned support responsibilities.

---

## SSR-004 — Authorization at API Layer

Frontend visibility shall never constitute authorization.

---

## SSR-005 — Object-Level Authorization

The backend shall verify that an agent may access:

```text
ticket
conversation
customer
attachment
knowledge document
workflow
integration
```

before returning or modifying the resource.

---

## 77. AI Security Requirements

AI tools shall be governed by:

```text
agent identity
tenant
role
permission
tool permission
workflow permission
approval policy
execution budget
```

The system shall prevent:

* Unauthorized tools
* Privilege escalation
* Cross-tenant access
* Secret access
* Infinite loops
* Repeated actions
* Unauthorized data exports
* Unauthorized deletion
* Unbounded execution
* Uncontrolled external communication

---

## 78. Observability Requirements

The Human Support Agent module shall generate:

### Logs

```text
agent_login
agent_logout
ticket_view
ticket_create
ticket_update
ticket_assign
ticket_transfer
ticket_escalate
ticket_resolve
ticket_reopen
conversation_takeover
message_send
internal_note_create
ai_suggestion
ai_tool_execution
workflow_execution
approval_request
approval_decision
```

---

## 79. Distributed Tracing

Agent actions shall be traceable across:

```text
Frontend
   ↓
API Gateway
   ↓
Auth
   ↓
Support Service
   ↓
AI Gateway
   ↓
RAG
   ↓
LLM
   ↓
Workflow Engine
   ↓
External Integration
```

Correlation IDs and trace IDs shall allow engineers to investigate a complete support action.

SalesGenie's stored observability requirements call for correlation IDs, distributed tracing across services, AI calls, MCP calls and integrations, plus audit events for security-sensitive and business-critical actions.

---

## 80. Performance Requirements

The Human Support Agent workspace shall be optimized for:

* Fast ticket loading
* Fast customer lookup
* Fast conversation rendering
* Fast message delivery
* Fast AI suggestions
* Fast knowledge retrieval
* Real-time queue updates

Long-running operations shall execute asynchronously.

---

## 81. Reliability Requirements

The system shall support:

```text
retry
backoff
circuit breaker
dead-letter queue
idempotency
graceful degradation
provider fallback
worker recovery
database recovery
message replay
```

Human support shall remain operational when an AI provider becomes unavailable.

---

## 82. Concurrency Requirements

The system shall safely support:

```text
multiple agents viewing one ticket
multiple agents collaborating
AI + human simultaneous context
customer response during agent processing
external webhook arrival during ticket update
manager reassignment during agent work
```

Race conditions shall not result in:

* Duplicate messages
* Lost messages
* Conflicting ownership
* Invalid ticket states
* Duplicate workflow execution

---

## 83. Database Requirements

Core entities shall include:

```text
SupportAgent
SupportTeam
AgentSkill
AgentAvailability
AgentCapacity

SupportTicket
TicketAssignment
TicketTransfer
TicketEscalation
TicketInternalNote
TicketTag
TicketAttachment
TicketEvent

Conversation
ConversationParticipant
ConversationMessage
ConversationEvent

Customer
CustomerIdentity
CustomerTimeline

AIInteraction
AISuggestion
AIHandoff
AIToolExecution

KnowledgeDocument
KnowledgeChunk
KnowledgeVersion

SLAPolicy
SLATimer
EscalationPolicy
RoutingRule

Notification
NotificationPreference

CustomerFeedback
AgentFeedback
QualityReview

SupportAuditEvent
```

---

## 84. API Requirements

The module shall expose versioned APIs similar to:

```text
GET    /api/v1/support/agent/me
GET    /api/v1/support/agent/dashboard

GET    /api/v1/support/tickets
POST   /api/v1/support/tickets
GET    /api/v1/support/tickets/{ticket_id}
PATCH  /api/v1/support/tickets/{ticket_id}

POST   /api/v1/support/tickets/{ticket_id}/assign
POST   /api/v1/support/tickets/{ticket_id}/transfer
POST   /api/v1/support/tickets/{ticket_id}/escalate
POST   /api/v1/support/tickets/{ticket_id}/resolve
POST   /api/v1/support/tickets/{ticket_id}/reopen

GET    /api/v1/support/tickets/{ticket_id}/messages
POST   /api/v1/support/tickets/{ticket_id}/messages

GET    /api/v1/support/tickets/{ticket_id}/notes
POST   /api/v1/support/tickets/{ticket_id}/notes

GET    /api/v1/support/conversations
GET    /api/v1/support/conversations/{conversation_id}
POST   /api/v1/support/conversations/{conversation_id}/takeover
POST   /api/v1/support/conversations/{conversation_id}/release

POST   /api/v1/support/ai/suggest
POST   /api/v1/support/ai/summarize
POST   /api/v1/support/ai/translate
POST   /api/v1/support/ai/recommend
POST   /api/v1/support/ai/similar-cases

GET    /api/v1/support/knowledge/search

GET    /api/v1/support/customers
GET    /api/v1/support/customers/{customer_id}
GET    /api/v1/support/customers/{customer_id}/timeline

GET    /api/v1/support/agent/performance
GET    /api/v1/support/agent/notifications

POST   /api/v1/support/feedback
POST   /api/v1/support/ai-feedback
```

---

## 85. Event-Driven Requirements

The module shall publish events such as:

```text
support.ticket.created
support.ticket.updated
support.ticket.assigned
support.ticket.transferred
support.ticket.escalated
support.ticket.resolved
support.ticket.reopened

support.conversation.created
support.conversation.message.created
support.conversation.human_takeover
support.conversation.human_released

support.agent.status_changed
support.agent.capacity_changed

support.ai.suggestion.generated
support.ai.suggestion.accepted
support.ai.suggestion.rejected
support.ai.handoff.created
support.ai.tool.executed

support.sla.warning
support.sla.breached

support.customer.feedback.created
support.agent.feedback.created

support.workflow.started
support.workflow.completed
support.workflow.failed
```

---

## 86. Analytics Requirements

The system shall calculate Support Agent KPIs.

## Productivity

```text
tickets_handled
tickets_resolved
messages_sent
conversations_handled
active_cases
```

## Speed

```text
average_first_response_time
median_first_response_time
average_resolution_time
median_resolution_time
```

## Quality

```text
CSAT
reopen_rate
escalation_rate
resolution_quality
QA_score
```

## SLA

```text
SLA_compliance
SLA_breach_rate
SLA_at_risk_count
```

## AI Collaboration

```text
AI_suggestion_acceptance_rate
AI_suggestion_edit_rate
AI_suggestion_rejection_rate
AI_assisted_resolution_rate
AI_handoff_rate
```

SalesGenie's stored analytics model includes AI accuracy, average response time, hallucination rate, customer satisfaction, average resolution time, AI cost and token usage, supporting the requirement for unified human/AI operational analytics.

---

## 87. Support Agent Analytics Dashboard

The agent dashboard shall provide:

```text
Today's Tickets
Open Tickets
Resolved Tickets
SLA At Risk
SLA Breached
Average Response Time
Average Resolution Time
CSAT
Escalations
AI Assistance Usage
Current Capacity
```

---

## 88. Support Manager Analytics

Managers shall be able to compare:

```text
Agent
Team
Channel
Category
Product
Priority
Customer Tier
AI vs Human
```

Metrics shall include:

```text
volume
resolution
CSAT
SLA
response time
resolution time
escalation
reopen rate
AI assistance
cost
```

---

## 89. Human vs AI Analytics

The platform shall distinguish support resolution paths:

```text
AI_ONLY
HUMAN_ONLY
AI_ASSISTED_HUMAN
AI_TO_HUMAN
HUMAN_TO_AI
AI_HUMAN_COLLABORATIVE
```

Managers shall be able to evaluate:

```text
resolution rate
resolution time
CSAT
reopen rate
escalation rate
cost per resolution
SLA compliance
```

---

## 90. AI Copilot Quality Metrics

The system shall measure:

```text
suggestion_acceptance_rate
suggestion_edit_rate
suggestion_rejection_rate
suggestion_latency
knowledge_relevance
groundedness
citation_accuracy
agent_feedback
```

---

## 91. Agent Quality Assurance

The QA system shall support:

```text
automatic sampling
manual review
AI-assisted review
scoring forms
policy checks
customer feedback correlation
coaching recommendations
```

---

## 92. Human-in-the-Loop Governance

The following actions shall be configurable as human approval actions:

```text
refund
financial adjustment
data deletion
data export
security change
account ownership change
bulk outreach
sensitive customer-data disclosure
policy override
high-impact workflow
```

SalesGenie's stored governance requirements explicitly require human approval for configured high-risk actions and logging of tool execution, decision, result, latency and approval state.

---

## 93. Auditability Requirements

Every material support operation shall be traceable to:

```text
who
what
when
where
why
under_which_policy
under_which_permission
result
```

For AI-assisted operations:

```text
AI model
prompt version
retrieval sources
tool calls
human approval
final action
```

shall be traceable where applicable.

---

## 94. Data Governance

The module shall support:

* Data retention.
* Data deletion.
* Customer data export.
* Attachment lifecycle management.
* Audit retention.
* AI interaction retention.
* Knowledge provenance.
* Permission-aware access.
* Sensitive data redaction.

The platform shall also account for AI memory, vector indexes, object storage, backups and logs when implementing deletion and retention policies.

---

## 95. Testing Requirements

The Human Support Agent module shall have:

## Unit Tests

* Ticket state transitions
* Assignment rules
* SLA calculations
* Permission checks
* AI permission checks
* Message validation

## Integration Tests

* Auth
* Support service
* AI gateway
* RAG
* CRM
* Notification
* Workflow engine
* External channels

## E2E Tests

* Login
* Ticket creation
* Ticket assignment
* Agent response
* AI takeover
* Human takeover
* Escalation
* Resolution
* Reopening
* CSAT

## Security Tests

* Cross-tenant access
* Unauthorized ticket access
* Unauthorized customer access
* Unauthorized workflow execution
* Unauthorized tool execution
* Permission escalation

## Failure Tests

* AI provider unavailable
* Database unavailable
* Redis unavailable
* Queue unavailable
* Integration unavailable
* Duplicate webhook
* Duplicate message
* Worker restart
* Network timeout

SalesGenie's production audit requirements specifically call for negative tests around permission failures, provider failures, duplicate events, timeouts, retries, partial outages and cross-tenant isolation.

---

## 96. AI Evaluation Requirements

AI copilot functionality shall be evaluated for:

```text
answer_correctness
groundedness
retrieval_precision
retrieval_recall
citation_accuracy
summarization_accuracy
intent_accuracy
recommendation_quality
hallucination_rate
unsafe_response_rate
agent_acceptance_rate
```

---

## 97. Performance SLO Requirements

The system shall establish measurable SLOs for:

```text
ticket_list_latency
ticket_open_latency
customer_search_latency
conversation_load_latency
message_send_latency
AI_suggestion_latency
knowledge_search_latency
notification_latency
```

Long-running tasks shall execute asynchronously.

SalesGenie's stored performance requirements emphasize API, database, queue, WebSocket, RAG and LLM latency, worker concurrency, queue backpressure, caching and measurable SLOs.

---

## 98. Reliability Requirements

The module shall support graceful degradation.

Examples:

### AI unavailable

```text
AI unavailable
    ↓
Human support remains operational
```

### Knowledge service unavailable

```text
Knowledge unavailable
    ↓
Agent notified
    ↓
Existing conversation remains accessible
    ↓
Human resolution continues
```

### Notification service unavailable

```text
Notification failure
    ↓
Ticket state remains authoritative
    ↓
Notification retry
```

---

## 99. Disaster Recovery

The system shall support:

* Database backup
* Point-in-time recovery where applicable
* Event replay
* Queue recovery
* Dead-letter processing
* Worker restart
* Service failover
* Configuration rollback
* Incident recovery procedures

---

## 100. Production Readiness Criteria

The Human Support Agent module shall not be considered production-ready until:

* Authentication works.
* RBAC works.
* Tenant isolation is verified.
* Ticket lifecycle is enforced.
* Agent assignment works.
* Queue management works.
* Conversations work.
* Human takeover works.
* AI copilot works.
* Knowledge retrieval works.
* Customer 360 works.
* SLA tracking works.
* Escalation works.
* Transfer works.
* Attachments work.
* Notifications work.
* Audit logs work.
* Analytics work.
* Failure handling works.
* AI provider fallback works.
* Security tests pass.
* Cross-tenant isolation tests pass.
* Duplicate event tests pass.
* Load tests pass.
* Critical APIs are documented.
* Observability is operational.
* Deployment and rollback procedures are verified.
* High-risk actions are governed by approval policies.
* No uncontrolled AI action path exists.
* No ownerless active ticket path exists.

---

## 101. End-to-End Human Support Agent Workflow

```text
                    CUSTOMER
                       │
                       ▼
              OMNICHANNEL GATEWAY
                       │
                       ▼
               IDENTITY RESOLUTION
                       │
                       ▼
               CONVERSATION SERVICE
                       │
                       ▼
                  AI TRIAGE
                       │
          ┌────────────┴─────────────┐
          │                          │
      AI RESOLVABLE              HUMAN REQUIRED
          │                          │
          │                          ▼
          │                   ROUTING ENGINE
          │                          │
          │                   ┌──────┴──────┐
          │                   │             │
          │               TEAM QUEUE     DIRECT AGENT
          │                   │             │
          │                   └──────┬──────┘
          │                          ▼
          │                  SUPPORT AGENT
          │                          │
          │              ┌───────────┼───────────┐
          │              │           │           │
          │              ▼           ▼           ▼
          │          CUSTOMER      RAG       AI COPILOT
          │          CONTEXT      SEARCH      ASSISTANCE
          │              │           │           │
          │              └───────────┼───────────┘
          │                          ▼
          │                    HUMAN DECISION
          │                          │
          │              ┌───────────┼───────────┐
          │              │           │           │
          │              ▼           ▼           ▼
          │           RESOLVE     ESCALATE    TRANSFER
          │              │           │           │
          │              └───────────┼───────────┘
          │                          ▼
          │                   CUSTOMER CONFIRM
          │                          │
          │                          ▼
          │                        CSAT
          │                          │
          │                          ▼
          │                    QA + ANALYTICS
          │                          │
          │                          ▼
          │                 CONTINUOUS IMPROVEMENT
          │
          ▼
      AI RESOLUTION
          │
          ▼
      CUSTOMER CONFIRM
          │
          ▼
         CSAT
```

---

## 102. Reference Human Support Agent State Machine

```text
NEW
 │
 ▼
OPEN
 │
 ▼
ASSIGNED
 │
 ▼
IN_PROGRESS
 │
 ├───────────────┐
 │               │
 ▼               ▼
WAITING_CUSTOMER  WAITING_INTERNAL
 │               │
 └───────┬───────┘
         ▼
     IN_PROGRESS
         │
    ┌────┴────┐
    │         │
    ▼         ▼
ESCALATED   TRANSFERRED
    │         │
    └────┬────┘
         ▼
     IN_PROGRESS
         │
         ▼
      RESOLVED
         │
    ┌────┴────┐
    │         │
    ▼         ▼
  CLOSED   REOPENED
              │
              ▼
          IN_PROGRESS
```

---

## 103. FAANG-Level Quality Bar

The Human Support Agent module shall be engineered as a production support operating system rather than a simple ticket dashboard.

The implementation shall provide:

```text
Unified agent workspace
+
Omnichannel support
+
Customer 360
+
Ticket lifecycle
+
Intelligent routing
+
SLA enforcement
+
Human escalation
+
AI copilot
+
RAG knowledge
+
Workflow execution
+
Human approval
+
Quality assurance
+
Real-time collaboration
+
Analytics
+
Auditability
+
RBAC
+
Multi-tenant isolation
+
Observability
+
Fault tolerance
+
AI governance
+
Cost control
```

The architecture shall support the broader SalesGenie platform's enterprise AI capabilities including multi-agent orchestration, RAG, memory, tool calling, human-in-the-loop approvals, semantic enterprise search, prompt evaluation, LLM routing, AI guardrails and agent-performance analytics.

---

## 104. Final Product Outcome

The completed SalesGenie Human Support Agent shall allow a support organization to operate a complete human-support lifecycle:

```text
Customer Request
        ↓
Intelligent Intake
        ↓
AI Triage
        ↓
Human Routing
        ↓
Agent Workspace
        ↓
Customer 360
        ↓
Knowledge + AI Copilot
        ↓
Human Diagnosis
        ↓
Response / Action
        ↓
SLA Monitoring
        ↓
Escalation When Required
        ↓
Resolution
        ↓
Customer Confirmation
        ↓
CSAT
        ↓
QA
        ↓
Analytics
        ↓
Knowledge Improvement
        ↓
AI Improvement
        ↓
Operational Optimization
```

The Human Support Agent is therefore not merely a user interface for replying to tickets. It shall function as a governed human-execution layer inside SalesGenie's larger AI support ecosystem, where AI provides intelligence and automation while the human agent retains operational control, customer responsibility, and authority over governed support decisions.
