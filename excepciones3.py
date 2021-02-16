def edad(edad):
    if edad < 0:
        raise TypeError("La edad no es negativa jamas warro")
    if edad < 20:
        return "eres muy joven"
    elif edad < 40:
        return "Eres joven"
    elif edad < 65:
        return "Eres maduro"
    elif edad < 100:
        return "cuidate"

print(edad(15))

import math

def calculaRaiz(num1):
    if num1 < 0:
        raise ValueError ("EL NUMERO NO ES NEGATIVO WARRO")
    else:
        return math.sqrt(num1)

intr1 = float(input("dime un numero por favor: "))
try:
    print(calculaRaiz(intr1))
except ValueError as NumeroNegativoError:
    print(NumeroNegativoError)

print("programa terminado")
