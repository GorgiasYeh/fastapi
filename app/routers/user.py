from fastapi import HTTPException, Response, status, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    tags=['Users']
)

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=schemas.User)
def register(new_user: schemas.CreateUser, response: Response, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(
        (models.User.email == new_user.email) |
        (models.User.userName == new_user.userName)
    ).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="已被註冊"
        )
    
    user = models.User(**new_user.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.post("/login")
def register(login_user: schemas.LoginUser, response: Response, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.userName == login_user.userName).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="無此使用者")
    
    if not user.password == login_user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="密碼錯誤")
    
    return {"message":"ok"}