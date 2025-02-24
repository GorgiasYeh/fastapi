import time
from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import trip
from .routers import user, info

retries = 5
while retries:
    try:
        models.Base.metadata.create_all(bind=engine)
        break  # DB 連線成功，跳出迴圈
    except Exception as e:
        print("等待資料庫啟動中...", e)
        time.sleep(2)
        retries -= 1

app = FastAPI()

app.include_router(user.router)
app.include_router(info.router)
app.include_router(trip.router)

@app.get("/")
def read_root():
    return {"Hello": "我在測試 FastAPI的自動部署"}

