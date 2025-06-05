from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from colorama import Fore, init
from pydantic import BaseModel
import time


init(autoreset=True)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

event = asyncio.Event()
latest_data = {"message": "Initial message", "timestamp": time.time()}

@app.get("/")
async def home():
    return {"ping": "pong"}

class Data(BaseModel):
    message: str

@app.post("/update")
async def update(request: Request, data:Data):
    latest_data["message"] = data.message
    latest_data["timestamp"] = time.time()
    event.set()
    event.clear()
    return {"status":"updated"}


@app.get("/poll")
async def poll(last_seen: float = 0):
    timeout = 15
    if latest_data["timestamp"] <= last_seen:
        try:
            await asyncio.wait_for(event.wait(), timeout)
        except asyncio.TimeoutError:
            return JSONResponse(content={"message": None, "timestamp": last_seen})
        
    return JSONResponse(content={
        "message": latest_data["message"],
        "timestamp": latest_data["timestamp"]
    })

async def server_sent_events():    
    while True:
        await asyncio.sleep(1)
        yield f"data: Server time: {time.ctime()}\n\n"
        
@app.get("/stream")
async def stream():
    return StreamingResponse(server_sent_events(), media_type="text/event-stream") 


@app.websocket("/ws")
async def connect_websocket(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            print(Fore.BLUE + f"Client >> {data}")
            text = input("Server >> ")
            await websocket.send_text(text)
            
    except WebSocketDisconnect:
        print("Client disconnected")