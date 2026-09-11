def saludar_analista(nombre, apellido):
    saludo = (f"Hola {nombre} {apellido}!, "
              f"bienvenido al curso de Python "
              f"para analistas de datos.")
    return saludo

respuesta = saludar_analista("Juan", "Perez")
print(respuesta)