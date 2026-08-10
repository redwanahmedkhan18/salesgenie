import { AuthProvider } from "../../auth/AuthProvider";
import { ProtectedRoute } from "../../auth/ProtectedRoute";
import { TeamManagement } from "../../components/team/TeamManagement";

export default function TeamPage() {
  return (
    <AuthProvider>
      <ProtectedRoute requiredRoles={["super_admin", "workspace_admin", "org_admin"]}>
        <TeamManagement />
      </ProtectedRoute>
    </AuthProvider>
  );
}
