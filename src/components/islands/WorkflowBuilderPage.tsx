import { AuthProvider } from "../../auth/AuthProvider";
import { ProtectedRoute } from "../../auth/ProtectedRoute";
import WorkflowBuilder from "./WorkflowBuilder";

export default function WorkflowBuilderPage() {
  return (
    <AuthProvider>
      <ProtectedRoute
        requiredRoles={[
          "org_admin",
          "super_admin",
          "workspace_admin",
        ]}
      >
        <WorkflowBuilder />
      </ProtectedRoute>
    </AuthProvider>
  );
}