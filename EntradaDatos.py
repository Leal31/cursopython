#Entrada de datos

nombre = input("Digite su nombre: ")

print(f"Hola {nombre}")

numero = int(input("Digia tu edad"))

if numero<18:
    print(f"{nombre}, te faltan {18-numero} años para ser mayor de edad")
else:
    print("Eres mayor de edad")
