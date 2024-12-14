from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from ..dependencies.Database import Base

class Orders(Base):
    __tablename__ = 'orders'

    orderId = Column(Integer, primary_key=True, autoincrement=True)
    customerId = Column(Integer, ForeignKey('customers.customerId'), nullable=False)
    orderType = Column(Enum('Takeout', 'Delivery', name='order_type'), nullable=False)
    orderDate = Column(DateTime, nullable=False, default=datetime.utcnow)
    orderStatus = Column(Enum('Pending', 'In Progress', 'Shipped', 'Delivered', 'Cancelled', name='order_status'), nullable=False)
    trackingNumber = Column(String(50), unique=True, nullable=False)
    promotionId = Column(Integer, ForeignKey('promotions.promotionId'), nullable=True)

    customer = relationship('Customers', back_populates='orders')
    promotion = relationship('Promotions', back_populates='orders')
    orderDetails = relationship('OrderDetails', back_populates='order')
    paymentInfo = relationship('PaymentInfo', back_populates='order')
