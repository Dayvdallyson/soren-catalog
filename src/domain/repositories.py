from abc import ABC, abstractmethod
from src.domain.entities import Product

class ProductRepository(ABC):
  @abstractmethod
  def get_by_id(self, product_id: int) -> Product | None: ...

  @abstractmethod
  def create(self, product: Product) -> Product: ...

class Cache(ABC):
  @abstractmethod
  def get(self, key: str) -> str | None: ...

  @abstractmethod
  def set(self, key: str, value: str, ttl: int = 300) -> None: ...

  @abstractmethod
  def delete(self, key: str) -> None: ...

class SearchIndex(ABC):
  @abstractmethod
  def index(self, product: Product) -> None: ...

  @abstractmethod
  def search(self, query: str) -> list[dict]: ...

class TaskQueue(ABC):
  @abstractmethod
  def enqueue(self, func_path: str, *args) -> None: ...
