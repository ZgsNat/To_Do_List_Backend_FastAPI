# src/infrastructure/database/models/user_model.py
from sqlalchemy import Column, Integer, String, Enum, Date
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class Role(enum.Enum):
    USER = "user"
    ADMIN = "admin"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    dob = Column(Date)  # Date of Birth
    role = Column(Enum(Role), default=Role.USER)
    