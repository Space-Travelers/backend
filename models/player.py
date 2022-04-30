from pydantic import BaseModel

class PlayerRegister(BaseModel):
    name: str
    last_name:str
    email: str
    password: str
    age: int
    level: str
    gender:str
    school:str
    avatar:str

class PlayerLogin(BaseModel):
    email:str
    password:str



class StatsUpdate(BaseModel):
    email:str
    statistic:str
    points:int