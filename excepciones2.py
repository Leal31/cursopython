def divide():
    try:

        op1 = (float(input("introduce un numero: ")))

        op2 = (float(input("introduce otro numero: ")))

        print("la division es: " + str(op1/op2))

    except ValueError:
        print("el valor introducido es erroneo")
    except ZeroDivisionError:
        print("no puedes dividir por 0 pendejo")
    
    finally:
        
        print("calculo realizado")
divide()
