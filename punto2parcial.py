grafo = {
    "Luke Skywalker": {"Leia Organa": 5, "Han Solo": 3},
    "Leia Organa": {"Luke Skywalker": 5, "Han Solo": 5},
    "Han Solo": {"Luke Skywalker": 3, "Leia Organa": 5},
    # Agregar más relaciones aquí...
}
def kruskal_mst(grafo):
    aristas = []

    # Crear una lista de aristas
    for personaje1, relaciones in grafo.items():
        for personaje2, episodios in relaciones.items():
            aristas.append((personaje1, personaje2, episodios))

    # Ordenar las aristas por la cantidad de episodios
    aristas.sort(key=lambda x: x[2])

    # Inicializar estructuras para el MST
    mst = {}
    conjuntos_disjuntos = {personaje: personaje for personaje in grafo}

    for arista in aristas:
        personaje1, personaje2, episodios = arista

        if conjuntos_disjuntos[personaje1] != conjuntos_disjuntos[personaje2]:
            mst[(personaje1, personaje2)] = episodios
            conjunto1 = conjuntos_disjuntos[personaje1]
            conjunto2 = conjuntos_disjuntos[personaje2]

            # Fusionar los conjuntos disjuntos
            for personaje, conjunto in conjuntos_disjuntos.items():
                if conjunto == conjunto1:
                    conjuntos_disjuntos[personaje] = conjunto2

    return mst

mst = kruskal_mst(grafo)
print("Árbol de Expansión Mínimo:")
print(mst)

max_episodios = 0
personajes_max = []

for personaje1, relaciones in grafo.items():
    for personaje2, episodios in relaciones.items():
        if episodios > max_episodios:
            max_episodios = episodios
            personajes_max = [personaje1, personaje2]
        elif episodios == max_episodios:
            personajes_max.append(personaje1)
            personajes_max.append(personaje2)

print("Número máximo de episodios compartidos:", max_episodios)
print("Personajes correspondientes:", personajes_max)

grafo = [
    ("Personaje1", "Personaje2", 3),
    ("Personaje2", "Personaje3", 2),
    ("Personaje4", "Personaje2", 4),
    # Agrega más aristas aquí...
]

# Función para encontrar el MST utilizando el algoritmo de Kruskal
def kruskal_mst(grafo):
    # Implementa el algoritmo de Kruskal aquí para encontrar el MST
    # Devuelve el MST como una lista de aristas
    pass

# Llama a la función para encontrar el MST
mst = kruskal_mst(grafo)

# Definición del grafo como una lista de aristas
grafo = [
    ("Personaje1", "Personaje2", 3),
    ("Personaje2", "Personaje3", 2),
    ("Personaje4", "Personaje2", 4),
    # Agrega más aristas aquí...
]

# Función para encontrar el MST utilizando el algoritmo de Kruskal
def kruskal_mst(grafo):
    grafo_ordenado = sorted(grafo, key=lambda x: x[2])  # Ordena las aristas por peso
    mst = []
    conjuntos_disjuntos = {}

    def encontrar_conjunto(personaje):
        if personaje not in conjuntos_disjuntos:
            return personaje
        return encontrar_conjunto(conjuntos_disjuntos[personaje])

    for arista in grafo_ordenado:
        personaje1, personaje2, peso = arista
        conjunto1 = encontrar_conjunto(personaje1)
        conjunto2 = encontrar_conjunto(personaje2)

        if conjunto1 != conjunto2:
            mst.append(arista)
            conjuntos_disjuntos[conjunto1] = conjunto2

    return mst

# Llama a la función para encontrar el MST
mst = kruskal_mst(grafo)

# Verifica si Yoda está presente en el MST
yoda_presente = any("Yoda" in arista for arista in mst)

if yoda_presente:
    print("El MST contiene a Yoda.")
else:
    print("El MST no contiene a Yoda.")

grafo = [
    ("Luke Skywalker", "Leia Organa", 5),
    ("Han Solo", "Chewbacca", 3),
    ("Obi-Wan Kenobi", "Yoda", 4),
    ("Darth Vader", "Emperor Palpatine", 6),
    # Agrega más aristas aquí...
]

# Inicializar variables para el número máximo de episodios compartidos y los nombres de los personajes
max_episodios_compartidos = 0
personaje1_max = None
personaje2_max = None

# Iterar a través de las aristas para encontrar el máximo
for arista in grafo:
    personaje1, personaje2, episodios = arista
    if episodios > max_episodios_compartidos:
        max_episodios_compartidos = episodios
        personaje1_max = personaje1
        personaje2_max = personaje2

if personaje1_max and personaje2_max:
    print(f"El número máximo de episodios compartidos es {max_episodios_compartidos}, entre {personaje1_max} y {personaje2_max}.")
else:
    print("No se encontraron personajes que compartan episodios en el grafo.")

grafo = {
    "Luke Skywalker": {
        "Leia Organa": 5,
        "Han Solo": 3,
        "Obi-Wan Kenobi": 2,
        # Agregar más relaciones aquí...
    },
    "Darth Vader": {
        "Emperor Palpatine": 6,
        "Boba Fett": 4,
        "Obi-Wan Kenobi": 3,
        # Agregar más relaciones aquí...
    },
    "Yoda": {
        "Obi-Wan Kenobi": 4,
        "Luke Skywalker": 3,
        # Agregar más relaciones aquí...
    },
    "Boba Fett": {
        "Darth Vader": 4,
        "Han Solo": 2,
        # Agregar más relaciones aquí...
    },
    "C-3PO": {
        "Leia Organa": 3,
        "R2-D2": 5,
        # Agregar más relaciones aquí...
    },
    "Leia Organa": {
        "Luke Skywalker": 5,
        "Han Solo": 5,
        # Agregar más relaciones aquí...
    },
    "Rey": {
        "Finn": 3,
        # Agregar más relaciones aquí...
    },
    "Kylo Ren": {
        "General Hux": 4,
        # Agregar más relaciones aquí...
    },
    "Chewbacca": {
        "Han Solo": 3,
        "Rey": 4,
        # Agregar más relaciones aquí...
    },
    "Han Solo": {
        "Leia Organa": 5,
        "Chewbacca": 3,
        "Luke Skywalker": 3,
        "Boba Fett": 2,
        # Agregar más relaciones aquí...
    },
    "R2-D2": {
        "C-3PO": 5,
        "Luke Skywalker": 4,
        # Agregar más relaciones aquí...
    },
    "BB-8": {
        "Poe Dameron": 4,
        # Agregar más relaciones aquí...
    }
}

# Imprimir el grafo para verificar las relaciones cargadas
for personaje, relaciones in grafo.items():
    print(f"{personaje}: {relaciones}")