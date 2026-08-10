import React from 'react';
import { AuthProvider } from "../auth/AuthProvider";
import { ProtectedRoute } from "../auth/ProtectedRoute";
import WorkspaceAdminDashboardPage from "./islands/WorkspaceAdminDashboardPage";

export default function WorkspaceAdminPage() {
  return (
    <AuthProvider>
      <ProtectedRoute requiredRoles={['super_admin', 'workspace_admin']}>
        <WorkspaceAdminDashboardPage />
      </ProtectedRoute>
    </AuthProvider>
  );
}
