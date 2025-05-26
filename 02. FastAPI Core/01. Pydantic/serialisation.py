from __future__ import annotations

from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator, computed_field
from typing import Dict, List, Optional, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from .models import Address

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool
    created_at: datetime
    address: Address
    tags: List[str] = []
    
