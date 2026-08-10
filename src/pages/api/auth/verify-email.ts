import type { APIRoute } from 'astro';
import { checkRateLimit, logAuditEvent, getClientIp } from '../../../lib/auth-middleware';

export const POST: APIRoute = async (context) => {
  if (checkRateLimit(context, 'auth:verify-email', 60 * 1000, 10)) {
    return new Response(JSON.stringify({
      success: false,
      message: 'Too many requests. Please try again later.',
    }), {
      status: 429,
      headers: { 'Content-Type': 'application/json' },
    });
  }

  const clientIp = await getClientIp(context) || 'unknown';

  try {
    const { token } = await context.request.json();

    if (!token || typeof token !== 'string' || token.length > 512) {
      logAuditEvent({
        action: 'email_verification_failed',
        resource_type: 'auth',
        ip_address: clientIp,
        severity: 'low',
        details: { reason: 'invalid_token' },
      });
      return new Response(JSON.stringify({
        success: false,
        message: 'Invalid verification token',
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

    const response = await fetch(`${baseUrl}/api/v1/auth/verify-email`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ token }),
    });

    const data = await response.json().catch(() => ({ success: false, message: 'Verification service unavailable' }));

    if (response.ok) {
      logAuditEvent({
        action: 'email_verification_success',
        resource_type: 'auth',
        ip_address: clientIp,
        severity: 'low',
        details: {},
      });
    } else {
      logAuditEvent({
        action: 'email_verification_failed',
        resource_type: 'auth',
        ip_address: clientIp,
        severity: 'medium',
        details: { reason: 'backend_rejected' },
      });
    }

    return new Response(JSON.stringify(data), {
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
      action: 'email_verification_error',
      resource_type: 'auth',
      ip_address: clientIp,
      severity: 'medium',
      details: { error: 'exception_occurred' },
    });
    return new Response(JSON.stringify({
      success: false,
      message: 'An error occurred during email verification',
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
