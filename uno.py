print("Bienvenido, ahora probaras esta actividad !")
numero = input("Ingresa un número del 1 al 1000: ")
numero = int(numero)

if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")