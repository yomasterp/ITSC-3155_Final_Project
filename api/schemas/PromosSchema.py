from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Base schema for Promotions
class PromotionsBase(BaseModel):
    code: str
    expirationDate: datetime
    discountPercentage: float
    status: str

# Schema for creating a new Promotion
class PromotionsCreate(PromotionsBase):
    pass

# Schema for updating an existing Promotion
class PromotionsUpdate(BaseModel):
    code: Optional[str] = None
    expirationDate: Optional[datetime] = None
    discountPercentage: Optional[float] = None
    status: Optional[str] = None

# Schema for returning Promotion data (includes promotionId)
class Promotions(PromotionsBase):
    promotionId: int

    class Config:
        orm_mode = True
