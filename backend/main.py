from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI

app = FastAPI()

if __name__ == '__main__':
    import os
    import uvicorn

    host: str = os.environ.get('HOST', '127.0.0.1')
    port: int = int(os.environ.get('PORT', '42069'))
    env: str = os.environ.get('ENV', 'DEV')
    
    uvicorn.run('main:app', host=host, port=port, reload=env.lower() == 'dev')
