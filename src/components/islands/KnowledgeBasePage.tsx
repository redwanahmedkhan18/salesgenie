import { AuthProvider } from "../../auth/AuthProvider";
import { ProtectedRoute } from "../../auth/ProtectedRoute";
import KnowledgeBase from "./KnowledgeBase";

export default function KnowledgeBasePage() {
  return (
    <AuthProvider>
      <ProtectedRoute
        requiredRoles={[
          "knowledge_manager",
          "support_manager",
          "org_admin",
          "super_admin",
        ]}
      >
        <KnowledgeBase />
      </ProtectedRoute>
    </AuthProvider>
  );
}