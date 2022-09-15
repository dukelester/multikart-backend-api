from datetime import datetime
from pydantic import BaseModel, constr, validator
from uuid import UUID

class ProductsSchema(BaseModel):
    product_id: UUID
    product_title: constr()
    description: constr()
    category: str
    price: float
    quantity_in_stock: int | None = None
    # tags: list[str] | None = None
    created_at: datetime
    isActive: bool
    
    class Config:
        orm_mode = True
        
    # validations 
    @validator('product_id')
    def validate_product_id(cls, product_id):
        if type(product_id) != UUID:
            raise ValueError('Invalid UUID')
        return product_id
    
    @validator("product_title")
    def validate_product_title(cls, product_title):
        if len(product_title) > 100 or len(product_title) < 2:
            raise ValueError("The title is either too short or too Long!")
        return product_title
    
    @validator("description")
    def validate_description(cls,description):
        if len(description) > 1000 or len(description) < 10:
            raise ValueError("The description is either too short or too long exeeding 1000 characters!") 
        return description
    
    @validator('category')
    def validate_category(cls, category):
        if type(category) != str or len(category) > 200 or len(category) < 3:
            raise ValueError("Invalid category ")
        return category
    
    @validator("price")
    def validate_price(cls, price):
        if type(price) != float:
            raise ValueError("The price must be a float or decimal") 
        if price > 20000000 or price <=  0:
            raise ValueError('Invalid price ')
        return price
    
    # @validator("tags")
    # def validate_tags(cls, tags):
    #     if len(tags) == 0:
    #         raise ValueError("The tags can't be empty")
    #     if type(tags) != list:
    #         raise ValueError("Invalid data passed")
    #     return tags
    @validator("isActive")
    def validate_isActive(cls, isActive):
        if type(isActive) != bool:
            raise ValueError("Invalid Type")
        return isActive
    
    @validator('quantity_in_stock')
    def validate_quantity_in_stock(cls, quantity_in_stock):
        if quantity_in_stock <= 0:
            raise ValueError("Invalid quantity in stock")
        return quantity_in_stock
    
    
    
    