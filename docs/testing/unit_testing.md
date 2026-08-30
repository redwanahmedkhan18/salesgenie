# SalesGenie — Unit Testing Requirements

**Document:** `unit_testing.md`  
**Product:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Requirement Scope:** User Requirements, System Requirements, Functional Requirements  
**Testing Model:** Human + AI-Assisted + AI-Driven Unit Testing  
**Architecture:** Enterprise Microservices + Multi-Agent AI + Event-Driven Architecture  
**Target Scale:** 10M+ users, 500K concurrent conversations  
**Priority:** Critical

---

## 1. Purpose

The SalesGenie Unit Testing subsystem shall provide a deterministic, isolated, repeatable, automated, and AI-assisted framework for validating individual software units before they are integrated with other components.

Unit testing shall cover:

- Frontend components.
- Backend functions.
- Classes.
- Services.
- Controllers.
- API handlers.
- Domain logic.
- Business rules.
- Database repositories through mocks/fakes.
- Cache abstractions.
- Queue producers/consumers through mocks.
- Event handlers.
- Webhook handlers.
- Authentication logic.
- Authorization logic.
- Billing logic.
- Lead intelligence logic.
- Search logic.
- RAG components.
- AI agents.
- Prompt-processing utilities.
- Tool-selection logic.
- Workflow components.
- Data transformation.
- Validation.
- Error handling.
- Security-sensitive code.

Unit tests shall not replace integration, contract, E2E, performance, security, AI evaluation, or chaos testing.

---

## 2. Core Objectives

The unit testing system shall ensure:

1. Individual units behave according to their contracts.
2. Business rules are explicitly validated.
3. Edge cases are covered.
4. Failure paths are tested.
5. Security-sensitive logic is tested.
6. Regression defects are permanently protected where appropriate.
7. Tests execute quickly enough for continuous developer feedback.
8. Tests are deterministic and reproducible.
9. Tests can run locally and in CI/CD.
10. AI-generated tests are reviewed and governed.
11. Test coverage reflects meaningful behavior rather than only line count.
12. Unit tests remain isolated from external infrastructure.
13. Tests provide actionable failure diagnostics.
14. Critical code cannot be merged while mandatory unit tests fail.

---

## 3. Testing Philosophy

SalesGenie shall follow:

```text
Fast
↓
Isolated
↓
Deterministic
↓
Repeatable
↓
Meaningful
↓
Automated
↓
Continuously Executed
```

The preferred testing order shall be:

```text
Unit Test
    ↓
Component Test
    ↓
Integration Test
    ↓
Contract Test
    ↓
End-to-End Test
```

The system shall maximize validation at the unit level before expensive distributed testing.

---

## 4. Actors

## 4.1 Human Actors

### HR-001 — Developer

The developer shall:

* Create unit tests.
* Run unit tests locally.
* Inspect failures.
* Fix defects.
* Review AI-generated tests.
* Approve test changes.

### HR-002 — QA Engineer

The QA engineer shall:

* Define unit-test standards.
* Review critical test coverage.
* Validate edge cases.
* Audit test quality.
* Maintain regression requirements.

### HR-003 — SDET

The SDET shall:

* Maintain testing infrastructure.
* Build reusable test utilities.
* Improve test execution performance.
* Maintain CI/CD test integration.

### HR-004 — AI/ML Engineer

The AI/ML engineer shall:

* Test AI-specific deterministic components.
* Maintain evaluation fixtures.
* Test preprocessing and postprocessing.
* Test agent logic.
* Test tool routing.
* Test safety logic.

### HR-005 — Security Engineer

The security engineer shall define unit tests for security-critical logic.

### HR-006 — Release Engineer

The release engineer shall enforce unit-test quality gates.

---

## 5. AI Actors

### AI-001 — Unit Test Generator

The AI agent shall generate candidate unit tests from:

* Source code.
* Function signatures.
* Type definitions.
* Docstrings.
* Requirements.
* User stories.
* API contracts.
* Existing tests.
* Historical bugs.

### AI-002 — Unit Test Reviewer

The AI agent shall analyze tests for:

* Missing edge cases.
* Weak assertions.
* Duplicate coverage.
* Over-mocking.
* Brittle assumptions.
* Missing negative cases.

### AI-003 — Test Mutation Analyzer

The AI agent shall identify whether tests detect intentional mutations.

### AI-004 — Failure Diagnosis Agent

The AI agent shall analyze failed unit tests and produce probable root causes.

### AI-005 — Regression Test Agent

The AI agent shall identify production defects that should become unit-test regression cases.

### AI-006 — Test Optimization Agent

The AI agent shall identify:

* Slow tests.
* Redundant tests.
* Duplicate fixtures.
* Expensive setup.
* Poor test isolation.

---

## 6. User Requirements

## UR-001 — Create Unit Tests

Developers shall be able to create unit tests for any supported application component.

---

## UR-002 — Run Individual Tests

Developers shall be able to run a single test without executing the complete test suite.

---

## UR-003 — Run Test Modules

Developers shall be able to run:

```text
Single Test
Single File
Single Module
Single Service
Entire Unit Suite
```

---

## UR-004 — Local Execution

Developers shall be able to execute unit tests locally before committing code.

---

## UR-005 — CI Execution

Every relevant code change shall trigger appropriate unit tests through CI/CD.

---

## UR-006 — Test Results

Authorized users shall be able to view:

* Passed tests.
* Failed tests.
* Skipped tests.
* Duration.
* Failure reason.
* Stack trace.
* Coverage.
* Commit.
* Branch.
* Environment.

---

## UR-007 — Test Search

Users shall be able to search tests by:

* Test ID.
* Service.
* Module.
* Function.
* Feature.
* Requirement.
* Tag.
* Owner.
* Failure status.

---

## UR-008 — Test Filtering

Users shall be able to filter tests by:

```text
PASS
FAIL
SKIPPED
FLAKY
QUARANTINED
SLOW
SECURITY
CRITICAL
REGRESSION
AI
```

---

## 7. Test Case Structure

Every production-grade unit test shall contain enough information to explain:

```yaml
test_id:
title:
purpose:
unit_under_test:
preconditions:
fixtures:
input:
expected_output:
expected_side_effects:
mocked_dependencies:
assertions:
category:
priority:
severity:
owner:
requirements:
```

---

## 8. Test Naming Requirements

## SR-001

Test names shall clearly communicate:

```text
Given
When
Then
```

Example pattern:

```text
test_should_reject_expired_jwt_when_expiration_is_in_the_past
```

Names shall describe behavior rather than implementation details.

---

## 9. Test Isolation

## SR-002

A unit test shall test one logical unit of behavior.

A unit test shall not depend on:

* Production database.
* Production Redis.
* External API.
* Real LLM provider.
* Real payment provider.
* Real email provider.
* Real CRM.
* Real filesystem unless explicitly abstracted.
* Network availability.

---

## 10. Dependency Isolation

External dependencies shall be replaced with:

```text
Mock
Stub
Fake
Spy
In-Memory Implementation
Test Double
```

where appropriate.

---

## 11. Determinism

## SR-003

Unit tests shall produce the same result for the same:

```text
Code Version
Input
Configuration
Fixture
Dependency Behavior
```

---

## 12. Randomness Control

## SR-004

Tests involving randomness shall use controlled seeds.

Randomized tests shall record the seed when failures occur.

---

## 13. Time Control

## SR-005

Time-dependent code shall use injectable clocks or equivalent abstractions.

Tests shall support deterministic validation of:

* Token expiration.
* TTL.
* Subscription periods.
* Retry delays.
* Scheduling.
* Timestamps.

---

## 14. Network Isolation

## SR-006

Unit tests shall not require network access.

Unexpected external network calls shall fail the test.

---

## 15. Database Isolation

## SR-007

Database-dependent logic shall be tested at the unit level through repositories, mocks, fakes, or deterministic in-memory abstractions.

Actual database behavior shall be validated separately through integration tests.

---

## 16. Redis Isolation

## SR-008

Redis-dependent units shall use mocks/fakes for unit testing.

Actual Redis behavior shall be validated through integration tests.

---

## 17. Queue Isolation

## SR-009

Queue producers and consumers shall use mocked or in-memory queue abstractions during unit testing.

---

## 18. Event Isolation

## SR-010

Event handlers shall be tested with deterministic event fixtures.

Tests shall validate:

* Valid event.
* Invalid event.
* Missing fields.
* Unknown event type.
* Duplicate event.
* Malformed payload.

---

## 19. Error Handling

## SR-011

Every critical unit shall test expected failure paths.

Examples:

```text
Invalid Input
Null Input
Missing Field
Invalid Type
Unauthorized
Forbidden
Not Found
Conflict
Timeout
Dependency Error
Malformed Response
Unexpected Exception
```

---

## 20. Boundary Testing

## SR-012

Tests shall cover:

```text
Minimum Value
Minimum - 1
Minimum + 1
Maximum - 1
Maximum
Maximum + 1
Empty
Null
Missing
Very Large
Very Small
```

where applicable.

---

## 21. Validation Testing

## FR-001

Input validators shall be tested against:

* Valid inputs.
* Invalid inputs.
* Boundary values.
* Unicode.
* Special characters.
* Whitespace.
* Malformed formats.
* Oversized values.

---

## 22. Business Logic Testing

## FR-002

Every critical business rule shall have explicit unit-test coverage.

Examples:

```text
Lead Scoring
Subscription Limits
Usage Enforcement
Role Permissions
Conversation Routing
AI Escalation
Billing Entitlements
Workflow Conditions
Search Permissions
```

---

## 23. Authentication Unit Testing

## FR-003

Authentication components shall have tests for:

```text
Valid Login
Invalid Password
Unknown User
Expired Token
Malformed Token
Invalid Signature
Wrong Issuer
Wrong Audience
Missing Claims
Missing Subject
Refresh Token
Logout
Session Expiration
```

---

## 24. JWT Testing

## FR-004

JWT validation shall test:

```text
exp
iat
iss
aud
sub
signature
algorithm
token structure
```

The system shall explicitly validate seconds-vs-milliseconds handling for timestamps.

---

## 25. Authorization Testing

## FR-005

Authorization units shall test:

```text
User + Role + Permission + Resource + Action
```

Examples:

```text
Admin can manage users
Sales Agent can access assigned leads
Support Agent can access support conversations
Developer can access developer resources
End User cannot access admin resources
Tenant A cannot access Tenant B resources
```

---

## 26. RBAC Testing

## FR-006

Every privileged role shall have positive and negative authorization tests.

---

## 27. Tenant Isolation Testing

## FR-007

Tenant-aware functions shall test that:

```text
Tenant A Request
        ↓
Tenant A Resource = ALLOWED
Tenant B Resource = DENIED
```

Cross-tenant access shall be treated as a critical security failure.

---

## 28. API Handler Unit Testing

## FR-008

API handlers shall test:

* Request parsing.
* Validation.
* Authentication.
* Authorization.
* Business logic invocation.
* Response transformation.
* Error mapping.
* Status codes.

---

## 29. Serialization Testing

## FR-009

Serializers shall be tested for:

* Required fields.
* Optional fields.
* Type conversion.
* Null handling.
* Nested structures.
* Invalid data.

---

## 30. Pagination Testing

## FR-010

Pagination logic shall test:

```text
First Page
Middle Page
Last Page
Empty Page
Invalid Page
Invalid Page Size
Maximum Page Size
```

---

## 31. Filtering Testing

## FR-011

Filtering logic shall test:

* Single filter.
* Multiple filters.
* Empty filters.
* Invalid filters.
* Conflicting filters.
* Unauthorized filters.

---

## 32. Sorting Testing

## FR-012

Sorting logic shall test:

* Ascending.
* Descending.
* Multiple fields.
* Null values.
* Duplicate values.
* Invalid fields.

---

## 33. Lead Intelligence Unit Testing

## FR-013

Lead intelligence components shall test:

```text
Lead Scoring
Company Classification
Lead Qualification
Lead Enrichment
Deduplication
Ranking
Filtering
Search
Data Normalization
```

---

## 34. Search Unit Testing

## FR-014

Search-related units shall test:

* Query normalization.
* Tokenization.
* Filters.
* Ranking calculations.
* Permission filtering.
* Pagination.
* Empty results.
* Invalid queries.

---

## 35. Ranking Unit Testing

## FR-015

Ranking algorithms shall test:

* Correct score calculation.
* Tie handling.
* Missing features.
* Invalid scores.
* Boundary scores.
* Stable ordering.

---

## 36. RAG Unit Testing

## FR-016

RAG components shall be unit-tested independently.

Components include:

```text
Text Cleaner
Chunker
Metadata Extractor
Embedding Adapter
Retriever Adapter
Reranker
Context Builder
Citation Builder
Prompt Builder
Response Parser
```

---

## 37. Chunking Tests

## FR-017

Chunking logic shall test:

* Empty document.
* Short document.
* Exact chunk boundary.
* Oversized document.
* Unicode.
* Tables.
* Repeated text.
* Metadata preservation.

---

## 38. Retrieval Tests

## FR-018

Retrieval adapters shall test:

* Correct query transformation.
* Result parsing.
* Empty results.
* Duplicate results.
* Invalid results.
* Ranking metadata.
* Permission metadata.

Actual vector database behavior shall be validated separately.

---

## 39. Prompt Builder Testing

## FR-019

Prompt-building components shall test:

* Required instructions.
* Context insertion.
* Variable substitution.
* Missing variables.
* Escaping.
* Length constraints.
* Injection-resistant handling.

---

## 40. LLM Adapter Unit Testing

## FR-020

LLM adapters shall be tested using mocked provider responses.

Tests shall cover:

```text
Successful Response
Malformed Response
Empty Response
Timeout
Rate Limit
Provider Error
Invalid JSON
Unexpected Schema
Token Usage
```

Actual model quality shall be tested through AI evaluation suites rather than conventional unit tests.

---

## 41. AI Agent Unit Testing

## FR-021

Deterministic agent components shall be unit-tested.

Examples:

```text
State Transition
Goal Validation
Tool Selection Rules
Permission Validation
Action Validation
Retry Policy
Termination Condition
Escalation Condition
```

---

## 42. Agent State Testing

## FR-022

Agent state machines shall test:

```text
INITIAL
PLANNING
EXECUTING
WAITING
ESCALATED
COMPLETED
FAILED
CANCELLED
```

Invalid transitions shall be rejected.

---

## 43. Tool Selection Testing

## FR-023

Tool routing logic shall test:

```text
Correct Tool
Incorrect Tool
No Tool
Multiple Tools
Unauthorized Tool
Malformed Parameters
Missing Parameters
```

---

## 44. Tool Authorization Testing

## FR-024

The tool authorization layer shall prevent unauthorized tools from being executed.

Tests shall explicitly verify denied actions.

---

## 45. Tool Parameter Testing

## FR-025

Tool parameter validators shall test:

* Required parameters.
* Optional parameters.
* Wrong types.
* Missing parameters.
* Extra parameters.
* Malformed values.
* Boundary values.

---

## 46. Multi-Agent Unit Testing

## FR-026

Multi-agent orchestration units shall test:

* Agent selection.
* Agent delegation.
* Task routing.
* State transitions.
* Failure handling.
* Conflict resolution.
* Termination conditions.

Actual distributed communication shall be tested separately.

---

## 47. Human Handoff Testing

## FR-027

Escalation logic shall test:

```text
AI Handles
AI Escalates
Human Accepts
Human Rejects
No Human Available
Escalation Timeout
Escalation Cancellation
```

---

## 48. Workflow Unit Testing

## FR-028

Workflow nodes shall be independently tested.

Examples:

```text
Trigger
Condition
Transform
HTTP Request
AI Node
CRM Node
Notification
Delay
Retry
Branch
Merge
```

---

## 49. Workflow Condition Testing

## FR-029

Workflow conditions shall test:

* True.
* False.
* Null.
* Missing values.
* Invalid types.
* Nested conditions.
* AND.
* OR.
* NOT.

---

## 50. Webhook Unit Testing

## FR-030

Webhook handlers shall test:

```text
Valid Signature
Invalid Signature
Missing Signature
Valid Payload
Malformed Payload
Duplicate Event
Unknown Event
Replay Attempt
```

---

## 51. Event Handler Testing

## FR-031

Event handlers shall test:

* Valid events.
* Invalid events.
* Idempotency.
* Retry logic.
* Error mapping.
* Event version compatibility.

---

## 52. Queue Producer Testing

## FR-032

Queue producers shall test:

* Correct topic/queue.
* Correct payload.
* Required metadata.
* Correlation ID.
* Idempotency key.
* Serialization errors.

---

## 53. Queue Consumer Testing

## FR-033

Queue consumers shall test:

* Valid message.
* Invalid message.
* Duplicate message.
* Processing failure.
* Retry.
* Dead-letter routing.

---

## 54. Billing Unit Testing

## FR-034

Billing logic shall test:

```text
Plan Creation
Subscription Creation
Upgrade
Downgrade
Cancellation
Renewal
Usage Limit
Overage
Invoice
Payment Failure
Entitlement
```

---

## 55. Usage Calculation Testing

## FR-035

Usage calculations shall test:

* Zero usage.
* Normal usage.
* Boundary usage.
* Limit reached.
* Limit exceeded.
* Duplicate usage events.
* Concurrent usage updates.

---

## 56. Cache Logic Testing

## FR-036

Cache abstractions shall test:

```text
Cache Hit
Cache Miss
Expired Entry
Invalidation
Stale Entry
Serialization Failure
Cache Failure
Fallback
```

---

## 57. Configuration Testing

## FR-037

Configuration loading shall test:

* Valid configuration.
* Missing configuration.
* Invalid configuration.
* Default values.
* Environment overrides.
* Secret references.

Secrets shall never be asserted directly in logs or test output.

---

## 58. Feature Flag Testing

## FR-038

Feature flag logic shall test:

```text
Enabled
Disabled
Unknown
Tenant Override
User Override
Environment Override
Expired Flag
```

---

## 59. Internationalization Testing

## FR-039

Localization utilities shall test:

* Language selection.
* Missing translations.
* Fallback language.
* Parameter interpolation.
* Date formatting.
* Number formatting.
* Currency formatting.

---

## 60. Error Model Testing

## FR-040

Every service shall have standardized tests for error transformation.

Internal exceptions shall map to appropriate domain/API errors.

---

## 61. Logging Unit Testing

## FR-041

Critical logging utilities shall test:

* Required fields.
* Correlation IDs.
* Request IDs.
* User/tenant identifiers where permitted.
* Severity.
* Secret redaction.

---

## 62. Metrics Unit Testing

## FR-042

Metric instrumentation shall test:

* Correct metric name.
* Correct labels.
* Counter increments.
* Histogram observations.
* Error counters.
* Avoidance of high-cardinality labels.

---

## 63. Distributed Trace Unit Testing

## FR-043

Tracing utilities shall test:

* Trace ID propagation.
* Span creation.
* Parent-child relationships.
* Context propagation.
* Error tagging.

---

## 64. Data Transformation Testing

## FR-044

Transformation functions shall test:

```text
Input Schema
↓
Normalization
↓
Transformation
↓
Output Schema
```

Invalid input shall fail predictably.

---

## 65. PII Protection Testing

## FR-045

Redaction utilities shall test removal or masking of sensitive information from:

* Logs.
* Errors.
* Debug output.
* Test artifacts.

---

## 66. Security-Sensitive Unit Testing

## FR-046

Security-critical utilities shall have mandatory unit tests for:

* Authentication.
* Authorization.
* Encryption helpers.
* Signature validation.
* Input validation.
* Secret redaction.
* Tenant isolation.
* Permission checks.

---

## 67. Injection Testing

## FR-047

Security-related units shall test malicious inputs including:

```text
SQL Injection Payloads
XSS Payloads
Command Injection
Path Traversal
Header Injection
Prompt Injection
Template Injection
Malformed JSON
```

---

## 68. AI-Assisted Test Generation

## FR-048

AI shall analyze source code and generate candidate unit tests.

The generated tests shall include:

```text
Happy Path
Negative Path
Boundary Case
Null Case
Exception Case
Security Case
Regression Case
```

where relevant.

---

## 69. AI Test Generation Constraints

## SR-013

AI-generated tests shall not:

* Introduce production credentials.
* Call production systems.
* Disable security controls.
* Remove mandatory tests.
* Modify production data.
* Bypass approval policies.

---

## 70. AI Test Review

## FR-049

AI shall evaluate generated tests for:

```text
Coverage
Correctness
Assertion Strength
Isolation
Determinism
Maintainability
Redundancy
Security
```

---

## 71. Human Approval

## FR-050

Human developers or authorized reviewers shall approve AI-generated tests before they become mandatory protected tests for critical functionality.

---

## 72. Mutation Testing

## FR-051

The unit testing framework shall support mutation testing for critical modules.

Example:

```text
Original:
if score >= 80

Mutation:
if score > 80
```

The test suite should detect the mutation.

---

## 73. Coverage Requirements

## SR-014

The system shall collect:

```text
Line Coverage
Branch Coverage
Function Coverage
Statement Coverage
Condition Coverage where appropriate
```

---

## 74. Critical Code Coverage

## SR-015

Higher coverage requirements shall apply to critical domains such as:

```text
Authentication
Authorization
Billing
Tenant Isolation
Security
Usage Enforcement
Permission Validation
Data Integrity
AI Safety Controls
```

Coverage thresholds shall be defined by repository/service policy rather than relying on one global percentage.

---

## 75. Coverage Quality

## FR-052

Coverage shall not be considered sufficient merely because lines execute.

Tests shall contain meaningful assertions.

---

## 76. Weak Assertion Detection

## FR-053

The system shall identify tests that:

* Execute code without assertions.
* Assert only non-null values.
* Assert implementation details unnecessarily.
* Mock everything without validating behavior.
* Have unreachable assertions.

---

## 77. Test Duplication

## FR-054

The system shall identify duplicate or substantially overlapping tests.

---

## 78. Test Performance

## SR-016

Unit tests shall be optimized for rapid feedback.

Slow tests shall be identified automatically.

---

## 79. Test Duration Thresholds

The system shall support configurable thresholds for:

```text
Individual Test
Test File
Test Module
Complete Unit Suite
```

Tests exceeding thresholds shall be flagged.

---

## 80. Flaky Test Detection

## FR-055

The system shall identify tests whose results vary without code changes.

Flakiness metrics shall include:

```text
Pass Rate
Failure Rate
Retry Success Rate
Historical Failure Count
```

---

## 81. Flaky Test Quarantine

## FR-056

Flaky tests may be quarantined according to policy.

Critical security, authorization, billing, and tenant-isolation tests shall not be silently ignored because they are flaky.

---

## 82. Test Fixtures

## FR-057

Reusable fixtures shall support:

* Users.
* Organizations.
* Roles.
* Permissions.
* Leads.
* Conversations.
* Agents.
* Knowledge documents.
* Subscriptions.
* API requests.
* Events.

Fixtures shall remain isolated between tests.

---

## 83. Fixture Cleanup

## SR-017

Tests shall not depend on execution order.

Test state shall be reset between independent tests.

---

## 84. Property-Based Testing

## FR-058

Property-based testing shall be supported for suitable deterministic algorithms.

Examples:

```text
Validators
Parsers
Ranking
Normalization
Serialization
Pagination
Scoring
```

---

## 85. Fuzz Testing

## FR-059

Fuzz tests shall be supported for security-sensitive parsers and validators.

---

## 86. Regression Tests

## FR-060

When a production bug is fixed at the unit-testable layer, an appropriate regression unit test shall be added.

---

## 87. Test-to-Requirement Traceability

## FR-061

Critical requirements shall map to unit tests where the behavior can be validated at unit scope.

```text
Requirement
    ↓
Implementation
    ↓
Unit Test
    ↓
Test Run
    ↓
Evidence
```

---

## 88. Test Metadata

Each test execution shall record:

```yaml
test_run_id:
test_id:
service:
module:
commit_sha:
branch:
build_id:
framework_version:
started_at:
completed_at:
duration_ms:
status:
failure_type:
```

---

## 89. Failure Diagnostics

## FR-062

Failed unit tests shall provide:

* Test name.
* Assertion failure.
* Stack trace.
* Input fixture.
* Expected result.
* Actual result.
* Relevant logs.
* Commit SHA.
* Environment.

Secrets shall be automatically redacted.

---

## 90. AI Failure Analysis

## FR-063

AI shall analyze failed unit tests and classify probable causes:

```text
Implementation Defect
Test Defect
Fixture Defect
Dependency Mock Defect
Configuration Defect
Environment Defect
Race Condition
Flaky Test
Unknown
```

AI classifications shall remain recommendations unless policy explicitly allows automated remediation.

---

## 91. Automated Fix Suggestions

## FR-064

AI may propose:

* Code fixes.
* Test fixes.
* Fixture corrections.
* Missing assertions.
* Additional test cases.

Production code changes shall require normal code-review controls.

---

## 92. Pull Request Testing

## FR-065

Pull requests shall automatically execute affected unit tests.

---

## 93. Changed-Code Testing

## FR-066

The testing system shall identify changed modules and execute relevant unit tests.

Dependency-aware test selection may be used.

---

## 94. Full Regression Testing

## FR-067

A complete unit-test suite shall remain available for:

* Main branch.
* Release candidates.
* Nightly execution.
* Major architectural changes.

---

## 95. CI/CD Quality Gate

## FR-068

A pull request shall not merge when mandatory unit tests fail.

---

## 96. Critical Failure Policy

A merge shall be blocked for failures involving:

```text
Authentication
Authorization
Tenant Isolation
Billing
Security
Data Integrity
AI Safety Controls
Critical Business Logic
```

unless an explicitly authorized exception exists.

---

## 97. Test Result Storage

## SR-018

Test results shall be retained according to organizational retention policy.

Historical data shall support trend analysis.

---

## 98. Test Trend Analysis

## FR-069

The system shall track:

```text
Pass Rate
Failure Rate
Coverage
Flakiness
Execution Time
Test Count
Regression Count
```

over time.

---

## 99. Test Debt

## FR-070

The system shall identify:

* Untested critical code.
* Low-assertion tests.
* Missing negative cases.
* Flaky tests.
* Slow tests.
* Duplicated tests.
* Stale tests.

---

## 100. Unit Test Debt Score

The system may calculate:

```text
Test Debt =
Untested Critical Paths
+
Missing Branch Coverage
+
Flaky Tests
+
Slow Tests
+
Weak Assertions
+
Stale Tests
```

---

## 101. Test Ownership

## FR-071

Every critical unit-test module shall have an identifiable owning team.

---

## 102. Code Ownership

Tests shall follow service ownership boundaries.

Examples:

```text
Auth Service
    → Auth Tests

Billing Service
    → Billing Tests

Lead Intelligence
    → Lead Intelligence Tests

AI Gateway
    → AI Gateway Tests

Workflow Service
    → Workflow Tests
```

---

## 103. Microservice Unit Testing

Each microservice shall maintain an independent unit-test suite.

At minimum:

```text
Auth Service
Billing Service
Lead Intelligence Service
AI Gateway
Conversation Service
Workflow Service
Notification Service
Integration Services
Developer Platform
Admin Platform
```

where applicable.

---

## 104. Shared Library Testing

Shared libraries shall have independent unit-test suites.

Examples:

```text
Authentication Library
Authorization Library
Logging Library
Metrics Library
Tracing Library
Configuration Library
Event Library
API Client Library
Security Library
```

---

## 105. SDK Unit Testing

SDK components shall test:

* Request construction.
* Authentication.
* Serialization.
* Response parsing.
* Error mapping.
* Retry handling.
* Pagination.

---

## 106. API Client Testing

API clients shall use mocked HTTP responses.

Tests shall cover:

```text
200
201
204
400
401
403
404
409
429
500
502
503
504
Timeout
Malformed Response
```

---

## 107. Retry Logic

## FR-072

Retry utilities shall test:

* Retryable errors.
* Non-retryable errors.
* Maximum retries.
* Exponential backoff.
* Jitter.
* Retry exhaustion.

---

## 108. Idempotency Testing

## FR-073

Idempotent business operations shall be tested with repeated identical requests.

Expected behavior shall be explicitly asserted.

---

## 109. Concurrency Unit Testing

## FR-074

Concurrency-sensitive units shall test:

* Simultaneous updates.
* Lock acquisition.
* Lock failure.
* Race conditions.
* Duplicate execution.
* State consistency.

---

## 110. Security Regression Suite

## FR-075

Previously discovered security bugs shall be represented by permanent unit tests where technically appropriate.

---

## 111. AI Safety Unit Suite

The AI safety control layer shall have dedicated deterministic unit tests for:

```text
Permission Checks
Tool Authorization
Prompt Policy Enforcement
PII Redaction
Content Filtering
Action Validation
Human Approval Enforcement
Tenant Isolation
```

---

## 112. Prompt Injection Unit Testing

## FR-076

Prompt-processing utilities shall test representative malicious instructions.

Tests shall verify that application-level controls do not incorrectly treat untrusted content as trusted instructions.

---

## 113. Agent Permission Unit Testing

## FR-077

An agent shall not be able to invoke a tool merely because the tool exists.

Authorization must be evaluated independently.

---

## 114. AI Output Parsing

## FR-078

Structured AI output parsers shall test:

```text
Valid JSON
Invalid JSON
Missing Field
Extra Field
Wrong Type
Null Value
Empty Response
Partial Response
Unexpected Schema
```

---

## 115. AI Mocking Strategy

## SR-019

Unit tests shall mock LLM providers.

The test suite shall not depend on:

* Network availability.
* Provider availability.
* Model randomness.
* External API rate limits.

---

## 116. AI Golden Fixtures

## FR-079

Representative AI responses may be stored as versioned fixtures for deterministic testing of:

* Parsers.
* Routers.
* Validators.
* Safety filters.
* Agent state transitions.

---

## 117. Human Review of AI Tests

## FR-080

Human reviewers shall verify AI-generated tests for critical code before approval.

Review shall focus on:

```text
Correctness
Coverage
Security
Isolation
Assertions
Maintainability
```

---

## 118. AI Test Governance

## SR-020

AI-generated tests shall include metadata:

```yaml
generated_by: ai
generator:
model:
generation_timestamp:
source_commit:
review_status:
reviewer:
```

---

## 119. AI Test Trust Levels

Tests may be classified as:

```text
AI_GENERATED
AI_REVIEWED
HUMAN_REVIEWED
PROTECTED
MANDATORY
```

Only authorized policies may promote tests between trust levels.

---

## 120. Protected Tests

## FR-081

Protected tests shall not be deleted or modified without appropriate review.

---

## 121. Test Change Review

Changes to critical unit tests shall require code review.

---

## 122. Test Code Quality

Unit-test code shall follow the same engineering standards as production code.

It shall be:

* Readable.
* Maintainable.
* Modular.
* Deterministic.
* Documented where necessary.

---

## 123. Anti-Patterns

The testing system shall identify or discourage:

```text
Testing Implementation Instead of Behavior
Over-Mocking
Under-Assertion
Test Interdependence
Shared Mutable State
Random Test Data Without Seeds
Hidden Network Calls
Hidden Database Calls
Excessive Fixture Complexity
Copy-Pasted Tests
Tests That Never Fail
```

---

## 124. Unit Test Execution Modes

Supported modes:

```text
LOCAL
WATCH
TARGETED
AFFECTED
FULL
CI
NIGHTLY
RELEASE
```

---

## 125. Watch Mode

## FR-082

Developers shall be able to automatically rerun affected unit tests when source files change.

---

## 126. Parallel Execution

## FR-083

Independent tests shall execute in parallel.

Tests with shared resources shall be isolated appropriately.

---

## 127. Test Ordering

## SR-021

The correctness of the unit suite shall not depend on execution order.

Randomized test ordering may be used to detect hidden dependencies.

---

## 128. Test Reproducibility

A failed test shall be reproducible using:

```text
Commit SHA
Test ID
Fixture Version
Configuration Version
Random Seed
Dependency Versions
```

where applicable.

---

## 129. Environment Consistency

Unit tests shall execute consistently across:

```text
Developer Machine
CI Runner
Staging Build Environment
Release Pipeline
```

within supported platform differences.

---

## 130. Containerized Unit Testing

## FR-084

Unit tests shall support execution inside reproducible containers where appropriate.

---

## 131. Python Backend Testing

Backend unit tests shall cover:

```text
Services
Models
Serializers
Validators
Repositories
Utilities
Business Logic
API Handlers
Workers
Event Handlers
```

---

## 132. TypeScript / Frontend Testing

Frontend unit tests shall cover:

```text
Components
Hooks
Utilities
State Management
Validation
API Clients
Formatters
Reducers
Permission Helpers
i18n Utilities
```

---

## 133. ML Component Testing

ML preprocessing and deterministic ML components shall be unit-tested for:

* Feature extraction.
* Normalization.
* Encoding.
* Data validation.
* Postprocessing.
* Threshold logic.
* Label mapping.

---

## 134. Model Inference Testing

Deterministic inference wrappers shall test:

* Input schema.
* Output schema.
* Invalid input.
* Missing features.
* Shape mismatch.
* Model-loading failure.
* Version mismatch.

Model quality shall be evaluated using dedicated ML evaluation tests.

---

## 135. Data Validation

## FR-085

Data validation utilities shall test:

```text
Schema Valid
Schema Invalid
Missing Fields
Extra Fields
Wrong Types
Boundary Values
Nested Structures
Unicode
```

---

## 136. Serialization Compatibility

## FR-086

Versioned serializers shall test backward and forward compatibility where required.

---

## 137. API Versioning

## FR-087

Version-specific business logic shall have unit tests protecting behavior differences between API versions.

---

## 138. Configuration Matrix

Critical units shall be tested across supported configuration combinations.

Examples:

```text
Feature Flag ON/OFF
Language EN/Other Supported Languages
Plan Free/Paid/Enterprise
Role Admin/Agent/Developer/User
AI Provider A/B/C
```

---

## 139. Negative Testing

## FR-088

At least one negative test shall exist for every critical validation or authorization rule.

---

## 140. Security Boundary Testing

## FR-089

Every security boundary shall have both:

```text
Allowed Case
Denied Case
```

tests.

---

## 141. Error Message Testing

## FR-090

User-facing error transformations shall be tested for:

* Correct error code.
* Safe message.
* No secret leakage.
* No internal stack trace leakage.
* Correct localization where applicable.

---

## 142. Test Reporting

The reporting system shall expose:

```text
Total Tests
Passed
Failed
Skipped
Flaky
Duration
Coverage
Changed-Code Coverage
Critical Test Status
```

---

## 143. CI Quality Gate Example

```text
                Pull Request
                     │
                     ▼
             Static Validation
                     │
                     ▼
              Unit Test Suite
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
       PASS                    FAIL
          │                     │
          ▼                     ▼
      Coverage              Block Merge
          │
          ▼
    Security Unit Tests
          │
          ▼
       AI Safety
          │
          ▼
      Quality Gate
          │
          ▼
       Allow Merge
```

---

## 144. Recommended Test Distribution

The SalesGenie testing pyramid shall prefer:

```text
              E2E
             /   \
        Integration
          /       \
       Contract/API
         /       \
      Component
       /         \
      Unit Tests
```

Unit tests should represent the largest portion of deterministic automated tests.

---

## 145. Critical Unit Test Categories

The following categories shall receive highest priority:

```text
Authentication
Authorization
Tenant Isolation
Billing
Usage Enforcement
Security Controls
Data Validation
Data Integrity
AI Safety
Agent Permissions
Tool Authorization
Lead Scoring
Search Permissions
Workflow Conditions
Event Idempotency
Webhook Verification
```

---

## 146. Unit Testing Dashboard

The platform shall expose:

```text
Total Unit Tests
Passing Tests
Failing Tests
Skipped Tests
Flaky Tests
Coverage
Critical Coverage
Changed-Code Coverage
Average Execution Time
Slowest Tests
Failure Trends
Test Debt
AI-Generated Tests
AI Test Acceptance Rate
Regression Tests
```

---

## 147. Quality Metrics

The unit testing system shall track:

```text
Test Pass Rate
Test Failure Rate
Branch Coverage
Line Coverage
Mutation Score
Flaky Test Rate
Mean Test Duration
Regression Detection Rate
Defect Escape Rate
Test Debt
Critical Test Coverage
Changed-Code Coverage
```

---

## 148. Release Gate Requirements

Production release shall be blocked when:

```text
Mandatory Unit Test Fails
OR
Critical Security Unit Test Fails
OR
Critical Authorization Test Fails
OR
Tenant Isolation Test Fails
OR
Billing Integrity Test Fails
OR
AI Safety Control Test Fails
```

---

## 149. Human + AI Testing Workflow

```text
Requirement
    ↓
Developer Implementation
    ↓
AI Test Generation
    ↓
AI Test Review
    ↓
Human Review
    ↓
Unit Test Execution
    ↓
Coverage Analysis
    ↓
Mutation Analysis
    ↓
Failure Analysis
    ↓
Fix
    ↓
Re-run
    ↓
CI Quality Gate
    ↓
Merge
```

---

## 150. AI-Driven Continuous Improvement

The AI testing subsystem shall continuously analyze:

```text
Source Changes
+
Production Bugs
+
Incident Reports
+
Failed Tests
+
Coverage Gaps
+
Mutation Survivors
+
Flaky Tests
```

and recommend:

```text
New Tests
Test Improvements
Missing Edge Cases
Regression Tests
Fixture Improvements
Refactoring Opportunities
```

---

## 151. Production Incident → Unit Regression

```text
Production Incident
        ↓
Root Cause Analysis
        ↓
Identify Unit Boundary
        ↓
Generate Regression Test
        ↓
Human Review
        ↓
Add to Protected Suite
        ↓
CI/CD
        ↓
Permanent Regression Protection
```

---

## 152. Test Security

Unit testing infrastructure shall:

* Never expose production credentials.
* Never commit secrets.
* Redact secrets from test failures.
* Isolate sensitive fixtures.
* Prevent unauthorized production calls.
* Validate security-sensitive code.

---

## 153. Test Data Policy

Test data shall be:

```text
Synthetic
Anonymized
Masked
Non-Production
Version Controlled
Reproducible
```

where applicable.

---

## 154. Test Artifact Policy

Artifacts shall not contain:

* Passwords.
* API keys.
* Access tokens.
* Private keys.
* Unmasked sensitive information.

---

## 155. Definition of Ready

A unit-testable feature shall be considered ready when:

```text
Requirement Defined
AND
Behavior Defined
AND
Acceptance Criteria Defined
AND
Dependencies Identified
AND
Error Cases Identified
AND
Security Boundaries Identified
```

---

## 156. Definition of Done

A unit-tested implementation shall be considered complete when:

```text
Unit Tests Implemented
AND
Positive Cases Covered
AND
Negative Cases Covered
AND
Boundary Cases Covered
AND
Critical Security Cases Covered
AND
Meaningful Assertions Exist
AND
Tests Are Deterministic
AND
Tests Pass Locally
AND
Tests Pass CI
AND
Coverage Policy Satisfied
AND
No Critical Regression Exists
```

---

## 157. Enterprise Unit Testing Acceptance Criteria

SalesGenie shall satisfy all of the following:

* Every critical business rule has unit-level validation where technically appropriate.
* Every authentication and authorization boundary has positive and negative tests.
* Tenant isolation has automated unit-level protection.
* Billing and usage calculations are comprehensively unit-tested.
* Critical AI safety controls are unit-tested.
* Agent state transitions are unit-tested.
* Tool authorization is unit-tested.
* RAG preprocessing and deterministic retrieval logic are unit-tested.
* LLM adapters are tested using deterministic mocks.
* External dependencies are isolated from unit tests.
* Unit tests execute without network dependency.
* Unit tests are deterministic and reproducible.
* Failed tests produce actionable diagnostics.
* Flaky tests are detected and controlled.
* Critical tests cannot be silently quarantined.
* AI-generated tests are governed.
* Human reviewers retain authority over critical test promotion.
* Production incidents can generate regression unit tests.
* CI/CD blocks merges on mandatory unit-test failures.
* Test coverage is combined with assertion quality and mutation testing.
* Test ownership is explicit.
* Test history is auditable.
* Test execution is continuously monitored.

---

## 158. Ultimate Unit Testing Architecture

```text
                         SALESGENIE
                             │
                             ▼
                    ┌─────────────────┐
                    │ Source / Change │
                    └────────┬────────┘
                             ▼
                    ┌─────────────────┐
                    │ AI Test Generator│
                    └────────┬────────┘
                             ▼
                    ┌─────────────────┐
                    │ Human Review     │
                    └────────┬────────┘
                             ▼
                    ┌─────────────────┐
                    │ Unit Test Runner │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        ▼                    ▼                    ▼
   Backend Tests       Frontend Tests       AI/ML Tests
        │                    │                    │
        └────────────────────┼────────────────────┘
                             ▼
                    ┌─────────────────┐
                    │ Coverage Engine │
                    └────────┬────────┘
                             ▼
                    ┌─────────────────┐
                    │ Mutation Testing│
                    └────────┬────────┘
                             ▼
                    ┌─────────────────┐
                    │ AI Failure      │
                    │ Analyzer        │
                    └────────┬────────┘
                             ▼
                    ┌─────────────────┐
                    │ Quality Gates   │
                    └────────┬────────┘
                             ▼
                    ┌─────────────────┐
                    │ CI/CD Pipeline  │
                    └────────┬────────┘
                             ▼
                         MERGE / BLOCK
```

---

## 159. Core Engineering Principles

1. **Test behavior, not implementation details.**
2. **Keep unit tests isolated from external infrastructure.**
3. **Prefer deterministic tests.**
4. **Test failure paths as aggressively as success paths.**
5. **Treat security boundaries as first-class unit-test targets.**
6. **Treat tenant isolation as a critical invariant.**
7. **Use mocks only where they preserve meaningful behavioral validation.**
8. **Do not confuse code coverage with test quality.**
9. **Use mutation testing to validate test effectiveness.**
10. **Use AI to expand test coverage, not to bypass engineering judgment.**
11. **Require human approval for critical AI-generated tests.**
12. **Convert production defects into permanent regression protection where appropriate.**
13. **Keep unit tests fast enough for continuous developer feedback.**
14. **Never allow flaky tests to silently weaken critical release gates.**
15. **Make every important failure reproducible.**
16. **Continuously improve the test suite using production evidence.**

---

## 160. Ultimate Goal

```text
                 HIGH DEVELOPMENT VELOCITY
                           +
                    FAST FEEDBACK
                           +
                     HIGH COVERAGE
                           +
                  STRONG ASSERTIONS
                           +
                    DETERMINISM
                           +
                    SECURITY
                           +
                  AI TEST ASSISTANCE
                           +
                  HUMAN GOVERNANCE
                           +
                CONTINUOUS REGRESSION
                           =
              ENTERPRISE-GRADE SALESGENIE
                    UNIT TESTING
```
