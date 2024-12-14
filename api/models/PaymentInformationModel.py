from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from ..dependencies.Database import Base

class PaymentInfo(Base):
    __tablename__ = 'payment_info'

    paymentId = Column(Integer, primary_key=True, autoincrement=True)
    orderId = Column(Integer, ForeignKey('orders.orderId'), nullable=False)
    cardNumber = Column(String(19), nullable=False)
    expiryDate = Column(String(5), nullable=False)
    cardHolderName = Column(String(100), nullable=False)
    paymentType = Column(Enum('Credit Card', 'Debit Card', 'PayPal', name='payment_type'), nullable=False)

    order = relationship('Orders', back_populates='paymentInfo')
