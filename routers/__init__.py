from fastapi import APIRouter
from .minigames import router as minigames_router
from .player import router as players_router

router = APIRouter()



router.include_router(minigames_router, tags=["minigames"], prefix="/minigames")
router.include_router(players_router, tags=["player"], prefix="/player")
