from __future__ import annotations

from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator, computed_field
from typing import Dict, List, Optional
from datetime import datetime


#    M M     M M    O O O O O   D D D      E E E E    L         S S S S S
#    M  M   M  M    O       O   D     D    E          L         S
#    M    M    M    O       O   D      D   E E E      L         S S S S S
#    M         M    O       O   D     D    E          L                 S
#    M         M    O O O O O   D D D      E E E E    L L L L   S S S S S 

# Basic Pydantic model with optional fielf value
class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]
    

class BlogPost(BaseModel):
    user_id: int
    title: str
    content: Optional[str]
    image_url : Optional[str]
    
# Pydantic model with Field
class Employee(BaseModel):
    user_id: int
    name: str = Field(..., min_length=5, max_length=60, description="Employee name", examples=["Jhon Doe"] )
    department: str = 'general'
    salary: float = Field(..., ge=10000)
    
# Basic Pydantic model with model and field validator
class User(BaseModel):
    username: str
    name: str
    email: EmailStr
    hashed_password: int
    is_true: bool
    address: Address 
    
    
    @field_validator('username')
    def validate_username(cls, value):
        
        if len(value) < 4:
            raise ValueError ("Username must be 4 characters long")
        
        return value
    
# Pydantic model with model validators
class Signup(BaseModel):
    password: str
    confirm_password: str
    
    
    @model_validator(mode='after') #  type: ignore
    def match_password(cls, values):
        if values.password != values.confirm_password:
            raise ValueError('Password mismatch')
        
        return values
    
# Pydantic model with compute field
class Product(BaseModel):
    price: float
    quantity: float
    id: int
    price: float
    in_stock: bool = True 
    
    @computed_field
    @property
    def total_price(self) -> float :
        return self.price * self.quantity
    
    
class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_night: float
    
    @computed_field
    @property
    def total_amount(self)-> float:
        return self.nights * self.rate_night
    
class Address(BaseModel):
    street: set
    city: str
    postal_code: str
    
# Pydantic model with nested model
class Comment(BaseModel):
    id: int
    user_id: int
    replies: Optional[List[Comment]] = None

# Incase of forwarding referencing(when a class is referencing itself) the script must have this method call from the class 
Comment.model_rebuild()

# Pydantic model with nested model
class Lession(BaseModel):
    lession_id: int
    topic: str
    content: str

# Pydantic model with nested model
class Module(BaseModel):
    module_id: int
    name: str
    lessions: List[Lession] 

# Pydantic model with nested model
class Course(BaseModel):
    course_id: int
    name: int
    modules: List[Module]


# Model serialisation