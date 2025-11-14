from .estructuras import ListaEnlazada, Producto
from typing import List

def cargar_inventario(ruta_archivo: str) -> ListaEnlazada:
    """
    Carga el inventario desde un archivo JSON.
    
    Args:
        ruta_archivo: Ruta al archivo JSON
        
    Returns:
        ListaEnlazada con los productos cargados
        
    Raises:
        FileNotFoundError: Si el archivo no existe
        ValueError: Si el formato del JSON es inválido
    """
    import json
    from .builders import construir_desde_json
    
    inventario = construir_desde_json(ruta_archivo)
    if inventario is None:
        raise FileNotFoundError(f"No se pudo cargar el archivo: {ruta_archivo}")
    return inventario

def calcular_valor_total(inventario: ListaEnlazada) -> float:
    """Calcula el valor total del inventario usando iteración."""
    return sum(producto.cantidad * producto.precio for producto in inventario)

def obtener_stock_bajo(inventario: ListaEnlazada, umbral: int = 10) -> List[Producto]:
    """Obtiene productos con stock bajo usando iteración."""
    return [p for p in inventario if p.cantidad < umbral]

def obtener_productos_mas_caros(inventario: ListaEnlazada, n: int = 5) -> List[Producto]:
    """Obtiene los N productos más caros."""
    productos_ordenados = sorted(inventario, key=lambda p: p.precio, reverse=True)
    return productos_ordenados[:n]

def obtener_productos_mas_vendidos(inventario: ListaEnlazada, n: int = 5) -> List[Producto]:
    """Obtiene los N productos más vendidos."""
    productos_ordenados = sorted(inventario, key=lambda p: p.veces_vendido, reverse=True)
    return productos_ordenados[:n]

def vender_producto(inventario: ListaEnlazada, nombre: str, cantidad: int = 1) -> bool:
    """
    Registra una venta de producto.
    
    Returns:
        True si la venta fue exitosa, False si no hay suficiente stock
    """
    producto = inventario.obtener_producto(nombre)
    if producto and producto.cantidad >= cantidad:
        producto.cantidad -= cantidad
        producto.veces_vendido += cantidad
        return True
    return False