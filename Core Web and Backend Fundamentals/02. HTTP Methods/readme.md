## HTTP Methods

HTTP defines a set of request methods to indicate the desired action to be performed on a resource. These methods are sometimes referred to as **HTTP verbs**.

---

### 🔹 GET

- **Description**:  
  The `GET` method requests data from a specified resource.  
  It should have **no side effects** (i.e., not modify data).

- **Usage**:  
  Used to retrieve HTML pages, images, stylesheets, scripts, etc.

- **Characteristics**:
  - **Safe**: Yes
  - **Idempotent**: Yes
  - **Cacheable**: Yes
  - **Request Body**: Not allowed
  - **Example**:
    ```
    GET /users HTTP/1.1
    ```

---

### 🔹 POST

- **Description**:  
  The `POST` method is used to **submit data** to be processed to a specified resource.  
  Often used for **creating** new resources (e.g., in a database).

- **Usage**:
  - Form submissions
  - File uploads
  - API calls that create resources

- **Characteristics**:
  - **Safe**: No
  - **Idempotent**: No
  - **Cacheable**: Not by default
  - **Request Body**: Required (usually JSON, form-data)
  - **Example**:
    ```http
    POST /users HTTP/1.1
    Content-Type: application/json

    {
      "name": "Alice",
      "email": "alice@example.com"
    }
    ```

---

### 🔹 PUT

- **Description**:  
  The `PUT` method replaces all current representations of the target resource with the request payload.  
  Commonly used to **update or create** a resource.

- **Usage**:
  - Full update of a resource (e.g., updating an entire user profile)
  - Replacing files on a server

- **Characteristics**:
  - **Safe**: No
  - **Idempotent**: Yes
  - **Cacheable**: No
  - **Request Body**: Required
  - **Example**:
    ```http
    PUT /users/123 HTTP/1.1
    Content-Type: application/json

    {
      "name": "Alice",
      "email": "newalice@example.com"
    }
    ```

---

### 🔹 PATCH

- **Description**:  
  The `PATCH` method applies **partial modifications** to a resource.

- **Usage**:
  - Updating a single field in a resource (e.g., just the user's name)
  - Efficient for bandwidth because only changes are sent

- **Characteristics**:
  - **Safe**: No
  - **Idempotent**: Yes (in theory, but depends on implementation)
  - **Cacheable**: No
  - **Request Body**: Required
  - **Example**:
    ```http
    PATCH /users/123 HTTP/1.1
    Content-Type: application/json

    {
      "email": "patched@example.com"
    }
    ```

---

### 🔹 DELETE

- **Description**:  
  The `DELETE` method removes the specified resource from the server.

- **Usage**:
  - Removing a user, file, or record

- **Characteristics**:
  - **Safe**: No
  - **Idempotent**: Yes
  - **Cacheable**: No
  - **Request Body**: Optional or not allowed (depends on server)
  - **Example**:
    ```http
    DELETE /users/123 HTTP/1.1
    ```

---

### 🔹 HEAD

- **Description**:  
  The `HEAD` method is identical to `GET` but **only returns headers**, not the body.

- **Usage**:
  - Checking if a resource exists
  - Checking the size of a file (using `Content-Length`)
  - Used in **HTTP caching** and **SEO crawlers**

- **Characteristics**:
  - **Safe**: Yes
  - **Idempotent**: Yes
  - **Cacheable**: Yes
  - **Request Body**: Not allowed
  - **Example**:
    ```http
    HEAD /file.zip HTTP/1.1
    ```

---

### 🔹 OPTIONS

- **Description**:  
  The `OPTIONS` method returns the **HTTP methods** that the server supports for a specified URL.

- **Usage**:
  - CORS preflight checks
  - Discovering supported API operations

- **Characteristics**:
  - **Safe**: Yes
  - **Idempotent**: Yes
  - **Cacheable**: Sometimes
  - **Request Body**: Optional
  - **Example**:
    ```http
    OPTIONS /api/data HTTP/1.1
    ```

---

### 🔹 TRACE

- **Description**:  
  Echoes back the received request for diagnostic purposes.  
  Rarely used. Often **disabled** for security reasons.

- **Usage**:
  - Debugging, testing intermediaries like proxies or gateways

- **Characteristics**:
  - **Safe**: Yes
  - **Idempotent**: Yes
  - **Cacheable**: No
  - **Request Body**: Not used
  - **Example**:
    ```http
    TRACE /debug HTTP/1.1
    ```

---

### 🔹 CONNECT

- **Description**:  
  Converts the request connection to a **tunnel**, typically used for **SSL (HTTPS)** through an HTTP proxy.

- **Usage**:
  - Establishing a tunnel to a remote server via a proxy

- **Characteristics**:
  - **Safe**: No
  - **Idempotent**: Yes
  - **Cacheable**: No
  - **Request Body**: Not used
  - **Example**:
    ```http
    CONNECT www.example.com:443 HTTP/1.1
    ```

---

### 📌 Summary Table of HTTP Methods

| Method   | Safe | Idempotent | Cacheable | Description                         |
|----------|------|------------|-----------|-------------------------------------|
| GET      | Yes  | Yes        | Yes       | Retrieve data                       |
| POST     | No   | No         | No        | Submit/create data                  |
| PUT      | No   | Yes        | No        | Replace a resource                  |
| PATCH    | No   | Yes        | No        | Partially update a resource         |
| DELETE   | No   | Yes        | No        | Remove a resource                   |
| HEAD     | Yes  | Yes        | Yes       | Get headers only                    |
| OPTIONS  | Yes  | Yes        | Sometimes | Get supported HTTP methods          |
| TRACE    | Yes  | Yes        | No        | Diagnostic tool (rarely used)       |
| CONNECT  | No   | Yes        | No        | Establish a tunnel (e.g. HTTPS)     |

---

### 🔒 Best Practices

- Use `GET` for data retrieval only; avoid side effects.
- Use `POST` for creation, `PUT` for full update, `PATCH` for partial update.
- Prefer `DELETE` over `POST` for deletions to improve clarity.
- Avoid using `TRACE` and `CONNECT` unless necessary due to security risks.

