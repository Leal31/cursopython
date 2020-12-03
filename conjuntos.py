#le decimos al sistema que sera un conjunto
conjuntos = set()
#Añadimos valores al conjuntos
conjunto = {1, 2, 3, "Que tal", 4.56, 3, 5.23}
#añadir elemento aparte
conjunto.add(5)
#quitar elementos
conjunto.discard(3)
#vaciar elementos
#conjunto.clear()
#buscar elementos
print(3 in conjunto)
#ver si no esta en el conjunto
print(3 not in conjunto)

print(conjunto)
#ver si son iguales los conjuntos
a = {1, 2, 3}
b = {3, 4, 5}

print(a == b)
#unir elementos
c = a | b
print(c)
#intersectas elementos
c = a & b

print(c)
#diferenciar elementos
c = a - b
print(c)

#diferencia simetrica
c = a ^ b
print(c)
#sub conjunto
c = {1, 2, 3, 4, 5}
print(a.issubset(c))
#superconjunto
print(c.issuperset(a))
#disconexos
print(a.isdisjoint(conjunto))
#conjuntos inmutables
d = frozenset({1, 2, 7})
