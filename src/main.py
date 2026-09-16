from decimal import Decimal
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, field_serializer
from src.domain.entities import Product
from src.infrastructure.factory import UseCaseFactory
from src.infrastructure.db.models import Base
from src.infrastructure.db.session import engine

Base.metadata.create_all(bind=engine)
app = FastAPI(title="SOREN Catalog")

class ProductIn(BaseModel):
  name: str
  description: str = ""
  price: Decimal
  stock: int =  0

class ProductOut(BaseModel):
  model_config = ConfigDict(from_attributes=True)

  id: int | None
  name: str
  description: str
  price: Decimal
  stock: int

  @field_serializer("price")
  def serialize_price(self, price: Decimal) -> float:
    return float(price)

@app.get("/products/search")
def search_products(q: str):
  return UseCaseFactory.search_products_use_case().execute(q)

@app.post("/products", status_code=201, response_model=ProductOut)
def create_product(payload: ProductIn):
  product = Product(id=None, **payload.model_dump())
  return UseCaseFactory.create_product_use_case().execute(product)

@app.get("/products/{product_id}", response_model=ProductOut)
def get_product(product_id: int):
  product = UseCaseFactory.get_product_use_case().execute(product_id)
  if not product:
    raise HTTPException(status_code=404, detail="Product not found")
  return product

@app.post("/notify/welcome")
def notify_welcome(email: str, name: str):
  UseCaseFactory.send_welcome_email_use_case().execute(email, name)
  return {"status": "queued"}
