from fastapi import FastAPI, Depends
from pydantic import EmailStr, BaseModel

app = FastAPI()


class UserSignup(BaseModel):
    """
    Schema for user signup data.
    """
    username: str
    email: EmailStr
    password: str


class Settings(BaseModel):
    """
    Application settings data.
    """
    app_name: str = 'Chai App'
    admin_email: str = 'admin@chai.com'


def get_settings() -> Settings:
    """
    Dependency that returns app settings.
    """
    return Settings()


@app.post('/signup')
def signup(user: UserSignup):
    """
    Endpoint to register a new user.
    Returns a confirmation message with username and email.
    """
    return {"user": f"username: {user.username}, email: {user.email}"}


@app.get("/setting")
def get_setting(settings: Settings = Depends(get_settings)):
    """
    Endpoint to fetch current application settings.
    """
    return settings


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
