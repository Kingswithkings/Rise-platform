"use client";

import { type FormEvent, useState } from "react";
import { useRouter } from "next/navigation";

import { useAuth } from "@/providers/auth-provider";

export function LoginForm() {
  const router = useRouter();
  const { login } = useAuth();
  const [error, setError] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setError(null);
    setIsSubmitting(true);
    const data = new FormData(event.currentTarget);

    try {
      await login({
        email: String(data.get("email")),
        password: String(data.get("password")),
      });
      router.replace("/dashboard");
    } catch {
      setError("Unable to sign in with those credentials.");
      setIsSubmitting(false);
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Email
        <input name="email" type="email" autoComplete="email" required />
      </label>
      <label>
        Password
        <input name="password" type="password" autoComplete="current-password" required />
      </label>
      {error && <p role="alert">{error}</p>}
      <button disabled={isSubmitting} type="submit">
        {isSubmitting ? "Signing in…" : "Sign in"}
      </button>
    </form>
  );
}
