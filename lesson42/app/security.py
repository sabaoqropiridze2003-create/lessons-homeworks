from pwdlib import PasswordHash
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from app.database import get_db
from sqlalchemy.orm import Session
from app.models.user import User

password_hasher = PasswordHash.recommended()

def hash_password(password :str):
    return password_hasher.hash(password)

def verify_password(password: str, hashed_password: str):
    return password_hasher.verify(password, hashed_password)

SECRET_KEY = "SABA"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTE = 120

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

# print(create_access_token({"user_id": 5}))

# def verify_token(token: str):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#     except JWTError:
#         return "Token invalid or expired. Please log in again"

#     return payload

# print(verify_token("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo1LCJleHAiOjE3OTAzODUzODV9.qZs6Xu86Ln5zULwuxXGsYXPs7E3xwdv47MMewr3k_uA"))

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_curent_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        user_id = payload.get("user_id")

        if not user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token invalid or expired, Please log in again")
        
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token invalid or expired, Please log in again")

    user = db.get(User, user_id)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token invalid or expired, Please log in again")
    
    return user 

def require_admin(current_user: User = Depends(get_curent_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="you don't have permision to access this route")

    return current_user
