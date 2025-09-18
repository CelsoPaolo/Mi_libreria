import pytest
import os
from inventario_libreria.estructuras import Producto, ListaEnlazada
from inventario_libreria.funciones import calcular_valor_total, obtener_stock_bajo, obtener_productos_mas_caros, obtener_productos_mas_vendidos
from inventario_libreria.builders import construir_desde_json

# Fixture para cargar el inventario de prueba
@pytest.fixture
def inventario_test():
    """Fixture que construye y retorna un inventario para las pruebas."""
    ruta_json = 'inventario.json'
    if not os.path.exists(ruta_json):
        # En un escenario real, puedes crear un archivo de prueba.
        # Para este ejemplo, asumimos que el archivo ya esta en la ruta.
        return None
    
    return construir_desde_json(ruta_json)

def test_valor_total(inventario_test):
    """Prueba que el calculo de valor total sea correcto."""
    if inventario_test:
        valor_total = calcular_valor_total(inventario_test)
        # Calcula el valor total esperado manualmente para la comparacion
        # Total esperado basado en el inventario.json que creamos
        # (50*15) + (20*45.5) + (5*5) + (8*120) + (15*30) + (12*85) + (3*10) + (25*20) + (40*55) + (2*250) = 750 + 910 + 25 + 960 + 450 + 1020 + 30 + 500 + 2200 + 500 = 7345
        assert valor_total == 7345.0, "El valor total no es el esperado."

def test_obtener_stock_bajo(inventario_test):
    """Prueba que la funcion de stock bajo retorne los productos correctos."""
    if inventario_test:
        productos_bajos = obtener_stock_bajo(inventario_test, 10)
        nombres_bajos = [p.nombre for p in productos_bajos]
        # Productos esperados con stock < 10: Calcetines, Chamarra, Gorra, Vestido
        assert set(nombres_bajos) == {"Calcetines", "Chamarra de cuero", "Gorra de béisbol", "Vestido de noche"}, "Los productos con stock bajo no son correctos."

def test_productos_mas_caros(inventario_test):
    """Prueba que la funcion de productos mas caros retorne los productos correctos."""
    if inventario_test:
        productos_caros = obtener_productos_mas_caros(inventario_test, 3)
        nombres_caros = [p.nombre for p in productos_caros]
        # Productos esperados: Vestido, Chamarra, Zapatillas
        assert nombres_caros == ["Vestido de noche", "Chamarra de cuero", "Zapatillas deportivas"], "Los productos mas caros no son correctos."

def test_productos_mas_vendidos(inventario_test):
    """Prueba que la funcion de productos mas vendidos retorne los productos correctos."""
    if inventario_test:
        productos_vendidos = obtener_productos_mas_vendidos(inventario_test, 3)
        nombres_vendidos = [p.nombre for p in productos_vendidos]
        # Productos esperados: Jeans, Camiseta, Sudadera
        assert nombres_vendidos == ["Jeans ajustados", "Camiseta", "Sudadera con capucha"], "Los productos mas vendidos no son correctos."