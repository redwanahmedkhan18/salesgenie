```md id="p5r8kx"
# SalesGenie Prompt Engineering Standards

## Enterprise AI Prompt Architecture & Engineering Guidelines

**Project:** SalesGenie  
**Platform:** AI Customer Support & Sales Agent Platform  
**Document Version:** 1.0  
**Document Type:** Prompt Engineering Standard  


---

# Table of Contents

1. Introduction
2. Prompt Engineering Philosophy
3. Prompt Architecture Principles
4. Prompt Lifecycle Management
5. Prompt Design Standards
6. System Prompt Standards
7. Developer Prompt Standards
8. User Prompt Handling
9. Context Engineering Standards
10. Role-Based Prompt Design
11. AI Agent Prompt Architecture
12. Customer Support Agent Prompts
13. Sales Agent Prompts
14. Lead Qualification Prompts
15. RAG Prompt Standards
16. Retrieval Context Prompts
17. Tool Calling Prompts
18. Function Calling Standards
19. Memory Prompt Architecture
20. Conversation Management Prompts
21. Safety and Guardrail Prompts
22. Prompt Security Standards
23. Prompt Versioning
24. Prompt Evaluation Framework
25. Prompt Testing Strategy
26. Prompt Monitoring
27. Production Prompt Checklist


---

# 1. Introduction


## 1.1 Purpose


This document defines prompt engineering standards for SalesGenie.


SalesGenie uses Large Language Models to power:


- AI customer support agents
- AI sales representatives
- AI workflow automation
- AI knowledge assistants
- Enterprise business automation


The purpose of this standard is to create reliable, secure, and scalable AI behavior.


---

## 1.2 Scope


This standard applies to:


- System prompts
- Agent prompts
- RAG prompts
- Tool prompts
- Workflow prompts
- Safety prompts
- Evaluation prompts


---

# 2. Prompt Engineering Philosophy


SalesGenie follows enterprise prompt engineering principles:


```

Clear Instructions

*

Relevant Context

*

Controlled Behavior

*

Reliable Output

*

Continuous Evaluation

```


---

# 2.1 Prompt Engineering Goals


Prompts must:


- Reduce hallucination
- Improve accuracy
- Maintain consistency
- Control AI behavior
- Improve user experience


---

# 3. Prompt Architecture Principles


SalesGenie prompts follow layered architecture.


```

System Instructions

```
    +
```

Developer Instructions

```
    +
```

Business Rules

```
    +
```

Retrieved Knowledge

```
    +
```

Conversation Context

```
    +
```

User Input

```
    |

    V

  LLM Response
```

```


---

# 3.1 Prompt Hierarchy


Priority order:


```

1. System Prompt

2. Security Rules

3. Business Rules

4. Developer Instructions

5. Retrieved Context

6. User Message

```


Higher priority instructions override lower priority instructions.


---

# 4. Prompt Lifecycle Management


Prompt lifecycle:


```

Design

|

Review

|

Testing

|

Deployment

|

Monitoring

|

Optimization

````


---

# 4.1 Prompt Ownership


Every production prompt must have:


```json
{
"prompt_id":"support_agent_v1",

"owner":"ai_team",

"version":"1.0",

"status":"production"
}
````

---

# 5. Prompt Design Standards

Every prompt must contain:

```
Role

Objective

Context

Instructions

Constraints

Output Format

Examples

```

---

# 5.1 Prompt Structure Template

```text
ROLE:

You are a specialized AI assistant.


OBJECTIVE:

Your goal is to help users achieve a specific task.


CONTEXT:

Use provided business information.


INSTRUCTIONS:

Follow these rules.


CONSTRAINTS:

Do not perform restricted actions.


OUTPUT FORMAT:

Return structured responses.

```

---

# 6. System Prompt Standards

System prompts define AI identity and behavior.

Example:

```text
You are SalesGenie AI Customer Support Agent.

Your responsibility is to provide accurate,
professional and helpful customer support.

Always use company knowledge before answering.

Never invent unsupported information.

Escalate complex issues to human agents.

```

---

# 6.1 System Prompt Requirements

Must include:

* AI role
* Business objective
* Safety rules
* Response behavior
* Limitations

---

# 7. Developer Prompt Standards

Developer prompts define application behavior.

Example:

```text
Follow SalesGenie support policies.

Prioritize customer satisfaction.

Use available tools when required.

Return structured JSON responses.

```

---

# 8. User Prompt Handling

User input must be:

* Sanitized
* Validated
* Classified

Pipeline:

```
User Message

      |

Input Validation

      |

Intent Detection

      |

Prompt Construction

      |

LLM Execution

```

---

# 9. Context Engineering Standards

Context is critical for AI accuracy.

Context sources:

```
Conversation History

+

Customer Profile

+

Retrieved Documents

+

Business Rules

+

Previous Actions

```

---

# 9.1 Context Optimization

Avoid:

* Irrelevant information
* Duplicate content
* Excessive history

Use:

* Summarization
* Context ranking
* Token management

---

# 10. Role-Based Prompt Design

SalesGenie uses specialized AI roles.

Examples:

```
Customer Support Agent

Sales Development Representative

Knowledge Assistant

Workflow Agent

Analytics Assistant

```

---

# 11. AI Agent Prompt Architecture

Agent prompt structure:

```
Agent Identity

        |

Goal Definition

        |

Available Tools

        |

Decision Rules

        |

Execution Policy

        |

Response Format

```

---

# 11.1 Agent Prompt Example

```text
You are SalesGenie Sales Agent.

Your goal is to qualify leads and schedule meetings.

You can use CRM tools.

Always verify customer information.

Do not promise unavailable products.

```

---

# 12. Customer Support Agent Prompts

Example:

```text
You are an enterprise customer support assistant.

Responsibilities:

- Answer customer questions
- Resolve common issues
- Retrieve knowledge articles
- Escalate complex cases


Rules:

- Be polite
- Be accurate
- Never fabricate solutions

```

---

# 12.1 Support Escalation Prompt

```text
If the issue requires human intervention:

1. Explain the limitation.

2. Create escalation request.

3. Provide customer summary.

```

---

# 13. Sales Agent Prompts

Example:

```text
You are an AI sales development representative.

Your goals:

- Understand customer needs
- Qualify leads
- Recommend solutions
- Schedule meetings


Never pressure customers.

Always personalize communication.

```

---

# 14. Lead Qualification Prompts

Framework:

```
Customer Need

+

Budget

+

Authority

+

Timeline

+

Intent

```

Example:

```text
Analyze the lead information.

Classify the lead:

HOT

WARM

COLD


Provide reasoning and recommended action.

```

---

# 15. RAG Prompt Standards

RAG prompts must enforce grounded responses.

Template:

```text
Answer the question using only the provided context.

If the answer is unavailable:

Say:
"I do not have enough information."

Context:

{retrieved_documents}


Question:

{user_query}

```

---

# 15.1 RAG Response Rules

AI must:

* Cite retrieved information
* Avoid assumptions
* Maintain factual accuracy

---

# 16. Retrieval Context Prompts

Example:

```text
You are given company knowledge.

Select only information relevant to the user's question.

Ignore unrelated documents.

```

---

# 17. Tool Calling Prompts

Tools must have clear descriptions.

Example:

```text
Tool:

create_ticket


Purpose:

Creates customer support tickets.


Use when:

Customer reports unresolved problems.

```

---

# 17.1 Tool Usage Rules

Agents must:

* Validate inputs
* Use correct tools
* Handle failures
* Explain actions

---

# 18. Function Calling Standards

Functions require:

```json
{
"name":"create_customer",

"description":"Creates a customer record",

"parameters":{
"name":"string",
"email":"string"
}
}
```

---

# 19. Memory Prompt Architecture

Memory types:

```
Short-Term Memory

Conversation Context


Long-Term Memory

Customer Preferences


Business Memory

Company Knowledge

```

---

# 19.1 Memory Rules

AI should:

* Store useful information
* Respect privacy
* Avoid sensitive storage

---

# 20. Conversation Management Prompts

Conversation rules:

```text
Maintain conversation context.

Remember previous messages.

Ask clarification when required.

Provide concise answers.

```

---

# 21. Safety and Guardrail Prompts

Safety prompt example:

```text
You must follow company policies.

Do not reveal confidential information.

Do not bypass security controls.

Do not execute unauthorized actions.

```

---

# 22. Prompt Security Standards

Protect against:

```
Prompt Injection

Jailbreak Attempts

Data Extraction

Instruction Manipulation

```

---

# 22.1 Prompt Injection Defense

Use:

```
Input Filtering

Instruction Separation

Context Isolation

Output Validation

```

---

# 23. Prompt Versioning

Every prompt requires version control.

Example:

```
support_agent_prompt_v1.0

support_agent_prompt_v1.1

support_agent_prompt_v2.0

```

---

# 23.1 Prompt Change Rules

Changes require:

* Testing
* Evaluation
* Approval
* Documentation

---

# 24. Prompt Evaluation Framework

Evaluate:

## Accuracy

```
Correct Answers

Relevant Responses

```

---

## Safety

```
Policy Compliance

No Data Leakage

```

---

## Performance

```
Latency

Token Usage

Cost

```

---

# 25. Prompt Testing Strategy

Testing includes:

```
Unit Prompt Tests

Regression Tests

A/B Testing

Human Evaluation

Adversarial Testing

```

---

# 25.1 Test Cases

Example:

Input:

```
Customer asks refund policy.

```

Expected:

```
AI retrieves refund policy.

Provides accurate answer.

```

---

# 26. Prompt Monitoring

Monitor:

```
Response Quality

User Feedback

Token Usage

Failure Rate

Hallucination Rate

```

---

# 26.1 Prompt Analytics

Track:

```json
{
"prompt_version":"1.0",

"model":"gpt-model",

"tokens_used":1200,

"quality_score":0.92
}
```

---

# 27. Production Prompt Checklist

Before production:

```
✓ Prompt Reviewed

✓ Security Rules Added

✓ Tested Against Edge Cases

✓ RAG Context Validated

✓ Output Format Verified

✓ Version Created

✓ Monitoring Enabled

✓ Cost Evaluated

✓ Rollback Available

```

---


```
```
