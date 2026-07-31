import React, { useState } from 'react';
import { useAuth } from '../auth/AuthProvider';
import type { PlatformRole } from '../lib/types';

export function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [tenantId, setTenantId] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [mfaRequired, setMfaRequired] = useState(false);
  const [mfaCode, setMfaCode] = useState('');
  const [showMfa, setShowMfa] = useState(false);

  const { login } = useAuth();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (showMfa) {
      await handleMfaSubmit(e);
      return;
    }

    setIsSubmitting(true);
    setError(null);

    try {
      const response = await login(email, password, tenantId || undefined);

      if (response.mfa_required) {
        setMfaRequired(true);
        setShowMfa(true);
      }
    } catch (err: any) {
      setError(err.message || 'Login failed. Please check your credentials.');
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleMfaSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitting(true);
    setError(null);

    try {
      await login(email, password, mfaCode);
      window.location.href = '/app/dashboard';
    } catch (err: any) {
      setError(err.message || 'MFA verification failed.');
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleOAuthLogin = (provider: string) => {
    const redirectUri = encodeURIComponent(window.location.origin + '/auth/callback');
    window.location.href = `http://localhost:8001/api/v1/auth/callback/${provider}?code=dev&redirect_uri=${redirectUri}`;
  };

  return (
    <div className="min-h-screen flex items-center justify-center"
      style={{
        background: 'linear-gradient(135deg, #0f1117 0%, #1a1d29 50%, #0f1117 100%)',
        color: 'var(--color-foreground)',
      }}>
      <div className="w-full max-w-md mx-4">
        <div className="text-center mb-8">
          <div className="w-12 h-12 rounded-xl flex items-center justify-center mx-auto mb-4"
            style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>
            SG
          </div>
          <h1 className="text-2xl font-bold">SalesGenie Enterprise</h1>
          <p className="text-sm mt-1" style={{ color: 'var(--color-muted-foreground)' }}>
            AI Customer Support & Sales Platform
          </p>
        </div>

        <div className="rounded-2xl p-8"
          style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          {!showMfa ? (
            <form onSubmit={handleSubmit} className="space-y-5">
              <div>
                <label className="block text-sm font-medium mb-1.5" style={{ color: 'var(--color-foreground)' }}>
                  Email Address
                </label>
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="you@company.com"
                  required
                  disabled={isSubmitting}
                  className="w-full px-4 py-2.5 rounded-xl text-sm outline-none transition-colors"
                  style={{
                    background: 'var(--color-background)',
                    color: 'var(--color-foreground)',
                    border: '1px solid var(--color-border)',
                  }}
                />
              </div>

              <div>
                <label className="block text-sm font-medium mb-1.5" style={{ color: 'var(--color-foreground)' }}>
                  Password
                </label>
                <input
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="••••••••"
                  required
                  disabled={isSubmitting}
                  className="w-full px-4 py-2.5 rounded-xl text-sm outline-none transition-colors"
                  style={{
                    background: 'var(--color-background)',
                    color: 'var(--color-foreground)',
                    border: '1px solid var(--color-border)',
                  }}
                />
              </div>

              <div>
                <label className="block text-sm font-medium mb-1.5" style={{ color: 'var(--color-foreground)' }}>
                  Organization ID <span style={{ color: 'var(--color-muted-foreground)' }}>(optional)</span>
                </label>
                <input
                  type="text"
                  value={tenantId}
                  onChange={(e) => setTenantId(e.target.value)}
                  placeholder="your-org-id"
                  disabled={isSubmitting}
                  className="w-full px-4 py-2.5 rounded-xl text-sm outline-none transition-colors"
                  style={{
                    background: 'var(--color-background)',
                    color: 'var(--color-foreground)',
                    border: '1px solid var(--color-border)',
                  }}
                />
              </div>

              {error && (
                <div className="p-3 rounded-lg text-sm"
                  style={{ background: 'rgba(205,66,63,0.15)', color: '#cd4239', border: '1px solid rgba(205,66,63,0.3)' }}>
                  {error}
                </div>
              )}

              <button
                type="submit"
                disabled={isSubmitting}
                className="w-full py-2.5 rounded-xl font-semibold text-sm transition-all disabled:opacity-60"
                style={{
                  background: 'var(--color-primary)',
                  color: 'var(--color-on-primary)',
                }}
              >
                {isSubmitting ? 'Signing In...' : 'Sign In'}
              </button>
            </form>
          ) : (
            <form onSubmit={handleSubmit} className="space-y-5">
              <div>
                <label className="block text-sm font-medium mb-1.5" style={{ color: 'var(--color-foreground)' }}>
                  Multi-Factor Authentication Code
                </label>
                <p className="text-xs mb-3" style={{ color: 'var(--color-muted-foreground)' }}>
                  Enter the 6-digit code from your authenticator app
                </p>
                <input
                  type="text"
                  value={mfaCode}
                  onChange={(e) => setMfaCode(e.target.value.replace(/\D/g, '').slice(0, 6))}
                  placeholder="000000"
                  maxLength={6}
                  required
                  disabled={isSubmitting}
                  className="w-full px-4 py-2.5 rounded-xl text-sm text-center outline-none transition-colors"
                  style={{
                    background: 'var(--color-background)',
                    color: 'var(--color-foreground)',
                    border: '1px solid var(--color-border)',
                  }}
                />
              </div>

              {error && (
                <div className="p-3 rounded-lg text-sm"
                  style={{ background: 'rgba(205,66,63,0.15)', color: '#cd4239', border: '1px solid rgba(205,66,63,0.3)' }}>
                  {error}
                </div>
              )}

              <button
                type="submit"
                disabled={isSubmitting || mfaCode.length < 6}
                className="w-full py-2.5 rounded-xl font-semibold text-sm transition-all disabled:opacity-60"
                style={{
                  background: 'var(--color-primary)',
                  color: 'var(--color-on-primary)',
                }}
              >
                {isSubmitting ? 'Verifying...' : 'Verify & Sign In'}
              </button>

              <button
                type="button"
                onClick={() => setShowMfa(false)}
                className="w-full py-2.5 rounded-xl font-semibold text-sm transition-colors"
                style={{
                  background: 'transparent',
                  color: 'var(--color-muted-foreground)',
                }}
              >
                ← Back to Login
              </button>
            </form>
          )}

          {!showMfa && (
            <>
              <div className="relative my-6">
                <div className="absolute inset-0 flex items-center" style={{ borderTop: '1px solid var(--color-border)' }} />
                <div className="relative flex justify-center">
                  <span className="px-3 text-xs" style={{ color: 'var(--color-muted-foreground)', background: 'var(--color-card)' }}>
                    Or continue with
                  </span>
                </div>
              </div>

              <div className="grid grid-cols-1 gap-3">
                <button
                  type="button"
                  onClick={() => handleOAuthLogin('google')}
                  className="py-2.5 rounded-xl text-sm font-medium transition-colors flex items-center justify-center gap-2"
                  style={{
                    background: 'var(--color-background)',
                    color: 'var(--color-foreground)',
                    border: '1px solid var(--color-border)',
                  }}
                >
                  <svg className="w-5 h-5" viewBox="0 0 533.98 544.02">
                    <path fill="#4285F4" d="M533.98 278.93c.03-26.53-7.06-52.38-19.61-74.87L359.05 199.67c-5.88-10.83-14.31-20.44-24.82-27.85-14.92-9.27-32.8-14.89-51.64-14.89-39.8 0-72.6 25.76-85.3 60.38-5.72 16.63-5.72 34.21 0 50.84-12.7 34.62-45.5 60.38-85.3 60.38-18.84 0-36.72-5.62-51.64-14.89-10.51-7.41-18.94-17-24.82-27.85L87.03 193.28C74.43 217.77 67.4 243.83 67.4 271.43c0 45.83 18.94 88.21 50.21 120.59 15.73 15.28 34.35 26.23 54.35 33.12 6.36 2.34 12.9 3.55 19.4 3.55 20.45 0 39.8-8.19 54.82-22.31 19.38-17.68 32.52-40.17 36.95-65.83 4.23-24.98 2.38-51.12-5.34-74.87L185.63 278.93c6.36 18.95 23.54 33.25 43.54 33.25 20.45 0 36.95-14.3 38.75-34.25 2.8-2.78 5.63-5.56 8.4-8.34 5.33-5.17 10.63-10.34 15.92-15.51 8.35-8.1 16.47-16.28 24.3-24.51 8.11-8.07 15.81-16.22 24.02-24.23 5.33-5.17 10.63-10.34 15.92-15.51 2.8-2.78 5.63-5.56 8.4-8.34 1.94-1.89 3.89-3.78 5.83-5.67 1.94-1.89 3.89-3.78 5.83-5.67 3.88-3.78 7.77-7.56 11.65-11.34 8.35-8.1 16.47-16.28 24.3-24.51 5.33-5.17 10.63-10.34 15.92-15.51 8.11-8.07 15.81-16.22 24.02-24.23 5.33-5.17 10.63-10.34 15.92-15.51 2.8-2.78 5.63-5.56 8.4-8.34 1.94-1.89 3.89-3.78 5.83-5.67 1.94-1.89 3.89-3.78 5.83-5.67 3.88-3.78 7.77-7.56 11.65-11.34L441.7 108.43c1.94 1.89 3.89 3.78 5.83 5.67 8.11 8.07 15.81 16.22 24.02 24.23 8.11 8.07 16.19 16.16 24.3 24.51 5.33 5.17 10.63 10.34 15.92 15.51 8.35 8.1 16.47 16.28 24.3 24.51 8.11 8.07 15.81 16.22 24.02 24.23 5.33 5.17 10.63 10.34 15.92 15.51 2.8 2.78 5.63 5.56 8.4 8.34 1.94 1.89 3.89 3.78 5.83 5.67 1.94 1.89 3.89 3.78 5.83 5.67 3.88 3.78 7.77 7.56 11.65 11.34l161.86 161.86c3.17 3.17 6.02 6.51 8.5 9.91L533.98 278.93z"/>
                    <path fill="#DB4437" d="M432 161.86C417.33 151.01 400.88 145.61 383.18 145.61c-30.89 0-56.68 20.02-66.5 47.57-3.8 11.59-3.8 23.98 0 35.58-9.82 27.55-35.61 47.57-66.5 47.57-19.88 0-38.28-7.52-52.08-20.18-6.88-6.07-12.58-12.91-17.92-20.51-1.83-2.64-3.48-5.43-5.04-8.22-3.2-5.66-6.3-11.31-9.37-16.95-5.58-9.82-11.67-19.27-18.28-28.16L383.18 145.61c2.53 3.55 5.43 6.81 8.5 9.91L432 161.86z"/>
                    <path fill="#F4B400" d="M276 377.97c26.48 0 49.02-9.77 66.82-26.35-3.17-3.17-6.51-6.51-9.91-9.91L276 318.19c-3.17 3.17-6.51 6.51-9.91 9.91 17.8 16.58 40.34 26.35 66.82 26.35m-66.82-80.36c-17.66 0-32.52-12.4-36.28-29.06-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67L120.25 193.28c-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67L43.82 193.28c-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67L43.82 193.28c-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67L43.82 193.28c-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67L43.82 193.28c-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67L43.82 193.28c-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67L43.82 193.28c-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67L43.82 193.28c-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67L43.82 193.28c-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67L43.82 193.28c-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67L43.82 193.28c-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67L43.82 193.28c-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67L43.82 193.28c-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67L43.82 193.28c-3.17 1.89-6.51 3.78-9.91 5.67-3.17 1.89-6.51 3.78-9.91 5.67z"/>
                    <path fill="#34A853" d="M120.25 193.28c11.45-11.45 25.12-17.75 39.82-17.75 13.25 0 24.82 4.9 33.95 13.05 10.32 9.65 16.47 22.88 17.3 35.91-1.08 5.78-3.32 11.45-6.64 16.52-5.59 8.38-12.92 15.21-21.67 20.35-7.75 4.94-16.28 8.59-25.36 10.93L120.25 193.28z"/>
                  </svg>
                  Continue with Google
                </button>
              </div>
            </>
          )}
        </div>

        <div className="mt-6 text-center">
          <p className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
            Don't have an account?{' '}
            <a href="#" className="font-medium" style={{ color: 'var(--color-primary)' }}>
              Contact your administrator
            </a>
          </p>
        </div>
      </div>
    </div>
  );
}
