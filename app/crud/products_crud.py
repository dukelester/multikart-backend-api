from sqlalchemy.orm import Session
from models.products_models import Product
from schemas import products_schema

def get_all_products(db: Session):
    return db.query(Product).filter(Product.isActive == True).all()

def create_product(db: Session, product: products_schema.ProductsSchema):
    new_product = Product( 
                          product_id=product.product_id,
        product_title = product.product_title, description=product.description,category=product.category,
        price=product.price,quantity_in_stock=product.quantity_in_stock,isActive=product.isActive,
        created_at=product.created_at
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product
    
    