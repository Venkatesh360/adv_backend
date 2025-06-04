from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from faker import Faker
from colorama import Fore, init

init(autoreset=True)

DB_URL = "sqlite:///user.db"
fake = Faker()

engine = create_engine(DB_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    """
    Represents a user in the system.

    Attributes:
        id (int): Primary key identifier for the user.
        username (str): The username of the user.
        posts (List[Post]): List of posts made by the user, lazily loaded.
    
    Relationships:
        posts: Lazy-loaded relationship to Post objects with foreign key user_id.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    
    # Lazy loading: posts are loaded from the database only when accessed
    posts = relationship("Post", lazy="select", backref="user")

    def __repr__(self):
        return Fore.BLUE + f"User(id={self.id}, username='{self.username}')"


class Post(Base):
    """
    Represents a post created by a user.

    Attributes:
        id (int): Primary key identifier for the post.
        content (str): Content of the post.
        user_id (int): Foreign key to the user who created the post.
    """
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    content = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return Fore.GREEN + f"Post(id={self.id}, content='{self.content}', user_id={self.user_id})"


# Create tables in the database
Base.metadata.create_all(engine)


def add_dummy_data():
    """
    Adds a user with two dummy posts to the database.

    Uses Faker to generate random usernames and sentences for the post content.
    Commits the new objects to the session.
    """
    user = User(username=fake.user_name())
    post1 = Post(content=fake.sentence())
    post2 = Post(content=fake.sentence())
    
    user.posts.append(post1)
    user.posts.append(post2)
    
    session.add(user)
    session.commit()


def show_user_posts():
    """
    Queries all users and prints their information along with their posts.

    Demonstrates lazy loading by accessing the posts attribute, which triggers a separate SQL query per user.
    """
    users = session.query(User).all()
    for user in users:
        print(user)
        for post in user.posts:  # Lazy loading triggers here
            print("  ", post)


# Uncomment these to run example usage
# add_dummy_data()
# show_user_posts()
