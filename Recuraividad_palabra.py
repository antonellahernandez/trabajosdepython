def contar_palabra_recursiva(palabra, vector, indice=0, contador=0):

    if indice == len(vector):
        return contador

    if vector[indice] == palabra:
        contador += 1

    return contar_palabra_recursiva(palabra, vector, indice + 1, contador)


vector_palabras = ["Hola", "teclado", "Hola", "computadora", "Hola"]
palabra_buscada = "Hola"

cantidad = contar_palabra_recursiva(palabra_buscada, vector_palabras)
print(f"La palabra '{palabra_buscada}' aparece {cantidad} veces en el vector.")
