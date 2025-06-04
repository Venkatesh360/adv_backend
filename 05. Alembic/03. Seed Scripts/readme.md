# Seed Scripts in SQLAlchemy/Alembic Projects

Seed scripts are used to populate your database with initial or test data. This is especially useful for setting up local environments, CI testing, or deploying default values in production.

---

## 🧱 When to Use Seed Scripts

- Populate reference data (e.g., roles, categories).
- Insert test/demo data during development.
- Initialize essential app configuration entries.

---

## 🛠️ Typical Setup

Seed scripts are usually placed in a dedicated folder in your project, like:

```
project_root/
├── alembic/
├── app/
├── seeds/
│   └── seed_users.py
```

---

## 🧬 Example: SQLAlchemy Seed Script

```python
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import User

def seed_users():
    db: Session = SessionLocal()
    users = [
        User(name="Alice", email="alice@example.com"),
        User(name="Bob", email="bob@example.com")
    ]
    db.add_all(users)
    db.commit()
    db.close()

if __name__ == '__main__':
    seed_users()
```

---

## 🚀 Running the Script

```bash
python seeds/seed_users.py
```

You can also write a master seeding script that runs multiple seeders in sequence:

```python
from seeds.seed_users import seed_users
from seeds.seed_roles import seed_roles

if __name__ == '__main__':
    seed_roles()
    seed_users()
```

---

## ✅ Best Practices

- Keep seed data **idempotent**: rerunning it shouldn’t duplicate entries.
- Group related seeders by domain (e.g., `seed_products.py`, `seed_orders.py`).
- Avoid hardcoding sensitive or user-specific data.
- Use environment checks to avoid running dev seeds in production.

---

## 🧪 Tip for Testing

In test environments, use seed scripts to insert data before running test suites. This ensures consistent initial states.

---

## 🔗 Integration with Alembic

While Alembic is for schema migrations, seed scripts are for **data**. Do **not** put seed logic in Alembic migration files—keep concerns separated for clarity and rollback safety.
