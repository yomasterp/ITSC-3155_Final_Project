from pydantic import BaseModel
from typing import Optional

# Base schema for Payment Information
class PaymentInfoBase(BaseModel):
    orderId: int
    cardNumber: str
    expiryDate: str
    cardHolderName: str
    paymentType: str

# Schema for creating new Payment Information
class PaymentInfoCreate(PaymentInfoBase):
    pass

# Schema for updating existing Payment Information
class PaymentInfoUpdate(BaseModel):
    cardNumber: Optional[str] = None
    expiryDate: Optional[str] = None
    cardHolderName: Optional[str] = None
    paymentType: Optional[str] = None

# Schema for returning Payment Information data (includes paymentId)
class PaymentInfo(PaymentInfoBase):
    paymentId: int

    class Config:
        orm_mode = True
