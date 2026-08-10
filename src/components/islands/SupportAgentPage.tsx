import React from 'react';
import { AuthProvider } from '../../auth/AuthProvider';
import { ProtectedRoute } from '../../auth/ProtectedRoute';
import SupportAgentDashboard from './SupportAgentDashboard';

export default function SupportAgentPage() {
  return (
    <AuthProvider>
      <ProtectedRoute requiredRoles={['super_admin', 'org_admin', 'support_manager', 'support_agent']}>
        <SupportAgentDashboard />
      </ProtectedRoute>
    </AuthProvider>
  );
}
