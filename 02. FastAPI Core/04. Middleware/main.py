from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from middleware import log_middleware
import time

# Create FastAPI application instance
app = FastAPI()

# ================================
# Simple Inline Middleware
# ================================

@app.middleware("http")
async def simple_middleware(request: Request, call_next):
    """
    Middleware that logs entry/exit and adds request processing time to the response headers.
    
    Args:
        request (Request): The incoming HTTP request object.
        call_next (Callable): The next middleware or route handler in the chain.

    Returns:
        Response: The final response with an additional X-Process-Time header.
    """
    print("Entering First Middleware")

    start_time = time.time()

    # Forward the request to the next middleware/route handler
    response: Response = await call_next(request)

    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)

    print("Exiting First Middleware")

    return response

# ================================
# External Middleware via dispatch function
# ================================

# Adds custom middleware (imported from middleware.py) using Starlette's BaseHTTPMiddleware
app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)

# ================================
# Route Handlers
# ================================

@app.get("/")
async def home():
    """
    Root endpoint to test the server.
    
    Returns:
        dict: A simple response indicating the server is running.
    """
    return {"ping": "pong"}
