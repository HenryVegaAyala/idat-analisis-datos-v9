import pandas as pd

data = pd.read_csv("facturacion_datos.csv")

# fillna -> Reemplazar valores nulos por un valor específico
data["id_cliente"] = data["id_cliente"].fillna("Desconocido")

# dropna -> Eliminar filas con valores nulos
data = data.dropna()

# drop_duplicates -> Eliminar filas duplicadas
data = data.drop_duplicates()

print(data)