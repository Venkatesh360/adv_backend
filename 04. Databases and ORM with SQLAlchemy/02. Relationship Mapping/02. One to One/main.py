from __future__ import annotations

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship, Mapped, mapped_column
from colorama import Fore, init
from faker import Faker

# Automatically reset terminal text color after each print
init(autoreset=True)

# Database configuration
DB = "sqlite:///user.db"
engine = create_engine(DB, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Faker instance for generating fake data
fake = Faker()

# Base class for all ORM models
class Base(DeclarativeBase):
    """
    Base class for all ORM models.
    Provides an auto-incrementing primary key 'id' for all subclasses.
    """
    id: Mapped[int] = mapped_column(primary_key=True)


class User(Base):
    """
    User model representing a user.

    Fields:
        - id: Primary key (inherited from Base).
        - name: User's full name.
        - email: User's email address.
        - address: One-to-one relationship to Address.
    """
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)

    # One-to-one relationship to Address; uselist=False enforces one-to-one
    address: Mapped[Address] = relationship("Address", back_populates="user", uselist=False)

    def __repr__(self):
        return Fore.GREEN + f"<User(name={self.name}, email={self.email})>"


class Address(Base):
    """
    Address model representing the address of a user.

    Fields:
        - id: Primary key (auto-generated).
        - user_id: Foreign key to User.id (unique to enforce one-to-one).
        - city: City name.
        - state: State name.
        - zip_code: ZIP code.
        - user: Relationship back to User.
    """
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
    city: Mapped[str] = mapped_column(String)
    state: Mapped[str] = mapped_column(String)
    zip_code: Mapped[str] = mapped_column(String)

    # Relationship back to the User object
    user: Mapped[User] = relationship("User", back_populates="address")

    def __repr__(self) -> str:
        return Fore.YELLOW + f"<Address(city={self.city}, state={self.state}, zip_code={self.zip_code})>"


# Drop all tables and recreate schema
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# Inline test
if __name__ == "__main__":
    # Create a new user and associated address using Faker
    user = User(name=fake.name(), email=fake.email())
    address = Address(city=fake.city(), state=fake.state(), zip_code=fake.zipcode(), user=user)

    # Add user (and cascade address) to the session and commit
    session.add(user)
    session.commit()

    print("\n=== One-to-One Test ===")
    fetched_user = session.query(User).first()
    fetched_address = session.query(Address).first()

    print(f"User: {fetched_user}")
    print(f"User's Address: {fetched_user.address}")
    print(f"Address's User: {fetched_address.user}")
