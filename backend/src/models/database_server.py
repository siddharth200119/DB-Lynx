from typing import Dict, Optional
from pydantic import BaseModel
from src.enums import DatabaseDialects

class DatabaseServer(BaseModel):
    id: Optional[int]
    dialect: DatabaseDialects
    connection_string: str
    nickname: str

    @property
    def properties(self) -> Dict[str, str]:
        return self.dialect.value.parse(self.connection_string)
