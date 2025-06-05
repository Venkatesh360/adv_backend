# JWT (JSON Web Token) Explained

JWT (JSON Web Token) is a compact and self-contained way of securely transmitting information between parties as a JSON object. It is commonly used for authentication and authorization.

---

## 🔧 Structure of a JWT

A JWT is made up of **three** parts separated by dots (`.`):

```
header.payload.signature
```

### 1. Header

- Typically consists of two parts:
  - Algorithm used (e.g., HS256)
  - Token type (JWT)

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

### 2. Payload

- Contains the claims — statements about an entity (typically, the user) and additional metadata.

```json
{
  "sub": "1234567890",
  "name": "John Doe",
  "admin": true,
  "exp": 1712345678
}
```

### 3. Signature

- Used to verify that the message wasn't changed along the way.
- Created using the encoded header, encoded payload, a secret, and the algorithm:

```
HMACSHA256(
  base64UrlEncode(header) + "." + base64UrlEncode(payload),
  secret)
```

---

## 🔐 How JWT Works in Authentication

1. User logs in with credentials.
2. Server validates credentials and generates a JWT.
3. JWT is sent back to the client.
4. Client stores the token (typically in `localStorage` or `Authorization` header).
5. For protected routes, client sends JWT in headers.
6. Server verifies the token and grants access if valid.

---

## ✅ Benefits of Using JWT

- **Stateless**: No need to store session on server.
- **Compact**: Can be sent via URL, POST, or inside headers.
- **Self-contained**: Holds all required information for authentication.

---

## 🚨 Security Considerations

- Always use **HTTPS** to protect tokens in transit.
- Use **short expiration times**.
- Store tokens securely on the client side.
- **Do not store sensitive information** in the payload (as it's only base64-encoded).

---

## 🧪 Example in FastAPI (Token Generation & Verification)

```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta

app = FastAPI()

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
```

---

## 📝 Summary

| Key Point | Description                                                     |
| --------- | --------------------------------------------------------------- |
| Stateless | JWT contains all needed info, so no server storage is required. |
| Expirable | Include `exp` claim to auto-expire token.                       |
| Secure    | Must use HTTPS and secret keys properly.                        |

JWT is a simple, secure way to handle authentication and authorization when used correctly.
