import type { APIRoute } from 'astro';
import { logAuditEvent, getClientIp } from '../../../../lib/auth-middleware';

export const POST: APIRoute = async (context) => {
  const clientIp = await getClientIp(context) || 'unknown';
  logAuditEvent({
    action: 'logout',
    resource_type: 'auth',
    ip_address: clientIp,
    severity: 'low',
    details: {},
  });

  const cookieFlags = 'HttpOnly; SameSite=Strict; Path=/' + (process.env.NODE_ENV === 'production' ? '; Secure' : '') + '; Max-Age=0';
  const setCookieHeader = `auth_token=; ${cookieFlags}, refresh_token=; ${cookieFlags}`;

  return new Response(JSON.stringify({
    success: true,
    message: 'Logged out successfully',
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
