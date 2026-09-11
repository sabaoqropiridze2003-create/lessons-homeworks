from fastapi import FastAPI, Query, Path, HTTPException, status
from typing import List, Optional
from pydantic import BaseModel, Field, field_validator, model_validator

app = FastAPI(
    title="FastAPI",
    version="1.0.0",
    description="FastAPI project"
)

products = [
    {"id": 1, "name": "Apple", "price": 100, "is_available": True},
    {"id": 2, "name": "Banana", "price": 200, "is_available": False},
    {"id": 3, "name": "Orange", "price": 300, "is_available": True},
    {"id": 4, "name": "Grape", "price": 400, "is_available": False},
    {"id": 5, "name": "Strawberry", "price": 500, "is_available": True},
    {"id": 6, "name": "Blueberry", "price": 600, "is_available": False},
    {"id": 7, "name": "Apple", "price": 700, "is_available": True},
    {"id": 8, "name": "Pineapple", "price": 800, "is_available": False}
]


@app.get("/")
def read_root():
    return {"Hello": "World"}

# @app.get("/products")
# def read_products(category: str = None, limit:int = Query(10,ge=1), offset: int = 0):
#     return {
#         "category": category,
#         "limit": limit,
#         "offset": offset,
#     }


# @app.get("/products")
# def read_products(name: str | None = None, limit: int | None = None, is_available: bool = True):
#     filtered_products = products

#     if name:
#         filtered_products = [
#             product for product in filtered_products if product["name"].lower() == name.lower()]

#     if limit:
#         filtered_products = filtered_products[:limit]

#     # filtered_products = [product for product in filtered_products if product["is_available"] == is_available]

#     return filtered_products


# @app.get("/products/{product_id}")
# def read_product(product_id: int = Path(ge=1)):
#     for product in products:
#         if product["id"] == product_id:
#             return product
#     return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")


# @app.post("/products/create", status_code=status.HTTP_201_CREATED)
# def create_product(product: dict):
#     products.append(product)

#     return {
#         "message": "Product created",
#         "product": product
#     }


# class ProductCreate(BaseModel):
#     name: str = Field(min_length=3, max_length=20)
#     price: float = Field(gt=0)
#     is_available: bool = True
#     # description: Optional[str] = None
#     description: str | None = None
    
    

# @app.post("/products/create", status_code=status.HTTP_201_CREATED)
# def create_product(product: ProductCreate):
#     # print(type(product))
#     print(product.name)
#     print(product.price)
#     print(product.is_available)
#     print(product.description)

    
#     return {
#         "message": "product created",
#         "product": product
#     }

# class ProductCreate(BaseModel):
#     name: str
#     price: float
#     is_available: bool = True
#     description: str | None = None

#     @field_validator("name")
#     @classmethod
#     def name_must_be_uppercase(cls, value):
#         if value.islower():
#             raise ValueError("name must be uppercase")
#         return value.upper()

# @app.post("/products/create", status_code=status.HTTP_201_CREATED)
# def create_product(product: ProductCreate):
#     return {
#         "message": "product createed",
#         "product": product
#     }

# class ProductCreate(BaseModel):
#     price: float = Field(gt=0)
#     discount: float = Field(gt=0)

#     @model_validator(mode="after")
#     def check_discount(self):
#         if self.discount > self.price:
#             raise ValueError("discount must be less than price")
#         return self
    
# @app.post("/products/create", status_code=status.HTTP_201_CREATED)
# def create_product(product: ProductCreate):
#     return {
#         "message": "product createed",
#         "product": product
#     }

class ProductResponse(BaseModel):
    id: int
    name: str

@app.get("/products", response_model=List[ProductResponse])
def read_products():
    return products

class ProductDetailResponse(BaseModel):
    name: str
    price: float
    is_available: bool
    id: int
    
@app.get("/products/{product_id}", response_model=ProductDetailResponse)
def read_product(product_id: int = Path(ge=1)):
    for product in products:
        if product["id"] == product_id:
            return product
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

