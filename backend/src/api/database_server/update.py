from typing import Optional
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.models.database_server import DatabaseServer
from src.enums.database_dialects import DatabaseDialects
from src.utils.app_db import execute_query

router = APIRouter()

class DatabaseServerUpdate(BaseModel):
    """
    Pydantic model for updating a database server. All fields are optional.
    """
    nickname: Optional[str] = None
    connection_string: Optional[str] = None
    dialect: Optional[DatabaseDialects] = None

@router.patch("/{server_id}", response_model=DatabaseServer)
async def update_database_server(server_id: int, server_update: DatabaseServerUpdate):
    """
    Updates a database server configuration by its ID. Only the provided
    fields will be updated.
    """
    # Get the fields that are actually set in the request body
    update_data = server_update.model_dump(exclude_unset=True)
    
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")

    # Map 'nickname' from the model to 'name' in the database
    if 'nickname' in update_data:
        update_data['name'] = update_data.pop('nickname')
        
    # Convert dialect enum to its string name for database storage
    if 'dialect' in update_data and update_data['dialect'] is not None:
        update_data['dialect'] = update_data['dialect'].name

    # Build the SET clause for the SQL query dynamically
    set_clause = ", ".join([f"{key} = ?" for key in update_data.keys()])
    params = list(update_data.values())
    params.append(server_id)
    
    query = f"UPDATE database_servers SET {set_clause} WHERE id = ?"
    
    _, error = execute_query(query, tuple(params))
    
    if error:
        raise HTTPException(status_code=500, detail=f"Failed to update database server: {error}")
        
    # After updating, fetch the full, updated record to return
    # This ensures the response body is accurate
    get_router = APIRouter() # A bit of a hack to reuse the get logic
    from .get import get_database_server as get_db_server
    return await get_db_server(server_id)
