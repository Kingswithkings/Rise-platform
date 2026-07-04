import { afterEach, describe, expect, it, vi } from "vitest";

import { apiRequest } from "./api";

describe("apiRequest", () => {
  afterEach(() => {
    vi.unstubAllGlobals();
  });

  it("returns typed JSON for a successful response", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn().mockResolvedValue(
        new Response(JSON.stringify({ status: "healthy" }), {
          status: 200,
          headers: { "Content-Type": "application/json" },
        }),
      ),
    );

    await expect(apiRequest<{ status: string }>("/health")).resolves.toEqual({
      status: "healthy",
    });
  });

  it("throws when the API returns an error", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue(new Response(null, { status: 503 })));

    await expect(apiRequest("/health")).rejects.toThrow("status 503");
  });
});
