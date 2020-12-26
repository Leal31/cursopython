#Bucle while
import math

numero = int(input("Digite un numero por favor: "))

while numero < 0:
    print("Error: Numero negativo detectado")
    numero = int(input("Digite un numero por favor: "))
print(f"\nSu raiz cuadrada es: {(math.sqrt(numero)):.2f}")


