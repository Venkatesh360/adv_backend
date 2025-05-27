from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class Address(BaseModel):
    """
    Represents a physical address.
    """
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    """
    Represents a user with personal details and address.
    
    Attributes:
        id: Unique identifier for the user.
        name: Full name of the user.
        email: User's email address.
        is_active: Boolean indicating if the user is active.
        created_at: Timestamp when the user was created.
        address: Nested Address model for user's address.
        tags: List of tags associated with the user (default empty).
    """
    id: int
    name: str
    email: str
    is_active: bool
    created_at: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y')},
        str_to_lower=True
    )
