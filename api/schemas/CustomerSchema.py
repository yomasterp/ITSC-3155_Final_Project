from pydantic import BaseModel, EmailStr
from typing import Optional

# Base schema for Customer
class CustomerBase(BaseModel):
    name: str
    email: EmailStr
    phoneNumber: Optional[str] = None
    address: Optional[str] = None

# Schema for creating a new Customer
class CustomerCreate(CustomerBase):
    pass

# Schema for updating an existing Customer
class CustomerUpdate(CustomerBase):
    phoneNumber: Optional[str] = None
    address: Optional[str] = None

# Schema for returning Customer data (includes customerId)
class Customer(CustomerBase):
    customerId: int

    class Config:
        orm_mode = True
