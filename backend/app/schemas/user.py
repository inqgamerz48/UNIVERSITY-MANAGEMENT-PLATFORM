from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from uuid import UUID

class UserBase(BaseModel):
    email: EmailStr
    is_active: Optional[bool] = True
    role: Optional[str] = "student"

class UserCreate(UserBase):
    clerk_id: str

class UserUpdate(UserBase):
    pass

class UserInDBBase(UserBase):
    id: UUID
    clerk_id: str
    created_at: datetime

    class Config:
        from_attributes = True

class User(UserInDBBase):
    pass
