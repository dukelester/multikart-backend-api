
from sqlalchemy import String, Integer, Column, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from database.database import Base

class Product(Base):
    __tablename__="products"
    product_id = Column(String, unique=True, primary_key=True)
    product_title = Column(String(100), index=True)
    description = Column(String(1000))
    category = Column(String(100), index=True)
    price = Column(Float, index=True)
    quantity_in_stock = Column(Integer, index=True)
    tags = Column(String)
    created_at = Column()
    isActive = Column(Boolean)
    

class Images(Base):
    pass

