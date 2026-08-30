# SalesGenie — Prompt Evaluation Requirements

## 1. Document Overview

### 1.1 Purpose

The **Prompt Evaluation** subsystem shall provide SalesGenie with an enterprise-grade evaluation framework for systematically measuring, validating, comparing, and governing AI prompt quality across development, testing, staging, canary, and production environments.

The subsystem shall support both:

- AI-based prompt evaluation
- Human-based prompt evaluation
- AI-assisted human evaluation
- Automated regression evaluation
- LLM-as-a-Judge evaluation
- Rule-based evaluation
- Dataset-based evaluation
- Production-feedback evaluation
- Safety evaluation
- Security evaluation
- RAG-groundedness evaluation
- Tool-use evaluation
- Multilingual evaluation
- Cost and latency evaluation
- Prompt-version comparison
- Agent-level evaluation
- Model-level evaluation
- Human review workflows
- Evaluation gates for production deployment

The subsystem shall provide objective, reproducible, auditable, and statistically meaningful evidence for deciding whether a prompt version is suitable for production.

---

## 2. Scope

The Prompt Evaluation subsystem shall evaluate prompts used by:

- AI support agents
- Human support agents using AI assistance
- AI sales agents
- Human sales agents using AI assistance
- Hybrid AI + human support
- Lead-generation agents
- RAG agents
- Conversation intelligence
- Voice AI
- Email AI
- WhatsApp AI
- Telegram AI
- Facebook Messenger AI
- SMS AI
- Web Chat
- Social Inbox
- Ticket management
- Customer-service automation
- Workflow automation
- Multi-agent systems
- Agent orchestration
- LLM Gateway
- Model routing
- Knowledge-base systems
- Analytics and reporting
- AI guardrails
- AI human handoff

---

## 3. Evaluation Objectives

The Prompt Evaluation subsystem shall determine whether a prompt:

1. Produces correct outputs.
2. Follows instructions.
3. Produces grounded responses.
4. Avoids hallucinations.
5. Uses tools correctly.
6. Escalates correctly.
7. Protects sensitive information.
8. Respects safety policies.
9. Produces consistent outputs.
10. Meets formatting requirements.
11. Provides acceptable latency.
12. Operates within cost constraints.
13. Performs consistently across models.
14. Performs consistently across channels.
15. Performs consistently across languages.
16. Improves or degrades against a baseline.
17. Performs adequately under adversarial conditions.
18. Produces acceptable business outcomes.
19. Meets human quality standards.
20. Is safe for production deployment.

---

## 4. User Requirements

## UR-001 — Create Evaluation

Authorized users shall be able to create an evaluation for a prompt version.

An evaluation shall contain:

- Prompt version
- Dataset
- Evaluation criteria
- Evaluation method
- Model
- Model parameters
- Environment
- Evaluator
- Thresholds
- Evaluation timestamp

---

## UR-002 — Evaluate Prompt Version

Users shall be able to execute an evaluation against a specific prompt version.

---

## UR-003 — Evaluate Multiple Versions

Users shall be able to evaluate multiple prompt versions against the same dataset and evaluation criteria.

---

## UR-004 — Baseline Evaluation

Users shall be able to select a production version as the evaluation baseline.

---

## UR-005 — Candidate Evaluation

Users shall be able to evaluate a candidate version against the baseline.

---

## UR-006 — Version Comparison

Users shall be able to compare evaluation results between versions.

The comparison shall include:

- Accuracy
- Relevance
- Groundedness
- Safety
- Hallucination
- Tool correctness
- Format compliance
- Latency
- Token usage
- Cost
- Human score
- Business metrics

---

## UR-007 — Evaluation Dashboard

Users shall be able to view an evaluation dashboard containing:

- Overall score
- Metric scores
- Pass/fail status
- Regression status
- Safety status
- Cost status
- Latency status
- Human evaluation status
- AI evaluation status

---

## UR-008 — Evaluation History

Users shall be able to view the complete evaluation history of a prompt.

---

## UR-009 — Evaluation Lineage

Users shall be able to identify:

```text
Prompt
    ↓
Prompt Version
    ↓
Evaluation
    ↓
Dataset
    ↓
Model
    ↓
Evaluator
    ↓
Result
```

---

## UR-010 — Evaluation Reproducibility

Users shall be able to reproduce an evaluation using the same:

* Prompt version
* Dataset version
* Model
* Model version
* Parameters
* Evaluation configuration

---

## UR-011 — Evaluation Dataset

Users shall be able to create and manage evaluation datasets.

---

## UR-012 — Dataset Versioning

Users shall be able to maintain immutable versions of evaluation datasets.

---

## UR-013 — Test Case Creation

Users shall be able to create individual evaluation cases.

Each case may contain:

* Input
* Context
* Expected output
* Expected behavior
* Evaluation criteria
* Metadata
* Severity
* Category

---

## UR-014 — Golden Dataset

Users shall be able to define a trusted golden dataset.

---

## UR-015 — Regression Dataset

Users shall be able to define datasets specifically for regression testing.

---

## UR-016 — Adversarial Dataset

Users shall be able to define adversarial datasets.

Examples:

* Prompt injection
* Jailbreak
* Data leakage
* Malicious instructions
* Tool abuse
* Context manipulation

---

## UR-017 — Human Evaluation

Human evaluators shall be able to review AI outputs manually.

---

## UR-018 — Human Scoring

Human evaluators shall be able to assign configurable scores.

Example:

```text
1 = Unacceptable
2 = Poor
3 = Acceptable
4 = Good
5 = Excellent
```

---

## UR-019 — Human Evaluation Rubrics

Administrators shall be able to define evaluation rubrics.

---

## UR-020 — Human Evaluation Comments

Human evaluators shall be able to provide comments explaining evaluation decisions.

---

## UR-021 — Human Evaluation Labels

Human evaluators shall be able to classify outputs using labels such as:

```text
CORRECT
INCORRECT
PARTIALLY_CORRECT
HALLUCINATION
UNSAFE
IRRELEVANT
ESCALATION_REQUIRED
TOOL_ERROR
FORMAT_ERROR
```

---

## UR-022 — AI Evaluation

Users shall be able to evaluate outputs automatically using AI evaluators.

---

## UR-023 — LLM-as-a-Judge

The system shall support LLM-based evaluation.

---

## UR-024 — Rule-Based Evaluation

Users shall be able to define deterministic evaluation rules.

---

## UR-025 — Hybrid Evaluation

Users shall be able to combine:

```text
AI Evaluation
+
Rule-Based Evaluation
+
Human Evaluation
```

into a single evaluation pipeline.

---

## UR-026 — Evaluation Criteria

Users shall be able to configure criteria such as:

* Accuracy
* Relevance
* Helpfulness
* Groundedness
* Factuality
* Safety
* Security
* Tone
* Empathy
* Completeness
* Conciseness
* Instruction following
* Format compliance
* Tool correctness
* Escalation correctness

---

## UR-027 — Custom Metrics

Authorized users shall be able to create organization-specific evaluation metrics.

---

## UR-028 — Metric Weighting

Users shall be able to assign different weights to evaluation metrics.

Example:

```text
Accuracy       = 30%
Groundedness   = 25%
Safety         = 25%
Format         = 10%
Tone           = 10%
```

---

## UR-029 — Threshold Configuration

Users shall be able to configure minimum acceptable thresholds.

---

## UR-030 — Pass/Fail Evaluation

The system shall determine whether an evaluation passes configured thresholds.

---

## UR-031 — Regression Detection

Users shall be able to identify whether a candidate prompt performs worse than the baseline.

---

## UR-032 — Regression Severity

Regression shall be classified as:

```text
NONE
LOW
MEDIUM
HIGH
CRITICAL
```

---

## UR-033 — Evaluation Alerts

Users shall receive alerts when:

* Evaluation fails
* Safety score decreases
* Accuracy decreases
* Hallucination increases
* Cost increases
* Latency increases
* Tool errors increase
* Customer satisfaction decreases

---

## UR-034 — Production Evaluation

Users shall be able to evaluate prompts using sampled production conversations.

---

## UR-035 — Continuous Evaluation

Users shall be able to configure recurring evaluations.

---

## UR-036 — Scheduled Evaluation

Users shall be able to schedule evaluations:

* Hourly
* Daily
* Weekly
* Monthly
* Event-triggered

---

## UR-037 — Evaluation Trigger

Users shall be able to trigger evaluations when:

* Prompt version changes
* Model changes
* Provider changes
* Agent changes
* Workflow changes
* Guardrails change
* Knowledge base changes

---

## UR-038 — Evaluation Approval

Authorized reviewers shall be able to approve evaluation results.

---

## UR-039 — Evaluation Rejection

Authorized reviewers shall be able to reject evaluation results.

---

## UR-040 — Evaluation Review Queue

Human evaluators shall have access to a queue of outputs requiring review.

---

## UR-041 — Blind Evaluation

The system shall support blind evaluation where the evaluator does not know which prompt version generated an output.

---

## UR-042 — Pairwise Evaluation

Human and AI evaluators shall be able to compare two outputs and select the better result.

---

## UR-043 — Ranking Evaluation

Evaluators shall be able to rank multiple outputs.

---

## UR-044 — Evaluation Sampling

Users shall be able to configure evaluation sampling rates.

---

## UR-045 — Evaluation Filters

Users shall be able to filter evaluations by:

* Prompt
* Version
* Agent
* Tenant
* Channel
* Model
* Provider
* Dataset
* Evaluator
* Date
* Status
* Severity

---

## UR-046 — Evaluation Search

Users shall be able to search evaluation results.

---

## UR-047 — Evaluation Export

Authorized users shall be able to export evaluation results.

---

## UR-048 — Evaluation Audit

Users shall be able to inspect who created, executed, reviewed, approved, or rejected an evaluation.

---

## UR-049 — Evaluation Incident Linking

Users shall be able to associate evaluation failures with production incidents.

---

## UR-050 — Feedback-to-Evaluation

Human feedback from SalesGenie conversations shall be convertible into evaluation cases.

---

## 5. System Requirements

## SR-001 — Evaluation Engine

The system shall provide a centralized evaluation engine capable of executing multiple evaluation strategies.

---

## SR-002 — Evaluation Types

The system shall support:

```text
Pointwise Evaluation
Pairwise Evaluation
Ranking Evaluation
Rule-Based Evaluation
LLM-as-a-Judge
Human Evaluation
Hybrid Evaluation
Regression Evaluation
Safety Evaluation
Security Evaluation
RAG Evaluation
Tool Evaluation
Performance Evaluation
Cost Evaluation
Business Outcome Evaluation
```

---

## SR-003 — Evaluation Job Architecture

Evaluations shall execute as asynchronous jobs for large datasets.

---

## SR-004 — Evaluation Job States

Evaluation jobs shall support:

```text
QUEUED
RUNNING
PAUSED
COMPLETED
FAILED
CANCELLED
PARTIALLY_COMPLETED
```

---

## SR-005 — Evaluation Job ID

Every evaluation execution shall receive a globally unique evaluation job ID.

---

## SR-006 — Evaluation Run ID

Every evaluation run shall receive a unique run identifier.

---

## SR-007 — Evaluation Metadata

Every run shall store:

```text
evaluation_id
run_id
prompt_id
prompt_version_id
dataset_id
dataset_version_id
model_id
model_version
provider_id
environment
evaluator_id
evaluation_method
configuration
created_at
started_at
completed_at
status
```

---

## SR-008 — Immutable Evaluation Results

Completed evaluation results shall be immutable.

Corrections shall create a new evaluation run.

---

## SR-009 — Dataset Versioning

Evaluation datasets shall be immutable after publication.

---

## SR-010 — Dataset Lineage

Every evaluation shall reference the exact dataset version used.

---

## SR-011 — Evaluator Versioning

AI evaluator prompts and evaluator models shall be versioned.

---

## SR-012 — Evaluator Reproducibility

The system shall record the exact evaluator configuration.

---

## SR-013 — AI Judge Configuration

LLM-as-a-Judge evaluations shall record:

* Judge model
* Judge model version
* Judge prompt
* Judge prompt version
* Temperature
* Top-p
* Token limits
* System instructions
* Evaluation rubric

---

## SR-014 — Deterministic Evaluation

Where possible, deterministic evaluation shall be supported through:

* Exact matching
* Regex
* JSON schema
* Rules
* Validators
* Tool-call validation

---

## SR-015 — Statistical Evaluation

The system shall calculate statistical metrics for sufficiently large evaluation datasets.

---

## SR-016 — Confidence Intervals

The evaluation engine should support confidence intervals for aggregate metrics.

---

## SR-017 — Sample Size

The system shall support configurable minimum sample sizes for production decisions.

---

## SR-018 — Metric Aggregation

The system shall calculate:

* Mean
* Median
* Minimum
* Maximum
* Percentiles
* Standard deviation
* Pass rate
* Failure rate

where applicable.

---

## SR-019 — Distribution Analysis

The system shall support distribution-level analysis rather than relying only on average scores.

---

## SR-020 — Outlier Detection

The evaluation engine shall identify anomalous outputs.

---

## SR-021 — Regression Engine

The system shall compare candidate results against baseline results.

---

## SR-022 — Regression Thresholds

Thresholds shall be configurable per:

* Metric
* Prompt
* Agent
* Tenant
* Environment
* Risk level

---

## SR-023 — Evaluation Gates

The system shall support automated gates for:

```text
Minimum Accuracy
Minimum Groundedness
Minimum Safety
Maximum Hallucination
Maximum Cost
Maximum Latency
Minimum Tool Accuracy
Minimum Customer Satisfaction
```

---

## SR-024 — Hard Safety Gates

Certain safety and security criteria shall be hard blockers and shall not be overridden by aggregate scores.

---

## SR-025 — Weighted Evaluation

The engine shall calculate weighted aggregate scores.

---

## SR-026 — Metric Independence

Individual metric failures shall remain visible even when the aggregate score passes.

---

## SR-027 — Evaluation Explainability

AI evaluators shall provide evidence supporting evaluation decisions.

---

## SR-028 — AI Judge Evidence

AI evaluation records shall contain:

* Score
* Reason
* Evidence
* Failed criteria
* Confidence
* Evaluation metadata

---

## SR-029 — Human Evaluation Evidence

Human evaluators shall provide configurable evidence or comments for critical decisions.

---

## SR-030 — Human-AI Agreement

The system shall measure agreement between human and AI evaluations.

---

## SR-031 — Evaluator Calibration

The system shall support calibration workflows for human evaluators.

---

## SR-032 — Evaluator Quality

The system shall track evaluator consistency and disagreement rates.

---

## SR-033 — Inter-Rater Reliability

The system should support metrics such as:

* Cohen's kappa
* Fleiss' kappa
* Krippendorff's alpha

where applicable.

---

## SR-034 — Evaluation Queue

Human evaluation tasks shall be distributed through an evaluation queue.

---

## SR-035 — Evaluation Assignment

Evaluation tasks shall support assignment based on:

* Role
* Expertise
* Language
* Channel
* Product
* Region
* Workload

---

## SR-036 — Evaluation Workload Balancing

The system shall distribute human evaluation tasks fairly.

---

## SR-037 — Evaluation Deduplication

The system shall prevent accidental duplicate evaluation tasks.

---

## SR-038 — Blind Evaluation Support

The system shall hide version identity when blind evaluation is enabled.

---

## SR-039 — Pairwise Randomization

Pairwise evaluations shall randomize output ordering to minimize positional bias.

---

## SR-040 — Evaluation Security

Evaluation datasets may contain sensitive customer information and shall be protected accordingly.

---

## SR-041 — Tenant Isolation

Tenant evaluation data shall be logically isolated.

---

## SR-042 — Evaluation RBAC

The system shall enforce permissions such as:

```text
evaluation.read
evaluation.create
evaluation.execute
evaluation.cancel
evaluation.review
evaluation.approve
evaluation.reject
evaluation.export
evaluation.admin
dataset.read
dataset.create
dataset.update
dataset.publish
rubric.create
rubric.update
rubric.admin
```

---

## SR-043 — Evaluation Audit Logging

The system shall audit:

```text
EVALUATION_CREATED
EVALUATION_STARTED
EVALUATION_COMPLETED
EVALUATION_FAILED
EVALUATION_CANCELLED
RESULT_REVIEWED
RESULT_APPROVED
RESULT_REJECTED
DATASET_CREATED
DATASET_VERSIONED
DATASET_PUBLISHED
RUBRIC_CREATED
RUBRIC_UPDATED
```

---

## SR-044 — Evaluation API

The system shall expose APIs for:

* Create evaluation
* Get evaluation
* List evaluations
* Execute evaluation
* Cancel evaluation
* Get results
* Compare results
* Review results
* Approve results
* Reject results
* Export results

---

## SR-045 — Evaluation Event Architecture

The evaluation subsystem shall publish lifecycle events through SalesGenie's event-driven architecture.

---

## SR-046 — Evaluation Queue

Large evaluation workloads shall use a distributed job queue.

---

## SR-047 — Evaluation Parallelism

The system shall support parallel evaluation of independent test cases.

---

## SR-048 — Evaluation Retry

Transient evaluation failures shall support controlled retry policies.

---

## SR-049 — Idempotency

Evaluation jobs shall support idempotent execution.

---

## SR-050 — Partial Recovery

If an evaluation fails partway through, completed test cases shall not needlessly be reprocessed.

---

## SR-051 — Evaluation Checkpointing

Large evaluations should support checkpointing.

---

## SR-052 — Rate Limiting

The evaluation engine shall respect model/provider rate limits.

---

## SR-053 — Cost Controls

The system shall enforce configurable evaluation budgets.

---

## SR-054 — Evaluation Budget

Users shall be able to define:

* Maximum tokens
* Maximum cost
* Maximum test cases
* Maximum runtime

---

## SR-055 — Cost Estimation

The system shall estimate evaluation cost before execution where provider pricing information is available.

---

## SR-056 — Cost Tracking

Actual evaluation cost shall be recorded.

---

## SR-057 — Model Routing Integration

The evaluation engine shall integrate with the Model Routing subsystem.

---

## SR-058 — LLM Gateway Integration

The evaluation engine shall execute inference through the LLM Gateway where applicable.

---

## SR-059 — Prompt Version Integration

Every evaluation shall reference an immutable prompt version.

---

## SR-060 — Agent Version Integration

Every agent-level evaluation shall reference the corresponding agent version.

---

## SR-061 — Knowledge Base Integration

RAG evaluations shall record:

* Knowledge base
* Knowledge-base version
* Retrieved documents
* Retrieval configuration
* Context provided to the model

---

## SR-062 — Tool Integration

Tool-use evaluations shall record:

* Available tools
* Tool definitions
* Tool calls
* Tool arguments
* Tool responses
* Tool authorization

---

## SR-063 — Channel Integration

Evaluations shall identify the channel:

```text
CHAT
EMAIL
WHATSAPP
TELEGRAM
FACEBOOK_MESSENGER
SMS
VOICE
WEBCHAT
SOCIAL_INBOX
```

---

## SR-064 — Production Sampling

The system shall support configurable sampling of production conversations for evaluation.

---

## SR-065 — Privacy Controls

Production evaluation sampling shall support:

* PII redaction
* Sensitive-data masking
* Access restrictions
* Retention policies

---

## SR-066 — Evaluation Observability

The subsystem shall provide:

* Metrics
* Logs
* Distributed traces
* Alerts
* Evaluation telemetry

---

## SR-067 — Evaluation Traceability

Every evaluation output shall be traceable to:

```text
Request
Prompt Version
Agent Version
Dataset Case
Model
Provider
Evaluator
Evaluation Result
```

---

## SR-068 — Multi-Model Evaluation

A prompt shall be evaluable across multiple supported models.

---

## SR-069 — Multi-Provider Evaluation

A prompt shall be evaluable across multiple LLM providers.

---

## SR-070 — Multilingual Evaluation

The system shall support evaluation across supported SalesGenie languages.

---

## SR-071 — Locale-Specific Evaluation

Evaluation criteria may vary by locale.

---

## SR-072 — Evaluation Templates

Administrators shall be able to define reusable evaluation templates.

---

## SR-073 — Evaluation Policies

Organizations shall be able to define mandatory evaluation policies.

---

## SR-074 — Risk-Based Evaluation

High-risk prompts shall require stricter evaluation policies.

---

## SR-075 — Continuous Production Evaluation

The system shall support ongoing evaluation of active production versions.

---

## 6. Functional Requirements

## FR-001 — Create Evaluation

The system shall allow authorized users to create an evaluation configuration.

---

## FR-002 — Select Prompt Version

Users shall be able to select one or more prompt versions.

---

## FR-003 — Select Dataset

Users shall be able to select a dataset and exact dataset version.

---

## FR-004 — Select Evaluation Method

Users shall be able to choose:

```text
Rule-Based
Exact Match
Semantic Similarity
LLM-as-a-Judge
Human Review
Pairwise
Ranking
Hybrid
```

---

## FR-005 — Select Metrics

Users shall be able to select evaluation metrics.

---

## FR-006 — Configure Metric Weights

Users shall be able to assign weights to selected metrics.

---

## FR-007 — Configure Thresholds

Users shall be able to configure pass/fail thresholds.

---

## FR-008 — Run Evaluation

The system shall execute an evaluation against all selected cases.

---

## FR-009 — Parallel Evaluation

Independent cases shall be evaluated concurrently where infrastructure and provider limits permit.

---

## FR-010 — Evaluation Progress

Users shall be able to monitor:

```text
Total Cases
Completed
Failed
Remaining
Pass Rate
Current Cost
Elapsed Time
Estimated Remaining Time
```

---

## FR-011 — Cancel Evaluation

Authorized users shall be able to cancel running evaluations.

---

## FR-012 — Retry Failed Cases

Users shall be able to retry failed evaluation cases.

---

## FR-013 — Resume Evaluation

The system shall support resuming interrupted evaluation jobs.

---

## FR-014 — Evaluation Results

The system shall generate case-level results.

Each result shall include:

```text
Input
Expected Output
Actual Output
Metrics
Scores
Pass/Fail
Evaluator
Evidence
Latency
Tokens
Cost
```

---

## FR-015 — Aggregate Results

The system shall calculate aggregate evaluation metrics.

---

## FR-016 — Metric Breakdown

Users shall be able to inspect every metric independently.

---

## FR-017 — Failure Analysis

Users shall be able to view failed test cases.

---

## FR-018 — Failure Categorization

The system shall categorize failures.

Example:

```text
HALLUCINATION
INSTRUCTION_FAILURE
SAFETY_FAILURE
SECURITY_FAILURE
TOOL_FAILURE
FORMAT_FAILURE
GROUNDING_FAILURE
ESCALATION_FAILURE
LATENCY_FAILURE
COST_FAILURE
```

---

## FR-019 — Error Severity

Failures shall be classified by severity.

---

## FR-020 — Evidence View

Users shall be able to inspect the evidence behind an evaluation result.

---

## FR-021 — AI Evaluation Explanation

AI judges shall produce structured explanations.

---

## FR-022 — AI Evaluation Confidence

AI judges shall return confidence where supported.

---

## FR-023 — Human Evaluation Task

The system shall create human evaluation tasks from selected outputs.

---

## FR-024 — Human Evaluation Interface

The interface shall provide:

* Input
* Context
* AI output
* Expected behavior
* Rubric
* Score controls
* Labels
* Comments
* Submit action

---

## FR-025 — Human Evaluation Assignment

The system shall assign tasks to qualified evaluators.

---

## FR-026 — Human Evaluation Submission

Evaluators shall be able to submit scores and comments.

---

## FR-027 — Human Evaluation Review

Managers shall be able to review human evaluation decisions.

---

## FR-028 — Human Evaluation Calibration

The system shall provide calibration examples to evaluators.

---

## FR-029 — Human-AI Disagreement

The system shall identify cases where AI and human evaluators disagree significantly.

---

## FR-030 — Disagreement Review

Authorized reviewers shall be able to investigate AI-human disagreements.

---

## FR-031 — Pairwise Evaluation

The system shall present two outputs and ask the evaluator to select:

```text
A Better
B Better
Tie
Both Invalid
```

---

## FR-032 — Pairwise Randomization

The system shall randomize A/B ordering.

---

## FR-033 — Ranking Evaluation

Users shall be able to rank multiple outputs.

---

## FR-034 — Blind Evaluation

The system shall hide prompt/version identity when blind evaluation is enabled.

---

## FR-035 — Rule Evaluation

The system shall support deterministic validators.

Examples:

```text
Required phrase
Forbidden phrase
Regex
JSON schema
Length
Field presence
Tool-call requirement
Tool-call prohibition
```

---

## FR-036 — Semantic Evaluation

The system shall support semantic similarity evaluation.

---

## FR-037 — LLM Judge

The system shall invoke configured judge models for qualitative evaluation.

---

## FR-038 — Judge Rubric

The LLM judge shall evaluate against a structured rubric.

---

## FR-039 — Judge Evidence

The judge shall provide evidence supporting its score.

---

## FR-040 — Judge Versioning

The judge prompt and judge configuration shall be versioned.

---

## FR-041 — Regression Evaluation

The system shall automatically compare a candidate prompt against a baseline.

---

## FR-042 — Regression Report

The system shall generate:

```text
Improved Metrics
Regressed Metrics
Unchanged Metrics
New Failures
Resolved Failures
Critical Regressions
```

---

## FR-043 — Regression Gate

The system shall automatically mark a candidate as:

```text
PASS
FAIL
REVIEW_REQUIRED
```

---

## FR-044 — Critical Regression

Any configured critical regression shall be capable of blocking production deployment.

---

## FR-045 — Safety Evaluation

The system shall test:

* Harmful requests
* Unsafe responses
* Policy violations
* Jailbreaks
* Prompt injection
* Sensitive-data disclosure

---

## FR-046 — Security Evaluation

The system shall test:

* Credential disclosure
* System-prompt leakage
* Data exfiltration
* Unauthorized tool use
* Privilege escalation
* Cross-tenant leakage

---

## FR-047 — RAG Evaluation

The system shall evaluate:

* Retrieval relevance
* Context relevance
* Groundedness
* Citation correctness
* Unsupported claims
* Context utilization

---

## FR-048 — Tool Evaluation

The system shall evaluate:

* Tool selection
* Tool arguments
* Tool ordering
* Authorization
* Tool response handling
* Confirmation requirements

---

## FR-049 — Escalation Evaluation

The system shall determine whether the agent:

* Should resolve
* Should ask clarification
* Should escalate
* Should transfer to human
* Should create a ticket

---

## FR-050 — Multilingual Evaluation

The system shall evaluate language-specific behavior.

---

## FR-051 — Voice Evaluation

Voice prompt evaluation shall support:

* Transcription accuracy
* Response appropriateness
* Turn-taking
* Escalation
* Voice-agent policy adherence

---

## FR-052 — Channel Evaluation

The system shall evaluate channel-specific requirements.

---

## FR-053 — Customer Satisfaction Evaluation

The system shall associate evaluation results with customer satisfaction where available.

---

## FR-054 — Business Outcome Evaluation

Sales prompts shall support evaluation of:

* Lead qualification
* Conversion
* Appointment booking
* Sales opportunity creation
* Follow-up quality

---

## FR-055 — Support Outcome Evaluation

Support prompts shall support evaluation of:

* Resolution
* First-contact resolution
* Escalation accuracy
* Ticket creation
* SLA compliance
* Customer satisfaction

---

## FR-056 — Cost Evaluation

The system shall calculate:

```text
Input Tokens
Output Tokens
Total Tokens
Cost per Case
Total Evaluation Cost
Cost Difference vs Baseline
```

---

## FR-057 — Latency Evaluation

The system shall calculate:

```text
Average Latency
P50
P90
P95
P99
Maximum Latency
```

---

## FR-058 — Production Sampling Evaluation

The system shall sample production interactions for continuous evaluation.

---

## FR-059 — Production Evaluation Privacy

Production evaluation data shall be sanitized according to configured privacy policies.

---

## FR-060 — Continuous Evaluation

The system shall automatically evaluate a configurable percentage of production traffic.

---

## FR-061 — Scheduled Evaluation

Users shall be able to schedule recurring evaluation runs.

---

## FR-062 — Event-Triggered Evaluation

The system shall automatically trigger evaluations after significant configuration changes.

---

## FR-063 — Evaluation Template

Users shall be able to create reusable evaluation templates.

---

## FR-064 — Evaluation Policy

Administrators shall be able to define evaluation policies.

---

## FR-065 — Risk-Based Evaluation

High-risk prompt versions shall automatically receive enhanced evaluation requirements.

---

## FR-066 — Production Gate

The system shall prevent production deployment when mandatory evaluation requirements fail.

---

## FR-067 — Evaluation Approval

Authorized reviewers shall be able to approve successful evaluation results.

---

## FR-068 — Evaluation Rejection

Authorized reviewers shall be able to reject evaluation results.

---

## FR-069 — Evaluation Override

Only explicitly authorized roles shall be able to override evaluation failures.

All overrides shall require:

* Reason
* Actor
* Timestamp
* Affected version
* Failed criteria

---

## FR-070 — Evaluation Dashboard

The dashboard shall display:

```text
Overall Score
Metric Scores
Pass Rate
Failure Rate
Regression Status
Safety Status
Human Score
AI Score
Cost
Latency
Trend
```

---

## FR-071 — Evaluation Trends

Users shall be able to inspect evaluation metrics over time.

---

## FR-072 — Version Trend Comparison

Users shall be able to compare performance across prompt versions.

---

## FR-073 — Model Trend Comparison

Users shall be able to compare prompt performance across models.

---

## FR-074 — Provider Comparison

Users shall be able to compare evaluation results across LLM providers.

---

## FR-075 — Channel Comparison

Users shall be able to compare evaluation performance across channels.

---

## FR-076 — Tenant Comparison

Authorized enterprise administrators shall be able to compare evaluation results across tenants according to access policy.

---

## FR-077 — Evaluation Export

The system shall export evaluation results in structured formats.

---

## FR-078 — Evaluation API

All major evaluation operations shall be available through APIs.

---

## FR-079 — Evaluation Webhooks

The system shall emit evaluation lifecycle events.

---

## FR-080 — Evaluation Notifications

The system shall notify relevant stakeholders about evaluation outcomes.

---

## 7. AI-Based Functional Requirements

## AI-FR-001 — AI Judge

AI shall evaluate prompt outputs against configurable evaluation rubrics.

---

## AI-FR-002 — AI Quality Scoring

AI shall score outputs for:

* Correctness
* Relevance
* Helpfulness
* Completeness
* Tone
* Instruction following

---

## AI-FR-003 — AI Groundedness Evaluation

AI shall determine whether an answer is supported by supplied knowledge.

---

## AI-FR-004 — AI Hallucination Detection

AI shall identify claims unsupported by:

* User input
* Retrieved context
* Authorized tools
* Known system data

---

## AI-FR-005 — AI Safety Evaluation

AI shall detect unsafe or policy-violating responses.

---

## AI-FR-006 — AI Security Evaluation

AI shall identify potential:

* Prompt injection
* Jailbreak
* Data leakage
* Privilege escalation
* System-prompt extraction

---

## AI-FR-007 — AI Tool Evaluation

AI shall evaluate whether tools were selected and invoked correctly.

---

## AI-FR-008 — AI Escalation Evaluation

AI shall determine whether escalation or human handoff was appropriate.

---

## AI-FR-009 — AI Tone Evaluation

AI shall evaluate:

* Professionalism
* Empathy
* Clarity
* Brand alignment
* Cultural appropriateness

---

## AI-FR-010 — AI Consistency Evaluation

AI shall evaluate consistency across similar inputs.

---

## AI-FR-011 — AI Regression Analysis

AI shall identify likely causes of performance regression between versions.

---

## AI-FR-012 — AI Failure Clustering

AI shall group similar failures into clusters.

Example:

```text
Cluster 1 → Hallucination
Cluster 2 → Tool misuse
Cluster 3 → Poor escalation
Cluster 4 → Incorrect policy interpretation
```

---

## AI-FR-013 — AI Test Generation

AI shall generate additional evaluation cases from detected weaknesses.

---

## AI-FR-014 — AI Adversarial Test Generation

AI shall generate adversarial inputs for robustness testing.

---

## AI-FR-015 — AI Evaluation Optimization

AI shall recommend improved evaluation criteria based on observed failures.

---

## AI-FR-016 — AI Prompt Diagnosis

AI shall identify prompt instructions likely responsible for failures.

---

## AI-FR-017 — AI Improvement Recommendation

AI shall recommend:

```text
KEEP
MODIFY
REMOVE
ADD
RETEST
ROLLBACK
```

for problematic prompt instructions.

---

## AI-FR-018 — AI Evaluation Summary

AI shall generate human-readable summaries of evaluation results.

---

## AI-FR-019 — AI Deployment Recommendation

AI may recommend:

```text
PROMOTE
HOLD
RETEST
REJECT
ROLLBACK
```

based on evaluation evidence.

AI recommendations shall not bypass mandatory governance policies.

---

## AI-FR-020 — AI Drift Detection

AI shall identify behavioral drift between:

* Historical versions
* Current production versions
* New candidate versions

---

## AI-FR-021 — AI Production Monitoring

AI shall analyze production evaluation samples and identify emerging quality degradation.

---

## AI-FR-022 — AI Root-Cause Analysis

AI shall correlate:

```text
Prompt Changes
+
Model Changes
+
Knowledge Base Changes
+
Tool Changes
+
Production Failures
```

to identify probable causes.

---

## AI-FR-023 — AI Evaluation Confidence

AI evaluation results shall include confidence where supported.

---

## AI-FR-024 — AI-Human Disagreement Detection

AI shall identify significant disagreement between AI and human evaluations.

---

## 8. Human-Based Functional Requirements

## HR-FR-001 — Human Review

Human evaluators shall manually inspect selected outputs.

---

## HR-FR-002 — Human Scoring

Human evaluators shall assign configurable scores.

---

## HR-FR-003 — Human Labels

Human evaluators shall assign standardized labels.

---

## HR-FR-004 — Human Comments

Human evaluators shall provide explanations for significant failures.

---

## HR-FR-005 — Human Rubric

Human evaluation shall use organization-defined rubrics.

---

## HR-FR-006 — Human Calibration

The platform shall provide calibration exercises to improve evaluator consistency.

---

## HR-FR-007 — Human Blind Review

Evaluators shall be able to review outputs without knowing their prompt version.

---

## HR-FR-008 — Human Pairwise Review

Evaluators shall compare multiple outputs and identify the best response.

---

## HR-FR-009 — Human Ranking

Evaluators shall rank outputs based on configured criteria.

---

## HR-FR-010 — Human Escalation Review

Support managers shall be able to review whether AI escalation decisions were appropriate.

---

## HR-FR-011 — Human Tool Review

Qualified reviewers shall be able to verify AI tool usage.

---

## HR-FR-012 — Human Safety Review

Authorized reviewers shall be able to review safety-critical outputs.

---

## HR-FR-013 — Human Security Review

Security reviewers shall be able to inspect suspected data-leakage or prompt-injection failures.

---

## HR-FR-014 — Human Approval

Authorized reviewers shall be able to approve evaluation results for deployment gates.

---

## HR-FR-015 — Human Rejection

Authorized reviewers shall be able to reject results.

---

## HR-FR-016 — Human Override

Authorized reviewers may override selected evaluation failures where governance permits.

Overrides shall always be audited.

---

## HR-FR-017 — Human Feedback Loop

Human reviewers shall be able to convert recurring failures into new evaluation cases.

---

## HR-FR-018 — Human Incident Review

Human operators shall be able to associate evaluation failures with incidents.

---

## 9. Evaluation Metric Framework

## 9.1 Core Quality Metrics

```text
Accuracy
Correctness
Relevance
Helpfulness
Completeness
Instruction Following
Consistency
Clarity
Conciseness
```

---

## 9.2 AI Safety Metrics

```text
Safety Score
Policy Compliance
Harmful Response Rate
Jailbreak Success Rate
Prompt Injection Success Rate
Sensitive Data Disclosure Rate
Unsafe Tool Action Rate
```

---

## 9.3 RAG Metrics

```text
Retrieval Relevance
Context Relevance
Context Recall
Context Precision
Groundedness
Citation Correctness
Unsupported Claim Rate
```

---

## 9.4 Tool Metrics

```text
Tool Selection Accuracy
Tool Argument Accuracy
Tool Invocation Success
Tool Authorization Compliance
Tool Call Efficiency
Tool Error Rate
```

---

## 9.5 Support Metrics

```text
Resolution Accuracy
First Contact Resolution
Escalation Accuracy
Ticket Creation Accuracy
SLA Compliance
Customer Satisfaction
```

---

## 9.6 Sales Metrics

```text
Lead Qualification Accuracy
Lead Intent Classification
Opportunity Creation Accuracy
Appointment Booking Accuracy
Follow-Up Quality
Conversion Rate
Revenue Attribution
```

---

## 9.7 Performance Metrics

```text
P50 Latency
P90 Latency
P95 Latency
P99 Latency
Time to First Token
Total Response Time
```

---

## 9.8 Cost Metrics

```text
Input Tokens
Output Tokens
Total Tokens
Cost per Request
Cost per Conversation
Evaluation Cost
Cost Difference vs Baseline
```

---

## 10. Evaluation Pipeline

```text
                     Prompt Version
                           │
                           ▼
                   Evaluation Config
                           │
                           ▼
                     Dataset Loader
                           │
                           ▼
                    Test Case Runner
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
        Rule Engine     AI Judge     Human Queue
             │             │             │
             └─────────────┼─────────────┘
                           │
                           ▼
                    Result Aggregator
                           │
                           ▼
                    Regression Engine
                           │
                           ▼
                    Safety Gate
                           │
                           ▼
                    Quality Gate
                           │
                           ▼
                     Cost Gate
                           │
                           ▼
                    Latency Gate
                           │
                           ▼
                  Human Approval Gate
                           │
                           ▼
                 Production Decision
```

---

## 11. Evaluation Lifecycle

```text
DRAFT
  │
  ▼
CONFIGURED
  │
  ▼
QUEUED
  │
  ▼
RUNNING
  │
  ├───────────────► FAILED
  │
  ▼
COMPLETED
  │
  ▼
ANALYZING
  │
  ├───────────────► REGRESSION
  │
  ▼
REVIEW_REQUIRED
  │
  ├───────────────► REJECTED
  │
  ▼
APPROVED
  │
  ▼
DEPLOYMENT_GATE
  │
  ├───────────────► BLOCKED
  │
  ▼
PASSED
```

---

## 12. Evaluation Architecture

```text
                         SalesGenie
                             │
                             ▼
                    Prompt Evaluation API
                             │
                             ▼
                    Evaluation Orchestrator
                             │
          ┌──────────────────┼───────────────────┐
          │                  │                   │
          ▼                  ▼                   ▼
    Dataset Service      Evaluation Engine   Human Review
          │                  │                   │
          │          ┌───────┼────────┐          │
          │          │       │        │          │
          │          ▼       ▼        ▼          │
          │        Rules   AI Judge  Metrics      │
          │          │       │        │          │
          └──────────┴───────┼────────┘          │
                             │                   │
                             ▼                   │
                      Result Aggregator ◄────────┘
                             │
                             ▼
                       Regression Engine
                             │
                             ▼
                        Policy Gates
                             │
                             ▼
                      Deployment Manager
```

---

## 13. Evaluation Dataset Requirements

Each evaluation dataset shall support:

```text
dataset_id
dataset_version
name
description
domain
language
channel
created_by
created_at
status
case_count
```

Each test case shall support:

```text
case_id
dataset_version
input
context
expected_output
expected_behavior
category
severity
tags
metadata
```

---

## 14. Evaluation Result Object

```json
{
  "evaluation_id": "eval_001",
  "run_id": "run_001",
  "prompt_id": "prompt_support_001",
  "prompt_version_id": "pv_2_3_1",
  "dataset_id": "support_golden_dataset",
  "dataset_version": "12.0",
  "model_id": "model_001",
  "model_version": "latest",
  "provider_id": "provider_001",
  "status": "COMPLETED",
  "metrics": {
    "accuracy": 0.96,
    "groundedness": 0.97,
    "safety": 0.995,
    "relevance": 0.95,
    "format_compliance": 0.99,
    "tool_accuracy": 0.98,
    "human_score": 4.7,
    "latency_p95_ms": 920,
    "average_cost": 0.0031
  },
  "regression": {
    "baseline_version": "2.2.4",
    "accuracy_delta": 0.021,
    "groundedness_delta": 0.018,
    "cost_delta": 0.004,
    "latency_delta_ms": 42,
    "status": "PASS"
  },
  "decision": "PROMOTE"
}
```

---

## 15. Evaluation Governance Matrix

| Operation                   |        AI | Human Evaluator |    Manager | AI Platform Admin | Super Admin |
| --------------------------- | --------: | --------------: | ---------: | ----------------: | ----------: |
| Create Evaluation           |       Yes |             Yes |        Yes |               Yes |         Yes |
| Configure Dataset           |       Yes |      Restricted |        Yes |               Yes |         Yes |
| Execute Evaluation          |       Yes |             Yes |        Yes |               Yes |         Yes |
| Review Results              |       Yes |             Yes |        Yes |               Yes |         Yes |
| Approve Results             |        No |      Restricted |        Yes |               Yes |         Yes |
| Reject Results              |        No |             Yes |        Yes |               Yes |         Yes |
| Override Gate               |        No |              No | Restricted |               Yes |         Yes |
| Configure Rubric            | AI Assist |             Yes |        Yes |               Yes |         Yes |
| Configure Threshold         |        No |      Restricted |        Yes |               Yes |         Yes |
| Export Results              |        No |      Restricted |        Yes |               Yes |         Yes |
| Configure Evaluation Policy |        No |              No | Restricted |               Yes |         Yes |
| Modify Security Gates       |        No |              No |         No |        Restricted |         Yes |

---

## 16. Evaluation Gate Requirements

## Mandatory Gates

Production-bound prompt versions shall satisfy:

```text
Validation Gate
      ↓
Functional Test Gate
      ↓
Regression Gate
      ↓
Safety Gate
      ↓
Security Gate
      ↓
Groundedness Gate
      ↓
Tool Gate
      ↓
Cost Gate
      ↓
Latency Gate
      ↓
Human Review Gate
```

---

## 17. Hard-Failure Conditions

The following shall be capable of immediately failing an evaluation:

```text
Critical Safety Violation
Critical Security Violation
Cross-Tenant Data Leakage
Unauthorized Tool Execution
Credential Disclosure
System Prompt Leakage
Critical Hallucination
Critical Policy Violation
Critical Regression
```

Aggregate scores shall not automatically override hard-failure conditions.

---

## 18. Human + AI Evaluation Model

```text
                         Evaluation Case
                               │
                ┌──────────────┴──────────────┐
                │                             │
                ▼                             ▼
             AI Judge                    Human Judge
                │                             │
                ▼                             ▼
          AI Score + Evidence          Human Score + Evidence
                │                             │
                └──────────────┬──────────────┘
                               ▼
                       Agreement Analysis
                               │
                ┌──────────────┴──────────────┐
                │                             │
             Agreement                  Disagreement
                │                             │
                ▼                             ▼
            Aggregate                  Human Review Queue
                                             │
                                             ▼
                                      Final Decision
```

---

## 19. Continuous Evaluation

SalesGenie shall continuously evaluate production behavior using configurable sampling.

Example:

```text
Production Traffic
       │
       ▼
5% Evaluation Sample
       │
       ▼
Automatic Evaluation
       │
       ├── Quality Drop
       │       ↓
       │    Alert
       │       ↓
       │    Human Review
       │
       └── Normal
               ↓
          Continue Monitoring
```

---

## 20. Incident-to-Evaluation Feedback Loop

```text
Production Incident
        │
        ▼
Identify Prompt Version
        │
        ▼
Analyze Failed Output
        │
        ▼
Human Investigation
        │
        ▼
AI Root-Cause Analysis
        │
        ▼
Create Regression Case
        │
        ▼
Add to Regression Dataset
        │
        ▼
Evaluate Candidate Version
        │
        ▼
Compare Against Baseline
        │
        ▼
Deploy Only If Gates Pass
```

---

## 21. Evaluation Observability

Every evaluation request shall propagate:

```text
request_id
trace_id
evaluation_id
evaluation_run_id
prompt_id
prompt_version_id
agent_id
agent_version_id
dataset_id
dataset_version_id
model_id
model_version
provider_id
channel
tenant_id
environment
```

The observability platform shall allow operators to navigate:

```text
Prompt Version
      ↓
Evaluation Run
      ↓
Test Case
      ↓
Model Request
      ↓
Model Response
      ↓
Evaluation Result
      ↓
Production Outcome
```

---

## 22. Evaluation Analytics

The system shall provide dashboards for:

## Prompt Quality

```text
Accuracy
Groundedness
Safety
Relevance
Completeness
Instruction Following
```

## Version Comparison

```text
Current Version
Candidate Version
Metric Delta
Regression
Improvement
```

## Human Evaluation

```text
Human Score
Evaluator Agreement
Evaluator Disagreement
Calibration Score
Review Completion
```

## AI Evaluation

```text
AI Score
Judge Confidence
Judge Agreement
AI-Human Agreement
```

## Operational Performance

```text
Latency
Token Usage
Cost
Evaluation Runtime
Failure Rate
```

---

## 23. Non-Functional Requirements

## NFR-001 — Availability

The evaluation API shall target:

```text
99.9% availability
```

---

## NFR-002 — Scalability

The evaluation engine shall support horizontally scalable workers.

---

## NFR-003 — Parallelism

Independent evaluation cases shall be evaluated concurrently.

---

## NFR-004 — Reliability

Transient provider failures shall not corrupt evaluation results.

---

## NFR-005 — Fault Tolerance

Evaluation jobs shall support retry, checkpointing, and partial recovery.

---

## NFR-006 — Reproducibility

Completed evaluations shall be reproducible from immutable artifacts.

---

## NFR-007 — Auditability

Every evaluation lifecycle event shall be auditable.

---

## NFR-008 — Security

Evaluation data shall be encrypted in transit and at rest.

---

## NFR-009 — Tenant Isolation

Evaluation data shall remain isolated between tenants.

---

## NFR-010 — Privacy

Production conversation evaluation shall support PII masking and redaction.

---

## NFR-011 — Performance

The system shall optimize evaluation throughput while respecting model/provider rate limits.

---

## NFR-012 — Cost Efficiency

The system shall prevent uncontrolled evaluation spending through configurable budgets and limits.

---

## NFR-013 — Extensibility

The evaluation framework shall support adding new:

* Metrics
* Judges
* Models
* Providers
* Rubrics
* Datasets
* Evaluation algorithms
* Business metrics

without major architectural changes.

---

## NFR-014 — Explainability

AI evaluation decisions shall be accompanied by evidence and structured reasoning artifacts.

---

## NFR-015 — Determinism

Deterministic evaluators shall produce repeatable results for identical inputs and configurations.

---

## NFR-016 — Version Integrity

Evaluations shall always reference immutable prompt and dataset versions.

---

## NFR-017 — Disaster Recovery

Evaluation configurations, datasets, results, and audit history shall be recoverable.

---

## NFR-018 — Observability

Evaluation workers shall expose:

* Logs
* Metrics
* Traces
* Health checks
* Error telemetry

---

## 24. Prompt Evaluation API Requirements

## POST `/evaluations`

Create an evaluation.

---

## GET `/evaluations/{evaluation_id}`

Retrieve evaluation configuration and status.

---

## POST `/evaluations/{evaluation_id}/run`

Start an evaluation run.

---

## POST `/evaluations/{evaluation_id}/cancel`

Cancel a running evaluation.

---

## GET `/evaluations/{evaluation_id}/runs`

List evaluation runs.

---

## GET `/evaluations/runs/{run_id}`

Retrieve evaluation run metadata.

---

## GET `/evaluations/runs/{run_id}/results`

Retrieve case-level results.

---

## GET `/evaluations/runs/{run_id}/summary`

Retrieve aggregate metrics.

---

## POST `/evaluations/runs/{run_id}/review`

Submit human evaluation review.

---

## POST `/evaluations/runs/{run_id}/approve`

Approve evaluation results.

---

## POST `/evaluations/runs/{run_id}/reject`

Reject evaluation results.

---

## GET `/evaluations/compare`

Compare two or more evaluation runs.

---

## GET `/evaluations/metrics`

Retrieve evaluation metrics.

---

## 25. Acceptance Criteria

The Prompt Evaluation subsystem shall be considered production-ready when:

* [ ] Prompt versions can be evaluated independently.
* [ ] Multiple prompt versions can be compared.
* [ ] Baseline evaluation is supported.
* [ ] Candidate evaluation is supported.
* [ ] Immutable evaluation results are supported.
* [ ] Evaluation datasets are versioned.
* [ ] Golden datasets are supported.
* [ ] Regression datasets are supported.
* [ ] Adversarial datasets are supported.
* [ ] Individual test cases are supported.
* [ ] Batch evaluation is supported.
* [ ] Parallel evaluation is supported.
* [ ] Evaluation jobs are asynchronous.
* [ ] Evaluation jobs support retries.
* [ ] Evaluation jobs support cancellation.
* [ ] Evaluation jobs support recovery.
* [ ] Rule-based evaluation is supported.
* [ ] Semantic evaluation is supported.
* [ ] LLM-as-a-Judge is supported.
* [ ] Human evaluation is supported.
* [ ] Hybrid AI + human evaluation is supported.
* [ ] Pairwise evaluation is supported.
* [ ] Ranking evaluation is supported.
* [ ] Blind evaluation is supported.
* [ ] Human evaluation rubrics are configurable.
* [ ] AI evaluator rubrics are configurable.
* [ ] AI evaluator versions are tracked.
* [ ] Human evaluator identities are audited.
* [ ] Human-AI agreement is measurable.
* [ ] Evaluator calibration is supported.
* [ ] Inter-rater reliability can be calculated.
* [ ] Accuracy is measurable.
* [ ] Relevance is measurable.
* [ ] Groundedness is measurable.
* [ ] Hallucination is measurable.
* [ ] Safety is measurable.
* [ ] Security is measurable.
* [ ] Tool correctness is measurable.
* [ ] Escalation correctness is measurable.
* [ ] Format compliance is measurable.
* [ ] Cost is measurable.
* [ ] Latency is measurable.
* [ ] Customer satisfaction can be incorporated.
* [ ] Business outcomes can be incorporated.
* [ ] Metric weighting is supported.
* [ ] Thresholds are configurable.
* [ ] Hard safety gates are supported.
* [ ] Regression detection is supported.
* [ ] Regression severity is supported.
* [ ] Production deployment gates are supported.
* [ ] Evaluation failures can block deployment.
* [ ] Authorized overrides are audited.
* [ ] AI can generate additional test cases.
* [ ] AI can identify likely failure causes.
* [ ] AI can cluster failures.
* [ ] AI can recommend prompt improvements.
* [ ] AI can detect behavioral drift.
* [ ] Human evaluators can manually inspect outputs.
* [ ] Human evaluators can score outputs.
* [ ] Human evaluators can add labels.
* [ ] Human evaluators can add comments.
* [ ] Human reviewers can approve evaluations.
* [ ] Human reviewers can reject evaluations.
* [ ] Production traffic can be sampled.
* [ ] Production evaluation supports privacy controls.
* [ ] Continuous evaluation is supported.
* [ ] Scheduled evaluation is supported.
* [ ] Event-triggered evaluation is supported.
* [ ] Evaluation policies are configurable.
* [ ] Risk-based evaluation is supported.
* [ ] High-risk prompts receive enhanced evaluation.
* [ ] Evaluation results are traceable to exact prompt versions.
* [ ] Evaluation results are traceable to exact dataset versions.
* [ ] Evaluation results are traceable to exact model versions.
* [ ] Evaluation results are traceable to exact evaluator versions.
* [ ] LLM Gateway integration is implemented.
* [ ] Model Routing integration is implemented.
* [ ] Agent Versioning integration is implemented.
* [ ] Prompt Versioning integration is implemented.
* [ ] Knowledge Base integration is implemented.
* [ ] Tool evaluation integration is implemented.
* [ ] Guardrail evaluation is implemented.
* [ ] Human handoff evaluation is implemented.
* [ ] Omnichannel evaluation is implemented.
* [ ] Tenant isolation is verified.
* [ ] RBAC is enforced.
* [ ] Audit logging is implemented.
* [ ] Evaluation observability is implemented.
* [ ] Evaluation analytics are available.
* [ ] Evaluation APIs are implemented.
* [ ] Evaluation lifecycle events are published.
* [ ] Disaster recovery has been tested.
* [ ] Evaluation cost controls are enforced.
* [ ] Evaluation privacy controls are enforced.
* [ ] Critical safety failures cannot be hidden by aggregate scores.
* [ ] Production-bound prompt versions cannot bypass mandatory evaluation gates.
