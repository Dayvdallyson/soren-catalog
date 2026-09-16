from sqlalchemy.orm import Session
from src.domain.entities import Product
from src.domain.repositories import ProductRepository
from src.infrastructure.db.models import ProductModel


class PostgresProductRepository(ProductRepository):
    def __init__(self, session: Session):
        self._session = session

    def get_by_id(self, product_id: int) -> Product | None:
        row = self._session.get(ProductModel, product_id)
        return self._to_entity(row) if row else None

    def create(self, product: Product) -> Product:
        row = ProductModel(
            name=product.name,
            description=product.description,
            price=product.price,
            stock=product.stock,
        )
        self._session.add(row)
        self._session.commit()
        self._session.refresh(row)
        return self._to_entity(row)

    @staticmethod
    def _to_entity(row: ProductModel) -> Product:
        return Product(
            id=row.id, name=row.name, description=row.description,
            price=row.price, stock=row.stock,
        )
