import numpy as np

lista = [22, 21, 23, 90, 22, 20, 105, 21]

sensores = np.array(lista)
print(sensores)
error = sensores > 50
print(error)

errores = sensores[error]
print(errores)

a = len(errores)
print(a)
