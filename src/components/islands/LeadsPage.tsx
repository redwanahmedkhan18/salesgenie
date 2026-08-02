import { AuthProvider } from "../../auth/AuthProvider";
import { ProtectedRoute } from "../../auth/ProtectedRoute";
import { LeadIntelligence } from "../../components/islands/leads/LeadIntelligence";

export default function LeadsPage() {
  return (
    <AuthProvider>
      <ProtectedRoute requiredRoles={['org_admin', 'super_admin', 'sales_manager', 'sales_agent', 'knowledge_manager']}>
        <LeadIntelligence />
      </ProtectedRoute>
    </AuthProvider>
  );
}