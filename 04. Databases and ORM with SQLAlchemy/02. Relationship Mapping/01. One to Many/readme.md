# SQLAlchemy: One-to-Many Relationship

This guide explains how to define a **one-to-many** relationship using SQLAlchemy ORM.

## Concept

In a one-to-many relationship, one row in a table (parent) is associated with multiple rows in another table (child). For example, one `Author` can have many `Books`.

---

## 📄 `one_to_many_relationship.md`

# One-to-Many in SQLAlchemy

## Models

Let's create an example with `Author` and `Book`.

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship("Book", back_populates="author", cascade="all, delete")

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))

    author = relationship("Author", back_populates="books")
```

## Explanation

- The `Author` class has a `books` relationship to access all related `Book` instances.
- The `Book` class has a foreign key `author_id` pointing to `Author.id`.
- `back_populates` is used to make the relationship bidirectional.
- `cascade="all, delete"` ensures that when an author is deleted, their books are also deleted.

## Usage Example

```python
author = Author(name="George Orwell")
book1 = Book(title="1984")
book2 = Book(title="Animal Farm")

author.books = [book1, book2]
session.add(author)
session.commit()
```

## Querying

```python
# Get all books by an author
author = session.query(Author).filter_by(name="George Orwell").first()
for book in author.books:
    print(book.title)
```

```

```
