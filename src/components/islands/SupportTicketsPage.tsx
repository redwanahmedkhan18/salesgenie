import { AuthProvider } from "../../auth/AuthProvider";
import { ProtectedRoute } from "../../auth/ProtectedRoute";
import SupportTickets from "./SupportTickets";

export default function SupportTicketsPage() {
  return (
    <AuthProvider>
      <ProtectedRoute
        requiredRoles={[
          "support_manager",
          "support_agent",
          "org_admin",
          "super_admin",
          "end_user",
        ]}
      >
        <SupportTickets />
      </ProtectedRoute>
    </AuthProvider>
  );
}