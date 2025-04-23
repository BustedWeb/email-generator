def crear_item_controller(item):
    precio_final = item.precio * 1.16
    return {"nombre": item.nombre, "precio_final": precio_final}