# One-to-Many Relationships in SQLAlchemy with Lazy Loading

## Introduction

In relational databases, a **one-to-many** relationship occurs when a single record in one table (the **parent**) is associated with multiple records in another table (the **child**).

For example, a single **User** can have many **Posts**.

---

## How SQLAlchemy Models One-to-Many

SQLAlchemy represents this relationship using the `relationship()` function combined with foreign keys:

- The **child** table contains a foreign key referencing the **parent** table's primary key.
- The **parent** table declares a `relationship()` to the child class.

Example:

- `Post` table has a `user_id` foreign key pointing to `User.id`.
- `User` class has a `posts` relationship referencing multiple `Post` objects.

---

## Lazy Loading Explained

By default, SQLAlchemy uses **lazy loading** for relationships. This means:

- When you query a `User`, SQLAlchemy **does not** immediately fetch all related `Post` records.
- The related posts are loaded **only when you first access** the `posts` attribute on a `User` instance.
- This triggers a separate SQL query to fetch the posts for that user.

### Benefits

- Efficient initial queries: You don’t fetch large amounts of related data unless needed.
- Reduces upfront load, speeding up initial data retrieval.

### Potential Downsides

- **N+1 query problem:** If you query multiple users and access their posts one by one, this results in many additional queries — one per user.
- This can cause performance issues in large datasets.

---

## How to Control Loading Behavior

SQLAlchemy lets you specify the loading strategy:

- **lazy='select'** (default): Lazy load posts when accessed.
- **joined**: Load parent and child tables together in a single query using SQL JOIN.
- **subquery**: Load related objects in a separate query but in bulk for all parents.
- **dynamic**: Returns a query object for further filtering instead of a list.

Example:

```python
posts = relationship("Post", lazy="select")
```

## Summary

- One-to-many relationships model "one parent, many children".

- Foreign key in child table links to parent.

- SQLAlchemy's lazy loading fetches related records only when accessed, improving efficiency but can cause many queries if not handled carefully.
