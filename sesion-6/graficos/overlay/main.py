import matplotlib.pyplot as plt

mes = ["Enero", "Febrero", "Marzo", "Abril"]

luz = [100, 80, 120, 90]
agua = [50, 60, 90, 40]

plt.plot(
    mes,
    luz,
    label="Servicios de luz",
    marker="o",
    linewidth=3,
    color="green",
)

plt.plot(
    mes,
    agua,
    label="Servicios de agua",
    marker="s",
    linewidth=3,
    color="blue",
)

plt.title("Servicios de luz y agua", fontsize=18)
plt.xlabel("Meses", fontsize=14)
plt.ylabel("Consumo", fontsize=14)

plt.grid(True, linestyle="--", linewidth=0.4)

plt.legend()

plt.show()