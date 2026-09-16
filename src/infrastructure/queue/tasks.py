import smtplib
from src.config import settings
from src.infrastructure.db.session import SessionLocal
from src.infrastructure.db.postgres_repository import PostgresProductRepository
from src.infrastructure.search.meilisearch_index import MeilisearchIndex
from src.infrastructure.queue.email_builder import EmailBuilder

def index_product_task(product_id: int) -> None:
  session = SessionLocal()
  try:
    product = PostgresProductRepository(session).get_by_id(product_id)
    if product:
      MeilisearchIndex().index(product)
  finally:
    session.close()

def send_email_task(to: str, name: str) -> None:
  message = (
    EmailBuilder()
    .from_("noreply@soren.local")
    .to(to)
    .subject("Welcome!")
    .body(f"Hey {name}, welcome to the catalog!")
    .build()
  )

  with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as smtp:
    smtp.send_message(message)
