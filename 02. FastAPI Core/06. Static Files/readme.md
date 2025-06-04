# Serving Static Files in FastAPI

## What are Static Files?

Static files are files that do not change dynamically. Examples include:

- Images
- CSS stylesheets
- JavaScript files
- PDFs or other documents

FastAPI allows you to serve static files using `StaticFiles` from `starlette.staticfiles`.

---

## Basic Setup

Create a directory called `static/` and place your files there.

### Directory Structure Example

```
project/
├── main.py
└── static/
    ├── style.css
    └── script.js
```

### Code Example

```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
```

This will serve files under `static/` at the URL path `/static/`.

Example: `/static/style.css`

---

## Using Static Files in HTML

You can use static file URLs in your HTML templates:

```html
<link rel="stylesheet" href="/static/style.css" />
<script src="/static/script.js"></script>
```

---

## Tips

- Ensure the static directory path is correct relative to the file running the app.
- Use proper cache headers for static files in production.
- Mount multiple static directories if needed under different paths.

---

## Example: Mount Multiple Static Directories

```python
app.mount("/assets", StaticFiles(directory="assets"), name="assets")
app.mount("/images", StaticFiles(directory="images"), name="images")
```

---

## Summary

- Use `StaticFiles` to serve files like CSS, JS, and images.
- Mount them using `app.mount()`.
- Accessible at the specified route prefix.

---

## References

- [FastAPI Static Files Docs](https://fastapi.tiangolo.com/tutorial/static-files/)
- [Starlette Static Files](https://www.starlette.io/staticfiles/)
