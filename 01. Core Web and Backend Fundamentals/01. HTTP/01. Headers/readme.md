# HTTP Headers Overview

HTTP headers are key-value pairs sent in HTTP requests and responses. They provide essential metadata about the request/response or about the body content itself.

---

## 📌 Categories of HTTP Headers

### 1. **General Headers**

- Used in both request and response.
- Do not apply to the content of the message body.

#### Common Headers:

- `Cache-Control`: Directs caching mechanisms.
- `Connection`: Controls connection management (e.g., `keep-alive`).
- `Date`: The date and time the message was sent.

---

### 2. **Request Headers**

- Sent by the client to provide context about the request.

#### Examples:

| Header            | Description                                                         |
| ----------------- | ------------------------------------------------------------------- |
| `Host`            | Specifies the domain being requested.                               |
| `User-Agent`      | Identifies the client (browser, app).                               |
| `Accept`          | Specifies acceptable content types (`application/json`, etc.).      |
| `Accept-Language` | Indicates preferred language (e.g., `en-US`).                       |
| `Authorization`   | Sends credentials (e.g., `Bearer token`).                           |
| `Cookie`          | Sends cookies stored on the client.                                 |
| `Referer`         | The page that linked to the requested resource.                     |
| `Content-Type`    | Type of body data sent (`application/json`, `multipart/form-data`). |
| `Content-Length`  | Size of the body in bytes.                                          |

---

### 3. **Response Headers**

- Sent by the server to provide metadata about the response.

#### Examples:

| Header                        | Description                                             |
| ----------------------------- | ------------------------------------------------------- |
| `Server`                      | Describes the server software.                          |
| `Set-Cookie`                  | Instructs the browser to store a cookie.                |
| `Content-Type`                | Media type of the returned content.                     |
| `Content-Length`              | Size of the response body in bytes.                     |
| `Access-Control-Allow-Origin` | For CORS, specifies who can access the resource.        |
| `Location`                    | Redirect target for 3xx responses.                      |
| `WWW-Authenticate`            | Used in 401 responses to define authentication methods. |

---

### 4. **Entity Headers**

- Provide information about the body/content of the resource.

#### Examples:

- `Content-Encoding`: Type of encoding used (e.g., `gzip`).
- `Content-Language`: Language of the body.
- `Last-Modified`: Timestamp of the last modification.
- `ETag`: Identifier for a specific version of a resource (used for caching).

---

## 🔐 Security-Related Headers

| Header                      | Purpose                                       |
| --------------------------- | --------------------------------------------- |
| `Strict-Transport-Security` | Enforces HTTPS.                               |
| `X-Frame-Options`           | Prevents clickjacking (`DENY`, `SAMEORIGIN`). |
| `X-XSS-Protection`          | Cross-site scripting filter (legacy).         |
| `Content-Security-Policy`   | Defines approved sources for content.         |
| `Referrer-Policy`           | Controls how much referrer info is sent.      |
| `Permissions-Policy`        | Controls which APIs the page can use.         |

---

## 🧪 Sample HTTP Request

```http
GET /api/user HTTP/1.1
Host: example.com
Authorization: Bearer abc123
Accept: application/json
User-Agent: curl/7.64.1

```

## 🧾 Sample HTTP Response

http
Copy code
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 123
Set-Cookie: sessionId=abc123; HttpOnly
Cache-Control: no-cache
