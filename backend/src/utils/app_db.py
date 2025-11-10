import sqlite3
import os
from typing import Optional, Tuple, Union
from dotenv import load_dotenv

load_dotenv()

DATABASE_PATH = os.getenv("DB_PATH", "app.db")

def get_db_connection() -> Tuple[Optional[sqlite3.Connection], Optional[sqlite3.Error]]:
    """Establishes a connection to the SQLite database."""
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        conn.row_factory = sqlite3.Row
        return conn, None
    except sqlite3.Error as e:
        return None, e

def execute_query(query, params=()):
    """
    Executes a given SQL query with optional parameters.

    Args:
        query (str): The SQL query to execute.
        params (tuple, optional): The parameters to substitute in the query. Defaults to ().

    Returns:
        tuple: A tuple containing a list of dictionaries (on success) or None (on failure),
               and an error message (on failure) or None (on success).
    """
    conn, err = get_db_connection()
    if err:
        return None, err

    try:
        cursor = conn.cursor()
        cursor.execute(query, params)

        # If cursor.description is not None, it's a query that returns rows.
        if cursor.description:
            results = [dict(row) for row in cursor.fetchall()]
        else:
            conn.commit()
            if query.strip().upper().startswith("INSERT"):
                results = {"last_row_id": cursor.lastrowid}
            else:
                results = {"message": "Query executed successfully."}

        conn.close()
        return results, None
    except sqlite3.Error as e:
        conn.close()
        return None, e
