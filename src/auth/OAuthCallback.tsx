import React, { useEffect, useState } from 'react';

export default function OAuthCallback() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  
  useEffect(() => {
    const handleOAuthCallback = async () => {
      try {
        const params = new URLSearchParams(window.location.search);
        const code = params.get('code');
        const state = params.get('state');
        
        let provider = 'google';
        if (state) {
          try {
            const decodedState = JSON.parse(atob(state));
            provider = decodedState.provider || provider;
          } catch {}
        }
        
        if (!code) {
          setError('No authorization code found in URL');
          setLoading(false);
          return;
        }
        
        const response = await fetch(`http://localhost:8001/api/v1/auth/callback/${provider}?code=${code}${state ? `&state=${encodeURIComponent(state)}` : ''}`, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
        });
        
        if (!response.ok) {
          const errorText = await response.text();
          try {
            const errorData = JSON.parse(errorText);
            throw new Error(errorData.detail || 'OAuth callback failed');
          } catch {
            throw new Error(errorText || 'OAuth callback failed');
          }
        }
        
        const data = await response.json();
        
        localStorage.setItem('auth_token', data.access_token);
        localStorage.setItem('oauth_provider', provider);
        
        try {
          const tokenPayload = atob(data.access_token.split('.')[1]);
          const payload = JSON.parse(tokenPayload);
          const user = {
            id: payload.sub,
            email: payload.email || `${payload.sub}@${provider}.com`,
            full_name: payload.full_name || null,
            avatar_url: payload.avatar_url || null,
            tenant_id: payload.tenant_id || 'default_tenant',
            created_at: new Date().toISOString(),
          };
          localStorage.setItem('user_data', JSON.stringify(user));
        } catch (e) {
          localStorage.setItem('user_data', JSON.stringify({
            id: `oauth_${provider}_${Date.now()}`,
            email: `user@${provider}.com`,
            full_name: null,
            avatar_url: null,
            tenant_id: 'oauth_tenant',
            created_at: new Date().toISOString(),
          }));
        }
        
        window.location.href = '/app/dashboard';
        
      } catch (err: any) {
        console.error('OAuth callback error:', err);
        setError(err.message || 'Authentication failed');
        setLoading(false);
      }
    };
    
    handleOAuthCallback();
  }, []);
  
  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center"
        style={{
          background: 'linear-gradient(135deg, #0f1117 0%, #1a1d29 50%, #0f1117 100%)',
        }}>
        <div className="text-center">
          <div className="w-12 h-12 mx-auto mb-4 rounded-xl flex items-center justify-center animate-spin"
            style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>
            SG
          </div>
          <h2 className="text-xl font-bold" style={{ color: 'var(--color-foreground)' }}>
            Authenticating...
          </h2>
          <p className="text-sm mt-2" style={{ color: 'var(--color-muted-foreground)' }}>
            Please wait while we complete your sign-in
          </p>
        </div>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className="min-h-screen flex items-center justify-center"
        style={{
          background: 'linear-gradient(135deg, #0f1117 0%, #1a1d29 50%, #0f1117 100%)',
        }}>
        <div className="rounded-2xl p-6 max-w-md"
          style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <div className="text-center mb-4">
            <div className="w-12 h-12 mx-auto rounded-full flex items-center justify-center mb-2"
              style={{ background: 'rgba(205,66,63,0.2)', color: '#cd4239' }}>
              !
            </div>
            <h2 className="text-lg font-bold" style={{ color: 'var(--color-foreground)' }}>
              Authentication Error
            </h2>
          </div>
          <p className="text-sm mb-4" style={{ color: 'var(--color-muted-foreground)' }}>
            {error}
          </p>
          <a href="/login" className="block text-center py-2 rounded-xl font-medium text-sm"
            style={{
              background: 'var(--color-primary)',
              color: 'var(--color-on-primary)',
            }}>
            Try Again
          </a>
        </div>
      </div>
    );
  }
  
  return null;
}