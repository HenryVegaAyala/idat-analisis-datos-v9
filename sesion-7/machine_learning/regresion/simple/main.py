import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. Cargar los datos
data = pd.read_csv('ventas_marketing.csv')

# 2. Preparar los datos
X = data[["marketing"]] # Dataframe de una sola columna

Y = data["ventas"] # Serie de una sola columna

# 3. Crear el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X, Y) # Se encarga de encontrar la mejor línea que se ajusta a los datos

variable_a_predecir = input("Ingrese la inversión en marketing para predecir las ventas: ")

# 4. Hacer predicciones
nueva_prediccion = pd.DataFrame([[float(variable_a_predecir)]], columns=["marketing"])

prediccion = modelo.predict(nueva_prediccion)

print(f"La predicción de ventas para una inversión en marketing de "
      f"${variable_a_predecir} es: {prediccion[0]:.2f}")