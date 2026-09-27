from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user import UserCreate, UserResponse, UserLogin
from app.database import get_db
from app.models.user import User
from app.security import hash_password, verify_password, create_access_token, get_curent_user, require_admin
from sqlalchemy.orm import Session


router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    existing_user_name = db.query(User).filter(User.username == user.username).first()

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

    access_token = create_access_token(data={"user_id": db_user.id})

    return {
        "token": access_token,
        "token_type": "bearer" 
    }

# @router.get("/me")
# def get_me(token: str = Depends(oauth2_scheme)):
#     print(token)

#     return token

@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_curent_user)):
    return current_user

@router.get("/", response_model=list[UserResponse])
def get_users(current_user: User = Depends(require_admin),db: Session = Depends(get_db)):
    users = db.query(User).all()

    return users

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, curent_user: User = Depends(require_admin), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    return user