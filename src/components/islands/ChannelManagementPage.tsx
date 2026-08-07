import { AuthProvider } from "../../auth/AuthProvider";
import { ProtectedRoute } from "../../auth/ProtectedRoute";
import { ChannelManagement } from "./channels/ChannelManagement";

export default function ChannelManagementPage() {
  return (
    <AuthProvider>
      <ProtectedRoute
        requiredRoles={[
          "org_admin",
          "super_admin",
          "workspace_admin",
          "knowledge_manager",
        ]}
      >
        <ChannelManagement />
      </ProtectedRoute>
    </AuthProvider>
  );
}