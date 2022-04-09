from fastapi import APIRouter
from .minigames import router as minigames_router

router = APIRouter()
router.include_router(minigames_router, tags=["minigames"], prefix="/minigames")