pila_peliculas = [
    ("Rio 2", 2014),
    ("El planeta de los simios: confrontacion", 2014),
    ("Aviones 2: equipo de rescate", 2014),
    ("Batman vs superman: el origen de la justicia", 2016),
    ("Escuadron suicida", 2016),
    ("Deadpool", 2016),
    ("Re loca", 2018),
    ("Hotel Transylvania 3: mostruos de vacasiones", 2018),
    ("Mision imposible: recuperacion", 2018)
]

peliculas_2014 = []
peliculas_2016 = []
peliculas_2018 = []


def pelicula_año(pila, año, peliculas):
    pila_aux = []
    while len(pila) > 0:
        pelicula = pila.pop()
        if pelicula[1] == año:
            peliculas.append(pelicula[0])
        pila_aux.append(pelicula)
    while len(pila_aux) > 0:
        pila.append(pila_aux.pop())
    return peliculas


peliculas_2014 = pelicula_año(pila_peliculas, 2014, peliculas_2014)
peliculas_2016 = pelicula_año(pila_peliculas, 2016, peliculas_2016)
peliculas_2018 = pelicula_año(pila_peliculas, 2018, peliculas_2018)

print("Las peliculas estrenadas en el año 2014 son ", peliculas_2014)
print("Las peliculas estrenadas en el año 2016 son ", peliculas_2016)
print("Las peliculas estrenada en el año 2018 son ", peliculas_2018)
