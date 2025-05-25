
# 🛡️ Same-Origin Policy (SOP) & CORS Explained

---

## ✅ What is the Same-Origin Policy?

The **Same-Origin Policy (SOP)** is a security concept enforced by web browsers that prevents scripts running on one **origin** (domain + protocol + port) from interacting with content from a different origin.

---

## 🔐 Why SOP Exists

To protect users from malicious websites trying to:

- Steal sensitive information (cookies, tokens, user data)
- Interfere with authenticated sessions from other sites

---

## 🔍 What Is an "Origin"?

An origin is defined as:

```
<scheme>://<hostname>:<port>
```

| URL                          | Origin Components             |
|------------------------------|-------------------------------|
| `http://example.com:80`      | `http`, `example.com`, `80`   |
| `https://example.com:443`    | `https`, `example.com`, `443` |
| `http://api.example.com:80`  | `http`, `api.example.com`, `80` |

Even a small difference in any part makes it a **different origin**.

---

## 🔒 Same-Origin Policy In Action

### ✅ Allowed:
```javascript
// Running on http://example.com
fetch('/api/data');          // Same origin
localStorage.getItem('key'); // Same origin
```

### ❌ Blocked by SOP:
```javascript
// Running on http://example.com
fetch('http://api.example.com/data'); // Cross-origin
document.domain = 'evil.com';         // Blocked
iframe.contentWindow.document         // Blocked
```

---

## 🧠 What SOP Restricts

| Resource                     | Restricted by SOP? |
|-----------------------------|---------------------|
| DOM access (JavaScript)     | ✅ Yes              |
| Cookies                     | ✅ Yes              |
| localStorage / sessionStorage | ✅ Yes           |
| AJAX (fetch, XMLHttpRequest)| ✅ Yes              |
| `<img>`, `<script>`, `<link>` | ❌ No (but can't read response) |

---

## 🔄 Bypassing SOP (Safely)

- **Use CORS**: Controlled way to allow cross-origin AJAX requests.
- **Use `postMessage()`** for iframe communication.
- **Use JSONP** (deprecated, GET-only workaround).

---

## ✅ Summary

| Key Point    | Description                                                  |
|--------------|--------------------------------------------------------------|
| What         | A browser rule preventing cross-origin access to sensitive data |
| Why          | Protects users from malicious sites                          |
| Affects      | JavaScript, cookies, storage, AJAX                          |
| Exceptions   | CORS, `<img>`, `<script>`, `postMessage`                    |
| Backend Devs | Must enable CORS if your frontend and backend are on different origins |

---

## ✅ CORS (Cross-Origin Resource Sharing) — Definition

**CORS** is a browser security feature that controls how a web page running on one origin (domain + port + protocol) can make requests to a different origin.

---

## 🔒 Why CORS Exists

By default, browsers follow the **Same-Origin Policy**, which blocks requests between different origins to protect users from malicious websites (like stealing cookies or user data from another site).

However, many real-world apps need cross-origin requests — for example:

> A React app on `http://localhost:3000` calling a FastAPI backend on `http://localhost:8000`.

This is where **CORS** comes in — it allows the server to tell the browser:

> "Yes, it's safe to let this other origin access my resources."

---

## 🔧 How CORS Works

When the frontend tries a cross-origin request:

### 🔹 1. The browser sends the request:
```
Origin: http://localhost:3000
```

### 🔹 2. The server responds with CORS headers:
```
Access-Control-Allow-Origin: http://localhost:3000
```

If this header is **not present** or doesn’t match the requesting origin, the browser **blocks** the response.

---

## 🔁 Preflight Requests

For some requests (e.g., with `PUT`, `DELETE`, or custom headers), the browser first sends a **preflight request**:

```
OPTIONS /api/data
Origin: http://localhost:3000
Access-Control-Request-Method: PUT
```

The server must respond with:

```
Access-Control-Allow-Origin: http://localhost:3000
Access-Control-Allow-Methods: PUT, GET
Access-Control-Allow-Headers: Content-Type
```

---

## ✅ Common CORS Headers

| Header                        | Purpose                                     |
|------------------------------|---------------------------------------------|
| `Access-Control-Allow-Origin` | Whitelist allowed origins                   |
| `Access-Control-Allow-Methods`| Which HTTP methods are allowed              |
| `Access-Control-Allow-Headers`| Which headers can be sent by the client     |
| `Access-Control-Allow-Credentials` | Allow cookies/auth headers           |
| `Access-Control-Expose-Headers`   | Which response headers can be read     |
| `Access-Control-Max-Age`     | Cache time for preflight result             |

---

## 🛠️ Example: Enabling CORS in FastAPI

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## ✅ TL;DR

- **CORS** is a browser-side protection, not a server protocol.
- The server must **opt-in** to allow cross-origin access using CORS headers.
- It's **only enforced by browsers** — not tools like `curl` or Postman.

