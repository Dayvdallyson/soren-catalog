from rq import Queue
from src.domain.repositories import TaskQueue
from src.infrastructure.queue.connection import QueueConnection


class RQTaskQueue(TaskQueue):
  def __init__(self):
    self._queue = Queue("catalog", connection=QueueConnection.get_instance())

  def enqueue(self, func_path: str, *args) -> None:
    self._queue.enqueue(func_path, *args)
