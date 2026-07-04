import { apiRequest } from "@/services/api";
import type { AuthToken, LoginCredentials } from "@/types/auth";

export function login(credentials: LoginCredentials): Promise<AuthToken> {
  return apiRequest<AuthToken>("/auth/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(credentials),
  });
}
