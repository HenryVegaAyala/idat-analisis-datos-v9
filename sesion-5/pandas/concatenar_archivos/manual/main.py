import pandas as pd
from pathlib import Path

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

DATA_DIR = (Path(__file__)).resolve().parent / "../database"

enero = pd.read_csv(DATA_DIR / "ventas_enero_2026.csv")
febrero = pd.read_csv(DATA_DIR / "ventas_febrero_2026.csv")
marzo = pd.read_csv(DATA_DIR / "ventas_marzo_2026.csv")

consolidado = pd.concat([enero, febrero, marzo], ignore_index=True)

print(consolidado)