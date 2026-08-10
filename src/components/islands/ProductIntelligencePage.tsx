import { AuthProvider } from "../../auth/AuthProvider";
import { ProtectedRoute } from "../../auth/ProtectedRoute";
import ProductIntelligenceApp from "./ProductIntelligenceApp";

export default function ProductIntelligencePage() {
  return (
    <AuthProvider>
      <ProtectedRoute
        requiredRoles={[
          "org_admin",
          "super_admin",
          "knowledge_manager",
        ]}
      >
        <ProductIntelligenceApp />
      </ProtectedRoute>
    </AuthProvider>
  );
}
