from typing import Dict, Optional, Tuple
from sqlalchemy import Engine, Result
from sqlalchemy.engine.reflection import Inspector
from sqlalchemy import create_engine, inspect, text

class DataBase():
    def __init__(self, name: str, size: int, connection_string: str) -> None:
        self.name = name
        self.size = size
        self.connection_string = connection_string
        self.db_engine : Optional[Engine] = None
        self.internals: Optional[Inspector] = None

    def connect(self, return_internals: bool = False) -> Optional[Inspector]:
        if(not self.db_engine):
            self.db_engine = create_engine(self.connection_string)
            if return_internals:
                internals = inspect(self.db_engine)
                self.internals = internals
                return self.internals

    def query(self, query: str, params: Dict[str, str]) -> Result:
        self.connect()
        with self.db_engine.connect() as conn:
            result = conn.execute(text(query), params)
            return result
