#Ejercicio numero 1
lista = [1,2,3,"Emanuel",2,2,1,"Emanuel",3]

lista = list(set(lista))

print(lista)

#Ejercicio numero 2

lista1 = [1, 2, 3, 4, "Emanuel", "cebolla", "lechuga", 1,2,3,4,5,5,5,5,5,6,2,1]

lista2 = ["Aguacate", "Pimenton", "Pasta", 123546,2,3,4,5,1,2]

#Eliminar elementos repetidos

a = set(lista1)
b = set(lista2)

union = list(a | b)
soloA = list(a - b)
soloB = list(b - a)
interseccion = list(a & b)

print(f"Lista de elementos que aparecen en las dos listas: {union}")
print(f"Lista de elementos que aparecen en la primera lista pero no en la segunda: {soloA}")
print(f"Lista de elementos que aparecen en la segunda lista pero no en la primera: {soloB}")
print(f"Lista de elementos que aparecen en ambas listas: {interseccion}")

#Ejercicio numero 3
personajes = []
Aragon = {"Nombre" : "Aragon","Clase" : "Guerrero", "Raza" : "Dunadan del Norte"}
Gandalf = {"Nombre" : "Gandalf", "Clase" : "Mago", "Raza" : "Istar"}
Legolas = {"Nombre" : "Legolas", "Clase" : "Arquero", "Raza" : "Elfo Sindar"}
personajes.append(Aragon)
personajes.append(Gandalf)
personajes.append(Legolas)
print(personajes)
