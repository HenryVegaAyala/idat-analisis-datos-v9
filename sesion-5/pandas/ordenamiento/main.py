import pandas as pd
from pathlib import Path

DATA_DIR = (Path(__file__)).resolve().parent / "../../database"

csv_data = DATA_DIR / "dataset.txt"

# Leer el archivo CSV y crear un DataFrame
df = pd.read_csv(csv_data)

# Ordenar el DataFrame de menor a mayor
resultados_a = df.sort_values("Store ID")
print(resultados_a)

print("-" * 100)

# Ordenar el DataFrame de mayor a menor
resultados_b = df.sort_values("Store ID", ascending=False)
print(resultados_b)

print("-" * 100)

# Ordenar el DataFrame por múltiples columnas
resultados_c = df.sort_values(["Store ID", "Total Price"], ascending=[True, False])

print(resultados_c)