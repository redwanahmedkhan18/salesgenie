export const prerender = false;

import type { APIRoute } from 'astro';
import { checkRateLimit, logAuditEvent, getClientIp, validateId } from '../../../../lib/auth-middleware';

export const GET: APIRoute = async (context) => {
  if (checkRateLimit(context, 'auth:reset-token', 60 * 1000, 10)) {
    return new Response(JSON.stringify({
      valid: false,
      detail: 'Too many requests. Please try again later.',
    }), {
      status: 429,
      headers: { 'Content-Type': 'application/json' },
    });
  }

  const clientIp = await getClientIp(context) || 'unknown';

  try {
    const token = context.url.pathname.split('/').pop() || '';

    if (!token || !validateId(token)) {
      logAuditEvent({
        action: 'reset_token_validation_failed',
        resource_type: 'auth',
        ip_address: clientIp,
        severity: 'low',
        details: { reason: 'invalid_token_format' },
      });
      return new Response(JSON.stringify({
        valid: false,
        detail: 'Invalid token',
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

    const response = await fetch('/api/v1/auth/reset-token/' + encodeURIComponent(token), {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
    });

    const data = await response.json().catch(() => ({ success: false, message: 'Token validation failed' }));

    if (!response.ok) {
      logAuditEvent({
        action: 'reset_token_validation_failed',
        resource_type: 'auth',
        ip_address: clientIp,
        severity: 'medium',
        details: { reason: 'backend_rejected' },
      });
      return new Response(JSON.stringify({
        valid: false,
        detail: 'Invalid or expired reset token',
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

    logAuditEvent({
      action: 'reset_token_validation_success',
      resource_type: 'auth',
      ip_address: clientIp,
      severity: 'low',
      details: {},
    });

    return new Response(JSON.stringify({
      valid: true,
      email: data.email || null,
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
      action: 'reset_token_validation_error',
      resource_type: 'auth',
      ip_address: clientIp,
      severity: 'medium',
      details: { error: 'exception_occurred' },
    });
    return new Response(JSON.stringify({
      valid: false,
      detail: 'An error occurred during token validation',
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
