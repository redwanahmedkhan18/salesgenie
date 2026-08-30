# SALESGENIE — AUTHENTICATION ARCHITECTURE REQUIREMENTS

**File:** `authentication_architecture.md`  
**Project:** SalesGenie  
**Document Type:** Authentication Architecture — User Requirements, System Requirements & Functional Requirements  
**Version:** 1.0.0  
**Status:** Architecture Baseline  
**Security Classification:** Confidential  
**Target:** Enterprise / FAANG-Level Multi-Tenant SaaS

---

## 1. DOCUMENT PURPOSE

This document defines the complete authentication architecture for SalesGenie.

SalesGenie authentication MUST provide secure, scalable, auditable and tenant-aware identity management for:

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
- AI Agent
- Developer
- End User
- External Client
- API Client
- Service Account
- Other authorized platform identities

The architecture MUST support both:

```text
Human Authentication
+
Machine Authentication
+
AI Agent Identity
+
Service-to-Service Authentication
```

The authentication platform MUST provide:

* Account registration
* Email verification
* Google authentication
* Password authentication
* Password reset
* Session management
* Device management
* Location awareness
* MFA
* Account recovery
* Login protection
* Risk-based authentication
* Token management
* OAuth/OIDC
* API authentication
* Service authentication
* AI-agent authentication
* Tenant-aware identity
* Security notifications
* Audit logging
* Session revocation
* Account lockout
* Suspicious-login detection
* Human security escalation
* AI-assisted security analysis
* Enterprise SSO
* SCIM provisioning
* Secure logout

---

## 2. AUTHENTICATION VISION

SalesGenie authentication MUST follow:

> Zero Trust + Defense in Depth + Least Privilege + Tenant Isolation + Risk-Based Authentication + Secure-by-Default.

The architecture MUST assume:

```text
Every request is untrusted
Every device may be compromised
Every token may eventually be stolen
Every integration may fail
Every identity must be continuously evaluated
```

Authentication MUST therefore not be treated as a one-time login event only.

The security lifecycle SHOULD be:

```text
Identity
   ↓
Authentication
   ↓
Session Establishment
   ↓
Continuous Risk Evaluation
   ↓
Authorization
   ↓
Session Monitoring
   ↓
Reauthentication when necessary
   ↓
Session Revocation / Logout
```

---

## 3. AUTHENTICATION PRINCIPLES

## AUTH-PRINCIPLE-001 — Zero Trust

No authenticated identity SHALL automatically receive access to every resource.

Authentication establishes identity.

Authorization determines access.

---

## AUTH-PRINCIPLE-002 — Least Privilege

Every identity MUST receive only the minimum permissions required.

---

## AUTH-PRINCIPLE-003 — Tenant Isolation

An authenticated user from Organization A MUST NOT be able to access Organization B resources unless explicitly authorized.

---

## AUTH-PRINCIPLE-004 — Secure Defaults

New accounts MUST start with the most restrictive reasonable security configuration.

---

## AUTH-PRINCIPLE-005 — Continuous Verification

High-risk actions MUST be capable of triggering additional verification even when the user already has a valid session.

---

## 4. USER REQUIREMENTS

## UR-AUTH-001 — User Registration

Users MUST be able to create SalesGenie accounts using:

1. Email + password
2. Google authentication

Additional enterprise identity providers MAY be supported later.

---

## UR-AUTH-002 — Email Verification

A newly registered email/password account MUST be verified before normal account access is enabled.

The system MUST send a 6-digit verification code.

Example:

```text
Registration
     ↓
Email submitted
     ↓
Password created
     ↓
Verification code generated
     ↓
Email sent
     ↓
User enters 6-digit code
     ↓
Verification successful
     ↓
Account activated
     ↓
Login page
```

---

## UR-AUTH-003 — Verification Code Expiration

The email verification code MUST expire after:

```text
15 minutes
```

Expired codes MUST be rejected.

---

## UR-AUTH-004 — Verification Code Security

Verification codes MUST:

* Be cryptographically generated
* Be single-use
* Expire automatically
* Have limited retry attempts
* Be rate limited
* Never be stored as plaintext where avoidable
* Never appear in application logs

---

## UR-AUTH-005 — Google Registration

Users MUST be able to select:

```text
Continue with Google
```

The platform MUST authenticate the identity using a secure OAuth 2.0 / OpenID Connect flow.

---

## UR-AUTH-006 — Google Account Password

After successful Google registration, SalesGenie MUST require the user to establish a SalesGenie password if the product policy requires password-based recovery or fallback authentication.

The system MUST NOT retrieve or store the user's Google password.

---

## UR-AUTH-007 — Login

Users MUST be able to log in using their registered:

* Username
* Email
* Password

or supported identity providers.

---

## UR-AUTH-008 — Designation-Based Dashboard

After successful authentication, the system MUST determine the user's authorized designation and redirect them to the appropriate dashboard.

Example:

```text
Super Admin
    ↓
Super Admin Dashboard

Sales Manager
    ↓
Sales Dashboard

Marketing Manager
    ↓
Marketing Dashboard

SEO Specialist
    ↓
SEO Workspace

Support Agent
    ↓
Support Console

End User
    ↓
Customer Dashboard
```

Dashboard selection MUST be based on authorization claims rather than frontend-only role checks.

---

## UR-AUTH-009 — Invalid Login Protection

The platform MUST protect against:

* Brute-force attacks
* Credential stuffing
* Password spraying
* Automated login attempts
* Suspicious login behavior

---

## UR-AUTH-010 — Password Requirements

Passwords MUST contain at least:

```text
8 characters
+
Uppercase letter
+
Lowercase letter
+
Digit
+
Special character
```

The system SHOULD enforce stronger requirements for privileged accounts.

---

## UR-AUTH-011 — Password Reset

Users MUST be able to request a password reset using:

* Registered email
* Registered username

The system MUST NOT reveal whether an account exists through overly specific error messages.

Preferred response:

```text
"If an account exists for the provided information,
we will send password recovery instructions."
```

---

## UR-AUTH-012 — Password Reset Verification

The system MUST send a secure verification:

```text
Code
OR
Secure verification link
```

The reset request MUST be associated with:

* Account
* Request timestamp
* Device information
* Approximate location information where available
* IP address internally
* Request ID

---

## UR-AUTH-013 — Password Reset Notification

The user MUST receive a security notification containing relevant information about the password-reset request.

Example:

```text
Password reset requested

Device: Firefox / Ubuntu
Approximate location: Dhaka, Bangladesh
Time: 22 Aug 2026
```

The system MUST avoid exposing unnecessary sensitive information.

---

## UR-AUTH-014 — New Password

After successful reset verification, the user MUST see:

```text
New Password
Confirm Password
```

Both fields MUST match.

---

## UR-AUTH-015 — Password Reuse

The platform SHOULD prevent reuse of recently used passwords, especially for privileged accounts.

---

## UR-AUTH-016 — Logout

Users MUST have a proper logout mechanism.

Logout MUST invalidate the current session/token according to the token architecture.

---

## UR-AUTH-017 — Logout All Devices

Users SHOULD be able to:

```text
Log out of this device
Log out of all devices
```

---

## UR-AUTH-018 — Device Management

Users SHOULD be able to view:

* Device
* Browser
* Operating system
* Approximate location
* Last active time
* Session status

and revoke sessions.

---

## UR-AUTH-019 — Suspicious Login Notification

Users MUST receive security notifications when suspicious authentication activity is detected.

Examples:

* New device
* Unusual location
* Multiple failed attempts
* Password reset
* MFA change
* Recovery method change

---

## UR-AUTH-020 — MFA

The platform MUST support Multi-Factor Authentication.

Preferred methods:

* TOTP authenticator
* Recovery codes
* WebAuthn / passkeys
* Security keys

SMS SHOULD NOT be the primary MFA mechanism where stronger methods are available.

---

## UR-AUTH-021 — Privileged Account MFA

The following identities MUST require MFA:

* Super Admin
* Platform Admin
* Security Admin
* Billing Admin
* Organization Owner
* Organization Admin
* Workplace Admin

Organizations SHOULD be able to enforce MFA for additional roles.

---

## UR-AUTH-022 — Passkeys

SalesGenie SHOULD support passkeys using WebAuthn.

Passkeys SHOULD be preferred for phishing-resistant authentication.

---

## UR-AUTH-023 — Account Recovery

The platform MUST provide secure account recovery without allowing attackers to bypass identity verification.

---

## UR-AUTH-024 — Session Visibility

Users MUST be able to view active sessions.

---

## UR-AUTH-025 — Session Revocation

Users MUST be able to revoke suspicious sessions.

Privileged administrators MUST have controlled capability to revoke sessions according to authorization policies.

---

## 5. SYSTEM REQUIREMENTS

## SYS-AUTH-001 — Identity Provider

SalesGenie MUST have a centralized identity/authentication service.

Recommended conceptual architecture:

```text
                   Authentication Service
                           |
       +-------------------+-------------------+
       |                   |                   |
   Password             Google              Enterprise
   Authentication       OIDC/OAuth           SSO
       |                   |                   |
       +-------------------+-------------------+
                           |
                    Identity Service
                           |
                    Session Service
                           |
                    Token Service
```

---

## SYS-AUTH-002 — Authentication Service Responsibilities

The authentication service MUST handle:

* Registration
* Login
* Email verification
* Password management
* OAuth/OIDC
* MFA
* Session management
* Token issuance
* Token revocation
* Recovery
* Device tracking
* Authentication audit events

---

## SYS-AUTH-003 — Identity Model

Every identity SHOULD have a unique immutable identifier.

Example:

```text
user_id = UUID
```

Email and username MUST NOT be used as the immutable primary identity identifier.

---

## SYS-AUTH-004 — Identity Attributes

A user identity SHOULD contain:

```text
user_id
username
email
email_verified
password_status
account_status
mfa_status
created_at
updated_at
last_login_at
```

Role and tenant relationships SHOULD be modeled separately.

---

## SYS-AUTH-005 — Account Status

Supported states SHOULD include:

```text
PENDING_VERIFICATION
ACTIVE
SUSPENDED
LOCKED
DISABLED
DELETED
RECOVERY_REQUIRED
```

---

## SYS-AUTH-006 — Email Verification State

Example:

```text
email_verified = false
```

MUST prevent normal authenticated access until verification requirements are satisfied.

---

## SYS-AUTH-007 — Secure Password Storage

Passwords MUST NEVER be stored in plaintext.

Use a modern password hashing algorithm such as:

```text
Argon2id
```

or another industry-approved password hashing mechanism.

---

## SYS-AUTH-008 — Password Hashing Parameters

Password hashing configuration MUST be:

* Strong
* Versioned
* Upgradeable
* Tunable according to infrastructure capacity

The system MUST support password-hash migration when stronger parameters become necessary.

---

## SYS-AUTH-009 — Credential Protection

Credentials MUST NOT appear in:

* Logs
* Analytics
* Traces
* Error messages
* URLs
* Client-side telemetry

---

## SYS-AUTH-010 — Token Architecture

SalesGenie SHOULD use short-lived access tokens with refresh-token/session mechanisms.

Conceptually:

```text
Login
  ↓
Access Token
  +
Refresh Token / Session
```

Access tokens SHOULD have short lifetimes.

---

## SYS-AUTH-011 — Access Token

Access tokens MUST contain only necessary claims.

Example:

```text
sub
iss
aud
iat
exp
jti
tenant context where appropriate
authorization context where appropriate
```

Sensitive information MUST NOT be embedded unnecessarily.

---

## SYS-AUTH-012 — Refresh Token Security

Refresh tokens MUST:

* Be high entropy
* Be revocable
* Be rotated where appropriate
* Be bound to a session
* Have expiration
* Be protected against replay

---

## SYS-AUTH-013 — Refresh Token Rotation

The system SHOULD implement refresh-token rotation.

```text
Refresh Token A
      ↓
Refresh
      ↓
Access Token B
      +
Refresh Token B

Token A → invalidated
```

Replay of an invalidated refresh token SHOULD trigger security controls.

---

## SYS-AUTH-014 — Token Revocation

The platform MUST support revoking:

* Individual sessions
* Refresh tokens
* User sessions
* Organization sessions
* Emergency global sessions

---

## SYS-AUTH-015 — JWT Validation

If JWTs are used, services MUST validate:

```text
Signature
Issuer
Audience
Expiration
Issued-at where applicable
Not-before where applicable
Algorithm
Key ID
```

---

## SYS-AUTH-016 — JWT Time Handling

Expiration timestamps MUST use consistent units.

For example:

```text
JWT exp → Unix seconds
```

The application MUST NOT compare JWT seconds directly with JavaScript millisecond timestamps.

Correct conceptual comparison:

```text
current_time_seconds = floor(Date.now() / 1000)
```

---

## SYS-AUTH-017 — Signing Keys

Token signing keys MUST be stored securely.

Recommended:

* KMS
* Secret manager
* HSM where required

Private signing keys MUST NOT be committed to source control.

---

## SYS-AUTH-018 — Key Rotation

Signing keys MUST support rotation.

Example:

```text
Key A → Active
Key B → Prepared

Rotate

Key B → Active
Key A → Verification-only
```

Old keys MUST remain available for validation only as long as required by token lifetime and migration policy.

---

## SYS-AUTH-019 — HTTPS

All authentication communication MUST use TLS.

Plain HTTP MUST NOT be used for production authentication traffic.

---

## SYS-AUTH-020 — Secure Cookies

If cookies are used for session/refresh mechanisms, they SHOULD use:

```text
Secure
HttpOnly
SameSite
```

with an appropriate SameSite policy for the application's architecture.

---

## SYS-AUTH-021 — CSRF Protection

Cookie-based authenticated operations MUST implement appropriate CSRF protection.

---

## SYS-AUTH-022 — CORS

CORS MUST use explicit trusted origins.

Wildcard authentication origins MUST NOT be used in production.

---

## SYS-AUTH-023 — Login Rate Limiting

Login endpoints MUST implement rate limiting based on multiple signals.

Potential dimensions:

```text
IP
Account
Device
Network
Tenant
```

---

## SYS-AUTH-024 — Credential Stuffing Detection

The system SHOULD detect repeated authentication attempts against many accounts from shared infrastructure.

---

## SYS-AUTH-025 — Password Spraying Detection

The system SHOULD detect repeated attempts using common passwords across many accounts.

---

## SYS-AUTH-026 — Account Lockout

Account lockout MUST be carefully implemented to avoid enabling attackers to permanently lock legitimate users.

Preferred approach:

```text
Progressive delays
+
Risk-based controls
+
Temporary lock
+
MFA challenge
```

rather than indefinite permanent lockout.

---

## SYS-AUTH-027 — CAPTCHA / Bot Protection

The platform SHOULD dynamically require bot challenges when authentication risk increases.

---

## SYS-AUTH-028 — Risk Engine

SalesGenie SHOULD contain an authentication risk engine.

Inputs MAY include:

```text
IP reputation
Device
Location
Login velocity
Failed attempts
Known sessions
Behavior
ASN/network
MFA status
Credential risk
```

Output:

```text
LOW
MEDIUM
HIGH
CRITICAL
```

---

## SYS-AUTH-029 — Risk-Based Authentication

Example:

```text
Normal login
   ↓
Low risk
   ↓
Password authentication

New device
   ↓
Medium risk
   ↓
Password + MFA

Impossible travel / anomaly
   ↓
High risk
   ↓
Additional verification

Critical risk
   ↓
Block + security review
```

---

## SYS-AUTH-030 — AI-Assisted Security

AI MAY assist in:

* Anomaly detection
* Login behavior analysis
* Threat classification
* Risk scoring
* Security event correlation

AI MUST NOT be the sole authority for irreversible high-impact security decisions.

---

## SYS-AUTH-031 — Human Security Escalation

High-risk authentication events MUST be capable of escalation to authorized human security personnel.

```text
Security AI
    ↓
Risk assessment
    ↓
Rule Engine
    ↓
Human Security Team
```

---

## SYS-AUTH-032 — Audit Logging

Authentication events MUST be auditable.

Events include:

```text
Registration
Email verification
Login success
Login failure
Logout
Password change
Password reset
MFA enrollment
MFA removal
Google login
Session creation
Session revocation
Account lock
Account unlock
Security escalation
```

---

## SYS-AUTH-033 — Audit Log Integrity

Security logs SHOULD be tamper-resistant and access-controlled.

---

## SYS-AUTH-034 — Privacy

Authentication telemetry MUST follow applicable privacy requirements.

Location information SHOULD be approximate where exact location is unnecessary.

---

## 6. FUNCTIONAL REQUIREMENTS

## FR-AUTH-001 — Registration

The system SHALL provide an account registration endpoint/UI.

Required fields:

```text
Email
Username where applicable
Password
Confirm Password
```

---

## FR-AUTH-002 — Registration Validation

The system SHALL validate:

* Email syntax
* Email uniqueness
* Username uniqueness
* Password policy
* Terms acceptance where required
* Abuse/rate limits

---

## FR-AUTH-003 — Email Verification Code

The system SHALL generate a 6-digit verification code.

Properties:

```text
6 digits
15-minute expiration
Single-use
Attempt limited
Rate limited
```

---

## FR-AUTH-004 — Verification

The system SHALL allow users to enter the verification code.

Successful verification SHALL:

```text
Mark email verified
Activate account according to policy
Invalidate code
Record audit event
```

---

## FR-AUTH-005 — Resend Verification

Users SHALL be able to request another verification code subject to rate limits.

---

## FR-AUTH-006 — Verification Attempts

The system SHALL limit incorrect verification attempts.

After excessive failures:

```text
Invalidate code
Require new code
Potentially increase risk score
```

---

## FR-AUTH-007 — Google OAuth

The system SHALL support:

```text
Continue with Google
```

using OAuth 2.0 / OpenID Connect.

---

## FR-AUTH-008 — OAuth State Validation

OAuth flows MUST validate:

* State
* Nonce where applicable
* Redirect URI
* Issuer
* Authorization response
* Token signature/claims

---

## FR-AUTH-009 — OAuth Account Linking

Users MAY link Google authentication to an existing SalesGenie account after appropriate identity verification.

The system MUST prevent account takeover through unsafe automatic account linking.

---

## FR-AUTH-010 — Google Registration Password

If password fallback is part of the SalesGenie account policy, Google-created users SHALL be prompted to create a SalesGenie password after registration.

---

## FR-AUTH-011 — Login

The system SHALL support:

```text
Username/email
+
Password
```

---

## FR-AUTH-012 — Login Response

Successful login SHALL return or establish:

```text
Authenticated session
Access token where applicable
Refresh/session mechanism
User identity
Authorization context
```

---

## FR-AUTH-013 — Failed Login

Failed login SHALL return a generic authentication failure.

The system MUST NOT reveal:

```text
"Email exists but password is wrong"
```

versus:

```text
"Email does not exist"
```

---

## FR-AUTH-014 — MFA Challenge

When MFA is required, login SHALL transition to:

```text
Password verified
      ↓
MFA challenge
      ↓
MFA verified
      ↓
Session established
```

---

## FR-AUTH-015 — TOTP

The system SHOULD support TOTP enrollment.

Enrollment:

```text
Generate secret
 ↓
Display QR code
 ↓
User scans authenticator
 ↓
User enters verification code
 ↓
MFA activated
```

---

## FR-AUTH-016 — Recovery Codes

MFA enrollment SHALL generate recovery codes.

Recovery codes MUST:

* Be one-time use
* Be securely stored
* Be displayed only during enrollment/recovery
* Be regeneratable
* Be invalidated when regenerated

---

## FR-AUTH-017 — Passkey Enrollment

The system SHOULD support:

```text
Create Passkey
```

using WebAuthn.

---

## FR-AUTH-018 — Passkey Login

Users SHALL be able to authenticate using registered passkeys.

---

## FR-AUTH-019 — Password Change

Authenticated users SHALL be able to change passwords.

The system SHOULD require:

```text
Current password
New password
Confirm password
```

unless a verified recovery flow is being used.

---

## FR-AUTH-020 — Password Reset Request

Users SHALL be able to initiate password recovery with:

```text
Username
OR
Email
```

---

## FR-AUTH-021 — Password Reset Token

Password-reset links SHALL use:

* High-entropy random tokens
* Short expiration
* Single-use semantics
* Server-side validation

Tokens MUST NOT contain plaintext passwords.

---

## FR-AUTH-022 — Password Reset Code

Where code-based recovery is enabled, the code SHALL:

```text
Expire
Be single-use
Be rate limited
Be attempt limited
```

---

## FR-AUTH-023 — Reset Security Notification

A password-reset request SHALL trigger a security notification.

---

## FR-AUTH-024 — Password Reset Session Handling

After a successful password reset, the platform SHOULD revoke existing sessions depending on security policy.

For high-risk resets:

```text
Revoke all sessions
Require fresh login
```

---

## FR-AUTH-025 — Logout

Logout SHALL invalidate the appropriate session/refresh credentials.

---

## FR-AUTH-026 — Logout All

Users SHALL be able to invalidate all active sessions.

---

## FR-AUTH-027 — Session List

The system SHALL provide active-session information.

Example:

```text
Device
Browser
OS
Approximate location
Last active
Created
Current session
```

---

## FR-AUTH-028 — Session Revocation

Users SHALL be able to revoke individual sessions.

---

## FR-AUTH-029 — Admin Session Revocation

Authorized administrators SHALL be able to revoke sessions according to RBAC and security policy.

Every such action MUST be audited.

---

## FR-AUTH-030 — Session Expiration

Sessions MUST expire according to configurable security policy.

---

## FR-AUTH-031 — Idle Timeout

Privileged sessions SHOULD have configurable idle timeouts.

---

## FR-AUTH-032 — Absolute Session Lifetime

Sessions MUST have an absolute maximum lifetime regardless of activity.

---

## FR-AUTH-033 — Reauthentication

The system SHOULD require reauthentication for sensitive actions.

Examples:

```text
Change password
Disable MFA
Change email
Delete account
Change billing ownership
Create API credentials
Change security settings
Access highly sensitive data
```

---

## FR-AUTH-034 — Step-Up Authentication

Risky operations SHALL support step-up authentication.

---

## FR-AUTH-035 — Device Trust

The system MAY allow users to designate a device as trusted after successful MFA.

Trust MUST be revocable and time-limited.

---

## FR-AUTH-036 — New Device Detection

The platform SHALL detect new or materially changed devices.

---

## FR-AUTH-037 — New Location Detection

The system SHOULD detect materially unusual login locations.

Location analysis MUST account for:

* VPNs
* Mobile networks
* Corporate networks
* IP geolocation inaccuracies

---

## FR-AUTH-038 — Impossible Travel Detection

The system SHOULD detect impossible-travel patterns.

Example:

```text
Dhaka
10:00

New York
10:20
```

The system MUST treat this as a risk signal rather than automatic proof of compromise.

---

## FR-AUTH-039 — Security Email

Security emails SHOULD be sent for:

* New device
* Password change
* Password reset
* MFA changes
* Suspicious login
* Session revocation
* Account recovery

---

## FR-AUTH-040 — Security Notification Center

SalesGenie SHOULD maintain an in-app security notification center.

---

## 7. ROLE AND IDENTITY ARCHITECTURE

Authentication MUST remain separate from authorization.

```text
Authentication
     ↓
Who are you?

Authorization
     ↓
What can you do?
```

---

## SYS-RBAC-001 — Role Assignment

Roles MUST be stored as authorization relationships rather than hardcoded inside authentication logic.

---

## SYS-RBAC-002 — Multiple Roles

A user MAY have multiple roles where organizational policy permits.

Example:

```text
User
 ├── Organization Admin
 ├── Marketing Manager
 └── Business Analyst
```

---

## SYS-RBAC-003 — Scoped Roles

Roles MUST support scopes:

```text
Platform
Organization
Workplace
Team
Project
Resource
```

---

## SYS-RBAC-004 — Tenant Context

A session MUST carry or resolve the appropriate tenant context.

---

## SYS-RBAC-005 — Role Change

Role changes MUST take effect without requiring application redeployment.

High-impact role changes SHOULD invalidate or refresh authorization sessions.

---

## 8. ENTERPRISE AUTHENTICATION

## FR-ENTERPRISE-001 — SSO

Enterprise customers SHOULD support:

* SAML 2.0
* OpenID Connect
* OAuth 2.0

---

## FR-ENTERPRISE-002 — Enterprise Identity Providers

Potential providers:

```text
Microsoft Entra ID
Google Workspace
Okta
Auth0
Other SAML/OIDC providers
```

---

## FR-ENTERPRISE-003 — Domain-Based SSO

Organizations MAY configure verified domains.

Example:

```text
company.com
```

Users from the domain MAY be routed toward enterprise SSO.

---

## FR-ENTERPRISE-004 — SCIM

Enterprise plans SHOULD support SCIM provisioning.

Operations:

```text
Create user
Update user
Disable user
Delete/deprovision user
Group synchronization
```

---

## FR-ENTERPRISE-005 — Just-In-Time Provisioning

The platform MAY provision users upon successful enterprise SSO authentication.

---

## 9. SERVICE-TO-SERVICE AUTHENTICATION

SalesGenie is a microservices platform.

Therefore service-to-service authentication MUST NOT rely solely on user JWTs.

---

## SYS-SERVICE-AUTH-001

Services MUST authenticate themselves when communicating with other services.

Possible mechanisms:

```text
mTLS
Short-lived service tokens
Workload identity
Signed service credentials
```

---

## SYS-SERVICE-AUTH-002

Service credentials MUST:

* Be short-lived where possible
* Be rotated
* Be centrally managed
* Never be committed to source control

---

## SYS-SERVICE-AUTH-003

Every service request SHOULD include:

```text
service identity
request ID
trace ID
tenant context where applicable
```

---

## 10. API AUTHENTICATION

SalesGenie MUST support multiple API authentication models.

```text
User Session
OAuth Access Token
API Key
Service Credential
Webhook Signature
```

---

## FR-API-AUTH-001 — API Keys

Users/organizations MAY generate API keys where permitted.

API keys MUST support:

```text
Name
Created
Expiration
Scopes
Last used
Status
```

---

## FR-API-AUTH-002 — API Key Hashing

API secrets SHOULD be stored as hashes rather than plaintext where operationally possible.

---

## FR-API-AUTH-003 — API Key Rotation

Users SHALL be able to rotate/revoke API keys.

---

## FR-API-AUTH-004 — Scoped API Keys

API keys MUST support limited scopes.

Example:

```text
leads:read
leads:write
analytics:read
campaigns:execute
```

---

## 11. AI AGENT IDENTITY

AI agents MUST have distinct identities.

Example:

```text
AI Sales Agent
AI Marketing Agent
AI SEO Agent
AI Support Agent
AI Finance Agent
```

---

## SYS-AI-AUTH-001

Every AI agent MUST have:

```text
agent_id
tenant_id
owner
permissions
tool scopes
model policy
execution policy
expiration/version
```

---

## SYS-AI-AUTH-002

AI agents MUST NOT automatically inherit unrestricted human permissions.

---

## SYS-AI-AUTH-003

Agent permissions MUST follow least privilege.

---

## SYS-AI-AUTH-004

High-risk AI actions MUST require additional authorization.

Examples:

```text
Issue refund
Delete customer
Change subscription
Send high-volume campaign
Modify security policy
Change billing settings
```

---

## 12. AI + HUMAN AUTHENTICATION CONTROL

SalesGenie MUST support hybrid operational security.

```text
                    Action
                       |
                 Risk Evaluation
                       |
          +------------+------------+
          |                         |
        Low                       High
          |                         |
      AI allowed              Human approval
          |                         |
          +------------+------------+
                       |
                   Execution
```

---

## 13. ACCOUNT RECOVERY ARCHITECTURE

Recovery MUST be more restrictive than normal authentication.

Possible recovery signals:

```text
Verified email
MFA
Passkey
Recovery codes
Previously trusted device
Enterprise administrator
Human security review
```

No single weak signal SHOULD be sufficient for privileged account recovery.

---

## 14. PRIVILEGED IDENTITY PROTECTION

Privileged accounts MUST have additional controls.

Required for critical roles:

```text
MFA
Strong password
Session timeout
Step-up authentication
Security alerts
Audit logging
Device monitoring
```

---

## 15. BREAK-GLASS ACCESS

SalesGenie SHOULD support emergency administrative access.

Break-glass accounts MUST:

* Be extremely restricted
* Use strong authentication
* Be monitored
* Trigger alerts
* Be audited
* Be used only during emergencies

---

## 16. AUTHENTICATION EVENT MODEL

Example:

```json
{
  "event_type": "AUTH_LOGIN_SUCCESS",
  "event_id": "uuid",
  "user_id": "uuid",
  "tenant_id": "uuid",
  "session_id": "uuid",
  "device_id": "uuid",
  "ip_address": "redacted-or-protected",
  "risk_score": 12,
  "authentication_method": "password_mfa",
  "timestamp": "2026-08-22T00:00:00Z"
}
```

Sensitive fields MUST be protected according to security and privacy requirements.

---

## 17. AUTHENTICATION STATE MACHINE

```text
                 +----------------+
                 |     Signup     |
                 +-------+--------+
                         |
                         ↓
               +-------------------+
               | Pending Verify    |
               +---------+---------+
                         |
                 6-digit code
                         |
                         ↓
               +-------------------+
               | Email Verified    |
               +---------+---------+
                         |
                         ↓
               +-------------------+
               |      Active       |
               +---------+---------+
                         |
             +-----------+-----------+
             |                       |
          Login                    Risk Event
             |                       |
             ↓                       ↓
       Authentication          Step-up MFA
             |                       |
             +-----------+-----------+
                         |
                         ↓
                   Authenticated
                         |
              +----------+----------+
              |                     |
           Active                Logout
              |                     |
              |                     ↓
              |                Revoked
              |
              ↓
       Suspicious Activity
              |
              ↓
      Security Investigation
              |
       +------+------+
       |             |
     Clear         Block
       |             |
       ↓             ↓
    Active        Locked
```

---

## 18. REGISTRATION FLOW

```text
User
 |
 ↓
Registration Page
 |
 +---- Email
 |
 +---- Username
 |
 +---- Password
 |
 +---- Confirm Password
 |
 ↓
Validation
 |
 ↓
Create Pending Account
 |
 ↓
Generate 6-digit code
 |
 ↓
Send Email
 |
 ↓
User enters code
 |
 ↓
Validate code
 |
 +---- Invalid → Retry / Expire
 |
 ↓
Email Verified
 |
 ↓
Activate Account
 |
 ↓
Redirect to Login
```

---

## 19. GOOGLE AUTHENTICATION FLOW

```text
User
 |
 ↓
Continue with Google
 |
 ↓
Google Authorization
 |
 ↓
Authorization Code
 |
 ↓
Backend
 |
 ↓
Validate OAuth/OIDC response
 |
 ↓
Identify Google account
 |
 +---- Existing user → Login
 |
 +---- New user → Create account
                       |
                       ↓
                Set SalesGenie password
                       |
                       ↓
                Registration complete
                       |
                       ↓
                     Login
```

---

## 20. LOGIN FLOW

```text
User
 |
 ↓
Email / Username
 +
Password
 |
 ↓
Rate Limit Check
 |
 ↓
Credential Verification
 |
 ↓
Risk Evaluation
 |
 +----------+-----------+
 |          |           |
Low       Medium       High
 |          |           |
 ↓          ↓           ↓
Login     MFA        Block/Review
 |          |           |
 +----------+-----------+
            |
            ↓
       Session Created
            |
            ↓
     Authorization Load
            |
            ↓
      Dashboard Routing
```

---

## 21. PASSWORD RESET FLOW

```text
Forgot Password
       |
       ↓
Username / Email
       |
       ↓
Generic Response
       |
       ↓
Security Evaluation
       |
       ↓
Verification Email
       |
       +------ Code
       |
       +------ Secure Link
       |
       ↓
Verification
       |
       ↓
New Password
       |
       ↓
Confirm Password
       |
       ↓
Password Policy Validation
       |
       ↓
Password Updated
       |
       ↓
Session Revocation Policy
       |
       ↓
Security Notification
       |
       ↓
Login
```

---

## 22. LOGOUT FLOW

```text
Logout
  ↓
Current Session Identified
  ↓
Session Revoked
  ↓
Refresh Credential Revoked
  ↓
Client Credentials Cleared
  ↓
Audit Event
  ↓
Login Page
```

---

## 23. SESSION ARCHITECTURE

Each session SHOULD contain:

```text
session_id
user_id
tenant_id
device_id
created_at
last_activity_at
expires_at
ip metadata
location metadata
authentication method
risk state
status
```

---

## 24. SESSION STATES

```text
ACTIVE
IDLE
REAUTH_REQUIRED
SUSPICIOUS
REVOKED
EXPIRED
LOCKED
```

---

## 25. DEVICE FINGERPRINTING

Device identification SHOULD use privacy-conscious signals.

The system SHOULD avoid collecting unnecessary invasive fingerprinting data.

Possible signals:

```text
Browser family
OS family
Device characteristics
Session identifiers
Trusted-device credential
```

---

## 26. AUTHENTICATION CACHE

Authentication services MAY use Redis for:

* Verification attempts
* Rate limits
* Temporary OTP state
* Session metadata
* Risk counters
* Short-lived security challenges

Sensitive long-term identity data MUST remain in durable storage.

---

## 27. EMAIL SECURITY

Authentication emails MUST:

* Use verified sending infrastructure
* Avoid password disclosure
* Use signed links
* Use short-lived recovery tokens
* Avoid leaking account existence
* Support localization
* Include security guidance

---

## 28. EMAIL VERIFICATION SECURITY

Verification URLs MUST NOT expose sensitive account information.

Preferred:

```text
https://app.example.com/verify?token=<opaque-token>
```

rather than:

```text
?email=user@example.com&password=...
```

---

## 29. PASSWORD RESET SECURITY

Password-reset tokens MUST be:

```text
Random
High entropy
Single use
Short lived
Server validated
Revocable
```

---

## 30. AUTHENTICATION API DESIGN

Conceptual endpoints:

```text
POST /api/v1/auth/register
POST /api/v1/auth/verify-email
POST /api/v1/auth/resend-verification
POST /api/v1/auth/login
POST /api/v1/auth/logout
POST /api/v1/auth/logout-all

POST /api/v1/auth/password/change
POST /api/v1/auth/password/forgot
POST /api/v1/auth/password/verify
POST /api/v1/auth/password/reset

GET  /api/v1/auth/sessions
DELETE /api/v1/auth/sessions/{session_id}

POST /api/v1/auth/mfa/enroll
POST /api/v1/auth/mfa/verify
DELETE /api/v1/auth/mfa

POST /api/v1/auth/passkeys/register
POST /api/v1/auth/passkeys/authenticate

GET /api/v1/auth/oauth/google
GET /api/v1/auth/oauth/google/callback
```

Exact API paths MAY evolve according to `api_architecture.md`.

---

## 31. ERROR HANDLING

Authentication APIs MUST avoid sensitive information leakage.

Example:

```json
{
  "error": {
    "code": "AUTHENTICATION_FAILED",
    "message": "Invalid credentials."
  }
}
```

The response SHOULD NOT disclose whether the username/email exists.

---

## 32. AUTHENTICATION SECURITY HEADERS

Production authentication responses SHOULD use appropriate security headers, including where applicable:

```text
Strict-Transport-Security
Content-Security-Policy
X-Content-Type-Options
Referrer-Policy
Permissions-Policy
```

---

## 33. AUTHENTICATION RATE LIMITS

Separate limits SHOULD exist for:

```text
Registration
Login
Verification
Resend code
Password reset
MFA
OAuth initiation
API token creation
Session operations
```

---

## 34. ACCOUNT ENUMERATION PROTECTION

The following operations MUST avoid unnecessary account enumeration:

```text
Forgot password
Registration
Email verification resend
Username recovery
```

---

## 35. SECURITY NOTIFICATION MODEL

Security notifications MUST be generated as events.

```text
Authentication Event
       ↓
Security Event Processor
       ↓
Notification Policy
       ↓
Email / In-App / Other Channel
```

---

## 36. AUTHENTICATION OBSERVABILITY

Metrics MUST include:

```text
Login success rate
Login failure rate
Registration rate
Verification rate
Password reset rate
MFA success rate
MFA failure rate
OAuth success rate
Session count
Session revocations
Suspicious logins
Account locks
Token refresh failures
```

Metrics MUST be aggregated carefully to avoid exposing personal information.

---

## 37. SECURITY SLOs

Authentication MUST have strict availability and latency objectives.

Target examples:

```text
Login API p95             < 500 ms
Token validation          < 100 ms target
Session lookup            < 100 ms target
Verification API p95      < 300 ms
Password reset API p95    < 500 ms
```

External email delivery latency MUST NOT be confused with authentication API latency.

---

## 38. HIGH AVAILABILITY

Authentication MUST be treated as a Tier-0/Tier-1 critical service.

Recommended:

```text
Multiple instances
+
Multiple availability zones
+
Replicated database
+
Distributed cache
+
Redundant email provider
+
Monitoring
+
Disaster recovery
```

---

## 39. AUTHENTICATION FAILURE STRATEGY

If Redis becomes unavailable:

```text
Do not silently bypass security controls.
```

If email provider becomes unavailable:

```text
Do not automatically disable verification.
```

If Google OAuth becomes unavailable:

```text
Existing password-based users MAY continue logging in.
```

If identity database becomes unavailable:

```text
Fail securely.
```

---

## 40. SECURITY FAIL-CLOSED REQUIREMENTS

The authentication system MUST fail closed for:

* Invalid token
* Invalid signature
* Expired token
* Unknown session
* Unknown identity
* Invalid authorization state
* Untrusted issuer
* Invalid audience

---

## 41. AUTHENTICATION TESTING

Mandatory testing:

```text
Unit tests
Integration tests
API tests
OAuth tests
MFA tests
Session tests
Security tests
Load tests
Concurrency tests
Chaos tests
Penetration tests
Token replay tests
Brute-force tests
Credential stuffing simulations
```

---

## 42. SECURITY TEST CASES

The system MUST test:

```text
Expired verification code
Expired reset token
Reused reset token
Invalid MFA
Repeated MFA failures
Invalid JWT
Expired JWT
Wrong issuer
Wrong audience
Wrong signature
Algorithm confusion
Token replay
Session replay
OAuth CSRF
OAuth nonce failure
OAuth state failure
Account enumeration
Rate-limit bypass
Concurrent password reset
Concurrent login
Session revocation
```

---

## 43. AUTHENTICATION ACCEPTANCE CRITERIA

The authentication architecture SHALL be considered complete when:

```text
[ ] Email registration works
[ ] Username registration works where enabled
[ ] Password policy is enforced
[ ] 6-digit email verification works
[ ] Verification expires after 15 minutes
[ ] Verification attempts are limited
[ ] Resend verification is rate limited
[ ] Google OAuth works
[ ] Google identity is securely validated
[ ] Google users can establish a SalesGenie password
[ ] Login works
[ ] Invalid login is safely handled
[ ] Account enumeration is prevented
[ ] Password reset works
[ ] Reset code/link expires
[ ] Reset token is single use
[ ] Reset security notification works
[ ] Password change works
[ ] Logout works
[ ] Logout-all works
[ ] Session listing works
[ ] Session revocation works
[ ] MFA works
[ ] TOTP works
[ ] Recovery codes work
[ ] Passkey support is available or architecturally supported
[ ] Privileged roles require MFA
[ ] Risk-based authentication works
[ ] Suspicious login detection works
[ ] AI-assisted security analysis works
[ ] Human security escalation works
[ ] Authentication audit logs work
[ ] JWT validation is correct
[ ] Token expiration uses correct time units
[ ] Token rotation works
[ ] Token revocation works
[ ] Signing key rotation works
[ ] HTTPS is enforced
[ ] Secure cookies are used where applicable
[ ] CSRF protection works where applicable
[ ] CORS is restricted
[ ] Login rate limiting works
[ ] Service-to-service authentication works
[ ] API authentication works
[ ] API key scopes work
[ ] AI-agent identities are isolated
[ ] Tenant isolation works
[ ] Enterprise SSO architecture exists
[ ] SCIM architecture exists
[ ] Authentication service is highly available
[ ] Disaster recovery is tested
[ ] Load testing is completed
[ ] Security testing is completed
```

---

## 44. REFERENCE AUTHENTICATION ARCHITECTURE

```text
                           INTERNET
                              |
                              ↓
                       WAF / DDoS Layer
                              |
                              ↓
                       API Gateway
                              |
                    +---------+---------+
                    |                   |
              Authentication       Public APIs
                 Service                |
                    |                   |
        +-----------+-----------+       |
        |           |           |       |
     Password     Google       SSO      |
        |          OIDC        SAML     |
        |           |           |       |
        +-----------+-----------+-------+
                    |
              Identity Service
                    |
        +-----------+-----------+
        |           |           |
    Session      Token        Risk
    Service      Service      Engine
        |           |           |
        +-----------+-----------+
                    |
             Authorization
                    |
          +---------+---------+
          |                   |
       RBAC/ABAC          Tenant Context
          |                   |
          +---------+---------+
                    |
              Application APIs
                    |
       +------------+-------------+
       |            |             |
      Sales       Marketing     Support
       |            |             |
       +------------+-------------+
                    |
              Event / Audit Bus
                    |
       +------------+-------------+
       |                          |
 Security Analytics         Audit Storage
       |
 AI Security Engine
       |
 Human Security Team
```

---

## 45. COMPLETE AUTHENTICATION LIFECYCLE

```text
                    Registration
                         |
                         ↓
                 Email Verification
                         |
                         ↓
                   Identity Created
                         |
                         ↓
                   Authentication
                         |
                         ↓
                 Risk Evaluation
                         |
             +-----------+-----------+
             |                       |
          Low Risk                High Risk
             |                       |
             ↓                       ↓
       Session Created          Step-up MFA
             |                       |
             +-----------+-----------+
                         |
                         ↓
                    Authorization
                         |
                         ↓
                  Application Access
                         |
                         ↓
               Continuous Monitoring
                         |
             +-----------+-----------+
             |                       |
          Normal                 Suspicious
             |                       |
             ↓                       ↓
         Continue             Reauthentication
                                     |
                              +------+------+
                              |             |
                           Verified       Failed
                              |             |
                              ↓             ↓
                           Continue       Revoke
                                            |
                                            ↓
                                       Human Review
```

---

## 46. FINAL ARCHITECTURAL PRINCIPLES

SalesGenie authentication MUST follow these principles:

1. Authentication and authorization MUST remain separate.
2. Every identity MUST have a unique immutable identifier.
3. Passwords MUST never be stored in plaintext.
4. Modern password hashing MUST be used.
5. Email verification MUST be mandatory for password-based registration.
6. The verification code MUST be 6 digits and expire after 15 minutes.
7. Verification codes MUST be single-use and rate limited.
8. Google authentication MUST use secure OAuth/OIDC.
9. Google passwords MUST never be accessed or stored.
10. Password reset MUST require verified recovery.
11. Password-reset tokens MUST be short-lived and single-use.
12. Security notifications MUST be generated for sensitive authentication events.
13. Sessions MUST be revocable.
14. Privileged users MUST use MFA.
15. Phishing-resistant authentication SHOULD be supported through passkeys.
16. Access tokens MUST be short-lived.
17. Refresh/session credentials MUST be protected and revocable.
18. Token validation MUST verify signature, issuer, audience and expiration.
19. JWT time units MUST be handled correctly.
20. Signing keys MUST support secure rotation.
21. Authentication MUST use TLS.
22. Authentication endpoints MUST be rate limited.
23. Account enumeration MUST be minimized.
24. Tenant isolation MUST apply to identity and sessions.
25. Service-to-service authentication MUST use workload identities or equivalent secure credentials.
26. AI agents MUST have independent identities and limited permissions.
27. AI MUST assist security rather than become the sole authority for irreversible high-impact decisions.
28. Human security escalation MUST be available for high-risk cases.
29. Authentication events MUST be auditable.
30. Authentication MUST be highly available.
31. Authentication MUST fail securely.
32. Enterprise SSO and SCIM MUST be architecturally supported.
33. Authentication infrastructure MUST scale horizontally.
34. Security controls MUST scale with traffic.
35. Privacy MUST be respected when processing device and location information.

---

## 47. DEFINITION OF DONE

`authentication_architecture.md` is considered implemented when SalesGenie provides a production-grade identity platform capable of securely authenticating:

```text
Human Users
      +
Administrators
      +
Enterprise Users
      +
API Clients
      +
Service Accounts
      +
AI Agents
```

while maintaining:

```text
Identity Security
+
Tenant Isolation
+
Risk-Based Authentication
+
MFA
+
Session Security
+
Token Security
+
OAuth/OIDC
+
Enterprise SSO
+
Auditability
+
AI-Assisted Detection
+
Human Security Escalation
+
High Availability
+
Scalability
+
Privacy
```

The final authentication architecture MUST ensure that:

> **A valid login proves identity, but access is granted only after authorization, tenant validation, policy evaluation, and—when necessary—additional risk verification.**
