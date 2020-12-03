edad = int(input("Digite su edad: "))
if 0 < edad < 105:
    print("Edad valida")
    if edad >= 18:
         print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
else:
    print("Edad incorrecta")
