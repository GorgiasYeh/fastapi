from fastapi import HTTPException, Response, status, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import oauth2
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

@router.post("/login", response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.userName == user_credentials.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="無此使用者")
    
    if not user.password == user_credentials.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="密碼錯誤")
    
    access_token = oauth2.create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/info", response_model=schemas.User)
def getInfo(db: Session =Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    print(current_user)
    
    # user =  db.query(models.User).filter(id=current_user).first()
    
    return current_user