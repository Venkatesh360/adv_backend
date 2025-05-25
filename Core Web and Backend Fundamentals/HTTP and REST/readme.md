
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

**HTTP/2** was designed to address the performance limitations of HTTP/1.1 and bring modern improvements to web communication.

### Key Features

- **Binary Framing Layer**:  
  Unlike previous versions that used plain text, HTTP/2 uses a **binary format**.  
  - Messages are broken into small units called **frames**.
  - These frames are handled by the binary framing layer and transmitted over a single TCP connection.

- **Full Request and Response Multiplexing**:  
  HTTP/2 allows multiple requests and responses to be in flight at the same time over a single connection.  
  - Messages are split into frames.
  - These frames can be interleaved during transmission and then reassembled on the other end.  
  - This eliminates the **head-of-line blocking** issue of HTTP/1.1.

- **Stream Prioritization**:  
  HTTP/2 allows developers to assign **priority levels** to different requests.  
  - Higher-priority requests receive more frames from the server.
  - For example, a request for a critical CSS file may be given higher priority than an image.

- **Server Push**:  
  The server can **proactively send resources** the client is likely to need, even before the client explicitly requests them.  
  - For example, if the client requests an HTML page, the server might also push the associated CSS and JS files.

- **Header Compression (HPACK)**:  
  HTTP/2 introduces **HPACK**, a mechanism to compress HTTP headers.  
  - In HTTP/1.1, headers were sent in plain text for every request.
  - HPACK compresses headers and maintains a table of previously seen headers to improve future compression.

---

### Summary

HTTP/2 dramatically improves performance with:
- Efficient use of a single connection
- Reduced latency
- Smarter resource loading
- Compressed and optimized metadata (headers)

These advancements make HTTP/2 a major step forward for faster, more reliable web experiences.
