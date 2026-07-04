import Link from "next/link";
import type { ReactNode } from "react";

export function AppShell({ children }: Readonly<{ children: ReactNode }>) {
  return (
    <>
      <header className="site-header">
        <Link href="/">RISE</Link>
        <nav aria-label="Primary navigation">
          <Link href="/login">Sign in</Link>
        </nav>
      </header>
      {children}
    </>
  );
}
