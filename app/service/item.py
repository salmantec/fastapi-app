import logging
from typing import Optional

from app.common.request import ItemRequest
from app.common.response import ItemResponse
import app.repository.item as item_repository

logger = logging.getLogger(__name__)


def save_item(item: ItemRequest) -> ItemResponse:
    logger.info(f"Saving Item: {item}")
    results = item_repository.save_item(item)
    return ItemResponse(**results[0])