# SalesGenie — Lead Assignment

## FAANG-Level User Requirements, System Requirements & Functional Requirements

**Module:** `lead_assignment.md`
**Platform:** SalesGenie Enterprise AI Sales & Revenue Intelligence Platform
**Processing Modes:** AI-Based + Human-Assisted
**Architecture:** Multi-Tenant, Event-Driven, Microservices, AI-Agentic
**Requirement Level:** Enterprise / FAANG-Level
**Version:** 1.0

---

## 1. Module Overview

The Lead Assignment module is responsible for converting a routing decision into a controlled, traceable, and actionable ownership relationship between a lead and its assigned destination.

The module shall support assignment to:

* Individual sales agents
* SDRs
* BDRs
* Account executives
* Sales managers
* Sales teams
* Queues
* Territories
* AI sales agents
* AI workflows
* Human-AI hybrid teams

The module shall support:

* AI-based assignment
* Human-based assignment
* Hybrid assignment
* Automatic assignment
* Manual assignment
* Manager-approved assignment
* Conditional assignment
* Temporary assignment
* Permanent ownership
* Shared assignment
* Primary/secondary ownership
* Assignment acceptance
* Assignment rejection
* Assignment transfer
* Assignment reassignment
* Assignment escalation
* Assignment expiration
* Assignment recovery
* Assignment history
* Assignment audit
* Assignment analytics
* Assignment optimization

---

## 2. Business Objectives

The Lead Assignment module shall:

1. Establish a single source of truth for lead ownership.
2. Ensure every actionable lead has an accountable destination.
3. Prevent duplicate or conflicting ownership.
4. Minimize assignment latency.
5. Ensure high-value leads reach the appropriate sales personnel.
6. Support both AI and human sales operations.
7. Provide controlled human override of AI decisions.
8. Preserve complete assignment history.
9. Enforce organizational ownership boundaries.
10. Automatically recover from rejected, expired, or failed assignments.
11. Maintain SLA accountability.
12. Provide transparent assignment decisions.
13. Measure assignment effectiveness.
14. Optimize assignment using historical outcomes.
15. Connect assignment outcomes to pipeline and revenue performance.

---

## 3. Assignment Lifecycle

```text
Lead Created
    ↓
Lead Qualified
    ↓
Routing Decision
    ↓
Assignment Candidate Identified
    ↓
Eligibility Validation
    ↓
Capacity Validation
    ↓
Availability Validation
    ↓
AI Recommendation / Human Selection
    ↓
Assignment Created
    ↓
Notification
    ↓
Acceptance
    ↓
Work Started
    ↓
Outcome
    ↓
Conversion / Rejection / Reassignment
    ↓
Revenue Attribution
```

Alternative failure path:

```text
Assignment Created
       ↓
No Acceptance
       ↓
SLA Breach
       ↓
Escalation
       ↓
Reassignment
       ↓
New Assignment
```

---

## 4. User Roles

| Role               | Assignment Responsibilities                  |
| ------------------ | -------------------------------------------- |
| Super Admin        | Platform-wide assignment governance          |
| Organization Admin | Organization assignment policies             |
| Workplace Admin    | Workplace assignment configuration           |
| Sales Manager      | Assign, transfer, and reassign leads         |
| RevOps Manager     | Assignment policy and performance management |
| Sales Agent        | Accept, reject, and manage assigned leads    |
| SDR/BDR            | Handle assigned prospects                    |
| Account Executive  | Manage assigned opportunities                |
| AI Sales Agent     | Handle eligible automated assignments        |
| AI Routing Agent   | Recommend assignment destinations            |
| Support Agent      | Handle leads requiring support               |
| Data Analyst       | Analyze assignment performance               |
| End User/Client    | Access authorized assignment information     |

---

## 5. User Requirements

## UR-001 — Automatic Assignment

Users shall be able to configure SalesGenie to automatically assign leads after routing.

## UR-002 — Manual Assignment

Authorized users shall be able to manually assign a lead to an eligible destination.

## UR-003 — AI Assignment

The system shall use AI to recommend the most suitable assignee.

## UR-004 — Human-Assisted Assignment

Users shall be able to review AI recommendations before assignment.

## UR-005 — Hybrid Assignment

The system shall support:

```text
Business Rules
+
AI Recommendation
+
Human Approval
=
Final Assignment
```

## UR-006 — Primary Owner

Every actionable lead shall have a primary owner when organizational policy requires ownership.

## UR-007 — Secondary Owner

Users shall be able to assign secondary participants when supported by the organization.

## UR-008 — Team Assignment

Users shall be able to assign leads to teams.

## UR-009 — Queue Assignment

Users shall be able to assign leads to queues when direct assignment is unavailable.

## UR-010 — AI Agent Assignment

Users shall be able to assign eligible leads to AI sales agents.

## UR-011 — Human Agent Assignment

Users shall be able to assign leads to human sales representatives.

## UR-012 — Manager Assignment

Managers shall be able to assign leads to themselves or authorized team members.

## UR-013 — Skill-Based Assignment

The system shall support assignment according to agent skills.

## UR-014 — Territory-Based Assignment

The system shall respect configured geographic ownership.

## UR-015 — Account Ownership

Existing account ownership shall be considered before assigning related leads.

## UR-016 — Product Expertise

Users shall be able to assign leads according to product expertise.

## UR-017 — Industry Expertise

Users shall be able to assign leads according to industry expertise.

## UR-018 — Language Matching

The system shall support assignment according to required language.

## UR-019 — Lead Score

Assignment decisions shall be able to use lead scores.

## UR-020 — Intent

Assignment decisions shall be able to use purchase intent.

## UR-021 — Revenue Potential

Assignment decisions shall be able to consider estimated revenue.

## UR-022 — Priority

Users shall be able to mark leads with assignment priorities.

## UR-023 — VIP Assignment

VIP leads shall be assignable using dedicated policies.

## UR-024 — SLA Assignment

The system shall assign leads according to configured response-time requirements.

## UR-025 — Capacity Awareness

The system shall consider current assignee workload.

## UR-026 — Availability Awareness

The system shall consider agent availability.

## UR-027 — Assignment Acceptance

Agents shall be able to accept assignments when acceptance is required.

## UR-028 — Assignment Rejection

Agents shall be able to reject assignments when organizational policy permits.

## UR-029 — Rejection Reason

Users shall be able to provide a reason for rejecting an assignment.

## UR-030 — Reassignment

Authorized users shall be able to reassign leads.

## UR-031 — Transfer

Authorized users shall be able to transfer ownership.

## UR-032 — Automatic Reassignment

The system shall automatically reassign leads when configured conditions occur.

## UR-033 — Escalation

The system shall escalate assignments that breach configured SLAs.

## UR-034 — Temporary Assignment

The system shall support temporary ownership.

## UR-035 — Assignment Expiration

Organizations shall be able to configure assignment expiration.

## UR-036 — Assignment Explanation

Users shall be able to understand why an assignee was selected.

## UR-037 — Human Override

Authorized users shall be able to override AI recommendations.

## UR-038 — Assignment History

Users with appropriate permissions shall be able to view assignment history.

## UR-039 — Assignment Search

Authorized users shall be able to search assignments.

## UR-040 — Assignment Filtering

Users shall be able to filter assignments by:

* Agent
* Team
* Status
* Date
* Territory
* Priority
* Lead score
* Assignment source
* AI/human origin
* SLA state

## UR-041 — Assignment Dashboard

Managers shall have visibility into assignment status.

## UR-042 — Bulk Assignment

Authorized users shall be able to assign multiple leads in bulk.

## UR-043 — Bulk Reassignment

Authorized users shall be able to reassign multiple leads.

## UR-044 — Assignment Simulation

Users shall be able to preview the expected assignee before executing assignment.

## UR-045 — Assignment Audit

Users with appropriate permissions shall be able to inspect assignment actions.

---

## 6. AI-Based User Requirements

## AI-UR-001 — Intelligent Assignee Prediction

AI shall identify the assignee most likely to produce the desired business outcome.

## AI-UR-002 — Lead-Agent Compatibility

AI shall calculate compatibility between lead characteristics and assignee capabilities.

## AI-UR-003 — Conversion Prediction

AI shall estimate conversion probability for candidate assignees.

## AI-UR-004 — Revenue Prediction

AI shall estimate expected revenue associated with candidate assignments.

## AI-UR-005 — Response Prediction

AI shall estimate expected response time.

## AI-UR-006 — Workload Prediction

AI shall consider current and projected workload.

## AI-UR-007 — Skill Matching

AI shall match lead requirements against assignee skills.

## AI-UR-008 — Contextual Matching

AI shall consider relevant lead context including:

* Industry
* Company size
* Product interest
* Geography
* Language
* Lead source
* Campaign
* Intent
* Engagement
* Previous conversations
* Existing account relationships

## AI-UR-009 — Historical Performance

AI shall consider historical assignment outcomes where permitted.

## AI-UR-010 — Dynamic Assignment

AI shall update recommendations when lead or assignee conditions change.

## AI-UR-011 — Confidence Scoring

AI assignment recommendations shall expose confidence information.

## AI-UR-012 — Explainability

AI shall provide human-readable assignment reasons.

## AI-UR-013 — Alternative Assignees

AI shall be able to provide alternative eligible assignees.

## AI-UR-014 — Assignment Optimization

AI shall identify assignment patterns associated with improved business outcomes.

## AI-UR-015 — Assignment Anomaly Detection

AI shall detect unusual assignment behavior.

## AI-UR-016 — Assignment Drift Detection

AI shall identify when historical assignment policies become ineffective.

## AI-UR-017 — AI Learning

AI shall learn from accepted, rejected, transferred, converted, and won assignments where appropriate.

## AI-UR-018 — AI Safety

AI shall never assign a lead outside the user's authorized tenant, organization, workplace, or ownership boundary.

---

## 7. Human-Based User Requirements

## HUMAN-UR-001 — Direct Assignment

Authorized humans shall be able to directly assign leads.

## HUMAN-UR-002 — Assignment Override

Authorized humans shall be able to override AI assignment recommendations.

## HUMAN-UR-003 — Manual Reassignment

Managers shall be able to reassign leads.

## HUMAN-UR-004 — Assignment Approval

Organizations shall be able to require human approval for selected assignment categories.

## HUMAN-UR-005 — Assignment Exceptions

Users shall be able to define exceptions to automated assignment.

## HUMAN-UR-006 — Ownership Protection

Managers shall be able to protect strategic account ownership.

## HUMAN-UR-007 — Assignment Freeze

Authorized administrators shall be able to temporarily prevent automatic reassignment.

## HUMAN-UR-008 — Emergency Reassignment

Administrators shall be able to perform emergency reassignment during:

* Employee departure
* Agent outage
* Territory changes
* Organizational restructuring
* System incidents
* Campaign surges

## HUMAN-UR-009 — Assignment Review

Managers shall be able to review AI-generated assignments.

## HUMAN-UR-010 — Assignment Governance

Human administrators shall be able to define mandatory constraints that AI cannot override.

---

## 8. System Requirements

## SR-001 — Multi-Tenant Assignment

Assignment data shall be strictly isolated by tenant.

## SR-002 — Organization Isolation

Assignment ownership shall respect organization boundaries.

## SR-003 — Workplace Isolation

Workplace-level assignment policies shall be enforced.

## SR-004 — RBAC

Assignment operations shall integrate with SalesGenie's centralized authorization system.

## SR-005 — Fine-Grained Permissions

The system shall support permissions such as:

```text
lead.assignment.view
lead.assignment.create
lead.assignment.update
lead.assignment.delete
lead.assignment.transfer
lead.assignment.reassign
lead.assignment.override
lead.assignment.approve
lead.assignment.bulk
lead.assignment.audit
```

## SR-006 — Assignment State Management

The system shall maintain a canonical assignment state.

```text
UNASSIGNED
PENDING
RECOMMENDED
AWAITING_APPROVAL
ASSIGNED
ACCEPTED
REJECTED
IN_PROGRESS
TRANSFERRED
REASSIGNED
ESCALATED
EXPIRED
COMPLETED
FAILED
CANCELLED
```

## SR-007 — Assignment Ownership

The system shall maintain a canonical active owner.

## SR-008 — Assignment History

All ownership changes shall be persisted.

## SR-009 — Assignment Versioning

Assignment policies shall be versioned.

## SR-010 — Policy Association

Each assignment shall reference the policy or decision process responsible for the assignment.

## SR-011 — AI Model Association

AI-generated assignments shall reference the model version used.

## SR-012 — Assignment Source

The system shall distinguish:

```text
AI
HUMAN
RULE
HYBRID
IMPORT
API
WORKFLOW
SYSTEM
```

## SR-013 — Idempotency

Repeated assignment requests shall not create duplicate active assignments.

## SR-014 — Concurrency Protection

Concurrent assignment operations shall be protected against race conditions.

## SR-015 — Assignment Lock

The system shall support assignment locking when required.

## SR-016 — Ownership Consistency

The system shall prevent inconsistent ownership across integrated services.

## SR-017 — Assignment Validation

The system shall validate assignee eligibility before creating an assignment.

## SR-018 — Capacity Validation

The system shall validate assignee capacity.

## SR-019 — Availability Validation

The system shall validate assignee availability.

## SR-020 — Permission Validation

The system shall validate that the actor is authorized to perform the requested assignment.

## SR-021 — Assignment Notification

The system shall notify assignees when appropriate.

## SR-022 — SLA Tracking

The system shall track assignment-related SLAs.

## SR-023 — Escalation Engine

The system shall support configurable escalation rules.

## SR-024 — Reassignment Engine

The system shall support automatic reassignment.

## SR-025 — Queue Integration

The assignment service shall integrate with lead queues.

## SR-026 — Workflow Integration

Assignments shall trigger configurable workflows.

## SR-027 — CRM Integration

Assignment ownership shall synchronize with supported CRM systems.

## SR-028 — Event Integration

The system shall publish assignment events.

## SR-029 — Audit Integration

All consequential assignment operations shall generate audit events.

## SR-030 — Analytics Integration

Assignment events shall be available to analytics services.

---

## 9. Functional Requirements

## FR-001 — Create Assignment

The system shall create a lead assignment containing:

```text
Assignment ID
Lead ID
Tenant ID
Organization ID
Workplace ID
Assignee ID
Assignee Type
Assignment Source
Assignment Policy
Policy Version
AI Model Version
Confidence
Reason
Priority
SLA
Created By
Created At
Status
```

## FR-002 — Validate Assignment

Before creating an assignment, the system shall validate:

```text
Lead Exists
Assignee Exists
Assignee Is Active
Assignee Is Eligible
User Has Permission
Tenant Matches
Organization Matches
Workplace Matches
Capacity Available
Availability Valid
Ownership Rules Valid
```

## FR-003 — Automatic Assignment

The system shall automatically create assignments following an approved routing decision.

## FR-004 — Manual Assignment

Authorized users shall be able to select an assignee and create an assignment.

## FR-005 — AI Recommendation

The AI engine shall rank eligible assignees.

Example:

```text
Candidate A → 92%
Candidate B → 84%
Candidate C → 76%
```

## FR-006 — AI Assignment

Organizations shall be able to configure AI assignment as:

```text
RECOMMEND_ONLY
REQUIRE_APPROVAL
AUTO_ASSIGN
AUTO_ASSIGN_WITH_EXCEPTION_REVIEW
```

## FR-007 — Human Approval

Assignments requiring approval shall enter an approval queue.

## FR-008 — Approve Assignment

Authorized reviewers shall be able to approve AI recommendations.

## FR-009 — Reject Assignment

Authorized reviewers shall be able to reject AI recommendations.

## FR-010 — Modify Recommendation

Authorized reviewers shall be able to select an alternative assignee.

## FR-011 — Assignment Acceptance

Agents shall be able to accept assignments when acceptance is enabled.

## FR-012 — Assignment Rejection

Agents shall be able to reject assignments when permitted.

## FR-013 — Rejection Reason

The system shall record rejection reasons.

Example:

```text
Wrong Territory
Wrong Product
Insufficient Capacity
Conflict of Interest
Existing Account Owner
Unavailable
Incorrect Assignment
Other
```

## FR-014 — Transfer Assignment

Authorized users shall be able to transfer an assignment.

## FR-015 — Reassignment

Authorized users shall be able to replace the current assignee.

## FR-016 — Automatic Reassignment

The system shall automatically reassign leads after configurable triggers.

Possible triggers:

```text
SLA Breach
Agent Unavailable
Agent Deactivated
Assignment Rejected
Assignment Expired
Territory Changed
Account Ownership Changed
Capacity Exceeded
```

## FR-017 — Temporary Assignment

The system shall support temporary assignment with expiration.

## FR-018 — Assignment Expiration

Expired assignments shall transition into the configured fallback workflow.

## FR-019 — Escalation

The system shall escalate unresolved assignments according to policy.

## FR-020 — Assignment Queue

The system shall support unassigned and pending assignment queues.

## FR-021 — Queue Prioritization

Queues shall support prioritization based on:

* Lead score
* Intent
* Revenue
* Priority
* SLA
* Lead age
* VIP status

## FR-022 — Assignment Lock

The system shall prevent unauthorized changes to protected assignments.

## FR-023 — Ownership Protection

Protected strategic-account assignments shall require elevated permissions to modify.

## FR-024 — Bulk Assignment

Authorized users shall be able to assign multiple leads.

## FR-025 — Bulk Reassignment

Authorized users shall be able to reassign multiple leads.

## FR-026 — Bulk Validation

Bulk assignment shall validate every lead independently.

Invalid records shall not silently overwrite valid records.

## FR-027 — Assignment Simulation

Users shall be able to preview:

```text
Lead
Candidate Assignee
Assignment Strategy
Expected Result
Policy
Confidence
Potential Conflicts
```

## FR-028 — Historical Replay

The system shall support replaying historical leads against assignment policies.

## FR-029 — What-If Assignment

Users shall be able to compare alternative assignment strategies.

## FR-030 — Conflict Detection

The system shall detect:

```text
Invalid Assignee
Inactive Assignee
Duplicate Ownership
Protected Ownership
Capacity Overflow
Territory Conflict
Permission Conflict
Tenant Conflict
Organization Conflict
Workplace Conflict
Policy Conflict
```

## FR-031 — Assignment Explanation

For AI-assisted assignments, the system shall return:

```text
Recommended Assignee
Confidence
Primary Factors
Supporting Signals
Alternative Assignees
Expected Conversion
Expected Revenue
Policy Applied
Model Version
```

## FR-032 — Assignment Notification

The system shall notify the assignee through configured communication channels.

## FR-033 — Assignment Reminder

The system shall send reminders for assignments approaching SLA limits.

## FR-034 — SLA Breach

The system shall detect assignment SLA breaches.

## FR-035 — Escalation Notification

The system shall notify managers when configured escalation thresholds are reached.

## FR-036 — Assignment History

The system shall provide chronological assignment history.

Example:

```text
10:00 — AI recommended Agent A
10:01 — Manager approved
10:01 — Agent A assigned
10:15 — Agent A rejected
10:16 — System reassigned to Agent B
10:20 — Agent B accepted
```

## FR-037 — Assignment Audit

The system shall record:

```text
Actor
Action
Previous Owner
New Owner
Reason
Timestamp
IP / Session Context
Policy Version
AI Model Version
```

## FR-038 — Assignment Search

Users shall be able to search assignments using supported filters.

## FR-039 — Assignment Dashboard

The dashboard shall provide:

```text
Total Assigned
Unassigned
Pending
Accepted
Rejected
Reassigned
Escalated
Expired
Completed
Failed
```

## FR-040 — Agent Workload

Managers shall be able to view current assignment workload.

## FR-041 — Agent Assignment Performance

The system shall calculate:

```text
Assignment Count
Acceptance Rate
Rejection Rate
Response Time
Conversion Rate
Opportunity Rate
Win Rate
Revenue
SLA Compliance
```

## FR-042 — AI Assignment Performance

The system shall measure:

```text
AI Recommendation Accuracy
AI Acceptance Rate
AI Override Rate
AI Reassignment Rate
AI Conversion Lift
AI Revenue Lift
```

## FR-043 — Human Assignment Performance

The system shall measure human assignment outcomes.

## FR-044 — AI vs Human Comparison

Managers shall be able to compare:

```text
AI Assignment
vs
Human Assignment
vs
Rule-Based Assignment
```

using business outcomes.

## FR-045 — Assignment Optimization

AI shall identify opportunities to improve assignment policies.

Example:

```text
Current:
Enterprise healthcare leads → Round Robin

Recommendation:
Assign healthcare enterprise leads to specialized Agent Group A.

Expected Impact:
+13% conversion
-18% response time
+9% expected revenue
```

## FR-046 — Assignment Experiments

The platform shall support controlled experiments between assignment strategies.

## FR-047 — Assignment Attribution

The platform shall connect assignment outcomes with:

* Opportunities
* Deals
* Revenue
* Conversion
* Customer acquisition

## FR-048 — Ownership Synchronization

The system shall synchronize ownership changes with integrated CRM systems.

## FR-049 — Failure Recovery

Failed assignment operations shall be retried according to configured policies.

## FR-050 — Dead-Letter Handling

Repeatedly failed assignment events shall enter a dead-letter mechanism for investigation.

## FR-051 — Reconciliation

The system shall periodically detect discrepancies between SalesGenie ownership and integrated systems.

## FR-052 — Assignment Repair

Authorized administrators shall be able to repair inconsistent assignment states.

---

## 10. AI Assignment Decision Architecture

```text
Lead
  ↓
Lead Context Extraction
  ↓
Eligibility Filtering
  ↓
Assignee Candidate Generation
  ↓
Hard Constraint Validation
  ↓
Skill Matching
  ↓
Territory Matching
  ↓
Product Matching
  ↓
Industry Matching
  ↓
Availability Evaluation
  ↓
Capacity Evaluation
  ↓
Historical Performance
  ↓
Conversion Prediction
  ↓
Revenue Prediction
  ↓
Response-Time Prediction
  ↓
AI Ranking
  ↓
Confidence Evaluation
  ↓
Business Policy Validation
  ↓
Human Approval / Automatic Assignment
  ↓
Assignment
```

---

## 11. AI Assignment Scoring Model

The conceptual assignment score may combine:

```text
Assignment Score =
    Lead-Agent Fit
  + Skill Match
  + Industry Match
  + Product Match
  + Territory Match
  + Language Match
  + Account Compatibility
  + Historical Conversion
  + Expected Revenue
  + Availability
  + Capacity
  + Response Performance
  + SLA Compatibility
```

Hard constraints shall be evaluated separately from optimization factors.

```text
Hard Constraint Failure
        ↓
Candidate Eliminated

Hard Constraints Passed
        ↓
AI Optimization
```

AI optimization shall never override mandatory authorization or ownership constraints.

---

## 12. Human-in-the-Loop Assignment

```text
Lead
 ↓
AI Assignment Recommendation
 ↓
Confidence Evaluation
 ↓
 ┌───────────────────────────┐
 │ High Confidence           │
 │                           │
 │ Automatic Assignment      │
 └───────────────────────────┘

 ┌───────────────────────────┐
 │ Medium Confidence         │
 │                           │
 │ Human Approval            │
 └───────────────────────────┘

 ┌───────────────────────────┐
 │ Low Confidence            │
 │                           │
 │ Manual Assignment         │
 └───────────────────────────┘
```

Human reviewers shall be able to:

```text
Approve
Reject
Modify
Reassign
Defer
Escalate
```

---

## 13. Assignment Data Model

## Lead Assignment

```text
LeadAssignment
├── id
├── tenant_id
├── organization_id
├── workplace_id
├── lead_id
├── assignee_id
├── assignee_type
├── assignment_source
├── assignment_strategy
├── routing_policy_id
├── routing_policy_version
├── ai_model_id
├── ai_model_version
├── confidence_score
├── assignment_score
├── reason
├── priority
├── sla_deadline
├── status
├── assigned_by
├── assigned_at
├── accepted_at
├── rejected_at
├── transferred_at
├── completed_at
├── created_at
└── updated_at
```

## Assignment History

```text
AssignmentHistory
├── id
├── assignment_id
├── lead_id
├── previous_assignee_id
├── new_assignee_id
├── action
├── actor_id
├── actor_type
├── reason
├── policy_version
├── model_version
├── timestamp
└── metadata
```

## Assignee Profile

```text
AssigneeProfile
├── assignee_id
├── role
├── team_id
├── skills
├── industries
├── products
├── languages
├── territories
├── availability
├── capacity
├── current_load
├── performance_score
├── conversion_rate
├── response_time
└── assignment_eligibility
```

---

## 14. API Requirements

The module should expose APIs conceptually equivalent to:

```http
POST   /api/v1/leads/{lead_id}/assignment
GET    /api/v1/leads/{lead_id}/assignment
PATCH  /api/v1/leads/{lead_id}/assignment
DELETE /api/v1/leads/{lead_id}/assignment

POST   /api/v1/leads/{lead_id}/assignment/accept
POST   /api/v1/leads/{lead_id}/assignment/reject
POST   /api/v1/leads/{lead_id}/assignment/transfer
POST   /api/v1/leads/{lead_id}/assignment/reassign
POST   /api/v1/leads/{lead_id}/assignment/escalate

POST   /api/v1/assignments
GET    /api/v1/assignments
GET    /api/v1/assignments/{assignment_id}

POST   /api/v1/assignments/bulk
POST   /api/v1/assignments/bulk/reassign

POST   /api/v1/assignments/simulate
POST   /api/v1/assignments/replay
POST   /api/v1/assignments/validate

POST   /api/v1/assignments/ai/recommend
POST   /api/v1/assignments/ai/explain
POST   /api/v1/assignments/ai/optimize

GET    /api/v1/assignments/queues
GET    /api/v1/assignments/analytics
GET    /api/v1/assignments/performance
GET    /api/v1/assignments/history
GET    /api/v1/assignments/audit
```

---

## 15. Event Requirements

The assignment service shall publish and consume events such as:

```text
LeadCreated
LeadQualified
LeadScored
LeadRouted

AssignmentRequested
AssignmentValidationStarted
AssignmentValidationCompleted

AIRoutingRecommendationCreated
AIAssignmentRecommendationCreated

AssignmentCreated
AssignmentApproved
AssignmentRejected

AssignmentAccepted
AssignmentDeclined
AssignmentExpired

AssignmentTransferred
AssignmentReassigned
AssignmentEscalated

AssignmentCompleted
AssignmentFailed
AssignmentCancelled

AssignmentSLABreached

AgentAvailabilityChanged
AgentCapacityChanged

AccountOwnershipChanged
TerritoryChanged

AssignmentOptimizationRecommended
AssignmentExperimentStarted
AssignmentExperimentCompleted
```

---

## 16. SalesGenie Workflow Integration

```text
Lead Discovery
      ↓
Lead Enrichment
      ↓
Lead Qualification
      ↓
Lead Segmentation
      ↓
Lead Scoring
      ↓
Lead Routing
      ↓
Lead Assignment
      ↓
Sales Sequence
      ↓
Outreach Automation
      ↓
Opportunity Management
      ↓
Deal Management
      ↓
Sales Forecasting
      ↓
Sales Analytics
      ↓
Revenue Attribution
```

---

## 17. AI Agent Integration

The Lead Assignment module shall integrate with SalesGenie's multi-agent architecture.

Potential agents:

```text
Lead Intelligence Agent
Lead Qualification Agent
Lead Segmentation Agent
Lead Routing Agent
Lead Assignment Agent
Sales Research Agent
Personalization Agent
Outreach Agent
Follow-Up Agent
Sales Assistant Agent
Revenue Intelligence Agent
Human Escalation Agent
```

The AI Assignment Agent shall:

1. Receive eligible assignment requests.
2. Validate available candidates.
3. Apply hard constraints.
4. Rank eligible candidates.
5. Produce confidence.
6. Produce explanation.
7. Request human approval when required.
8. Create an assignment only when authorized.
9. Monitor assignment outcomes.
10. Learn from permitted outcome data.

---

## 18. Security Requirements

The system shall enforce:

* Authentication
* RBAC
* Fine-grained authorization
* Tenant isolation
* Organization isolation
* Workplace isolation
* Ownership protection
* API authorization
* Encryption in transit
* Encryption at rest
* Audit logging
* Rate limiting
* Input validation
* Output validation
* Secure secret management
* Data-loss prevention
* AI prompt-injection protection
* Cross-tenant access prevention
* Assignment tamper protection

AI agents shall operate under equivalent authorization constraints to human actors.

---

## 19. AI Safety and Governance

The AI assignment system shall:

1. Never assign outside the tenant boundary.
2. Never bypass RBAC.
3. Never bypass account ownership protection.
4. Never override mandatory business constraints.
5. Never use unauthorized sensitive attributes for assignment.
6. Detect suspicious assignment patterns.
7. Support human override.
8. Preserve model version information.
9. Preserve policy version information.
10. Provide assignment explanations.
11. Provide confidence thresholds.
12. Support deterministic fallback.
13. Validate AI-generated assignment parameters.
14. Protect against prompt injection through lead content.
15. Record consequential AI assignment decisions.
16. Support assignment fairness monitoring where appropriate.

---

## 20. Performance Requirements

Target production objectives:

```text
Simple assignment:
P95 < 250 ms

Complex assignment:
P95 < 750 ms

AI-assisted assignment:
P95 < 3 seconds

Human approval recommendation:
P95 < 2 seconds

Assignment notification:
Target < 5 seconds

Bulk assignment:
Horizontally scalable
```

Performance targets shall be configurable by deployment and service tier.

---

## 21. Scalability Requirements

The platform shall be architected to support:

```text
10M+ leads
Millions of active assignments
Millions of assignment-history records
Thousands of organizations
Large sales teams
High-volume inbound campaigns
Concurrent assignment requests
Large bulk assignment operations
High-frequency agent availability changes
```

Assignment workers shall support horizontal scaling.

---

## 22. Reliability Requirements

The assignment service shall support:

* Idempotency
* Transactional assignment
* Distributed locking where required
* Retry policies
* Dead-letter queues
* Circuit breakers
* Timeouts
* Assignment reconciliation
* Failure recovery
* Queue persistence
* Graceful degradation
* Automatic fallback

---

## 23. Graceful Degradation

The assignment hierarchy should support:

```text
AI Assignment
      ↓ failure
Hybrid Assignment
      ↓ failure
Rule-Based Assignment
      ↓ failure
Queue Assignment
      ↓ failure
Manual Assignment
```

The system shall prioritize reliable ownership establishment over advanced AI optimization.

---

## 24. Observability Requirements

The system shall monitor:

```text
Assignment latency
Assignment throughput
Assignment success rate
Assignment failure rate
Assignment rejection rate
Assignment reassignment rate
Assignment transfer rate
Assignment SLA breach rate
AI assignment latency
AI confidence
AI override rate
Queue depth
Agent workload
Agent availability
Conversion rate
Revenue per assignment
```

Each assignment transaction shall include a correlation ID for distributed tracing.

---

## 25. Assignment Analytics

## Operational Metrics

```text
Total Assignment Requests
Successful Assignments
Failed Assignments
Pending Assignments
Unassigned Leads
Assignment Latency
```

## Agent Metrics

```text
Assignments Received
Assignments Accepted
Assignments Rejected
Response Time
Conversion Rate
Win Rate
Revenue
SLA Compliance
```

## AI Metrics

```text
AI Recommendations
AI Acceptance Rate
AI Override Rate
AI Reassignment Rate
AI Confidence
AI Conversion Lift
AI Revenue Lift
```

## Business Metrics

```text
Qualified Leads
Opportunities
Deals
Win Rate
Revenue
Average Deal Value
Revenue per Assignment
```

---

## 26. Assignment Optimization

The AI optimization engine shall evaluate:

```text
Historical Assignments
+
Lead Characteristics
+
Agent Characteristics
+
Agent Performance
+
Response Times
+
Capacity
+
Availability
+
Conversion Outcomes
+
Revenue Outcomes
+
SLA Performance
```

and identify assignment opportunities.

Example:

```text
Current Assignment:
Enterprise SaaS leads → General Sales Pool

AI Recommendation:
Enterprise SaaS leads → Enterprise Specialists

Expected Impact:
+12% conversion
-15% response time
+10% expected revenue
```

Recommendations shall require appropriate approval before modifying production assignment behavior.

---

## 27. Assignment Experimentation

The platform shall support controlled experiments.

Example:

```text
Control:
Manager-Based Assignment

Experiment:
AI-Based Assignment
```

The system shall measure:

* Assignment latency
* Acceptance rate
* Response time
* Conversion
* Opportunity creation
* Win rate
* Revenue
* SLA compliance

Experiments shall support configurable traffic allocation and isolation.

---

## 28. Assignment Conflict Detection

The system shall detect:

```text
Duplicate active owner
Invalid assignee
Inactive assignee
Protected account ownership
Capacity overflow
Territory conflict
Organization conflict
Workplace conflict
Tenant conflict
Permission conflict
Circular transfer
Expired assignment
Invalid AI recommendation
Conflicting assignment policy
```

The system shall prevent unsafe assignment activation or route the case to human review.

---

## 29. Assignment Lifecycle

```text
UNASSIGNED
    ↓
PENDING
    ↓
RECOMMENDED
    ↓
AWAITING_APPROVAL
    ↓
ASSIGNED
    ↓
ACCEPTED
    ↓
IN_PROGRESS
    ↓
COMPLETED
```

Alternative paths:

```text
ASSIGNED
    ↓
REJECTED
    ↓
REASSIGNED
```

```text
ASSIGNED
    ↓
SLA_BREACHED
    ↓
ESCALATED
    ↓
REASSIGNED
```

```text
ASSIGNED
    ↓
TRANSFERRED
    ↓
NEW_OWNER
```

---

## 30. Human Override Governance

Every human override shall record:

```text
Override User
Original Assignee
New Assignee
Original AI Recommendation
AI Confidence
Override Reason
Timestamp
Assignment Policy Version
AI Model Version
```

Organizations may require a mandatory override reason.

---

## 31. Assignment Audit Trail

Every consequential assignment action shall be auditable.

Example:

```text
10:00:00
AI recommended Agent A
Confidence: 93%

10:00:01
Manager approved recommendation

10:00:02
Agent A assigned

10:08:12
Agent A rejected assignment
Reason: Territory conflict

10:08:15
System selected Agent B

10:08:16
Agent B assigned

10:09:40
Agent B accepted
```

---

## 32. Acceptance Criteria

* [ ] Automatic assignment works.
* [ ] Manual assignment works.
* [ ] AI assignment recommendations work.
* [ ] AI automatic assignment works.
* [ ] Human approval works.
* [ ] Human override works.
* [ ] Primary ownership is maintained.
* [ ] Secondary ownership is supported where configured.
* [ ] Team assignment works.
* [ ] Queue assignment works.
* [ ] AI-agent assignment works.
* [ ] Human-agent assignment works.
* [ ] Skill matching works.
* [ ] Territory matching works.
* [ ] Industry matching works.
* [ ] Product matching works.
* [ ] Language matching works.
* [ ] Lead-score-based assignment works.
* [ ] Intent-based assignment works.
* [ ] Revenue-based assignment works.
* [ ] Capacity validation works.
* [ ] Availability validation works.
* [ ] Assignment acceptance works.
* [ ] Assignment rejection works.
* [ ] Rejection reasons are recorded.
* [ ] Reassignment works.
* [ ] Transfer works.
* [ ] Automatic reassignment works.
* [ ] Assignment escalation works.
* [ ] Assignment expiration works.
* [ ] Assignment SLA monitoring works.
* [ ] Bulk assignment works.
* [ ] Bulk reassignment works.
* [ ] Assignment simulation works.
* [ ] Historical replay works.
* [ ] Assignment conflict detection works.
* [ ] Assignment history is preserved.
* [ ] Assignment audit logging works.
* [ ] AI confidence is stored.
* [ ] AI model version is stored.
* [ ] Assignment policy version is stored.
* [ ] Assignment explanations are available.
* [ ] AI optimization recommendations work.
* [ ] Assignment experiments are supported.
* [ ] Assignment analytics are available.
* [ ] Revenue attribution is supported.
* [ ] CRM synchronization works.
* [ ] RBAC is enforced.
* [ ] Tenant isolation is enforced.
* [ ] Organization isolation is enforced.
* [ ] Workplace isolation is enforced.
* [ ] Duplicate ownership is prevented.
* [ ] Assignment race conditions are prevented.
* [ ] Failed assignments can recover.
* [ ] AI-provider failure does not prevent deterministic assignment.
* [ ] Assignment events are observable.
* [ ] Distributed tracing is supported.

---

## 33. FAANG-Level Product Outcome

SalesGenie's Lead Assignment module should evolve beyond a basic CRM ownership field into an:

**AI-Powered Revenue-Aware Lead Ownership and Accountability Engine**

For every lead, SalesGenie should be able to answer:

```text
WHO owns this lead?

WHY was this person or AI agent selected?

WHEN must they respond?

WHAT happens if they fail to respond?

HOW confident was the system?

WHO changed the assignment?

WHAT business outcome resulted?
```

The complete assignment intelligence loop should be:

```text
Lead
  ↓
Qualification
  ↓
Scoring
  ↓
Intent Detection
  ↓
Routing
  ↓
Candidate Generation
  ↓
Eligibility Validation
  ↓
AI/Human Assignment Decision
  ↓
Assignment Creation
  ↓
Notification
  ↓
Acceptance
  ↓
Sales Engagement
  ↓
SLA Monitoring
  ↓
Escalation / Reassignment
  ↓
Opportunity Creation
  ↓
Deal Conversion
  ↓
Revenue Attribution
  ↓
Assignment Performance Evaluation
  ↓
AI Optimization
  ↓
Improved Future Assignments
```

The ultimate goal is not merely to assign a lead to a salesperson.

The goal is to establish **the most appropriate, accountable, measurable, explainable, and revenue-optimized owner for every lead while preserving human control, AI governance, security, tenant isolation, and operational reliability.**
