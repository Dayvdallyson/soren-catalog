from rq import Worker, Queue
from src.infrastructure.queue.connection import QueueConnection

if __name__ == "__main__":
    connection = QueueConnection.get_instance()
    Worker([Queue("catalog", connection=connection)], connection=connection).work()
