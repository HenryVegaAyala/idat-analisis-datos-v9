import pandas as pd

# Crear un DataFrame a partir de un diccionario

data = {
    "Nombres": ["Juan", "Pedro"],
    "Edades": [25, 30],
    "Ciudad": ["Lima", "Arequipa"]
}

df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df)