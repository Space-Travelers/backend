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
    text:int

class PlayerLogin(BaseModel):
    email:str
    password:str