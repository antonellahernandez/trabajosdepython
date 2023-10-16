class TreeNode:
    def __init__(self, name, is_hero):
        self.name = name
        self.is_hero = is_hero
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, name, is_hero):
        self.root = self._insert_rec(self.root, name, is_hero)

    def _insert_rec(self, node, name, is_hero):
        if node is None:
            return TreeNode(name, is_hero)

        if name < node.name:
            node.left = self._insert_rec(node.left, name, is_hero)
        elif name > node.name:
            node.right = self._insert_rec(node.right, name, is_hero)

        return node


# Ejemplo de cómo usar la BinaryTree
mcu_tree = BinaryTree()
mcu_tree.insert("Iron Man", True)
mcu_tree.insert("Captain America", True)
mcu_tree.insert("Thor", True)
mcu_tree.insert("Hulk", True)
mcu_tree.insert("Black Widow", True)
mcu_tree.insert("Loki", False)
mcu_tree.insert("Thanos", False)


def list_villains_in_order(node):
    if node is None:
        return []

    villains = list_villains_in_order(node.left)

    if not node.is_hero:  # Filtrar villanos
        villains.append(node.name)

    villains += list_villains_in_order(node.right)

    return villains


villains_sorted = list_villains_in_order(mcu_tree.root)
villains_sorted.sort()  # Ordenar alfabéticamente

print("Villanos ordenados alfabéticamente:")
for villain in villains_sorted:
    print(villain)


def count_superheroes(node):
    if node is None:
        return 0

    count = count_superheroes(node.left)

    if node.is_hero:
        count += 1

    count += count_superheroes(node.right)

    return count


num_superheroes = count_superheroes(mcu_tree.root)

print(f"Número de superhéroes en el árbol: {num_superheroes}")


def find_and_rename_doctor_strange(node):
    if node is None:
        return

    # Verificar si el nombre del nodo contiene "Doctor Strange" de manera aproximada (ignorando mayúsculas y minúsculas)
    if "doctor strange" in node.name.lower():
        # Modificar el nombre
        node.name = "Doctor Strange"  # Modificación del nombre deseado

    # Recursivamente buscar en los subárboles izquierdo y derecho
    find_and_rename_doctor_strange(node.left)
    find_and_rename_doctor_strange(node.right)


# Llamar a la función para encontrar y modificar "Doctor Strange"
find_and_rename_doctor_strange(mcu_tree.root)


def superheroes_in_reverse_order(node, heroes_list):
    if node is None:
        return

    # Recorrido in-order inverso
    superheroes_in_reverse_order(node.right, heroes_list)

    if node.is_hero:
        heroes_list.append(node.name)

    superheroes_in_reverse_order(node.left, heroes_list)


# Crear una lista para almacenar los superhéroes en orden inverso
superheroes_reverse = []
superheroes_in_reverse_order(mcu_tree.root, superheroes_reverse)

# Imprimir los superhéroes en orden inverso
print("Superhéroes ordenados de manera descendente:")
for hero in reversed(superheroes_reverse):
    print(hero)

# Crear dos árboles para superhéroes y villanos
superheroes_tree = BinaryTree()
villains_tree = BinaryTree()

# Función para separar a los personajes en superhéroes y villanos


def separate_characters(node):
    if node is None:
        return

    if node.is_hero:
        superheroes_tree.insert(node.name, True)
    else:
        villains_tree.insert(node.name, False)

    separate_characters(node.left)
    separate_characters(node.right)


# Separar los personajes en superhéroes y villanos
separate_characters(mcu_tree.root)

# Función para contar los nodos en un árbol


def count_nodes(node):
    if node is None:
        return 0

    count = 1
    count += count_nodes(node.left)
    count += count_nodes(node.right)
    return count


# Determinar la cantidad de nodos en cada árbol
num_superheroes_nodes = count_nodes(superheroes_tree.root)
num_villains_nodes = count_nodes(villains_tree.root)

print(f"Número de nodos en el árbol de superhéroes: {num_superheroes_nodes}")
print(f"Número de nodos en el árbol de villanos: {num_villains_nodes}")

# Función para realizar un barrido in-order en un árbol y almacenar los elementos en una lista


def in_order_traversal(node, result_list):
    if node is None:
        return

    in_order_traversal(node.left, result_list)
    result_list.append(node.name)
    in_order_traversal(node.right, result_list)


# Realizar un barrido ordenado alfabéticamente en el árbol de superhéroes
superheroes_sorted = []
in_order_traversal(superheroes_tree.root, superheroes_sorted)

# Realizar un barrido ordenado alfabéticamente en el árbol de villanos
villains_sorted = []
in_order_traversal(villains_tree.root, villains_sorted)

# Imprimir los resultados
print("Superhéroes ordenados alfabéticamente:")
for hero in superheroes_sorted:
    print(hero)

print("\nVillanos ordenados alfabéticamente:")
for villain in villains_sorted:
    print(villain)
