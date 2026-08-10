import type { APIRoute } from 'astro';
import { requireAuth, requirePermission, logAuditEvent, getClientIp, validateId } from '../../../../lib/auth-middleware';

export const POST: APIRoute = async (context) => {
  const auth = requireAuth(context);
  if (!auth) {
    return new Response(JSON.stringify({
      success: false,
      message: 'Unauthorized',
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

  if (!requirePermission(context, 'org:switch')) {
    logAuditEvent({
      action: 'org_switch_denied',
      resource_type: 'auth',
      user_id: auth.user.id,
      ip_address: await getClientIp(context) || undefined,
      severity: 'high',
      details: { reason: 'insufficient_permissions' },
    });
    return new Response(JSON.stringify({
      success: false,
      message: 'Forbidden: insufficient permissions to switch organizations',
    }), {
      status: 403,
      headers: {
        'Content-Type': 'application/json',
        'X-Content-Type-Options': 'nosniff',
        'X-Frame-Options': 'DENY',
        'Referrer-Policy': 'no-referrer',
      },
    });
  }

  try {
    const body = await context.request.json();
    const { org_id } = body;

    if (!org_id || typeof org_id !== 'string' || !validateId(org_id)) {
      return new Response(JSON.stringify({
        success: false,
        message: 'Invalid organization ID',
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

    if (org_id === auth.tenant_id) {
      return new Response(JSON.stringify({
        success: true,
        message: 'Already in this organization',
        access_token: '',
        refresh_token: '',
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

    const userTenantCheck = await fetch(
      `${process.env.AUTH_SERVICE_URL || 'http://localhost:8001'}/api/v1/auth/organizations/${encodeURIComponent(org_id)}/users/${encodeURIComponent(auth.user.id)}`,
      {
        headers: {
          Authorization: context.request.headers.get('authorization') || '',
          'Content-Type': 'application/json',
        },
      }
    );

    if (!userTenantCheck.ok) {
      logAuditEvent({
        action: 'org_switch_denied',
        resource_type: 'organization',
        user_id: auth.user.id,
        tenant_id: org_id,
        ip_address: await getClientIp(context) || undefined,
        severity: 'high',
        details: { reason: 'not_member_of_tenant' },
      });
      return new Response(JSON.stringify({
        success: false,
        message: 'You do not have access to the requested organization',
      }), {
        status: 403,
        headers: {
          'Content-Type': 'application/json',
          'X-Content-Type-Options': 'nosniff',
          'X-Frame-Options': 'DENY',
          'Referrer-Policy': 'no-referrer',
        },
      });
    }

    const tokenResponse = await fetch(
      `${process.env.AUTH_SERVICE_URL || 'http://localhost:8001'}/api/v1/auth/tokens/issue`,
      {
        method: 'POST',
        headers: {
          Authorization: context.request.headers.get('authorization') || '',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ tenant_id: org_id }),
      }
    );

    if (!tokenResponse.ok) {
      return new Response(JSON.stringify({
        success: false,
        message: 'Failed to issue new token for tenant',
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

    const tokenData = await tokenResponse.json();

    logAuditEvent({
      action: 'org_switch_success',
      resource_type: 'organization',
      user_id: auth.user.id,
      ip_address: await getClientIp(context) || undefined,
      severity: 'medium',
      details: { from_tenant: auth.tenant_id, to_tenant: org_id },
    });

    const cookieFlags = 'HttpOnly; SameSite=Strict; Path=/' + (process.env.NODE_ENV === 'production' ? '; Secure' : '') + '; Max-Age=3600';
    const refreshCookieFlags = 'HttpOnly; SameSite=Strict; Path=/' + (process.env.NODE_ENV === 'production' ? '; Secure' : '') + '; Max-Age=86400';
    const setCookieHeader = `auth_token=${tokenData.access_token}; ${cookieFlags}, refresh_token=${tokenData.refresh_token}; ${refreshCookieFlags}`;

    return new Response(JSON.stringify({
      success: true,
      access_token: tokenData.access_token,
      refresh_token: tokenData.refresh_token,
    }), {
      status: 200,
      headers: {
        'Content-Type': 'application/json',
        'X-Content-Type-Options': 'nosniff',
        'X-Frame-Options': 'DENY',
        'Referrer-Policy': 'no-referrer',
        'Set-Cookie': setCookieHeader,
      },
    });
  } catch (error) {
    logAuditEvent({
      action: 'org_switch_error',
      resource_type: 'auth',
      user_id: auth.user.id,
      ip_address: await getClientIp(context) || undefined,
      severity: 'medium',
      details: { error: 'exception_occurred' },
    });
    return new Response(JSON.stringify({
      success: false,
      message: 'An error occurred during organization switch',
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
