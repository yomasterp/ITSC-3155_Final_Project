from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.Database import Base

class RatingsReviews(Base):
    __tablename__ = 'ratings_reviews'

    reviewId = Column(Integer, primary_key=True, autoincrement=True)
    menuItemId = Column(Integer, ForeignKey('menu_items.menuItemId'), nullable=False)
    customerId = Column(Integer, ForeignKey('customers.customerId'), nullable=False)
    rating = Column(Integer, nullable=False)
    reviewText = Column(Text, nullable=True)
    createdAt = Column(DateTime, nullable=False, default=datetime.utcnow)

    menuItem = relationship('MenuItems', back_populates='reviews')
    customer = relationship('Customers', back_populates='reviews')
