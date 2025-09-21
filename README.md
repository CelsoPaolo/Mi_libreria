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
```
# Quiénes podrían usar esta librería y por qué

Esta librería es una herramienta de gestión de inventario simple y modular. Es ideal para:

* **Desarrolladores** principiantes: Es un excelente proyecto para aprender sobre la estructura de una librería, el uso de clases y la implementación de pruebas unitarias.

* **Pequeños negocios**: Puede ser utilizada como una solución rápida para gestionar inventarios sencillos sin la complejidad de un software comercial.

* **Analistas de datos**: Ofrece una base para prototipar ideas o para manejar pequeños conjuntos de datos de inventario.

# ¿Para qué les serviría?

* **Gestión eficiente**: Permite llevar un control sencillo del stock y las ventas de productos de manera programática.

* **Toma de decisiones**: Ayuda a identificar rápidamente productos con bajo stock o los más populares.

* **Automatización**: La librería puede ser integrada en scripts para automatizar reportes o alertas de inventario.


![agregando captura](Captura%20de%20pantalla%202025-09-20%20211544.png)