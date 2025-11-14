from .estructuras import Producto
from typing import Union

class ProductoFactory:
    """Factory para crear diferentes tipos de productos con validación."""
    
    @staticmethod
    def crear_ropa(nombre: str, cantidad: int, precio: float, veces_vendido: int = 0, 
                  talla: str = "M", material: str = "Algodón") -> Producto:
        """Crea un producto de tipo ropa."""
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
            
        producto = Producto(nombre, cantidad, precio, veces_vendido)
        producto.tipo = "ropa"
        producto.talla = talla
        producto.material = material
        return producto

    @staticmethod
    def crear_electronico(nombre: str, cantidad: int, precio: float, veces_vendido: int = 0,
                         garantia_meses: int = 12, voltaje: str = "110V") -> Producto:
        """Crea un producto de tipo electrónico."""
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
            
        producto = Producto(nombre, cantidad, precio, veces_vendido)
        producto.tipo = "electronico"
        producto.garantia_meses = garantia_meses
        producto.voltaje = voltaje
        return producto

    @staticmethod
    def desde_dict(datos: dict) -> Producto:
        """Crea un producto desde un diccionario."""
        tipo = datos.get('tipo', 'ropa')
        
        if tipo == 'ropa':
            return ProductoFactory.crear_ropa(
                datos['nombre'],
                datos['cantidad'],
                datos['precio'],
                datos.get('veces_vendido', 0),
                datos.get('talla', 'M'),
                datos.get('material', 'Algodón')
            )
        elif tipo == 'electronico':
            return ProductoFactory.crear_electronico(
                datos['nombre'],
                datos['cantidad'],
                datos['precio'],
                datos.get('veces_vendido', 0),
                datos.get('garantia_meses', 12),
                datos.get('voltaje', '110V')
            )
        else:
            raise ValueError(f"Tipo de producto no soportado: {tipo}")