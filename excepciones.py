def sumar(numero1, numero2):
    return numero1 + numero2

def restar(numero1, numero2):
    return numero1 - numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2

def dividir(numero1, numero2):
    try:
        return numero1 / numero2
    except ZeroDivisionError:
        print("no se puede dividir entre 0")
        return "operacion erronea"
while True:
    
    try:
        num1 = int(input("introduce un numero por favor: "))

        num2 = int(input("introduce un segundo numero: "))
        break
    except ValueError:
        print("no seas pendejo eso no es un numero, hacele de nuevo, mamon...")

operador = input("Que quieres hacer con esos numeros(+,-,*,/): ")

if operador == '+':
    print(sumar(num1, num2))
elif operador == '-':
    print(restar(num1, num2))
elif operador == '*':
    print(multiplicar(num1, num2))
elif operador == '/':
    print(dividir(num1, num2))
else:
    print("no es un operador valido")
print("sigamos el programa")
