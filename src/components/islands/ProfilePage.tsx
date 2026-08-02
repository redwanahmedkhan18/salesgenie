import { AuthProvider } from "../../auth/AuthProvider";
import { ProtectedRoute } from "../../auth/ProtectedRoute";
import { UserProfile } from "../../auth/UserProfile";

export default function ProfilePage() {
    return (
        <AuthProvider>
            <ProtectedRoute>
                <UserProfile />
            </ProtectedRoute>
        </AuthProvider>
    );
}