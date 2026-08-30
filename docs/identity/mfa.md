# SALES GENIE — MULTI-FACTOR AUTHENTICATION (MFA)

## FAANG-Level User Requirements, System Requirements & Functional Requirements

**Document:** `mfa.md`  
**Product:** SalesGenie  
**Version:** 1.0.0  
**Status:** Production Specification  
**Classification:** Security Critical  
**Architecture:** Enterprise Multi-Tenant SaaS + Microservices + Event-Driven + Zero-Trust + AI-Assisted Security + Human-in-the-Loop

---

## 1. DOCUMENT PURPOSE

This document defines the complete Multi-Factor Authentication (MFA) requirements for SalesGenie.

MFA is a foundational security subsystem responsible for protecting:

- User accounts
- Administrative accounts
- Organization accounts
- Workplace accounts
- Sales accounts
- Support accounts
- Developer accounts
- AI-agent management
- API credentials
- Billing operations
- Security operations
- Third-party integrations
- Privileged administrative actions

SalesGenie SHALL support both:

1. Automated/AI-assisted security analysis
2. Human security intervention

AI SHALL assist with risk analysis and recommendations, while deterministic security policies SHALL remain authoritative for critical authentication decisions.

---

## 2. MFA OBJECTIVES

SalesGenie MFA SHALL:

1. Provide strong protection against account takeover.
2. Support multiple authentication factors.
3. Support risk-based MFA.
4. Support mandatory MFA for privileged roles.
5. Support organization-level MFA policies.
6. Support workplace-level MFA policies.
7. Support user-level MFA enrollment.
8. Support MFA recovery.
9. Support secure device management.
10. Support trusted-device management.
11. Support step-up authentication.
12. Support emergency security controls.
13. Detect suspicious MFA behavior.
14. Prevent MFA bypass.
15. Protect against brute-force OTP attacks.
16. Protect against OTP replay.
17. Support auditability.
18. Support AI-assisted anomaly detection.
19. Support human security investigation.
20. Maintain tenant isolation.
21. Provide high availability.
22. Support enterprise-scale deployment.

---

## 3. MFA DESIGN PRINCIPLES

SalesGenie MFA SHALL follow:

- Zero Trust
- Defense in depth
- Least privilege
- Secure by default
- Phishing-resistant authentication where possible
- Risk-based authentication
- Strong cryptography
- Tenant isolation
- Explicit user consent
- Secure recovery
- Immutable auditing
- Human-in-the-loop security
- Privacy by design
- Fail-closed security decisions

---

## 4. AUTHENTICATION FACTORS

SalesGenie SHALL support the following factor categories.

## 4.1 Knowledge Factor

Something the user knows.

Examples:

- Password
- Passphrase
- Recovery information where appropriate

Password alone SHALL NOT qualify as MFA.

---

## 4.2 Possession Factor

Something the user possesses.

Examples:

- Authenticator application
- Hardware security key
- Passkey
- Verified mobile device
- Email verification code where policy permits

---

## 4.3 Inherence Factor

Something the user is.

Examples:

- Biometric authentication through supported platform authentication mechanisms

SalesGenie SHOULD avoid directly storing raw biometric data.

---

## 5. SUPPORTED MFA METHODS

SalesGenie SHOULD support:

```text
TOTP Authenticator
Passkeys / WebAuthn
Hardware Security Keys
Push Authentication
Email OTP
SMS OTP where permitted
Recovery Codes
Biometric Platform Authentication
```

Phishing-resistant methods SHALL receive the highest security classification.

---

## 6. MFA SECURITY RANKING

Recommended ranking:

| MFA Method                   | Security Level |
| ---------------------------- | -------------- |
| Passkey / WebAuthn           | Very High      |
| Hardware Security Key        | Very High      |
| Platform Biometric + Passkey | Very High      |
| TOTP                         | High           |
| Push Authentication          | High           |
| Email OTP                    | Medium         |
| SMS OTP                      | Medium/Lower   |

SMS and email SHALL NOT be the preferred factor for highly privileged accounts when stronger mechanisms are available.

---

## 7. USER ROLES

MFA SHALL apply to all relevant SalesGenie roles.

## 7.1 End User

Can:

* Enroll MFA
* Configure MFA
* Verify MFA
* Remove approved MFA factors
* Manage trusted devices
* Generate recovery codes
* Review MFA activity

---

## 7.2 Sales Agent

Requires MFA according to organization policy and risk level.

---

## 7.3 Support Agent

Requires MFA due to access to customer information.

---

## 7.4 Marketing Specialist

Requires MFA according to role and organizational security policy.

---

## 7.5 SEO Specialist

Requires MFA according to organization policy.

---

## 7.6 Team Manager

Requires stronger authentication for management functions.

---

## 7.7 Organization Admin

MFA SHALL be mandatory by default.

---

## 7.8 Organization Owner

MFA SHALL be mandatory.

---

## 7.9 Workplace Admin

MFA SHALL be mandatory.

---

## 7.10 Platform Admin

MFA SHALL be mandatory.

---

## 7.11 Security Admin

Phishing-resistant MFA SHOULD be mandatory.

---

## 7.12 Billing Admin

Strong MFA SHALL be mandatory.

---

## 7.13 Developer

MFA SHALL be required for:

* Developer dashboard
* API credential management
* Application management
* Production access

---

## 7.14 Super Admin

Super Admin accounts SHALL require the strongest available authentication controls.

Recommended:

```text
Passkey/WebAuthn
+
Hardware Security Key
+
Backup Security Key
+
Recovery Procedure
```

---

## 8. USER REQUIREMENTS

## UR-001 — MFA Enrollment

Users SHALL be able to enroll MFA after account registration.

---

## UR-002 — Mandatory MFA

Administrators SHALL be able to make MFA mandatory.

---

## UR-003 — MFA Setup

The system SHALL guide users through MFA setup.

Example:

```text
Account
   |
   v
Security Settings
   |
   v
Enable MFA
   |
   v
Choose Method
   |
   v
Register Factor
   |
   v
Verify Factor
   |
   v
Generate Recovery Codes
   |
   v
MFA Enabled
```

---

## UR-004 — TOTP Enrollment

Users SHALL be able to configure authenticator applications.

The system SHALL support standard TOTP implementations.

---

## UR-005 — QR Enrollment

For TOTP enrollment, SalesGenie SHOULD provide a QR code.

Users SHALL also have an option to enter a setup key manually.

---

## UR-006 — TOTP Verification

Users SHALL provide a valid current TOTP code.

The system SHALL prevent reuse of already accepted codes within the applicable validation window.

---

## UR-007 — Passkey Enrollment

Users SHALL be able to register passkeys using supported browsers and operating systems.

---

## UR-008 — Security Key Enrollment

Users SHALL be able to register hardware security keys.

Users SHOULD be able to register multiple security keys.

---

## UR-009 — Multiple Factors

Users SHOULD be able to register multiple MFA methods.

Example:

```text
Primary:
Passkey

Backup:
TOTP

Emergency:
Recovery Codes
```

---

## UR-010 — Recovery Codes

The system SHALL generate one-time recovery codes during MFA enrollment.

Recovery codes SHALL:

* Be randomly generated
* Be single-use
* Be securely stored
* Never be stored in plaintext
* Be replaceable
* Be revocable

---

## UR-011 — MFA Login

When MFA is required:

```text
Username / Email
        |
        v
Password
        |
        v
MFA Challenge
        |
        v
Successful Verification
        |
        v
Authenticated Session
```

---

## UR-012 — Trusted Device

Users MAY mark a device as trusted when permitted by policy.

Trusted-device functionality SHALL NOT bypass mandatory MFA for privileged operations unless explicitly configured.

---

## UR-013 — Trusted Device Expiration

Trusted-device authorization SHALL have an expiration period.

---

## UR-014 — MFA Challenge

The system SHALL clearly identify:

* Authentication method
* Challenge purpose
* Security warning
* Expiration
* Retry limitations

---

## UR-015 — MFA Failure

After excessive failures, the system SHALL apply security controls.

Possible actions:

```text
Temporary lock
Increasing delay
Additional verification
Security alert
Risk escalation
Human investigation
```

---

## UR-016 — MFA Notification

Users SHALL receive notifications for important MFA events.

Examples:

* MFA enabled
* MFA disabled
* New passkey
* New security key
* Recovery code generated
* MFA method removed
* Trusted device added
* Suspicious MFA attempt

---

## UR-017 — MFA Removal

Removing MFA SHALL require strong authentication.

For privileged accounts, removal SHOULD require additional verification or administrative approval.

---

## UR-018 — MFA Recovery

Users SHALL have a secure recovery mechanism when they lose access to their primary MFA factor.

---

## UR-019 — Security Escalation

High-risk MFA recovery requests SHALL be escalated to human security personnel.

---

## UR-020 — Risk-Based MFA

The system SHALL dynamically require MFA based on risk.

---

## UR-021 — Step-Up MFA

MFA SHALL be available for sensitive actions even when the user already has an active session.

---

## UR-022 — MFA Session Binding

Successful MFA SHALL be associated with the relevant authenticated session and authentication context.

---

## UR-023 — MFA Audit

All important MFA operations SHALL be auditable.

---

## 9. SYSTEM REQUIREMENTS

## SR-001 — Dedicated MFA Service

SalesGenie SHALL implement a dedicated MFA service.

Example:

```text
mfa_service
```

Responsibilities:

* Factor enrollment
* Factor verification
* Challenge generation
* Challenge validation
* Recovery-code management
* Passkey management
* Security-key management
* MFA policy enforcement
* MFA event generation
* Risk-based MFA
* Audit integration

---

## SR-002 — MFA Service Integration

MFA SHALL integrate with:

```text
auth_service
session_service
authorization_service
rbac_service
abac_policy_engine
security_service
notification_service
audit_service
user_service
device_service
risk_engine
```

---

## SR-003 — MFA Architecture

```text
                 Authentication
                       |
                       v
                  MFA Service
                       |
        +--------------+--------------+
        |              |              |
       TOTP         WebAuthn        Push
        |              |              |
        +--------------+--------------+
                       |
                       v
                  Risk Engine
                       |
              +--------+--------+
              |                 |
           Low Risk          High Risk
              |                 |
              v                 v
            Allow          Strong MFA
                                |
                                v
                         Security Decision
```

---

## SR-004 — Cryptographic Security

MFA secrets SHALL be protected using strong cryptographic mechanisms.

TOTP secrets SHOULD be encrypted at rest using managed encryption keys.

---

## SR-005 — Secret Storage

MFA secrets SHALL NOT be:

* Logged
* Exposed in API responses
* Stored in frontend source code
* Stored in plaintext database fields

---

## SR-006 — TOTP Secret Protection

TOTP secrets SHALL be encrypted or protected using appropriate key-management mechanisms.

---

## SR-007 — Recovery Code Storage

Recovery codes SHALL be stored using secure hashes.

The plaintext codes SHALL be shown only when generated.

---

## SR-008 — Challenge Expiration

MFA challenges SHALL expire.

Recommended baseline:

```text
OTP:
5 minutes or less

Push:
Short-lived challenge

WebAuthn:
Browser/platform controlled challenge lifetime
```

---

## SR-009 — OTP Length

SalesGenie SHALL support six-digit OTPs.

For security-sensitive flows, stronger challenge mechanisms SHOULD be preferred.

---

## SR-010 — OTP Attempt Limit

OTP challenges SHALL have a maximum attempt count.

Example:

```text
Maximum attempts:
5
```

Exact policy SHALL be configurable.

---

## SR-011 — OTP Replay Protection

An accepted OTP challenge SHALL NOT be reusable.

---

## SR-012 — Rate Limiting

MFA endpoints SHALL implement rate limits by:

* User
* IP
* Device
* Session
* Tenant
* Challenge

---

## SR-013 — Anti-Automation

The MFA service SHALL detect automated attacks.

Possible controls:

* Rate limiting
* Progressive delay
* Risk scoring
* CAPTCHA where appropriate
* Device analysis
* IP reputation

---

## SR-014 — MFA Policy Engine

The platform SHALL support configurable MFA policies.

Example:

```text
MFA Policy
|
+-- Required?
+-- Allowed Methods
+-- Minimum Assurance Level
+-- Trusted Device Duration
+-- Challenge Frequency
+-- Recovery Rules
+-- Risk Threshold
+-- Privileged Requirements
```

---

## SR-015 — Policy Hierarchy

MFA policies SHALL follow:

```text
Platform
   |
Organization
   |
Workplace
   |
Role
   |
User
```

A child policy SHALL NOT weaken mandatory platform security requirements.

---

## SR-016 — Authentication Assurance Level

SalesGenie SHOULD classify authentication strength.

Example:

```text
AAL1:
Password

AAL2:
Password + TOTP

AAL3-equivalent strong phishing-resistant:
Passkey / Security Key
```

Exact compliance terminology SHALL follow the applicable security standard adopted by the deployment.

---

## SR-017 — Privileged MFA

Privileged users SHALL have stronger requirements.

Example:

```text
Super Admin
Security Admin
Billing Admin
Platform Admin
Organization Owner
```

Recommended:

```text
Phishing-resistant MFA
+
Short session lifetime
+
Step-up authentication
+
Security monitoring
```

---

## SR-018 — Step-Up Authentication

The system SHALL support authentication context such as:

```text
mfa_verified_at
mfa_method
authentication_assurance
authentication_context
```

---

## SR-019 — Sensitive Action Timeout

MFA verification for sensitive actions SHALL have a short validity period.

Example:

```text
5–15 minutes
```

Policy SHALL determine the exact value.

---

## SR-020 — MFA Device Binding

Where supported, MFA credentials SHALL be bound to an appropriate user/device identity.

---

## SR-021 — WebAuthn

SalesGenie SHOULD implement WebAuthn/FIDO2 for phishing-resistant authentication.

The system SHALL validate:

* Challenge
* Origin
* RP ID
* Signature
* Credential ID
* User verification
* Attestation according to policy

---

## SR-022 — Passkey Security

Private keys SHALL remain on the user's device/platform.

SalesGenie SHALL NOT receive or store the private key.

---

## SR-023 — Hardware Security Keys

The system SHALL support security-key registration and revocation.

Users SHOULD be allowed multiple registered keys.

---

## SR-024 — Push Authentication

If push authentication is supported, challenges SHALL be:

* Unique
* Time-limited
* Bound to a transaction/context
* Protected against replay

---

## SR-025 — Number Matching

Push authentication SHOULD support number matching to reduce push-fatigue attacks.

---

## SR-026 — MFA Fatigue Protection

SalesGenie SHALL detect repeated MFA push requests.

Example:

```text
20 push requests
within 2 minutes
```

The system SHOULD automatically:

* Rate-limit requests
* Block additional pushes
* Increase risk
* Notify user
* Escalate if required

---

## SR-027 — MFA Reset Protection

MFA reset SHALL be treated as a high-risk security operation.

---

## SR-028 — Recovery Risk Engine

Recovery risk SHALL consider:

```text
Account history
Device
IP
Location
Previous MFA
Password reset status
Recent security events
Behavioral anomalies
```

---

## 10. FUNCTIONAL REQUIREMENTS

## FR-001 — Enable MFA

The system SHALL expose:

```http
POST /api/v1/mfa/enable
```

---

## FR-002 — List MFA Methods

```http
GET /api/v1/mfa/methods
```

Response SHOULD identify:

```text
Method
Status
Created At
Last Used
Device
```

Sensitive secrets SHALL never be returned.

---

## FR-003 — TOTP Setup

```http
POST /api/v1/mfa/totp/setup
```

The system SHALL return a temporary enrollment payload containing:

* QR provisioning data
* Manual setup key where permitted
* Enrollment ID

The secret SHALL not be persisted as active until verification succeeds.

---

## FR-004 — TOTP Verify

```http
POST /api/v1/mfa/totp/verify
```

The system SHALL:

1. Validate enrollment.
2. Validate TOTP.
3. Enforce expiration and attempt policy.
4. Activate the factor.
5. Generate recovery codes.
6. Record audit event.
7. Notify user.

---

## FR-005 — Disable TOTP

```http
DELETE /api/v1/mfa/totp
```

Requires strong authentication.

---

## FR-006 — WebAuthn Registration

```http
POST /api/v1/mfa/webauthn/register/options
POST /api/v1/mfa/webauthn/register/verify
```

---

## FR-007 — WebAuthn Authentication

```http
POST /api/v1/mfa/webauthn/auth/options
POST /api/v1/mfa/webauthn/auth/verify
```

---

## FR-008 — Security Key Registration

Users SHALL be able to register multiple hardware security keys.

Each credential SHALL have:

```text
credential_id
user_id
device_name
created_at
last_used_at
status
```

---

## FR-009 — Rename MFA Device

Users SHALL be able to assign a human-readable name.

Example:

```text
"YubiKey Office"
"MacBook Passkey"
"Android Authenticator"
```

---

## FR-010 — Revoke MFA Device

Users SHALL be able to revoke an individual MFA credential after successful authentication.

---

## FR-011 — Recovery Codes

```http
POST /api/v1/mfa/recovery-codes/regenerate
```

Generating new recovery codes SHALL invalidate previous unused recovery codes.

---

## FR-012 — Recovery Code Verification

```http
POST /api/v1/mfa/recovery-code/verify
```

Each recovery code SHALL be single-use.

---

## FR-013 — MFA Challenge Creation

```http
POST /api/v1/mfa/challenge
```

The system SHALL create a challenge based on authentication context.

---

## FR-014 — MFA Challenge Verification

```http
POST /api/v1/mfa/challenge/verify
```

---

## FR-015 — MFA Challenge State

A challenge SHALL have:

```text
CREATED
PENDING
VERIFIED
FAILED
EXPIRED
LOCKED
CANCELLED
```

---

## FR-016 — MFA Login Flow

```text
Login
 |
 v
Password Verification
 |
 v
Risk Evaluation
 |
 +------------------------+
 |                        |
Low Risk               High Risk
 |                        |
 v                        v
MFA Required?         Strong MFA
 |                        |
 +-----------+------------+
             |
             v
       MFA Challenge
             |
       +-----+-----+
       |           |
    Success      Failure
       |           |
       v           v
   Session      Risk Increase
    Created         |
                    v
                Security Event
```

---

## FR-017 — Risk-Based MFA

The system SHALL calculate risk before deciding whether additional MFA is required.

Signals MAY include:

```text
New device
New country
New IP
VPN/proxy
Impossible travel
Abnormal login time
Credential risk
Behavioral anomaly
Administrative role
Sensitive action
Recent password change
Recent MFA reset
```

---

## FR-018 — MFA Decision Engine

Example:

```json
{
  "risk_score": 87,
  "risk_level": "HIGH",
  "required_assurance": "PHISHING_RESISTANT",
  "action": "STEP_UP"
}
```

---

## FR-019 — Sensitive Operations

The following SHALL support mandatory step-up MFA:

```text
Password change
Email change
MFA removal
MFA reset
API key creation
API key deletion
Billing changes
Payment method changes
Subscription changes
Organization deletion
User deletion
Role escalation
Security policy changes
Data export
Credential management
Integration credential access
```

---

## FR-020 — MFA Before Privilege Escalation

A user SHALL complete required MFA before receiving privileged authorization.

---

## FR-021 — Admin MFA

Administrative login SHALL enforce MFA.

---

## FR-022 — Security Admin MFA

Security Admin SHALL require phishing-resistant MFA where supported.

---

## FR-023 — Billing MFA

Billing Admin SHALL require strong MFA.

---

## FR-024 — Organization MFA Policy

Organization administrators SHALL configure MFA requirements for their organization where authorized.

---

## FR-025 — Workplace MFA Policy

Workplace administrators SHALL configure workplace-level MFA requirements within inherited security boundaries.

---

## FR-026 — Role-Specific MFA

The system SHALL support different MFA requirements by role.

Example:

```text
End User:
Optional/Policy-Based

Sales Agent:
Policy-Based

Support Agent:
Mandatory

Organization Admin:
Mandatory

Security Admin:
Phishing-Resistant Mandatory
```

---

## FR-027 — Trusted Device

The system SHALL support trusted-device registration.

Trusted devices SHALL have:

```text
Device ID
User ID
Created At
Last Used
Expiration
Risk State
Status
```

---

## FR-028 — Trusted Device Revoke

Users SHALL be able to revoke trusted-device status.

---

## FR-029 — Trusted Device Security

Trusted-device state SHALL NOT be considered equivalent to a permanent MFA exemption.

---

## FR-030 — MFA Event Logging

Events SHALL include:

```text
MFA_ENABLED
MFA_DISABLED
MFA_CHALLENGE_CREATED
MFA_SUCCESS
MFA_FAILURE
MFA_LOCKED
MFA_EXPIRED
MFA_DEVICE_ADDED
MFA_DEVICE_REMOVED
MFA_RECOVERY_CODE_GENERATED
MFA_RECOVERY_CODE_USED
MFA_POLICY_CHANGED
MFA_STEP_UP_REQUIRED
MFA_STEP_UP_SUCCESS
MFA_STEP_UP_FAILURE
MFA_RESET_REQUESTED
MFA_RESET_COMPLETED
```

---

## 11. MFA DATA MODEL

## 11.1 MFA Factor

```text
MFAFactor
--------------------------------
id
user_id
tenant_id
organization_id
workplace_id
type
status
assurance_level
created_at
last_used_at
verified_at
revoked_at
device_id
metadata
```

---

## 11.2 TOTP Factor

```text
TOTPMFAFactor
--------------------------------
id
factor_id
encrypted_secret
algorithm
digits
period
created_at
last_used_at
```

---

## 11.3 WebAuthn Credential

```text
WebAuthnCredential
--------------------------------
id
user_id
credential_id
public_key
sign_count
aaguid
rp_id
device_name
user_verified
created_at
last_used_at
status
```

The private key SHALL remain outside SalesGenie.

---

## 11.4 Recovery Code

```text
RecoveryCode
--------------------------------
id
user_id
code_hash
created_at
used_at
status
```

---

## 11.5 MFA Challenge

```text
MFAChallenge
--------------------------------
id
user_id
session_id
factor_type
challenge_hash
created_at
expires_at
attempt_count
max_attempts
status
risk_score
purpose
```

---

## 12. MFA POLICY DATA MODEL

```text
MFAPolicy
--------------------------------
id
scope_type
scope_id
enabled
required
allowed_methods
minimum_assurance_level
trusted_device_enabled
trusted_device_duration
challenge_frequency
max_attempts
lockout_duration
risk_threshold
privileged_requirement
created_at
updated_at
```

---

## 13. MFA API ARCHITECTURE

```text
                    API Gateway
                         |
                         v
                  Authentication
                         |
                         v
                    MFA Service
                         |
      +------------------+------------------+
      |                  |                  |
      v                  v                  v
    TOTP              WebAuthn            Push
      |                  |                  |
      +------------------+------------------+
                         |
                         v
                    Risk Engine
                         |
            +------------+------------+
            |                         |
            v                         v
        Policy Engine            Security Engine
            |                         |
            +------------+------------+
                         |
                         v
                    Audit Service
```

---

## 14. EVENT-DRIVEN MFA ARCHITECTURE

SalesGenie SHALL publish:

```text
mfa.enabled
mfa.disabled
mfa.challenge.created
mfa.challenge.success
mfa.challenge.failed
mfa.factor.added
mfa.factor.removed
mfa.recovery.generated
mfa.recovery.used
mfa.reset.requested
mfa.reset.completed
mfa.risk.changed
mfa.locked
```

Architecture:

```text
MFA Service
    |
    v
Event Bus
    |
    +--> Security Service
    +--> Audit Service
    +--> Notification Service
    +--> Analytics Service
    +--> AI Risk Engine
    +--> Compliance Service
```

---

## 15. AI-ASSISTED MFA SECURITY

The AI security system MAY analyze:

* MFA failure patterns
* Login behavior
* Device behavior
* Location behavior
* Authentication timing
* Factor switching
* Recovery attempts
* Push notification patterns
* Account takeover indicators
* Abnormal administrative activity

---

## 16. AI MFA RISK EXAMPLE

```json
{
  "user_id": "user_123",
  "risk_score": 96,
  "risk_level": "CRITICAL",
  "signals": [
    "new_device",
    "new_country",
    "multiple_failed_totp",
    "recent_password_reset",
    "unusual_login_time"
  ],
  "recommended_action": "BLOCK_AND_ESCALATE",
  "confidence": 0.98
}
```

The final enforcement SHALL be determined by the security policy engine.

---

## 17. MFA ATTACK PROTECTION

SalesGenie SHALL protect against:

## 17.1 Brute Force

Controls:

* Attempt limits
* Rate limiting
* Progressive delays
* Account/device risk scoring

---

## 17.2 OTP Replay

Each accepted challenge SHALL become invalid.

---

## 17.3 OTP Enumeration

The system SHALL avoid revealing whether:

* Code is almost correct
* User exists
* Factor exists
* Challenge belongs to another account

---

## 17.4 MFA Fatigue

Repeated push requests SHALL trigger protective controls.

---

## 17.5 SIM Swap Risk

SMS-based MFA SHOULD receive increased risk weighting.

High-risk accounts SHOULD use phishing-resistant factors.

---

## 17.6 Phishing

SalesGenie SHOULD prioritize:

```text
Passkeys
WebAuthn
Security Keys
```

because they provide stronger phishing resistance than shared OTP codes.

---

## 18. MFA RECOVERY FLOW

```text
User Loses MFA
       |
       v
Recovery Request
       |
       v
Risk Evaluation
       |
       +-----------------------+
       |                       |
     LOW/MEDIUM              HIGH
       |                       |
       v                       v
Recovery Flow            Human Security Review
       |                       |
       v                       v
Identity Verification     Strong Verification
       |                       |
       +-----------+-----------+
                   |
                   v
             MFA Reset
                   |
                   v
             Force Re-login
                   |
                   v
             New MFA Setup
                   |
                   v
                Audit
```

---

## 19. MFA RESET SECURITY

MFA reset SHALL:

1. Require identity verification.
2. Perform risk assessment.
3. Invalidate suspicious active sessions where appropriate.
4. Invalidate recovery codes where appropriate.
5. Notify the user.
6. Generate security events.
7. Require new MFA enrollment.

---

## 20. HUMAN SECURITY INTERVENTION

Human security personnel SHALL be able to review:

```text
User
Account History
MFA Factors
Device History
Login History
Risk Score
Recovery Attempts
MFA Failures
Security Events
```

They MAY:

```text
Approve Recovery
Reject Recovery
Force MFA Reset
Freeze Account
Revoke Sessions
Require Strong MFA
Escalate Incident
```

All actions SHALL be audited.

---

## 21. MFA WITH SESSION MANAGEMENT

MFA SHALL integrate tightly with `session_management.md`.

```text
Authentication
      |
      v
MFA
      |
      v
Authentication Context
      |
      v
Session Creation
      |
      v
Session Risk Monitoring
```

When MFA is revoked:

```text
MFA Revoked
     |
     v
Risk Evaluation
     |
     v
Session Review
     |
     +--> Continue
     +--> Reauthenticate
     +--> Revoke
```

---

## 22. MFA WITH RBAC

RBAC SHALL determine whether MFA is mandatory.

Example:

```text
Role = Security Admin
        |
        v
MFA Required = TRUE
        |
        v
Phishing Resistant = REQUIRED
```

---

## 23. MFA WITH ABAC

ABAC SHALL evaluate contextual conditions.

Example:

```text
User:
Billing Admin

Action:
Change Payment Method

Device:
Unknown

Location:
New Country

Risk:
High

MFA:
Not recently verified

Decision:
DENY until strong MFA succeeds
```

---

## 24. MFA WITH BILLING SECURITY

Billing operations SHALL use step-up MFA.

Examples:

```text
Change subscription
Change payment method
Issue refund
Download sensitive invoices
Change billing owner
Modify payment gateway
```

Recommended flow:

```text
Billing Action
      |
      v
Risk Evaluation
      |
      v
Strong MFA
      |
      v
Authorization
      |
      v
Execute
      |
      v
Audit
```

---

## 25. MFA WITH AI AGENTS

AI agents SHALL NOT use human MFA credentials.

Instead:

```text
AI Agent
   |
   v
Machine Identity
   |
   v
Scoped Credential
   |
   v
Policy Evaluation
   |
   v
Tool Execution
```

Human approval MAY be required for high-impact operations.

---

## 26. MFA WITH SUPPORT

Support agents SHALL use MFA.

Customer account recovery SHALL NOT be performed solely based on information visible to a support agent.

High-risk recovery SHALL be escalated to security personnel.

---

## 27. NOTIFICATION REQUIREMENTS

Notifications SHALL be sent for:

```text
MFA Enabled
MFA Disabled
New Passkey
New Security Key
New Trusted Device
MFA Recovery
Recovery Code Generated
Recovery Code Used
MFA Failure Spike
Suspicious MFA Activity
MFA Reset
```

Notifications SHOULD include:

* Approximate location
* Device
* Timestamp
* Security action
* User guidance

Precise location SHOULD NOT be unnecessarily exposed.

---

## 28. MFA DASHBOARD

User dashboard:

```text
Security
|
+-- MFA Status
|
+-- Authentication Methods
|     +-- Passkey
|     +-- TOTP
|     +-- Security Key
|     +-- Push
|
+-- Trusted Devices
|
+-- Recovery Codes
|
+-- Recent MFA Activity
|
+-- Security Alerts
```

---

## 29. ADMIN MFA DASHBOARD

Security administrators SHALL see:

```text
MFA Adoption
MFA Coverage
MFA Failures
MFA Resets
High-Risk MFA Events
Recovery Requests
Unprotected Privileged Accounts
Weak Authentication Methods
```

---

## 30. MFA ANALYTICS

Metrics:

```text
mfa_adoption_rate
mfa_success_rate
mfa_failure_rate
mfa_reset_rate
mfa_recovery_rate
totp_usage
passkey_usage
security_key_usage
push_usage
sms_usage
high_risk_mfa_rate
mfa_fatigue_events
```

---

## 31. SECURITY SLOs

Recommended targets:

```text
MFA service availability: 99.99%+
MFA verification latency: <300 ms typical
Challenge creation latency: <200 ms typical
Critical security event propagation: <5 seconds target
```

---

## 32. OBSERVABILITY

The MFA service SHALL expose:

```text
Metrics
Logs
Traces
Security Events
Audit Events
Health Checks
```

Sensitive MFA secrets SHALL never appear in logs.

---

## 33. DATA RETENTION

MFA event retention SHALL follow:

* Security requirements
* Compliance requirements
* Organization policy
* Applicable privacy regulations

Sensitive data SHALL be retained only as long as necessary.

---

## 34. TESTING REQUIREMENTS

## Unit Tests

Test:

* TOTP generation
* TOTP verification
* Challenge expiration
* Retry limits
* Recovery code validation
* Factor activation
* Factor revocation
* Policy evaluation
* Risk evaluation

---

## Integration Tests

Test:

```text
Authentication + MFA
MFA + Session
MFA + RBAC
MFA + ABAC
MFA + Security
MFA + Notification
MFA + Audit
MFA + Redis
MFA + PostgreSQL
```

---

## Security Tests

Test:

```text
OTP brute force
OTP replay
OTP enumeration
MFA bypass
Session bypass
Recovery abuse
Token replay
Push fatigue
Device spoofing
Privilege escalation
Tenant isolation
WebAuthn origin validation
Challenge tampering
```

---

## 35. PERFORMANCE REQUIREMENTS

Target baseline:

```text
TOTP verification: <100 ms typical
MFA challenge creation: <200 ms
WebAuthn verification: <300 ms typical
Recovery-code validation: <100 ms typical
```

Targets SHALL be validated through load testing.

---

## 36. HIGH AVAILABILITY

MFA SHALL NOT depend on a single service instance.

Recommended:

```text
                 Load Balancer
                       |
             +---------+---------+
             |         |         |
          MFA-1      MFA-2      MFA-3
             |         |         |
             +---------+---------+
                       |
                 Distributed Cache
                       |
                    Database
```

---

## 37. DISASTER RECOVERY

The MFA architecture SHALL support:

* Encrypted backups
* Key recovery
* Factor metadata recovery
* Database recovery
* Regional failover
* Emergency administrative access
* Recovery procedures
* Regular recovery testing

---

## 38. BREAK-GLASS MFA

Emergency administrative access SHALL support controlled break-glass procedures.

```text
Emergency
    |
    v
Break-Glass Request
    |
    v
Strong Verification
    |
    v
Explicit Reason
    |
    v
Temporary Access
    |
    v
Security Notification
    |
    v
Complete Audit
```

Break-glass credentials SHALL be tightly controlled.

---

## 39. COMPLIANCE

The MFA architecture SHOULD support controls relevant to:

* SOC 2
* ISO 27001
* GDPR
* CCPA/CPRA where applicable
* PCI DSS for applicable billing environments
* Enterprise security requirements

Compliance implementation SHALL be based on the actual deployment scope and applicable jurisdiction.

---

## 40. ACCEPTANCE CRITERIA

The MFA system SHALL be considered production-ready when:

* Users can enroll MFA.
* TOTP works correctly.
* Passkeys work correctly.
* Security keys work correctly.
* Recovery codes work correctly.
* MFA challenges expire correctly.
* OTP replay is prevented.
* Brute-force protection works.
* MFA fatigue protection works where push is supported.
* MFA removal requires strong authentication.
* MFA recovery is risk-aware.
* Privileged users require strong MFA.
* Step-up MFA works.
* Organization policies work.
* Workplace policies work.
* RBAC integration works.
* ABAC integration works.
* Session integration works.
* AI risk analysis works.
* Human security escalation works.
* All sensitive events are audited.
* Secrets never appear in logs.
* Tenant isolation is verified.
* MFA service survives instance failure.
* Load testing meets SLOs.
* Disaster recovery has been tested.

---

## 41. END-TO-END MFA FLOW

```text
                     USER
                       |
                       v
                Authentication
                       |
                       v
                  Risk Engine
                       |
          +------------+------------+
          |                         |
       Low Risk                  High Risk
          |                         |
          |                    Strong MFA
          |                         |
          +------------+------------+
                       |
                       v
                  MFA Policy
                       |
                       v
                MFA Challenge
                       |
       +---------------+---------------+
       |               |               |
      TOTP          Passkey          Key
       |               |               |
       +---------------+---------------+
                       |
                       v
                  Verification
                       |
              +--------+--------+
              |                 |
            PASS              FAIL
              |                 |
              v                 v
       Authentication       Risk Increase
          Context               |
              |                 v
              v              Security
           Session            Event
           Creation
              |
              v
          Dashboard
```

---

## 42. MASTER MFA SECURITY MODEL

```text
                         SALES GENIE
                              |
                        MFA SECURITY
                              |
       +----------------------+----------------------+
       |                      |                      |
 Authentication          Authorization          Session
       |                      |                      |
       +----------------------+----------------------+
                              |
                         MFA Service
                              |
       +----------+-----------+-----------+-----------+
       |          |           |           |           |
      TOTP     Passkey     Security     Push      Recovery
                            Key
       |          |           |           |           |
       +----------+-----------+-----------+-----------+
                              |
                         Risk Engine
                              |
                    +---------+---------+
                    |                   |
                AI Security       Human Security
                    |                   |
                    +---------+---------+
                              |
                       Policy Engine
                              |
                    +---------+---------+
                    |                   |
                  ALLOW              BLOCK
                    |
                    v
                  Session
                    |
                    v
                  Audit
```

---

## 43. FINAL ARCHITECTURAL REQUIREMENT

SalesGenie's MFA subsystem SHALL NOT be implemented as a simple OTP screen.

It SHALL operate as a complete authentication-security control plane integrating:

```text
Password Authentication
+
Passkeys
+
WebAuthn
+
TOTP
+
Security Keys
+
Recovery Codes
+
Risk-Based Authentication
+
Step-Up Authentication
+
Device Intelligence
+
Session Management
+
RBAC
+
ABAC
+
AI Security
+
Human Security
+
Audit Logging
+
Notifications
+
Event-Driven Architecture
+
Multi-Tenant Policy Management
+
High Availability
+
Observability
```

The final system SHALL prioritize phishing-resistant authentication for privileged users, maintain secure recovery mechanisms, prevent MFA bypass and replay, detect suspicious authentication behavior, provide human security escalation, and maintain complete auditability across the SalesGenie platform.

---

## 44. MASTER REQUIREMENT SUMMARY

```text
                      MFA REQUEST
                           |
                           v
                    Risk Evaluation
                           |
              +------------+------------+
              |                         |
           LOW RISK                  HIGH RISK
              |                         |
              v                         v
       Policy Evaluation          Strong MFA Required
              |                         |
              +------------+------------+
                           |
                           v
                     MFA Challenge
                           |
             +-------------+-------------+
             |             |             |
           Passkey        TOTP       Security Key
             |             |             |
             +-------------+-------------+
                           |
                           v
                      Verification
                           |
                  +--------+--------+
                  |                 |
                SUCCESS            FAIL
                  |                 |
                  v                 v
             Auth Context       Risk Increase
                  |                 |
                  v                 v
               Session          Security Event
                  |                 |
                  v                 v
             Authorization     Human Review
                  |
                  v
                Access
                  |
                  v
                Audit
```

**MFA is a foundational security subsystem of SalesGenie and SHALL be tightly integrated with Authentication, Session Management, RBAC, ABAC, Security, Billing, Support, AI Agents, Administration, API Gateway, Audit, Notification, Risk Management, and Event-Driven infrastructure.**
