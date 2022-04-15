import email
from fastapi import APIRouter
from utils.player import register_player, authentication_player
from models.player import PlayerRegister, PlayerLogin
router = APIRouter()


@router.post("/register")
async def register(player:PlayerRegister):
    if(register_player(player)):
        return {"message:" "Player registered"}
    return {"message:" "Player not registered"}

@router.post("/login")
async  def login(player:PlayerLogin):
    if(authentication_player(player)):
        return {"message:" "Player logged"}
    return {"message:" "Player not logged"}


