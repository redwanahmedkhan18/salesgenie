import { AuthProvider } from "../auth/AuthProvider";
import { ProtectedRoute } from "../auth/ProtectedRoute";
import { RoleDashboard } from "../auth/RoleDashboard";

export default function DashboardApp() {
  return (
    <AuthProvider>
      <ProtectedRoute>
        <RoleDashboard />
      </ProtectedRoute>
    </AuthProvider>
  );
}