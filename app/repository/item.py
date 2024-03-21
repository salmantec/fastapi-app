import logging
from sqlalchemy import insert

from app.common.request import ItemRequest
from app.model.item import ItemTable

logger = logging.getLogger(__name__)


def save_item(item: ItemRequest) -> list[dict]:
    logger.debug(f"Persisting Item: {item}")
    sql = insert(ItemTable).values(**item.dict()).returning(*ItemTable.fields())
    results =