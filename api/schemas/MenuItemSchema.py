from pydantic import BaseModel
from typing import Optional

# Base schema for Menu Items
class MenuItemsBase(BaseModel):
    name: str
    price: float
    calories: int
    category: str

# Schema for creating a new Menu Item
class MenuItemsCreate(MenuItemsBase):
    pass

# Schema for updating an existing Menu Item
class MenuItemsUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None
    category: Optional[str] = None

# Schema for returning Menu Item data (includes menuItemId)
class MenuItems(MenuItemsBase):
    menuItemId: int

    class Config:
        orm_mode = True
