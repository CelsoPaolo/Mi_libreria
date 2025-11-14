"""
Inventario Librería - Una librería para gestión de inventarios.
"""

from .estructuras import Producto, ListaEnlazada
from .builders import InventarioBuilder, construir_desde_json
from .factory import ProductoFactory
from .funciones import (
    cargar_inventario,
    calcular_valor_total,
    obtener_stock_bajo,
    obtener_productos_mas_caros,
    obtener_productos_mas_vendidos,
    vender_producto
)

__version__ = "0.2.0"
__author__ = "Celso Paolo Velasco Espinoza"
__all__ = [
    'Producto',
    'ListaEnlazada', 
    'InventarioBuilder',
    'ProductoFactory',
    'cargar_inventario',
    'calcular_valor_total',
    'obtener_stock_bajo',
    'obtener_productos_mas_caros',
    'obtener_productos_mas_vendidos',
    'vender_producto',
    'construir_desde_json'
]