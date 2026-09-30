import pandas as pd
import scipy.stats as st

# 1. Cargar los datos del archivo CSV
df = pd.read_csv("embalaje_puntaje.csv")

# 2. Separar en 2 grupos según el tipo de embalaje
embalaje_tradicional = df[df["embalaje"] == "A"]["puntuacion"]  # Filtro para obtener el valor del embalaje tradicional
embalaje_ecologico = df[df["embalaje"] == "B"]["puntuacion"]  # Filtro para obtener el valor del embalaje ecológico

# 3. Calcular el Test A/B
resultado = st.ttest_ind(embalaje_tradicional, embalaje_ecologico)

# 4. Imprimir el resultado del Test A/B
print(f"Valor P: {resultado.pvalue:.4f}")

if resultado.pvalue < 0.05:
    print(f"Rechazamos la hipótesis nula. Hay evidencia "
          f"suficiente para afirmar que hay una diferencia "
          f"significativa entre los dos tipos de embalaje.")
else:
    print(f"No rechazamos la hipótesis nula. No hay "
          f"evidencia suficiente para afirmar que hay "
          f"una diferencia significativa entre los dos "
          f"tipos de embalaje.")