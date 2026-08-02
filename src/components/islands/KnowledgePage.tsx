import { AuthProvider } from "../../auth/AuthProvider";
import { ProtectedRoute } from "../../auth/ProtectedRoute";
import KnowledgeBase from "./KnowledgeBase";

export default function KnowledgePage() {
    return (
        <AuthProvider>
            <ProtectedRoute requiredRoles={['org_admin', 'super_admin', 'workspace_admin', 'sales_manager', 'sales_agent', 'knowledge_manager']}>
                <KnowledgeBase />
            </ProtectedRoute>
        </AuthProvider>
    );
}