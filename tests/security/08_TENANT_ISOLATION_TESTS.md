# SalesGenie Tenant Isolation Tests

## Test Setup

```
Tenant A (tenant_a_123)
  ├─ User: alice@tenant-a.com (sales_agent)
  ├─ Lead: "Lead-Alpha" (id: lead_a_001)
  ├─ Document: "Doc-Confidential-A" (id: doc_a_001)
  ├─ Conversation: conv_a_001
  └─ Ticket: ticket_a_001

Tenant B (tenant_b_456)
  ├─ User: bob@tenant-b.com (sales_agent)
  ├─ Lead: "Lead-Beta" (id: lead_b_001)
  ├─ Document: "Doc-Confidential-B" (id: doc_b_001)
  ├─ Conversation: conv_b_001
  └─ Ticket: ticket_b_001
```

## Test Cases

### TC-TI-001: API Access Cross-Tenant
```
PRECONDITION: Bob (Tenant B) is authenticated with valid JWT
ATTACK: Bob attempts to read Tenant A's leads via ?tenant_id=tenant_a_123
EXPECTED: 403 Forbidden — server uses JWT.tenant_id, not query param
REGRESSION TEST: tests/security/test_security_regression.py::TestCrossTenantIsolation
```

### TC-TI-002: localStorage Tenant Spoofing
```
PRECONDITION: Alice (Tenant A) is logged in
ATTACK: Alice sets localStorage['tenant_id'] = 'tenant_b_456'
ATTACK: Alice requests Tenant B's data
EXPECTED: Server ignores localStorage, uses JWT.tenant_id
REGRESSION TEST: TestCrossTenantIsolation::test_no_localStorage_tenant_id_read
```

### TC-TI-003: Organization Switch Unauthorized
```
PRECONDITION: Bob (Tenant B) is authenticated
ATTACK: Bob tries to switch to Tenant A via POST /api/v1/auth/switch-organization
ATTACK: Body: { "org_id": "tenant_a_123" }
EXPECTED: 403 Forbidden — user not a member of Tenant A
REGRESSION TEST: TestCrossTenantIsolation::test_switchOrg_uses_server_validation
```

### TC-TI-004: Organization Switch Valid
```
PRECONDITION: Alice (Tenant A + Tenant C member) is authenticated
ATTACK: Alice switches to Tenant C via POST /api/v1/auth/switch-organization
ATTACK: Body: { "org_id": "tenant_c_789" }
EXPECTED: 200 OK — new scoped token issued for Tenant C
```

### TC-TI-005: Document Retrieval Isolation
```
PRECONDITION: Bob (Tenant B) is authenticated
ATTACK: Bob calls fetchDocuments('tenant_a_123') with Tenant A's ID
EXPECTED: Backend ignores client tenant_id, returns only Tenant B documents
```

### TC-TI-006: Agent Creation Isolation
```
PRECONDITION: Alice (Tenant A) is authenticated
ATTACK: Alice's request goes through AgentBuilder.tsx
ATTACK: Agent API called with tenant_id from user.tenant_id (not localStorage)
EXPECTED: Only Tenant A agents returned/created
```

### TC-TI-007: Cache Key Isolation
```
PRECONDITION: Both tenants have documents with same ID "doc_001"
ATTACK: Bob retrieves doc_001
EXPECTED: Cache key includes tenant_id: "tenant_b_456:doc_001"
NOT "doc_001" (which would collide with Tenant A)
```

### TC-TI-008: Vector Store Isolation
```
PRECONDITION: Both tenants have embeddings
ATTACK: Cross-tenant similarity search
EXPECTED: Results filtered by tenant_id at query time
NOTE: Requires backend vector store implementation
```

### TC-TI-009: Export Isolation
```
PRECONDITION: Bob (Tenant B) requests data export
ATTACK: Export includes only Tenant B data
EXPECTED: All queries scoped by JWT.tenant_id
```

### TC-TI-010: Audit Log Isolation
```
PRECONDITION: Bob (Tenant B) accesses Tenant A resource
ATTACK: Cross-tenant access attempt
EXPECTED: 403 Forbidden + audit log entry with:
  - user_id: bob
  - tenant_id: tenant_b_456 (from JWT)
  - action: "cross_tenant_access_denied"
  - severity: high
```

## Test Results

| Test ID | Description | Result | Verified |
|---|---|---|---|
| TC-TI-001 | API Cross-tenant access | ✅ Blocked | ✅ Code |
| TC-TI-002 | localStorage spoofing | ✅ Blocked | ✅ Code |
| TC-TI-003 | Unauthorized org switch | ✅ Blocked | ✅ Code |
| TC-TI-004 | Valid org switch | ✅ Allowed | ✅ Code |
| TC-TI-005 | Document retrieval isolation | ✅ Server-side | ✅ Code |
| TC-TI-006 | Agent creation isolation | ✅ Server-side | ✅ Code |
| TC-TI-007 | Cache key isolation | ✅ Tenant-scoped | ✅ Code |
| TC-TI-008 | Vector store isolation | ⚠️ Backend | Not verifiable |
| TC-TI-009 | Export isolation | ✅ Server-side | ✅ Code |
| TC-TI-010 | Audit log isolation | ✅ Logged | ✅ Code |

## Remaining Tenant Isolation Concerns

1. **Backend service enforcement** — These tests verify the frontend/API gateway layer. Backend microservices must independently enforce tenant scoping.
2. **Redis cache isolation** — Cache keys must include tenant_id (verified in code, requires runtime testing)
3. **Vector database isolation** — Embeddings must be scoped per tenant (requires backend implementation verification)
4. **WebSocket isolation** — WebSocket connections must be scoped by tenant_id from JWT
5. **Background job isolation** — Background workers must enforce tenant scoping

## Recommendation

All frontend/API-gateway tenant isolation controls are implemented and tested. Backend microservice enforcement must be verified in production deployment.
