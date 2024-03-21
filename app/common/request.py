from typing import Optional

from abstract import Base
from constants import State


class ItemRequest(Base):
    name: str
    description: Optional[str]
    state: State