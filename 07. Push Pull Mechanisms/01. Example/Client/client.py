import websockets
import asyncio
import sseclient
from colorama import Fore, init
import requests
import time

init(autoreset=True)

async def ws_connect():
    uri="ws://localhost:8000/ws"
    socket = await websockets.connect(uri)
    try:
        while True:
            print("Connected to server")
            msg = input("client >>")
            await socket.send(msg)
            response = await socket.recv()
            if response == "break":
                break
            print(Fore.BLUE + f"Server >> {response}")
    finally:
        await socket.close()
    
        
async def long_polling():
    last_seen = 0
    
    while True:
        res = requests.get("http://localhost:8000/poll", params={"last_seen": last_seen})
        data = res.json()
        
        if data:
            print(f"New message: {data["message"]}")
            last_seen = data["timestamp"]
            
        else:
            print("No new messages")
            
        time.sleep(1)


async def get_stream():
    res = requests.get("http://localhost:8000/stream", stream=True)
    client = sseclient.SSEClient(res) # type: ignore
    
    try:
        for event in client.events():
            print("Received:", event.data)
    finally:
        client.close()

if __name__ == "__main__":
    # asyncio.run(ws_connect())
    asyncio.run(get_stream())
        