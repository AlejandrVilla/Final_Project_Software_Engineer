# Practica 9: Estilos de programación

## Things
La declaracion de la clase evento que se usará como una entidad en la lógica del dominio
```
class Evento:
    def __init__(evento, detalles_, link_, id_, nombre_, fecha_, hora_inicio_, hora_fin_):
        evento.detalles = detalles_
        evento.link = link_
        evento.id = id_
        evento.nombre = nombre_
        evento.fecha = fecha_
        evento.hora_inicio = hora_inicio_
        evento.hora_fin = hora_fin_
    
    def getDetalles(evento):
        return evento.detalles
    def getLink(evento):
        return evento.link
    def getId(evento):
        return evento.id
    def getNombre(evento):
        return evento.nombre
    def getFecha(evento):
        return evento.fecha
    def getHoraInicio(evento):
        return evento.hora_inicio
    def getHoraFin(evento):
        return evento.hora_fin

    def setDetalles(evento, detalles_):
        evento.detalles = detalles_
    def setLink(evento, link_):
        if not "www" in link_:
            raise("Expected a www in ", link_)
        evento.link = link_
    def getId(evento, id_):
        evento.id = id_
    def getNombre(evento, nombre_):
        evento.nombre = nombre_
    def getFecha(evento, fecha_):
        evento.fecha = fecha_
    def getHoraInicio(evento, hora_inicio_):
        evento.hora_inicio = hora_inicio_
    def getHoraFin(evento, hora_fin_):
        evento.hora_fin = hora_fin_

```

## Declared intentions
Cuando un nuevo link se va añadir a la entidad evento, esta debe contener la "www" dentro de la cadena, sinó esta no sería válida
El archivo es 
```
def setLink(evento, link_):
        if not "www" in link_:
            raise("Expected a www in ", link_)
```

## Cook book
Users es una variable global que se usa dentro de varias funciones 
```
users = []

list_log = modelLogin.get_all_usuario()
list_user = modelUser.get_all_usuarios()

n = 1
for x, y in zip(list_log,list_user):
    users.append(User(
        id=n, contrasenia=x.get('contrasenia'),corre=x.get('correo'),
        nombre=x.get('nombre'), apellido=x.get('apellido'),
        nombres=y.get('nombres'), apellidos=y.get('apellidos'),
        correo=y.get('correo'), lista=y.get('listaEventos'),))
    n += 1


@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

```
