from fastapi import FastAPI, Query, Path

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

@app.get("/products")
def read_products(name: str | None = None, limit: int | None = None, is_available: bool = True):
    filtered_products = products

    if name:
        filtered_products = [product for product in filtered_products if product["name"].lower() == name.lower()]

    if limit:
        filtered_products = filtered_products[:limit]

    filtered_products = [product for product in filtered_products if product["is_available"] == is_available]

    return filtered_products

@app.get("/products/{product_id}")
def read_product(product_id: int = Path(ge=1)):
    for product in products:
        if product["id"] == product_id:
            return product
    return {"error": "Product not found"}
