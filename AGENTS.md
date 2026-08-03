# Antigravity System Instruction & Engineering Workflow Protocol

This file serves as the core operational harness for the workspace AI agents. It overrides default model behaviors to restrict hallucination, enforce predictable system architecture evolution, and guarantee full-stack contract compliance.

All generation pipelines, code refactoring tasks, and feature loops must execute exactly according to the strict modular sequence below.

---

## 1. Architectural Development Sequence

When writing, editing, or evaluating codebase changes, you must parse and process the foundational layout components sequentially. Do not initialize client-side components until the complete service contract and data layers are fully realized.

### Phase A: Core Service Layer, Architecture & AI Orchestration
--architecture-patterns --backend-architect --database-architect --fastapi-development --fastapi-expert --fastapi-microservices-serverless --fastapi-python --langchain --langgraph --langgraph-human-in-the-loop --llm --llm-application-dev-langchain-ag... --prompt-engineering --pydantic-ai-agent --python-backend --python-backend-expert --python-fastapi-development --rag-agent-builder --rag-implementation --rag-retrieval --software-architecture --system-architect

### Phase B: Client Application, Frameworks & Deployment
--astro --astro-framework --deploy-to-vercel --frontend-developer --nextjs-best-practices --nextjs-react-typescript --react-modernization --tailwind-4-docs --typescript-react-patterns --vercel-cli-with-tokens --vercel-composition-patterns --vercel-optimize --vercel-react-best-practices --vercel-react-native-skills --vercel-react-view-transitions --web-design-guidelines --writing-guidelines

---

## 2. Global Design Contract Alignment

Before finalizing any full-stack implementation, compiling component libraries, or establishing state synchronization boundaries, you must strictly validate the codebase state against the primary structural specification:

--- Design.md

---

## 3. Core Developer Constraints
- **Zero Hallucination:** If a skill folder is omitted from the tracks above, do not implement it unless explicitly requested.
- **Contract First:** Always inspect data serialization models, schemas, and API routes inside the backend pipeline prior to constructing UI pages or hooks.
- **State Integrity:** Keep business logic completely decoupled from presentational components.

## 4. Security Development Protocol

### Security-First Development
Never commit code that introduces security vulnerabilities. All changes must pass security validation:

#### Input Validation Requirements
- All user inputs must be sanitized using `security_protection.py` sanitizers
- SQL injection protection must be applied to all database queries
- XSS protection required for all string outputs
- File path validation for any file operations

#### Secrets Management
- No secrets in source code (enforced by `secrets_detector` scan)
- Use environment variables or secret managers only
- Rotate API keys every 90 days minimum

#### Rate Limiting
- Apply rate limits to all public endpoints
- Stricter limits on authentication endpoints
- Adaptive throttling during high traffic

#### Container Security
- Use `dockerfile` with non-root user
- Scan images with `trivy` or `clair` before deployment
- Enable security scanning in CI/CD pipeline

#### Runtime Protection
- Enable `PYTHONSAFEPATH=1` in all services
- Set appropriate resource limits (memory, CPU)
- Enable watchdog monitoring for process health

### Security Testing Pipeline
All changes trigger:
1. SAST scan (`bandit` or `semgrep`)
2. Dependency scan (`safety` or `pip-audit`)
3. Container scan (`trivy`)
4. Security integration tests

### Incident Response
On security alert:
1. Isolate affected services
2. Review audit logs
3. Apply IP blocks via `security_manager`
4. Generate incident report
5. Notify security team within 5 minutes

### High Availability Requirements
- Services must be accessible via load balancer
- Circuit breakers must protect against cascade failures
- Auto-scaling triggers at 80% resource utilization
- Graceful degradation during partial outages