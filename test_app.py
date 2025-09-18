from inventario_libreria.funciones import calcular_valor_total, obtener_stock_bajo, obtener_productos_mas_caros, obtener_productos_mas_vendidos
from inventario_libreria.builders import construir_desde_json, InventarioBuilder

# Usa la funcion para construir el inventario desde el archivo JSON
mi_inventario = construir_desde_json('inventario.json')

if mi_inventario:
    # 1. Calcular el valor total del inventario
    valor_total = calcular_valor_total(mi_inventario)
    print(f"El valor total del inventario de ropa es: ${valor_total:,.2f}")

    # 2. Identificar productos con stock bajo
    productos_por_reponer = obtener_stock_bajo(mi_inventario, 10)
    nombres_productos_bajos = [p.nombre for p in productos_por_reponer]
    print(f"Productos que necesitan ser reabastecidos (stock < 10): {nombres_productos_bajos}")

    # 3. Obtener los 3 productos más caros
    productos_mas_caros = obtener_productos_mas_caros(mi_inventario, 3)
    nombres_productos_caros = [p.nombre for p in productos_mas_caros]
    print(f"Los 3 productos más caros son: {nombres_productos_caros}")

    # 4. Obtener los 3 productos más vendidos
    productos_mas_vendidos = obtener_productos_mas_vendidos(mi_inventario, 3)
    nombres_productos_vendidos = [p.nombre for p in productos_mas_vendidos]
    print(f"Los 3 productos más vendidos son: {nombres_productos_vendidos}")
else:
    print("No se pudo cargar el inventario. Revise el archivo inventario.json.")