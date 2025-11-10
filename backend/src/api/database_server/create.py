from fastapi import APIRouter, HTTPException
from src.models.database_server import DatabaseServer
from src.utils.app_db import execute_query

router = APIRouter()

@router.post("/", response_model=DatabaseServer, status_code=201)
async def create_database_server(server: DatabaseServer):
    """
    Creates a new database server configuration.
    """
    query = """
        INSERT INTO database_servers (name, connection_string, dialect)
        VALUES (?, ?, ?)
    """
    
    # The model uses 'nickname', but the table has 'name'. We map it here.
    # The dialect is stored as the name of the enum member (e.g., "POSTGRESQL").
    params = (server.nickname, server.connection_string, server.dialect.name)
    
    result, error = execute_query(query, params)
    
    if error:
        raise HTTPException(status_code=500, detail=f"Failed to create database server: {error}")
        
    server.id = result["last_row_id"]
    return server
