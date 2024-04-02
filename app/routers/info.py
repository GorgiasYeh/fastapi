import random
import string
from fastapi import APIRouter, Depends

from app import oauth2, schemas
from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/Info",
    tags=['Info']
)

def random_color():
    # 生成隨機色碼，格式為 #RRGGBB
    return f'#{"".join(random.choices(string.hexdigits[:16], k=6))}'

@router.get("/", response_model=schemas.InfoPydantic)
def getInfo(db: Session =Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    info = schemas.InfoPydantic(
        deviceName= random.choice(['爺爺', '奶奶', '爸爸', '媽媽', '兒子', '女兒']),
        power= random.randint(0, 100),
        trackingModeColor=random_color(),
        connected=random.choice(['Y', 'N']),
        connectStatus=random.choice(['onLine', 'offLine']),
        step=random.randint(1000, 10000),
        lockMode=random.choice(['Y', 'N']))
    
    return info