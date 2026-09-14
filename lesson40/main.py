from fastapi import FastAPI, status


from database import SessionLocal
from models import Product

app = FastAPI()

# @app.post("/products")
# def create_product():
#     db = SessionLocal()

#     new_product = Product(name="hard coded car", price=15000.0, in_stock=True)

#     db.add(new_product)
#     db.commit()
#     db.refresh(new_product)

#     db.close()

#     return {"message": "product created", "id": new_product.id}


# @app.get("/products")
# def get_products():
#     db = SessionLocal()
#     products = db.query(Product).all()
#     db.close()
#     return products



#depandency injection ვარიანტი

# from sqlalchemy.orm import Session
# from database import get_db
# from fastapi import Depends

# @app.post("/products")
# def create_product(db: Session = Depends(get_db)):
#     new_product = Product(name="RTX 5090", price=10000.0, in_stock=True)

#     db.add(new_product)
#     db.commit()
#     db.refresh(new_product)
#     return {"message": "Product created", "id":new_product.id}

# @app.get("/products")
# def get_products(db: Session = Depends(get_db)):
#     products = db.query(Product).all()
#     return products

# @app.get("/products/{id}")
# def get_product(id: int, db: Session = Depends(get_db)):
#     product = db.query(Product).filter(Product.id == id).first()
#     return product

# @app.put("/product_update/{id}")
# def update_product(id:int, db: Session = Depends(get_db)):
#     exs_product = db.query(Product).filter(Product.id == id).first()
#     exs_product.name = "updated name"
#     exs_product.price = 2000.0
#     exs_product.in_stock = True

#     db.add(exs_product)
#     db.commit()

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import ProductCreate, ProductResponse

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
    new_product = Product(**product.model_dump())
    
