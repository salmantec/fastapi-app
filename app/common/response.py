from typing import Optional
from uuid import UUID

from abstract import Base
from constants import State


class ItemResponse(Base):
    id: UUID
    name: str
    description: Optional[str]
    state: State