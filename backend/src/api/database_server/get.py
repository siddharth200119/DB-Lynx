from fastapi import APIRouter, HTTPException
from src.models.database_server import DatabaseServer
from src.enums.database_dialects import DatabaseDialects
from src.utils.app_db import execute_query

router = APIRouter()

@router.get("/{server_id}", response_model=DatabaseServer)
async def get_database_server(server_id: int):
    """
    Retrieves a single database server configuration by its ID.
    """
    query = "SELECT id, name, connection_string, dialect FROM database_servers WHERE id = ?"
    params = (server_id,)
    
    results, error = execute_query(query, params)
    
    if error:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve database server: {error}")
        
    if not results:
        raise HTTPException(status_code=404, detail=f"Database server with id {server_id} not found")
        
    row = results[0]
    
    dialect_enum_member = DatabaseDialects._missing_(row['dialect'])
    if not dialect_enum_member:
        # This indicates inconsistent data in the database.
        raise HTTPException(status_code=500, detail=f"Unknown dialect '{row['dialect']}' found for server id {server_id}")

    server = DatabaseServer(
        id=row['id'],
        nickname=row['name'], # map 'name' from db to 'nickname' in model
        connection_string=row['connection_string'],
        dialect=dialect_enum_member
    )
        
    return server
