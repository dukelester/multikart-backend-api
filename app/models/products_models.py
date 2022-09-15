
from datetime import datetime
from email.policy import default
from sqlalchemy import String, Integer, Column, Boolean, ForeignKey, Float,DateTime
from sqlalchemy.orm import relationship
from database.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Product(Base):
    __tablename__="products"
    product_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_title = Column(String(100), index=True)
    description = Column(String(1000))
    category = Column(String(100), index=True)
    price = Column(Float, index=True)
    quantity_in_stock = Column(Integer, index=True)
    # tags = Column(String)
    created_at = Column(DateTime,default=datetime.now())
    isActive = Column(Boolean, default=False)
    
# class Images(Base):
#     pass

