from fastapi import APIRouter, HTTPException, status
from src.utils.app_db import execute_query

router = APIRouter()

@router.delete("/{server_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_database_server(server_id: int):
    """
    Deletes a database server configuration by its ID.
    """
    # To provide a 404 if not found, we can check existence first,
    # or check the number of affected rows after DELETE.
    # Checking first gives a clearer intent.
    
    # For SQLite, we can't easily get the number of affected rows from execute_query,
    # so we'll check for existence before deleting.
    
    get_query = "SELECT id FROM database_servers WHERE id = ?"
    get_results, get_error = execute_query(get_query, (server_id,))

    if get_error:
        raise HTTPException(status_code=500, detail=f"Failed to check for database server: {get_error}")

    if not get_results:
        raise HTTPException(status_code=404, detail=f"Database server with id {server_id} not found")

    # If it exists, delete it
    delete_query = "DELETE FROM database_servers WHERE id = ?"
    _, delete_error = execute_query(delete_query, (server_id,))
    
    if delete_error:
        raise HTTPException(status_code=500, detail=f"Failed to delete database server: {delete_error}")
        
    # Return with a 204 status code, so no response body is needed.
    return
