from .base import DatabaseDialect
from PIL.Image import Image
from typing import Optional, Any, Dict, List
from urllib.parse import urlparse
from sqlalchemy import create_engine, engine, text
from sqlalchemy.exc import SQLAlchemyError
from ..database import DataBase

class PostgresqlDialect(DatabaseDialect):
    def __init__(self, logo: Image, description: Optional[str] = None) -> None:
        super().__init__(logo, description)

    def parse(self, connection_string: str) -> Dict[str, Any]:
        parsed = urlparse(connection_string)

        return {
            "scheme": parsed.scheme,
            "user": parsed.username,
            "password": parsed.password,
            "host": parsed.hostname,
            "port": parsed.port,
            "database": parsed.path.lstrip("/"),
        }

    def test_connection(self, connection_string: str) -> bool:
        """
        Test a PostgreSQL connection using SQLAlchemy.
        Returns True if successful, False otherwise.
        """
        try:
            engine = create_engine(connection_string)
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            return True
        except SQLAlchemyError as e:
            print(f"Connection failed: {e}")
            return False

    def connect(self, connection_string: str, list_all_databases: bool = False) -> List[DataBase]:
        databases: List[DataBase] = []
        parsed_url = urlparse(connection_string)

        if list_all_databases:
            # Connect to the default 'postgres' database to query for all databases
            # This is a common practice for PostgreSQL administration tasks.
            admin_db_url = parsed_url._replace(path="/postgres").geturl()
            try:
                engine = create_engine(admin_db_url)
                with engine.connect() as conn:
                    # Query for all non-template databases and their sizes.
                    query = text("SELECT datname, pg_database_size(datname) FROM pg_database WHERE datistemplate = false;")
                    result = conn.execute(query)
                    for row in result:
                        db_name, db_size = row[0], row[1]
                        db_connection_string = parsed_url._replace(path=f"/{db_name}").geturl()
                        databases.append(DataBase(name=db_name, size=db_size, connection_string=db_connection_string))
            except SQLAlchemyError as e:
                print(f"Error while listing all databases: {e}")
                # Depending on desired error handling, you might want to raise or log.
                return []
        else:
            # Connect to the single, specified database.
            db_name = parsed_url.path.lstrip("/")
            if not db_name:
                # Cannot connect if no database is specified in the URI
                return []
            
            try:
                engine = create_engine(connection_string)
                with engine.connect() as conn:
                    # Get the size of the specified database.
                    query = text("SELECT pg_database_size(:db_name)")
                    size_result = conn.execute(query, {"db_name": db_name}).scalar_one_or_none()
                    db_size = size_result if size_result is not None else 0
                    
                    database = DataBase(name=db_name, size=db_size, connection_string=connection_string)
                    databases.append(database)
            except SQLAlchemyError as e:
                print(f"Error connecting to database '{db_name}': {e}")
                # Depending on desired error handling, you might want to raise or log.
                return []
                
        return databases
