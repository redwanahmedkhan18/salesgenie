import { AuthProvider } from "../../auth/AuthProvider";
import { ProtectedRoute } from "../../auth/ProtectedRoute";
import { useErrorReporting } from "../../lib/useErrorReporting";
import type { PlatformRole } from '../../lib/types';
import type { ReactNode } from 'react';

interface AppProvidersProps {
  children: ReactNode;
  requiredRoles?: PlatformRole[];
  redirectTo?: string;
}

export default function AppProviders({ children, requiredRoles = [], redirectTo = '/login' }: AppProvidersProps) {
  useErrorReporting();

  return (
    <AuthProvider>
      <ProtectedRoute requiredRoles={requiredRoles} redirectTo={redirectTo}>
        {children}
      </ProtectedRoute>
    </AuthProvider>
  );
}