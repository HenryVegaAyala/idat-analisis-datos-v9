import matplotlib.pyplot as plt

semanas = [1, 2, 3, 4]
kilometros = [2, 5, 4, 8]

plt.plot(
    semanas,
    kilometros,
    color="green",
    marker="o",
    linestyle="--",
    linewidth=2,
    markersize=8,
)

plt.title('Progreso de kilometraje semanal', fontsize=17)
plt.xlabel('Semanas', fontsize=14)
plt.ylabel('Kilómetros recorridos', fontsize=14)

plt.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()

# Mostrar valores en cada punto
for x, y in zip(semanas, kilometros):
    plt.text(x, y + 0.2, str(y), ha="center")

plt.show()
