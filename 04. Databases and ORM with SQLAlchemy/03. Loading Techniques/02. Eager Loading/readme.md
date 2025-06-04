# SQLAlchemy Eager Loading

Eager loading is a technique where related objects are loaded **immediately** along with the parent object in the **same database query** or with as few queries as possible. This helps avoid the N+1 query problem caused by lazy loading.

---

## Why Use Eager Loading?

- When you know you'll need related objects upfront.
- To reduce the number of SQL queries.
- To improve performance for bulk data retrieval.

---

## Types of Eager Loading in SQLAlchemy

- **joined loading**: Uses a SQL JOIN to load related objects in one query.
- **subquery loading**: Loads related objects using a separate query but fetches all related objects in bulk.

---

## 📄 `eager_loading_example.md`

````markdown
# SQLAlchemy Eager Loading Example

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, joinedload

Base = declarative_base()
engine = create_engine('sqlite:///user.db')
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)

    posts = relationship("Post", back_populates="user", lazy='select')

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="posts")


# Query with eager loading (joinedload)
users = session.query(User).options(joinedload(User.posts)).all()

for user in users:
    print(user.username)
    for post in user.posts:
        print("  ", post.content)
```
````

## Explanation

- `joinedload(User.posts)` tells SQLAlchemy to load posts **in the same query** using a SQL JOIN.
- This avoids extra queries when accessing `user.posts`.
- This method improves performance when accessing related data for many objects.

---
