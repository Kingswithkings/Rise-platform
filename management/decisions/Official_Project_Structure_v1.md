# Official Project Structure v1.0

This structure is frozen unless there is a strong architectural reason to change it.

```text
rise-platform/
├── backend/
├── frontend/
├── mobile/
├── docs/
├── management/
├── design/
├── infrastructure/
├── scripts/
├── tests/
├── .github/
├── docker-compose.yml
├── Makefile
├── README.md
├── CHANGELOG.md
└── ROADMAP.md
```

## Separation of Concerns

- `backend/` — application code
- `frontend/` — web client
- `mobile/` — mobile client
- `docs/` — engineering and technical knowledge
- `management/` — planning, delivery, governance, and project management
- `design/` — brand, UX, UI, and product design assets
- `infrastructure/` — deployment and infrastructure assets
- `scripts/` — automation scripts
- `tests/` — cross-system test assets
