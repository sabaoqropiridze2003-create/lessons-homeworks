from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user import UserCreate, UserResponse, UserLogin
from app.database import get_db
from app.models.user import User
from app.security import hash_password, verify_password
from sqlalchemy.orm import Session

router = APIRouter(prefix="/user", tags=["users"])

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    existing_user_name = db.query(User).filter(user.username == user.username).first()

    if existing_user_name:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="There is existing account with this username")

    existing_user_email = db.query(User).filter(User.email == user.email).first()

    if existing_user_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="There is existing account with this email")

    hashed_password = hash_password(user.password)
    data = user.model_dump(exclude={"password"})

    new_user = User(**data, hashed_password = hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()

    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    return {"message": "Login successful", "user": db_user}