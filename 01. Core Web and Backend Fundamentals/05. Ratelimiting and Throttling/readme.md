
# 🚦 Rate Limiting & Throttling in Web Applications

---

## ✅ What is Rate Limiting?

**Rate limiting** is a technique used to control how many requests a user or client can make to a server in a given period of time.

It helps:

- Prevent abuse and DoS attacks
- Reduce server load
- Enforce fair usage
- Protect APIs and backend resources

---

## 📊 Example Use Case

> Limit each IP address to 100 requests per minute.

If someone exceeds this limit, the server responds with a `429 Too Many Requests` status code.

---

## ⏱️ What is Throttling?

**Throttling** is a broader concept. It refers to the act of **delaying or limiting** requests to ensure they don’t overwhelm the server.

It includes:

- Hard limits (rate limiting)
- Gradual slowdown (e.g., delay responses after X requests)
- Priority queues

Think of **rate limiting** as a specific *form* of throttling.

---

## 🧠 Why Are They Important?

| Reason            | Benefit                             |
|------------------|-------------------------------------|
| Security          | Blocks abuse, brute force, spam    |
| Performance       | Prevents backend overload          |
| Cost Control      | Avoids unnecessary infrastructure spend |
| Fair Usage        | Ensures one user doesn't starve others |
| API Protection    | Enforces quota, monetization plans |

---

## 🧪 Types of Rate Limiting Algorithms

### 1. **Fixed Window**

- Each time window (e.g., 1 minute) has a request counter.
- Requests are allowed until the counter exceeds the limit.
- Simple but can cause bursts at window edges.

```python
# Pseudocode
if request_count[current_minute] >= limit:
    block()
else:
    allow()
```

---

### 2. **Sliding Window**

- Looks at a rolling window instead of fixed intervals.
- Provides smoother limiting.

---

### 3. **Token Bucket**

- Tokens are added to a bucket at fixed intervals.
- Each request consumes one token.
- If bucket is empty, request is denied.
- Allows short bursts.

---

### 4. **Leaky Bucket**

- Requests flow through a “leaky” queue at a constant rate.
- Excess is discarded or delayed.

---

## 🔧 HTTP Status Codes for Rate Limiting

| Code | Meaning               |
|------|------------------------|
| `429`| Too Many Requests     |
| `503`| Service Unavailable (often used with retry headers) |

---

## 📦 Headers Used in Rate Limiting

| Header                     | Description                            |
|---------------------------|----------------------------------------|
| `X-RateLimit-Limit`       | Max number of requests allowed         |
| `X-RateLimit-Remaining`   | Number of requests left in current window |
| `X-RateLimit-Reset`       | Time when the limit resets (Unix time) |
| `Retry-After`             | How long the client should wait before retrying (seconds or date) |

---

## 🛠️ Example: Rate Limiting with FastAPI & slowapi

```python
from fastapi import FastAPI, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/")
@limiter.limit("5/minute")
async def home(request: Request):
    return {"message": "Welcome"}
```

---

## 💡 Best Practices

- Rate limit by IP or authenticated user
- Provide meaningful headers and messages
- Log rate limit violations
- Use exponential backoff for retries
- Adjust limits for different plans (free vs. premium)

---

## ⚠️ Beware

| Pitfall               | Issue                                   |
|-----------------------|-----------------------------------------|
| Shared IPs            | May block many users unfairly (e.g., behind NAT) |
| Clock Drift           | Can cause inconsistencies in windowing  |
| User Enumeration      | Rate limiting login pages helps prevent credential stuffing |

---

## ✅ Summary

| Concept      | Summary                                                |
|--------------|--------------------------------------------------------|
| Rate Limiting | Controls request count in a time window              |
| Throttling    | Broader: may delay, drop, or queue requests           |
| Use Cases     | APIs, login, form submissions, file uploads           |
| Techniques    | Fixed window, sliding window, token bucket, leaky bucket |
| HTTP Status   | `429 Too Many Requests`                              |

