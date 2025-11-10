
"""
create database_servers table
"""

from yoyo import step

__depends__ = {}

steps = [
    step(
        """
        CREATE TABLE database_servers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dialect TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            host TEXT NOT NULL,
            port INTEGER NOT NULL,
            default_database TEXT NOT NULL,
            show_all_databases BOOLEAN NOT NULL DEFAULT 0
        );
        """,
        """
        DROP TABLE database_servers;
        """
    )
]
