import { AuthProvider } from "../../auth/AuthProvider";
import { ProtectedRoute } from "../../auth/ProtectedRoute";
import AuditLogs from "./AuditLogs";

export default function AuditLogsPage() {
  return (
    <AuthProvider>
      <ProtectedRoute
        requiredRoles={[
          "org_admin",
          "super_admin",
          "auditor",
        ]}
      >
        <AuditLogs />
      </ProtectedRoute>
    </AuthProvider>
  );
}