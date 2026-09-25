import matplotlib.pyplot as plt

edades = [20, 22, 21, 25, 30, 35, 18, 19, 40, 45, 22, 23, 21]

plt.hist(edades, bins=5, color="blue", edgecolor="black")

plt.show()