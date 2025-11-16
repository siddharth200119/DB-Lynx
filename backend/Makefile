
.PHONY: build dev test help db

# ----------------
# PYTHON TARGETS
# ----------------

build: ## Build the project into a single executable
	uv run pyinstaller --onefile main.py

dev: ## Run the project in development mode
	uv run main.py

test: ## Run all tests
	uv run pytest

help: ## Show available commands
	@echo "Available commands:"
	@awk 'BEGIN {FS = ":.*?## "}; /^[a-zA-Z0-9_-]+:.*?## / {printf "  %-10s %s\n", $$1, $$2}' Makefile

# ----------------
# GO DB-MANAGER
# ----------------

DB_BIN=./db-manager

db: ## Run db-manager with arguments. Example: make db init
	@$(DB_BIN) $(filter-out $@,$(MAKECMDGOALS))

# Prevent "nothing to be done" errors
%:
	@:
