from typing import List
from fastapi import APIRouter, HTTPException
from src.models.database_server import DatabaseServer
from src.enums.database_dialects import DatabaseDialects
from src.utils.app_db import execute_query

router = APIRouter()

@router.get("/", response_model=List[DatabaseServer])
async def list_database_servers():
    """
    Retrieves a list of all database server configurations.
    """
    query = "SELECT id, name, connection_string, dialect FROM database_servers"
    
    results, error = execute_query(query)
    
    if error:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve database servers: {error}")
        
    servers = []
    for row in results:
        # Convert the dialect string from the DB to a DatabaseDialects enum member
        dialect_enum_member = DatabaseDialects._missing_(row['dialect'])
        if not dialect_enum_member:
            # This case should ideally not happen if data is consistent.
            # We'll log a warning or handle it as an error, for now, we skip.
            print(f"Warning: Found an unknown dialect '{row['dialect']}' in the database.")
            continue

        servers.append(
            DatabaseServer(
                id=row['id'],
                nickname=row['name'], # map 'name' from db to 'nickname' in model
                connection_string=row['connection_string'],
                dialect=dialect_enum_member
            )
        )
        
    return servers
