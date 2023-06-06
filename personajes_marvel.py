
class Cola:
    def __init__(self):

        self.cola_personajes = list([
            ("Tony Stark", "Iron Man", "M"),
            ("Steve Rogers", "Capitán América", "M"),
            ("Natasha Romanoff", "Black Widow", "F"),
            ("Carol Danvers", "Capitana Marvel", "F"),
            ("Scott Lang", "Ant-Man", "M"),
            ("Peter Parker", "Spider-Man", "M")
        ])

    def obtener_nombre_capitana_marvel(self):
        for personaje in self.cola_personajes:
            if personaje[1] == "Capitana Marvel":
                return personaje[0]
        return "Capitana Marvel no encontrado"

    def mostrar_personajes_femeninos(self):
        print("Personajes femeninos:")
        for personaje in self.cola_personajes:
            if personaje[2] == "F":
                print(personaje[0])

    def mostrar_personajes_masculinos(self):
        print("Personajes masculinos:")
        for personaje in self.cola_personajes:
            if personaje[2] == "M":
                print(personaje[0])

    def buscar_nombre_superheroe(self, nombre_personaje):
        for personaje in self.cola_personajes:
            if personaje[0] == nombre_personaje:
                return personaje[1]
        return None

    def mostrar_personajes_nombre_comienza_con(self, letra):
        for personaje in self.cola_personajes:
            if personaje[0].startswith(letra):
                print(
                    f"Nombre: {personaje[0]}, Superhéroe: {personaje[1]}, Género: {personaje[2]}")

    def buscar_nombre_superheroe_carol_danvers(self):
        for personaje in self.cola_personajes:
            if personaje[0] == "Carol Danvers":
                return personaje[1]
        return None


cola_objeto = Cola()

nombre_personaje_capitana_marvel = cola_objeto.obtener_nombre_capitana_marvel()
print("El nombre del personaje de Capitana Marvel es:",
      nombre_personaje_capitana_marvel)


cola_objeto.mostrar_personajes_femeninos()


cola_objeto.mostrar_personajes_masculinos()


nombre_superheroe_scott_lang = cola_objeto.buscar_nombre_superheroe(
    "Scott Lang")
if nombre_superheroe_scott_lang is not None:
    print(f"El superhéroe de Scott Lang es: {nombre_superheroe_scott_lang}")
else:
    print("No se encontró el personaje Scott Lang en la cola.")


cola_objeto.mostrar_personajes_nombre_comienza_con("S")

nombre_superheroe_carol_danvers = cola_objeto.buscar_nombre_superheroe_carol_danvers()
if nombre_superheroe_carol_danvers is not None:
    print(
        f"El nombre de superhéroe de Carol Danvers es: {nombre_superheroe_carol_danvers}")
else:
    print("Carol Danvers no se encuentra en la cola de personajes.")
