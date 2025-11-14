class Producto:
    """Clase que representa un producto en el inventario."""
    def __init__(self, nombre: str, cantidad: int, precio: float, veces_vendido: int = 0):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.veces_vendido = veces_vendido

class Nodo:
    """Clase que representa un nodo en la lista enlazada."""
    def __init__(self, producto: Producto):
        self.producto = producto
        self.siguiente = None

class ListaEnlazada:
    """Lista enlazada con funcionalidad completa."""
    
    def __init__(self):
        self.cabeza = None
        self._tamano = 0  # CORREGIDO: faltaban dos puntos

    def agregar_producto(self, producto: Producto):  # CORREGIDO: "Producto" con mayúscula
        nuevo_nodo = Nodo(producto)  # CORREGIDO: "Nodo" con mayúscula
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self._tamano += 1  # CORREGIDO: faltaba el punto en "_tamano"

    def obtener_producto(self, nombre: str) -> Producto | None:
        """Obtiene un producto por nombre."""
        actual = self.cabeza
        while actual:
            if actual.producto.nombre == nombre:
                return actual.producto
            actual = actual.siguiente
        return None

    def __len__(self) -> int:
        """Permite usar len(inventario)."""
        return self._tamano

    def __iter__(self):
        """Hace la lista iterable."""
        actual = self.cabeza
        while actual:
            yield actual.producto
            actual = actual.siguiente