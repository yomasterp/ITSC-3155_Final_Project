from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.dialects.mysql import DECIMAL
from sqlalchemy.orm import relationship
from ..dependencies.Database import Base

class MenuItems(Base):
    __tablename__ = 'menu_items'

    menuItemId = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    calories = Column(Integer, nullable=False)
    category = Column(Enum('Vegetarian', 'Non-Vegetarian', 'Vegan', 'Gluten-Free', 'Dairy-Free', name='category_type'), nullable=False)

    orderDetails = relationship('OrderDetails', back_populates='menuItem')
    ingredients = relationship('Ingredients', back_populates='menuItem')
    reviews = relationship('RatingsReviews', back_populates='menuItem')
