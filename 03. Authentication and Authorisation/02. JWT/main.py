from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, Field
from datetime import datetime, timedelta
import bcrypt
import uuid
import jwt

app = FastAPI()

SECRET_KEY = "ae24d2f464bb9e2e91d8c5e57483406546755cc62c4102436d26daf62cbef244"
ALGORITHM = "HS256"

oauth = OAuth2PasswordBearer(tokenUrl="/login")


class UserLogin(BaseModel):
    """
    Request schema for user login.

    Attributes:
        email (str): User's email address.
        password (str): User's password.
    """
    email: str = Field(..., min_length=5)
    password: str


# Simulated user database with email as key
# Value is a tuple of (hashed_password, user_id)
demo_db = {
    "user@gmail.com": (
        bcrypt.hashpw("password".encode(), bcrypt.gensalt()),
        str(uuid.uuid4())
    )
}


def get_token_data(token: str = Depends(oauth)) -> dict:
    """
    Dependency to decode and validate JWT access token.

    Args:
        token (str): JWT token passed via Authorization header.

    Returns:
        dict: Payload of the token.

    Raises:
        HTTPException: If token is expired or invalid.
    """
    try:
        payload = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
        exp = datetime.utcfromtimestamp(payload["exp"])
        if exp < datetime.utcnow():
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")


@app.get("/")
async def home():
    """
    Health check endpoint.

    Returns:
        dict: Confirmation message that API is alive.
    """
    return {"ping": "pong"}


@app.post("/login")
async def login(user: UserLogin):
    """
    Authenticates user and returns a JWT token if successful.

    Args:
        user (UserLogin): Login credentials.

    Returns:
        dict: Access token.

    Raises:
        HTTPException: If user is not found or password is invalid.
    """
    hashed = demo_db.get(user.email, None)
    if not hashed:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    is_match = bcrypt.checkpw(user.password.encode(), hashed[0])  # type: ignore
    if not is_match:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")

    payload = {
        "user_id": hashed[1],
        "exp": (datetime.utcnow() + timedelta(days=3)).timestamp()
    }

    token = jwt.encode(payload=payload, key=SECRET_KEY, algorithm=ALGORITHM)
    return {"token": token}


@app.get("/data")
async def get_data(token_data: dict = Depends(get_token_data)):
    """
    Protected route that requires a valid JWT token.

    Args:
        token_data (dict): Decoded token payload (injected via dependency).

    Returns:
        dict: User-specific protected data.
    """
    return {
        "message": "Access granted to protected data.",
        "user_id": token_data["user_id"]
    }
