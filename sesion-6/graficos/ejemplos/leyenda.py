import matplotlib.pyplot as plt

# Datos de ejemplo
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]

plt.plot(y1, label='Serie 1', color='blue')
plt.plot(y2, label='Serie 2', color='orange')

plt.legend()
plt.show()