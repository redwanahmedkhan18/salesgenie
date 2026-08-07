import { AuthProvider } from "../../auth/AuthProvider";
import { ProtectedRoute } from "../../auth/ProtectedRoute";
import CustomerManagement from "./CustomerManagement";

export default function CustomersPage() {
  return (
    <AuthProvider>
      <ProtectedRoute
        requiredRoles={[
          "org_admin",
          "super_admin",
          "sales_manager",
          "sales_agent",
          "support_manager",
        ]}
      >
        <CustomerManagement />
      </ProtectedRoute>
    </AuthProvider>
  );
}