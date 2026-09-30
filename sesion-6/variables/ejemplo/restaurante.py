import pandas as pd

clientes = [20, 22, 22, 25, 61]

data = pd.Series(clientes)

promedio = data.mean()
mediana = data.median()
moda = data.mode()

print(f"Promedio: {promedio}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda.values[0]}")