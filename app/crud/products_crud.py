from pydantic import ValidationError
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.products_models import Product
from app.schemas import products_schema

def get_all_products(db: Session):
    return db.query(Product).filter(Product.isActive == True).all()

def check_if_exists(db: Session, product: products_schema.ProductsSchema):
    return bool(db.query(Product).filter(Product.product_id == product.product_id).first())

def create_product(db: Session, product: products_schema.ProductsSchema):
    if check_if_exists(db=db, product=product):
        raise HTTPException( status_code=400, detail="The product with that Id already Exists!")
    try:
        new_product = Product( product_id=product.product_id,
            product_title = product.product_title, description=product.description,category=product.category,
            price=product.price,quantity_in_stock=product.quantity_in_stock,isActive=product.isActive,
            created_at=product.created_at
        )
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product
    except ValidationError as e:
        print(e)
        raise e
        
    