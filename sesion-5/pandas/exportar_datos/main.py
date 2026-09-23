import pandas as pd
from pathlib import Path

DATA_DIR = (Path(__file__)).resolve().parent / "../../database"

csv_data = DATA_DIR / "dataset.txt"

df = pd.read_csv(csv_data)

df["new_column"] = pd.Timestamp.now()

df.to_csv("dataset.csv")
df.to_excel("dataset.xlsx")