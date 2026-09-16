import numpy as np

lista = [10, 20, 30, 40]
print(f"Lista original: {lista}")

array = np.array(lista)
print(f"Array de NumPy: {array}")

print(lista * 3) # Repetición de la lista
print(array * 3) # Multiplicación de cada elemento