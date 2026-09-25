import matplotlib.pyplot as plt

edades = [
    18, 19, 21, 25, 26, 26, 30, 32, 38, 40, 45, 50
]

plt.hist(
    edades,
    bins=5,
    color="skyblue",
    edgecolor="black"
)

plt.title("Distribución de edades", fontsize=17)
plt.xlabel("Edad", fontsize=14)
plt.ylabel("Frecuencia", fontsize=14)

plt.show()