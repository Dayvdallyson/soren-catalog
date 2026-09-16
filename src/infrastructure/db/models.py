from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ProductModel(Base):
  __tablename__ = "products"

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)
  description = Column(String, default="")
  price = Column(Numeric(10, 2), nullable=False)
  stock = Column(Integer, default=0)
