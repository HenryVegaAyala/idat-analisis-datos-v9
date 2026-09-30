import pandas as pd
import scipy.stats as st
import numpy as np

df = pd.read_csv("tiempos_de_entrega_delivery.csv")

vehiculo_tradicional = df[df["vehiculo"] == "Tradicional"]["minutos"]
vehiculo_electrico = df[df["vehiculo"] == "Electrica"]["minutos"]

ic_tradicional = st.t.interval(
    confidence=0.95,
    df=len(vehiculo_tradicional) - 1,
    loc=np.mean(vehiculo_tradicional),
    scale=st.sem(vehiculo_tradicional),
)

print(f"Rangos del intervalo de confianza del 95% "
      f"para el tiempo de entrega con vehículo "
      f"tradicional: {ic_tradicional[0]:.2f} a {ic_tradicional[1]:.2f} minutos")

print(f"Promedio del vehículo tradicional: {np.mean(ic_tradicional):.2f} minutos")

ic_electrico = st.t.interval(
    confidence=0.95,
    df=len(vehiculo_electrico) - 1,
    loc=np.mean(vehiculo_electrico),
    scale=st.sem(vehiculo_electrico),
)

print(f"Rangos del intervalo de confianza del 95% "
      f"para el tiempo de entrega con vehículo "
      f"eléctrico: {ic_electrico[0]:.2f} a {ic_electrico[1]:.2f} minutos")

print(f"Promedio del vehículo eléctrico: {np.mean(ic_electrico):.2f} minutos")

# Paso 2: Prueba de test A/B

resultado = st.ttest_ind(vehiculo_tradicional, vehiculo_electrico)
print(f"Valor P: {resultado.pvalue:.5f}")

if resultado.pvalue < 0.05:
    print("Rechazamos la hipótesis nula: "
          "hay una diferencia significativa "
          "en los tiempos de entrega entre los vehículos.")
else:
    print("No rechazamos la hipótesis nula: "
          "no hay una diferencia significativa "
          "en los tiempos de entrega entre los vehículos.")