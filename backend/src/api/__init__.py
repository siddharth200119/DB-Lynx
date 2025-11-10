
from fastapi import APIRouter
from .health_check import router as health_check_router

router = APIRouter(prefix='/api')

router.include_router(health_check_router)

__all__ = [router]
