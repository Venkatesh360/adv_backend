from __future__ import annotations

from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator, computed_field
from typing import Dict, List, Optional
from datetime import datetime


class Cart(BaseModel):
    """
    Represents a shopping cart for a user with items and their quantities.
    """
    user_id: int
    items: List[str]
    quantities: Dict[str, int]


class BlogPost(BaseModel):
    """
    Represents a blog post by a user, including optional content and image.
    """
    user_id: int
    title: str
    content: Optional[str]
    image_url: Optional[str]


class Employee(BaseModel):
    """
    Represents an employee with constraints on name length and salary.
    """
    user_id: int
    name: str = Field(
        ..., 
        min_length=5, 
        max_length=60, 
        description="Employee name", 
        examples=["John Doe"]
    )
    department: str = 'general'
    salary: float = Field(..., ge=10000)


class Address(BaseModel):
    """
    Represents an address with street, city, and postal code.
    """
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    """
    Represents a user with username validation and nested address.
    """
    username: str
    name: str
    email: EmailStr
    hashed_password: int
    is_true: bool
    address: Address

    @field_validator('username')
    def validate_username(cls, value: str) -> str:
        """
        Validate that username is at least 4 characters long.
        """
        if len(value) < 4:
            raise ValueError("Username must be at least 4 characters long")
        return value


class Signup(BaseModel):
    """
    Represents a signup form ensuring password and confirm_password match.
    """
    password: str
    confirm_password: str

    @model_validator(mode='after')  # type: ignore
    def match_password(cls, values: Signup) -> Signup:
        """
        Validate that password and confirm_password fields are equal.
        """
        if values.password != values.confirm_password:
            raise ValueError('Password mismatch')
        return values


class Product(BaseModel):
    """
    Represents a product with price, quantity, and stock status.
    """
    id: int
    price: float
    quantity: float
    in_stock: bool = True

    @computed_field
    @property
    def total_price(self) -> float:
        """
        Compute total price as price multiplied by quantity.
        """
        return self.price * self.quantity


class Booking(BaseModel):
    """
    Represents a booking with computed total amount.
    """
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_night: float

    @computed_field
    @property
    def total_amount(self) -> float:
        """
        Compute total amount as nights multiplied by rate per night.
        """
        return self.nights * self.rate_night


class Comment(BaseModel):
    """
    Represents a comment with possible nested replies.
    """
    id: int
    user_id: int
    replies: Optional[List[Comment]] = None


# To handle forward references when a class references itself
Comment.model_rebuild()


class Lession(BaseModel):
    """
    Represents a lesson in a module.
    """
    lession_id: int
    topic: str
    content: str


class Module(BaseModel):
    """
    Represents a module containing lessons.
    """
    module_id: int
    name: str
    lessions: List[Lession]


class Course(BaseModel):
    """
    Represents a course consisting of modules.
    """
    course_id: int
    name: int
    modules: List[Module]


# Model serialization can be done by calling .json(), .dict(), etc. on model instances
