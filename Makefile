.PHONY: up down test lint

up:
	docker compose up --build

down:
	docker compose down

test:
	docker compose run --rm backend pytest

lint:
	docker compose run --rm backend ruff check app tests
	docker compose run --rm backend black --check app tests
	docker compose run --rm frontend npm run typecheck
	docker compose run --rm frontend npm run lint
	docker compose run --rm frontend npm run format:check
