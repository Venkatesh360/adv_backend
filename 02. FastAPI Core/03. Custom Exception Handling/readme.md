# Exception Handling in FastAPI (with Emphasis on Custom Exceptions)

FastAPI provides robust mechanisms for handling exceptions, ensuring APIs remain informative and resilient. This includes built-in exception handling and support for defining custom exceptions.

---

## ✅ Built-in Exception Handling
FastAPI automatically catches common exceptions like `HTTPException` and returns appropriate responses.

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/item/{item_id}")
def read_item(item_id: int):
    if item_id == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}
```

---

## 🧩 Custom Exception Handling
You can define your own exception classes and handlers for more precise control over error handling.

### 1. Define a Custom Exception
```python
class ItemNotFoundError(Exception):
    def __init__(self, item_id: int):
        self.item_id = item_id
```

### 2. Create an Exception Handler
```python
from fastapi.responses import JSONResponse
from fastapi.requests import Request

@app.exception_handler(ItemNotFoundError)
async def item_not_found_handler(request: Request, exc: ItemNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"message": f"Item {exc.item_id} not found."},
    )
```

### 3. Raise Custom Exceptions in Endpoints
```python
@app.get("/custom-item/{item_id}")
def get_custom_item(item_id: int):
    if item_id == 0:
        raise ItemNotFoundError(item_id)
    return {"item_id": item_id}
```

---

## 🔧 Use Cases for Custom Exception Handling
- Database-related errors (e.g., integrity violations)
- Business logic violations (e.g., exceeded quota)
- Authentication/authorization failures (e.g., expired tokens)
- Data validation issues not caught by Pydantic

---

## 📋 Best Practices
- Log exceptions for debugging/auditing
- Return consistent error formats (e.g., `{ "error": "..." }`)
- Avoid exposing internal server details
- Document expected errors in your OpenAPI schema

---

## 📚 References
- [FastAPI Exception Handling Docs](https://fastapi.tiangolo.com/tutorial/handling-errors/)

This setup ensures graceful API failure with informative responses and clean logging for maintainers.
