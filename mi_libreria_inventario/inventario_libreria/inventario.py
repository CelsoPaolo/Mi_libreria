class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

#metrica de inventario atomica

class Nodo:
    def __init__(self, producto):
        self.producto = producto
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_producto(self, producto):  #asegura que cada producto que añadas se coloque al final de la cola del inventario, manteniendo el orden y la estructura de la lista enlazada.
        nuevo_nodo = Nodo(producto)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

def calcular_valor_total(inventario):
    valor_total = 0
    actual = inventario.cabeza
    while actual:
        valor_total += actual.producto.cantidad * actual.producto.precio
        actual = actual.siguiente
    return valor_total

def obtener_stock_bajo(inventario, umbral):
    productos_bajos = []
    actual = inventario.cabeza
    while actual:
        if actual.producto.cantidad < umbral:
            productos_bajos.append(actual.producto)
        actual = actual.siguiente
    return productos_bajos

def obtener_productos_mas_caros(inventario, n):
    productos = []
    actual = inventario.cabeza
    while actual:
        productos.append(actual.producto)
        actual = actual.siguiente
    
    productos.sort(key=lambda p: p.precio, reverse=True)
    return productos[:n]