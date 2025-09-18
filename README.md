# Mi_libreria

# Inventario Librería

Una librería pequeña para la gestión de inventario y cálculos básicos. Este proyecto fue desarrollado como parte de un ejercicio de empaquetado y publicación en PyPI.

## Funcionalidades Principales

* **Gestión de inventario**: Carga de datos desde un archivo JSON.
* **Análisis de stock**: Identifica productos con stock bajo.
* **Análisis de ventas**: Identifica productos más vendidos.
* **Generación de reportes**: Crea reportes en formato Markdown.
* **Cálculos básicos**: Realiza sumas y restas de productos.

## Requisitos

* Python 3.8 o superior
* Los paquetes se instalarán automáticamente con `pip`.

## Instalación

Puedes instalar la librería directamente desde PyPI usando `pip`:

```bash
pip install inventario-libreria
```

---

Ejemplos de Uso
```markdown
Ejemplos de Uso

1.  **Cargar el inventario desde un archivo JSON**:
    ```python
    from inventario_libreria.funciones import cargar_inventario
    from inventario_libreria.builders import construir_reporte

    inventario_cargado = cargar_inventario("inventario.json")

    # Muestra el inventario por consola
    print(construir_reporte(inventario_cargado.obtener_productos()))
    ```

2.  **Obtener productos con stock bajo**:
    ```python
    from inventario_libreria.funciones import cargar_inventario, obtener_stock_bajo
    from inventario_libreria.builders import construir_reporte

    inventario_cargado = cargar_inventario("inventario.json")
    productos_bajo_stock = obtener_stock_bajo(inventario_cargado)

    print(f"Productos con stock bajo: {productos_bajo_stock}")
    ```

3.  **Obtener productos más vendidos**:
    ```python
    from inventario_libreria.funciones import cargar_inventario, obtener_productos_mas_vendidos
    from inventario_libreria.builders import construir_reporte

    inventario_cargado = cargar_inventario("inventario.json")
    productos_mas_vendidos = obtener_productos_mas_vendidos(inventario_cargado, 3)

    print(f"Los 3 productos más vendidos son: {productos_mas_vendidos}")
    ```

## Contribuciones

Si deseas contribuir, puedes hacerlo a través de mi repositorio en GitHub. ¡Toda contribución es bienvenida!

## Licencia

Este proyecto está bajo la Licencia MIT.