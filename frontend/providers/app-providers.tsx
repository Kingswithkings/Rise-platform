"use client";

import type { ReactNode } from "react";

import { AuthProvider } from "@/providers/auth-provider";
import { ThemeProvider } from "@/providers/theme-provider";

export function AppProviders({ children }: Readonly<{ children: ReactNode }>) {
  return (
    <ThemeProvider>
      <AuthProvider>{children}</AuthProvider>
    </ThemeProvider>
  );
}
