import React from 'react';
import { AuthProvider } from '../../auth/AuthProvider';
import { ProtectedRoute } from '../../auth/ProtectedRoute';
import SalesManagerDashboard from './SalesManagerDashboard';

export default function SalesManagerPage() {
  return (
    <AuthProvider>
      <ProtectedRoute requiredRoles={['super_admin', 'org_admin', 'sales_manager']}>
        <SalesManagerDashboard />
      </ProtectedRoute>
    </AuthProvider>
  );
}
