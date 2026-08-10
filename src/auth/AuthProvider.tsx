import { createContext, useContext, useReducer, useEffect, type ReactNode } from 'react';
import { apiClient } from '../lib/api-client';
import { secureTokenStorage, clearAuth } from '../lib/secure-storage';
import type { User, Session, PlatformRole, LoginResponse } from '../lib/types';

const JWT_ALGORITHMS = ['HS256', 'HS384', 'HS512', 'RS256', 'RS384', 'RS512'];
const MAX_TOKEN_AGE = 24 * 60 * 60;
const MAX_TOKEN_LENGTH = 4096;

interface AuthState {
  user: User | null;
  session: Session | null;
  roles: PlatformRole[];
  permissions: string[];
  isLoading: boolean;
  isAuthenticated: boolean;
}

interface AuthContextType extends AuthState {
  login: (email: string, password: string, mfaCode?: string) => Promise<LoginResponse>;
  logout: () => void;
  refreshSession: () => Promise<void>;
  hasPermission: (permission: string) => boolean;
  hasRole: (role: PlatformRole) => boolean;
  hasAnyRole: (roles: PlatformRole[]) => boolean;
  switchOrganization: (orgId: string) => Promise<void>;
  forgotPassword: (email: string) => Promise<{ success: boolean; message: string; token?: string }>;
  resetPassword: (token: string, newPassword: string, confirmPassword: string) => Promise<{ success: boolean; message: string }>;
  validateResetToken: (token: string) => Promise<{ valid: boolean; email?: string; error?: string }>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

type AuthAction =
  | { type: 'SET_LOADING' }
  | { type: 'SET_NOT_LOADING' }
  | { type: 'SET_AUTH'; payload: { user: User; session: Session; roles: PlatformRole[]; permissions: string[] } }
  | { type: 'SET_MFA_REQUIRED'; payload: { user_id: string; tenant_id: string } }
  | { type: 'LOGOUT' }
  | { type: 'AUTH_ERROR' };

function authReducer(state: AuthState, action: AuthAction): AuthState {
  switch (action.type) {
    case 'SET_LOADING':
      return { ...state, isLoading: true };
    case 'SET_NOT_LOADING':
      return { ...state, isLoading: false };
    case 'SET_AUTH':
      return {
        ...state,
        user: action.payload.user,
        session: action.payload.session,
        roles: action.payload.roles,
        permissions: action.payload.permissions,
        isLoading: false,
        isAuthenticated: true,
      };
    case 'LOGOUT':
      return {
        user: null,
        session: null,
        roles: [],
        permissions: [],
        isLoading: false,
        isAuthenticated: false,
      };
    case 'AUTH_ERROR':
      return {
        user: null,
        session: null,
        roles: [],
        permissions: [],
        isLoading: false,
        isAuthenticated: false,
      };
    default:
      return state;
  }
}

interface JwtPayload {
  sub: string;
  email?: string;
  roles?: PlatformRole[];
  tenant_id?: string;
  exp?: number;
  iat?: number;
  aud?: string | string[];
  iss?: string;
}

function decodeJWT(token: string): { sub: string; email?: string; roles?: PlatformRole[]; tenant_id?: string; exp?: number; valid: boolean } {
  try {
    if (!token || token.length > MAX_TOKEN_LENGTH) {
      return { sub: '', roles: [], tenant_id: 'default_tenant', valid: false };
    }
    const parts = token.split('.');
    if (parts.length !== 3) {
      return { sub: '', roles: [], tenant_id: 'default_tenant', valid: false };
    }

    const parseBase64Url = (str: string): string => {
      if (typeof Buffer !== 'undefined') {
        return Buffer.from(str, 'base64url').toString('utf-8');
      }
      let base64 = str.replace(/-/g, '+').replace(/_/g, '/');
      while (base64.length % 4 !== 0) base64 += '=';
      return atob(base64);
    };

    const header = JSON.parse(parseBase64Url(parts[0]));
    if (!JWT_ALGORITHMS.includes(header.alg) || header.alg === 'none' || header.alg === 'None') {
      return { sub: '', roles: [], tenant_id: 'default_tenant', valid: false };
    }

    const payload: JwtPayload = JSON.parse(parseBase64Url(parts[1]));

    if (typeof payload.sub !== 'string' || !payload.sub) {
      return { sub: '', roles: [], tenant_id: 'default_tenant', valid: false };
    }

    if (payload.exp !== undefined && (typeof payload.exp !== 'number' || isNaN(payload.exp))) {
      return { sub: '', roles: [], tenant_id: 'default_tenant', valid: false };
    }

    if (payload.iat !== undefined && (typeof payload.iat !== 'number' || isNaN(payload.iat))) {
      return { sub: '', roles: [], tenant_id: 'default_tenant', valid: false };
    }

    if (payload.exp !== undefined) {
      const now = Math.floor(Date.now() / 1000);
      if (payload.exp <= now) {
        return { sub: '', roles: [], tenant_id: 'default_tenant', valid: false };
      }
    }

    const audCheck = (aud: string | string[] | undefined): boolean => {
      if (!aud) return true;
      if (Array.isArray(aud)) return aud.includes(window.location.origin);
      return aud === window.location.origin;
    };
    if (!audCheck(payload.aud)) {
      return { sub: '', roles: [], tenant_id: 'default_tenant', valid: false };
    }

    if (payload.iat !== undefined && payload.exp !== undefined) {
      const age = payload.exp - payload.iat;
      if (age <= 0 || age > MAX_TOKEN_AGE) {
        return { sub: '', roles: [], tenant_id: 'default_tenant', valid: false };
      }
    }

    const expectedIssuer = import.meta.env.PUBLIC_JWT_ISSUER || process.env.JWT_ISSUER || 'salesgenie';
    if (payload.iss !== undefined && payload.iss !== expectedIssuer) {
      return { sub: '', roles: [], tenant_id: 'default_tenant', valid: false };
    }

    return {
      sub: payload.sub,
      email: payload.email,
      roles: Array.isArray(payload.roles) ? payload.roles as PlatformRole[] : [],
      tenant_id: typeof payload.tenant_id === 'string' ? payload.tenant_id : 'default_tenant',
      exp: payload.exp,
      valid: true,
    };
  } catch (error) {
    console.error('JWT decoding/validation failed:', error);
    return { sub: '', roles: [], tenant_id: 'default_tenant', valid: false };
  }
}

export function AuthProvider({ children }: { children: ReactNode }) {
  const [state, dispatch] = useReducer(authReducer, {
    user: null,
    session: null,
    roles: [],
    permissions: [],
    isLoading: true,
    isAuthenticated: false,
  });

  useEffect(() => {
    initializeAuth();
  }, []);

  const initializeAuth = async () => {
    dispatch({ type: 'SET_LOADING' });
    try {
      const token = secureTokenStorage.getItem('auth_token');
      const refreshToken = secureTokenStorage.getItem('refresh_token');

       if (token) {
        const decoded = decodeJWT(token);
        const now = Math.floor(Date.now() / 1000);
        const isTokenValid = decoded.exp ? decoded.exp > now : true;
        const isRefreshTokenValid = !!refreshToken;

        if (!decoded.valid || (!isTokenValid && !isRefreshTokenValid)) {
          clearAuth();
          dispatch({ type: 'LOGOUT' });
          return;
        }

        if (isTokenValid || isRefreshTokenValid) {
          const userData = secureTokenStorage.getItem('user_data');
          let user: User | null = null;
          if (userData) {
            try {
              user = JSON.parse(userData);
            } catch {
              user = null;
            }
          }

           if (!user) {
             try {
               user = await apiClient.getUserProfile();
               secureTokenStorage.setItem('user_data', JSON.stringify(user));
             } catch {
              user = {
                id: decoded.sub,
                email: decoded.email || '',
                full_name: null,
                avatar_url: null,
                tenant_id: decoded.tenant_id || 'default_tenant',
                created_at: new Date().toISOString(),
              };
            }
          }

          let roles: PlatformRole[] = (decoded.roles || []) as PlatformRole[];
          if (roles.length === 0) {
            const storedRoles = secureTokenStorage.getItem('roles');
            if (storedRoles) {
              try {
                roles = JSON.parse(storedRoles) as PlatformRole[];
              } catch {}
            }
          }

          if (roles.length === 0) {
            roles = ['end_user'];
          }

          const permissions = derivePermissions(roles);
          secureTokenStorage.setItem('roles', JSON.stringify(roles));
          secureTokenStorage.setItem('permissions', JSON.stringify(permissions));

          if (decoded.roles) {
            secureTokenStorage.setItem('jwt_roles', JSON.stringify(decoded.roles));
          }

          dispatch({
            type: 'SET_AUTH',
            payload: {
              user,
              session: {
                token,
                refreshToken: refreshToken || '',
                expiresAt: (decoded.exp || now + 3600) * 1000,
                user,
                roles,
                permissions,
              },
              roles,
              permissions,
            },
          });
        } else {
          dispatch({ type: 'LOGOUT' });
        }
      } else if (refreshToken) {
        await refreshSession();
      } else {
        dispatch({ type: 'LOGOUT' });
      }
    } catch (error) {
      console.error('Auth initialization error:', error);
      dispatch({ type: 'AUTH_ERROR' });
    } finally {
      dispatch({ type: 'SET_NOT_LOADING' });
    }
  };

  const login = async (email: string, password: string, mfaCode?: string): Promise<LoginResponse> => {
    dispatch({ type: 'SET_LOADING' });
    try {
      const response = await apiClient.login({ email, password, mfa_code: mfaCode });

       if (response.mfa_required) {
         return response;
       }

        const decoded = decodeJWT(response.access_token);
        if (!decoded.valid) {
          dispatch({ type: 'AUTH_ERROR' });
          throw new Error('Invalid authentication token received');
        }
       const roles = response.roles as PlatformRole[];
       const permissions = derivePermissions(roles);

       const user: User = {
         id: response.user_id,
         email,
         full_name: null,
         avatar_url: null,
         tenant_id: response.tenant_id,
         created_at: new Date().toISOString(),
       };

       const isProduction = process.env.NODE_ENV === 'production';
       if (!isProduction) {
         secureTokenStorage.setItem('auth_token', response.access_token);
         secureTokenStorage.setItem('refresh_token', response.refresh_token);
       }
       secureTokenStorage.setItem('user_data', JSON.stringify(user));
       secureTokenStorage.setItem('roles', JSON.stringify(roles));
       secureTokenStorage.setItem('permissions', JSON.stringify(permissions));

       dispatch({
         type: 'SET_AUTH',
         payload: {
           user,
           session: {
             token: response.access_token,
             refreshToken: response.refresh_token,
             expiresAt: Date.now() + response.expires_in * 1000,
             user,
             roles,
             permissions,
           },
           roles,
           permissions,
         },
       });

       return response;
    } catch (error) {
      dispatch({ type: 'AUTH_ERROR' });
      throw error;
    }
  };

  const refreshSession = async (): Promise<void> => {
    try {
      const refreshToken = secureTokenStorage.getItem('refresh_token');
      if (!refreshToken) {
        dispatch({ type: 'LOGOUT' });
        return;
      }

      const response = await apiClient.refresh(refreshToken);

      const decoded = decodeJWT(response.access_token);
      if (!decoded.valid) {
        clearAuth();
        dispatch({ type: 'LOGOUT' });
        return;
      }
      const roles = response.roles as PlatformRole[];
      const permissions = derivePermissions(roles);

      const userData = secureTokenStorage.getItem('user_data');
      let user: User | null = null;
      if (userData) {
        user = JSON.parse(userData);
      }

      if (!user) {
        user = {
          id: response.user_id,
          email: '',
          full_name: null,
          avatar_url: null,
          tenant_id: response.tenant_id,
          created_at: new Date().toISOString(),
        };
      }

      secureTokenStorage.setItem('auth_token', response.access_token);
      secureTokenStorage.setItem('roles', JSON.stringify(roles));
      secureTokenStorage.setItem('permissions', JSON.stringify(permissions));

      const isProduction = process.env.NODE_ENV === 'production';
      if (!isProduction) {
        secureTokenStorage.setItem('refresh_token', response.refresh_token);
      }

      dispatch({
        type: 'SET_AUTH',
        payload: {
          user,
          session: {
            token: response.access_token,
            refreshToken: response.refresh_token,
            expiresAt: Date.now() + response.expires_in * 1000,
            user,
            roles,
            permissions,
          },
          roles,
          permissions,
        },
      });
    } catch (error) {
      console.error('Token refresh failed:', error);
      dispatch({ type: 'LOGOUT' });
    }
  };

  const logout = async () => {
    try {
      await fetch('/api/v1/auth/logout', { method: 'POST' });
    } catch {
    }
    clearAuth();
    dispatch({ type: 'LOGOUT' });
  };

  const hasPermission = (permission: string): boolean => {
    return state.permissions.includes(permission);
  };

  const hasRole = (role: PlatformRole): boolean => {
    return state.roles.includes(role);
  };

  const hasAnyRole = (roles: PlatformRole[]): boolean => {
    return state.roles.some(r => roles.includes(r));
  };

  const switchOrganization = async (orgId: string) => {
    if (!orgId || typeof orgId !== 'string' || orgId.length > 128 || !/^[a-zA-Z0-9_-]+$/.test(orgId)) {
      throw new Error('Invalid organization ID format');
    }
    try {
      const response = await fetch('/api/v1/auth/switch-organization', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ org_id: orgId }),
      });

      if (!response.ok) {
        const error = await response.text().catch(() => 'Unknown error');
        throw new Error(error);
      }

      const data = await response.json();
      const decoded = decodeJWT(data.access_token);

      if (!decoded.valid || decoded.tenant_id !== orgId) {
        throw new Error('Server rejected organization switch');
      }

      const roles = decoded.roles as PlatformRole[] || state.roles;
      const permissions = derivePermissions(roles);

      const isProduction = process.env.NODE_ENV === 'production';
      if (!isProduction) {
        secureTokenStorage.setItem('auth_token', data.access_token);
        secureTokenStorage.setItem('refresh_token', data.refresh_token);
      }
      secureTokenStorage.setItem('roles', JSON.stringify(roles));
      secureTokenStorage.setItem('permissions', JSON.stringify(permissions));

      if (state.session) {
        const updatedSession: Session = {
          ...state.session,
          token: data.access_token,
          refreshToken: data.refresh_token,
          user: { ...state.session.user, tenant_id: orgId },
        };
        dispatch({
          type: 'SET_AUTH',
          payload: {
            user: updatedSession.user,
            session: updatedSession,
            roles,
            permissions,
          },
        });
      }
    } catch (error) {
      console.error('Organization switch failed:', error);
      throw error;
    }
  };

  const forgotPassword = async (email: string): Promise<{ success: boolean; message: string; token?: string }> => {
    dispatch({ type: 'SET_LOADING' });
    try {
      const response = await apiClient.forgotPassword(email);
      dispatch({ type: 'SET_NOT_LOADING' });
      return response;
    } catch (error) {
      dispatch({ type: 'SET_NOT_LOADING' });
      throw error;
    }
  };

  const validateResetToken = async (token: string): Promise<{ valid: boolean; email?: string; error?: string }> => {
    dispatch({ type: 'SET_LOADING' });
    try {
      const response = await apiClient.getResetToken(token);
      dispatch({ type: 'SET_NOT_LOADING' });
      return { valid: true, email: response.email };
    } catch (error: any) {
      dispatch({ type: 'SET_NOT_LOADING' });
      return { valid: false, error: error.message || 'Invalid or expired reset token' };
    }
  };

  const resetPassword = async (token: string, newPassword: string, confirmPassword: string): Promise<{ success: boolean; message: string }> => {
    dispatch({ type: 'SET_LOADING' });
    try {
      const response = await apiClient.resetPassword({
        token,
        new_password: newPassword,
        confirm_password: confirmPassword,
      });
      dispatch({ type: 'SET_NOT_LOADING' });
      return response;
    } catch (error) {
      dispatch({ type: 'SET_NOT_LOADING' });
      throw error;
    }
  };

  const value: AuthContextType = {
    ...state,
    login,
    logout,
    refreshSession,
    hasPermission,
    hasRole,
    hasAnyRole,
    switchOrganization,
    forgotPassword,
    resetPassword,
    validateResetToken,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function derivePermissions(roles: PlatformRole[]): string[] {
  const permissions: string[] = [];

  const rolePermissions: Record<string, string[]> = {
    super_admin: ['*'],
    workspace_admin: ['org:read', 'org:write', 'user:read', 'user:write', 'user:invite', 'agent:read', 'agent:write', 'agent:execute', 'knowledge:read', 'knowledge:write', 'leads:read', 'leads:write', 'ticket:read', 'ticket:write', 'analytics:read', 'workflow:manage', 'billing:read'],
    org_admin: ['org:read', 'user:read', 'user:write', 'user:invite', 'agent:read', 'agent:execute', 'knowledge:read', 'leads:read', 'leads:write', 'ticket:read', 'ticket:write', 'analytics:read', 'workflow:manage'],
    sales_manager: ['leads:read', 'leads:write', 'deals:manage', 'analytics:read', 'agent:execute'],
    sales_agent: ['leads:read', 'leads:write', 'agent:execute', 'knowledge:read'],
    support_manager: ['ticket:read', 'ticket:write', 'ticket:assign', 'analytics:read', 'agent:execute', 'knowledge:read', 'knowledge:write'],
    support_agent: ['ticket:read', 'ticket:write', 'agent:execute', 'knowledge:read'],
    knowledge_manager: ['knowledge:read', 'knowledge:write', 'knowledge:delete', 'prompt:manage', 'agent:read'],
    auditor: ['system:audit:read', 'org:read', 'user:read', 'analytics:read', 'billing:read'],
    end_user: ['agent:execute', 'knowledge:read', 'ticket:read', 'ticket:write'],
  };

  for (const role of roles) {
    const perms = rolePermissions[role];
    if (perms) {
      permissions.push(...perms);
    }
  }

  return [...new Set(permissions)];
}

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    if (typeof window === 'undefined') {
      return {
        user: null,
        session: null,
        roles: [],
        permissions: [] as string[],
        isLoading: false,
        isAuthenticated: false,
        login: async () => ({ access_token: '', refresh_token: '', expires_in: 0, user_id: '', tenant_id: '', roles: [], mfa_required: false } as any),
        logout: () => {},
        refreshSession: async () => {},
        hasPermission: () => false,
        hasRole: () => false,
        hasAnyRole: () => false,
        switchOrganization: () => {},
        forgotPassword: async () => ({ success: false, message: '' }),
        resetPassword: async () => ({ success: false, message: '' }),
        validateResetToken: async () => ({ valid: false }),
      };
    }
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};
