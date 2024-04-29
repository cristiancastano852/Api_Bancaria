from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class User(BaseModel):
    id: Optional[str]
    username: str
    name: str
    email: str
    phone: Optional[str] = None
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)