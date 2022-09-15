from fastapi import APIRouter, Depends, HTTPException
from app.crud import ratings_crud
from app.dependencies.database_dependency import get_db
from sqlalchemy.orm import Session
from app.schemas.ratings_schema import RatingSchema,Rating

router = APIRouter(
    prefix="/ratings",
    tags=["ratings"]
    
)

@router.get("/", status_code=200)
def allRatings(db: Session = Depends(get_db) ):
    return ratings_crud.get_all_ratings(db)

@router.post("/search", response_model=Rating)
def getRatingsByName(product_name: str, db: Session = Depends(get_db) ):
    if len(ratings_crud.get_all_ratings(db)) > 0:
        print(product_name)
        return ratings_crud.get_rating_by_product_name(db,product_name=product_name)
    raise HTTPException( status_code=400, detail="No Ratings found ...")

@router.post('/', response_model=Rating, status_code=201, tags=['create a new rating'])
def addRating(rating: RatingSchema,db: Session = Depends(get_db)):
    print(rating)
    return ratings_crud.create_new_rating(db=db, rating=rating)