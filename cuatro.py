nombre = input("Ingresa tu nombre completo: ")

while not nombre.replace(' ', '').isalpha():
    nombre = input("Ingresa un nombre válido (solo letras y espacios): ")

edad = input("Ingresa tu edad: ")
telefono = input("Ingresa tu número de teléfono: ")
correo = input("Ingresa tu correo electrónico: ")

print("\nResumen de la información ingresada:")
print("Nombre: ", nombre)
print("Edad: ", edad)
print("Teléfono: ", telefono)
print("Correo electrónico: ", correo)