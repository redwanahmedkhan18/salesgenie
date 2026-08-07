import { AuthProvider } from "../../auth/AuthProvider";
import { ProtectedRoute } from "../../auth/ProtectedRoute";
import AnalyticsDashboard from "./AnalyticsDashboard";

export default function AnalyticsDashboardPage() {
  return (
    <AuthProvider>
      <ProtectedRoute
        requiredRoles={[
          "org_admin",
          "super_admin",
          "auditor",
        ]}
      >
        <AnalyticsDashboard />
      </ProtectedRoute>
    </AuthProvider>
  );
}