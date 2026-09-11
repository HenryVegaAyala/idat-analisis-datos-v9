# Condicionales en Python

# if: "si pasa esto..."
# elif: "si pasa esto otro... o si no pasa lo anterior"
# else: "si no pasa esto... o no cumple con la condición o por defecto"

# Ejemplo: Edad
edad = input("¿Cuál es tu edad? ")
edad = int(edad) # Convertimos la edad a un número entero

if edad < 18:
    print("Eres menor de edad.")
else:
    print("Eres mayor de edad.")

# Ejemplo: Calificación
nota = input("¿Cuál es tu calificación? ")
nota = float(nota) # Convertimos la nota a un número decimal

if nota >= 18:
    print("Excelente, has aprobado con honores.")
elif nota >= 14:
    print("Bien, has aprobado.")
elif nota >= 10:
    print("Suficiente, has aprobado por poco.")
else:
    print("Lo siento, has reprobado.")