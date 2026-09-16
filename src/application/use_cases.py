import json
from src.domain.entities import Product
from src.domain.repositories import ProductRepository, Cache, SearchIndex, TaskQueue


class GetProductUseCase:
    def __init__(self, repository: ProductRepository, cache: Cache):
        self._repository = repository
        self._cache = cache

    def execute(self, product_id: int) -> Product | None:
        cache_key = f"product:{product_id}"

        cached = self._cache.get(cache_key)
        if cached:
            return Product(**json.loads(cached))

        product = self._repository.get_by_id(product_id)
        if product:
            self._cache.set(cache_key, json.dumps(product.__dict__, default=str))
        return product


class CreateProductUseCase:
    def __init__(self, repository: ProductRepository, cache: Cache, queue: TaskQueue):
        self._repository = repository
        self._cache = cache
        self._queue = queue

    def execute(self, product: Product) -> Product:
        created = self._repository.create(product)
        self._cache.delete(f"product:{created.id}")
        self._queue.enqueue("src.infrastructure.queue.tasks.index_product_task", created.id)
        return created


class SearchProductsUseCase:
    def __init__(self, search_index: SearchIndex):
        self._search_index = search_index

    def execute(self, query: str) -> list[dict]:
        return self._search_index.search(query)


class SendWelcomeEmailUseCase:
    """Demonstrates the async task -> outside world branch of the diagram."""

    def __init__(self, queue: TaskQueue):
        self._queue = queue

    def execute(self, email: str, name: str) -> None:
        self._queue.enqueue("src.infrastructure.queue.tasks.send_email_task", email, name)
