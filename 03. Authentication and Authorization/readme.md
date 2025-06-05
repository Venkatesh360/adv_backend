# Authentication vs Authorization

Understanding **Authentication** and **Authorization** is essential for building secure systems. Though often used together, they serve different purposes.

---

## 🔐 Authentication

**Authentication** is the process of verifying the identity of a user or system.

### Examples:

- Logging in with a username and password
- Fingerprint scan or facial recognition
- API key/token validation

### Common Methods:

- **Basic Auth** (username/password)
- **Token-based** (JWT, OAuth)
- **Multi-Factor Authentication (MFA)**

### In Code (FastAPI JWT example):

```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
```

---

## 🛡️ Authorization

**Authorization** is the process of determining what an authenticated user is allowed to do.

### Examples:

- Access control (admin vs regular user)
- File permissions (read/write)
- API scope limitations

### Common Mechanisms:

- **Role-Based Access Control (RBAC)**
- **Attribute-Based Access Control (ABAC)**
- **Access Control Lists (ACL)**

### In Code (FastAPI Role Check Example):

```python
def get_current_user_role(token: str = Depends(oauth2_scheme)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    role = payload.get("role")
    if not role:
        raise HTTPException(status_code=403, detail="Role not found")
    return role

@app.get("/admin")
def read_admin_data(role: str = Depends(get_current_user_role)):
    if role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    return {"message": "Welcome, admin!"}
```

---

## 🔄 Key Differences

| Aspect        | Authentication                      | Authorization                        |
| ------------- | ----------------------------------- | ------------------------------------ |
| Purpose       | Verify identity                     | Grant or deny access                 |
| Happens when? | Before authorization                | After authentication                 |
| Based on      | Credentials (password, token, etc.) | Policies, roles, or privileges       |
| Example       | Login with email and password       | Admin can delete, user can only read |

---

## ✅ Summary

- Authentication answers: **"Who are you?"**
- Authorization answers: **"What are you allowed to do?"**

Both are crucial for application security and should be implemented correctly.
