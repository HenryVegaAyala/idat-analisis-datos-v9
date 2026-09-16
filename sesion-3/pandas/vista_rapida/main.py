import pandas as pd
from pathlib import Path

# Carpeta donde está main.py
BASE_DIR = Path(__file__).resolve().parent

# Directorio donde está la base de datos
DATABASE_DIR = BASE_DIR / "../../database"
csv_path = DATABASE_DIR / "data_ventas_enero_2026.csv"

# Leer el archivo CSV
df = pd.read_csv(csv_path)

print(df)