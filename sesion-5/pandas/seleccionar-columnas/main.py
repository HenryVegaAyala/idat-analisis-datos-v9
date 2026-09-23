import pandas as pd
from pathlib import Path

DATA_DIR = (Path(__file__)).resolve().parent / "../../database"

csv_data = DATA_DIR / "dataset.txt"

# Leer el archivo CSV y crear un DataFrame
df = pd.read_csv(csv_data)

print(
    df[["Store ID", "Total Price"]]
)