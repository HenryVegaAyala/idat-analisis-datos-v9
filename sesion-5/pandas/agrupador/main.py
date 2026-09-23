import pandas as pd
from pathlib import Path

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

DATA_DIR = (Path(__file__)).resolve().parent / "../../database"

csv_data = DATA_DIR / "dataset.txt"

# Leer el archivo CSV y crear un DataFrame
df = pd.read_csv(csv_data)

# Agrupar los datos por la columna 'Store ID' y calcular la suma de la columna 'Total Price'
agrupado = df.groupby('Store ID')['Total Price'].sum()

# print(agrupado)

# agrupador de datos
resultados = (df.groupby('Store ID')['Total Price']
              .sum()
              .rename("Total Price Sum")
              .reset_index())

print(resultados)