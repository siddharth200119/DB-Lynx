from abc import ABC, abstractmethod
from types import ModuleType
from typing import Any, Optional, Dict, List
from PIL.Image import Image
from ..database import DataBase

class DatabaseDialect(ABC):
    def __init__(self, logo: Image, description: Optional[str] = None) -> None:
        super().__init__()
        self.logo: Image = logo
        self.description: Optional[str] = description

    @abstractmethod
    def parse(self, connection_string: str) -> Dict[str, Any]:
        pass

    @abstractmethod
    def test_connection(self, connection_string: str) -> bool:
        pass
    
    @abstractmethod
    def connect(self, connection_string: str) -> List[DataBase]:
        pass
