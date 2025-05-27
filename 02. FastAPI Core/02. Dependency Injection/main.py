from fastapi import FastAPI, Depends
from pydantic import EmailStr, BaseModel

app = FastAPI()

class UserSignup(BaseModel):
    username: str   
    email: EmailStr
    password: str
    
class Settings(BaseModel):
    app_name: str = 'Chai App'
    admin_email: str = 'admin@chai.com'
    
    
def get_settings():
    return Settings()


@app.post('/signup')
def signup(user: UserSignup):
    return {"user": f"username: {user.username}, email: {user.email}"}


@app.get("/setting")
def get_setting(setting: Settings = Depends(get_settings)):
    pass