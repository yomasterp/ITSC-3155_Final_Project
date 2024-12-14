from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from ..dependencies.Database import Base

class Ingredients(Base):
    __tablename__ = 'ingredients'

    ingredientId = Column(Integer, primary_key=True, index=True, autoincrement=True)
    menuItemId = Column(Integer, ForeignKey('menu_items.menuItemId'), nullable=False)
    resourceId = Column(Integer, ForeignKey('resources.resourceId'), nullable=False)
    description = Column(Text, nullable=False)
    amount = Column(Integer, nullable=False, default=0)

    menuItem = relationship('MenuItems', back_populates='ingredients')
    resource = relationship('Resources', back_populates='ingredients')
