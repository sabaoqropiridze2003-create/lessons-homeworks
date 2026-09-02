from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "world"}

# @app.get("/info")
# def read_info():
#     return {"name": "my first app",
#             "version": "1.0",
#             "description": "my first app"
#             }

# @app.get("/users")
# def read_users():
#     return [{"id":1, "name": "girogi", "grade":100},
#             {"id":2, "name": "saba", "grade":78},
#             {"id":3, "name": "anano", "grade":86}
#             ]


products_db = {
    1: {"name": "Laptop", "price": 1200.0, "in_stock": True},
    2: {"name": "Mouse", "price": 25.0, "in_stock": True},
    3: {"name": "Keyboard", "price": 75.0, "in_stock": False}
}


@app.get("/products")
def get_all_products():
    return products_db


@app.get("/info")
def get_info():
    return {"name": "My API", "verison": "1.0.0"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/products")
def create_product(product: dict):
    return {"message": "created product", "product": product}

@app.put("/update")
def update_product(new_product: dict):
    return {"message": "updated product", "product": new_product}

@app.patch("/update_items")
def patch_product(new_product: dict):
    return{"message": "updated product", "product": new_product}

@app.delete("/delete_item")
def delete_product(id: int):
    return {"message": "deleted product", "deleted product with id": id}