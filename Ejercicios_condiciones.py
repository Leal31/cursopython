#Dos numeros y los compara para ver cual es par o cual es impar
numero1 = int(input("Digita un numero: "))
numero2 = int(input("Digita otro numero: "))

if numero1 % 2 == 0 and numero2 % 2 == 0:
    print("Ambos son pares")
elif numero1 % 2 == 0 and numero2 % 2 != 0:
    print(f"{numero1} es par")
elif numero1 % 2 != 0 and numero2 % 2 == 0:
    print(f"{numero2} es par")
else:
    print("ninguno es par")
numero1 = int(input("Digite un numero: "))
numero2 = int(input("Digite un numero: "))
numero3 = int(input("Digite un numero: "))

if numero1 > numero2 and  numero1 > numero3:
    print(f"{numero1} es el numero mayor ")
elif numero2 > numero1 and numero2 > numero3:
    print(f"{numero2} es el numero mayor")
elif numero3 > numero1 and numero3 > numero2:
    print(f"{numero3} es el numero mayor")
elif numero1 == numero2 and numero1 == numero3 and numero2 == numero3:
    print("Todos los numeros son iguales")
caracter = input("Digite un caracter por favor: ").lower()
if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
    print(f"{caracter} es una vocal")
else:
    print(f"{caracter} no es una vocal")
numero1 = float(input("Digite un numero: "))
numero2 = float(input("Digite un numero: "))
opcion = input("Digite que quisiera hacer (Sumar(+), Restar(-), Multiplicar(*), Dividir(/))")

if opcion=='+':
    operacion = numero1 + numero2
    print(f"La suma de {numero1} y {numero2} es: {operacion:.2f}")
elif opcion == '-':
    operacion = numero1 - numero2
    print(f"La resta de {numero1} y {numero2} es: {operacion:.2f}")
elif opcion == '*':
    operacion = numero1 * numero2
    print(f"La multiplicacion de {numero1} y {numero2} es: {operacion:.2f}")
elif opcion == '/':
    operacion = numero1 / numero2
    print(f"La division de {numero1} y {numero2} es: {operacion:.2f}")
else:
    print("Eso no es un caracter valido")
saldo_inicial = 1000

usuario = input("Que quisiera hacer en su cuenta:\n (I = ingresar dinero)\n (R = Retirar dinero)\n (M = Mostrar dinero en su cuenta)\n (S = Salir)").upper()

if usuario == 'I':
    ingresar = float(input("Cuanto dinero desea ingresar?: "))
    saldo_inicial += ingresar
    print(f"El saldo de su cuenta ahora es: {saldo_inicial}")
    print("Muchisimas gracias, vuelva pronto")
elif usuario == 'R':
    retirar = float(input("Cuanto dinero desea retirar?: "))
    if retirar > saldo_inicial:
        print("No puede retirar tanto dinero")
    else:
        saldo_inicial -= retirar
        print(f"Su saldo restante es: {saldo_inicial}")
    print("Muchisimas gracias, vuelva pronto")
elif usuario == 'M':
    print(f"El saldo que hay en su cuenta es: {saldo_inicial}")
    print("Muchisimas gracias, vuelva pronto")
elif usuario == 'S':
    print("Muchisimas gracias, vuelva pronto")
else:
    print("Esto no es una opcion valida, por favor ingrese de nuevo para ingresar una opcion valida")
