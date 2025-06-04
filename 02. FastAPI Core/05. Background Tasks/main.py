from fastapi import FastAPI, BackgroundTasks, Depends, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

# ================================
# Utility: Background Task
# ================================

def write_notification(email: str, message: str = ""):
    """
    Writes a notification message to a log file.
    
    Args:
        email (str): The recipient's email address.
        message (str): The notification message.
    """
    with open('log.txt', mode='a') as email_file:
        content = f"Notification for {email}: {message}"
        email_file.write(content + "\n")

# ================================
# Dependency Function
# ================================

async def get_query(email: str, background_tasks: BackgroundTasks) -> str:
    """
    Dependency that adds a background task to write a notification.

    Args:
        email (str): The email to send the notification to.
        background_tasks (BackgroundTasks): FastAPI's background task manager.

    Returns:
        str: A success message.
    """
    background_tasks.add_task(write_notification, email, message="hello")
    return "Message added successfully"

# ================================
# Routes
# ================================

@app.post("/send_notification/{email}")
async def send_notification(email: str, message: str = Depends(get_query)):
    """
    Endpoint to send a background notification to the provided email.

    Args:
        email (str): Email address from the path parameter.
        message (str): Message returned from dependency (injected via Depends).

    Returns:
        JSONResponse: Confirmation or error message.
    """
    if not message:
        raise HTTPException(status_code=409, detail="Error writing message")

    return JSONResponse(status_code=202, content={"detail": message})


@app.post("/get_item")
async def get_item() -> dict:
    """
    Returns a fixed item.

    Returns:
        dict: A simple key-value item.
    """
    return {12: "This item"}


@app.post("/get_item/{id}")
async def get_item_by_id(id: int) -> dict:
    """
    Returns an item based on the provided ID.

    Args:
        id (int): The ID of the item.

    Returns:
        dict: A key-value pair for the item.
    """
    return {id: "This is the item"}
