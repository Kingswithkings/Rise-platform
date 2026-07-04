import { expect, test } from "@playwright/test";

test("shows the RISE platform landing page", async ({ page }) => {
  await page.goto("/");
  await expect(page.getByRole("heading", { name: "RISE" })).toBeVisible();
  await expect(page.getByRole("link", { name: "Open API documentation" })).toBeVisible();
});
