# Load environment variables from .env
include .env
export $(shell sed 's/=.*//' .env)

DB_URI ?= sqlite:///${DB_PATH}

# Initialize migrations folder
init:
	@echo "📁 Initializing migrations directory..."
	@uv run yoyo init migrations

# Apply all migrations
db-migrate:
	@echo "🚀 Applying all pending migrations to $(DB_URI)..."
	@uv run yoyo apply -d "$(DB_URI)"

# Rollback last migration
db-rollback:
	@echo "⏪ Rolling back last migration on $(DB_URI)..."
	@uv run yoyo rollback -d "$(DB_URI)"

# Apply a specific migration file
db-migrate-file:
	@if [ -z "$(f)" ]; then echo "❌ Please specify a file with 'f=<path>'"; exit 1; fi
	@echo "🚀 Applying migration file $(f) to $(DB_URI)..."
	@uv run yoyo apply -d "$(DB_URI)" "$(f)"

# Rollback a specific migration file
db-rollback-file:
	@if [ -z "$(f)" ]; then echo "❌ Please specify a file with 'f=<path>'"; exit 1; fi
	@echo "⏪ Rolling back migration file $(f) on $(DB_URI)..."
	@uv run yoyo rollback -d "$(DB_URI)" "$(f)"

# Create a new migration
create-migration:
	@if [ -z "$(n)" ]; then echo "❌ Please specify a migration name with 'n=<name>'"; exit 1; fi
	@echo "📝 Creating new migration: $(n)"
	@uv run yoyo new -d "$(DB_URI)" migrations/$(n).py

