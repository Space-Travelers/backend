from fastapi import APIRouter

from utils.minigames import quiz_game,def_game

router = APIRouter()

@router.get("/quiz")
async def quiz_game_route():
    return quiz_game()
    

@router.get("/definiciones")
async def definciones_game_route():
    return def_game()
    

