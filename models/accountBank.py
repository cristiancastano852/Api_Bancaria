from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum


class AccountType(str, Enum):
    ahorros = "Ahorros"
    corriente = "Corriente"

class AccountBank(BaseModel):
    id: Optional[str]
    user_id: str
    account_number: str
    balance: float
    account_type: AccountType
    is_active: bool = True
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)