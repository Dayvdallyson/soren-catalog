from dataclasses import dataclass
from decimal import Decimal

@dataclass(frozen=True)
class Product():
  id: int | None
  name: str
  description: str
  price: Decimal
  stock: int
