#Escribir la siguiente expresion en forma de expresion algoritmica
a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))

expresion = (a ** 3 * (b ** 2 - 2 * a * c)) / (2 * b)
print(f"El resultado es: {expresion}")
#Escribir la otra expresion
a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = ((3 + 5 * 8) < 3 and (-6 / 3 * 4) + 2 < 2) or (a > b)
print(f"El resultado logico es: {c}")
a = input("Digite a: ")
b = input("Digite b: ")

a , b = b, a

print(f"Ahora a es {a} y b es {b}")
#Hallar el area y la longitud de una circunferencia
import math
radio = float(input("Digite el radio de una circunferencia(cm): "))
area = math.pi * radio ** 2
longitud = 2 * math.pi * radio
print(f"El area del circulo es {area:.4f}cm, y la longitud de la circunferencia es {longitud:.4f}cm")

factura = float(input("Digite el valor de su compra: "))

precio = factura * 0.15
precio_total = factura - precio
print(f"el precio total por su compra es {precio_total:.2f}")
