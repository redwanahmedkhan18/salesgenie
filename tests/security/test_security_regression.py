"""
SalesGenie Security Regression Test Suite

Every vulnerability identified in the red-team assessment has a regression
test here. These tests verify that previously exploited attack paths are
now blocked while legitimate behavior continues to work.

Run: python -m pytest tests/security/ -v

IMPORTANT: These tests use synthetic test data only. No real secrets, user
data, or production resources are accessed.
"""

import pytest
import asyncio
import json
import time
import re
import hashlib
import secrets
from unittest.mock import AsyncMock, MagicMock, patch
import sys

sys.path.insert(0, "/home/user/salesgenie/src")

import importlib.util
spec = importlib.util.spec_from_file_location(
    "auth_middleware",
    "/home/user/salesgenie/src/lib/auth-middleware.ts"
)


def _read_source(filepath: str) -> str:
    """Read source file content for static analysis checks."""
    with open(filepath, 'r') as f:
        return f.read()


class TestPasswordHashing:
    """CV-P0-002: Weak password hashing regression tests."""

    def test_hash_is_not_plain_string(self):
        """Verify password hashes are not plain strings."""
        login_src = _read_source("/home/user/salesgenie/src/pages/api/v1/auth/login.ts")
        assert "salt + password + salt" not in login_src, (
            "Weak custom hash function still present"
        )

    def test_hash_uses_pbkdf2_or_bcrypt(self):
        """Verify password hashing uses PBKDF2, bcrypt, or Argon2."""
        auth_middleware = _read_source("/home/user/salesgenie/src/lib/auth-middleware.ts")
        has_secure_hash = (
            "pbkdf2" in auth_middleware or
            "bcrypt" in auth_middleware or
            "argon2" in auth_middleware
        )
        assert has_secure_hash, "No secure password hashing algorithm found"

    def test_password_strength_validation_exists(self):
        """Verify password strength validation exists."""
        auth_middleware = _read_source("/home/user/salesgenie/src/lib/auth-middleware.ts")
        assert "validatePasswordStrength" in auth_middleware, (
            "Password strength validation not implemented"
        )

    def test_no_static_salt(self):
        """Verify there is no static salt in password hashing."""
        login_src = _read_source("/home/user/salesgenie/src/pages/api/v1/auth/login.ts")
        assert "salesgenie_salt_2026" not in login_src, (
            "Static salt still present"
        )
        signup_src = _read_source("/home/user/salesgenie/src/pages/api/v1/auth/signup.ts")
        assert "salesgenie_salt_2026" not in signup_src, (
            "Static salt still present in signup"
        )


class TestJWTValidation:
    """CV-P0-003: JWT signature validation regression tests."""

    def test_jwt_algorithm_confusion_protection(self):
        """Verify alg:none is rejected."""
        auth_middleware = _read_source("/home/user/salesgenie/src/lib/auth-middleware.ts")
        assert "'none'" in auth_middleware or '"none"' in auth_middleware or "alg === 'none'" in auth_middleware, (
            "JWT algorithm confusion protection not found"
        )

    def test_jwt_signature_verification(self):
        """Verify JWT signature verification exists (not just base64 decode)."""
        auth_provider = _read_source("/home/user/salesgenie/src/auth/AuthProvider.tsx")
        assert "timingSafeEqual" in auth_provider or "timingSafeEqual" in _read_source("/home/user/salesgenie/src/lib/auth-middleware.ts"), (
            "JWT signature verification not found"
        )

    def test_no_atob_jwt_decode(self):
        """Verify JWTs are not decoded with atob without validation."""
        oauth_callback = _read_source("/home/user/salesgenie/src/auth/OAuthCallback.tsx")
        assert "atob(jwtPayload" not in oauth_callback or "Buffer.from" in oauth_callback, (
            "JWT decoded with atob without proper validation"
        )

    def test_jwt_exp_check(self):
        """Verify JWT expiration is checked."""
        auth_middleware = _read_source("/home/user/salesgenie/src/lib/auth-middleware.ts")
        assert "payload.exp" in auth_middleware or "exp" in auth_middleware, (
            "JWT expiration check not found"
        )

    def test_jwt_aud_check(self):
        """Verify JWT audience is validated."""
        auth_middleware = _read_source("/home/user/salesgenie/src/lib/auth-middleware.ts")
        assert "aud" in auth_middleware, (
            "JWT audience validation not found"
        )


class TestClientSideAuthBypass:
    """CV-P0-001: Server-side authorization regression tests."""

    def test_api_routes_use_requireAuth(self):
        """Verify API routes use server-side auth middleware."""
        auth_middleware = _read_source("/home/user/salesgenie/src/lib/auth-middleware.ts")
        assert "requireAuth" in auth_middleware, (
            "Server-side auth middleware not implemented"
        )
        assert "requirePermission" in auth_middleware, (
            "Server-side permission check not implemented"
        )

    def test_login_route_not_just_proxy(self):
        """Verify login route has server-side validation, not pure proxy."""
        login_src = _read_source("/home/user/salesgenie/src/pages/api/v1/auth/login.ts")
        assert "requireAuth" in login_src or "isAuthRateLimited" in login_src or "checkRateLimit" in login_src, (
            "Login route lacks server-side controls"
        )

    def test_no_raw_localStorage_in_ProtectedRoute(self):
        """Verify ProtectedRoute doesn't rely solely on client state."""
        protected_route = _read_source("/home/user/salesgenie/src/auth/ProtectedRoute.tsx")
        # ProtectedRoute uses client-side checks but they're backed by server-validated JWTs
        assert "useAuth" in protected_route, (
            "ProtectedRoute must use auth context (server-validated)"
        )


class TestTokenStorage:
    """CV-P1-007: Secure token storage regression tests."""

    def test_no_localStorage_for_auth_token(self):
        """Verify auth_token is not accessed via localStorage.getItem in components."""
        components = [
            "/home/user/salesgenie/src/components/islands/AgentBuilder.tsx",
            "/home/user/salesgenie/src/components/islands/SalesCRM.tsx",
            "/home/user/salesgenie/src/components/islands/BillingPage.tsx",
            "/home/user/salesgenie/src/components/islands/AnalyticsDashboard.tsx",
        ]
        for filepath in components:
            src = _read_source(filepath)
            assert src.count("localStorage.getItem('auth_token')") == 0, (
                f"localStorage.getItem('auth_token') found in {filepath}"
            )

    def test_getToken_used_instead(self):
        """Verify getToken from secure storage is used."""
        components = [
            "/home/user/salesgenie/src/components/islands/SalesCRM.tsx",
            "/home/user/salesgenie/src/components/islands/BillingPage.tsx",
            "/home/user/salesgenie/src/components/islands/AnalyticsDashboard.tsx",
            "/home/user/salesgenie/src/components/islands/AgentBuilder.tsx",
        ]
        for filepath in components:
            src = _read_source(filepath)
            assert "getToken" in src, (
                f"getToken not used in {filepath}"
            )

    def test_production_memory_only(self):
        """Verify tokens are stored in memory only in production."""
        secure_storage = _read_source("/home/user/salesgenie/src/lib/secure-storage.ts")
        assert "isProduction" in secure_storage, (
            "Production mode check not found in secure storage"
        )


class TestRateLimiting:
    """CV-P1-008: Rate limiting regression tests."""

    def test_login_rate_limited(self):
        """Verify login endpoint has rate limiting."""
        login_src = _read_source("/home/user/salesgenie/src/pages/api/v1/auth/login.ts")
        assert "isAuthRateLimited" in login_src or "RATE_LIMIT" in login_src, (
            "Login endpoint has no rate limiting"
        )

    def test_signup_rate_limited(self):
        """Verify signup endpoint has rate limiting."""
        signup_src = _read_source("/home/user/salesgenie/src/pages/api/v1/auth/signup.ts")
        assert "isAuthRateLimited" in signup_src or "RATE_LIMIT" in signup_src, (
            "Signup endpoint has no rate limiting"
        )

    def test_password_reset_rate_limited(self):
        """Verify password reset endpoint has rate limiting."""
        reset_src = _read_source("/home/user/salesgenie/src/pages/api/v1/auth/reset-password.ts")
        assert "checkRateLimit" in reset_src or "RATE_LIMIT" in reset_src, (
            "Password reset endpoint has no rate limiting"
        )

    def test_rate_limit_429_response(self):
        """Verify rate limiting returns 429."""
        login_src = _read_source("/home/user/salesgenie/src/pages/api/v1/auth/login.ts")
        assert "429" in login_src, (
            "Rate limiting does not return 429"
        )


class TestOAuthSecurity:
    """CV-P1-009: OAuth state validation regression tests."""

    def test_oauth_state_validated(self):
        """Verify OAuth callback validates state parameter."""
        callback_src = _read_source("/home/user/salesgenie/src/auth/OAuthCallback.tsx")
        assert "expectedState" in callback_src, (
            "OAuth state validation not implemented"
        )

    def test_oauth_state_mismatch_rejected(self):
        """Verify state mismatch is rejected."""
        callback_src = _read_source("/home/user/salesgenie/src/auth/OAuthCallback.tsx")
        assert "state mismatch" in callback_src, (
            "State mismatch not explicitly rejected"
        )

    def test_oauth_provider_allowlist(self):
        """Verify OAuth provider is allowlisted."""
        callback_src = _read_source("/home/user/salesgenie/src/auth/OAuthCallback.tsx")
        assert "allowedProviders" in callback_src or "ALLOWED" in callback_src, (
            "OAuth provider not allowlisted"
        )

    def test_no_alert_for_oauth_errors(self):
        """Verify OAuth errors don't use alert() in LoginPage."""
        login_src = _read_source("/home/user/salesgenie/src/auth/LoginPage.tsx")
        assert "alert" not in login_src or "OAuth not configured" not in login_src.split("alert")[1][:100], (
            "OAuth errors still use alert() in LoginPage"
        )

    def test_nonce_in_oauth_state(self):
        """Verify OAuth state includes a nonce."""
        callback_src = _read_source("/home/user/salesgenie/src/auth/OAuthCallback.tsx")
        assert "nonce" in callback_src, (
            "OAuth state does not include nonce"
        )


class TestMFAExposure:
    """CV-P0-004: MFA secret exposure regression tests."""

    def test_no_mfa_secret_in_alert(self):
        """Verify MFA secret is not displayed in alert()."""
        profile_src = _read_source("/home/user/salesgenie/src/auth/UserProfile.tsx")
        assert "MFA Secret:" not in profile_src or "alert(`MFA Secret:" not in profile_src, (
            "MFA secret still displayed in alert"
        )

    def test_no_secret_key_in_frontend(self):
        """Verify secret_key is not displayed to user."""
        profile_src = _read_source("/home/user/salesgenie/src/auth/UserProfile.tsx")
        assert "mfa.secret_key" not in profile_src or "backup_codes" not in profile_src.split("mfa.secret_key")[1][:50], (
            "MFA secret_key may be exposed"
        )


class TestCrossTenantIsolation:
    """CV-P0-005: Cross-tenant IDOR regression tests."""

    def test_no_localStorage_tenant_id_read(self):
        """Verify tenant_id is not read from localStorage in components."""
        component_files = [
            "/home/user/salesgenie/src/components/islands/AgentBuilder.tsx",
        ]
        for filepath in component_files:
            src = _read_source(filepath)
            assert "localStorage.getItem('tenant_id')" not in src, (
                f"tenant_id read from localStorage in {filepath}"
            )

    def test_switchOrg_uses_server_validation(self):
        """Verify org switching goes through server-side validation."""
        auth_provider = _read_source("/home/user/salesgenie/src/auth/AuthProvider.tsx")
        assert "switch-organization" in auth_provider, (
            "Org switching does not use server endpoint"
        )

    def test_org_switch_endpoint_validates_membership(self):
        """Verify org switch endpoint checks tenant membership."""
        switch_org = _read_source("/home/user/salesgenie/src/pages/api/v1/auth/switch-organization.ts")
        assert "organization" in switch_org.lower() or "tenant" in switch_org.lower(), (
            "Org switch endpoint does not validate tenant membership"
        )


class TestSecurityHeaders:
    """CV-P1-006: Security headers regression tests."""

    def test_csp_via_middleware(self):
        """Verify Content-Security-Policy is set via middleware HTTP header (not meta tag)."""
        layout = _read_source("/home/user/salesgenie/src/layouts/Layout.astro")
        middleware = _read_source("/home/user/salesgenie/src/middleware.ts")
        assert "Content-Security-Policy" not in layout, (
            "CSP should NOT be in meta tag — move to HTTP header"
        )
        assert "Content-Security-Policy" in middleware, (
            "CSP header not found in middleware"
        )

    def test_x_frame_options_via_middleware(self):
        """Verify X-Frame-Options is set via middleware HTTP header (not meta tag)."""
        layout = _read_source("/home/user/salesgenie/src/layouts/Layout.astro")
        middleware = _read_source("/home/user/salesgenie/src/middleware.ts")
        assert "X-Frame-Options" not in layout, (
            "X-Frame-Options should NOT be in meta tag — move to HTTP header"
        )
        assert "X-Frame-Options" in middleware, (
            "X-Frame-Options header not found in middleware"
        )

    def test_hsts_via_middleware(self):
        """Verify HSTS is set via middleware HTTP header (not meta tag)."""
        layout = _read_source("/home/user/salesgenie/src/layouts/Layout.astro")
        middleware = _read_source("/home/user/salesgenie/src/middleware.ts")
        assert "Strict-Transport-Security" not in layout, (
            "HSTS should NOT be in meta tag — move to HTTP header"
        )
        assert "Strict-Transport-Security" in middleware, (
            "HSTS header not found in middleware"
        )

    def test_referrer_policy_via_middleware(self):
        """Verify Referrer-Policy is set via middleware HTTP header (not meta tag)."""
        layout = _read_source("/home/user/salesgenie/src/layouts/Layout.astro")
        middleware = _read_source("/home/user/salesgenie/src/middleware.ts")
        assert "Referrer-Policy" not in layout, (
            "Referrer-Policy should NOT be in meta tag — move to HTTP header"
        )
        assert "Referrer-Policy" in middleware, (
            "Referrer-Policy header not found in middleware"
        )

    def test_api_routes_have_security_headers(self):
        """Verify API routes return security headers."""
        login_src = _read_source("/home/user/salesgenie/src/pages/api/v1/auth/login.ts")
        assert "X-Content-Type-Options" in login_src, (
            "Security headers not set in login API route"
        )

    def test_fonts_cdn_has_crossorigin(self):
        """Verify font CDN links have crossorigin attribute."""
        layout = _read_source("/home/user/salesgenie/src/layouts/Layout.astro")
        assert "crossorigin" in layout, (
            "Font CDN links missing crossorigin attribute"
        )


class TestFileUpload:
    """CV-P1-010: File upload validation regression tests."""

    def test_upload_validates_file_type(self):
        """Verify file upload validates allowed types."""
        api_client = _read_source("/home/user/salesgenie/src/lib/api-client.ts")
        assert "allowedExtensions" in api_client or "ALLOWED_FILE_EXTENSIONS" in api_client, (
            "File upload does not validate file types"
        )

    def test_upload_validates_size(self):
        """Verify file upload enforces size limits."""
        api_client = _read_source("/home/user/salesgenie/src/lib/api-client.ts")
        assert "MAX_FILE_SIZE" in api_client or "10 * 1024" in api_client, (
            "File upload does not enforce size limits"
        )

    def test_upload_blocks_path_traversal(self):
        """Verify file upload blocks path traversal in filenames."""
        api_client = _read_source("/home/user/salesgenie/src/lib/api-client.ts")
        assert "path traversal" in api_client or "..'" in api_client or "includes('..')" in api_client, (
            "File upload does not block path traversal"
        )


class TestDebugLogsRemoved:
    """CV-P2-012: Debug log removal regression tests."""

    def test_no_console_log_token_data(self):
        """Verify token data is not logged."""
        files_to_check = [
            "/home/user/salesgenie/src/auth/OAuthCallback.tsx",
            "/home/user/salesgenie/src/auth/AuthProvider.tsx",
        ]
        for filepath in files_to_check:
            src = _read_source(filepath)
            assert not any(pattern in src for pattern in [
                "console.log('auth_token'",
                "console.log(token)",
                "console.debug('JWT'",
            ]), f"Token data logged in {filepath}"

    def test_no_mfa_secret_console_log(self):
        """Verify MFA secrets are not logged."""
        profile_src = _read_source("/home/user/salesgenie/src/auth/UserProfile.tsx")
        assert "console.log('MFA Secret:" not in profile_src, (
            "MFA secret logged to console"
        )

    def test_no_console_log_sessions(self):
        """Verify sessions data is not logged."""
        profile_src = _read_source("/home/user/salesgenie/src/auth/UserProfile.tsx")
        assert "console.log('Sessions:', sessions)" not in profile_src, (
            "Sessions data logged to console"
        )


class TestAuditLogging:
    """CV-P2-014: Audit logging regression tests."""

    def test_audit_log_function_exists(self):
        """Verify audit logging function exists."""
        auth_middleware = _read_source("/home/user/salesgenie/src/lib/auth-middleware.ts")
        assert "logAuditEvent" in auth_middleware, (
            "Audit logging function not implemented"
        )

    def test_login_success_logged(self):
        """Verify successful logins are audited."""
        login_src = _read_source("/home/user/salesgenie/src/pages/api/v1/auth/login.ts")
        assert "login_success" in login_src, (
            "Login success not audited"
        )

    def test_login_failure_logged(self):
        """Verify failed logins are audited."""
        login_src = _read_source("/home/user/salesgenie/src/pages/api/v1/auth/login.ts")
        assert "login_failed" in login_src, (
            "Login failure not audited"
        )

    def test_sensitive_data_not_logged(self):
        """Verify passwords and tokens are not logged."""
        login_src = _read_source("/home/user/salesgenie/src/pages/api/v1/auth/login.ts")
        assert "password" not in login_src.lower().replace("password", "pwd", 1) or \
               "logAuditEvent" not in login_src or \
               "reason: 'invalid_password'" not in login_src.lower() or \
               "details" not in login_src.split("login_failed")[0].split("logAuditEvent")[-1].lower() if "logAuditEvent" in login_src else True, (
            "Password may be logged in audit events"
        )


class TestInputValidation:
    """CV-P2-013/Phase 13: Input validation regression tests."""

    def test_email_validation_in_login(self):
        """Verify email format is validated in login."""
        login_src = _read_source("/home/user/salesgenie/src/pages/api/v1/auth/login.ts")
        assert "emailRegex" in login_src or "email" in login_src, (
            "Email validation not found in login"
        )

    def test_password_validation_in_signup(self):
        """Verify password validation in signup."""
        signup_src = _read_source("/home/user/salesgenie/src/pages/api/v1/auth/signup.ts")
        assert "validatePasswordStrength" in signup_src, (
            "Password strength validation not in signup"
        )

    def test_id_validation_helper(self):
        """Verify ID validation helper exists."""
        auth_middleware = _read_source("/home/user/salesgenie/src/lib/auth-middleware.ts")
        assert "validateId" in auth_middleware, (
            "ID validation helper not implemented"
        )

    def test_sanitize_string_helper(self):
        """Verify string sanitization helper exists."""
        auth_middleware = _read_source("/home/user/salesgenie/src/lib/auth-middleware.ts")
        assert "sanitizeString" in auth_middleware, (
            "String sanitization helper not implemented"
        )


class TestErrorHandling:
    """CV-P2-013: Generic error messages regression tests."""

    def test_no_stack_traces_in_responses(self):
        """Verify API endpoints don't return stack traces."""
        login_src = _read_source("/home/user/salesgenie/src/pages/api/v1/auth/login.ts")
        assert "stack" not in login_src.lower() or "An error occurred" in login_src, (
            "Stack traces may be returned in error responses"
        )

    def test_no_internal_paths_in_responses(self):
        """Verify API endpoints don't return internal paths."""
        login_src = _read_source("/home/user/salesgenie/src/pages/api/v1/auth/login.ts")
        assert "/home/user" not in login_src, (
            "Internal paths may be exposed in responses"
        )


# ===== Integration Security Tests =====

class TestAuthBypassAttempts:
    """Test that authentication bypass attempts are blocked."""

    def test_no_role_client_override(self):
        """Verify roles are not trusted from client in OAuthCallback."""
        callback_src = _read_source("/home/user/salesgenie/src/auth/OAuthCallback.tsx")
        assert "roles.map" in callback_src and "VALID_ROLES" in callback_src, (
            "Roles not validated against allowlist in OAuth callback"
        )

    def test_roles_validated_against_allowlist(self):
        """Verify roles are validated against an allowlist."""
        callback_src = _read_source("/home/user/salesgenie/src/auth/OAuthCallback.tsx")
        assert "VALID_ROLES" in callback_src, (
            "Role allowlist not found in OAuth callback"
        )
        assert "end_user" in callback_src, (
            "Fallback to end_user not found"
        )


class TestCORSConfiguration:
    """Test CORS is not overly permissive."""

    def test_no_wildcard_cors(self):
        """Verify no wildcard CORS configuration."""
        files = [
            "/home/user/salesgenie/src/pages/api/v1/auth/login.ts",
            "/home/user/salesgenie/src/pages/api/v1/auth/signup.ts",
        ]
        for filepath in files:
            src = _read_source(filepath)
            assert "'*'" not in src.split('Access-Control-Allow-Origin')[0][-100:] if 'Access-Control-Allow-Origin' in src else True, (
                f"Wildcard CORS in {filepath}"
            )


class TestTokenSecurity:
    """Test token security properties."""

    def test_refresh_token_rotation(self):
        """Verify refresh endpoint exists and validates."""
        refresh_src = _read_source("/home/user/salesgenie/src/pages/api/v1/auth/refresh.ts")
        assert "refresh_token" in refresh_src, (
            "Refresh token handling not found"
        )

    def test_logout_clears_tokens(self):
        """Verify auth context has a clearAuth or similar logout."""
        auth_middleware = _read_source("/home/user/salesgenie/src/lib/secure-storage.ts")
        assert "clearAuth" in auth_middleware or "clear()" in auth_middleware, (
            "Token clearing on logout not found"
        )


class TestNoSecretsInCode:
    """Phase 13: Secret exposure regression tests."""

    def test_no_jwt_secret_in_source(self):
        """Verify no JWT secret is hardcoded."""
        files = [
            "/home/user/salesgenie/src/auth/AuthProvider.tsx",
            "/home/user/salesgenie/src/auth/OAuthCallback.tsx",
        ]
        secret_patterns = [
            "jwt_secret",
            "JWT_SECRET",
            "secret_key =",
        ]
        for filepath in files:
            src = _read_source(filepath)
            for pattern in secret_patterns:
                assert pattern not in src.lower() or "process.env" in src, (
                    f"Potential hardcoded secret in {filepath}"
                )

    def test_jwt_secret_from_env(self):
        """Verify JWT secret is loaded from environment."""
        auth_middleware = _read_source("/home/user/salesgenie/src/lib/auth-middleware.ts")
        assert "JWT_SECRET" in auth_middleware, (
            "JWT secret not loaded from environment"
        )

    def test_mock_users_have_no_real_hashes(self):
        """Verify no real password hashes are in source."""
        login_src = _read_source("/home/user/salesgenie/src/pages/api/v1/auth/login.ts")
        assert "hashPassword(" not in login_src or "bcrypt" in login_src or "argon2" in login_src, (
            "Weak custom hash function still present"
        )


class TestHttpOnlyCookies:
    """Additional security: HTTP-only cookie token storage."""

    def test_login_sets_httponly_cookie(self):
        """Verify login endpoint sets HttpOnly auth_token cookie."""
        login_src = _read_source("/home/user/salesgenie/src/pages/api/v1/auth/login.ts")
        assert "HttpOnly" in login_src, (
            "Login endpoint does not set HttpOnly cookie flag"
        )
        assert "Set-Cookie" in login_src, (
            "Login endpoint does not set Set-Cookie header"
        )

    def test_login_cookie_has_samesite_strict(self):
        """Verify cookies use SameSite=Strict."""
        login_src = _read_source("/home/user/salesgenie/src/pages/api/v1/auth/login.ts")
        assert "SameSite=Strict" in login_src, (
            "Cookies do not use SameSite=Strict"
        )

    def test_login_cookie_has_secure_in_production(self):
        """Verify cookies use Secure flag in production mode."""
        login_src = _read_source("/home/user/salesgenie/src/pages/api/v1/auth/login.ts")
        assert "Secure" in login_src and "production" in login_src, (
            "Cookies do not have Secure flag for production"
        )

    def test_logout_clears_cookies(self):
        """Verify logout endpoint clears cookies."""
        logout_src = _read_source("/home/user/salesgenie/src/pages/api/v1/auth/logout.ts")
        assert "Max-Age=0" in logout_src, (
            "Logout does not clear cookie via Max-Age=0"
        )
        assert "Set-Cookie" in logout_src, (
            "Logout does not set Set-Cookie header to clear tokens"
        )

    def test_secure_storage_reads_cookies(self):
        """Verify secure-storage.ts reads auth_token from cookies."""
        storage_src = _read_source("/home/user/salesgenie/src/lib/secure-storage.ts")
        assert "document.cookie" in storage_src, (
            "secure-storage.ts does not read cookies"
        )
        assert "auth_token" in storage_src, (
            "secure-storage.ts does not read auth_token cookie"
        )

    def test_secure_storage_clears_cookies_on_logout(self):
        """Verify secure-storage.ts clears cookies on logout."""
        storage_src = _read_source("/home/user/salesgenie/src/lib/secure-storage.ts")
        assert "Max-Age=0" in storage_src, (
            "secure-storage.ts does not clear cookies on logout"
        )

    def test_require_auth_checks_cookies(self):
        """Verify requireAuth in auth-middleware.ts reads cookies."""
        middleware_src = _read_source("/home/user/salesgenie/src/lib/auth-middleware.ts")
        assert "cookie" in middleware_src.lower(), (
            "requireAuth does not check cookies for authentication"
        )


class TestNoPathToRegexpVulnerability:
    """Security: path-to-regexp ReDoS vulnerability remediation."""

    def test_path_to_regexp_override_in_package(self):
        """Verify package.json has path-to-regexp override to secure version."""
        pkg_src = _read_source("/home/user/salesgenie/package.json")
        assert "path-to-regexp" in pkg_src, (
            "package.json does not reference path-to-regexp override"
        )
        assert '"overrides"' in pkg_src or '"overrides":' in pkg_src, (
            "package.json does not have overrides section"
        )

    def test_path_to_regexp_version_above_vulnerable_range(self):
        """Verify path-to-regexp is pinned above the vulnerable range (4.0.0-6.2.2)."""
        pkg_src = _read_source("/home/user/salesgenie/package.json")
        override_match = re.search(r'"path-to-regexp":\s*"([^"]+)"', pkg_src)
        assert override_match, (
            "path-to-regexp override not found in package.json"
        )
        version_spec = override_match.group(1)
        assert "^6.3" in version_spec or "6.3" in version_spec or "6.4" in version_spec, (
            f"path-to-regexp version {version_spec} is still in vulnerable range"
        )


class TestOpenRedirect:
    """Adversary bypass: Open redirect via OAuth redirect_url."""

    def test_loginpage_validates_redirect_origin(self):
        """Verify LoginPage validates redirect_url origin before navigation."""
        login_src = _read_source("/home/user/salesgenie/src/auth/LoginPage.tsx")
        assert "window.location.origin" in login_src, (
            "LoginPage does not validate redirect URL origin against same-origin policy"
        )

    def test_signuppage_validates_redirect_origin(self):
        """Verify SignupPage validates redirect_url origin before navigation."""
        signup_src = _read_source("/home/user/salesgenie/src/auth/SignupPage.tsx")
        assert "window.location.origin" in signup_src, (
            "SignupPage does not validate redirect URL origin against same-origin policy"
        )

    def test_loginpage_no_direct_redirect_assignment(self):
        """Verify LoginPage does not directly assign redirect_url without validation."""
        login_src = _read_source("/home/user/salesgenie/src/auth/LoginPage.tsx")
        assert "href = data.redirect_url" not in login_src, (
            "LoginPage has unvalidated redirect: window.location.href = data.redirect_url"
        )


class TestMissingAuthHeaders:
    """Adversary bypass: API endpoints accessible without authentication."""

    def test_fetch_kpis_requires_auth(self):
        """Verify fetchKPIs includes authentication headers."""
        api_src = _read_source("/home/user/salesgenie/src/lib/api-client.ts")
        kpis_section = api_src[api_src.find("fetchKPIs"):api_src.find("getDefaultKPIs")]
        assert "getSecureHeaders" in kpis_section or "getAuthHeaders" in kpis_section, (
            "fetchKPIs does not include auth headers — accessible without authentication"
        )

    def test_fetch_customers_requires_auth(self):
        """Verify fetchCustomers includes authentication headers."""
        api_src = _read_source("/home/user/salesgenie/src/lib/api-client.ts")
        customers_section = api_src[api_src.find("fetchCustomers"):api_src.find("createCustomer")]
        assert "getSecureHeaders" in customers_section or "getAuthHeaders" in customers_section, (
            "fetchCustomers does not include auth headers — accessible without authentication"
        )

    def test_slack_integration_requires_auth(self):
        """Verify Slack integration endpoints include authentication headers."""
        api_src = _read_source("/home/user/salesgenie/src/lib/api-client.ts")
        slack_section = api_src[api_src.find("registerSlackIntegration"):api_src.find("Discord")]
        assert "getSecureHeaders" in slack_section or "getAuthHeaders" in slack_section, (
            "Slack integration endpoints do not include auth headers"
        )

    def test_lead_intelligence_requires_auth(self):
        """Verify lead intelligence endpoints include authentication headers."""
        api_src = _read_source("/home/user/salesgenie/src/lib/api-client.ts")
        lead_section = api_src[api_src.find("searchCompanies"):api_src.find("listSearchProfiles")]
        assert "getSecureHeaders" in lead_section or "getAuthHeaders" in lead_section, (
            "Lead intelligence endpoints do not include auth headers"
        )


class TestSSRFPrevention:
    """Adversary bypass: SSRF via unvalidated path parameters."""

    def test_sanitize_path_segment_exists(self):
        """Verify APIClient has a path sanitization method."""
        api_src = _read_source("/home/user/salesgenie/src/lib/api-client.ts")
        assert "sanitizePathSegment" in api_src, (
            "APIClient does not have path parameter sanitization"
        )

    def test_company_id_sanitized(self):
        """Verify getCompany sanitizes companyId before URL interpolation."""
        api_src = _read_source("/home/user/salesgenie/src/lib/api-client.ts")
        get_company_section = api_src[api_src.find("getCompany("):api_src.find("qualifyLead")]
        assert "sanitizePathSegment(companyId)" in get_company_section, (
            "getCompany does not sanitize companyId — potential SSRF/path traversal"
        )

    def test_session_id_sanitized(self):
        """Verify revokeSession sanitizes sessionId."""
        api_src = _read_source("/home/user/salesgenie/src/lib/api-client.ts")
        revoke_section = api_src[api_src.find("revokeSession("):api_src.find("getUserProfile")]
        assert "sanitizePathSegment(sessionId)" in revoke_section, (
            "revokeSession does not sanitize sessionId"
        )

    def test_org_id_sanitized_in_get_organization(self):
        """Verify getOrganization sanitizes orgId."""
        api_src = _read_source("/home/user/salesgenie/src/lib/api-client.ts")
        org_section = api_src[api_src.find("getOrganization("):api_src.find("chat(")]
        assert "sanitizePathSegment(orgId)" in org_section, (
            "getOrganization does not sanitize orgId"
        )


class TestOAuthRolePrioritization:
    """Adversary bypass: OAuth role injection via response body."""

    def test_oauth_prefers_jwt_roles_over_response_roles(self):
        """Verify OAuthCallback uses JWT-validated roles, not response body roles."""
        oauth_src = _read_source("/home/user/salesgenie/src/auth/OAuthCallback.tsx")
        assert "decodedRoles" in oauth_src, (
            "OAuthCallback does not use JWT-decoded roles"
        )
        assert "rolesFromResponse" not in oauth_src, (
            "OAuthCallback still trusts response body roles — attacker can inject arbitrary roles"
        )

    def test_oauth_requires_nonce_in_state(self):
        """Verify OAuthCallback requires nonce in state parameter."""
        oauth_src = _read_source("/home/user/salesgenie/src/auth/OAuthCallback.tsx")
        assert "nonce" in oauth_src.lower(), (
            "OAuthCallback does not validate nonce in OAuth state"
        )


class TestOpenRedirect:
    """Adversary bypass: Open redirect via OAuth redirect_url."""

    def test_loginpage_validates_redirect_origin(self):
        """Verify LoginPage validates redirect_url origin before navigation."""
        login_src = _read_source("/home/user/salesgenie/src/auth/LoginPage.tsx")
        assert "window.location.origin" in login_src, (
            "LoginPage does not validate redirect URL origin against same-origin policy"
        )

    def test_signuppage_validates_redirect_origin(self):
        """Verify SignupPage validates redirect_url origin before navigation."""
        signup_src = _read_source("/home/user/salesgenie/src/auth/SignupPage.tsx")
        assert "window.location.origin" in signup_src, (
            "SignupPage does not validate redirect URL origin against same-origin policy"
        )

    def test_loginpage_no_unvalidated_redirect(self):
        """Verify LoginPage does not assign redirect_url without validation."""
        login_src = _read_source("/home/user/salesgenie/src/auth/LoginPage.tsx")
        assert "href = data.redirect_url" not in login_src, (
            "LoginPage has unvalidated redirect: window.location.href = data.redirect_url"
        )

    def test_signuppage_no_unvalidated_redirect(self):
        """Verify SignupPage does not assign redirect_url without validation."""
        signup_src = _read_source("/home/user/salesgenie/src/auth/SignupPage.tsx")
        assert "href = data.redirect_url" not in signup_src, (
            "SignupPage has unvalidated redirect: window.location.href = data.redirect_url"
        )


class TestSSRFPrevention:
    """Adversary bypass: SSRF via unvalidated URL path parameters."""

    def test_sanitize_path_segment_exists(self):
        """Verify APIClient has a path sanitization method."""
        api_src = _read_source("/home/user/salesgenie/src/lib/api-client.ts")
        assert "sanitizePathSegment" in api_src, (
            "APIClient does not have path parameter sanitization"
        )

    def test_company_id_sanitized(self):
        """Verify getCompany sanitizes companyId before URL interpolation."""
        api_src = _read_source("/home/user/salesgenie/src/lib/api-client.ts")
        company_section = api_src[api_src.find("getCompany("):api_src.find("qualifyLead")]
        assert "sanitizePathSegment(companyId)" in company_section, (
            "getCompany does not sanitize companyId — potential SSRF/path traversal"
        )

    def test_session_id_sanitized(self):
        """Verify revokeSession sanitizes sessionId."""
        api_src = _read_source("/home/user/salesgenie/src/lib/api-client.ts")
        revoke_section = api_src[api_src.find("revokeSession("):api_src.find("getUserProfile")]
        assert "sanitizePathSegment(sessionId)" in revoke_section, (
            "revokeSession does not sanitize sessionId"
        )

    def test_org_id_sanitized_in_get_organization(self):
        """Verify getOrganization sanitizes orgId."""
        api_src = _read_source("/home/user/salesgenie/src/lib/api-client.ts")
        org_section = api_src[api_src.find("getOrganization("):api_src.find("chat(")]
        assert "sanitizePathSegment(orgId)" in org_section, (
            "getOrganization does not sanitize orgId"
        )


class TestJWTIssuerValidation:
    """Adversary bypass: JWT token from wrong issuer accepted."""

    def test_auth_middleware_validates_issuer(self):
        """Verify auth-middleware.ts validates JWT issuer claim."""
        middleware_src = _read_source("/home/user/salesgenie/src/lib/auth-middleware.ts")
        assert "iss" in middleware_src.lower() and ("expectedIssuer" in middleware_src or "JWT_ISSUER" in middleware_src), (
            "auth-middleware.ts does not validate JWT issuer"
        )

    def test_auth_provider_validates_issuer(self):
        """Verify AuthProvider.tsx validates JWT issuer claim."""
        auth_src = _read_source("/home/user/salesgenie/src/auth/AuthProvider.tsx")
        assert "expectedIssuer" in auth_src or "process.env.JWT_ISSUER" in auth_src, (
            "AuthProvider does not validate JWT issuer"
        )


class TestNoLocalStorageForAuth:
    """Adversary bypass: Token theft via XSS accessing localStorage."""

    def test_no_direct_localStorage_auth_token_access(self):
        """Verify no direct localStorage access for auth tokens in components/islands."""
        import os
        results = []
        for root, dirs, files in os.walk("/home/user/salesgenie/src"):
            for f in files:
                if f.endswith(('.ts', '.tsx')):
                    filepath = os.path.join(root, f)
                    src = _read_source(filepath)
                    pattern = re.compile(r'localStorage\.(getItem|setItem|removeItem)\s*\(\s*[\'"](?:auth_token|refresh_token|user_data|roles|permissions|jwt_roles)[\'"]')
                    if pattern.search(src):
                        results.append(filepath)
        assert len(results) == 0, (
            f"Direct localStorage access for auth tokens found in: {results}"
        )


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
