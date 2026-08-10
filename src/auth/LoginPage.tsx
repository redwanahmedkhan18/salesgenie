import React, { useState } from 'react';
import { useAuth } from './AuthProvider';
import { AUTH_SERVICE_URL } from '../lib/api-client';
import { secureTokenStorage } from '../lib/secure-storage';

export function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [tenantId, setTenantId] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
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
         setShowMfa(true);
       } else {
        window.location.href = '/app/dashboard';
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

  const handleOAuthLogin = async () => {
    try {
      const nonce = crypto.randomUUID();
      const stateData = { provider: 'google', timestamp: Date.now(), signup: false, nonce };
      const state = btoa(JSON.stringify(stateData));
      secureTokenStorage.setItem('oauth_csrf_state' as any, state);
      const response = await fetch(`${AUTH_SERVICE_URL}/api/v1/auth/redirect/google?state=${encodeURIComponent(state)}`);
      const data = await response.json();
      if (data.redirect_url) {
        const redirectUrl = new URL(data.redirect_url, window.location.origin);
        if (redirectUrl.origin === window.location.origin) {
          window.location.href = redirectUrl.href;
        } else {
          setError('Invalid redirect URL. Possible phishing attempt detected.');
        }
      } else if (data.mock) {
        setError(data.message || 'OAuth not configured. Please use the regular login form.');
      }
    } catch (err) {
      console.error('OAuth redirect failed:', err);
      setError('Unable to connect to authentication service. Please try again.');
    }
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

              <div className="relative my-6">
                <div className="absolute inset-0 flex items-center" style={{ borderTop: '1px solid var(--color-border)' }} />
                <div className="relative flex justify-center">
                  <span className="px-3 text-xs" style={{ color: 'var(--color-muted-foreground)', background: 'var(--color-card)' }}>
                    Or continue with
                  </span>
                </div>
              </div>

              <button
                type="button"
                onClick={handleOAuthLogin}
                className="w-full py-2.5 rounded-xl text-sm font-medium transition-colors flex items-center justify-center gap-2"
                style={{
                  background: 'var(--color-background)',
                  color: 'var(--color-foreground)',
                  border: '1px solid var(--color-border)',
                }}
              >
                <svg className="w-5 h-5" viewBox="0 0 532 544">
                  <path fill="#4285F4" d="M532 274.9c0-18.5-1.5-36.3-4.5-53.3-12.3-55.7-60.3-95.5-117.6-95.5C232.6 126 186.2 165.4 151.2 211.7c-3.2 4.7-5.8 9.8-7.8 14.9l-61.8-15.3C85.5 185.7 39.7 225.8 27.5 281.7c-18.4 85.1 11.4 172.3 76.5 211.8 30.2 17.1 65.4 29.9 103.8 29.9 49.9 0 97.2-20.5 132.1-54.3 30.6-28.4 50.7-63.7 56.6-103.5 5.3-32.2-5.5-61.3-24.6-84.3z"/>
                </svg>
                Continue with Google
              </button>

              <button
                type="button"
                onClick={() => window.location.href = '/forgot-password'}
                className="text-xs underline text-amber-400 hover:text-amber-300 transition-colors"
                style={{ color: '#f7a501' }}>
                Forgot Password?
              </button>

              <button
                type="button"
                onClick={() => window.location.href = '/signup'}
                className="w-full py-2.5 rounded-xl text-sm font-medium transition-colors"
                style={{
                  background: 'transparent',
                  color: 'var(--color-muted-foreground)',
                }}
              >
                Create Account
              </button>
            </form>
          ) : (
            <form onSubmit={handleSubmit} className="space-y-5">
              <div>
                <label className="block text-sm font-medium mb-1.5" style={{ color: 'var(--color-foreground)' }}>
                  MFA Code
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
        </div>
      </div>
    </div>
  );
}