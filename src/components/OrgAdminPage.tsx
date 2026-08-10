import React from 'react';
import { AuthProvider } from "../auth/AuthProvider";
import { ProtectedRoute } from "../auth/ProtectedRoute";
import OrganizationAdminDashboardPage from "./islands/OrganizationAdminDashboardPage";

export default function OrgAdminPage() {
  return (
    <AuthProvider>
      <ProtectedRoute requiredRoles={['super_admin', 'workspace_admin', 'org_admin']}>
        <OrganizationAdminDashboardPage />
      </ProtectedRoute>
    </AuthProvider>
  );
}
