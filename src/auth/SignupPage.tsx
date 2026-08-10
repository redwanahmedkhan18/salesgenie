import React, { useState } from 'react';
import { AUTH_SERVICE_URL } from '../lib/api-client';
import { secureTokenStorage } from '../lib/secure-storage';

export function SignupPage() {
  const [formData, setFormData] = useState({
    full_name: '',
    email: '',
    password: '',
    confirm_password: '',
    company: '',
    agree_terms: false,
  });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);
  const [verificationSent, setVerificationSent] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (formData.password !== formData.confirm_password) {
      setError('Passwords do not match');
      return;
    }

    if (!formData.agree_terms) {
      setError('You must agree to the Terms of Service and Privacy Policy');
      return;
    }

    setIsSubmitting(true);
    setError(null);
    setSuccess(null);

    try {
      const response = await fetch(`${AUTH_SERVICE_URL}/api/v1/auth/signup`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          full_name: formData.full_name,
          email: formData.email,
          password: formData.password,
          company: formData.company,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || 'Signup failed');
      }

      setVerificationSent(true);
      setSuccess('Account created! Please check your email to verify your account. You can now login.');
    } catch (err: any) {
      setError(err.message || 'Signup failed. Please try again.');
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleOAuthLogin = async () => {
    try {
      const nonce = crypto.randomUUID();
      const stateData = { provider: 'google', timestamp: Date.now(), signup: true, nonce };
      const state = btoa(JSON.stringify(stateData));
      secureTokenStorage.setItem('oauth_csrf_state' as any, state);
      const response = await fetch(`${AUTH_SERVICE_URL}/api/v1/auth/redirect/google?state=${encodeURIComponent(state)}`);
      const data = await response.json();
      if (data.redirect_url) {
        try {
          const redirectUrl = new URL(data.redirect_url, window.location.origin);
          if (redirectUrl.origin === window.location.origin) {
            window.location.href = redirectUrl.href;
          } else {
            setError('Invalid redirect URL. Possible phishing attempt detected.');
          }
        } catch {
          setError('Invalid redirect URL received from authentication service.');
        }
      } else if (data.mock) {
        setError(data.message || 'OAuth not configured. Please use the regular login form.');
      }
    } catch (err) {
      console.error('OAuth redirect failed:', err);
      setError('Unable to connect to authentication service. Please try again.');
    }
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
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
          <h1 className="text-2xl font-bold">Create Account</h1>
          <p className="text-sm mt-1" style={{ color: 'var(--color-muted-foreground)' }}>
            Join SalesGenie Enterprise
          </p>
        </div>

        <div className="rounded-2xl p-8"
          style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <form onSubmit={handleSubmit} className="space-y-5">
            {!verificationSent ? (
              <>
                <div>
                  <label className="block text-sm font-medium mb-1.5" style={{ color: 'var(--color-foreground)' }}>
                    Full Name
                  </label>
                  <input
                    type="text"
                    name="full_name"
                    value={formData.full_name}
                    onChange={handleChange}
                    placeholder="John Doe"
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
                    Work Email
                  </label>
                  <input
                    type="email"
                    name="email"
                    value={formData.email}
                    onChange={handleChange}
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
                    name="password"
                    value={formData.password}
                    onChange={handleChange}
                    placeholder="••••••••"
                    required
                    disabled={isSubmitting}
                    minLength={8}
                    className="w-full px-4 py-2.5rounded-xl text-sm outline-none transition-colors"
                    style={{
                      background: 'var(--color-background)',
                      color: 'var(--color-foreground)',
                      border: '1px solid var(--color-border)',
                    }}
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium mb-1.5" style={{ color: 'var(--color-foreground)' }}>
                    Confirm Password
                  </label>
                  <input
                    type="password"
                    name="confirm_password"
                    value={formData.confirm_password}
                    onChange={handleChange}
                    placeholder="••••••••"
                    required
                    disabled={isSubmitting}
                    minLength={8}
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
                    Company
                  </label>
                  <input
                    type="text"
                    name="company"
                    value={formData.company}
                    onChange={handleChange}
                    placeholder="Company Name"
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

                <div className="flex items-start gap-3">
                  <div className="flex items-center h-5">
                    <input
                      type="checkbox"
                      checked={formData.agree_terms}
                      onChange={(e) => setFormData({ ...formData, agree_terms: e.target.checked })}
                      className="h-4 w-4 rounded border border-color-border focus:ring-color-primary focus:ring-color-primary"
                      style={{
                        borderColor: 'var(--color-border)',
                        backgroundColor: formData.agree_terms ? 'var(--color-primary)' : 'transparent',
                      }}
                    />
                  </div>
                  <div className="text-sm">
                    <span style={{ color: 'var(--color-foreground)' }}>
                      I agree to the{' '}
                    </span>
                    <a
                      href="/terms"
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-color-primary hover:underline font-medium"
                      style={{ color: 'var(--color-primary)' }}
                    >
                      Terms of Service
                    </a>
                    <span style={{ color: 'var(--color-foreground)' }}> and </span>
                    <a
                      href="/privacy"
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-color-primary hover:underline font-medium"
                      style={{ color: 'var(--color-primary)' }}
                    >
                      Privacy Policy
                    </a>
                  </div>
                </div>

                <button
                  type="submit"
                  disabled={isSubmitting}
                  className="w-full py-2.5 rounded-xl font-semibold text-sm transition-all disabled:opacity-60"
                  style={{
                    background: 'var(--color-primary)',
                    color: 'var(--color-on-primary)',
                  }}
                >
                  {isSubmitting ? 'Creating Account...' : 'Create Account'}
                </button>
              </>
            ) : (
              <div className="text-center p-4"
                style={{ background: 'rgba(66,183,207,0.1)', border: '1px solid rgba(66,183,207,0.3)' }}>
                <p className="text-sm" style={{ color: 'var(--color-foreground)' }}>
                  {success}
                </p>
                <button
                  type="button"
                  onClick={() => window.location.href = '/login'}
                  className="mt-4 py-2 rounded-xl text-sm font-medium transition-colors"
                  style={{
                    background: 'var(--color-primary)',
                    color: 'var(--color-on-primary)',
                  }}
                >
                  Go to Login
                </button>
              </div>
            )}
          </form>

          {!verificationSent && (
            <>
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
                onClick={() => window.location.href = '/login'}
                className="w-full py-2.5 rounded-xl text-sm font-medium transition-colors"
                style={{
                  background: 'transparent',
                  color: 'var(--color-muted-foreground)',
                }}
              >
                Already have an account? Sign In
              </button>
            </>
          )}
        </div>
      </div>
    </div>
  );
}