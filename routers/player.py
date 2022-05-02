
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
    print(authentication_player(player))
    player_login = authentication_player(player)
    if(player_login):
        return  player_login
    return {"Player not logged"}


