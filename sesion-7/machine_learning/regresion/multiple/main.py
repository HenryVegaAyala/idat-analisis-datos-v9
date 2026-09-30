import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("datos_salarios.csv")

x = df[["experiencia", "estudios"]]
y = df["salario"]

modelo = LinearRegression()
modelo.fit(x, y)

experiencia = input("Introduce la experiencia en años: ")
estudios = input("Introduce el nivel de estudios: ")

prediccion = pd.DataFrame([[experiencia, estudios]], columns=["experiencia", "estudios"])

resultado = modelo.predict(prediccion)

print(f"El salario estimado es: S/.{resultado[0]:.2f}")