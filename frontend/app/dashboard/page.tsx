import { ProtectedRoute } from "@/components/protected-route";

export default function DashboardPage() {
  return (
    <ProtectedRoute>
      <main>
        <h1>Dashboard</h1>
        <p>Your protected RISE workspace.</p>
      </main>
    </ProtectedRoute>
  );
}
