# Real-time Communication Techniques in Web Applications

Modern web applications often need real-time communication between clients and servers. Three primary techniques are commonly used to achieve this:

- **Long Polling**
- **Server-Sent Events (SSE)**
- **WebSockets**

---

## 1. Long Polling

Long polling is a technique where the client sends a request to the server and waits for a response. If the server has no data available, it holds the request open until data becomes available or a timeout occurs.

### How it Works

1. Client sends a request.
2. Server holds the request open until data is available or timeout.
3. Server responds with data.
4. Client processes data and immediately sends another request.

### Pros:

- Works with all browsers.
- Doesn't require special protocols beyond HTTP.

### Cons:

- Inefficient: repeated connections, increased latency.
- Not truly real-time.
- Can overload server with frequent connections.

---

## 2. Server-Sent Events (SSE)

SSE is a standard describing how servers can initiate data transmission toward browser clients once an initial client connection has been established.

### How it Works

1. Client opens a single HTTP connection.
2. Server keeps the connection open and pushes updates as events.
3. Client listens using `EventSource` API.

### Pros:

- Simple and built-in support in most modern browsers.
- Ideal for unidirectional, real-time updates (e.g., news feeds, stock prices).
- Uses standard HTTP.

### Cons:

- Only supports one-way communication (server to client).
- Limited support in non-browser environments.

---

## 3. WebSockets

WebSockets provide a full-duplex communication channel over a single, long-lived TCP connection.

### How it Works

1. Client and server upgrade the HTTP connection to WebSocket.
2. Both can send/receive data independently.
3. The connection stays open until explicitly closed.

### Pros:

- True bidirectional communication.
- Low latency and efficient for frequent updates.
- Ideal for chat apps, gaming, collaborative tools.

### Cons:

- Slightly complex setup (requires upgrade handshake).
- Not all environments support it natively (e.g., older proxies).

---

## Comparison Table

| Feature           | Long Polling    | SSE                    | WebSockets              |
| ----------------- | --------------- | ---------------------- | ----------------------- |
| Protocol          | HTTP            | HTTP                   | WS (via HTTP upgrade)   |
| Browser Support   | Universal       | Modern Browsers        | Modern Browsers         |
| Direction         | Server → Client | Server → Client        | Bi-directional          |
| Complexity        | Low             | Low                    | Medium                  |
| Latency           | High            | Low                    | Very Low                |
| Use Case Examples | Notifications   | Live Feeds, Dashboards | Chat, Multiplayer Games |

---

## Summary

- Use **long polling** for basic backward compatibility.
- Use **SSE** for simple one-way real-time feeds.
- Use **WebSockets** for full-duplex, low-latency communication.
