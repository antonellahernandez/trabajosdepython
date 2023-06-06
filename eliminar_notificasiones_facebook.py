class Cola:
    def eliminar_notificaciones_facebook(self):
        nueva_cola = []

        for notificacion in self.cola:
            aplicacion = notificacion["aplicacion"]

            if aplicacion != "Facebook":
                nueva_cola.append(notificacion)

        self.cola = nueva_cola


cola_notificaciones = [
    {"hora": "08:30", "aplicacion": "Instagram", "mensaje": "Nueva publicación"},
    {"hora": "09:15", "aplicacion": "Facebook",
        "mensaje": "Amigo solicitó tu amistad"},
    {"hora": "10:45", "aplicacion": "Twitter", "mensaje": "Nuevo seguidor"},
    {"hora": "11:20", "aplicacion": "Facebook",
        "mensaje": "Publicación etiquetada"},
    {"hora": "12:10", "aplicacion": "WhatsApp", "mensaje": "Nuevo mensaje"},
]


print("Cola de notificaciones antes de eliminar las de Facebook:")
for notificacion in cola_notificaciones:
    print(notificacion)


cola_objeto = Cola()
cola_objeto.cola = cola_notificaciones


cola_objeto.eliminar_notificaciones_facebook()

print("\nCola de notificaciones después de eliminar las de Facebook:")
for notificacion in cola_objeto.cola:
    print(notificacion)


def contar_notificaciones_entre_horas(notificaciones, hora_inicio, hora_fin):
    pila_temporal = []
    contador = 0

    for notificacion in notificaciones:
        hora = notificacion["hora"]

        if hora >= hora_inicio and hora <= hora_fin:
            pila_temporal.append(notificacion)
            contador += 1

    print("Notificaciones almacenadas en la pila:")
    while len(pila_temporal) > 0:
        notificacion = pila_temporal.pop()
        print(notificacion)

    return contador


class Cola:
    def mostrar_notificaciones_python_twitter(self, cola):
        for notificacion in cola:
            aplicacion = notificacion["aplicacion"]
            mensaje = notificacion["mensaje"]

            if aplicacion == "Twitter" and "Python" in mensaje:
                print(notificacion)


cola_notificaciones = [
    {"hora": "08:30", "aplicacion": "Instagram", "mensaje": "Nueva publicación"},
    {"hora": "09:15", "aplicacion": "Facebook",
        "mensaje": "Amigo solicitó tu amistad"},
    {"hora": "10:45", "aplicacion": "Twitter", "mensaje": "Nuevo seguidor"},
    {"hora": "11:20", "aplicacion": "Twitter",
        "mensaje": "Aprende Python de manera fácil"},
    {"hora": "12:10", "aplicacion": "WhatsApp", "mensaje": "Nuevo mensaje"},
]


cola_objeto = Cola()


print("Notificaciones de Twitter con la palabra 'Python':")
cola_objeto.mostrar_notificaciones_python_twitter(cola_notificaciones)


class Pila:
    def contar_notificaciones_entre_horas(self, notificaciones, hora_inicio, hora_fin):
        pila_temporal = []
        cantidad = 0

        for notificacion in notificaciones:
            hora = notificacion["hora"]

            if hora >= hora_inicio and hora <= hora_fin:
                pila_temporal.append(notificacion)
                cantidad += 1

        self.pila = pila_temporal

        return cantidad


pila_notificaciones = [
    {"hora": "08:30", "aplicacion": "Instagram", "mensaje": "Nueva publicación"},
    {"hora": "09:15", "aplicacion": "Facebook",
        "mensaje": "Amigo solicitó tu amistad"},
    {"hora": "10:45", "aplicacion": "Twitter", "mensaje": "Nuevo seguidor"},
    {"hora": "11:20", "aplicacion": "Facebook",
        "mensaje": "Publicación etiquetada"},
    {"hora": "12:10", "aplicacion": "WhatsApp", "mensaje": "Nuevo mensaje"},
]


pila_objeto = Pila()
pila_objeto.pila = pila_notificaciones


hora_inicio = "11:43"
hora_fin = "15:57"


cantidad = pila_objeto.contar_notificaciones_entre_horas(
    pila_notificaciones, hora_inicio, hora_fin)
print("Cantidad de notificaciones entre",
      hora_inicio, "y", hora_fin, ":", cantidad)


print("Notificaciones almacenadas en la pila:")
for notificacion in pila_objeto.pila:
    print(notificacion)
