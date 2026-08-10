import React from 'react';
import { AuthProvider } from '../../auth/AuthProvider';
import { ProtectedRoute } from '../../auth/ProtectedRoute';
import SalesAgentDashboard from './SalesAgentDashboard';

export default function SalesAgentPage() {
  return (
    <AuthProvider>
      <ProtectedRoute requiredRoles={['super_admin', 'org_admin', 'sales_manager', 'sales_agent']}>
        <SalesAgentDashboard />
      </ProtectedRoute>
    </AuthProvider>
  );
}
