from fastapi import APIRouter

from utils.minigames import challenge_type

router = APIRouter()

@router.get("/{challenge}")
async def minigame_type(challenge:str):
    return challenge_type(challenge)
    
@router.get("/")
async def minagames():
    return {"message": "Welcome to the quiz game"}