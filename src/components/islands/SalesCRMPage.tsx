import { AuthProvider } from "../../auth/AuthProvider";
import { ProtectedRoute } from "../../auth/ProtectedRoute";
import SalesCRM from "./SalesCRM";

export default function SalesCRMPage() {
  return (
    <AuthProvider>
      <ProtectedRoute
        requiredRoles={[
          "org_admin",
          "super_admin",
          "sales_manager",
          "sales_agent",
        ]}
      >
        <SalesCRM />
      </ProtectedRoute>
    </AuthProvider>
  );
}