"use client";

import {
  createContext,
  type ReactNode,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useState,
} from "react";

import { login as requestLogin } from "@/services/auth";
import type { AuthState, LoginCredentials } from "@/types/auth";

const TOKEN_KEY = "rise_access_token";

type AuthContextValue = AuthState & {
  login: (credentials: LoginCredentials) => Promise<void>;
  logout: () => void;
};

const AuthContext = createContext<AuthContextValue | null>(null);

export function AuthProvider({ children }: Readonly<{ children: ReactNode }>) {
  const [token, setToken] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const hydrationTask = window.setTimeout(() => {
      setToken(window.localStorage.getItem(TOKEN_KEY));
      setIsLoading(false);
    }, 0);
    return () => window.clearTimeout(hydrationTask);
  }, []);

  const login = useCallback(async (credentials: LoginCredentials) => {
    const response = await requestLogin(credentials);
    window.localStorage.setItem(TOKEN_KEY, response.access_token);
    setToken(response.access_token);
  }, []);

  const logout = useCallback(() => {
    window.localStorage.removeItem(TOKEN_KEY);
    setToken(null);
  }, []);

  const value = useMemo<AuthContextValue>(
    () => ({ token, isAuthenticated: token !== null, isLoading, login, logout }),
    [isLoading, login, logout, token],
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth(): AuthContextValue {
  const context = useContext(AuthContext);
  if (context === null) {
    throw new Error("useAuth must be used within AuthProvider");
  }
  return context;
}
