import { AuthProvider } from "../../auth/AuthProvider";
import { ProtectedRoute } from "../../auth/ProtectedRoute";
import FileManager from "./FileManager";

export default function FilesPage() {
  return (
    <AuthProvider>
      <ProtectedRoute>
        <FileManager />
      </ProtectedRoute>
    </AuthProvider>
  );
}