
import React from 'react';
import { useAuth } from './AuthProvider';
import type { PlatformRole } from '../lib/types';

interface ProtectedRouteProps {
  children: React.ReactNode;
  requiredRoles?: PlatformRole[];
  requiredPermissions?: string[];
  redirectTo?: string;
}

function AccessDenied({
  requiredRoles = [],
  userRoles = [],
}: {
  requiredRoles?: PlatformRole[];
  userRoles?: PlatformRole[];
}) {
  return (
    <div
      className="flex items-center justify-center min-h-screen"
      style={{ background: 'var(--color-background)' }}
    >
      <div
        className="text-center p-8 rounded-xl max-w-lg"
        style={{
          background: 'var(--color-card)',
          border: '1px solid var(--color-border)',
        }}
      >
        <div className="text-5xl mb-4">🔒</div>

        <h2
          className="text-2xl font-bold mb-2"
          style={{ color: 'var(--color-foreground)' }}
        >
          Access Denied
        </h2>

        <p
          className="text-sm mb-4"
          style={{ color: 'var(--color-muted-foreground)' }}
        >
          Your account doesn't have permission to access this page.
        </p>

        {requiredRoles.length > 0 && (
          <>
            <div
              className="text-xs font-semibold mb-1"
              style={{ color: 'var(--color-foreground)' }}
            >
              Required Roles
            </div>

            <div
              className="text-xs mb-3"
              style={{ color: 'var(--color-muted-foreground)' }}
            >
              {requiredRoles.join(', ')}
            </div>
          </>
        )}

        <div
          className="text-xs font-semibold mb-1"
          style={{ color: 'var(--color-foreground)' }}
        >
          Your Roles
        </div>

        <div
          className="text-xs"
          style={{ color: 'var(--color-muted-foreground)' }}
        >
          {userRoles.length > 0 ? userRoles.join(', ') : 'No roles assigned'}
        </div>
      </div>
    </div>
  );
}

export function ProtectedRoute({
  children,
  requiredRoles = [],
  requiredPermissions = [],
  redirectTo = '/login',
}: ProtectedRouteProps) {
  const {
    isLoading,
    isAuthenticated,
    roles,
    permissions,
  } = useAuth();

  if (isLoading) {
    return (
      <div
        className="flex items-center justify-center min-h-screen"
        style={{ background: 'var(--color-background)' }}
      >
        <div
          className="flex items-center gap-3"
          style={{ color: 'var(--color-foreground)' }}
        >
          <div className="w-6 h-6 border-2 border-current border-t-transparent rounded-full animate-spin" />
          <span>Loading...</span>
        </div>
      </div>
    );
  }

  if (!isAuthenticated) {
    if (typeof window !== 'undefined' && !window.location) {
      return null;
    }
    if (typeof window !== 'undefined') {
      window.location.replace(redirectTo);
    }
    return null;
  }

  if (
    requiredRoles.length > 0 &&
    !roles.some(role => requiredRoles.includes(role))
  ) {
    return (
      <AccessDenied
        requiredRoles={requiredRoles}
        userRoles={roles}
      />
    );
  }

  if (requiredPermissions.length > 0) {
    const hasAllPermissions = requiredPermissions.every(permission =>
      permissions.includes(permission)
    );

    if (!hasAllPermissions) {
      return (
        <AccessDenied
          requiredRoles={requiredRoles}
          userRoles={roles}
        />
      );
    }
  }

  return <>{children}</>;
}

interface RoleBasedRouteProps {
  children: React.ReactNode;
  requiredRoles: PlatformRole[];
}

export function RoleBasedRoute({
  children,
  requiredRoles,
}: RoleBasedRouteProps) {
  const { roles, hasAnyRole } = useAuth();

  if (!hasAnyRole(requiredRoles)) {
    return (
      <AccessDenied
        requiredRoles={requiredRoles}
        userRoles={roles}
      />
    );
  }

  return <>{children}</>;
}