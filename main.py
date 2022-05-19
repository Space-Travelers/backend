from typing import Optional
from fastapi import Depends, FastAPI
from routers import router as minigames_router
from routers import router as players_router
from fastapi_utils.tasks import repeat_every
from utils.cronjobs import decrese_stats_players_in_db
app = FastAPI()

@app.get("/")
def root():
    return {"SpaceTravelers": "Bienvenidos a juegos para niños SpaceTravelers"}

@app.on_event("startup")
@repeat_every(seconds=60*10)
def decrease_stats_players()->None:
    decrese_stats_players_in_db()
    print("Decrease stats players")
  
app.include_router(minigames_router)
app.include_router(players_router)
