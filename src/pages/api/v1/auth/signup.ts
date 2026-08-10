export const prerender = false;

import type { APIRoute } from 'astro';
import { isAuthRateLimited, hashPassword, validatePasswordStrength, logAuditEvent, getClientIp } from '../../../../lib/auth-middleware';

const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

const mockUsers: Map<string, { id: string; email: string; full_name: string; company: string; passwordHash: string; created_at: string; verified: boolean; tenant_id: string }> = new Map();

const BASE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_AUTH_SERVICE_PORT || 8001}`
  : "/api";

export const POST: APIRoute = async (context) => {
  if (isAuthRateLimited(context)) {
    return new Response(JSON.stringify({
      success: false,
      message: 'Too many signup attempts. Please try again later.',
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
    const body = await context.request.json();
    const { full_name, email, password, company, agree_terms } = body;

    const clientIp = await getClientIp(context) || 'unknown';

    if (!full_name || typeof full_name !== 'string' || full_name.length < 2) {
      return new Response(JSON.stringify({
        success: false,
        message: 'Invalid input provided',
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    if (!email || typeof email !== 'string' || !emailRegex.test(email)) {
      return new Response(JSON.stringify({
        success: false,
        message: 'Invalid input provided',
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    if (!password || typeof password !== 'string') {
      return new Response(JSON.stringify({
        success: false,
        message: 'Invalid input provided',
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const pwdValidation = validatePasswordStrength(password);
    if (!pwdValidation.valid) {
      return new Response(JSON.stringify({
        success: false,
        message: 'Password does not meet security requirements',
        errors: pwdValidation.errors,
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    if (!company || typeof company !== 'string' || company.length < 2) {
      return new Response(JSON.stringify({
        success: false,
        message: 'Invalid input provided',
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    if (agree_terms !== true) {
      return new Response(JSON.stringify({
        success: false,
        message: 'Terms agreement is required',
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const normalizedEmail = email.toLowerCase().trim();

    if (mockUsers.has(normalizedEmail)) {
      logAuditEvent({
        action: 'signup_failed',
        resource_type: 'auth',
        ip_address: clientIp,
        severity: 'low',
        details: { reason: 'email_exists' },
      });
      return new Response(JSON.stringify({
        success: false,
        message: 'An account with this email already exists. Please login or use a different email.',
        code: 'EMAIL_EXISTS',
      }), {
        status: 409,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const userId = `user_${Date.now()}`;
    const tenant_id = `tenant_${userId}`;
    const passwordHash = await hashPassword(password);

    mockUsers.set(normalizedEmail, {
      id: userId,
      email: normalizedEmail,
      full_name,
      company,
      passwordHash,
      created_at: new Date().toISOString(),
      verified: false,
      tenant_id,
    });

    try {
      const response = await fetch(`${BASE_URL}/api/v1/auth/signup`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          full_name,
          email: normalizedEmail,
          password,
          company,
          agree_terms: true,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        logAuditEvent({
          action: 'signup_failed',
          resource_type: 'auth',
          user_email: normalizedEmail,
          ip_address: clientIp,
          severity: 'medium',
          details: { reason: errorData.detail || 'backend_rejected' },
        });
        return new Response(JSON.stringify({
          success: false,
          message: errorData.detail || 'Signup failed',
        }), {
          status: response.status,
          headers: {
            'Content-Type': 'application/json',
            'X-Content-Type-Options': 'nosniff',
            'X-Frame-Options': 'DENY',
            'Referrer-Policy': 'no-referrer',
          },
        });
      }
    } catch {
    }

    logAuditEvent({
      action: 'signup_success',
      resource_type: 'auth',
      ip_address: clientIp,
      tenant_id,
      severity: 'low',
      details: { method: 'email' },
    });

    return new Response(JSON.stringify({
      success: true,
      message: 'Account created successfully. Please check your email to verify your account. You can now login.',
      user_id: userId,
      tenant_id,
    }), {
      status: 200,
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
      action: 'signup_error',
      resource_type: 'auth',
      ip_address: clientIp,
      severity: 'medium',
      details: { error: error instanceof Error ? error.name : 'unknown' },
    });
    return new Response(JSON.stringify({
      success: false,
      message: 'An error occurred during signup',
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
