import type { APIRoute } from 'astro';
import { checkRateLimit, logAuditEvent, getClientIp } from '../../../../lib/auth-middleware';

export const POST: APIRoute = async (context) => {
  if (checkRateLimit(context, 'auth:refresh', 60 * 1000, 10)) {
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
    const { refresh_token } = await context.request.json();

    const clientIp = await getClientIp(context) || 'unknown';

    if (!refresh_token || typeof refresh_token !== 'string' || refresh_token.length > 4096) {
      logAuditEvent({
        action: 'refresh_failed',
        resource_type: 'auth',
        ip_address: clientIp,
        severity: 'low',
        details: { reason: 'missing_or_invalid_token' },
      });
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

    const response = await fetch(`${baseUrl}/api/v1/auth/refresh`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ refresh_token }),
    });

    const data = await response.json();

    if (response.ok) {
      logAuditEvent({
        action: 'token_refresh_success',
        resource_type: 'auth',
        ip_address: clientIp,
        severity: 'low',
        details: {},
      });
    }

    return new Response(JSON.stringify(data), {
      status: response.ok ? 200 : response.status,
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
      action: 'refresh_error',
      resource_type: 'auth',
      ip_address: clientIp,
      severity: 'medium',
      details: { error: 'refresh_failed' },
    });
    return new Response(JSON.stringify({
      success: false,
      message: 'An error occurred during token refresh',
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
