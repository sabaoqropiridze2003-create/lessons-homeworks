from pydantic import BaseModel, Field, EmailStr, model_validator, field_validator
from datetime import datetime
import re

class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50,description="The username of the user")
    email: EmailStr
    password: str = Field(min_length=8, max_length=100, description="The pssword of the user")
    confirm_password: str = Field(min_length=8, max_length=100, description="The confirmation pssword of the user")

    @model_validator(mode="before")
    def passwords_match(cls, value):
        password = value.get("password")
        confirm_password = value.get("confirm_password")
        if password != confirm_password:
            raise ValueError("Passwords do not match, please write correct password")
        return value

    @field_validator("password")
    def validate_password_strength(cls, password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long") 
        if not re.search(r"[A-Z]", password):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", password):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", password):
            raise ValueError("Password must contain at least one digit")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise ValueError("Password must contain at least one special character")
        return password


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    registered_at: datetime

class UserLogin(BaseModel):
    username: str = Field(min_length=3, max_length=50,description="The username of the user")
    password: str = Field(min_length=8, max_length=100, description="The pssword of the user")