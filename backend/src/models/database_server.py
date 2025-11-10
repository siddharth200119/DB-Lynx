from typing import Dict, Optional
from pydantic import BaseModel, field_serializer
from src.enums import DatabaseDialects

class DatabaseServer(BaseModel):
    id: Optional[int] = None
    dialect: DatabaseDialects
    connection_string: str
    nickname: str

    @field_serializer('dialect')
    def serialize_dialect(self, dialect: DatabaseDialects, _info):
        return dialect.name

    @property
    def properties(self) -> Dict[str, str]:
        return self.dialect.value.parse(self.connection_string)
