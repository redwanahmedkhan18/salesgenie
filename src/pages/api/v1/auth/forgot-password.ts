import type { APIRoute } from 'astro';
import { checkRateLimit, logAuditEvent, getClientIp } from '../../../../lib/auth-middleware';

const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export const POST: APIRoute = async (context) => {
  if (checkRateLimit(context, 'auth:forgot', 60 * 1000, 3)) {
    return new Response(JSON.stringify({
      success: false,
      message: 'Too many requests. Please try again later.',
    }), {
      status: 429,
      headers: {
        'Content-Type': 'application/json',
        'Retry-After': '60',
      },
    });
  }

  try {
    const { email } = await context.request.json();
    const clientIp = await getClientIp(context) || 'unknown';

    if (!email || typeof email !== 'string' || !emailRegex.test(email)) {
      return new Response(JSON.stringify({
        success: false,
        message: 'Invalid request',
      }), {
        status: 400,
        headers: {
          'Content-Type': 'application/json',
          'X-Content-Type-Options': 'nosniff',
          'X-Frame-Options': 'DENY',
          'Referrer-Policy': 'no-referrer',
        },
      });
    }

    const baseUrl = import.meta.env.DEV
      ? `http://localhost:${import.meta.env.PUBLIC_AUTH_SERVICE_PORT || 8001}`
      : '/api';

    const response = await fetch(`${baseUrl}/api/v1/auth/forgot-password`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email }),
    });

    await response.json().catch(() => ({}));

    logAuditEvent({
      action: 'password_reset_requested',
      resource_type: 'auth',
      ip_address: clientIp,
      severity: 'low',
      details: { email_provided: true },
    });

    return new Response(JSON.stringify({
      success: true,
      message: 'If an account with that email exists, a reset link has been sent',
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
    logAuditEvent({
      action: 'forgot_password_error',
      resource_type: 'auth',
      severity: 'medium',
      details: { error: 'request_failed' },
    });
    return new Response(JSON.stringify({
      success: true,
      message: 'If an account with that email exists, a reset link has been sent',
    }), {
      status: 200,
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
