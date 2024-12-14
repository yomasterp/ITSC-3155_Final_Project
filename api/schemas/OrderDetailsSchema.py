from pydantic import BaseModel
from typing import Optional

# Base schema for Order Details
class OrderDetailsBase(BaseModel):
    orderId: int
    menuItemId: int
    quantity: int
    amount: float
    total: Optional[float] = None
    promotionId: Optional[int] = None

# Schema for creating a new Order Detail
class OrderDetailsCreate(OrderDetailsBase):
    pass

# Schema for updating an existing Order Detail
class OrderDetailsUpdate(BaseModel):
    menuItemId: Optional[int] = None
    quantity: Optional[int] = None
    amount: Optional[float] = None
    total: Optional[float] = None
    promotionId: Optional[int] = None

# Schema for returning Order Detail data (includes orderDetailId)
class OrderDetails(OrderDetailsBase):
    orderDetailId: int

    class Config:
        orm_mode = True
