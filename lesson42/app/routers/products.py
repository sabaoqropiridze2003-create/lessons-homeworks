from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from app.models.product import Product
from app.models.category import Category
from app.database import get_db, get_async_db
from sqlalchemy.orm import Session
from app.schemas.product import ProductCreate, ProductResponse, ProductUpdate
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from pathlib import Path
from uuid import uuid4
UPLOAD_FOLDER = Path("uploads/products")

router = APIRouter(prefix="/products", tags=["products"])


########ORIGINAL###################

# @router.get("/", response_model=list[ProductResponse])
# def get_products(page: int | None = 1, limit: int | None = 3,db: Session = Depends(get_db)):


#     total = db.query(Product).all()

#     offset = (page - 1) * limit

#     products = db.query(Product).offset(offset).limit(limit).all()

#     return products


##################async version##############
@router.get("/")
async def get_products(page: int | None = 1, limit: int | None = 3, db: AsyncSession = Depends(get_async_db)):
    total_procts_query = await db.execute(select(func.count(Product.id)))

    total = total_procts_query.scalar()

    offset = (page - 1) * limit

    products = await db.execute(select(Product).offset(offset).limit(limit))

    product_list = products.scalars().all()

    return {
        "total": total,
        "products": product_list
    }


#######original################
# @router.post("/create", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
# def create_product(product: ProductCreate, db: Session = Depends(get_db)):
#     category = db.get(Category, product.category_id)

#     if not category:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

#     new_product = Product(**product.model_dump())

#     db.add(new_product)
#     db.commit()
#     db.refresh(new_product)

#     return new_product

##################async version#####################

# @router.post("/create", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
# async def create_product(product: ProductCreate, db: AsyncSession = Depends(get_async_db)):
#     category = await db.get(Category, product.category_id)

#     if not category:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

#     new_product = Product(**product.model_dump())

#     db.add(new_product)
#     await db.commit()
#     await db.refresh(new_product)

#     return new_product

###################adding images###############

@router.post("/create", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(
    product: ProductCreate = Depends(ProductCreate.as_form),
    image: UploadFile = File(...),
    db: Session = Depends(get_db)):

    category = db.get(Category, product.category_id)

    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="category not found")

    extensions = Path(image.filename).suffix.lower()
    allowed_exstensions = [".jpg", ".jpeg", ".png", ".webp"]

    if extensions not in allowed_exstensions:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="invalid image extension")

    filename = f"{uuid4()}{extensions}"
    file_path = UPLOAD_FOLDER / filename

    UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

    with file_path.open("wb") as buffer:
        buffer.write(image.file.read())

    new_product = Product(
        **product.model_dump(),
        image = f"/uploads/products/{filename}"
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.get(Product, product_id)

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    return product

@router.put("/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
def update_product(product_id: int, product: ProductUpdate , db: Session = Depends(get_db)):
    product_to_update = db.get(Product, product_id)

    if not product_to_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    if product.category_id is not None:
        category = db.get(Category, product.category_id)

        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

    data = product.model_dump(exclude_unset=True).items()

    for field, value in data:
        setattr(product_to_update, field, value)

    db.commit()
    db.refresh(product_to_update)

    return product_to_update

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product_to_delete = db.get(Product, product_id)

    if not product_to_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    db.delete(product_to_delete)
    db.commit()

    return {"detail": "Product deleted successfully"}