'''
Un generador es una funcion que mediante un bucle,
puede tomar ciertos valores de una funcion
preestablecida
'''
def generaPares(limite):

    numero = 1


    while numero < limite:
       yield numero * 2 
       numero += 1

devuelvePares = generaPares(10)

#for i in devuelvePares:
#    print(i)

#imprimir solo un par de valores
print(next(devuelvePares))

print('aqui podria ir mas codigo')
print(next(devuelvePares))
print('mas codigo')
print(next(devuelvePares))

