import pytest
import os
import tempfile
import json
from inventario_libreria import (
    Producto, 
    ListaEnlazada, 
    InventarioBuilder,
    ProductoFactory,
    cargar_inventario,
    calcular_valor_total,
    obtener_stock_bajo,
    vender_producto
)

class TestProducto:
    def test_creacion_producto(self):
        producto = Producto("Camiseta", 10, 25.0, 5)
        assert producto.nombre == "Camiseta"
        assert producto.cantidad == 10
        assert producto.precio == 25.0
        assert producto.veces_vendido == 5

class TestListaEnlazada:
    def test_agregar_y_obtener_producto(self):
        lista = ListaEnlazada()
        producto = Producto("Test", 5, 10.0)
        lista.agregar_producto(producto)
        
        assert len(lista) == 1
        assert lista.obtener_producto("Test") == producto

    def test_eliminar_producto(self):
        lista = ListaEnlazada()
        producto = Producto("Test", 5, 10.0)
        lista.agregar_producto(producto)
        
        assert lista.eliminar_producto("Test") == True
        assert len(lista) == 0
        assert lista.obtener_producto("Test") is None

class TestInventarioBuilder:
    def test_construir_inventario(self):
        builder = InventarioBuilder()
        inventario = builder.agregar_producto("Producto1", 10, 15.0).construir()
        
        assert len(inventario) == 1
        assert inventario.obtener_producto("Producto1") is not None

def test_carga_inventario_json():
    # Crear archivo temporal para测试
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump([{"nombre": "Test", "cantidad": 5, "precio": 10.0}], f)
        temp_path = f.name
    
    try:
        inventario = cargar_inventario(temp_path)
        assert len(inventario) == 1
        assert inventario.obtener_producto("Test") is not None
    finally:
        os.unlink(temp_path)

if __name__ == "__main__":
    pytest.main([__file__, "-v"])