from __future__ import annotations

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship, Mapped, mapped_column
from colorama import Fore, init

# Automatically reset terminal text color after each print
init(autoreset=True)

# Database configuration
DB = "sqlite:///user.db"
engine = create_engine(DB, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Faker instance for generating fake data

# Base class for all ORM models
class Base(DeclarativeBase):
    """
    Base class for all ORM models. Automatically includes a primary key 'id'.
    """
    id: Mapped[int] = mapped_column(primary_key=True)

class Employee(Base):
    """
    Employee model representing a user in the system.

    Fields:
        - id: Primary key.
        - username: Name of the employee.
        - email: Email address.
        - manager_id: ID of the manager (self-referential FK).
        - addresses: List of addresses associated with the employee.
        - subordinates: Employees who report to this manager.
        - manager: The manager this employee reports to.
    """
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    manager_id: Mapped[int] = mapped_column(ForeignKey("employees.id"), nullable=True)

    # One-to-many relationship: one employee can have multiple addresses
    addresses: Mapped[list[Address]] = relationship("Address", back_populates="employee")

    # Self-referential one-to-many: manager to subordinates
    subordinates: Mapped[list[Employee]] = relationship("Employee", back_populates="manager")
    manager: Mapped[Employee | None] = relationship("Employee", back_populates="subordinates", remote_side=[id])

    def __repr__(self) -> str:
        return Fore.YELLOW + f"<Employee (username={self.username}, email={self.email})>"

class Address(Base):
    """
    Address model representing the address of an employee.

    Fields:
        - employee_id: Foreign key to the associated employee.
        - city: City name.
        - state: State name.
        - zip_code: ZIP code.
        - employee: Relationship back to the Employee.
    """
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True)
    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id"))
    city: Mapped[str] = mapped_column(String)
    state: Mapped[str] = mapped_column(String)
    zip_code: Mapped[str] = mapped_column(String)

    # Many-to-one relationship back to Employee
    employee: Mapped[Employee] = relationship("Employee", back_populates="addresses")
    
    def __repr__(self) -> str:
        return Fore.YELLOW + f"<Address (city={self.city}, state={self.state}, zip_code={self.zip_code})>"

# Drop existing tables and create new ones
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

if __name__ == "__main__":
    # Create a manager
    manager = Employee(username="Alice Manager", email="alice.manager@example.com")

    # Create a subordinate reporting to the manager
    subordinate = Employee(username="Bob Employee", email="bob@example.com")
    subordinate.manager = manager

    # Create addresses for both
    address1 = Address(city="New York", state="NY", zip_code="10001", employee=manager)
    address2 = Address(city="Los Angeles", state="CA", zip_code="90001", employee=subordinate)

    # Add all to the session and commit
    session.add_all([manager, subordinate, address1, address2])
    session.commit()

    # Fetch and print to verify relationships
    print("\n=== Test Output ===")
    fetched_manager = session.query(Employee).filter_by(username="Alice Manager").first()
    fetched_sub = session.query(Employee).filter_by(username="Bob Employee").first()

    print(f"Manager: {fetched_manager}")
    print(f"Subordinates of Manager: {fetched_manager.subordinates}")
    print(f"Manager of {fetched_sub.username}: {fetched_sub.manager}")
    print(f"Addresses of Manager: {fetched_manager.addresses}")
    print(f"Addresses of Subordinate: {fetched_sub.addresses}")
