import { ApiStatus } from "@/features/platform/components/api-status";

export default function HomePage() {
  return (
    <main>
      <p className="eyebrow">Platform Foundation</p>
      <h1>RISE</h1>
      <p>The marketplace infrastructure is running.</p>
      <ApiStatus />
      <a href="http://localhost:8000/docs">Open API documentation</a>
    </main>
  );
}
