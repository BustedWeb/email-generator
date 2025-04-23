from fastapi import APIRouter
from controllers.test import crear_item_controller
from models.test import Item 

router = APIRouter()

@router.post("/items")
def crear_item(item: Item):
    return crear_item_controller(item)

