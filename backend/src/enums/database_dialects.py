from enum import Enum
from src.classes.database_dialect.postgresql import PostgresqlDialect

class DatabaseDialects(Enum):
    POSTGRESQL = PostgresqlDialect(logo=None)

    @classmethod
    def _missing_(cls, value):
        if isinstance(value, str):
            for member in cls:
                if member.name == value.upper():
                    return member
        return None
