from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.Database import Base

class Resources(Base):
    __tablename__ = 'resources'

    resourceId = Column(Integer, primary_key=True, index=True)
    item = Column(String(50), nullable=False)
    amount = Column(Integer, nullable=False)
    unit = Column(String(20), nullable=False)

    ingredients = relationship('Ingredients', back_populates='resource')
