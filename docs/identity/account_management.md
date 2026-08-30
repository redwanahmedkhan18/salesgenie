# SALES GENIE — ACCOUNT MANAGEMENT

## FAANG-Level User Requirements, System Requirements & Functional Requirements

**Document:** `account_management.md`  
**Product:** SalesGenie  
**Version:** 1.0.0  
**Status:** Production Specification  
**Classification:** Security-Critical / Enterprise  
**Architecture:** Multi-Tenant SaaS + Microservices + Event-Driven + Zero-Trust + AI-Assisted + Human-in-the-Loop

---

## 1. DOCUMENT PURPOSE

This document defines the complete Account Management requirements for SalesGenie.

The Account Management subsystem SHALL provide secure lifecycle management for every human account and authorized machine identity within the platform.

It SHALL manage:

- Account creation
- Account activation
- Account verification
- Account profile
- Account status
- Account lifecycle
- Account recovery
- Account security
- Account ownership
- Account preferences
- Account deletion
- Account suspension
- Account restoration
- Account transfer
- Account archival
- Account privacy
- Account sessions
- Account devices
- Account authentication factors
- Account roles
- Account organization membership
- Account workplace membership
- Account audit history
- Account notifications
- Account data export
- Account compliance controls
- AI-assisted account security
- Human security intervention

Account Management SHALL integrate with:

```text
Authentication
MFA
Authorization
RBAC
ABAC
Session Management
Organization Management
Workplace Management
Billing
Security
Audit
Notification
Support
AI Risk Engine
API Gateway
Event Bus
Data Platform
```

---

## 2. ACCOUNT MANAGEMENT OBJECTIVES

SalesGenie SHALL provide:

1. Secure account lifecycle management.
2. Strong identity integrity.
3. Multi-tenant account isolation.
4. Role-aware account management.
5. Organization-aware account management.
6. Workplace-aware account management.
7. Secure account recovery.
8. Secure account deletion.
9. Account suspension and restoration.
10. Account ownership management.
11. Account profile management.
12. Account security management.
13. Device management.
14. Session management.
15. MFA management integration.
16. Privacy controls.
17. Data export.
18. Auditability.
19. AI-based anomaly detection.
20. Human security escalation.
21. Enterprise administration.
22. High availability.
23. Horizontal scalability.
24. Strong data protection.

---

## 3. DESIGN PRINCIPLES

Account Management SHALL follow:

* Zero Trust
* Least privilege
* Secure by default
* Defense in depth
* Privacy by design
* Tenant isolation
* Data minimization
* Explicit authorization
* Strong authentication
* Immutable auditing
* Human-in-the-loop for high-risk operations
* Fail-closed security decisions
* Separation of duties
* Event-driven architecture

---

## 4. ACCOUNT TYPES

SalesGenie SHALL support multiple account classes.

## 4.1 End User

Customer/user who consumes SalesGenie services.

---

## 4.2 Sales Agent

Human sales employee.

---

## 4.3 Support Agent

Human support employee.

---

## 4.4 Marketing Specialist

Marketing operations user.

---

## 4.5 SEO Specialist

SEO operations user.

---

## 4.6 Team Manager

Manages teams and team members.

---

## 4.7 Sales Manager

Manages sales teams and pipelines.

---

## 4.8 Marketing Manager

Manages marketing operations.

---

## 4.9 SEO Manager

Manages SEO operations.

---

## 4.10 Product Manager

Manages product-related operations.

---

## 4.11 Finance Manager

Manages financial analytics and authorized financial operations.

---

## 4.12 Business Analyst

Analyzes business performance.

---

## 4.13 Support Manager

Manages support operations.

---

## 4.14 AI Agent

Non-human machine identity operating under scoped authorization.

---

## 4.15 Developer

Developer account with application/API capabilities.

---

## 4.16 Organization Admin

Manages organization-level resources.

---

## 4.17 Organization Owner

Owns the organization and high-level organizational permissions.

---

## 4.18 Workplace Admin

Manages workplace-level resources.

---

## 4.19 Platform Admin

Manages platform-level operations.

---

## 4.20 Security Admin

Manages security operations.

---

## 4.21 Billing Admin

Manages billing operations.

---

## 4.22 Super Admin

Highest platform-level administrative account.

---

## 5. ACCOUNT LIFECYCLE

The account lifecycle SHALL support:

```text
INVITED
   |
   v
REGISTERED
   |
   v
EMAIL_VERIFICATION_REQUIRED
   |
   v
VERIFIED
   |
   v
ACTIVE
   |
   +----------+
   |          |
   v          v
SUSPENDED   LOCKED
   |          |
   +-----+----+
         |
         v
      RESTORED
         |
         v
       ACTIVE
         |
         v
DELETION_REQUESTED
         |
         v
DELETION_GRACE_PERIOD
         |
         v
DELETED
         |
         v
ARCHIVED
```

---

## 6. ACCOUNT STATUS MODEL

Supported statuses:

```text
PENDING
INVITED
UNVERIFIED
ACTIVE
INACTIVE
SUSPENDED
LOCKED
SECURITY_HOLD
DELETION_REQUESTED
DELETING
DELETED
ARCHIVED
```

---

## 7. USER REQUIREMENTS

## UR-001 — Account Registration

Users SHALL be able to create a SalesGenie account through supported registration methods.

Supported methods:

```text
Email + Password
Google OAuth
Enterprise SSO where enabled
Invitation
```

---

## UR-002 — Email Verification

New accounts SHALL require email verification according to the authentication policy.

The verification mechanism SHALL integrate with `user_signup_and_authentication.md`.

---

## UR-003 — Account Profile

Users SHALL be able to manage permitted profile information.

Example:

```text
First Name
Last Name
Display Name
Profile Picture
Phone Number
Job Title
Designation
Time Zone
Language
Country
```

Sensitive fields SHALL require additional authorization.

---

## UR-004 — Username

The system SHALL support a unique username where configured.

Username changes SHALL be subject to security policy.

---

## UR-005 — Email Address

Users SHALL be able to request an email-address change.

Changing an email SHALL require strong verification.

---

## UR-006 — Email Change Verification

When an email is changed:

```text
Current Identity Verification
        |
        v
New Email Verification
        |
        v
Security Notification
        |
        v
Email Updated
```

---

## UR-007 — Password Management

Users SHALL be able to change their password.

Password changes SHALL require:

* Current authentication
* New password
* Confirm password
* Password policy validation

---

## UR-008 — Password Reset

Users SHALL be able to initiate password recovery through the authentication subsystem.

---

## UR-009 — MFA Integration

Users SHALL be able to manage MFA from Account Security.

MFA implementation SHALL follow `mfa.md`.

---

## UR-010 — Device Management

Users SHALL be able to view and manage recognized devices.

---

## UR-011 — Session Management

Users SHALL be able to view active sessions and revoke sessions.

---

## UR-012 — Account Security

Users SHALL have access to:

```text
Security Status
MFA
Devices
Sessions
Recent Login Activity
Security Alerts
Recovery Options
```

---

## UR-013 — Account Notifications

Users SHALL receive security notifications for important account changes.

---

## UR-014 — Account Suspension

Authorized administrators SHALL be able to suspend accounts according to RBAC/ABAC policy.

---

## UR-015 — Account Restoration

Authorized administrators SHALL be able to restore suspended accounts.

Restoration SHALL require appropriate authorization.

---

## UR-016 — Account Locking

The system SHALL automatically lock or restrict accounts when security policies require it.

---

## UR-017 — Security Hold

Security administrators SHALL be able to place accounts under security hold.

---

## UR-018 — Account Deletion

Users SHALL be able to request account deletion.

---

## UR-019 — Account Deletion Grace Period

SalesGenie SHOULD support a configurable deletion grace period.

Example:

```text
Deletion Requested
       |
       v
30-Day Grace Period
       |
       +--> Cancel Deletion
       |
       v
Permanent Deletion
```

The actual period SHALL be configurable according to product and compliance requirements.

---

## UR-020 — Data Export

Users SHALL be able to request an export of their account data where applicable.

---

## UR-021 — Organization Membership

Users SHALL be able to view their organization memberships where permitted.

---

## UR-022 — Workplace Membership

Users SHALL be able to view their workplace memberships where permitted.

---

## UR-023 — Role Visibility

Users SHALL be able to see their active designation/role.

---

## UR-024 — Role Changes

Role changes SHALL only occur through authorized administrative workflows.

Users SHALL NOT directly elevate their own privileges.

---

## UR-025 — Invitation

Authorized administrators SHALL be able to invite users.

---

## UR-026 — Invitation Acceptance

Invited users SHALL be able to accept invitations through secure invitation flows.

---

## UR-027 — Invitation Expiration

Invitations SHALL expire.

---

## UR-028 — Account Ownership

The system SHALL identify account ownership and organizational ownership relationships.

---

## UR-029 — Account Transfer

Authorized administrators SHALL be able to transfer ownership where business rules permit.

High-risk transfers SHALL require additional verification.

---

## UR-030 — Account Activity

Users SHALL be able to view appropriate account activity.

---

## UR-031 — Privacy Controls

Users SHALL be able to manage available privacy preferences.

---

## UR-032 — Communication Preferences

Users SHALL be able to configure:

```text
Product Notifications
Security Notifications
Marketing Emails
Usage Alerts
Billing Notifications
Support Notifications
```

Security notifications SHALL not be disabled when required by policy.

---

## UR-033 — Language

Users SHALL be able to select supported languages.

---

## UR-034 — Time Zone

Users SHALL be able to configure their preferred time zone.

---

## UR-035 — Profile Picture

Users MAY upload a profile picture subject to:

* File type validation
* Size limits
* Malware scanning
* Content validation

---

## UR-036 — Account Search

Authorized administrators SHALL be able to search accounts.

Search MAY include:

```text
User ID
Email
Username
Name
Role
Organization
Workplace
Status
Creation Date
Last Login
```

---

## UR-037 — Account Filtering

Administrators SHALL be able to filter accounts.

---

## UR-038 — Account Details

Authorized administrators SHALL be able to view account details appropriate to their permissions.

---

## UR-039 — Account Actions

Authorized administrators SHALL be able to perform permitted account actions.

---

## UR-040 — Account Audit

All sensitive account operations SHALL be auditable.

---

## 8. SYSTEM REQUIREMENTS

## SR-001 — Dedicated Account Service

SalesGenie SHALL implement a dedicated account management service.

Recommended:

```text
account_service
```

Responsibilities:

```text
Profile Management
Account Lifecycle
Account Status
Account Preferences
Membership
Invitation
Ownership
Deletion
Suspension
Account Security Integration
Audit Events
```

---

## SR-002 — Service Dependencies

The Account Service SHALL integrate with:

```text
auth_service
mfa_service
session_service
authorization_service
rbac_service
abac_policy_engine
organization_service
workplace_service
billing_service
security_service
notification_service
audit_service
storage_service
risk_engine
```

---

## SR-003 — API Gateway

All external account-management APIs SHALL pass through the API Gateway.

---

## SR-004 — Authentication

Account APIs SHALL require authenticated access unless explicitly designated as public authentication endpoints.

---

## SR-005 — Authorization

Every account-management operation SHALL be evaluated through authorization policies.

---

## SR-006 — Tenant Isolation

Account data SHALL be isolated by:

```text
Platform
Organization
Workplace
User
```

No tenant SHALL access another tenant's account data without explicit authorized platform-level permission.

---

## SR-007 — Data Encryption

Sensitive account data SHALL be encrypted:

```text
In Transit
At Rest
In Backups
```

---

## SR-008 — Database Security

Recommended primary datastore:

```text
PostgreSQL
```

The database SHALL support:

* Encryption
* Foreign keys
* Constraints
* Transaction integrity
* Indexing
* Auditing integration

---

## SR-009 — Cache

Redis MAY be used for:

```text
Account session metadata
Rate limiting
Temporary verification states
Invitation state
Distributed locks
```

Sensitive long-term account information SHALL not rely exclusively on cache storage.

---

## SR-010 — Event Bus

Account lifecycle events SHALL be published through the event bus.

---

## SR-011 — Event Types

Recommended events:

```text
account.created
account.verified
account.activated
account.updated
account.suspended
account.locked
account.restored
account.security_hold
account.deletion_requested
account.deleted
account.archived
account.email_changed
account.password_changed
account.mfa_changed
account.device_added
account.device_removed
account.session_revoked
account.role_changed
account.organization_joined
account.organization_left
account.invited
account.invitation_accepted
```

---

## SR-012 — Idempotency

Critical account operations SHALL support idempotency.

Examples:

```text
Invitation creation
Deletion request
Account restoration
Email change
Ownership transfer
```

---

## SR-013 — Concurrency Control

The system SHALL prevent conflicting account operations.

Example:

```text
Admin A:
Suspends User

Admin B:
Deletes User

```

The system SHALL maintain consistent lifecycle state.

---

## SR-014 — Optimistic Locking

Account records SHOULD use versioning for concurrent updates.

---

## SR-015 — Audit Trail

Sensitive account changes SHALL generate immutable audit records.

---

## SR-016 — Soft Deletion

The system SHOULD support soft deletion before permanent deletion.

---

## SR-017 — Data Retention

Account records SHALL follow configurable retention policies.

---

## SR-018 — Account Recovery

Recovery SHALL integrate with:

```text
Authentication
MFA
Security Risk Engine
Human Security
```

---

## SR-019 — Account Risk Score

Accounts MAY have a dynamic security risk score.

Example:

```json
{
  "risk_score": 82,
  "risk_level": "HIGH"
}
```

Risk scores SHALL not be treated as sole authorization decisions for critical actions unless explicitly defined by deterministic policy.

---

## SR-020 — Device Intelligence

The system SHOULD maintain device metadata such as:

```text
Device ID
Device Type
OS
Browser
First Seen
Last Seen
Approximate Location
Risk State
```

Raw fingerprinting SHALL follow privacy requirements.

---

## SR-021 — Account State Machine

Account transitions SHALL be validated by a deterministic state machine.

Invalid transitions SHALL be rejected.

---

## SR-022 — Role Separation

Account management SHALL remain separate from authorization.

Account Service SHALL not independently grant privileges.

---

## SR-023 — Service-to-Service Authentication

Internal services SHALL use secure machine authentication.

Recommended:

```text
mTLS
Service Identity
Short-Lived Tokens
Scoped Credentials
```

---

## SR-024 — Administrative Access

Administrative account-management operations SHALL require:

```text
Authentication
MFA
Authorization
Policy Evaluation
Audit
```

---

## SR-025 — Privileged Account Protection

Privileged accounts SHALL have stricter account-management controls.

---

## SR-026 — API Rate Limiting

Account APIs SHALL implement rate limiting.

---

## SR-027 — Abuse Prevention

The system SHALL protect against:

```text
Account Enumeration
Invitation Abuse
Password Reset Abuse
Email Change Abuse
Account Creation Abuse
Deletion Abuse
Privilege Escalation
Tenant Enumeration
```

---

## SR-028 — Privacy

Account APIs SHALL expose only the minimum required personal information.

---

## SR-029 — PII Protection

PII SHALL be protected in:

```text
Database
Logs
Events
Analytics
Exports
Backups
```

---

## SR-030 — Logging

Application logs SHALL never contain:

```text
Passwords
MFA Secrets
Recovery Codes
Session Tokens
OAuth Client Secrets
API Keys
Payment Secrets
```

---

## SR-031 — Observability

The service SHALL expose:

```text
Metrics
Logs
Traces
Health
Security Events
Audit Events
```

---

## 9. FUNCTIONAL REQUIREMENTS

## FR-001 — Create Account

```http
POST /api/v1/accounts
```

The service SHALL:

1. Validate request.
2. Verify authorization.
3. Validate uniqueness.
4. Create account.
5. Emit `account.created`.
6. Create audit record.

---

## FR-002 — Get Current Account

```http
GET /api/v1/accounts/me
```

---

## FR-003 — Update Current Account

```http
PATCH /api/v1/accounts/me
```

Only permitted fields SHALL be editable.

---

## FR-004 — Get Account

```http
GET /api/v1/accounts/{account_id}
```

Authorization SHALL be evaluated before returning data.

---

## FR-005 — Update Account

```http
PATCH /api/v1/accounts/{account_id}
```

---

## FR-006 — Suspend Account

```http
POST /api/v1/accounts/{account_id}/suspend
```

The system SHALL:

* Verify authorization
* Validate state
* Record reason
* Update status
* Revoke sessions where policy requires
* Emit event
* Notify appropriate parties
* Audit action

---

## FR-007 — Restore Account

```http
POST /api/v1/accounts/{account_id}/restore
```

---

## FR-008 — Lock Account

```http
POST /api/v1/accounts/{account_id}/lock
```

---

## FR-009 — Unlock Account

```http
POST /api/v1/accounts/{account_id}/unlock
```

---

## FR-010 — Security Hold

```http
POST /api/v1/accounts/{account_id}/security-hold
```

---

## FR-011 — Request Deletion

```http
POST /api/v1/accounts/me/deletion-request
```

---

## FR-012 — Cancel Deletion

```http
POST /api/v1/accounts/me/deletion-request/cancel
```

---

## FR-013 — Administrative Deletion

```http
DELETE /api/v1/accounts/{account_id}
```

This SHALL require elevated permissions and policy validation.

---

## FR-014 — Permanent Deletion

Permanent deletion SHALL be separated from ordinary user-facing deletion requests.

---

## FR-015 — Account Search

```http
GET /api/v1/accounts
```

Supported parameters:

```text
query
email
username
role
status
organization_id
workplace_id
created_from
created_to
last_login_from
last_login_to
page
limit
sort
```

---

## FR-016 — Pagination

Account lists SHALL use cursor-based pagination at large scale.

Offset pagination MAY be supported for small datasets.

---

## FR-017 — Account Filtering

The system SHALL support compound filters.

Example:

```text
organization = ACME
AND
role = Sales Agent
AND
status = ACTIVE
```

---

## FR-018 — Account Sorting

Authorized administrators SHALL be able to sort by:

```text
Created Date
Last Login
Name
Status
Risk
```

---

## FR-019 — Profile Update

```http
PATCH /api/v1/accounts/me/profile
```

---

## FR-020 — Preferences Update

```http
PATCH /api/v1/accounts/me/preferences
```

---

## FR-021 — Notification Preferences

```http
PATCH /api/v1/accounts/me/notifications
```

---

## FR-022 — Change Email

```http
POST /api/v1/accounts/me/email/change
```

Flow:

```text
Current Authentication
        |
        v
Risk Evaluation
        |
        v
New Email
        |
        v
Verification
        |
        v
Security Notification
        |
        v
Email Changed
```

---

## FR-023 — Change Password

```http
POST /api/v1/accounts/me/password/change
```

---

## FR-024 — Password Reset

Handled by authentication service.

Account Service SHALL consume the corresponding security event.

---

## FR-025 — MFA Management

MFA operations SHALL delegate to `mfa_service`.

---

## FR-026 — Session Management

Session operations SHALL delegate to `session_service`.

---

## FR-027 — Device Management

```http
GET /api/v1/accounts/me/devices
DELETE /api/v1/accounts/me/devices/{device_id}
```

---

## FR-028 — Session Management

```http
GET /api/v1/accounts/me/sessions
POST /api/v1/accounts/me/sessions/{session_id}/revoke
```

---

## FR-029 — Account Invitations

```http
POST /api/v1/accounts/invitations
```

---

## FR-030 — Invitation List

```http
GET /api/v1/accounts/invitations
```

---

## FR-031 — Cancel Invitation

```http
DELETE /api/v1/accounts/invitations/{invitation_id}
```

---

## FR-032 — Resend Invitation

```http
POST /api/v1/accounts/invitations/{invitation_id}/resend
```

Rate limits SHALL apply.

---

## FR-033 — Accept Invitation

```http
POST /api/v1/accounts/invitations/{token}/accept
```

The token SHALL be:

* Short-lived
* Single-use
* Cryptographically random
* Stored securely
* Invalidated after use

---

## FR-034 — Organization Membership

The Account Service SHALL integrate with Organization Service.

---

## FR-035 — Add Organization Member

Authorized organization administrators SHALL be able to add users.

---

## FR-036 — Remove Organization Member

Authorized administrators SHALL be able to remove members according to policy.

---

## FR-037 — Workplace Membership

The Account Service SHALL integrate with Workplace Service.

---

## FR-038 — Role Assignment

Role assignment SHALL be delegated to the authorization/RBAC subsystem.

Account Service SHALL record membership relationships but SHALL NOT bypass authorization policy.

---

## FR-039 — Role Change Event

Role changes SHALL emit:

```text
account.role_changed
```

---

## FR-040 — Ownership Transfer

Ownership transfer SHALL require:

```text
Current Owner Authorization
Strong MFA
Target Verification
Policy Validation
Audit
Notification
```

---

## FR-041 — Ownership Transfer Flow

```text
Current Owner
     |
     v
Request Transfer
     |
     v
Strong MFA
     |
     v
Select New Owner
     |
     v
Target Verification
     |
     v
Policy Evaluation
     |
     v
Transfer
     |
     v
Audit + Notification
```

---

## FR-042 — Account Risk

The system SHALL expose security risk status only to authorized users.

---

## FR-043 — Security Alerts

Users SHALL receive account-security alerts.

---

## FR-044 — Account Activity

```http
GET /api/v1/accounts/me/activity
```

The endpoint SHALL return only events that the user is authorized to see.

---

## FR-045 — Administrative Audit

```http
GET /api/v1/admin/accounts/{account_id}/audit
```

This SHALL require appropriate administrative authorization.

---

## FR-046 — Account Export

```http
POST /api/v1/accounts/me/export
```

The export process SHOULD be asynchronous.

---

## FR-047 — Export Job

```text
Export Requested
      |
      v
Authorization
      |
      v
Security Verification
      |
      v
Create Job
      |
      v
Generate Export
      |
      v
Encrypt
      |
      v
Temporary Download
      |
      v
Expiration
```

---

## FR-048 — Account Avatar

The system SHALL validate uploaded profile images.

---

## FR-049 — Account Search Security

Search APIs SHALL prevent unauthorized tenant enumeration.

---

## FR-050 — Bulk Account Operations

Authorized administrators MAY perform bulk operations.

Examples:

```text
Suspend Users
Activate Users
Invite Users
Assign Permitted Roles
Remove Users
```

Bulk operations SHALL:

* Require appropriate permissions
* Have rate limits
* Support partial failure reporting
* Produce audit events
* Use asynchronous jobs at scale

---

## 10. ADMIN ACCOUNT MANAGEMENT

Administrative dashboards SHALL provide:

```text
Account Overview
User Directory
Pending Invitations
Suspended Accounts
Locked Accounts
Security Holds
Recently Created Accounts
Recently Active Accounts
Recently Inactive Accounts
High-Risk Accounts
```

---

## 11. SUPER ADMIN ACCOUNT MANAGEMENT

Super Admin SHALL have platform-level account management capabilities subject to security policy.

Capabilities MAY include:

```text
Search Platform Users
View Account Metadata
Suspend Account
Restore Account
Security Hold
Force Reauthentication
Revoke Sessions
Require MFA
Force Password Reset
Review Account Audit
```

Permanent deletion SHOULD require additional safeguards and separation of duties.

---

## 12. ORGANIZATION ACCOUNT MANAGEMENT

Organization Admin SHALL be able to:

```text
View Organization Users
Invite Users
Remove Users
View Membership
Manage Permitted Roles
Suspend Members
Restore Members
Configure Account Policies
```

They SHALL NOT access unrelated organizations.

---

## 13. WORKPLACE ACCOUNT MANAGEMENT

Workplace Admin SHALL be able to:

```text
View Workplace Users
Invite Users
Remove Users
Manage Workplace Membership
Manage Workplace Policies
Review Account Activity
```

---

## 14. SECURITY ADMIN ACCOUNT MANAGEMENT

Security Admin SHALL be able to:

```text
Review Security Holds
Review Risk Signals
Revoke Sessions
Force MFA
Require Reauthentication
Lock Accounts
Unlock Accounts
Investigate Recovery
Review Security Audit
```

Every action SHALL be audited.

---

## 15. BILLING ACCOUNT MANAGEMENT

Billing administrators SHALL be able to view account information required for billing operations.

Billing administrators SHALL NOT receive unnecessary authentication secrets or unrelated personal data.

---

## 16. SUPPORT ACCOUNT MANAGEMENT

Support agents SHALL have restricted account-management access.

They MAY:

```text
Search Customer
View Allowed Profile
Review Support History
Initiate Approved Recovery Workflow
```

They SHALL NOT:

```text
View Passwords
View MFA Secrets
Bypass MFA
Directly Modify Authentication Secrets
Grant Privileges
```

---

## 17. AI-ASSISTED ACCOUNT MANAGEMENT

SalesGenie MAY use AI to assist with:

```text
Account Risk Analysis
Suspicious Account Detection
Duplicate Account Detection
Unusual Activity Detection
Account Health Analysis
Security Recommendation
Support Routing
Account Classification
```

AI SHALL NOT autonomously perform high-impact account operations without deterministic policy authorization.

---

## 18. AI ACCOUNT RISK ANALYSIS

Example:

```json
{
  "account_id": "usr_123",
  "risk_score": 91,
  "risk_level": "CRITICAL",
  "signals": [
    "new_device",
    "unusual_location",
    "multiple_failed_logins",
    "recent_password_reset",
    "privileged_role"
  ],
  "recommended_action": "SECURITY_HOLD",
  "requires_human_review": true
}
```

---

## 19. HUMAN-IN-THE-LOOP ACCOUNT SECURITY

High-risk events SHALL be eligible for human review.

Example:

```text
AI Risk Engine
      |
      v
High-Risk Account
      |
      v
Security Queue
      |
      v
Human Security Analyst
      |
      +--> Approve
      +--> Reject
      +--> Suspend
      +--> Security Hold
      +--> Force Reauthentication
      +--> Force MFA
```

---

## 20. ACCOUNT SECURITY EVENTS

The system SHALL detect:

```text
Multiple Failed Logins
Impossible Travel
New Device
New Location
Email Change
Password Change
MFA Change
Role Change
Ownership Change
Mass Account Changes
Suspicious Session
Unusual Data Export
Suspicious API Activity
```

---

## 21. ACCOUNT EVENT SCHEMA

Example:

```json
{
  "event_id": "evt_123",
  "event_type": "account.updated",
  "account_id": "usr_123",
  "tenant_id": "tenant_123",
  "actor_id": "usr_456",
  "actor_type": "organization_admin",
  "timestamp": "2026-08-22T15:00:00Z",
  "ip_address": "redacted",
  "device_id": "device_123",
  "changes": [
    "designation"
  ],
  "risk_score": 12,
  "correlation_id": "corr_123"
}
```

---

## 22. ACCOUNT DATA MODEL

## 22.1 Account

```text
Account
--------------------------------
id
user_id
tenant_id
organization_id
workplace_id
username
email
email_verified
status
account_type
display_name
first_name
last_name
profile_image_id
phone
job_title
timezone
language
country
created_at
updated_at
last_login_at
suspended_at
locked_at
deleted_at
version
```

---

## 22.2 Account Security

```text
AccountSecurity
--------------------------------
id
account_id
risk_score
risk_level
last_security_review
password_changed_at
mfa_enabled
security_hold
failed_login_count
last_failed_login_at
last_security_event_at
```

---

## 22.3 Account Preferences

```text
AccountPreferences
--------------------------------
id
account_id
language
timezone
theme
marketing_notifications
product_notifications
usage_notifications
billing_notifications
support_notifications
created_at
updated_at
```

---

## 22.4 Invitation

```text
Invitation
--------------------------------
id
organization_id
workplace_id
email
invited_by
role
token_hash
expires_at
accepted_at
status
created_at
```

---

## 22.5 Membership

```text
Membership
--------------------------------
id
account_id
organization_id
workplace_id
membership_type
status
created_at
updated_at
```

---

## 22.6 Account Deletion Request

```text
AccountDeletionRequest
--------------------------------
id
account_id
requested_by
reason
requested_at
grace_period_ends_at
cancelled_at
completed_at
status
```

---

## 23. ACCOUNT API ARCHITECTURE

```text
                         Client
                           |
                           v
                       API Gateway
                           |
                           v
                  Authentication Layer
                           |
                           v
                   Authorization Layer
                           |
                           v
                    Account Service
                           |
       +-------------------+-------------------+
       |                   |                   |
       v                   v                   v
   PostgreSQL           Redis              Event Bus
       |                                       |
       |                       +---------------+---------------+
       |                       |               |               |
       v                       v               v               v
 Organization              Security        Audit          Notification
 Service                    Service        Service           Service
```

---

## 24. ACCOUNT EVENT-DRIVEN ARCHITECTURE

```text
Account Service
      |
      v
Event Bus
      |
      +--> Security Service
      |
      +--> Audit Service
      |
      +--> Notification Service
      |
      +--> Analytics Service
      |
      +--> Billing Service
      |
      +--> Organization Service
      |
      +--> Workplace Service
      |
      +--> AI Risk Engine
```

---

## 25. ACCOUNT MANAGEMENT WITH RBAC

RBAC SHALL determine which account-management operations are available to each role.

Example:

```text
Super Admin
    |
    +--> Platform Accounts

Organization Owner
    |
    +--> Organization Accounts

Organization Admin
    |
    +--> Organization Members

Workplace Admin
    |
    +--> Workplace Members

Team Manager
    |
    +--> Team Members

End User
    |
    +--> Own Account
```

---

## 26. ACCOUNT MANAGEMENT WITH ABAC

ABAC SHALL evaluate:

```text
User
Role
Organization
Workplace
Resource
Action
Device
Location
Risk
Time
Authentication Context
```

Example:

```text
User:
Organization Admin

Action:
Delete Account

Target:
Organization Member

Risk:
HIGH

MFA:
Verified

Policy:
Deletion Requires Owner Approval

Decision:
DENY
```

---

## 27. ACCOUNT MANAGEMENT WITH MFA

Sensitive operations SHALL use step-up MFA.

Examples:

```text
Change Email
Change Password
Disable MFA
Delete Account
Transfer Ownership
Export Data
Change Role
Security Hold Removal
Billing Ownership Change
```

---

## 28. ACCOUNT MANAGEMENT WITH SESSION MANAGEMENT

Account changes MAY trigger session invalidation.

Examples:

```text
Password Changed
      |
      v
Review Active Sessions
      |
      v
Revoke High-Risk Sessions
```

For high-risk security events:

```text
Security Hold
      |
      v
Revoke All Sessions
      |
      v
Require Reauthentication
```

---

## 29. ACCOUNT MANAGEMENT WITH BILLING

Account Service SHALL integrate with Billing Service.

Events MAY include:

```text
Account Created
Subscription Owner Changed
Billing Contact Changed
Organization Owner Changed
Account Deleted
Organization Closed
```

Account deletion SHALL NOT automatically erase financial records that must legally or contractually be retained.

---

## 30. ACCOUNT MANAGEMENT WITH SUPPORT

Support workflows SHALL use scoped account-management permissions.

Support actions SHALL be auditable.

---

## 31. ACCOUNT MANAGEMENT WITH AI AGENTS

AI agents SHALL have separate machine identities.

They SHALL NOT be represented as ordinary human users.

Example:

```text
AI Agent
    |
    v
Agent Identity
    |
    v
Scoped Permissions
    |
    v
ABAC Evaluation
    |
    v
Tool Execution
```

AI agents SHALL have:

```text
Agent ID
Owner
Tenant
Scope
Status
Credential
Created At
Last Used
Risk State
```

---

## 32. ACCOUNT DELETION ARCHITECTURE

```text
User
 |
 v
Delete Request
 |
 v
Authentication
 |
 v
MFA / Step-Up
 |
 v
Risk Evaluation
 |
 v
Policy Validation
 |
 v
Deletion Grace Period
 |
 +----> Cancel
 |
 v
Deletion Job
 |
 +--> Account Data
 +--> Preferences
 +--> Devices
 +--> Sessions
 +--> Memberships
 +--> Personal Data
 |
 v
Retention Exceptions
 |
 v
Audit
 |
 v
Deleted / Archived
```

---

## 33. DATA EXPORT SECURITY

Exports SHALL:

* Require authentication.
* Require authorization.
* Require step-up MFA where appropriate.
* Be encrypted.
* Expire.
* Be access-controlled.
* Be audited.

---

## 34. ACCOUNT ENUMERATION PROTECTION

Authentication and account-recovery APIs SHALL avoid revealing whether a particular email/username exists where such disclosure creates security risk.

Responses SHOULD be appropriately generalized.

---

## 35. ACCOUNT CREATION ABUSE PROTECTION

SalesGenie SHALL protect against:

```text
Bot Registration
Mass Registration
Fake Accounts
Invitation Abuse
Email Abuse
Credential Stuffing
```

Controls MAY include:

```text
Rate Limiting
Risk Scoring
CAPTCHA
Email Verification
IP Reputation
Device Reputation
Behavioral Analysis
```

---

## 36. DUPLICATE ACCOUNT DETECTION

The AI/risk engine MAY detect potentially duplicate accounts using:

```text
Email
Domain
Organization
Invitation
Device
Behavior
Account Metadata
```

AI recommendations SHALL not automatically merge accounts.

---

## 37. ACCOUNT MERGE

If account merging is supported:

```text
Source Account
      |
      v
Ownership Verification
      |
      v
Strong MFA
      |
      v
Conflict Analysis
      |
      v
Human Approval where required
      |
      v
Merge
      |
      v
Audit
```

---

## 38. ACCOUNT OWNERSHIP SECURITY

Ownership changes SHALL be treated as critical operations.

They SHALL require:

```text
Strong Authentication
MFA
Authorization
Policy Validation
Audit
Notification
```

---

## 39. SECURITY NOTIFICATIONS

Security-critical notifications SHALL be delivered independently from ordinary marketing preferences.

Examples:

```text
New Login
Password Change
Email Change
MFA Change
New Device
Account Suspension
Ownership Transfer
Deletion Request
Security Hold
```

---

## 40. ADMIN AUDIT REQUIREMENTS

Every privileged account-management operation SHALL contain:

```text
Actor
Target
Action
Timestamp
Tenant
Organization
Workplace
Reason
Authentication Context
IP Metadata
Device Metadata
Result
Correlation ID
```

---

## 41. AUDIT IMMUTABILITY

Audit records SHALL be append-only.

Administrative users SHALL not directly modify or delete audit records through ordinary account-management APIs.

---

## 42. OBSERVABILITY REQUIREMENTS

Metrics SHOULD include:

```text
account_creation_rate
account_activation_rate
account_verification_rate
account_suspension_rate
account_lock_rate
account_deletion_rate
account_recovery_rate
account_export_rate
invitation_acceptance_rate
account_update_rate
high_risk_account_count
```

---

## 43. SECURITY SLOs

Recommended targets:

```text
Account API availability: 99.99%+
Read latency: <200 ms typical
Standard update latency: <300 ms typical
Security event propagation: <5 seconds target
Critical account operation audit: near-real-time
```

Actual SLOs SHALL be validated through production load testing.

---

## 44. SCALABILITY

The Account Service SHALL support horizontal scaling.

```text
                Load Balancer
                     |
          +----------+----------+
          |          |          |
      Account-1  Account-2  Account-3
          |          |          |
          +----------+----------+
                     |
                  Database
```

Large account searches SHALL use:

* Indexed queries
* Cursor pagination
* Search indexes where required
* Read replicas where appropriate
* Asynchronous bulk processing

---

## 45. HIGH AVAILABILITY

Account management SHALL avoid single points of failure.

Critical dependencies SHOULD support:

```text
Replication
Failover
Health Checks
Circuit Breakers
Retries
Timeouts
Dead-Letter Queues
```

---

## 46. FAILURE HANDLING

The system SHALL distinguish:

```text
Authentication Failure
Authorization Failure
Validation Failure
Conflict
Rate Limit
Temporary Dependency Failure
Permanent Failure
Security Block
```

The API SHALL return consistent error formats.

---

## 47. IDEMPOTENCY

Critical mutation APIs SHOULD support:

```http
Idempotency-Key: <unique-key>
```

Especially:

```text
Invitation
Deletion
Ownership Transfer
Bulk Operations
Export
```

---

## 48. SECURITY TESTING

The Account Management subsystem SHALL be tested against:

```text
IDOR
Broken Access Control
Privilege Escalation
Tenant Escape
Account Enumeration
Mass Assignment
Session Hijacking
CSRF where applicable
Authentication Bypass
MFA Bypass
Invitation Token Abuse
Deletion Abuse
Ownership Transfer Abuse
Race Conditions
Replay Attacks
API Abuse
```

---

## 49. PENETRATION TESTING

Before production deployment, Account Management SHALL undergo security testing including:

* API penetration testing
* Authorization testing
* Tenant-isolation testing
* Authentication testing
* Session testing
* MFA integration testing
* Data exposure testing
* Rate-limit testing
* Race-condition testing

---

## 50. TESTING REQUIREMENTS

## Unit Tests

Test:

```text
Account Creation
Account Update
State Transitions
Deletion
Suspension
Restoration
Invitation
Membership
Ownership Transfer
Preferences
Validation
```

---

## Integration Tests

Test:

```text
Account + Auth
Account + MFA
Account + Session
Account + RBAC
Account + ABAC
Account + Organization
Account + Workplace
Account + Billing
Account + Security
Account + Audit
Account + Notification
Account + Event Bus
```

---

## End-to-End Tests

Test:

```text
Registration
Verification
Login
Profile Update
Password Change
MFA Enrollment
Device Management
Session Revocation
Organization Membership
Role Change
Suspension
Restoration
Deletion
Export
Recovery
```

---

## 51. PERFORMANCE TESTING

The platform SHALL test:

```text
10K concurrent account requests
100K concurrent account requests
Large account directory searches
Bulk invitations
Bulk suspension
Bulk restoration
High-volume login events
High-volume security events
```

Final capacity targets SHALL be established through production load testing rather than assumed solely from architecture.

---

## 52. DISASTER RECOVERY

Account Management SHALL support:

```text
Database Backup
Encrypted Backup
Point-in-Time Recovery
Cross-Region Recovery
Event Replay
Service Failover
Data Integrity Verification
```

---

## 53. BUSINESS CONTINUITY

If a non-critical dependency fails, Account Management SHALL continue operating where safely possible.

Example:

```text
Notification Service Down
        |
        v
Account Update
        |
        v
Commit Account Change
        |
        v
Queue Notification
        |
        v
Retry Notification
```

Security-critical dependencies SHALL fail closed when necessary.

---

## 54. BREAK-GLASS ACCOUNT OPERATIONS

Emergency account operations SHALL require:

```text
Explicit Reason
Strong Authentication
Strong MFA
Elevated Authorization
Time-Limited Access
Audit
Security Notification
Post-Incident Review
```

---

## 55. ADMIN DASHBOARD

## Account Directory

```text
+----------------------------------------------------+
| Account Management                                 |
+----------------------------------------------------+
| Search                                             |
| Filters                                            |
+----------------------------------------------------+
| User | Email | Role | Org | Status | Risk | Action|
+----------------------------------------------------+
| ...                                                |
+----------------------------------------------------+
```

---

## 56. ACCOUNT DETAILS DASHBOARD

```text
Account
|
+-- Profile
|
+-- Organization
|
+-- Workplace
|
+-- Roles
|
+-- Security
|     +-- MFA
|     +-- Devices
|     +-- Sessions
|     +-- Risk
|
+-- Billing
|
+-- Activity
|
+-- Audit
|
+-- Support
|
+-- Data
```

---

## 57. USER ACCOUNT DASHBOARD

```text
My Account
|
+-- Profile
+-- Security
+-- MFA
+-- Sessions
+-- Devices
+-- Organizations
+-- Workplaces
+-- Notifications
+-- Privacy
+-- Data Export
+-- Delete Account
```

---

## 58. ACCOUNT SECURITY DASHBOARD

```text
Security
|
+-- Security Score
+-- MFA Status
+-- Password Status
+-- Active Sessions
+-- Devices
+-- Recent Login Activity
+-- Security Alerts
+-- Recovery
```

---

## 59. ACCOUNT HEALTH SCORE

SalesGenie MAY calculate an account security-health score.

Example:

```text
MFA Enabled              +30
Strong MFA               +20
Recent Password Change   +10
Known Device             +10
Old/Weak Security        -20
Suspicious Activity      -30
```

The score SHALL be advisory unless incorporated into deterministic security policy.

---

## 60. ACCOUNT SECURITY AUTOMATION

The system MAY automatically:

```text
Detect Suspicious Activity
Require MFA
Revoke Sessions
Lock Account
Create Security Incident
Notify User
Create Human Review Case
```

Critical actions SHALL follow deterministic security policy.

---

## 61. HUMAN SECURITY OVERRIDE

Authorized security personnel MAY override automated decisions where policy permits.

Every override SHALL require:

```text
Actor
Reason
Authentication
Authorization
Timestamp
Target
Previous Decision
New Decision
```

---

## 62. PRIVACY REQUIREMENTS

SalesGenie SHALL:

* Minimize PII collection.
* Minimize PII exposure.
* Protect account data.
* Provide data export where applicable.
* Support deletion workflows.
* Respect retention requirements.
* Restrict administrative access.
* Audit privileged access.

---

## 63. COMPLIANCE

The Account Management subsystem SHOULD support controls relevant to:

```text
SOC 2
ISO 27001
GDPR
CCPA/CPRA
PCI DSS where applicable
Enterprise security requirements
```

Compliance implementation SHALL depend on actual deployment scope and jurisdiction.

---

## 64. ACCEPTANCE CRITERIA

Account Management SHALL be considered production-ready when:

* Account creation works.
* Account verification works.
* Profile management works.
* Email changes are protected.
* Password changes integrate correctly.
* MFA integration works.
* Session management works.
* Device management works.
* Invitations work.
* Membership management works.
* Role changes are properly authorized.
* Organization isolation works.
* Workplace isolation works.
* Account suspension works.
* Account restoration works.
* Security holds work.
* Account deletion works.
* Deletion grace periods work.
* Data export works.
* Ownership transfer is protected.
* AI risk analysis works.
* Human security escalation works.
* All privileged actions are audited.
* Secrets are never logged.
* Tenant isolation passes security testing.
* APIs are rate-limited.
* Bulk operations are protected.
* Disaster recovery is tested.
* Service failure handling works.
* Horizontal scaling is validated.

---

## 65. END-TO-END ACCOUNT MANAGEMENT FLOW

```text
                         USER
                           |
                           v
                     Registration
                           |
                           v
                    Email Verification
                           |
                           v
                       Account
                           |
                           v
                    Authentication
                           |
                           v
                         MFA
                           |
                           v
                    Session Creation
                           |
                           v
                     Authorization
                           |
                           v
                       Dashboard
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
       Profile          Security        Organization
          |                |                |
          v                v                v
      Preferences        MFA           Membership
          |                |                |
          +----------------+----------------+
                           |
                           v
                    Account Activity
                           |
                           v
                     Risk Engine
                           |
                +----------+----------+
                |                     |
              Normal                High Risk
                |                     |
                v                     v
              Allow             Human Security
                                      |
                                      v
                              Security Decision
```

---

## 66. MASTER ACCOUNT SECURITY MODEL

```text
                         SALES GENIE
                              |
                       ACCOUNT SERVICE
                              |
        +---------------------+---------------------+
        |                     |                     |
     Identity             Lifecycle             Profile
        |                     |                     |
        v                     v                     v
 Authentication          Status              Preferences
        |
        +----------+
        |          |
       MFA      Sessions
        |
        v
   Risk Engine
        |
        +----------------------+
        |                      |
        v                      v
   AI Security          Human Security
        |                      |
        +----------+-----------+
                   |
                   v
              Policy Engine
                   |
          +--------+--------+
          |                 |
        ALLOW              DENY
          |
          v
    Authorization
          |
          v
       Resource
          |
          v
        Audit
```

---

## 67. MASTER ACCOUNT LIFECYCLE

```text
                    ACCOUNT CREATION
                           |
                           v
                       PENDING
                           |
                           v
                     VERIFICATION
                           |
                           v
                        ACTIVE
                           |
              +------------+------------+
              |            |            |
              v            v            v
           INACTIVE     SUSPENDED     LOCKED
              |            |            |
              +------------+------------+
                           |
                           v
                       RESTORED
                           |
                           v
                         ACTIVE
                           |
                           v
                  DELETION REQUESTED
                           |
                           v
                  GRACE PERIOD
                           |
                  +--------+--------+
                  |                 |
                  v                 v
              CANCELLED          DELETE
                                    |
                                    v
                                ARCHIVED
```

---

## 68. FINAL ARCHITECTURAL REQUIREMENT

The SalesGenie Account Management subsystem SHALL NOT be implemented as a simple user-profile CRUD module.

It SHALL operate as an enterprise identity lifecycle and account-security control plane integrating:

```text
Account Lifecycle
+
Identity
+
Authentication
+
MFA
+
Session Management
+
RBAC
+
ABAC
+
Organization Management
+
Workplace Management
+
Device Management
+
Security Risk
+
AI-Assisted Security
+
Human Security
+
Billing
+
Support
+
Notifications
+
Audit
+
Event-Driven Architecture
+
Data Privacy
+
High Availability
+
Scalability
+
Disaster Recovery
```

The system SHALL enforce strict separation between:

```text
Account Ownership
Account Management
Authentication
Authorization
Security Operations
Billing Operations
```

No account-management API SHALL independently grant unauthorized privileges.

All high-impact account operations SHALL require appropriate authentication, authorization, policy evaluation, and auditability.

---

## 69. MASTER REQUIREMENT SUMMARY

```text
                         ACCOUNT REQUEST
                               |
                               v
                       Authentication
                               |
                               v
                             MFA
                               |
                               v
                       Risk Evaluation
                               |
                               v
                       Authorization
                               |
                 +-------------+-------------+
                 |                           |
               ALLOW                        DENY
                 |
                 v
             ABAC Policy
                 |
                 v
          Account Operation
                 |
        +--------+--------+
        |        |        |
      Profile  Security  Membership
        |        |        |
        +--------+--------+
                 |
                 v
            Event Bus
                 |
       +---------+---------+
       |         |         |
     Audit    Security   Notification
                 |
                 v
            AI Risk Engine
                 |
                 v
          Human Escalation
```

**Account Management is a core SalesGenie control-plane subsystem. It SHALL provide secure, auditable, multi-tenant lifecycle management for human and machine identities while integrating authentication, MFA, authorization, security, organization/workplace membership, billing, support, AI-assisted risk detection, and human security operations.**
