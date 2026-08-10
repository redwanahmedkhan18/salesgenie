import type { APIRoute } from 'astro';
import { checkRateLimit, logAuditEvent, getClientIp, validatePasswordStrength } from '../../../../lib/auth-middleware';

export const POST: APIRoute = async (context) => {
  if (checkRateLimit(context, 'auth:reset', 60 * 1000, 5)) {
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

  const clientIp = await getClientIp(context) || 'unknown';

  try {
    const { token, new_password, confirm_password } = await context.request.json();

    if (!token || !new_password || !confirm_password) {
      logAuditEvent({
        action: 'password_reset_failed',
        resource_type: 'auth',
        ip_address: clientIp,
        severity: 'low',
        details: { reason: 'missing_fields' },
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

    if (new_password !== confirm_password) {
      logAuditEvent({
        action: 'password_reset_failed',
        resource_type: 'auth',
        ip_address: clientIp,
        severity: 'low',
        details: { reason: 'password_mismatch' },
      });
      return new Response(JSON.stringify({
        success: false,
        message: 'Passwords do not match',
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

    const pwdValidation = validatePasswordStrength(new_password);
    if (!pwdValidation.valid) {
      return new Response(JSON.stringify({
        success: false,
        message: 'Password does not meet security requirements',
        errors: pwdValidation.errors,
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

    if (token.length > 512) {
      logAuditEvent({
        action: 'password_reset_failed',
        resource_type: 'auth',
        ip_address: clientIp,
        severity: 'low',
        details: { reason: 'token_too_large' },
      });
      return new Response(JSON.stringify({
        success: false,
        message: 'Invalid or expired reset token',
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

    const response = await fetch(`${baseUrl}/api/v1/auth/reset-password`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ token, new_password, confirm_password }),
    });

    const data = await response.json().catch(() => ({}));

    if (response.ok) {
      logAuditEvent({
        action: 'password_reset_success',
        resource_type: 'auth',
        ip_address: clientIp,
        severity: 'medium',
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
    logAuditEvent({
      action: 'password_reset_error',
      resource_type: 'auth',
      ip_address: clientIp,
      severity: 'medium',
      details: { error: 'reset_failed' },
    });
    return new Response(JSON.stringify({
      success: false,
      message: 'An error occurred during password reset',
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
