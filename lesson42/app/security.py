from pwdlib import PasswordHash
from jose import jwt, JWTError
from datetime import datetime, timedelta

password_hasher = PasswordHash.recommended()

def hash_password(password :str):
    return password_hasher.hash(password)

def verify_password(password: str, hashed_password: str):
    return password_hasher.verify(password, hashed_password)

SECRET_KEY = "SABA"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTE = 10

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