from typing import Optional
from fastapi import Depends, FastAPI
from routers import router as minigames_router
from routers import router as players_router

app = FastAPI()

@app.get("/")
def root():
    return {"SpaceTravelers": "Bienvenidos a juegos para niños SpaceTravelers"}

app.include_router(minigames_router)
app.include_router(players_router)
