import random

MINIMO = 1

dificultad = input("Elige la dificultad (F,M,D): ")

if dificultad == "F":
    maximo = 10
elif dificultad == "M":
    maximo = 50
elif dificultad == "D":
    maximo = 100
elif dificultad not in "DMF":
    print("Error: No se encontro la dificultad")
    maximo = 10



numero_azar = random.randint(MINIMO, maximo)
intentos = 0

while True:
    intento_usuario = int(input(f"Introduce un número [{MINIMO}]-{maximo}]: "))
    intentos += 1
    if intento_usuario > numero_azar:
        print("Te has pasado! El número es más pequeño que " + str 
        (intento_usuario))
    elif intento_usuario < numero_azar:
        print("Te has quedado corto! El número es más grande que " + str
        (intento_usuario))
    else:   
        break

print("Has acertado! El número era " + str(numero_azar))
print(f"Has tardado {intentos} número de intentos.")




























