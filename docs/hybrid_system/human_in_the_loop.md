# Human-in-the-Loop (HITL) Requirements

## SalesGenie — Enterprise AI Customer Support, Sales & Business Automation Platform

**Document:** `human_in_the_loop.md`  
**Version:** 1.0  
**Status:** Requirements Specification  
**Scope:** AI + Human Collaboration  
**Architecture:** Enterprise Microservices + Multi-Agent AI + RAG + Event-Driven + Human-in-the-Loop  
**Target Scale:** 10M+ users, 500K+ concurrent conversations  
**Primary Principle:** AI may recommend, draft, classify, retrieve, analyze, and execute only within explicitly authorized boundaries; humans must be able to review, approve, modify, reject, override, or take ownership of AI-driven workflows.

---

## 1. Purpose

The Human-in-the-Loop (HITL) subsystem provides a controlled collaboration layer between SalesGenie AI agents and authorized human users.

The subsystem must allow humans to:

- Review AI decisions.
- Approve or reject AI actions.
- Modify AI-generated outputs.
- Take ownership of conversations.
- Override AI decisions.
- Resolve low-confidence AI cases.
- Review sensitive operations.
- Correct AI classifications.
- Provide feedback for AI improvement.
- Escalate AI failures.
- Audit all AI-to-human interactions.
- Resume AI automation after human intervention.
- Configure approval policies.
- Control which AI actions require human approval.

The system must support HITL across:

- Sales.
- Lead generation.
- Customer support.
- Marketing.
- SEO.
- Product launch intelligence.
- Finance.
- Business intelligence.
- AI agents.
- RAG.
- Workflow automation.
- Omnichannel communication.
- Advertising.
- CRM.
- External integrations.

---

## 2. Product Objectives

## 2.1 Primary Objectives

1. Prevent unsafe or unauthorized AI actions.
2. Allow humans to intervene at any point in an AI workflow.
3. Minimize unnecessary human intervention.
4. Route uncertain decisions to appropriate users.
5. Preserve complete decision context.
6. Maintain deterministic auditability.
7. Enable human correction of AI outputs.
8. Support AI-assisted human decision making.
9. Support human-controlled AI execution.
10. Maintain business continuity when AI systems fail.

## 2.2 Secondary Objectives

- Improve AI quality using human feedback.
- Reduce support-agent workload.
- Improve sales-agent productivity.
- Reduce false-positive and false-negative decisions.
- Provide explainable AI decisions.
- Support enterprise governance.
- Support regulatory audit requirements.
- Enable configurable approval policies.

---

## 3. HITL Operating Modes

SalesGenie SHALL support the following operational modes.

## 3.1 AI-Only

AI executes automatically when:

- Confidence is above threshold.
- Action is permitted.
- Risk is low.
- No approval policy applies.
- Required data is available.

```text
REQUEST
   ↓
AI
   ↓
HIGH CONFIDENCE
   ↓
POLICY CHECK
   ↓
AUTO EXECUTION
```

## 3.2 AI-Assisted Human

AI generates recommendations while humans make the final decision.

```text
REQUEST
   ↓
AI ANALYSIS
   ↓
RECOMMENDATION
   ↓
HUMAN DECISION
   ↓
EXECUTION
```

## 3.3 Human Approval

AI prepares an action but cannot execute until approved.

```text
AI ACTION
   ↓
APPROVAL REQUIRED
   ↓
HUMAN REVIEW
   ↓
APPROVE / REJECT / MODIFY
   ↓
EXECUTION
```

## 3.4 Human Takeover

Human completely takes control of the workflow.

```text
AI
 ↓
ESCALATION
 ↓
HUMAN TAKEOVER
 ↓
HUMAN CONTROL
```

## 3.5 Human Override

Human overrides an AI decision.

```text
AI DECISION
     ↓
HUMAN OVERRIDE
     ↓
ALTERNATIVE DECISION
     ↓
EXECUTION
```

## 3.6 AI Resume

After human intervention, AI may resume under policy constraints.

---

## 4. User Roles

HITL functionality SHALL respect SalesGenie RBAC/ABAC.

Supported roles include:

* Super Admin
* Platform Admin
* Security Admin
* Billing Admin
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
* End User
* External Client

Additional custom roles SHALL be supported.

---

## 5. User Requirements

## UR-001 — Human Review

The system SHALL allow authorized users to review AI-generated decisions before execution.

## UR-002 — Approval

Users SHALL be able to approve AI-generated actions.

## UR-003 — Rejection

Users SHALL be able to reject AI-generated actions.

## UR-004 — Modification

Users SHALL be able to modify AI-generated outputs before execution.

## UR-005 — AI Override

Authorized users SHALL be able to override AI decisions.

## UR-006 — Human Takeover

Authorized human users SHALL be able to take complete ownership of an AI-managed workflow or conversation.

## UR-007 — AI Resume

Users SHALL be able to return a workflow to AI control after intervention.

## UR-008 — Escalation

Users SHALL be able to escalate AI-generated cases to appropriate teams.

## UR-009 — Review Queue

Users SHALL receive a centralized queue containing cases requiring human intervention.

## UR-010 — Prioritization

Users SHALL be able to prioritize HITL tasks by:

* Severity.
* Confidence.
* Risk.
* Customer value.
* Revenue impact.
* SLA.
* Age.
* Business priority.
* Escalation level.

## UR-011 — Assignment

Managers SHALL be able to assign HITL tasks to specific users or teams.

## UR-012 — Self-Assignment

Authorized users SHALL be able to claim available HITL tasks.

## UR-013 — AI Explanation

Users SHALL be able to inspect why an AI agent produced a decision.

## UR-014 — Evidence

Users SHALL be able to inspect supporting evidence used by AI.

## UR-015 — Confidence

Users SHALL be able to view AI confidence information where applicable.

## UR-016 — Alternatives

Users SHALL be able to view alternative AI recommendations.

## UR-017 — Human Correction

Users SHALL be able to correct AI-generated:

* Intent.
* Sentiment.
* Lead score.
* Lead qualification.
* Entity extraction.
* Classification.
* Response.
* Recommendation.
* Routing.
* Priority.
* Next action.

## UR-018 — Feedback

Users SHALL be able to submit structured feedback about AI decisions.

## UR-019 — Comments

Users SHALL be able to add comments to HITL cases.

## UR-020 — Collaboration

Multiple authorized humans SHALL be able to collaborate on the same case where policy permits.

## UR-021 — Attachments

Users SHALL be able to attach relevant documents, screenshots, evidence, and files.

## UR-022 — Internal Notes

Users SHALL be able to add private internal notes that are not exposed to customers.

## UR-023 — Customer Visibility

The system SHALL clearly distinguish customer-visible actions from internal actions.

## UR-024 — Approval History

Users SHALL be able to view the complete approval history.

## UR-025 — Decision History

Users SHALL be able to view the complete AI and human decision timeline.

## UR-026 — SLA Awareness

Users SHALL be able to see remaining SLA time for pending HITL tasks.

## UR-027 — Notifications

Users SHALL receive notifications when:

* A review is assigned.
* A review is escalated.
* An approval is required.
* An SLA is approaching.
* An SLA is breached.
* A decision is rejected.
* AI requests assistance.
* A human takes ownership.
* A workflow resumes.

## UR-028 — Bulk Review

Authorized users SHALL be able to process multiple low-risk HITL tasks when policy permits.

## UR-029 — Search

Users SHALL be able to search HITL cases.

## UR-030 — Filtering

Users SHALL be able to filter cases by:

* Status.
* Priority.
* Role.
* Team.
* AI agent.
* Workflow.
* Confidence.
* Risk.
* SLA.
* Customer.
* Organization.
* Channel.
* Date.
* Decision type.

## UR-031 — Audit

Authorized users SHALL be able to inspect HITL audit records.

## UR-032 — Privacy

Users SHALL only see HITL data permitted by tenant, role, permission, and policy.

## UR-033 — Human Escalation

Users SHALL be able to escalate cases to managers, specialists, security personnel, or other designated roles.

## UR-034 — AI Failure Recovery

Users SHALL be able to take over workflows when an AI agent fails.

## UR-035 — Integration Failure Recovery

Users SHALL be able to intervene when external integrations fail.

## UR-036 — Sensitive Action Approval

Users SHALL be able to approve sensitive operations such as:

* High-value customer communication.
* Financial actions.
* Refunds.
* Discounts.
* Campaign launches.
* Ad budget changes.
* Bulk outreach.
* Data deletion.
* Account changes.
* External system modifications.

## UR-037 — Policy Awareness

Users SHALL see why human approval was requested.

## UR-038 — Decision Consistency

The system SHALL provide enough context for humans to make consistent decisions.

## UR-039 — Accessibility

HITL interfaces SHALL be accessible according to SalesGenie's accessibility requirements.

## UR-040 — Internationalization

HITL interfaces SHALL support SalesGenie's internationalization and localization architecture.

---

## 6. System Requirements

## SR-001 — HITL Service

SalesGenie SHALL implement a dedicated HITL service or bounded domain responsible for:

* Review tasks.
* Approvals.
* Escalations.
* Human assignments.
* Human decisions.
* Overrides.
* Feedback.
* HITL state management.

## SR-002 — Event-Driven Architecture

HITL operations SHALL integrate with the event bus.

Representative events:

```text
AI_DECISION_CREATED
AI_APPROVAL_REQUIRED
HITL_TASK_CREATED
HITL_TASK_ASSIGNED
HITL_TASK_CLAIMED
HITL_TASK_STARTED
HITL_TASK_APPROVED
HITL_TASK_REJECTED
HITL_TASK_MODIFIED
HITL_TASK_ESCALATED
HITL_TASK_OVERRIDDEN
HITL_TASK_COMPLETED
HITL_TASK_EXPIRED
HUMAN_TAKEOVER_STARTED
HUMAN_TAKEOVER_COMPLETED
AI_CONTROL_RESUMED
AI_FEEDBACK_SUBMITTED
AI_DECISION_CORRECTED
```

## SR-003 — Workflow Integration

HITL SHALL integrate with the workflow engine.

A workflow action SHALL be able to specify:

```yaml
requires_human_approval: true
approval_policy: high_risk
timeout: 30m
escalation_policy: manager
```

## SR-004 — Agent Integration

AI agents SHALL be able to request human intervention.

## SR-005 — Confidence Integration

HITL routing SHALL support AI confidence scores.

## SR-006 — Risk Integration

HITL routing SHALL support risk scores.

## SR-007 — Policy Engine

The system SHALL implement configurable HITL policies.

Example:

```text
IF confidence < 0.75
THEN human_review

IF transaction_amount > threshold
THEN manager_approval

IF customer_sentiment = highly_negative
THEN human_support

IF action = data_deletion
THEN mandatory_approval
```

## SR-008 — RBAC

Every HITL operation SHALL enforce RBAC.

## SR-009 — ABAC

Sensitive HITL operations SHALL support ABAC conditions including:

* Organization.
* Workplace.
* Team.
* Resource.
* Customer.
* Risk level.
* Data classification.
* Action type.
* Environment.

## SR-010 — Tenant Isolation

HITL data SHALL remain isolated between tenants.

## SR-011 — Auditability

Every HITL state transition SHALL be auditable.

## SR-012 — Idempotency

Approval, rejection, escalation, and execution operations SHALL be idempotent.

## SR-013 — Concurrency Control

The system SHALL prevent conflicting human actions.

Example:

```text
Agent A claims task
        ↓
Agent B cannot simultaneously claim task
```

## SR-014 — Optimistic Locking

HITL records SHALL support version-based concurrency control.

## SR-015 — Transaction Integrity

Human decisions and downstream workflow transitions SHALL maintain transactional consistency.

## SR-016 — Retry

Transient failures SHALL be retried safely.

## SR-017 — Dead-Letter Handling

Failed HITL events SHALL be routed to dead-letter processing.

## SR-018 — Timeout Handling

Pending approvals SHALL support configurable timeouts.

## SR-019 — Escalation

Expired HITL tasks SHALL automatically escalate according to policy.

## SR-020 — Offline Resilience

The system SHALL preserve pending HITL work during temporary service outages.

---

## 7. HITL Domain Model

Core entities SHALL include:

```text
HITLTask
HITLRequest
AIProposal
HumanDecision
Approval
Rejection
Override
Escalation
Assignment
ReviewSession
HumanFeedback
Evidence
DecisionPolicy
ApprovalPolicy
EscalationPolicy
SLA
AuditRecord
WorkflowCheckpoint
ConversationContext
```

---

## 8. HITL Task State Machine

```text
CREATED
   ↓
QUEUED
   ↓
ASSIGNED
   ↓
CLAIMED
   ↓
IN_REVIEW
   ├── APPROVED
   ├── REJECTED
   ├── MODIFIED
   ├── OVERRIDDEN
   ├── ESCALATED
   └── EXPIRED
           ↓
       ESCALATED
           ↓
       HUMAN_REVIEW
           ↓
        RESOLVED
           ↓
      WORKFLOW_RESUME
```

---

## 9. Functional Requirements

## FR-001 — Create HITL Task

The backend SHALL create a HITL task whenever an AI workflow requires human intervention.

The task SHALL contain:

* Task ID.
* Tenant ID.
* Organization ID.
* Workplace ID.
* Workflow ID.
* Workflow execution ID.
* Agent ID.
* User/customer context.
* AI decision.
* Confidence score.
* Risk score.
* Reason for escalation.
* Required action.
* Priority.
* SLA.
* Created timestamp.
* Expiration timestamp.

---

## FR-002 — HITL Queue

The frontend SHALL provide a HITL queue.

The queue SHALL display:

* Task.
* Customer.
* AI agent.
* Decision.
* Confidence.
* Risk.
* Priority.
* SLA.
* Assignment.
* Status.
* Created time.

Backend API:

```text
GET /api/v1/hitl/tasks
```

---

## FR-003 — Task Details

Frontend SHALL provide a detailed HITL workspace.

Backend:

```text
GET /api/v1/hitl/tasks/{task_id}
```

The workspace SHALL contain:

```text
Customer Context
Conversation Context
AI Decision
AI Reasoning Summary
Confidence
Risk
Evidence
Retrieved Knowledge
Previous Actions
Recommended Action
Alternative Actions
Human Decision Controls
Audit Timeline
Comments
Internal Notes
Attachments
```

---

## 10. AI Decision Review

## FR-004 — AI Proposal

AI SHALL generate a structured proposal.

Example:

```json
{
  "decision": "send_follow_up_email",
  "confidence": 0.87,
  "risk_score": 0.21,
  "reason": "Lead demonstrated high purchase intent",
  "recommended_action": "Send personalized follow-up",
  "evidence": []
}
```

## FR-005 — Evidence Display

Frontend SHALL display evidence supporting the AI proposal.

Evidence may originate from:

* RAG.
* CRM.
* Customer history.
* Conversation history.
* Lead intelligence.
* External integrations.
* Analytics.
* Workflow context.

---

## 11. Human Approval

## FR-006 — Approve

Frontend SHALL provide an approval action.

```text
POST /api/v1/hitl/tasks/{task_id}/approve
```

Approval SHALL:

1. Validate authorization.
2. Validate task state.
3. Validate policy.
4. Record human identity.
5. Record timestamp.
6. Record optional comment.
7. Emit approval event.
8. Resume workflow.
9. Audit the operation.

---

## 12. Human Rejection

## FR-007 — Reject

```text
POST /api/v1/hitl/tasks/{task_id}/reject
```

Rejection SHALL support:

* Reason.
* Comment.
* Correction.
* Escalation.

---

## 13. Human Modification

## FR-008 — Modify AI Output

Humans SHALL be able to modify AI-generated output before execution.

Examples:

```text
AI:
"Send 20% discount"

Human:
"Send 10% discount"
```

The system SHALL preserve both versions.

---

## 14. Human Override

## FR-009 — Override AI Decision

Authorized users SHALL be able to override AI decisions.

```text
POST /api/v1/hitl/tasks/{task_id}/override
```

Override SHALL require:

* Authorized role.
* Override reason.
* New decision.
* Optional comment.

High-risk overrides SHALL require additional authorization where policy requires it.

---

## 15. Human Takeover

## FR-010 — Conversation Takeover

Human agents SHALL be able to take over AI-managed conversations.

```text
POST /api/v1/conversations/{conversation_id}/takeover
```

During takeover:

```text
AI = PAUSED
Human = ACTIVE
```

## FR-011 — AI Resume

```text
POST /api/v1/conversations/{conversation_id}/resume-ai
```

AI SHALL resume only if:

* Human permits it.
* Policy permits it.
* No unresolved escalation exists.

---

## 16. Review Assignment

## FR-012 — Assign Task

Managers SHALL be able to assign tasks.

```text
POST /api/v1/hitl/tasks/{task_id}/assign
```

Supported assignment targets:

* User.
* Team.
* Role.
* Queue.

## FR-013 — Claim Task

Users SHALL be able to claim unassigned tasks.

```text
POST /api/v1/hitl/tasks/{task_id}/claim
```

---

## 17. Escalation

## FR-014 — Manual Escalation

```text
POST /api/v1/hitl/tasks/{task_id}/escalate
```

## FR-015 — Automatic Escalation

The system SHALL automatically escalate based on:

* SLA breach.
* AI failure.
* Repeated rejection.
* High risk.
* Low confidence.
* Customer escalation.
* VIP customer.
* Revenue impact.
* Security policy.

---

## 18. AI Confidence Routing

## FR-016 — Confidence Thresholds

The system SHALL support configurable thresholds.

Example:

```text
Confidence >= 0.90
→ AI execution

0.75–0.89
→ AI + human review

0.50–0.74
→ mandatory human review

< 0.50
→ human takeover
```

Thresholds SHALL be configurable per:

* Organization.
* Agent.
* Workflow.
* Action.
* Customer segment.
* Risk level.

---

## 19. Risk-Based Routing

## FR-017 — Risk Engine Integration

The system SHALL route actions based on risk.

Example:

```text
LOW RISK
→ AI

MEDIUM RISK
→ Human approval

HIGH RISK
→ Manager approval

CRITICAL RISK
→ Security / specialized human review
```

---

## 20. Approval Policies

## FR-018 — Policy Configuration

Authorized administrators SHALL configure approval policies.

Policies SHALL support:

* Action type.
* Confidence.
* Risk.
* Monetary threshold.
* Customer segment.
* Data sensitivity.
* Channel.
* Agent.
* Workflow.
* Integration.
* Role.
* Environment.

---

## 21. Multi-Level Approval

## FR-019 — Approval Chains

The system SHALL support multi-level approvals.

Example:

```text
Sales Agent
     ↓
Sales Manager
     ↓
Organization Owner
```

or:

```text
AI
 ↓
Support Agent
 ↓
Support Manager
```

---

## 22. Parallel Approval

## FR-020 — Parallel Approvals

The system SHALL support parallel approval requirements.

Example:

```text
Finance Approval
        +
Security Approval
        ↓
Execution
```

---

## 23. Approval Delegation

## FR-021 — Delegation

Authorized users SHALL be able to delegate approval responsibilities.

Delegation SHALL support:

* Start date.
* End date.
* Scope.
* Role.
* Workflow.
* Action type.

---

## 24. Approval Expiration

## FR-022 — Approval Expiry

Approvals SHALL expire according to policy.

Expired approvals SHALL not be executed automatically unless explicitly configured.

---

## 25. Human Review Interface

## FR-023 — Review Workspace

The frontend SHALL provide:

```text
┌─────────────────────────────────────────────┐
│ HITL REVIEW                                 │
├─────────────────────────────────────────────┤
│ Customer Context                            │
│                                             │
│ AI Recommendation                           │
│ Confidence: 87%                             │
│ Risk: LOW                                   │
│                                             │
│ Evidence                                    │
│                                             │
│ Recommended Action                          │
│                                             │
│ [Approve] [Modify] [Reject] [Override]      │
│                                             │
│ Internal Notes                              │
│ Comments                                    │
│                                             │
│ Decision Timeline                           │
└─────────────────────────────────────────────┘
```

---

## 26. Conversation HITL

## FR-024 — AI/Human Chat State

Frontend SHALL clearly indicate:

```text
AI ACTIVE
HUMAN REVIEW
HUMAN ACTIVE
AI PAUSED
ESCALATED
```

## FR-025 — Takeover Indicator

Customers SHALL receive appropriate indication when a human agent takes over, subject to organization policy.

## FR-026 — Agent Context Transfer

When a human takes over, the system SHALL provide:

* Conversation summary.
* Customer profile.
* Intent.
* Sentiment.
* Previous AI actions.
* Relevant knowledge.
* Recommended response.
* Open tasks.
* Customer history.

---

## 27. AI-Generated Response Review

## FR-027 — Response Drafting

AI SHALL be able to prepare responses for human approval.

Human SHALL be able to:

* Edit.
* Regenerate.
* Shorten.
* Expand.
* Change tone.
* Translate.
* Reject.
* Send.

---

## 28. Sales HITL

## FR-028 — Lead Review

Sales users SHALL be able to review AI-generated:

* Lead scores.
* Qualification.
* Buying intent.
* Recommended actions.
* Lead routing.
* Lead assignments.

## FR-029 — Lead Correction

Human users SHALL be able to correct AI lead classifications.

---

## 29. Marketing HITL

## FR-030 — Campaign Approval

Marketing users SHALL be able to review AI-generated campaigns.

Human approval SHALL optionally be required before:

* Publishing.
* Sending emails.
* Launching ads.
* Changing budgets.
* Posting social content.

---

## 30. Advertising HITL

## FR-031 — Ad Budget Approval

High-impact advertising budget changes SHALL support human approval.

Example:

```text
AI proposes:
Increase daily budget from $500 → $2,000

Policy:
Budget increase > 100%
→ Manager approval
```

---

## 31. Finance HITL

## FR-032 — Financial Approval

Human approval SHALL be supported for:

* Refunds.
* Payments.
* Credits.
* Discounts.
* Financial adjustments.
* High-value transactions.
* Budget changes.

---

## 32. SEO HITL

## FR-033 — SEO Review

Human users SHALL review AI-generated:

* SEO strategies.
* Content.
* Keywords.
* Technical recommendations.
* Backlink recommendations.

---

## 33. Product Launch HITL

## FR-034 — Product Launch Review

Human users SHALL review AI recommendations involving:

* Market strategy.
* Competitor analysis.
* Pricing.
* Product positioning.
* GTM strategy.
* Launch risk.

---

## 34. RAG HITL

## FR-035 — Retrieval Review

Humans SHALL be able to report incorrect or irrelevant retrieval results.

Users SHALL be able to mark:

```text
Relevant
Partially Relevant
Irrelevant
Incorrect
Outdated
Conflicting
```

---

## 35. Agent HITL

## FR-036 — Agent Intervention

AI agents SHALL be able to request human assistance.

Example:

```text
Agent:
"I cannot confidently determine the customer's intent."

→ Create HITL Task
```

## FR-037 — Agent Pause

Humans SHALL be able to pause agents.

## FR-038 — Agent Resume

Humans SHALL be able to resume agents.

## FR-039 — Agent Termination

Authorized users SHALL be able to terminate unsafe or malfunctioning agents.

---

## 36. Workflow HITL

## FR-040 — Approval Node

Workflow Builder SHALL support a Human Approval node.

Example:

```text
Lead Created
    ↓
AI Qualification
    ↓
Human Approval
    ↓
CRM Update
    ↓
Email
```

## FR-041 — Human Input Node

Workflow Builder SHALL support:

```text
Human Input
```

## FR-042 — Human Review Node

Workflow Builder SHALL support:

```text
Human Review
```

## FR-043 — Human Decision Branch

Workflow conditions SHALL support:

```text
IF human_decision == approved
    → continue

ELSE
    → alternative path
```

---

## 37. Frontend Requirements

## FR-044 — HITL Dashboard

Frontend SHALL provide a dedicated HITL dashboard.

Dashboard SHALL show:

* Pending reviews.
* My tasks.
* Team tasks.
* Escalated tasks.
* SLA breaches.
* High-risk cases.
* Low-confidence cases.
* AI failures.
* Approval statistics.
* Human workload.
* AI intervention rate.

---

## 38. HITL Task Center

## FR-045 — Task Views

Frontend SHALL provide:

```text
My Tasks
Team Tasks
Unassigned
Escalated
High Priority
Expired
Completed
Rejected
Approved
```

---

## 39. Backend APIs

The backend SHALL expose versioned APIs.

Minimum API surface:

```text
GET    /api/v1/hitl/tasks
POST   /api/v1/hitl/tasks
GET    /api/v1/hitl/tasks/{id}
POST   /api/v1/hitl/tasks/{id}/claim
POST   /api/v1/hitl/tasks/{id}/assign
POST   /api/v1/hitl/tasks/{id}/approve
POST   /api/v1/hitl/tasks/{id}/reject
POST   /api/v1/hitl/tasks/{id}/modify
POST   /api/v1/hitl/tasks/{id}/override
POST   /api/v1/hitl/tasks/{id}/escalate
POST   /api/v1/hitl/tasks/{id}/complete
POST   /api/v1/hitl/tasks/{id}/cancel
GET    /api/v1/hitl/tasks/{id}/history
GET    /api/v1/hitl/tasks/{id}/evidence
POST   /api/v1/hitl/tasks/{id}/comments
POST   /api/v1/hitl/tasks/{id}/feedback

GET    /api/v1/hitl/policies
POST   /api/v1/hitl/policies
PUT    /api/v1/hitl/policies/{id}
DELETE /api/v1/hitl/policies/{id}

GET    /api/v1/hitl/queues
POST   /api/v1/hitl/queues

GET    /api/v1/hitl/metrics
GET    /api/v1/hitl/audit
```

---

## 40. Real-Time Frontend Communication

The frontend SHALL support real-time HITL updates using WebSocket or Server-Sent Events where appropriate.

Events SHALL include:

```text
task.created
task.assigned
task.claimed
task.updated
task.escalated
task.approved
task.rejected
task.expired
conversation.takeover
conversation.resume
ai.request_help
```

---

## 41. Notification Integration

HITL SHALL integrate with the notification platform.

Supported channels:

* In-app.
* Email.
* Push.
* SMS where configured.
* Slack.
* Microsoft Teams.

---

## 42. Human Feedback System

## FR-046 — Structured Feedback

Humans SHALL be able to provide:

```text
Correct
Incorrect
Partially Correct
Unsafe
Irrelevant
Incomplete
Outdated
```

## FR-047 — Feedback Metadata

Feedback SHALL capture:

* User.
* Role.
* Decision.
* AI agent.
* Model.
* Prompt version.
* Workflow.
* Timestamp.
* Original output.
* Corrected output.
* Feedback reason.

---

## 43. AI Learning Pipeline

Human feedback SHALL optionally flow into AI quality systems.

```text
HUMAN DECISION
      ↓
FEEDBACK
      ↓
DATA VALIDATION
      ↓
AI EVALUATION
      ↓
DATASET
      ↓
MODEL / PROMPT IMPROVEMENT
```

Human feedback SHALL not automatically modify production models without an approved ML governance process.

---

## 44. Audit Requirements

Every human decision SHALL record:

```text
decision_id
task_id
user_id
role
tenant_id
organization_id
action
previous_state
new_state
reason
comment
timestamp
ip_address
session_id
correlation_id
workflow_id
agent_id
model_id
prompt_version
```

---

## 45. Security Requirements

## SR-021 — Authorization

All HITL APIs SHALL enforce authorization server-side.

Frontend permissions SHALL never be treated as the security boundary.

## SR-022 — Sensitive Operations

Sensitive operations SHALL require stronger authentication or step-up authentication where configured.

## SR-023 — Privileged Override

AI overrides SHALL require appropriate privileges.

## SR-024 — Audit Integrity

Audit records SHALL be tamper-resistant.

## SR-025 — Data Protection

Sensitive customer information SHALL be protected according to SalesGenie's data-security requirements.

---

## 46. Privacy Requirements

HITL SHALL support:

* Tenant isolation.
* Data minimization.
* Data retention policies.
* Data deletion.
* Consent requirements.
* Sensitive-data masking.
* PII redaction.
* Access logging.

---

## 47. Performance Requirements

## PR-001

HITL task creation SHOULD complete within 200 ms under normal conditions.

## PR-002

HITL queue APIs SHOULD achieve p95 latency below 300 ms under normal load.

## PR-003

Real-time task updates SHOULD reach connected clients within 1 second under normal operating conditions.

## PR-004

The HITL subsystem SHALL support horizontal scaling.

## PR-005

HITL queues SHALL support large organizations with millions of tasks.

---

## 48. Reliability Requirements

## RR-001

Human approval SHALL never be lost.

## RR-002

A successful approval SHALL be durable before workflow continuation.

## RR-003

Duplicate approval requests SHALL not cause duplicate business actions.

## RR-004

HITL state SHALL survive service restart.

## RR-005

HITL tasks SHALL remain recoverable after infrastructure failures.

---

## 49. Observability

The HITL subsystem SHALL expose:

```text
hitl_tasks_created
hitl_tasks_pending
hitl_tasks_completed
hitl_tasks_escalated
hitl_tasks_expired
hitl_tasks_approved
hitl_tasks_rejected
hitl_tasks_overridden
human_takeovers
ai_resumptions
human_response_time
approval_latency
escalation_latency
sla_breach_rate
ai_intervention_rate
human_override_rate
human_correction_rate
```

Distributed traces SHALL connect:

```text
User Request
 ↓
AI Agent
 ↓
Workflow
 ↓
HITL
 ↓
Human
 ↓
External Service
```

---

## 50. HITL Analytics

The dashboard SHALL provide:

## Operational Metrics

* Open HITL tasks.
* Average resolution time.
* Median resolution time.
* SLA compliance.
* Escalation rate.
* Task backlog.

## AI Metrics

* AI intervention rate.
* AI confidence distribution.
* Human override rate.
* Human correction rate.
* AI rejection rate.
* AI approval rate.

## Human Metrics

* Tasks per agent.
* Average handling time.
* Approval rate.
* Rejection rate.
* Escalation rate.
* Workload distribution.

---

## 51. Queue Management

Queues SHALL support:

* Priority queues.
* Role queues.
* Team queues.
* Skill-based queues.
* Organization queues.
* SLA queues.
* High-risk queues.
* VIP customer queues.

---

## 52. Skill-Based Routing

The system SHALL route HITL tasks based on required expertise.

Example:

```text
Financial dispute
→ Finance Manager

Security incident
→ Security Admin

Sales opportunity
→ Sales Manager

Technical issue
→ Support Specialist

SEO issue
→ SEO Specialist
```

---

## 53. AI-Assisted Human Review

AI SHALL assist humans by providing:

* Case summaries.
* Recommended decisions.
* Suggested responses.
* Relevant documents.
* Similar historical cases.
* Risk analysis.
* Customer history.
* Recommended next actions.

Humans SHALL remain in control of configured decision points.

---

## 54. Human-Assisted AI

Humans SHALL be able to provide:

* Additional context.
* Missing information.
* Corrected intent.
* New instructions.
* Approved constraints.
* Business rules.

AI SHALL incorporate permitted human input into subsequent workflow execution.

---

## 55. Context Preservation

When a case transitions between AI and humans, the system SHALL preserve:

```text
Conversation
Customer profile
Workflow state
Agent state
Memory
RAG context
Tool calls
External API results
Previous decisions
Human decisions
Audit history
```

---

## 56. Failure Handling

If AI fails:

```text
AI Failure
   ↓
Retry
   ↓
Fallback Model
   ↓
Still Failed
   ↓
HITL Escalation
   ↓
Human Resolution
```

---

## 57. Human Timeout Handling

If a human does not respond within configured SLA:

```text
Task Created
   ↓
Reminder
   ↓
Escalation
   ↓
Manager
   ↓
Specialist / Emergency Queue
```

The system SHALL never silently discard an unresolved critical task.

---

## 58. Emergency Override

Authorized emergency operators SHALL be able to:

* Pause AI agents.
* Stop workflows.
* Disable actions.
* Freeze outbound communication.
* Disable integrations.
* Force human takeover.

All emergency actions SHALL be audited.

---

## 59. Human Approval for External Actions

Approval policies SHALL support external side effects including:

* Sending email.
* Sending SMS.
* Sending WhatsApp messages.
* Publishing social content.
* Creating CRM records.
* Updating CRM records.
* Launching advertisements.
* Changing advertising budgets.
* Creating invoices.
* Issuing refunds.
* Updating customer data.
* Deleting data.

---

## 60. Frontend Permission Model

Frontend SHALL dynamically determine available HITL controls from backend permissions.

Example:

```text
Can Approve
Can Reject
Can Modify
Can Override
Can Assign
Can Escalate
Can Takeover
Can Resume AI
Can Terminate Agent
Can View Evidence
Can View PII
```

The backend SHALL independently enforce every permission.

---

## 61. Responsive Design

HITL interfaces SHALL work across:

* Desktop.
* Laptop.
* Tablet.
* Mobile.

Critical actions SHALL remain accessible on smaller screens.

---

## 62. Accessibility

The HITL system SHALL support:

* Keyboard navigation.
* Screen readers.
* Focus management.
* Accessible dialogs.
* Accessible tables.
* Accessible alerts.
* Color-independent status indicators.
* Sufficient contrast.
* Reduced motion.
* WCAG-aligned interaction patterns.

---

## 63. Internationalization

HITL SHALL support:

* Localized UI strings.
* Localized dates.
* Localized times.
* Time zones.
* Number formats.
* Currency.
* RTL languages where applicable.

AI-generated customer responses SHALL support configured customer languages.

---

## 64. Data Model Requirements

Example:

```text
hitl_tasks
-----------
id
tenant_id
organization_id
workplace_id
workflow_id
workflow_execution_id
agent_id
conversation_id
customer_id
task_type
status
priority
confidence_score
risk_score
reason
ai_decision
recommended_action
assigned_user_id
assigned_team_id
sla_deadline
created_at
updated_at
completed_at
version
```

```text
hitl_decisions
--------------
id
task_id
decision_type
decision_value
user_id
reason
comment
created_at
```

```text
hitl_evidence
-------------
id
task_id
source_type
source_id
content_reference
relevance_score
created_at
```

```text
hitl_feedback
--------------
id
task_id
user_id
feedback_type
feedback_reason
original_output
corrected_output
created_at
```

---

## 65. API Security

HITL APIs SHALL implement:

* JWT/OAuth authentication.
* RBAC.
* ABAC.
* Rate limiting.
* Request validation.
* Idempotency keys.
* CSRF protection where applicable.
* Audit logging.
* Tenant validation.
* Resource ownership checks.

---

## 66. Event Contracts

Example:

```json
{
  "event_type": "HITL_TASK_CREATED",
  "event_id": "uuid",
  "tenant_id": "uuid",
  "task_id": "uuid",
  "workflow_id": "uuid",
  "agent_id": "uuid",
  "reason": "LOW_CONFIDENCE",
  "confidence": 0.61,
  "risk_score": 0.72,
  "timestamp": "ISO-8601"
}
```

---

## 67. Idempotency

Approval APIs SHALL support idempotency.

Example:

```http
Idempotency-Key: <unique-request-id>
```

Repeated requests SHALL return the existing decision instead of executing the action twice.

---

## 68. Human Decision Governance

Human decisions SHALL be governed by:

* Role permissions.
* Approval policies.
* Organizational policies.
* Data access policies.
* Security policies.
* Compliance policies.
* Workflow constraints.

---

## 69. AI Safety Integration

HITL SHALL integrate with:

* AI guardrails.
* Prompt injection defense.
* Data-loss prevention.
* AI safety.
* Agent governance.
* AI observability.
* Agent observability.

Potential unsafe AI outputs SHALL be routed to humans before execution where policy requires.

---

## 70. Human Review Quality Controls

The system SHALL detect:

* Repeated reviewer overrides.
* Abnormally fast approvals.
* Excessive bulk approvals.
* Suspicious approval patterns.
* Conflicting reviewer decisions.
* Repeated policy bypasses.

Security or governance teams SHALL be able to investigate anomalous human activity.

---

## 71. Approval Fraud Prevention

The system SHALL prevent:

* Self-approval where prohibited.
* Unauthorized delegation.
* Duplicate approvals.
* Approval after expiration.
* Approval of already-completed tasks.
* Cross-tenant approvals.
* Privilege escalation through HITL.

---

## 72. Workflow Checkpointing

Before requiring human intervention, the workflow engine SHALL persist a checkpoint.

Checkpoint SHALL contain:

```text
workflow state
variables
agent state
tool state
conversation state
pending action
approval policy
retry state
execution context
```

After approval, execution SHALL resume from the checkpoint.

---

## 73. Human Review Queue Prioritization

Priority calculation MAY use:

```text
Priority =
Customer Value
+ Revenue Impact
+ Risk
+ SLA Urgency
+ Confidence Uncertainty
+ Business Priority
```

The scoring algorithm SHALL be configurable.

---

## 74. Similar Case Recommendation

AI SHALL optionally retrieve similar historical HITL cases.

Humans SHALL be able to inspect:

* Previous decision.
* Outcome.
* Similarity.
* Reviewer reasoning.

---

## 75. Decision Explainability

AI recommendations SHALL provide an actionable explanation.

The system SHALL avoid exposing internal chain-of-thought.

Instead, the frontend SHALL present:

```text
Decision Summary
Key Factors
Evidence
Confidence
Risk
Policy Trigger
Recommended Action
```

---

## 76. Human Review Lifecycle

```text
AI REQUEST
   ↓
POLICY EVALUATION
   ↓
HITL TASK CREATED
   ↓
QUEUE
   ↓
ASSIGNMENT
   ↓
HUMAN REVIEW
   ↓
┌───────────┬───────────┬───────────┐
↓           ↓           ↓
APPROVE    MODIFY      REJECT
↓           ↓           ↓
EXECUTE    REVIEW      ESCALATE
            ↓
          APPROVE
            ↓
         EXECUTE
            ↓
        AUDIT
            ↓
       AI RESUME
```

---

## 77. End-to-End Example

```text
Customer sends message
        ↓
Omnichannel Gateway
        ↓
Conversation Service
        ↓
AI Support Agent
        ↓
Intent Detection
        ↓
RAG Retrieval
        ↓
AI Response Generation
        ↓
Confidence = 0.61
        ↓
Policy Engine
        ↓
HITL REQUIRED
        ↓
HITL Queue
        ↓
Support Agent
        ↓
Review Context
        ↓
Human edits response
        ↓
Approve
        ↓
Workflow resumes
        ↓
Message sent
        ↓
Conversation updated
        ↓
Audit event
        ↓
Human feedback recorded
        ↓
AI quality pipeline
```

---

## 78. Acceptance Criteria

The implementation SHALL be considered complete when:

* [ ] AI can create HITL tasks.
* [ ] Human users can view HITL tasks.
* [ ] Human users can claim tasks.
* [ ] Managers can assign tasks.
* [ ] Users can approve tasks.
* [ ] Users can reject tasks.
* [ ] Users can modify AI outputs.
* [ ] Authorized users can override AI decisions.
* [ ] Users can escalate tasks.
* [ ] AI agents can request human assistance.
* [ ] Humans can take over conversations.
* [ ] Humans can resume AI.
* [ ] Approval policies are configurable.
* [ ] Confidence-based routing works.
* [ ] Risk-based routing works.
* [ ] SLA timers work.
* [ ] Automatic escalation works.
* [ ] HITL state survives service restart.
* [ ] Duplicate approvals are prevented.
* [ ] Tenant isolation is enforced.
* [ ] RBAC is enforced.
* [ ] ABAC is enforced where required.
* [ ] Audit records are generated.
* [ ] AI evidence is displayed.
* [ ] Human feedback is recorded.
* [ ] HITL events are observable.
* [ ] HITL metrics are available.
* [ ] Real-time task updates work.
* [ ] Notifications work.
* [ ] Workflow checkpoints work.
* [ ] AI can resume after approval.
* [ ] Emergency AI takeover controls work.
* [ ] Frontend and backend permissions are synchronized.
* [ ] Accessibility requirements are met.
* [ ] Internationalization requirements are met.
* [ ] Security testing passes.
* [ ] Integration testing passes.
* [ ] E2E HITL workflows pass.
* [ ] Failure and recovery scenarios pass.

---

## 79. Definition of Done

The HITL subsystem SHALL be considered production-ready only when:

1. Every human intervention is authorization-controlled.
2. Every decision is auditable.
3. Every approval is idempotent.
4. Every critical workflow has a recoverable checkpoint.
5. No unauthorized human can execute privileged AI actions.
6. AI cannot bypass mandatory approval policies.
7. Human takeover reliably pauses AI execution.
8. AI cannot resume without satisfying resume policy.
9. SLA-based escalation is operational.
10. Human feedback is captured for AI quality evaluation.
11. HITL integrates with SalesGenie's AI agents, workflows, RAG, CRM, support, sales, marketing, finance, notification, security, and observability systems.
12. The frontend provides complete review, approval, modification, escalation, takeover, and audit workflows.
13. The backend remains the authoritative enforcement layer.
14. HITL remains operational during partial service failures.
15. All critical HITL workflows have automated unit, integration, API, E2E, security, performance, and failure-recovery tests.

---

## 80. Architectural Principle

SalesGenie's HITL system SHALL follow:

```text
                 USER / CUSTOMER
                       │
                       ▼
                AI / AGENT SYSTEM
                       │
                       ▼
               CONFIDENCE + RISK
                       │
                       ▼
                 POLICY ENGINE
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
       AI ONLY      HUMAN REVIEW   HUMAN ONLY
          │            │            │
          │            ▼            │
          │      APPROVE/MODIFY     │
          │       /REJECT/OVERRIDE  │
          │            │            │
          └────────────┼────────────┘
                       ▼
                 WORKFLOW ENGINE
                       │
                       ▼
              EXTERNAL ACTIONS
                       │
                       ▼
                OBSERVABILITY
                       │
                       ▼
                    AUDIT
                       │
                       ▼
                AI QUALITY LOOP
```

**Core rule:**

> **AI should automate low-risk, high-confidence work; humans should control uncertainty, high-impact decisions, exceptions, and safety-critical operations.**
