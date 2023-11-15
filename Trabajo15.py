# Crear un grafo representado como un diccionario de diccionarios
grafo = {
    "La Gran Muralla China": {"nombre": "La Gran Muralla China", "pais": "China", "tipo": "arquitectonica", "relaciones": {}},
    "Chichén Itzá": {"nombre": "Chichén Itzá", "pais": "México", "tipo": "arquitectonica", "relaciones": {}},
    "El Cristo Redentor": {"nombre": "El Cristo Redentor", "pais": "Brasil", "tipo": "arquitectonica", "relaciones": {}},
    "Machu Picchu": {"nombre": "Machu Picchu", "pais": "Perú", "tipo": "arquitectonica", "relaciones": {}},
    "Petra": {"nombre": "Petra", "pais": "Jordania", "tipo": "arquitectonica", "relaciones": {}},
    "Coliseo Romano": {"nombre": "Coliseo Romano", "pais": "Italia", "tipo": "arquitectonica", "relaciones": {}},
    "Taj Mahal": {"nombre": "Taj Mahal", "pais": "India", "tipo": "arquitectonica", "relaciones": {}},
    "Bahía de Ha-Long": {"nombre": "Bahía de Ha-Long", "pais": "Vietnam", "tipo": "natural", "relaciones": {}},
    "Cataratas del Iguazú": {"nombre": "Cataratas del Iguazú", "pais": ["Argentina", "Brasil"], "tipo": "natural", "relaciones": {}},
    "Montaña de la Mesa": {"nombre": "Montaña de la Mesa", "pais": "Sudáfrica", "tipo": "natural", "relaciones": {}},
    "Amazonia": {"nombre": "Amazonia", "pais": ["Brasil", "Perú", "Colombia", "Venezuela", "Ecuador", "Bolivia", "Guyana", "Surinam", "Guyana Francesa"], "tipo": "natural", "relaciones": {}},
    "Halong Bay": {"nombre": "Halong Bay", "pais": "Vietnam", "tipo": "natural", "relaciones": {}},
    "Parque Nacional de Komodo": {"nombre": "Parque Nacional de Komodo", "pais": "Indonesia", "tipo": "natural", "relaciones": {}}
}

# Establecer relaciones entre las maravillas
grafo["La Gran Muralla China"]["relaciones"] = {
    "Chichén Itzá": 5,
    "El Cristo Redentor": 8,
    "Machu Picchu": 6
}

grafo["Chichén Itzá"]["relaciones"] = {
    "La Gran Muralla China": 5,
    "El Cristo Redentor": 7,
    "Machu Picchu": 4
}

grafo["El Cristo Redentor"]["relaciones"] = {
    "La Gran Muralla China": 8,
    "Chichén Itzá": 7,
    "Machu Picchu": 5
}

grafo["Machu Picchu"]["relaciones"] = {
    "La Gran Muralla China": 6,
    "Chichén Itzá": 4,
    "El Cristo Redentor": 5
}

# ... (establecer relaciones para las demás maravillas)

# Imprimir el grafo
for maravilla, atributos in grafo.items():
    print(f"{atributos['nombre']} ({atributos['tipo']} - {atributos['pais']}): {atributos['relaciones']}")
    
# Establecer relaciones entre las maravillas
for maravilla1 in grafo.values():
    for maravilla2 in grafo.values():
        if maravilla1 != maravilla2 and maravilla1["tipo"] == maravilla2["tipo"]:
            distancia = 1  # Puedes asignar la distancia que prefieras
            maravilla1["relaciones"][maravilla2["nombre"]] = distancia

# Imprimir el grafo con relaciones
for maravilla, atributos in grafo.items():
    print(f"{atributos['nombre']} ({atributos['tipo']} - {atributos['pais']}): {atributos['relaciones']}")

# Calcular el árbol de expansión mínima para cada tipo de maravilla
from itertools import combinations

def obtener_mst_por_tipo(tipo):
    subgrafo = {nodo: atributos for nodo, atributos in grafo.items() if atributos["tipo"] == tipo}
    nodos = list(subgrafo.keys())
    mst = {nodo: {} for nodo in nodos}

    for nodo1, nodo2 in combinations(nodos, 2):
        distancia = subgrafo[nodo1]["relaciones"][nodo2]
        mst[nodo1][nodo2] = mst[nodo2][nodo1] = distancia

    return mst

# Calcular y mostrar el árbol de expansión mínima para maravillas arquitectónicas y naturales
mst_arquitectonicas = obtener_mst_por_tipo("arquitectonica")
mst_naturales = obtener_mst_por_tipo("natural")

print("\nÁrbol de expansión mínima de maravillas arquitectónicas:")
for nodo, vecinos in mst_arquitectonicas.items():
    for vecino, distancia in vecinos.items():
        print(f"{nodo} -- {vecino}: {distancia} unidades de distancia")

print("\nÁrbol de expansión mínima de maravillas naturales:")
for nodo, vecinos in mst_naturales.items():
    for vecino, distancia in vecinos.items():
        print(f"{nodo} -- {vecino}: {distancia} unidades de distancia")

# Obtener la lista de países con maravillas arquitectónicas y naturales
paises_arquitectonicas = set()
paises_naturales = set()

for atributos in grafo.values():
    nombre = atributos["nombre"]
    pais = atributos["pais"]
    tipo = atributos["tipo"]

    if tipo == "arquitectonica":
        paises_arquitectonicas.add(pais)
    elif tipo == "natural":
        paises_naturales.add(pais)

# Comprobar si existen países con maravillas arquitectónicas y naturales
paises_con_arquitectonicas_y_naturales = paises_arquitectonicas.intersection(paises_naturales)

print("\nPaíses con maravillas arquitectónicas y naturales:")
print(paises_con_arquitectonicas_y_naturales)

# Determinar si algún país tiene más de una maravilla del mismo tipo
paises_con_mas_de_una_maravilla_del_mismo_tipo = set()

for pais in set(paises_arquitectonicas).union(set(paises_naturales)):
    maravillas_pais = [atributos["tipo"] for atributos in grafo.values() if atributos["pais"] == pais]
    
    if len(set(maravillas_pais)) < len(maravillas_pais):
        paises_con_mas_de_una_maravilla_del_mismo_tipo.add(pais)

print("\nPaíses con más de una maravilla del mismo tipo:")
print(paises_con_mas_de_una_maravilla_del_mismo_tipo)