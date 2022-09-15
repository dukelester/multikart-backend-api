from datetime import datetime
from pydantic import BaseModel

class RatingSchema(BaseModel):
    product_name: str
    rating: int
    comment: str
    rated_at: datetime
    
    
class Rating(RatingSchema):
    id: int
    
    class Config:
        orm_mode = True