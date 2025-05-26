# SQLAlchemy Core vs SQLAlchemy ORM

SQLAlchemy is a powerful SQL toolkit and Object Relational Mapper (ORM) for Python. It provides two primary ways to interact with databases:

- **SQLAlchemy Core**: A lower-level, SQL expression language.
- **SQLAlchemy ORM**: A higher-level, object-oriented abstraction for database access.

## 1. SQLAlchemy Core

SQLAlchemy Core uses a schema-centric and SQL-centric approach. It is closer to writing raw SQL but offers a Pythonic API.

### Features:
- Explicit SQL expressions
- Full control over the database schema and queries
- More suitable for complex or dynamic SQL generation
- Clear separation of logic and schema

### Example:
```python
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///example.db')
metadata = MetaData()

users = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer)
)

metadata.create_all(engine)
```

## 2. SQLAlchemy ORM

The ORM layer allows you to map Python classes to database tables and use object-oriented code to interact with the database.

### Features:
- Easier to work with for developers used to OOP
- Automatically handles relationships, joins, and lazy loading
- Ideal for rapid development and complex data models

### Example:
```python
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String

Base = declarative_base()
engine = create_engine('sqlite:///example.db')

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
```

## 3. When to Use What?

| Feature               | SQLAlchemy Core       | SQLAlchemy ORM         |
|----------------------|------------------------|--------------------------|
| Abstraction Level     | Low (closer to SQL)    | High (object-oriented)   |
| Flexibility           | High                   | Moderate                 |
| Learning Curve        | Steeper (for beginners) | Easier for Python devs   |
| Performance           | Slightly better        | Slight overhead          |
| Use Case              | Complex queries, ETL   | CRUD apps, rapid protos  |

## Conclusion

- Use **SQLAlchemy Core** when you need fine-grained control over SQL or are building libraries or tools.
- Use **SQLAlchemy ORM** for typical application development where working with objects is more intuitive.

Both layers can be mixed within the same application, providing the flexibility to choose the right tool for the job.
