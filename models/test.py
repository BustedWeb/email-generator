from pydantic import BaseModel

class Item(BaseModel):
    nombre: str
    precio: float