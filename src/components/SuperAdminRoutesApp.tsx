import React from 'react';
import { AuthProvider } from "../auth/AuthProvider";
import { ProtectedRoute } from "../auth/ProtectedRoute";
import SuperAdminRoutesPage from "./islands/SuperAdminRoutesPage";

export default function SuperAdminRoutesApp() {
  return (
    <AuthProvider>
      <ProtectedRoute requiredRoles={['super_admin', 'workspace_admin']}>
        <SuperAdminRoutesPage />
      </ProtectedRoute>
    </AuthProvider>
  );
}
