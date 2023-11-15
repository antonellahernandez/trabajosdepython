# Crear el grafo representado como un diccionario de diccionarios
grafo = {
    "cocina": {"comedor": 5, "cochera": 8, "quincho": 6},
    "comedor": {"cocina": 5, "habitacion1": 7, "habitacion2": 4},
    "cochera": {"cocina": 8},
    "quincho": {"cocina": 6},
    "habitacion1": {"comedor": 7, "sala_estar": 3, "baño1": 3},
    "habitacion2": {"comedor": 4, "sala_estar": 5, "baño2": 4},
    "sala_estar": {"habitacion1": 3, "habitacion2": 5, "terraza": 2},
    "terraza": {"sala_estar": 2, "patio": 10},
    "patio": {"terraza": 10},
    "baño1": {"habitacion1": 3},
    "baño2": {"habitacion2": 4}
}

# Función para calcular el árbol de expansión mínima (MST)
def prim(grafo):
    arbol_expansion = {}
    vertices_no_incluidos = list(grafo.keys())
    primer_vertice = vertices_no_incluidos[0]
    vertices_no_incluidos.remove(primer_vertice)

    while vertices_no_incluidos:
        min_peso = float('inf')
        min_arista = None
        for vertice_incluido in arbol_expansion:
            for vecino, peso in grafo[vertice_incluido].items():
                if vecino in vertices_no_incluidos and peso < min_peso:
                    min_peso = peso
                    min_arista = (vertice_incluido, vecino)
        arista = min_arista
        arbol_expansion[arista[1]] = {arista[0]: min_peso}
        vertices_no_incluidos.remove(arista[1])

    return arbol_expansion

# Obtener el árbol de expansión mínima
arbol_expansion = prim(grafo)

# Mostrar el árbol de expansión mínima
print("Árbol de Expansión Mínima:")
for vertice, vecinos in arbol_expansion.items():
    for vecino, peso in vecinos.items():
        print(f"{vertice} -- {vecino}: {peso} metros")

# Calcular la longitud total del árbol de expansión mínima
metros_cables_total = sum([peso for vecinos in arbol_expansion.values() for peso in vecinos.values()])
print(f"Cantidad total de metros de cables para conectar todos los ambientes: {metros_cables_total} metros")

# Función para encontrar el camino más corto usando el algoritmo de Dijkstra
def dijkstra(grafo, inicio, fin):
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[inicio] = 0
    camino = {}

    while grafo:
        vertice_actual = min(grafo, key=lambda x: distancias[x])
        for vecino, peso in grafo[vertice_actual].items():
            if distancias[vertice_actual] + peso < distancias[vecino]:
                distancias[vecino] = distancias[vertice_actual] + peso
                camino[vecino] = vertice_actual
        grafo.pop(vertice_actual)

    # Reconstruir el camino
    camino_reconstruido = [fin]
    while fin != inicio:
        fin = camino[fin]
        camino_reconstruido.append(fin)
    return camino_reconstruido[::-1]

# Encontrar el camino más corto desde habitacion1 hasta sala_estar
camino_corto = dijkstra(grafo, "habitacion1", "sala_estar")

# Mostrar el camino más corto
print(f"Camino más corto desde habitacion1 hasta sala_estar: {camino_corto}")
metros_cable_red = sum([grafo[camino_corto[i]][camino_corto[i+1]] for i in range(len(camino_corto)-1)])
print(f"Cantidad de metros de cable de red necesarios: {metros_cable_red} metros")