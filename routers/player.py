
from fastapi import APIRouter
from utils.player import login_accepted, player_stats, register_player, authentication_player, stats_update
from models.player import PlayerRegister, PlayerLogin, StatsUpdate
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
        login_accepted(player)
        return  player_login
    return {"Player not logged"}

@router.post("/statistics")
async  def updateStats(player:StatsUpdate):
    if(stats_update(player)):
        print(player_stats(player))
        player_updated = player_stats(player)
        return player_updated
    return {"message:" "Player not updated"}

