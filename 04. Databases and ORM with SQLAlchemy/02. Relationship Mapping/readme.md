# Relationship Mapping and Types in SQLAlchemy

SQLAlchemy ORM allows defining relationships between tables using Python classes. Relationship mapping helps manage associations and navigate related objects easily.

## 1. What is Relationship Mapping?

Relationship mapping connects database tables via foreign keys, enabling Python objects to reference related objects naturally. It allows:

- Accessing related objects through attributes
- Cascading operations (delete, update)
- Querying related data efficiently

## 2. Types of Relationship Mapping in SQLAlchemy

SQLAlchemy supports several types of relationships:

### a) One-to-Many

A single record in one table relates to multiple records in another.

```python
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey

class Parent(Base):
    __tablename__ = 'parents'
    id = Column(Integer, primary_key=True)
    children = relationship('Child', back_populates='parent')

class Child(Base):
    __tablename__ = 'children'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parents.id'))
    parent = relationship('Parent', back_populates='children')
```

### b) Many-to-One

The inverse of one-to-many. Many records relate to a single parent.

(Same as above but viewed from child to parent side)

### c) One-to-One

A special case of one-to-many where only one child corresponds to one parent.

```python
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    address = relationship('Address', uselist=False, back_populates='user')

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='address')
```

### d) Many-to-Many

Many records in one table relate to many records in another, via an association table.

```python
association_table = Table(
    'association', Base.metadata,
    Column('left_id', ForeignKey('left.id'), primary_key=True),
    Column('right_id', ForeignKey('right.id'), primary_key=True)
)

class Left(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    rights = relationship('Right', secondary=association_table, back_populates='lefts')

class Right(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)
    lefts = relationship('Left', secondary=association_table, back_populates='rights')
```

## 3. Parameters of `relationship()`

- `back_populates`: Defines complementary attribute on the related class
- `secondary`: Specifies the association table for many-to-many
- `uselist`: Indicates whether the attribute is a list or scalar (useful for one-to-one)
- `cascade`: Controls cascading behavior on related objects

## Conclusion

Relationship mapping in SQLAlchemy ORM provides a powerful way to work with related data as native Python objects, supporting all common relational patterns.