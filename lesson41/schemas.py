from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0)
    stock: int = Field(default=0, ge=0)
    is_available: bool = Field(default=True)
    description: str | None = Field(default=None, max_length=500)
class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    stock: int
    is_available: bool
    description: str | None = None

    class Config:
        from_attributes = True