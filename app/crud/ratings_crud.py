from sqlalchemy.orm import Session
from app.models.rating_models import Rating
from app.schemas.ratings_schema import RatingSchema
from pydantic import ValidationError

def get_all_ratings(db: Session):
    return db.query(Rating).all()

def check_for_rating(db: Session, rating: RatingSchema):
    if db.query(Rating).filter(Rating.id == rating.id).first():
        return True
    return False

def get_rating_by_product_name(db: Session, product_name:str):
    return db.query(Rating).filter(Rating.product_name == product_name)

def create_new_rating(db: Session, rating: RatingSchema):
    try:
        new_rating = Rating(
            product_name = rating.product_name,
            rating = rating.rating,
            comment= rating.comment,
            rated_at = rating.rated_at,
            # id=rating.id
        )
        db.add(new_rating)
        db.commit()
        db.refresh(new_rating)
        return new_rating
    except ValidationError as e:
        print(e)
        raise e