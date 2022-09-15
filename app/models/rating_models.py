from datetime import datetime
from email.policy import default
from operator import index
from sqlalchemy import String, Integer, Column, Boolean, ForeignKey, Float,DateTime
from sqlalchemy.orm import relationship
from app.database.database import Base

class Rating(Base):
    __tablename__='ratings'
    id = Column(Integer, primary_key=True)
    product_name = Column(String, index=True)
    rating = Column(Integer, index=True)
    rated_at = Column(DateTime, default=datetime.now())
    comment = Column(String, index=True)