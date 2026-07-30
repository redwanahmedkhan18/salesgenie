import type { ReactNode } from "react";
import { AuthProvider } from "../auth/AuthProvider";

interface Props {
  children: ReactNode;
}

export default function AppProviders({ children }: Props) {
  return (
    <AuthProvider>
      {children}
    </AuthProvider>
  );
}