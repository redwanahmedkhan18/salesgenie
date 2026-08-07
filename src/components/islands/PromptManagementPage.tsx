import { AuthProvider } from "../../auth/AuthProvider";
import { ProtectedRoute } from "../../auth/ProtectedRoute";
import PromptManagement from "./PromptManagement";

export default function PromptManagementPage() {
  return (
    <AuthProvider>
      <ProtectedRoute
        requiredRoles={[
          "org_admin",
          "super_admin",
          "knowledge_manager",
          "support_manager",
        ]}
      >
        <PromptManagement />
      </ProtectedRoute>
    </AuthProvider>
  );
}