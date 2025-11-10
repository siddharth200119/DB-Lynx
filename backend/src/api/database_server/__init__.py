from fastapi import APIRouter

from . import create, delete, get, list, update

router = APIRouter(
    prefix="/database-server",
    tags=["Database Server"],
)

router.include_router(create.router)
router.include_router(delete.router)
router.include_router(get.router)
router.include_router(list.router)
router.include_router(update.router)
