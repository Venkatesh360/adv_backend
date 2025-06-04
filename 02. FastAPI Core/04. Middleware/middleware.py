from fastapi import Request
from logger import logger
import time

async def log_middleware(request: Request, call_next):
    """
    Custom logging middleware that logs HTTP request metadata and processing time.
    
    Args:
        request (Request): The incoming HTTP request.
        call_next (Callable): The next middleware or route handler in the chain.
    
    Returns:
        Response: The HTTP response after processing.
    """
    print("Entering Second Middleware")

    start = time.time()

    # Pass the request to the next middleware/route handler
    response = await call_next(request)

    process_time = time.time() - start

    # Construct log entry
    log_dict = {
        'url': request.url.path,
        'method': request.method,
        'process_time': process_time
    }

    # Log with structured data
    logger.info(log_dict, extra=log_dict)

    print("Exiting Second Middleware")

    return response
