import numpy as np

ventas = np.array([1500, 2300, 1800, 2100, 2500])

# Calcular la venta total
venta_total = np.sum(ventas)
print(f"Venta total: {venta_total}")

# Calcular la venta promedio
venta_promedio = np.mean(ventas)
print(f"Venta promedio: {venta_promedio}")

# Calcular la venta máxima
venta_maxima = np.max(ventas)
print(f"Venta máxima: {venta_maxima}")