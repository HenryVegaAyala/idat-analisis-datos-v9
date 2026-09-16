import pprint

import pandas as pd

# Leer el archivo CSV y crear un DataFrame

df = pd.read_csv("data_ventas_enero_2026.csv")

print(df)

# Leer el archivo Excel y crear un DataFrame
df_excel = pd.read_excel("data_resultado_2026.xlsx", sheet_name="Sheet1")

print(df_excel)