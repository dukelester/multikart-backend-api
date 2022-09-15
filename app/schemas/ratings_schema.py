from datetime import datetime
from pydantic import BaseModel, validator

class RatingSchema(BaseModel):
    product_name: str
    rating: int
    comment: str
    rated_at: datetime
    
    @validator("product_name")
    def validate_product_name(cls, product_name):
        if type(product_name) != str or len(product_name) < 3 or len(product_name) > 100:
            raise ValueError("Invalid Product name ")
        return product_name
    
    @validator('rating')
    def validate_rating(cls,rating):
        if type(rating) != int or rating < 0 or rating is None or rating > 10:
            raise ValueError("This is an invalid rating")
        return rating
    
    @validator("comment")
    def validate_comment(cls, comment):
        if type(comment) != str or len(comment) < 10 or " " not in comment or len(comment) > 1000:
            raise ValueError("Invalid comment ..")
        return comment

class Rating(RatingSchema):
    id: int
    
    class Config:
        orm_mode = True