import React from 'react';
import { useAuth } from '../auth/AuthProvider';
import type { PlatformRole } from '../lib/types';

interface ProtectedRouteProps {
  children: React.ReactNode;
  requiredRoles?: PlatformRole[];
  requiredPermissions?: string[];
  redirectTo?: string;
}

export function ProtectedRoute({
  children,
  requiredRoles = [],
  requiredPermissions = [],
  redirectTo = '/login',
}: ProtectedRouteProps) {
  const { user, isAuthenticated, roles, permissions, isLoading } = useAuth();

  if (isLoading) {
    return (
      <div className="flex items-center justify-center min-h-screen" style={{ background: 'var(--color-background)' }}>
        <div className="flex items-center gap-3" style={{ color: 'var(--color-foreground)' }}>
          <div className="w-6 h-6 border-2 border-current border-t-transparent rounded-full animate-spin" />
          <span>Loading...</span>
        </div>
      </div>
    );
  }

  if (!isAuthenticated) {
    window.location.href = redirectTo;
    return null;
  }

  if (requiredRoles.length > 0 && !roles.some(role => requiredRoles.includes(role))) {
    window.location.href = '/unauthorized';
    return null;
  }

  if (requiredPermissions.length > 0) {
    const hasAllPermissions = requiredPermissions.every(perm => permissions.includes(perm));
    if (!hasAllPermissions) {
      window.location.href = '/unauthorized';
      return null;
    }
  }

  return <>{children}</>;
}

export function RoleBasedRoute({
  children,
  requiredRoles,
}: {
  children: React.ReactNode;
  requiredRoles: PlatformRole[];
}) {
  const { roles, hasAnyRole } = useAuth();

  if (!hasAnyRole(requiredRoles)) {
    return (
      <div className="flex items-center justify-center min-h-screen" style={{ background: 'var(--color-background)' }}>
        <div className="text-center p-8 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <div className="text-4xl mb-4">🚫</div>
          <h2 className="text-xl font-bold mb-2" style={{ color: 'var(--color-foreground)' }}>Access Denied</h2>
          <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
            You don't have permission to access this page.
          </p>
          <p className="text-xs mt-2" style={{ color: 'var(--color-muted-foreground)' }}>
            Required roles: {requiredRoles.join(', ')}
          </p>
          <p className="text-xs mt-1" style={{ color: 'var(--color-muted-foreground)' }}>
            Your roles: {roles.join(', ')}
          </p>
        </div>
      </div>
    );
  }

  return <>{children}</>;
}
