from sqlalchemy import Integer, String, Float, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship 

from database import Base

class Expense(Base):
  __tablename__ = 'expenses'
  id = Column(Integer, primary_key=True, index=True)
  title = Column(Float, nullable=False)
  amount = Column(Float, nullable=False)
  note = Column(String, nullable=True)

category_id = Column(Integer, ForeignKey('categories.id', nullable=False))  