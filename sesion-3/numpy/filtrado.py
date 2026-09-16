import numpy as np

edades = np.array([17, 15, 20, 25, 30, 16, 85])

# Implementación de filtrado (Condición de búsqueda)
filtrado =  edades >= 18

# Aplicar el filtrado al array original
print(filtrado)
edades_filtradas = edades[filtrado]

# Resultado del filtrado
print(edades_filtradas)