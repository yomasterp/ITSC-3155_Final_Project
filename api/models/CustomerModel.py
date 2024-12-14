from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.Database import Base

class Customer(Base):
    __tablename__ = 'customers'

    customerId = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phoneNumber = Column(String(20), nullable=False)
    address = Column(String(200), nullable=False)

    orders = relationship('Order', back_populates='customer')
    reviews = relationship('RatingAndReview', back_populates='customer')
