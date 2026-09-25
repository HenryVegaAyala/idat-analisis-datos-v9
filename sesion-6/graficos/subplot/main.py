import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 2, figsize=(10, 5)) # una sola fila solo se usa indice
# fig, axs = plt.subplots(2, 2, figsize=(10, 5)) # si usamos 2 filas a mas  se una intervalo

fig.suptitle('Ejemplo de visualización de datos con subplots')

# Grafico de lineas
meses = ['Enero', 'Febrero', 'Marzo']
ventas = [100, 2000, 2550]

axs[0].plot(meses, ventas, marker='o')
axs[0].set_title('Ventas por mes')
axs[0].set_xlabel('Meses')
axs[0].set_ylabel('Ventas')

# Grafico de barras
productos = ['Producto A', 'Producto B', 'Producto C']
cantidades = [50, 75, 100]

axs[1].bar(productos, cantidades, color='orange')
axs[1].set_title('Cantidad de productos vendidos')
axs[1].set_xlabel('Productos')
axs[1].set_ylabel('Cantidad')

plt.show()