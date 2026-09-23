import pandas as pd
from pathlib import Path

DATA_DIR = (Path(__file__)).resolve().parent / "../../database"

csv_data = DATA_DIR / "dataset.txt"

# Leer el archivo CSV y crear un DataFrame
df = pd.read_csv(csv_data)
print(df.head())
print("-" * 150)

# Eliminar filas del archivo en memoria
df.drop([0, 1], axis=0, inplace=True)
print(df)
print("-" * 150)

# Eliminar columnas del archivo en memoria
df.drop(["Store ID", "Total Price"], axis=1, inplace=True)
print(df)