import json
from .estructuras import ListaEnlazada, Producto
from .factory import ProductoFactory
from typing import List

class InventarioBuilder:
    """Builder para construir inventarios con validación."""
    
    def __init__(self):
        self._inventario = ListaEnlazada()
        self._productos_agregados = set()

    def agregar_producto(self, nombre: str, cantidad: int, precio: float, veces_vendido: int = 0) -> 'InventarioBuilder':
        if nombre in self._productos_agregados:
            raise ValueError(f"El producto '{nombre}' ya existe en el inventario")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
            
        producto = Producto(nombre, cantidad, precio, veces_vendido)
        self._inventario.agregar_producto(producto)
        self._productos_agregados.add(nombre)
        return self

    def construir(self) -> ListaEnlazada:
        """Retorna el inventario construido."""
        if len(self._inventario) == 0:
            raise ValueError("No se pueden construir inventarios vacíos")
        return self._inventario

def construir_desde_json(ruta_archivo: str) -> ListaEnlazada:
    """
    Construye un inventario desde JSON con mejor manejo de errores.
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
        
        if not isinstance(datos, list):
            raise ValueError("El JSON debe contener una lista de productos")
            
        builder = InventarioBuilder()
        for item in datos:
            builder.agregar_producto(
                item['nombre'],
                item['cantidad'],
                item['precio'],
                item.get('veces_vendido', 0)
            )
        return builder.construir()
        
    except FileNotFoundError:
        raise FileNotFoundError(f"Archivo no encontrado: {ruta_archivo}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error en formato JSON: {e}")
    except KeyError as e:
        raise ValueError(f"Falta campo requerido en JSON: {e}")