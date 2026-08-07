import { AuthProvider } from "../../auth/AuthProvider";
import { ProtectedRoute } from "../../auth/ProtectedRoute";
import SearchInterface from "./SearchInterface";

export default function SearchPage() {
  return (
    <AuthProvider>
      <ProtectedRoute>
        <SearchInterface />
      </ProtectedRoute>
    </AuthProvider>
  );
}