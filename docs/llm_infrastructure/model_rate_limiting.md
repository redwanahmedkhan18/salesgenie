# SalesGenie — Model Rate Limiting Requirements

## 1. Document Overview

### 1.1 Purpose

The **Model Rate Limiting** subsystem provides enterprise-grade control over AI/LLM request throughput, token consumption, concurrency, burst traffic, provider quotas, tenant budgets, and model-specific capacity.

The subsystem must protect SalesGenie from:

- LLM provider rate-limit violations
- API quota exhaustion
- runaway AI agents
- accidental request storms
- malicious abuse
- tenant-level resource starvation
- excessive token consumption
- uncontrolled concurrent model execution
- cascading failures across AI services
- unfair resource allocation between tenants
- unexpected AI infrastructure costs

The system must support both:

1. **AI-driven rate management**
2. **Human-controlled rate-management policies**

The design must operate across SalesGenie's multi-tenant, multi-agent, multi-model, omnichannel enterprise architecture.

---

## 2. Scope

The Model Rate Limiting subsystem shall govern AI-model traffic originating from:

- AI support agents
- Human-assisted support workflows
- Hybrid AI + human conversations
- Sales agents
- Lead-generation agents
- RAG agents
- Workflow agents
- Voice agents
- Document intelligence agents
- Customer-service automation
- Conversation intelligence
- Scheduled reports
- Analytics
- Background jobs
- API consumers
- Web applications
- External integrations
- Internal microservices
- Administrative operations

Rate limiting shall be enforceable at multiple dimensions:

- Global
- Platform
- Organization / tenant
- Workspace
- User
- Role
- AI agent
- Agent type
- Conversation
- Session
- API client
- Integration
- Channel
- Model provider
- Model
- Endpoint
- Operation
- IP / network identity
- Token budget
- Request count
- Concurrency
- Cost
- Time window

---

## 3. User Requirements

## UR-001 — Platform Owner Rate-Limit Management

The platform owner shall be able to define global AI-model rate limits.

The platform owner shall be able to configure:

- Requests per second
- Requests per minute
- Requests per hour
- Requests per day
- Tokens per second
- Tokens per minute
- Tokens per hour
- Tokens per day
- Concurrent requests
- Concurrent conversations
- Concurrent agent executions
- Maximum input tokens
- Maximum output tokens
- Maximum context size
- Maximum AI spend
- Burst capacity
- Queue capacity
- Retry limits

---

## UR-002 — Tenant-Level Rate Limits

Organization administrators shall be able to configure AI resource limits for their organization.

They shall be able to define separate limits for:

- Total AI requests
- Total tokens
- Total model cost
- Concurrent AI requests
- Concurrent agents
- Individual users
- Individual agents
- Channels
- Models
- Providers
- Workflows

---

## UR-003 — User-Level Rate Limits

Authorized administrators shall be able to configure per-user AI limits.

A user may have:

- Request quota
- Token quota
- Cost quota
- Concurrent request limit
- Agent execution limit
- Workflow execution limit
- Channel-specific limits
- Model-specific limits

---

## UR-004 — Role-Based Rate Limits

The system shall support different limits based on user roles.

Example roles:

- Super Admin
- Organization Admin
- Manager
- Support Manager
- Support Agent
- Sales Manager
- Sales Agent
- Analyst
- Developer
- AI Agent
- API Client
- End User

Each role may have independent rate-limit policies.

---

## UR-005 — AI Agent Rate Limits

Administrators shall be able to configure limits for individual AI agents.

The system shall support:

- Agent request limits
- Agent token limits
- Agent concurrency limits
- Agent workflow limits
- Agent tool-call limits
- Agent retry limits
- Agent budget limits
- Agent channel limits

---

## UR-006 — Model-Specific Limits

Administrators shall be able to define limits for individual models.

Examples:

- GPT-class models
- Gemini-class models
- Claude-class models
- Grok-class models
- Mistral-class models
- Local/self-hosted models

Each model may have independent:

- RPM
- TPM
- RPD
- TPD
- concurrency
- burst
- cost
- retry
- queue limits

---

## UR-007 — Provider-Specific Limits

The system shall support provider-specific limits.

Each provider may have different:

- Requests-per-minute limits
- Tokens-per-minute limits
- Daily quotas
- Concurrent-request limits
- Burst limits
- Error thresholds
- Cost limits

Provider policies shall not be assumed to be identical.

---

## UR-008 — Channel-Based Limits

Administrators shall be able to apply rate limits based on communication channels.

Supported channels shall include:

- Web Chat
- Chat
- Email
- WhatsApp
- Telegram
- Facebook Messenger
- SMS
- Voice
- Social Inbox
- API

---

## UR-009 — Human Support Rate Management

Human support managers shall be able to control AI usage associated with human-assisted support.

The system shall allow managers to limit:

- AI suggestions per agent
- AI response generation
- AI summarization
- AI translation
- AI classification
- AI conversation analysis
- AI knowledge retrieval
- AI response regeneration

---

## UR-010 — AI-Automated Rate Management

The system shall automatically adjust model traffic according to:

- Current provider capacity
- Provider rate-limit responses
- Queue depth
- Request latency
- Error rates
- Token consumption
- Tenant priority
- Model availability
- System health
- Cost constraints

---

## UR-011 — Burst Traffic Handling

The system shall support temporary traffic bursts.

Users shall be able to configure:

- Burst capacity
- Burst duration
- Burst refill rate
- Burst priority
- Burst fallback behavior

---

## UR-012 — Rate-Limit Visibility

Authorized users shall be able to view:

- Current usage
- Current limits
- Remaining quota
- Consumed quota
- Rate-limit violations
- Throttled requests
- Queued requests
- Rejected requests
- Retry attempts
- Provider throttling
- Token consumption

---

## UR-013 — Rate-Limit Notifications

The system shall notify authorized users when thresholds are reached.

Notifications shall support:

- Warning thresholds
- Critical thresholds
- Quota exhaustion
- Provider throttling
- Repeated violations
- Abnormal usage
- Budget exhaustion

---

## UR-014 — Emergency Controls

Super Admins shall be able to:

- Pause AI traffic
- Pause a provider
- Pause a model
- Pause an agent
- Pause a tenant
- Reduce global limits
- Increase global limits
- Block specific API clients
- Enable emergency throttling

---

## UR-015 — Human Override

Authorized human administrators shall be able to override automated rate-management decisions.

Overrides shall support:

- Temporary limit increases
- Temporary limit reductions
- Priority access
- Emergency bypass
- Provider bypass
- Model bypass
- Tenant bypass

Every override shall be audited.

---

## UR-016 — Priority-Based Access

The system shall support priority classes.

Example:

```text
P0 — Critical enterprise operations
P1 — High-priority support
P2 — Standard support
P3 — Sales automation
P4 — Background workflows
P5 — Batch analytics
```

Higher-priority requests shall receive preferential access during resource contention.

---

## UR-017 — Fair Resource Allocation

The system shall prevent one tenant, user, agent, or workflow from monopolizing shared AI capacity.

---

## UR-018 — Graceful Degradation

When rate limits are reached, SalesGenie shall degrade gracefully rather than failing the entire platform.

Possible actions:

* Queue request
* Delay request
* Retry request
* Switch model
* Switch provider
* Reduce model capacity
* Disable non-critical AI features
* Route to human support
* Return controlled error

---

## 4. System Requirements

## SR-001 — Distributed Rate Limiting

The system shall implement distributed rate limiting across all SalesGenie AI services.

Rate limiting shall remain consistent when multiple application instances process requests concurrently.

---

## SR-002 — High Availability

The rate-limiting subsystem shall not become a single point of failure for AI services.

If the rate-limit service becomes unavailable, the system shall follow a configurable fail-open or fail-closed policy depending on operation criticality.

---

## SR-003 — Multi-Tenant Isolation

All rate-limit counters and policies shall support strict tenant isolation.

A tenant shall never be able to consume another tenant's allocated quota.

---

## SR-004 — Hierarchical Rate Limits

The system shall evaluate rate limits hierarchically.

Example:

```text
Platform
   ↓
Provider
   ↓
Model
   ↓
Tenant
   ↓
Role
   ↓
User
   ↓
Agent
   ↓
Conversation
   ↓
Request
```

A request shall be permitted only when all applicable policies allow execution.

---

## SR-005 — Multiple Rate-Limiting Algorithms

The system shall support:

* Token Bucket
* Leaky Bucket
* Fixed Window
* Sliding Window
* Sliding Window Counter
* Concurrency Limiting
* Token-Based Limiting
* Cost-Based Limiting
* Adaptive Limiting

---

## SR-006 — Token Bucket Support

Token Bucket shall be supported for burst-aware traffic.

The implementation shall support:

* Capacity
* Refill rate
* Current tokens
* Consumption
* Burst capacity
* Expiration

---

## SR-007 — Sliding Window Support

Sliding-window policies shall support accurate request-rate enforcement without excessive boundary spikes.

---

## SR-008 — Concurrency Limiting

The system shall limit simultaneous model executions.

Concurrency shall be configurable per:

* Platform
* Provider
* Model
* Tenant
* User
* Agent
* Workflow

---

## SR-009 — Token-Based Limiting

The system shall track:

* Input tokens
* Output tokens
* Cached tokens
* Reasoning tokens where available
* Total tokens
* Estimated tokens when exact provider data is unavailable

---

## SR-010 — Cost-Aware Limiting

The system shall support limits based on:

* Estimated cost
* Actual provider cost
* Daily budget
* Monthly budget
* Tenant budget
* Agent budget
* Model budget

---

## SR-011 — Provider Quota Awareness

The system shall maintain provider-specific quota configurations.

Provider quota definitions shall support:

```text
requests_per_second
requests_per_minute
requests_per_hour
requests_per_day
tokens_per_second
tokens_per_minute
tokens_per_hour
tokens_per_day
concurrency_limit
burst_limit
cost_limit
```

---

## SR-012 — HTTP Rate-Limit Handling

The system shall correctly process provider responses such as:

```text
HTTP 429
HTTP 408
HTTP 503
HTTP 529
```

where applicable.

---

## SR-013 — Retry-After Support

The system shall respect provider-provided:

```text
Retry-After
```

information whenever available.

---

## SR-014 — Exponential Backoff

Retry mechanisms shall support exponential backoff with:

* Initial delay
* Maximum delay
* Backoff multiplier
* Jitter
* Maximum retries

---

## SR-015 — Retry Storm Prevention

The system shall prevent multiple distributed workers from repeatedly retrying the same throttled operation simultaneously.

---

## SR-016 — Distributed Counter Store

The rate-limit subsystem shall use a low-latency distributed state store.

The implementation may use:

* Redis
* Redis Cluster
* Managed Redis
* Distributed in-memory systems

Counters shall support atomic operations.

---

## SR-017 — Atomicity

Rate-limit counters shall be updated atomically.

Concurrent requests shall not bypass limits because of race conditions.

---

## SR-018 — Low Latency

Rate-limit evaluation should introduce minimal overhead.

Target:

```text
p50 <= 5 ms
p95 <= 15 ms
p99 <= 30 ms
```

excluding external model-provider latency.

---

## SR-019 — Scalability

The system shall support SalesGenie's target architecture of:

* Millions of users
* Large numbers of tenants
* Hundreds of thousands of concurrent conversations
* Large-scale AI-agent execution
* High request throughput
* Multi-region deployments

---

## SR-020 — Clock Consistency

Distributed rate-limit evaluation shall use consistent time semantics.

The system shall avoid relying on local server clock assumptions for critical quota calculations.

---

## SR-021 — Configuration Versioning

Rate-limit policies shall be versioned.

Every policy shall support:

* Policy ID
* Version
* Created timestamp
* Updated timestamp
* Created by
* Updated by
* Effective timestamp
* Expiration timestamp
* Status

---

## SR-022 — Policy Precedence

The system shall define deterministic policy precedence.

Example:

```text
Emergency Global Policy
        >
Provider Policy
        >
Model Policy
        >
Tenant Policy
        >
Role Policy
        >
User Policy
        >
Agent Policy
        >
Conversation Policy
```

---

## SR-023 — Quota Reservation

The system should support quota reservation before expensive model execution.

This shall reduce race conditions where multiple requests consume more resources than the available quota.

---

## SR-024 — Quota Reconciliation

After model execution, the system shall reconcile:

* Reserved tokens
* Actual tokens
* Estimated cost
* Actual cost
* Request duration
* Provider usage

---

## SR-025 — Usage Persistence

Rate-limit events shall be persisted for:

* Auditing
* Analytics
* Billing
* Cost management
* Capacity planning
* Security analysis

---

## SR-026 — Observability

The subsystem shall expose metrics for:

* Requests allowed
* Requests rejected
* Requests throttled
* Requests queued
* Requests retried
* Tokens consumed
* Tokens rejected
* Provider 429s
* Model failures
* Queue depth
* Concurrency
* Limit utilization
* Budget utilization

---

## SR-027 — Auditability

Every administrative rate-limit modification shall generate an audit event.

Audit data shall include:

* Actor
* Tenant
* Policy
* Previous value
* New value
* Timestamp
* Reason
* Source
* IP/device metadata where permitted

---

## SR-028 — Security

Rate-limit configuration APIs shall require authentication and authorization.

Administrative operations shall enforce SalesGenie's RBAC and permission system.

---

## SR-029 — API Protection

All externally exposed AI APIs shall support:

* Authentication
* Authorization
* Rate limiting
* Abuse detection
* Request validation
* Quota enforcement

---

## SR-030 — Idempotency

Rate-limit policy changes shall support idempotent administrative operations where applicable.

---

## SR-031 — Queue Management

When configured, throttled requests shall be placed into controlled queues.

Queues shall support:

* Priority
* FIFO
* Fair scheduling
* Maximum queue depth
* TTL
* Cancellation
* Dead-letter handling

---

## SR-032 — Queue Expiration

Queued AI requests shall expire after configurable TTL values.

Expired requests shall not execute unexpectedly.

---

## SR-033 — Request Cancellation

Users and services shall be able to cancel queued requests.

---

## SR-034 — Provider Failover

When a provider reaches a rate limit, the system may route eligible requests to an alternative provider/model.

---

## SR-035 — Model Failover

When a model reaches its limit, the system may select a compatible fallback model according to model-routing policy.

---

## SR-036 — Semantic Compatibility

Fallback models shall only be selected when they satisfy configured requirements such as:

* Capability
* Context window
* Tool support
* Language support
* Latency requirements
* Cost constraints
* Safety requirements

---

## SR-037 — Human Escalation

If AI execution cannot proceed because of rate limits and the operation is customer-critical, the system shall be capable of escalating to a human support agent.

---

## SR-038 — Human Workload Protection

AI rate limiting shall not create uncontrolled human workload spikes.

When large numbers of AI requests fail simultaneously, human escalation shall be rate-controlled as well.

---

## SR-039 — Configuration Safety

Dangerous configuration changes shall require appropriate permissions and optionally confirmation.

Examples:

* Removing global limits
* Increasing tenant limits dramatically
* Disabling throttling
* Enabling emergency bypass
* Changing provider quotas

---

## SR-040 — Disaster Recovery

Rate-limit configuration and persistent usage data shall be recoverable after service failure.

---

## 5. Functional Requirements

## FR-001 — Create Rate-Limit Policy

The system shall allow authorized administrators to create a rate-limit policy.

Required attributes shall include:

```text
policy_id
policy_name
scope
scope_id
resource_type
algorithm
limit
window
burst_capacity
concurrency_limit
priority
status
effective_at
expires_at
created_by
```

---

## FR-002 — Update Rate-Limit Policy

Authorized users shall be able to modify existing policies.

The system shall preserve the previous policy version.

---

## FR-003 — Delete Rate-Limit Policy

Authorized users shall be able to deactivate policies without necessarily destroying historical records.

---

## FR-004 — Enable / Disable Policy

Policies shall support:

```text
ACTIVE
INACTIVE
SCHEDULED
EXPIRED
EMERGENCY
```

---

## FR-005 — Request Evaluation

Every eligible AI-model request shall pass through rate-limit evaluation before model execution.

The evaluator shall determine:

```text
ALLOW
THROTTLE
QUEUE
RETRY
FALLBACK
REJECT
ESCALATE_HUMAN
```

---

## FR-006 — Hierarchical Evaluation

The evaluator shall calculate all applicable policies before granting execution.

---

## FR-007 — Request Counter

The system shall increment the applicable request counter when a request is accepted.

---

## FR-008 — Token Counter

The system shall track token consumption at the applicable policy scopes.

---

## FR-009 — Concurrency Counter

The system shall reserve and release concurrency slots around model execution.

---

## FR-010 — Quota Reservation

Before execution, the system shall reserve the expected resource consumption where reservation is enabled.

---

## FR-011 — Quota Release

After execution, unused reserved capacity shall be returned.

---

## FR-012 — Usage Reconciliation

The system shall reconcile estimated and actual model usage.

---

## FR-013 — Rate-Limit Response

When a request exceeds a limit, the API shall return a structured response.

Example:

```json
{
  "error": "RATE_LIMITED",
  "message": "Model request rate limit exceeded",
  "scope": "tenant",
  "retry_after_seconds": 12,
  "limit": 100,
  "remaining": 0,
  "reset_at": "2026-08-26T15:00:00Z",
  "request_id": "req_xxx"
}
```

---

## FR-014 — Standard Rate-Limit Headers

The API should expose:

```text
X-RateLimit-Limit
X-RateLimit-Remaining
X-RateLimit-Reset
Retry-After
```

where applicable.

---

## FR-015 — Queue Throttled Requests

If queuing is enabled, requests exceeding temporary capacity shall enter the appropriate priority queue.

---

## FR-016 — Reject Excessive Requests

Requests exceeding hard limits shall be rejected immediately.

---

## FR-017 — Automatic Retry

Transient provider throttling shall trigger retry logic according to policy.

---

## FR-018 — Exponential Backoff

The retry subsystem shall apply exponential backoff and jitter.

---

## FR-019 — Retry Budget

Each request shall have a maximum retry budget.

---

## FR-020 — Provider Rate-Limit Detection

The system shall detect provider-specific throttling signals.

---

## FR-021 — Adaptive Provider Throttling

When provider throttling increases, SalesGenie shall dynamically reduce request concurrency where configured.

---

## FR-022 — Adaptive Recovery

When provider capacity recovers, the system may gradually restore traffic.

Traffic restoration shall avoid sudden request spikes.

---

## FR-023 — Provider Health Scoring

The rate limiter may consume provider health metrics such as:

```text
429 rate
5xx rate
latency
timeout rate
queue depth
capacity utilization
```

---

## FR-024 — Model Health Integration

Model health shall influence model rate allocation.

---

## FR-025 — Tenant Quota Enforcement

Tenant usage shall never exceed configured hard limits.

---

## FR-026 — Tenant Soft Limits

The system shall support warning thresholds before hard quota exhaustion.

Example:

```text
70% — informational
80% — warning
90% — critical warning
100% — hard limit
```

---

## FR-027 — User Quota Enforcement

Individual users shall be constrained by their assigned policies.

---

## FR-028 — Agent Quota Enforcement

Individual AI agents shall be constrained by their assigned policies.

---

## FR-029 — Workflow Quota Enforcement

Automated workflows shall consume and respect configured AI quotas.

---

## FR-030 — Background Job Limits

Background AI tasks shall have independent limits so that they cannot starve interactive customer-facing workloads.

---

## FR-031 — Interactive Priority

Customer-facing conversations shall receive configurable priority over background workloads.

---

## FR-032 — Human Support Priority

Requests required to assist active human support agents shall receive configurable priority.

---

## FR-033 — Critical Operation Priority

Critical enterprise operations shall be able to bypass lower-priority queues without bypassing security or hard safety constraints.

---

## FR-034 — Channel Limits

The system shall apply independent limits to each supported communication channel.

---

## FR-035 — API Client Limits

External API clients shall have independent limits.

---

## FR-036 — IP-Based Protection

The system shall support IP/network-based throttling for abuse protection where appropriate.

---

## FR-037 — Abuse Detection

The system shall identify abnormal request patterns such as:

* Request bursts
* Repeated retries
* Credential abuse
* Agent loops
* Bot traffic
* Token exhaustion attacks
* Endpoint flooding

---

## FR-038 — Agent Loop Protection

The system shall detect repeated AI-agent execution loops.

Examples:

```text
Agent A → Tool → Agent A → Tool → Agent A
```

The system shall terminate or throttle pathological loops.

---

## FR-039 — Tool-Call Limiting

AI agents shall have configurable limits for external tool invocations.

---

## FR-040 — Recursive Agent Limiting

The system shall restrict recursive or nested agent execution.

---

## FR-041 — Conversation-Level Limiting

A conversation shall have configurable AI request and token limits.

---

## FR-042 — Session-Level Limiting

A session shall have configurable AI usage limits.

---

## FR-043 — Cost-Based Enforcement

Requests shall be blocked, queued, or rerouted when configured cost thresholds are exceeded.

---

## FR-044 — Budget Forecasting

The system may estimate whether continued traffic will exhaust a budget before the billing period ends.

---

## FR-045 — Cost-Aware Throttling

The system may reduce expensive-model usage when budget utilization reaches configurable thresholds.

---

## FR-046 — Low-Cost Fallback

When configured, expensive models may fall back to lower-cost compatible models.

---

## FR-047 — High-Quality Fallback

For critical workloads, the system shall prioritize quality requirements over cost limits when authorized.

---

## FR-048 — Human Fallback

When AI execution is unavailable because of rate limits, the system shall support routing to human agents for eligible interactions.

---

## FR-049 — AI-to-Human Escalation

The system shall provide the human agent with relevant context when escalation occurs.

Context may include:

* Conversation
* Customer information
* AI reasoning metadata permitted by policy
* Failed request
* Rate-limit reason
* Model/provider
* Previous attempts
* Retrieved knowledge
* Agent state

---

## FR-050 — Human-to-AI Resume

After a human resolves an interaction, authorized workflows may resume AI assistance subject to current limits.

---

## FR-051 — Administrative Dashboard

The system shall provide a rate-limit management dashboard.

The dashboard shall display:

```text
Requests / second
Requests / minute
Requests / hour
Requests / day

Tokens / second
Tokens / minute
Tokens / hour
Tokens / day

Concurrent requests
Queued requests
Rejected requests
Throttled requests

Provider utilization
Model utilization
Tenant utilization
Budget utilization
```

---

## FR-052 — Real-Time Utilization

Authorized administrators shall be able to view near-real-time quota utilization.

---

## FR-053 — Historical Analytics

The system shall provide historical rate-limit analytics.

Users shall be able to analyze:

* Usage trends
* Peak periods
* Limit violations
* Provider throttling
* Model saturation
* Tenant consumption
* Agent consumption
* Cost impact

---

## FR-054 — Rate-Limit Audit Logs

Every rate-limit decision may be recorded with:

```text
request_id
tenant_id
user_id
agent_id
provider
model
scope
policy_id
decision
limit
remaining
retry_after
tokens
estimated_cost
actual_cost
timestamp
```

---

## FR-055 — Policy Simulation

Administrators should be able to simulate rate-limit policies against historical traffic before activating them.

---

## FR-056 — Policy Dry Run

The system shall support a dry-run mode where rate-limit policies generate recommendations without enforcing them.

---

## FR-057 — Scheduled Policies

Administrators shall be able to schedule policies.

Examples:

```text
Business hours
Peak hours
Maintenance windows
Campaign periods
Product launches
Promotional campaigns
Enterprise events
```

---

## FR-058 — Temporary Overrides

Administrators shall be able to create temporary overrides with:

```text
start_time
end_time
scope
limit
reason
approved_by
```

---

## FR-059 — Approval Workflow

High-risk rate-limit changes shall optionally require approval from an authorized administrator.

---

## FR-060 — Automatic Policy Rollback

The system shall support automatic rollback of temporary policies after expiration.

---

## FR-061 — Rate-Limit Alerts

The system shall generate alerts for:

* 80% utilization
* 90% utilization
* 100% utilization
* Repeated 429 responses
* Abnormal request bursts
* Agent loops
* Budget exhaustion
* Provider degradation

Thresholds shall be configurable.

---

## FR-062 — Notification Channels

Alerts may be delivered through:

* In-app notifications
* Email
* Slack
* Microsoft Teams
* Webhooks
* Incident-management integrations

---

## FR-063 — Rate-Limit Event Webhooks

The system shall provide webhook events for important rate-limit transitions.

Examples:

```text
rate_limit.warning
rate_limit.throttled
rate_limit.rejected
rate_limit.exhausted
rate_limit.recovered
provider.rate_limited
model.rate_limited
tenant.quota_exhausted
```

---

## FR-064 — Event-Driven Integration

Rate-limit events shall be publishable through SalesGenie's event-driven architecture.

---

## FR-065 — Billing Integration

The subsystem shall provide usage information to the billing system.

Billing integration shall support:

* Requests
* Tokens
* Model usage
* Provider usage
* AI cost
* Tenant consumption
* Quota utilization

---

## FR-066 — Usage Tracking Integration

The rate limiter shall integrate with model usage tracking.

---

## FR-067 — Model Routing Integration

The rate limiter shall provide routing signals to the model-routing subsystem.

---

## FR-068 — Model Selection Integration

Model selection shall consider current:

* Rate-limit status
* Provider capacity
* Quota
* Cost
* Concurrency
* Availability

---

## FR-069 — LLM Gateway Integration

All model requests passing through the SalesGenie LLM Gateway shall be eligible for rate-limit enforcement.

---

## FR-070 — RAG Integration

RAG-related model requests shall respect the same quota hierarchy.

---

## FR-071 — Voice AI Integration

Voice AI model requests shall support dedicated concurrency and throughput limits.

---

## FR-072 — Batch Processing Limits

Batch operations shall have separate limits from interactive requests.

---

## FR-073 — Scheduled Job Limits

Scheduled AI reports and background AI jobs shall consume configurable quotas.

---

## FR-074 — Graceful Queue Backpressure

When downstream model capacity decreases, upstream services shall receive backpressure signals.

---

## FR-075 — Circuit Breaker Integration

Repeated provider throttling may activate a circuit breaker.

Circuit-breaker states:

```text
CLOSED
OPEN
HALF_OPEN
```

---

## FR-076 — Recovery Testing

The system shall periodically verify whether throttled providers/models have recovered.

---

## FR-077 — Fallback Chain

Administrators shall be able to configure fallback chains.

Example:

```text
Primary Model
    ↓
Secondary Model
    ↓
Low-Cost Model
    ↓
Human Agent
```

---

## FR-078 — Fallback Constraints

Fallback shall respect:

* Tenant permissions
* Model permissions
* Data residency
* Provider availability
* Cost policies
* Security policies
* Model capability requirements
* Compliance rules

---

## FR-079 — Rate-Limit Reason Codes

Every rejected or throttled request shall provide a machine-readable reason.

Examples:

```text
TENANT_RPM_EXCEEDED
TENANT_TPM_EXCEEDED
USER_LIMIT_EXCEEDED
AGENT_LIMIT_EXCEEDED
MODEL_RPM_EXCEEDED
MODEL_TPM_EXCEEDED
PROVIDER_QUOTA_EXCEEDED
CONCURRENCY_LIMIT_EXCEEDED
COST_LIMIT_EXCEEDED
GLOBAL_LIMIT_EXCEEDED
ABUSE_DETECTED
QUEUE_FULL
```

---

## FR-080 — Client-Friendly Errors

Frontend and API clients shall receive actionable error information.

The UI should communicate:

* Why the request was limited
* Estimated wait time
* Retry time
* Remaining quota
* Alternative action where applicable

---

## FR-081 — Super Admin Controls

Super Admins shall be able to:

* View all tenants
* View all rate-limit policies
* View all providers
* View all models
* View quota consumption
* Override policies
* Suspend model traffic
* Suspend provider traffic
* Configure emergency policies

---

## FR-082 — Organization Admin Controls

Organization Admins shall only manage policies within their authorized organization.

---

## FR-083 — Support Manager Controls

Support managers shall be able to view and configure AI usage limits relevant to support teams.

---

## FR-084 — Support Agent Experience

Human support agents shall receive clear feedback when AI assistance is throttled.

The system shall avoid exposing unnecessary infrastructure details.

---

## FR-085 — AI Agent Experience

AI agents shall receive structured rate-limit signals so that they can:

* Wait
* Retry
* Select another model
* Reduce workload
* Escalate
* Stop execution

---

## FR-086 — Agent-Aware Backoff

AI agents shall support server-provided retry recommendations.

---

## FR-087 — Context Preservation

Rate limiting shall not unnecessarily destroy conversation or agent state.

---

## FR-088 — Request Idempotency

Retries shall preserve idempotency where supported to prevent duplicate side effects.

---

## FR-089 — Duplicate Request Prevention

The system shall prevent accidental duplicate model execution caused by retries or network failures where technically feasible.

---

## FR-090 — Rate-Limit Testing

The subsystem shall support automated tests for:

* Single-node limits
* Distributed limits
* Burst traffic
* Concurrent requests
* Provider 429s
* Retry storms
* Queue overflow
* Tenant isolation
* Policy precedence
* Fallback
* Emergency overrides
* Recovery

---

## 6. AI-Based Requirements

## AI-FR-001 — Adaptive Rate Prediction

The system may use AI/ML to predict future model demand based on:

* Historical traffic
* Time of day
* Day of week
* Campaign activity
* Customer volume
* Scheduled jobs
* Agent activity
* Provider behavior

---

## AI-FR-002 — Predictive Throttling

The AI subsystem may proactively reduce traffic before expected quota exhaustion.

---

## AI-FR-003 — Intelligent Model Selection

AI-based routing may select a model based on:

```text
quality
latency
cost
availability
quota
rate-limit state
context requirements
task complexity
```

---

## AI-FR-004 — Anomaly Detection

The system may detect abnormal usage patterns using machine-learning techniques.

---

## AI-FR-005 — Agent Loop Detection

AI models may identify pathological agent execution patterns.

---

## AI-FR-006 — Capacity Forecasting

The system may predict:

* Provider saturation
* Tenant quota exhaustion
* Model saturation
* Budget exhaustion

---

## AI-FR-007 — Intelligent Queue Prioritization

AI may estimate request urgency using signals such as:

* Customer priority
* SLA
* Conversation type
* Revenue impact
* Support severity
* Enterprise tier

AI decisions must remain subject to deterministic policy boundaries.

---

## AI-FR-008 — Intelligent Retry Decision

AI may recommend whether to:

* Retry
* Wait
* Switch provider
* Switch model
* Escalate to human
* Reject

---

## AI-FR-009 — AI Safety Boundary

AI-generated rate-limit decisions shall never override:

* Hard security policies
* Compliance restrictions
* Explicit administrative blocks
* Absolute provider limits
* Tenant isolation
* Legal requirements

---

## 7. Human-Control Requirements

## HR-001 — Human Policy Configuration

Administrators shall have complete control over deterministic rate-limit policies.

---

## HR-002 — Human Approval

High-impact changes shall optionally require human approval.

---

## HR-003 — Human Override

Authorized administrators shall be able to override AI-generated recommendations.

---

## HR-004 — Human Auditability

All manual decisions shall be auditable.

---

## HR-005 — Human Emergency Control

Human administrators shall always retain emergency control over AI traffic.

---

## HR-006 — Explainability

The administrative interface shall explain why a request was:

* Allowed
* Throttled
* Queued
* Rejected
* Retried
* Rerouted
* Escalated

---

## 8. Non-Functional Requirements

## NFR-001 — Availability

The subsystem should target:

```text
99.99% availability
```

for production deployments.

---

## NFR-002 — Performance

Rate-limit evaluation should remain low latency under normal and peak traffic.

---

## NFR-003 — Scalability

The architecture shall horizontally scale across:

* API instances
* Workers
* Redis nodes
* Regions
* Tenants
* Providers
* Models

---

## NFR-004 — Reliability

Rate-limit decisions shall remain deterministic and consistent under concurrent load.

---

## NFR-005 — Security

Rate-limit configuration and usage data shall be protected using SalesGenie's authentication, RBAC, encryption, and tenant-isolation mechanisms.

---

## NFR-006 — Observability

The subsystem shall expose:

* Metrics
* Logs
* Traces
* Alerts
* Audit events

---

## NFR-007 — Maintainability

Policies shall be configurable without requiring application redeployment.

---

## NFR-008 — Extensibility

The system shall support new:

* Providers
* Models
* Channels
* Agents
* Workflows
* Rate-limit algorithms
* Pricing models

without redesigning the core subsystem.

---

## NFR-009 — Fault Isolation

Failure of one provider, model, tenant, or agent shall not cause uncontrolled failure across the platform.

---

## NFR-010 — Compliance

Rate-limit data and administrative actions shall comply with applicable organizational security and data-governance requirements.

---

## 9. Core Rate-Limit Decision Model

```text
Incoming AI Request
        |
        v
Authentication
        |
        v
Authorization
        |
        v
Request Classification
        |
        v
Identify Tenant / User / Agent / Channel
        |
        v
Identify Provider / Model
        |
        v
Load Applicable Policies
        |
        v
Check Global Limits
        |
        v
Check Provider Limits
        |
        v
Check Model Limits
        |
        v
Check Tenant Limits
        |
        v
Check User Limits
        |
        v
Check Agent Limits
        |
        v
Check Conversation Limits
        |
        v
Check Token Budget
        |
        v
Check Cost Budget
        |
        v
Check Concurrency
        |
        v
Check Abuse / Agent Loop
        |
        v
+-----------------------------+
| Rate-Limit Decision Engine  |
+-----------------------------+
        |
        +------> ALLOW
        |
        +------> QUEUE
        |
        +------> RETRY
        |
        +------> FALLBACK MODEL
        |
        +------> FALLBACK PROVIDER
        |
        +------> HUMAN HANDOFF
        |
        +------> REJECT
```

## 10. Rate-Limit Policy Object

```json
{
  "policy_id": "rlp_xxxxx",
  "name": "Enterprise Support AI Policy",
  "scope": {
    "type": "tenant",
    "id": "tenant_xxxxx"
  },
  "resource": {
    "type": "llm_request",
    "provider": "provider_x",
    "model": "model_x"
  },
  "algorithm": "token_bucket",
  "limits": {
    "requests_per_second": 20,
    "requests_per_minute": 500,
    "tokens_per_minute": 100000,
    "concurrency": 50
  },
  "burst": {
    "enabled": true,
    "capacity": 100,
    "duration_seconds": 30
  },
  "behavior": {
    "on_limit": "queue",
    "retry": true,
    "fallback": true,
    "human_handoff": true
  },
  "priority": 1,
  "status": "active"
}
```

## 11. Rate-Limit Decision Object

```json
{
  "request_id": "req_xxxxx",
  "decision": "THROTTLE",
  "reason_code": "MODEL_TPM_EXCEEDED",
  "scope": "model",
  "policy_id": "rlp_xxxxx",
  "limit": 100000,
  "remaining": 0,
  "retry_after_seconds": 14,
  "queue_allowed": true,
  "fallback_allowed": true,
  "human_handoff_allowed": true
}
```

## 12. Acceptance Criteria

The implementation shall be considered production-ready when:

* [ ] Global model rate limits are enforceable.
* [ ] Provider-specific rate limits are enforceable.
* [ ] Tenant-specific rate limits are enforceable.
* [ ] User-specific rate limits are enforceable.
* [ ] AI-agent limits are enforceable.
* [ ] Token limits are enforced.
* [ ] Cost limits are enforced.
* [ ] Concurrency limits are enforced.
* [ ] Burst traffic is controlled.
* [ ] Distributed counters are atomic.
* [ ] Provider 429 responses are handled.
* [ ] Retry-After is respected.
* [ ] Exponential backoff is implemented.
* [ ] Retry storms are prevented.
* [ ] Requests can be queued.
* [ ] Queue expiration is supported.
* [ ] Provider fallback is supported.
* [ ] Model fallback is supported.
* [ ] Human escalation is supported.
* [ ] Human administrators can override policies.
* [ ] AI recommendations cannot override hard security policies.
* [ ] Rate-limit policies are versioned.
* [ ] Administrative changes are audited.
* [ ] Usage is integrated with billing.
* [ ] Usage is integrated with model usage tracking.
* [ ] Usage is integrated with model routing.
* [ ] Real-time utilization is available.
* [ ] Historical rate-limit analytics are available.
* [ ] Abuse detection is supported.
* [ ] Agent-loop protection is supported.
* [ ] Background workloads cannot starve interactive workloads.
* [ ] Multi-tenant isolation is verified.
* [ ] Failure isolation is verified.
* [ ] Load testing validates distributed enforcement.
* [ ] Recovery behavior is tested.
* [ ] Emergency throttling is available.
* [ ] The system supports horizontal scaling.
* [ ] APIs expose actionable rate-limit responses.
* [ ] Super Admin controls are implemented.
* [ ] Organization Admin controls are implemented.
* [ ] Support Manager controls are implemented.
* [ ] Human support agents receive understandable AI-throttling feedback.
* [ ] AI agents receive machine-readable throttling signals.
