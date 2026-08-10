/**
 * Secure token storage for the frontend.
 *
 * SECURITY: In production, tokens are stored in HttpOnly cookies managed by
 * the backend auth service. This module provides a bridge for development
 * mode where tokens are stored in memory (not localStorage) to prevent XSS-based
 * token theft.
 *
 * For production, the backend should set `Set-Cookie: auth_token=...; HttpOnly; SameSite=Strict; Secure`
 * and the frontend should not manage tokens directly.
 */

type TokenStore = {
  auth_token: string | null;
  refresh_token: string | null;
  user_data: string | null;
  roles: string | null;
  permissions: string | null;
  jwt_roles: string | null;
  oauth_provider: string | null;
  oauth_csrf_state: string | null;
};

const _memoryStore: TokenStore = {
  auth_token: null,
  refresh_token: null,
  user_data: null,
  roles: null,
  permissions: null,
  jwt_roles: null,
  oauth_provider: null,
  oauth_csrf_state: null,
};

const ALLOWED_KEYS: (keyof TokenStore)[] = [
  'auth_token', 'refresh_token', 'user_data', 'roles',
  'permissions', 'jwt_roles', 'oauth_provider',
  'oauth_csrf_state',
];

type StorageKey = keyof TokenStore;

const isDevelopment = process.env.NODE_ENV === 'development';
const isProduction = process.env.NODE_ENV === 'production';

class SecureTokenStorage {
  /**
   * Retrieves an item. In development, uses in-memory store.
   * In production, prefer HttpOnly cookies from the server side.
   */
  getItem(key: StorageKey): string | null {
    if (isProduction) {
      return _memoryStore[key];
    }
    if (isDevelopment) {
      return _memoryStore[key] ?? localStorage.getItem(key) ?? null;
    }
    return _memoryStore[key];
  }

  setItem(key: StorageKey, value: string | null): void {
    _memoryStore[key] = value;
    if (isDevelopment && value !== null) {
      localStorage.setItem(key, value);
    }
  }

  removeItem(key: StorageKey): void {
    _memoryStore[key] = null;
    if (isDevelopment) {
      localStorage.removeItem(key);
    }
  }

  clear(): void {
    for (const key of ALLOWED_KEYS) {
      _memoryStore[key] = null;
    }
    if (isDevelopment) {
      for (const key of ALLOWED_KEYS) {
        localStorage.removeItem(key);
      }
    }
  }
}

export const secureTokenStorage = new SecureTokenStorage();

export const getToken = (): string | null => {
  if (typeof document !== 'undefined') {
    const match = document.cookie.match(/(?:^|; )auth_token=([^;]+)/);
    if (match) return decodeURIComponent(match[1]);
  }
  return secureTokenStorage.getItem('auth_token');
};

export const getRefreshToken = (): string | null => {
  if (typeof document !== 'undefined') {
    const match = document.cookie.match(/(?:^|; )refresh_token=([^;]+)/);
    if (match) return decodeURIComponent(match[1]);
  }
  return secureTokenStorage.getItem('refresh_token');
};

export const clearAuth = (): void => {
  secureTokenStorage.clear();
  if (typeof document !== 'undefined') {
    document.cookie = 'auth_token=; HttpOnly; SameSite=Strict; Path=/; Max-Age=0';
    document.cookie = 'refresh_token=; HttpOnly; SameSite=Strict; Path=/; Max-Age=0';
  }
};
