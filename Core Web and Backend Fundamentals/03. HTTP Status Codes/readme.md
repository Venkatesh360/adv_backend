## HTTP Status Codes

HTTP status codes are issued by a server in response to a client's request made to the server. They are categorized into five classes and help indicate whether a request was successful, redirected, resulted in an error, or is still processing.

---

### 🔵 1xx — Informational

These codes indicate that the request was received and understood and that the process is continuing.

- **100 Continue**  
  The initial part of a request has been received and the client can continue with the rest.

- **101 Switching Protocols**  
  The server is switching protocols as requested by the client.

- **102 Processing (WebDAV)**  
  The server has received and is processing the request, but no response is available yet.

---

### 🟢 2xx — Success

These codes indicate that the request was successfully received, understood, and accepted.

#### Most Used:

- **200 OK**  
  Standard response for successful HTTP requests.  
  _Example: A successful `GET` request for a web page._

- **201 Created**  
  The request has been fulfilled and a new resource is created.  
  _Example: After a `POST` request to create a new user._

- **204 No Content**  
  The server successfully processed the request but is not returning any content.  
  _Example: A `DELETE` request._

- **202 Accepted**  
  The request has been accepted for processing, but the processing is not complete.

- **206 Partial Content**  
  Used when the client requests a portion of the file using range headers.

---

### 🟡 3xx — Redirection

These codes indicate that the client must take additional action to complete the request.

#### Most Used:

- **301 Moved Permanently**  
  The requested resource has been permanently moved to a new URL.

- **302 Found (Previously "Moved Temporarily")**  
  The requested resource resides temporarily under a different URI.

- **304 Not Modified**  
  Indicates that the resource has not been modified since the last request. Used with caching.

- **307 Temporary Redirect**  
  Same as 302, but the HTTP method must not change.

- **308 Permanent Redirect**  
  Like 301, but the method and body are preserved.

---

### 🔴 4xx — Client Errors

These codes indicate an error caused by the client.

#### Most Used:

- **400 Bad Request**  
  The server could not understand the request due to invalid syntax.

- **401 Unauthorized**  
  Authentication is required and has failed or has not been provided.

- **403 Forbidden**  
  The client does not have access rights to the content.

- **404 Not Found**  
  The server cannot find the requested resource.

- **405 Method Not Allowed**  
  The request method is known by the server but is not supported by the target resource.

- **408 Request Timeout**  
  The server timed out waiting for the request.

- **429 Too Many Requests**  
  The user has sent too many requests in a given amount of time (rate limiting).

---

### 🔴 5xx — Server Errors

These codes indicate that the server failed to fulfill a valid request.

#### Most Used:

- **500 Internal Server Error**  
  A generic error message, given when no more specific message is suitable.

- **502 Bad Gateway**  
  The server received an invalid response from the upstream server.

- **503 Service Unavailable**  
  The server is currently unavailable (e.g., due to overload or maintenance).

- **504 Gateway Timeout**  
  The server did not receive a timely response from the upstream server.

- **505 HTTP Version Not Supported**  
  The server does not support the HTTP protocol version used in the request.

---

### 📌 Summary Table

| Code | Meaning                  | Type          |
|------|--------------------------|---------------|
| 200  | OK                       | Success       |
| 201  | Created                  | Success       |
| 204  | No Content               | Success       |
| 301  | Moved Permanently        | Redirection   |
| 302  | Found                    | Redirection   |
| 304  | Not Modified             | Redirection   |
| 400  | Bad Request              | Client Error  |
| 401  | Unauthorized             | Client Error  |
| 403  | Forbidden                | Client Error  |
| 404  | Not Found                | Client Error  |
| 405  | Method Not Allowed       | Client Error  |
| 429  | Too Many Requests        | Client Error  |
| 500  | Internal Server Error    | Server Error  |
| 502  | Bad Gateway              | Server Error  |
| 503  | Service Unavailable      | Server Error  |
| 504  | Gateway Timeout          | Server Error  |

---

