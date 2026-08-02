import React, { createContext, useContext, useReducer, useEffect, type ReactNode } from 'react';
import { apiClient } from '../lib/api-client';
import type { User, Session, PlatformRole, LoginRequest, LoginResponse } from '../lib/types';

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
  switchOrganization: (orgId: string) => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

type AuthAction =
  | { type: 'SET_LOADING' }
  | { type: 'SET_AUTH'; payload: { user: User; session: Session; roles: PlatformRole[]; permissions: string[] } }
  | { type: 'SET_MFA_REQUIRED'; payload: { user_id: string; tenant_id: string } }
  | { type: 'LOGOUT' }
  | { type: 'AUTH_ERROR' };

function authReducer(state: AuthState, action: AuthAction): AuthState {
  switch (action.type) {
    case 'SET_LOADING':
      return { ...state, isLoading: true };
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

function decodeJWT(token: string): { sub: string; email?: string; roles?: PlatformRole[]; tenant_id?: string; exp?: number } {
  try {
    const payload = JSON.parse(atob(token.split('.')[1]));
    return payload;
  } catch {
    return { sub: '', roles: [], tenant_id: 'default_tenant' };
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
      const token = localStorage.getItem('auth_token');
      const refreshToken = localStorage.getItem('refresh_token');

      if (token) {
        const decoded = decodeJWT(token);
        const now = Math.floor(Date.now() / 1000);

        if (decoded.exp && decoded.exp > now) {
          const userData = localStorage.getItem('user_data');
          let user: User | null = null;
          if (userData) {
            user = JSON.parse(userData);
          }

          if (!user) {
            try {
              user = await apiClient.getUserProfile();
              localStorage.setItem('user_data', JSON.stringify(user));
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

          const roles = (decoded.roles || []) as PlatformRole[];
          const permissions = derivePermissions(roles);

          dispatch({
            type: 'SET_AUTH',
            payload: {
              user,
              session: {
                token,
                refreshToken: refreshToken || '',
                expiresAt: (decoded.exp || 0) * 1000,
                user,
                roles,
                permissions,
              },
              roles,
              permissions,
            },
          });
        } else if (refreshToken) {
          await refreshSession();
        } else {
          dispatch({ type: 'LOGOUT' });
        }
      } else {
        dispatch({ type: 'LOGOUT' });
      }
    } catch (error) {
      console.error('Auth initialization error:', error);
      dispatch({ type: 'AUTH_ERROR' });
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

      localStorage.setItem('auth_token', response.access_token);
      localStorage.setItem('refresh_token', response.refresh_token);
      localStorage.setItem('user_data', JSON.stringify(user));

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
      const refreshToken = localStorage.getItem('refresh_token');
      if (!refreshToken) {
        dispatch({ type: 'LOGOUT' });
        return;
      }

      const response = await apiClient.refresh(refreshToken);

      const decoded = decodeJWT(response.access_token);
      const roles = response.roles as PlatformRole[];
      const permissions = derivePermissions(roles);

      const userData = localStorage.getItem('user_data');
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

      localStorage.setItem('auth_token', response.access_token);

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

  const logout = () => {
    localStorage.removeItem('auth_token');
    localStorage.removeItem('refresh_token');
    localStorage.removeItem('user_data');
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

  const switchOrganization = (orgId: string) => {
    if (state.session) {
      const updatedSession: Session = {
        ...state.session,
        user: { ...state.session.user, tenant_id: orgId },
      };
      dispatch({
        type: 'SET_AUTH',
        payload: {
          user: updatedSession.user,
          session: updatedSession,
          roles: state.roles,
          permissions: state.permissions,
        },
      });
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
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

function derivePermissions(roles: PlatformRole[]): string[] {
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
        permissions: [],
        isLoading: true,
        isAuthenticated: false,
        login: async () => ({ access_token: '', refresh_token: '', expires_in: 0, user_id: '', tenant_id: '', roles: [], mfa_required: false } as any),
        logout: () => {},
        refreshSession: async () => {},
        hasPermission: () => false,
        hasRole: () => false,
        hasAnyRole: () => false,
        switchOrganization: () => {},
      };
    }
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};
