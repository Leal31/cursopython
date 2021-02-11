def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        for subElemento in elemento:
            yield subElemento

ciudades_devueltas = devuelve_ciudades("Madrid", "Cali", "Bogota", "Valencia")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
