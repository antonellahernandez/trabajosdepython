# Define una clase para representar un nodo del árbol.
from collections import defaultdict


class CreatureNode:
    def __init__(self, criatura, derrotada_por):
        self.criatura = criatura
        self.derrotada_por = derrotada_por
        self.left = None
        self.right = None

# Función para insertar un nodo en el árbol.


def insert(root, criatura, derrotada_por):
    if root is None:
        return CreatureNode(criatura, derrotada_por)
    if criatura < root.criatura:
        root.left = insert(root.left, criatura, derrotada_por)
    else:
        root.right = insert(root.right, criatura, derrotada_por)
    return root

# Función para realizar un recorrido inorden del árbol y mostrar los datos.


def inorden_traversal(root):
    if root:
        inorden_traversal(root.left)
        print(
            f"Criatura: {root.criatura} | Derrotada por: {root.derrotada_por}")
        inorden_traversal(root.right)


# Crear un árbol con los datos de la tabla.
data = [
    ("Talos", "Hércules"),
    ("Minotauro", "Teseo"),
    ("Cerbero", "Hércules"),
    ("Medusa", "Perseo"),
    ("Hidra de Lerna", "Hércules")
]

root = None
for criatura, derrotada_por in data:
    root = insert(root, criatura, derrotada_por)

# Realizar la consulta solicitada:
print("Listado inorden de las criaturas y quienes las derrotaron:")
inorden_traversal(root)

# Define una clase para representar un nodo del árbol.


class CreatureNode:
    def __init__(self, criatura, derrotada_por, descripcion):
        self.criatura = criatura
        self.derrotada_por = derrotada_por
        self.descripcion = descripcion
        self.left = None
        self.right = None

# Función para insertar un nodo en el árbol.


def insert(root, criatura, derrotada_por, descripcion):
    if root is None:
        return CreatureNode(criatura, derrotada_por, descripcion)
    if criatura < root.criatura:
        root.left = insert(root.left, criatura, derrotada_por, descripcion)
    else:
        root.right = insert(root.right, criatura, derrotada_por, descripcion)
    return root

# Función para realizar un recorrido inorden del árbol y mostrar los datos.


def inorden_traversal(root):
    if root:
        inorden_traversal(root.left)
        print(
            f"Criatura: {root.criatura} | Derrotada por: {root.derrotada_por} | Descripción: {root.descripcion}")
        inorden_traversal(root.right)


# Crear un árbol con los datos de la tabla.
data = [
    ("Talos", "Hércules", "Un gigante de bronce que protegía la isla de Creta."),
    ("Minotauro", "Teseo",
     "Una criatura mitad hombre y mitad toro que habitaba el laberinto de Creta."),
    ("Cerbero", "Hércules", "El perro de tres cabezas que guardaba la entrada al Hades."),
    ("Medusa", "Perseo",
     "Una gorgona cuyo contacto visual convertía a las personas en piedra."),
    ("Hidra de Lerna", "Hércules",
     "Una serpiente acuática con múltiples cabezas que regeneraban cuando se cortaban.")
]

root = None
for criatura, derrotada_por, descripcion in data:
    root = insert(root, criatura, derrotada_por, descripcion)

# Realizar la consulta solicitada:
print("Listado inorden de las criaturas y quienes las derrotaron:")
inorden_traversal(root)

# Función para buscar y mostrar la información de una criatura en el árbol.


def buscar_criatura(root, nombre_criatura):
    if root is None:
        print(f"Criatura {nombre_criatura} no encontrada.")
        return
    if nombre_criatura == root.criatura:
        print(f"Información de la criatura {nombre_criatura}:")
        print(f"Criatura: {root.criatura}")
        print(f"Derrotada por: {root.derrotada_por}")
        print(f"Descripción: {root.descripcion}")
    elif nombre_criatura < root.criatura:
        buscar_criatura(root.left, nombre_criatura)
    else:
        buscar_criatura(root.right, nombre_criatura)


# Llamamos a la función para buscar la información de la criatura "Talos".
nombre_criatura_a_buscar = "Talos"
buscar_criatura(root, nombre_criatura_a_buscar)


# Diccionario para mantener un recuento de cuántas criaturas ha derrotado cada héroe o dios.
heroes_derrotas = defaultdict(int)

# Función para contar las derrotas de las criaturas.


def contar_derrotas(root):
    if root is not None:
        # Actualiza el recuento para el héroe o dios actual.
        heroes_derrotas[root.derrotada_por] += 1
        # Recorre los hijos del árbol.
        contar_derrotas(root.left)
        contar_derrotas(root.right)


# Llamamos a la función para contar las derrotas.
contar_derrotas(root)

# Encuentra los tres héroes o dioses con más derrotas.
heroes_top_3 = sorted(heroes_derrotas.items(),
                      key=lambda x: x[1], reverse=True)[:3]

# Imprime los tres héroes o dioses con más derrotas.
print("Los 3 héroes o dioses con más derrotas son:")
for heroe, derrotas in heroes_top_3:
    print(f"{heroe}: {derrotas} criaturas derrotadas.")

# Clase para representar cada criatura.


class Criatura:
    def __init__(self, nombre, derrotada_por):
        self.nombre = nombre
        self.derrotada_por = derrotada_por

# Clase para representar un nodo en el árbol binario.


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Clase para representar cada nodo del árbol


class TreeNode:
    def __init__(self, nombre, derrotada_por):
        self.nombre = nombre
        self.derrotada_por = derrotada_por
        self.left = None
        self.right = None


# Clase para representar un nodo del árbol.
class Nodo:
    def __init__(self, nombre, derrotada_por):
        self.nombre = nombre
        self.derrotada_por = derrotada_por
        self.left = None
        self.right = None

# Función para realizar un recorrido inorden y listar las criaturas derrotadas por Heracles.


def listar_criaturas_derrotadas_por_heracles(root, heracles):
    if root is not None:
        # Recorre el subárbol izquierdo.
        listar_criaturas_derrotadas_por_heracles(root.left, heracles)

        # Si la criatura fue derrotada por Heracles, imprímela.
        if root.derrotada_por == heracles:
            print(f"{root.nombre} fue derrotada por Heracles.")

        # Recorre el subárbol derecho.
        listar_criaturas_derrotadas_por_heracles(root.right, heracles)

# Función para mostrar toda la información de la criatura Talos.


def mostrar_informacion_de_criatura(root, criatura):
    if root is not None:
        if root.nombre == criatura:
            print(f"Nombre: {root.nombre}")
            print(f"Derrotada por: {root.derrotada_por}")
        mostrar_informacion_de_criatura(root.left, criatura)
        mostrar_informacion_de_criatura(root.right, criatura)


# Crear el árbol con los datos de la tabla.
root = Nodo("Heracles", "None")
root.left = Nodo("Nemean Lion", "Heracles")
root.right = Nodo("Hydra", "Heracles")
root.left.left = Nodo("Erymanthian Boar", "Heracles")
root.left.right = Nodo("Ceryneian Hind", "Heracles")
root.right.left = Nodo("Ceryneian Hind", "Heracles")
root.right.right = Nodo("Ceryneian Hind", "Heracles")

# Listar las criaturas derrotadas por Heracles.
print("Criaturas derrotadas por Heracles:")
listar_criaturas_derrotadas_por_heracles(root, "Heracles")

# Mostrar toda la información de la criatura Talos.
print("\nInformación de la criatura Talos:")
mostrar_informacion_de_criatura(root, "Talos")

# Clase para representar un nodo del árbol.


class Nodo:
    def __init__(self, nombre, derrotada_por):
        self.nombre = nombre
        self.derrotada_por = derrotada_por
        self.left = None
        self.right = None

# Clase para representar un nodo del árbol.


class Nodo:
    def __init__(self, nombre, derrotada_por):
        self.nombre = nombre
        self.derrotada_por = derrotada_por
        self.left = None
        self.right = None

# Clase para representar un nodo del árbol.


class Nodo:
    def __init__(self, nombre, derrotada_por):
        self.nombre = nombre
        self.derrotada_por = derrotada_por
        self.left = None
        self.right = None

# Función para listar las criaturas que no han sido derrotadas.


def listar_criaturas_no_derrotadas(root):
    if root is not None:
        # Recorre el subárbol izquierdo.
        listar_criaturas_no_derrotadas(root.left)

        # Si la criatura no ha sido derrotada, imprímela.
        if root.derrotada_por == "None":
            print(f"{root.nombre} no ha sido derrotada.")

        # Recorre el subárbol derecho.
        listar_criaturas_no_derrotadas(root.right)


# Crear el árbol con los datos de la tabla.
root = Nodo("Heracles", "None")
root.left = Nodo("Nemean Lion", "Heracles")
root.right = Nodo("Hydra", "Heracles")
root.left.left = Nodo("Erymanthian Boar", "Heracles")
root.left.right = Nodo("Ceryneian Hind", "Heracles")
root.right.left = Nodo("Ceryneian Hind", "Heracles")
root.right.right = Nodo("Ceryneian Hind", "Heracles")
root.left.left.left = Nodo("Unicorn", "None")
root.left.left.right = Nodo("Minotaur", "None")

# Listar las criaturas que no han sido derrotadas.
print("Criaturas que no han sido derrotadas:")
listar_criaturas_no_derrotadas(root)

# Clase para representar un nodo del árbol.


class Nodo:
    def __init__(self, nombre, derrotada_por, capturada):
        self.nombre = nombre
        self.derrotada_por = derrotada_por
        self.capturada = capturada  # Nuevo campo "capturada"
        self.left = None
        self.right = None

# Clase para representar un nodo del árbol.


class Nodo:
    def __init__(self, nombre, derrotada_por, capturada):
        self.nombre = nombre
        self.derrotada_por = derrotada_por
        self.capturada = capturada  # Nuevo campo
        self.left = None
        self.right = None

# Función para listar las criaturas que no han sido derrotadas.


def listar_criaturas_no_derrotadas(root):
    if root is not None:
        # Recorre el subárbol izquierdo.
        listar_criaturas_no_derrotadas(root.left)

        # Si la criatura no ha sido derrotada (derrotada_por es "None"), imprímela.
        if root.derrotada_por == "None":
            print(
                f"{root.nombre} no ha sido derrotada y fue capturada por {root.capturada}.")

        # Recorre el subárbol derecho.
        listar_criaturas_no_derrotadas(root.right)


# Crear el árbol con los datos de la tabla, incluyendo la información de captura.
root = Nodo("Heracles", "None", "None")
root.left = Nodo("Nemean Lion", "Heracles", "None")
root.right = Nodo("Hydra", "Heracles", "None")
root.left.left = Nodo("Erymanthian Boar", "Heracles", "None")
root.left.right = Nodo("Ceryneian Hind", "Heracles", "None")
root.right.left = Nodo("Ceryneian Hind", "Heracles", "None")
root.right.right = Nodo("Ceryneian Hind", "Heracles", "None")
root.left.left.left = Nodo("Unicorn", "None", "None")
root.left.left.right = Nodo("Minotaur", "None", "None")

# Listar las criaturas que no han sido derrotadas y mostrar quién las capturó.
print("Criaturas que no han sido derrotadas:")
listar_criaturas_no_derrotadas(root)

# Función para modificar los nodos de las criaturas atrapadas por Heracles.


def modificar_criaturas_atrapadas(root, criaturas):
    if root is not None:
        # Recorre el subárbol izquierdo.
        modificar_criaturas_atrapadas(root.left, criaturas)

        # Si la criatura está en la lista de criaturas, modifica el nodo.
        if root.nombre in criaturas:
            root.derrotada_por = "Heracles"
            root.capturada = "Heracles"

        # Recorre el subárbol derecho.
        modificar_criaturas_atrapadas(root.right, criaturas)


# Crear el árbol con los datos de la tabla.
root = Nodo("Heracles", "None", "None")
root.left = Nodo("Nemean Lion", "Heracles", "Zeus")
root.right = Nodo("Hydra", "Heracles", "Athena")
root.left.left = Nodo("Erymanthian Boar", "Heracles", "None")
root.left.right = Nodo("Ceryneian Hind", "Heracles", "None")
root.right.left = Nodo("Ceryneian Hind", "Heracles", "None")
root.right.right = Nodo("Ceryneian Hind", "Heracles", "None")
root.left.left.left = Nodo("Unicorn", "None", "None")
root.left.left.right = Nodo("Minotaur", "None", "None")

# Lista de criaturas atrapadas por Heracles.
criaturas_atrapadas_por_heracles = [
    "Cerbero", "Toro de Creta", "Cierva Cerinea", "Jabalí de Erimanto"]

# Modificar los nodos de las criaturas atrapadas por Heracles.
modificar_criaturas_atrapadas(root, criaturas_atrapadas_por_heracles)

# Función para listar todas las criaturas y su información.


def listar_criaturas_y_su_informacion(root):
    if root is not None:
        # Recorre el subárbol izquierdo.
        listar_criaturas_y_su_informacion(root.left)

        # Imprime la información de la criatura.
        print(
            f"Criatura: {root.nombre}, Derrotada por: {root.derrotada_por}, Capturada por: {root.capturada}")

        # Recorre el subárbol derecho.
        listar_criaturas_y_su_informacion(root.right)


# Listar todas las criaturas y su información.
print("Listado inorden de las criaturas y quienes las derrotaron:")
listar_criaturas_y_su_informacion(root)

# Función para buscar criaturas por coincidencia en el nombre.


def buscar_criaturas_por_coincidencia(root, texto_buscado, resultado):
    if root is not None:
        # Realiza una búsqueda recursiva en el subárbol izquierdo.
        buscar_criaturas_por_coincidencia(root.left, texto_buscado, resultado)

        # Comprueba si el nombre de la criatura contiene el texto buscado.
        if texto_buscado.lower() in root.nombre.lower():
            resultado.append(root)

        # Realiza una búsqueda recursiva en el subárbol derecho.
        buscar_criaturas_por_coincidencia(root.right, texto_buscado, resultado)


# Lista para almacenar las criaturas que coinciden con la búsqueda.
criaturas_coincidentes = []

# Realizar la búsqueda por coincidencia (por ejemplo, buscar "Cer" coincidirá con "Cerbero").
texto_buscado = "Cer"
buscar_criaturas_por_coincidencia(root, texto_buscado, criaturas_coincidentes)

# Mostrar las criaturas coincidentes.
if criaturas_coincidentes:
    print(f"Criaturas que coinciden con '{texto_buscado}':")
    for criatura in criaturas_coincidentes:
        print(
            f"Criatura: {criatura.nombre}, Derrotada por: {criatura.derrotada_por}, Capturada por: {criatura.capturada}")
else:
    print(f"No se encontraron criaturas que coincidan con '{texto_buscado}'.")

# Clase para representar un nodo del árbol.


class Nodo:
    def __init__(self, nombre, descripcion, capturada, hijos=[]):
        self.nombre = nombre
        self.descripcion = descripcion
        self.capturada = capturada
        self.hijos = hijos

# Función para encontrar un nodo en el árbol por nombre.


def encontrar_nodo_por_nombre(root, nombre):
    if root is None:
        return None

    if nombre == root.nombre:
        return root

    for hijo in root.hijos:
        nodo_encontrado = encontrar_nodo_por_nombre(hijo, nombre)
        if nodo_encontrado is not None:
            return nodo_encontrado

    return None

# Función para modificar el nodo y agregar información sobre Heracles.


def agregar_derrota_por_heracles(root, nombre):
    nodo_a_modificar = encontrar_nodo_por_nombre(root, nombre)
    if nodo_a_modificar is not None:
        # Agregar información sobre la derrota por Heracles.
        nodo_a_modificar.capturada = "Heracles"


# Ejemplo de uso para modificar el nodo de las Aves del Estínfalo.
nodo_raiz = Nodo("Criaturas Mitológicas", "Descripción de las criaturas", "Ninguna", [
    Nodo("Basilisco", "Descripción del Basilisco", "Ninguna"),
    Nodo("Sirenas", "Descripción de las Sirenas", "Ninguna"),
    Nodo("Aves del Estínfalo", "Descripción de las Aves del Estínfalo", "Ninguna")
])

# Modificar el nodo de las Aves del Estínfalo y agregar información sobre Heracles.
nombre_criatura = "Aves del Estínfalo"
agregar_derrota_por_heracles(nodo_raiz, nombre_criatura)

# Mostrar la información actualizada del árbol.


def imprimir_arbol(root, nivel=0):
    if root is not None:
        print("  " * nivel + f"- {root.nombre} ({root.capturada})")
        for hijo in root.hijos:
            imprimir_arbol(hijo, nivel + 1)


print("Árbol actualizado:")
imprimir_arbol(nodo_raiz)

# Clase para representar un nodo del árbol.


class Nodo:
    def __init__(self, nombre, descripcion, capturada, hijos=[]):
        self.nombre = nombre
        self.descripcion = descripcion
        self.capturada = capturada
        self.hijos = hijos

# Función para imprimir un listado por nivel del árbol.


def listado_por_nivel(root):
    if root is None:
        return

    # Usaremos una cola para realizar el recorrido por niveles.
    cola = [root]

    while cola:
        nodo = cola.pop(0)  # Obtenemos el primer nodo de la cola.
        print(f"{nodo.nombre} ({nodo.capturada})")

        # Agregamos los hijos de este nodo a la cola.
        cola.extend(nodo.hijos)


# Ejemplo de uso para imprimir un listado por nivel del árbol.
nodo_raiz = Nodo("Criaturas Mitológicas", "Descripción de las criaturas", "Ninguna", [
    Nodo("Basilisco", "Descripción del Basilisco", "Ninguna"),
    Nodo("Sirenas", "Descripción de las Sirenas", "Ninguna"),
    Nodo("Dragón Ladón", "Descripción de Dragón Ladón", "Heracles")
])

print("Listado por nivel del árbol:")
listado_por_nivel(nodo_raiz)

# Clase para representar un nodo del árbol.


class Nodo:
    def __init__(self, nombre, descripcion, capturada, hijos=[]):
        self.nombre = nombre
        self.descripcion = descripcion
        self.capturada = capturada
        self.hijos = hijos

# Función para buscar y mostrar las criaturas capturadas por Heracles.


def criaturas_capturadas_por_heracles(nodo):
    criaturas_capturadas = []

    if nodo.capturada == "Heracles":
        criaturas_capturadas.append(nodo.nombre)

    for hijo in nodo.hijos:
        criaturas_capturadas.extend(criaturas_capturadas_por_heracles(hijo))

    return criaturas_capturadas


# Ejemplo de uso para mostrar las criaturas capturadas por Heracles.
nodo_raiz = Nodo("Criaturas Mitológicas", "Descripción de las criaturas", "Ninguna", [
    Nodo("Basilisco", "Descripción del Basilisco", "Ninguna"),
    Nodo("Sirenas", "Descripción de las Sirenas", "Ninguna"),
    Nodo("Dragón Ladón", "Descripción de Dragón Ladón", "Heracles", [
        Nodo("Aves del Estínfalo",
             "Descripción de las Aves del Estínfalo", "Ninguna"),
        Nodo("Cerbero", "Descripción de Cerbero", "Heracles"),
        Nodo("Toro de Creta", "Descripción de Toro de Creta", "Heracles"),
        Nodo("Cierva Cerinea", "Descripción de Cierva Cerinea", "Heracles"),
        Nodo("Jabalí de Erimanto", "Descripción de Jabalí de Erimanto", "Heracles"),
    ])
])

print("Criaturas capturadas por Heracles:")
criaturas_capturadas = criaturas_capturadas_por_heracles(nodo_raiz)
for criatura in criaturas_capturadas:
    print(criatura)
