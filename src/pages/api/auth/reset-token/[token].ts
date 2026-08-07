import type { APIRoute } from 'astro';

export const GET: APIRoute = async ({ url }) => {
  try {
    const token = url.pathname.split('/').pop() || '';
    
    const response = await fetch('/api/v1/auth/reset-token/' + token, {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
    });
    
    const data = await response.json().catch(() => ({ success: false, message: 'Token validation failed' }));
    
    if (!response.ok) {
      return new Response(JSON.stringify({ 
        valid: false, 
        detail: data.detail || 'Invalid or expired reset token' 
      }), {
        status: response.status,
        headers: { 'Content-Type': 'application/json' },
      });
    }
    
    return new Response(JSON.stringify({ 
      valid: true, 
      email: data.email || null 
    }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (error) {
    return new Response(JSON.stringify({ 
      valid: false, 
      detail: 'Server error during token validation' 
    }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
};