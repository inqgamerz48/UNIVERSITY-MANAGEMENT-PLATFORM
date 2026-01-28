from sqlalchemy import Column, String, Boolean, DateTime, Enum
from sqlalchemy.sql import func
from app.db.session import Base
import enum

class UserRole(str, enum.Enum):
    STUDENT = "student"
    FACULTY = "faculty"
    ADMIN = "admin"
    PARENT = "parent"

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True) # Clerk ID or internal UUID? Clerk ID is string.
    # We will use internal UUID for our DB, and store clerk_id as bridge.
    # Actually, using Clerk ID as PK is cleaner if 1:1 map.
    # Let's use UUID for PK and clerk_id as unique index for flexibility.
    
    clerk_id = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(String, default=UserRole.STUDENT.value) # Storing as string for simplicity with Enum
    
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
