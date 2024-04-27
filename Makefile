.PHONY: test
test:
	@echo "Running tests"
	@pytest -v -x -s --cov=src -vv

.PHONY: coverage
coverage:
	@echo "Running coverage"
	@coverage html
	@coverage report

.PHONY: clean
clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .coverage
	@rm -rf htmlcov

.PHONY: start-db
start-db:
	@echo "Starting server"
	@docker compose up
