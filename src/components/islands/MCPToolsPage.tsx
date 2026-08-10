import { AuthProvider } from "../../auth/AuthProvider";
import { ProtectedRoute } from "../../auth/ProtectedRoute";
import MCPToolsApp from "./MCPToolsApp";

export default function MCPToolsPage() {
  return (
    <AuthProvider>
      <ProtectedRoute
        requiredRoles={[
          "org_admin",
          "super_admin",
          "knowledge_manager",
        ]}
      >
        <MCPToolsApp />
      </ProtectedRoute>
    </AuthProvider>
  );
}
