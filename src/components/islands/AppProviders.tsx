import React from 'react';
import { AuthProvider } from "../../auth/AuthProvider";
import { ProtectedRoute } from "../../auth/ProtectedRoute";

interface AppProvidersProps {
  children: React.ReactNode;
  requiredRoles?: string[];
  redirectTo?: string;
}

export default function AppProviders({ children, requiredRoles = [], redirectTo = '/login' }: AppProvidersProps) {
  return (
    <AuthProvider>
      <ProtectedRoute requiredRoles={requiredRoles as any} redirectTo={redirectTo}>
        {children}
      </ProtectedRoute>
    </AuthProvider>
  );
}