from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Base schema for Orders
class OrdersBase(BaseModel):
    customerId: int
    orderType: str
    orderStatus: str
    trackingNumber: str
    promotionId: Optional[int] = None

# Schema for creating a new Order
class OrdersCreate(OrdersBase):
    pass

# Schema for updating an existing Order
class OrdersUpdate(BaseModel):
    orderType: Optional[str] = None
    orderStatus: Optional[str] = None
    trackingNumber: Optional[str] = None
    promotionId: Optional[int] = None

# Schema for returning Order data (includes orderId and orderDate)
class Orders(OrdersBase):
    orderId: int
    orderDate: datetime

    class Config:
        orm_mode = True
