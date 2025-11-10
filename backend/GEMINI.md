# Project Knowledge Base (GEMINI.md)

## Overview

This project is a FastAPI backend for a "DB-Ninja" application. It seems to be a tool for managing connections to multiple database servers.

## Core Technologies

*   **Backend Framework:** FastAPI
*   **Programming Language:** Python 3.12+
*   **Package Manager:** `uv`
*   **Database:** SQLite (for the application's own data)
*   **Database Migrations:** `yoyo-migrations`
*   **Environment Management:** `python-dotenv`

## Project Structure

*   `main.py`: The main entry point for the FastAPI application.
*   `src/`: The main source code directory.
    *   `api/`: Contains the API endpoints.
        *   `database_servers/`: Endpoints for managing database servers (`/api/database-servers`).
        *   `health_check/`: A health check endpoint.
    *   `enums/`: Contains enum-like structures (using `typing.Literal`).
        *   `database_dialects.py`: Defines the supported database dialects.
    *   `models/`: Contains Pydantic models.
        *   `database.py`: Defines the `DatabaseServer` model.
    *   `utils/`: Contains utility functions.
        *   `app_db.py`: Utility for connecting to the local SQLite database (`app.db`) and executing queries.
*   `migrations/`: Contains database migration scripts for `yoyo-migrations`.
*   `.env`: Environment variable configuration file.
*   `pyproject.toml`: Project metadata and dependencies.
*   `yoyo.ini`: Configuration for `yoyo-migrations`.
*   `Makefile`: Contains useful commands for database migrations.

## Database

*   The application uses a local SQLite database named `app.db` to store its own data.
*   The `database_servers` table stores the connection information for other databases.
*   The table schema is defined in `migrations/20251108_01_r9NNN-databases-table.py`.

## API Endpoints

The main API is prefixed with `/api`.

*   **`POST /api/database-servers`**: Creates a new database server connection configuration.
*   **`GET /api/database-servers`**: Retrieves a list of all database server configurations.
*   **`GET /api/database-servers?id={id}`**: Retrieves a single database server configuration by its ID.
*   **`POST /api/database-servers/test-connection`**: Tests the connection to a given database server.

## Supported Database Dialects

The application aims to support connecting to the following databases:
*   PostgreSQL
*   SQLite
*   MSSQL
*   MySQL
*   MongoDB

## How to Run

1.  Install dependencies from `pyproject.toml` using `uv`.
2.  Run the application: `uv run main`.

## Makefile Commands

The `Makefile` provides several commands for managing database migrations with `yoyo-migrations`:

*   `make init`: Initializes the migrations directory.
*   `make db-migrate`: Applies all pending migrations.
*   `make db-rollback`: Rolls back the last migration.
*   `make db-migrate-file f=<path>`: Applies a specific migration file.
*   `make db-rollback-file f=<path>`: Rolls back a specific migration file.
*   `make create-migration n=<name>`: Creates a new migration file.
