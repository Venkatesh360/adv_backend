from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
app = FastAPI()


@app.get("/")
async def home():
    return {"hello":"world"}


app.mount("/static", StaticFiles(directory="static"), name="static")