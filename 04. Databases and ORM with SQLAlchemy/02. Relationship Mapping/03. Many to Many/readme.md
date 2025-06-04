# SQLAlchemy: Many-to-Many Relationship

This guide explains how to define a **many-to-many** relationship using SQLAlchemy ORM.

## Concept

In a many-to-many relationship, multiple records in one table are associated with multiple records in another table. For example, a `Student` can enroll in many `Courses`, and a `Course` can have many `Students`.

---

## 📄 `many_to_many_relationship.md`

# Many-to-Many in SQLAlchemy

## Models

Here's an example with `Student` and `Course`.

```python
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# Association table (no model class)
student_course = Table(
    'student_course',
    Base.metadata,
    Column('student_id', ForeignKey('students.id'), primary_key=True),
    Column('course_id', ForeignKey('courses.id'), primary_key=True)
)

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    courses = relationship("Course", secondary=student_course, back_populates="students")

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String)

    students = relationship("Student", secondary=student_course, back_populates="courses")
```

## Explanation

- A **secondary** table `student_course` is used to map the many-to-many relationship.
- `relationship(..., secondary=..., back_populates=...)` creates bidirectional links.
- No need to define a class for the association table unless you need to store extra metadata (e.g., enrollment date).

## Usage Example

```python
s1 = Student(name="Alice")
s2 = Student(name="Bob")

c1 = Course(title="Math")
c2 = Course(title="Science")

s1.courses.append(c1)
s1.courses.append(c2)
s2.courses.append(c1)

session.add_all([s1, s2])
session.commit()
```

## Querying

```python
# Get all courses for Alice
student = session.query(Student).filter_by(name="Alice").first()
for course in student.courses:
    print(course.title)

# Get all students in Math
course = session.query(Course).filter_by(title="Math").first()
for student in course.students:
    print(student.name)
```

```

```
