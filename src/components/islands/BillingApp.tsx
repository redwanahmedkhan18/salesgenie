import React from 'react';
import { AuthProvider } from "../../auth/AuthProvider";
import { ProtectedRoute } from "../../auth/ProtectedRoute";
import BillingContent from "./BillingPage";

export default function BillingApp() {
  return (
    <AuthProvider>
      <ProtectedRoute 
        requiredRoles={["org_admin", "super_admin", "workspace_admin", "end_user"]}
        redirectTo="/login"
      >
        <BillingContent />
      </ProtectedRoute>
    </AuthProvider>
  );
}