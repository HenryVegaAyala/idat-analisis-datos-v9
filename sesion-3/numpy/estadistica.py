import numpy as np

lista = [1, 2, 3]

array = np.array(lista)

# estadística

suma_total = np.sum(array)
print(f"Suma total: {suma_total}")

promedio = np.mean(array)
print(f"Promedio: {promedio}")

maximo_valor = np.max(array)
print(f"Máximo valor: {maximo_valor}")

desviacion_estandar = np.std(array)
print(f"Desviación estándar: {desviacion_estandar}")