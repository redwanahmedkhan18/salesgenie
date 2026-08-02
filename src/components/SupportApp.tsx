import { AuthProvider } from "../auth/AuthProvider";
import { ProtectedRoute } from "../auth/ProtectedRoute";
import SupportTickets from "./islands/SupportTickets";

export default function SupportApp() {
    return (
        <AuthProvider>
            <ProtectedRoute
                requiredRoles={[
                    "support_manager",
                    "support_agent",
                    "org_admin",
                    "super_admin",
                ]}
            >
                <SupportTickets />
            </ProtectedRoute>
        </AuthProvider>
    );
}