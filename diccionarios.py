#Diccionarios
diccionario = {"azul": "blue", "rojo": "red", "verde": "green"}
print(diccionario)
#solo un elemento del diccionario
print(diccionario["azul"])
#añadir un elemento a un diccionario
diccionario["amarillo"] = "yellow"
print(diccionario)
#borrar un elemento del diccionario
del(diccionario["verde"])
print(diccionario)
#combinar un elemento
diccionario = {"Emanuel":{"edad":22,"estatura": 1.72}, "Jose":[21, 1.75], "Maria":[22,1.66]}
print(diccionario)
print(diccionario["Emanuel"])
#diccionario parte 2
equipo = {10: "Paulo Dybala", 11: "Douglas Costa", 7:"Cristiano Ronaldo", 17: "Mario Mandzukic"}
print(equipo)
#Solo un valor
print(equipo[10])
print(equipo.get(14, "No existe un jugador con ese dorsal"))
#saber si hay el valor en el diccionario
print(10 in equipo)
#Saber todas las claves del diccionario
print(equipo.keys())
#Saber los valores del diccionario
print(equipo.values())
#como saber valores del diccionario
print(equipo.items())
#Cuantos elementos hay en el diccionario
print(len(equipo))
#borrar todos los elementos del diccionario
'''
equipo.clear()
print(equipo)
'''
