import pandas as pd
import numpy as np
import scipy.stats as st

# 1. Leer y cargar los datos del archivo CSV
df = pd.read_csv("heladeria_gastos.csv")
datos_gastos = df["gasto"]

# 2. Calcular el intervalo de confianza
intervalo = st.t.interval(
    confidence=0.95,           # Nivel de confianza del 95%
    df=len(datos_gastos) - 1,  # Grados de libertad
    loc=np.mean(datos_gastos), # Media o promedio de los datos
    scale=st.sem(datos_gastos) # Error estándar de la media
)

# 3. Imprimir el intervalo de confianza
limite_inferior = intervalo[0]
limite_superior = intervalo[1]

print(f"Con un 95% de confianza, el gasto promedio se encuentra "
      f"entre S/. {limite_inferior:.2f} "
      f"y S/. {limite_superior:.2f}.")

# 4. Calcular el promedio de los gastos
promedio_gastos = np.mean(datos_gastos)
print(f"El gasto promedio es de S/. {promedio_gastos:.2f}.")

# 5. Calcular el margen de error
margen_error = (limite_superior - promedio_gastos)
print(f"El margen de error es de S/. {margen_error:.2f}.")