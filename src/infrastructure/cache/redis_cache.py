import redis
from src.domain.repositories import Cache
from src.config import settings

class RedisConnection:
  _instance: redis.Redis | None = None

  @classmethod
  def get_instance(cls) -> redis.Redis:
    if cls._instance is None:
      cls._instance = redis.from_url(settings.REDIS_URL, decode_responses=True)
    return cls._instance

class RedisCache(Cache):
  def __init__(self):
    self._client = RedisConnection.get_instance()

  def get(self, key: str) -> str | None:
    return self._client.get(key)

  def set(self, key: str, value: str, ttl: int = 300) -> None:
    self._client.set(key, value, ex=ttl)

  def delete(self, key: str) -> None:
    self._client.delete(key)
