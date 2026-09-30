import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("datos_fuga.csv")

x = df[["antiguedad", "cuota_mensual"]]
y = df["fuga"]

modelo = LogisticRegression()
modelo.fit(x, y)

experiencia = input("Introduce la antigüedad: ")
estudios = input("Introduce cuota mensual: ")

prediccion = pd.DataFrame([[experiencia, estudios]], columns=["antiguedad", "cuota_mensual"])

resultado = modelo.predict(prediccion)

if resultado[0] == 1:
    print("El cliente tiene probabilidad de fuga.")
else:
    print("El cliente tiene baja probabilidad de fuga.")