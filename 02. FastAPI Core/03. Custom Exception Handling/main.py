from fastapi import FastAPI
from fastapi import Request, status, Header
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
import traceback
import jwt
import logging

app = FastAPI()

users = {
    1 : "user1",
    2 : "user2",
    3 : "user3",
    4 : "user1",
}
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging

app = FastAPI()

# Sample user database
users = {
    1: "Alice",
    2: "Bob"
}

# -------------------------------
# Custom Exception: User Not Found
# -------------------------------
class UserAuthenticationError(Exception):
    """
    Raised when a user with a given user_id is not found.
    """
    def __init__(self, user_id: int):
        self.user_id = user_id

@app.exception_handler(UserAuthenticationError)
async def handle_user_error(request: Request, exc: UserAuthenticationError):
    """
    Handles UserAuthenticationError and returns a 404 with user details.
    """
    logging.error(f"User {exc.user_id} not found from {request.client}")
    return JSONResponse(
        status_code=404,
        content={"detail": f"User with ID {exc.user_id} not found"}
    )

@app.get("/api/user/{user_id}")
async def authenticate_user(request: Request, user_id: int):
    """
    Checks if user exists. Raises UserAuthenticationError if not found.
    """
    if user_id not in users:
        raise UserAuthenticationError(user_id)
    
    return {"message": f"User ID: {user_id} belongs to {users[user_id]}"}


# -------------------------------
# Custom Exception: Resource Limit
# -------------------------------
class ResourceLimitError(Exception):
    """
    Raised when access to a resource exceeds the allowed limit.
    """
    def __init__(self, resource: str, limit: int):
        self.resource = resource
        self.limit = limit

@app.exception_handler(ResourceLimitError)
async def limit_exceeded_handler(request: Request, exc: ResourceLimitError):
    """
    Handles ResourceLimitError and returns a 429 with retry instructions.
    """
    return JSONResponse(
        status_code=429,
        content={
            "error": "LimitExceeded",
            "resource": exc.resource,
            "limit": exc.limit,
            "message": f"Limit exceeded for {exc.resource}. Max allowed: {exc.limit}"
        },
        headers={"Retry-After": "60"}
    )

@app.get("/api/resource")
async def get_resource(resource: str):
    """
    Always raises ResourceLimitError for demonstration.
    """
    raise ResourceLimitError(resource, 10)


# -----------------------------------------
# Central Logging for All Custom Exceptions
# -----------------------------------------
logger = logging.getLogger("fastapi")
logging.basicConfig(level=logging.ERROR)

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    """
    Handle all unhandled exceptions globally.

    Args:
        request (Request): Incoming request.
        exc (Exception): Unhandled exception.

    Returns:
        JSONResponse: 500 Internal Server Error response.
    """
    tb_str = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
    
    logger.error(f"Unhandled error: {exc} from {request.url}")
    return JSONResponse(
        status_code=500,
        content={"error": "InternalServerError", "message": "Something went wrong."}
    )

@app.get("/api/cause-error")
async def cause_error():
    """
    Endpoint that triggers a ZeroDivisionError to test the global exception handler.

    Returns:
        dict: This will never be returned due to the intentional error.
    """
    result = 1 / 0  # This will raise a ZeroDivisionError
    return {"result": result}


# -----------------------------------------
# Handle FastAPI Validation Errors Globally
# -----------------------------------------
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Handle request body/query parameter validation errors.

    Args:
        request (Request): Incoming request.
        exc (RequestValidationError): Validation error raised by FastAPI.

    Returns:
        JSONResponse: 422 Unprocessable Entity response with details.
    """
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": "ValidationError",
            "details": exc.errors(),
            "body": exc.body
        }
    )

class Item(BaseModel):
    name: str
    price: float
    quantity: int


@app.post("/items/")
async def create_item(item: Item):
    """
    Create a new item. Validates request using Pydantic.

    Args:
        item (Item): The item data.

    Returns:
        dict: Confirmation message and received item.
    """
    return {"message": "Item received", "item": item}


# -----------------------------------------
# Handle JWT/OAuth Exceptions from External Libs
# -----------------------------------------
SECRET_KEY = "your-secret-key"

@app.exception_handler(jwt.PyJWTError)
async def jwt_error_handler(request: Request, exc: jwt.PyJWTError):
    """
    Handle JWT-related errors using PyJWTError.

    Args:
        request (Request): Incoming request.
        exc (PyJWTError): Exception raised during JWT validation.

    Returns:
        JSONResponse: 401 Unauthorized error with a message.
    """
    return JSONResponse(
        status_code=401,
        content={"error": "InvalidToken", "message": "Invalid or expired JWT token"}
    )

@app.get("/protected")
async def protected_route(authorization: str = Header(...)):
    """
    Protected route that requires a valid JWT token in the Authorization header.

    Args:
        authorization (str): Header in the form 'Bearer <token>'.

    Returns:
        dict: Decoded token payload if valid.
    """
    try:
        token = authorization.split(" ")[1]  # Expecting 'Bearer <token>'
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return {"message": "Token is valid", "user": payload}
    except jwt.PyJWTError as e:
        raise e  # Will be handled by jwt_error_handler


# -----------------------------------------
# Reusable Base Exception + Inheritance
# -----------------------------------------
class APIException(Exception):
    """
    Base exception class for custom API errors.
    """
    def __init__(self, message: str, code: int = 400):
        self.message = message
        self.code = code

class InvalidCredentials(APIException):
    """
    Custom exception for authentication failures.
    """
    def __init__(self):
        super().__init__("Invalid credentials", code=401)

@app.exception_handler(APIException)
async def api_exception_handler(request: Request, exc: APIException):
    """
    Handler for all exceptions inheriting from APIException.

    Args:
        request (Request): Incoming request.
        exc (APIException): Raised exception.

    Returns:
        JSONResponse: Custom error response.
    """
    return JSONResponse(
        status_code=exc.code,
        content={"error": exc.__class__.__name__, "message": exc.message}
    )


# -----------------------------------------
# Uvicorn Entrypoint
# -----------------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
