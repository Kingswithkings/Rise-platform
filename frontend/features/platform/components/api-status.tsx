"use client";

import { useEffect, useState } from "react";

type Health = { status: string };

export function ApiStatus() {
  const [status, setStatus] = useState("checking");

  useEffect(() => {
    fetch("http://localhost:8000/health")
      .then((response) => {
        if (!response.ok) throw new Error("API unavailable");
        return response.json() as Promise<Health>;
      })
      .then((health) => setStatus(health.status))
      .catch(() => setStatus("unavailable"));
  }, []);

  return <div className="status">API status: {status}</div>;
}
