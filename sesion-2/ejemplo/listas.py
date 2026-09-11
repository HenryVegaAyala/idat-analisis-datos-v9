# 1. Crear una lista de productos de cadenas
productos = ["libros", "lapiceros", "cuadernos", "mochilas", "calculadoras"]

# 2. Crear una lista de precios de productos de números
precios = [15, 1, 5, 30, 25]

# 3. Crear una lista de valores mixtos
valores_mixtos = ["Hola", 10, True, 3.14, None]

# 4. Acceder a un elemento de una lista por su índice
producto_escogido = productos[2]
print(f"Producto escogido: {producto_escogido}")

# 5. Acceder al último elemento de una lista
ultimo_producto = productos[-1]
print(f"Último producto: {ultimo_producto}")

# 6. Agregar un nuevo producto a la lista
productos.append("Hoja bond")
print(f"Lista de productos agregados: {productos}")

# 7. Cambiar o actualizar un elemento de la lista
productos[1] = "lapiceros de colores"
print(f"Lista de productos actualizada: {productos}")

# 8. Eliminar un elemento de la lista por su índice
del productos[-1]
print(f"Lista de productos después de eliminar el último: {productos}")

# 9. Eliminar un elemento de la lista por su valor
productos.remove("lapiceros de colores")
print(f"Lista de productos después de eliminar: {productos}")

# 10. Obtener la longitud de la lista
total_productos = len(productos)
print(f"Total de productos: {total_productos}")
