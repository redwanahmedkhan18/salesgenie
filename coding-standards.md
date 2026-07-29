```md
# SalesGenie Coding Standards

## Enterprise Software Engineering Guidelines

**Project:** SalesGenie  
**Platform:** AI Customer Support & Sales Agent Platform  
**Document Version:** 1.0  
**Document Type:** Coding Standards & Engineering Practices  


---

# Table of Contents

1. Introduction
2. Coding Philosophy
3. General Coding Principles
4. Software Design Principles
5. Backend Coding Standards
6. Python Coding Standards
7. Django/FastAPI Standards
8. API Development Standards
9. Database Coding Standards
10. Frontend Coding Standards
11. TypeScript Standards
12. React/Next.js Standards
13. AI/ML Coding Standards
14. RAG Development Standards
15. Agent Development Standards
16. Error Handling Standards
17. Logging Standards
18. Security Coding Standards
19. Testing Standards
20. Git Standards
21. Code Review Standards
22. Documentation Standards
23. Performance Standards
24. Production Readiness Checklist


---

# 1. Introduction


## 1.1 Purpose


This document defines coding standards and engineering practices for SalesGenie.


The purpose is to ensure:


- High-quality software development
- Maintainable codebase
- Scalable architecture
- Secure implementation
- Consistent engineering practices
- Enterprise-level reliability


---

## 1.2 Scope


These standards apply to:


- Backend development
- Frontend development
- AI/ML development
- Database development
- API development
- Infrastructure code
- Testing code


---

# 2. Coding Philosophy


SalesGenie follows professional software engineering principles:


```

Readable Code

*

Maintainable Architecture

*

Security First

*

Test Driven Development

*

Continuous Improvement

````


---

# 2.1 Code Quality Principles


Every code contribution must prioritize:


## Readability


Code should be easy for another engineer to understand.


Bad:


```python
x = a+b*c
````

Good:

```python
total_price = base_price + tax_amount * quantity
```

---

## Simplicity

Avoid unnecessary complexity.

Prefer:

* Simple functions
* Clear naming
* Small modules

Avoid:

* Over-engineering
* Deep inheritance
* Duplicate logic

---

## Maintainability

Code should support:

* Future features
* Team collaboration
* Easy debugging

---

# 3. General Coding Principles

## 3.1 DRY Principle

Do not repeat yourself.

Bad:

```python
send_email(user1)
send_email(user2)
send_email(user3)
```

Good:

```python
for user in users:
    send_email(user)
```

---

## 3.2 SOLID Principles

SalesGenie follows SOLID design principles.

## Single Responsibility Principle

A class should have one responsibility.

Bad:

```python
class UserManager:

    def create_user():
        pass

    def send_email():
        pass

    def generate_report():
        pass
```

Good:

```python
class UserService:
    pass


class EmailService:
    pass


class ReportService:
    pass
```

---

## Open/Closed Principle

Software should be open for extension and closed for modification.

---

## Liskov Substitution Principle

Child classes must replace parent classes safely.

---

## Interface Segregation Principle

Avoid large interfaces.

---

## Dependency Inversion Principle

Depend on abstractions, not concrete implementations.

---

# 4. Naming Conventions

## 4.1 Variables

Use descriptive names.

Bad:

```python
x = get_customer()
```

Good:

```python
customer = get_customer()
```

---

## 4.2 Functions

Functions should use verbs.

Good:

```python
create_customer()

validate_token()

generate_embedding()

process_payment()
```

---

## 4.3 Classes

Classes use PascalCase.

Example:

```python
class CustomerService:
    pass
```

---

## 4.4 Constants

Use uppercase.

Example:

```python
MAX_RETRY_COUNT = 3
```

---

# 5. Backend Coding Standards

SalesGenie backend follows:

* Clean architecture
* Domain-driven design
* Service-oriented design

Architecture:

```
API Layer

     |

Application Layer

     |

Domain Layer

     |

Infrastructure Layer

```

---

# 5.1 Backend Folder Structure

Recommended:

```
backend/

├── apps/

│   ├── users/

│   ├── customers/

│   ├── agents/

│   ├── workflows/


├── services/

├── repositories/

├── core/

├── config/

├── tests/

└── manage.py

```

---

# 5.2 Business Logic Rules

Business logic must not exist inside:

* Controllers
* Views
* API routes

Bad:

```python
def create_agent(request):

    save_database()
    call_llm()
    send_email()

```

Good:

```python
def create_agent():

    agent_service.create()

```

---

# 6. Python Coding Standards

SalesGenie Python follows PEP 8.

---

## 6.1 Formatting

Use:

* Black formatter
* Ruff linting
* isort imports

Example:

```python
from typing import List

from services.agent import AgentService
```

---

## 6.2 Type Hints

Always use type hints.

Bad:

```python
def create_agent(name):
    pass
```

Good:

```python
def create_agent(name: str) -> Agent:
    pass
```

---

## 6.3 Function Size

Functions should be:

* Short
* Focused
* Testable

Recommended:

```
< 50 lines

```

---

# 7. Django/FastAPI Standards

## API Views

Views should only handle:

* Request
* Validation
* Response

Example:

```python
def create_agent(request):

    data = serializer.validate()

    return agent_service.create(data)

```

---

# 7.1 Service Layer Pattern

Business logic belongs in services.

Example:

```
views.py

     |

services.py

     |

repositories.py

     |

database

```

---

# 8. Database Coding Standards

## 8.1 Query Optimization

Avoid:

```python
for customer in customers:
    customer.orders.all()
```

Use:

```python
Customer.objects.prefetch_related(
    "orders"
)
```

---

## 8.2 Database Naming

Tables:

```
users

customers

ai_agents

workflows

conversations

```

---

## 8.3 Migration Standards

Every schema change requires:

* Migration file
* Review
* Testing

---

# 9. Frontend Coding Standards

SalesGenie frontend follows:

* Component-driven architecture
* Type safety
* Clean UI patterns

---

# 9.1 Component Rules

Components should:

* Have one responsibility
* Be reusable
* Avoid business logic

Bad:

```
LargeComponent.tsx

1000+ lines

```

Good:

```
components/

CustomerCard.tsx

AgentCard.tsx

ChatWindow.tsx

```

---

# 10. TypeScript Standards

Always enable:

```json
{
"strict": true
}
```

---

## Avoid any

Bad:

```typescript
let data:any;
```

Good:

```typescript
let customer:Customer;
```

---

# 11. React / Next.js Standards

## Component Naming

Use PascalCase:

```typescript
CustomerDashboard

AgentBuilder

ChatInterface
```

---

## Hooks Rules

Custom hooks:

```typescript
useCustomer()

useAgent()

useWorkflow()
```

---

## State Management

Use:

* React Query
* Zustand
* Redux Toolkit

Avoid excessive global state.

---

# 12. AI/ML Coding Standards

AI code must be:

* Reproducible
* Version controlled
* Observable

---

# 12.1 Model Versioning

Track:

```
Model Version

Dataset Version

Training Parameters

Evaluation Results

```

---

# 12.2 ML Pipeline Structure

Recommended:

```
ml/

├── data/

├── preprocessing/

├── models/

├── training/

├── evaluation/

└── deployment/

```

---

# 13. RAG Development Standards

RAG implementations must include:

* Document versioning
* Embedding versioning
* Retrieval evaluation
* Metadata filtering

---

Example:

```python
retrieve_documents(
    query=query,
    organization_id=organization_id
)
```

---

# 14. AI Agent Coding Standards

AI agents must have:

```
Agent Definition

+

Tools

+

Memory

+

Policies

+

Evaluation

```

---

Agent code example:

```python
class SalesAgent:

    def execute(self, task):
        pass
```

---

# 15. Error Handling Standards

Never expose internal errors.

Bad:

```json
{
"error":"database password incorrect"
}
```

Good:

```json
{
"error":{
"code":"DATABASE_ERROR",
"message":"Unable to process request"
}
}
```

---

# 16. Logging Standards

Use structured logging.

Example:

```json
{
"event":"agent_execution",

"user_id":"123",

"status":"success",

"duration":250
}
```

---

# 17. Security Coding Standards

Developers must:

* Validate input
* Encrypt sensitive data
* Avoid hardcoded secrets
* Use environment variables

Bad:

```python
API_KEY="12345"
```

Good:

```python
API_KEY=os.getenv("API_KEY")
```

---

# 18. Testing Standards

Every feature requires:

* Unit tests
* Integration tests
* API tests

Testing pyramid:

```
          E2E Tests

       Integration Tests

     Unit Tests

```

---

# 19. Git Standards

## Commit Format

Use:

```
type(scope): description

```

Examples:

```
feat(agent): add AI sales agent

fix(api): resolve authentication bug

docs(rag): update architecture

```

---

# 20. Code Review Standards

Every pull request must verify:

* Code quality
* Security
* Testing
* Documentation
* Performance

---

# 21. Documentation Standards

Code documentation must include:

* Purpose
* Parameters
* Return values
* Examples

Example:

```python
def generate_response(query:str)->str:
    """
    Generate AI response.

    Args:
        query:
            User question.

    Returns:
        Generated response.
    """
```

---

# 22. Performance Standards

Developers must optimize:

* Database queries
* API latency
* AI inference cost
* Memory usage

---

# 23. Production Readiness Checklist

Before production:

```
✓ Code reviewed

✓ Tests passing

✓ Security checked

✓ Documentation updated

✓ Monitoring added

✓ Error handling implemented

✓ Performance validated

✓ Deployment verified

```

---



```
```
