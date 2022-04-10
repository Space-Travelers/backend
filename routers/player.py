import email
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class PlayerRegister(BaseModel):
    name: str
    last_name:str
    email: str
    password: str
    age: int
    gender:str
    school:str

class PlayerLogin(BaseModel):
    email:str
    password:str

@router.post("/register")
async def register(player:PlayerRegister):
    return player

@router.post("/login")
async  def login(player:PlayerLogin):
    return player