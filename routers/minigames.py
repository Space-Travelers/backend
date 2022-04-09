from fastapi import APIRouter

from utils.minigames import challenge_type

router = APIRouter()

@router.get("/{challenge}")
async def quiz_game_route(challenge:str):
    return challenge_type(challenge)
    
