poetry-venv:
	poetry shell

.PHONY: lint
lint:
	poetry run ruff check app/ tests/
	poetry run mypy app/ tests/

.PHONY: format
format:
	poetry run ruff format app/ tests/

.PHONY: test
test:
	poetry run pytest tests

.PHONY: build
build: lint test

.PHONY: run
run:
	poetry run uvicorn app.main:app
