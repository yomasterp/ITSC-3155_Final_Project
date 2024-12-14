from pydantic import BaseModel
from typing import Optional

# Base schema for Ingredients
class IngredientsBase(BaseModel):
    menuItemId: int
    resourceId: int
    description: str
    amount: int

# Schema for creating a new Ingredient
class IngredientsCreate(IngredientsBase):
    pass

# Schema for updating an existing Ingredient
class IngredientsUpdate(BaseModel):
    menuItemId: Optional[int] = None
    resourceId: Optional[int] = None
    description: Optional[str] = None
    amount: Optional[int] = None

# Schema for returning Ingredient data (includes ingredientId)
class Ingredients(IngredientsBase):
    ingredientId: int

    class Config:
        orm_mode = True
