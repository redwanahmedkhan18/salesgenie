import { AuthProvider } from "./AuthProvider";
import { SignupPage } from "./SignupPage";

export default function SignupApp() {
  return (
    <AuthProvider>
      <SignupPage />
    </AuthProvider>
  );
}