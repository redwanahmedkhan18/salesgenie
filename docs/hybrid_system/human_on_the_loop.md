# Human-on-the-Loop (HOTL) Requirements — SalesGenie

## 1. Document Purpose

This document defines FAANG-level User Requirements (UR), System Requirements (SR), and Functional Requirements (FR) for the **Human-on-the-Loop (HOTL)** capability of SalesGenie.

Human-on-the-Loop means that AI agents and automated workflows are permitted to operate autonomously within explicitly defined boundaries while authorized humans continuously monitor, supervise, audit, intervene, override, pause, modify, approve, or terminate AI-driven operations when required.

The system SHALL support:

- Autonomous AI execution
- Continuous human supervision
- Real-time monitoring
- Human intervention
- AI pause/resume
- Human override
- AI action cancellation
- Policy-based intervention
- Confidence-based supervision
- Risk-based supervision
- Exception handling
- Escalation
- Human approval gates
- Human takeover
- Auditability
- Explainability
- AI decision inspection
- Workflow supervision
- Multi-agent supervision
- Cross-channel supervision
- Safety controls
- Compliance controls
- Tenant isolation
- Role-based supervision
- Emergency shutdown
- Post-action review
- AI performance feedback

---

## 2. Scope

The HOTL system SHALL supervise AI activity across the complete SalesGenie platform, including:

- AI Customer Support
- AI Sales Agents
- AI Marketing Agents
- AI SEO Agents
- AI Lead Generation
- AI Lead Qualification
- AI Lead Scoring
- AI Lead Enrichment
- AI Lead Routing
- AI Outreach
- AI Email Generation
- AI Campaign Management
- AI Advertising Optimization
- AI Product Launch Intelligence
- AI Business Intelligence
- AI Financial Analysis
- AI Reporting
- AI Workflow Automation
- n8n workflows
- MCP tools
- RAG systems
- Knowledge Base operations
- Multi-agent orchestration
- LLM operations
- External integrations
- Omnichannel communication
- Customer-facing AI interactions
- Internal AI operations

---

## 3. Core HOTL Architecture

```text
                         USER / SYSTEM EVENT
                                |
                                v
                     +-----------------------+
                     | AI AGENT / WORKFLOW   |
                     +-----------+-----------+
                                 |
                                 v
                     +-----------------------+
                     | POLICY EVALUATION     |
                     +-----------+-----------+
                                 |
                 +---------------+---------------+
                 |               |               |
                 v               v               v
             LOW RISK        MEDIUM RISK      HIGH RISK
                 |               |               |
                 v               v               v
          AUTONOMOUS EXEC.   MONITORED EXEC.   HUMAN SUPERVISION
                 |               |               |
                 +---------------+---------------+
                                 |
                                 v
                     +-----------------------+
                     | HOTL CONTROL PLANE    |
                     +-----------+-----------+
                                 |
              +------------------+------------------+
              |                  |                  |
              v                  v                  v
       MONITORING          INTERVENTION       ESCALATION
              |                  |                  |
              v                  v                  v
       HUMAN DASHBOARD     PAUSE/OVERRIDE      HUMAN QUEUE
              |                  |                  |
              +------------------+------------------+
                                 |
                                 v
                     +-----------------------+
                     | EXECUTION CONTROL     |
                     +-----------+-----------+
                                 |
                                 v
                         ACTION / RESULT
                                 |
                                 v
                     +-----------------------+
                     | AUDIT + OBSERVABILITY  |
                     +-----------------------+
```

---

## 4. HOTL Operating Modes

SalesGenie SHALL support multiple supervision modes.

## 4.1 Autonomous Mode

AI operates without requiring human approval for every action.

Human users SHALL retain the ability to:

* Monitor
* Pause
* Stop
* Override
* Modify
* Disable
* Review

## 4.2 Monitored Mode

AI executes actions autonomously while a human supervisor monitors execution.

## 4.3 Supervised Mode

AI can execute predefined actions but must escalate specific conditions to a human.

## 4.4 Approval-Gated Mode

AI prepares an action but cannot execute until an authorized human approves it.

## 4.5 Human-Takeover Mode

A human assumes direct control over an AI conversation, workflow, or task.

## 4.6 Emergency-Stop Mode

AI execution is immediately suspended for the affected scope.

---

## 5. User Roles

The HOTL system SHALL support supervision according to SalesGenie's RBAC/ABAC architecture.

Potential supervisors include:

* Super Admin
* Platform Admin
* Security Admin
* Organization Owner
* Organization Admin
* Workplace Admin
* Team Manager
* Sales Manager
* Sales Agent
* Marketing Manager
* Marketing Specialist
* SEO Manager
* SEO Specialist
* Product Manager
* Finance Manager
* Business Analyst
* Support Manager
* Support Agent
* AI Agent Builder
* Developer
* External Client

Permissions SHALL determine:

* Which AI agents a user can monitor
* Which workflows a user can monitor
* Which organizations/workplaces they can access
* Which actions they can approve
* Which actions they can override
* Which agents they can pause
* Which agents they can terminate
* Which logs they can inspect
* Which policies they can modify

---

## 6. User Requirements

## UR-001 — AI Activity Visibility

Users SHALL be able to view active AI operations relevant to their permissions.

The interface SHALL display:

* Agent name
* Agent ID
* Agent type
* Agent version
* Organization
* Workplace
* Team
* Current task
* Current status
* Start time
* Execution duration
* Current workflow
* Current action
* Risk level
* Confidence level
* Model
* Token usage
* Estimated cost
* Tools being used
* External systems being accessed
* Human supervision state

---

## UR-002 — Real-Time AI Monitoring

Authorized users SHALL be able to monitor AI execution in near real time.

The monitoring interface SHALL provide:

* Live agent status
* Current action
* Current workflow node
* Tool invocation
* External API activity
* Model calls
* Errors
* Warnings
* Escalations
* Policy violations
* Confidence changes
* Risk changes

---

## UR-003 — AI Agent Supervision

Users SHALL be able to supervise individual AI agents.

Users SHALL be able to:

* Observe
* Pause
* Resume
* Stop
* Restart
* Disable
* Take over
* Escalate
* Inspect
* Review
* Override

subject to authorization.

---

## UR-004 — Workflow Supervision

Users SHALL be able to supervise AI workflows.

The interface SHALL expose:

* Workflow execution status
* Workflow graph
* Current node
* Completed nodes
* Pending nodes
* Failed nodes
* Skipped nodes
* AI decisions
* Tool calls
* Human intervention points

---

## UR-005 — AI Decision Monitoring

Users SHALL be able to inspect significant AI decisions.

Decision records SHALL include:

* Decision ID
* Agent
* Input context
* Relevant knowledge sources
* Model
* Prompt version
* Decision
* Confidence
* Risk classification
* Policy evaluation
* Selected action
* Alternative actions where available
* Human intervention status
* Final outcome

---

## UR-006 — Human Intervention

Authorized humans SHALL be able to intervene in active AI execution.

Interventions SHALL include:

* Pause
* Resume
* Cancel
* Override
* Modify
* Redirect
* Escalate
* Reassign
* Take over
* Terminate

---

## UR-007 — AI Pause

Users SHALL be able to pause an AI agent or workflow.

Pause SHALL prevent new executable actions while preserving:

* Current state
* Context
* Memory
* Workflow state
* Conversation state
* Pending tasks
* Tool state where supported

---

## UR-008 — AI Resume

Authorized users SHALL be able to resume paused execution.

The system SHALL validate:

* User authorization
* Agent state
* Workflow state
* Policy state
* Security state
* Pending action validity

before resuming.

---

## UR-009 — AI Override

Authorized humans SHALL be able to override AI decisions.

Examples:

* Reject AI-generated lead score
* Modify lead qualification
* Override routing
* Change campaign action
* Reject generated content
* Modify customer response
* Override workflow branch
* Block external communication
* Force human response

---

## UR-010 — Human Takeover

Users with appropriate permissions SHALL be able to take control of AI conversations.

The system SHALL support:

```text
AI Conversation
      |
      v
Human Takeover
      |
      v
Human Conversation
      |
      v
Human Resolution
      |
      v
AI Resume / Close
```

---

## UR-011 — Human-to-AI Handoff

After human intervention, users SHALL be able to return control to AI where permitted.

The handoff SHALL preserve relevant context.

---

## UR-012 — Escalation

Users SHALL receive escalations when:

* AI confidence is low
* Risk is high
* Policy violation is detected
* Customer requests human assistance
* AI repeatedly fails
* External API fails
* Sensitive operation is detected
* Financial operation exceeds threshold
* Security anomaly is detected
* AI enters an undefined state

---

## UR-013 — Supervision Queue

Users SHALL have a centralized supervision queue.

The queue SHALL support:

* Priority
* Risk
* Confidence
* Organization
* Agent
* Workflow
* Channel
* Customer
* Timestamp
* SLA
* Status
* Assignment

---

## UR-014 — Intervention Assignment

Supervision tasks SHALL be assignable to authorized humans.

Supported assignment modes:

* Manual assignment
* Role-based assignment
* Team assignment
* Skill-based assignment
* Round-robin
* Load-based assignment
* Priority-based assignment
* AI-recommended assignment

---

## UR-015 — AI Risk Visibility

Users SHALL be able to see AI risk classifications.

Minimum levels:

* Informational
* Low
* Medium
* High
* Critical

---

## UR-016 — Confidence Visibility

Users SHALL be able to inspect AI confidence.

Confidence SHALL be associated with:

* Classification
* Recommendation
* Generated response
* Lead score
* Intent detection
* Sentiment detection
* Tool selection
* Workflow decision

---

## UR-017 — Action Preview

For configurable high-risk operations, users SHALL be able to preview the proposed AI action before execution.

Preview SHALL include:

* Proposed action
* Target
* Parameters
* Data involved
* Expected impact
* Risk
* Confidence
* Policy evaluation
* Estimated cost

---

## UR-018 — Human Approval

Authorized users SHALL be able to approve or reject AI actions.

Actions SHALL support:

* Approve
* Reject
* Request modification
* Request additional information
* Delegate
* Escalate

---

## UR-019 — Intervention Reason

Users SHALL provide a reason for material interventions.

Reason types SHALL include:

* Incorrect decision
* Safety concern
* Compliance concern
* Customer request
* Business policy
* Security concern
* Cost concern
* Quality issue
* Strategic override
* Other

---

## UR-020 — Auditability

Users SHALL be able to inspect a complete history of AI and human interventions.

The history SHALL include:

* Actor
* Actor type
* Action
* Timestamp
* Previous state
* New state
* Reason
* Target
* Result
* Correlation ID

---

## 7. System Requirements

## SR-001 — HOTL Control Plane

SalesGenie SHALL implement a centralized HOTL control plane.

The control plane SHALL coordinate:

* AI execution state
* Human intervention
* Policy enforcement
* Approval
* Escalation
* Supervision
* Audit
* Emergency controls

---

## SR-002 — Agent State Management

The system SHALL maintain durable state for every supervised AI execution.

Minimum state:

```text
CREATED
QUEUED
RUNNING
WAITING
WAITING_FOR_HUMAN
PAUSED
ESCALATED
TAKEN_OVER
RESUMING
COMPLETED
FAILED
CANCELLED
TERMINATED
```

---

## SR-003 — Distributed Execution Control

HOTL controls SHALL work across distributed microservices.

The system SHALL support:

* Distributed workers
* Agent services
* Workflow services
* AI Gateway
* RAG services
* Integration services
* Message queues
* Event bus
* External APIs

---

## SR-004 — Event-Driven Supervision

All important AI lifecycle events SHALL be published to the event bus.

Example events:

```text
agent.created
agent.started
agent.action.started
agent.action.completed
agent.action.failed
agent.policy.warning
agent.policy.violation
agent.confidence.changed
agent.risk.changed
agent.escalated
agent.paused
agent.resumed
agent.overridden
agent.takeover.started
agent.takeover.completed
agent.terminated
human.approval.requested
human.approval.completed
```

---

## SR-005 — Idempotent Intervention

Human intervention commands SHALL be idempotent.

Repeated requests SHALL NOT cause unintended duplicate effects.

---

## SR-006 — Authorization Enforcement

Every HOTL operation SHALL pass through authorization controls.

Authorization SHALL consider:

* User identity
* Role
* Permission
* Organization
* Workplace
* Team
* Agent ownership
* Resource ownership
* Risk level
* Action type
* Tenant policy

---

## SR-007 — Tenant Isolation

HOTL data SHALL be isolated between tenants.

Users SHALL NOT be able to monitor or control resources belonging to unauthorized tenants.

---

## SR-008 — Policy Engine

The system SHALL provide policy-based supervision.

Policies SHALL support:

* Agent restrictions
* Tool restrictions
* Channel restrictions
* Data restrictions
* Financial thresholds
* Risk thresholds
* Confidence thresholds
* Approval requirements
* Time restrictions
* User restrictions
* Geographic restrictions
* Compliance restrictions

---

## SR-009 — Risk Engine

The system SHALL calculate action risk.

Risk inputs MAY include:

* Action type
* Data sensitivity
* Customer impact
* Financial impact
* External system
* Confidence
* Historical failures
* Agent reliability
* Tool sensitivity
* Policy rules

---

## SR-010 — Confidence Engine

The platform SHALL track AI confidence and support configurable thresholds.

Example:

```text
confidence >= 0.90
    -> autonomous

0.70 <= confidence < 0.90
    -> monitored

0.50 <= confidence < 0.70
    -> human review

confidence < 0.50
    -> human takeover
```

Thresholds SHALL be configurable by policy.

---

## SR-011 — Approval Engine

The approval engine SHALL manage human approval workflows.

It SHALL support:

* Single approval
* Multi-step approval
* Parallel approval
* Sequential approval
* Role-based approval
* Threshold-based approval
* Delegated approval
* Expiring approval

---

## SR-012 — Escalation Engine

The escalation engine SHALL determine:

* Whether escalation is required
* Who receives escalation
* Priority
* SLA
* Escalation deadline
* Fallback supervisor
* Escalation path

---

## SR-013 — Emergency Stop

SalesGenie SHALL support emergency AI shutdown at:

* Agent level
* Workflow level
* Organization level
* Workplace level
* Team level
* Tool level
* Model level
* Integration level
* Platform level

---

## SR-014 — Kill Switch

Authorized administrators SHALL have access to an emergency kill switch.

The kill switch SHALL:

1. Stop new AI executions.
2. Prevent new external actions.
3. Cancel or pause eligible running operations.
4. Preserve execution state.
5. Generate security/audit events.
6. Notify authorized administrators.

---

## SR-015 — Real-Time State Propagation

Intervention commands SHALL propagate to distributed services with bounded latency.

The system SHALL avoid stale execution state during intervention.

---

## SR-016 — Event Ordering

The HOTL system SHALL preserve causal ordering for state-changing events where required.

---

## SR-017 — Durable Intervention Records

Human interventions SHALL be durably stored.

Records SHALL survive:

* Service restart
* Worker restart
* Deployment
* Network failure
* Database failover

---

## SR-018 — Observability Integration

HOTL SHALL integrate with:

* Logging
* Metrics
* Distributed tracing
* AI observability
* Agent observability
* Incident alerting
* Database monitoring

---

## SR-019 — Performance

The HOTL control plane SHALL support high-frequency agent events without becoming a bottleneck.

---

## SR-020 — High Availability

HOTL control services SHALL support high availability and failover.

A control-plane failure SHALL NOT silently permit unauthorized high-risk AI actions.

---

## 8. Functional Requirements

## FR-001 — Register AI Execution

The system SHALL create a supervision record whenever an AI agent begins a significant execution.

Required fields:

```text
execution_id
agent_id
agent_version
workflow_id
organization_id
workplace_id
user_id
session_id
channel
risk_level
confidence
status
started_at
```

---

## FR-002 — Track Current AI Action

The system SHALL continuously track the current AI action.

---

## FR-003 — Track Agent Lifecycle

The system SHALL track all agent lifecycle transitions.

---

## FR-004 — Display Active Agents

Frontend SHALL provide an active-agent monitoring dashboard.

Example:

```text
Active AI Agents
------------------------------------------------
Agent       Task             Risk      Status
------------------------------------------------
Sales AI    Lead scoring     Low       Running
Support AI  Customer chat    Medium    Running
Marketing   Campaign draft   Medium    Waiting
Finance AI  Forecast         High      Review
------------------------------------------------
```

---

## FR-005 — Agent Detail View

Users SHALL be able to open an agent detail page containing:

* Agent identity
* Current task
* Workflow
* Execution timeline
* Decisions
* Tool calls
* Model calls
* Risk
* Confidence
* Cost
* Errors
* Interventions
* Audit trail

---

## FR-006 — Pause Agent

Frontend SHALL expose a pause control where permitted.

Backend SHALL:

1. Validate authorization.
2. Validate current state.
3. Create intervention command.
4. Publish intervention event.
5. Update execution state.
6. Confirm state transition.
7. Record audit event.

---

## FR-007 — Resume Agent

Frontend SHALL allow authorized users to resume paused agents.

---

## FR-008 — Cancel Execution

Users SHALL be able to cancel eligible executions.

Cancellation SHALL be propagated to workers.

---

## FR-009 — Terminate Agent

Authorized administrators SHALL be able to terminate an AI agent.

Termination SHALL require appropriate permission and SHALL generate an immutable audit record.

---

## FR-010 — Override Decision

Users SHALL be able to override AI decisions.

The system SHALL preserve:

```text
AI decision
Human decision
Difference
Human reason
Timestamp
Actor
Final outcome
```

---

## FR-011 — Modify AI Action

Users SHALL be able to modify supported AI actions before execution.

---

## FR-012 — Approve AI Action

The frontend SHALL expose approval controls for approval-gated operations.

---

## FR-013 — Reject AI Action

Users SHALL be able to reject proposed AI actions.

---

## FR-014 — Request Revision

Users SHALL be able to request that AI revise a proposed action.

---

## FR-015 — Human Takeover

The system SHALL support human takeover of supported AI conversations.

Takeover SHALL:

* Lock AI response generation where required
* Assign conversation to human
* Preserve context
* Preserve customer history
* Preserve AI reasoning metadata according to privacy policy
* Record takeover event

---

## FR-016 — Resume AI After Takeover

After human resolution, authorized users SHALL be able to return the conversation to AI.

---

## FR-017 — Supervision Queue

The frontend SHALL provide a supervision queue.

Each item SHALL display:

* Priority
* Risk
* Confidence
* Agent
* Customer
* Organization
* Task
* SLA
* Created time
* Assigned supervisor
* Status

---

## FR-018 — Queue Filtering

Users SHALL filter supervision tasks by:

* Priority
* Risk
* Confidence
* Agent
* Workflow
* Organization
* Workplace
* Team
* Channel
* Status
* Date
* SLA

---

## FR-019 — Queue Sorting

Users SHALL sort by:

* Risk
* Priority
* SLA
* Age
* Confidence
* Customer value
* Financial impact

---

## FR-020 — Queue Assignment

Users SHALL assign supervision tasks to humans or teams.

---

## FR-021 — Automatic Assignment

The system SHALL support automatic assignment according to configured policies.

---

## FR-022 — Escalation

The system SHALL automatically escalate unresolved supervision items.

---

## FR-023 — SLA Tracking

Each escalation SHALL support:

* Response SLA
* Resolution SLA
* Escalation deadline
* Breach detection

---

## FR-024 — Notification

HOTL events SHALL generate appropriate notifications.

Supported channels:

* In-app
* Email
* Push
* SMS where configured
* Slack
* Microsoft Teams

---

## FR-025 — Notification Preferences

Users SHALL configure:

* Event types
* Severity
* Notification channels
* Quiet hours
* Escalation preferences

---

## 9. AI Decision Supervision

## FR-026 — Decision Timeline

The system SHALL display an execution timeline.

Example:

```text
10:01:02 Agent started
10:01:03 Retrieved customer context
10:01:04 Called CRM
10:01:05 Generated recommendation
10:01:05 Risk increased to HIGH
10:01:06 Human approval requested
10:01:21 Human approved
10:01:22 Action executed
10:01:24 Result received
```

---

## FR-027 — Decision Context

Users SHALL be able to inspect the context used for significant AI decisions, subject to data-access policies.

---

## FR-028 — Tool Invocation Inspection

Users SHALL be able to inspect:

* Tool name
* Tool version
* Input parameters
* Output
* Execution duration
* Status
* Error
* Authorization result

Sensitive secrets SHALL NEVER be exposed.

---

## FR-029 — Model Inspection

The system SHALL expose:

* Model provider
* Model name
* Model version where available
* Prompt version
* Temperature/configuration where applicable
* Token usage
* Latency
* Cost
* Safety result

---

## FR-030 — RAG Inspection

For RAG-enabled decisions, users SHALL be able to inspect:

* Knowledge base
* Documents
* Retrieval results
* Retrieval score
* Ranking
* Citation metadata
* Knowledge version

Sensitive documents SHALL be masked or inaccessible according to permissions.

---

## 10. Human Intervention Controls

## FR-031 — Pause Workflow

Users SHALL be able to pause a workflow.

---

## FR-032 — Resume Workflow

Users SHALL be able to resume a workflow.

---

## FR-033 — Skip Workflow Node

Authorized users SHALL be able to skip supported workflow nodes.

---

## FR-034 — Retry Workflow Node

Users SHALL be able to retry failed nodes.

---

## FR-035 — Re-run AI Decision

Users SHALL be able to request a new AI decision when supported.

---

## FR-036 — Change Workflow Path

Authorized users SHALL be able to redirect execution to an approved workflow branch.

---

## FR-037 — Disable Tool

Authorized administrators SHALL be able to disable an AI tool.

---

## FR-038 — Block Integration

Administrators SHALL be able to block AI access to an external integration.

---

## FR-039 — Change Model

Authorized users SHALL be able to switch supported AI model configurations where policy permits.

---

## FR-040 — Force Human Response

A supervisor SHALL be able to force an AI conversation into human-only mode.

---

## 11. Risk-Based Human-on-the-Loop

## FR-041 — Risk Classification

The system SHALL classify AI actions based on configured risk policies.

---

## FR-042 — Low-Risk Autonomous Execution

Low-risk actions MAY execute autonomously.

---

## FR-043 — Medium-Risk Monitoring

Medium-risk actions SHALL generate enhanced monitoring events.

---

## FR-044 — High-Risk Supervision

High-risk actions SHALL require human supervision or approval according to policy.

---

## FR-045 — Critical-Risk Blocking

Critical-risk actions SHALL be blocked or require explicit authorized human approval.

---

## 12. High-Risk Action Categories

The system SHALL support configurable high-risk policies for:

* Financial transactions
* Refunds
* Subscription changes
* Billing operations
* Mass outbound messaging
* Customer deletion
* Data deletion
* Permission changes
* Role changes
* Security configuration
* API key creation
* Credential changes
* External system modifications
* Advertising budget changes
* Campaign activation
* High-volume lead outreach
* Sensitive customer communications
* Compliance-sensitive actions

---

## 13. Human Approval Workflow

## FR-046 — Approval Request

AI SHALL create approval requests for actions requiring human authorization.

---

## FR-047 — Approval Expiration

Approval requests SHALL support expiration.

---

## FR-048 — Approval Delegation

Authorized supervisors SHALL be able to delegate approval responsibilities.

---

## FR-049 — Approval History

The system SHALL preserve complete approval history.

---

## FR-050 — Multi-Level Approval

The system SHALL support approval chains.

Example:

```text
AI Agent
   |
   v
Sales Manager
   |
   v
Organization Owner
   |
   v
Execution
```

---

## 14. Human Feedback

## FR-051 — Intervention Feedback

Users SHALL be able to provide feedback after intervention.

---

## FR-052 — Feedback Categories

Feedback SHALL support:

* Correct
* Incorrect
* Unsafe
* Irrelevant
* Incomplete
* Hallucination
* Wrong tool
* Wrong customer
* Wrong classification
* Wrong recommendation
* Policy violation
* Other

---

## FR-053 — AI Learning Dataset

Where explicitly enabled, validated human feedback MAY be exported into AI evaluation or improvement pipelines.

Human feedback SHALL NOT automatically modify production model behavior.

---

## 15. Frontend Requirements

## FR-054 — HOTL Dashboard

Frontend SHALL provide a dedicated HOTL dashboard.

Dashboard components SHALL include:

* Active agents
* Running workflows
* Human review queue
* Escalations
* High-risk actions
* Paused agents
* Failed agents
* Pending approvals
* Intervention metrics
* SLA status

---

## FR-055 — Real-Time Updates

Frontend SHALL receive real-time state updates using appropriate mechanisms such as:

* WebSockets
* Server-Sent Events
* Event streaming
* Efficient polling fallback

---

## FR-056 — Agent Status Indicator

The UI SHALL clearly distinguish:

* Running
* Monitoring
* Waiting
* Waiting for human
* Paused
* Escalated
* Taken over
* Failed
* Completed
* Terminated

---

## FR-057 — Intervention Confirmation

Destructive operations SHALL require confirmation.

Examples:

```text
Terminate Agent?
Pause Workflow?
Cancel Execution?
Disable Tool?
Block Integration?
```

---

## FR-058 — Optimistic UI Restrictions

High-risk state transitions SHALL NOT rely solely on optimistic frontend updates.

The frontend SHALL wait for authoritative backend confirmation.

---

## FR-059 — Permission-Aware UI

Controls SHALL be dynamically displayed or disabled according to backend-provided authorization.

Frontend permissions SHALL NOT replace backend authorization.

---

## FR-060 — Error Handling

Frontend SHALL clearly communicate:

* Permission denied
* Intervention failed
* Agent already stopped
* Agent state changed
* Conflict
* Timeout
* Service unavailable
* Approval expired
* Execution completed before intervention

---

## 16. Backend API Requirements

## FR-061 — Agent Monitoring API

Example:

```http
GET /api/v1/ai/agents/active
GET /api/v1/ai/agents/{agent_id}
GET /api/v1/ai/agents/{agent_id}/executions
```

---

## FR-062 — Intervention API

Example:

```http
POST /api/v1/hotl/interventions
POST /api/v1/hotl/agents/{agent_id}/pause
POST /api/v1/hotl/agents/{agent_id}/resume
POST /api/v1/hotl/agents/{agent_id}/cancel
POST /api/v1/hotl/agents/{agent_id}/terminate
```

---

## FR-063 — Workflow Control API

Example:

```http
POST /api/v1/hotl/workflows/{workflow_id}/pause
POST /api/v1/hotl/workflows/{workflow_id}/resume
POST /api/v1/hotl/workflows/{workflow_id}/cancel
POST /api/v1/hotl/workflows/{workflow_id}/retry
POST /api/v1/hotl/workflows/{workflow_id}/redirect
```

---

## FR-064 — Approval API

Example:

```http
GET  /api/v1/hotl/approvals
GET  /api/v1/hotl/approvals/{approval_id}
POST /api/v1/hotl/approvals/{approval_id}/approve
POST /api/v1/hotl/approvals/{approval_id}/reject
POST /api/v1/hotl/approvals/{approval_id}/delegate
```

---

## FR-065 — Supervision Queue API

Example:

```http
GET /api/v1/hotl/supervision-queue
POST /api/v1/hotl/supervision-queue/{item_id}/assign
POST /api/v1/hotl/supervision-queue/{item_id}/escalate
POST /api/v1/hotl/supervision-queue/{item_id}/resolve
```

---

## FR-066 — Audit API

Example:

```http
GET /api/v1/hotl/audit
GET /api/v1/hotl/executions/{execution_id}/audit
```

---

## 17. WebSocket / Event Requirements

The frontend SHALL receive events such as:

```text
HOTL_AGENT_STARTED
HOTL_AGENT_PAUSED
HOTL_AGENT_RESUMED
HOTL_AGENT_ESCALATED
HOTL_AGENT_TERMINATED
HOTL_ACTION_STARTED
HOTL_ACTION_COMPLETED
HOTL_ACTION_FAILED
HOTL_APPROVAL_REQUIRED
HOTL_APPROVAL_COMPLETED
HOTL_HUMAN_TAKEOVER
HOTL_HUMAN_RELEASE
HOTL_POLICY_VIOLATION
HOTL_RISK_CHANGED
HOTL_CONFIDENCE_CHANGED
HOTL_EMERGENCY_STOP
```

---

## 18. Database Requirements

The HOTL subsystem SHALL maintain durable records for:

## AgentExecution

```text
execution_id
agent_id
agent_version
workflow_id
organization_id
workplace_id
team_id
session_id
status
risk_level
confidence
started_at
completed_at
created_at
updated_at
```

## AgentAction

```text
action_id
execution_id
action_type
tool_id
status
risk_level
confidence
input_reference
output_reference
started_at
completed_at
```

## HumanIntervention

```text
intervention_id
execution_id
action_id
actor_id
intervention_type
reason
previous_state
new_state
created_at
```

## ApprovalRequest

```text
approval_id
execution_id
action_id
requested_by
assigned_to
risk_level
status
expires_at
approved_at
rejected_at
```

## Escalation

```text
escalation_id
execution_id
priority
reason
assigned_to
sla_deadline
status
created_at
resolved_at
```

---

## 19. Security Requirements

## SR-021 — Strong Authentication

Sensitive HOTL actions SHALL require authenticated users.

---

## SR-022 — Step-Up Authentication

High-risk operations MAY require MFA or step-up authentication.

---

## SR-023 — Least Privilege

HOTL permissions SHALL follow least-privilege principles.

---

## SR-024 — Secret Protection

The system SHALL never expose:

* API keys
* OAuth refresh tokens
* Passwords
* Service credentials
* Encryption keys
* Access tokens

through monitoring interfaces.

---

## SR-025 — Audit Integrity

Material HOTL events SHALL be tamper-resistant and auditable.

---

## SR-026 — Session Security

Expired or revoked sessions SHALL immediately lose HOTL control permissions.

---

## 20. AI Safety Requirements

## SR-027 — AI Cannot Bypass Human Controls

AI agents SHALL NOT be able to bypass HOTL policies.

---

## SR-028 — Policy Enforcement Outside the Agent

Critical policies SHALL be enforced outside the LLM/agent itself.

---

## SR-029 — Tool Authorization

Every sensitive tool invocation SHALL be authorization-controlled.

---

## SR-030 — Human Override Priority

Where policy permits human override, an authorized human decision SHALL take precedence over an AI recommendation.

---

## SR-031 — Prompt Injection Resistance

Human supervision controls SHALL remain effective even when AI encounters:

* Prompt injection
* Malicious documents
* Malicious webpages
* Adversarial user input
* Tool-output injection

---

## 21. AI + Human Conversation Supervision

The system SHALL support:

```text
Customer
   |
   v
AI Support Agent
   |
   +---- High confidence ----> AI responds
   |
   +---- Medium confidence --> Monitor
   |
   +---- Low confidence -----> Human review
   |
   +---- Explicit request ---> Human takeover
```

---

## 22. Sales AI HOTL

Human supervisors SHALL be able to monitor:

* Lead discovery
* Lead scoring
* Lead qualification
* Lead enrichment
* Lead assignment
* Outreach generation
* Email generation
* Sales sequences
* CRM updates
* Deal recommendations
* Sales forecasting

High-risk actions such as mass outreach SHALL support configurable approval thresholds.

---

## 23. Marketing AI HOTL

Human supervisors SHALL be able to monitor:

* Campaign creation
* Content generation
* Audience selection
* Email campaigns
* Social media content
* Ad optimization
* Budget recommendations
* Campaign activation

Campaign publication and significant budget modifications SHALL support configurable approval gates.

---

## 24. Support AI HOTL

Human supervisors SHALL monitor:

* Customer conversations
* Sentiment
* Intent
* AI responses
* Escalations
* Customer complaints
* Refund requests
* Sensitive issues

Users SHALL be able to take over conversations instantly.

---

## 25. Finance AI HOTL

Financial AI operations SHALL support enhanced supervision.

Examples:

* Revenue analysis
* Expense analysis
* Profitability analysis
* Forecasting
* Budget recommendations
* Financial anomaly detection

Financial actions affecting external systems SHALL require explicit authorization according to policy.

---

## 26. Advertising AI HOTL

The system SHALL support supervision of:

* Campaign creation
* Campaign activation
* Campaign pausing
* Budget changes
* Bid changes
* Audience changes
* Creative selection
* Optimization recommendations

Budget thresholds SHALL be configurable.

---

## 27. Product Launch AI HOTL

Humans SHALL be able to supervise:

* Market analysis
* Competitor analysis
* Positioning
* GTM recommendations
* Launch forecasts
* Risk analysis
* Strategic recommendations

AI SHALL NOT autonomously commit strategic business decisions without configured authorization.

---

## 28. Workflow Automation HOTL

The workflow engine SHALL support human intervention nodes.

Example:

```text
Trigger
  |
  v
AI Research
  |
  v
AI Analysis
  |
  v
Risk Evaluation
  |
  +---- Low Risk ----> Execute
  |
  +---- High Risk ---> Human Approval
                         |
                    +----+----+
                    |         |
                 Approve     Reject
                    |         |
                    v         v
                 Execute      Stop
```

---

## 29. MCP HOTL

MCP tools SHALL support supervision controls.

For sensitive MCP tools:

```text
Agent
  |
  v
MCP Tool Request
  |
  v
Policy Engine
  |
  +---- Allowed ------> Execute
  |
  +---- Review -------> Human Approval
  |
  +---- Block --------> Deny
```

The system SHALL record:

* MCP server
* Tool
* Parameters
* Authorization
* Risk
* Human approval
* Result

---

## 30. RAG HOTL

Human supervisors SHALL be able to review high-impact RAG decisions.

The system SHALL support:

* Retrieval inspection
* Citation inspection
* Source validation
* Knowledge-base version inspection
* Incorrect-source reporting
* Retrieval override where supported

---

## 31. Emergency Operations

## FR-067 — Emergency Stop

Authorized administrators SHALL be able to execute emergency stop.

---

## FR-068 — Scope Selection

Emergency stop SHALL support:

```text
Single Agent
Single Workflow
Single Tool
Single Integration
Workplace
Organization
Platform
```

---

## FR-069 — Emergency Broadcast

Emergency stop events SHALL be propagated to all relevant services.

---

## FR-070 — Emergency Audit

Every emergency operation SHALL create a high-severity immutable audit record.

---

## 32. Failure Handling

If human supervision infrastructure becomes unavailable:

* High-risk actions SHALL fail closed.
* Approval-gated actions SHALL NOT execute.
* Low-risk actions MAY continue according to policy.
* Running operations SHALL enter a safe state where possible.
* Administrators SHALL be notified.

---

## 33. Conflict Handling

The system SHALL handle concurrent human interventions.

Example:

```text
Supervisor A -> Pause
Supervisor B -> Terminate
Agent         -> Completed
```

The backend SHALL use authoritative state validation and idempotent commands to determine the final valid state.

---

## 34. Observability Requirements

HOTL SHALL expose metrics including:

### Operational Metrics

* Active supervised agents
* Active workflows
* Paused agents
* Human takeover count
* Intervention count
* Escalation count
* Approval count
* Rejection count
* Cancellation count
* Termination count

### AI Metrics

* Average confidence
* Low-confidence decisions
* High-risk actions
* AI failure rate
* Human override rate
* AI-to-human escalation rate
* Human-to-AI return rate

### Human Metrics

* Queue depth
* Average response time
* Average resolution time
* SLA breach rate
* Supervisor workload
* Assignment distribution

---

## 35. Audit Requirements

Every significant HOTL action SHALL generate an audit event.

Minimum event:

```json
{
  "event_id": "uuid",
  "event_type": "agent.paused",
  "actor_type": "human",
  "actor_id": "uuid",
  "organization_id": "uuid",
  "resource_id": "uuid",
  "previous_state": "RUNNING",
  "new_state": "PAUSED",
  "reason": "Safety review",
  "timestamp": "ISO-8601",
  "correlation_id": "uuid",
  "trace_id": "uuid"
}
```

---

## 36. API Authorization Matrix

| Action            | Sales Agent | Manager | Org Admin | Security Admin | Super Admin |
| ----------------- | ----------: | ------: | --------: | -------------: | ----------: |
| View Own AI       |         Yes |     Yes |       Yes |            Yes |         Yes |
| View Team AI      |          No |     Yes |       Yes |            Yes |         Yes |
| Pause Agent       |     Limited |     Yes |       Yes |            Yes |         Yes |
| Resume Agent      |     Limited |     Yes |       Yes |            Yes |         Yes |
| Override Decision |     Limited |     Yes |       Yes |            Yes |         Yes |
| Human Takeover    |         Yes |     Yes |       Yes |            Yes |         Yes |
| Terminate Agent   |          No | Limited |       Yes |            Yes |         Yes |
| Emergency Stop    |          No |      No |   Limited |            Yes |         Yes |
| Change Policy     |          No |      No |   Limited |            Yes |         Yes |

Actual authorization SHALL be enforced by the backend RBAC/ABAC system.

---

## 37. Frontend-to-Backend Integration

The HOTL frontend SHALL connect to backend services for:

```text
Authentication
Authorization
Agent Monitoring
Agent Execution
Workflow Monitoring
Workflow Control
Human Intervention
Approvals
Escalations
Notifications
Audit Logs
Risk Engine
Confidence Engine
Policy Engine
Agent Management
AI Gateway
LLM Gateway
MCP
RAG
CRM
Support
Marketing
Advertising
Billing
Analytics
Observability
```

No security-sensitive operation SHALL be implemented exclusively on the frontend.

---

## 38. State Synchronization

Frontend state SHALL be synchronized with backend authoritative state.

Example:

```text
Frontend
   |
   | Pause Agent
   v
API Gateway
   |
   v
HOTL Control Plane
   |
   v
Authorization
   |
   v
Execution Controller
   |
   v
Agent Worker
   |
   v
Event Bus
   |
   v
WebSocket/SSE
   |
   v
Frontend
```

---

## 39. Concurrency Requirements

The system SHALL prevent:

* Double approval
* Double termination
* Conflicting takeover
* Duplicate intervention
* Race-condition-based execution
* Unauthorized resume
* Stale-state actions

The backend SHALL implement:

* Optimistic locking
* Version checks
* Idempotency keys
* Transactional state transitions
* Event correlation

where appropriate.

---

## 40. Data Privacy

HOTL monitoring SHALL follow privacy policies.

The system SHALL support:

* PII masking
* Sensitive-data redaction
* Field-level access control
* Tenant isolation
* Data retention policies
* Data deletion
* Audit access controls

---

## 41. Compliance

The HOTL subsystem SHALL support configurable compliance requirements for:

* GDPR
* CCPA
* Enterprise security policies
* Audit requirements
* Data retention
* Access reviews
* Human authorization
* Sensitive-action controls

---

## 42. Performance Requirements

The HOTL control plane SHALL be designed for SalesGenie's target architecture of:

* 10M+ users
* 500K+ concurrent conversations
* Large-scale AI agent execution
* Distributed workflows
* High-volume event streams

Monitoring infrastructure SHALL scale independently from AI execution workloads.

---

## 43. Reliability Requirements

HOTL SHALL provide:

* High availability
* Durable state
* Event replay
* Idempotent commands
* Failover
* Backpressure
* Safe degradation
* Disaster recovery
* Audit preservation

---

## 44. Disaster Recovery

HOTL state SHALL be included in disaster recovery planning.

Recovery SHALL preserve, where applicable:

* Active executions
* Pending approvals
* Human interventions
* Escalations
* Audit records
* Agent states
* Workflow states
* Policies

---

## 45. Testing Requirements

The HOTL system SHALL be tested using:

## Unit Testing

* State transitions
* Authorization
* Policy evaluation
* Risk calculation
* Confidence thresholds
* Escalation logic
* Approval logic

## Integration Testing

* Agent ↔ HOTL
* Workflow ↔ HOTL
* HOTL ↔ Event Bus
* HOTL ↔ Database
* HOTL ↔ Notification service
* HOTL ↔ WebSocket
* HOTL ↔ Authorization service

## E2E Testing

Test complete flows:

```text
AI Execution
    -> Risk Detection
    -> Human Escalation
    -> Queue Assignment
    -> Human Approval
    -> AI Resume
    -> Execution
    -> Audit
```

## Chaos Testing

Test:

* Control-plane failure
* Event bus failure
* Database failure
* Worker failure
* Network partition
* WebSocket failure
* Duplicate commands
* Concurrent intervention

---

## 46. Security Testing

The HOTL system SHALL be tested against:

* Privilege escalation
* Broken access control
* Tenant isolation failure
* IDOR
* Session hijacking
* CSRF
* API abuse
* Race conditions
* Command replay
* Prompt injection
* Tool abuse
* MCP abuse
* Audit tampering

---

## 47. Acceptance Criteria

The implementation SHALL be considered production-ready when:

* Authorized humans can monitor AI agents in real time.
* Unauthorized humans cannot control protected agents.
* AI actions can be paused according to policy.
* AI actions can be resumed safely.
* Human takeover works for supported conversations.
* High-risk operations can require approval.
* Human decisions override AI decisions where policy permits.
* Escalations reach authorized supervisors.
* Approval workflows are durable.
* Intervention events are auditable.
* Tenant isolation is enforced.
* Emergency stop functions correctly.
* Frontend state reflects backend-authoritative state.
* Concurrent intervention conflicts are handled safely.
* HOTL continues functioning during individual service failures.
* Sensitive information is protected.
* All significant interventions are traceable.
* AI cannot bypass human authorization controls.

---

## 48. End-to-End Reference Workflow

```text
CUSTOMER / BUSINESS EVENT
          |
          v
     AI AGENT
          |
          v
   AI REASONING / TASK
          |
          v
   RISK + CONFIDENCE
          |
          v
   POLICY EVALUATION
          |
     +----+----+
     |         |
     v         v
LOW RISK    HIGH RISK
     |         |
     v         v
AUTONOMOUS   HUMAN QUEUE
     |         |
     |         v
     |    SUPERVISOR
     |         |
     |    +----+----+
     |    |         |
     |    v         v
     | APPROVE    REJECT
     |    |         |
     |    v         v
     | EXECUTE     STOP
     |    |
     +----+
          |
          v
       RESULT
          |
          v
  OBSERVABILITY
          |
          v
       AUDIT LOG
          |
          v
   AI PERFORMANCE
      ANALYTICS
          |
          v
 HUMAN FEEDBACK / REVIEW
```

---

## 49. Golden Rule

> **AI may operate autonomously, but humans must retain authoritative visibility, intervention, override, escalation, and emergency-control capabilities over AI operations within their authorized scope.**

The HOTL architecture SHALL ensure that human supervision is a **control-plane capability**, not merely a frontend feature.

The backend SHALL remain the authoritative source of:

* Authorization
* Agent state
* Workflow state
* Intervention state
* Approval state
* Risk state
* Policy enforcement
* Execution control
* Audit history

The frontend SHALL provide the human supervisory interface, while the backend SHALL enforce the actual control boundaries.
