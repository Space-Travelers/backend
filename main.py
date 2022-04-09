from typing import Optional
from fastapi import Depends, FastAPI
from routers import router as minigames_router

app = FastAPI()
app.include_router(minigames_router)
