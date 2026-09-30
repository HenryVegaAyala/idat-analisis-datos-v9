import pandas as pd
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("dato_credito.csv")

x = df[["ingreso", "morosidad"]]
y = df["aprobado"]

modelo = DecisionTreeClassifier()
modelo.fit(x, y)

salario = input("Introduce el salario: ")
morosidad = input("Introduce si tiene mororsidad: ")

prediccion = pd.DataFrame([[salario, morosidad]], columns=["ingreso", "morosidad"])

resultado = modelo.predict(prediccion)

if resultado[0] == 1:
    print("El crédito fue aprobado.")
else:
    print("El crédito fue rechazado.")