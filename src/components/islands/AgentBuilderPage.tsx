import { AuthProvider } from "../../auth/AuthProvider";
import { ProtectedRoute } from "../../auth/ProtectedRoute";
import AgentBuilder from "./AgentBuilder";

export default function AgentBuilderPage() {
  return (
    <AuthProvider>
      <ProtectedRoute
        requiredRoles={[
          "org_admin",
          "super_admin",
          "knowledge_manager",
          "sales_manager",
        ]}
      >
        <AgentBuilder />
      </ProtectedRoute>
    </AuthProvider>
  );
}