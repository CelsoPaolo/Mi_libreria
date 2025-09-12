

from inventario_libreria.inventario import ListaEnlazada, Producto, calcular_valor_total, obtener_stock_bajo, obtener_productos_mas_caros

mi_inventario_tienda_ropa = ListaEnlazada()
mi_inventario_tienda_ropa.agregar_producto(Producto("Camiseta", 50, 15.00))
mi_inventario_tienda_ropa.agregar_producto(Producto("Pantalón", 20, 45.50))
mi_inventario_tienda_ropa.agregar_producto(Producto("Calcetines", 5, 5.00))
mi_inventario_tienda_ropa.agregar_producto(Producto("Chamarra de cuero", 8, 120.00))
mi_inventario_tienda_ropa.agregar_producto(Producto("Sudadera con capucha", 15, 30.00))
mi_inventario_tienda_ropa.agregar_producto(Producto("Zapatillas deportivas", 12, 85.00))
mi_inventario_tienda_ropa.agregar_producto(Producto("Gorra de béisbol", 3, 10.00))
mi_inventario_tienda_ropa.agregar_producto(Producto("Bufanda de lana", 25, 20.00))
mi_inventario_tienda_ropa.agregar_producto(Producto("Jeans ajustados", 40, 55.00))
mi_inventario_tienda_ropa.agregar_producto(Producto("Vestido de noche", 2, 250.00))


valor_total = calcular_valor_total(mi_inventario_tienda_ropa)
print(f"El valor total del inventario de ropa es: ${valor_total:,.2f}")

productos_por_reponer = obtener_stock_bajo(mi_inventario_tienda_ropa, 10)
nombres_productos_bajos = [p.nombre for p in productos_por_reponer]
print(f"Productos que necesitan ser reabastecidos: {nombres_productos_bajos}")

productos_mas_caros = obtener_productos_mas_caros(mi_inventario_tienda_ropa, 3)
nombres_productos_caros = [p.nombre for p in productos_mas_caros]
print(f"Los 3 productos más caros son: {nombres_productos_caros}")