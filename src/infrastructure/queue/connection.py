import redis
from src.config import settings

class QueueConnection:
  _instance: redis.Redis | None = None

  @classmethod
  def get_instance(cls) -> redis.Redis:
    if cls._instance is None:
      cls._instance = redis.from_url(settings.REDIS_URL)
    return cls._instance
