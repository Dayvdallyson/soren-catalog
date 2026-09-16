from src.infrastructure.db.session import SessionLocal
from src.infrastructure.db.postgres_repository import PostgresProductRepository
from src.infrastructure.cache.redis_cache import RedisCache
from src.infrastructure.search.meilisearch_index import MeilisearchIndex
from src.infrastructure.queue.producer import RQTaskQueue
from src.application.use_cases import (
  GetProductUseCase,
  CreateProductUseCase,
  SearchProductsUseCase,
  SendWelcomeEmailUseCase,
)

class UseCaseFactory:
  @staticmethod
  def get_product_use_case() -> GetProductUseCase:
    return GetProductUseCase(PostgresProductRepository(SessionLocal()), RedisCache())

  @staticmethod
  def create_product_use_case() -> CreateProductUseCase:
    return CreateProductUseCase(
      PostgresProductRepository(SessionLocal()), RedisCache(), RQTaskQueue()
    )

  @staticmethod
  def search_products_use_case() -> SearchProductsUseCase:
    return SearchProductsUseCase(MeilisearchIndex())

  @staticmethod
  def send_welcome_email_use_case() -> SendWelcomeEmailUseCase:
    return SendWelcomeEmailUseCase(RQTaskQueue())
