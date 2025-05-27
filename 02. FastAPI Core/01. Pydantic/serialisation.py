from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Dict, List, Optional, TYPE_CHECKING
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    postal_code: str
    

class User(BaseModel):
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
 
