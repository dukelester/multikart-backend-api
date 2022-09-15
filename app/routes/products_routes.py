from fastapi import APIRouter

router = APIRouter(
    prefix="/products",
    tags=['products routes']
)

@router.get("/", tags=['All Products'])
def allProducts():
    return { " all": "Products " }