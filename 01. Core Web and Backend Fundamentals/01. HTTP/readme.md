
# What is HTTP?

HTTP stands for **HyperText Transfer Protocol**. It is the protocol used by browsers to communicate with web servers. When a browser requests a web page, the server responds with the code for that page.

HTTP was originally designed for transferring HTML files. However, developers later realized that HTTP can also be used to transfer other types of content such as images, videos, and more. Now http is used for an array of services which inculde APIs, File Transfers and a multitude of services.

## HTTP/0.9

HTTP/0.9 only supported **GET** requests and did not include any headers or status codes. It was a very simple version of the protocol, mainly intended for transferring HTML documents.

## HTTPS Connection Establishment

Before any data is exchanged between the browser (client) and the web server over **HTTPS**, a secure connection must be established. This process is called the **TLS (Transport Layer Security) handshake**. Here are the main steps:

### 1. **Client Hello**
The browser sends a "Client Hello" message to the server. This includes:
- Supported TLS versions
- A list of supported encryption algorithms (cipher suites)
- A randomly generated number (used later for key generation)

### 2. **Server Hello**
The server replies with a "Server Hello" message, which includes:
- Selected TLS version
- Selected cipher suite
- Its own randomly generated number
- The server’s **SSL/TLS certificate** (which includes the public key and is signed by a trusted Certificate Authority)

### 3. **Certificate Verification**
The browser:
- Verifies that the certificate is valid and trusted
- Extracts the server's **public key** from the certificate

### 4. **Key Exchange**
- The client and server work together (using public-key cryptography) to securely generate a **shared session key**, which will be used to encrypt all further communication.

### 5. **Finished Messages**
- Both the client and server send a final message encrypted with the session key to confirm that encryption is working.

### 6. **Secure Communication Begins**
Once the TLS handshake is complete, the client and server can begin securely exchanging HTTP data — now it's called **HTTPS**.

All data is now encrypted, ensuring **confidentiality**, **integrity**, and **authentication**.

![HTTPS ](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F0e18db0d-f511-4f85-bb58-388fce70d42e_2631x2103.png)

## HTTP/1.0

An upgrade to HTTP/0.9, **HTTP/1.0** introduced several important features:

- **Headers** and **status codes**
- New request methods like **POST** and **HEAD**

However, HTTP/1.0 had a major limitation:  
Each request required a **separate TCP connection**. This meant:

- For **every resource** (HTML, image, CSS, JS), a new connection had to be established.
- For **HTTPS**, this also meant repeating:
  - The **certificate check**
  - The **TLS handshake** (key exchange)

This resulted in a lot of **back-and-forth communication**, making page loads slower due to the overhead of multiple connection setups.

## HTTP/1.1

**HTTP/1.1** introduced several significant improvements over HTTP/1.0, many of which are still in use today:

### Key Features

- **Persistent Connections**:  
  HTTP/1.1 supports keeping a TCP connection open for multiple requests/responses. This avoids the overhead of opening and closing a new connection for every single resource.

- **Request Pipelining**:  
  Clients can send multiple HTTP requests without waiting for each corresponding response. For example, if a browser needs two images, it can send two `GET` requests simultaneously, reducing wait time.

- **Chunked Transfer Encoding**:  
  Large files can be sent in smaller chunks instead of waiting for the full response to be ready. This allows web pages to start rendering sooner, improving user experience—especially for large or dynamic content.

- **Better Caching and Conditional Requests**:  
  HTTP/1.1 introduced headers like:
  - `Cache-Control`
  - `ETag`
  - `If-Modified-Since`

  These helped reduce unnecessary data transfers by allowing the browser to use cached content or request resources only if they’ve changed.

---

### Limitations: Head-of-Line (HOL) Blocking

As websites grew more complex, HTTP/1.1 began to show its limitations—especially with **head-of-line blocking** in pipelined requests.

If one request in the pipeline is delayed (e.g., a large image), all following requests must wait, causing performance issues. Because of this, most browsers disabled request pipelining by default.

---

### Workarounds by Developers

To mitigate HTTP/1.1’s limitations, developers used strategies such as:

- **Domain Sharding**:  
  Serving static assets (images, scripts, etc.) from multiple subdomains to increase the number of parallel TCP connections (e.g., 6 connections per subdomain).

- **Asset Bundling**:  
  - Combining multiple JavaScript files into one
  - Merging multiple CSS files into one
  - Using **CSS sprites** to combine multiple images into a single file

These methods helped reduce the number of HTTP requests, improving page load times despite HTTP/1.1’s limitations.


## HTTP/2

HTTP/2 was designed to overcome performance limitations of HTTP/1.1 while preserving the existing semantics (i.e., same methods, status codes, and URIs). It brought major architectural changes to optimize how data is sent between client and server.

---

### 🔒 Secure by Default

While HTTP/2 **does not strictly require TLS**, **all major browsers only support HTTP/2 over HTTPS**. This means that in practical use, HTTP/2 is **secure by default**.

- Browsers like Chrome, Firefox, Safari, and Edge will **not establish an HTTP/2 connection unless it uses TLS (HTTPS)**.
- HTTP/2 connections use modern cipher suites and TLS extensions that improve both **security and performance**.

---

### 🔁 Protocol Negotiation During TLS (ALPN)

HTTP/2 relies on **ALPN (Application-Layer Protocol Negotiation)** during the **TLS handshake** to negotiate whether the client and server both support HTTP/2.

- During the TLS handshake, the client advertises supported protocols (like `h2` for HTTP/2 or `http/1.1`).
- If the server supports HTTP/2, it responds with `h2`, and the connection continues using HTTP/2.
- If not, the server falls back to HTTP/1.1.

**Why ALPN Matters:**
- Avoids sending an HTTP/1.1 request only to upgrade later.
- Faster and cleaner protocol switching.
- Improves initial connection time.

---

### 🔄 Binary Framing Layer

HTTP/2 introduces a **binary framing layer**:
- HTTP messages (requests and responses) are split into **binary-encoded frames**.
- These frames are then multiplexed and transmitted over a single TCP connection.
- This is a big change from HTTP/1.x, which sent messages as plain text.

---

### 🔁 Full Multiplexing

- **Multiple requests and responses can be in flight at the same time over one connection.**
- These are broken into frames and interleaved.
- Solves the **Head-of-Line (HOL) blocking** problem in HTTP/1.1 where one blocked request delayed others.

---

### 🎯 Stream Prioritization

- Streams can be **assigned priorities and dependencies**.
- The server can allocate resources more efficiently:
  - High-priority streams get more bandwidth.
  - Useful for progressive rendering of web pages (e.g., prioritize CSS before images).

---

### 📦 Server Push

- The server can **proactively send resources** to the client **before** the client explicitly requests them.
- Example: If the client requests an HTML page, the server can also push the linked CSS and JS files.
- This reduces the number of round-trips and improves load time.

---

### 📉 Header Compression

- HTTP/1.x sent repetitive headers with each request/response (e.g., cookies, user-agent).
- HTTP/2 uses **HPACK**, a binary header compression format that:
  - Compresses headers using Huffman coding.
  - Maintains a shared header table between client and server.
  - Sends smaller deltas for recurring headers.

---

### 🧠 Summary of Key Features

| Feature              | HTTP/1.1              | HTTP/2                        |
|----------------------|-----------------------|-------------------------------|
| Protocol Format       | Text                  | Binary                        |
| Multiplexing          | ❌ No                 | ✅ Yes                         |
| Header Compression    | ❌ No (plaintext)     | ✅ Yes (HPACK)                |
| Server Push           | ❌ No                 | ✅ Yes                         |
| Stream Prioritization | ❌ No                 | ✅ Yes                         |
| Secure by Default     | ❌ Optional           | ✅ Practically required       |
| Protocol Negotiation  | ❌ Upgrade header     | ✅ ALPN during TLS handshake  |

---

### 🌐 Real-World Impact

- Faster page loads, especially on high-latency networks.
- Fewer TCP connections = less overhead = better use of network resources.
- Significant performance improvement on mobile and low-bandwidth devices.

---

**Note**: HTTP/2 still uses TCP under the hood, so **TCP Head-of-Line blocking** (at the packet level) is still a limitation. This is addressed in **HTTP/3**, which is based on QUIC (UDP).
