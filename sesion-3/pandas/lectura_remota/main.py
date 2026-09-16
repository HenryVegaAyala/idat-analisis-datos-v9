import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", None)

df = pd.read_csv("https://raw.githubusercontent.com/kwaldenphd/pandas-intro/main/data/titanic.csv")

print(df.head())