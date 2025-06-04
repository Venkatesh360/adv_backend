# Background Tasks in FastAPI

## What are Background Tasks?

Background tasks allow you to **run operations after sending the response** to the client. This is useful for tasks that:

- Take time to complete.
- Don't need to block the response.
- Can be safely done later (e.g., sending emails, logging, cleanup).

FastAPI provides built-in support using `BackgroundTasks` from `fastapi`.

---

## Basic Example

```python
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def write_log(message: str):
    with open("log.txt", mode="a") as log_file:
        log_file.write(message + "\n")

@app.post("/send-log")
async def send_log(background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, "Log message written in background")
    return {"message": "Log scheduled"}
```

### Explanation

- `BackgroundTasks` is injected into your route.
- `add_task(func, *args)` schedules the function to run after the response is sent.

---

## Use Cases

- Sending confirmation emails.
- Logging or audit trails.
- Database cleanup.
- External API calls that are not critical to user response.
- Data transformations or file processing.

---

## Dependency Injection with Background Tasks

BackgroundTasks can be passed to dependencies as well:

```python
from fastapi import Depends

def notify_admin(background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, "Notify admin called")

@app.get("/action")
async def do_action(dep=Depends(notify_admin)):
    return {"message": "Action complete"}
```

---

## Notes

- Background tasks are run **in the same process/thread**, after the response is sent.
- They are **not suitable** for long-running or blocking tasks. Use Celery or other background workers in that case.
- Exceptions in background tasks are not propagated to the client.

---

## Summary

- Use `BackgroundTasks` for post-response operations.
- Ideal for fast, non-blocking, secondary actions.
- For heavy background work, consider task queues like Celery.

---

## References

- [FastAPI Background Tasks Docs](https://fastapi.tiangolo.com/tutorial/background-tasks/)
