import matplotlib.pyplot as plt

horas = [1, 2, 3, 4]
ventas = [10, 20, 25, 30]

plt.plot(horas, ventas)
plt.title("Ventas de café por hora")
plt.xlabel("Hora del día")
plt.ylabel("Número de ventas")
plt.show()
