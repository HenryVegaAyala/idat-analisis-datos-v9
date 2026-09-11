def calcular_igv(precio_base: float | int):
    igv = 0.18
    impuesto = precio_base * igv
    precio_total = precio_base + impuesto

    return precio_total


# Ejemplo de uso uno a uno
producto_a = calcular_igv(100)
print(f"El precio total del producto A con IGV es: {producto_a}")

producto_b = calcular_igv(250)
print(f"El precio total del producto B con IGV es: {producto_b}")

# Ejemplo de uso con un bucle
productos = [100, 200, 500, 9000, 40, 20, 5]
for item in productos:
    resultado = calcular_igv(item)
    print(f"El precio total del producto con precio base {item} con IGV es: {resultado}")
