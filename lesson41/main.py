from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal, engine, get_db
from models import Base, Product
from schemas import ProductCreate, ProductResponse





app = FastAPI(
    title="my first API",
    version="1.0.0",
    description="this is a simple api built with fastapi",
)




@app.get("/products", response_model=list[ProductResponse])
def get_all_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products

@app.get("/products/{product_id}", response_model=list[ProductResponse])
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product



@app.post("/products", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    db_product.name = product.name
    db_product.price = product.price
    db_product.stock = product.stock
    db_product.is_available = product.is_available
    db_product.description = product.description
    db_product.rating = product.rating  # Update the rating field

    db.commit()
    db.refresh(db_product)
    return db_product


@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted successfully"}