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
        if not re.search(r'[A-Z]', value):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r'[0-9]', value):
            raise ValueError('Password must contain at least one number')
        if not re.search(r'[\W_]', value):
            raise ValueError('Password must contain at least one special character')
        return value


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    registered_at: datetime

class UserLogin(BaseModel):
    username: str = Field(min_length=3, max_length=50,description="The username of the user")
    password: str = Field(min_length=3, max_length=100, description="The pssword of the user")