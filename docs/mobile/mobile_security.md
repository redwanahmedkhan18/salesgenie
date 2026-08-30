# Mobile Security Requirements — SalesGenie

**Document:** `mobile_security.md`
**Product:** SalesGenie — Enterprise AI Customer Support, Sales, Marketing, Analytics & Workflow Automation Platform
**Scope:** iOS and Android mobile applications, mobile APIs, authentication, authorization, local storage, network communication, push notifications, AI agents, integrations, analytics, billing, customer data, administrative functions, and backend services.

---

## 1. Purpose

This document defines the enterprise-grade security requirements for the SalesGenie mobile platform.

The mobile security architecture shall protect:

* User identities
* Authentication credentials
* Access tokens and refresh tokens
* Organization and tenant data
* Customer and prospect data
* CRM records
* Sales information
* Marketing information
* Financial information
* AI conversations
* AI agent configurations
* RAG knowledge
* Documents
* Workflow definitions
* Integration credentials
* API keys
* Payment and billing information
* Notifications
* Analytics
* Audit records
* Device information
* Application state
* Offline data
* Cached data
* Administrative operations

The mobile application shall operate as an untrusted client. All authoritative security decisions must be enforced by backend services.

---

## 2. Security Objectives

SalesGenie mobile security shall provide:

1. Confidentiality
2. Integrity
3. Availability
4. Authentication
5. Authorization
6. Tenant isolation
7. Least-privilege access
8. Secure credential storage
9. Secure communications
10. Secure session management
11. Device security
12. Application integrity
13. API security
14. Data protection
15. Privacy protection
16. AI security
17. Secure integration access
18. Fraud prevention
19. Threat detection
20. Security observability
21. Auditability
22. Incident response
23. Secure update mechanisms
24. Regulatory compliance

---

## 3. Security Principles

## 3.1 Zero Trust

The mobile application shall never be inherently trusted.

Every request shall be evaluated based on:

* Identity
* Authentication state
* Authorization
* Tenant
* Workplace
* Role
* Permissions
* Device/session state
* Risk signals
* Resource ownership
* Policy
* Request context

---

## 3.2 Least Privilege

Users, applications, devices, agents and services shall receive only the minimum permissions required.

---

## 3.3 Backend Authority

The frontend shall never be the authoritative source for:

* Role
* Permission
* Subscription entitlement
* Tenant membership
* Billing limits
* AI authorization
* Administrative authorization
* Resource ownership
* Security policy
* Compliance state

---

## 3.4 Defense in Depth

Security shall be enforced across:

```text
Device
  ↓
Mobile Application
  ↓
Network Security
  ↓
API Gateway
  ↓
Authentication
  ↓
Authorization
  ↓
Service Security
  ↓
Database Security
  ↓
Audit / Monitoring
```

---

## 4. User Roles

The mobile security architecture shall support the SalesGenie role hierarchy:

* Super Admin
* Platform Admin
* Security Admin
* Billing Admin
* Organization Owner
* Organization Admin
* Workplace Admin
* Team Manager
* Sales Manager
* Sales Agent
* Marketing Manager
* Marketing Specialist
* SEO Manager
* SEO Specialist
* Product Manager
* Finance Manager
* Business Analyst
* Support Manager
* Support Agent
* AI Agent Builder
* Developer
* End User
* External Client

Backend authorization shall determine which mobile features each role can access.

---

## 5. User Requirements

## UR-001 — Secure Login

Users shall be able to securely authenticate through the mobile application.

Supported authentication mechanisms shall include:

* Email/password
* Google OAuth
* MFA
* Passkeys where supported
* Enterprise SSO where available
* Device-based authentication
* Biometric authentication as a local authentication mechanism

---

## UR-002 — Secure Logout

Users shall be able to explicitly log out from:

* Current device
* All active devices
* Individual sessions

Logout shall invalidate or revoke server-side session credentials where supported.

---

## UR-003 — MFA

Users shall be able to configure and use MFA.

Supported mechanisms may include:

* TOTP
* Authenticator applications
* Passkeys
* Security keys
* Email verification
* SMS verification where required

MFA enforcement shall be controlled by backend security policies.

---

## UR-004 — Biometric Authentication

Users shall be able to unlock the application using:

* Face ID
* Touch ID
* Android BiometricPrompt
* Device PIN/passcode fallback

Biometric authentication shall unlock locally protected credentials rather than replace backend authentication.

---

## UR-005 — Session Visibility

Users shall be able to view active sessions where permitted.

Session information may include:

* Device
* Platform
* Approximate location
* Last activity
* Login time
* IP metadata where permitted
* Session status

---

## UR-006 — Session Revocation

Users shall be able to revoke suspicious sessions.

Security administrators shall be able to revoke sessions according to RBAC policies.

---

## UR-007 — Device Management

Users and authorized administrators shall be able to view registered devices.

The system shall support:

* Device registration
* Device removal
* Device trust state
* Device risk state
* Session association

---

## UR-008 — Secure Notifications

Users shall receive security-sensitive notifications without exposing confidential information on the lock screen.

---

## UR-009 — Secure AI Usage

Users shall be able to securely access:

* AI agents
* AI conversations
* AI-generated recommendations
* AI workflows
* AI sales intelligence
* AI marketing automation
* AI analytics
* AI support functions

Access shall be enforced by backend authorization.

---

## UR-010 — Secure Offline Mode

Where offline functionality is supported, sensitive data shall be encrypted locally and protected against unauthorized access.

---

## UR-011 — Secure File Access

Users shall be able to upload and download documents securely.

The application shall prevent unauthorized access to documents belonging to other users, workplaces or organizations.

---

## UR-012 — Secure Billing

Users shall be able to access billing information according to their permissions.

Sensitive payment credentials shall not be stored directly in the mobile application.

---

## UR-013 — Secure Integrations

Users shall be able to connect integrations securely.

Examples:

* Gmail
* Google Drive
* Slack
* HubSpot
* Salesforce
* Zendesk
* Jira
* Notion
* Microsoft Teams
* LinkedIn
* Facebook
* Instagram
* WhatsApp
* YouTube
* TikTok

OAuth authorization shall be handled through secure backend-controlled flows whenever possible.

---

## UR-014 — Security Alerts

Users shall receive security alerts for:

* New login
* New device
* Suspicious login
* Password change
* MFA change
* Session revocation
* API key changes
* Integration changes
* Permission changes
* Organization membership changes
* Administrative actions

---

## UR-015 — Privacy Controls

Users shall be able to manage available privacy settings.

---

## UR-016 — Account Recovery

Users shall be able to securely recover accounts through backend-controlled recovery workflows.

---

## UR-017 — Security Reporting

Users shall be able to report:

* Suspicious activity
* Account compromise
* Unauthorized access
* Malicious content
* AI security incidents
* Integration abuse
* Data leakage

---

## UR-018 — Secure Application Updates

Users shall receive security-critical application updates.

The mobile application shall support minimum-version enforcement when required by backend security policy.

---

## 6. System Requirements

## SR-001 — Mobile Client Must Be Untrusted

The backend shall treat every mobile client as potentially compromised.

The backend shall never trust:

* Client-side role information
* Client-side permission flags
* Client-side feature flags
* Client-side subscription status
* Client-side tenant IDs
* Client-side security decisions

---

## SR-002 — TLS

All production network communication shall use HTTPS with modern TLS.

Plain HTTP shall be prohibited for production API communication.

---

## SR-003 — Certificate Validation

The mobile application shall perform strict certificate validation.

Certificate pinning may be implemented for high-risk endpoints where operationally appropriate.

---

## SR-004 — API Gateway

All mobile API requests shall pass through the SalesGenie API gateway or approved API security layer.

The gateway shall provide:

* Authentication
* Authorization enforcement
* Rate limiting
* Request validation
* Threat detection
* API version validation
* Abuse prevention
* Request tracing

---

## SR-005 — OAuth Security

OAuth implementations shall use:

* Authorization Code Flow
* PKCE
* Secure redirect handling
* State validation
* Nonce validation where applicable
* Secure token handling

Implicit OAuth flows shall not be used.

---

## SR-006 — Token Security

Access tokens and refresh tokens shall:

* Have controlled lifetimes
* Be scoped
* Be securely stored
* Be transmitted only over TLS
* Support revocation
* Support rotation
* Avoid unnecessary persistence

---

## SR-007 — Secure Storage

Sensitive mobile data shall use platform secure storage.

iOS shall use:

* Keychain
* Secure Enclave where applicable

Android shall use:

* Android Keystore
* Encrypted storage mechanisms

---

## SR-008 — No Plaintext Secrets

The application shall never store the following in plaintext:

* Passwords
* Refresh tokens
* API keys
* OAuth client secrets
* Integration credentials
* Encryption keys
* Payment credentials
* Database credentials
* Service credentials

---

## SR-009 — Application Secrets

Long-lived backend secrets shall never be embedded inside the mobile binary.

The following shall never be hardcoded:

```text
DATABASE_PASSWORD
PRIVATE_API_KEY
JWT_SIGNING_SECRET
ENCRYPTION_KEY
OAUTH_CLIENT_SECRET
SERVICE_ACCOUNT_PRIVATE_KEY
```

---

## SR-010 — Secure Configuration

Public mobile configuration shall contain only information safe for client exposure.

Sensitive configuration shall be delivered through protected backend mechanisms.

---

## SR-011 — Authentication Service

The mobile application shall communicate with the centralized SalesGenie authentication service.

The authentication service shall manage:

* Identity
* Login
* MFA
* Tokens
* Sessions
* Device registration
* Account recovery
* Security events

---

## SR-012 — Authorization Service

Authorization shall be enforced server-side through:

* RBAC
* ABAC
* Resource ownership
* Tenant isolation
* Permission policies
* Organization policies
* Workplace policies

---

## SR-013 — Tenant Isolation

Every authenticated API request shall be associated with an authorized tenant context.

The backend shall prevent:

```text
Tenant A → Tenant B Data
Organization A → Organization B Data
Workplace A → Workplace B Data
User A → User B Private Data
```

---

## SR-014 — API Request Integrity

Requests shall contain appropriate:

* Authorization
* Correlation ID
* Request ID
* Device/session context
* API version
* Content type

Sensitive requests may require additional anti-replay controls.

---

## SR-015 — Replay Protection

High-risk operations shall use replay-resistant mechanisms where appropriate.

Examples:

* Payment operations
* Permission changes
* MFA changes
* Password changes
* API key creation
* Integration authorization
* Administrative actions

---

## SR-016 — Rate Limiting

The backend shall enforce rate limits per:

* User
* Device
* IP
* Session
* Organization
* API key
* Endpoint
* Integration
* AI agent

---

## SR-017 — Abuse Prevention

The system shall detect and mitigate:

* Credential stuffing
* Brute force
* Token abuse
* API scraping
* Automated account creation
* Excessive AI requests
* Malicious file uploads
* Suspicious automation
* Session hijacking

---

## SR-018 — Secure Deep Links

Deep links shall be validated.

The application shall prevent unauthorized deep-link execution.

---

## SR-019 — Universal Links / App Links

Where supported, the application shall use:

* iOS Universal Links
* Android App Links

Domain verification shall be enforced.

---

## SR-020 — Secure WebViews

WebViews shall be restricted.

The application shall prevent:

* Arbitrary navigation
* JavaScript injection
* Unauthorized file access
* Credential leakage
* Unsafe URL schemes

---

## SR-021 — Screenshot Protection

Highly sensitive screens may use platform-specific protections.

Examples:

* Android screenshot restrictions
* Sensitive UI masking
* iOS privacy overlays

---

## SR-022 — Clipboard Security

Sensitive information shall not be copied to the clipboard by default.

Where copying is permitted, the application should warn users about sensitive content.

---

## SR-023 — Background Privacy

Sensitive information shall not remain visible when the application enters the background.

The application shall display a privacy overlay where appropriate.

---

## SR-024 — Logging Security

The mobile application shall never log:

* Passwords
* Access tokens
* Refresh tokens
* API keys
* Payment credentials
* MFA secrets
* Personal secrets
* Confidential customer data

---

## SR-025 — Crash Reporting

Crash reports shall be sanitized before transmission.

Sensitive data shall be excluded from:

* Stack traces
* Metadata
* Breadcrumbs
* Request bodies
* Headers
* Local storage dumps

---

## 7. Functional Requirements

## 7.1 Authentication

### FR-AUTH-001

The application shall provide secure login.

### FR-AUTH-002

The application shall validate authentication responses from the backend.

### FR-AUTH-003

The application shall securely store refresh credentials.

### FR-AUTH-004

The application shall automatically refresh access tokens when permitted.

### FR-AUTH-005

The application shall handle expired sessions.

### FR-AUTH-006

The application shall redirect unauthenticated users to authentication.

### FR-AUTH-007

The application shall invalidate local authentication state after logout.

### FR-AUTH-008

The backend shall invalidate revoked sessions.

---

## 8. MFA Functional Requirements

### FR-MFA-001

The application shall support MFA enrollment.

### FR-MFA-002

The application shall support MFA verification.

### FR-MFA-003

The application shall support MFA recovery mechanisms.

### FR-MFA-004

MFA configuration changes shall require strong authentication.

### FR-MFA-005

MFA changes shall generate security audit events.

### FR-MFA-006

The backend shall enforce organization-level MFA policies.

---

## 9. Biometric Security

### FR-BIO-001

The application shall detect supported biometric capabilities.

### FR-BIO-002

The application shall allow users to enable biometric unlock.

### FR-BIO-003

Biometric credentials shall never be transmitted to SalesGenie servers.

### FR-BIO-004

Biometric unlock shall release locally protected credentials only after successful platform authentication.

### FR-BIO-005

The application shall require fallback authentication when biometric authentication fails according to platform policy.

---

## 10. Session Management

### FR-SESSION-001

The backend shall issue short-lived access tokens.

### FR-SESSION-002

The backend shall issue securely managed refresh credentials.

### FR-SESSION-003

Refresh tokens shall support rotation.

### FR-SESSION-004

Compromised refresh tokens shall be revocable.

### FR-SESSION-005

The system shall detect refresh-token reuse where supported.

### FR-SESSION-006

The mobile application shall gracefully handle session expiration.

### FR-SESSION-007

The system shall support remote session revocation.

---

## 11. Device Security

### FR-DEVICE-001

The application shall register devices securely.

### FR-DEVICE-002

Device registration shall be associated with an authenticated user.

### FR-DEVICE-003

The backend shall maintain device/session relationships.

### FR-DEVICE-004

Users shall be able to revoke devices where permitted.

### FR-DEVICE-005

Administrators shall be able to revoke sessions according to permissions.

### FR-DEVICE-006

Risk signals may include:

* Root detection
* Jailbreak detection
* Emulator detection
* Debugger detection
* Application integrity
* Device reputation
* Abnormal behavior

---

## 12. Root/Jailbreak Detection

### FR-INTEGRITY-001

The application may detect potentially compromised devices.

### FR-INTEGRITY-002

High-risk functionality may be restricted on compromised devices.

### FR-INTEGRITY-003

The application shall avoid treating root/jailbreak detection as the sole security boundary.

### FR-INTEGRITY-004

Backend risk controls shall remain authoritative.

---

## 13. API Security

### FR-API-001

Every protected API request shall require valid authentication.

### FR-API-002

Every protected resource shall require server-side authorization.

### FR-API-003

The backend shall validate all request parameters.

### FR-API-004

The backend shall reject malformed requests.

### FR-API-005

The backend shall prevent mass assignment vulnerabilities.

### FR-API-006

The backend shall prevent IDOR/BOLA vulnerabilities.

### FR-API-007

The backend shall enforce object-level authorization.

### FR-API-008

The backend shall enforce tenant-level authorization.

### FR-API-009

The backend shall enforce rate limits.

### FR-API-010

The backend shall record security-relevant API events.

---

## 14. Data Security

### FR-DATA-001

Sensitive data shall be encrypted in transit.

### FR-DATA-002

Sensitive local data shall be encrypted at rest.

### FR-DATA-003

Sensitive cached API responses shall be encrypted or avoided.

### FR-DATA-004

Temporary sensitive files shall be securely managed.

### FR-DATA-005

Downloaded documents shall inherit backend authorization policies.

### FR-DATA-006

Deleted local sensitive data shall become inaccessible to the application.

---

## 15. Offline Security

### FR-OFFLINE-001

Offline functionality shall be explicitly defined per feature.

### FR-OFFLINE-002

Sensitive offline data shall be encrypted.

### FR-OFFLINE-003

Offline data shall be associated with the correct tenant and user.

### FR-OFFLINE-004

Offline operations shall be queued securely.

### FR-OFFLINE-005

Offline mutations shall be authorized again when synchronized.

### FR-OFFLINE-006

Conflicting authorization changes shall invalidate unauthorized offline operations.

### FR-OFFLINE-007

The application shall not allow offline access after account/session revocation where policy requires immediate enforcement.

---

## 16. File Security

### FR-FILE-001

File uploads shall be authenticated.

### FR-FILE-002

File uploads shall be authorized.

### FR-FILE-003

Backend services shall validate file type.

### FR-FILE-004

Backend services shall validate file size.

### FR-FILE-005

Malware scanning shall be performed where required.

### FR-FILE-006

Files shall be stored in protected object storage.

### FR-FILE-007

File download URLs shall be short-lived and access-controlled.

### FR-FILE-008

Users shall not be able to enumerate unauthorized files.

---

## 17. AI Security

### FR-AI-001

Mobile users shall only access authorized AI agents.

### FR-AI-002

AI agent permissions shall be enforced by backend services.

### FR-AI-003

AI tools shall execute according to server-side authorization.

### FR-AI-004

The mobile client shall never directly receive privileged AI tool credentials.

### FR-AI-005

AI actions shall be auditable.

### FR-AI-006

High-risk AI actions shall support human approval.

### FR-AI-007

Prompt injection defenses shall be implemented server-side.

### FR-AI-008

Sensitive data shall not be unnecessarily exposed to LLM providers.

### FR-AI-009

AI agent tool access shall respect tenant isolation.

### FR-AI-010

AI-generated actions shall contain sufficient metadata for auditing.

---

## 18. AI + Human Hybrid Security

### FR-HYBRID-001

AI agents shall be able to request human approval for high-risk operations.

### FR-HYBRID-002

Human reviewers shall only see data they are authorized to access.

### FR-HYBRID-003

Approval actions shall be authenticated.

### FR-HYBRID-004

Approval actions shall be authorized.

### FR-HYBRID-005

Approval events shall be audited.

### FR-HYBRID-006

The system shall prevent unauthorized users from approving AI actions.

---

## 19. Integration Security

### FR-INTEGRATION-001

Integration credentials shall be managed by backend services.

### FR-INTEGRATION-002

OAuth tokens shall not be exposed unnecessarily to mobile clients.

### FR-INTEGRATION-003

Integration permissions shall be scoped.

### FR-INTEGRATION-004

Users shall be able to revoke integrations where authorized.

### FR-INTEGRATION-005

Integration changes shall generate audit events.

### FR-INTEGRATION-006

Backend services shall enforce integration ownership.

### FR-INTEGRATION-007

Integration tokens shall be encrypted at rest.

---

## 20. Notification Security

### FR-NOTIFY-001

Push notifications shall use authenticated device registration.

### FR-NOTIFY-002

Notification payloads shall avoid sensitive information.

### FR-NOTIFY-003

Security-sensitive notification details shall be retrieved through authenticated API calls.

### FR-NOTIFY-004

Notification tokens shall be revocable.

### FR-NOTIFY-005

Notification preferences shall be stored server-side where required.

### FR-NOTIFY-006

Notification authorization shall be tenant-aware.

---

## 21. Payment and Billing Security

### FR-BILLING-001

Mobile clients shall never store raw payment credentials unless explicitly required by a certified payment SDK.

### FR-BILLING-002

Payment operations shall be executed through secure backend/payment-provider workflows.

### FR-BILLING-003

Billing permissions shall be enforced server-side.

### FR-BILLING-004

Invoice access shall be authorization-controlled.

### FR-BILLING-005

Refund operations shall require appropriate privileges.

### FR-BILLING-006

Billing security events shall be audited.

---

## 22. Administrative Security

### FR-ADMIN-001

Administrative mobile functions shall require elevated permissions.

### FR-ADMIN-002

Administrative APIs shall enforce RBAC/ABAC.

### FR-ADMIN-003

High-risk administrative operations shall support step-up authentication.

### FR-ADMIN-004

Administrative actions shall be audited.

### FR-ADMIN-005

Super Admin operations shall require stronger security controls.

### FR-ADMIN-006

Security Admin operations shall be separately authorized.

### FR-ADMIN-007

Billing Admin operations shall be restricted to billing resources.

### FR-ADMIN-008

Administrators shall not automatically receive unrestricted access to customer data.

---

## 23. Role and Permission Synchronization

### FR-RBAC-001

The mobile application shall retrieve effective permissions from backend services.

### FR-RBAC-002

Permission changes shall propagate to active sessions according to security policy.

### FR-RBAC-003

The mobile application shall not permanently cache authorization decisions.

### FR-RBAC-004

Revoked permissions shall prevent future unauthorized API operations.

### FR-RBAC-005

Frontend feature visibility shall not replace backend authorization.

---

## 24. Tenant Isolation

### FR-TENANT-001

Every tenant-sensitive API request shall contain server-derived tenant context.

### FR-TENANT-002

The backend shall validate resource ownership.

### FR-TENANT-003

Cross-tenant resource access shall be denied.

### FR-TENANT-004

Cross-tenant search shall be prohibited unless explicitly authorized.

### FR-TENANT-005

Tenant boundaries shall apply to:

* Users
* Contacts
* Leads
* Accounts
* Opportunities
* Conversations
* Tickets
* Documents
* Knowledge bases
* AI agents
* Workflows
* Integrations
* Reports
* Analytics
* Billing
* Audit logs

---

## 25. Secure Search

### FR-SEARCH-001

Mobile search requests shall be authenticated.

### FR-SEARCH-002

Search results shall be filtered by backend permissions.

### FR-SEARCH-003

Search indexes shall enforce tenant isolation.

### FR-SEARCH-004

Semantic search shall enforce document-level permissions.

### FR-SEARCH-005

AI-powered search shall not bypass authorization.

---

## 26. RAG Security

### FR-RAG-001

RAG queries shall execute within the user's authorization context.

### FR-RAG-002

Unauthorized documents shall never be retrieved.

### FR-RAG-003

Vector search shall enforce tenant boundaries.

### FR-RAG-004

Knowledge-base permissions shall be evaluated server-side.

### FR-RAG-005

AI responses shall not expose unauthorized retrieved content.

### FR-RAG-006

RAG audit events shall capture security-relevant retrieval information.

---

## 27. Secure Analytics

### FR-ANALYTICS-001

Analytics events shall avoid sensitive information.

### FR-ANALYTICS-002

User identifiers shall be minimized where possible.

### FR-ANALYTICS-003

Analytics access shall follow tenant permissions.

### FR-ANALYTICS-004

Administrative analytics shall require appropriate authorization.

### FR-ANALYTICS-005

Financial analytics shall be restricted to authorized roles.

---

## 28. Audit Logging

### FR-AUDIT-001

The backend shall generate immutable audit events for security-sensitive operations.

Events shall include:

* Login
* Logout
* Failed login
* MFA change
* Password change
* Device registration
* Session revocation
* Permission changes
* Role changes
* Organization membership changes
* Integration changes
* API key changes
* AI agent changes
* Workflow execution
* Administrative operations
* Billing operations
* Security incidents

### FR-AUDIT-002

Audit records shall contain:

```text
event_id
timestamp
actor_id
tenant_id
organization_id
workplace_id
action
resource_type
resource_id
result
ip_metadata
device_metadata
session_id
request_id
correlation_id
risk_context
```

### FR-AUDIT-003

Audit records shall be protected against unauthorized modification.

---

## 29. Security Monitoring

### FR-MONITOR-001

The backend shall monitor mobile authentication activity.

### FR-MONITOR-002

The backend shall monitor suspicious device activity.

### FR-MONITOR-003

The backend shall detect abnormal API usage.

### FR-MONITOR-004

The backend shall detect unusual login patterns.

### FR-MONITOR-005

The backend shall correlate mobile security events with backend events.

### FR-MONITOR-006

Security events shall integrate with the SalesGenie incident-management system.

---

## 30. Threat Detection

The platform shall detect where technically feasible:

* Brute-force attacks
* Credential stuffing
* Token theft
* Session hijacking
* API abuse
* Bot activity
* Account takeover
* Impossible travel
* Abnormal device changes
* Suspicious IP activity
* Data scraping
* Excessive exports
* Malicious file uploads
* AI abuse
* Prompt injection attempts
* Tool abuse
* Integration abuse

---

## 31. Account Takeover Protection

### FR-ATO-001

The system shall detect abnormal authentication behavior.

### FR-ATO-002

The system shall support adaptive authentication.

### FR-ATO-003

High-risk operations shall trigger step-up authentication.

### FR-ATO-004

Compromised sessions shall be revocable.

### FR-ATO-005

Users shall receive account-security notifications.

---

## 32. Secure Password Handling

### FR-PASSWORD-001

Passwords shall be transmitted only over TLS.

### FR-PASSWORD-002

Passwords shall never be stored by the mobile application.

### FR-PASSWORD-003

Password reset shall be backend-controlled.

### FR-PASSWORD-004

Password changes shall invalidate appropriate sessions.

### FR-PASSWORD-005

Password security events shall be audited.

---

## 33. Secure API Keys

### FR-APIKEY-001

API keys shall never be embedded in the application binary.

### FR-APIKEY-002

Users shall be able to create API keys only with appropriate permissions.

### FR-APIKEY-003

API keys shall be displayed securely.

### FR-APIKEY-004

Full API keys shall not be repeatedly displayed after creation.

### FR-APIKEY-005

API keys shall support revocation.

### FR-APIKEY-006

API key creation and revocation shall be audited.

---

## 34. Secure Cache

### FR-CACHE-001

Sensitive data shall not be stored in insecure caches.

### FR-CACHE-002

Authentication state shall be stored only in secure storage.

### FR-CACHE-003

Cached tenant data shall be isolated.

### FR-CACHE-004

Sensitive cached data shall be deleted after logout according to policy.

---

## 35. Secure Database Interaction

The mobile application shall never connect directly to:

* PostgreSQL
* Redis
* Data warehouse
* Vector database
* Object storage databases
* Internal microservice databases

All data access shall occur through authenticated backend APIs.

---

## 36. Backend Connectivity Requirements

The mobile application shall securely communicate with:

```text
Mobile Application
        │
        ▼
API Gateway
        │
        ├── Authentication Service
        ├── Authorization Service
        ├── User Service
        ├── Organization Service
        ├── CRM Service
        ├── Lead Intelligence Service
        ├── Sales Service
        ├── Marketing Service
        ├── SEO Service
        ├── Support Service
        ├── AI Gateway
        ├── Agent Service
        ├── RAG Service
        ├── Workflow Service
        ├── Integration Service
        ├── Notification Service
        ├── Billing Service
        ├── Analytics Service
        └── Audit/Security Service
```

---

## 37. Mobile API Security Contract

Every protected API shall support:

```text
Authentication
Authorization
Tenant Validation
Input Validation
Rate Limiting
Threat Detection
Request Tracing
Audit Logging
Error Sanitization
```

---

## 38. Secure Error Handling

### FR-ERROR-001

The mobile application shall not display backend stack traces.

### FR-ERROR-002

Internal infrastructure details shall not be exposed to users.

### FR-ERROR-003

Security-sensitive errors shall use generic messages where appropriate.

### FR-ERROR-004

The backend shall return structured error codes.

Example:

```json
{
  "error": {
    "code": "AUTHORIZATION_DENIED",
    "message": "You do not have permission to perform this action.",
    "request_id": "request-id"
  }
}
```

---

## 39. Secure AI Tool Execution

AI agents shall never directly execute privileged operations from the mobile client.

The execution model shall be:

```text
Mobile User
    ↓
Authenticated API
    ↓
AI Gateway
    ↓
Agent Authorization
    ↓
Tool Permission Check
    ↓
Policy Evaluation
    ↓
Human Approval if Required
    ↓
Tool Execution
    ↓
Audit Event
    ↓
Result
```

---

## 40. High-Risk Operations

The following operations should support additional security controls:

* Delete organization
* Delete workplace
* Delete customer data
* Export large datasets
* Change administrator roles
* Change security settings
* Disable MFA
* Create API keys
* Rotate integration credentials
* Change billing ownership
* Issue refunds
* Modify payment configuration
* Execute privileged AI tools
* Execute destructive workflows
* Bulk delete records
* Change tenant configuration

---

## 41. Step-Up Authentication

The backend shall support step-up authentication for high-risk operations.

Possible mechanisms:

* MFA
* Passkey
* Biometric confirmation
* Reauthentication
* Security key
* Trusted-device verification

---

## 42. Secure Data Export

### FR-EXPORT-001

Exports shall require authorization.

### FR-EXPORT-002

Large exports shall require additional controls.

### FR-EXPORT-003

Export operations shall be audited.

### FR-EXPORT-004

Export files shall use protected storage.

### FR-EXPORT-005

Export download URLs shall expire.

### FR-EXPORT-006

The system shall prevent unauthorized cross-tenant exports.

---

## 43. Secure Report Access

Reports shall be protected according to:

* User permissions
* Organization permissions
* Workplace permissions
* Report ownership
* Data sensitivity
* Role

---

## 44. Secure Push Token Management

The backend shall maintain:

```text
user_id
device_id
platform
push_token
application_version
device_status
last_seen
security_state
```

Push tokens shall be revocable and rotated as required.

---

## 45. Mobile Application Integrity

The application should implement:

* Code signing
* Secure release builds
* Release certificate protection
* Binary integrity validation
* Runtime integrity checks
* Debug build separation
* Secure update mechanisms

---

## 46. Anti-Tampering

The application should detect:

* Modified binaries
* Unauthorized code injection
* Debugging attempts
* Hooking frameworks
* Runtime instrumentation
* Unexpected package signatures

Backend risk controls shall remain authoritative.

---

## 47. Secure Build Pipeline

Mobile builds shall use secure CI/CD pipelines.

The pipeline shall enforce:

```text
Source Code
    ↓
Dependency Scanning
    ↓
Static Analysis
    ↓
Secret Scanning
    ↓
Security Tests
    ↓
Build
    ↓
Code Signing
    ↓
Artifact Verification
    ↓
Release
```

---

## 48. Dependency Security

All mobile dependencies shall be:

* Version controlled
* Vulnerability scanned
* Regularly updated
* License reviewed
* Monitored for known vulnerabilities

---

## 49. Supply Chain Security

The system shall protect against:

* Malicious dependencies
* Dependency confusion
* Compromised packages
* Typosquatting
* Build pipeline compromise
* Signing-key compromise

---

## 50. Secure Update Requirements

### FR-UPDATE-001

The application shall periodically verify supported versions.

### FR-UPDATE-002

Critical vulnerabilities may trigger mandatory upgrades.

### FR-UPDATE-003

The backend shall be able to block unsupported insecure versions.

### FR-UPDATE-004

Users shall receive clear upgrade instructions.

---

## 51. Privacy Requirements

The application shall minimize collection of:

* Device data
* Location data
* Personal data
* Usage data
* Behavioral data

Only necessary information shall be collected.

---

## 52. Sensitive Data Classification

SalesGenie shall classify mobile-accessible data as:

### Public

* Public product information
* Public marketing information

### Internal

* Internal business configuration
* Non-sensitive analytics

### Confidential

* Customer information
* Leads
* Sales pipelines
* AI conversations
* Documents

### Restricted

* Payment information
* Credentials
* API keys
* Security data
* Authentication secrets
* Sensitive customer information

---

## 53. Data Retention

Mobile-local data retention shall be minimized.

The application shall define retention policies for:

* Cache
* Offline records
* Temporary files
* Logs
* Crash reports
* Analytics data
* Authentication state

---

## 54. Secure Deletion

When required, the system shall support deletion of locally stored sensitive information after:

* Logout
* Device removal
* Account deletion
* Organization removal
* Security revocation

---

## 55. Accessibility Security

Security controls shall remain accessible to users with disabilities.

Examples:

* MFA
* Biometric alternatives
* Security dialogs
* Session controls
* Permission prompts
* Account recovery

Security shall not depend exclusively on inaccessible interaction patterns.

---

## 56. Localization Security

Localized security messages shall preserve security semantics.

Translations shall not weaken:

* Authentication warnings
* Security alerts
* Permission descriptions
* Consent requirements
* Privacy notices
* Account recovery instructions

---

## 57. Security Testing Requirements

The mobile platform shall undergo:

* Unit security testing
* Integration security testing
* API security testing
* E2E security testing
* Penetration testing
* Static analysis
* Dynamic analysis
* Dependency scanning
* Secret scanning
* Mobile application security testing
* Authentication testing
* Authorization testing
* Session testing
* Cryptographic testing
* Network security testing
* Storage security testing
* AI security testing

---

## 58. OWASP Alignment

The mobile application shall address applicable risks from:

* OWASP Mobile Top 10
* OWASP API Security Top 10
* OWASP ASVS
* OWASP MASVS
* OWASP LLM security guidance

---

## 59. Security Observability

The mobile security architecture shall integrate with SalesGenie's observability platform.

Security telemetry shall support:

```text
Authentication Metrics
Authorization Metrics
Session Metrics
Device Risk Metrics
API Abuse Metrics
Security Event Metrics
AI Security Metrics
Integration Security Metrics
Application Integrity Metrics
```

---

## 60. Incident Response

The mobile platform shall integrate with the centralized incident response system.

The system shall support:

```text
Detection
   ↓
Classification
   ↓
Risk Assessment
   ↓
Containment
   ↓
Session Revocation
   ↓
Credential Revocation
   ↓
User Notification
   ↓
Investigation
   ↓
Recovery
   ↓
Post-Incident Review
```

---

## 61. Remote Security Controls

Authorized security administrators shall be able to:

* Revoke sessions
* Revoke devices
* Disable accounts
* Force logout
* Require password reset
* Require MFA
* Disable compromised integrations
* Block insecure app versions
* Restrict high-risk functionality
* Trigger security investigations

---

## 62. Security Feature Flags

Security-sensitive functionality shall support controlled feature flags.

Examples:

```text
require_mfa
disable_legacy_auth
require_minimum_app_version
disable_high_risk_ai_tools
disable_file_uploads
disable_external_integrations
force_reauthentication
enable_device_attestation
```

Feature flags shall be evaluated server-side for security-critical decisions.

---

## 63. Compliance

The mobile platform shall support applicable compliance requirements including:

* GDPR
* CCPA/CPRA
* Data protection requirements
* Enterprise security requirements
* Applicable payment security requirements

Compliance controls shall be enforced across both mobile and backend systems.

---

## 64. Security Acceptance Criteria

The SalesGenie mobile platform shall not be considered production-ready until:

* Authentication is secure.
* MFA is implemented.
* Sessions are revocable.
* Tokens are securely stored.
* TLS is enforced.
* Authorization is backend-controlled.
* Tenant isolation is verified.
* Sensitive data is encrypted.
* No production secrets exist in the binary.
* API security testing passes.
* Mobile penetration testing passes.
* Dependency vulnerabilities are controlled.
* Secure logging is implemented.
* Audit logging is operational.
* Security monitoring is operational.
* Incident response is integrated.
* Secure update mechanisms are operational.
* AI operations are authorization-controlled.
* RAG access is permission-aware.
* Integration credentials are protected.
* High-risk operations support additional security controls.
* Root/jailbreak and tampering risks are addressed.
* Privacy requirements are implemented.
* Security-critical failures fail closed.

---

## 65. Security Architecture Summary

```text
                         SALES GENIE MOBILE
                                │
                    ┌───────────┴───────────┐
                    │                       │
              iOS Application        Android Application
                    │                       │
                    └───────────┬───────────┘
                                │
                         TLS / Secure Network
                                │
                                ▼
                         API Gateway / WAF
                                │
                ┌───────────────┼────────────────┐
                │               │                │
                ▼               ▼                ▼
        Authentication    Authorization     Threat Detection
                │               │                │
                └───────────────┼────────────────┘
                                ▼
                       Tenant / Policy Layer
                                │
                ┌───────────────┼────────────────┐
                ▼               ▼                ▼
           AI Gateway       Business APIs    Integration APIs
                │               │                │
                ▼               ▼                ▼
           AI Agents        Microservices     External APIs
                │               │                │
                └───────────────┼────────────────┘
                                ▼
                         Data Protection
                                │
             ┌──────────────────┼──────────────────┐
             ▼                  ▼                  ▼
          Database          Object Storage      Vector DB
             │                  │                  │
             └──────────────────┼──────────────────┘
                                ▼
                    Security / Audit Platform
                                │
                ┌───────────────┼────────────────┐
                ▼               ▼                ▼
            Logging          Metrics          Tracing
                │               │                │
                └───────────────┼────────────────┘
                                ▼
                      Security Operations
                                │
                ┌───────────────┼────────────────┐
                ▼               ▼                ▼
          Threat Detection   Incident Mgmt   Admin Controls
```

---

## 66. Core Security Invariants

The following invariants shall always hold:

```text
1. The mobile client is never trusted.

2. Authentication is required for protected resources.

3. Authorization is always enforced server-side.

4. Tenant boundaries cannot be bypassed from the mobile client.

5. Client-side role checks are never security boundaries.

6. Sensitive credentials are never stored in plaintext.

7. Backend secrets are never embedded in the application.

8. Sensitive traffic uses authenticated encrypted channels.

9. AI agents cannot bypass authorization.

10. RAG cannot retrieve unauthorized information.

11. Integrations cannot expose unrestricted credentials.

12. High-risk operations require stronger controls.

13. Security events are auditable.

14. Revoked sessions cannot continue privileged access.

15. Security failures default to deny.

16. Mobile security controls complement, but never replace, backend security.
```

---

## 67. Final Security Requirement

SalesGenie mobile security shall follow the principle:

```text
                NEVER TRUST THE CLIENT
                         │
                         ▼
                  VERIFY IDENTITY
                         │
                         ▼
                VERIFY AUTHORIZATION
                         │
                         ▼
                  VERIFY TENANT
                         │
                         ▼
                   VERIFY POLICY
                         │
                         ▼
                 VERIFY RISK CONTEXT
                         │
                         ▼
                EXECUTE AUTHORIZED ACTION
                         │
                         ▼
                     AUDIT IT
                         │
                         ▼
                    MONITOR IT
```

The mobile application shall provide a secure user experience, but **all authoritative security controls shall remain enforced by SalesGenie's backend, API gateway, identity platform, authorization services, AI gateway, integration services, data layer, and security operations infrastructure.**
