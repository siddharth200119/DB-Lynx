
from fastapi import APIRouter
from .health_check import router as health_check_router
from .database_server import router as database_server_router

router = APIRouter(prefix='/api')

router.include_router(health_check_router)
router.include_router(database_server_router)

__all__ = [router]
