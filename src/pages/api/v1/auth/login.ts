import type { APIRoute } from 'astro';
import { checkRateLimit, logAuditEvent, getClientIp } from '../../../../lib/auth-middleware';

const BASE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_AUTH_SERVICE_PORT || 8001}`
  : '/api';

const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export const POST: APIRoute = async (context) => {
  if (checkRateLimit(context, 'auth:login', 15 * 60 * 1000, 5)) {
    const clientIp = await getClientIp(context) || 'unknown';
    logAuditEvent({
      action: 'rate_limit_exceeded',
      resource_type: 'auth',
      ip_address: clientIp,
      severity: 'medium',
      details: { endpoint: 'login', reason: 'too_many_attempts' },
    });
    return new Response(JSON.stringify({
      success: false,
      message: 'Too many login attempts. Please try again later.',
      code: 'RATE_LIMITED',
    }), {
      status: 429,
      headers: {
        'Content-Type': 'application/json',
        'Retry-After': '900',
      },
    });
  }

  try {
    const rawBody = await context.request.text();
    const body = rawBody ? JSON.parse(rawBody) : {};
    const { email, password, mfa_code } = body;

    const clientIp = await getClientIp(context) || 'unknown';

    if (!email || typeof email !== 'string' || !emailRegex.test(email)) {
      logAuditEvent({
        action: 'login_failed',
        resource_type: 'auth',
        ip_address: clientIp,
        severity: 'low',
        details: { reason: 'invalid_email_format' },
      });
      return new Response(JSON.stringify({
        success: false,
        message: 'Invalid credentials',
      }), {
        status: 401,
        headers: {
          'Content-Type': 'application/json',
          'X-Content-Type-Options': 'nosniff',
          'X-Frame-Options': 'DENY',
          'Referrer-Policy': 'no-referrer',
        },
      });
    }

    if (!password || typeof password !== 'string') {
      logAuditEvent({
        action: 'login_failed',
        resource_type: 'auth',
        ip_address: clientIp,
        severity: 'low',
        details: { reason: 'missing_password' },
      });
      return new Response(JSON.stringify({
        success: false,
        message: 'Invalid credentials',
      }), {
        status: 401,
        headers: {
          'Content-Type': 'application/json',
          'X-Content-Type-Options': 'nosniff',
          'X-Frame-Options': 'DENY',
          'Referrer-Policy': 'no-referrer',
        },
      });
    }

    const normalizedEmail = email.toLowerCase().trim();
    const constantTimeDelay = () => new Promise(r => setTimeout(r, 200 + Math.random() * 300));

    let authSuccess = false;

    try {
      const response = await fetch(`${BASE_URL}/api/v1/auth/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: normalizedEmail, password, mfa_code }),
      });

      const data = await response.json();

      if (response.ok) {
        logAuditEvent({
          action: 'login_success',
          resource_type: 'auth',
          user_email: normalizedEmail,
          ip_address: clientIp,
          tenant_id: data.tenant_id,
          severity: 'low',
          details: { method: 'password' },
        });

        const cookieFlags = 'HttpOnly; SameSite=Strict; Path=/' + (process.env.NODE_ENV === 'production' ? '; Secure' : '') + '; Max-Age=3600';
        const refreshCookieFlags = 'HttpOnly; SameSite=Strict; Path=/' + (process.env.NODE_ENV === 'production' ? '; Secure' : '') + '; Max-Age=86400';
        const setCookieHeader = `auth_token=${data.access_token}; ${cookieFlags}, refresh_token=${data.refresh_token}; ${refreshCookieFlags}`;

        return new Response(JSON.stringify(data), {
          status: 200,
          headers: {
            'Content-Type': 'application/json',
            'X-Content-Type-Options': 'nosniff',
            'X-Frame-Options': 'DENY',
            'Referrer-Policy': 'no-referrer',
            'Set-Cookie': setCookieHeader,
          },
        });
      }

      logAuditEvent({
        action: 'login_failed',
        resource_type: 'auth',
        user_email: normalizedEmail,
        ip_address: clientIp,
        severity: 'medium',
        details: { reason: data.detail || 'backend_rejected' },
      });

      return new Response(JSON.stringify(data), {
        status: response.status,
        headers: {
          'Content-Type': 'application/json',
          'X-Content-Type-Options': 'nosniff',
          'X-Frame-Options': 'DENY',
          'Referrer-Policy': 'no-referrer',
        },
      });
    } catch {
      await constantTimeDelay();
      logAuditEvent({
        action: 'login_failed',
        resource_type: 'auth',
        user_email: normalizedEmail,
        ip_address: clientIp,
        severity: 'low',
        details: { reason: 'user_not_found' },
      });
    }

    logAuditEvent({
      action: 'login_failed',
      resource_type: 'auth',
      ip_address: clientIp,
      severity: 'medium',
      details: { reason: 'invalid_credentials' },
    });

    return new Response(JSON.stringify({
      success: false,
      message: 'Invalid credentials',
    }), {
      status: 401,
      headers: {
        'Content-Type': 'application/json',
        'X-Content-Type-Options': 'nosniff',
        'X-Frame-Options': 'DENY',
        'Referrer-Policy': 'no-referrer',
      },
    });
  } catch (error) {
    const clientIp = await getClientIp(context) || 'unknown';
    logAuditEvent({
      action: 'login_error',
      resource_type: 'auth',
      ip_address: clientIp,
      severity: 'medium',
      details: { error: error instanceof Error ? error.name : 'unknown' },
    });
    return new Response(JSON.stringify({
      success: false,
      message: 'An error occurred during authentication',
    }), {
      status: 500,
      headers: {
        'Content-Type': 'application/json',
        'X-Content-Type-Options': 'nosniff',
        'X-Frame-Options': 'DENY',
        'Referrer-Policy': 'no-referrer',
      },
    });
  }
};

export const GET: APIRoute = async () => {
  return new Response(JSON.stringify({
    success: false,
    message: 'Method not allowed',
  }), {
    status: 405,
    headers: {
      'Content-Type': 'application/json',
      'X-Content-Type-Options': 'nosniff',
      'X-Frame-Options': 'DENY',
      'Referrer-Policy': 'no-referrer',
    },
  });
};
