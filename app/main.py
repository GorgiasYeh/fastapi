from fastapi import FastAPI
from app.database import  engine
from app import models
from app.routers import trip
from .routers import user, info

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(info.router)
app.include_router(trip.router)

@app.get("/")
def read_root():
    return {"Hello": "World"} 

