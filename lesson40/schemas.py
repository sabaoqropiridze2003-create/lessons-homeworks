from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0)
    in_stock: bool = Field(default=True)

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool

    class Config:
        from_attributes = True