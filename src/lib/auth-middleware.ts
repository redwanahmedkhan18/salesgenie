import type { APIContext } from 'astro';
import type { PlatformRole } from './types';

const JWT_SECRET = process.env.JWT_SECRET || process.env.SALESGENIE_JWT_SECRET;
const JWT_ALGORITHMS = ['HS256', 'HS384', 'HS512', 'RS256', 'RS384', 'RS512'];
const MAX_TOKEN_AGE = 24 * 60 * 60;
const MAX_TOKEN_LENGTH = 4096;

interface JwtPayload {
  sub: string;
  email?: string;
  roles?: PlatformRole[];
  tenant_id?: string;
  exp?: number;
  iat?: number;
  iss?: string;
  aud?: string | string[];
}

const RATE_LIMIT_STORE: Map<string, { count: number; resetAt: number }> = new Map();

const AUTH_RATE_LIMIT = {
  windowMs: 15 * 60 * 1000,
  maxRequests: 50,
  keyPrefix: 'auth:login',
};

const API_RATE_LIMIT = {
  windowMs: 60 * 1000,
  maxRequests: 100,
  keyPrefix: 'api',
};

function isRateLimited(
  key: string,
  windowMs: number,
  maxRequests: number
): boolean {
  const now = Date.now();
  const entry = RATE_LIMIT_STORE.get(key);
  if (!entry || entry.resetAt < now) {
    RATE_LIMIT_STORE.set(key, { count: 1, resetAt: now + windowMs });
    return false;
  }
  entry.count++;
  return entry.count > maxRequests;
}

function getRateLimitKey(context: APIContext, prefix: string): string {
  const forwardedFor = context.request.headers.get('x-forwarded-for');
  const ip = forwardedFor ? forwardedFor.split(',')[0].trim() : 'unknown';
  return `${prefix}:${ip}`;
}

export function requireAuth(context: APIContext): {
  user: { id: string; email: string; roles: PlatformRole[]; tenant_id: string };
  tenant_id: string;
} | null {
  const authHeader = context.request.headers.get('authorization');
  let token: string | null = null;

  if (authHeader && authHeader.startsWith('Bearer ')) {
    token = authHeader.substring(7);
  } else {
    const cookieHeader = context.request.headers.get('cookie');
    if (cookieHeader) {
      const cookies = cookieHeader.split(';').map(c => c.trim());
      for (const cookie of cookies) {
        const [name, ...valueParts] = cookie.split('=');
        if (name === 'auth_token') {
          token = decodeURIComponent(valueParts.join('='));
          break;
        }
      }
    }
  }

  if (!token) {
    return null;
  }

  try {
    if (token.length > MAX_TOKEN_LENGTH) {
      return null;
    }
    const parts = token.split('.');
    if (parts.length !== 3) {
      return null;
    }

    try {
      const header = JSON.parse(Buffer.from(parts[0], 'base64').toString());
      if (header.alg === 'none' || header.alg === 'None') {
        return null;
      }

      if (header.alg !== 'HS256' && header.alg !== 'HS384' && header.alg !== 'HS512') {
        return null;
      }

      const [headerB64, payloadB64, signatureB64] = parts;
      const signingInput = `${headerB64}.${payloadB64}`;
      const expectedSignature = Buffer.from(
        require('crypto').createHmac('sha256', JWT_SECRET).update(signingInput).digest('base64url')
      ).toString('base64url');

      const providedSignature = Buffer.from(signatureB64, 'base64').toString('base64url');

      const nodeCrypto = require('crypto');
      const signatureMatch = nodeCrypto.timingSafeEqual(
        Buffer.from(expectedSignature),
        Buffer.from(providedSignature)
      );

      if (!signatureMatch) {
        return null;
      }

      const payload: JwtPayload = JSON.parse(
        Buffer.from(payloadB64, 'base64').toString()
      );

      const now = Math.floor(Date.now() / 1000);
      if (payload.exp && payload.exp < now) {
        return null;
      }

      const expectedIssuer = import.meta.env.PUBLIC_JWT_ISSUER || process.env.JWT_ISSUER || 'salesgenie';
      if (payload.iss && payload.iss !== expectedIssuer) {
        return null;
      }

      return {
        user: {
          id: payload.sub,
          email: payload.email || '',
          roles: (payload.roles || ['end_user']) as PlatformRole[],
          tenant_id: payload.tenant_id || '',
        },
        tenant_id: payload.tenant_id || '',
      };
    } catch {
      return null;
    }
  } catch {
    return null;
  }
}

export function requireRole(context: APIContext, requiredRoles: PlatformRole[]): boolean {
  const auth = requireAuth(context);
  if (!auth) return false;
  return requiredRoles.some(role => auth.user.roles.includes(role));
}

export function requirePermission(context: APIContext, permission: string): boolean {
  const auth = requireAuth(context);
  if (!auth) return false;

  if (auth.user.roles.includes('super_admin')) return true;

  const rolePermissions: Record<PlatformRole, string[]> = {
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

  let permissions: string[] = [];
  for (const role of auth.user.roles) {
    const perms = rolePermissions[role];
    if (perms) permissions = permissions.concat(perms);
  }
  permissions = [...new Set(permissions)];

  if (permissions.includes('*')) return true;
  return permissions.includes(permission);
}

export function checkRateLimit(
  context: APIContext,
  prefix: string,
  windowMs: number = API_RATE_LIMIT.windowMs,
  maxRequests: number = API_RATE_LIMIT.maxRequests
): boolean {
  const key = `${prefix}:${getRateLimitKey(context, prefix)}`;
  return isRateLimited(key, windowMs, maxRequests);
}

export function getAuthRateLimitKey(context: APIContext): string {
  return getRateLimitKey(context, AUTH_RATE_LIMIT.keyPrefix);
}

export function isAuthRateLimited(context: APIContext): boolean {
  return isRateLimited(
    getAuthRateLimitKey(context),
    AUTH_RATE_LIMIT.windowMs,
    AUTH_RATE_LIMIT.maxRequests
  );
}

const AUDIT_LOG: AuditLogEntry[] = [];

export interface AuditLogEntry {
  action: string;
  resource_type: string;
  resource_id?: string;
  user_id?: string;
  user_email?: string;
  tenant_id?: string;
  ip_address?: string;
  user_agent?: string;
  severity: 'low' | 'medium' | 'high' | 'critical';
  details: Record<string, unknown>;
  timestamp: string;
}

export function logAuditEvent(entry: Omit<AuditLogEntry, 'timestamp'>): void {
  const fullEntry: AuditLogEntry = {
    ...entry,
    timestamp: new Date().toISOString(),
  };
  AUDIT_LOG.push(fullEntry);
  if (AUDIT_LOG.length > 10000) {
    AUDIT_LOG.shift();
  }
  if (['high', 'critical'].includes(entry.severity)) {
    console.warn('[SECURITY AUDIT]', JSON.stringify({
      action: entry.action,
      resource_type: entry.resource_type,
      severity: entry.severity,
      user_id: entry.user_id,
      tenant_id: entry.tenant_id,
      timestamp: fullEntry.timestamp,
    }));
  }
}

export async function getClientIp(context: APIContext): Promise<string | null> {
  const forwardedFor = context.request.headers.get('x-forwarded-for');
  if (forwardedFor) {
    return forwardedFor.split(',')[0].trim();
  }
  return context.clientAddress || null;
}

export function validateId(id: string): boolean {
  return /^[a-zA-Z0-9_-]+$/.test(id) && id.length <= 128;
}

export function sanitizeString(input: string, maxLength: number = 10000): string {
  return input
    .replace(/[\x00-\x1f\x7f-\x9f]/g, '')
    .replace(/[<>'"&]/g, '')
    .slice(0, maxLength);
}

export async function hashPassword(password: string): Promise<string> {
  const nodeCrypto = require('crypto');
  const salt = nodeCrypto.randomBytes(32).toString('hex');
  const iterations = 100000;
  const hash = nodeCrypto.pbkdf2Sync(password, salt, iterations, 64, 'sha256').toString('hex');
  return `pbkdf2_sha256$${iterations}$${salt}$${hash}`;
}

export async function verifyPassword(password: string, storedHash: string): Promise<boolean> {
  try {
    const [algorithm, iterationsStr, salt, hash] = storedHash.split('$');
    if (algorithm !== 'pbkdf2_sha256') return false;
    const iterations = parseInt(iterationsStr, 10);
    const nodeCrypto = require('crypto');
    const computedHash = nodeCrypto.pbkdf2Sync(password, salt, iterations, 64, 'sha256').toString('hex');
    return nodeCrypto.timingSafeEqual(Buffer.from(hash), Buffer.from(computedHash));
  } catch {
    return false;
  }
}

export function validatePasswordStrength(password: string): { valid: boolean; errors: string[] } {
  const errors: string[] = [];
  if (password.length < 12) errors.push('Password must be at least 12 characters');
  if (!/[A-Z]/.test(password)) errors.push('Password must contain at least 1 uppercase letter');
  if (!/[a-z]/.test(password)) errors.push('Password must contain at least 1 lowercase letter');
  if (!/[0-9]/.test(password)) errors.push('Password must contain at least 1 number');
  if (!/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(password)) {
    errors.push('Password must contain at least 1 special character');
  }
  if (password.length > 128) errors.push('Password must be at most 128 characters');
  return { valid: errors.length === 0, errors };
}

export const ALLOWED_FILE_TYPES = [
  'text/plain',
  'text/csv',
  'application/json',
  'application/pdf',
  'application/msword',
  'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
  'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
  'application/vnd.openxmlformats-officedocument.presentationml.presentation',
];

export const ALLOWED_FILE_EXTENSIONS = [
  '.txt', '.csv', '.json', '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx',
];

export const MAX_FILE_SIZE = 10 * 1024 * 1024;

export function validateFileUpload(file: { name: string; type: string; size: number }): { valid: boolean; errors: string[] } {
  const errors: string[] = [];

  const ext = '.' + file.name.split('.').pop()?.toLowerCase();
  if (!ext || !ALLOWED_FILE_EXTENSIONS.includes(ext)) {
    errors.push(`File type ${ext || 'unknown'} is not allowed`);
  }

  if (!ALLOWED_FILE_TYPES.includes(file.type) && file.type !== 'application/octet-stream') {
    errors.push(`MIME type ${file.type} is not allowed`);
  }

  if (file.size > MAX_FILE_SIZE) {
    errors.push(`File size exceeds maximum of ${MAX_FILE_SIZE} bytes`);
  }

  if (file.name.includes('..') || file.name.includes('/') || file.name.includes('\\')) {
    errors.push('Invalid filename: path traversal detected');
  }

  return { valid: errors.length === 0, errors };
}
