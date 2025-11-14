#!/usr/bin/env python3
"""
Script de gestión de inventario - Interfaz práctica para tu librería
"""

from inventario_libreria import cargar_inventario, ListaEnlazada, Producto
from inventario_libreria.builders import InventarioBuilder

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*50)
    print("🛒 SISTEMA DE GESTIÓN DE INVENTARIO")
    print("="*50)
    print("1. 📦 Ver todos los productos")
    print("2. 🔍 Buscar producto por nombre")
    print("3. 📈 Ver productos con stock bajo")
    print("4. 💰 Ver productos más caros")
    print("5. 🏆 Ver productos más vendidos")
    print("6. ➕ Agregar nuevo producto")
    print("7. 🛒 Registrar venta")
    print("8. 📊 Valor total del inventario")
    print("9. ❌ Salir")
    print("="*50)

def ver_todos_productos(inventario):
    """Muestra todos los productos"""
    print("\n📦 LISTA COMPLETA DE PRODUCTOS:")
    print("-" * 40)
    for producto in inventario:
        print(f"├─ {producto.nombre}")
        print(f"│  Stock: {producto.cantidad} | Precio: ${producto.precio} | Vendidos: {producto.veces_vendido}")
    print("-" * 40)

def buscar_producto(inventario):
    """Busca un producto por nombre"""
    nombre = input("🔍 Ingresa el nombre del producto a buscar: ").strip()
    producto = inventario.obtener_producto(nombre)
    
    if producto:
        print(f"\n✅ PRODUCTO ENCONTRADO:")
        print(f"   Nombre: {producto.nombre}")
        print(f"   Stock: {producto.cantidad}")
        print(f"   Precio: ${producto.precio:.2f}")
        print(f"   Veces vendido: {producto.veces_vendido}")
    else:
        print(f"❌ Producto '{nombre}' no encontrado")

def ver_stock_bajo(inventario):
    """Muestra productos con stock bajo"""
    from inventario_libreria.funciones import obtener_stock_bajo
    
    productos_bajos = obtener_stock_bajo(inventario, 10)
    
    if productos_bajos:
        print("\n⚠️  PRODUCTOS CON STOCK BAJO (<10 unidades):")
        for producto in productos_bajos:
            print(f"   • {producto.nombre} - Stock: {producto.cantidad}")
    else:
        print("✅ Todos los productos tienen stock suficiente")

def ver_productos_caros(inventario):
    """Muestra los productos más caros"""
    from inventario_libreria.funciones import obtener_productos_mas_caros
    
    productos_caros = obtener_productos_mas_caros(inventario, 3)
    
    print("\n💎 PRODUCTOS MÁS CAROS:")
    for i, producto in enumerate(productos_caros, 1):
        print(f"   {i}. {producto.nombre} - ${producto.precio:.2f}")

def ver_mas_vendidos(inventario):
    """Muestra los productos más vendidos"""
    from inventario_libreria.funciones import obtener_productos_mas_vendidos
    
    mas_vendidos = obtener_productos_mas_vendidos(inventario, 3)
    
    print("\n🔥 PRODUCTOS MÁS VENDIDOS:")
    for i, producto in enumerate(mas_vendidos, 1):
        print(f"   {i}. {producto.nombre} - Vendidos: {producto.veces_vendido}")

def agregar_nuevo_producto(inventario):
    """Agrega un nuevo producto al inventario"""
    print("\n➕ AGREGAR NUEVO PRODUCTO")
    
    nombre = input("Nombre del producto: ").strip()
    
    # Verificar si ya existe
    if inventario.obtener_producto(nombre):
        print(f"❌ El producto '{nombre}' ya existe")
        return
    
    try:
        cantidad = int(input("Cantidad en stock: "))
        precio = float(input("Precio: $"))
        
        # Crear y agregar el producto
        nuevo_producto = Producto(nombre, cantidad, precio)
        inventario.agregar_producto(nuevo_producto)
        
        print(f"✅ Producto '{nombre}' agregado exitosamente!")
        
    except ValueError:
        print("❌ Error: Cantidad debe ser número entero, Precio debe ser número")

def registrar_venta(inventario):
    """Registra una venta de producto"""
    print("\n🛒 REGISTRAR VENTA")
    
    nombre = input("Nombre del producto vendido: ").strip()
    producto = inventario.obtener_producto(nombre)
    
    if not producto:
        print(f"❌ Producto '{nombre}' no encontrado")
        return
    
    print(f"   Stock actual de {producto.nombre}: {producto.cantidad}")
    
    try:
        cantidad_vendida = int(input("Cantidad vendida: "))
        
        if cantidad_vendida <= 0:
            print("❌ La cantidad debe ser mayor a 0")
            return
            
        if cantidad_vendida > producto.cantidad:
            print(f"❌ Stock insuficiente. Solo hay {producto.cantidad} unidades")
            return
        
        # Actualizar stock y ventas
        producto.cantidad -= cantidad_vendida
        producto.veces_vendido += cantidad_vendida
        
        print(f"✅ Venta registrada!")
        print(f"   Nuevo stock de {producto.nombre}: {producto.cantidad}")
        print(f"   Total vendido: {producto.veces_vendido}")
        
    except ValueError:
        print("❌ Error: La cantidad debe ser un número entero")

def ver_valor_total(inventario):
    """Muestra el valor total del inventario"""
    from inventario_libreria.funciones import calcular_valor_total
    
    valor_total = calcular_valor_total(inventario)
    print(f"\n💰 VALOR TOTAL DEL INVENTARIO: ${valor_total:,.2f}")

def main():
    """Función principal"""
    print("🔄 Cargando inventario...")
    
    try:
        inventario = cargar_inventario("inventario.json")
        print("✅ Inventario cargado exitosamente!")
    except Exception as e:
        print(f"❌ Error al cargar inventario: {e}")
        return
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("\n👉 Selecciona una opción (1-9): ").strip()
            
            if opcion == "1":
                ver_todos_productos(inventario)
            elif opcion == "2":
                buscar_producto(inventario)
            elif opcion == "3":
                ver_stock_bajo(inventario)
            elif opcion == "4":
                ver_productos_caros(inventario)
            elif opcion == "5":
                ver_mas_vendidos(inventario)
            elif opcion == "6":
                agregar_nuevo_producto(inventario)
            elif opcion == "7":
                registrar_venta(inventario)
            elif opcion == "8":
                ver_valor_total(inventario)
            elif opcion == "9":
                print("\n👋 ¡Hasta luego!")
                break
            else:
                print("❌ Opción inválida. Por favor elige 1-9")
                
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    main()