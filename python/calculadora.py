numero1 = int(input("Introduce numero 1: "))
numero2 = int(input("Introduce numero 2: "))

operaciones_posibles = ["+","-","*","/"]

operacion = input("Introduce una operación [+ - * /]: ")

while operacion not in operaciones_posibles:
    operacion = input("Introduce una operación [+ - * /]: ")


try: 
    resultado = eval(f"{numero1} {operacion} {numero2}")
except ZeroDivisionError:
    resultado = "Error"
    print("Error: NO SE PUEDE DIVIDOR ENTRE 0")


print(f"{numero1} {operacion} {numero2} = {resultado}")







































































