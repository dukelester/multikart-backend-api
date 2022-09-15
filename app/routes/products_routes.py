from fastapi import APIRouter, Depends
from schemas.products_schema import ProductsSchema
from sqlalchemy.orm import Session
from dependencies import database_dependency
from crud import products_crud

router = APIRouter(
    prefix="/products",
    tags=['products routes']
)

@router.get("/", tags=['All Products'])
def allProducts(db: Session = Depends(database_dependency.get_db)):
    all_products = products_crud.get_all_products(db) 
    return { " all": all_products }

@router.post("/", tags=["Add a new Product"], status_code=201, response_model=ProductsSchema)
def addProduct(*,db: Session = Depends(database_dependency.get_db), product: ProductsSchema):
    product = products_crud.create_product(db, product)
    return { "success": product }
