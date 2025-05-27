# Dependency Injection in FastAPI

Dependency Injection (DI) is a design pattern that allows components to be decoupled and more easily managed, tested, and reused. FastAPI has built-in support for DI using the `Depends` function.

## 1. What is Dependency Injection?

Dependency Injection allows you to declare "dependencies" (functions or classes) that should be provided to your path operations or other parts of your code. FastAPI takes care of resolving and calling them for you.

## 2. Using `Depends`

FastAPI provides the `Depends` utility to declare dependencies.

### Basic Example:
```python
from fastapi import FastAPI, Depends

app = FastAPI()

def common_parameters(q: str = None):
    return {"q": q}

@app.get("/items/")
def read_items(commons: dict = Depends(common_parameters)):
    return commons
```

## 3. Dependency Classes

You can also use classes to encapsulate dependencies:
```python
class CommonQueryParams:
    def __init__(self, q: str = None, skip: int = 0, limit: int = 10):
        self.q = q
        self.skip = skip
        self.limit = limit

@app.get("/users/")
def read_users(commons: CommonQueryParams = Depends()):
    return {"q": commons.q, "skip": commons.skip, "limit": commons.limit}
```

## 4. Sub-Dependencies

Dependencies can have their own dependencies:
```python
def get_db():
    db = connect_to_db()
    try:
        yield db
    finally:
        db.close()

def get_current_user(db=Depends(get_db)):
    return query_user_from_db(db)

@app.get("/profile")
def read_profile(user=Depends(get_current_user)):
    return user
```

## 5. Dependency Injection in Background Tasks, Middleware, and Routers

You can use `Depends` in:
- Route handlers
- Background tasks
- Event handlers (startup/shutdown)
- APIRouter dependencies (global dependencies)

## 6. Benefits of DI in FastAPI
- Encourages modular code
- Easy testing with mock dependencies
- Automatic validation and type checking
- Cleaner, more maintainable code

## Conclusion

Dependency Injection in FastAPI is simple yet powerful. By using `Depends`, you can build reusable, testable, and modular components for your application. This makes FastAPI a robust choice for scalable APIs.
