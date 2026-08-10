import { useEffect, useState } from 'react';
import { derivePermissions } from './AuthProvider';
import type { PlatformRole } from '../lib/types';
import { AUTH_SERVICE_URL } from '../lib/api-client';
import { secureTokenStorage } from '../lib/secure-storage';

const VALID_ROLES: PlatformRole[] = [
  'super_admin', 'workspace_admin', 'org_admin',
  'sales_manager', 'sales_agent',
  'support_manager', 'support_agent',
  'knowledge_manager', 'auditor', 'end_user'
];

const CSRF_STATE_KEY = 'oauth_csrf_state';

export default function OAuthCallback() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const handleOAuthCallback = async () => {
      try {
        const params = new URLSearchParams(window.location.search);
        const code = params.get('code');
        const state = params.get('state');
        const error = params.get('error');

        if (error) {
          setError('Authentication was denied or failed. Please try again.');
          setLoading(false);
          return;
        }

        if (!code) {
          setError('No authorization code found in URL');
          setLoading(false);
          return;
        }

         const expectedState = secureTokenStorage.getItem(CSRF_STATE_KEY as any);
         secureTokenStorage.removeItem(CSRF_STATE_KEY as any);

         if (!state) {
           setError('Invalid OAuth state: state parameter missing');
           setLoading(false);
           return;
         }

         const providedState = decodeURIComponent(state);
         const stateMatch = expectedState && providedState === expectedState;
         if (!stateMatch) {
          setError('Invalid OAuth state: state mismatch detected');
          setLoading(false);
          return;
        }

        let provider = 'google';
        if (providedState) {
          try {
            const decodedState = JSON.parse(atob(providedState));
            if (decodedState && typeof decodedState === 'object' && typeof decodedState.provider === 'string') {
              const allowedProviders = ['google', 'github', 'microsoft', 'slack', 'auth0'];
              if (allowedProviders.includes(decodedState.provider) && decodedState.nonce) {
                provider = decodedState.provider;
              } else {
                setError('Invalid OAuth provider in state');
                setLoading(false);
                return;
              }
            }
          } catch {
            setError('Invalid OAuth state encoding');
            setLoading(false);
            return;
          }
        }

        const response = await fetch(`${AUTH_SERVICE_URL}/api/v1/auth/callback/${encodeURIComponent(provider)}?code=${encodeURIComponent(code)}&state=${encodeURIComponent(providedState)}`, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
          credentials: 'same-origin',
        });

        const data = await response.json().catch(() => ({}));

        if (!response.ok) {
          const detail = typeof data.detail === 'string' ? data.detail : 'OAuth callback failed';
          throw new Error(detail);
        }

        if (data.mock) {
          setError('OAuth is not configured for this environment. Please use the regular login form.');
          setLoading(false);
          return;
        }

        const accessToken = data.access_token;
        const refreshToken = data.refresh_token || '';
        const jwtPayload = accessToken.split('.');
        let decodedRoles: string[] = [];
        let decodedTenantId: string | undefined;
        let decodedEmail: string | undefined;
        let decodedSub: string | undefined;
        let decodedFullName: string | undefined;
        let decodedAvatar: string | undefined;

        if (jwtPayload.length === 3) {
          try {
            const header = JSON.parse(Buffer.from(jwtPayload[0], 'base64url').toString());
            if (!['HS256', 'HS384', 'HS512', 'RS256', 'RS384', 'RS512'].includes(header.alg)) {
              throw new Error('Invalid JWT algorithm');
            }
            const payload: Record<string, unknown> = JSON.parse(Buffer.from(jwtPayload[1], 'base64url').toString());

            if (!(payload.sub && typeof payload.sub === 'string')) {
              throw new Error('Invalid token: missing sub');
            }
            if (payload.exp && (typeof payload.exp !== 'number' || Number.isNaN(payload.exp))) {
              throw new Error('Invalid token: invalid exp');
            }
            const now = Math.floor(Date.now() / 1000);
            const expNum = typeof payload.exp === 'number' ? payload.exp : undefined;
            if (expNum && expNum < now) {
              throw new Error('Token expired');
            }
            const aud = payload.aud;
            if (aud !== undefined) {
              const audValid = Array.isArray(aud)
                ? aud.includes(window.location.origin)
                : aud === window.location.origin;
              if (!audValid) {
                throw new Error('Invalid token audience');
              }
            }

            decodedRoles = Array.isArray(payload.roles) ? payload.roles.map(String) : [];
            decodedTenantId = typeof payload.tenant_id === 'string' ? payload.tenant_id : undefined;
            decodedEmail = typeof payload.email === 'string' ? payload.email : undefined;
            decodedSub = typeof payload.sub === 'string' ? payload.sub : undefined;
            decodedFullName = typeof payload.full_name === 'string' ? payload.full_name : undefined;
            decodedAvatar = typeof payload.avatar_url === 'string' ? payload.avatar_url : undefined;
          } catch {
            throw new Error('Invalid token format');
          }
        } else {
          throw new Error('Invalid token format');
        }

         const isProduction = process.env.NODE_ENV === 'production';
         if (!isProduction) {
           secureTokenStorage.setItem('auth_token', accessToken);
           secureTokenStorage.setItem('refresh_token', refreshToken);
         }
         secureTokenStorage.setItem('oauth_provider', provider);

         let roles: PlatformRole[] = [];
         if (decodedRoles.length > 0) {
           roles = decodedRoles as PlatformRole[];
         } else if (Array.isArray(data.roles)) {
           roles = data.roles.map((r: unknown) => String(r)) as PlatformRole[];
         }

         roles = roles.map((r: string) => {
           if (VALID_ROLES.includes(r as PlatformRole)) {
             return r as PlatformRole;
           }
           return 'end_user';
         });

        if (roles.length === 0) {
          roles = ['end_user'];
        }

        secureTokenStorage.setItem('roles', JSON.stringify(roles));

        const permissions = derivePermissions(roles);
        secureTokenStorage.setItem('permissions', JSON.stringify(permissions));

        const user = {
          id: decodedSub || `oauth_${provider}_${Date.now()}`,
          email: decodedEmail || (data.email || `${provider}_user@salesgenie.local`),
          full_name: decodedFullName || null,
          avatar_url: decodedAvatar || null,
          tenant_id: decodedTenantId || 'default_tenant',
          created_at: new Date().toISOString(),
        };

        secureTokenStorage.setItem('user_data', JSON.stringify(user));

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
