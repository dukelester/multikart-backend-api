from fastapi import APIRouter, Depends
from app.schemas.products_schema import ProductsSchema
from sqlalchemy.orm import Session
from app.dependencies import database_dependency
from app.crud import products_crud

router = APIRouter(
    prefix="/products",
    tags=['products routes']
)

@router.get("/", tags=['All Products'])
def allProducts(db: Session = Depends(database_dependency.get_db)):
    return  products_crud.get_all_products(db) 

@router.post("/", tags=["Add a new Product"], status_code=201, response_model=ProductsSchema)
def addProduct(*,db: Session = Depends(database_dependency.get_db), product: ProductsSchema):
    product = products_crud.create_product(db=db, product=product)
    return { "success": product }
