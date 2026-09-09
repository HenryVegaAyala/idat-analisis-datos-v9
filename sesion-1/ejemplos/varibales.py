# 1. Texto simple -> string
negocio = "Café python!"

# 2. Texto con comillas simples -> string
slogan = 'El mejor café de la ciudad'

# 3. Número entero -> int
sillas_disponibles = 20

# 4. Número decimal -> float
precio_cafe = 2.50

# 5. Valor booleano -> bool (verdadero)
esta_abierto = True

# 6. Valor booleano -> bool (falso)
tiene_wifi = False

# 7. Texto largo
direccion = "Avenida angamos 635, Miraflores, Lima, Perú"

# 8. Número como texto -> string
codigo_postal = "15074"

# 9. Variable vacía
proxima_oferta = None

# 10. Variables con caracteres especiales
emoji_cafe = "☕"

# 11. Multiplicador de cadenas
print("*" * 100)

# 12. Concatenación de cadenas o variables
concatenar_v1 = negocio + " " + slogan
print(concatenar_v1)

# 13. Concatenación con f-strings
concatenar_v2 = f"{negocio} {slogan}"
print(concatenar_v2)

# 14. Concatenación de variables
print(f'Bienvenido al {concatenar_v2} {emoji_cafe}, me ubico en {direccion}')
