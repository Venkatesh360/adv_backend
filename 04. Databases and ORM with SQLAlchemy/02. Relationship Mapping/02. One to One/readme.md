# SQLAlchemy: One-to-One Relationship

This guide explains how to define a **one-to-one** relationship using SQLAlchemy ORM.

## Concept

In a one-to-one relationship, one row in a table is related to **only one** row in another table. For example, a `User` can have one `Profile`.

---

## 📄 `one_to_one_relationship.md`

# One-to-One in SQLAlchemy

## Models

Here's an example with `User` and `Profile`.

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)

    profile = relationship("Profile", back_populates="user", uselist=False, cascade="all, delete")

class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    bio = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)

    user = relationship("User", back_populates="profile")
```

## Explanation

- `uselist=False` tells SQLAlchemy that this is a one-to-one relationship (not one-to-many).
- The `user_id` in `Profile` has a `unique=True` constraint to enforce that each profile is linked to only one user.
- `back_populates` makes the relationship bidirectional.
- `cascade="all, delete"` ensures the profile is deleted if the user is deleted.

## Usage Example

```python
user = User(username="venkatesh")
profile = Profile(bio="Software Developer")

user.profile = profile
session.add(user)
session.commit()
```

## Querying

```python
# Accessing the profile of a user
user = session.query(User).filter_by(username="venkatesh").first()
print(user.profile.bio)

# Accessing the user from a profile
profile = session.query(Profile).first()
print(profile.user.username)
```

```

```
