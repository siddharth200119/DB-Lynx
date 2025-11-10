"""
Recreate database_servers table to use a connection string
"""

from yoyo import step

__depends__ = {}

steps = [
    step(
        """
        CREATE TABLE database_servers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            connection_string TEXT NOT NULL,
            dialect TEXT NOT NULL,
            show_all_databases BOOLEAN NOT NULL DEFAULT 0
        );
        """,
        """
        DROP TABLE database_servers;
        """
    )
]
