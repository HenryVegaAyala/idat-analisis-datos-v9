import pandas as pd
import glob
from pathlib import Path

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

DATA_DIR = (Path(__file__)).resolve().parent / "../database"

# Buscar archivos CSV en el directorio
csv_files = glob.glob(str(DATA_DIR / "ventas_*.csv"))

# Buscar y contar todos los archivos CSV encontrados
print(f"Archivos CSV encontrados: {len(csv_files)}")

data_frames = []

# Leer cada archivo CSV y agregarlo a la lista de DataFrames
for archivo in csv_files:
    df = pd.read_csv(archivo)

    data_frames.append(df)

# Concatenar todos los DataFrames en uno solo
df_concatenado = pd.concat(data_frames, ignore_index=True)

print(df_concatenado)