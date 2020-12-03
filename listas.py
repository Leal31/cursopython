#Listas
Lista = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes',2,3,1,3,4,2 ,231, 23.1, [1, 2 , 3], True]
#Imprimir elementos de la lista
print(Lista)
#Imprimimos un elemento de la lista
print(Lista[0])
#Imprimimos un elemento en reversa de la Lista
print(Lista[-3])
#Imprimimos elementos de la lista en un rango determinado
print(Lista[0:3])
#Imprimimos desde el fin al inicio
print(Lista[:4])
# Imprimimos desde cierto punto a cierto punto
print(Lista[2:4])
#Imprimimos de inicio a fin de la lista
print(Lista[2:])
#Cuantos elementos tiene la Lista
print(len(Lista))
#Añadir un elemento aparte a la lista
Lista2 = [1, 2, 4, 5]
Lista2.append("Alejandro")
print(Lista2)
#Añadir un elemento en un punto especificio
Lista2.insert(2, 3)
print(Lista2)
#Añadir mas de un elemento
Lista2.extend([6, 7, 8])
print(Lista2)
#Concatenar listas
Lista3 = Lista + Lista2
print(Lista3)
#Buscar una elemento de la lista
print(3 in Lista2)
#Imprimir donde esta un elemento
print(Lista2.index("Alejandro"))
#Ver si hay valores repetidos
print(Lista.count(2))
#Eliminar valores
Lista.pop(5)
print(Lista)
Lista.remove("Lunes")
print(Lista)
#Eliminar la lista
'''
Lista.clear()
print(Lista)
'''
#Voltear la lista
Lista.reverse()
print(Lista)
#De mayor a menor
Lista4 = [2,1,23,4,5151,241,4,24,2,9,-2]
Lista4.sort(reverse = True)
print(Lista4)
