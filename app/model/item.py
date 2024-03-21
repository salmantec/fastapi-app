from sqlalchemy import Column, String, UUID
from sqlalchemy.orm import declarative_base
import uuid

SQLAlchemyBase = declarative_base()


class ItemTable(SQLAlchemyBase):
    __tablename__ = "item"

    id = Column(UUID, primary_key=True, default=uuid.uuid4())
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    state = Column(String, nullable=False)

    @classmethod
    def fields(cls):
        return [
            cls.id,
            cls.name,
            cls.description,
            cls.state
        ]