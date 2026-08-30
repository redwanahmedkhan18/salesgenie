# frontend_security.md

## SalesGenie Frontend Security Requirements

**Document:** `frontend_security.md`  
**Project:** SalesGenie  
**Document Type:** User Requirements + System Requirements + Functional Requirements  
**Security Model:** Zero Trust + Defense in Depth + Secure-by-Default  
**Architecture:** Enterprise SaaS + Multi-Tenant + Microservices + AI/Multi-Agent  
**Primary Clients:** Web Application, Admin Console, Organization Workspaces, External Client Portal  
**Security Principle:** The frontend is an untrusted client and MUST NOT be treated as an authorization boundary.

---

## 1. Purpose

SalesGenie frontend security SHALL protect:

- User identities
- Authentication sessions
- Access tokens
- Organization and tenant data
- Customer data
- Sales data
- Marketing data
- Financial data
- AI conversations
- AI agent configurations
- RAG knowledge
- Uploaded documents
- API credentials
- Integration credentials
- Billing information
- Administrative functions
- Audit information
- Personally identifiable information
- Confidential business information

The frontend SHALL enforce secure interaction patterns while relying on backend services for authoritative authentication, authorization, validation, policy enforcement, tenant isolation, and data protection.

---

## 2. Security Principles

The frontend SHALL follow:

1. Zero Trust
2. Defense in Depth
3. Least Privilege
4. Secure by Default
5. Fail Closed
6. Never Trust Client Input
7. Never Trust Client Authorization
8. Minimize Sensitive Data Exposure
9. Explicit Authentication State
10. Explicit Authorization State
11. Strong Session Management
12. Secure API Communication
13. Strong Content Security Policy
14. Safe Error Handling
15. Auditability
16. Privacy by Design
17. Data Minimization
18. Secure Dependency Management
19. Supply-Chain Security
20. Continuous Security Testing

---

## 3. Security Boundary

The frontend SHALL be considered an untrusted environment.

The frontend MUST NOT be responsible for authoritative:

- Permission enforcement
- Role enforcement
- Tenant isolation
- Financial authorization
- Administrative authorization
- API authorization
- Data ownership validation
- Resource ownership validation
- Security policy enforcement
- Billing entitlement enforcement
- AI tool authorization

The backend MUST independently validate every security-sensitive request.

Frontend authorization SHALL exist primarily for:

- UX
- Navigation control
- Feature visibility
- Interaction control
- Early rejection
- User guidance

Backend authorization SHALL remain authoritative.

---

## 4. User Roles

The frontend SHALL support security-aware interfaces for:

- Super Admin
- Platform Admin
- Security Admin
- Billing Admin
- Organization Owner
- Organization Admin
- Workplace Admin
- Team Manager
- Sales Manager
- Sales Agent
- Marketing Manager
- Marketing Specialist
- SEO Manager
- SEO Specialist
- Product Manager
- Finance Manager
- Business Analyst
- Support Manager
- Support Agent
- AI Agent Builder
- Developer
- End User
- External Client

The frontend MUST dynamically determine accessible features from backend-provided authorization policies.

---

## 5. User Requirements

## UR-001 — Secure Authentication

Users SHALL be able to authenticate securely.

The frontend SHALL support:

- Email/password authentication
- OAuth authentication
- MFA
- Session restoration
- Session expiration
- Logout
- Logout from all devices
- Password recovery
- Account verification
- Suspicious-login handling
- Account lockout messaging
- Security challenge flows

---

## UR-002 — Secure Session Management

Users SHALL be protected against unauthorized session use.

The frontend SHALL:

- Detect authentication state
- Detect session expiration
- Refresh sessions securely
- Handle revoked sessions
- Handle invalid sessions
- Clear client authentication state after logout
- Prevent access to authenticated screens after session invalidation
- Prevent stale authenticated UI

---

## UR-003 — Secure Authorization

Users SHALL only see and interact with features they are authorized to use.

Examples:

- Sales Agent cannot access Super Admin controls
- Marketing Specialist cannot access financial administration
- External Client cannot access internal organization administration
- Support Agent cannot modify billing configuration
- AI Agent Builder cannot bypass security controls

---

## UR-004 — Tenant Isolation

Users SHALL only access data belonging to authorized organizations, workplaces, teams, and resources.

The frontend SHALL:

- Display only authorized tenant context
- Prevent accidental cross-tenant navigation
- Require explicit tenant switching
- Display current organization/workspace context
- Clear cached tenant-specific data during tenant switching
- Avoid exposing identifiers belonging to unauthorized tenants

Backend services MUST enforce actual tenant isolation.

---

## UR-005 — Secure Administrative Access

Administrative interfaces SHALL require appropriate authorization.

Sensitive administrative pages SHALL include:

- Permission checks
- Session validation
- Backend authorization
- Security confirmation where required
- Audit tracking

---

## UR-006 — Secure API Communication

All frontend-to-backend communication SHALL use secure authenticated channels.

The frontend SHALL:

- Use HTTPS in production
- Validate API responses
- Handle authentication failures
- Handle authorization failures
- Handle rate limits
- Handle expired credentials
- Avoid transmitting unnecessary sensitive information

---

## UR-007 — Secure AI Interaction

Users SHALL interact with AI agents through controlled interfaces.

The frontend SHALL protect:

- AI prompts
- Conversations
- Agent configuration
- Tool execution requests
- Uploaded knowledge
- AI-generated actions
- Human approvals
- Agent permissions
- Sensitive context

The frontend MUST NOT assume that an AI-generated action is trusted.

---

## UR-008 — Secure File Uploads

Users SHALL be able to upload files securely.

The frontend SHALL:

- Restrict supported file types
- Enforce client-side size limits
- Reject obviously unsafe files
- Display upload security status
- Prevent executable file previews
- Avoid rendering untrusted HTML
- Use signed upload URLs where applicable

Backend services MUST perform authoritative file validation and malware scanning.

---

## UR-009 — Secure Error Handling

Users SHALL receive safe errors without sensitive internal information.

Frontend errors MUST NOT expose:

- Stack traces
- Database credentials
- Internal hostnames
- Secrets
- API keys
- JWT contents
- Internal service topology
- Infrastructure credentials
- SQL statements
- Debug information

---

## UR-010 — Security Notifications

Users SHALL receive security notifications for relevant events.

Examples:

- New login
- Password changed
- MFA changed
- Email changed
- Suspicious login
- Session revoked
- API key created
- API key revoked
- Integration connected
- Integration disconnected
- Role changed
- Permission changed

---

## 6. System Requirements

## SR-001 — Secure Transport

The production frontend MUST use HTTPS.

HTTP MUST NOT be used for authenticated production communication.

The frontend SHALL support:

- TLS 1.2+
- HSTS
- Secure API endpoints
- Secure WebSocket connections using WSS

---

## SR-002 — Authentication Architecture

The frontend authentication architecture SHALL integrate with the centralized authentication service.

Expected flow:

```text
USER
 │
 ▼
FRONTEND
 │
 ▼
AUTH SERVICE
 │
 ├── Identity Validation
 ├── MFA
 ├── OAuth
 ├── Session Management
 └── Token Issuance
 │
 ▼
FRONTEND SESSION
 │
 ▼
API GATEWAY
 │
 ▼
MICROSERVICES
```

---

## SR-003 — Token Security

Authentication tokens SHALL be handled securely.

The preferred architecture SHALL use:

* Secure
* HttpOnly
* SameSite cookies

for refresh/session credentials where compatible with the backend architecture.

Sensitive tokens SHOULD NOT be stored in:

```text
localStorage
sessionStorage
URL parameters
query strings
DOM attributes
HTML
client-visible configuration
```

If browser-accessible access tokens are unavoidable, their exposure SHALL be minimized and their lifetime SHALL be short.

---

## SR-004 — Token Lifecycle

The frontend SHALL support:

```text
Token Issued
     ↓
Token Used
     ↓
Token Refreshed
     ↓
Token Expired
     ↓
Session Revoked
     ↓
Local Security State Cleared
     ↓
User Re-authentication
```

The frontend MUST NOT treat a locally decoded JWT as authoritative authorization.

---

## SR-005 — Authorization Model

The frontend SHALL consume backend authorization information.

Authorization MAY include:

```text
user
organization
workplace
team
role
permissions
scopes
resource
action
conditions
entitlements
```

Example:

```text
can(
    user,
    action="lead.update",
    resource="lead:123"
)
```

The backend MUST independently validate the request.

---

## SR-006 — RBAC Support

Frontend navigation and UI components SHALL support RBAC.

Example:

```text
Sales Agent
 ├── Leads
 ├── Contacts
 ├── Opportunities
 └── Conversations

Sales Manager
 ├── Leads
 ├── Contacts
 ├── Opportunities
 ├── Team Analytics
 └── Sales Forecasting

Super Admin
 ├── Organizations
 ├── Users
 ├── Security
 ├── Billing
 ├── Platform Monitoring
 └── System Configuration
```

---

## SR-007 — ABAC Support

The frontend SHALL support conditional UI behavior based on attributes such as:

* Organization
* Workplace
* Team
* User role
* Resource ownership
* Geographic restrictions
* Subscription
* Feature entitlement
* Security state

Backend policy enforcement SHALL remain authoritative.

---

## 7. Content Security Policy

The frontend SHALL implement a restrictive Content Security Policy.

The CSP SHALL restrict:

* Script sources
* Style sources
* Image sources
* Font sources
* Frame sources
* Connection sources
* Object sources
* Media sources
* Worker sources

Example conceptual policy:

```text
default-src 'self';

script-src 'self';

style-src 'self';

img-src 'self' data: https:;

font-src 'self' https:;

connect-src 'self'
    https://api.salesgenie.example
    wss://api.salesgenie.example;

object-src 'none';

frame-src 'none';

base-uri 'self';

form-action 'self';

frame-ancestors 'none';
```

The actual production policy MUST be generated according to deployed dependencies and services.

---

## 8. XSS Protection

The frontend SHALL protect against:

* Reflected XSS
* Stored XSS
* DOM-based XSS
* Mutation XSS
* HTML injection
* JavaScript URL injection

The frontend MUST:

* Escape untrusted content
* Avoid unsafe HTML rendering
* Sanitize rich text
* Avoid arbitrary script execution
* Avoid `eval`
* Avoid `new Function`
* Avoid unsafe dynamic script injection

---

## 9. DOM Security

The frontend MUST NOT insert untrusted content directly using unsafe DOM APIs.

High-risk APIs SHALL be prohibited unless explicitly reviewed:

```text
innerHTML
outerHTML
insertAdjacentHTML
document.write
eval
Function()
setTimeout(string)
setInterval(string)
```

Trusted sanitization libraries SHALL be used when HTML rendering is required.

---

## 10. CSRF Protection

If cookie-based authentication is used, the frontend SHALL support CSRF protection.

The architecture SHALL support:

* SameSite cookies
* CSRF tokens where required
* Origin validation
* Referer validation where appropriate
* Secure cookie configuration

State-changing requests MUST NOT rely solely on browser cookies without appropriate CSRF protection.

---

## 11. CORS

The frontend SHALL communicate only with explicitly authorized origins.

The production API SHALL NOT use:

```text
Access-Control-Allow-Origin: *
```

for authenticated APIs.

Allowed origins SHALL be explicitly configured.

---

## 12. Clickjacking Protection

Sensitive SalesGenie pages MUST be protected from clickjacking.

The platform SHALL support:

```text
frame-ancestors 'none'
```

or an explicitly approved embedding policy.

---

## 13. Secure Headers

The frontend deployment SHALL support appropriate security headers including:

```text
Content-Security-Policy
Strict-Transport-Security
X-Content-Type-Options
Referrer-Policy
Permissions-Policy
Cross-Origin-Opener-Policy
Cross-Origin-Resource-Policy
```

Legacy headers SHALL be used only when technically appropriate.

---

## 14. Sensitive Data Handling

The frontend SHALL minimize sensitive data stored in browser memory.

Sensitive information includes:

* Passwords
* API keys
* Access tokens
* Refresh tokens
* Payment credentials
* Integration credentials
* Customer PII
* Financial records
* Private documents
* Security configuration
* Internal system metadata

Sensitive values SHALL NOT be unnecessarily stored in:

```text
localStorage
sessionStorage
IndexedDB
URL
browser history
analytics events
console logs
error messages
```

---

## 15. Browser Storage Security

Allowed browser storage SHALL be classified.

Example:

| Data           | localStorage | sessionStorage |            HttpOnly Cookie |
| -------------- | -----------: | -------------: | -------------------------: |
| Theme          |          Yes |       Optional |                         No |
| Language       |          Yes |       Optional |                         No |
| UI preferences |          Yes |       Optional |                         No |
| Access token   |        Avoid |          Avoid | Preferred where applicable |
| Refresh token  |           No |             No |                  Preferred |
| Password       |           No |             No |                         No |
| API key        |           No |             No |                         No |
| Financial data |           No |             No |                         No |
| Sensitive PII  |        Avoid |          Avoid |                         No |

---

## 16. Authentication State Security

The frontend SHALL implement a centralized authentication state manager.

The authentication state SHALL include:

```text
anonymous
authenticating
authenticated
refreshing
expired
revoked
locked
mfa_required
error
```

UI components MUST NOT independently implement authentication logic.

---

## 17. Route Protection

Protected routes SHALL require authenticated state.

Example:

```text
/public
/login
/signup
/forgot-password
```

versus:

```text
/dashboard
/leads
/crm
/marketing
/seo
/finance
/support
/settings
/admin
```

Protected routes SHALL be guarded by authentication and authorization policies.

---

## 18. Privileged Route Protection

Administrative routes SHALL require elevated authorization.

Example:

```text
/admin
/admin/users
/admin/organizations
/admin/security
/admin/billing
/admin/audit
/admin/system
```

The frontend SHALL:

1. Verify authenticated state
2. Verify required permissions
3. Load protected data from backend
4. Handle backend authorization failure
5. Avoid exposing privileged information before authorization

---

## 19. Tenant Context Security

Every tenant-aware frontend request SHALL include the appropriate tenant context through the approved backend mechanism.

The frontend SHALL prevent:

```text
Tenant A
   ↓
Tenant B resource
```

from occurring through stale client state.

Tenant switching SHALL trigger:

```text
Validate membership
      ↓
Update active tenant
      ↓
Clear tenant-specific cache
      ↓
Reload permissions
      ↓
Reload feature entitlements
      ↓
Reload workspace data
```

---

## 20. Cache Security

The frontend SHALL prevent sensitive information from remaining in caches after:

* Logout
* Tenant switching
* Account switching
* Session revocation
* Permission downgrade

Sensitive cached resources SHALL support:

* TTL
* Invalidation
* User isolation
* Tenant isolation
* Permission-aware caching

---

## 21. API Security

Every API request SHALL support appropriate:

* Authentication
* Authorization
* Request validation
* Response validation
* Timeout handling
* Rate-limit handling
* Error handling
* Retry policy

The frontend MUST NOT assume that HTTP status `200` alone means the operation is security-safe.

---

## 22. API Response Validation

Frontend API clients SHALL validate expected response structures.

The frontend SHOULD use schema validation for critical API responses.

Invalid responses SHALL fail safely.

---

## 23. API Error Handling

The API client SHALL classify errors.

Example:

```text
400 → Validation Error
401 → Authentication Required
403 → Authorization Denied
404 → Resource Not Found
409 → Conflict
422 → Semantic Validation Error
429 → Rate Limited
500 → Internal Server Error
502 → Gateway Error
503 → Service Unavailable
504 → Timeout
```

The frontend SHALL avoid exposing backend internals.

---

## 24. Rate-Limit Handling

The frontend SHALL correctly handle rate limits.

When receiving:

```text
429 Too Many Requests
```

the frontend SHALL:

* Display appropriate feedback
* Respect server retry information
* Avoid uncontrolled retries
* Use exponential backoff where appropriate
* Prevent request storms

---

## 25. Retry Security

Automatic retries SHALL NOT be applied blindly to sensitive operations.

The frontend SHALL distinguish:

```text
GET
safe/idempotent operations
```

from:

```text
POST
DELETE
financial operations
permission changes
security operations
```

Sensitive mutations MUST NOT be duplicated through unsafe retry behavior.

---

## 26. WebSocket Security

WebSocket connections SHALL:

* Use WSS
* Require authenticated sessions
* Validate authorization
* Support session expiration
* Support connection revocation
* Avoid sensitive data leakage
* Handle reconnect securely

WebSocket messages SHALL be validated.

---

## 27. Real-Time Security

Real-time events SHALL be permission-aware.

The frontend MUST NOT subscribe to channels outside the user's authorization scope.

Examples:

```text
organization.events
workplace.events
team.events
user.events
admin.events
security.events
billing.events
ai.events
```

Sensitive administrative channels SHALL require elevated authorization.

---

## 28. File Security

The frontend SHALL validate:

* File size
* MIME type
* Extension
* Upload destination
* Upload status

The backend SHALL perform authoritative:

* MIME validation
* Content inspection
* Malware scanning
* Content sanitization
* Access control

---

## 29. Document Preview Security

The frontend MUST NOT execute active content from uploaded documents.

Potentially dangerous formats SHALL be handled safely.

Examples:

```text
HTML
SVG
JavaScript
XML
Executable files
Macro-enabled documents
```

Previews SHOULD be rendered through sandboxed or server-generated representations.

---

## 30. Image Security

User-provided images SHALL be treated as untrusted.

The frontend SHALL avoid:

* Executing SVG scripts
* Trusting image metadata
* Embedding arbitrary external resources
* Rendering unsafe HTML masquerading as images

---

## 31. AI Prompt Security

AI prompts SHALL be treated as untrusted input.

The frontend SHALL support detection and safe handling of:

* Prompt injection indicators
* Malicious instructions
* Tool-execution requests
* Sensitive data requests
* Credential requests
* Privilege escalation attempts

The frontend MUST NOT be the only prompt-injection defense.

---

## 32. AI Tool Execution Security

The frontend SHALL clearly distinguish:

```text
AI suggestion
```

from:

```text
AI authorized action
```

High-risk operations SHALL require backend authorization and, where configured, human approval.

Examples:

```text
Delete customer
Send campaign
Send email
Modify CRM record
Change billing
Issue refund
Change permissions
Execute workflow
Call external API
Publish content
```

---

## 33. Human Approval Security

For high-risk AI operations:

```text
AI proposes action
       ↓
Policy evaluation
       ↓
Human approval
       ↓
Backend authorization
       ↓
Execution
       ↓
Audit event
```

The frontend MUST NOT directly execute privileged actions based solely on AI output.

---

## 34. Secrets Management

The frontend MUST NOT contain:

* Database credentials
* Private API keys
* Service account secrets
* Cloud credentials
* Signing keys
* Encryption keys
* Internal service credentials

Build-time public environment variables SHALL be treated as public.

---

## 35. Environment Security

The frontend SHALL distinguish:

```text
development
test
staging
production
```

Production secrets MUST NOT be embedded into development artifacts.

Development debugging features MUST NOT accidentally reach production.

---

## 36. Source Map Security

Production source maps SHALL be controlled.

If source maps are published, the security implications SHALL be reviewed.

Sensitive source code and internal implementation details SHOULD NOT be unnecessarily exposed publicly.

---

## 37. Dependency Security

Frontend dependencies SHALL be continuously monitored.

The project SHALL support:

* Dependency vulnerability scanning
* Lockfile integrity
* Automated updates
* License validation
* Malicious package detection
* Dependency provenance
* Software Composition Analysis

---

## 38. Supply-Chain Security

The build system SHALL protect against:

* Dependency substitution
* Malicious packages
* Compromised dependencies
* Build script injection
* CI/CD credential theft
* Artifact tampering

Production builds SHOULD use reproducible or verifiable build processes.

---

## 39. Third-Party Script Security

Third-party JavaScript SHALL be minimized.

Every third-party script SHALL be reviewed for:

* Business necessity
* Security impact
* Data access
* Privacy impact
* CSP compatibility
* Supply-chain risk

Third-party scripts MUST NOT receive unnecessary access to sensitive application data.

---

## 40. Analytics Security

Analytics instrumentation SHALL NOT capture:

* Passwords
* Access tokens
* API keys
* Payment credentials
* Private messages
* Sensitive customer records
* Private documents

Sensitive fields SHALL be redacted.

---

## 41. Logging Security

Frontend logs SHALL avoid sensitive information.

Forbidden:

```text
console.log(password)
console.log(token)
console.log(apiKey)
console.log(customerPII)
```

Production logging SHALL be controlled and privacy-aware.

---

## 42. Browser Console Security

Security-sensitive information SHALL NOT be exposed through:

* Console logs
* Debug panels
* React/Astro development overlays
* Global variables
* Window objects

Production debug tooling SHALL be disabled or protected.

---

## 43. URL Security

Sensitive information MUST NOT be placed into URLs.

Forbidden:

```text
?token=
?password=
?api_key=
?secret=
?session=
```

URLs SHALL NOT expose unnecessary internal identifiers.

---

## 44. Open Redirect Protection

The frontend SHALL validate redirect destinations.

The application MUST NOT blindly redirect users based on arbitrary query parameters.

Unsafe:

```text
/login?redirect=https://attacker.example
```

Redirect targets SHALL be allowlisted or validated as internal routes.

---

## 45. PostMessage Security

If `postMessage` is used, the frontend SHALL:

* Validate origin
* Validate message structure
* Validate message type
* Reject unknown senders
* Avoid transmitting secrets

Wildcard origins SHALL NOT be used for sensitive communication.

---

## 46. iframe Security

Sensitive application pages SHALL not be embedded unless explicitly required.

Third-party iframes SHALL:

* Use sandboxing where possible
* Have restricted permissions
* Use explicit origins
* Avoid access to sensitive application state

---

## 47. Clipboard Security

Sensitive information copied to the clipboard SHALL be minimized.

The frontend SHOULD:

* Warn users when copying secrets
* Avoid automatic copying of credentials
* Clear sensitive clipboard values where appropriate

---

## 48. Browser Permission Security

The application SHALL request only necessary browser permissions.

Examples:

* Notifications
* Camera
* Microphone
* Location
* Clipboard
* File system

Permissions SHALL be requested only when required.

---

## 49. Voice Security

For AI voice and call-center features:

The frontend SHALL:

* Request microphone access explicitly
* Display recording state
* Display call state
* Stop recording when the session ends
* Prevent unauthorized microphone access
* Handle permission revocation

---

## 50. Security Settings UI

Users SHALL have access to security controls appropriate to their role.

Security settings MAY include:

```text
Password
MFA
Active Sessions
Login History
Trusted Devices
Security Alerts
API Keys
Connected Applications
OAuth Connections
Privacy
Data Export
Data Deletion
```

---

## 51. Active Session Management

Users SHALL be able to view active sessions where supported.

Information MAY include:

* Device
* Browser
* Approximate location
* Last activity
* Login time
* Session status

Users SHALL be able to revoke sessions where authorized.

---

## 52. MFA Security

The frontend SHALL support:

* MFA enrollment
* MFA verification
* MFA recovery
* MFA removal
* Backup codes
* Security challenge handling

MFA changes SHOULD require re-authentication.

---

## 53. Re-Authentication

Sensitive operations SHOULD require re-authentication.

Examples:

```text
Change password
Disable MFA
Change email
Delete organization
Change billing ownership
Create privileged API key
Change security policy
Delete sensitive data
```

---

## 54. Security Risk Confirmation

High-risk operations SHALL provide explicit confirmation.

Example:

```text
Action
  ↓
Risk Classification
  ↓
User Confirmation
  ↓
Backend Authorization
  ↓
Execution
  ↓
Audit
```

---

## 55. Billing Security

The frontend SHALL never process raw payment credentials unless explicitly required and handled by a compliant payment provider.

The frontend SHALL use secure payment-provider components where applicable.

The frontend MUST NOT store:

* Card numbers
* CVV
* Payment authentication secrets

---

## 56. Account Deletion Security

Account deletion SHALL require:

* Authentication
* Authorization
* Explicit confirmation
* Backend policy validation
* Audit logging

For high-risk accounts, re-authentication SHOULD be required.

---

## 57. Organization Deletion Security

Organization deletion SHALL require:

* Organization owner authorization
* Backend validation
* Explicit confirmation
* Confirmation of consequences
* Audit event
* Appropriate recovery/grace period where configured

---

## 58. Permission Change Security

Changing permissions SHALL require appropriate authorization.

The frontend SHALL display:

* Current role
* Requested role
* Permissions granted
* Permissions removed
* Security impact

The backend SHALL enforce authorization.

---

## 59. API Key Security UI

The frontend SHALL support secure API key management.

API keys SHALL:

* Be displayed only when necessary
* Be masked after creation
* Never be logged
* Support revocation
* Support expiration
* Support scoped permissions

The full secret SHOULD be shown only once.

---

## 60. OAuth Security

OAuth flows SHALL support:

* State validation
* PKCE where applicable
* Secure redirect handling
* Explicit consent
* Token lifecycle handling
* Connection revocation

OAuth credentials MUST NOT be exposed unnecessarily to frontend JavaScript.

---

## 61. Integration Security

Connected integrations SHALL display:

```text
Provider
Connection Status
Authorized Scopes
Connected Account
Last Synchronization
Security Status
Disconnect
```

Users SHALL be able to revoke integrations where authorized.

---

## 62. Security Audit UI

Authorized users SHALL be able to view security events.

Events MAY include:

```text
LOGIN
LOGOUT
LOGIN_FAILURE
PASSWORD_CHANGE
MFA_ENABLED
MFA_DISABLED
ROLE_CHANGED
PERMISSION_CHANGED
API_KEY_CREATED
API_KEY_REVOKED
OAUTH_CONNECTED
OAUTH_DISCONNECTED
DATA_EXPORTED
DATA_DELETED
SECURITY_POLICY_CHANGED
```

---

## 63. Security Event Integrity

Frontend-generated security events SHALL NOT be considered authoritative.

Authoritative security audit events SHALL be generated or validated by backend services.

---

## 64. Privacy Controls

The frontend SHALL support privacy controls including:

* Consent
* Cookie preferences
* Data export
* Data deletion
* Privacy settings
* Marketing preferences
* Tracking preferences

---

## 65. Consent Security

Consent state SHALL be:

* Explicit
* Versioned
* Timestamped
* Auditable
* Revocable where required

Backend systems SHALL maintain authoritative consent records.

---

## 66. Accessibility Security

Security controls SHALL remain accessible.

The frontend SHALL support:

* Keyboard navigation
* Screen readers
* Accessible error messages
* Focus management
* Accessible MFA controls
* Accessible confirmation dialogs

Security MUST NOT depend exclusively on visual indicators.

---

## 67. Localization Security

Localized security messages SHALL preserve security semantics.

Translations MUST NOT alter:

* Confirmation meaning
* Warning severity
* Security instructions
* Authentication requirements
* Authorization semantics

---

## 68. Internationalization Security

The frontend SHALL prevent localization-based attacks including:

* Bidirectional text abuse
* Unicode confusables
* Homograph attacks
* Malicious localized URLs
* Unsafe interpolation

User-generated content SHALL remain untrusted regardless of language.

---

## 69. Frontend Functional Requirements

## FR-001 — Authentication Guard

The system SHALL implement a centralized authentication guard.

---

## FR-002 — Authorization Guard

The system SHALL implement centralized permission-aware route and component guards.

---

## FR-003 — Secure API Client

The application SHALL provide a centralized API client responsible for:

* Authentication
* Authorization context
* Request headers
* CSRF handling
* Retry policy
* Timeout handling
* Rate-limit handling
* Error normalization
* Response validation
* Session expiration

---

## FR-004 — Session Refresh

The API client SHALL automatically refresh sessions according to backend policy.

Expired or revoked sessions SHALL force secure re-authentication.

---

## FR-005 — Logout

Logout SHALL:

1. Notify backend
2. Revoke session where supported
3. Clear authentication state
4. Clear sensitive cache
5. Clear tenant-specific state
6. Redirect to a public page

---

## FR-006 — Permission Fetching

The frontend SHALL retrieve effective permissions from the backend.

---

## FR-007 — Permission Cache

Permissions SHALL be cached only for a controlled period and invalidated when:

* Role changes
* Tenant changes
* Session changes
* User permissions change
* Security policy changes

---

## FR-008 — Feature Entitlement Security

Subscription features SHALL be controlled by backend-provided entitlements.

Frontend feature flags SHALL NOT replace backend entitlement enforcement.

---

## FR-009 — Role-Based Navigation

Navigation SHALL dynamically adapt to the authenticated user's permissions.

---

## FR-010 — Unauthorized Page

The frontend SHALL provide a secure `403 Forbidden` experience without exposing internal authorization details.

---

## FR-011 — Authentication Failure

The frontend SHALL provide a safe `401 Unauthorized` experience.

---

## FR-012 — Session Expiration

The frontend SHALL notify users when sessions expire and provide a secure re-authentication path.

---

## FR-013 — Concurrent Session Handling

The frontend SHALL handle session revocation from another device.

---

## FR-014 — Tenant Switching

Tenant switching SHALL:

1. Validate membership
2. Update tenant context
3. Clear sensitive cache
4. Refresh permissions
5. Refresh entitlements
6. Reload tenant data

---

## FR-015 — Secure Search

Search results SHALL be permission-filtered by backend services.

The frontend MUST NOT assume that hidden results are sufficient for access control.

---

## FR-016 — Secure Data Tables

Data tables SHALL not render records the backend has not authorized.

---

## FR-017 — Secure Forms

Forms SHALL:

* Validate inputs
* Normalize data
* Reject invalid values
* Prevent unsafe HTML
* Handle server validation
* Display safe errors

---

## FR-018 — Security-Sensitive Forms

Sensitive forms SHALL support:

* Re-authentication
* Confirmation
* CSRF protection
* Secure submission
* Audit event integration

---

## FR-019 — Secure Notifications

Security notifications SHALL be delivered through the notification platform and SHALL avoid sensitive information.

---

## FR-020 — Secure Toasts

Toast messages MUST NOT reveal:

* Secrets
* Tokens
* Internal infrastructure
* Database information
* Sensitive PII

---

## 70. Frontend Security Architecture

```text
                         USER
                           │
                           ▼
                 ┌──────────────────┐
                 │ SalesGenie UI    │
                 │                  │
                 │ Secure Routes    │
                 │ Secure Forms     │
                 │ CSP              │
                 │ XSS Protection   │
                 │ Input Validation │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Auth State       │
                 │ Manager          │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Secure API       │
                 │ Client           │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ API Gateway      │
                 └────────┬─────────┘
                          │
              ┌───────────┼───────────┐
              ▼           ▼           ▼
           Auth       Policy       Services
           Service    Engine       Layer
              │           │           │
              └───────────┼───────────┘
                          ▼
                   Security Controls
                          │
          ┌───────────────┼────────────────┐
          ▼               ▼                ▼
       RBAC/ABAC       Tenant          Audit
                       Isolation       Logging
```

---

## 71. Secure Frontend Request Lifecycle

```text
USER ACTION
    │
    ▼
CLIENT VALIDATION
    │
    ▼
AUTHENTICATION CHECK
    │
    ▼
PERMISSION CHECK
    │
    ▼
REQUEST SANITIZATION
    │
    ▼
SECURE API REQUEST
    │
    ▼
API GATEWAY
    │
    ▼
BACKEND AUTHORIZATION
    │
    ▼
TENANT VALIDATION
    │
    ▼
RESOURCE AUTHORIZATION
    │
    ▼
BUSINESS LOGIC
    │
    ▼
AUDIT EVENT
    │
    ▼
SECURE RESPONSE
    │
    ▼
RESPONSE VALIDATION
    │
    ▼
SAFE UI RENDERING
```

---

## 72. Security Classification

The frontend SHALL classify data as:

```text
PUBLIC
INTERNAL
CONFIDENTIAL
SENSITIVE
HIGHLY_SENSITIVE
SECRET
```

Example:

| Data                       | Classification   |
| -------------------------- | ---------------- |
| Marketing page             | PUBLIC           |
| Product documentation      | PUBLIC           |
| Organization analytics     | CONFIDENTIAL     |
| Customer records           | SENSITIVE        |
| Financial information      | HIGHLY_SENSITIVE |
| API secrets                | SECRET           |
| Authentication credentials | SECRET           |

---

## 73. Security Telemetry

The frontend SHOULD emit security telemetry for:

* Authentication failures
* Authorization failures
* Suspicious navigation
* Session anomalies
* CSP violations
* API security errors
* Repeated rate limits
* Unexpected authentication state
* Security-sensitive UI actions

Telemetry MUST exclude sensitive values.

---

## 74. CSP Violation Monitoring

The frontend SHALL support CSP violation reporting.

The system SHOULD detect:

* Unauthorized script execution
* Unexpected external resources
* Inline script violations
* Unexpected connection destinations

---

## 75. Security Monitoring Integration

Frontend security events SHALL integrate with:

```text
Frontend
   ↓
Telemetry
   ↓
Observability Platform
   ↓
Security Monitoring
   ↓
Threat Detection
   ↓
Incident Alerting
   ↓
Security Admin
```

---

## 76. Incident Handling

If the frontend detects a security-critical state, it SHALL fail safely.

Examples:

```text
Invalid session
Invalid authorization state
Malformed security response
Compromised configuration
Unexpected API origin
CSP violation
```

Possible actions:

* Stop sensitive operation
* Clear session state
* Force re-authentication
* Disable affected feature
* Notify user
* Emit security telemetry

---

## 77. Security Testing Requirements

The frontend SHALL be tested against:

### Authentication

* Brute-force scenarios
* Session fixation
* Session hijacking
* Token leakage
* Logout bypass
* Expired tokens
* Revoked tokens

### Authorization

* RBAC bypass
* ABAC bypass
* Privilege escalation
* Tenant isolation bypass
* IDOR
* Forced browsing

### Injection

* XSS
* HTML injection
* DOM injection
* URL injection
* JavaScript injection

### Browser Security

* CSRF
* Clickjacking
* CSP bypass
* CORS misconfiguration
* postMessage abuse

### Data Security

* Sensitive storage
* Sensitive logging
* Cache leakage
* Clipboard leakage
* URL leakage

---

## 78. Security Acceptance Criteria

The frontend SHALL NOT be considered production-ready unless:

* Authentication is secure
* Sessions are securely managed
* Authorization is backend-enforced
* Tenant isolation is backend-enforced
* Sensitive tokens are protected
* CSP is implemented
* XSS defenses are implemented
* CSRF protection exists where required
* CORS is restricted
* Sensitive data is not logged
* Secrets are absent from frontend bundles
* Third-party scripts are reviewed
* Dependencies are scanned
* Security headers are configured
* Administrative routes are protected
* AI actions are permission-controlled
* File uploads are securely handled
* Security events are observable
* Security testing passes
* Critical vulnerabilities are resolved

---

## 79. Security Non-Functional Requirements

## NFR-SEC-001

Security controls SHALL fail closed.

## NFR-SEC-002

Security-sensitive operations SHALL be auditable.

## NFR-SEC-003

Authentication state SHALL be consistent across the application.

## NFR-SEC-004

Authorization decisions SHALL be server authoritative.

## NFR-SEC-005

Tenant isolation SHALL be server authoritative.

## NFR-SEC-006

Sensitive data exposure SHALL be minimized.

## NFR-SEC-007

Security controls SHALL not significantly degrade normal application usability.

## NFR-SEC-008

Security mechanisms SHALL support horizontal scaling.

## NFR-SEC-009

Security telemetry SHALL support centralized observability.

## NFR-SEC-010

Security controls SHALL be compatible with microservices architecture.

---

## 80. Security Anti-Patterns — Prohibited

The frontend MUST NOT:

```text
Trust client-side role checks
Trust hidden UI elements as authorization
Store refresh tokens in localStorage
Store passwords
Expose API secrets
Expose cloud credentials
Embed database credentials
Trust AI-generated permissions
Trust user-provided authorization claims
Trust JWT claims without backend validation
Disable TLS
Use wildcard CORS for authenticated APIs
Render unsanitized HTML
Use eval()
Log credentials
Put tokens in URLs
Automatically retry financial mutations
Trust arbitrary redirect URLs
Trust arbitrary postMessage origins
Expose internal stack traces
Expose internal service topology
```

---

## 81. Security Ownership Model

```text
Frontend
   │
   ├── Secure UI
   ├── Secure State
   ├── Secure Storage
   ├── Secure API Client
   └── Security UX
           │
           ▼
API Gateway
   │
   ├── Authentication
   ├── Rate Limiting
   └── Request Security
           │
           ▼
Authorization / Policy Layer
   │
   ├── RBAC
   ├── ABAC
   ├── Tenant Isolation
   └── Resource Authorization
           │
           ▼
Backend Services
   │
   ├── Validation
   ├── Business Rules
   ├── Data Security
   └── Audit
           │
           ▼
Security Platform
   │
   ├── Monitoring
   ├── Threat Detection
   ├── SIEM
   ├── Incident Response
   └── Compliance
```

---

## 82. Final Security Requirement

SalesGenie frontend security SHALL operate under the following invariant:

```text
THE FRONTEND IS NEVER TRUSTED.

Frontend controls
        +
Secure browser architecture
        +
Secure authentication
        +
Secure session management
        +
Secure API communication
        +
Backend authorization
        +
Tenant isolation
        +
Security monitoring
        +
Auditability
        +
Continuous security testing
        =
ENTERPRISE-GRADE FRONTEND SECURITY
```

The frontend SHALL provide strong client-side defenses, but **no frontend control SHALL be treated as the authoritative security boundary**. Every security-sensitive operation MUST ultimately be validated by the appropriate backend service, authorization policy engine, tenant-isolation mechanism, and audit system.
