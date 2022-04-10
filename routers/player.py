import email
from fastapi import APIRouter
from pydantic import BaseModel
from utils.player import register_player
router = APIRouter()

class PlayerRegister(BaseModel):
    name: str
    last_name:str
    email: str
    password: str
    age: int
    level: str
    gender:str
    school:str

class PlayerLogin(BaseModel):
    email:str
    password:str

@router.post("/register")
async def register(player:PlayerRegister):
    if(register_player(player)):
        return {"message:" "Player registered"}
    return {"message:" "Player not registered"}

@router.post("/login")
async  def login(player:PlayerLogin):
    return player