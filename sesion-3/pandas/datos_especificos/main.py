import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "../../database"

csv_path = DATA_DIR / "data_ventas_enero_2026.csv"

# Leer el archivo CSV
df = pd.read_csv(csv_path)

print(df[["producto", "precio_unitario"]])  # Imprime la columna "Producto" y "precio_unitario)