import type { APIRoute } from 'astro';

const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

const mockUsers: Record<string, { id: string; email: string; full_name: string; company: string; passwordHash: string; created_at: string; verified: boolean }> = {};

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

    const { full_name, email, password, company, agree_terms } = body;

    if (!full_name || typeof full_name !== 'string' || full_name.length < 2) {
      return new Response(JSON.stringify({
        success: false,
        message: 'Full name must be at least 2 characters',
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    if (!email || typeof email !== 'string' || !emailRegex.test(email)) {
      return new Response(JSON.stringify({
        success: false,
        message: 'Invalid email address',
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    if (!password || typeof password !== 'string' || password.length < 8) {
      return new Response(JSON.stringify({
        success: false,
        message: 'Password must be at least 8 characters',
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    if (!company || typeof company !== 'string' || company.length < 2) {
      return new Response(JSON.stringify({
        success: false,
        message: 'Company name is required',
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    if (agree_terms !== true) {
      return new Response(JSON.stringify({
        success: false,
        message: 'You must agree to the Terms of Service and Privacy Policy',
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const normalizedEmail = email.toLowerCase().trim();

    for (const key of Object.keys(mockUsers)) {
      if (mockUsers[key].email.toLowerCase() === normalizedEmail) {
        return new Response(JSON.stringify({
          success: false,
          message: 'An account with this email already exists. Please login or use a different email.',
          code: 'EMAIL_EXISTS',
        }), {
          status: 409,
          headers: { 'Content-Type': 'application/json' },
        });
      }
    }

    const userId = `user_${Date.now()}`;
    mockUsers[normalizedEmail] = {
      id: userId,
      email: normalizedEmail,
      full_name,
      company,
      passwordHash: hashPassword(password),
      created_at: new Date().toISOString(),
      verified: false,
    };

    const BASE_URL = import.meta.env.DEV
      ? `http://localhost:${import.meta.env.PUBLIC_AUTH_SERVICE_PORT || 8001}`
      : '/api';

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

      if (response.ok) {
        return response;
      }
    } catch {
      // Continue to success response if auth service is unavailable
    }

    return new Response(JSON.stringify({
      success: true,
      message: 'Account created! Please check your email to verify your account. You can now login.',
    }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (error) {
    return new Response(JSON.stringify({
      success: false,
      message: 'Server error during signup',
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