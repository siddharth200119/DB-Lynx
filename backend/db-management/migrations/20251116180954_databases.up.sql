-- Migration: databases
-- Created: 2025-11-16T18:09:54+05:30
-- Direction: UP

CREATE TABLE databases (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  dialect TEXT,
  connection_string TEXT
)
