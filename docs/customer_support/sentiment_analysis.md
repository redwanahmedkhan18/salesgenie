# SalesGenie — AI-Powered Touch Sentiment Analysis

## FAANG-Level User Requirements, System Requirements & Functional Requirements

---

## 1. Document Overview

## 1.1 Feature Name

**Touch Sentiment Analysis**

## 1.2 Product

**SalesGenie — Enterprise AI Customer Support & Sales Agent Platform**

## 1.3 Feature Purpose

Touch Sentiment Analysis is an enterprise-grade AI intelligence capability that analyzes customer interactions across SalesGenie's omnichannel support ecosystem to determine:

* Customer sentiment
* Sentiment intensity
* Emotional state
* Sentiment trajectory
* Positive and negative sentiment events
* Frustration and dissatisfaction signals
* Escalation risk
* Churn risk signals
* Customer satisfaction risk
* Root causes of negative sentiment
* Resolution impact on sentiment
* AI-agent impact on sentiment
* Human-agent impact on sentiment
* Channel-specific sentiment behavior
* Product/service-specific sentiment
* Sentiment trends and anomalies
* Recommended next actions

The system must support both **AI-driven automated analysis** and **human-in-the-loop review, correction, governance, and intervention**.

---

## 2. Product Objectives

SalesGenie Touch Sentiment Analysis shall:

1. Analyze customer interactions in real time and asynchronously.
2. Detect sentiment at message, turn, conversation, ticket, customer, product, channel, and organization levels.
3. Detect sentiment changes throughout a customer journey.
4. Identify deteriorating conversations before they become escalations.
5. Automatically alert or route high-risk interactions to human support agents.
6. Help AI agents adapt response tone according to customer emotional state.
7. Provide human agents with actionable sentiment intelligence.
8. Identify why customers are becoming negative.
9. Correlate sentiment with CSAT, NPS, churn, conversion, resolution, refund, escalation, and retention signals.
10. Analyze AI-agent and human-agent interactions separately and jointly.
11. Provide explainable sentiment predictions with confidence scores and evidence.
12. Support multilingual and cross-channel sentiment analysis.
13. Continuously improve through human feedback and model evaluation.
14. Protect customer privacy and enforce tenant isolation.
15. Provide enterprise-grade auditability, observability, reliability, and scalability.

---

## 3. User Requirements

## UR-001 — Real-Time Customer Sentiment

The system shall allow authorized users to view the current sentiment of an active customer interaction in near real time.

### Users

* End users
* Human support agents
* AI support agents
* Support supervisors
* Customer success managers
* Organization administrators

### Requirements

* Display current sentiment.
* Display sentiment intensity.
* Display confidence.
* Update sentiment as new messages arrive.
* Display sentiment changes over time.
* Identify significant negative sentiment events.
* Identify significant positive sentiment events.

---

## UR-002 — Sentiment Classification

The system shall classify customer sentiment using configurable sentiment categories.

Minimum supported categories:

* Very Positive
* Positive
* Slightly Positive
* Neutral
* Slightly Negative
* Negative
* Very Negative

The system should support custom organization-specific sentiment taxonomies.

---

## UR-003 — Emotional State Detection

The system shall identify emotional states where sufficient evidence exists.

Examples:

* Frustration
* Anger
* Confusion
* Disappointment
* Anxiety
* Urgency
* Satisfaction
* Excitement
* Appreciation
* Concern
* Fear
* Resignation
* Trust
* Distrust

Emotion detection shall be separate from sentiment polarity.

---

## UR-004 — Sentiment Intensity

Users shall be able to determine how strongly a customer expresses a sentiment.

The system shall provide:

* Numerical sentiment score
* Intensity score
* Confidence score
* Human-readable sentiment label

---

## UR-005 — Sentiment Trajectory

The system shall show how customer sentiment changes throughout a conversation.

Examples:

```text
Negative → Very Negative → Negative → Neutral → Positive
```

Users shall be able to identify:

* Initial sentiment
* Lowest sentiment
* Highest sentiment
* Final sentiment
* Sentiment delta
* Recovery rate
* Deterioration rate

---

## UR-006 — Negative Sentiment Detection

The system shall identify negative customer sentiment automatically.

Negative signals may include:

* Explicit complaints
* Repeated complaints
* Escalation language
* Cancellation requests
* Refund requests
* Threats to leave
* Negative product feedback
* Repeated unresolved issues
* Excessive waiting
* Agent dissatisfaction
* AI-agent dissatisfaction
* Billing complaints
* Service failures
* Policy frustration

---

## UR-007 — Sentiment-Based Escalation

The system shall allow organizations to configure escalation rules based on sentiment.

Example:

```text
IF sentiment <= Very Negative
AND confidence >= 0.85
THEN escalate to human support supervisor
```

Possible escalation destinations:

* Specific human agent
* Support team
* Supervisor
* Customer success team
* Escalation queue
* Priority queue
* Executive support queue

---

## UR-008 — AI Agent Sentiment Awareness

AI support agents shall be able to consume sentiment intelligence during conversations.

The AI agent shall be able to:

* Adjust response tone.
* Reduce repetitive responses.
* Increase empathy.
* Avoid aggressive upselling.
* Stop unnecessary automation.
* Trigger human handoff.
* Prioritize urgent requests.
* Acknowledge frustration.
* Modify response length.
* Offer resolution-oriented responses.

---

## UR-009 — Human Agent Sentiment Assistance

Human agents shall receive sentiment intelligence while interacting with customers.

The system should provide:

* Current sentiment
* Sentiment trend
* Emotional state
* Escalation risk
* Key negative triggers
* Recommended response strategy
* Recommended next action
* Relevant customer history

---

## UR-010 — Sentiment Explanation

Users shall be able to understand why the AI assigned a particular sentiment.

The system should expose:

* Relevant message
* Trigger phrase
* Sentiment score
* Confidence
* Detected emotion
* Detected topic
* Supporting context
* Model version

The system shall avoid exposing confidential internal model prompts or security-sensitive implementation details.

---

## UR-011 — Human Correction

Authorized human reviewers shall be able to correct sentiment predictions.

Human reviewers shall be able to:

* Change sentiment
* Change emotion
* Change intensity
* Mark prediction as incorrect
* Add explanation
* Add review notes
* Confirm AI prediction
* Flag ambiguous cases

Human corrections shall be retained as feedback data.

---

## UR-012 — Feedback Learning

The system shall use approved human feedback to improve future sentiment classification.

The system shall support:

* Feedback collection
* Annotation
* Dataset generation
* Model evaluation
* Model comparison
* Threshold tuning
* Taxonomy updates
* Drift monitoring

Production model updates shall require appropriate authorization and validation.

---

## UR-013 — Omnichannel Sentiment

The system shall support sentiment analysis across available SalesGenie channels, including:

* Website chat
* AI chat
* Human support chat
* Email
* WhatsApp
* Telegram
* Messenger
* Social messaging
* Support tickets
* Voice transcripts
* CRM interactions
* Other configured channels

---

## UR-014 — Multilingual Sentiment

The system shall support multilingual sentiment analysis.

The system should:

* Detect language.
* Analyze sentiment in the original language when supported.
* Preserve language metadata.
* Handle mixed-language conversations.
* Support translated analysis where required.
* Avoid treating translation artifacts as customer sentiment.

---

## UR-015 — Conversation-Level Sentiment

The system shall calculate an overall sentiment score for each conversation.

The calculation should consider:

* Individual interaction sentiment
* Sentiment intensity
* Message importance
* Recency
* Conversation progression
* Customer context
* Resolution state

---

## UR-016 — Ticket-Level Sentiment

Users shall be able to view sentiment associated with support tickets.

Ticket sentiment shall include:

* Opening sentiment
* Current sentiment
* Closing sentiment
* Sentiment change
* Negative events
* Escalation risk
* Resolution impact

---

## UR-017 — Customer-Level Sentiment

Authorized users shall be able to view aggregate sentiment for customers.

The system shall support:

* Current customer sentiment
* Historical sentiment
* Average sentiment
* Recent sentiment
* Sentiment trend
* Product-specific sentiment
* Channel-specific sentiment
* Support-specific sentiment
* Churn-risk correlation

---

## UR-018 — Product Sentiment

Users shall be able to determine sentiment associated with:

* Products
* Features
* Services
* Plans
* Pricing
* Policies
* Integrations
* Support processes

---

## UR-019 — Topic + Sentiment Analysis

The system shall associate sentiment with topics.

Example:

```text
Topic: Billing
Sentiment: Very Negative
Confidence: 0.94
Volume: 1,284 interactions
```

Possible topics:

* Billing
* Pricing
* Product quality
* Login
* Performance
* Delivery
* Onboarding
* Refund
* Technical support
* Feature request
* Account management

---

## UR-020 — Sentiment Root Cause

The system shall identify probable causes behind sentiment changes.

Example:

```text
Negative Sentiment Driver:
Repeated authentication failures

Evidence:
Customer attempted login 5 times.

Impact:
High frustration probability.

Recommended Action:
Escalate to technical support.
```

---

## 4. System Requirements

## 4.1 Architecture Requirements

## SR-001 — Microservice Architecture

Touch Sentiment Analysis shall integrate with SalesGenie's enterprise microservice architecture.

Relevant services may include:

* AI Gateway
* Conversation Service
* Support Service
* Ticket Service
* Customer Service
* Analytics Service
* Notification Service
* Knowledge Service
* Vector Service
* Workflow Service
* Channel Services

---

## SR-002 — Event-Driven Processing

The system shall support event-driven sentiment processing.

Example event:

```json
{
  "event": "customer.message.created",
  "conversation_id": "conv_123",
  "tenant_id": "tenant_001",
  "channel": "whatsapp",
  "message_id": "msg_456",
  "timestamp": "2026-08-25T15:00:00Z"
}
```

The sentiment engine shall consume the event without blocking message delivery.

---

## SR-003 — Real-Time Processing

Sentiment analysis should operate asynchronously from the customer response pipeline.

Target:

```text
Message received
        ↓
Event emitted
        ↓
Sentiment analysis
        ↓
Risk evaluation
        ↓
Alert / routing
        ↓
Analytics update
```

---

## SR-004 — Batch Processing

The system shall support historical analysis of:

* Existing conversations
* Existing tickets
* Historical email
* Historical chat
* Historical transcripts
* Customer feedback
* Imported datasets

---

## 5. AI/ML System Requirements

## SR-005 — Sentiment Model

The system shall use an NLP/LLM/classification architecture capable of sentiment analysis.

The architecture may include:

* Transformer classifier
* Fine-tuned language model
* LLM-based classifier
* Small language model
* Ensemble classifier
* Hybrid rules + ML model

---

## SR-006 — Structured AI Output

The model shall produce schema-validated output.

Example:

```json
{
  "sentiment": "negative",
  "sentiment_score": -0.82,
  "intensity": 0.91,
  "emotion": "frustration",
  "confidence": 0.94,
  "risk_level": "high",
  "topics": [
    "billing",
    "refund"
  ],
  "drivers": [
    "unexpected charge",
    "refund delay"
  ],
  "requires_human_review": true
}
```

---

## SR-007 — Confidence Estimation

Every AI sentiment prediction shall contain confidence information.

The system shall distinguish:

* High confidence
* Medium confidence
* Low confidence
* Unknown / insufficient evidence

Low-confidence predictions shall be eligible for human review.

---

## SR-008 — Context-Aware Analysis

The model shall analyze sentiment using conversation context rather than relying solely on isolated keywords.

The system should account for:

* Previous messages
* Conversation history
* Customer context
* Topic
* Agent responses
* AI responses
* Resolution status
* Conversation stage

---

## SR-009 — Sarcasm and Negation

The system should attempt to detect:

* Sarcasm
* Negation
* Indirect complaints
* Polite dissatisfaction
* Repeated frustration
* Context-dependent emotional statements

---

## SR-010 — Sentiment Shift Detection

The system shall calculate sentiment changes between interaction points.

Example:

```text
Previous score: -0.20
Current score: -0.78
Delta: -0.58
```

A significant deterioration shall be eligible for an alert.

---

## SR-011 — AI/Human Attribution

The system shall distinguish between:

* Customer sentiment
* Human-agent behavior
* AI-agent behavior

The system shall never incorrectly attribute an agent's emotional language to the customer.

---

## 6. Data Requirements

## SR-012 — Sentiment Data Model

The system shall maintain sentiment records containing at minimum:

```text
sentiment_id
tenant_id
organization_id
customer_id
conversation_id
ticket_id
message_id
channel
actor_type
language
sentiment_label
sentiment_score
intensity_score
emotion
confidence_score
risk_level
topics
drivers
model_version
created_at
updated_at
```

---

## SR-013 — Tenant Isolation

Sentiment data must be isolated by tenant.

No tenant shall be able to access:

* Another tenant's conversations
* Another tenant's sentiment records
* Another tenant's analytics
* Another tenant's embeddings
* Another tenant's model feedback

---

## SR-014 — Data Lineage

Each sentiment result shall be traceable to:

* Original interaction
* Conversation
* Customer
* Channel
* Model version
* Analysis timestamp
* Processing pipeline
* Human corrections

---

## 7. Functional Requirements

## FR-001 — Analyze Message Sentiment

The system shall analyze each eligible customer message.

### Input

```text
Customer message
Conversation context
Customer context
Channel
Language
```

### Output

```text
Sentiment
Score
Intensity
Emotion
Confidence
Risk
Topics
Drivers
```

---

## FR-002 — Analyze Conversation Sentiment

The system shall aggregate message-level sentiment into conversation-level sentiment.

The calculation shall consider:

* Message sentiment
* Message recency
* Interaction importance
* Sentiment intensity
* Conversation progression

---

## FR-003 — Calculate Initial Sentiment

The system shall calculate the customer's sentiment at the beginning of a conversation.

---

## FR-004 — Calculate Current Sentiment

The system shall maintain the latest available customer sentiment.

---

## FR-005 — Calculate Final Sentiment

After conversation closure, the system shall calculate final sentiment.

---

## FR-006 — Calculate Sentiment Delta

The system shall calculate:

```text
Sentiment Delta =
Final Sentiment - Initial Sentiment
```

It shall also support intermediate sentiment changes.

---

## FR-007 — Detect Sentiment Deterioration

The system shall identify significant deterioration.

Example:

```text
Initial: Positive
Current: Very Negative

Result:
Critical Sentiment Deterioration
```

---

## FR-008 — Detect Sentiment Recovery

The system shall identify when customer sentiment improves.

Example:

```text
Very Negative
      ↓
Negative
      ↓
Neutral
      ↓
Positive
```

---

## FR-009 — Detect Emotional Signals

The system shall identify supported emotional states and associate them with confidence.

---

## FR-010 — Detect High-Risk Sentiment

The system shall classify sentiment risk.

Example:

```text
LOW
MEDIUM
HIGH
CRITICAL
```

Risk evaluation may consider:

* Sentiment
* Intensity
* Repetition
* Customer value
* Churn indicators
* Escalation language
* Complaint frequency
* Resolution failure

---

## FR-011 — Trigger Sentiment Alerts

The system shall trigger alerts when configured thresholds are reached.

Example:

```text
IF sentiment_score <= -0.75
AND confidence >= 0.85
THEN create sentiment_alert
```

---

## FR-012 — Trigger Sentiment-Based Escalation

The system shall support automatic human escalation.

Example:

```text
Customer
   ↓
AI Support
   ↓
Very Negative Sentiment
   ↓
Escalation Engine
   ↓
Human Support Agent
```

---

## FR-013 — Preserve Conversation Context During Handoff

When escalation occurs, the human agent shall receive:

* Conversation history
* Customer information
* Sentiment history
* Sentiment triggers
* Detected topics
* Recommended action
* AI-agent actions
* Previous failed attempts

The customer should not be forced to repeat previously provided information.

---

## FR-014 — Sentiment-Aware AI Response

The AI agent shall use sentiment state to modify its response strategy.

Example:

```text
Customer sentiment:
Very Negative

AI behavior:
- Stop upselling
- Avoid repetitive questions
- Acknowledge frustration
- Prioritize resolution
- Offer human assistance
```

---

## FR-015 — Sentiment-Aware Routing

The routing engine shall use sentiment as one routing signal.

Routing may consider:

```text
Sentiment
+
Intent
+
Priority
+
Customer tier
+
Topic
+
Language
+
Agent skill
+
SLA
```

---

## FR-016 — Human Review Queue

The system shall create a review queue for:

* Low-confidence predictions
* Ambiguous sentiment
* Sarcasm
* Conflicting signals
* Critical escalations
* Model anomalies

---

## FR-017 — Human Sentiment Correction

Authorized reviewers shall be able to modify AI predictions.

The system shall record:

```text
Original prediction
Human correction
Reviewer
Timestamp
Reason
Model version
```

---

## FR-018 — Human Feedback

Users shall be able to provide feedback:

```text
Correct
Incorrect
Partially Correct
Unclear
```

---

## FR-019 — Sentiment Search

Users shall be able to search conversations using sentiment filters.

Example:

```text
sentiment = very_negative
channel = whatsapp
date = last_7_days
topic = billing
```

---

## FR-020 — Sentiment Filtering

Users shall be able to filter by:

* Sentiment
* Emotion
* Confidence
* Risk
* Channel
* Product
* Customer
* Agent
* AI agent
* Topic
* Date
* Organization
* Ticket status

---

## FR-021 — Sentiment Dashboard

The system shall provide an enterprise sentiment dashboard.

Dashboard metrics shall include:

* Total analyzed interactions
* Positive percentage
* Neutral percentage
* Negative percentage
* Very negative percentage
* Average sentiment
* Sentiment trend
* Sentiment delta
* Escalation count
* High-risk conversations
* Sentiment recovery rate
* Top negative drivers
* Top positive drivers

---

## FR-022 — Channel Sentiment Analytics

Users shall be able to compare sentiment across:

```text
WhatsApp
Email
Website
Messenger
Telegram
Voice
Tickets
Social channels
```

---

## FR-023 — Agent Sentiment Analytics

Supervisors shall be able to analyze customer sentiment associated with interactions handled by human agents.

Metrics may include:

* Average customer sentiment
* Sentiment improvement
* Sentiment deterioration
* Escalation rate
* Recovery rate
* Negative sentiment volume
* Resolution-associated sentiment

Sentiment analytics shall not automatically be used for employee compensation, disciplinary action, or employment decisions.

---

## FR-024 — AI Agent Sentiment Analytics

The system shall separately analyze sentiment outcomes associated with AI-agent interactions.

Metrics:

* AI conversation sentiment
* AI sentiment recovery
* AI escalation rate
* AI handoff rate
* Negative sentiment after AI response
* Positive sentiment after AI response
* Failed sentiment recovery

---

## FR-025 — AI vs Human Comparison

Authorized managers shall be able to compare:

```text
AI-only support
Human-only support
AI → Human hybrid support
```

using sentiment-related operational metrics.

---

## FR-026 — Product Sentiment Analytics

The system shall identify products and features associated with sentiment changes.

Example:

```text
Product:
Enterprise CRM Integration

Sentiment:
-32%

Primary driver:
Integration failures
```

---

## FR-027 — Topic Sentiment Analytics

The system shall calculate sentiment by topic.

Example:

```text
Billing       -0.71
Onboarding    +0.24
Performance   -0.56
Support       +0.41
Pricing       -0.39
```

---

## FR-028 — Root Cause Analysis

The AI shall generate probable sentiment drivers.

Example:

```text
Negative sentiment increased primarily because:

1. Billing discrepancy
2. Delayed response
3. Repeated troubleshooting
4. No successful resolution
```

---

## FR-029 — Sentiment Anomaly Detection

The system shall identify unusual sentiment patterns.

Examples:

* Sudden negative sentiment spike
* Product-specific sentiment collapse
* Channel-specific sentiment deterioration
* Unusual escalation increase
* Sudden negative sentiment from high-value customers

---

## FR-030 — Sentiment Trend Forecasting

The system may predict future sentiment trends using historical signals.

Possible outputs:

```text
Current sentiment: -0.42
Forecast: -0.61
Risk: Increasing dissatisfaction
```

Predictions shall clearly be labeled as forecasts rather than facts.

---

## FR-031 — Customer Risk Correlation

The system shall correlate sentiment with:

* Churn
* Refund
* Cancellation
* Escalation
* CSAT
* NPS
* Conversion
* Retention
* Lifetime value

---

## FR-032 — Customer Journey Sentiment

The system shall support sentiment analysis across the customer lifecycle.

Example:

```text
Lead
 ↓
Prospect
 ↓
Customer
 ↓
Onboarding
 ↓
Support
 ↓
Renewal
 ↓
Expansion
```

---

## FR-033 — Sentiment-Based Workflow Automation

Sentiment events shall be usable as workflow triggers.

Example:

```text
Trigger:
Customer becomes Very Negative

Actions:
1. Create priority ticket
2. Notify supervisor
3. Assign human agent
4. Update customer risk
5. Record sentiment event
6. Start escalation workflow
```

---

## FR-034 — Notification System

Sentiment alerts shall support:

* In-app notifications
* Email
* Slack
* Microsoft Teams
* Mobile notifications
* Workflow notifications

---

## FR-035 — Sentiment API

The system shall expose authenticated APIs for sentiment data.

Example endpoints:

```text
POST /api/v1/sentiment/analyze
GET  /api/v1/sentiment/messages/{message_id}
GET  /api/v1/sentiment/conversations/{conversation_id}
GET  /api/v1/sentiment/customers/{customer_id}
GET  /api/v1/sentiment/analytics
GET  /api/v1/sentiment/alerts
POST /api/v1/sentiment/feedback
POST /api/v1/sentiment/review
```

---

## FR-036 — Sentiment Event API

The system shall support event publication for:

```text
sentiment.detected
sentiment.changed
sentiment.deteriorated
sentiment.recovered
sentiment.threshold_reached
sentiment.escalation_required
sentiment.review_required
sentiment.reviewed
```

---

## FR-037 — Model Versioning

Every sentiment result shall identify the model version.

The system shall support:

* Model version tracking
* A/B model evaluation
* Rollback
* Threshold configuration
* Model performance monitoring

---

## FR-038 — Model Evaluation

The system shall evaluate sentiment models using appropriate metrics.

Minimum metrics:

* Accuracy
* Precision
* Recall
* F1
* Confusion matrix
* Calibration
* Per-class performance
* Per-language performance
* Per-channel performance

---

## FR-039 — Human-in-the-Loop Evaluation

Human reviewers shall provide labeled examples for model evaluation.

The platform shall support:

```text
AI prediction
      ↓
Human validation
      ↓
Ground truth
      ↓
Evaluation dataset
      ↓
Model evaluation
      ↓
Model improvement
```

---

## FR-040 — Model Drift Detection

The system shall monitor sentiment model performance for drift.

Possible drift dimensions:

* Language
* Channel
* Product
* Customer segment
* Topic
* Time period
* Sentiment category
* Vocabulary

---

## FR-041 — Explainability

The system shall provide human-readable explanations for important sentiment decisions.

Explanations should distinguish:

```text
Observed evidence
AI interpretation
Confidence
Recommended action
```

---

## FR-042 — Privacy Controls

The system shall support:

* Data minimization
* Role-based access
* Tenant isolation
* Encryption
* Retention policies
* Deletion workflows
* Audit logging
* Consent-aware processing
* PII protection

---

## FR-043 — PII Protection

The sentiment pipeline shall support detection and protection of sensitive customer information.

Potential PII includes:

* Names
* Email addresses
* Phone numbers
* Addresses
* Payment information
* Account identifiers
* Authentication information

---

## FR-044 — Audit Logging

The system shall record:

* Sentiment analysis events
* Model versions
* Human corrections
* Configuration changes
* Threshold changes
* Escalation events
* Data access
* Export events

---

## FR-045 — Role-Based Access Control

Access shall be controlled according to SalesGenie's RBAC model.

Example roles:

```text
Super Admin
Organization Admin
Support Manager
Support Supervisor
Human Support Agent
AI Agent
Customer Success Manager
Analyst
Auditor
End User
```

---

## FR-046 — Permission Model

Example permissions:

```text
sentiment:read
sentiment:analyze
sentiment:review
sentiment:correct
sentiment:export
sentiment:configure
sentiment:analytics
sentiment:admin
```

---

## 8. Non-Functional Requirements

## NFR-001 — Scalability

The system shall support SalesGenie's target enterprise architecture.

Target capability:

```text
10M+ users
500K+ concurrent conversations
Millions of daily interactions
Large-scale historical sentiment analysis
```

---

## NFR-002 — Availability

The sentiment subsystem should support enterprise-grade availability and graceful degradation.

If sentiment analysis is unavailable:

```text
Customer conversation continues
        ↓
Sentiment event queued
        ↓
Analysis resumes
```

Sentiment processing failure must not block customer support.

---

## NFR-003 — Latency

Real-time sentiment analysis should target low-latency processing suitable for active conversations.

Target:

```text
P50 < 300 ms
P95 < 1 second
P99 < 2 seconds
```

Actual targets shall be validated against production infrastructure and model selection.

---

## NFR-004 — Reliability

The system shall support:

* Retries
* Timeouts
* Circuit breakers
* Dead-letter queues
* Idempotency
* Duplicate-event handling
* Provider fallback
* Model fallback

---

## NFR-005 — Observability

The system shall expose:

* Request metrics
* Model latency
* Queue latency
* Error rate
* Classification distribution
* Confidence distribution
* Escalation rate
* Model drift
* Cost per analysis
* Token consumption

---

## NFR-006 — Cost Optimization

The system shall minimize unnecessary AI inference.

Optimization techniques may include:

* Small-model routing
* Caching
* Batch inference
* Event deduplication
* Context compression
* Classification models for simple cases
* LLM fallback for ambiguous cases

---

## 9. AI Decision Policy

The sentiment system shall operate according to the following hierarchy:

```text
                    Customer Interaction
                           │
                           ▼
                    Sentiment Analysis
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
         Positive       Neutral       Negative
                                         │
                                         ▼
                                  Risk Evaluation
                                         │
                         ┌───────────────┼──────────────┐
                         ▼               ▼              ▼
                       Low            Medium          High
                                                         │
                                                         ▼
                                                Human Escalation
```

AI shall not independently perform irreversible or high-impact actions solely because of sentiment classification.

---

## 10. Human-in-the-Loop Architecture

```text
Customer
   │
   ▼
Omnichannel Channel
   │
   ▼
Conversation Service
   │
   ▼
Sentiment Engine
   │
   ├── Sentiment Classification
   ├── Emotion Detection
   ├── Topic Detection
   ├── Risk Detection
   └── Sentiment Trajectory
           │
           ▼
      Decision Engine
           │
     ┌─────┴─────┐
     ▼           ▼
     AI Action   Human Review
     │           │
     ▼           ▼
 AI Response   Agent Intervention
     │           │
     └─────┬─────┘
           ▼
       Resolution
           │
           ▼
    Outcome Analysis
           │
           ▼
    Analytics + Learning
```

---

## 11. Sentiment State Machine

```text
UNKNOWN
   │
   ▼
NEUTRAL
   │
 ┌─┴──────────────┐
 ▼                ▼
POSITIVE        NEGATIVE
 │                │
 ▼                ▼
VERY_POSITIVE   VERY_NEGATIVE
                  │
                  ▼
             HUMAN_ESCALATION
                  │
                  ▼
             HUMAN_HANDOFF
                  │
                  ▼
               RESOLVED
```

The state machine shall support transitions in both directions as new evidence becomes available.

---

## 12. Example Sentiment Decision

## Input

```text
Customer:
"I have contacted support three times and nobody has fixed this.
I am extremely frustrated and will cancel my subscription if this
isn't resolved today."
```

## AI Output

```json
{
  "sentiment": "very_negative",
  "sentiment_score": -0.93,
  "intensity": 0.96,
  "emotion": "anger",
  "confidence": 0.97,
  "risk_level": "critical",
  "topics": [
    "support",
    "subscription",
    "technical_issue"
  ],
  "signals": [
    "repeated_failure",
    "frustration",
    "cancellation_intent",
    "urgency"
  ],
  "recommended_action": "human_escalation"
}
```

---

## 13. Example Hybrid Support Workflow

```text
Customer sends message
        │
        ▼
AI analyzes sentiment
        │
        ▼
Negative sentiment detected
        │
        ▼
AI attempts resolution
        │
        ▼
Sentiment deteriorates
        │
        ▼
Escalation threshold reached
        │
        ▼
Human agent notified
        │
        ▼
Conversation transferred
        │
        ▼
Human resolves issue
        │
        ▼
Sentiment becomes positive
        │
        ▼
Conversation closed
        │
        ▼
Outcome recorded
```

---

## 14. Executive Analytics Requirements

Executives shall be able to view:

* Overall customer sentiment
* Sentiment trend
* Sentiment by product
* Sentiment by channel
* Sentiment by customer segment
* Sentiment by region
* Sentiment by issue
* Sentiment-driven escalation
* Sentiment-driven churn risk
* AI vs human sentiment outcomes
* Sentiment recovery rate
* Top customer pain points
* Emerging dissatisfaction trends

---

## 15. Support Manager Requirements

Support managers shall be able to:

1. Monitor live negative sentiment.
2. Monitor critical conversations.
3. Identify recurring sentiment problems.
4. Identify unresolved customer frustration.
5. Identify problematic workflows.
6. Analyze sentiment by support queue.
7. Analyze AI-agent performance.
8. Analyze human-agent handling outcomes.
9. Review sentiment escalations.
10. Review human corrections.
11. Configure sentiment thresholds.
12. Create sentiment-triggered workflows.

---

## 16. Human Support Agent Requirements

Human agents shall receive:

```text
Customer
Current sentiment
Sentiment trend
Emotion
Risk
Topic
Root cause
Conversation history
AI summary
Recommended response strategy
Escalation reason
```

The agent shall be able to:

* Accept handoff
* Reject handoff
* Override AI sentiment
* Correct sentiment
* Add notes
* Resolve conversation
* Escalate further

---

## 17. AI Support Agent Requirements

The AI agent shall:

* Monitor sentiment continuously.
* Adjust tone dynamically.
* Avoid inappropriate sales behavior during negative sentiment.
* Detect escalation signals.
* Request human intervention when necessary.
* Preserve context during handoff.
* Record actions.
* Respect confidence thresholds.
* Avoid making unsupported emotional assumptions.
* Defer to human judgment for ambiguous or high-impact cases.

---

## 18. Analytics & Reporting Requirements

The system shall support:

### Operational Reports

* Daily sentiment report
* Weekly sentiment report
* Monthly sentiment report
* Channel sentiment report
* Agent sentiment report
* AI sentiment report
* Escalation report
* Negative sentiment report

### Strategic Reports

* Customer pain-point report
* Product sentiment report
* Churn sentiment report
* Sentiment-driven revenue risk
* Customer experience trend
* Sentiment anomaly report
* Executive sentiment intelligence

---

## 19. Alerting Rules

Organizations shall be able to define rules such as:

```text
IF sentiment = VERY_NEGATIVE
THEN create priority ticket
```

```text
IF sentiment_score < -0.80
AND confidence > 0.90
THEN notify supervisor
```

```text
IF sentiment decreases by > 0.50
THEN trigger escalation
```

```text
IF cancellation_intent = TRUE
AND sentiment < -0.60
THEN route to customer_success
```

```text
IF negative_sentiment_volume increases > 30%
THEN trigger anomaly alert
```

---

## 20. Configuration Requirements

Authorized administrators shall be able to configure:

* Sentiment thresholds
* Confidence thresholds
* Escalation rules
* Alert rules
* Notification destinations
* Supported languages
* Sentiment categories
* Emotion categories
* Topic taxonomy
* Risk thresholds
* Human-review thresholds
* Data retention
* Model selection
* Model fallback
* Workflow actions

---

## 21. Security Requirements

The system shall enforce:

* Authentication
* Authorization
* RBAC
* Tenant isolation
* API authorization
* Encryption in transit
* Encryption at rest
* Secure secrets management
* Audit logging
* Rate limiting
* Abuse protection
* Input validation
* Output validation

---

## 22. AI Safety Requirements

The system shall:

1. Avoid treating sentiment as absolute truth.
2. Provide confidence estimates.
3. Flag ambiguous cases.
4. Support human override.
5. Avoid sensitive inferences that are not necessary for support.
6. Avoid discriminatory conclusions.
7. Avoid using sentiment alone for employee employment decisions.
8. Avoid automatically taking irreversible actions solely from sentiment.
9. Preserve evidence supporting important decisions.
10. Maintain auditability of AI decisions.

---

## 23. Quality Requirements

The sentiment engine shall be evaluated across:

```text
Accuracy
Precision
Recall
F1
Calibration
Latency
False Positive Rate
False Negative Rate
Language Performance
Channel Performance
Topic Performance
Drift
Human Agreement
```

Critical sentiment classes shall receive particular attention because false negatives may cause missed escalations.

---

## 24. Acceptance Criteria

The feature shall be considered production-ready when:

* [ ] Real-time sentiment analysis works.
* [ ] Historical sentiment analysis works.
* [ ] Message-level sentiment works.
* [ ] Conversation-level sentiment works.
* [ ] Ticket-level sentiment works.
* [ ] Customer-level aggregation works.
* [ ] Sentiment trajectory works.
* [ ] Sentiment deterioration detection works.
* [ ] Sentiment recovery detection works.
* [ ] Emotion detection works.
* [ ] Topic + sentiment correlation works.
* [ ] Sentiment root-cause detection works.
* [ ] Confidence scoring works.
* [ ] Human review works.
* [ ] Human correction works.
* [ ] AI-agent sentiment awareness works.
* [ ] Human-agent sentiment assistance works.
* [ ] Sentiment-based routing works.
* [ ] Sentiment-based escalation works.
* [ ] Omnichannel processing works.
* [ ] Multilingual processing works.
* [ ] Sentiment dashboards work.
* [ ] Sentiment APIs work.
* [ ] Event-driven processing works.
* [ ] RBAC is enforced.
* [ ] Tenant isolation is verified.
* [ ] Audit logging works.
* [ ] PII protection works.
* [ ] Model versioning works.
* [ ] Model evaluation works.
* [ ] Model drift monitoring works.
* [ ] Failure fallback works.
* [ ] Queue retry and dead-letter handling works.
* [ ] Observability dashboards work.
* [ ] Cost monitoring works.
* [ ] Human override works.
* [ ] AI recommendations are not treated as authoritative without required approval.
* [ ] Security testing passes.
* [ ] Load testing passes.
* [ ] Accessibility testing passes.
* [ ] Production rollback is available.

---

## 25. FAANG-Level Definition of Done

Touch Sentiment Analysis shall not be considered complete merely because a sentiment label is displayed.

A production-grade implementation must provide:

```text
Data Ingestion
        ↓
Normalization
        ↓
Language Detection
        ↓
Sentiment Classification
        ↓
Emotion Detection
        ↓
Topic Detection
        ↓
Context Analysis
        ↓
Confidence Estimation
        ↓
Sentiment Trajectory
        ↓
Risk Detection
        ↓
Root Cause Analysis
        ↓
Decision Engine
        ↓
AI Response Adaptation
        ↓
Human Escalation
        ↓
Workflow Automation
        ↓
Analytics
        ↓
Human Review
        ↓
Feedback
        ↓
Model Evaluation
        ↓
Drift Detection
        ↓
Continuous Improvement
```

The final system must therefore operate as a **closed-loop Customer Sentiment Intelligence Platform**, not merely as a sentiment classifier.

---

## 26. Core Product Principle

> **SalesGenie should not only determine whether a customer is positive or negative. It should understand how the customer's emotional state is changing, why it is changing, what business risk that change represents, and what AI or human action should occur next.**

This principle shall guide the architecture, AI models, workflows, dashboards, APIs, human-review mechanisms, and production implementation of Touch Sentiment Analysis.
