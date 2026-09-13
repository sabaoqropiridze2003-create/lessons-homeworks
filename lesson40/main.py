from fastapi import FastAPI
from starlette import status

from database import SessionLocal
from models import Product

app = FastAPI()

@app.post("/products")
def create_product():
    db = SessionLocal()

    new_product = Product(name="hard coded car", price=15000.0, in_stock=True)

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    db.close()

    return {"message": "product created", "id": new_product.id}


@app.get("/products")
def get_products():
    db = SessionLocal()
    products = db.query(Product).all()
    db.close()
    return products