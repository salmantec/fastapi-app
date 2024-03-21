from fastapi import APIRouter

from app.common.request import ItemRequest
from app.common.response import ItemResponse
import app.service.item as item_service

item_router = APIRouter(prefix="/item")


@item_router.post("/")
async def create_item(new_item: ItemRequest) -> ItemResponse:
    return item_service.save_item(new_item)


