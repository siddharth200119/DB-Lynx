from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from src.api import router as api_routes
from src.events import router as event_routes

app = FastAPI()

app.include_router(router=api_routes)
app.include_router(router=event_routes)

if __name__ == '__main__':
    import uvicorn
    import os
    
    host = os.environ.get('HOST', '127.0.0.1')
    try:
        port = int(os.environ.get('PORT', '8000'))
    except Exception as e:
        port = 8000

    env = os.environ.get('ENV', 'DEV')

    uvicorn.run('main:app', host=host, port=port, reload=env.lower() == 'dev')
