import { AuthProvider } from "../../auth/AuthProvider";
import { ProtectedRoute } from "../../auth/ProtectedRoute";
import FileManager from "./FileManager";

export default function FileManagerPage() {
  return (
    <AuthProvider>
      <ProtectedRoute>
        <FileManager />
      </ProtectedRoute>
    </AuthProvider>
  );
}