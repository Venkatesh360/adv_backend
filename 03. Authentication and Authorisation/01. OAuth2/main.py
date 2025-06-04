from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import requests
import os


app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Replace these with secure environment variables or config
CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
REDIRECT_URI = "http://localhost:8000/auth/callback"


@app.get("/")
def home():
    """
    Health check endpoint.

    Returns:
        dict: A simple ping response to confirm the server is running.
    """
    return {"ping": "pong"}


@app.get("/login/google")
async def login_google():
    """
    Generates the Google OAuth2 URL to redirect the user for authentication.

    Returns:
        dict: Dictionary with the generated login URL.
    """
    url = (
        "https://accounts.google.com/o/oauth2/auth"
        f"?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&scope=openid%20profile%20email"
        f"&access_type=offline"
        f"&prompt=consent"
    )
    return {"url": url}


@app.get("/auth/callback")
async def auth_google(code: str):
    """
    Callback endpoint triggered after Google authenticates the user.

    Args:
        code (str): Authorization code received from Google.

    Returns:
        dict: User profile info or error details.
    """
    token_url = "https://oauth2.googleapis.com/token"
    token_data = {
        "code": code,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code",
    }

    try:
        # Exchange authorization code for access token
        token_response = requests.post(token_url, data=token_data)
        token_response.raise_for_status()
        token_json = token_response.json()

        if "access_token" not in token_json:
            raise HTTPException(status_code=400, detail="Failed to obtain access token")

        access_token = token_json["access_token"]

        # Fetch user info
        user_info_response = requests.get(
            "https://www.googleapis.com/oauth2/v1/userinfo",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        user_info_response.raise_for_status()
        user = user_info_response.json()

        return {"user": user}

    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
