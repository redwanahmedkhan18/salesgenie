import { AuthProvider } from "./AuthProvider";
import { LoginPage } from "./LoginPage";

export default function LoginApp() {
  return (
    <AuthProvider>
      <LoginPage />
    </AuthProvider>
  );
}