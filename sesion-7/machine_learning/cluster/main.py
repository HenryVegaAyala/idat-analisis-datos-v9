import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("datos_clientes.csv")

x = df[["gasto_anual", "visitas_mes"]]

modelo = KMeans(n_clusters=3)
modelo.fit(x)

df["cluster"] = modelo.labels_

print(df)