from pydantic import BaseModel
from typing import Optional

# Base schema for Resources
class ResourcesBase(BaseModel):
    item: str
    amount: int
    unit: str

# Schema for creating a new Resource
class ResourcesCreate(ResourcesBase):
    pass

# Schema for updating an existing Resource
class ResourcesUpdate(BaseModel):
    item: Optional[str] = None
    amount: Optional[int] = None
    unit: Optional[str] = None

# Schema for returning Resource data (includes resourceId)
class Resources(ResourcesBase):
    resourceId: int

    class Config:
        orm_mode = True
