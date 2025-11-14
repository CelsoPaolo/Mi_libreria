from inventario_libreria.funciones import calcular_valor_total, obtener_stock_bajo, obtener_productos_mas_caros, obtener_productos_mas_vendidos
from inventario_libreria.builders import construir_desde_json

def main():
    """Función principal para demostrar el uso de la librería."""
    
    # Construir el inventario desde JSON
    mi_inventario = construir_desde_json('inventario.json')

    if not mi_inventario:
        print("No se pudo cargar el inventario. Revise el archivo 'inventario.json'.")
        return

    print("📊 === REPORTE DE INVENTARIO === 📊\n")

    # 1. Calcular el valor total del inventario
    valor_total = calcular_valor_total(mi_inventario)
    print(f"Valor total del inventario: ${valor_total:,.2f}\n")

    # 2. Identificar productos con stock bajo
    productos_por_reponer = obtener_stock_bajo(mi_inventario, 10)
    nombres_productos_bajos = [p.nombre for p in productos_por_reponer]
    print(f"Productos que necesitan reposición (stock < 10): {nombres_productos_bajos}\n")

    # 3. Obtener los 3 productos más caros
    productos_mas_caros = obtener_productos_mas_caros(mi_inventario, 3)
    nombres_productos_caros = [p.nombre for p in productos_mas_caros]
    print(f"Los 3 productos más caros: {nombres_productos_caros}\n")

    # 4. Obtener los 3 productos más vendidos
    productos_mas_vendidos = obtener_productos_mas_vendidos(mi_inventario, 3)
    nombres_productos_vendidos = [p.nombre for p in productos_mas_vendidos]
    print(f"Los 3 productos más vendidos: {nombres_productos_vendidos}\n")

    print("✅ Demostración completada exitosamente!")

    

if __name__ == "__main__":
    main()