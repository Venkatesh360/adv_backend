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

class Base(DeclarativeBase):
    """
    Base class for all ORM models.
    Provides a primary key column 'id' for all subclasses.
    """
    id: Mapped[int] = mapped_column(primary_key=True)


class FollowingAssociation(Base):
    """
    Association table for many-to-many self-referential User following.

    Fields:
        - id: Primary key.
        - user_id: ID of the follower.
        - following_id: ID of the user being followed.
    """
    __tablename__ = "following_associations"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    following_id: Mapped[int] = mapped_column(ForeignKey("users.id"))


class User(Base):
    """
    User model with many-to-many self-referential relationship.

    Fields:
        - id: Primary key.
        - username: Username of the user.
        - email: Email address.
        - following: List of users this user is following.
        - followers: List of users following this user.
    """
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)

    following: Mapped[list[User]] = relationship(
        "User",
        secondary="following_associations",
        primaryjoin=lambda: User.id == FollowingAssociation.user_id,
        secondaryjoin=lambda: User.id == FollowingAssociation.following_id,
        back_populates="followers"
    )

    followers: Mapped[list[User]] = relationship(
        "User",
        secondary="following_associations",
        primaryjoin=lambda: User.id == FollowingAssociation.following_id,
        secondaryjoin=lambda: User.id == FollowingAssociation.user_id,
        back_populates="following"
    )

    def __repr__(self) -> str:
        return Fore.GREEN + f"<User(username={self.username}, email={self.email})>"


# Drop and recreate all tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Inline test
if __name__ == "__main__":
    # Create 3 users
    alice = User(username="Alice", email="alice@example.com")
    bob = User(username="Bob", email="bob@example.com")
    carol = User(username="Carol", email="carol@example.com")

    # Alice follows Bob and Carol
    alice.following.extend([bob, carol])

    # Bob follows Carol
    bob.following.append(carol)

    # Add all users to session
    session.add_all([alice, bob, carol])
    session.commit()

    # Test results
    print("\n=== Following Test ===")
    for user in session.query(User).all():
        print(f"{user.username} is following {[u.username for u in user.following]}")
        print(f"{user.username} is followed by {[u.username for u in user.followers]}")
        print()
