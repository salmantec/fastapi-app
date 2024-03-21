import logging
from typing import Optional, Union
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

class AbstractConnection(ABC):
    def __init__(self, override_url=None):
        self.override_url = override_url
        self._engine: Optional[Union[]]