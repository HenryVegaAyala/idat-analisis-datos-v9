def convertir_soles(monto_dolares: float | int, tasa_cambio: float = 3.80):
    monto_soles = monto_dolares * tasa_cambio
    return monto_soles

# Ejemplo de conversion por defecto
resultado1 = convertir_soles(100)
print(f"100 dólares equivalen a {resultado1} soles")

# Ejemplo de conversion con tasa de cambio personalizada
resultado2 = convertir_soles(200, 3.60)
print(f"200 dólares equivalen a {resultado2} soles")
