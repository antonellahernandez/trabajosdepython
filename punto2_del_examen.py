class Personaje:
    def __init__(self, superheroe, nombre_personaje, grupo, anio_aparicion):
        self.superheroe = superheroe
        self.nombre_personaje = nombre_personaje
        self.grupo = grupo
        self.anio_aparicion = anio_aparicion


class Lista:
    def __init__(self):
        self.__elements = []

    def insert(self, value):
        self.__elements.append(value)

    def search(self, search_value):
        for index, element in enumerate(self.__elements):
            if element.superheroe == search_value:
                return index
        return None

    def get_element_by_index(self, index):
        if 0 <= index < len(self.__elements):
            return self.__elements[index]
        return None


class Cola:
    def __init__(self):
        self.__elements = []

    def encolar(self, value):
        self.__elements.append(value)

    def desencolar(self):
        if not self.esta_vacia():
            return self.__elements.pop(0)
        return None

    def esta_vacia(self):
        return len(self.__elements) == 0

    def tamano(self):
        return len(self.__elements)


lista_personajes = Lista()


lista_personajes.insert(
    Personaje("Black Widow", "Natasha Romanoff", "", 1964))
lista_personajes.insert(
    Personaje("Captain America", "Steve Rogers", "Avengers", 1941))
lista_personajes.insert(
    Personaje("Iron Man", "Tony Stark", "Avengers", 1963))
lista_personajes.insert(
    Personaje("Hulk", "Bruce Banner", "Avengers", 1962))
lista_personajes.insert(
    Personaje("Thor", "Thor Odinson", "Avengers", 1962))
lista_personajes.insert(
    Personaje("Spider-Man", "Peter Parker", "Avengers", 1962))
lista_personajes.insert(
    Personaje("Black Panther", "T'Challa", "Avengers", 1966))
lista_personajes.insert(
    Personaje("Ant-Man", "Scott Lang", "Avengers", 1962))
lista_personajes.insert(
    Personaje("Star Lord", "Peter Quill", "Guardianes de la galaxia", 1976))
lista_personajes.insert(
    Personaje("Gamora", "", "Guardianes de la galaxia", 1975))
lista_personajes.insert(
    Personaje("Drax", "", "Guardianes de la galaxia", 1973))
lista_personajes.insert(
    Personaje("Mr. Fantastic", "Reed Richards", "Los cuatro fantásticos", 1961))
lista_personajes.insert(
    Personaje("Invisible Woman", "Sue Storm", "Los cuatro fantásticos", 1961))
lista_personajes.insert(
    Personaje("Human Torch", "Johnny Storm", "Los cuatro fantásticos", 1961))
lista_personajes.insert(
    Personaje("The Thing", "Ben Grimm", "Los cuatro fantásticos", 1961))
lista_personajes.insert(
    Personaje("Capitana Marvel", "Carol Danvers", "Avengers", 1967))
lista_personajes.insert(
    Personaje("Loki", "", "Avengers", 1962))

# a. Determinar si "Capitana Marvel" está en la lista y mostrar su nombre de personaje
capitana_marvel_index = lista_personajes.search("Capitana Marvel")

if capitana_marvel_index is not None:
    personaje = lista_personajes.get_element_by_index(capitana_marvel_index)
    print("El nombre del personaje de Capitana Marvel es:",
          personaje.nombre_personaje)
else:
    print("Capitana Marvel no está en la lista.")

# b. Almacenar los superhéroes que pertenezcan al grupo "Guardianes de la galaxia" en una cola e indicar cuántos son
cola_guardianes = Cola()

for personaje in lista_personajes._Lista__elements:
    if personaje.grupo == "Guardianes de la galaxia":
        cola_guardianes.encolar(personaje)

print("Cantidad de superhéroes en el grupo 'Guardianes de la galaxia':",
      cola_guardianes.tamano())

# c. Mostrar de manera descendente los superhéroes que pertenecen al grupo "Los cuatro fantásticos" y "Guardianes de la galaxia"
grupos = ["Los cuatro fantásticos", "Guardianes de la galaxia"]

for grupo in grupos:
    print(f"Superhéroes del grupo '{grupo}' (en orden descendente):")
    for personaje in reversed(lista_personajes._Lista__elements):
        if personaje.grupo == grupo:
            print(personaje.superheroe)
    print()

# d. Listar los superhéroes que tengan nombre de personajes cuyo año de aparición sea posterior a 1960
print("Superhéroes con nombre de personajes cuyo año de aparición es posterior a 1960:")
for personaje in lista_personajes._Lista__elements:
    if personaje.nombre_personaje != "" and personaje.anio_aparicion > 1960:
        print(personaje.superheroe)


for personaje in lista_personajes._Lista__elements:
    if personaje.superheroe == "Vlanck Widow":
        personaje.superheroe = "Black Widow"
        break

# Imprimir el nombre corregido del superhéroe "Black Widow"
for personaje in lista_personajes._Lista__elements:
    if personaje.superheroe == "Black Widow":
        print("Superhéroe corregido:", personaje.superheroe)
        break

# f. Dada una lista auxiliar con los siguientes personajes ("Black Cat", "Hulk", "Rocket Raccoon", "Loki"), complete el resto de la información y agreguelos a la lista principal en el caso de no estar cargados
lista_auxiliar = [
    Personaje("Black Cat", "", "", 1979),
    Personaje("Hulk", "", "Avengers", 1962),
    Personaje("Rocket Raccoon", "", "Guardianes de la galaxia", 1976),
    Personaje("Loki", "", "Avengers", 1962),
]

for personaje_auxiliar in lista_auxiliar:
    if lista_personajes.search(personaje_auxiliar.superheroe) is None:
        lista_personajes.insert(personaje_auxiliar)

# g. Mostrar todos los personajes que comienzan con C, P o S
print("Personajes que comienzan con C, P o S:")
for personaje in lista_personajes._Lista__elements:
    if personaje.superheroe[0] in ["C", "P", "S"]:
        print(personaje.superheroe)

# h. Cargue al menos 20 superheroes a la lista.
lista_personajes.insert(
    Personaje("Scarlet Witch", "Wanda Maximoff", "Avengers", 1964))
lista_personajes.insert(
    Personaje("Vision", "", "Avengers", 1968))
lista_personajes.insert(
    Personaje("Falcon", "Sam Wilson", "Avengers", 1969))
lista_personajes.insert(
    Personaje("War Machine", "James Rhodes", "Avengers", 1979))
lista_personajes.insert(
    Personaje("Doctor Strange", "Stephen Strange", "Avengers", 1963))
lista_personajes.insert(
    Personaje("Groot", "", "Guardianes de la galaxia", 1960))
lista_personajes.insert(
    Personaje("Rocket", "", "Guardianes de la galaxia", 1976))
lista_personajes.insert(
    Personaje("Nebula", "", "Guardianes de la galaxia", 1985))
lista_personajes.insert(
    Personaje("Mister Fantastic", "Reed Richards", "Los cuatro fantásticos", 1961))
lista_personajes.insert(
    Personaje("Invisible Woman", "Sue Storm", "Los cuatro fantásticos", 1961))
lista_personajes.insert(
    Personaje("Human Torch", "Johnny Storm", "Los cuatro fantásticos", 1961))
lista_personajes.insert(
    Personaje("The Thing", "Ben Grimm", "Los cuatro fantásticos", 1961))
lista_personajes.insert(
    Personaje("Silver Surfer", "", "", 1966))
lista_personajes.insert(
    Personaje("Wolverine", "Logan", "X-Men", 1974))
lista_personajes.insert(
    Personaje("Cyclops", "Scott Summers", "X-Men", 1963))
lista_personajes.insert(
    Personaje("Jean Grey", "Marvel Girl", "X-Men", 1963))
lista_personajes.insert(
    Personaje("Storm", "Ororo Munroe", "X-Men", 1975))
lista_personajes.insert(
    Personaje("Beast", "Henry McCoy", "X-Men", 1963))
lista_personajes.insert(
    Personaje("Rogue", "", "X-Men", 1981))

print()

# i. Mostrar todos los superhéroes de la lista
print("Lista de superhéroes:")
for personaje in lista_personajes._Lista__elements:
    print(personaje.superheroe)
# j. Mostrar la cantidad total de superhéroes en la lista
print("Cantidad total de superhéroes:", len(lista_personajes._Lista__elements))
