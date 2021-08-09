.PHONY: setup
setup:
	python -m poetry install

.PHONY: format
format:
	python -m poetry run black src tests
	python -m poetry run isort src tests --profile black

.PHONY: lint
lint:
	python -m poetry run flake8 src tests

.PHONY: type-check
type-check:
	python -m poetry run mypy src tests

.PHONY: test
test:
	python -m poetry run pytest tests
