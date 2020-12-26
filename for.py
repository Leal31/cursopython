#Bucle For
for i in [1, 2, 3, 4, 5, "Emanuel", "Holi"]:
    print(i)

coleccion = {1,2,3,4,5,6,7,8,9,10}

for i in coleccion:
    print(f"Elemento: {i}")

coleccion = {"Emanuel":16, "Mario":21, "Jose":23}
for clave, valor in coleccion.items():
    print(f"{clave} -> {valor}")

coleccion = "Emanuel"

for i in coleccion:
    print(f"{i}", end =" ")

for i in range(5):
    print(i)


for i in range(5, 20,2):
    print(i)
