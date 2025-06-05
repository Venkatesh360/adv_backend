# OAuth 2.0 Explained and Comparison with Other OAuth Versions

## What is OAuth?

OAuth (Open Authorization) is an open standard protocol that allows secure authorization from web, mobile, and desktop applications via a third-party service without exposing user credentials.

---

## OAuth 2.0 Overview

OAuth 2.0 is the industry-standard protocol for authorization. It provides **secure delegated access** to resources on behalf of a user by issuing access tokens to third-party applications.

### Key Features of OAuth 2.0

- **Token Types:** Mainly uses Bearer tokens.
- **Flows (Grant Types):**
  - **Authorization Code Grant:** Used by web and mobile apps. It requires an authorization code before exchanging it for an access token.
  - **Implicit Grant:** Simplified flow for browser-based apps, but less secure (being deprecated).
  - **Resource Owner Password Credentials Grant:** Users provide credentials directly to the app (less recommended).
  - **Client Credentials Grant:** Used for machine-to-machine authentication.
  - **Refresh Token:** Allows obtaining a new access token without user interaction.

### OAuth 2.0 Flow (Authorization Code Grant)

1. User tries to access a third-party app.
2. The app redirects the user to the authorization server.
3. User logs in and grants permission.
4. Authorization server sends an authorization code to the app.
5. The app exchanges the code for an access token.
6. The app uses the access token to access the user's resources.

---

## Comparison with OAuth 1.0 and OAuth 1.0a

| Feature                 | OAuth 1.0/1.0a                                                         | OAuth 2.0                                             |
| ----------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------- |
| **Protocol Complexity** | More complex; requires cryptographic signing of each request.          | Simpler; no request signing, uses HTTPS for security. |
| **Token Types**         | Uses Access Tokens and Secret Tokens (request token and access token). | Uses Bearer tokens (simpler token usage).             |
| **Security**            | Requires cryptographic signatures on requests to verify authenticity.  | Relies on HTTPS to secure tokens, no request signing. |
| **Client Types**        | Primarily supports web applications.                                   | Supports web, mobile, desktop, and IoT applications.  |
| **Token Revocation**    | Limited support.                                                       | Better support including refresh tokens.              |
| **Flexibility**         | Less flexible, fewer grant types.                                      | Multiple grant types for various use cases.           |
| **Adoption**            | Older and less adopted now.                                            | Industry standard, widely adopted.                    |

---

## Summary

OAuth 2.0 simplifies authorization flows, improves flexibility, and is widely adopted across modern applications compared to OAuth 1.0/1.0a, which had complex signing requirements and limited flows.

---

## Example OAuth 2.0 Authorization Code Flow (Simplified)

```plaintext
User --> Client --> Authorization Server
  |           |           |
  |-- Request Authorization -->|
  |           |           |
  |<-- Authorization Code --|
  |           |           |
  |-- Request Access Token (with Code) -->|
  |           |           |
  |<-- Access Token ---------|
  |           |           |
  |-- Access Resource (with Token) -->|
  |           |           |
  |<-- Protected Resource ----|
```
