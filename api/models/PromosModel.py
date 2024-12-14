from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, DECIMAL, Enum
from sqlalchemy.orm import relationship
from ..dependencies.Database import Base

class Promotions(Base):
    __tablename__ = 'promotions'

    promotionId = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(20), unique=True, nullable=False)
    expirationDate = Column(DateTime, nullable=False)
    discountPercentage = Column(DECIMAL(5, 2), nullable=False)
    status = Column(Enum('Expired', 'Valid', name='status'), nullable=False)

    orders = relationship('Orders', back_populates='promotion')
    orderDetails = relationship('OrderDetails', back_populates='promotion')
