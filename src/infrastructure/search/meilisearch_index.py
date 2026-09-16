import meilisearch
from src.domain.entities import Product
from src.domain.repositories import SearchIndex
from src.config import settings

class MeilisearchIndex(SearchIndex):
  def __init__(self):
    client = meilisearch.Client(settings.MEILI_URL, settings.MEILI_KEY)
    self._index = client.index("products")

  def index(self, product: Product) -> None:
    self._index.add_documents([{
      "id": product.id,
      "name": product.name,
      "description": product.description,
      "price": float(product.price),
    }])

  def search(self, query: str) -> list[dict]:
    return self._index.search(query)["hits"]
