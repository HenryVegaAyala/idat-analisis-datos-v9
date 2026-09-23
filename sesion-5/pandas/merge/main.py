import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

clientes = pd.read_csv("database/clientes.csv")
ventas = pd.read_csv("database/ventas.csv")

# Ejemplo de inner join
consolidado_inner = pd.merge(
    ventas,
    clientes,
    on="id_cliente",
    how="inner"
)

# print(consolidado_inner)

# Ejemplo de left join
consolidado_left = pd.merge(
    ventas,
    clientes,
    on="id_cliente",
    how="left"
)

# print(consolidado_left)

# Ejemplo de right join
consolidado_right = pd.merge(
    ventas,
    clientes,
    on="id_cliente",
    how="right"
)

# print(consolidado_right)


# Ejemplo de outer join
consolidado_outer = pd.merge(
    ventas,
    clientes,
    on="id_cliente",
    how="outer"
)

print(consolidado_outer)
