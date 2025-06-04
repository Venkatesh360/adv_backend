# Middleware in FastAPI

## What is Middleware?

Middleware is a function that runs **before and/or after** each request in a web application. In FastAPI, middleware allows you to:

- Intercept requests before they reach the route handler.
- Process responses before they are returned to the client.
- Perform tasks like logging, authentication, CORS, GZip compression, request/response modification, etc.

---

## How to Create Middleware in FastAPI

FastAPI uses `@app.middleware("http")` to define middleware for HTTP requests.

### Basic Example

```python
from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware("http")
async def log_request_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"Request: {request.url.path} completed in {process_time:.4f}s")
    return response
```

### Explanation

- `request`: The incoming HTTP request.
- `call_next(request)`: Passes the request to the next middleware or route handler and gets the response.
- You can modify the request/response around this call.

---

## Use Cases

1. **Logging**
2. **Timing/Performance Monitoring**
3. **Custom Headers**
4. **Authentication/Authorization**
5. **Request Validation**
6. **CORS, GZip (via built-in middleware)**

---

## Adding Built-in Middleware

### Example: GZip Middleware

```python
from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=1000)
```

### Example: CORS Middleware

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for security in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## Order of Middleware Execution

Middleware is executed in the **order it is added** for requests and in **reverse order** for responses. So, if you have multiple middleware functions, they form a **stack**.

---

## Summary

- Middleware allows cross-cutting concerns (like logging, auth, compression).
- Use `@app.middleware("http")` for custom logic.
- Use `app.add_middleware()` for built-in or reusable classes.
- Middleware is powerful for decoupling logic and keeping your app modular.

---

## References

- [FastAPI Middleware Docs](https://fastapi.tiangolo.com/advanced/middleware/)
- [Starlette Middleware](https://www.starlette.io/middleware/)
