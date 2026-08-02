import { AuthProvider } from "../../auth/AuthProvider";
import { ProtectedRoute } from "../../auth/ProtectedRoute";
import ConversationInbox from "./ConversationInbox";

export default function ConversationInboxPage() {
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
        <ConversationInbox />
      </ProtectedRoute>
    </AuthProvider>
  );
}