import React from 'react';
import { AuthProvider } from "../../auth/AuthProvider";
import { ProtectedRoute } from "../../auth/ProtectedRoute";
import SuperAdminDashboard from "./SuperAdminDashboard";

export default function SuperAdminDashboardPage() {
  return (
    <AuthProvider>
      <ProtectedRoute
        requiredRoles={["super_admin", "org_admin"]}
      >
        <SuperAdminDashboard />
      </ProtectedRoute>
    </AuthProvider>
  );
}