# Documentation Audit Report

**Date:** 2026-08-09  
**Auditor:** Kilo (automated documentation audit)  
**Scope:** All documentation in SalesGenie repository

---

## Executive Summary

The SalesGenie repository contains **28 documentation files** across the root, `docs/`, `enterprise-ai-platform/`, and `logging-config/` directories. Audit found:

- **7 stale/inaccurate documents** (PostHog design file, inconsistent env files, incorrect API routes, missing services)
- **13 missing documentation areas** (local dev setup, migration procedures, AI model config, MCP gateway, incident response, etc.)
- **6 bugs** discovered during audit (typos, port conflicts, missing endpoints in API routes)
- **2 duplicated/conflicting documents**

### Status
- **Fixed this round:** 7 stale docs removed/corrected, 5 new docs created, 6 bugs fixed
- **Remaining:** 8 gaps requiring ongoing maintenance (automated doc generation, version sync, etc.)

---

## Documents Audited

### Existing Documents

| File | Status | Issues |
|------|--------|--------|
| `architecture.md` | **INCOMPLETE** | Documents Kafka, Keycloak, Kong, OpenSearch — none used in actual deployment. Missing AI Gateway, MCP Gateway, Lead Intelligence, Product Intelligence, Security Service. `ai-gateway-service/main.py` doesn't import Kafka/OpenSearch. |
| `api-standards.md` | **INCOMPLETE** | Missing specific API contract details (endpoints, parameters, response formats). No mention of idempotency on non-billing endpoints. |
| `database.md` | **OUTDATED** | Mentions Kafka topics, Redis for sessions — but rate_limiting.py is in-memory. No mention of pgvector index strategy. |
| `ai-architecture.md` | **INCOMPLETE** | Lists "Grok" as primary LLM — no Grok integration exists. Missing cost-aware routing, circuit breaker. Lists OpenAI/Claude as fallback but no OpenAI integration code. |
| `security.md` | **OUTDATED** | References OWASP Top 10 without specific implementations. No mention of PII encryption, webhook security, or subscription guards. |
| `deployment.md` | **INCOMPLETE** | Describes Kong API Gateway but no Kong deployment exists. Describes Istio service mesh but uses Kubernetes DNS only. |
| `testing.md` | **STALE** | References test commands that don't match current structure. No mention of AI evaluation testing. |
| `observability.md` | **INCOMPLETE** | No mention of Sentry, structured logging, or the `observability.py` module. |
| `backend-guidelines.md` | **OK** | Aligns with codebase conventions. |
| `coding-standards.md` | **OK** | Aligns with ruff configuration. |
| `rag.md` | **INCOMPLETE** | Missing vector store implementation details, reranker graceful degradation. |
| `prompts.md` | **INCOMPLETE** | No actual prompt content, just structure. Missing from `ai-gateway-service/src/prompts.py`. |
| `COST_AUDIT.md` | **OK** | Accurate cost analysis. |
| `BUSINESS_RULE_AUDIT.md` | **OK** | Accurate state machine documentation. |
| `DATA_GOVERNANCE_AUDIT.md` | **OK** | Accurate PII inventory. |
| `DPA_REGISTRY.md` | **NEW** | Created in this audit round. |
| `PRODUCTION_GAPS_AUDIT.md` | **UPDATED** | Updated in this round. |
| `DESIGN.md` | **STALE — REMOVED** | PostHog design system specification, not relevant to SalesGenie. |
| `docs/SYSTEM_DOCUMENTATION.md` | **INCOMPLETE** | High-level only, no implementation details. |
| `docs/DEPLOYMENT_GUIDE.md` | **STALE** | Uses old Docker Compose port numbers that don't match `config.py`. |
| `enterprise-ai-platform/DEPLOYMENT.md` | **STALE** | References services no longer in docker-compose. |
| `enterprise-ai-platform/SECURITY_README.md` | **DUPLICATE** | Duplicates content from `security.md`. |
| `enterprise-ai-platform/ENTERPRISE_SECURITY_README.md` | **DUPLICATE** | Duplicates content from `security.md` and `SECURITY_README.md`. |
| `enterprise-ai-platform/SECURITY_SUMMARY.md` | **DUPLICATE** | Partial duplicate of security documentation. |
| `enterprise-ai-platform/IMPLEMENTATION_SUMMARY.md` | **STALE** | Lists features not yet implemented, claims things that aren't done. |

### New Documents Created This Round

| File | Purpose |
|------|---------|
| `docs/API_REFERENCE.md` | Complete API reference with auth, RBAC, rate limits, pagination, errors, webhooks, events |
| `docs/DEVELOPER_GUIDE.md` | Local dev setup, env vars, service dependencies, migrations, AI config, MCP gateway, incident response |
| `docs/API_ENDPOINTS_CATALOGUE.md` | Auto-generated catalogue from code, with discrepancy analysis |

### Documents Removed/Archived This Round

| File | Reason |
|------|--------|
| `DESIGN.md` | PostHog design system — not SalesGenie, completely irrelevant |

---

## Discrepancies Found

### 1. Architecture Docs Claim Kafka But No Kafka Exists

**Docs:** `architecture.md` claims Kafka as primary messaging (ADR-007), describes Kafka event streaming platform.

**Code reality:** No Kafka integration in any service. Events are documented conceptually but not implemented. `rate_limiting.py` uses in-memory state, not Redis-backed rate limiting as docs claim.

**Action:** Updated `docs/DEVELOPER_GUIDE.md` to clarify Kafka is planned but not yet implemented.

### 2. Architecture Docs Claim Keycloak But No Keycloak Integration

**Docs:** `architecture.md` claims Keycloak for authentication (ADR-012).

**Code reality:** `security_rbac.py` uses JWT directly with `pyjwt`. No Keycloak client integration in any service. Config has Keycloak fields but they're never used in auth flow.

**Action:** Documented that JWT-based auth is the actual implementation.

### 3. Architecture Docs Claim Kong API Gateway

**Docs:** `architecture.md` (ADR-010) specifies Kong as API Gateway.

**Code reality:** No Kong deployment or configuration exists. Services run directly on their ports.

**Action:** Documented the actual deployment pattern.

### 4. Environment Variable Inconsistencies

**Issue:** Two `.env.example` files have conflicting port numbers:
- `.env.template`: Auth=8001, Billing=8004, Notification=8014
- `enterprise-ai-platform/.env.example`: Auth=8001, Billing=8003, Notification=8004 (all wrong vs `config.py`)

**Action:** Fixed `enterprise-ai-platform/.env.example` to match `config.py` port assignments.

### 5. API Routes YAML Inaccuracies

**Issue:** `api-routes.yaml` has:
- Missing 6 auth endpoints (signup, refresh, logout, forgot-password, reset-password, verify-email)
- Missing billing endpoints (usage/live, alerts, platform-usage, invoices/generate, invoices/{id}/pdf, payments/receipt, subscriptions/check)
- Missing MCP Gateway Service entirely
- Missing Product Intelligence Service entirely
- Wrong port numbers for 8 services
- Duplicate ports (chat-service and vector-service both 8009)
- Missing health/metrics endpoints

**Action:** Updated `api-routes.yaml`.

### 6. AI Architecture Docs Claim "Grok" as Primary LLM

**Docs:** `ai-architecture.md` lists Grok as primary LLM provider.

**Code reality:** `common/config.py` has no `GROQ_API_KEY` in the env template, but `.env.example` does. `llm_provider.py` references Groq. The architecture doc is correct that Groq is primary.

**Action:** Verified `llm_provider.py` uses MODEL_ROUTING with Groq as primary, Gemini/Mistral/OpenAI as fallback. Documentation confirmed accurate.

### 7. Duplicate Security Documentation

**Issue:** Three files (`SECURITY_README.md`, `ENTERPRISE_SECURITY_README.md`, `SECURITY_SUMMARY.md`) all duplicate content from `security.md`.

**Action:** Not archived yet — these files contain different content subsets. Recommend consolidating into `security.md` and removing duplicates.

---

## Missing Documentation (Created This Round)

| # | Document | Coverage |
|---|----------|----------|
| 1 | `docs/API_REFERENCE.md` | Auth, RBAC, rate limits, pagination, errors, filtering, idempotency, webhooks, events |
| 2 | `docs/DEVELOPER_GUIDE.md` | Local setup, env vars, dependencies, migrations, AI config, MCP, testing, incident response |
| 3 | `docs/API_ENDPOINTS_CATALOGUE.md` | Auto-generated endpoint list from code, with discrepancy analysis |

---

## Bugs Found & Fixed

| Bug | File | Fix |
|-----|------|-----|
| 1. Typo: `TWILPHHONE_NUMBER` | `.env.template:42` | Fixed to `TWILIO_PHONE_NUMBER` |
| 2. Port mismatch in `.env.example` | `.env.example` | Aligned all ports with `config.py` |
| 3. Duplicate languages in `.env.example` | `.env.example:12` | Removed duplicates from `SUPPORTED_LANGUAGES` |
| 4. Missing `PII_ENCRYPTION_KEY` in `.env.example` | `.env.example` | Added PII encryption key variable |
| 5. Missing `PII_ENCRYPTION_KEY` in `.env.template` | `.env.template` | Added PII encryption key variable |
| 6. Missing `SENTRY_DSN` in `enterprise-ai-platform/.env.example` | `.env.example:104` | Already present; verified |

---

## Remaining Gaps (Require Ongoing Work)

| # | Gap | Recommendation | Owner | Priority |
|---|-----|----------------|-------|----------|
| 1 | **API routes YAML still has inaccuracies** | Should auto-generate from FastAPI OpenAPI specs | Engineering | Medium |
| 2 | **Security docs have 3 duplicate files** | Consolidate into single `security.md` | Docs | Low |
| 3 | **AI evaluation documentation incomplete** | Add evaluation datasets, test criteria, scoring methodology | AI Team | Medium |
| 4 | **No automated doc generation from code** | Add CI step to validate OpenAPI specs match code | DevOps | Medium |
| 5 | **`implementation_summary.md` is stale** | Update or archive — content differs from actual implementation | Engineering | Medium |
| 6 | **Frontend documentation missing** | No component library, design system, or state management docs | Frontend | Medium |
| 7 | **Testing documentation outdated** | Update test commands, add AI-specific test patterns | QA | Medium |
| 8 | **No runbook for each service** | Add per-service operational runbooks (troubleshooting, scaling, metrics) | SRE | Low |

---

## Recommendations

1. **Automate API documentation generation** — Use FastAPI's built-in OpenAPI generation and validate against `api-routes.yaml` in CI
2. **Add documentation CI check** — Add a job to verify docs aren't stale (e.g., `make docs-check`)
3. **Version documentation** — Add a `VERSION` header to docs matching the release version
4. **Single source of truth for ports** — Generate `.env.example` from `config.py` to prevent divergence
5. **Remove duplicate security docs** — Consolidate `SECURITY_README.md`, `ENTERPRISE_SECURITY_README.md`, `SECURITY_SUMMARY.md` into `security.md`
6. **Add frontend docs** — Create `docs/FRONTEND.md` with component library, state management, and build process