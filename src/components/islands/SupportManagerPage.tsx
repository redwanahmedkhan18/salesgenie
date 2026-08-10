import React from 'react';
import { AuthProvider } from '../../auth/AuthProvider';
import { ProtectedRoute } from '../../auth/ProtectedRoute';
import SupportManagerDashboard from './SupportManagerDashboard';

export default function SupportManagerPage() {
  return (
    <AuthProvider>
      <ProtectedRoute requiredRoles={['super_admin', 'org_admin', 'support_manager']}>
        <SupportManagerDashboard />
      </ProtectedRoute>
    </AuthProvider>
  );
}
