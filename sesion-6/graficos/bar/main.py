import matplotlib.pyplot as plt

animales = ["Perros", "Gatos", "Aves", "Peces"]
cantidad = [45, 38, 12, 5]

plt.bar(
    animales,
    cantidad,
    color=["orange", "blue", "green", "cyan"],
)

plt.grid(True, linestyle="--", alpha=0.4)

plt.title("Cantidad de animales por tipo", fontsize=17)
plt.xlabel("Tipo de animal", fontsize=14)
plt.ylabel("Cantidad", fontsize=14)

for x, y in zip(animales, cantidad):
    plt.text(x, y + 1, str(y), va="center")

plt.show()