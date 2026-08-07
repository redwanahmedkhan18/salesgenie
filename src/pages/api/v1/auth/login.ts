import type { APIRoute } from 'astro';

const BASE_URL = import.meta.env.DEV
  ? `http://localhost:${import.meta.env.PUBLIC_AUTH_SERVICE_PORT || 8001}`
  : '/api';

const mockUsers: Record<string, { id: string; email: string; passwordHash: string; } | undefined> = {};

const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function hashPassword(password: string): string {
  let hash = 0;
  const salt = 'salesgenie_salt_2026';
  const combined = salt + password + salt;
  for (let i = 0; i < combined.length; i++) {
    const char = combined.charCodeAt(i);
    hash = ((hash << 5) - hash) + char;
    hash = hash & hash;
  }
  return `sb_${hash.toString(36)}_${salt}`;
}

export const POST: APIRoute = async ({ request }) => {
  try {
    const body = await request.json();

    const { email, password, mfa_code } = body;

    if (!email || typeof email !== 'string' || !emailRegex.test(email)) {
      return new Response(JSON.stringify({
        success: false,
        message: 'Invalid email address',
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    if (!password || typeof password !== 'string') {
      return new Response(JSON.stringify({
        success: false,
        message: 'Password is required',
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const normalizedEmail = email.toLowerCase().trim();

    const user = mockUsers[normalizedEmail];

    if (user) {
      const isValidPassword = hashPassword(password) === user.passwordHash;

      if (!isValidPassword) {
        return new Response(JSON.stringify({
          success: false,
          message: 'Invalid email or password',
          code: 'INVALID_CREDENTIALS',
        }), {
          status: 401,
          headers: { 'Content-Type': 'application/json' },
        });
      }
    }

    const bodyPayload: Record<string, unknown> = {
      email: body.email,
      password: body.password,
    };
    if (mfa_code) bodyPayload.mfa_code = mfa_code;

    try {
      const response = await fetch(`${BASE_URL}/api/v1/auth/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(bodyPayload),
      });

      const data = await response.json();

      return new Response(JSON.stringify(data), {
        status: response.ok ? 200 : response.status,
        headers: { 'Content-Type': 'application/json' },
      });
    } catch {
      return new Response(JSON.stringify({
        success: false,
        message: 'Authentication service unavailable. Please try again later.'
      }), {
        status: 503,
        headers: { 'Content-Type': 'application/json' },
      });
    }
  } catch (error) {
    return new Response(JSON.stringify({
      success: false,
      message: 'Server error during login'
    }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
};

export const GET: APIRoute = async () => {
  return new Response(JSON.stringify({
    success: false,
    message: 'Method not allowed'
  }), {
    status: 405,
    headers: { 'Content-Type': 'application/json' },
  });
};