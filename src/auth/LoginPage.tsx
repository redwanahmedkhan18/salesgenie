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

              <div className="grid grid-cols-3 gap-3">
                <button
                  type="button"
                  onClick={() => handleOAuthLogin('google')}
                  className="py-2.5 rounded-xl text-sm font-medium transition-colors"
                  style={{
                    background: 'var(--color-background)',
                    color: 'var(--color-foreground)',
                    border: '1px solid var(--color-border)',
                  }}
                >
                  Google
                </button>
                <button
                  type="button"
                  onClick={() => handleOAuthLogin('microsoft')}
                  className="py-2.5 rounded-xl text-sm font-medium transition-colors"
                  style={{
                    background: 'var(--color-background)',
                    color: 'var(--color-foreground)',
                    border: '1px solid var(--color-border)',
                  }}
                >
                  Microsoft
                </button>
                <button
                  type="button"
                  onClick={() => handleOAuthLogin('github')}
                  className="py-2.5 rounded-xl text-sm font-medium transition-colors"
                  style={{
                    background: 'var(--color-background)',
                    color: 'var(--color-foreground)',
                    border: '1px solid var(--color-border)',
                  }}
                >
                  GitHub
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
