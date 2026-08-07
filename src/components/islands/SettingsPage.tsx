import { AuthProvider } from "../../auth/AuthProvider";
import { ProtectedRoute } from "../../auth/ProtectedRoute";
import SettingsAdmin from "./SettingsAdmin";

export default function SettingsPage() {
  return (
    <AuthProvider>
      <ProtectedRoute
        requiredRoles={[
          "org_admin",
          "super_admin",
          "workspace_admin",
        ]}
      >
        <SettingsAdmin />
      </ProtectedRoute>
    </AuthProvider>
  );
}