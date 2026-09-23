from pydantic import BaseModel, Field, EmailStr, model_validator, field_validator
from datetime import datetime
import re

class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50,description="The username of the user")
    email: EmailStr
    password: str = Field(min_length=8, max_length=100, description="The pssword of the user")


    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one digit")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError("Password must contain at least one special character")
        return value


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    registered_at: datetime

class UserLogin(BaseModel):
    username: str = Field(min_length=3, max_length=50,description="The username of the user")
    password: str = Field(min_length=8, max_length=100, description="The pssword of the user")