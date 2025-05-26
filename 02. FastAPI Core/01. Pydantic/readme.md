# 📦 Pydantic — Data Validation and Settings Management Using Python Type Hints

---

## ✅ What is Pydantic?

**Pydantic** is a Python library for data validation and parsing using Python's type hints.

It enforces type constraints at runtime and auto-generates errors for invalid data.

Pydantic is the backbone of data validation in **FastAPI** and is widely used in modern Python APIs.

---

## 🧠 Core Features

- Type-safe data validation
- Automatic data parsing
- Detailed error messages
- Built-in support for JSON and dict input
- Nested models and complex data structures
- Environment variable parsing (via `BaseSettings`)

---

## 🧪 Basic Example

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool = True

data = {'id': '123', 'name': 'Alice'}
user = User(**data)

print(user.id)         # 123 (auto-converted to int)
print(user.is_active)  # True (default value)
```

---

## 🚨 Validation Errors

Pydantic provides detailed error messages when data is invalid.

```python
User(id='abc', name='Bob')
```

Raises:

```
pydantic.error_wrappers.ValidationError: 1 validation error
id
  value is not a valid integer (type=type_error.integer)
```

---

## 🔁 Nested Models

```python
class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    name: str
    address: Address

user = User(name="Alice", address={"city": "NY", "zip_code": "10001"})
```

---

## 📋 List and Dict Fields

```python
from typing import List, Dict

class User(BaseModel):
    name: str
    tags: List[str]
    preferences: Dict[str, str]

u = User(name="Alice", tags=["dev", "python"], preferences={"theme": "dark"})
```

---

## 📆 Date and Time Parsing

```python
from datetime import datetime
from pydantic import BaseModel

class Event(BaseModel):
    name: str
    timestamp: datetime

e = Event(name="Launch", timestamp="2023-08-15T14:30:00Z")
print(e.timestamp)  # datetime object
```

---

## ✅ Optional Fields

```python
from typing import Optional

class User(BaseModel):
    name: str
    email: Optional[str] = None
```

---

## 🔐 Field Validation

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(..., min_length=3)
    age: int = Field(..., gt=0, lt=120)
```

---

## 🧪 Custom Validators

```python
from pydantic import validator

class User(BaseModel):
    name: str
    age: int

    @validator('age')
    def check_age(cls, v):
        if v < 18:
            raise ValueError('User must be 18+')
        return v
```

---

## 🔄 Model Methods

- `.dict()` – Return model as dict
- `.json()` – Return model as JSON
- `.copy()` – Shallow copy
- `.schema()` – Return schema
- `.parse_obj()` – Construct model from dict
- `.parse_raw()` – Construct from JSON string

---

## ⚙️ Environment Variables & Settings

```python
from pydantic import BaseSettings

class Settings(BaseSettings):
    db_url: str
    debug: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
```

This auto-loads `.env` file and parses environment variables.

---

## 🔁 Model Inheritance

```python
class User(BaseModel):
    id: int
    name: str

class Admin(User):
    role: str = "admin"
```

---

## 💡 Use with FastAPI

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    password: str

@app.post("/login/")
def login(user: User):
    return {"username": user.username}
```

---

## 🧱 Advanced Types

| Type              | Description                    |
|-------------------|--------------------------------|
| `EmailStr`        | Validates email format         |
| `AnyUrl` / `HttpUrl` | Validates URLs            |
| `constr`          | String with length/regex checks |
| `conint`, `confloat` | Numeric constraints       |
| `SecretStr`       | Password masking               |

```python
from pydantic import EmailStr, conint

class Contact(BaseModel):
    email: EmailStr
    age: conint(gt=0)
```

---

## 🧩 Summary

| Feature               | Supported? ✅ |
|------------------------|----------------|
| Runtime validation     | ✅              |
| Default values         | ✅              |
| Nested models          | ✅              |
| Type coercion          | ✅              |
| Custom validation      | ✅              |
| JSON serialization     | ✅              |
| Settings via `.env`    | ✅              |

---

Pydantic helps you write safer and more robust Python code with minimal effort. It is a must-know for backend developers using FastAPI or working with APIs.


