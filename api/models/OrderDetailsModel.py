from sqlalchemy import Column, Integer, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from ..dependencies.Database import Base

class OrderDetails(Base):
    __tablename__ = 'order_details'

    orderDetailId = Column(Integer, primary_key=True, autoincrement=True)
    orderId = Column(Integer, ForeignKey('orders.orderId'), nullable=False)
    menuItemId = Column(Integer, ForeignKey('menu_items.menuItemId'), nullable=False)
    quantity = Column(Integer, nullable=False)
    amount = Column(DECIMAL(10, 2), index=True, nullable=False)
    total = Column(DECIMAL(10, 2), nullable=True)
    promotionId = Column(Integer, ForeignKey('promotions.promotionId'), nullable=True)

    order = relationship('Orders', back_populates='orderDetails')
    menuItem = relationship('MenuItems', back_populates='orderDetails')
    promotion = relationship('Promotions', back_populates='orderDetails')
